"""dilution_rate_trajectory d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

QQTRS = 4
QQTRS_2Y = 8
QQTRS_3Y = 12
QQTRS_5Y = 20
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


def f26_drtj_151_insider_participation_in_offerings_proxy_d2(sharesbas: pd.Series, insider_sell_value: pd.Series, close: pd.Series) -> pd.Series:
    if sharesbas is None or insider_sell_value is None or close is None or len(sharesbas) == 0:
        return pd.Series(np.nan, index=getattr(sharesbas, "index", None))
    insider_63d = insider_sell_value.rolling(QDAYS, min_periods=5).sum()
    share_growth = sharesbas - sharesbas.shift(QQTRS)
    denom = share_growth * close
    return _safe_div(insider_63d, denom).diff().diff()


def f26_drtj_152_convertible_vs_secondary_classifier_d2(sharesbas: pd.Series, debtc: pd.Series) -> pd.Series:
    if sharesbas is None or debtc is None or len(sharesbas) == 0:
        return pd.Series(np.nan, index=getattr(sharesbas, "index", None))
    shares_yoy = _safe_div(sharesbas, sharesbas.shift(QQTRS)) - 1.0
    debtc_yoy = _safe_div(debtc, debtc.shift(QQTRS)) - 1.0
    dilution = shares_yoy > 0.05
    convert = dilution & (debtc_yoy < -0.1)
    secondary = dilution & (debtc_yoy.abs() < 0.1)
    out = pd.Series(0.0, index=sharesbas.index)
    out = out.where(~convert, 1.0)
    out = out.where(~(secondary & ~convert), -1.0)
    valid = shares_yoy.notna() & debtc_yoy.notna()
    out = out.where(valid, np.nan)
    return out.diff().diff()


DILUTION_RATE_TRAJECTORY_D2_REGISTRY_151_225 = {
    "f26_drtj_151_insider_participation_in_offerings_proxy_d2": {"inputs": ["sharesbas", "insider_sell_value", "close"], "func": f26_drtj_151_insider_participation_in_offerings_proxy_d2},
    "f26_drtj_152_convertible_vs_secondary_classifier_d2": {"inputs": ["sharesbas", "debtc"], "func": f26_drtj_152_convertible_vs_secondary_classifier_d2},
}
