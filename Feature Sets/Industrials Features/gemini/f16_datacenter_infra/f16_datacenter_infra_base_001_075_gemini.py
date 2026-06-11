import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return _slope_pct(s, w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()

def f16_datacenter_infra_revenue_base_5d_v001_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_5d_v002_signal(assets):
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_5d_v003_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_5d_v004_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_10d_v005_signal(revenue):
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_10d_v006_signal(assets):
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_10d_v007_signal(capex):
    res = _sma(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_10d_v008_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_21d_v009_signal(revenue):
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_21d_v010_signal(assets):
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_21d_v011_signal(capex):
    res = _sma(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_21d_v012_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_42d_v013_signal(revenue):
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_42d_v014_signal(assets):
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_42d_v015_signal(capex):
    res = _sma(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_42d_v016_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_63d_v017_signal(revenue):
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_63d_v018_signal(assets):
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_63d_v019_signal(capex):
    res = _sma(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_63d_v020_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_126d_v021_signal(revenue):
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_126d_v022_signal(assets):
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_126d_v023_signal(capex):
    res = _sma(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_126d_v024_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_252d_v025_signal(revenue):
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_252d_v026_signal(assets):
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_252d_v027_signal(capex):
    res = _sma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_252d_v028_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_504d_v029_signal(revenue):
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_504d_v030_signal(assets):
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_504d_v031_signal(capex):
    res = _sma(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_504d_v032_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_756d_v033_signal(revenue):
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_756d_v034_signal(assets):
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_756d_v035_signal(capex):
    res = _sma(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_756d_v036_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_1008d_v037_signal(revenue):
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_1008d_v038_signal(assets):
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_1008d_v039_signal(capex):
    res = _sma(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_1008d_v040_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_base_1260d_v041_signal(revenue):
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_base_1260d_v042_signal(assets):
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_base_1260d_v043_signal(capex):
    res = _sma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_base_1260d_v044_signal(revenue, assets):
    res = _sma(_ratio(revenue, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_z_5d_v045_signal(revenue):
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_z_5d_v046_signal(assets):
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_z_5d_v047_signal(capex):
    res = _z(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_z_5d_v048_signal(revenue, assets):
    res = _z(_ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_z_10d_v049_signal(revenue):
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_z_10d_v050_signal(assets):
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_z_10d_v051_signal(capex):
    res = _z(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_z_10d_v052_signal(revenue, assets):
    res = _z(_ratio(revenue, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_z_21d_v053_signal(revenue):
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_z_21d_v054_signal(assets):
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_z_21d_v055_signal(capex):
    res = _z(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_z_21d_v056_signal(revenue, assets):
    res = _z(_ratio(revenue, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_z_42d_v057_signal(revenue):
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_z_42d_v058_signal(assets):
    res = _z(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_z_42d_v059_signal(capex):
    res = _z(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_z_42d_v060_signal(revenue, assets):
    res = _z(_ratio(revenue, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_z_63d_v061_signal(revenue):
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_z_63d_v062_signal(assets):
    res = _z(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_z_63d_v063_signal(capex):
    res = _z(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_z_63d_v064_signal(revenue, assets):
    res = _z(_ratio(revenue, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_z_126d_v065_signal(revenue):
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_z_126d_v066_signal(assets):
    res = _z(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_z_126d_v067_signal(capex):
    res = _z(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_z_126d_v068_signal(revenue, assets):
    res = _z(_ratio(revenue, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_z_252d_v069_signal(revenue):
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_z_252d_v070_signal(assets):
    res = _z(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_z_252d_v071_signal(capex):
    res = _z(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_asset_turnover_z_252d_v072_signal(revenue, assets):
    res = _z(_ratio(revenue, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_revenue_z_504d_v073_signal(revenue):
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_assets_z_504d_v074_signal(assets):
    res = _z(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_datacenter_infra_capex_z_504d_v075_signal(capex):
    res = _z(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 16...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        try:
            res = func(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            break
    print("Success.")
