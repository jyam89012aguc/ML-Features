"""options_skew_at_peak d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
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


def _nan_series_like(*candidates):
    for c in candidates:
        if c is not None and hasattr(c, "index"):
            return pd.Series(np.nan, index=c.index)
    return pd.Series(dtype=float)


def _is_unusable(s):
    if s is None:
        return True
    if not isinstance(s, pd.Series):
        return True
    if len(s) == 0:
        return True
    if s.isna().all():
        return True
    return False


def f17_oskp_151_risk_reversal_25_delta_30d_d1(iv_25d_call_30d: pd.Series, iv_25d_put_30d: pd.Series) -> pd.Series:
    if _is_unusable(iv_25d_call_30d) or _is_unusable(iv_25d_put_30d):
        return _nan_series_like(iv_25d_call_30d, iv_25d_put_30d)
    return (iv_25d_call_30d - iv_25d_put_30d).diff()


def f17_oskp_152_tail_skew_10_delta_30d_d1(iv_10d_put_30d: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    if _is_unusable(iv_10d_put_30d) or _is_unusable(atm_iv_30d):
        return _nan_series_like(iv_10d_put_30d, atm_iv_30d)
    return (iv_10d_put_30d - atm_iv_30d).diff()


def f17_oskp_153_vol_of_vol_atm_iv_21d_d1(atm_iv_30d: pd.Series) -> pd.Series:
    if _is_unusable(atm_iv_30d):
        return _nan_series_like(atm_iv_30d)
    return atm_iv_30d.diff().rolling(MDAYS, min_periods=WDAYS).std().diff()


def f17_oskp_154_max_pain_proxy_distance_d1(max_pain_strike: pd.Series, close: pd.Series) -> pd.Series:
    if _is_unusable(max_pain_strike) or _is_unusable(close):
        return _nan_series_like(max_pain_strike, close)
    return _safe_div(max_pain_strike - close, close).diff()


def f17_oskp_155_oi_concentration_hhi_by_strike_d1(oi_hhi_input: pd.Series) -> pd.Series:
    if _is_unusable(oi_hhi_input):
        return _nan_series_like(oi_hhi_input)
    return oi_hhi_input.astype(float).diff()


def f17_oskp_156_iv_beta_to_vix_63d_d1(atm_iv_30d: pd.Series, vix: pd.Series) -> pd.Series:
    if _is_unusable(atm_iv_30d) or _is_unusable(vix):
        return _nan_series_like(atm_iv_30d, vix)
    da = atm_iv_30d.diff()
    dv = vix.diff()
    cov = da.rolling(QDAYS, min_periods=MDAYS).cov(dv)
    var = dv.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(cov, var).diff()


OPTIONS_SKEW_AT_PEAK_D1_REGISTRY_151_225 = {
    "f17_oskp_151_risk_reversal_25_delta_30d_d1": {"inputs": ["iv_25d_call_30d", "iv_25d_put_30d"], "func": f17_oskp_151_risk_reversal_25_delta_30d_d1},
    "f17_oskp_152_tail_skew_10_delta_30d_d1": {"inputs": ["iv_10d_put_30d", "atm_iv_30d"], "func": f17_oskp_152_tail_skew_10_delta_30d_d1},
    "f17_oskp_153_vol_of_vol_atm_iv_21d_d1": {"inputs": ["atm_iv_30d"], "func": f17_oskp_153_vol_of_vol_atm_iv_21d_d1},
    "f17_oskp_154_max_pain_proxy_distance_d1": {"inputs": ["max_pain_strike", "close"], "func": f17_oskp_154_max_pain_proxy_distance_d1},
    "f17_oskp_155_oi_concentration_hhi_by_strike_d1": {"inputs": ["oi_hhi_input"], "func": f17_oskp_155_oi_concentration_hhi_by_strike_d1},
    "f17_oskp_156_iv_beta_to_vix_63d_d1": {"inputs": ["atm_iv_30d", "vix"], "func": f17_oskp_156_iv_beta_to_vix_63d_d1},
}
