import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _cv(s, w): return s.rolling(w, min_periods=min(w, 5)).std() / _sma(s, w).replace(0, np.nan)
def _rev_log(r): return np.log1p(r.clip(lower=0))
def _rev_vs_assets(r, a): return r / a.replace(0, np.nan)

def f11_revenue_level_log_revenue_base_v001_signal(arg_revenue) -> pd.Series:
    res = _rev_log(arg_revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_base_v002_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rev_vs_assets(arg_revenue, arg_assets)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_mcap_base_v003_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = arg_revenue / arg_marketcap.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_ev_base_v004_signal(arg_revenue, arg_ev) -> pd.Series:
    res = arg_revenue / arg_ev.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_shares_base_v005_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = arg_revenue / arg_shareswa.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_63d_base_v006_signal(arg_revenue) -> pd.Series:
    res = _sma(_rev_log(arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_126d_base_v007_signal(arg_revenue) -> pd.Series:
    res = _sma(_rev_log(arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_252d_base_v008_signal(arg_revenue) -> pd.Series:
    res = _sma(_rev_log(arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_504d_base_v009_signal(arg_revenue) -> pd.Series:
    res = _sma(_rev_log(arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_756d_base_v010_signal(arg_revenue) -> pd.Series:
    res = _sma(_rev_log(arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_1260d_base_v011_signal(arg_revenue) -> pd.Series:
    res = _sma(_rev_log(arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_63d_base_v012_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_rev_vs_assets(arg_revenue, arg_assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_126d_base_v013_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_rev_vs_assets(arg_revenue, arg_assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_252d_base_v014_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_rev_vs_assets(arg_revenue, arg_assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_504d_base_v015_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_rev_vs_assets(arg_revenue, arg_assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_756d_base_v016_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_rev_vs_assets(arg_revenue, arg_assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_1260d_base_v017_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_rev_vs_assets(arg_revenue, arg_assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_63d_base_v018_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_126d_base_v019_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_252d_base_v020_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_504d_base_v021_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_756d_base_v022_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_1260d_base_v023_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_63d_base_v024_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _sma(arg_revenue / arg_ev.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_126d_base_v025_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _sma(arg_revenue / arg_ev.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_252d_base_v026_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _sma(arg_revenue / arg_ev.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_504d_base_v027_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _sma(arg_revenue / arg_ev.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_756d_base_v028_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _sma(arg_revenue / arg_ev.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_1260d_base_v029_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _sma(arg_revenue / arg_ev.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_63d_base_v030_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_126d_base_v031_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_252d_base_v032_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_504d_base_v033_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_756d_base_v034_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_1260d_base_v035_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_63d_base_v036_signal(arg_revenue) -> pd.Series:
    res = _z(arg_revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_126d_base_v037_signal(arg_revenue) -> pd.Series:
    res = _z(arg_revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_252d_base_v038_signal(arg_revenue) -> pd.Series:
    res = _z(arg_revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_504d_base_v039_signal(arg_revenue) -> pd.Series:
    res = _z(arg_revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_756d_base_v040_signal(arg_revenue) -> pd.Series:
    res = _z(arg_revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_1260d_base_v041_signal(arg_revenue) -> pd.Series:
    res = _z(arg_revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_63d_base_v042_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _z(_rev_vs_assets(arg_revenue, arg_assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_126d_base_v043_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _z(_rev_vs_assets(arg_revenue, arg_assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_252d_base_v044_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _z(_rev_vs_assets(arg_revenue, arg_assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_504d_base_v045_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _z(_rev_vs_assets(arg_revenue, arg_assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_756d_base_v046_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _z(_rev_vs_assets(arg_revenue, arg_assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_1260d_base_v047_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _z(_rev_vs_assets(arg_revenue, arg_assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_63d_base_v048_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_126d_base_v049_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_252d_base_v050_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_504d_base_v051_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_756d_base_v052_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_1260d_base_v053_signal(arg_revenue, arg_marketcap) -> pd.Series:
    res = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_63d_base_v054_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _z(arg_revenue / arg_ev.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_126d_base_v055_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _z(arg_revenue / arg_ev.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_252d_base_v056_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _z(arg_revenue / arg_ev.replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_504d_base_v057_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _z(arg_revenue / arg_ev.replace(0, np.nan), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_756d_base_v058_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _z(arg_revenue / arg_ev.replace(0, np.nan), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_1260d_base_v059_signal(arg_revenue, arg_ev) -> pd.Series:
    res = _z(arg_revenue / arg_ev.replace(0, np.nan), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_63d_base_v060_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _max(arg_revenue, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_126d_base_v061_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _max(arg_revenue, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_252d_base_v062_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _max(arg_revenue, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_504d_base_v063_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _max(arg_revenue, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_756d_base_v064_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _max(arg_revenue, 756).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_1260d_base_v065_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _max(arg_revenue, 1260).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_63d_base_v066_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_126d_base_v067_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_252d_base_v068_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_504d_base_v069_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_756d_base_v070_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 756).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_1260d_base_v071_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 1260).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_63d_base_v072_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _min(arg_revenue, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_126d_base_v073_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _min(arg_revenue, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_252d_base_v074_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _min(arg_revenue, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_504d_base_v075_signal(arg_revenue) -> pd.Series:
    res = arg_revenue / _min(arg_revenue, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_revenue", "arg_assets", "arg_marketcap", "arg_ev", "arg_shareswa"]}

F11_REVENUE_LEVEL_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(['f11_revenue_level_log_revenue_base_v001_signal', 'f11_revenue_level_rev_assets_base_v002_signal', 'f11_revenue_level_rev_mcap_base_v003_signal', 'f11_revenue_level_rev_ev_base_v004_signal', 'f11_revenue_level_rev_shares_base_v005_signal', 'f11_revenue_level_sma_log_rev_63d_base_v006_signal', 'f11_revenue_level_sma_log_rev_126d_base_v007_signal', 'f11_revenue_level_sma_log_rev_252d_base_v008_signal', 'f11_revenue_level_sma_log_rev_504d_base_v009_signal', 'f11_revenue_level_sma_log_rev_756d_base_v010_signal', 'f11_revenue_level_sma_log_rev_1260d_base_v011_signal', 'f11_revenue_level_sma_rev_assets_63d_base_v012_signal', 'f11_revenue_level_sma_rev_assets_126d_base_v013_signal', 'f11_revenue_level_sma_rev_assets_252d_base_v014_signal', 'f11_revenue_level_sma_rev_assets_504d_base_v015_signal', 'f11_revenue_level_sma_rev_assets_756d_base_v016_signal', 'f11_revenue_level_sma_rev_assets_1260d_base_v017_signal', 'f11_revenue_level_sma_rev_mcap_63d_base_v018_signal', 'f11_revenue_level_sma_rev_mcap_126d_base_v019_signal', 'f11_revenue_level_sma_rev_mcap_252d_base_v020_signal', 'f11_revenue_level_sma_rev_mcap_504d_base_v021_signal', 'f11_revenue_level_sma_rev_mcap_756d_base_v022_signal', 'f11_revenue_level_sma_rev_mcap_1260d_base_v023_signal', 'f11_revenue_level_sma_rev_ev_63d_base_v024_signal', 'f11_revenue_level_sma_rev_ev_126d_base_v025_signal', 'f11_revenue_level_sma_rev_ev_252d_base_v026_signal', 'f11_revenue_level_sma_rev_ev_504d_base_v027_signal', 'f11_revenue_level_sma_rev_ev_756d_base_v028_signal', 'f11_revenue_level_sma_rev_ev_1260d_base_v029_signal', 'f11_revenue_level_sma_rev_shares_63d_base_v030_signal', 'f11_revenue_level_sma_rev_shares_126d_base_v031_signal', 'f11_revenue_level_sma_rev_shares_252d_base_v032_signal', 'f11_revenue_level_sma_rev_shares_504d_base_v033_signal', 'f11_revenue_level_sma_rev_shares_756d_base_v034_signal', 'f11_revenue_level_sma_rev_shares_1260d_base_v035_signal', 'f11_revenue_level_z_rev_63d_base_v036_signal', 'f11_revenue_level_z_rev_126d_base_v037_signal', 'f11_revenue_level_z_rev_252d_base_v038_signal', 'f11_revenue_level_z_rev_504d_base_v039_signal', 'f11_revenue_level_z_rev_756d_base_v040_signal', 'f11_revenue_level_z_rev_1260d_base_v041_signal', 'f11_revenue_level_z_rev_assets_63d_base_v042_signal', 'f11_revenue_level_z_rev_assets_126d_base_v043_signal', 'f11_revenue_level_z_rev_assets_252d_base_v044_signal', 'f11_revenue_level_z_rev_assets_504d_base_v045_signal', 'f11_revenue_level_z_rev_assets_756d_base_v046_signal', 'f11_revenue_level_z_rev_assets_1260d_base_v047_signal', 'f11_revenue_level_z_rev_mcap_63d_base_v048_signal', 'f11_revenue_level_z_rev_mcap_126d_base_v049_signal', 'f11_revenue_level_z_rev_mcap_252d_base_v050_signal', 'f11_revenue_level_z_rev_mcap_504d_base_v051_signal', 'f11_revenue_level_z_rev_mcap_756d_base_v052_signal', 'f11_revenue_level_z_rev_mcap_1260d_base_v053_signal', 'f11_revenue_level_z_rev_ev_63d_base_v054_signal', 'f11_revenue_level_z_rev_ev_126d_base_v055_signal', 'f11_revenue_level_z_rev_ev_252d_base_v056_signal', 'f11_revenue_level_z_rev_ev_504d_base_v057_signal', 'f11_revenue_level_z_rev_ev_756d_base_v058_signal', 'f11_revenue_level_z_rev_ev_1260d_base_v059_signal', 'f11_revenue_level_rev_dist_peak_63d_base_v060_signal', 'f11_revenue_level_rev_dist_peak_126d_base_v061_signal', 'f11_revenue_level_rev_dist_peak_252d_base_v062_signal', 'f11_revenue_level_rev_dist_peak_504d_base_v063_signal', 'f11_revenue_level_rev_dist_peak_756d_base_v064_signal', 'f11_revenue_level_rev_dist_peak_1260d_base_v065_signal', 'f11_revenue_level_rev_assets_dist_peak_63d_base_v066_signal', 'f11_revenue_level_rev_assets_dist_peak_126d_base_v067_signal', 'f11_revenue_level_rev_assets_dist_peak_252d_base_v068_signal', 'f11_revenue_level_rev_assets_dist_peak_504d_base_v069_signal', 'f11_revenue_level_rev_assets_dist_peak_756d_base_v070_signal', 'f11_revenue_level_rev_assets_dist_peak_1260d_base_v071_signal', 'f11_revenue_level_rev_dist_trough_63d_base_v072_signal', 'f11_revenue_level_rev_dist_trough_126d_base_v073_signal', 'f11_revenue_level_rev_dist_trough_252d_base_v074_signal', 'f11_revenue_level_rev_dist_trough_504d_base_v075_signal']) if callable(globals().get(n))
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1500
    np.random.seed(42)
    # Simulate fundamental data with step functions
    steps = 10
    step_size = sz // steps
    base_rev = np.repeat(np.random.lognormal(10, 1, steps), step_size)
    if len(base_rev) < sz:
        base_rev = np.concatenate([base_rev, [base_rev[-1]] * (sz - len(base_rev))])
    
    d = pd.DataFrame({
        "arg_revenue": pd.Series(base_rev * (1 + np.random.normal(0, 0.01, sz))),
        "arg_assets": pd.Series(base_rev * np.random.uniform(0.5, 2.0, sz)),
        "arg_marketcap": pd.Series(base_rev * np.random.uniform(5, 20, sz)),
        "arg_ev": pd.Series(base_rev * np.random.uniform(6, 25, sz)),
        "arg_shareswa": pd.Series(np.ones(sz) * 1e6),
        "ticker": ["T"]*sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in F11_REVENUE_LEVEL_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
        assert r.std() > 0, f"{n} failed std: {r.std()}"
    print(f"OK")
