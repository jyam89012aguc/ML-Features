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

def f06_receivable_turnover_receivables_base_5d_v001_signal(receivables):
    res = _sma(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_5d_v002_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_5d_v003_signal(cashneq):
    res = _sma(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_5d_v004_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_5d_v005_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_10d_v006_signal(receivables):
    res = _sma(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_10d_v007_signal(revenue):
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_10d_v008_signal(cashneq):
    res = _sma(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_10d_v009_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_10d_v010_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_21d_v011_signal(receivables):
    res = _sma(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_21d_v012_signal(revenue):
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_21d_v013_signal(cashneq):
    res = _sma(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_21d_v014_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_21d_v015_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_42d_v016_signal(receivables):
    res = _sma(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_42d_v017_signal(revenue):
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_42d_v018_signal(cashneq):
    res = _sma(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_42d_v019_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_42d_v020_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_63d_v021_signal(receivables):
    res = _sma(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_63d_v022_signal(revenue):
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_63d_v023_signal(cashneq):
    res = _sma(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_63d_v024_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_63d_v025_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_126d_v026_signal(receivables):
    res = _sma(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_126d_v027_signal(revenue):
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_126d_v028_signal(cashneq):
    res = _sma(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_126d_v029_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_126d_v030_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_252d_v031_signal(receivables):
    res = _sma(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_252d_v032_signal(revenue):
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_252d_v033_signal(cashneq):
    res = _sma(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_252d_v034_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_252d_v035_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_504d_v036_signal(receivables):
    res = _sma(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_504d_v037_signal(revenue):
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_504d_v038_signal(cashneq):
    res = _sma(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_504d_v039_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_504d_v040_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_756d_v041_signal(receivables):
    res = _sma(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_756d_v042_signal(revenue):
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_756d_v043_signal(cashneq):
    res = _sma(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_756d_v044_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_756d_v045_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_1008d_v046_signal(receivables):
    res = _sma(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_1008d_v047_signal(revenue):
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_1008d_v048_signal(cashneq):
    res = _sma(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_1008d_v049_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_1008d_v050_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_base_1260d_v051_signal(receivables):
    res = _sma(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_base_1260d_v052_signal(revenue):
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_base_1260d_v053_signal(cashneq):
    res = _sma(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_base_1260d_v054_signal(receivables, revenue):
    res = _sma(_ratio(receivables, revenue) * 365, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_base_1260d_v055_signal(cashneq, revenue):
    res = _sma(_ratio(cashneq, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_z_5d_v056_signal(receivables):
    res = _z(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_z_5d_v057_signal(revenue):
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_z_5d_v058_signal(cashneq):
    res = _z(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_z_5d_v059_signal(receivables, revenue):
    res = _z(_ratio(receivables, revenue) * 365, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_z_5d_v060_signal(cashneq, revenue):
    res = _z(_ratio(cashneq, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_z_10d_v061_signal(receivables):
    res = _z(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_z_10d_v062_signal(revenue):
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_z_10d_v063_signal(cashneq):
    res = _z(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_z_10d_v064_signal(receivables, revenue):
    res = _z(_ratio(receivables, revenue) * 365, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_z_10d_v065_signal(cashneq, revenue):
    res = _z(_ratio(cashneq, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_z_21d_v066_signal(receivables):
    res = _z(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_z_21d_v067_signal(revenue):
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_z_21d_v068_signal(cashneq):
    res = _z(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_z_21d_v069_signal(receivables, revenue):
    res = _z(_ratio(receivables, revenue) * 365, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_z_21d_v070_signal(cashneq, revenue):
    res = _z(_ratio(cashneq, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_receivables_z_42d_v071_signal(receivables):
    res = _z(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_revenue_z_42d_v072_signal(revenue):
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cashneq_z_42d_v073_signal(cashneq):
    res = _z(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_dso_proxy_z_42d_v074_signal(receivables, revenue):
    res = _z(_ratio(receivables, revenue) * 365, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_receivable_turnover_cash_to_rev_z_42d_v075_signal(cashneq, revenue):
    res = _z(_ratio(cashneq, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 06...")
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
