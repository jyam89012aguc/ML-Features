"""distribution_signature d2 features 151-225 — second-derivative wrappers (acceleration; gap-fill extension)."""
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


def f07_dsig_151_spring_upthrust_ratio_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    new_high = high >= rmax21
    new_low = low <= rmin21
    upthrust = (new_high & (pos < (1.0 / 3.0))).astype(float)
    spring = (new_low & (pos > (2.0 / 3.0))).astype(float)
    up_ct = upthrust.rolling(QDAYS, min_periods=MDAYS).sum()
    sp_ct = spring.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(up_ct, sp_ct).diff().diff()


def f07_dsig_152_distribution_day_after_252d_high_count_42d_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    ret = _safe_log(close).diff()
    dist_day = ((ret < -0.002) & (volume > volume.shift(1))).astype(float)
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_new_high = (high >= rmax252) & rmax252.notna()
    HORIZON = 2 * MDAYS
    n = len(close)
    pos = np.arange(n, dtype=np.float64)
    high_pos = np.where(is_new_high.values, pos, -np.inf)
    cm = np.fmax.accumulate(high_pos)
    last_high_idx = pd.Series(np.where(cm == -np.inf, np.nan, cm), index=close.index)
    dd_arr = dist_day.values.astype(float)
    dd_safe = np.where(np.isnan(dd_arr), 0.0, dd_arr)
    cum_dd = np.concatenate(([0.0], np.cumsum(dd_safe)))
    t_arr = pos.astype(np.int64)
    lh = last_high_idx.values
    window_start = t_arr - HORIZON + 1
    qualifies = (~np.isnan(lh)) & (lh >= window_start)
    lh_int = np.where(np.isnan(lh), 0, lh).astype(np.int64)
    raw = cum_dd[t_arr + 1] - cum_dd[lh_int + 1]
    out = np.where(qualifies, raw, np.nan)
    return pd.Series(out, index=close.index).diff().diff()


DISTRIBUTION_SIGNATURE_D2_REGISTRY_151_225 = {
    "f07_dsig_151_spring_upthrust_ratio_63d_d2": {"inputs": ["close", "high", "low"], "func": f07_dsig_151_spring_upthrust_ratio_63d_d2},
    "f07_dsig_152_distribution_day_after_252d_high_count_42d_d2": {"inputs": ["close", "volume", "high"], "func": f07_dsig_152_distribution_day_after_252d_high_count_42d_d2},
}
