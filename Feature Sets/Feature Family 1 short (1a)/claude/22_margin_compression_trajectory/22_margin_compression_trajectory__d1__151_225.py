"""margin_compression_trajectory d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


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


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def f22_mctj_151_decremental_incremental_margin_asymmetry_8q_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    if revenue is None or opinc is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    drev = revenue.diff()
    dopi = opinc.diff()
    ratio = _safe_div(dopi, drev)
    down_ratio = ratio.where(drev < 0)
    up_ratio = ratio.where(drev > 0)
    down_mean = down_ratio.rolling(QQTRS_2Y, min_periods=3).mean()
    up_mean = up_ratio.rolling(QQTRS_2Y, min_periods=3).mean()
    return (down_mean - up_mean).diff()


def f22_mctj_152_margin_compression_cogs_share_4q_d1(revenue: pd.Series, gp: pd.Series, sgna: pd.Series, depamor: pd.Series) -> pd.Series:
    if revenue is None or gp is None or sgna is None or depamor is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    cogs = revenue - gp
    dcogs = cogs.diff()
    dsgna = sgna.diff()
    ddep = depamor.diff()
    num = dcogs.rolling(QQTRS, min_periods=2).sum()
    den = (dcogs + dsgna + ddep).rolling(QQTRS, min_periods=2).sum()
    return _safe_div(num, den).diff()


def f22_mctj_153_etr_normalized_margin_trend_8q_d1(opinc: pd.Series, taxexp: pd.Series, ebt: pd.Series, revenue: pd.Series) -> pd.Series:
    if opinc is None or taxexp is None or ebt is None or revenue is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    pretax_margin = _safe_div(ebt, revenue)
    etr = _safe_div(taxexp, ebt)
    pm_slope = _rolling_slope(pretax_margin, QQTRS_2Y)
    etr_slope = _rolling_slope(etr, QQTRS_2Y)
    return (pm_slope - etr_slope).diff()


MARGIN_COMPRESSION_TRAJECTORY_D1_REGISTRY_151_225 = {
    "f22_mctj_151_decremental_incremental_margin_asymmetry_8q_d1": {"inputs": ["revenue", "opinc"], "func": f22_mctj_151_decremental_incremental_margin_asymmetry_8q_d1},
    "f22_mctj_152_margin_compression_cogs_share_4q_d1": {"inputs": ["revenue", "gp", "sgna", "depamor"], "func": f22_mctj_152_margin_compression_cogs_share_4q_d1},
    "f22_mctj_153_etr_normalized_margin_trend_8q_d1": {"inputs": ["opinc", "taxexp", "ebt", "revenue"], "func": f22_mctj_153_etr_normalized_margin_trend_8q_d1},
}
