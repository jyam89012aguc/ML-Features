import pandas as pd
import numpy as np
import inspect

def _ri_ratio(num, den): return num / den.replace(0, np.nan)
def _ri_zscore(s, w): return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

def f18ri_sgn_shr_zscore_756d_base_v076_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_zscore(ratio, 756)

def f18ri_sgn_shr_zscore_1260d_base_v077_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_zscore(ratio, 1260)

def f18ri_sgn_shr_mean_rel_252d_base_v078_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_sgn_shr_mean_rel_756d_base_v079_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_sgn_shr_mean_rel_1260d_base_v080_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_int_shr_raw_base_v081_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return ratio

def f18ri_int_shr_zscore_63d_base_v082_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_zscore(ratio, 63)

def f18ri_int_shr_zscore_126d_base_v083_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_zscore(ratio, 126)

def f18ri_int_shr_zscore_252d_base_v084_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_zscore(ratio, 252)

def f18ri_int_shr_zscore_504d_base_v085_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_zscore(ratio, 504)

def f18ri_int_shr_zscore_756d_base_v086_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_zscore(ratio, 756)

def f18ri_int_shr_zscore_1260d_base_v087_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_zscore(ratio, 1260)

def f18ri_int_shr_mean_rel_252d_base_v088_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_int_shr_mean_rel_756d_base_v089_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_int_shr_mean_rel_1260d_base_v090_signal(arg_intangibles: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_opinv_rev_raw_base_v091_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return ratio

def f18ri_opinv_rev_zscore_63d_base_v092_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_zscore(ratio, 63)

def f18ri_opinv_rev_zscore_126d_base_v093_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_zscore(ratio, 126)

def f18ri_opinv_rev_zscore_252d_base_v094_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_zscore(ratio, 252)

def f18ri_opinv_rev_zscore_504d_base_v095_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_zscore(ratio, 504)

def f18ri_opinv_rev_zscore_756d_base_v096_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_zscore(ratio, 756)

def f18ri_opinv_rev_zscore_1260d_base_v097_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_zscore(ratio, 1260)

def f18ri_opinv_rev_mean_rel_252d_base_v098_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_opinv_rev_mean_rel_756d_base_v099_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_opinv_rev_mean_rel_1260d_base_v100_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_opinv_ast_raw_base_v101_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return ratio

def f18ri_opinv_ast_zscore_63d_base_v102_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_zscore(ratio, 63)

def f18ri_opinv_ast_zscore_126d_base_v103_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_zscore(ratio, 126)

def f18ri_opinv_ast_zscore_252d_base_v104_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_zscore(ratio, 252)

def f18ri_opinv_ast_zscore_504d_base_v105_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_zscore(ratio, 504)

def f18ri_opinv_ast_zscore_756d_base_v106_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_zscore(ratio, 756)

def f18ri_opinv_ast_zscore_1260d_base_v107_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_zscore(ratio, 1260)

def f18ri_opinv_ast_mean_rel_252d_base_v108_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_opinv_ast_mean_rel_756d_base_v109_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_opinv_ast_mean_rel_1260d_base_v110_signal(arg_rnd: pd.Series, arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio((arg_rnd + arg_sgna), arg_assets)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_rnd_opinv_raw_base_v111_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return ratio

def f18ri_rnd_opinv_zscore_63d_base_v112_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_zscore(ratio, 63)

def f18ri_rnd_opinv_zscore_126d_base_v113_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_zscore(ratio, 126)

def f18ri_rnd_opinv_zscore_252d_base_v114_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_zscore(ratio, 252)

def f18ri_rnd_opinv_zscore_504d_base_v115_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_zscore(ratio, 504)

def f18ri_rnd_opinv_zscore_756d_base_v116_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_zscore(ratio, 756)

def f18ri_rnd_opinv_zscore_1260d_base_v117_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_zscore(ratio, 1260)

def f18ri_rnd_opinv_mean_rel_252d_base_v118_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_rnd_opinv_mean_rel_756d_base_v119_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_rnd_opinv_mean_rel_1260d_base_v120_signal(arg_rnd: pd.Series, arg_sgna: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, (arg_rnd + arg_sgna))
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_roa_raw_base_v121_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return ratio

def f18ri_roa_zscore_63d_base_v122_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_zscore(ratio, 63)

def f18ri_roa_zscore_126d_base_v123_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_zscore(ratio, 126)

def f18ri_roa_zscore_252d_base_v124_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_zscore(ratio, 252)

def f18ri_roa_zscore_504d_base_v125_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_zscore(ratio, 504)

def f18ri_roa_zscore_756d_base_v126_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_zscore(ratio, 756)

def f18ri_roa_zscore_1260d_base_v127_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_zscore(ratio, 1260)

def f18ri_roa_mean_rel_252d_base_v128_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_roa_mean_rel_756d_base_v129_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_roa_mean_rel_1260d_base_v130_signal(arg_assets: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_margin_raw_base_v131_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return ratio

def f18ri_margin_zscore_63d_base_v132_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_zscore(ratio, 63)

def f18ri_margin_zscore_126d_base_v133_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_zscore(ratio, 126)

def f18ri_margin_zscore_252d_base_v134_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_zscore(ratio, 252)

def f18ri_margin_zscore_504d_base_v135_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_zscore(ratio, 504)

def f18ri_margin_zscore_756d_base_v136_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_zscore(ratio, 756)

def f18ri_margin_zscore_1260d_base_v137_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_zscore(ratio, 1260)

def f18ri_margin_mean_rel_252d_base_v138_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_margin_mean_rel_756d_base_v139_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_margin_mean_rel_1260d_base_v140_signal(arg_revenue: pd.Series, arg_netinc: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_netinc, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_int_tang_raw_base_v141_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return ratio

def f18ri_int_tang_zscore_63d_base_v142_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_zscore(ratio, 63)

def f18ri_int_tang_zscore_126d_base_v143_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_zscore(ratio, 126)

def f18ri_int_tang_zscore_252d_base_v144_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_zscore(ratio, 252)

def f18ri_int_tang_zscore_504d_base_v145_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_zscore(ratio, 504)

def f18ri_int_tang_zscore_756d_base_v146_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_zscore(ratio, 756)

def f18ri_int_tang_zscore_1260d_base_v147_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_zscore(ratio, 1260)

def f18ri_int_tang_mean_rel_252d_base_v148_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_int_tang_mean_rel_756d_base_v149_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_int_tang_mean_rel_1260d_base_v150_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, (arg_assets - arg_intangibles))
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {
    "rnd": "sep.rnd", "sgna": "sep.sgna", "intangibles": "sep.intangibles", 
    "revenue": "sep.revenue", "assets": "sep.assets", "netinc": "sep.netinc", "shareswa": "sep.shareswa"
}

f18ri_NAMES = [f for f in globals() if f.startswith("f18ri_") and f.endswith("_signal")]

f18ri_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v.replace("arg_", "") for v in inspect.signature(globals()[n]).parameters]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(f18ri_NAMES)
}

if __name__ == "__main__":
    sz = 1500
    d = pd.DataFrame({
        "arg_rnd": np.random.rand(sz) * 100,
        "arg_sgna": np.random.rand(sz) * 200,
        "arg_intangibles": np.random.rand(sz) * 500,
        "arg_revenue": np.random.rand(sz) * 1000 + 100,
        "arg_assets": np.random.rand(sz) * 2000 + 500,
        "arg_netinc": np.random.randn(sz) * 50,
        "arg_shareswa": np.random.rand(sz) * 100 + 10,
        "ticker": ["T"] * sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in f18ri_BASE_REGISTRY_076_150.items():
        # Mapping arg_ names to the synthetic data
        res = c["func"](**{f"arg_{i}": d[f"arg_{i}"] for i in c["inputs"]})
        assert isinstance(res, pd.Series)
        assert len(res) > 0
        if res.nunique() <= 2:
             print(f"Warning: {n} has low nunique: {res.nunique()}")
        if res.std() <= 0:
             # Some raw ratios might have 0 std if data is constant, but synthetic is random
             assert res.std() > 0 or res.nunique() == 1
    print("OK")

