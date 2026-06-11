import pandas as pd
import numpy as np
import inspect

def _ri_ratio(num, den): return num / den.replace(0, np.nan)
def _ri_zscore(s, w): return (s - s.rolling(w, min_periods=1).mean()) / s.rolling(w, min_periods=1).std().replace(0, np.nan)

def f18ri_rnd_rev_raw_base_v001_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return ratio

def f18ri_rnd_rev_zscore_63d_base_v002_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_zscore(ratio, 63)

def f18ri_rnd_rev_zscore_126d_base_v003_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_zscore(ratio, 126)

def f18ri_rnd_rev_zscore_252d_base_v004_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_zscore(ratio, 252)

def f18ri_rnd_rev_zscore_504d_base_v005_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_zscore(ratio, 504)

def f18ri_rnd_rev_zscore_756d_base_v006_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_zscore(ratio, 756)

def f18ri_rnd_rev_zscore_1260d_base_v007_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_zscore(ratio, 1260)

def f18ri_rnd_rev_mean_rel_252d_base_v008_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_rnd_rev_mean_rel_756d_base_v009_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_rnd_rev_mean_rel_1260d_base_v010_signal(arg_rnd: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_rnd_ast_raw_base_v011_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return ratio

def f18ri_rnd_ast_zscore_63d_base_v012_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_zscore(ratio, 63)

def f18ri_rnd_ast_zscore_126d_base_v013_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_zscore(ratio, 126)

def f18ri_rnd_ast_zscore_252d_base_v014_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_zscore(ratio, 252)

def f18ri_rnd_ast_zscore_504d_base_v015_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_zscore(ratio, 504)

def f18ri_rnd_ast_zscore_756d_base_v016_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_zscore(ratio, 756)

def f18ri_rnd_ast_zscore_1260d_base_v017_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_zscore(ratio, 1260)

def f18ri_rnd_ast_mean_rel_252d_base_v018_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_rnd_ast_mean_rel_756d_base_v019_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_rnd_ast_mean_rel_1260d_base_v020_signal(arg_rnd: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_sgn_rev_raw_base_v021_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return ratio

def f18ri_sgn_rev_zscore_63d_base_v022_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_zscore(ratio, 63)

def f18ri_sgn_rev_zscore_126d_base_v023_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_zscore(ratio, 126)

def f18ri_sgn_rev_zscore_252d_base_v024_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_zscore(ratio, 252)

def f18ri_sgn_rev_zscore_504d_base_v025_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_zscore(ratio, 504)

def f18ri_sgn_rev_zscore_756d_base_v026_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_zscore(ratio, 756)

def f18ri_sgn_rev_zscore_1260d_base_v027_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_zscore(ratio, 1260)

def f18ri_sgn_rev_mean_rel_252d_base_v028_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_sgn_rev_mean_rel_756d_base_v029_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_sgn_rev_mean_rel_1260d_base_v030_signal(arg_sgna: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_sgn_ast_raw_base_v031_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return ratio

def f18ri_sgn_ast_zscore_63d_base_v032_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_zscore(ratio, 63)

def f18ri_sgn_ast_zscore_126d_base_v033_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_zscore(ratio, 126)

def f18ri_sgn_ast_zscore_252d_base_v034_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_zscore(ratio, 252)

def f18ri_sgn_ast_zscore_504d_base_v035_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_zscore(ratio, 504)

def f18ri_sgn_ast_zscore_756d_base_v036_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_zscore(ratio, 756)

def f18ri_sgn_ast_zscore_1260d_base_v037_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_zscore(ratio, 1260)

def f18ri_sgn_ast_mean_rel_252d_base_v038_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_sgn_ast_mean_rel_756d_base_v039_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_sgn_ast_mean_rel_1260d_base_v040_signal(arg_sgna: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_int_ast_raw_base_v041_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return ratio

def f18ri_int_ast_zscore_63d_base_v042_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_zscore(ratio, 63)

def f18ri_int_ast_zscore_126d_base_v043_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_zscore(ratio, 126)

def f18ri_int_ast_zscore_252d_base_v044_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_zscore(ratio, 252)

def f18ri_int_ast_zscore_504d_base_v045_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_zscore(ratio, 504)

def f18ri_int_ast_zscore_756d_base_v046_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_zscore(ratio, 756)

def f18ri_int_ast_zscore_1260d_base_v047_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_zscore(ratio, 1260)

def f18ri_int_ast_mean_rel_252d_base_v048_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_int_ast_mean_rel_756d_base_v049_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_int_ast_mean_rel_1260d_base_v050_signal(arg_intangibles: pd.Series, arg_assets: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_assets)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_int_rev_raw_base_v051_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return ratio

def f18ri_int_rev_zscore_63d_base_v052_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_zscore(ratio, 63)

def f18ri_int_rev_zscore_126d_base_v053_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_zscore(ratio, 126)

def f18ri_int_rev_zscore_252d_base_v054_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_zscore(ratio, 252)

def f18ri_int_rev_zscore_504d_base_v055_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_zscore(ratio, 504)

def f18ri_int_rev_zscore_756d_base_v056_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_zscore(ratio, 756)

def f18ri_int_rev_zscore_1260d_base_v057_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_zscore(ratio, 1260)

def f18ri_int_rev_mean_rel_252d_base_v058_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_int_rev_mean_rel_756d_base_v059_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_int_rev_mean_rel_1260d_base_v060_signal(arg_intangibles: pd.Series, arg_revenue: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_intangibles, arg_revenue)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_rnd_shr_raw_base_v061_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return ratio

def f18ri_rnd_shr_zscore_63d_base_v062_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_zscore(ratio, 63)

def f18ri_rnd_shr_zscore_126d_base_v063_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_zscore(ratio, 126)

def f18ri_rnd_shr_zscore_252d_base_v064_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_zscore(ratio, 252)

def f18ri_rnd_shr_zscore_504d_base_v065_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_zscore(ratio, 504)

def f18ri_rnd_shr_zscore_756d_base_v066_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_zscore(ratio, 756)

def f18ri_rnd_shr_zscore_1260d_base_v067_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_zscore(ratio, 1260)

def f18ri_rnd_shr_mean_rel_252d_base_v068_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(252, min_periods=1).mean())

def f18ri_rnd_shr_mean_rel_756d_base_v069_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(756, min_periods=1).mean())

def f18ri_rnd_shr_mean_rel_1260d_base_v070_signal(arg_rnd: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_rnd, arg_shareswa)
    return _ri_ratio(ratio, ratio.rolling(1260, min_periods=1).mean())

def f18ri_sgn_shr_raw_base_v071_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return ratio

def f18ri_sgn_shr_zscore_63d_base_v072_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_zscore(ratio, 63)

def f18ri_sgn_shr_zscore_126d_base_v073_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_zscore(ratio, 126)

def f18ri_sgn_shr_zscore_252d_base_v074_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_zscore(ratio, 252)

def f18ri_sgn_shr_zscore_504d_base_v075_signal(arg_sgna: pd.Series, arg_shareswa: pd.Series) -> pd.Series:
    ratio = _ri_ratio(arg_sgna, arg_shareswa)
    return _ri_zscore(ratio, 504)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {
    "rnd": "sep.rnd", "sgna": "sep.sgna", "intangibles": "sep.intangibles", 
    "revenue": "sep.revenue", "assets": "sep.assets", "netinc": "sep.netinc", "shareswa": "sep.shareswa"
}

f18ri_NAMES = [f for f in globals() if f.startswith("f18ri_") and f.endswith("_signal")]

f18ri_BASE_REGISTRY_001_075 = {
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
    for n, c in f18ri_BASE_REGISTRY_001_075.items():
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

