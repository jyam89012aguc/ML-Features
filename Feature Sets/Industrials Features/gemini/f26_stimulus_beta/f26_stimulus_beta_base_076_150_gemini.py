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

def f26_stimulus_beta_asset_growth_z_504d_v076_signal(assets):
    res = _z(_slope_pct(assets, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_z_756d_v077_signal(revenue):
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_z_756d_v078_signal(assets):
    res = _z(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_z_756d_v079_signal(capex):
    res = _z(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_z_756d_v080_signal(assets):
    res = _z(_slope_pct(assets, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_z_1008d_v081_signal(revenue):
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_z_1008d_v082_signal(assets):
    res = _z(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_z_1008d_v083_signal(capex):
    res = _z(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_z_1008d_v084_signal(assets):
    res = _z(_slope_pct(assets, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_z_1260d_v085_signal(revenue):
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_z_1260d_v086_signal(assets):
    res = _z(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_z_1260d_v087_signal(capex):
    res = _z(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_z_1260d_v088_signal(assets):
    res = _z(_slope_pct(assets, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_5d_v089_signal(revenue):
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_5d_v090_signal(assets):
    res = _drawdown(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_5d_v091_signal(capex):
    res = _drawdown(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_5d_v092_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_10d_v093_signal(revenue):
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_10d_v094_signal(assets):
    res = _drawdown(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_10d_v095_signal(capex):
    res = _drawdown(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_10d_v096_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_21d_v097_signal(revenue):
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_21d_v098_signal(assets):
    res = _drawdown(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_21d_v099_signal(capex):
    res = _drawdown(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_21d_v100_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_42d_v101_signal(revenue):
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_42d_v102_signal(assets):
    res = _drawdown(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_42d_v103_signal(capex):
    res = _drawdown(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_42d_v104_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_63d_v105_signal(revenue):
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_63d_v106_signal(assets):
    res = _drawdown(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_63d_v107_signal(capex):
    res = _drawdown(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_63d_v108_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_126d_v109_signal(revenue):
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_126d_v110_signal(assets):
    res = _drawdown(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_126d_v111_signal(capex):
    res = _drawdown(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_126d_v112_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_252d_v113_signal(revenue):
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_252d_v114_signal(assets):
    res = _drawdown(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_252d_v115_signal(capex):
    res = _drawdown(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_252d_v116_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_504d_v117_signal(revenue):
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_504d_v118_signal(assets):
    res = _drawdown(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_504d_v119_signal(capex):
    res = _drawdown(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_504d_v120_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_756d_v121_signal(revenue):
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_756d_v122_signal(assets):
    res = _drawdown(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_756d_v123_signal(capex):
    res = _drawdown(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_756d_v124_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_1008d_v125_signal(revenue):
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_1008d_v126_signal(assets):
    res = _drawdown(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_1008d_v127_signal(capex):
    res = _drawdown(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_1008d_v128_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_dd_1260d_v129_signal(revenue):
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_dd_1260d_v130_signal(assets):
    res = _drawdown(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_dd_1260d_v131_signal(capex):
    res = _drawdown(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_dd_1260d_v132_signal(assets):
    res = _drawdown(_slope_pct(assets, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_rec_5d_v133_signal(revenue):
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_rec_5d_v134_signal(assets):
    res = _recovery(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_rec_5d_v135_signal(capex):
    res = _recovery(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_rec_5d_v136_signal(assets):
    res = _recovery(_slope_pct(assets, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_rec_10d_v137_signal(revenue):
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_rec_10d_v138_signal(assets):
    res = _recovery(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_rec_10d_v139_signal(capex):
    res = _recovery(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_rec_10d_v140_signal(assets):
    res = _recovery(_slope_pct(assets, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_rec_21d_v141_signal(revenue):
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_rec_21d_v142_signal(assets):
    res = _recovery(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_rec_21d_v143_signal(capex):
    res = _recovery(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_rec_21d_v144_signal(assets):
    res = _recovery(_slope_pct(assets, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_rec_42d_v145_signal(revenue):
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_rec_42d_v146_signal(assets):
    res = _recovery(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_capex_rec_42d_v147_signal(capex):
    res = _recovery(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_asset_growth_rec_42d_v148_signal(assets):
    res = _recovery(_slope_pct(assets, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_revenue_rec_63d_v149_signal(revenue):
    res = _recovery(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_stimulus_beta_assets_rec_63d_v150_signal(assets):
    res = _recovery(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 26...")
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
