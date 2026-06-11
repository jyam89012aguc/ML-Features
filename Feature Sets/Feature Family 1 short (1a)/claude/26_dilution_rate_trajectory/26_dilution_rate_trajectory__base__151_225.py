"""dilution_rate_trajectory base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for dilution-rate detection.
This file carries indices 151-152 (2 distinct hypotheses). Reserved range up to 225.

Inputs: quarterly fundamentals + insider data. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20

# Daily windows for insider sell rollups
QDAYS = 63


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


# ============================================================
#                    FEATURES 151-152
# ============================================================


def f26_drtj_151_insider_participation_in_offerings_proxy(sharesbas: pd.Series, insider_sell_value: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of share-count growth (in $ value) matched by insider sell dollars.

    numerator: insider_sell_value rolled 63d-sum.
    denominator: (sharesbas − sharesbas.shift(QQTRS)) × close — $ value of yoy share growth.
    """
    if sharesbas is None or insider_sell_value is None or close is None or len(sharesbas) == 0:
        return pd.Series(np.nan, index=getattr(sharesbas, "index", None))
    insider_63d = insider_sell_value.rolling(QDAYS, min_periods=5).sum()
    share_growth = sharesbas - sharesbas.shift(QQTRS)
    denom = share_growth * close
    return _safe_div(insider_63d, denom)


def f26_drtj_152_convertible_vs_secondary_classifier(sharesbas: pd.Series, debtc: pd.Series) -> pd.Series:
    """+1 = convert-to-equity (share count grew & current debt fell sharply).
    −1 = pure secondary (share count grew & current debt roughly unchanged).
    0 otherwise.
    """
    if sharesbas is None or debtc is None or len(sharesbas) == 0:
        return pd.Series(np.nan, index=getattr(sharesbas, "index", None))
    shares_yoy = _safe_div(sharesbas, sharesbas.shift(QQTRS)) - 1.0
    debtc_yoy = _safe_div(debtc, debtc.shift(QQTRS)) - 1.0
    dilution = shares_yoy > 0.05
    convert = dilution & (debtc_yoy < -0.1)
    # "≈ 0" interpreted as |yoy| < 0.1 (i.e. not a big decline)
    secondary = dilution & (debtc_yoy.abs() < 0.1)
    out = pd.Series(0.0, index=sharesbas.index)
    out = out.where(~convert, 1.0)
    out = out.where(~(secondary & ~convert), -1.0)
    # propagate NaN where inputs missing
    valid = shares_yoy.notna() & debtc_yoy.notna()
    out = out.where(valid, np.nan)
    return out


# ============================================================
#                    REGISTRY
# ============================================================

DILUTION_RATE_TRAJECTORY_BASE_REGISTRY_151_225 = {
    "f26_drtj_151_insider_participation_in_offerings_proxy": {"inputs": ["sharesbas", "insider_sell_value", "close"], "func": f26_drtj_151_insider_participation_in_offerings_proxy},
    "f26_drtj_152_convertible_vs_secondary_classifier": {"inputs": ["sharesbas", "debtc"], "func": f26_drtj_152_convertible_vs_secondary_classifier},
}
