"""moving_average_extension_dynamics d2 features 151-225 — second-derivative wrappers (acceleration; gap-fill extension)."""
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


def _anchored_vwap_from_252d_low(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    n = len(close)
    pos = np.arange(n, dtype=np.float64)
    cv = (close * volume).values.astype(float)
    vv = volume.values.astype(float)
    cum_pv = np.concatenate(([0.0], np.cumsum(np.where(np.isnan(cv), 0.0, cv))))
    cum_v = np.concatenate(([0.0], np.cumsum(np.where(np.isnan(vv), 0.0, vv))))
    MIN_PERIODS = QDAYS

    def _argmin_window(w):
        if np.isnan(w).all():
            return np.nan
        return float(np.nanargmin(w))

    win_argmin = low.rolling(YDAYS, min_periods=MIN_PERIODS).apply(_argmin_window, raw=True)
    win_len = np.minimum(pos + 1.0, float(YDAYS))
    abs_idx = pos - (win_len - 1.0) + win_argmin.values
    valid = ~np.isnan(abs_idx)
    abs_idx_safe = np.where(valid, abs_idx, 0).astype(np.int64)
    t_int = pos.astype(np.int64)
    pv_sum = cum_pv[t_int + 1] - cum_pv[abs_idx_safe]
    v_sum = cum_v[t_int + 1] - cum_v[abs_idx_safe]
    vwap = np.where((v_sum > 0) & valid, pv_sum / np.where(v_sum == 0, np.nan, v_sum), np.nan)
    return pd.Series(vwap, index=close.index)


def _psar_numpy(high_arr, low_arr, af_init=0.02, af_step=0.02, af_max=0.2):
    n = len(high_arr)
    psar = np.full(n, np.nan, dtype=np.float64)
    if n < 2:
        return psar
    if np.isnan(high_arr[0]) or np.isnan(low_arr[0]) or np.isnan(high_arr[1]) or np.isnan(low_arr[1]):
        return psar
    bull = high_arr[1] >= high_arr[0]
    if bull:
        sar = low_arr[0]
        ep = high_arr[1]
    else:
        sar = high_arr[0]
        ep = low_arr[1]
    af = af_init
    psar[1] = sar
    for i in range(2, n):
        h = high_arr[i]
        l = low_arr[i]
        prev_h = high_arr[i - 1]
        prev_l = low_arr[i - 1]
        if np.isnan(h) or np.isnan(l):
            psar[i] = np.nan
            continue
        sar = sar + af * (ep - sar)
        if bull:
            if not np.isnan(prev_l):
                sar = min(sar, prev_l)
            if i >= 2 and not np.isnan(low_arr[i - 2]):
                sar = min(sar, low_arr[i - 2])
            if l < sar:
                bull = False
                sar = ep
                ep = l
                af = af_init
            else:
                if h > ep:
                    ep = h
                    af = min(af + af_step, af_max)
        else:
            if not np.isnan(prev_h):
                sar = max(sar, prev_h)
            if i >= 2 and not np.isnan(high_arr[i - 2]):
                sar = max(sar, high_arr[i - 2])
            if h > sar:
                bull = True
                sar = ep
                ep = h
                af = af_init
            else:
                if l < ep:
                    ep = l
                    af = min(af + af_step, af_max)
        psar[i] = sar
    return psar


def _wilder_atr_numpy(high_arr, low_arr, close_arr, n):
    m = len(close_arr)
    tr = np.full(m, np.nan, dtype=np.float64)
    for i in range(1, m):
        if np.isnan(high_arr[i]) or np.isnan(low_arr[i]) or np.isnan(close_arr[i - 1]):
            tr[i] = np.nan
            continue
        tr[i] = max(high_arr[i] - low_arr[i], abs(high_arr[i] - close_arr[i - 1]), abs(low_arr[i] - close_arr[i - 1]))
    atr = np.full(m, np.nan, dtype=np.float64)
    if m <= n:
        return atr
    seed_vals = tr[1:n + 1]
    seed_valid = seed_vals[~np.isnan(seed_vals)]
    if len(seed_valid) < max(n // 3, 2):
        return atr
    atr[n] = float(np.mean(seed_valid))
    for i in range(n + 1, m):
        if np.isnan(tr[i]) or np.isnan(atr[i - 1]):
            atr[i] = atr[i - 1]
        else:
            atr[i] = (atr[i - 1] * (n - 1) + tr[i]) / n
    return atr


def _supertrend_numpy(high_arr, low_arr, close_arr, period=10, factor=3.0):
    n = len(close_arr)
    atr = _wilder_atr_numpy(high_arr, low_arr, close_arr, period)
    hl2 = (high_arr + low_arr) / 2.0
    upper_basic = hl2 + factor * atr
    lower_basic = hl2 - factor * atr
    final_upper = np.full(n, np.nan, dtype=np.float64)
    final_lower = np.full(n, np.nan, dtype=np.float64)
    supert = np.full(n, np.nan, dtype=np.float64)
    for i in range(n):
        if np.isnan(upper_basic[i]) or np.isnan(lower_basic[i]) or np.isnan(close_arr[i]):
            continue
        if i == 0 or np.isnan(final_upper[i - 1]):
            final_upper[i] = upper_basic[i]
            final_lower[i] = lower_basic[i]
            supert[i] = lower_basic[i] if close_arr[i] >= hl2[i] else upper_basic[i]
            continue
        if upper_basic[i] < final_upper[i - 1] or close_arr[i - 1] > final_upper[i - 1]:
            final_upper[i] = upper_basic[i]
        else:
            final_upper[i] = final_upper[i - 1]
        if lower_basic[i] > final_lower[i - 1] or close_arr[i - 1] < final_lower[i - 1]:
            final_lower[i] = lower_basic[i]
        else:
            final_lower[i] = final_lower[i - 1]
        prev_st = supert[i - 1]
        if not np.isnan(prev_st) and prev_st == final_upper[i - 1]:
            if close_arr[i] > final_upper[i]:
                supert[i] = final_lower[i]
            else:
                supert[i] = final_upper[i]
        else:
            if close_arr[i] < final_lower[i]:
                supert[i] = final_upper[i]
            else:
                supert[i] = final_lower[i]
    return supert


def f08_maed_151_anchored_vwap_from_252d_low_distance_d2(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    vwap = _anchored_vwap_from_252d_low(close, volume, low)
    return (_safe_log(close) - _safe_log(vwap)).diff().diff()


def f08_maed_152_parabolic_sar_distance_atr_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    psar = _psar_numpy(high.values.astype(float), low.values.astype(float))
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(close - pd.Series(psar, index=close.index), atr).diff().diff()


def f08_maed_153_chandelier_exit_distance_atr_22d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    PERIOD = 22
    h22 = high.rolling(PERIOD, min_periods=max(PERIOD // 3, 2)).max()
    atr22 = _atr(high, low, close, n=PERIOD)
    chandelier = h22 - 3.0 * atr22
    return _safe_div(close - chandelier, atr22).diff().diff()


def f08_maed_154_supertrend_distance_atr_10_3_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    st = _supertrend_numpy(high.values.astype(float), low.values.astype(float), close.values.astype(float), period=10, factor=3.0)
    atr10 = _atr(high, low, close, n=10)
    return _safe_div(close - pd.Series(st, index=close.index), atr10).diff().diff()


def f08_maed_155_bars_since_last_sma_200_touch_d2(close: pd.Series) -> pd.Series:
    sma200 = close.rolling(200, min_periods=100).mean()
    touch = (_safe_div((close - sma200).abs(), sma200) < 0.005).astype(float)
    touch = touch.where(sma200.notna() & close.notna(), np.nan)

    def _dsls(w):
        valid = ~np.isnan(w)
        if valid.sum() == 0:
            return np.nan
        idx = np.where(w == 1.0)[0]
        if idx.size == 0:
            return np.nan
        return float((len(w) - 1) - int(idx.max()))

    return touch.rolling(YDAYS, min_periods=MDAYS).apply(_dsls, raw=True).diff().diff()


MOVING_AVERAGE_EXTENSION_DYNAMICS_D2_REGISTRY_151_225 = {
    "f08_maed_151_anchored_vwap_from_252d_low_distance_d2": {"inputs": ["close", "volume", "low"], "func": f08_maed_151_anchored_vwap_from_252d_low_distance_d2},
    "f08_maed_152_parabolic_sar_distance_atr_d2": {"inputs": ["high", "low", "close"], "func": f08_maed_152_parabolic_sar_distance_atr_d2},
    "f08_maed_153_chandelier_exit_distance_atr_22d_d2": {"inputs": ["high", "low", "close"], "func": f08_maed_153_chandelier_exit_distance_atr_22d_d2},
    "f08_maed_154_supertrend_distance_atr_10_3_d2": {"inputs": ["high", "low", "close"], "func": f08_maed_154_supertrend_distance_atr_10_3_d2},
    "f08_maed_155_bars_since_last_sma_200_touch_d2": {"inputs": ["close"], "func": f08_maed_155_bars_since_last_sma_200_touch_d2},
}
