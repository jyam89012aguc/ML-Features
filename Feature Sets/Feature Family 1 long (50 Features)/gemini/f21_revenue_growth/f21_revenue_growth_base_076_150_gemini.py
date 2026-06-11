import pandas as pd
import numpy as np

def _rg_growth(s, w): return s.pct_change(w)
def _rg_zscore(s, w): return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)
def _rg_sma(s, w): return s.rolling(w, min_periods=1).mean()
def _rg_vol(s, w): return s.rolling(w, min_periods=1).std()

def f21_revenue_growth_sma_assets_growth_504d_base_v076_signal(arg_assets) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_756d_base_v077_signal(arg_assets) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_assets_growth_1260d_base_v078_signal(arg_assets) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_63d_base_v079_signal(arg_netinc) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_126d_base_v080_signal(arg_netinc) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_252d_base_v081_signal(arg_netinc) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_504d_base_v082_signal(arg_netinc) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_756d_base_v083_signal(arg_netinc) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_sma_netinc_growth_1260d_base_v084_signal(arg_netinc) -> pd.Series:
    res = _rg_sma(_rg_growth(arg_netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_63d_base_v085_signal(arg_revenue) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_126d_base_v086_signal(arg_revenue) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_252d_base_v087_signal(arg_revenue) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_504d_base_v088_signal(arg_revenue) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_756d_base_v089_signal(arg_revenue) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_rev_growth_1260d_base_v090_signal(arg_revenue) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_63d_base_v091_signal(arg_assets) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_126d_base_v092_signal(arg_assets) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_252d_base_v093_signal(arg_assets) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_504d_base_v094_signal(arg_assets) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_756d_base_v095_signal(arg_assets) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_assets_growth_1260d_base_v096_signal(arg_assets) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_63d_base_v097_signal(arg_netinc) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_126d_base_v098_signal(arg_netinc) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_252d_base_v099_signal(arg_netinc) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_504d_base_v100_signal(arg_netinc) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_756d_base_v101_signal(arg_netinc) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_vol_netinc_growth_1260d_base_v102_signal(arg_netinc) -> pd.Series:
    res = _rg_vol(_rg_growth(arg_netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_63d_base_v103_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue, 63) - _rg_growth(arg_assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_126d_base_v104_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue, 126) - _rg_growth(arg_assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_252d_base_v105_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue, 252) - _rg_growth(arg_assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_504d_base_v106_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue, 504) - _rg_growth(arg_assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_756d_base_v107_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue, 756) - _rg_growth(arg_assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_assets_growth_diff_1260d_base_v108_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue, 1260) - _rg_growth(arg_assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_63d_base_v109_signal(arg_revenue, arg_netinc) -> pd.Series:
    res = _rg_growth(arg_revenue, 63) - _rg_growth(arg_netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_126d_base_v110_signal(arg_revenue, arg_netinc) -> pd.Series:
    res = _rg_growth(arg_revenue, 126) - _rg_growth(arg_netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_252d_base_v111_signal(arg_revenue, arg_netinc) -> pd.Series:
    res = _rg_growth(arg_revenue, 252) - _rg_growth(arg_netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_504d_base_v112_signal(arg_revenue, arg_netinc) -> pd.Series:
    res = _rg_growth(arg_revenue, 504) - _rg_growth(arg_netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_756d_base_v113_signal(arg_revenue, arg_netinc) -> pd.Series:
    res = _rg_growth(arg_revenue, 756) - _rg_growth(arg_netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_vs_netinc_growth_diff_1260d_base_v114_signal(arg_revenue, arg_netinc) -> pd.Series:
    res = _rg_growth(arg_revenue, 1260) - _rg_growth(arg_netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_63d_base_v115_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc, 63) - _rg_growth(arg_assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_126d_base_v116_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc, 126) - _rg_growth(arg_assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_252d_base_v117_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc, 252) - _rg_growth(arg_assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_504d_base_v118_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc, 504) - _rg_growth(arg_assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_756d_base_v119_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc, 756) - _rg_growth(arg_assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_vs_assets_growth_diff_1260d_base_v120_signal(arg_netinc, arg_assets) -> pd.Series:
    res = _rg_growth(arg_netinc, 1260) - _rg_growth(arg_assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_63d_base_v121_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_126d_base_v122_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_252d_base_v123_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_504d_base_v124_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 504).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_756d_base_v125_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 756).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_growth_accel_1260d_base_v126_signal(arg_revenue) -> pd.Series:
    res = _rg_growth(arg_revenue, 1260).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_63d_base_v127_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_126d_base_v128_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_252d_base_v129_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_504d_base_v130_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 504).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_756d_base_v131_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 756).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_assets_growth_accel_1260d_base_v132_signal(arg_assets) -> pd.Series:
    res = _rg_growth(arg_assets, 1260).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_63d_base_v133_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_126d_base_v134_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_252d_base_v135_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_504d_base_v136_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 504).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_756d_base_v137_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 756).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_netinc_growth_accel_1260d_base_v138_signal(arg_netinc) -> pd.Series:
    res = _rg_growth(arg_netinc, 1260).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_63d_base_v139_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_126d_base_v140_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_252d_base_v141_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_504d_base_v142_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 504).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_756d_base_v143_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 756).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_per_share_growth_accel_1260d_base_v144_signal(arg_revenue, arg_shareswa) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_shareswa.replace(0, np.nan), 1260).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_63d_base_v145_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_126d_base_v146_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_252d_base_v147_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_504d_base_v148_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 504).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_756d_base_v149_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 756).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_revenue_growth_rev_assets_growth_accel_1260d_base_v150_signal(arg_revenue, arg_assets) -> pd.Series:
    res = _rg_growth(arg_revenue / arg_assets.replace(0, np.nan), 1260).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_revenue", "arg_assets", "arg_netinc", "arg_shareswa"]}

F21_REVENUE_GROWTH_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted([f for f in globals() if f.startswith('f21_revenue_growth_') and f.endswith('_signal')])
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 5000
    np.random.seed(42)
    steps = 20
    step_size = sz // steps
    base_rev = np.repeat(np.random.lognormal(10, 1, steps), step_size)
    if len(base_rev) < sz:
        base_rev = np.concatenate([base_rev, [base_rev[-1]] * (sz - len(base_rev))])
    
    d = pd.DataFrame({
        "arg_revenue": pd.Series(base_rev * (1 + np.random.normal(0, 0.05, sz))),
        "arg_assets": pd.Series(base_rev * np.random.uniform(0.5, 2.0, sz)),
        "arg_netinc": pd.Series(base_rev * np.random.uniform(-0.1, 0.2, sz)),
        "arg_shareswa": pd.Series(np.ones(sz) * 1e6),
        "ticker": ["T"]*sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in F21_REVENUE_GROWTH_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
        assert r.std() > 0, f"{n} failed std: {r.std()}"
    print(f"OK")
