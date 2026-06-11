import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


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


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


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


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0); dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(au, ad))


def _mad(s, n):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        v = w[valid]
        med = np.median(v)
        return float(np.median(np.abs(v - med)))
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _iqr(s, n):
    q75 = s.rolling(n, min_periods=max(n // 3, 2)).quantile(0.75)
    q25 = s.rolling(n, min_periods=max(n // 3, 2)).quantile(0.25)
    return q75 - q25


def _trimmed_mean(s, n, trim=0.1):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        v = np.sort(w[valid])
        k = int(len(v) * trim)
        if len(v) - 2 * k <= 0:
            return float(np.mean(v))
        return float(np.mean(v[k:len(v) - k]))
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _trimmed_std(s, n, trim=0.1):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        v = np.sort(w[valid])
        k = int(len(v) * trim)
        if len(v) - 2 * k <= 1:
            return float(np.std(v, ddof=1)) if len(v) > 1 else np.nan
        return float(np.std(v[k:len(v) - k], ddof=1))
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _hurst_rs(s, n):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid].astype(float)
        if v.size < 20:
            return np.nan
        mean = v.mean()
        dev = v - mean
        cum = np.cumsum(dev)
        r = cum.max() - cum.min()
        sd = v.std(ddof=1)
        if sd == 0 or r <= 0:
            return np.nan
        return float(np.log(r / sd) / np.log(len(v)))
    return s.rolling(n, min_periods=20).apply(_f, raw=True)


def f47_atxs_301_multi_tf_2way_bull_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    return ((e21 > 0) & (e63 > 0)).astype(float).where(a.notna(), np.nan)


def f47_atxs_302_multi_tf_3way_bull_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return ((e21 > 0) & (e63 > 0) & (e252 > 0)).astype(float).where(a.notna(), np.nan)


def f47_atxs_303_multi_tf_3way_bear_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return ((e21 < 0) & (e63 < 0) & (e252 < 0)).astype(float).where(a.notna(), np.nan)


def f47_atxs_304_count_multi_tf_bull_agreement_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    f = ((e21 > 0) & (e63 > 0) & (e252 > 0)).astype(float)
    return f.rolling(QDAYS, min_periods=MDAYS).sum().where(a.notna(), np.nan)


def f47_atxs_305_count_multi_tf_bull_agreement_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    f = ((e21 > 0) & (e63 > 0) & (e252 > 0)).astype(float)
    return f.rolling(YDAYS, min_periods=QDAYS).sum().where(a.notna(), np.nan)


def f47_atxs_306_longest_multi_tf_bull_streak_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    s = _streak_true((e21 > 0) & (e63 > 0) & (e252 > 0))
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(a.notna(), np.nan)


def f47_atxs_307_multi_tf_short_vs_long_disagree(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return (np.sign(e21) != np.sign(e252)).astype(float).where(a.notna(), np.nan)


def f47_atxs_308_bars_since_multi_tf_bull_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return _bars_since_true((e21 > 0) & (e63 > 0) & (e252 > 0))


def f47_atxs_309_bars_since_multi_tf_bear_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return _bars_since_true((e21 < 0) & (e63 < 0) & (e252 < 0))


def f47_atxs_310_multi_tf_magnitude_divergence(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - _sma(close, MDAYS), a) - _safe_div(close - _sma(close, YDAYS), a)


def f47_atxs_311_close_minus_sma21_over_mad21(close: pd.Series) -> pd.Series:
    return _safe_div(close - _sma(close, MDAYS), _mad(close, MDAYS))


def f47_atxs_312_close_minus_sma63_over_mad63(close: pd.Series) -> pd.Series:
    return _safe_div(close - _sma(close, QDAYS), _mad(close, QDAYS))


def f47_atxs_313_close_minus_median21_over_iqr21(close: pd.Series) -> pd.Series:
    med = close.rolling(MDAYS, min_periods=WDAYS).median()
    return _safe_div(close - med, _iqr(close, MDAYS))


def f47_atxs_314_close_minus_median252_over_iqr252(close: pd.Series) -> pd.Series:
    med = close.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(close - med, _iqr(close, YDAYS))


def f47_atxs_315_close_minus_q75_close_past_21(close: pd.Series) -> pd.Series:
    return close - close.rolling(MDAYS, min_periods=WDAYS).quantile(0.75)


def f47_atxs_316_close_minus_q95_close_past_252(close: pd.Series) -> pd.Series:
    return close - close.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)


def f47_atxs_317_close_minus_median252_over_mad252(close: pd.Series) -> pd.Series:
    med = close.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(close - med, _mad(close, YDAYS))


def f47_atxs_318_close_minus_trimmed_mean_21_over_trimmed_std_21(close: pd.Series) -> pd.Series:
    return _safe_div(close - _trimmed_mean(close, MDAYS), _trimmed_std(close, MDAYS))


def f47_atxs_319_mean_ext_in_high_vol_regime_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = (a > med)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_320_mean_ext_in_low_vol_regime_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = (a <= med)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_321_count_extreme_ext_in_high_vol_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = ((e > 2.0) & (a > med)).astype(float)
    return cond.rolling(QDAYS, min_periods=MDAYS).sum().where(med.notna(), np.nan)


def f47_atxs_322_count_extreme_ext_in_low_vol_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = ((e > 2.0) & (a <= med)).astype(float)
    return cond.rolling(QDAYS, min_periods=MDAYS).sum().where(med.notna(), np.nan)


def f47_atxs_323_current_streak_ext_above_3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _streak_true(e > 3.0).where(e.notna(), np.nan)


def f47_atxs_324_mean_ext_when_in_bottom_25pct_range_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos < 0.25)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_325_mean_ext_when_rsi_above_70_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = (_rsi(close, 14) > 70.0)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_326_mean_ext_when_rsi_below_30_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = (_rsi(close, 14) < 30.0)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_327_close_minus_pivot_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    return _safe_div(close - p, _atr(high, low, close, MDAYS))


def f47_atxs_328_close_minus_R1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * p - low.shift(1)
    return _safe_div(close - r1, _atr(high, low, close, MDAYS))


def f47_atxs_329_close_minus_R2_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = p + (high.shift(1) - low.shift(1))
    return _safe_div(close - r2, _atr(high, low, close, MDAYS))


def f47_atxs_330_close_minus_R3_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r3 = high.shift(1) + 2.0 * (p - low.shift(1))
    return _safe_div(close - r3, _atr(high, low, close, MDAYS))


def f47_atxs_331_close_minus_S1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s1 = 2.0 * p - high.shift(1)
    return _safe_div(close - s1, _atr(high, low, close, MDAYS))


def f47_atxs_332_close_minus_S2_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s2 = p - (high.shift(1) - low.shift(1))
    return _safe_div(close - s2, _atr(high, low, close, MDAYS))


def f47_atxs_333_close_minus_S3_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s3 = low.shift(1) - 2.0 * (high.shift(1) - p)
    return _safe_div(close - s3, _atr(high, low, close, MDAYS))


def f47_atxs_334_pivot_band_position(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * p - low.shift(1)
    s1 = 2.0 * p - high.shift(1)
    return _safe_div(close - p, r1 - s1)


def f47_atxs_335_close_above_R2_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = p + (high.shift(1) - low.shift(1))
    return (close > r2).astype(float).where(r2.notna(), np.nan)


def f47_atxs_336_close_above_R3_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r3 = high.shift(1) + 2.0 * (p - low.shift(1))
    return (close > r3).astype(float).where(r3.notna(), np.nan)


def f47_atxs_337_close_minus_fib_382_retrace_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = hh - 0.382 * (hh - ll)
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_338_close_minus_fib_618_retrace_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = hh - 0.618 * (hh - ll)
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_339_close_minus_fib_50_retrace_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = (hh + ll) / 2.0
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_340_close_minus_fib_1272_extension_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = ll + 1.272 * (hh - ll)
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_341_close_minus_fib_1618_extension_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = ll + 1.618 * (hh - ll)
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_342_position_in_fib_236_786_channel(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    f236 = hh - 0.236 * (hh - ll)
    f786 = hh - 0.786 * (hh - ll)
    return _safe_div(close - f786, f236 - f786)


def f47_atxs_343_realized_vol_21_pct_rank_252(close: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return rv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_344_realized_vol_63_pct_rank_252(close: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return rv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_345_vol_cone_position(close: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    med = rv.rolling(YDAYS, min_periods=QDAYS).median()
    iqr = _iqr(rv, YDAYS)
    return _safe_div(rv - med, iqr)


def f47_atxs_346_realized_vol_zscore_504(close: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return _rolling_zscore(rv, DDAYS_2Y, min_periods=YDAYS)


def f47_atxs_347_vol_of_vol_pct_rank_252(close: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    vov = rv.rolling(MDAYS, min_periods=WDAYS).std()
    return vov.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_348_mean_ext_when_vol_top_quartile(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    q75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    cond = (a > q75)
    return e.where(cond, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f47_atxs_349_mean_ext_when_vol_bottom_quartile(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    q25 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    cond = (a < q25)
    return e.where(cond, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f47_atxs_350_vol_top_decile_with_close_above_sma21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    q90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((a > q90) & (close > _sma(close, MDAYS))).astype(float).where(q90.notna(), np.nan)


def f47_atxs_351_bars_since_ext_crossed_above_zero(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    ev = (e.shift(1) <= 0) & (e > 0)
    return _bars_since_true(ev)


def f47_atxs_352_max_ext_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).max()


def f47_atxs_353_max_ext_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).max()


def f47_atxs_354_max_ext_past_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).max()


def f47_atxs_355_ext_velocity_5bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e - e.shift(WDAYS)) / float(WDAYS)


def f47_atxs_356_ext_velocity_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e - e.shift(MDAYS)) / float(MDAYS)


def f47_atxs_357_streak_ext_above_3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _streak_true(e > 3.0).where(e.notna(), np.nan)


def f47_atxs_358_streak_ext_above_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _streak_true(e > 5.0).where(e.notna(), np.nan)


def f47_atxs_359_ext_std_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).std()


def f47_atxs_360_ext_std_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).std()


def _ar1(s, n):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 4):
            return np.nan
        v = w[valid]
        if v.size < 3:
            return np.nan
        x = v[:-1]; y = v[1:]
        if x.std(ddof=1) == 0 or y.std(ddof=1) == 0:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    return s.rolling(n, min_periods=max(n // 3, 4)).apply(_f, raw=True)


def f47_atxs_361_ext_ar1_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _ar1(e, QDAYS)


def f47_atxs_362_ext_ar1_past_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _ar1(e, YDAYS)


def f47_atxs_363_hurst_rs_close_100(close: pd.Series) -> pd.Series:
    return _hurst_rs(close, 100)


def f47_atxs_364_ext_autocorr_lag1_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).apply(lambda w: float(pd.Series(w).autocorr(lag=1)) if pd.Series(w).std() > 0 else np.nan, raw=True)


def f47_atxs_365_ext_autocorr_lag5_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: float(pd.Series(w).autocorr(lag=5)) if pd.Series(w).std() > 0 else np.nan, raw=True)


def f47_atxs_366_ext_sign_change_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = close - _sma(close, MDAYS)
    sgn = np.sign(e)
    flip = ((sgn != sgn.shift(1)) & e.notna() & e.shift(1).notna()).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_367_mean_reversion_success_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    cond = (e.shift(WDAYS) > 2.0) & (e < 1.0)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_368_overshoot_recovery_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).max() - e


def f47_atxs_369_bars_since_ext_above_5_past_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _bars_since_true(e > 5.0)


def f47_atxs_370_bars_since_ext_above_7_past_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _bars_since_true(e > 7.0)


def f47_atxs_371_bars_since_ext_above_10_past_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _bars_since_true(e > 10.0)


def f47_atxs_372_ext_above_5_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e > 5.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_373_ext_above_7_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e > 7.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_374_ext_above_10_count_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e > 10.0).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_375_max_ext_cummax(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.cummax()


def f47_atxs_301_multi_tf_2way_bull_agreement_d1(high, low, close):
    return f47_atxs_301_multi_tf_2way_bull_agreement(high, low, close).diff()


def f47_atxs_302_multi_tf_3way_bull_agreement_d1(high, low, close):
    return f47_atxs_302_multi_tf_3way_bull_agreement(high, low, close).diff()


def f47_atxs_303_multi_tf_3way_bear_agreement_d1(high, low, close):
    return f47_atxs_303_multi_tf_3way_bear_agreement(high, low, close).diff()


def f47_atxs_304_count_multi_tf_bull_agreement_63_d1(high, low, close):
    return f47_atxs_304_count_multi_tf_bull_agreement_63(high, low, close).diff()


def f47_atxs_305_count_multi_tf_bull_agreement_252_d1(high, low, close):
    return f47_atxs_305_count_multi_tf_bull_agreement_252(high, low, close).diff()


def f47_atxs_306_longest_multi_tf_bull_streak_252_d1(high, low, close):
    return f47_atxs_306_longest_multi_tf_bull_streak_252(high, low, close).diff()


def f47_atxs_307_multi_tf_short_vs_long_disagree_d1(high, low, close):
    return f47_atxs_307_multi_tf_short_vs_long_disagree(high, low, close).diff()


def f47_atxs_308_bars_since_multi_tf_bull_agreement_d1(high, low, close):
    return f47_atxs_308_bars_since_multi_tf_bull_agreement(high, low, close).diff()


def f47_atxs_309_bars_since_multi_tf_bear_agreement_d1(high, low, close):
    return f47_atxs_309_bars_since_multi_tf_bear_agreement(high, low, close).diff()


def f47_atxs_310_multi_tf_magnitude_divergence_d1(high, low, close):
    return f47_atxs_310_multi_tf_magnitude_divergence(high, low, close).diff()


def f47_atxs_311_close_minus_sma21_over_mad21_d1(close):
    return f47_atxs_311_close_minus_sma21_over_mad21(close).diff()


def f47_atxs_312_close_minus_sma63_over_mad63_d1(close):
    return f47_atxs_312_close_minus_sma63_over_mad63(close).diff()


def f47_atxs_313_close_minus_median21_over_iqr21_d1(close):
    return f47_atxs_313_close_minus_median21_over_iqr21(close).diff()


def f47_atxs_314_close_minus_median252_over_iqr252_d1(close):
    return f47_atxs_314_close_minus_median252_over_iqr252(close).diff()


def f47_atxs_315_close_minus_q75_close_past_21_d1(close):
    return f47_atxs_315_close_minus_q75_close_past_21(close).diff()


def f47_atxs_316_close_minus_q95_close_past_252_d1(close):
    return f47_atxs_316_close_minus_q95_close_past_252(close).diff()


def f47_atxs_317_close_minus_median252_over_mad252_d1(close):
    return f47_atxs_317_close_minus_median252_over_mad252(close).diff()


def f47_atxs_318_close_minus_trimmed_mean_21_over_trimmed_std_21_d1(close):
    return f47_atxs_318_close_minus_trimmed_mean_21_over_trimmed_std_21(close).diff()


def f47_atxs_319_mean_ext_in_high_vol_regime_21_d1(high, low, close):
    return f47_atxs_319_mean_ext_in_high_vol_regime_21(high, low, close).diff()


def f47_atxs_320_mean_ext_in_low_vol_regime_21_d1(high, low, close):
    return f47_atxs_320_mean_ext_in_low_vol_regime_21(high, low, close).diff()


def f47_atxs_321_count_extreme_ext_in_high_vol_63_d1(high, low, close):
    return f47_atxs_321_count_extreme_ext_in_high_vol_63(high, low, close).diff()


def f47_atxs_322_count_extreme_ext_in_low_vol_63_d1(high, low, close):
    return f47_atxs_322_count_extreme_ext_in_low_vol_63(high, low, close).diff()


def f47_atxs_323_current_streak_ext_above_3_d1(high, low, close):
    return f47_atxs_323_current_streak_ext_above_3(high, low, close).diff()


def f47_atxs_324_mean_ext_when_in_bottom_25pct_range_21_d1(high, low, close):
    return f47_atxs_324_mean_ext_when_in_bottom_25pct_range_21(high, low, close).diff()


def f47_atxs_325_mean_ext_when_rsi_above_70_past_21_d1(high, low, close):
    return f47_atxs_325_mean_ext_when_rsi_above_70_past_21(high, low, close).diff()


def f47_atxs_326_mean_ext_when_rsi_below_30_past_21_d1(high, low, close):
    return f47_atxs_326_mean_ext_when_rsi_below_30_past_21(high, low, close).diff()


def f47_atxs_327_close_minus_pivot_over_atr21_d1(high, low, close):
    return f47_atxs_327_close_minus_pivot_over_atr21(high, low, close).diff()


def f47_atxs_328_close_minus_R1_over_atr21_d1(high, low, close):
    return f47_atxs_328_close_minus_R1_over_atr21(high, low, close).diff()


def f47_atxs_329_close_minus_R2_over_atr21_d1(high, low, close):
    return f47_atxs_329_close_minus_R2_over_atr21(high, low, close).diff()


def f47_atxs_330_close_minus_R3_over_atr21_d1(high, low, close):
    return f47_atxs_330_close_minus_R3_over_atr21(high, low, close).diff()


def f47_atxs_331_close_minus_S1_over_atr21_d1(high, low, close):
    return f47_atxs_331_close_minus_S1_over_atr21(high, low, close).diff()


def f47_atxs_332_close_minus_S2_over_atr21_d1(high, low, close):
    return f47_atxs_332_close_minus_S2_over_atr21(high, low, close).diff()


def f47_atxs_333_close_minus_S3_over_atr21_d1(high, low, close):
    return f47_atxs_333_close_minus_S3_over_atr21(high, low, close).diff()


def f47_atxs_334_pivot_band_position_d1(high, low, close):
    return f47_atxs_334_pivot_band_position(high, low, close).diff()


def f47_atxs_335_close_above_R2_state_d1(high, low, close):
    return f47_atxs_335_close_above_R2_state(high, low, close).diff()


def f47_atxs_336_close_above_R3_state_d1(high, low, close):
    return f47_atxs_336_close_above_R3_state(high, low, close).diff()


def f47_atxs_337_close_minus_fib_382_retrace_over_atr21_d1(high, low, close):
    return f47_atxs_337_close_minus_fib_382_retrace_over_atr21(high, low, close).diff()


def f47_atxs_338_close_minus_fib_618_retrace_over_atr21_d1(high, low, close):
    return f47_atxs_338_close_minus_fib_618_retrace_over_atr21(high, low, close).diff()


def f47_atxs_339_close_minus_fib_50_retrace_over_atr21_d1(high, low, close):
    return f47_atxs_339_close_minus_fib_50_retrace_over_atr21(high, low, close).diff()


def f47_atxs_340_close_minus_fib_1272_extension_over_atr21_d1(high, low, close):
    return f47_atxs_340_close_minus_fib_1272_extension_over_atr21(high, low, close).diff()


def f47_atxs_341_close_minus_fib_1618_extension_over_atr21_d1(high, low, close):
    return f47_atxs_341_close_minus_fib_1618_extension_over_atr21(high, low, close).diff()


def f47_atxs_342_position_in_fib_236_786_channel_d1(high, low, close):
    return f47_atxs_342_position_in_fib_236_786_channel(high, low, close).diff()


def f47_atxs_343_realized_vol_21_pct_rank_252_d1(close):
    return f47_atxs_343_realized_vol_21_pct_rank_252(close).diff()


def f47_atxs_344_realized_vol_63_pct_rank_252_d1(close):
    return f47_atxs_344_realized_vol_63_pct_rank_252(close).diff()


def f47_atxs_345_vol_cone_position_d1(close):
    return f47_atxs_345_vol_cone_position(close).diff()


def f47_atxs_346_realized_vol_zscore_504_d1(close):
    return f47_atxs_346_realized_vol_zscore_504(close).diff()


def f47_atxs_347_vol_of_vol_pct_rank_252_d1(close):
    return f47_atxs_347_vol_of_vol_pct_rank_252(close).diff()


def f47_atxs_348_mean_ext_when_vol_top_quartile_d1(high, low, close):
    return f47_atxs_348_mean_ext_when_vol_top_quartile(high, low, close).diff()


def f47_atxs_349_mean_ext_when_vol_bottom_quartile_d1(high, low, close):
    return f47_atxs_349_mean_ext_when_vol_bottom_quartile(high, low, close).diff()


def f47_atxs_350_vol_top_decile_with_close_above_sma21_d1(high, low, close):
    return f47_atxs_350_vol_top_decile_with_close_above_sma21(high, low, close).diff()


def f47_atxs_351_bars_since_ext_crossed_above_zero_d1(high, low, close):
    return f47_atxs_351_bars_since_ext_crossed_above_zero(high, low, close).diff()


def f47_atxs_352_max_ext_past_21_d1(high, low, close):
    return f47_atxs_352_max_ext_past_21(high, low, close).diff()


def f47_atxs_353_max_ext_past_63_d1(high, low, close):
    return f47_atxs_353_max_ext_past_63(high, low, close).diff()


def f47_atxs_354_max_ext_past_252_d1(high, low, close):
    return f47_atxs_354_max_ext_past_252(high, low, close).diff()


def f47_atxs_355_ext_velocity_5bar_d1(high, low, close):
    return f47_atxs_355_ext_velocity_5bar(high, low, close).diff()


def f47_atxs_356_ext_velocity_21bar_d1(high, low, close):
    return f47_atxs_356_ext_velocity_21bar(high, low, close).diff()


def f47_atxs_357_streak_ext_above_3_d1(high, low, close):
    return f47_atxs_357_streak_ext_above_3(high, low, close).diff()


def f47_atxs_358_streak_ext_above_5_d1(high, low, close):
    return f47_atxs_358_streak_ext_above_5(high, low, close).diff()


def f47_atxs_359_ext_std_past_21_d1(high, low, close):
    return f47_atxs_359_ext_std_past_21(high, low, close).diff()


def f47_atxs_360_ext_std_past_63_d1(high, low, close):
    return f47_atxs_360_ext_std_past_63(high, low, close).diff()


def f47_atxs_361_ext_ar1_past_63_d1(high, low, close):
    return f47_atxs_361_ext_ar1_past_63(high, low, close).diff()


def f47_atxs_362_ext_ar1_past_252_d1(high, low, close):
    return f47_atxs_362_ext_ar1_past_252(high, low, close).diff()


def f47_atxs_363_hurst_rs_close_100_d1(close):
    return f47_atxs_363_hurst_rs_close_100(close).diff()


def f47_atxs_364_ext_autocorr_lag1_past_21_d1(high, low, close):
    return f47_atxs_364_ext_autocorr_lag1_past_21(high, low, close).diff()


def f47_atxs_365_ext_autocorr_lag5_past_63_d1(high, low, close):
    return f47_atxs_365_ext_autocorr_lag5_past_63(high, low, close).diff()


def f47_atxs_366_ext_sign_change_count_63_d1(high, low, close):
    return f47_atxs_366_ext_sign_change_count_63(high, low, close).diff()


def f47_atxs_367_mean_reversion_success_count_63_d1(high, low, close):
    return f47_atxs_367_mean_reversion_success_count_63(high, low, close).diff()


def f47_atxs_368_overshoot_recovery_21d_d1(high, low, close):
    return f47_atxs_368_overshoot_recovery_21d(high, low, close).diff()


def f47_atxs_369_bars_since_ext_above_5_past_252_d1(high, low, close):
    return f47_atxs_369_bars_since_ext_above_5_past_252(high, low, close).diff()


def f47_atxs_370_bars_since_ext_above_7_past_252_d1(high, low, close):
    return f47_atxs_370_bars_since_ext_above_7_past_252(high, low, close).diff()


def f47_atxs_371_bars_since_ext_above_10_past_504_d1(high, low, close):
    return f47_atxs_371_bars_since_ext_above_10_past_504(high, low, close).diff()


def f47_atxs_372_ext_above_5_count_252_d1(high, low, close):
    return f47_atxs_372_ext_above_5_count_252(high, low, close).diff()


def f47_atxs_373_ext_above_7_count_252_d1(high, low, close):
    return f47_atxs_373_ext_above_7_count_252(high, low, close).diff()


def f47_atxs_374_ext_above_10_count_504_d1(high, low, close):
    return f47_atxs_374_ext_above_10_count_504(high, low, close).diff()


def f47_atxs_375_max_ext_cummax_d1(high, low, close):
    return f47_atxs_375_max_ext_cummax(high, low, close).diff()


_HLC = ["high", "low", "close"]


ATR_EXTENSION_SIGNATURE_D1_REGISTRY_301_375 = {
    "f47_atxs_301_multi_tf_2way_bull_agreement_d1": {"inputs": _HLC, "func": f47_atxs_301_multi_tf_2way_bull_agreement_d1},
    "f47_atxs_302_multi_tf_3way_bull_agreement_d1": {"inputs": _HLC, "func": f47_atxs_302_multi_tf_3way_bull_agreement_d1},
    "f47_atxs_303_multi_tf_3way_bear_agreement_d1": {"inputs": _HLC, "func": f47_atxs_303_multi_tf_3way_bear_agreement_d1},
    "f47_atxs_304_count_multi_tf_bull_agreement_63_d1": {"inputs": _HLC, "func": f47_atxs_304_count_multi_tf_bull_agreement_63_d1},
    "f47_atxs_305_count_multi_tf_bull_agreement_252_d1": {"inputs": _HLC, "func": f47_atxs_305_count_multi_tf_bull_agreement_252_d1},
    "f47_atxs_306_longest_multi_tf_bull_streak_252_d1": {"inputs": _HLC, "func": f47_atxs_306_longest_multi_tf_bull_streak_252_d1},
    "f47_atxs_307_multi_tf_short_vs_long_disagree_d1": {"inputs": _HLC, "func": f47_atxs_307_multi_tf_short_vs_long_disagree_d1},
    "f47_atxs_308_bars_since_multi_tf_bull_agreement_d1": {"inputs": _HLC, "func": f47_atxs_308_bars_since_multi_tf_bull_agreement_d1},
    "f47_atxs_309_bars_since_multi_tf_bear_agreement_d1": {"inputs": _HLC, "func": f47_atxs_309_bars_since_multi_tf_bear_agreement_d1},
    "f47_atxs_310_multi_tf_magnitude_divergence_d1": {"inputs": _HLC, "func": f47_atxs_310_multi_tf_magnitude_divergence_d1},
    "f47_atxs_311_close_minus_sma21_over_mad21_d1": {"inputs": ["close"], "func": f47_atxs_311_close_minus_sma21_over_mad21_d1},
    "f47_atxs_312_close_minus_sma63_over_mad63_d1": {"inputs": ["close"], "func": f47_atxs_312_close_minus_sma63_over_mad63_d1},
    "f47_atxs_313_close_minus_median21_over_iqr21_d1": {"inputs": ["close"], "func": f47_atxs_313_close_minus_median21_over_iqr21_d1},
    "f47_atxs_314_close_minus_median252_over_iqr252_d1": {"inputs": ["close"], "func": f47_atxs_314_close_minus_median252_over_iqr252_d1},
    "f47_atxs_315_close_minus_q75_close_past_21_d1": {"inputs": ["close"], "func": f47_atxs_315_close_minus_q75_close_past_21_d1},
    "f47_atxs_316_close_minus_q95_close_past_252_d1": {"inputs": ["close"], "func": f47_atxs_316_close_minus_q95_close_past_252_d1},
    "f47_atxs_317_close_minus_median252_over_mad252_d1": {"inputs": ["close"], "func": f47_atxs_317_close_minus_median252_over_mad252_d1},
    "f47_atxs_318_close_minus_trimmed_mean_21_over_trimmed_std_21_d1": {"inputs": ["close"], "func": f47_atxs_318_close_minus_trimmed_mean_21_over_trimmed_std_21_d1},
    "f47_atxs_319_mean_ext_in_high_vol_regime_21_d1": {"inputs": _HLC, "func": f47_atxs_319_mean_ext_in_high_vol_regime_21_d1},
    "f47_atxs_320_mean_ext_in_low_vol_regime_21_d1": {"inputs": _HLC, "func": f47_atxs_320_mean_ext_in_low_vol_regime_21_d1},
    "f47_atxs_321_count_extreme_ext_in_high_vol_63_d1": {"inputs": _HLC, "func": f47_atxs_321_count_extreme_ext_in_high_vol_63_d1},
    "f47_atxs_322_count_extreme_ext_in_low_vol_63_d1": {"inputs": _HLC, "func": f47_atxs_322_count_extreme_ext_in_low_vol_63_d1},
    "f47_atxs_323_current_streak_ext_above_3_d1": {"inputs": _HLC, "func": f47_atxs_323_current_streak_ext_above_3_d1},
    "f47_atxs_324_mean_ext_when_in_bottom_25pct_range_21_d1": {"inputs": _HLC, "func": f47_atxs_324_mean_ext_when_in_bottom_25pct_range_21_d1},
    "f47_atxs_325_mean_ext_when_rsi_above_70_past_21_d1": {"inputs": _HLC, "func": f47_atxs_325_mean_ext_when_rsi_above_70_past_21_d1},
    "f47_atxs_326_mean_ext_when_rsi_below_30_past_21_d1": {"inputs": _HLC, "func": f47_atxs_326_mean_ext_when_rsi_below_30_past_21_d1},
    "f47_atxs_327_close_minus_pivot_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_327_close_minus_pivot_over_atr21_d1},
    "f47_atxs_328_close_minus_R1_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_328_close_minus_R1_over_atr21_d1},
    "f47_atxs_329_close_minus_R2_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_329_close_minus_R2_over_atr21_d1},
    "f47_atxs_330_close_minus_R3_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_330_close_minus_R3_over_atr21_d1},
    "f47_atxs_331_close_minus_S1_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_331_close_minus_S1_over_atr21_d1},
    "f47_atxs_332_close_minus_S2_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_332_close_minus_S2_over_atr21_d1},
    "f47_atxs_333_close_minus_S3_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_333_close_minus_S3_over_atr21_d1},
    "f47_atxs_334_pivot_band_position_d1": {"inputs": _HLC, "func": f47_atxs_334_pivot_band_position_d1},
    "f47_atxs_335_close_above_R2_state_d1": {"inputs": _HLC, "func": f47_atxs_335_close_above_R2_state_d1},
    "f47_atxs_336_close_above_R3_state_d1": {"inputs": _HLC, "func": f47_atxs_336_close_above_R3_state_d1},
    "f47_atxs_337_close_minus_fib_382_retrace_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_337_close_minus_fib_382_retrace_over_atr21_d1},
    "f47_atxs_338_close_minus_fib_618_retrace_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_338_close_minus_fib_618_retrace_over_atr21_d1},
    "f47_atxs_339_close_minus_fib_50_retrace_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_339_close_minus_fib_50_retrace_over_atr21_d1},
    "f47_atxs_340_close_minus_fib_1272_extension_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_340_close_minus_fib_1272_extension_over_atr21_d1},
    "f47_atxs_341_close_minus_fib_1618_extension_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_341_close_minus_fib_1618_extension_over_atr21_d1},
    "f47_atxs_342_position_in_fib_236_786_channel_d1": {"inputs": _HLC, "func": f47_atxs_342_position_in_fib_236_786_channel_d1},
    "f47_atxs_343_realized_vol_21_pct_rank_252_d1": {"inputs": ["close"], "func": f47_atxs_343_realized_vol_21_pct_rank_252_d1},
    "f47_atxs_344_realized_vol_63_pct_rank_252_d1": {"inputs": ["close"], "func": f47_atxs_344_realized_vol_63_pct_rank_252_d1},
    "f47_atxs_345_vol_cone_position_d1": {"inputs": ["close"], "func": f47_atxs_345_vol_cone_position_d1},
    "f47_atxs_346_realized_vol_zscore_504_d1": {"inputs": ["close"], "func": f47_atxs_346_realized_vol_zscore_504_d1},
    "f47_atxs_347_vol_of_vol_pct_rank_252_d1": {"inputs": ["close"], "func": f47_atxs_347_vol_of_vol_pct_rank_252_d1},
    "f47_atxs_348_mean_ext_when_vol_top_quartile_d1": {"inputs": _HLC, "func": f47_atxs_348_mean_ext_when_vol_top_quartile_d1},
    "f47_atxs_349_mean_ext_when_vol_bottom_quartile_d1": {"inputs": _HLC, "func": f47_atxs_349_mean_ext_when_vol_bottom_quartile_d1},
    "f47_atxs_350_vol_top_decile_with_close_above_sma21_d1": {"inputs": _HLC, "func": f47_atxs_350_vol_top_decile_with_close_above_sma21_d1},
    "f47_atxs_351_bars_since_ext_crossed_above_zero_d1": {"inputs": _HLC, "func": f47_atxs_351_bars_since_ext_crossed_above_zero_d1},
    "f47_atxs_352_max_ext_past_21_d1": {"inputs": _HLC, "func": f47_atxs_352_max_ext_past_21_d1},
    "f47_atxs_353_max_ext_past_63_d1": {"inputs": _HLC, "func": f47_atxs_353_max_ext_past_63_d1},
    "f47_atxs_354_max_ext_past_252_d1": {"inputs": _HLC, "func": f47_atxs_354_max_ext_past_252_d1},
    "f47_atxs_355_ext_velocity_5bar_d1": {"inputs": _HLC, "func": f47_atxs_355_ext_velocity_5bar_d1},
    "f47_atxs_356_ext_velocity_21bar_d1": {"inputs": _HLC, "func": f47_atxs_356_ext_velocity_21bar_d1},
    "f47_atxs_357_streak_ext_above_3_d1": {"inputs": _HLC, "func": f47_atxs_357_streak_ext_above_3_d1},
    "f47_atxs_358_streak_ext_above_5_d1": {"inputs": _HLC, "func": f47_atxs_358_streak_ext_above_5_d1},
    "f47_atxs_359_ext_std_past_21_d1": {"inputs": _HLC, "func": f47_atxs_359_ext_std_past_21_d1},
    "f47_atxs_360_ext_std_past_63_d1": {"inputs": _HLC, "func": f47_atxs_360_ext_std_past_63_d1},
    "f47_atxs_361_ext_ar1_past_63_d1": {"inputs": _HLC, "func": f47_atxs_361_ext_ar1_past_63_d1},
    "f47_atxs_362_ext_ar1_past_252_d1": {"inputs": _HLC, "func": f47_atxs_362_ext_ar1_past_252_d1},
    "f47_atxs_363_hurst_rs_close_100_d1": {"inputs": ["close"], "func": f47_atxs_363_hurst_rs_close_100_d1},
    "f47_atxs_364_ext_autocorr_lag1_past_21_d1": {"inputs": _HLC, "func": f47_atxs_364_ext_autocorr_lag1_past_21_d1},
    "f47_atxs_365_ext_autocorr_lag5_past_63_d1": {"inputs": _HLC, "func": f47_atxs_365_ext_autocorr_lag5_past_63_d1},
    "f47_atxs_366_ext_sign_change_count_63_d1": {"inputs": _HLC, "func": f47_atxs_366_ext_sign_change_count_63_d1},
    "f47_atxs_367_mean_reversion_success_count_63_d1": {"inputs": _HLC, "func": f47_atxs_367_mean_reversion_success_count_63_d1},
    "f47_atxs_368_overshoot_recovery_21d_d1": {"inputs": _HLC, "func": f47_atxs_368_overshoot_recovery_21d_d1},
    "f47_atxs_369_bars_since_ext_above_5_past_252_d1": {"inputs": _HLC, "func": f47_atxs_369_bars_since_ext_above_5_past_252_d1},
    "f47_atxs_370_bars_since_ext_above_7_past_252_d1": {"inputs": _HLC, "func": f47_atxs_370_bars_since_ext_above_7_past_252_d1},
    "f47_atxs_371_bars_since_ext_above_10_past_504_d1": {"inputs": _HLC, "func": f47_atxs_371_bars_since_ext_above_10_past_504_d1},
    "f47_atxs_372_ext_above_5_count_252_d1": {"inputs": _HLC, "func": f47_atxs_372_ext_above_5_count_252_d1},
    "f47_atxs_373_ext_above_7_count_252_d1": {"inputs": _HLC, "func": f47_atxs_373_ext_above_7_count_252_d1},
    "f47_atxs_374_ext_above_10_count_504_d1": {"inputs": _HLC, "func": f47_atxs_374_ext_above_10_count_504_d1},
    "f47_atxs_375_max_ext_cummax_d1": {"inputs": _HLC, "func": f47_atxs_375_max_ext_cummax_d1},
}
