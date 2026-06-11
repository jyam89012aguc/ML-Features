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

def f46_mna_integration_mna_intensity_z_504d_v076_signal(ncfbus, assets):
    res = _z(_ratio(ncfbus, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_z_756d_v077_signal(ncfbus):
    res = _z(ncfbus, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_z_756d_v078_signal(revenue):
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_z_756d_v079_signal(assets):
    res = _z(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_z_756d_v080_signal(ncfbus, assets):
    res = _z(_ratio(ncfbus, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_z_1008d_v081_signal(ncfbus):
    res = _z(ncfbus, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_z_1008d_v082_signal(revenue):
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_z_1008d_v083_signal(assets):
    res = _z(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_z_1008d_v084_signal(ncfbus, assets):
    res = _z(_ratio(ncfbus, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_z_1260d_v085_signal(ncfbus):
    res = _z(ncfbus, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_z_1260d_v086_signal(revenue):
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_z_1260d_v087_signal(assets):
    res = _z(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_z_1260d_v088_signal(ncfbus, assets):
    res = _z(_ratio(ncfbus, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_5d_v089_signal(ncfbus):
    res = _drawdown(ncfbus, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_5d_v090_signal(revenue):
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_5d_v091_signal(assets):
    res = _drawdown(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_5d_v092_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_10d_v093_signal(ncfbus):
    res = _drawdown(ncfbus, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_10d_v094_signal(revenue):
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_10d_v095_signal(assets):
    res = _drawdown(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_10d_v096_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_21d_v097_signal(ncfbus):
    res = _drawdown(ncfbus, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_21d_v098_signal(revenue):
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_21d_v099_signal(assets):
    res = _drawdown(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_21d_v100_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_42d_v101_signal(ncfbus):
    res = _drawdown(ncfbus, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_42d_v102_signal(revenue):
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_42d_v103_signal(assets):
    res = _drawdown(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_42d_v104_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_63d_v105_signal(ncfbus):
    res = _drawdown(ncfbus, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_63d_v106_signal(revenue):
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_63d_v107_signal(assets):
    res = _drawdown(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_63d_v108_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_126d_v109_signal(ncfbus):
    res = _drawdown(ncfbus, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_126d_v110_signal(revenue):
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_126d_v111_signal(assets):
    res = _drawdown(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_126d_v112_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_252d_v113_signal(ncfbus):
    res = _drawdown(ncfbus, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_252d_v114_signal(revenue):
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_252d_v115_signal(assets):
    res = _drawdown(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_252d_v116_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_504d_v117_signal(ncfbus):
    res = _drawdown(ncfbus, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_504d_v118_signal(revenue):
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_504d_v119_signal(assets):
    res = _drawdown(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_504d_v120_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_756d_v121_signal(ncfbus):
    res = _drawdown(ncfbus, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_756d_v122_signal(revenue):
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_756d_v123_signal(assets):
    res = _drawdown(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_756d_v124_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_1008d_v125_signal(ncfbus):
    res = _drawdown(ncfbus, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_1008d_v126_signal(revenue):
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_1008d_v127_signal(assets):
    res = _drawdown(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_1008d_v128_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_dd_1260d_v129_signal(ncfbus):
    res = _drawdown(ncfbus, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_dd_1260d_v130_signal(revenue):
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_dd_1260d_v131_signal(assets):
    res = _drawdown(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_dd_1260d_v132_signal(ncfbus, assets):
    res = _drawdown(_ratio(ncfbus, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_rec_5d_v133_signal(ncfbus):
    res = _recovery(ncfbus, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_rec_5d_v134_signal(revenue):
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_rec_5d_v135_signal(assets):
    res = _recovery(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_rec_5d_v136_signal(ncfbus, assets):
    res = _recovery(_ratio(ncfbus, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_rec_10d_v137_signal(ncfbus):
    res = _recovery(ncfbus, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_rec_10d_v138_signal(revenue):
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_rec_10d_v139_signal(assets):
    res = _recovery(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_rec_10d_v140_signal(ncfbus, assets):
    res = _recovery(_ratio(ncfbus, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_rec_21d_v141_signal(ncfbus):
    res = _recovery(ncfbus, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_rec_21d_v142_signal(revenue):
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_rec_21d_v143_signal(assets):
    res = _recovery(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_rec_21d_v144_signal(ncfbus, assets):
    res = _recovery(_ratio(ncfbus, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_rec_42d_v145_signal(ncfbus):
    res = _recovery(ncfbus, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_rec_42d_v146_signal(revenue):
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_rec_42d_v147_signal(assets):
    res = _recovery(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_rec_42d_v148_signal(ncfbus, assets):
    res = _recovery(_ratio(ncfbus, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_rec_63d_v149_signal(ncfbus):
    res = _recovery(ncfbus, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_rec_63d_v150_signal(revenue):
    res = _recovery(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 46...")
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
