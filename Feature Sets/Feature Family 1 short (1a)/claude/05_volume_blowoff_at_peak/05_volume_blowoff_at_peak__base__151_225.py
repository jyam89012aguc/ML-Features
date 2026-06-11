"""volume_blowoff_at_peak base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for climactic-volume detection.
This file carries indices 151-155 (5 distinct hypotheses). Reserved range up to 225.

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
#                    FEATURES 151-155
# ============================================================


def f05_vbpk_151_amihud_illiquidity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of |log return| / dollar-volume over 63d — Amihud illiquidity proxy."""
    r = _safe_log(close).diff().abs()
    dv = (close * volume).replace(0, np.nan)
    ratio = _safe_div(r, dv)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean()


def f05_vbpk_152_volume_zscore_peak_then_5d_decay(volume: pd.Series) -> pd.Series:
    """Post-climax decay: mean(volume over last 5d) / volume at the peak bar within trailing 21d.

    PIT: post-peak bars (the 5-day mean) are anchored at t and look backward over the last
    5 bars (t-4..t); the peak bar is identified from the trailing 21-day window ending at t.
    Lower values indicate sharper decay since the climax.
    """
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

    return v.rolling(MDAYS, min_periods=WDAYS).apply(_ratio, raw=True)


def f05_vbpk_153_volume_pyramid_buildup_5d(volume: pd.Series) -> pd.Series:
    """Count of 5d windows within trailing 21d where volume strictly accelerates day-over-day."""
    v = volume.astype(float)
    accel = (
        (v.shift(4) < v.shift(3))
        & (v.shift(3) < v.shift(2))
        & (v.shift(2) < v.shift(1))
        & (v.shift(1) < v)
    ).astype(float)
    # require all five bars present
    have_all = v.notna() & v.shift(1).notna() & v.shift(2).notna() & v.shift(3).notna() & v.shift(4).notna()
    accel = accel.where(have_all, np.nan)
    return accel.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_154_penny_pump_signature(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Boolean (1/0): close < 5 AND vol z-score 252d > 4 AND 5d log return > 0.5."""
    vmean = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    vstd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    vz = _safe_div(volume - vmean, vstd)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    cond = (close < 5.0) & (vz > 4.0) & (r5 > 0.5)
    out = cond.astype(float)
    # propagate NaN where any operand is missing
    nan_mask = close.isna() | vz.isna() | r5.isna()
    return out.where(~nan_mask, np.nan)


def f05_vbpk_155_volume_decay_5d_post_climax(volume: pd.Series) -> pd.Series:
    """5d-mean volume divided by prior 21d max volume — decay-since-last-spike measure.

    The 21d max is computed over the bars strictly before the trailing 5d window
    (i.e. shifted by 5) so the climax and the post-climax mean do not overlap.
    """
    mean5 = volume.rolling(WDAYS, min_periods=WDAYS).mean()
    prior_max21 = volume.shift(WDAYS).rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(mean5, prior_max21)


# ============================================================
#                    REGISTRY
# ============================================================

VOLUME_BLOWOFF_AT_PEAK_BASE_REGISTRY_151_225 = {
    "f05_vbpk_151_amihud_illiquidity_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_151_amihud_illiquidity_63d},
    "f05_vbpk_152_volume_zscore_peak_then_5d_decay": {"inputs": ["volume"], "func": f05_vbpk_152_volume_zscore_peak_then_5d_decay},
    "f05_vbpk_153_volume_pyramid_buildup_5d": {"inputs": ["volume"], "func": f05_vbpk_153_volume_pyramid_buildup_5d},
    "f05_vbpk_154_penny_pump_signature": {"inputs": ["close", "volume"], "func": f05_vbpk_154_penny_pump_signature},
    "f05_vbpk_155_volume_decay_5d_post_climax": {"inputs": ["volume"], "func": f05_vbpk_155_volume_decay_5d_post_climax},
}
