import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _cft_ratio(num, den):
    return num / den.replace(0, np.nan)

def _cft_cv(s, w):
    return _std(s, w) / _sma(s, w).abs().replace(0, np.nan)

def _cft_zscore(s, w):
    return _z(s, w)

# 63d average of FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_63d_base_v076_signal(fcf, equity) -> pd.Series:
    res = _sma(_cft_ratio(fcf, equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_126d_base_v077_signal(fcf, equity) -> pd.Series:
    res = _sma(_cft_ratio(fcf, equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_252d_base_v078_signal(fcf, equity) -> pd.Series:
    res = _sma(_cft_ratio(fcf, equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_504d_base_v079_signal(fcf, equity) -> pd.Series:
    res = _sma(_cft_ratio(fcf, equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_756d_base_v080_signal(fcf, equity) -> pd.Series:
    res = _sma(_cft_ratio(fcf, equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of FCF to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_equity_1260d_base_v081_signal(fcf, equity) -> pd.Series:
    res = _sma(_cft_ratio(fcf, equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_63d_base_v082_signal(ncfo, equity) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_126d_base_v083_signal(ncfo, equity) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_252d_base_v084_signal(ncfo, equity) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_504d_base_v085_signal(ncfo, equity) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_756d_base_v086_signal(ncfo, equity) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of NCFO to Equity ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_equity_1260d_base_v087_signal(ncfo, equity) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_63d_base_v088_signal(fcf, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(fcf, liabilities), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_126d_base_v089_signal(fcf, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(fcf, liabilities), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_252d_base_v090_signal(fcf, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(fcf, liabilities), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_504d_base_v091_signal(fcf, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(fcf, liabilities), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_756d_base_v092_signal(fcf, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(fcf, liabilities), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of FCF to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_liab_1260d_base_v093_signal(fcf, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(fcf, liabilities), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_63d_base_v094_signal(ncfo, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, liabilities), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_126d_base_v095_signal(ncfo, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, liabilities), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_252d_base_v096_signal(ncfo, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, liabilities), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_504d_base_v097_signal(ncfo, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, liabilities), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_756d_base_v098_signal(ncfo, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, liabilities), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of NCFO to Liabilities ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_liab_1260d_base_v099_signal(ncfo, liabilities) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, liabilities), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_63d_base_v100_signal(fcf, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(fcf, workingcapital), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_126d_base_v101_signal(fcf, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(fcf, workingcapital), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_252d_base_v102_signal(fcf, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(fcf, workingcapital), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_504d_base_v103_signal(fcf, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(fcf, workingcapital), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_756d_base_v104_signal(fcf, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(fcf, workingcapital), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of FCF to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_wc_1260d_base_v105_signal(fcf, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(fcf, workingcapital), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_63d_base_v106_signal(ncfo, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, workingcapital), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_126d_base_v107_signal(ncfo, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, workingcapital), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_252d_base_v108_signal(ncfo, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, workingcapital), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_504d_base_v109_signal(ncfo, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, workingcapital), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_756d_base_v110_signal(ncfo, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, workingcapital), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of NCFO to Working Capital ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_wc_1260d_base_v111_signal(ncfo, workingcapital) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, workingcapital), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d coefficient of variation of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_63d_base_v112_signal(fcf) -> pd.Series:
    res = _cft_cv(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d coefficient of variation of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_126d_base_v113_signal(fcf) -> pd.Series:
    res = _cft_cv(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d coefficient of variation of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_252d_base_v114_signal(fcf) -> pd.Series:
    res = _cft_cv(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d coefficient of variation of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_504d_base_v115_signal(fcf) -> pd.Series:
    res = _cft_cv(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d coefficient of variation of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_756d_base_v116_signal(fcf) -> pd.Series:
    res = _cft_cv(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d coefficient of variation of FCF for cash flow trajectory
def f23_cash_flow_trajectory_fcf_cv_1260d_base_v117_signal(fcf) -> pd.Series:
    res = _cft_cv(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d coefficient of variation of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_63d_base_v118_signal(ncfo) -> pd.Series:
    res = _cft_cv(ncfo, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d coefficient of variation of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_126d_base_v119_signal(ncfo) -> pd.Series:
    res = _cft_cv(ncfo, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d coefficient of variation of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_252d_base_v120_signal(ncfo) -> pd.Series:
    res = _cft_cv(ncfo, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d coefficient of variation of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_504d_base_v121_signal(ncfo) -> pd.Series:
    res = _cft_cv(ncfo, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d coefficient of variation of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_756d_base_v122_signal(ncfo) -> pd.Series:
    res = _cft_cv(ncfo, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d coefficient of variation of NCFO for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_cv_1260d_base_v123_signal(ncfo) -> pd.Series:
    res = _cft_cv(ncfo, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d z-score of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_63d_base_v124_signal(fcf, netinc) -> pd.Series:
    res = _cft_zscore(_cft_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d z-score of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_126d_base_v125_signal(fcf, netinc) -> pd.Series:
    res = _cft_zscore(_cft_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_252d_base_v126_signal(fcf, netinc) -> pd.Series:
    res = _cft_zscore(_cft_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_504d_base_v127_signal(fcf, netinc) -> pd.Series:
    res = _cft_zscore(_cft_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_756d_base_v128_signal(fcf, netinc) -> pd.Series:
    res = _cft_zscore(_cft_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of FCF to Net Income ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_netinc_zscore_1260d_base_v129_signal(fcf, netinc) -> pd.Series:
    res = _cft_zscore(_cft_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d z-score of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_63d_base_v130_signal(ncfo, revenue) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d z-score of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_126d_base_v131_signal(ncfo, revenue) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_252d_base_v132_signal(ncfo, revenue) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_504d_base_v133_signal(ncfo, revenue) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_756d_base_v134_signal(ncfo, revenue) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of NCFO to Revenue ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_rev_zscore_1260d_base_v135_signal(ncfo, revenue) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_63d_base_v136_signal(fcf, capex) -> pd.Series:
    res = _sma(_cft_ratio(fcf, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_126d_base_v137_signal(fcf, capex) -> pd.Series:
    res = _sma(_cft_ratio(fcf, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_252d_base_v138_signal(fcf, capex) -> pd.Series:
    res = _sma(_cft_ratio(fcf, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_504d_base_v139_signal(fcf, capex) -> pd.Series:
    res = _sma(_cft_ratio(fcf, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_756d_base_v140_signal(fcf, capex) -> pd.Series:
    res = _sma(_cft_ratio(fcf, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of FCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_fcf_capex_1260d_base_v141_signal(fcf, capex) -> pd.Series:
    res = _sma(_cft_ratio(fcf, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_252d_base_v142_signal(ncfo, capex) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_504d_base_v143_signal(ncfo, capex) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_756d_base_v144_signal(ncfo, capex) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_1260d_base_v145_signal(ncfo, capex) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_zscore_252d_base_v146_signal(ncfo, capex) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_zscore_504d_base_v147_signal(ncfo, capex) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_zscore_756d_base_v148_signal(ncfo, capex) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of OCF to Capex ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_capex_zscore_1260d_base_v149_signal(ncfo, capex) -> pd.Series:
    res = _cft_zscore(_cft_ratio(ncfo, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of NCFO to NCFI ratio for cash flow trajectory
def f23_cash_flow_trajectory_ncfo_ncfi_252d_base_v150_signal(ncfo, ncfi) -> pd.Series:
    res = _sma(_cft_ratio(ncfo, ncfi), 252)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "fcf": np.random.normal(10, 2, n),
        "ncfo": np.random.normal(15, 3, n),
        "equity": np.random.normal(300, 30, n),
        "liabilities": np.random.normal(200, 20, n),
        "workingcapital": np.random.normal(50, 10, n),
        "netinc": np.random.normal(8, 2, n),
        "revenue": np.random.normal(100, 10, n),
        "capex": np.random.normal(5, 1, n),
        "ncfi": np.random.normal(-5, 1, n),
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f23_cash_flow_trajectory_"))]
    
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        
        source = inspect.getsource(func)
        assert any(prim in source for prim in ["_cft_ratio", "_cft_cv", "_cft_zscore"])

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f23_cash_flow_trajectory_"))]}
F23_CASH_FLOW_TRAJECTORY_REGISTRY_076_150 = REGISTRY
