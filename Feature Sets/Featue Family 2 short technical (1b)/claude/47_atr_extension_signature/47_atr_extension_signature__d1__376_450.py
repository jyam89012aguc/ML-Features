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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _bars_since_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_vwap(close, volume, n):
    num = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    den = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _camarilla_h1(high, low, close):
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    return pc + (ph - pl) * 1.1 / 12.0


def _camarilla_h2(high, low, close):
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    return pc + (ph - pl) * 1.1 / 6.0


def _camarilla_h3(high, low, close):
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    return pc + (ph - pl) * 1.1 / 4.0


def _camarilla_h4(high, low, close):
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    return pc + (ph - pl) * 1.1 / 2.0


def _camarilla_l1(high, low, close):
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    return pc - (ph - pl) * 1.1 / 12.0


def _camarilla_l2(high, low, close):
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    return pc - (ph - pl) * 1.1 / 6.0


def _camarilla_l3(high, low, close):
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    return pc - (ph - pl) * 1.1 / 4.0


def _camarilla_l4(high, low, close):
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    return pc - (ph - pl) * 1.1 / 2.0


def f47_atxs_376_close_minus_camarilla_h1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _camarilla_h1(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_377_close_minus_camarilla_h2_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _camarilla_h2(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_378_close_minus_camarilla_h3_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _camarilla_h3(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_379_close_minus_camarilla_h4_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _camarilla_h4(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_380_close_minus_camarilla_l1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _camarilla_l1(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_381_close_minus_camarilla_l2_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _camarilla_l2(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_382_close_minus_camarilla_l3_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _camarilla_l3(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_383_close_minus_camarilla_l4_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _camarilla_l4(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_384_close_above_camarilla_h4_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (close > _camarilla_h4(high, low, close)).astype(float).where(_camarilla_h4(high, low, close).notna(), np.nan)


def f47_atxs_385_close_above_camarilla_h3_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (close > _camarilla_h3(high, low, close)).astype(float).where(_camarilla_h3(high, low, close).notna(), np.nan)


def f47_atxs_386_close_minus_woodie_pivot_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2.0 * close.shift(1)) / 4.0
    return _safe_div(close - p, _atr(high, low, close, MDAYS))


def f47_atxs_387_close_minus_woodie_R1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2.0 * close.shift(1)) / 4.0
    return _safe_div(close - (2.0 * p - low.shift(1)), _atr(high, low, close, MDAYS))


def f47_atxs_388_close_minus_woodie_R2_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2.0 * close.shift(1)) / 4.0
    return _safe_div(close - (p + high.shift(1) - low.shift(1)), _atr(high, low, close, MDAYS))


def f47_atxs_389_close_minus_woodie_S1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2.0 * close.shift(1)) / 4.0
    return _safe_div(close - (2.0 * p - high.shift(1)), _atr(high, low, close, MDAYS))


def f47_atxs_390_close_minus_woodie_S2_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2.0 * close.shift(1)) / 4.0
    return _safe_div(close - (p - (high.shift(1) - low.shift(1))), _atr(high, low, close, MDAYS))


def _demark_x(high, low, close):
    ph = high.shift(1); pl = low.shift(1); pc = close.shift(1)
    bullish_prev = pc > (ph + pl) / 2.0
    bearish_prev = pc < (ph + pl) / 2.0
    x = pd.Series(np.nan, index=close.index)
    x = x.where(~bullish_prev, 2.0 * ph + pl + pc)
    x = x.where(~bearish_prev, ph + 2.0 * pl + pc)
    x = x.where(~(bullish_prev == bearish_prev), ph + pl + 2.0 * pc)
    return x / 4.0


def f47_atxs_391_close_minus_demark_x_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - _demark_x(high, low, close), _atr(high, low, close, MDAYS))


def f47_atxs_392_close_minus_demark_R1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    x = _demark_x(high, low, close)
    return _safe_div(close - (2.0 * x - low.shift(1)), _atr(high, low, close, MDAYS))


def f47_atxs_393_close_minus_demark_S1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    x = _demark_x(high, low, close)
    return _safe_div(close - (2.0 * x - high.shift(1)), _atr(high, low, close, MDAYS))


def _vwap_std(close, volume, n):
    vw = _rolling_vwap(close, volume, n)
    dev = close - vw
    return dev.rolling(n, min_periods=max(n // 3, 2)).std()


def f47_atxs_394_close_minus_vwap63_upper1sigma_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    sd = _vwap_std(close, volume, QDAYS)
    return _safe_div(close - (vw + sd), _atr(high, low, close, MDAYS))


def f47_atxs_395_close_minus_vwap63_upper2sigma_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    sd = _vwap_std(close, volume, QDAYS)
    return _safe_div(close - (vw + 2.0 * sd), _atr(high, low, close, MDAYS))


def f47_atxs_396_close_minus_vwap63_upper3sigma_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    sd = _vwap_std(close, volume, QDAYS)
    return _safe_div(close - (vw + 3.0 * sd), _atr(high, low, close, MDAYS))


def f47_atxs_397_close_minus_vwap63_lower1sigma_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    sd = _vwap_std(close, volume, QDAYS)
    return _safe_div(close - (vw - sd), _atr(high, low, close, MDAYS))


def f47_atxs_398_close_above_vwap63_upper2sigma_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    sd = _vwap_std(close, volume, QDAYS)
    return (close > (vw + 2.0 * sd)).astype(float).where(sd.notna(), np.nan)


def f47_atxs_399_vwap63_band_position(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    sd = _vwap_std(close, volume, QDAYS)
    return _safe_div(close - (vw - 2.0 * sd), 4.0 * sd)


def f47_atxs_400_vwap63_bandwidth_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sd = _vwap_std(close, volume, QDAYS)
    return _safe_div(4.0 * sd, _atr(high, low, close, MDAYS))


def f47_atxs_401_bars_since_close_above_vwap63_upper2sigma(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    sd = _vwap_std(close, volume, QDAYS)
    return _bars_since_true(close > (vw + 2.0 * sd))


def f47_atxs_402_close_over_q90_close_past_21(close: pd.Series) -> pd.Series:
    return _safe_div(close, close.rolling(MDAYS, min_periods=WDAYS).quantile(0.90))


def f47_atxs_403_close_over_q90_close_past_63(close: pd.Series) -> pd.Series:
    return _safe_div(close, close.rolling(QDAYS, min_periods=MDAYS).quantile(0.90))


def f47_atxs_404_close_over_q90_close_past_252(close: pd.Series) -> pd.Series:
    return _safe_div(close, close.rolling(YDAYS, min_periods=QDAYS).quantile(0.90))


def f47_atxs_405_close_over_q95_close_past_252(close: pd.Series) -> pd.Series:
    return _safe_div(close, close.rolling(YDAYS, min_periods=QDAYS).quantile(0.95))


def f47_atxs_406_close_over_q99_close_past_252(close: pd.Series) -> pd.Series:
    return _safe_div(close, close.rolling(YDAYS, min_periods=QDAYS).quantile(0.99))


def f47_atxs_407_close_below_q10_close_past_21_state(close: pd.Series) -> pd.Series:
    return (close < close.rolling(MDAYS, min_periods=WDAYS).quantile(0.10)).astype(float).where(close.shift(1).notna(), np.nan)


def f47_atxs_408_close_above_q90_close_past_21_state(close: pd.Series) -> pd.Series:
    return (close > close.rolling(MDAYS, min_periods=WDAYS).quantile(0.90)).astype(float).where(close.shift(1).notna(), np.nan)


def f47_atxs_409_close_above_q95_close_past_252_state(close: pd.Series) -> pd.Series:
    return (close > close.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)).astype(float).where(close.shift(1).notna(), np.nan)


def f47_atxs_410_count_close_above_q90_close_252_past_63(close: pd.Series) -> pd.Series:
    q90 = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (close > q90).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(q90.notna(), np.nan)


def f47_atxs_411_close_pct_rank_vol_weighted_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _f_pos(c_w, v_w):
        valid = ~(np.isnan(c_w) | np.isnan(v_w))
        if valid.sum() < MDAYS:
            return np.nan
        c = c_w[valid]; v = v_w[valid]
        if v.sum() == 0:
            return np.nan
        cur = c[-1]
        return float(((c < cur) * v).sum() / v.sum())
    n = len(close); out = np.full(n, np.nan)
    c_arr = close.to_numpy(dtype=float); v_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - QDAYS + 1)
        out[t] = _f_pos(c_arr[lo : t + 1], v_arr[lo : t + 1])
    return pd.Series(out, index=close.index)


def f47_atxs_412_close_pct_rank_vol_weighted_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    n = len(close); out = np.full(n, np.nan)
    c_arr = close.to_numpy(dtype=float); v_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - YDAYS + 1)
        c_w = c_arr[lo : t + 1]; v_w = v_arr[lo : t + 1]
        valid = ~(np.isnan(c_w) | np.isnan(v_w))
        if valid.sum() < QDAYS:
            continue
        c = c_w[valid]; v = v_w[valid]
        if v.sum() == 0:
            continue
        cur = c[-1]
        out[t] = float(((c < cur) * v).sum() / v.sum())
    return pd.Series(out, index=close.index)


def f47_atxs_413_sharpe_pct_rank_252(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    sh = _safe_div(r.rolling(MDAYS, min_periods=WDAYS).mean(), r.rolling(MDAYS, min_periods=WDAYS).std())
    return sh.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_414_sortino_pct_rank_252(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    dsd = r.where(r < 0).rolling(MDAYS, min_periods=WDAYS).std()
    so = _safe_div(mn, dsd)
    return so.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_415_calmar_ratio_252(close: pd.Series) -> pd.Series:
    ret_252 = close.pct_change(YDAYS)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    max_dd = dd.rolling(YDAYS, min_periods=QDAYS).min().abs()
    return _safe_div(ret_252, max_dd)


def f47_atxs_416_information_ratio_proxy_21d(close: pd.Series) -> pd.Series:
    r21 = close.pct_change(MDAYS)
    mean_r21 = r21.rolling(YDAYS, min_periods=QDAYS).mean()
    sd21 = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(r21 - mean_r21, sd21)


def f47_atxs_417_vol_of_sharpe_252(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    sh = _safe_div(r.rolling(MDAYS, min_periods=WDAYS).mean(), r.rolling(MDAYS, min_periods=WDAYS).std())
    return sh.rolling(YDAYS, min_periods=QDAYS).std()


def f47_atxs_418_return_to_pain_ratio_21(high: pd.Series, close: pd.Series) -> pd.Series:
    ret = close.pct_change(MDAYS)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    dd_21 = dd.rolling(MDAYS, min_periods=WDAYS).min().abs()
    return _safe_div(ret, dd_21)


def f47_atxs_419_ret5_over_atr5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - close.shift(WDAYS), _atr(high, low, close, WDAYS))


def f47_atxs_420_ret10_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - close.shift(10), _atr(high, low, close, MDAYS))


def f47_atxs_421_ret21_over_atr5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - close.shift(MDAYS), _atr(high, low, close, WDAYS))


def f47_atxs_422_ret63_over_atr21_alt(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - close.shift(QDAYS), _atr(high, low, close, MDAYS))


def f47_atxs_423_ret252_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - close.shift(YDAYS), _atr(high, low, close, MDAYS))


def f47_atxs_424_ret504_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - close.shift(DDAYS_2Y), _atr(high, low, close, MDAYS))


def f47_atxs_425_ret10_over_atr10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - close.shift(10), _atr(high, low, close, 10))


def f47_atxs_426_ret63_over_std63_close(close: pd.Series) -> pd.Series:
    return _safe_div(close - close.shift(QDAYS), close.rolling(QDAYS, min_periods=MDAYS).std())


def f47_atxs_427_std_hl_range_past_21(high: pd.Series, low: pd.Series) -> pd.Series:
    return (high - low).rolling(MDAYS, min_periods=WDAYS).std()


def f47_atxs_428_std_hl_range_past_63(high: pd.Series, low: pd.Series) -> pd.Series:
    return (high - low).rolling(QDAYS, min_periods=MDAYS).std()


def f47_atxs_429_hl_range_zscore_252(high: pd.Series, low: pd.Series) -> pd.Series:
    return _rolling_zscore(high - low, YDAYS, min_periods=QDAYS)


def f47_atxs_430_hl_range_pct_rank_252(high: pd.Series, low: pd.Series) -> pd.Series:
    return (high - low).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_431_range_expansion_rate_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r = (high - low).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(r - r.shift(MDAYS), _atr(high, low, close, MDAYS))


def f47_atxs_432_max_range_over_median_range_21(high: pd.Series, low: pd.Series) -> pd.Series:
    r = high - low
    return _safe_div(r.rolling(MDAYS, min_periods=WDAYS).max(), r.rolling(MDAYS, min_periods=WDAYS).median())


def f47_atxs_433_bars_since_hl_range_above_2xatr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _bars_since_true((high - low) > 2.0 * _atr(high, low, close, MDAYS))


def f47_atxs_434_count_hl_range_above_2xatr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cond = ((high - low) > 2.0 * _atr(high, low, close, MDAYS)).astype(float)
    return cond.rolling(YDAYS, min_periods=QDAYS).sum().where(cond.notna(), np.nan)


def f47_atxs_435_drawdown_from_21d_high_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(high.rolling(MDAYS, min_periods=WDAYS).max() - close, _atr(high, low, close, MDAYS))


def f47_atxs_436_drawdown_from_21d_high_over_atr5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(high.rolling(MDAYS, min_periods=WDAYS).max() - close, _atr(high, low, close, WDAYS))


def f47_atxs_437_drawdown_from_63d_high_over_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(high.rolling(QDAYS, min_periods=MDAYS).max() - close, _atr(high, low, close, QDAYS))


def f47_atxs_438_drawup_from_21d_low_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - low.rolling(MDAYS, min_periods=WDAYS).min(), _atr(high, low, close, MDAYS))


def f47_atxs_439_drawup_from_63d_low_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(close - low.rolling(QDAYS, min_periods=MDAYS).min(), _atr(high, low, close, MDAYS))


def f47_atxs_440_max_drawup_252_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    du = _safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, MDAYS))
    return du.rolling(YDAYS, min_periods=QDAYS).max()


def f47_atxs_441_drawup_drawdown_ratio_atr_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    du = _safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), a).rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(high.rolling(YDAYS, min_periods=QDAYS).max() - close, a).rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(du, dd)


def f47_atxs_442_drawup_drawdown_asymmetry_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    du = _safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), a)
    dd = _safe_div(high.rolling(YDAYS, min_periods=QDAYS).max() - close, a)
    return _safe_div(du - dd, du + dd)


def f47_atxs_443_close_cross_above_pivot_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    return ((close.shift(1) <= p.shift(1)) & (close > p)).astype(float).where(p.notna(), np.nan)


def f47_atxs_444_close_cross_above_R1_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * p - low.shift(1)
    return ((close.shift(1) <= r1.shift(1)) & (close > r1)).astype(float).where(r1.notna(), np.nan)


def f47_atxs_445_close_cross_above_R2_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = p + (high.shift(1) - low.shift(1))
    return ((close.shift(1) <= r2.shift(1)) & (close > r2)).astype(float).where(r2.notna(), np.nan)


def f47_atxs_446_close_cross_above_camarilla_h3_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h3 = _camarilla_h3(high, low, close)
    return ((close.shift(1) <= h3.shift(1)) & (close > h3)).astype(float).where(h3.notna(), np.nan)


def f47_atxs_447_close_cross_above_camarilla_h4_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h4 = _camarilla_h4(high, low, close)
    return ((close.shift(1) <= h4.shift(1)) & (close > h4)).astype(float).where(h4.notna(), np.nan)


def f47_atxs_448_bars_since_close_cross_above_R1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * p - low.shift(1)
    return _bars_since_true((close.shift(1) <= r1.shift(1)) & (close > r1))


def f47_atxs_449_bars_since_close_cross_above_R2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = p + (high.shift(1) - low.shift(1))
    return _bars_since_true((close.shift(1) <= r2.shift(1)) & (close > r2))


def f47_atxs_450_count_close_cross_above_R1_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * p - low.shift(1)
    ev = ((close.shift(1) <= r1.shift(1)) & (close > r1)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(r1.notna(), np.nan)


def f47_atxs_376_close_minus_camarilla_h1_over_atr21_d1(high, low, close):
    return f47_atxs_376_close_minus_camarilla_h1_over_atr21(high, low, close).diff()


def f47_atxs_377_close_minus_camarilla_h2_over_atr21_d1(high, low, close):
    return f47_atxs_377_close_minus_camarilla_h2_over_atr21(high, low, close).diff()


def f47_atxs_378_close_minus_camarilla_h3_over_atr21_d1(high, low, close):
    return f47_atxs_378_close_minus_camarilla_h3_over_atr21(high, low, close).diff()


def f47_atxs_379_close_minus_camarilla_h4_over_atr21_d1(high, low, close):
    return f47_atxs_379_close_minus_camarilla_h4_over_atr21(high, low, close).diff()


def f47_atxs_380_close_minus_camarilla_l1_over_atr21_d1(high, low, close):
    return f47_atxs_380_close_minus_camarilla_l1_over_atr21(high, low, close).diff()


def f47_atxs_381_close_minus_camarilla_l2_over_atr21_d1(high, low, close):
    return f47_atxs_381_close_minus_camarilla_l2_over_atr21(high, low, close).diff()


def f47_atxs_382_close_minus_camarilla_l3_over_atr21_d1(high, low, close):
    return f47_atxs_382_close_minus_camarilla_l3_over_atr21(high, low, close).diff()


def f47_atxs_383_close_minus_camarilla_l4_over_atr21_d1(high, low, close):
    return f47_atxs_383_close_minus_camarilla_l4_over_atr21(high, low, close).diff()


def f47_atxs_384_close_above_camarilla_h4_state_d1(high, low, close):
    return f47_atxs_384_close_above_camarilla_h4_state(high, low, close).diff()


def f47_atxs_385_close_above_camarilla_h3_state_d1(high, low, close):
    return f47_atxs_385_close_above_camarilla_h3_state(high, low, close).diff()


def f47_atxs_386_close_minus_woodie_pivot_over_atr21_d1(high, low, close):
    return f47_atxs_386_close_minus_woodie_pivot_over_atr21(high, low, close).diff()


def f47_atxs_387_close_minus_woodie_R1_over_atr21_d1(high, low, close):
    return f47_atxs_387_close_minus_woodie_R1_over_atr21(high, low, close).diff()


def f47_atxs_388_close_minus_woodie_R2_over_atr21_d1(high, low, close):
    return f47_atxs_388_close_minus_woodie_R2_over_atr21(high, low, close).diff()


def f47_atxs_389_close_minus_woodie_S1_over_atr21_d1(high, low, close):
    return f47_atxs_389_close_minus_woodie_S1_over_atr21(high, low, close).diff()


def f47_atxs_390_close_minus_woodie_S2_over_atr21_d1(high, low, close):
    return f47_atxs_390_close_minus_woodie_S2_over_atr21(high, low, close).diff()


def f47_atxs_391_close_minus_demark_x_over_atr21_d1(high, low, close):
    return f47_atxs_391_close_minus_demark_x_over_atr21(high, low, close).diff()


def f47_atxs_392_close_minus_demark_R1_over_atr21_d1(high, low, close):
    return f47_atxs_392_close_minus_demark_R1_over_atr21(high, low, close).diff()


def f47_atxs_393_close_minus_demark_S1_over_atr21_d1(high, low, close):
    return f47_atxs_393_close_minus_demark_S1_over_atr21(high, low, close).diff()


def f47_atxs_394_close_minus_vwap63_upper1sigma_over_atr21_d1(high, low, close, volume):
    return f47_atxs_394_close_minus_vwap63_upper1sigma_over_atr21(high, low, close, volume).diff()


def f47_atxs_395_close_minus_vwap63_upper2sigma_over_atr21_d1(high, low, close, volume):
    return f47_atxs_395_close_minus_vwap63_upper2sigma_over_atr21(high, low, close, volume).diff()


def f47_atxs_396_close_minus_vwap63_upper3sigma_over_atr21_d1(high, low, close, volume):
    return f47_atxs_396_close_minus_vwap63_upper3sigma_over_atr21(high, low, close, volume).diff()


def f47_atxs_397_close_minus_vwap63_lower1sigma_over_atr21_d1(high, low, close, volume):
    return f47_atxs_397_close_minus_vwap63_lower1sigma_over_atr21(high, low, close, volume).diff()


def f47_atxs_398_close_above_vwap63_upper2sigma_state_d1(close, volume):
    return f47_atxs_398_close_above_vwap63_upper2sigma_state(close, volume).diff()


def f47_atxs_399_vwap63_band_position_d1(close, volume):
    return f47_atxs_399_vwap63_band_position(close, volume).diff()


def f47_atxs_400_vwap63_bandwidth_over_atr21_d1(high, low, close, volume):
    return f47_atxs_400_vwap63_bandwidth_over_atr21(high, low, close, volume).diff()


def f47_atxs_401_bars_since_close_above_vwap63_upper2sigma_d1(close, volume):
    return f47_atxs_401_bars_since_close_above_vwap63_upper2sigma(close, volume).diff()


def f47_atxs_402_close_over_q90_close_past_21_d1(close):
    return f47_atxs_402_close_over_q90_close_past_21(close).diff()


def f47_atxs_403_close_over_q90_close_past_63_d1(close):
    return f47_atxs_403_close_over_q90_close_past_63(close).diff()


def f47_atxs_404_close_over_q90_close_past_252_d1(close):
    return f47_atxs_404_close_over_q90_close_past_252(close).diff()


def f47_atxs_405_close_over_q95_close_past_252_d1(close):
    return f47_atxs_405_close_over_q95_close_past_252(close).diff()


def f47_atxs_406_close_over_q99_close_past_252_d1(close):
    return f47_atxs_406_close_over_q99_close_past_252(close).diff()


def f47_atxs_407_close_below_q10_close_past_21_state_d1(close):
    return f47_atxs_407_close_below_q10_close_past_21_state(close).diff()


def f47_atxs_408_close_above_q90_close_past_21_state_d1(close):
    return f47_atxs_408_close_above_q90_close_past_21_state(close).diff()


def f47_atxs_409_close_above_q95_close_past_252_state_d1(close):
    return f47_atxs_409_close_above_q95_close_past_252_state(close).diff()


def f47_atxs_410_count_close_above_q90_close_252_past_63_d1(close):
    return f47_atxs_410_count_close_above_q90_close_252_past_63(close).diff()


def f47_atxs_411_close_pct_rank_vol_weighted_63_d1(close, volume):
    return f47_atxs_411_close_pct_rank_vol_weighted_63(close, volume).diff()


def f47_atxs_412_close_pct_rank_vol_weighted_252_d1(close, volume):
    return f47_atxs_412_close_pct_rank_vol_weighted_252(close, volume).diff()


def f47_atxs_413_sharpe_pct_rank_252_d1(close):
    return f47_atxs_413_sharpe_pct_rank_252(close).diff()


def f47_atxs_414_sortino_pct_rank_252_d1(close):
    return f47_atxs_414_sortino_pct_rank_252(close).diff()


def f47_atxs_415_calmar_ratio_252_d1(close):
    return f47_atxs_415_calmar_ratio_252(close).diff()


def f47_atxs_416_information_ratio_proxy_21d_d1(close):
    return f47_atxs_416_information_ratio_proxy_21d(close).diff()


def f47_atxs_417_vol_of_sharpe_252_d1(close):
    return f47_atxs_417_vol_of_sharpe_252(close).diff()


def f47_atxs_418_return_to_pain_ratio_21_d1(high, close):
    return f47_atxs_418_return_to_pain_ratio_21(high, close).diff()


def f47_atxs_419_ret5_over_atr5_d1(high, low, close):
    return f47_atxs_419_ret5_over_atr5(high, low, close).diff()


def f47_atxs_420_ret10_over_atr21_d1(high, low, close):
    return f47_atxs_420_ret10_over_atr21(high, low, close).diff()


def f47_atxs_421_ret21_over_atr5_d1(high, low, close):
    return f47_atxs_421_ret21_over_atr5(high, low, close).diff()


def f47_atxs_422_ret63_over_atr21_alt_d1(high, low, close):
    return f47_atxs_422_ret63_over_atr21_alt(high, low, close).diff()


def f47_atxs_423_ret252_over_atr21_d1(high, low, close):
    return f47_atxs_423_ret252_over_atr21(high, low, close).diff()


def f47_atxs_424_ret504_over_atr21_d1(high, low, close):
    return f47_atxs_424_ret504_over_atr21(high, low, close).diff()


def f47_atxs_425_ret10_over_atr10_d1(high, low, close):
    return f47_atxs_425_ret10_over_atr10(high, low, close).diff()


def f47_atxs_426_ret63_over_std63_close_d1(close):
    return f47_atxs_426_ret63_over_std63_close(close).diff()


def f47_atxs_427_std_hl_range_past_21_d1(high, low):
    return f47_atxs_427_std_hl_range_past_21(high, low).diff()


def f47_atxs_428_std_hl_range_past_63_d1(high, low):
    return f47_atxs_428_std_hl_range_past_63(high, low).diff()


def f47_atxs_429_hl_range_zscore_252_d1(high, low):
    return f47_atxs_429_hl_range_zscore_252(high, low).diff()


def f47_atxs_430_hl_range_pct_rank_252_d1(high, low):
    return f47_atxs_430_hl_range_pct_rank_252(high, low).diff()


def f47_atxs_431_range_expansion_rate_21_d1(high, low, close):
    return f47_atxs_431_range_expansion_rate_21(high, low, close).diff()


def f47_atxs_432_max_range_over_median_range_21_d1(high, low):
    return f47_atxs_432_max_range_over_median_range_21(high, low).diff()


def f47_atxs_433_bars_since_hl_range_above_2xatr21_d1(high, low, close):
    return f47_atxs_433_bars_since_hl_range_above_2xatr21(high, low, close).diff()


def f47_atxs_434_count_hl_range_above_2xatr21_252_d1(high, low, close):
    return f47_atxs_434_count_hl_range_above_2xatr21_252(high, low, close).diff()


def f47_atxs_435_drawdown_from_21d_high_over_atr21_d1(high, low, close):
    return f47_atxs_435_drawdown_from_21d_high_over_atr21(high, low, close).diff()


def f47_atxs_436_drawdown_from_21d_high_over_atr5_d1(high, low, close):
    return f47_atxs_436_drawdown_from_21d_high_over_atr5(high, low, close).diff()


def f47_atxs_437_drawdown_from_63d_high_over_atr63_d1(high, low, close):
    return f47_atxs_437_drawdown_from_63d_high_over_atr63(high, low, close).diff()


def f47_atxs_438_drawup_from_21d_low_over_atr21_d1(high, low, close):
    return f47_atxs_438_drawup_from_21d_low_over_atr21(high, low, close).diff()


def f47_atxs_439_drawup_from_63d_low_over_atr21_d1(high, low, close):
    return f47_atxs_439_drawup_from_63d_low_over_atr21(high, low, close).diff()


def f47_atxs_440_max_drawup_252_over_atr21_d1(high, low, close):
    return f47_atxs_440_max_drawup_252_over_atr21(high, low, close).diff()


def f47_atxs_441_drawup_drawdown_ratio_atr_252_d1(high, low, close):
    return f47_atxs_441_drawup_drawdown_ratio_atr_252(high, low, close).diff()


def f47_atxs_442_drawup_drawdown_asymmetry_atr_d1(high, low, close):
    return f47_atxs_442_drawup_drawdown_asymmetry_atr(high, low, close).diff()


def f47_atxs_443_close_cross_above_pivot_event_d1(high, low, close):
    return f47_atxs_443_close_cross_above_pivot_event(high, low, close).diff()


def f47_atxs_444_close_cross_above_R1_event_d1(high, low, close):
    return f47_atxs_444_close_cross_above_R1_event(high, low, close).diff()


def f47_atxs_445_close_cross_above_R2_event_d1(high, low, close):
    return f47_atxs_445_close_cross_above_R2_event(high, low, close).diff()


def f47_atxs_446_close_cross_above_camarilla_h3_event_d1(high, low, close):
    return f47_atxs_446_close_cross_above_camarilla_h3_event(high, low, close).diff()


def f47_atxs_447_close_cross_above_camarilla_h4_event_d1(high, low, close):
    return f47_atxs_447_close_cross_above_camarilla_h4_event(high, low, close).diff()


def f47_atxs_448_bars_since_close_cross_above_R1_d1(high, low, close):
    return f47_atxs_448_bars_since_close_cross_above_R1(high, low, close).diff()


def f47_atxs_449_bars_since_close_cross_above_R2_d1(high, low, close):
    return f47_atxs_449_bars_since_close_cross_above_R2(high, low, close).diff()


def f47_atxs_450_count_close_cross_above_R1_past_63_d1(high, low, close):
    return f47_atxs_450_count_close_cross_above_R1_past_63(high, low, close).diff()


_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_CV = ["close", "volume"]
_HC = ["high", "close"]


ATR_EXTENSION_SIGNATURE_D1_REGISTRY_376_450 = {
    "f47_atxs_376_close_minus_camarilla_h1_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_376_close_minus_camarilla_h1_over_atr21_d1},
    "f47_atxs_377_close_minus_camarilla_h2_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_377_close_minus_camarilla_h2_over_atr21_d1},
    "f47_atxs_378_close_minus_camarilla_h3_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_378_close_minus_camarilla_h3_over_atr21_d1},
    "f47_atxs_379_close_minus_camarilla_h4_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_379_close_minus_camarilla_h4_over_atr21_d1},
    "f47_atxs_380_close_minus_camarilla_l1_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_380_close_minus_camarilla_l1_over_atr21_d1},
    "f47_atxs_381_close_minus_camarilla_l2_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_381_close_minus_camarilla_l2_over_atr21_d1},
    "f47_atxs_382_close_minus_camarilla_l3_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_382_close_minus_camarilla_l3_over_atr21_d1},
    "f47_atxs_383_close_minus_camarilla_l4_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_383_close_minus_camarilla_l4_over_atr21_d1},
    "f47_atxs_384_close_above_camarilla_h4_state_d1": {"inputs": _HLC, "func": f47_atxs_384_close_above_camarilla_h4_state_d1},
    "f47_atxs_385_close_above_camarilla_h3_state_d1": {"inputs": _HLC, "func": f47_atxs_385_close_above_camarilla_h3_state_d1},
    "f47_atxs_386_close_minus_woodie_pivot_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_386_close_minus_woodie_pivot_over_atr21_d1},
    "f47_atxs_387_close_minus_woodie_R1_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_387_close_minus_woodie_R1_over_atr21_d1},
    "f47_atxs_388_close_minus_woodie_R2_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_388_close_minus_woodie_R2_over_atr21_d1},
    "f47_atxs_389_close_minus_woodie_S1_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_389_close_minus_woodie_S1_over_atr21_d1},
    "f47_atxs_390_close_minus_woodie_S2_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_390_close_minus_woodie_S2_over_atr21_d1},
    "f47_atxs_391_close_minus_demark_x_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_391_close_minus_demark_x_over_atr21_d1},
    "f47_atxs_392_close_minus_demark_R1_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_392_close_minus_demark_R1_over_atr21_d1},
    "f47_atxs_393_close_minus_demark_S1_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_393_close_minus_demark_S1_over_atr21_d1},
    "f47_atxs_394_close_minus_vwap63_upper1sigma_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_394_close_minus_vwap63_upper1sigma_over_atr21_d1},
    "f47_atxs_395_close_minus_vwap63_upper2sigma_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_395_close_minus_vwap63_upper2sigma_over_atr21_d1},
    "f47_atxs_396_close_minus_vwap63_upper3sigma_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_396_close_minus_vwap63_upper3sigma_over_atr21_d1},
    "f47_atxs_397_close_minus_vwap63_lower1sigma_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_397_close_minus_vwap63_lower1sigma_over_atr21_d1},
    "f47_atxs_398_close_above_vwap63_upper2sigma_state_d1": {"inputs": _CV, "func": f47_atxs_398_close_above_vwap63_upper2sigma_state_d1},
    "f47_atxs_399_vwap63_band_position_d1": {"inputs": _CV, "func": f47_atxs_399_vwap63_band_position_d1},
    "f47_atxs_400_vwap63_bandwidth_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_400_vwap63_bandwidth_over_atr21_d1},
    "f47_atxs_401_bars_since_close_above_vwap63_upper2sigma_d1": {"inputs": _CV, "func": f47_atxs_401_bars_since_close_above_vwap63_upper2sigma_d1},
    "f47_atxs_402_close_over_q90_close_past_21_d1": {"inputs": ["close"], "func": f47_atxs_402_close_over_q90_close_past_21_d1},
    "f47_atxs_403_close_over_q90_close_past_63_d1": {"inputs": ["close"], "func": f47_atxs_403_close_over_q90_close_past_63_d1},
    "f47_atxs_404_close_over_q90_close_past_252_d1": {"inputs": ["close"], "func": f47_atxs_404_close_over_q90_close_past_252_d1},
    "f47_atxs_405_close_over_q95_close_past_252_d1": {"inputs": ["close"], "func": f47_atxs_405_close_over_q95_close_past_252_d1},
    "f47_atxs_406_close_over_q99_close_past_252_d1": {"inputs": ["close"], "func": f47_atxs_406_close_over_q99_close_past_252_d1},
    "f47_atxs_407_close_below_q10_close_past_21_state_d1": {"inputs": ["close"], "func": f47_atxs_407_close_below_q10_close_past_21_state_d1},
    "f47_atxs_408_close_above_q90_close_past_21_state_d1": {"inputs": ["close"], "func": f47_atxs_408_close_above_q90_close_past_21_state_d1},
    "f47_atxs_409_close_above_q95_close_past_252_state_d1": {"inputs": ["close"], "func": f47_atxs_409_close_above_q95_close_past_252_state_d1},
    "f47_atxs_410_count_close_above_q90_close_252_past_63_d1": {"inputs": ["close"], "func": f47_atxs_410_count_close_above_q90_close_252_past_63_d1},
    "f47_atxs_411_close_pct_rank_vol_weighted_63_d1": {"inputs": _CV, "func": f47_atxs_411_close_pct_rank_vol_weighted_63_d1},
    "f47_atxs_412_close_pct_rank_vol_weighted_252_d1": {"inputs": _CV, "func": f47_atxs_412_close_pct_rank_vol_weighted_252_d1},
    "f47_atxs_413_sharpe_pct_rank_252_d1": {"inputs": ["close"], "func": f47_atxs_413_sharpe_pct_rank_252_d1},
    "f47_atxs_414_sortino_pct_rank_252_d1": {"inputs": ["close"], "func": f47_atxs_414_sortino_pct_rank_252_d1},
    "f47_atxs_415_calmar_ratio_252_d1": {"inputs": ["close"], "func": f47_atxs_415_calmar_ratio_252_d1},
    "f47_atxs_416_information_ratio_proxy_21d_d1": {"inputs": ["close"], "func": f47_atxs_416_information_ratio_proxy_21d_d1},
    "f47_atxs_417_vol_of_sharpe_252_d1": {"inputs": ["close"], "func": f47_atxs_417_vol_of_sharpe_252_d1},
    "f47_atxs_418_return_to_pain_ratio_21_d1": {"inputs": _HC, "func": f47_atxs_418_return_to_pain_ratio_21_d1},
    "f47_atxs_419_ret5_over_atr5_d1": {"inputs": _HLC, "func": f47_atxs_419_ret5_over_atr5_d1},
    "f47_atxs_420_ret10_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_420_ret10_over_atr21_d1},
    "f47_atxs_421_ret21_over_atr5_d1": {"inputs": _HLC, "func": f47_atxs_421_ret21_over_atr5_d1},
    "f47_atxs_422_ret63_over_atr21_alt_d1": {"inputs": _HLC, "func": f47_atxs_422_ret63_over_atr21_alt_d1},
    "f47_atxs_423_ret252_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_423_ret252_over_atr21_d1},
    "f47_atxs_424_ret504_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_424_ret504_over_atr21_d1},
    "f47_atxs_425_ret10_over_atr10_d1": {"inputs": _HLC, "func": f47_atxs_425_ret10_over_atr10_d1},
    "f47_atxs_426_ret63_over_std63_close_d1": {"inputs": ["close"], "func": f47_atxs_426_ret63_over_std63_close_d1},
    "f47_atxs_427_std_hl_range_past_21_d1": {"inputs": ["high", "low"], "func": f47_atxs_427_std_hl_range_past_21_d1},
    "f47_atxs_428_std_hl_range_past_63_d1": {"inputs": ["high", "low"], "func": f47_atxs_428_std_hl_range_past_63_d1},
    "f47_atxs_429_hl_range_zscore_252_d1": {"inputs": ["high", "low"], "func": f47_atxs_429_hl_range_zscore_252_d1},
    "f47_atxs_430_hl_range_pct_rank_252_d1": {"inputs": ["high", "low"], "func": f47_atxs_430_hl_range_pct_rank_252_d1},
    "f47_atxs_431_range_expansion_rate_21_d1": {"inputs": _HLC, "func": f47_atxs_431_range_expansion_rate_21_d1},
    "f47_atxs_432_max_range_over_median_range_21_d1": {"inputs": ["high", "low"], "func": f47_atxs_432_max_range_over_median_range_21_d1},
    "f47_atxs_433_bars_since_hl_range_above_2xatr21_d1": {"inputs": _HLC, "func": f47_atxs_433_bars_since_hl_range_above_2xatr21_d1},
    "f47_atxs_434_count_hl_range_above_2xatr21_252_d1": {"inputs": _HLC, "func": f47_atxs_434_count_hl_range_above_2xatr21_252_d1},
    "f47_atxs_435_drawdown_from_21d_high_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_435_drawdown_from_21d_high_over_atr21_d1},
    "f47_atxs_436_drawdown_from_21d_high_over_atr5_d1": {"inputs": _HLC, "func": f47_atxs_436_drawdown_from_21d_high_over_atr5_d1},
    "f47_atxs_437_drawdown_from_63d_high_over_atr63_d1": {"inputs": _HLC, "func": f47_atxs_437_drawdown_from_63d_high_over_atr63_d1},
    "f47_atxs_438_drawup_from_21d_low_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_438_drawup_from_21d_low_over_atr21_d1},
    "f47_atxs_439_drawup_from_63d_low_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_439_drawup_from_63d_low_over_atr21_d1},
    "f47_atxs_440_max_drawup_252_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_440_max_drawup_252_over_atr21_d1},
    "f47_atxs_441_drawup_drawdown_ratio_atr_252_d1": {"inputs": _HLC, "func": f47_atxs_441_drawup_drawdown_ratio_atr_252_d1},
    "f47_atxs_442_drawup_drawdown_asymmetry_atr_d1": {"inputs": _HLC, "func": f47_atxs_442_drawup_drawdown_asymmetry_atr_d1},
    "f47_atxs_443_close_cross_above_pivot_event_d1": {"inputs": _HLC, "func": f47_atxs_443_close_cross_above_pivot_event_d1},
    "f47_atxs_444_close_cross_above_R1_event_d1": {"inputs": _HLC, "func": f47_atxs_444_close_cross_above_R1_event_d1},
    "f47_atxs_445_close_cross_above_R2_event_d1": {"inputs": _HLC, "func": f47_atxs_445_close_cross_above_R2_event_d1},
    "f47_atxs_446_close_cross_above_camarilla_h3_event_d1": {"inputs": _HLC, "func": f47_atxs_446_close_cross_above_camarilla_h3_event_d1},
    "f47_atxs_447_close_cross_above_camarilla_h4_event_d1": {"inputs": _HLC, "func": f47_atxs_447_close_cross_above_camarilla_h4_event_d1},
    "f47_atxs_448_bars_since_close_cross_above_R1_d1": {"inputs": _HLC, "func": f47_atxs_448_bars_since_close_cross_above_R1_d1},
    "f47_atxs_449_bars_since_close_cross_above_R2_d1": {"inputs": _HLC, "func": f47_atxs_449_bars_since_close_cross_above_R2_d1},
    "f47_atxs_450_count_close_cross_above_R1_past_63_d1": {"inputs": _HLC, "func": f47_atxs_450_count_close_cross_above_R1_past_63_d1},
}
