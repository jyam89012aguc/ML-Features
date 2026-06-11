"""volume_distribution_dryup d2 features 151-225 — second-derivative wrappers (acceleration; gap-fill extension)."""
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


def f06_vddu_151_dryup_after_climax_21d_d2(volume: pd.Series) -> pd.Series:
    vmean = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    vstd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    vz = _safe_div(volume - vmean, vstd)
    climax = (vz > 3.0).astype(float)
    climax_vol = volume.where(climax > 0, np.nan)
    prior_climax_max = climax_vol.shift(MDAYS).rolling(MDAYS + 1, min_periods=1).max()
    mean21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(mean21, prior_climax_max).diff().diff()


def f06_vddu_152_dryup_given_prior_spike_indicator_63d_d2(volume: pd.Series) -> pd.Series:
    vmean = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    vstd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    vz = _safe_div(volume - vmean, vstd)
    climax = (vz > 3.0).astype(float)
    climax_vol = volume.where(climax > 0, np.nan)
    prior_climax_max = climax_vol.shift(MDAYS).rolling(MDAYS + 1, min_periods=1).max()
    mean21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    had_spike = prior_climax_max.notna()
    dried = mean21 < (0.5 * prior_climax_max)
    out = (had_spike & dried).astype(float)
    nan_mask = mean21.isna() | vz.isna()
    return out.where(~nan_mask, np.nan).diff().diff()


def f06_vddu_153_days_since_last_3sigma_volume_spike_d2(volume: pd.Series) -> pd.Series:
    vmean = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    vstd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    vz = _safe_div(volume - vmean, vstd)
    spike = (vz > 3.0).astype(float).where(vz.notna(), np.nan)

    def _dsls(w):
        valid = ~np.isnan(w)
        if valid.sum() == 0:
            return np.nan
        idx = np.where((w == 1.0))[0]
        if idx.size == 0:
            return np.nan
        return float((len(w) - 1) - int(idx.max()))

    return spike.rolling(YDAYS, min_periods=MDAYS).apply(_dsls, raw=True).diff().diff()


VOLUME_DISTRIBUTION_DRYUP_D2_REGISTRY_151_225 = {
    "f06_vddu_151_dryup_after_climax_21d_d2": {"inputs": ["volume"], "func": f06_vddu_151_dryup_after_climax_21d_d2},
    "f06_vddu_152_dryup_given_prior_spike_indicator_63d_d2": {"inputs": ["volume"], "func": f06_vddu_152_dryup_given_prior_spike_indicator_63d_d2},
    "f06_vddu_153_days_since_last_3sigma_volume_spike_d2": {"inputs": ["volume"], "func": f06_vddu_153_days_since_last_3sigma_volume_spike_d2},
}
