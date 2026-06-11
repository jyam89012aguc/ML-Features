import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _cv(s, w): return _std(s, w) / _sma(s, w).abs().replace(0, np.nan)
def _cf_fcf(ncfo, capex): return ncfo - capex.abs()
def _cf_fcf_ratio(num, den): return num / den.replace(0, np.nan)

# Jerk features (1-150)

# C1: FCF Margin (1-6)
def f13_cash_flow_snapshot_fcf_margin_63d_jerk_v001_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_126d_jerk_v002_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_252d_jerk_v003_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_504d_jerk_v004_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_756d_jerk_v005_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_margin_1260d_jerk_v006_signal(arg_fcf, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_revenue), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C2: OCF Margin (7-12)
def f13_cash_flow_snapshot_ocf_margin_63d_jerk_v007_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_126d_jerk_v008_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_252d_jerk_v009_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_504d_jerk_v010_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_756d_jerk_v011_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_margin_1260d_jerk_v012_signal(arg_ncfo, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_revenue), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C3: Cash Conversion (13-18)
def f13_cash_flow_snapshot_cash_conversion_63d_jerk_v013_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_126d_jerk_v014_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_252d_jerk_v015_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_504d_jerk_v016_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_756d_jerk_v017_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_cash_conversion_1260d_jerk_v018_signal(arg_ncfo, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_netinc), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C4: FCF Conversion (19-24)
def f13_cash_flow_snapshot_fcf_conversion_63d_jerk_v019_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_126d_jerk_v020_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_252d_jerk_v021_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_504d_jerk_v022_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_756d_jerk_v023_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_conversion_1260d_jerk_v024_signal(arg_fcf, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_netinc), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C5: Capex Intensity (25-30)
def f13_cash_flow_snapshot_capex_intensity_63d_jerk_v025_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_126d_jerk_v026_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_252d_jerk_v027_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_504d_jerk_v028_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_756d_jerk_v029_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_intensity_1260d_jerk_v030_signal(arg_capex, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_revenue), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C6: FCF per Share (31-36)
def f13_cash_flow_snapshot_fcf_per_share_63d_jerk_v031_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_126d_jerk_v032_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_252d_jerk_v033_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_504d_jerk_v034_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_756d_jerk_v035_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_per_share_1260d_jerk_v036_signal(arg_fcf, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_shareswa), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C7: OCF per Share (37-42)
def f13_cash_flow_snapshot_ocf_per_share_63d_jerk_v037_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_126d_jerk_v038_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_252d_jerk_v039_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_504d_jerk_v040_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_756d_jerk_v041_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_per_share_1260d_jerk_v042_signal(arg_ncfo, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_shareswa), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C8: Revenue per Share (43-48)
def f13_cash_flow_snapshot_rev_per_share_63d_jerk_v043_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_126d_jerk_v044_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_252d_jerk_v045_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_504d_jerk_v046_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_756d_jerk_v047_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_per_share_1260d_jerk_v048_signal(arg_revenue, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_shareswa), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C9: NetInc per Share (49-54)
def f13_cash_flow_snapshot_ni_per_share_63d_jerk_v049_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_126d_jerk_v050_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_252d_jerk_v051_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_504d_jerk_v052_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_756d_jerk_v053_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_per_share_1260d_jerk_v054_signal(arg_netinc, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_shareswa), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C10: Capex per Share (55-60)
def f13_cash_flow_snapshot_capex_per_share_63d_jerk_v055_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_126d_jerk_v056_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_252d_jerk_v057_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_504d_jerk_v058_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_756d_jerk_v059_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_per_share_1260d_jerk_v060_signal(arg_capex, arg_shareswa) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_shareswa), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C11: Capex to OCF (61-66)
def f13_cash_flow_snapshot_capex_to_ocf_63d_jerk_v061_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_126d_jerk_v062_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_252d_jerk_v063_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_504d_jerk_v064_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_756d_jerk_v065_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ocf_1260d_jerk_v066_signal(arg_capex, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_ncfo), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C12: FCF to OCF (67-72)
def f13_cash_flow_snapshot_fcf_to_ocf_63d_jerk_v067_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_126d_jerk_v068_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_252d_jerk_v069_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_504d_jerk_v070_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_756d_jerk_v071_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_ocf_1260d_jerk_v072_signal(arg_fcf, arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_ncfo), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C13: FCF to Capex (73-78)
def f13_cash_flow_snapshot_fcf_to_capex_63d_jerk_v073_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_126d_jerk_v074_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_252d_jerk_v075_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_504d_jerk_v076_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_756d_jerk_v077_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_to_capex_1260d_jerk_v078_signal(arg_fcf, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf, arg_capex.abs()), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C14: OCF to Capex (79-84)
def f13_cash_flow_snapshot_ocf_to_capex_63d_jerk_v079_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_126d_jerk_v080_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_252d_jerk_v081_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_504d_jerk_v082_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_756d_jerk_v083_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_to_capex_1260d_jerk_v084_signal(arg_ncfo, arg_capex) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo, arg_capex.abs()), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C15: OCF Z-Score (85-90)
def f13_cash_flow_snapshot_ocf_zscore_63d_jerk_v085_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_126d_jerk_v086_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_252d_jerk_v087_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_504d_jerk_v088_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_756d_jerk_v089_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_1260d_jerk_v090_signal(arg_ncfo) -> pd.Series:
    return _z(arg_ncfo, 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C16: FCF Z-Score (91-96)
def f13_cash_flow_snapshot_fcf_zscore_63d_jerk_v091_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_126d_jerk_v092_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_252d_jerk_v093_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_504d_jerk_v094_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_756d_jerk_v095_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_1260d_jerk_v096_signal(arg_fcf) -> pd.Series:
    return _z(arg_fcf, 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C17: Rev Z-Score (97-102)
def f13_cash_flow_snapshot_rev_zscore_63d_jerk_v097_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_126d_jerk_v098_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_252d_jerk_v099_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_504d_jerk_v100_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_756d_jerk_v101_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_zscore_1260d_jerk_v102_signal(arg_revenue) -> pd.Series:
    return _z(arg_revenue, 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C18: NI Z-Score (103-108)
def f13_cash_flow_snapshot_ni_zscore_63d_jerk_v103_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_126d_jerk_v104_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_252d_jerk_v105_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_504d_jerk_v106_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_756d_jerk_v107_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ni_zscore_1260d_jerk_v108_signal(arg_netinc) -> pd.Series:
    return _z(arg_netinc, 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C19: OCF CV (109-114)
def f13_cash_flow_snapshot_ocf_cv_63d_jerk_v109_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_126d_jerk_v110_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_252d_jerk_v111_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_504d_jerk_v112_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_756d_jerk_v113_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_cv_1260d_jerk_v114_signal(arg_ncfo) -> pd.Series:
    return _cv(arg_ncfo, 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C20: FCF CV (115-120)
def f13_cash_flow_snapshot_fcf_cv_63d_jerk_v115_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_126d_jerk_v116_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_252d_jerk_v117_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_504d_jerk_v118_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_756d_jerk_v119_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_cv_1260d_jerk_v120_signal(arg_fcf) -> pd.Series:
    return _cv(arg_fcf, 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C21: Net Margin (121-126)
def f13_cash_flow_snapshot_net_margin_63d_jerk_v121_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_126d_jerk_v122_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_252d_jerk_v123_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_504d_jerk_v124_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_756d_jerk_v125_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_net_margin_1260d_jerk_v126_signal(arg_netinc, arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_netinc, arg_revenue), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C22: Capex to NI (127-132)
def f13_cash_flow_snapshot_capex_to_ni_63d_jerk_v127_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_126d_jerk_v128_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_252d_jerk_v129_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_504d_jerk_v130_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_756d_jerk_v131_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_capex_to_ni_1260d_jerk_v132_signal(arg_capex, arg_netinc) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_capex, arg_netinc), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C23: FCF Z-Score Alt (133-138)
def f13_cash_flow_snapshot_fcf_zscore_alt_63d_jerk_v133_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 63), _sma(arg_fcf, 63).abs()), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_126d_jerk_v134_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 126), _sma(arg_fcf, 126).abs()), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_252d_jerk_v135_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 252), _sma(arg_fcf, 252).abs()), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_504d_jerk_v136_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 504), _sma(arg_fcf, 504).abs()), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_756d_jerk_v137_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 756), _sma(arg_fcf, 756).abs()), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_fcf_zscore_alt_1260d_jerk_v138_signal(arg_fcf) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_fcf - _sma(arg_fcf, 1260), _sma(arg_fcf, 1260).abs()), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C24: OCF Z-Score Alt (139-144)
def f13_cash_flow_snapshot_ocf_zscore_alt_63d_jerk_v139_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 63), _sma(arg_ncfo, 63).abs()), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_126d_jerk_v140_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 126), _sma(arg_ncfo, 126).abs()), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_252d_jerk_v141_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 252), _sma(arg_ncfo, 252).abs()), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_504d_jerk_v142_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 504), _sma(arg_ncfo, 504).abs()), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_756d_jerk_v143_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 756), _sma(arg_ncfo, 756).abs()), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_ocf_zscore_alt_1260d_jerk_v144_signal(arg_ncfo) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_ncfo - _sma(arg_ncfo, 1260), _sma(arg_ncfo, 1260).abs()), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

# C25: Rev Growth (145-150)
def f13_cash_flow_snapshot_rev_growth_63d_jerk_v145_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(63)), 63).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_126d_jerk_v146_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(126)), 126).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_252d_jerk_v147_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(252)), 252).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_504d_jerk_v148_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(504)), 504).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_756d_jerk_v149_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(756)), 756).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f13_cash_flow_snapshot_rev_growth_1260d_jerk_v150_signal(arg_revenue) -> pd.Series:
    return _sma(_cf_fcf_ratio(arg_revenue, arg_revenue.shift(1260)), 1260).diff(21).diff(21).replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['ncfo', 'capex', 'fcf', 'revenue', 'netinc', 'shareswa']}

F13_CASH_FLOW_SNAPSHOT_JERK_001_150_REGISTRY = {
    name: {"inputs": [p.name for p in inspect.signature(obj).parameters.values()], "func": obj}
    for name, obj in sorted(globals().items())
    if name.startswith("f13_cash_flow_snapshot_") and name.endswith("_signal") and callable(obj)
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
    for n, c in F13_CASH_FLOW_SNAPSHOT_JERK_001_150_REGISTRY.items():
        r = c['func'](**{i: d[i.replace('arg_', '')] for i in c['inputs']})
        assert isinstance(r, pd.Series), f'{n} failed'
        assert len(r) > 0, f'{n} empty'
        assert r.nunique() > 2, f'{n} too few unique values'
        assert r.std() > 0, f'{n} zero std'
    print('OK')
