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

def f49_tax_arbitrage_effective_tax_z_504d_v076_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_756d_v077_signal(taxexp):
    res = _z(taxexp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_756d_v078_signal(ebt):
    res = _z(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_756d_v079_signal(netinc):
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_756d_v080_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_1008d_v081_signal(taxexp):
    res = _z(taxexp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_1008d_v082_signal(ebt):
    res = _z(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_1008d_v083_signal(netinc):
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_1008d_v084_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_1260d_v085_signal(taxexp):
    res = _z(taxexp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_1260d_v086_signal(ebt):
    res = _z(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_1260d_v087_signal(netinc):
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_1260d_v088_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_5d_v089_signal(taxexp):
    res = _drawdown(taxexp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_5d_v090_signal(ebt):
    res = _drawdown(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_5d_v091_signal(netinc):
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_5d_v092_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_10d_v093_signal(taxexp):
    res = _drawdown(taxexp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_10d_v094_signal(ebt):
    res = _drawdown(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_10d_v095_signal(netinc):
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_10d_v096_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_21d_v097_signal(taxexp):
    res = _drawdown(taxexp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_21d_v098_signal(ebt):
    res = _drawdown(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_21d_v099_signal(netinc):
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_21d_v100_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_42d_v101_signal(taxexp):
    res = _drawdown(taxexp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_42d_v102_signal(ebt):
    res = _drawdown(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_42d_v103_signal(netinc):
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_42d_v104_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_63d_v105_signal(taxexp):
    res = _drawdown(taxexp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_63d_v106_signal(ebt):
    res = _drawdown(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_63d_v107_signal(netinc):
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_63d_v108_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_126d_v109_signal(taxexp):
    res = _drawdown(taxexp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_126d_v110_signal(ebt):
    res = _drawdown(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_126d_v111_signal(netinc):
    res = _drawdown(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_126d_v112_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_252d_v113_signal(taxexp):
    res = _drawdown(taxexp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_252d_v114_signal(ebt):
    res = _drawdown(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_252d_v115_signal(netinc):
    res = _drawdown(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_252d_v116_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_504d_v117_signal(taxexp):
    res = _drawdown(taxexp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_504d_v118_signal(ebt):
    res = _drawdown(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_504d_v119_signal(netinc):
    res = _drawdown(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_504d_v120_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_756d_v121_signal(taxexp):
    res = _drawdown(taxexp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_756d_v122_signal(ebt):
    res = _drawdown(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_756d_v123_signal(netinc):
    res = _drawdown(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_756d_v124_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_1008d_v125_signal(taxexp):
    res = _drawdown(taxexp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_1008d_v126_signal(ebt):
    res = _drawdown(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_1008d_v127_signal(netinc):
    res = _drawdown(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_1008d_v128_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_dd_1260d_v129_signal(taxexp):
    res = _drawdown(taxexp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_dd_1260d_v130_signal(ebt):
    res = _drawdown(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_dd_1260d_v131_signal(netinc):
    res = _drawdown(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_dd_1260d_v132_signal(taxexp, ebt):
    res = _drawdown(_ratio(taxexp, ebt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_rec_5d_v133_signal(taxexp):
    res = _recovery(taxexp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_rec_5d_v134_signal(ebt):
    res = _recovery(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_rec_5d_v135_signal(netinc):
    res = _recovery(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_rec_5d_v136_signal(taxexp, ebt):
    res = _recovery(_ratio(taxexp, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_rec_10d_v137_signal(taxexp):
    res = _recovery(taxexp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_rec_10d_v138_signal(ebt):
    res = _recovery(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_rec_10d_v139_signal(netinc):
    res = _recovery(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_rec_10d_v140_signal(taxexp, ebt):
    res = _recovery(_ratio(taxexp, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_rec_21d_v141_signal(taxexp):
    res = _recovery(taxexp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_rec_21d_v142_signal(ebt):
    res = _recovery(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_rec_21d_v143_signal(netinc):
    res = _recovery(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_rec_21d_v144_signal(taxexp, ebt):
    res = _recovery(_ratio(taxexp, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_rec_42d_v145_signal(taxexp):
    res = _recovery(taxexp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_rec_42d_v146_signal(ebt):
    res = _recovery(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_rec_42d_v147_signal(netinc):
    res = _recovery(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_rec_42d_v148_signal(taxexp, ebt):
    res = _recovery(_ratio(taxexp, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_rec_63d_v149_signal(taxexp):
    res = _recovery(taxexp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_rec_63d_v150_signal(ebt):
    res = _recovery(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 49...")
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
