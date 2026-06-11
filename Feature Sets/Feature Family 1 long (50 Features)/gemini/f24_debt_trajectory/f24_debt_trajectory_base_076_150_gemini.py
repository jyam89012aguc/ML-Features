import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _dt_ratio(num, den):
    return num / den.replace(0, np.nan)

def _dt_cv(s, w):
    return _std(s, w) / _sma(s, w).abs().replace(0, np.nan)

def _dt_zscore(s, w):
    return _z(s, w)

# 63d average of Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_63d_base_v076_signal(liabilities, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_126d_base_v077_signal(liabilities, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_252d_base_v078_signal(liabilities, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_504d_base_v079_signal(liabilities, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_756d_base_v080_signal(liabilities, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Liabilities to EBITDA ratio for debt trajectory
def f24_debt_trajectory_liab_ebitda_1260d_base_v081_signal(liabilities, ebitda) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_63d_base_v082_signal(liabilities, revenue) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_126d_base_v083_signal(liabilities, revenue) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_252d_base_v084_signal(liabilities, revenue) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_504d_base_v085_signal(liabilities, revenue) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_756d_base_v086_signal(liabilities, revenue) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Liabilities to Revenue ratio for debt trajectory
def f24_debt_trajectory_liab_rev_1260d_base_v087_signal(liabilities, revenue) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_63d_base_v088_signal(liabilities, equity) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_126d_base_v089_signal(liabilities, equity) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_252d_base_v090_signal(liabilities, equity) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_504d_base_v091_signal(liabilities, equity) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_756d_base_v092_signal(liabilities, equity) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Liabilities to Equity ratio for debt trajectory
def f24_debt_trajectory_liab_equity_1260d_base_v093_signal(liabilities, equity) -> pd.Series:
    res = _sma(_dt_ratio(liabilities, equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d coefficient of variation of Debt for debt trajectory
def f24_debt_trajectory_debt_cv_63d_base_v094_signal(debt) -> pd.Series:
    res = _dt_cv(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d coefficient of variation of Debt for debt trajectory
def f24_debt_trajectory_debt_cv_126d_base_v095_signal(debt) -> pd.Series:
    res = _dt_cv(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d coefficient of variation of Debt for debt trajectory
def f24_debt_trajectory_debt_cv_252d_base_v096_signal(debt) -> pd.Series:
    res = _dt_cv(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d coefficient of variation of Debt for debt trajectory
def f24_debt_trajectory_debt_cv_504d_base_v097_signal(debt) -> pd.Series:
    res = _dt_cv(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d coefficient of variation of Debt for debt trajectory
def f24_debt_trajectory_debt_cv_756d_base_v098_signal(debt) -> pd.Series:
    res = _dt_cv(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d coefficient of variation of Debt for debt trajectory
def f24_debt_trajectory_debt_cv_1260d_base_v099_signal(debt) -> pd.Series:
    res = _dt_cv(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d coefficient of variation of Liabilities for debt trajectory
def f24_debt_trajectory_liab_cv_63d_base_v100_signal(liabilities) -> pd.Series:
    res = _dt_cv(liabilities, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d coefficient of variation of Liabilities for debt trajectory
def f24_debt_trajectory_liab_cv_126d_base_v101_signal(liabilities) -> pd.Series:
    res = _dt_cv(liabilities, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d coefficient of variation of Liabilities for debt trajectory
def f24_debt_trajectory_liab_cv_252d_base_v102_signal(liabilities) -> pd.Series:
    res = _dt_cv(liabilities, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d coefficient of variation of Liabilities for debt trajectory
def f24_debt_trajectory_liab_cv_504d_base_v103_signal(liabilities) -> pd.Series:
    res = _dt_cv(liabilities, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d coefficient of variation of Liabilities for debt trajectory
def f24_debt_trajectory_liab_cv_756d_base_v104_signal(liabilities) -> pd.Series:
    res = _dt_cv(liabilities, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d coefficient of variation of Liabilities for debt trajectory
def f24_debt_trajectory_liab_cv_1260d_base_v105_signal(liabilities) -> pd.Series:
    res = _dt_cv(liabilities, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d z-score of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_zscore_63d_base_v106_signal(liabilities, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d z-score of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_zscore_126d_base_v107_signal(liabilities, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_zscore_252d_base_v108_signal(liabilities, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_zscore_504d_base_v109_signal(liabilities, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_zscore_756d_base_v110_signal(liabilities, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of Liabilities to Assets ratio for debt trajectory
def f24_debt_trajectory_liab_assets_zscore_1260d_base_v111_signal(liabilities, assets) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_63d_base_v112_signal(currentratio) -> pd.Series:
    res = _sma(currentratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_126d_base_v113_signal(currentratio) -> pd.Series:
    res = _sma(currentratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_252d_base_v114_signal(currentratio) -> pd.Series:
    res = _sma(currentratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_504d_base_v115_signal(currentratio) -> pd.Series:
    res = _sma(currentratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_756d_base_v116_signal(currentratio) -> pd.Series:
    res = _sma(currentratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_1260d_base_v117_signal(currentratio) -> pd.Series:
    res = _sma(currentratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d z-score of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_zscore_63d_base_v118_signal(currentratio) -> pd.Series:
    res = _dt_zscore(currentratio, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d z-score of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_zscore_126d_base_v119_signal(currentratio) -> pd.Series:
    res = _dt_zscore(currentratio, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_zscore_252d_base_v120_signal(currentratio) -> pd.Series:
    res = _dt_zscore(currentratio, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_zscore_504d_base_v121_signal(currentratio) -> pd.Series:
    res = _dt_zscore(currentratio, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_zscore_756d_base_v122_signal(currentratio) -> pd.Series:
    res = _dt_zscore(currentratio, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of Current Ratio for debt trajectory
def f24_debt_trajectory_current_ratio_zscore_1260d_base_v123_signal(currentratio) -> pd.Series:
    res = _dt_zscore(currentratio, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_63d_base_v124_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_126d_base_v125_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_252d_base_v126_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_504d_base_v127_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_756d_base_v128_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Debt to Working Capital ratio for debt trajectory
def f24_debt_trajectory_debt_wc_1260d_base_v129_signal(debt, workingcapital) -> pd.Series:
    res = _sma(_dt_ratio(debt, workingcapital), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d z-score of Liabilities to Operating Income ratio for debt trajectory
def f24_debt_trajectory_liab_opinc_zscore_63d_base_v130_signal(liabilities, opinc) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, opinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d z-score of Liabilities to Operating Income ratio for debt trajectory
def f24_debt_trajectory_liab_opinc_zscore_126d_base_v131_signal(liabilities, opinc) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, opinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of Liabilities to Operating Income ratio for debt trajectory
def f24_debt_trajectory_liab_opinc_zscore_252d_base_v132_signal(liabilities, opinc) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, opinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of Liabilities to Operating Income ratio for debt trajectory
def f24_debt_trajectory_liab_opinc_zscore_504d_base_v133_signal(liabilities, opinc) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, opinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of Liabilities to Operating Income ratio for debt trajectory
def f24_debt_trajectory_liab_opinc_zscore_756d_base_v134_signal(liabilities, opinc) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, opinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of Liabilities to Operating Income ratio for debt trajectory
def f24_debt_trajectory_liab_opinc_zscore_1260d_base_v135_signal(liabilities, opinc) -> pd.Series:
    res = _dt_zscore(_dt_ratio(liabilities, opinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d average of Total Assets to Total Liabilities ratio for debt trajectory
def f24_debt_trajectory_assets_liab_63d_base_v136_signal(assets, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(assets, liabilities), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d average of Total Assets to Total Liabilities ratio for debt trajectory
def f24_debt_trajectory_assets_liab_126d_base_v137_signal(assets, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(assets, liabilities), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Total Assets to Total Liabilities ratio for debt trajectory
def f24_debt_trajectory_assets_liab_252d_base_v138_signal(assets, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(assets, liabilities), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Total Assets to Total Liabilities ratio for debt trajectory
def f24_debt_trajectory_assets_liab_504d_base_v139_signal(assets, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(assets, liabilities), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Total Assets to Total Liabilities ratio for debt trajectory
def f24_debt_trajectory_assets_liab_756d_base_v140_signal(assets, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(assets, liabilities), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d average of Total Assets to Total Liabilities ratio for debt trajectory
def f24_debt_trajectory_assets_liab_1260d_base_v141_signal(assets, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(assets, liabilities), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d z-score of EBITDA to Debt ratio for debt trajectory
def f24_debt_trajectory_ebitda_debt_zscore_63d_base_v142_signal(ebitda, debt) -> pd.Series:
    res = _dt_zscore(_dt_ratio(ebitda, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d z-score of EBITDA to Debt ratio for debt trajectory
def f24_debt_trajectory_ebitda_debt_zscore_126d_base_v143_signal(ebitda, debt) -> pd.Series:
    res = _dt_zscore(_dt_ratio(ebitda, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d z-score of EBITDA to Debt ratio for debt trajectory
def f24_debt_trajectory_ebitda_debt_zscore_252d_base_v144_signal(ebitda, debt) -> pd.Series:
    res = _dt_zscore(_dt_ratio(ebitda, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d z-score of EBITDA to Debt ratio for debt trajectory
def f24_debt_trajectory_ebitda_debt_zscore_504d_base_v145_signal(ebitda, debt) -> pd.Series:
    res = _dt_zscore(_dt_ratio(ebitda, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d z-score of EBITDA to Debt ratio for debt trajectory
def f24_debt_trajectory_ebitda_debt_zscore_756d_base_v146_signal(ebitda, debt) -> pd.Series:
    res = _dt_zscore(_dt_ratio(ebitda, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# 1260d z-score of EBITDA to Debt ratio for debt trajectory
def f24_debt_trajectory_ebitda_debt_zscore_1260d_base_v147_signal(ebitda, debt) -> pd.Series:
    res = _dt_zscore(_dt_ratio(ebitda, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d average of Operating Income to Liabilities ratio for debt trajectory
def f24_debt_trajectory_opinc_liab_252d_base_v148_signal(opinc, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(opinc, liabilities), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d average of Operating Income to Liabilities ratio for debt trajectory
def f24_debt_trajectory_opinc_liab_504d_base_v149_signal(opinc, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(opinc, liabilities), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 756d average of Operating Income to Liabilities ratio for debt trajectory
def f24_debt_trajectory_opinc_liab_756d_base_v150_signal(opinc, liabilities) -> pd.Series:
    res = _sma(_dt_ratio(opinc, liabilities), 756)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "liabilities": np.random.normal(200, 40, n),
        "ebitda": np.random.normal(50, 10, n),
        "revenue": np.random.normal(400, 40, n),
        "equity": np.random.normal(300, 30, n),
        "debt": np.random.normal(100, 20, n),
        "assets": np.random.normal(500, 50, n),
        "currentratio": np.random.normal(1.5, 0.3, n),
        "workingcapital": np.random.normal(100, 20, n),
        "opinc": np.random.normal(40, 8, n),
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f24_debt_trajectory_"))]
    
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
        assert any(prim in source for prim in ["_dt_ratio", "_dt_cv", "_dt_zscore"])

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f24_debt_trajectory_"))]}
F24_DEBT_TRAJECTORY_REGISTRY_076_150 = REGISTRY
