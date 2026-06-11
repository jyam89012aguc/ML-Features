import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _cv(s, w): return _std(s, w) / _sma(s, w).abs().replace(0, np.nan)
def _cf_fcf(ncfo, capex): return ncfo - capex.abs()
def _cf_fcf_ratio(num, den): return num / den.replace(0, np.nan)

# Concepts 1-12.5 (Features 1-75)

# C1: FCF Margin (1-6)
def f13_cash_flow_snapshot_fcf_margin_63d_base_v001_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_126d_base_v002_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_252d_base_v003_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_504d_base_v004_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_756d_base_v005_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_1260d_base_v006_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 1260).replace([np.inf, -np.inf], np.nan)

# C2: OCF Margin (7-12)
def f13_cash_flow_snapshot_ocf_margin_63d_base_v007_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_126d_base_v008_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_252d_base_v009_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_504d_base_v010_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_756d_base_v011_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_1260d_base_v012_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 1260).replace([np.inf, -np.inf], np.nan)

# C3: Cash Conversion (13-18)
def f13_cash_flow_snapshot_cash_conversion_63d_base_v013_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_126d_base_v014_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_252d_base_v015_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_504d_base_v016_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_756d_base_v017_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_1260d_base_v018_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 1260).replace([np.inf, -np.inf], np.nan)

# C4: FCF Conversion (19-24)
def f13_cash_flow_snapshot_fcf_conversion_63d_base_v019_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_126d_base_v020_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_252d_base_v021_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_504d_base_v022_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_756d_base_v023_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_1260d_base_v024_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 1260).replace([np.inf, -np.inf], np.nan)

# C5: Capex Intensity (25-30)
def f13_cash_flow_snapshot_capex_intensity_63d_base_v025_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_126d_base_v026_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_252d_base_v027_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_504d_base_v028_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_756d_base_v029_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_1260d_base_v030_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 1260).replace([np.inf, -np.inf], np.nan)

# C6: FCF per Share (31-36)
def f13_cash_flow_snapshot_fcf_per_share_63d_base_v031_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_126d_base_v032_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_252d_base_v033_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_504d_base_v034_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_756d_base_v035_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_1260d_base_v036_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 1260).replace([np.inf, -np.inf], np.nan)

# C7: OCF per Share (37-42)
def f13_cash_flow_snapshot_ocf_per_share_63d_base_v037_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_126d_base_v038_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_252d_base_v039_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_504d_base_v040_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_756d_base_v041_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_1260d_base_v042_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 1260).replace([np.inf, -np.inf], np.nan)

# C8: Revenue per Share (43-48)
def f13_cash_flow_snapshot_rev_per_share_63d_base_v043_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_126d_base_v044_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_252d_base_v045_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_504d_base_v046_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_756d_base_v047_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_1260d_base_v048_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 1260).replace([np.inf, -np.inf], np.nan)

# C9: NetInc per Share (49-54)
def f13_cash_flow_snapshot_ni_per_share_63d_base_v049_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_126d_base_v050_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_252d_base_v051_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_504d_base_v052_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_756d_base_v053_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_1260d_base_v054_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 1260).replace([np.inf, -np.inf], np.nan)

# C10: Capex per Share (55-60)
def f13_cash_flow_snapshot_capex_per_share_63d_base_v055_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_126d_base_v056_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_252d_base_v057_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_504d_base_v058_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_756d_base_v059_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_1260d_base_v060_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 1260).replace([np.inf, -np.inf], np.nan)

# C11: Capex to OCF (61-66)
def f13_cash_flow_snapshot_capex_to_ocf_63d_base_v061_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_126d_base_v062_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_252d_base_v063_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_504d_base_v064_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_756d_base_v065_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_1260d_base_v066_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 1260).replace([np.inf, -np.inf], np.nan)

# C12: FCF to OCF (67-72)
def f13_cash_flow_snapshot_fcf_to_ocf_63d_base_v067_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_126d_base_v068_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_252d_base_v069_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 252).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_504d_base_v070_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 504).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_756d_base_v071_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 756).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_1260d_base_v072_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 1260).replace([np.inf, -np.inf], np.nan)

# C13 (part): FCF to Capex (73-75)
def f13_cash_flow_snapshot_fcf_to_capex_63d_base_v073_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 63).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_126d_base_v074_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 126).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_252d_base_v075_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 252).replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['ncfo', 'capex', 'fcf', 'revenue', 'netinc', 'shareswa']}

F13_CASH_FLOW_SNAPSHOT_BASE_001_075_REGISTRY = {
    "f13_cash_flow_snapshot_fcf_margin_63d_base_v001_signal": {"inputs": ['arg_fcf', 'arg_revenue'], "func": f13_cash_flow_snapshot_fcf_margin_63d_base_v001_signal},
    "f13_cash_flow_snapshot_fcf_margin_126d_base_v002_signal": {"inputs": ['arg_fcf', 'arg_revenue'], "func": f13_cash_flow_snapshot_fcf_margin_126d_base_v002_signal},
    "f13_cash_flow_snapshot_fcf_margin_252d_base_v003_signal": {"inputs": ['arg_fcf', 'arg_revenue'], "func": f13_cash_flow_snapshot_fcf_margin_252d_base_v003_signal},
    "f13_cash_flow_snapshot_fcf_margin_504d_base_v004_signal": {"inputs": ['arg_fcf', 'arg_revenue'], "func": f13_cash_flow_snapshot_fcf_margin_504d_base_v004_signal},
    "f13_cash_flow_snapshot_fcf_margin_756d_base_v005_signal": {"inputs": ['arg_fcf', 'arg_revenue'], "func": f13_cash_flow_snapshot_fcf_margin_756d_base_v005_signal},
    "f13_cash_flow_snapshot_fcf_margin_1260d_base_v006_signal": {"inputs": ['arg_fcf', 'arg_revenue'], "func": f13_cash_flow_snapshot_fcf_margin_1260d_base_v006_signal},
    "f13_cash_flow_snapshot_ocf_margin_63d_base_v007_signal": {"inputs": ['arg_ncfo', 'arg_revenue'], "func": f13_cash_flow_snapshot_ocf_margin_63d_base_v007_signal},
    "f13_cash_flow_snapshot_ocf_margin_126d_base_v008_signal": {"inputs": ['arg_ncfo', 'arg_revenue'], "func": f13_cash_flow_snapshot_ocf_margin_126d_base_v008_signal},
    "f13_cash_flow_snapshot_ocf_margin_252d_base_v009_signal": {"inputs": ['arg_ncfo', 'arg_revenue'], "func": f13_cash_flow_snapshot_ocf_margin_252d_base_v009_signal},
    "f13_cash_flow_snapshot_ocf_margin_504d_base_v010_signal": {"inputs": ['arg_ncfo', 'arg_revenue'], "func": f13_cash_flow_snapshot_ocf_margin_504d_base_v010_signal},
    "f13_cash_flow_snapshot_ocf_margin_756d_base_v011_signal": {"inputs": ['arg_ncfo', 'arg_revenue'], "func": f13_cash_flow_snapshot_ocf_margin_756d_base_v011_signal},
    "f13_cash_flow_snapshot_ocf_margin_1260d_base_v012_signal": {"inputs": ['arg_ncfo', 'arg_revenue'], "func": f13_cash_flow_snapshot_ocf_margin_1260d_base_v012_signal},
    "f13_cash_flow_snapshot_cash_conversion_63d_base_v013_signal": {"inputs": ['arg_ncfo', 'arg_netinc'], "func": f13_cash_flow_snapshot_cash_conversion_63d_base_v013_signal},
    "f13_cash_flow_snapshot_cash_conversion_126d_base_v014_signal": {"inputs": ['arg_ncfo', 'arg_netinc'], "func": f13_cash_flow_snapshot_cash_conversion_126d_base_v014_signal},
    "f13_cash_flow_snapshot_cash_conversion_252d_base_v015_signal": {"inputs": ['arg_ncfo', 'arg_netinc'], "func": f13_cash_flow_snapshot_cash_conversion_252d_base_v015_signal},
    "f13_cash_flow_snapshot_cash_conversion_504d_base_v016_signal": {"inputs": ['arg_ncfo', 'arg_netinc'], "func": f13_cash_flow_snapshot_cash_conversion_504d_base_v016_signal},
    "f13_cash_flow_snapshot_cash_conversion_756d_base_v017_signal": {"inputs": ['arg_ncfo', 'arg_netinc'], "func": f13_cash_flow_snapshot_cash_conversion_756d_base_v017_signal},
    "f13_cash_flow_snapshot_cash_conversion_1260d_base_v018_signal": {"inputs": ['arg_ncfo', 'arg_netinc'], "func": f13_cash_flow_snapshot_cash_conversion_1260d_base_v018_signal},
    "f13_cash_flow_snapshot_fcf_conversion_63d_base_v019_signal": {"inputs": ['arg_fcf', 'arg_netinc'], "func": f13_cash_flow_snapshot_fcf_conversion_63d_base_v019_signal},
    "f13_cash_flow_snapshot_fcf_conversion_126d_base_v020_signal": {"inputs": ['arg_fcf', 'arg_netinc'], "func": f13_cash_flow_snapshot_fcf_conversion_126d_base_v020_signal},
    "f13_cash_flow_snapshot_fcf_conversion_252d_base_v021_signal": {"inputs": ['arg_fcf', 'arg_netinc'], "func": f13_cash_flow_snapshot_fcf_conversion_252d_base_v021_signal},
    "f13_cash_flow_snapshot_fcf_conversion_504d_base_v022_signal": {"inputs": ['arg_fcf', 'arg_netinc'], "func": f13_cash_flow_snapshot_fcf_conversion_504d_base_v022_signal},
    "f13_cash_flow_snapshot_fcf_conversion_756d_base_v023_signal": {"inputs": ['arg_fcf', 'arg_netinc'], "func": f13_cash_flow_snapshot_fcf_conversion_756d_base_v023_signal},
    "f13_cash_flow_snapshot_fcf_conversion_1260d_base_v024_signal": {"inputs": ['arg_fcf', 'arg_netinc'], "func": f13_cash_flow_snapshot_fcf_conversion_1260d_base_v024_signal},
    "f13_cash_flow_snapshot_capex_intensity_63d_base_v025_signal": {"inputs": ['arg_capex', 'arg_revenue'], "func": f13_cash_flow_snapshot_capex_intensity_63d_base_v025_signal},
    "f13_cash_flow_snapshot_capex_intensity_126d_base_v026_signal": {"inputs": ['arg_capex', 'arg_revenue'], "func": f13_cash_flow_snapshot_capex_intensity_126d_base_v026_signal},
    "f13_cash_flow_snapshot_capex_intensity_252d_base_v027_signal": {"inputs": ['arg_capex', 'arg_revenue'], "func": f13_cash_flow_snapshot_capex_intensity_252d_base_v027_signal},
    "f13_cash_flow_snapshot_capex_intensity_504d_base_v028_signal": {"inputs": ['arg_capex', 'arg_revenue'], "func": f13_cash_flow_snapshot_capex_intensity_504d_base_v028_signal},
    "f13_cash_flow_snapshot_capex_intensity_756d_base_v029_signal": {"inputs": ['arg_capex', 'arg_revenue'], "func": f13_cash_flow_snapshot_capex_intensity_756d_base_v029_signal},
    "f13_cash_flow_snapshot_capex_intensity_1260d_base_v030_signal": {"inputs": ['arg_capex', 'arg_revenue'], "func": f13_cash_flow_snapshot_capex_intensity_1260d_base_v030_signal},
    "f13_cash_flow_snapshot_fcf_per_share_63d_base_v031_signal": {"inputs": ['arg_fcf', 'arg_shareswa'], "func": f13_cash_flow_snapshot_fcf_per_share_63d_base_v031_signal},
    "f13_cash_flow_snapshot_fcf_per_share_126d_base_v032_signal": {"inputs": ['arg_fcf', 'arg_shareswa'], "func": f13_cash_flow_snapshot_fcf_per_share_126d_base_v032_signal},
    "f13_cash_flow_snapshot_fcf_per_share_252d_base_v033_signal": {"inputs": ['arg_fcf', 'arg_shareswa'], "func": f13_cash_flow_snapshot_fcf_per_share_252d_base_v033_signal},
    "f13_cash_flow_snapshot_fcf_per_share_504d_base_v034_signal": {"inputs": ['arg_fcf', 'arg_shareswa'], "func": f13_cash_flow_snapshot_fcf_per_share_504d_base_v034_signal},
    "f13_cash_flow_snapshot_fcf_per_share_756d_base_v035_signal": {"inputs": ['arg_fcf', 'arg_shareswa'], "func": f13_cash_flow_snapshot_fcf_per_share_756d_base_v035_signal},
    "f13_cash_flow_snapshot_fcf_per_share_1260d_base_v036_signal": {"inputs": ['arg_fcf', 'arg_shareswa'], "func": f13_cash_flow_snapshot_fcf_per_share_1260d_base_v036_signal},
    "f13_cash_flow_snapshot_ocf_per_share_63d_base_v037_signal": {"inputs": ['arg_ncfo', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ocf_per_share_63d_base_v037_signal},
    "f13_cash_flow_snapshot_ocf_per_share_126d_base_v038_signal": {"inputs": ['arg_ncfo', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ocf_per_share_126d_base_v038_signal},
    "f13_cash_flow_snapshot_ocf_per_share_252d_base_v039_signal": {"inputs": ['arg_ncfo', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ocf_per_share_252d_base_v039_signal},
    "f13_cash_flow_snapshot_ocf_per_share_504d_base_v040_signal": {"inputs": ['arg_ncfo', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ocf_per_share_504d_base_v040_signal},
    "f13_cash_flow_snapshot_ocf_per_share_756d_base_v041_signal": {"inputs": ['arg_ncfo', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ocf_per_share_756d_base_v041_signal},
    "f13_cash_flow_snapshot_ocf_per_share_1260d_base_v042_signal": {"inputs": ['arg_ncfo', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ocf_per_share_1260d_base_v042_signal},
    "f13_cash_flow_snapshot_rev_per_share_63d_base_v043_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f13_cash_flow_snapshot_rev_per_share_63d_base_v043_signal},
    "f13_cash_flow_snapshot_rev_per_share_126d_base_v044_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f13_cash_flow_snapshot_rev_per_share_126d_base_v044_signal},
    "f13_cash_flow_snapshot_rev_per_share_252d_base_v045_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f13_cash_flow_snapshot_rev_per_share_252d_base_v045_signal},
    "f13_cash_flow_snapshot_rev_per_share_504d_base_v046_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f13_cash_flow_snapshot_rev_per_share_504d_base_v046_signal},
    "f13_cash_flow_snapshot_rev_per_share_756d_base_v047_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f13_cash_flow_snapshot_rev_per_share_756d_base_v047_signal},
    "f13_cash_flow_snapshot_rev_per_share_1260d_base_v048_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f13_cash_flow_snapshot_rev_per_share_1260d_base_v048_signal},
    "f13_cash_flow_snapshot_ni_per_share_63d_base_v049_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ni_per_share_63d_base_v049_signal},
    "f13_cash_flow_snapshot_ni_per_share_126d_base_v050_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ni_per_share_126d_base_v050_signal},
    "f13_cash_flow_snapshot_ni_per_share_252d_base_v051_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ni_per_share_252d_base_v051_signal},
    "f13_cash_flow_snapshot_ni_per_share_504d_base_v052_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ni_per_share_504d_base_v052_signal},
    "f13_cash_flow_snapshot_ni_per_share_756d_base_v053_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ni_per_share_756d_base_v053_signal},
    "f13_cash_flow_snapshot_ni_per_share_1260d_base_v054_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f13_cash_flow_snapshot_ni_per_share_1260d_base_v054_signal},
    "f13_cash_flow_snapshot_capex_per_share_63d_base_v055_signal": {"inputs": ['arg_capex', 'arg_shareswa'], "func": f13_cash_flow_snapshot_capex_per_share_63d_base_v055_signal},
    "f13_cash_flow_snapshot_capex_per_share_126d_base_v056_signal": {"inputs": ['arg_capex', 'arg_shareswa'], "func": f13_cash_flow_snapshot_capex_per_share_126d_base_v056_signal},
    "f13_cash_flow_snapshot_capex_per_share_252d_base_v057_signal": {"inputs": ['arg_capex', 'arg_shareswa'], "func": f13_cash_flow_snapshot_capex_per_share_252d_base_v057_signal},
    "f13_cash_flow_snapshot_capex_per_share_504d_base_v058_signal": {"inputs": ['arg_capex', 'arg_shareswa'], "func": f13_cash_flow_snapshot_capex_per_share_504d_base_v058_signal},
    "f13_cash_flow_snapshot_capex_per_share_756d_base_v059_signal": {"inputs": ['arg_capex', 'arg_shareswa'], "func": f13_cash_flow_snapshot_capex_per_share_756d_base_v059_signal},
    "f13_cash_flow_snapshot_capex_per_share_1260d_base_v060_signal": {"inputs": ['arg_capex', 'arg_shareswa'], "func": f13_cash_flow_snapshot_capex_per_share_1260d_base_v060_signal},
    "f13_cash_flow_snapshot_capex_to_ocf_63d_base_v061_signal": {"inputs": ['arg_capex', 'arg_ncfo'], "func": f13_cash_flow_snapshot_capex_to_ocf_63d_base_v061_signal},
    "f13_cash_flow_snapshot_capex_to_ocf_126d_base_v062_signal": {"inputs": ['arg_capex', 'arg_ncfo'], "func": f13_cash_flow_snapshot_capex_to_ocf_126d_base_v062_signal},
    "f13_cash_flow_snapshot_capex_to_ocf_252d_base_v063_signal": {"inputs": ['arg_capex', 'arg_ncfo'], "func": f13_cash_flow_snapshot_capex_to_ocf_252d_base_v063_signal},
    "f13_cash_flow_snapshot_capex_to_ocf_504d_base_v064_signal": {"inputs": ['arg_capex', 'arg_ncfo'], "func": f13_cash_flow_snapshot_capex_to_ocf_504d_base_v064_signal},
    "f13_cash_flow_snapshot_capex_to_ocf_756d_base_v065_signal": {"inputs": ['arg_capex', 'arg_ncfo'], "func": f13_cash_flow_snapshot_capex_to_ocf_756d_base_v065_signal},
    "f13_cash_flow_snapshot_capex_to_ocf_1260d_base_v066_signal": {"inputs": ['arg_capex', 'arg_ncfo'], "func": f13_cash_flow_snapshot_capex_to_ocf_1260d_base_v066_signal},
    "f13_cash_flow_snapshot_fcf_to_ocf_63d_base_v067_signal": {"inputs": ['arg_fcf', 'arg_ncfo'], "func": f13_cash_flow_snapshot_fcf_to_ocf_63d_base_v067_signal},
    "f13_cash_flow_snapshot_fcf_to_ocf_126d_base_v068_signal": {"inputs": ['arg_fcf', 'arg_ncfo'], "func": f13_cash_flow_snapshot_fcf_to_ocf_126d_base_v068_signal},
    "f13_cash_flow_snapshot_fcf_to_ocf_252d_base_v069_signal": {"inputs": ['arg_fcf', 'arg_ncfo'], "func": f13_cash_flow_snapshot_fcf_to_ocf_252d_base_v069_signal},
    "f13_cash_flow_snapshot_fcf_to_ocf_504d_base_v070_signal": {"inputs": ['arg_fcf', 'arg_ncfo'], "func": f13_cash_flow_snapshot_fcf_to_ocf_504d_base_v070_signal},
    "f13_cash_flow_snapshot_fcf_to_ocf_756d_base_v071_signal": {"inputs": ['arg_fcf', 'arg_ncfo'], "func": f13_cash_flow_snapshot_fcf_to_ocf_756d_base_v071_signal},
    "f13_cash_flow_snapshot_fcf_to_ocf_1260d_base_v072_signal": {"inputs": ['arg_fcf', 'arg_ncfo'], "func": f13_cash_flow_snapshot_fcf_to_ocf_1260d_base_v072_signal},
    "f13_cash_flow_snapshot_fcf_to_capex_63d_base_v073_signal": {"inputs": ['arg_fcf', 'arg_capex'], "func": f13_cash_flow_snapshot_fcf_to_capex_63d_base_v073_signal},
    "f13_cash_flow_snapshot_fcf_to_capex_126d_base_v074_signal": {"inputs": ['arg_fcf', 'arg_capex'], "func": f13_cash_flow_snapshot_fcf_to_capex_126d_base_v074_signal},
    "f13_cash_flow_snapshot_fcf_to_capex_252d_base_v075_signal": {"inputs": ['arg_fcf', 'arg_capex'], "func": f13_cash_flow_snapshot_fcf_to_capex_252d_base_v075_signal},
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
    for n, c in F13_CASH_FLOW_SNAPSHOT_BASE_001_075_REGISTRY.items():
        r = c['func'](**{i: d[i.replace('arg_', '')] for i in c['inputs']})
        assert isinstance(r, pd.Series), f'{n} failed'
        assert len(r) > 0, f'{n} empty'
        assert r.nunique() > 2, f'{n} too few unique values'
        assert r.std() > 0, f'{n} zero std'
    print('OK')
