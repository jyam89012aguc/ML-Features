"""peak_and_blowoff d2 features 151-225 — second-derivative wrappers (acceleration; gap-fill extension)."""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _erf_vec(z):
    sign = np.sign(z)
    a = np.abs(z)
    t = 1.0 / (1.0 + 0.3275911 * a)
    y = 1.0 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * np.exp(-a * a)
    return sign * y


def f01_pab_151_log_dist_above_504d_high_atr_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(_safe_log(high) - _safe_log(rmax), _safe_div(atr, close)).diff().diff()


def f01_pab_152_fib_extension_of_prior_swing_d2(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    prior_low = low.shift(QDAYS).rolling(YDAYS, min_periods=QDAYS).min()
    prior_high = high.shift(QDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    fib_target = prior_low + 1.618 * (prior_high - prior_low)
    return _safe_div(close, fib_target).diff().diff()


def f01_pab_153_ulcer_index_63d_d2(close: pd.Series) -> pd.Series:
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    dd_pct = _safe_div(close - rmax, rmax) * 100.0
    return np.sqrt((dd_pct ** 2).rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()


def f01_pab_154_pain_index_63d_d2(close: pd.Series) -> pd.Series:
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    dd_pct = _safe_div(close - rmax, rmax) * 100.0
    return dd_pct.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()


def f01_pab_155_tweezer_top_near_high_count_21d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = _safe_div(high, rmax) >= 0.95
    matching = _safe_div((high - high.shift(1)).abs(), high.shift(1)) < 0.005
    bearish = close < open_
    twz = (matching & near & near.shift(1).fillna(False) & bearish).astype(float)
    return twz.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_156_gravestone_doji_near_high_count_21d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = _safe_div(high, rmax) >= 0.95
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs()
    body_top = pd.concat([open_, close], axis=1).max(axis=1)
    body_bot = pd.concat([open_, close], axis=1).min(axis=1)
    upper_wick = high - body_top
    lower_wick = body_bot - low
    is_grave = (_safe_div(body, rng) < 0.10) & (_safe_div(lower_wick, rng) < 0.10) & (_safe_div(upper_wick, rng) > 0.70)
    return (is_grave & near).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_157_three_inside_down_near_high_count_63d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = _safe_div(high, rmax) >= 0.95
    bull1 = close.shift(2) > open_.shift(2)
    bear2 = close.shift(1) < open_.shift(1)
    inside2 = (low.shift(1) >= low.shift(2)) & (high.shift(1) <= high.shift(2))
    bear3 = (close < open_) & (close < close.shift(2))
    pat = (bull1 & bear2 & inside2 & bear3 & near).astype(float)
    return pat.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()


def f01_pab_158_three_outside_down_near_high_count_63d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = _safe_div(high, rmax) >= 0.95
    bull1 = close.shift(2) > open_.shift(2)
    engulf2 = (open_.shift(1) >= close.shift(2)) & (close.shift(1) < open_.shift(2)) & (close.shift(1) < open_.shift(1))
    bear3 = (close < open_) & (close < close.shift(1))
    pat = (bull1 & engulf2 & bear3 & near).astype(float)
    return pat.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()


def f01_pab_159_vertical_thrust_atr_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    thrust = (close - prior_max) > (3.0 * atr)
    return thrust.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_160_anderson_darling_stat_returns_63d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()

    def _ad(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        x = np.sort(w[valid])
        n = len(x)
        mu = x.mean()
        sd = x.std(ddof=1)
        if sd == 0 or not np.isfinite(sd):
            return np.nan
        z = (x - mu) / sd
        F = 0.5 * (1.0 + _erf_vec(z / np.sqrt(2.0)))
        F = np.clip(F, 1e-12, 1.0 - 1e-12)
        i = np.arange(1, n + 1)
        s = ((2 * i - 1) / n) * (np.log(F) + np.log(1.0 - F[::-1]))
        return -float(n) - float(s.sum())

    return r.rolling(QDAYS, min_periods=MDAYS).apply(_ad, raw=True).diff().diff()


PEAK_AND_BLOWOFF_D2_REGISTRY_151_225 = {
    "f01_pab_151_log_dist_above_504d_high_atr_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_151_log_dist_above_504d_high_atr_d2},
    "f01_pab_152_fib_extension_of_prior_swing_d2": {"inputs": ["close", "low", "high"], "func": f01_pab_152_fib_extension_of_prior_swing_d2},
    "f01_pab_153_ulcer_index_63d_d2": {"inputs": ["close"], "func": f01_pab_153_ulcer_index_63d_d2},
    "f01_pab_154_pain_index_63d_d2": {"inputs": ["close"], "func": f01_pab_154_pain_index_63d_d2},
    "f01_pab_155_tweezer_top_near_high_count_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_155_tweezer_top_near_high_count_21d_d2},
    "f01_pab_156_gravestone_doji_near_high_count_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_156_gravestone_doji_near_high_count_21d_d2},
    "f01_pab_157_three_inside_down_near_high_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_157_three_inside_down_near_high_count_63d_d2},
    "f01_pab_158_three_outside_down_near_high_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_158_three_outside_down_near_high_count_63d_d2},
    "f01_pab_159_vertical_thrust_atr_count_21d_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_159_vertical_thrust_atr_count_21d_d2},
    "f01_pab_160_anderson_darling_stat_returns_63d_d2": {"inputs": ["close"], "func": f01_pab_160_anderson_darling_stat_returns_63d_d2},
}
