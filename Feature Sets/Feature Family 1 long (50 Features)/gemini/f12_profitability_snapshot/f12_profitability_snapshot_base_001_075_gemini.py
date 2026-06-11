import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 5)).std().replace(0, np.nan)
def _prof_margin(num, den): return num / den.replace(0, np.nan)
def _prof_roe(ni, eq): return ni / eq.replace(0, np.nan)

def f12_profitability_snapshot_gross_margin_63d_base_v001_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_126d_base_v002_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_252d_base_v003_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_504d_base_v004_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_756d_base_v005_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gross_margin_1260d_base_v006_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_63d_base_v007_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_126d_base_v008_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_252d_base_v009_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_504d_base_v010_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_756d_base_v011_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_margin_1260d_base_v012_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_63d_base_v013_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_126d_base_v014_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_252d_base_v015_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_504d_base_v016_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_756d_base_v017_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_net_margin_1260d_base_v018_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_63d_base_v019_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_126d_base_v020_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_252d_base_v021_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_504d_base_v022_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_756d_base_v023_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roe_1260d_base_v024_signal(arg_netinc, arg_equity) -> pd.Series:
    res = _sma(_prof_roe(arg_netinc, arg_equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_63d_base_v025_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_126d_base_v026_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_252d_base_v027_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_504d_base_v028_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_756d_base_v029_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_roa_1260d_base_v030_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_63d_base_v031_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_126d_base_v032_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_252d_base_v033_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_504d_base_v034_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_756d_base_v035_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_eps_proxy_1260d_base_v036_signal(arg_netinc, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_netinc, arg_shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_63d_base_v037_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_126d_base_v038_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_252d_base_v039_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_504d_base_v040_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_756d_base_v041_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_per_share_1260d_base_v042_signal(arg_gp, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_63d_base_v043_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_126d_base_v044_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_252d_base_v045_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_504d_base_v046_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_756d_base_v047_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_per_share_1260d_base_v048_signal(arg_ebitda, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_63d_base_v049_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_126d_base_v050_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_252d_base_v051_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_504d_base_v052_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_756d_base_v053_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_sales_per_share_1260d_base_v054_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_63d_base_v055_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_126d_base_v056_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_252d_base_v057_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_504d_base_v058_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_756d_base_v059_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_asset_turnover_1260d_base_v060_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_63d_base_v061_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_126d_base_v062_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_252d_base_v063_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_504d_base_v064_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_756d_base_v065_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_equity_turnover_1260d_base_v066_signal(arg_revenue, arg_equity) -> pd.Series:
    res = _sma(_prof_margin(arg_revenue, arg_equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_63d_base_v067_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_126d_base_v068_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_252d_base_v069_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_504d_base_v070_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_756d_base_v071_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_ebitda_roa_1260d_base_v072_signal(arg_ebitda, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_ebitda, arg_assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_63d_base_v073_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_126d_base_v074_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_profitability_snapshot_gp_roa_252d_base_v075_signal(arg_gp, arg_assets) -> pd.Series:
    res = _sma(_prof_margin(arg_gp, arg_assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = 'read_only', 'fundamentals', 'ticker', 'date'
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f'fundamentals.{c}' for c in ['gp', 'netinc', 'ebitda', 'revenue', 'equity', 'assets', 'shareswa']}

F12_PROFITABILITY_SNAPSHOT_BASE_001_075_REGISTRY = {
    "f12_profitability_snapshot_gross_margin_63d_base_v001_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_63d_base_v001_signal},
    "f12_profitability_snapshot_gross_margin_126d_base_v002_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_126d_base_v002_signal},
    "f12_profitability_snapshot_gross_margin_252d_base_v003_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_252d_base_v003_signal},
    "f12_profitability_snapshot_gross_margin_504d_base_v004_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_504d_base_v004_signal},
    "f12_profitability_snapshot_gross_margin_756d_base_v005_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_756d_base_v005_signal},
    "f12_profitability_snapshot_gross_margin_1260d_base_v006_signal": {"inputs": ['arg_gp', 'arg_revenue'], "func": f12_profitability_snapshot_gross_margin_1260d_base_v006_signal},
    "f12_profitability_snapshot_ebitda_margin_63d_base_v007_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_63d_base_v007_signal},
    "f12_profitability_snapshot_ebitda_margin_126d_base_v008_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_126d_base_v008_signal},
    "f12_profitability_snapshot_ebitda_margin_252d_base_v009_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_252d_base_v009_signal},
    "f12_profitability_snapshot_ebitda_margin_504d_base_v010_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_504d_base_v010_signal},
    "f12_profitability_snapshot_ebitda_margin_756d_base_v011_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_756d_base_v011_signal},
    "f12_profitability_snapshot_ebitda_margin_1260d_base_v012_signal": {"inputs": ['arg_ebitda', 'arg_revenue'], "func": f12_profitability_snapshot_ebitda_margin_1260d_base_v012_signal},
    "f12_profitability_snapshot_net_margin_63d_base_v013_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_63d_base_v013_signal},
    "f12_profitability_snapshot_net_margin_126d_base_v014_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_126d_base_v014_signal},
    "f12_profitability_snapshot_net_margin_252d_base_v015_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_252d_base_v015_signal},
    "f12_profitability_snapshot_net_margin_504d_base_v016_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_504d_base_v016_signal},
    "f12_profitability_snapshot_net_margin_756d_base_v017_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_756d_base_v017_signal},
    "f12_profitability_snapshot_net_margin_1260d_base_v018_signal": {"inputs": ['arg_netinc', 'arg_revenue'], "func": f12_profitability_snapshot_net_margin_1260d_base_v018_signal},
    "f12_profitability_snapshot_roe_63d_base_v019_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_63d_base_v019_signal},
    "f12_profitability_snapshot_roe_126d_base_v020_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_126d_base_v020_signal},
    "f12_profitability_snapshot_roe_252d_base_v021_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_252d_base_v021_signal},
    "f12_profitability_snapshot_roe_504d_base_v022_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_504d_base_v022_signal},
    "f12_profitability_snapshot_roe_756d_base_v023_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_756d_base_v023_signal},
    "f12_profitability_snapshot_roe_1260d_base_v024_signal": {"inputs": ['arg_netinc', 'arg_equity'], "func": f12_profitability_snapshot_roe_1260d_base_v024_signal},
    "f12_profitability_snapshot_roa_63d_base_v025_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_63d_base_v025_signal},
    "f12_profitability_snapshot_roa_126d_base_v026_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_126d_base_v026_signal},
    "f12_profitability_snapshot_roa_252d_base_v027_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_252d_base_v027_signal},
    "f12_profitability_snapshot_roa_504d_base_v028_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_504d_base_v028_signal},
    "f12_profitability_snapshot_roa_756d_base_v029_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_756d_base_v029_signal},
    "f12_profitability_snapshot_roa_1260d_base_v030_signal": {"inputs": ['arg_netinc', 'arg_assets'], "func": f12_profitability_snapshot_roa_1260d_base_v030_signal},
    "f12_profitability_snapshot_eps_proxy_63d_base_v031_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_63d_base_v031_signal},
    "f12_profitability_snapshot_eps_proxy_126d_base_v032_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_126d_base_v032_signal},
    "f12_profitability_snapshot_eps_proxy_252d_base_v033_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_252d_base_v033_signal},
    "f12_profitability_snapshot_eps_proxy_504d_base_v034_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_504d_base_v034_signal},
    "f12_profitability_snapshot_eps_proxy_756d_base_v035_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_756d_base_v035_signal},
    "f12_profitability_snapshot_eps_proxy_1260d_base_v036_signal": {"inputs": ['arg_netinc', 'arg_shareswa'], "func": f12_profitability_snapshot_eps_proxy_1260d_base_v036_signal},
    "f12_profitability_snapshot_gp_per_share_63d_base_v037_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_63d_base_v037_signal},
    "f12_profitability_snapshot_gp_per_share_126d_base_v038_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_126d_base_v038_signal},
    "f12_profitability_snapshot_gp_per_share_252d_base_v039_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_252d_base_v039_signal},
    "f12_profitability_snapshot_gp_per_share_504d_base_v040_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_504d_base_v040_signal},
    "f12_profitability_snapshot_gp_per_share_756d_base_v041_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_756d_base_v041_signal},
    "f12_profitability_snapshot_gp_per_share_1260d_base_v042_signal": {"inputs": ['arg_gp', 'arg_shareswa'], "func": f12_profitability_snapshot_gp_per_share_1260d_base_v042_signal},
    "f12_profitability_snapshot_ebitda_per_share_63d_base_v043_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_63d_base_v043_signal},
    "f12_profitability_snapshot_ebitda_per_share_126d_base_v044_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_126d_base_v044_signal},
    "f12_profitability_snapshot_ebitda_per_share_252d_base_v045_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_252d_base_v045_signal},
    "f12_profitability_snapshot_ebitda_per_share_504d_base_v046_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_504d_base_v046_signal},
    "f12_profitability_snapshot_ebitda_per_share_756d_base_v047_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_756d_base_v047_signal},
    "f12_profitability_snapshot_ebitda_per_share_1260d_base_v048_signal": {"inputs": ['arg_ebitda', 'arg_shareswa'], "func": f12_profitability_snapshot_ebitda_per_share_1260d_base_v048_signal},
    "f12_profitability_snapshot_sales_per_share_63d_base_v049_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_63d_base_v049_signal},
    "f12_profitability_snapshot_sales_per_share_126d_base_v050_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_126d_base_v050_signal},
    "f12_profitability_snapshot_sales_per_share_252d_base_v051_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_252d_base_v051_signal},
    "f12_profitability_snapshot_sales_per_share_504d_base_v052_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_504d_base_v052_signal},
    "f12_profitability_snapshot_sales_per_share_756d_base_v053_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_756d_base_v053_signal},
    "f12_profitability_snapshot_sales_per_share_1260d_base_v054_signal": {"inputs": ['arg_revenue', 'arg_shareswa'], "func": f12_profitability_snapshot_sales_per_share_1260d_base_v054_signal},
    "f12_profitability_snapshot_asset_turnover_63d_base_v055_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_63d_base_v055_signal},
    "f12_profitability_snapshot_asset_turnover_126d_base_v056_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_126d_base_v056_signal},
    "f12_profitability_snapshot_asset_turnover_252d_base_v057_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_252d_base_v057_signal},
    "f12_profitability_snapshot_asset_turnover_504d_base_v058_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_504d_base_v058_signal},
    "f12_profitability_snapshot_asset_turnover_756d_base_v059_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_756d_base_v059_signal},
    "f12_profitability_snapshot_asset_turnover_1260d_base_v060_signal": {"inputs": ['arg_revenue', 'arg_assets'], "func": f12_profitability_snapshot_asset_turnover_1260d_base_v060_signal},
    "f12_profitability_snapshot_equity_turnover_63d_base_v061_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_63d_base_v061_signal},
    "f12_profitability_snapshot_equity_turnover_126d_base_v062_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_126d_base_v062_signal},
    "f12_profitability_snapshot_equity_turnover_252d_base_v063_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_252d_base_v063_signal},
    "f12_profitability_snapshot_equity_turnover_504d_base_v064_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_504d_base_v064_signal},
    "f12_profitability_snapshot_equity_turnover_756d_base_v065_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_756d_base_v065_signal},
    "f12_profitability_snapshot_equity_turnover_1260d_base_v066_signal": {"inputs": ['arg_revenue', 'arg_equity'], "func": f12_profitability_snapshot_equity_turnover_1260d_base_v066_signal},
    "f12_profitability_snapshot_ebitda_roa_63d_base_v067_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_63d_base_v067_signal},
    "f12_profitability_snapshot_ebitda_roa_126d_base_v068_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_126d_base_v068_signal},
    "f12_profitability_snapshot_ebitda_roa_252d_base_v069_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_252d_base_v069_signal},
    "f12_profitability_snapshot_ebitda_roa_504d_base_v070_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_504d_base_v070_signal},
    "f12_profitability_snapshot_ebitda_roa_756d_base_v071_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_756d_base_v071_signal},
    "f12_profitability_snapshot_ebitda_roa_1260d_base_v072_signal": {"inputs": ['arg_ebitda', 'arg_assets'], "func": f12_profitability_snapshot_ebitda_roa_1260d_base_v072_signal},
    "f12_profitability_snapshot_gp_roa_63d_base_v073_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_63d_base_v073_signal},
    "f12_profitability_snapshot_gp_roa_126d_base_v074_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_126d_base_v074_signal},
    "f12_profitability_snapshot_gp_roa_252d_base_v075_signal": {"inputs": ['arg_gp', 'arg_assets'], "func": f12_profitability_snapshot_gp_roa_252d_base_v075_signal}
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
    for n, c in F12_PROFITABILITY_SNAPSHOT_BASE_001_075_REGISTRY.items():
        r = c['func'](**{i: d[i.replace('arg_', '')] for i in c['inputs']})
        assert isinstance(r, pd.Series), f'{n} failed'
        assert len(r) > 0, f'{n} empty'
        assert r.nunique() > 2, f'{n} too few unique values: {r.nunique()}'
        assert r.std() > 0, f'{n} zero std'
    print('OK')
