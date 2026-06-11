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

def f11_revenue_level_log_revenue_jerk_v001_signal(arg_revenue) -> pd.Series:
    base = _rev_log(arg_revenue)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_jerk_v002_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_mcap_jerk_v003_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = arg_revenue / arg_marketcap.replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_ev_jerk_v004_signal(arg_revenue, arg_ev) -> pd.Series:
    base = arg_revenue / arg_ev.replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_shares_jerk_v005_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = arg_revenue / arg_shareswa.replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_63d_jerk_v006_signal(arg_revenue) -> pd.Series:
    base = _sma(_rev_log(arg_revenue), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_126d_jerk_v007_signal(arg_revenue) -> pd.Series:
    base = _sma(_rev_log(arg_revenue), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_252d_jerk_v008_signal(arg_revenue) -> pd.Series:
    base = _sma(_rev_log(arg_revenue), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_504d_jerk_v009_signal(arg_revenue) -> pd.Series:
    base = _sma(_rev_log(arg_revenue), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_756d_jerk_v010_signal(arg_revenue) -> pd.Series:
    base = _sma(_rev_log(arg_revenue), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_log_rev_1260d_jerk_v011_signal(arg_revenue) -> pd.Series:
    base = _sma(_rev_log(arg_revenue), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_63d_jerk_v012_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _sma(_rev_vs_assets(arg_revenue, arg_assets), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_126d_jerk_v013_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _sma(_rev_vs_assets(arg_revenue, arg_assets), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_252d_jerk_v014_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _sma(_rev_vs_assets(arg_revenue, arg_assets), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_504d_jerk_v015_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _sma(_rev_vs_assets(arg_revenue, arg_assets), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_756d_jerk_v016_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _sma(_rev_vs_assets(arg_revenue, arg_assets), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_assets_1260d_jerk_v017_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _sma(_rev_vs_assets(arg_revenue, arg_assets), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_63d_jerk_v018_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_126d_jerk_v019_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_252d_jerk_v020_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_504d_jerk_v021_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_756d_jerk_v022_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_mcap_1260d_jerk_v023_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_63d_jerk_v024_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _sma(arg_revenue / arg_ev.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_126d_jerk_v025_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _sma(arg_revenue / arg_ev.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_252d_jerk_v026_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _sma(arg_revenue / arg_ev.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_504d_jerk_v027_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _sma(arg_revenue / arg_ev.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_756d_jerk_v028_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _sma(arg_revenue / arg_ev.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_ev_1260d_jerk_v029_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _sma(arg_revenue / arg_ev.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_63d_jerk_v030_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_126d_jerk_v031_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_252d_jerk_v032_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_504d_jerk_v033_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_756d_jerk_v034_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_sma_rev_shares_1260d_jerk_v035_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _sma(arg_revenue / arg_shareswa.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_63d_jerk_v036_signal(arg_revenue) -> pd.Series:
    base = _z(arg_revenue, 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_126d_jerk_v037_signal(arg_revenue) -> pd.Series:
    base = _z(arg_revenue, 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_252d_jerk_v038_signal(arg_revenue) -> pd.Series:
    base = _z(arg_revenue, 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_504d_jerk_v039_signal(arg_revenue) -> pd.Series:
    base = _z(arg_revenue, 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_756d_jerk_v040_signal(arg_revenue) -> pd.Series:
    base = _z(arg_revenue, 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_1260d_jerk_v041_signal(arg_revenue) -> pd.Series:
    base = _z(arg_revenue, 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_63d_jerk_v042_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _z(_rev_vs_assets(arg_revenue, arg_assets), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_126d_jerk_v043_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _z(_rev_vs_assets(arg_revenue, arg_assets), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_252d_jerk_v044_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _z(_rev_vs_assets(arg_revenue, arg_assets), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_504d_jerk_v045_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _z(_rev_vs_assets(arg_revenue, arg_assets), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_756d_jerk_v046_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _z(_rev_vs_assets(arg_revenue, arg_assets), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_assets_1260d_jerk_v047_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _z(_rev_vs_assets(arg_revenue, arg_assets), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_63d_jerk_v048_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_126d_jerk_v049_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_252d_jerk_v050_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_504d_jerk_v051_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_756d_jerk_v052_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_mcap_1260d_jerk_v053_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _z(arg_revenue / arg_marketcap.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_63d_jerk_v054_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _z(arg_revenue / arg_ev.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_126d_jerk_v055_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _z(arg_revenue / arg_ev.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_252d_jerk_v056_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _z(arg_revenue / arg_ev.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_504d_jerk_v057_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _z(arg_revenue / arg_ev.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_756d_jerk_v058_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _z(arg_revenue / arg_ev.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_ev_1260d_jerk_v059_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _z(arg_revenue / arg_ev.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_63d_jerk_v060_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _max(arg_revenue, 63).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_126d_jerk_v061_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _max(arg_revenue, 126).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_252d_jerk_v062_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _max(arg_revenue, 252).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_504d_jerk_v063_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _max(arg_revenue, 504).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_756d_jerk_v064_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _max(arg_revenue, 756).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_peak_1260d_jerk_v065_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _max(arg_revenue, 1260).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_63d_jerk_v066_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 63).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_126d_jerk_v067_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 126).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_252d_jerk_v068_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 252).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_504d_jerk_v069_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 504).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_756d_jerk_v070_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 756).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_dist_peak_1260d_jerk_v071_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _max(_rev_vs_assets(arg_revenue, arg_assets), 1260).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_63d_jerk_v072_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _min(arg_revenue, 63).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_126d_jerk_v073_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _min(arg_revenue, 126).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_252d_jerk_v074_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _min(arg_revenue, 252).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_504d_jerk_v075_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _min(arg_revenue, 504).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_756d_jerk_v076_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _min(arg_revenue, 756).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_dist_trough_1260d_jerk_v077_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _min(arg_revenue, 1260).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_63d_jerk_v078_signal(arg_revenue) -> pd.Series:
    base = _cv(arg_revenue, 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_126d_jerk_v079_signal(arg_revenue) -> pd.Series:
    base = _cv(arg_revenue, 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_252d_jerk_v080_signal(arg_revenue) -> pd.Series:
    base = _cv(arg_revenue, 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_504d_jerk_v081_signal(arg_revenue) -> pd.Series:
    base = _cv(arg_revenue, 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_756d_jerk_v082_signal(arg_revenue) -> pd.Series:
    base = _cv(arg_revenue, 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_1260d_jerk_v083_signal(arg_revenue) -> pd.Series:
    base = _cv(arg_revenue, 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_assets_63d_jerk_v084_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _cv(_rev_vs_assets(arg_revenue, arg_assets), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_assets_126d_jerk_v085_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _cv(_rev_vs_assets(arg_revenue, arg_assets), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_assets_252d_jerk_v086_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _cv(_rev_vs_assets(arg_revenue, arg_assets), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_assets_504d_jerk_v087_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _cv(_rev_vs_assets(arg_revenue, arg_assets), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_assets_756d_jerk_v088_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _cv(_rev_vs_assets(arg_revenue, arg_assets), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_cv_rev_assets_1260d_jerk_v089_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _cv(_rev_vs_assets(arg_revenue, arg_assets), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_to_sma_63d_jerk_v090_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _sma(arg_revenue, 63).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_to_sma_126d_jerk_v091_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _sma(arg_revenue, 126).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_to_sma_252d_jerk_v092_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _sma(arg_revenue, 252).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_to_sma_504d_jerk_v093_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _sma(arg_revenue, 504).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_to_sma_756d_jerk_v094_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _sma(arg_revenue, 756).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_to_sma_1260d_jerk_v095_signal(arg_revenue) -> pd.Series:
    base = arg_revenue / _sma(arg_revenue, 1260).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_to_sma_63d_jerk_v096_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _sma(_rev_vs_assets(arg_revenue, arg_assets), 63).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_to_sma_126d_jerk_v097_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _sma(_rev_vs_assets(arg_revenue, arg_assets), 126).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_to_sma_252d_jerk_v098_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _sma(_rev_vs_assets(arg_revenue, arg_assets), 252).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_to_sma_504d_jerk_v099_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _sma(_rev_vs_assets(arg_revenue, arg_assets), 504).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_to_sma_756d_jerk_v100_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _sma(_rev_vs_assets(arg_revenue, arg_assets), 756).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_assets_to_sma_1260d_jerk_v101_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rev_vs_assets(arg_revenue, arg_assets) / _sma(_rev_vs_assets(arg_revenue, arg_assets), 1260).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_mcap_to_sma_63d_jerk_v102_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = (arg_revenue / arg_marketcap.replace(0, np.nan)) / _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 63).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_mcap_to_sma_126d_jerk_v103_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = (arg_revenue / arg_marketcap.replace(0, np.nan)) / _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 126).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_mcap_to_sma_252d_jerk_v104_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = (arg_revenue / arg_marketcap.replace(0, np.nan)) / _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 252).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_mcap_to_sma_504d_jerk_v105_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = (arg_revenue / arg_marketcap.replace(0, np.nan)) / _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 504).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_mcap_to_sma_756d_jerk_v106_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = (arg_revenue / arg_marketcap.replace(0, np.nan)) / _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 756).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_mcap_to_sma_1260d_jerk_v107_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = (arg_revenue / arg_marketcap.replace(0, np.nan)) / _sma(arg_revenue / arg_marketcap.replace(0, np.nan), 1260).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_ev_to_sma_63d_jerk_v108_signal(arg_revenue, arg_ev) -> pd.Series:
    base = (arg_revenue / arg_ev.replace(0, np.nan)) / _sma(arg_revenue / arg_ev.replace(0, np.nan), 63).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_ev_to_sma_126d_jerk_v109_signal(arg_revenue, arg_ev) -> pd.Series:
    base = (arg_revenue / arg_ev.replace(0, np.nan)) / _sma(arg_revenue / arg_ev.replace(0, np.nan), 126).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_ev_to_sma_252d_jerk_v110_signal(arg_revenue, arg_ev) -> pd.Series:
    base = (arg_revenue / arg_ev.replace(0, np.nan)) / _sma(arg_revenue / arg_ev.replace(0, np.nan), 252).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_ev_to_sma_504d_jerk_v111_signal(arg_revenue, arg_ev) -> pd.Series:
    base = (arg_revenue / arg_ev.replace(0, np.nan)) / _sma(arg_revenue / arg_ev.replace(0, np.nan), 504).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_ev_to_sma_756d_jerk_v112_signal(arg_revenue, arg_ev) -> pd.Series:
    base = (arg_revenue / arg_ev.replace(0, np.nan)) / _sma(arg_revenue / arg_ev.replace(0, np.nan), 756).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_rev_ev_to_sma_1260d_jerk_v113_signal(arg_revenue, arg_ev) -> pd.Series:
    base = (arg_revenue / arg_ev.replace(0, np.nan)) / _sma(arg_revenue / arg_ev.replace(0, np.nan), 1260).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_assets_63d_jerk_v114_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _ema(_rev_vs_assets(arg_revenue, arg_assets), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_assets_126d_jerk_v115_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _ema(_rev_vs_assets(arg_revenue, arg_assets), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_assets_252d_jerk_v116_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _ema(_rev_vs_assets(arg_revenue, arg_assets), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_assets_504d_jerk_v117_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _ema(_rev_vs_assets(arg_revenue, arg_assets), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_assets_756d_jerk_v118_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _ema(_rev_vs_assets(arg_revenue, arg_assets), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_assets_1260d_jerk_v119_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _ema(_rev_vs_assets(arg_revenue, arg_assets), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_mcap_63d_jerk_v120_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _ema(arg_revenue / arg_marketcap.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_mcap_126d_jerk_v121_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _ema(arg_revenue / arg_marketcap.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_mcap_252d_jerk_v122_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _ema(arg_revenue / arg_marketcap.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_mcap_504d_jerk_v123_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _ema(arg_revenue / arg_marketcap.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_mcap_756d_jerk_v124_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _ema(arg_revenue / arg_marketcap.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_mcap_1260d_jerk_v125_signal(arg_revenue, arg_marketcap) -> pd.Series:
    base = _ema(arg_revenue / arg_marketcap.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_ev_63d_jerk_v126_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _ema(arg_revenue / arg_ev.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_ev_126d_jerk_v127_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _ema(arg_revenue / arg_ev.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_ev_252d_jerk_v128_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _ema(arg_revenue / arg_ev.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_ev_504d_jerk_v129_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _ema(arg_revenue / arg_ev.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_ev_756d_jerk_v130_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _ema(arg_revenue / arg_ev.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_ev_1260d_jerk_v131_signal(arg_revenue, arg_ev) -> pd.Series:
    base = _ema(arg_revenue / arg_ev.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_shares_63d_jerk_v132_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _ema(arg_revenue / arg_shareswa.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_shares_126d_jerk_v133_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _ema(arg_revenue / arg_shareswa.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_shares_252d_jerk_v134_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _ema(arg_revenue / arg_shareswa.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_shares_504d_jerk_v135_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _ema(arg_revenue / arg_shareswa.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_shares_756d_jerk_v136_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _ema(arg_revenue / arg_shareswa.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_ema_rev_shares_1260d_jerk_v137_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _ema(arg_revenue / arg_shareswa.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_log_rev_to_sma_63d_jerk_v138_signal(arg_revenue) -> pd.Series:
    base = _rev_log(arg_revenue) / _sma(_rev_log(arg_revenue), 63).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_log_rev_to_sma_126d_jerk_v139_signal(arg_revenue) -> pd.Series:
    base = _rev_log(arg_revenue) / _sma(_rev_log(arg_revenue), 126).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_log_rev_to_sma_252d_jerk_v140_signal(arg_revenue) -> pd.Series:
    base = _rev_log(arg_revenue) / _sma(_rev_log(arg_revenue), 252).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_log_rev_to_sma_504d_jerk_v141_signal(arg_revenue) -> pd.Series:
    base = _rev_log(arg_revenue) / _sma(_rev_log(arg_revenue), 504).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_log_rev_to_sma_756d_jerk_v142_signal(arg_revenue) -> pd.Series:
    base = _rev_log(arg_revenue) / _sma(_rev_log(arg_revenue), 756).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_log_rev_to_sma_1260d_jerk_v143_signal(arg_revenue) -> pd.Series:
    base = _rev_log(arg_revenue) / _sma(_rev_log(arg_revenue), 1260).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_shares_63d_jerk_v144_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _z(arg_revenue / arg_shareswa.replace(0, np.nan), 63)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_shares_126d_jerk_v145_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _z(arg_revenue / arg_shareswa.replace(0, np.nan), 126)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_shares_252d_jerk_v146_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _z(arg_revenue / arg_shareswa.replace(0, np.nan), 252)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_shares_504d_jerk_v147_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _z(arg_revenue / arg_shareswa.replace(0, np.nan), 504)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_shares_756d_jerk_v148_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _z(arg_revenue / arg_shareswa.replace(0, np.nan), 756)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_z_rev_shares_1260d_jerk_v149_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _z(arg_revenue / arg_shareswa.replace(0, np.nan), 1260)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_revenue_level_log_rev_to_sma_extreme_jerk_v150_signal(arg_revenue) -> pd.Series:
    base = _rev_log(arg_revenue) / _sma(_rev_log(arg_revenue), 2520).replace(0, np.nan)
    res = base.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_revenue", "arg_assets", "arg_marketcap", "arg_ev", "arg_shareswa"]}

F11_REVENUE_LEVEL_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(['f11_revenue_level_log_revenue_jerk_v001_signal', 'f11_revenue_level_rev_assets_jerk_v002_signal', 'f11_revenue_level_rev_mcap_jerk_v003_signal', 'f11_revenue_level_rev_ev_jerk_v004_signal', 'f11_revenue_level_rev_shares_jerk_v005_signal', 'f11_revenue_level_sma_log_rev_63d_jerk_v006_signal', 'f11_revenue_level_sma_log_rev_126d_jerk_v007_signal', 'f11_revenue_level_sma_log_rev_252d_jerk_v008_signal', 'f11_revenue_level_sma_log_rev_504d_jerk_v009_signal', 'f11_revenue_level_sma_log_rev_756d_jerk_v010_signal', 'f11_revenue_level_sma_log_rev_1260d_jerk_v011_signal', 'f11_revenue_level_sma_rev_assets_63d_jerk_v012_signal', 'f11_revenue_level_sma_rev_assets_126d_jerk_v013_signal', 'f11_revenue_level_sma_rev_assets_252d_jerk_v014_signal', 'f11_revenue_level_sma_rev_assets_504d_jerk_v015_signal', 'f11_revenue_level_sma_rev_assets_756d_jerk_v016_signal', 'f11_revenue_level_sma_rev_assets_1260d_jerk_v017_signal', 'f11_revenue_level_sma_rev_mcap_63d_jerk_v018_signal', 'f11_revenue_level_sma_rev_mcap_126d_jerk_v019_signal', 'f11_revenue_level_sma_rev_mcap_252d_jerk_v020_signal', 'f11_revenue_level_sma_rev_mcap_504d_jerk_v021_signal', 'f11_revenue_level_sma_rev_mcap_756d_jerk_v022_signal', 'f11_revenue_level_sma_rev_mcap_1260d_jerk_v023_signal', 'f11_revenue_level_sma_rev_ev_63d_jerk_v024_signal', 'f11_revenue_level_sma_rev_ev_126d_jerk_v025_signal', 'f11_revenue_level_sma_rev_ev_252d_jerk_v026_signal', 'f11_revenue_level_sma_rev_ev_504d_jerk_v027_signal', 'f11_revenue_level_sma_rev_ev_756d_jerk_v028_signal', 'f11_revenue_level_sma_rev_ev_1260d_jerk_v029_signal', 'f11_revenue_level_sma_rev_shares_63d_jerk_v030_signal', 'f11_revenue_level_sma_rev_shares_126d_jerk_v031_signal', 'f11_revenue_level_sma_rev_shares_252d_jerk_v032_signal', 'f11_revenue_level_sma_rev_shares_504d_jerk_v033_signal', 'f11_revenue_level_sma_rev_shares_756d_jerk_v034_signal', 'f11_revenue_level_sma_rev_shares_1260d_jerk_v035_signal', 'f11_revenue_level_z_rev_63d_jerk_v036_signal', 'f11_revenue_level_z_rev_126d_jerk_v037_signal', 'f11_revenue_level_z_rev_252d_jerk_v038_signal', 'f11_revenue_level_z_rev_504d_jerk_v039_signal', 'f11_revenue_level_z_rev_756d_jerk_v040_signal', 'f11_revenue_level_z_rev_1260d_jerk_v041_signal', 'f11_revenue_level_z_rev_assets_63d_jerk_v042_signal', 'f11_revenue_level_z_rev_assets_126d_jerk_v043_signal', 'f11_revenue_level_z_rev_assets_252d_jerk_v044_signal', 'f11_revenue_level_z_rev_assets_504d_jerk_v045_signal', 'f11_revenue_level_z_rev_assets_756d_jerk_v046_signal', 'f11_revenue_level_z_rev_assets_1260d_jerk_v047_signal', 'f11_revenue_level_z_rev_mcap_63d_jerk_v048_signal', 'f11_revenue_level_z_rev_mcap_126d_jerk_v049_signal', 'f11_revenue_level_z_rev_mcap_252d_jerk_v050_signal', 'f11_revenue_level_z_rev_mcap_504d_jerk_v051_signal', 'f11_revenue_level_z_rev_mcap_756d_jerk_v052_signal', 'f11_revenue_level_z_rev_mcap_1260d_jerk_v053_signal', 'f11_revenue_level_z_rev_ev_63d_jerk_v054_signal', 'f11_revenue_level_z_rev_ev_126d_jerk_v055_signal', 'f11_revenue_level_z_rev_ev_252d_jerk_v056_signal', 'f11_revenue_level_z_rev_ev_504d_jerk_v057_signal', 'f11_revenue_level_z_rev_ev_756d_jerk_v058_signal', 'f11_revenue_level_z_rev_ev_1260d_jerk_v059_signal', 'f11_revenue_level_rev_dist_peak_63d_jerk_v060_signal', 'f11_revenue_level_rev_dist_peak_126d_jerk_v061_signal', 'f11_revenue_level_rev_dist_peak_252d_jerk_v062_signal', 'f11_revenue_level_rev_dist_peak_504d_jerk_v063_signal', 'f11_revenue_level_rev_dist_peak_756d_jerk_v064_signal', 'f11_revenue_level_rev_dist_peak_1260d_jerk_v065_signal', 'f11_revenue_level_rev_assets_dist_peak_63d_jerk_v066_signal', 'f11_revenue_level_rev_assets_dist_peak_126d_jerk_v067_signal', 'f11_revenue_level_rev_assets_dist_peak_252d_jerk_v068_signal', 'f11_revenue_level_rev_assets_dist_peak_504d_jerk_v069_signal', 'f11_revenue_level_rev_assets_dist_peak_756d_jerk_v070_signal', 'f11_revenue_level_rev_assets_dist_peak_1260d_jerk_v071_signal', 'f11_revenue_level_rev_dist_trough_63d_jerk_v072_signal', 'f11_revenue_level_rev_dist_trough_126d_jerk_v073_signal', 'f11_revenue_level_rev_dist_trough_252d_jerk_v074_signal', 'f11_revenue_level_rev_dist_trough_504d_jerk_v075_signal', 'f11_revenue_level_rev_dist_trough_756d_jerk_v076_signal', 'f11_revenue_level_rev_dist_trough_1260d_jerk_v077_signal', 'f11_revenue_level_cv_rev_63d_jerk_v078_signal', 'f11_revenue_level_cv_rev_126d_jerk_v079_signal', 'f11_revenue_level_cv_rev_252d_jerk_v080_signal', 'f11_revenue_level_cv_rev_504d_jerk_v081_signal', 'f11_revenue_level_cv_rev_756d_jerk_v082_signal', 'f11_revenue_level_cv_rev_1260d_jerk_v083_signal', 'f11_revenue_level_cv_rev_assets_63d_jerk_v084_signal', 'f11_revenue_level_cv_rev_assets_126d_jerk_v085_signal', 'f11_revenue_level_cv_rev_assets_252d_jerk_v086_signal', 'f11_revenue_level_cv_rev_assets_504d_jerk_v087_signal', 'f11_revenue_level_cv_rev_assets_756d_jerk_v088_signal', 'f11_revenue_level_cv_rev_assets_1260d_jerk_v089_signal', 'f11_revenue_level_rev_to_sma_63d_jerk_v090_signal', 'f11_revenue_level_rev_to_sma_126d_jerk_v091_signal', 'f11_revenue_level_rev_to_sma_252d_jerk_v092_signal', 'f11_revenue_level_rev_to_sma_504d_jerk_v093_signal', 'f11_revenue_level_rev_to_sma_756d_jerk_v094_signal', 'f11_revenue_level_rev_to_sma_1260d_jerk_v095_signal', 'f11_revenue_level_rev_assets_to_sma_63d_jerk_v096_signal', 'f11_revenue_level_rev_assets_to_sma_126d_jerk_v097_signal', 'f11_revenue_level_rev_assets_to_sma_252d_jerk_v098_signal', 'f11_revenue_level_rev_assets_to_sma_504d_jerk_v099_signal', 'f11_revenue_level_rev_assets_to_sma_756d_jerk_v100_signal', 'f11_revenue_level_rev_assets_to_sma_1260d_jerk_v101_signal', 'f11_revenue_level_rev_mcap_to_sma_63d_jerk_v102_signal', 'f11_revenue_level_rev_mcap_to_sma_126d_jerk_v103_signal', 'f11_revenue_level_rev_mcap_to_sma_252d_jerk_v104_signal', 'f11_revenue_level_rev_mcap_to_sma_504d_jerk_v105_signal', 'f11_revenue_level_rev_mcap_to_sma_756d_jerk_v106_signal', 'f11_revenue_level_rev_mcap_to_sma_1260d_jerk_v107_signal', 'f11_revenue_level_rev_ev_to_sma_63d_jerk_v108_signal', 'f11_revenue_level_rev_ev_to_sma_126d_jerk_v109_signal', 'f11_revenue_level_rev_ev_to_sma_252d_jerk_v110_signal', 'f11_revenue_level_rev_ev_to_sma_504d_jerk_v111_signal', 'f11_revenue_level_rev_ev_to_sma_756d_jerk_v112_signal', 'f11_revenue_level_rev_ev_to_sma_1260d_jerk_v113_signal', 'f11_revenue_level_ema_rev_assets_63d_jerk_v114_signal', 'f11_revenue_level_ema_rev_assets_126d_jerk_v115_signal', 'f11_revenue_level_ema_rev_assets_252d_jerk_v116_signal', 'f11_revenue_level_ema_rev_assets_504d_jerk_v117_signal', 'f11_revenue_level_ema_rev_assets_756d_jerk_v118_signal', 'f11_revenue_level_ema_rev_assets_1260d_jerk_v119_signal', 'f11_revenue_level_ema_rev_mcap_63d_jerk_v120_signal', 'f11_revenue_level_ema_rev_mcap_126d_jerk_v121_signal', 'f11_revenue_level_ema_rev_mcap_252d_jerk_v122_signal', 'f11_revenue_level_ema_rev_mcap_504d_jerk_v123_signal', 'f11_revenue_level_ema_rev_mcap_756d_jerk_v124_signal', 'f11_revenue_level_ema_rev_mcap_1260d_jerk_v125_signal', 'f11_revenue_level_ema_rev_ev_63d_jerk_v126_signal', 'f11_revenue_level_ema_rev_ev_126d_jerk_v127_signal', 'f11_revenue_level_ema_rev_ev_252d_jerk_v128_signal', 'f11_revenue_level_ema_rev_ev_504d_jerk_v129_signal', 'f11_revenue_level_ema_rev_ev_756d_jerk_v130_signal', 'f11_revenue_level_ema_rev_ev_1260d_jerk_v131_signal', 'f11_revenue_level_ema_rev_shares_63d_jerk_v132_signal', 'f11_revenue_level_ema_rev_shares_126d_jerk_v133_signal', 'f11_revenue_level_ema_rev_shares_252d_jerk_v134_signal', 'f11_revenue_level_ema_rev_shares_504d_jerk_v135_signal', 'f11_revenue_level_ema_rev_shares_756d_jerk_v136_signal', 'f11_revenue_level_ema_rev_shares_1260d_jerk_v137_signal', 'f11_revenue_level_log_rev_to_sma_63d_jerk_v138_signal', 'f11_revenue_level_log_rev_to_sma_126d_jerk_v139_signal', 'f11_revenue_level_log_rev_to_sma_252d_jerk_v140_signal', 'f11_revenue_level_log_rev_to_sma_504d_jerk_v141_signal', 'f11_revenue_level_log_rev_to_sma_756d_jerk_v142_signal', 'f11_revenue_level_log_rev_to_sma_1260d_jerk_v143_signal', 'f11_revenue_level_z_rev_shares_63d_jerk_v144_signal', 'f11_revenue_level_z_rev_shares_126d_jerk_v145_signal', 'f11_revenue_level_z_rev_shares_252d_jerk_v146_signal', 'f11_revenue_level_z_rev_shares_504d_jerk_v147_signal', 'f11_revenue_level_z_rev_shares_756d_jerk_v148_signal', 'f11_revenue_level_z_rev_shares_1260d_jerk_v149_signal', 'f11_revenue_level_log_rev_to_sma_extreme_jerk_v150_signal']) if callable(globals().get(n))
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
    for n, c in F11_REVENUE_LEVEL_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
        assert r.std() > 0, f"{n} failed std: {r.std()}"
    print(f"OK")
