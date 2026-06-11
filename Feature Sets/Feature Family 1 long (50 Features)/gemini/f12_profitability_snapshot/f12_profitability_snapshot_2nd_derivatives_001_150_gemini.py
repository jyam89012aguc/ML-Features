import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).std().replace(0, np.nan)
def _prof_margin(num, den): return num / den.replace(0, np.nan)
def _prof_roe(ni, eq): return ni / eq.replace(0, np.nan)

def f12_profitability_snapshot_gross_margin_63d_slope_v001_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_126d_slope_v002_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_252d_slope_v003_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_504d_slope_v004_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_756d_slope_v005_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_1260d_slope_v006_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_63d_slope_v007_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_126d_slope_v008_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_252d_slope_v009_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_504d_slope_v010_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_756d_slope_v011_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_1260d_slope_v012_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_63d_slope_v013_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_126d_slope_v014_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_252d_slope_v015_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_504d_slope_v016_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_756d_slope_v017_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_1260d_slope_v018_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_63d_slope_v019_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_126d_slope_v020_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_252d_slope_v021_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_504d_slope_v022_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_756d_slope_v023_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_1260d_slope_v024_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_63d_slope_v025_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_126d_slope_v026_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_252d_slope_v027_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_504d_slope_v028_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_756d_slope_v029_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_1260d_slope_v030_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_63d_slope_v031_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_126d_slope_v032_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_252d_slope_v033_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_504d_slope_v034_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_756d_slope_v035_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_1260d_slope_v036_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_63d_slope_v037_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_126d_slope_v038_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_252d_slope_v039_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_504d_slope_v040_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_756d_slope_v041_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_1260d_slope_v042_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_63d_slope_v043_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_126d_slope_v044_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_252d_slope_v045_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_504d_slope_v046_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_756d_slope_v047_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_1260d_slope_v048_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_63d_slope_v049_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_126d_slope_v050_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_252d_slope_v051_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_504d_slope_v052_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_756d_slope_v053_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_1260d_slope_v054_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_63d_slope_v055_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_126d_slope_v056_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_252d_slope_v057_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_504d_slope_v058_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_756d_slope_v059_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_1260d_slope_v060_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_63d_slope_v061_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_126d_slope_v062_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_252d_slope_v063_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_504d_slope_v064_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_756d_slope_v065_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_1260d_slope_v066_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_63d_slope_v067_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_126d_slope_v068_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_252d_slope_v069_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_504d_slope_v070_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_756d_slope_v071_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_1260d_slope_v072_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_63d_slope_v073_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_126d_slope_v074_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_252d_slope_v075_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_504d_slope_v076_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_756d_slope_v077_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_1260d_slope_v078_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_63d_slope_v079_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_126d_slope_v080_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_252d_slope_v081_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_504d_slope_v082_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_756d_slope_v083_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roe_1260d_slope_v084_signal(arg_ebitda, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_ebitda, arg_equity), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_63d_slope_v085_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_126d_slope_v086_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_252d_slope_v087_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_504d_slope_v088_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_756d_slope_v089_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roe_1260d_slope_v090_signal(arg_gp, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_gp, arg_equity), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_63d_slope_v091_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_126d_slope_v092_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_252d_slope_v093_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_504d_slope_v094_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_756d_slope_v095_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_gp_1260d_slope_v096_signal(arg_gp, arg_netinc) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_gp), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_63d_slope_v097_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_126d_slope_v098_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_252d_slope_v099_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_504d_slope_v100_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_756d_slope_v101_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ni_to_ebitda_1260d_slope_v102_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_ebitda), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_63d_slope_v103_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_126d_slope_v104_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_252d_slope_v105_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_504d_slope_v106_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_756d_slope_v107_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_to_gp_1260d_slope_v108_signal(arg_gp, arg_ebitda) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_gp), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_63d_slope_v109_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_126d_slope_v110_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_252d_slope_v111_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_504d_slope_v112_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_756d_slope_v113_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_cogs_to_rev_1260d_slope_v114_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_revenue - arg_gp), arg_revenue), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_63d_slope_v115_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_126d_slope_v116_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_252d_slope_v117_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_504d_slope_v118_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_756d_slope_v119_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_opex_to_rev_1260d_slope_v120_signal(arg_gp, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_gp - arg_ebitda), arg_revenue), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_63d_slope_v121_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_126d_slope_v122_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_252d_slope_v123_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_504d_slope_v124_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_756d_slope_v125_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_tax_int_to_rev_1260d_slope_v126_signal(arg_netinc, arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin((arg_ebitda - arg_netinc), arg_revenue), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_63d_slope_v127_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_126d_slope_v128_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_252d_slope_v129_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_504d_slope_v130_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_756d_slope_v131_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_to_assets_1260d_slope_v132_signal(arg_equity, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_equity, arg_assets), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_63d_slope_v133_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_126d_slope_v134_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_252d_slope_v135_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_504d_slope_v136_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_756d_slope_v137_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_assets_1260d_slope_v138_signal(arg_assets, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_assets), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_63d_slope_v139_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_126d_slope_v140_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_252d_slope_v141_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_504d_slope_v142_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_756d_slope_v143_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_shares_to_rev_1260d_slope_v144_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_shareswa, arg_revenue), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_63d_slope_v145_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 63).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_126d_slope_v146_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 126).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_252d_slope_v147_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 252).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_504d_slope_v148_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 504).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_756d_slope_v149_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 756).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_to_cogs_1260d_slope_v150_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, (arg_revenue - arg_gp)), 1260).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['gp', 'netinc', 'ebitda', 'revenue', 'equity', 'assets', 'shareswa']}

F12_PROFITABILITY_SNAPSHOT_SLOPE_001_150_REGISTRY = {
    "f12_profitability_snapshot_gross_margin_63d_slope_v001_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_63d_slope_v001_signal},
    "f12_profitability_snapshot_gross_margin_126d_slope_v002_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_126d_slope_v002_signal},
    "f12_profitability_snapshot_gross_margin_252d_slope_v003_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_252d_slope_v003_signal},
    "f12_profitability_snapshot_gross_margin_504d_slope_v004_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_504d_slope_v004_signal},
    "f12_profitability_snapshot_gross_margin_756d_slope_v005_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_756d_slope_v005_signal},
    "f12_profitability_snapshot_gross_margin_1260d_slope_v006_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_1260d_slope_v006_signal},
    "f12_profitability_snapshot_ebitda_margin_63d_slope_v007_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_63d_slope_v007_signal},
    "f12_profitability_snapshot_ebitda_margin_126d_slope_v008_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_126d_slope_v008_signal},
    "f12_profitability_snapshot_ebitda_margin_252d_slope_v009_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_252d_slope_v009_signal},
    "f12_profitability_snapshot_ebitda_margin_504d_slope_v010_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_504d_slope_v010_signal},
    "f12_profitability_snapshot_ebitda_margin_756d_slope_v011_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_756d_slope_v011_signal},
    "f12_profitability_snapshot_ebitda_margin_1260d_slope_v012_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_1260d_slope_v012_signal},
    "f12_profitability_snapshot_net_margin_63d_slope_v013_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_63d_slope_v013_signal},
    "f12_profitability_snapshot_net_margin_126d_slope_v014_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_126d_slope_v014_signal},
    "f12_profitability_snapshot_net_margin_252d_slope_v015_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_252d_slope_v015_signal},
    "f12_profitability_snapshot_net_margin_504d_slope_v016_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_504d_slope_v016_signal},
    "f12_profitability_snapshot_net_margin_756d_slope_v017_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_756d_slope_v017_signal},
    "f12_profitability_snapshot_net_margin_1260d_slope_v018_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_1260d_slope_v018_signal},
    "f12_profitability_snapshot_roe_63d_slope_v019_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_63d_slope_v019_signal},
    "f12_profitability_snapshot_roe_126d_slope_v020_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_126d_slope_v020_signal},
    "f12_profitability_snapshot_roe_252d_slope_v021_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_252d_slope_v021_signal},
    "f12_profitability_snapshot_roe_504d_slope_v022_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_504d_slope_v022_signal},
    "f12_profitability_snapshot_roe_756d_slope_v023_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_756d_slope_v023_signal},
    "f12_profitability_snapshot_roe_1260d_slope_v024_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_1260d_slope_v024_signal},
    "f12_profitability_snapshot_roa_63d_slope_v025_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_63d_slope_v025_signal},
    "f12_profitability_snapshot_roa_126d_slope_v026_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_126d_slope_v026_signal},
    "f12_profitability_snapshot_roa_252d_slope_v027_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_252d_slope_v027_signal},
    "f12_profitability_snapshot_roa_504d_slope_v028_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_504d_slope_v028_signal},
    "f12_profitability_snapshot_roa_756d_slope_v029_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_756d_slope_v029_signal},
    "f12_profitability_snapshot_roa_1260d_slope_v030_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_1260d_slope_v030_signal},
    "f12_profitability_snapshot_eps_proxy_63d_slope_v031_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_63d_slope_v031_signal},
    "f12_profitability_snapshot_eps_proxy_126d_slope_v032_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_126d_slope_v032_signal},
    "f12_profitability_snapshot_eps_proxy_252d_slope_v033_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_252d_slope_v033_signal},
    "f12_profitability_snapshot_eps_proxy_504d_slope_v034_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_504d_slope_v034_signal},
    "f12_profitability_snapshot_eps_proxy_756d_slope_v035_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_756d_slope_v035_signal},
    "f12_profitability_snapshot_eps_proxy_1260d_slope_v036_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_1260d_slope_v036_signal},
    "f12_profitability_snapshot_gp_per_share_63d_slope_v037_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_63d_slope_v037_signal},
    "f12_profitability_snapshot_gp_per_share_126d_slope_v038_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_126d_slope_v038_signal},
    "f12_profitability_snapshot_gp_per_share_252d_slope_v039_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_252d_slope_v039_signal},
    "f12_profitability_snapshot_gp_per_share_504d_slope_v040_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_504d_slope_v040_signal},
    "f12_profitability_snapshot_gp_per_share_756d_slope_v041_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_756d_slope_v041_signal},
    "f12_profitability_snapshot_gp_per_share_1260d_slope_v042_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_1260d_slope_v042_signal},
    "f12_profitability_snapshot_ebitda_per_share_63d_slope_v043_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_63d_slope_v043_signal},
    "f12_profitability_snapshot_ebitda_per_share_126d_slope_v044_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_126d_slope_v044_signal},
    "f12_profitability_snapshot_ebitda_per_share_252d_slope_v045_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_252d_slope_v045_signal},
    "f12_profitability_snapshot_ebitda_per_share_504d_slope_v046_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_504d_slope_v046_signal},
    "f12_profitability_snapshot_ebitda_per_share_756d_slope_v047_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_756d_slope_v047_signal},
    "f12_profitability_snapshot_ebitda_per_share_1260d_slope_v048_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_1260d_slope_v048_signal},
    "f12_profitability_snapshot_sales_per_share_63d_slope_v049_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_63d_slope_v049_signal},
    "f12_profitability_snapshot_sales_per_share_126d_slope_v050_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_126d_slope_v050_signal},
    "f12_profitability_snapshot_sales_per_share_252d_slope_v051_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_252d_slope_v051_signal},
    "f12_profitability_snapshot_sales_per_share_504d_slope_v052_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_504d_slope_v052_signal},
    "f12_profitability_snapshot_sales_per_share_756d_slope_v053_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_756d_slope_v053_signal},
    "f12_profitability_snapshot_sales_per_share_1260d_slope_v054_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_1260d_slope_v054_signal},
    "f12_profitability_snapshot_asset_turnover_63d_slope_v055_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_63d_slope_v055_signal},
    "f12_profitability_snapshot_asset_turnover_126d_slope_v056_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_126d_slope_v056_signal},
    "f12_profitability_snapshot_asset_turnover_252d_slope_v057_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_252d_slope_v057_signal},
    "f12_profitability_snapshot_asset_turnover_504d_slope_v058_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_504d_slope_v058_signal},
    "f12_profitability_snapshot_asset_turnover_756d_slope_v059_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_756d_slope_v059_signal},
    "f12_profitability_snapshot_asset_turnover_1260d_slope_v060_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_1260d_slope_v060_signal},
    "f12_profitability_snapshot_equity_turnover_63d_slope_v061_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_63d_slope_v061_signal},
    "f12_profitability_snapshot_equity_turnover_126d_slope_v062_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_126d_slope_v062_signal},
    "f12_profitability_snapshot_equity_turnover_252d_slope_v063_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_252d_slope_v063_signal},
    "f12_profitability_snapshot_equity_turnover_504d_slope_v064_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_504d_slope_v064_signal},
    "f12_profitability_snapshot_equity_turnover_756d_slope_v065_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_756d_slope_v065_signal},
    "f12_profitability_snapshot_equity_turnover_1260d_slope_v066_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_1260d_slope_v066_signal},
    "f12_profitability_snapshot_ebitda_roa_63d_slope_v067_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_63d_slope_v067_signal},
    "f12_profitability_snapshot_ebitda_roa_126d_slope_v068_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_126d_slope_v068_signal},
    "f12_profitability_snapshot_ebitda_roa_252d_slope_v069_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_252d_slope_v069_signal},
    "f12_profitability_snapshot_ebitda_roa_504d_slope_v070_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_504d_slope_v070_signal},
    "f12_profitability_snapshot_ebitda_roa_756d_slope_v071_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_756d_slope_v071_signal},
    "f12_profitability_snapshot_ebitda_roa_1260d_slope_v072_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_1260d_slope_v072_signal},
    "f12_profitability_snapshot_gp_roa_63d_slope_v073_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_63d_slope_v073_signal},
    "f12_profitability_snapshot_gp_roa_126d_slope_v074_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_126d_slope_v074_signal},
    "f12_profitability_snapshot_gp_roa_252d_slope_v075_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_252d_slope_v075_signal},
    "f12_profitability_snapshot_gp_roa_504d_slope_v076_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_504d_slope_v076_signal},
    "f12_profitability_snapshot_gp_roa_756d_slope_v077_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_756d_slope_v077_signal},
    "f12_profitability_snapshot_gp_roa_1260d_slope_v078_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_1260d_slope_v078_signal},
    "f12_profitability_snapshot_ebitda_roe_63d_slope_v079_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_63d_slope_v079_signal},
    "f12_profitability_snapshot_ebitda_roe_126d_slope_v080_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_126d_slope_v080_signal},
    "f12_profitability_snapshot_ebitda_roe_252d_slope_v081_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_252d_slope_v081_signal},
    "f12_profitability_snapshot_ebitda_roe_504d_slope_v082_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_504d_slope_v082_signal},
    "f12_profitability_snapshot_ebitda_roe_756d_slope_v083_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_756d_slope_v083_signal},
    "f12_profitability_snapshot_ebitda_roe_1260d_slope_v084_signal": {"inputs": ['arg_ebitda', 'arg_equity'], "func": f12_profitability_snapshot_ebitda_roe_1260d_slope_v084_signal},
    "f12_profitability_snapshot_gp_roe_63d_slope_v085_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_63d_slope_v085_signal},
    "f12_profitability_snapshot_gp_roe_126d_slope_v086_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_126d_slope_v086_signal},
    "f12_profitability_snapshot_gp_roe_252d_slope_v087_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_252d_slope_v087_signal},
    "f12_profitability_snapshot_gp_roe_504d_slope_v088_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_504d_slope_v088_signal},
    "f12_profitability_snapshot_gp_roe_756d_slope_v089_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_756d_slope_v089_signal},
    "f12_profitability_snapshot_gp_roe_1260d_slope_v090_signal": {"inputs": ['arg_gp', 'arg_equity'], "func": f12_profitability_snapshot_gp_roe_1260d_slope_v090_signal},
    "f12_profitability_snapshot_ni_to_gp_63d_slope_v091_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_63d_slope_v091_signal},
    "f12_profitability_snapshot_ni_to_gp_126d_slope_v092_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_126d_slope_v092_signal},
    "f12_profitability_snapshot_ni_to_gp_252d_slope_v093_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_252d_slope_v093_signal},
    "f12_profitability_snapshot_ni_to_gp_504d_slope_v094_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_504d_slope_v094_signal},
    "f12_profitability_snapshot_ni_to_gp_756d_slope_v095_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_756d_slope_v095_signal},
    "f12_profitability_snapshot_ni_to_gp_1260d_slope_v096_signal": {"inputs": ['arg_gp', 'arg_netinc'], "func": f12_profitability_snapshot_ni_to_gp_1260d_slope_v096_signal},
    "f12_profitability_snapshot_ni_to_ebitda_63d_slope_v097_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_63d_slope_v097_signal},
    "f12_profitability_snapshot_ni_to_ebitda_126d_slope_v098_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_126d_slope_v098_signal},
    "f12_profitability_snapshot_ni_to_ebitda_252d_slope_v099_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_252d_slope_v099_signal},
    "f12_profitability_snapshot_ni_to_ebitda_504d_slope_v100_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_504d_slope_v100_signal},
    "f12_profitability_snapshot_ni_to_ebitda_756d_slope_v101_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_756d_slope_v101_signal},
    "f12_profitability_snapshot_ni_to_ebitda_1260d_slope_v102_signal": {"inputs": ['arg_netinc', 'arg_ebitda'], "func": f12_profitability_snapshot_ni_to_ebitda_1260d_slope_v102_signal},
    "f12_profitability_snapshot_ebitda_to_gp_63d_slope_v103_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_63d_slope_v103_signal},
    "f12_profitability_snapshot_ebitda_to_gp_126d_slope_v104_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_126d_slope_v104_signal},
    "f12_profitability_snapshot_ebitda_to_gp_252d_slope_v105_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_252d_slope_v105_signal},
    "f12_profitability_snapshot_ebitda_to_gp_504d_slope_v106_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_504d_slope_v106_signal},
    "f12_profitability_snapshot_ebitda_to_gp_756d_slope_v107_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_756d_slope_v107_signal},
    "f12_profitability_snapshot_ebitda_to_gp_1260d_slope_v108_signal": {"inputs": ['arg_gp', 'arg_ebitda'], "func": f12_profitability_snapshot_ebitda_to_gp_1260d_slope_v108_signal},
    "f12_profitability_snapshot_cogs_to_rev_63d_slope_v109_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_63d_slope_v109_signal},
    "f12_profitability_snapshot_cogs_to_rev_126d_slope_v110_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_126d_slope_v110_signal},
    "f12_profitability_snapshot_cogs_to_rev_252d_slope_v111_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_252d_slope_v111_signal},
    "f12_profitability_snapshot_cogs_to_rev_504d_slope_v112_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_504d_slope_v112_signal},
    "f12_profitability_snapshot_cogs_to_rev_756d_slope_v113_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_756d_slope_v113_signal},
    "f12_profitability_snapshot_cogs_to_rev_1260d_slope_v114_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_cogs_to_rev_1260d_slope_v114_signal},
    "f12_profitability_snapshot_opex_to_rev_63d_slope_v115_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_63d_slope_v115_signal},
    "f12_profitability_snapshot_opex_to_rev_126d_slope_v116_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_126d_slope_v116_signal},
    "f12_profitability_snapshot_opex_to_rev_252d_slope_v117_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_252d_slope_v117_signal},
    "f12_profitability_snapshot_opex_to_rev_504d_slope_v118_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_504d_slope_v118_signal},
    "f12_profitability_snapshot_opex_to_rev_756d_slope_v119_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_756d_slope_v119_signal},
    "f12_profitability_snapshot_opex_to_rev_1260d_slope_v120_signal": {"inputs": ['arg_gp', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_opex_to_rev_1260d_slope_v120_signal},
    "f12_profitability_snapshot_tax_int_to_rev_63d_slope_v121_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_63d_slope_v121_signal},
    "f12_profitability_snapshot_tax_int_to_rev_126d_slope_v122_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_126d_slope_v122_signal},
    "f12_profitability_snapshot_tax_int_to_rev_252d_slope_v123_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_252d_slope_v123_signal},
    "f12_profitability_snapshot_tax_int_to_rev_504d_slope_v124_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_504d_slope_v124_signal},
    "f12_profitability_snapshot_tax_int_to_rev_756d_slope_v125_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_756d_slope_v125_signal},
    "f12_profitability_snapshot_tax_int_to_rev_1260d_slope_v126_signal": {"inputs": ['arg_netinc', 'arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_tax_int_to_rev_1260d_slope_v126_signal},
    "f12_profitability_snapshot_equity_to_assets_63d_slope_v127_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_63d_slope_v127_signal},
    "f12_profitability_snapshot_equity_to_assets_126d_slope_v128_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_126d_slope_v128_signal},
    "f12_profitability_snapshot_equity_to_assets_252d_slope_v129_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_252d_slope_v129_signal},
    "f12_profitability_snapshot_equity_to_assets_504d_slope_v130_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_504d_slope_v130_signal},
    "f12_profitability_snapshot_equity_to_assets_756d_slope_v131_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_756d_slope_v131_signal},
    "f12_profitability_snapshot_equity_to_assets_1260d_slope_v132_signal": {"inputs": ['arg_equity', 'arg_assets'], "func": f12_profitability_snapshot_equity_to_assets_1260d_slope_v132_signal},
    "f12_profitability_snapshot_shares_to_assets_63d_slope_v133_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_63d_slope_v133_signal},
    "f12_profitability_snapshot_shares_to_assets_126d_slope_v134_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_126d_slope_v134_signal},
    "f12_profitability_snapshot_shares_to_assets_252d_slope_v135_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_252d_slope_v135_signal},
    "f12_profitability_snapshot_shares_to_assets_504d_slope_v136_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_504d_slope_v136_signal},
    "f12_profitability_snapshot_shares_to_assets_756d_slope_v137_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_756d_slope_v137_signal},
    "f12_profitability_snapshot_shares_to_assets_1260d_slope_v138_signal": {"inputs": ['arg_assets', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_assets_1260d_slope_v138_signal},
    "f12_profitability_snapshot_shares_to_rev_63d_slope_v139_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_63d_slope_v139_signal},
    "f12_profitability_snapshot_shares_to_rev_126d_slope_v140_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_126d_slope_v140_signal},
    "f12_profitability_snapshot_shares_to_rev_252d_slope_v141_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_252d_slope_v141_signal},
    "f12_profitability_snapshot_shares_to_rev_504d_slope_v142_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_504d_slope_v142_signal},
    "f12_profitability_snapshot_shares_to_rev_756d_slope_v143_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_756d_slope_v143_signal},
    "f12_profitability_snapshot_shares_to_rev_1260d_slope_v144_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_shares_to_rev_1260d_slope_v144_signal},
    "f12_profitability_snapshot_gp_to_cogs_63d_slope_v145_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_63d_slope_v145_signal},
    "f12_profitability_snapshot_gp_to_cogs_126d_slope_v146_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_126d_slope_v146_signal},
    "f12_profitability_snapshot_gp_to_cogs_252d_slope_v147_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_252d_slope_v147_signal},
    "f12_profitability_snapshot_gp_to_cogs_504d_slope_v148_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_504d_slope_v148_signal},
    "f12_profitability_snapshot_gp_to_cogs_756d_slope_v149_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_756d_slope_v149_signal},
    "f12_profitability_snapshot_gp_to_cogs_1260d_slope_v150_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gp_to_cogs_1260d_slope_v150_signal}
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
    for n, c in F12_PROFITABILITY_SNAPSHOT_SLOPE_001_150_REGISTRY.items():
        r = c['func'](**{i: d[i.replace('arg_', '')] for i in c['inputs']})
        assert isinstance(r, pd.Series), f'{n} failed'
        assert len(r) > 0, f'{n} empty'
        assert r.nunique() > 2, f'{n} too few unique values: {r.nunique()}'
        assert r.std() > 0, f'{n} zero std'
    print('OK')
