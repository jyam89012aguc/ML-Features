"""short_interest_structure base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for short-interest structure detection.
This file carries indices 151-153 (3 distinct hypotheses). Reserved range up to 225.

Inputs: NSIR (shortinterest, daystocover, shortpctfloat), SEP (close).
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows, no .shift(-N).
Self-contained — no imports across families.
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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


# ============================================================
#                    FEATURES 151-153
# ============================================================


def f16_sint_151_dtc_vol_adjusted_252d(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    """Days-to-cover divided by 63d realized log-vol — DTC scaled by current vol regime."""
    rvol_63d = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(daystocover, rvol_63d)


def f16_sint_152_si_half_life_estimate_252d(shortinterest: pd.Series) -> pd.Series:
    """Estimate AR1 coef phi of log(SI).diff() over 252d rolling; return -1/log(|phi|) clipped to [1, 252]."""
    x = _safe_log(shortinterest).diff()

    def _ar1_halflife(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        if len(v) < 2:
            return np.nan
        y = v[1:]
        xl = v[:-1]
        if len(y) < 2:
            return np.nan
        xm = xl.mean()
        ym = y.mean()
        num = ((xl - xm) * (y - ym)).sum()
        den = ((xl - xm) ** 2).sum()
        if den == 0 or not np.isfinite(den):
            return np.nan
        phi = num / den
        a = abs(phi)
        if a <= 0 or a >= 1 or not np.isfinite(a):
            return np.nan
        lg = np.log(a)
        if lg == 0:
            return np.nan
        hl = -1.0 / lg
        return float(np.clip(hl, 1.0, 252.0))

    return x.rolling(YDAYS, min_periods=QDAYS).apply(_ar1_halflife, raw=True)


def f16_sint_153_days_since_max_spfloat_252d(shortpctfloat: pd.Series) -> pd.Series:
    """Bars since shortpctfloat hit its 252d max."""
    return shortpctfloat.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float(len(w) - 1 - int(np.argmax(w))), raw=True)


# ============================================================
#                    REGISTRY
# ============================================================

SHORT_INTEREST_STRUCTURE_BASE_REGISTRY_151_225 = {
    "f16_sint_151_dtc_vol_adjusted_252d": {"inputs": ["daystocover", "close"], "func": f16_sint_151_dtc_vol_adjusted_252d},
    "f16_sint_152_si_half_life_estimate_252d": {"inputs": ["shortinterest"], "func": f16_sint_152_si_half_life_estimate_252d},
    "f16_sint_153_days_since_max_spfloat_252d": {"inputs": ["shortpctfloat"], "func": f16_sint_153_days_since_max_spfloat_252d},
}
