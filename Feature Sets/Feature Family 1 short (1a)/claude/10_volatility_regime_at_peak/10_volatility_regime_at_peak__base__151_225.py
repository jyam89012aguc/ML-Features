"""volatility_regime_at_peak base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for vol-regime / cliff-change detection at price peaks.
This file carries indices 151-152 (2 distinct hypotheses). Reserved range up to 225.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


# ============================================================
#                    FEATURES 151-152
# ============================================================


def f10_vrap_151_rvol_21d_one_day_jump_pct(close: pd.Series) -> pd.Series:
    """Max of rvol21.pct_change() over trailing 21d — captures vol-cliff regime change."""
    r = _safe_log(close).diff()
    rvol21 = r.rolling(MDAYS, min_periods=MDAYS).std(ddof=0)
    pct = rvol21.pct_change().replace([np.inf, -np.inf], np.nan)
    return pct.rolling(MDAYS, min_periods=WDAYS).max()


def f10_vrap_152_count_abs_ret_gt_5sigma_63d(close: pd.Series) -> pd.Series:
    """Count of bars in 63d where |log return| > 5 * trailing-63d sigma at that bar."""
    r = _safe_log(close).diff()
    sigma = r.rolling(QDAYS, min_periods=MDAYS).std(ddof=0)
    extreme = (r.abs() > 5.0 * sigma).astype(float)
    # Mask bars where sigma was not computable
    extreme = extreme.where(sigma.notna() & r.notna(), np.nan)
    return extreme.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
#                    REGISTRY
# ============================================================

VOLATILITY_REGIME_AT_PEAK_BASE_REGISTRY_151_225 = {
    "f10_vrap_151_rvol_21d_one_day_jump_pct": {"inputs": ["close"], "func": f10_vrap_151_rvol_21d_one_day_jump_pct},
    "f10_vrap_152_count_abs_ret_gt_5sigma_63d": {"inputs": ["close"], "func": f10_vrap_152_count_abs_ret_gt_5sigma_63d},
}
