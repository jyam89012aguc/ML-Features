import pandas as pd
import numpy as np
import inspect

def _val_ratio(num, den):
    return num / den.replace(0, np.nan)

def _val_zscore(s, w):
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

# Ratio Groups 1-12 (72 features) + 3 from group 13 = 75 features

# 1. Trailing P/E (MarketCap / NetInc)
def f15_valuation_at_entry_pe_ratio(arg_marketcap, arg_netinc):
    return _val_ratio(arg_marketcap, arg_netinc)

def f15_valuation_at_entry_zscore_pe_63(arg_marketcap, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_pe_ratio(arg_marketcap, arg_netinc), 63)

def f15_valuation_at_entry_zscore_pe_126(arg_marketcap, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_pe_ratio(arg_marketcap, arg_netinc), 126)

def f15_valuation_at_entry_zscore_pe_252(arg_marketcap, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_pe_ratio(arg_marketcap, arg_netinc), 252)

def f15_valuation_at_entry_zscore_pe_504(arg_marketcap, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_pe_ratio(arg_marketcap, arg_netinc), 504)

def f15_valuation_at_entry_zscore_pe_756(arg_marketcap, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_pe_ratio(arg_marketcap, arg_netinc), 756)

# 2. EV/EBITDA
def f15_valuation_at_entry_evebitda_ratio(arg_ev, arg_ebitda):
    return _val_ratio(arg_ev, arg_ebitda)

def f15_valuation_at_entry_zscore_evebitda_63(arg_ev, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_evebitda_ratio(arg_ev, arg_ebitda), 63)

def f15_valuation_at_entry_zscore_evebitda_126(arg_ev, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_evebitda_ratio(arg_ev, arg_ebitda), 126)

def f15_valuation_at_entry_zscore_evebitda_252(arg_ev, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_evebitda_ratio(arg_ev, arg_ebitda), 252)

def f15_valuation_at_entry_zscore_evebitda_504(arg_ev, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_evebitda_ratio(arg_ev, arg_ebitda), 504)

def f15_valuation_at_entry_zscore_evebitda_756(arg_ev, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_evebitda_ratio(arg_ev, arg_ebitda), 756)

# 3. Price/Sales (MarketCap / Revenue)
def f15_valuation_at_entry_ps_ratio(arg_marketcap, arg_revenue):
    return _val_ratio(arg_marketcap, arg_revenue)

def f15_valuation_at_entry_zscore_ps_63(arg_marketcap, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ps_ratio(arg_marketcap, arg_revenue), 63)

def f15_valuation_at_entry_zscore_ps_126(arg_marketcap, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ps_ratio(arg_marketcap, arg_revenue), 126)

def f15_valuation_at_entry_zscore_ps_252(arg_marketcap, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ps_ratio(arg_marketcap, arg_revenue), 252)

def f15_valuation_at_entry_zscore_ps_504(arg_marketcap, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ps_ratio(arg_marketcap, arg_revenue), 504)

def f15_valuation_at_entry_zscore_ps_756(arg_marketcap, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ps_ratio(arg_marketcap, arg_revenue), 756)

# 4. Price/Book (MarketCap / Equity)
def f15_valuation_at_entry_pb_ratio(arg_marketcap, arg_equity):
    return _val_ratio(arg_marketcap, arg_equity)

def f15_valuation_at_entry_zscore_pb_63(arg_marketcap, arg_equity):
    return _val_zscore(f15_valuation_at_entry_pb_ratio(arg_marketcap, arg_equity), 63)

def f15_valuation_at_entry_zscore_pb_126(arg_marketcap, arg_equity):
    return _val_zscore(f15_valuation_at_entry_pb_ratio(arg_marketcap, arg_equity), 126)

def f15_valuation_at_entry_zscore_pb_252(arg_marketcap, arg_equity):
    return _val_zscore(f15_valuation_at_entry_pb_ratio(arg_marketcap, arg_equity), 252)

def f15_valuation_at_entry_zscore_pb_504(arg_marketcap, arg_equity):
    return _val_zscore(f15_valuation_at_entry_pb_ratio(arg_marketcap, arg_equity), 504)

def f15_valuation_at_entry_zscore_pb_756(arg_marketcap, arg_equity):
    return _val_zscore(f15_valuation_at_entry_pb_ratio(arg_marketcap, arg_equity), 756)

# 5. FCF Yield (FCF / MarketCap)
def f15_valuation_at_entry_fcf_yield_ratio(arg_fcf, arg_marketcap):
    return _val_ratio(arg_fcf, arg_marketcap)

def f15_valuation_at_entry_zscore_fcf_yield_63(arg_fcf, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_fcf_yield_ratio(arg_fcf, arg_marketcap), 63)

def f15_valuation_at_entry_zscore_fcf_yield_126(arg_fcf, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_fcf_yield_ratio(arg_fcf, arg_marketcap), 126)

def f15_valuation_at_entry_zscore_fcf_yield_252(arg_fcf, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_fcf_yield_ratio(arg_fcf, arg_marketcap), 252)

def f15_valuation_at_entry_zscore_fcf_yield_504(arg_fcf, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_fcf_yield_ratio(arg_fcf, arg_marketcap), 504)

def f15_valuation_at_entry_zscore_fcf_yield_756(arg_fcf, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_fcf_yield_ratio(arg_fcf, arg_marketcap), 756)

# 6. Earnings Yield (NetInc / MarketCap)
def f15_valuation_at_entry_earnings_yield_ratio(arg_netinc, arg_marketcap):
    return _val_ratio(arg_netinc, arg_marketcap)

def f15_valuation_at_entry_zscore_earnings_yield_63(arg_netinc, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_earnings_yield_ratio(arg_netinc, arg_marketcap), 63)

def f15_valuation_at_entry_zscore_earnings_yield_126(arg_netinc, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_earnings_yield_ratio(arg_netinc, arg_marketcap), 126)

def f15_valuation_at_entry_zscore_earnings_yield_252(arg_netinc, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_earnings_yield_ratio(arg_netinc, arg_marketcap), 252)

def f15_valuation_at_entry_zscore_earnings_yield_504(arg_netinc, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_earnings_yield_ratio(arg_netinc, arg_marketcap), 504)

def f15_valuation_at_entry_zscore_earnings_yield_756(arg_netinc, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_earnings_yield_ratio(arg_netinc, arg_marketcap), 756)

# 7. Sales Yield (Revenue / MarketCap)
def f15_valuation_at_entry_sales_yield_ratio(arg_revenue, arg_marketcap):
    return _val_ratio(arg_revenue, arg_marketcap)

def f15_valuation_at_entry_zscore_sales_yield_63(arg_revenue, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_sales_yield_ratio(arg_revenue, arg_marketcap), 63)

def f15_valuation_at_entry_zscore_sales_yield_126(arg_revenue, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_sales_yield_ratio(arg_revenue, arg_marketcap), 126)

def f15_valuation_at_entry_zscore_sales_yield_252(arg_revenue, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_sales_yield_ratio(arg_revenue, arg_marketcap), 252)

def f15_valuation_at_entry_zscore_sales_yield_504(arg_revenue, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_sales_yield_ratio(arg_revenue, arg_marketcap), 504)

def f15_valuation_at_entry_zscore_sales_yield_756(arg_revenue, arg_marketcap):
    return _val_zscore(f15_valuation_at_entry_sales_yield_ratio(arg_revenue, arg_marketcap), 756)

# 8. EV/Sales
def f15_valuation_at_entry_evs_ratio(arg_ev, arg_revenue):
    return _val_ratio(arg_ev, arg_revenue)

def f15_valuation_at_entry_zscore_evs_63(arg_ev, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_evs_ratio(arg_ev, arg_revenue), 63)

def f15_valuation_at_entry_zscore_evs_126(arg_ev, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_evs_ratio(arg_ev, arg_revenue), 126)

def f15_valuation_at_entry_zscore_evs_252(arg_ev, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_evs_ratio(arg_ev, arg_revenue), 252)

def f15_valuation_at_entry_zscore_evs_504(arg_ev, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_evs_ratio(arg_ev, arg_revenue), 504)

def f15_valuation_at_entry_zscore_evs_756(arg_ev, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_evs_ratio(arg_ev, arg_revenue), 756)

# 9. EV/FCF
def f15_valuation_at_entry_evfcf_ratio(arg_ev, arg_fcf):
    return _val_ratio(arg_ev, arg_fcf)

def f15_valuation_at_entry_zscore_evfcf_63(arg_ev, arg_fcf):
    return _val_zscore(f15_valuation_at_entry_evfcf_ratio(arg_ev, arg_fcf), 63)

def f15_valuation_at_entry_zscore_evfcf_126(arg_ev, arg_fcf):
    return _val_zscore(f15_valuation_at_entry_evfcf_ratio(arg_ev, arg_fcf), 126)

def f15_valuation_at_entry_zscore_evfcf_252(arg_ev, arg_fcf):
    return _val_zscore(f15_valuation_at_entry_evfcf_ratio(arg_ev, arg_fcf), 252)

def f15_valuation_at_entry_zscore_evfcf_504(arg_ev, arg_fcf):
    return _val_zscore(f15_valuation_at_entry_evfcf_ratio(arg_ev, arg_fcf), 504)

def f15_valuation_at_entry_zscore_evfcf_756(arg_ev, arg_fcf):
    return _val_zscore(f15_valuation_at_entry_evfcf_ratio(arg_ev, arg_fcf), 756)

# 10. MarketCap/EBITDA
def f15_valuation_at_entry_mcap_ebitda_ratio(arg_marketcap, arg_ebitda):
    return _val_ratio(arg_marketcap, arg_ebitda)

def f15_valuation_at_entry_zscore_mcap_ebitda_63(arg_marketcap, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_mcap_ebitda_ratio(arg_marketcap, arg_ebitda), 63)

def f15_valuation_at_entry_zscore_mcap_ebitda_126(arg_marketcap, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_mcap_ebitda_ratio(arg_marketcap, arg_ebitda), 126)

def f15_valuation_at_entry_zscore_mcap_ebitda_252(arg_marketcap, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_mcap_ebitda_ratio(arg_marketcap, arg_ebitda), 252)

def f15_valuation_at_entry_zscore_mcap_ebitda_504(arg_marketcap, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_mcap_ebitda_ratio(arg_marketcap, arg_ebitda), 504)

def f15_valuation_at_entry_zscore_mcap_ebitda_756(arg_marketcap, arg_ebitda):
    return _val_zscore(f15_valuation_at_entry_mcap_ebitda_ratio(arg_marketcap, arg_ebitda), 756)

# 11. EV/NetInc
def f15_valuation_at_entry_ev_netinc_ratio(arg_ev, arg_netinc):
    return _val_ratio(arg_ev, arg_netinc)

def f15_valuation_at_entry_zscore_ev_netinc_63(arg_ev, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_ev_netinc_ratio(arg_ev, arg_netinc), 63)

def f15_valuation_at_entry_zscore_ev_netinc_126(arg_ev, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_ev_netinc_ratio(arg_ev, arg_netinc), 126)

def f15_valuation_at_entry_zscore_ev_netinc_252(arg_ev, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_ev_netinc_ratio(arg_ev, arg_netinc), 252)

def f15_valuation_at_entry_zscore_ev_netinc_504(arg_ev, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_ev_netinc_ratio(arg_ev, arg_netinc), 504)

def f15_valuation_at_entry_zscore_ev_netinc_756(arg_ev, arg_netinc):
    return _val_zscore(f15_valuation_at_entry_ev_netinc_ratio(arg_ev, arg_netinc), 756)

# 12. EV/Equity
def f15_valuation_at_entry_ev_equity_ratio(arg_ev, arg_equity):
    return _val_ratio(arg_ev, arg_equity)

def f15_valuation_at_entry_zscore_ev_equity_63(arg_ev, arg_equity):
    return _val_zscore(f15_valuation_at_entry_ev_equity_ratio(arg_ev, arg_equity), 63)

def f15_valuation_at_entry_zscore_ev_equity_126(arg_ev, arg_equity):
    return _val_zscore(f15_valuation_at_entry_ev_equity_ratio(arg_ev, arg_equity), 126)

def f15_valuation_at_entry_zscore_ev_equity_252(arg_ev, arg_equity):
    return _val_zscore(f15_valuation_at_entry_ev_equity_ratio(arg_ev, arg_equity), 252)

def f15_valuation_at_entry_zscore_ev_equity_504(arg_ev, arg_equity):
    return _val_zscore(f15_valuation_at_entry_ev_equity_ratio(arg_ev, arg_equity), 504)

def f15_valuation_at_entry_zscore_ev_equity_756(arg_ev, arg_equity):
    return _val_zscore(f15_valuation_at_entry_ev_equity_ratio(arg_ev, arg_equity), 756)

# 13. ROE Val (NetInc / Equity) - Part 1 (3 features)
def f15_valuation_at_entry_roe_val_ratio(arg_netinc, arg_equity):
    return _val_ratio(arg_netinc, arg_equity)

def f15_valuation_at_entry_zscore_roe_val_63(arg_netinc, arg_equity):
    return _val_zscore(f15_valuation_at_entry_roe_val_ratio(arg_netinc, arg_equity), 63)

def f15_valuation_at_entry_zscore_roe_val_126(arg_netinc, arg_equity):
    return _val_zscore(f15_valuation_at_entry_roe_val_ratio(arg_netinc, arg_equity), 126)

def test_features():
    n = 1500
    data = {
        'marketcap': pd.Series(np.random.uniform(1e6, 1e9, n)),
        'ev': pd.Series(np.random.uniform(1e6, 1.2e9, n)),
        'netinc': pd.Series(np.random.uniform(1e5, 1e7, n)),
        'ebitda': pd.Series(np.random.uniform(2e5, 2e7, n)),
        'revenue': pd.Series(np.random.uniform(1e6, 1e8, n)),
        'equity': pd.Series(np.random.uniform(1e6, 5e8, n)),
        'fcf': pd.Series(np.random.uniform(5e4, 5e6, n)),
        'shareswa': pd.Series(np.random.uniform(1e5, 1e7, n)),
    }
    
    functions = [obj for name, obj in globals().items()
                 if (inspect.isfunction(obj) and name.startswith('f15_valuation_at_entry_'))]
    
    for func in functions:
        sig = inspect.signature(func)
        args = {param: data[param.replace('arg_', '')] for param in sig.parameters}
        res = func(**args)
        
        assert len(res) > 0, f"Function {func.__name__} returned empty result"
        assert res.nunique() > 2, f"Function {func.__name__} has too few unique values"
        assert res.std() > 0, f"Function {func.__name__} has zero standard deviation"

if __name__ == "__main__":
    test_features()
    print("All tests passed!")
