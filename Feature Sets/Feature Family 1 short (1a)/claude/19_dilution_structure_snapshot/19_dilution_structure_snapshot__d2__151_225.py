"""dilution_structure_snapshot d2 features 151-225 — second-derivative wrappers (gap-fill extension)."""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
QQTRS = 4


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


def f19_dssp_151_atm_offering_signature_63d_d2(sharesbas: pd.Series) -> pd.Series:
    prior = sharesbas.shift(1)
    delta = sharesbas - prior
    pct = _safe_div(delta, prior)
    trickle = ((delta > 0) & (pct < 0.005)).astype(float)
    return trickle.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()


def f19_dssp_152_pipe_event_indicator_q_d2(shareswa: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    sw_qoq = shareswa.pct_change(QDAYS)
    nc_qoq = ncfcommon.diff(QDAYS)
    sw_z = _rolling_zscore(sw_qoq, 8 * QDAYS, min_periods=2 * QDAYS)
    nc_z = _rolling_zscore(nc_qoq, 8 * QDAYS, min_periods=2 * QDAYS)
    return ((sw_z > 2.0) & (nc_z > 2.0)).astype(float).diff().diff()


def f19_dssp_153_sbc_dilution_share_yoy_d2(sbcomp: pd.Series, sharesbas: pd.Series, close: pd.Series) -> pd.Series:
    sbc_ttm = sbcomp.rolling(YDAYS, min_periods=QDAYS).sum()
    sbc_per_close = _safe_div(sbc_ttm, close)
    delta_shares_yoy = sharesbas.diff(YDAYS)
    return _safe_div(sbc_per_close, delta_shares_yoy).diff().diff()


def f19_dssp_154_dilution_during_drawdown_indicator_63d_d2(sharesbas: pd.Series, close: pd.Series) -> pd.Series:
    d63 = sharesbas.diff(QDAYS)
    z = _rolling_zscore(d63, YDAYS, min_periods=QDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return ((z > 2.0) & (dd < -0.20)).astype(float).diff().diff()


DILUTION_STRUCTURE_SNAPSHOT_D2_REGISTRY_151_225 = {
    "f19_dssp_151_atm_offering_signature_63d_d2": {"inputs": ["sharesbas"], "func": f19_dssp_151_atm_offering_signature_63d_d2},
    "f19_dssp_152_pipe_event_indicator_q_d2": {"inputs": ["shareswa", "ncfcommon"], "func": f19_dssp_152_pipe_event_indicator_q_d2},
    "f19_dssp_153_sbc_dilution_share_yoy_d2": {"inputs": ["sbcomp", "sharesbas", "close"], "func": f19_dssp_153_sbc_dilution_share_yoy_d2},
    "f19_dssp_154_dilution_during_drawdown_indicator_63d_d2": {"inputs": ["sharesbas", "close"], "func": f19_dssp_154_dilution_during_drawdown_indicator_63d_d2},
}
