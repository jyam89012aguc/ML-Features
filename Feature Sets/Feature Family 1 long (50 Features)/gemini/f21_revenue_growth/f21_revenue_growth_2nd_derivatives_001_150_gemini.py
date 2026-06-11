import pandas as pd
import numpy as np

def _rg_growth(s, w): return s.pct_change(w)
def _rg_zscore(s, w): return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)
def _rg_sma(s, w): return s.rolling(w, min_periods=1).mean()
def _rg_vol(s, w): return s.rolling(w, min_periods=1).std()

# Helper for slope
def _slope(s, w=63): return s.diff(w)

def f21_revenue_growth_revenue_growth_63d_slope_v001_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_126d_slope_v002_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_252d_slope_v003_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_504d_slope_v004_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_756d_slope_v005_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_revenue_growth_1260d_slope_v006_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_63d_slope_v007_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_126d_slope_v008_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_252d_slope_v009_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_504d_slope_v010_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_756d_slope_v011_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_1260d_slope_v012_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_63d_slope_v013_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_126d_slope_v014_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_252d_slope_v015_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_504d_slope_v016_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_756d_slope_v017_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_1260d_slope_v018_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_63d_slope_v019_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_126d_slope_v020_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_252d_slope_v021_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_504d_slope_v022_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_756d_slope_v023_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_1260d_slope_v024_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_63d_slope_v025_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_126d_slope_v026_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_252d_slope_v027_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_504d_slope_v028_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_756d_slope_v029_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_1260d_slope_v030_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_63d_slope_v031_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_126d_slope_v032_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_252d_slope_v033_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_504d_slope_v034_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_756d_slope_v035_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_roa_growth_1260d_slope_v036_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_assets.replace(0, np.nan), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_63d_slope_v037_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_126d_slope_v038_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_252d_slope_v039_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_504d_slope_v040_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_756d_slope_v041_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_net_margin_growth_1260d_slope_v042_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _rg_growth(arg_netinc / arg_revenue.replace(0, np.nan), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_63d_slope_v043_signal(arg_revenue) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_126d_slope_v044_signal(arg_revenue) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_252d_slope_v045_signal(arg_revenue) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_504d_slope_v046_signal(arg_revenue) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_756d_slope_v047_signal(arg_revenue) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_growth_1260d_slope_v048_signal(arg_revenue) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_63d_slope_v049_signal(arg_assets) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_assets, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_126d_slope_v050_signal(arg_assets) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_assets, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_252d_slope_v051_signal(arg_assets) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_assets, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_504d_slope_v052_signal(arg_assets) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_assets, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_756d_slope_v053_signal(arg_assets) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_assets, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_assets_growth_1260d_slope_v054_signal(arg_assets) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_assets, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_63d_slope_v055_signal(arg_netinc) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_netinc, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_126d_slope_v056_signal(arg_netinc) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_netinc, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_252d_slope_v057_signal(arg_netinc) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_netinc, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_504d_slope_v058_signal(arg_netinc) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_netinc, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_756d_slope_v059_signal(arg_netinc) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_netinc, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_netinc_growth_1260d_slope_v060_signal(arg_netinc) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_netinc, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_63d_slope_v061_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_126d_slope_v062_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_252d_slope_v063_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_504d_slope_v064_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_756d_slope_v065_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_zscore_rev_shares_growth_1260d_slope_v066_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_zscore(_rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_63d_slope_v067_signal(arg_revenue) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_revenue, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_126d_slope_v068_signal(arg_revenue) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_revenue, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_252d_slope_v069_signal(arg_revenue) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_revenue, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_504d_slope_v070_signal(arg_revenue) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_revenue, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_756d_slope_v071_signal(arg_revenue) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_revenue, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_rev_growth_1260d_slope_v072_signal(arg_revenue) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_revenue, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_63d_slope_v073_signal(arg_assets) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_assets, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_126d_slope_v074_signal(arg_assets) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_assets, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_252d_slope_v075_signal(arg_assets) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_assets, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_504d_slope_v076_signal(arg_assets) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_assets, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_756d_slope_v077_signal(arg_assets) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_assets, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_1260d_slope_v078_signal(arg_assets) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_assets, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_63d_slope_v079_signal(arg_netinc) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_netinc, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_126d_slope_v080_signal(arg_netinc) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_netinc, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_252d_slope_v081_signal(arg_netinc) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_netinc, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_504d_slope_v082_signal(arg_netinc) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_netinc, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_756d_slope_v083_signal(arg_netinc) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_netinc, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_1260d_slope_v084_signal(arg_netinc) -> pd.Series:
    base = _rg_sma(_rg_growth(arg_netinc, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_63d_slope_v085_signal(arg_revenue) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_revenue, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_126d_slope_v086_signal(arg_revenue) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_revenue, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_252d_slope_v087_signal(arg_revenue) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_revenue, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_504d_slope_v088_signal(arg_revenue) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_revenue, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_756d_slope_v089_signal(arg_revenue) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_revenue, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_1260d_slope_v090_signal(arg_revenue) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_revenue, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_63d_slope_v091_signal(arg_assets) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_assets, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_126d_slope_v092_signal(arg_assets) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_assets, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_252d_slope_v093_signal(arg_assets) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_assets, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_504d_slope_v094_signal(arg_assets) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_assets, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_756d_slope_v095_signal(arg_assets) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_assets, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_1260d_slope_v096_signal(arg_assets) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_assets, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_63d_slope_v097_signal(arg_netinc) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_netinc, 63), 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_126d_slope_v098_signal(arg_netinc) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_netinc, 126), 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_252d_slope_v099_signal(arg_netinc) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_netinc, 252), 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_504d_slope_v100_signal(arg_netinc) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_netinc, 504), 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_756d_slope_v101_signal(arg_netinc) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_netinc, 756), 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_1260d_slope_v102_signal(arg_netinc) -> pd.Series:
    base = _rg_vol(_rg_growth(arg_netinc, 1260), 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_63d_slope_v103_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue, 63) - _rg_growth(arg_assets, 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_126d_slope_v104_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue, 126) - _rg_growth(arg_assets, 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_252d_slope_v105_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue, 252) - _rg_growth(arg_assets, 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_504d_slope_v106_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue, 504) - _rg_growth(arg_assets, 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_756d_slope_v107_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue, 756) - _rg_growth(arg_assets, 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_1260d_slope_v108_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue, 1260) - _rg_growth(arg_assets, 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_63d_slope_v109_signal(arg_revenue, arg_netinc) -> pd.Series:
    base = _rg_growth(arg_revenue, 63) - _rg_growth(arg_netinc, 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_126d_slope_v110_signal(arg_revenue, arg_netinc) -> pd.Series:
    base = _rg_growth(arg_revenue, 126) - _rg_growth(arg_netinc, 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_252d_slope_v111_signal(arg_revenue, arg_netinc) -> pd.Series:
    base = _rg_growth(arg_revenue, 252) - _rg_growth(arg_netinc, 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_504d_slope_v112_signal(arg_revenue, arg_netinc) -> pd.Series:
    base = _rg_growth(arg_revenue, 504) - _rg_growth(arg_netinc, 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_756d_slope_v113_signal(arg_revenue, arg_netinc) -> pd.Series:
    base = _rg_growth(arg_revenue, 756) - _rg_growth(arg_netinc, 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_1260d_slope_v114_signal(arg_revenue, arg_netinc) -> pd.Series:
    base = _rg_growth(arg_revenue, 1260) - _rg_growth(arg_netinc, 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_63d_slope_v115_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc, 63) - _rg_growth(arg_assets, 63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_126d_slope_v116_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc, 126) - _rg_growth(arg_assets, 126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_252d_slope_v117_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc, 252) - _rg_growth(arg_assets, 252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_504d_slope_v118_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc, 504) - _rg_growth(arg_assets, 504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_756d_slope_v119_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc, 756) - _rg_growth(arg_assets, 756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_1260d_slope_v120_signal(arg_netinc, arg_assets) -> pd.Series:
    base = _rg_growth(arg_netinc, 1260) - _rg_growth(arg_assets, 1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_63d_slope_v121_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 63).diff(63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_126d_slope_v122_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 126).diff(126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_252d_slope_v123_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 252).diff(252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_504d_slope_v124_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 504).diff(504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_756d_slope_v125_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 756).diff(756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_1260d_slope_v126_signal(arg_revenue) -> pd.Series:
    base = _rg_growth(arg_revenue, 1260).diff(1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_63d_slope_v127_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 63).diff(63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_126d_slope_v128_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 126).diff(126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_252d_slope_v129_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 252).diff(252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_504d_slope_v130_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 504).diff(504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_756d_slope_v131_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 756).diff(756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_1260d_slope_v132_signal(arg_assets) -> pd.Series:
    base = _rg_growth(arg_assets, 1260).diff(1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_63d_slope_v133_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 63).diff(63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_126d_slope_v134_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 126).diff(126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_252d_slope_v135_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 252).diff(252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_504d_slope_v136_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 504).diff(504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_756d_slope_v137_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 756).diff(756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_1260d_slope_v138_signal(arg_netinc) -> pd.Series:
    base = _rg_growth(arg_netinc, 1260).diff(1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_63d_slope_v139_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 63).diff(63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_126d_slope_v140_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 126).diff(126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_252d_slope_v141_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 252).diff(252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_504d_slope_v142_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 504).diff(504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_756d_slope_v143_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 756).diff(756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_1260d_slope_v144_signal(arg_revenue, arg_shareswa) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 1260).diff(1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_63d_slope_v145_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 63).diff(63)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_126d_slope_v146_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 126).diff(126)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_252d_slope_v147_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 252).diff(252)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_504d_slope_v148_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 504).diff(504)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_756d_slope_v149_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 756).diff(756)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_1260d_slope_v150_signal(arg_revenue, arg_assets) -> pd.Series:
    base = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 1260).diff(1260)
    res = _slope(base)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_revenue", "arg_assets", "arg_netinc", "arg_shareswa"]}

F21_REVENUE_GROWTH_SLOPE_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted([f for f in globals() if f.startswith('f21_revenue_growth_') and f.endswith('_signal')])
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 5000
    np.random.seed(42)
    steps = 20
    step_size = sz // steps
    base_rev = np.repeat(np.random.lognormal(10, 1, steps), step_size)
    if len(base_rev) < sz:
        base_rev = np.concatenate([base_rev, [base_rev[-1]] * (sz - len(base_rev))])
    
    d = pd.DataFrame({
        "arg_revenue": pd.Series(base_rev * (1 + np.random.normal(0, 0.05, sz))),
        "arg_assets": pd.Series(base_rev * np.random.uniform(0.5, 2.0, sz)),
        "arg_netinc": pd.Series(base_rev * np.random.uniform(-0.1, 0.2, sz)),
        "arg_shareswa": pd.Series(np.ones(sz) * 1e6),
        "ticker": ["T"]*sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in F21_REVENUE_GROWTH_SLOPE_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
        assert r.std() > 0, f"{n} failed std: {r.std()}"
    print(f"OK")
