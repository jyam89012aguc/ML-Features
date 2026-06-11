"""moat_erosion_trajectory d3 features 151-225 — third-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _ttm(s, periods=QQTRS):
    return s.rolling(periods, min_periods=max(periods // 2, 2)).sum()


def f44_mert_151_switching_cost_proxy_deferred_rev_stickiness_d3(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    ratio = _safe_div(deferredrev, revenue)
    arr = ratio.to_numpy(dtype=float)
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    win = QQTRS_3Y
    lag = QQTRS
    min_obs = max(win // 2, lag + 2)
    for i in range(n):
        lo = max(0, i - win + 1)
        w = arr[lo:i + 1]
        if len(w) < lag + 2:
            continue
        x0 = w[lag:]
        x1 = w[:len(w) - lag]
        valid = ~np.isnan(x0) & ~np.isnan(x1)
        if valid.sum() < min_obs - lag:
            continue
        a = x0[valid]
        b = x1[valid]
        if a.size < 3:
            continue
        am = a.mean()
        bm = b.mean()
        num = ((a - am) * (b - bm)).sum()
        den = np.sqrt(((a - am) ** 2).sum() * ((b - bm) ** 2).sum())
        if den == 0 or not np.isfinite(den):
            continue
        out[i] = num / den
    return pd.Series(out, index=deferredrev.index).replace([np.inf, -np.inf], np.nan).diff().diff().diff()


def f44_mert_152_brand_marketing_investment_efficiency_d3(rnd: pd.Series, sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    d_rev_4q = revenue - revenue.shift(QQTRS)
    rnd_ttm = _ttm(rnd, QQTRS)
    sgna_ttm = _ttm(sgna, QQTRS)
    denom = rnd_ttm.fillna(0) + sgna_ttm.fillna(0)
    both_nan = rnd_ttm.isna() & sgna_ttm.isna()
    denom = denom.where(~both_nan, np.nan)
    return _safe_div(d_rev_4q, denom).diff().diff().diff()


MOAT_EROSION_TRAJECTORY_D3_REGISTRY_151_225 = {
    "f44_mert_151_switching_cost_proxy_deferred_rev_stickiness_d3": {"inputs": ["deferredrev", "revenue"], "func": f44_mert_151_switching_cost_proxy_deferred_rev_stickiness_d3},
    "f44_mert_152_brand_marketing_investment_efficiency_d3": {"inputs": ["rnd", "sgna", "revenue"], "func": f44_mert_152_brand_marketing_investment_efficiency_d3},
}
