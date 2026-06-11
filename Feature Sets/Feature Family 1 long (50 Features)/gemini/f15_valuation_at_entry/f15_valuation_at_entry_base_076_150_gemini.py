import pandas as pd
import numpy as np
import inspect

def _val_ratio(num, den):
    return num / den.replace(0, np.nan)

def _val_zscore(s, w):
    return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

# Ratio Groups 13 (part 2) + 14-25 (72 features) = 75 features

# 13. ROE Val (NetInc / Equity) - Part 2 (3 features)
def f15_valuation_at_entry_roe_val_ratio(arg_netinc, arg_equity):
    return _val_ratio(arg_netinc, arg_equity)

def f15_valuation_at_entry_zscore_roe_val_252(arg_netinc, arg_equity):
    return _val_zscore(f15_valuation_at_entry_roe_val_ratio(arg_netinc, arg_equity), 252)

def f15_valuation_at_entry_zscore_roe_val_504(arg_netinc, arg_equity):
    return _val_zscore(f15_valuation_at_entry_roe_val_ratio(arg_netinc, arg_equity), 504)

def f15_valuation_at_entry_zscore_roe_val_756(arg_netinc, arg_equity):
    return _val_zscore(f15_valuation_at_entry_roe_val_ratio(arg_netinc, arg_equity), 756)

# 14. FCF/Equity
def f15_valuation_at_entry_fcf_equity_ratio(arg_fcf, arg_equity):
    return _val_ratio(arg_fcf, arg_equity)

def f15_valuation_at_entry_zscore_fcf_equity_63(arg_fcf, arg_equity):
    return _val_zscore(f15_valuation_at_entry_fcf_equity_ratio(arg_fcf, arg_equity), 63)

def f15_valuation_at_entry_zscore_fcf_equity_126(arg_fcf, arg_equity):
    return _val_zscore(f15_valuation_at_entry_fcf_equity_ratio(arg_fcf, arg_equity), 126)

def f15_valuation_at_entry_zscore_fcf_equity_252(arg_fcf, arg_equity):
    return _val_zscore(f15_valuation_at_entry_fcf_equity_ratio(arg_fcf, arg_equity), 252)

def f15_valuation_at_entry_zscore_fcf_equity_504(arg_fcf, arg_equity):
    return _val_zscore(f15_valuation_at_entry_fcf_equity_ratio(arg_fcf, arg_equity), 504)

def f15_valuation_at_entry_zscore_fcf_equity_756(arg_fcf, arg_equity):
    return _val_zscore(f15_valuation_at_entry_fcf_equity_ratio(arg_fcf, arg_equity), 756)

# 15. EBITDA Margin (Valuation Context: EBITDA / Revenue)
def f15_valuation_at_entry_ebitda_margin_ratio(arg_ebitda, arg_revenue):
    return _val_ratio(arg_ebitda, arg_revenue)

def f15_valuation_at_entry_zscore_ebitda_margin_63(arg_ebitda, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ebitda_margin_ratio(arg_ebitda, arg_revenue), 63)

def f15_valuation_at_entry_zscore_ebitda_margin_126(arg_ebitda, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ebitda_margin_ratio(arg_ebitda, arg_revenue), 126)

def f15_valuation_at_entry_zscore_ebitda_margin_252(arg_ebitda, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ebitda_margin_ratio(arg_ebitda, arg_revenue), 252)

def f15_valuation_at_entry_zscore_ebitda_margin_504(arg_ebitda, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ebitda_margin_ratio(arg_ebitda, arg_revenue), 504)

def f15_valuation_at_entry_zscore_ebitda_margin_756(arg_ebitda, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_ebitda_margin_ratio(arg_ebitda, arg_revenue), 756)

# 16. NetInc Margin
def f15_valuation_at_entry_netinc_margin_ratio(arg_netinc, arg_revenue):
    return _val_ratio(arg_netinc, arg_revenue)

def f15_valuation_at_entry_zscore_netinc_margin_63(arg_netinc, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_netinc_margin_ratio(arg_netinc, arg_revenue), 63)

def f15_valuation_at_entry_zscore_netinc_margin_126(arg_netinc, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_netinc_margin_ratio(arg_netinc, arg_revenue), 126)

def f15_valuation_at_entry_zscore_netinc_margin_252(arg_netinc, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_netinc_margin_ratio(arg_netinc, arg_revenue), 252)

def f15_valuation_at_entry_zscore_netinc_margin_504(arg_netinc, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_netinc_margin_ratio(arg_netinc, arg_revenue), 504)

def f15_valuation_at_entry_zscore_netinc_margin_756(arg_netinc, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_netinc_margin_ratio(arg_netinc, arg_revenue), 756)

# 17. FCF Margin
def f15_valuation_at_entry_fcf_margin_ratio(arg_fcf, arg_revenue):
    return _val_ratio(arg_fcf, arg_revenue)

def f15_valuation_at_entry_zscore_fcf_margin_63(arg_fcf, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_fcf_margin_ratio(arg_fcf, arg_revenue), 63)

def f15_valuation_at_entry_zscore_fcf_margin_126(arg_fcf, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_fcf_margin_ratio(arg_fcf, arg_revenue), 126)

def f15_valuation_at_entry_zscore_fcf_margin_252(arg_fcf, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_fcf_margin_ratio(arg_fcf, arg_revenue), 252)

def f15_valuation_at_entry_zscore_fcf_margin_504(arg_fcf, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_fcf_margin_ratio(arg_fcf, arg_revenue), 504)

def f15_valuation_at_entry_zscore_fcf_margin_756(arg_fcf, arg_revenue):
    return _val_zscore(f15_valuation_at_entry_fcf_margin_ratio(arg_fcf, arg_revenue), 756)

# 18. Price (MarketCap / SharesWA)
def f15_valuation_at_entry_price_ratio(arg_marketcap, arg_shareswa):
    return _val_ratio(arg_marketcap, arg_shareswa)

def f15_valuation_at_entry_zscore_price_63(arg_marketcap, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_price_ratio(arg_marketcap, arg_shareswa), 63)

def f15_valuation_at_entry_zscore_price_126(arg_marketcap, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_price_ratio(arg_marketcap, arg_shareswa), 126)

def f15_valuation_at_entry_zscore_price_252(arg_marketcap, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_price_ratio(arg_marketcap, arg_shareswa), 252)

def f15_valuation_at_entry_zscore_price_504(arg_marketcap, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_price_ratio(arg_marketcap, arg_shareswa), 504)

def f15_valuation_at_entry_zscore_price_756(arg_marketcap, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_price_ratio(arg_marketcap, arg_shareswa), 756)

# 19. EV Per Share
def f15_valuation_at_entry_ev_per_share_ratio(arg_ev, arg_shareswa):
    return _val_ratio(arg_ev, arg_shareswa)

def f15_valuation_at_entry_zscore_ev_per_share_63(arg_ev, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ev_per_share_ratio(arg_ev, arg_shareswa), 63)

def f15_valuation_at_entry_zscore_ev_per_share_126(arg_ev, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ev_per_share_ratio(arg_ev, arg_shareswa), 126)

def f15_valuation_at_entry_zscore_ev_per_share_252(arg_ev, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ev_per_share_ratio(arg_ev, arg_shareswa), 252)

def f15_valuation_at_entry_zscore_ev_per_share_504(arg_ev, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ev_per_share_ratio(arg_ev, arg_shareswa), 504)

def f15_valuation_at_entry_zscore_ev_per_share_756(arg_ev, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ev_per_share_ratio(arg_ev, arg_shareswa), 756)

# 20. BVPS (Equity / SharesWA)
def f15_valuation_at_entry_bvps_ratio(arg_equity, arg_shareswa):
    return _val_ratio(arg_equity, arg_shareswa)

def f15_valuation_at_entry_zscore_bvps_63(arg_equity, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_bvps_ratio(arg_equity, arg_shareswa), 63)

def f15_valuation_at_entry_zscore_bvps_126(arg_equity, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_bvps_ratio(arg_equity, arg_shareswa), 126)

def f15_valuation_at_entry_zscore_bvps_252(arg_equity, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_bvps_ratio(arg_equity, arg_shareswa), 252)

def f15_valuation_at_entry_zscore_bvps_504(arg_equity, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_bvps_ratio(arg_equity, arg_shareswa), 504)

def f15_valuation_at_entry_zscore_bvps_756(arg_equity, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_bvps_ratio(arg_equity, arg_shareswa), 756)

# 21. EPS (NetInc / SharesWA)
def f15_valuation_at_entry_eps_ratio(arg_netinc, arg_shareswa):
    return _val_ratio(arg_netinc, arg_shareswa)

def f15_valuation_at_entry_zscore_eps_63(arg_netinc, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_eps_ratio(arg_netinc, arg_shareswa), 63)

def f15_valuation_at_entry_zscore_eps_126(arg_netinc, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_eps_ratio(arg_netinc, arg_shareswa), 126)

def f15_valuation_at_entry_zscore_eps_252(arg_netinc, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_eps_ratio(arg_netinc, arg_shareswa), 252)

def f15_valuation_at_entry_zscore_eps_504(arg_netinc, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_eps_ratio(arg_netinc, arg_shareswa), 504)

def f15_valuation_at_entry_zscore_eps_756(arg_netinc, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_eps_ratio(arg_netinc, arg_shareswa), 756)

# 22. FCF Per Share
def f15_valuation_at_entry_fcf_per_share_ratio(arg_fcf, arg_shareswa):
    return _val_ratio(arg_fcf, arg_shareswa)

def f15_valuation_at_entry_zscore_fcf_per_share_63(arg_fcf, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_fcf_per_share_ratio(arg_fcf, arg_shareswa), 63)

def f15_valuation_at_entry_zscore_fcf_per_share_126(arg_fcf, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_fcf_per_share_ratio(arg_fcf, arg_shareswa), 126)

def f15_valuation_at_entry_zscore_fcf_per_share_252(arg_fcf, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_fcf_per_share_ratio(arg_fcf, arg_shareswa), 252)

def f15_valuation_at_entry_zscore_fcf_per_share_504(arg_fcf, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_fcf_per_share_ratio(arg_fcf, arg_shareswa), 504)

def f15_valuation_at_entry_zscore_fcf_per_share_756(arg_fcf, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_fcf_per_share_ratio(arg_fcf, arg_shareswa), 756)

# 23. Rev Per Share
def f15_valuation_at_entry_rev_per_share_ratio(arg_revenue, arg_shareswa):
    return _val_ratio(arg_revenue, arg_shareswa)

def f15_valuation_at_entry_zscore_rev_per_share_63(arg_revenue, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_rev_per_share_ratio(arg_revenue, arg_shareswa), 63)

def f15_valuation_at_entry_zscore_rev_per_share_126(arg_revenue, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_rev_per_share_ratio(arg_revenue, arg_shareswa), 126)

def f15_valuation_at_entry_zscore_rev_per_share_252(arg_revenue, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_rev_per_share_ratio(arg_revenue, arg_shareswa), 252)

def f15_valuation_at_entry_zscore_rev_per_share_504(arg_revenue, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_rev_per_share_ratio(arg_revenue, arg_shareswa), 504)

def f15_valuation_at_entry_zscore_rev_per_share_756(arg_revenue, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_rev_per_share_ratio(arg_revenue, arg_shareswa), 756)

# 24. EBITDA Per Share
def f15_valuation_at_entry_ebitda_per_share_ratio(arg_ebitda, arg_shareswa):
    return _val_ratio(arg_ebitda, arg_shareswa)

def f15_valuation_at_entry_zscore_ebitda_per_share_63(arg_ebitda, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ebitda_per_share_ratio(arg_ebitda, arg_shareswa), 63)

def f15_valuation_at_entry_zscore_ebitda_per_share_126(arg_ebitda, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ebitda_per_share_ratio(arg_ebitda, arg_shareswa), 126)

def f15_valuation_at_entry_zscore_ebitda_per_share_252(arg_ebitda, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ebitda_per_share_ratio(arg_ebitda, arg_shareswa), 252)

def f15_valuation_at_entry_zscore_ebitda_per_share_504(arg_ebitda, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ebitda_per_share_ratio(arg_ebitda, arg_shareswa), 504)

def f15_valuation_at_entry_zscore_ebitda_per_share_756(arg_ebitda, arg_shareswa):
    return _val_zscore(f15_valuation_at_entry_ebitda_per_share_ratio(arg_ebitda, arg_shareswa), 756)

# 25. MarketCap / EV Ratio
def f15_valuation_at_entry_mcap_ev_ratio(arg_marketcap, arg_ev):
    return _val_ratio(arg_marketcap, arg_ev)

def f15_valuation_at_entry_zscore_mcap_ev_63(arg_marketcap, arg_ev):
    return _val_zscore(f15_valuation_at_entry_mcap_ev_ratio(arg_marketcap, arg_ev), 63)

def f15_valuation_at_entry_zscore_mcap_ev_126(arg_marketcap, arg_ev):
    return _val_zscore(f15_valuation_at_entry_mcap_ev_ratio(arg_marketcap, arg_ev), 126)

def f15_valuation_at_entry_zscore_mcap_ev_252(arg_marketcap, arg_ev):
    return _val_zscore(f15_valuation_at_entry_mcap_ev_ratio(arg_marketcap, arg_ev), 252)

def f15_valuation_at_entry_zscore_mcap_ev_504(arg_marketcap, arg_ev):
    return _val_zscore(f15_valuation_at_entry_mcap_ev_ratio(arg_marketcap, arg_ev), 504)

def f15_valuation_at_entry_zscore_mcap_ev_756(arg_marketcap, arg_ev):
    return _val_zscore(f15_valuation_at_entry_mcap_ev_ratio(arg_marketcap, arg_ev), 756)

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
