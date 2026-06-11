"""volume_blowoff_at_peak d2 features 151-225 — second-derivative wrappers (acceleration; gap-fill extension)."""
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


def f05_vbpk_151_amihud_illiquidity_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    ratio = _safe_div(r, dv)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()


def f05_vbpk_152_volume_zscore_peak_then_5d_decay_d2(volume: pd.Series) -> pd.Series:
    v = volume.astype(float)

    def _ratio(w):
        if len(w) < 5:
            return np.nan
        valid = ~np.isnan(w)
        if valid.sum() < 5:
            return np.nan
        idx_peak = int(np.nanargmax(w))
        peak_vol = w[idx_peak]
        if not np.isfinite(peak_vol) or peak_vol <= 0:
            return np.nan
        last5 = w[-5:]
        if np.isnan(last5).any():
            return np.nan
        return float(np.mean(last5) / peak_vol)

    return v.rolling(MDAYS, min_periods=WDAYS).apply(_ratio, raw=True).diff().diff()


def f05_vbpk_153_volume_pyramid_buildup_5d_d2(volume: pd.Series) -> pd.Series:
    v = volume.astype(float)
    accel = (
        (v.shift(4) < v.shift(3))
        & (v.shift(3) < v.shift(2))
        & (v.shift(2) < v.shift(1))
        & (v.shift(1) < v)
    ).astype(float)
    have_all = v.notna() & v.shift(1).notna() & v.shift(2).notna() & v.shift(3).notna() & v.shift(4).notna()
    accel = accel.where(have_all, np.nan)
    return accel.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f05_vbpk_154_penny_pump_signature_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vmean = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    vstd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    vz = _safe_div(volume - vmean, vstd)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    cond = (close < 5.0) & (vz > 4.0) & (r5 > 0.5)
    out = cond.astype(float)
    nan_mask = close.isna() | vz.isna() | r5.isna()
    return out.where(~nan_mask, np.nan).diff().diff()


def f05_vbpk_155_volume_decay_5d_post_climax_d2(volume: pd.Series) -> pd.Series:
    mean5 = volume.rolling(WDAYS, min_periods=WDAYS).mean()
    prior_max21 = volume.shift(WDAYS).rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(mean5, prior_max21).diff().diff()


VOLUME_BLOWOFF_AT_PEAK_D2_REGISTRY_151_225 = {
    "f05_vbpk_151_amihud_illiquidity_63d_d2": {"inputs": ["close", "volume"], "func": f05_vbpk_151_amihud_illiquidity_63d_d2},
    "f05_vbpk_152_volume_zscore_peak_then_5d_decay_d2": {"inputs": ["volume"], "func": f05_vbpk_152_volume_zscore_peak_then_5d_decay_d2},
    "f05_vbpk_153_volume_pyramid_buildup_5d_d2": {"inputs": ["volume"], "func": f05_vbpk_153_volume_pyramid_buildup_5d_d2},
    "f05_vbpk_154_penny_pump_signature_d2": {"inputs": ["close", "volume"], "func": f05_vbpk_154_penny_pump_signature_d2},
    "f05_vbpk_155_volume_decay_5d_post_climax_d2": {"inputs": ["volume"], "func": f05_vbpk_155_volume_decay_5d_post_climax_d2},
}
