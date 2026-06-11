"""margin_compression_trajectory base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for margin-compression detection.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: quarterly fundamentals. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
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


# ============================================================
#                    FEATURES 151-153
# ============================================================


def f22_mctj_151_decremental_incremental_margin_asymmetry_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Mean Δopinc/Δrev for down-rev quarters MINUS mean for up-rev quarters, 8q window.

    Decremental margin (slope when rev falls) typically exceeds incremental margin (slope when rev rises)
    for structurally pressured firms — fixed costs don't shrink as fast as variable revenue.
    """
    if revenue is None or opinc is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    drev = revenue.diff()
    dopi = opinc.diff()
    ratio = _safe_div(dopi, drev)
    # ratio when down q, ratio when up q
    down_ratio = ratio.where(drev < 0)
    up_ratio = ratio.where(drev > 0)
    down_mean = down_ratio.rolling(QQTRS_2Y, min_periods=3).mean()
    up_mean = up_ratio.rolling(QQTRS_2Y, min_periods=3).mean()
    return down_mean - up_mean


def f22_mctj_152_margin_compression_cogs_share_4q(revenue: pd.Series, gp: pd.Series, sgna: pd.Series, depamor: pd.Series) -> pd.Series:
    """COGS share of margin compression over 4q: Δcogs_sum / (Δcogs+Δsgna+Δdepamor)_sum.

    cogs ≈ revenue − gp. Decomposes which cost line is driving margin compression.
    """
    if revenue is None or gp is None or sgna is None or depamor is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    cogs = revenue - gp
    dcogs = cogs.diff()
    dsgna = sgna.diff()
    ddep = depamor.diff()
    num = dcogs.rolling(QQTRS, min_periods=2).sum()
    den = (dcogs + dsgna + ddep).rolling(QQTRS, min_periods=2).sum()
    return _safe_div(num, den)


def f22_mctj_153_etr_normalized_margin_trend_8q(opinc: pd.Series, taxexp: pd.Series, ebt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Pretax margin (ebt/revenue) slope over 8q MINUS effective-tax-rate (taxexp/ebt) slope over 8q.

    Strips "tax-stripped" benefit from headline margin trend so we see true operating compression.
    """
    if opinc is None or taxexp is None or ebt is None or revenue is None or len(revenue) == 0:
        return pd.Series(np.nan, index=getattr(revenue, "index", None))
    pretax_margin = _safe_div(ebt, revenue)
    etr = _safe_div(taxexp, ebt)
    pm_slope = _rolling_slope(pretax_margin, QQTRS_2Y)
    etr_slope = _rolling_slope(etr, QQTRS_2Y)
    return pm_slope - etr_slope


# ============================================================
#                    REGISTRY
# ============================================================

MARGIN_COMPRESSION_TRAJECTORY_BASE_REGISTRY_151_225 = {
    "f22_mctj_151_decremental_incremental_margin_asymmetry_8q": {"inputs": ["revenue", "opinc"], "func": f22_mctj_151_decremental_incremental_margin_asymmetry_8q},
    "f22_mctj_152_margin_compression_cogs_share_4q": {"inputs": ["revenue", "gp", "sgna", "depamor"], "func": f22_mctj_152_margin_compression_cogs_share_4q},
    "f22_mctj_153_etr_normalized_margin_trend_8q": {"inputs": ["opinc", "taxexp", "ebt", "revenue"], "func": f22_mctj_153_etr_normalized_margin_trend_8q},
}
