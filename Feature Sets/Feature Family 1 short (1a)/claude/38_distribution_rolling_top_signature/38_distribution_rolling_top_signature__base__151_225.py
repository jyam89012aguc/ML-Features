"""distribution_rolling_top_signature base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gap for distinguishing rolling-top distribution from spike-top blowoff.
This file carries index 151 (1 distinct hypothesis). Reserved range up to 225.

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
#                    FEATURES 151
# ============================================================


def f38_drts_151_rolling_vs_spike_top_classifier_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dwell / (1 + spike_score). dwell = fraction of bars in 63d with high within 5% of 63d max.
    spike_score = ((63d_max_high - close) / ATR21) at peak bar (= current bar's distance metric).
    """
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    near = (_safe_div(high, rmax) >= 0.95).astype(float)
    # Mask invalid bars so they don't count as 0
    near = near.where(rmax.notna() & high.notna(), np.nan)
    dwell = near.rolling(QDAYS, min_periods=MDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    spike_score = _safe_div(rmax - close, atr)
    return _safe_div(dwell, 1.0 + spike_score)


# ============================================================
#                    REGISTRY
# ============================================================

DISTRIBUTION_ROLLING_TOP_SIGNATURE_BASE_REGISTRY_151_225 = {
    "f38_drts_151_rolling_vs_spike_top_classifier_63d": {"inputs": ["close", "high", "low"], "func": f38_drts_151_rolling_vs_spike_top_classifier_63d},
}
