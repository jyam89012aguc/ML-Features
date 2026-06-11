"""short_interest_structure d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
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


def f16_sint_151_dtc_vol_adjusted_252d_d2(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    rvol_63d = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(daystocover, rvol_63d).diff().diff()


def f16_sint_152_si_half_life_estimate_252d_d2(shortinterest: pd.Series) -> pd.Series:
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

    return x.rolling(YDAYS, min_periods=QDAYS).apply(_ar1_halflife, raw=True).diff().diff()


def f16_sint_153_days_since_max_spfloat_252d_d2(shortpctfloat: pd.Series) -> pd.Series:
    return shortpctfloat.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float(len(w) - 1 - int(np.argmax(w))), raw=True).diff().diff()


SHORT_INTEREST_STRUCTURE_D2_REGISTRY_151_225 = {
    "f16_sint_151_dtc_vol_adjusted_252d_d2": {"inputs": ["daystocover", "close"], "func": f16_sint_151_dtc_vol_adjusted_252d_d2},
    "f16_sint_152_si_half_life_estimate_252d_d2": {"inputs": ["shortinterest"], "func": f16_sint_152_si_half_life_estimate_252d_d2},
    "f16_sint_153_days_since_max_spfloat_252d_d2": {"inputs": ["shortpctfloat"], "func": f16_sint_153_days_since_max_spfloat_252d_d2},
}
