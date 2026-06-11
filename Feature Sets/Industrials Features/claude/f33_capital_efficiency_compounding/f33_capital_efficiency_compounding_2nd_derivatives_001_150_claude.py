import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f33_roic_trajectory(roic, w):
    return _mean(roic, w) + (roic - roic.shift(w))


def _f33_roic_persistence(roic, w):
    m = _mean(roic, w)
    sd = _std(roic, w).replace(0, np.nan)
    return m / sd


def _f33_capital_efficiency_uplift(roic, roa, w):
    return _mean(roic - roa, w)


_BWINS = [5, 10, 21, 42, 63, 126, 189, 252, 378, 504]
_SWINS = [5, 21, 63, 126, 252]


def _build_features():
    feats = []
    idx = 1

    def add(fn, name):
        fn.__name__ = name
        feats.append(fn)

    for bw in _BWINS:
        for sw in _SWINS:
            v = f"v{idx:03d}"
            name = f"f33cec_f33_capital_efficiency_compounding_traj_{bw}d_slope_{v}_signal"

            def fn(roic, closeadj, bw=bw, sw=sw):
                base = _f33_roic_trajectory(roic, bw) * closeadj
                result = _slope_diff_norm(base, sw)
                return result.replace([np.inf, -np.inf], np.nan)

            add(fn, name)
            idx += 1

    for bw in _BWINS:
        for sw in _SWINS:
            v = f"v{idx:03d}"
            name = f"f33cec_f33_capital_efficiency_compounding_persist_{bw}d_slope_{v}_signal"

            def fn(roic, closeadj, bw=bw, sw=sw):
                base = _f33_roic_persistence(roic, bw) * closeadj
                result = _slope_pct(base, sw)
                return result.replace([np.inf, -np.inf], np.nan)

            add(fn, name)
            idx += 1

    for bw in _BWINS:
        for sw in _SWINS:
            v = f"v{idx:03d}"
            name = f"f33cec_f33_capital_efficiency_compounding_uplift_{bw}d_slope_{v}_signal"

            def fn(roic, roa, closeadj, bw=bw, sw=sw):
                base = _f33_capital_efficiency_uplift(roic, roa, bw) * closeadj
                result = _slope_diff_norm(base, sw)
                return result.replace([np.inf, -np.inf], np.nan)

            add(fn, name)
            idx += 1

    return feats


_FEATURES = _build_features()


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_CAPITAL_EFFICIENCY_COMPOUNDING_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    roa  = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe  = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "roa": roa, "roe": roe, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f33_roic_trajectory", "_f33_roic_persistence", "_f33_capital_efficiency_uplift")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f33_capital_efficiency_compounding_2nd_derivatives_001_150_claude: {n_features} features pass")
