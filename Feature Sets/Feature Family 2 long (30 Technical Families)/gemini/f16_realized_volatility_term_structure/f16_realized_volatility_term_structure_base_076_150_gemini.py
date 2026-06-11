# f16_realized_volatility_term_structure_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _rv(p, w):
    returns = np.log(p / p.shift(1).replace(0, np.nan))
    return returns.rolling(w, min_periods=min(w, 5)).std() * np.sqrt(252)

def _vspread(vs, vl):
    return (vs - vl) / vl.abs().replace(0, np.nan)

def _vz(v, w):
    return (v - _sma(v, w)) / _std(v, w).replace(0, np.nan)

def _vrank(v, w):
    return v.rolling(w, min_periods=min(w, 5)).rank(pct=True)

def _vov(v, w):
    return _std(v, w)

# f16rvts_f16_realized_volatility_term_structure_v076_signal: 5d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v077_signal: 10d vs 42d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v078_signal: 63d z-scored 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v079_signal: 126d volatility of 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v080_signal: 252d percentile rank of 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v081_signal: 126d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v082_signal: 10d vs 252d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v083_signal: 21d z-scored 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v084_signal: 42d volatility of 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v085_signal: 63d percentile rank of 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v086_signal: 42d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v087_signal: 63d vs 252d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v088_signal: 5d z-scored 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v089_signal: 10d volatility of 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v090_signal: 21d percentile rank of 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v091_signal: 10d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v092_signal: 21d vs 63d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v093_signal: 126d z-scored 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v094_signal: 252d volatility of 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v095_signal: 5d percentile rank of 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v096_signal: 252d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v097_signal: 5d vs 21d vol spread close

# f16rvts_f16_realized_volatility_term_structure_v098_signal: 42d z-scored 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v099_signal: 63d volatility of 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v100_signal: 126d percentile rank of 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v101_signal: 63d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v102_signal: 5d vs 126d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v103_signal: 10d z-scored 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v104_signal: 21d volatility of 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v105_signal: 42d percentile rank of 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v106_signal: 21d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v107_signal: 42d vs 126d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v108_signal: 252d z-scored 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v109_signal: 5d volatility of 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v110_signal: 10d percentile rank of 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v111_signal: 5d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v112_signal: 10d vs 42d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v113_signal: 63d z-scored 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v114_signal: 126d volatility of 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v115_signal: 252d percentile rank of 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v116_signal: 126d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v117_signal: 10d vs 252d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v118_signal: 21d z-scored 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v119_signal: 42d volatility of 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v120_signal: 63d percentile rank of 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v121_signal: 42d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v122_signal: 63d vs 252d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v123_signal: 5d z-scored 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v124_signal: 10d volatility of 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v125_signal: 21d percentile rank of 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v126_signal: 10d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v127_signal: 21d vs 63d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v128_signal: 126d z-scored 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v129_signal: 252d volatility of 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v130_signal: 5d percentile rank of 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v131_signal: 252d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v132_signal: 5d vs 21d vol spread close

# f16rvts_f16_realized_volatility_term_structure_v133_signal: 42d z-scored 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v134_signal: 63d volatility of 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v135_signal: 126d percentile rank of 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v136_signal: 63d realized vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v137_signal: 5d vs 126d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v138_signal: 10d z-scored 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v139_signal: 21d volatility of 5d vol close

# f16rvts_f16_realized_volatility_term_structure_v140_signal: 42d percentile rank of 10d vol close

# f16rvts_f16_realized_volatility_term_structure_v141_signal: 21d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v142_signal: 42d vs 126d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v143_signal: 252d z-scored 63d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v144_signal: 5d volatility of 126d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v145_signal: 10d percentile rank of 252d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v146_signal: 5d realized vol close

# f16rvts_f16_realized_volatility_term_structure_v147_signal: 10d vs 42d vol spread closeadj

# f16rvts_f16_realized_volatility_term_structure_v148_signal: 63d z-scored 21d vol close

# f16rvts_f16_realized_volatility_term_structure_v149_signal: 126d volatility of 42d vol closeadj

# f16rvts_f16_realized_volatility_term_structure_v150_signal: 252d percentile rank of 63d vol closeadj

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}
BASE_NAMES = [f for f in globals() if f.startswith("f16rvts_") and f.endswith("_signal")]
F16_REALIZED_VOLATILITY_TERM_STRUCTURE_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F16_REALIZED_VOLATILITY_TERM_STRUCTURE_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("OK")