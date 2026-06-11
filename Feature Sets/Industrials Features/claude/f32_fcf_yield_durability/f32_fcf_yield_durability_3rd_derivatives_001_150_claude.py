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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f32_fcf_yield(fcf, ev):
    return fcf / ev.replace(0, np.nan)


def _f32_fcf_yield_stability(fcf, ev, w):
    y = fcf / ev.replace(0, np.nan)
    return _mean(y, w) / _std(y, w).replace(0, np.nan)


def _f32_fcf_compound_quality(fcf, marketcap, w):
    y = fcf / marketcap.replace(0, np.nan)
    return _mean(y, w) - 0.5 * _std(y, w)


_BWINS = [5, 10, 21, 42, 63, 126, 189, 252, 378, 504]
_JWINS = [5, 21, 63, 126, 252]


def _build_features():
    feats = []
    idx = 1

    def add(fn, name):
        fn.__name__ = name
        feats.append(fn)

    for bw in _BWINS:
        for jw in _JWINS:
            v = f"v{idx:03d}"
            name = f"f32fyd_f32_fcf_yield_durability_yieldmean_{bw}d_jerk_{v}_signal"

            def fn(fcf, ev, closeadj, bw=bw, jw=jw):
                base = _mean(_f32_fcf_yield(fcf, ev), bw) * closeadj
                result = _jerk(base, jw)
                return result.replace([np.inf, -np.inf], np.nan)

            add(fn, name)
            idx += 1

    for bw in _BWINS:
        for jw in _JWINS:
            v = f"v{idx:03d}"
            name = f"f32fyd_f32_fcf_yield_durability_stability_{bw}d_jerk_{v}_signal"

            def fn(fcf, ev, closeadj, bw=bw, jw=jw):
                base = _f32_fcf_yield_stability(fcf, ev, bw) * closeadj
                result = _jerk(base, jw)
                return result.replace([np.inf, -np.inf], np.nan)

            add(fn, name)
            idx += 1

    for bw in _BWINS:
        for jw in _JWINS:
            v = f"v{idx:03d}"
            name = f"f32fyd_f32_fcf_yield_durability_compoundq_{bw}d_jerk_{v}_signal"

            def fn(fcf, marketcap, closeadj, bw=bw, jw=jw):
                base = _f32_fcf_compound_quality(fcf, marketcap, bw) * closeadj
                result = _jerk(base, jw)
                return result.replace([np.inf, -np.inf], np.nan)

            add(fn, name)
            idx += 1

    return feats


_FEATURES = _build_features()


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_FCF_YIELD_DURABILITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fcf      = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    debt     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    ev = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")

    cols = {
        "closeadj": closeadj, "fcf": fcf, "ev": ev, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f32_fcf_yield", "_f32_fcf_yield_stability", "_f32_fcf_compound_quality")
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
    print(f"OK f32_fcf_yield_durability_3rd_derivatives_001_150_claude: {n_features} features pass")
