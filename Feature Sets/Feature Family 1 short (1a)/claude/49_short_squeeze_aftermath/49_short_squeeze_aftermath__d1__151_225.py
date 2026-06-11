"""short_squeeze_aftermath d1 features 151-225 — first-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def f49_ssaf_151_re_shorting_during_decline_indicator_21d_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    if shortinterest is None or close is None:
        return pd.Series(np.nan)
    si_ch = shortinterest.diff(MDAYS)
    px_ch = _safe_log(close).diff(MDAYS)
    cond = (si_ch > 0) & (px_ch < -0.05)
    out = cond.astype(float)
    return out.where(si_ch.notna() & px_ch.notna(), np.nan).diff()


def f49_ssaf_152_post_event_window_gate_63d_d1(squeeze_event_date: pd.Series) -> pd.Series:
    if squeeze_event_date is None:
        return pd.Series(np.nan)
    try:
        ev = squeeze_event_date.astype(bool).astype(float)
    except Exception:
        return pd.Series(np.nan, index=squeeze_event_date.index if hasattr(squeeze_event_date, "index") else None)
    idx_pos = pd.Series(np.arange(len(ev), dtype=float), index=ev.index)
    last_event_idx = idx_pos.where(ev > 0, np.nan).ffill()
    days_since = idx_pos - last_event_idx
    cond = (days_since >= 1) & (days_since <= 63)
    out = cond.astype(float)
    return out.where(ev.notna(), np.nan).diff()


SHORT_SQUEEZE_AFTERMATH_D1_REGISTRY_151_225 = {
    "f49_ssaf_151_re_shorting_during_decline_indicator_21d_d1": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_151_re_shorting_during_decline_indicator_21d_d1},
    "f49_ssaf_152_post_event_window_gate_63d_d1": {"inputs": ["squeeze_event_date"], "func": f49_ssaf_152_post_event_window_gate_63d_d1},
}
