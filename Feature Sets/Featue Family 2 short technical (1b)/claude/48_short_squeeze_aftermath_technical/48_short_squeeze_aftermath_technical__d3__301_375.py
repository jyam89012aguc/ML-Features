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


def f48_ssat_301_si_over_21d_avg_volume(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_div(shortinterest.astype(float), volume.rolling(MDAYS, min_periods=WDAYS).mean())


def f48_ssat_302_si_over_21d_total_volume_alt(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_div(shortinterest.astype(float), volume.rolling(MDAYS, min_periods=WDAYS).sum())


def f48_ssat_303_si_over_63d_avg_volume(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_div(shortinterest.astype(float), volume.rolling(QDAYS, min_periods=MDAYS).mean())


def f48_ssat_304_si_over_252d_avg_volume(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_div(shortinterest.astype(float), volume.rolling(YDAYS, min_periods=QDAYS).mean())


def f48_ssat_305_dtc_over_median_dtc_252(daystocover: pd.Series) -> pd.Series:
    d = daystocover.astype(float)
    return _safe_div(d, d.rolling(YDAYS, min_periods=QDAYS).median())


def f48_ssat_306_shortpctfloat_over_median_252(shortpctfloat: pd.Series) -> pd.Series:
    p = shortpctfloat.astype(float)
    return _safe_div(p, p.rolling(YDAYS, min_periods=QDAYS).median())


def f48_ssat_307_si_1m_change_over_21d_total_vol(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_div(shortinterest.astype(float).diff(MDAYS), volume.rolling(MDAYS, min_periods=WDAYS).sum())


def f48_ssat_308_si_3m_change_over_63d_total_vol(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_div(shortinterest.astype(float).diff(QDAYS), volume.rolling(QDAYS, min_periods=MDAYS).sum())


def f48_ssat_309_hl_range_over_volume(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_div(high - low, volume)


def f48_ssat_310_hl_range_over_volume_sma_21(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_div(high - low, volume).rolling(MDAYS, min_periods=WDAYS).mean()


def f48_ssat_311_si_cv_21(shortinterest: pd.Series) -> pd.Series:
    s = shortinterest.astype(float)
    return _safe_div(s.rolling(MDAYS, min_periods=WDAYS).std(), s.rolling(MDAYS, min_periods=WDAYS).mean())


def f48_ssat_312_si_cv_63(shortinterest: pd.Series) -> pd.Series:
    s = shortinterest.astype(float)
    return _safe_div(s.rolling(QDAYS, min_periods=MDAYS).std(), s.rolling(QDAYS, min_periods=MDAYS).mean())


def f48_ssat_313_si_top5_share_252(shortinterest: pd.Series) -> pd.Series:
    s = shortinterest.astype(float).diff().abs()
    def _top5(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        if v.sum() == 0:
            return np.nan
        return float(np.sort(v)[-5:].sum() / v.sum())
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_top5, raw=True)


def f48_ssat_314_si_skew_252(shortinterest: pd.Series) -> pd.Series:
    return shortinterest.astype(float).rolling(YDAYS, min_periods=QDAYS).skew()


def f48_ssat_315_si_kurt_252(shortinterest: pd.Series) -> pd.Series:
    return shortinterest.astype(float).rolling(YDAYS, min_periods=QDAYS).kurt()


def f48_ssat_316_si_21d_range_over_mean(shortinterest: pd.Series) -> pd.Series:
    s = shortinterest.astype(float)
    return _safe_div(s.rolling(MDAYS, min_periods=WDAYS).max() - s.rolling(MDAYS, min_periods=WDAYS).min(),
                     s.rolling(MDAYS, min_periods=WDAYS).mean())


def f48_ssat_317_si_mad_252(shortinterest: pd.Series) -> pd.Series:
    s = shortinterest.astype(float)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        return float(np.median(np.abs(v - np.median(v))))
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f48_ssat_318_bars_since_si_252d_low(shortinterest: pd.Series) -> pd.Series:
    s = shortinterest.astype(float)
    return _bars_since_true(s == s.rolling(YDAYS, min_periods=QDAYS).min())


def f48_ssat_319_dcb_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    capit_21 = capit.astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    rally_10 = (close.pct_change(WDAYS).rolling(WDAYS, min_periods=2).max() > 0.05)
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    lower_high = (rh < rh.shift(10))
    return (capit_21 & rally_10 & lower_high).astype(float).where(a.notna() & rh.shift(10).notna(), np.nan)


def f48_ssat_320_dcb_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    capit_21 = capit.astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    rally_10 = (close.pct_change(WDAYS).rolling(WDAYS, min_periods=2).max() > 0.05)
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    lower_high = (rh < rh.shift(10))
    f = (capit_21 & rally_10 & lower_high).astype(float)
    return f.rolling(QDAYS, min_periods=MDAYS).sum().where(a.notna() & rh.shift(10).notna(), np.nan)


def f48_ssat_321_dcb_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    capit_21 = capit.astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    rally_10 = (close.pct_change(WDAYS).rolling(WDAYS, min_periods=2).max() > 0.05)
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    lower_high = (rh < rh.shift(10))
    f = (capit_21 & rally_10 & lower_high).astype(float)
    return f.rolling(YDAYS, min_periods=QDAYS).sum().where(a.notna() & rh.shift(10).notna(), np.nan)


def f48_ssat_322_head_and_shoulders_right_shoulder_flag(high: pd.Series, close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w
        idx_max = int(np.nanargmax(v))
        if not (MDAYS <= idx_max <= 2 * MDAYS):
            return 0.0
        peak = v[idx_max]
        return 1.0 if (peak > 0 and (v[-1] < peak * 0.95)) else 0.0
    return high.rolling(QDAYS, min_periods=MDAYS).apply(_f, raw=True)


def f48_ssat_323_head_and_shoulders_neckline_break(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ll21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    return (close < ll21).astype(float).where(ll21.notna(), np.nan)


def f48_ssat_324_neckline_break_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ll21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    return (close < ll21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(ll21.notna(), np.nan)


def f48_ssat_325_failed_bounce_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rally_5_ago = (close.pct_change(WDAYS).shift(WDAYS) > 0.05)
    failed_now = (close < close.shift(2 * WDAYS))
    return (rally_5_ago & failed_now).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(close.shift(2 * WDAYS).notna(), np.nan)


def f48_ssat_326_bounce_fade_rate_63(close: pd.Series) -> pd.Series:
    rally_5_ago = (close.pct_change(WDAYS).shift(WDAYS) > 0.05).astype(float)
    failed = (close < close.shift(2 * WDAYS)).astype(float)
    num = (rally_5_ago * failed).rolling(QDAYS, min_periods=MDAYS).sum()
    den = rally_5_ago.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den)


def f48_ssat_327_ewma_return_21_hl5(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    alpha = 1.0 - 0.5 ** (1.0 / 5.0)
    return r.ewm(alpha=alpha, adjust=False, min_periods=5).mean().rolling(MDAYS, min_periods=WDAYS).mean()


def f48_ssat_328_ewma_return_63_hl21(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    alpha = 1.0 - 0.5 ** (1.0 / MDAYS)
    return r.ewm(alpha=alpha, adjust=False, min_periods=MDAYS).mean().rolling(QDAYS, min_periods=MDAYS).mean()


def f48_ssat_329_linearly_weighted_return_21(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    weights = np.arange(1, MDAYS + 1, dtype=float)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < WDAYS:
            return np.nan
        x = w.copy()
        x[~valid] = 0.0
        wv = np.arange(1, len(w) + 1, dtype=float)
        wv[~valid] = 0.0
        ws = wv.sum()
        return (x * wv).sum() / ws if ws != 0 else np.nan
    return r.rolling(MDAYS, min_periods=WDAYS).apply(_f, raw=True)


def f48_ssat_330_linearly_weighted_return_63(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        x = w.copy()
        x[~valid] = 0.0
        wv = np.arange(1, len(w) + 1, dtype=float)
        wv[~valid] = 0.0
        ws = wv.sum()
        return (x * wv).sum() / ws if ws != 0 else np.nan
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_f, raw=True)


def f48_ssat_331_ewma_volume_21(volume: pd.Series) -> pd.Series:
    alpha = 1.0 - 0.5 ** (1.0 / 5.0)
    return volume.ewm(alpha=alpha, adjust=False, min_periods=5).mean().rolling(MDAYS, min_periods=WDAYS).mean()


def f48_ssat_332_ewma_rsi_21(close: pd.Series) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0); dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    ad = dn.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    rsi = 100.0 - 100.0 / (1.0 + _safe_div(au, ad))
    alpha = 1.0 - 0.5 ** (1.0 / 5.0)
    return rsi.ewm(alpha=alpha, adjust=False, min_periods=5).mean()


def f48_ssat_333_ewma_std_returns_21(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    alpha = 1.0 - 0.5 ** (1.0 / 5.0)
    return r.ewm(alpha=alpha, adjust=False, min_periods=5).std()


def f48_ssat_334_ewma_std_returns_63(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    alpha = 1.0 - 0.5 ** (1.0 / MDAYS)
    return r.ewm(alpha=alpha, adjust=False, min_periods=MDAYS).std()


def f48_ssat_335_cvar_95_past_63(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    q5 = r.rolling(QDAYS, min_periods=MDAYS).quantile(0.05)
    cvar = r.where(r <= q5, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    return cvar


def f48_ssat_336_cvar_99_past_252(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    q1 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.01)
    cvar = r.where(r <= q1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return cvar


def f48_ssat_337_max_drawdown_past_21(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.rolling(MDAYS, min_periods=WDAYS).min()


def f48_ssat_338_max_drawdown_past_63(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.rolling(QDAYS, min_periods=MDAYS).min()


def f48_ssat_339_drawdown_duration_252(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(high == rmax)


def f48_ssat_340_recovery_factor(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    dd_min = dd.rolling(YDAYS, min_periods=QDAYS).min()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bars_since = _bars_since_true(high == rmax)
    return _safe_div(dd_min, bars_since + 1.0)


def f48_ssat_341_downside_deviation_63(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    neg = r.where(r < 0, 0.0)
    return (neg ** 2).rolling(QDAYS, min_periods=MDAYS).mean().pow(0.5)


def f48_ssat_342_downside_deviation_252(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    neg = r.where(r < 0, 0.0)
    return (neg ** 2).rolling(YDAYS, min_periods=QDAYS).mean().pow(0.5)


def f48_ssat_343_profitable_bars_fraction_21(open_: pd.Series, close: pd.Series) -> pd.Series:
    return (close > open_).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().where(open_.notna(), np.nan)


def f48_ssat_344_profitable_bars_fraction_63(open_: pd.Series, close: pd.Series) -> pd.Series:
    return (close > open_).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(open_.notna(), np.nan)


def f48_ssat_345_profitable_bars_fraction_252(open_: pd.Series, close: pd.Series) -> pd.Series:
    return (close > open_).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(open_.notna(), np.nan)


def f48_ssat_346_up_streak_3plus_count_252(close: pd.Series) -> pd.Series:
    up = (close > close.shift(1))
    s = _streak_true(up)
    event = ((s == 3) & (s.shift(1) == 2)).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum().where(up.notna(), np.nan)


def f48_ssat_347_down_streak_3plus_count_252(close: pd.Series) -> pd.Series:
    dn = (close < close.shift(1))
    s = _streak_true(dn)
    event = ((s == 3) & (s.shift(1) == 2)).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum().where(dn.notna(), np.nan)


def f48_ssat_348_q75_returns_past_63(close: pd.Series) -> pd.Series:
    return close.pct_change().rolling(QDAYS, min_periods=MDAYS).quantile(0.75)


def f48_ssat_349_q25_returns_past_63(close: pd.Series) -> pd.Series:
    return close.pct_change().rolling(QDAYS, min_periods=MDAYS).quantile(0.25)


def f48_ssat_350_iqr_returns_past_252(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    return r.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - r.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)


def f48_ssat_351_drawdown_var_95_past_63(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.rolling(QDAYS, min_periods=MDAYS).quantile(0.05)


def f48_ssat_352_drawdown_var_99_past_252(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.rolling(YDAYS, min_periods=QDAYS).quantile(0.01)


def f48_ssat_353_drawdown_cvar_past_63(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    q5 = dd.rolling(QDAYS, min_periods=MDAYS).quantile(0.05)
    return dd.where(dd <= q5, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f48_ssat_354_drawdown_below_10pct_streak_current(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return _streak_true(dd < -0.10).where(dd.notna(), np.nan)


def f48_ssat_355_drawdown_below_50pct_streak_current(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return _streak_true(dd < -0.50).where(dd.notna(), np.nan)


def f48_ssat_356_longest_drawdown_below_50pct_streak_252(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    s = _streak_true(dd < -0.50)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(dd.notna(), np.nan)


def f48_ssat_357_bars_since_drawdown_crossed_neg10(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    ev = (dd.shift(1) >= -0.10) & (dd < -0.10)
    return _bars_since_true(ev)


def f48_ssat_358_bars_since_drawdown_crossed_neg50(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    ev = (dd.shift(1) >= -0.50) & (dd < -0.50)
    return _bars_since_true(ev)


def f48_ssat_359_max_drawup_past_252(low: pd.Series, close: pd.Series) -> pd.Series:
    return (_safe_div(close, low.rolling(YDAYS, min_periods=QDAYS).min()) - 1.0).rolling(YDAYS, min_periods=QDAYS).max()


def f48_ssat_360_drawup_drawdown_ratio_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    du = (_safe_div(close, low.rolling(YDAYS, min_periods=QDAYS).min()) - 1.0).rolling(YDAYS, min_periods=QDAYS).max()
    dd = (_safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0).rolling(YDAYS, min_periods=QDAYS).min().abs()
    return _safe_div(du, dd)


def f48_ssat_361_ext_above_3_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e > 3.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f48_ssat_362_ext_above_3_then_revert_within_5_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    cond = (e.shift(WDAYS) > 3.0) & (e < 0)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f48_ssat_363_ext_above_3_then_not_revert_within_21_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    cond = (e.shift(MDAYS) > 3.0) & (e > 1.0)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f48_ssat_364_mean_reversion_failure_rate_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    ext_events = (e.shift(MDAYS) > 3.0).astype(float)
    failures = ((e.shift(MDAYS) > 3.0) & (e > 1.0)).astype(float)
    return _safe_div(failures.rolling(YDAYS, min_periods=QDAYS).sum(), ext_events.rolling(YDAYS, min_periods=QDAYS).sum())


def f48_ssat_365_persistent_trend_score_63(close: pd.Series) -> pd.Series:
    up = (close > close.shift(1))
    dn = (close < close.shift(1))
    s_up = _streak_true(up)
    s_dn = _streak_true(dn)
    s = pd.concat([s_up, s_dn], axis=1).max(axis=1)
    return s.rolling(QDAYS, min_periods=MDAYS).max().where(up.notna(), np.nan)


def f48_ssat_366_bars_since_trend_reversal_252(close: pd.Series) -> pd.Series:
    from numpy import sign
    sl = close.rolling(MDAYS, min_periods=WDAYS).apply(
        lambda w: np.polyfit(np.arange(len(w)), w, 1)[0] if (~np.isnan(w)).sum() > 2 else np.nan,
        raw=True,
    )
    sgn = sign(sl)
    return _bars_since_true((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna())


def f48_ssat_367_efficiency_ratio_252(close: pd.Series) -> pd.Series:
    net_chg = (close - close.shift(YDAYS)).abs()
    sum_abs = close.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net_chg, sum_abs)


def f48_ssat_368_efficiency_ratio_504(close: pd.Series) -> pd.Series:
    net_chg = (close - close.shift(DDAYS_2Y)).abs()
    sum_abs = close.diff().abs().rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return _safe_div(net_chg, sum_abs)


def f48_ssat_369_vol_in_bottom_25pct_21d_range_past_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(MDAYS, min_periods=WDAYS).max()
    ll = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos < 0.25)
    return (volume.where(cond, 0.0)).rolling(QDAYS, min_periods=MDAYS).sum().where(pos.notna(), np.nan)


def f48_ssat_370_vol_in_bottom_25pct_252d_range_past_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos < 0.25)
    return (volume.where(cond, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum().where(pos.notna(), np.nan)


def f48_ssat_371_vol_on_heaviest_decline_days_past_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = close.pct_change()
    def _f(w):
        return np.nan  # placeholder
    n = len(close)
    out = np.full(n, np.nan)
    r_arr = r.to_numpy(dtype=float)
    v_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - QDAYS + 1)
        ret_w = r_arr[lo : t + 1]
        vol_w = v_arr[lo : t + 1]
        valid = ~np.isnan(ret_w) & ~np.isnan(vol_w)
        if valid.sum() < MDAYS:
            continue
        rw = ret_w[valid]; vw = vol_w[valid]
        if rw.size < 5:
            continue
        idx_sorted = np.argsort(rw)[:5]
        out[t] = float(vw[idx_sorted].sum())
    return pd.Series(out, index=close.index)


def f48_ssat_372_largest_single_decline_pct(close: pd.Series) -> pd.Series:
    return close.pct_change().rolling(YDAYS, min_periods=QDAYS).min()


def f48_ssat_373_bottom_of_range_vol_concentration_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos < 0.25)
    num = (volume.where(cond, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    den = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den)


def f48_ssat_374_vol_below_sma200_past_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    sma = _sma(close, 200)
    return (volume.where(close < sma, 0.0)).rolling(QDAYS, min_periods=MDAYS).sum().where(sma.notna(), np.nan)


def f48_ssat_375_vol_below_sma200_past_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    sma = _sma(close, 200)
    return (volume.where(close < sma, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum().where(sma.notna(), np.nan)


def f48_ssat_301_si_over_21d_avg_volume_d3(shortinterest, volume):
    return f48_ssat_301_si_over_21d_avg_volume(shortinterest, volume).diff().diff().diff()


def f48_ssat_302_si_over_21d_total_volume_alt_d3(shortinterest, volume):
    return f48_ssat_302_si_over_21d_total_volume_alt(shortinterest, volume).diff().diff().diff()


def f48_ssat_303_si_over_63d_avg_volume_d3(shortinterest, volume):
    return f48_ssat_303_si_over_63d_avg_volume(shortinterest, volume).diff().diff().diff()


def f48_ssat_304_si_over_252d_avg_volume_d3(shortinterest, volume):
    return f48_ssat_304_si_over_252d_avg_volume(shortinterest, volume).diff().diff().diff()


def f48_ssat_305_dtc_over_median_dtc_252_d3(daystocover):
    return f48_ssat_305_dtc_over_median_dtc_252(daystocover).diff().diff().diff()


def f48_ssat_306_shortpctfloat_over_median_252_d3(shortpctfloat):
    return f48_ssat_306_shortpctfloat_over_median_252(shortpctfloat).diff().diff().diff()


def f48_ssat_307_si_1m_change_over_21d_total_vol_d3(shortinterest, volume):
    return f48_ssat_307_si_1m_change_over_21d_total_vol(shortinterest, volume).diff().diff().diff()


def f48_ssat_308_si_3m_change_over_63d_total_vol_d3(shortinterest, volume):
    return f48_ssat_308_si_3m_change_over_63d_total_vol(shortinterest, volume).diff().diff().diff()


def f48_ssat_309_hl_range_over_volume_d3(high, low, volume):
    return f48_ssat_309_hl_range_over_volume(high, low, volume).diff().diff().diff()


def f48_ssat_310_hl_range_over_volume_sma_21_d3(high, low, volume):
    return f48_ssat_310_hl_range_over_volume_sma_21(high, low, volume).diff().diff().diff()


def f48_ssat_311_si_cv_21_d3(shortinterest):
    return f48_ssat_311_si_cv_21(shortinterest).diff().diff().diff()


def f48_ssat_312_si_cv_63_d3(shortinterest):
    return f48_ssat_312_si_cv_63(shortinterest).diff().diff().diff()


def f48_ssat_313_si_top5_share_252_d3(shortinterest):
    return f48_ssat_313_si_top5_share_252(shortinterest).diff().diff().diff()


def f48_ssat_314_si_skew_252_d3(shortinterest):
    return f48_ssat_314_si_skew_252(shortinterest).diff().diff().diff()


def f48_ssat_315_si_kurt_252_d3(shortinterest):
    return f48_ssat_315_si_kurt_252(shortinterest).diff().diff().diff()


def f48_ssat_316_si_21d_range_over_mean_d3(shortinterest):
    return f48_ssat_316_si_21d_range_over_mean(shortinterest).diff().diff().diff()


def f48_ssat_317_si_mad_252_d3(shortinterest):
    return f48_ssat_317_si_mad_252(shortinterest).diff().diff().diff()


def f48_ssat_318_bars_since_si_252d_low_d3(shortinterest):
    return f48_ssat_318_bars_since_si_252d_low(shortinterest).diff().diff().diff()


def f48_ssat_319_dcb_flag_d3(high, low, close, volume):
    return f48_ssat_319_dcb_flag(high, low, close, volume).diff().diff().diff()


def f48_ssat_320_dcb_count_63_d3(high, low, close, volume):
    return f48_ssat_320_dcb_count_63(high, low, close, volume).diff().diff().diff()


def f48_ssat_321_dcb_count_252_d3(high, low, close, volume):
    return f48_ssat_321_dcb_count_252(high, low, close, volume).diff().diff().diff()


def f48_ssat_322_head_and_shoulders_right_shoulder_flag_d3(high, close):
    return f48_ssat_322_head_and_shoulders_right_shoulder_flag(high, close).diff().diff().diff()


def f48_ssat_323_head_and_shoulders_neckline_break_d3(high, low, close):
    return f48_ssat_323_head_and_shoulders_neckline_break(high, low, close).diff().diff().diff()


def f48_ssat_324_neckline_break_count_252_d3(high, low, close):
    return f48_ssat_324_neckline_break_count_252(high, low, close).diff().diff().diff()


def f48_ssat_325_failed_bounce_count_63_d3(high, low, close):
    return f48_ssat_325_failed_bounce_count_63(high, low, close).diff().diff().diff()


def f48_ssat_326_bounce_fade_rate_63_d3(close):
    return f48_ssat_326_bounce_fade_rate_63(close).diff().diff().diff()


def f48_ssat_327_ewma_return_21_hl5_d3(close):
    return f48_ssat_327_ewma_return_21_hl5(close).diff().diff().diff()


def f48_ssat_328_ewma_return_63_hl21_d3(close):
    return f48_ssat_328_ewma_return_63_hl21(close).diff().diff().diff()


def f48_ssat_329_linearly_weighted_return_21_d3(close):
    return f48_ssat_329_linearly_weighted_return_21(close).diff().diff().diff()


def f48_ssat_330_linearly_weighted_return_63_d3(close):
    return f48_ssat_330_linearly_weighted_return_63(close).diff().diff().diff()


def f48_ssat_331_ewma_volume_21_d3(volume):
    return f48_ssat_331_ewma_volume_21(volume).diff().diff().diff()


def f48_ssat_332_ewma_rsi_21_d3(close):
    return f48_ssat_332_ewma_rsi_21(close).diff().diff().diff()


def f48_ssat_333_ewma_std_returns_21_d3(close):
    return f48_ssat_333_ewma_std_returns_21(close).diff().diff().diff()


def f48_ssat_334_ewma_std_returns_63_d3(close):
    return f48_ssat_334_ewma_std_returns_63(close).diff().diff().diff()


def f48_ssat_335_cvar_95_past_63_d3(close):
    return f48_ssat_335_cvar_95_past_63(close).diff().diff().diff()


def f48_ssat_336_cvar_99_past_252_d3(close):
    return f48_ssat_336_cvar_99_past_252(close).diff().diff().diff()


def f48_ssat_337_max_drawdown_past_21_d3(high, close):
    return f48_ssat_337_max_drawdown_past_21(high, close).diff().diff().diff()


def f48_ssat_338_max_drawdown_past_63_d3(high, close):
    return f48_ssat_338_max_drawdown_past_63(high, close).diff().diff().diff()


def f48_ssat_339_drawdown_duration_252_d3(high, close):
    return f48_ssat_339_drawdown_duration_252(high, close).diff().diff().diff()


def f48_ssat_340_recovery_factor_d3(high, close):
    return f48_ssat_340_recovery_factor(high, close).diff().diff().diff()


def f48_ssat_341_downside_deviation_63_d3(close):
    return f48_ssat_341_downside_deviation_63(close).diff().diff().diff()


def f48_ssat_342_downside_deviation_252_d3(close):
    return f48_ssat_342_downside_deviation_252(close).diff().diff().diff()


def f48_ssat_343_profitable_bars_fraction_21_d3(open_, close):
    return f48_ssat_343_profitable_bars_fraction_21(open_, close).diff().diff().diff()


def f48_ssat_344_profitable_bars_fraction_63_d3(open_, close):
    return f48_ssat_344_profitable_bars_fraction_63(open_, close).diff().diff().diff()


def f48_ssat_345_profitable_bars_fraction_252_d3(open_, close):
    return f48_ssat_345_profitable_bars_fraction_252(open_, close).diff().diff().diff()


def f48_ssat_346_up_streak_3plus_count_252_d3(close):
    return f48_ssat_346_up_streak_3plus_count_252(close).diff().diff().diff()


def f48_ssat_347_down_streak_3plus_count_252_d3(close):
    return f48_ssat_347_down_streak_3plus_count_252(close).diff().diff().diff()


def f48_ssat_348_q75_returns_past_63_d3(close):
    return f48_ssat_348_q75_returns_past_63(close).diff().diff().diff()


def f48_ssat_349_q25_returns_past_63_d3(close):
    return f48_ssat_349_q25_returns_past_63(close).diff().diff().diff()


def f48_ssat_350_iqr_returns_past_252_d3(close):
    return f48_ssat_350_iqr_returns_past_252(close).diff().diff().diff()


def f48_ssat_351_drawdown_var_95_past_63_d3(high, close):
    return f48_ssat_351_drawdown_var_95_past_63(high, close).diff().diff().diff()


def f48_ssat_352_drawdown_var_99_past_252_d3(high, close):
    return f48_ssat_352_drawdown_var_99_past_252(high, close).diff().diff().diff()


def f48_ssat_353_drawdown_cvar_past_63_d3(high, close):
    return f48_ssat_353_drawdown_cvar_past_63(high, close).diff().diff().diff()


def f48_ssat_354_drawdown_below_10pct_streak_current_d3(high, close):
    return f48_ssat_354_drawdown_below_10pct_streak_current(high, close).diff().diff().diff()


def f48_ssat_355_drawdown_below_50pct_streak_current_d3(high, close):
    return f48_ssat_355_drawdown_below_50pct_streak_current(high, close).diff().diff().diff()


def f48_ssat_356_longest_drawdown_below_50pct_streak_252_d3(high, close):
    return f48_ssat_356_longest_drawdown_below_50pct_streak_252(high, close).diff().diff().diff()


def f48_ssat_357_bars_since_drawdown_crossed_neg10_d3(high, close):
    return f48_ssat_357_bars_since_drawdown_crossed_neg10(high, close).diff().diff().diff()


def f48_ssat_358_bars_since_drawdown_crossed_neg50_d3(high, close):
    return f48_ssat_358_bars_since_drawdown_crossed_neg50(high, close).diff().diff().diff()


def f48_ssat_359_max_drawup_past_252_d3(low, close):
    return f48_ssat_359_max_drawup_past_252(low, close).diff().diff().diff()


def f48_ssat_360_drawup_drawdown_ratio_252_d3(high, low, close):
    return f48_ssat_360_drawup_drawdown_ratio_252(high, low, close).diff().diff().diff()


def f48_ssat_361_ext_above_3_count_63_d3(high, low, close):
    return f48_ssat_361_ext_above_3_count_63(high, low, close).diff().diff().diff()


def f48_ssat_362_ext_above_3_then_revert_within_5_count_63_d3(high, low, close):
    return f48_ssat_362_ext_above_3_then_revert_within_5_count_63(high, low, close).diff().diff().diff()


def f48_ssat_363_ext_above_3_then_not_revert_within_21_count_63_d3(high, low, close):
    return f48_ssat_363_ext_above_3_then_not_revert_within_21_count_63(high, low, close).diff().diff().diff()


def f48_ssat_364_mean_reversion_failure_rate_252_d3(high, low, close):
    return f48_ssat_364_mean_reversion_failure_rate_252(high, low, close).diff().diff().diff()


def f48_ssat_365_persistent_trend_score_63_d3(close):
    return f48_ssat_365_persistent_trend_score_63(close).diff().diff().diff()


def f48_ssat_366_bars_since_trend_reversal_252_d3(close):
    return f48_ssat_366_bars_since_trend_reversal_252(close).diff().diff().diff()


def f48_ssat_367_efficiency_ratio_252_d3(close):
    return f48_ssat_367_efficiency_ratio_252(close).diff().diff().diff()


def f48_ssat_368_efficiency_ratio_504_d3(close):
    return f48_ssat_368_efficiency_ratio_504(close).diff().diff().diff()


def f48_ssat_369_vol_in_bottom_25pct_21d_range_past_63_d3(high, low, close, volume):
    return f48_ssat_369_vol_in_bottom_25pct_21d_range_past_63(high, low, close, volume).diff().diff().diff()


def f48_ssat_370_vol_in_bottom_25pct_252d_range_past_252_d3(high, low, close, volume):
    return f48_ssat_370_vol_in_bottom_25pct_252d_range_past_252(high, low, close, volume).diff().diff().diff()


def f48_ssat_371_vol_on_heaviest_decline_days_past_63_d3(close, volume):
    return f48_ssat_371_vol_on_heaviest_decline_days_past_63(close, volume).diff().diff().diff()


def f48_ssat_372_largest_single_decline_pct_d3(close):
    return f48_ssat_372_largest_single_decline_pct(close).diff().diff().diff()


def f48_ssat_373_bottom_of_range_vol_concentration_252_d3(high, low, close, volume):
    return f48_ssat_373_bottom_of_range_vol_concentration_252(high, low, close, volume).diff().diff().diff()


def f48_ssat_374_vol_below_sma200_past_63_d3(close, volume):
    return f48_ssat_374_vol_below_sma200_past_63(close, volume).diff().diff().diff()


def f48_ssat_375_vol_below_sma200_past_252_d3(close, volume):
    return f48_ssat_375_vol_below_sma200_past_252(close, volume).diff().diff().diff()


_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_HC = ["high", "close"]
_CV = ["close", "volume"]


SHORT_SQUEEZE_AFTERMATH_TECHNICAL_D3_REGISTRY_301_375 = {
    "f48_ssat_301_si_over_21d_avg_volume_d3": {"inputs": ["shortinterest", "volume"], "func": f48_ssat_301_si_over_21d_avg_volume_d3},
    "f48_ssat_302_si_over_21d_total_volume_alt_d3": {"inputs": ["shortinterest", "volume"], "func": f48_ssat_302_si_over_21d_total_volume_alt_d3},
    "f48_ssat_303_si_over_63d_avg_volume_d3": {"inputs": ["shortinterest", "volume"], "func": f48_ssat_303_si_over_63d_avg_volume_d3},
    "f48_ssat_304_si_over_252d_avg_volume_d3": {"inputs": ["shortinterest", "volume"], "func": f48_ssat_304_si_over_252d_avg_volume_d3},
    "f48_ssat_305_dtc_over_median_dtc_252_d3": {"inputs": ["daystocover"], "func": f48_ssat_305_dtc_over_median_dtc_252_d3},
    "f48_ssat_306_shortpctfloat_over_median_252_d3": {"inputs": ["shortpctfloat"], "func": f48_ssat_306_shortpctfloat_over_median_252_d3},
    "f48_ssat_307_si_1m_change_over_21d_total_vol_d3": {"inputs": ["shortinterest", "volume"], "func": f48_ssat_307_si_1m_change_over_21d_total_vol_d3},
    "f48_ssat_308_si_3m_change_over_63d_total_vol_d3": {"inputs": ["shortinterest", "volume"], "func": f48_ssat_308_si_3m_change_over_63d_total_vol_d3},
    "f48_ssat_309_hl_range_over_volume_d3": {"inputs": ["high", "low", "volume"], "func": f48_ssat_309_hl_range_over_volume_d3},
    "f48_ssat_310_hl_range_over_volume_sma_21_d3": {"inputs": ["high", "low", "volume"], "func": f48_ssat_310_hl_range_over_volume_sma_21_d3},
    "f48_ssat_311_si_cv_21_d3": {"inputs": ["shortinterest"], "func": f48_ssat_311_si_cv_21_d3},
    "f48_ssat_312_si_cv_63_d3": {"inputs": ["shortinterest"], "func": f48_ssat_312_si_cv_63_d3},
    "f48_ssat_313_si_top5_share_252_d3": {"inputs": ["shortinterest"], "func": f48_ssat_313_si_top5_share_252_d3},
    "f48_ssat_314_si_skew_252_d3": {"inputs": ["shortinterest"], "func": f48_ssat_314_si_skew_252_d3},
    "f48_ssat_315_si_kurt_252_d3": {"inputs": ["shortinterest"], "func": f48_ssat_315_si_kurt_252_d3},
    "f48_ssat_316_si_21d_range_over_mean_d3": {"inputs": ["shortinterest"], "func": f48_ssat_316_si_21d_range_over_mean_d3},
    "f48_ssat_317_si_mad_252_d3": {"inputs": ["shortinterest"], "func": f48_ssat_317_si_mad_252_d3},
    "f48_ssat_318_bars_since_si_252d_low_d3": {"inputs": ["shortinterest"], "func": f48_ssat_318_bars_since_si_252d_low_d3},
    "f48_ssat_319_dcb_flag_d3": {"inputs": _HLCV, "func": f48_ssat_319_dcb_flag_d3},
    "f48_ssat_320_dcb_count_63_d3": {"inputs": _HLCV, "func": f48_ssat_320_dcb_count_63_d3},
    "f48_ssat_321_dcb_count_252_d3": {"inputs": _HLCV, "func": f48_ssat_321_dcb_count_252_d3},
    "f48_ssat_322_head_and_shoulders_right_shoulder_flag_d3": {"inputs": _HC, "func": f48_ssat_322_head_and_shoulders_right_shoulder_flag_d3},
    "f48_ssat_323_head_and_shoulders_neckline_break_d3": {"inputs": _HLC, "func": f48_ssat_323_head_and_shoulders_neckline_break_d3},
    "f48_ssat_324_neckline_break_count_252_d3": {"inputs": _HLC, "func": f48_ssat_324_neckline_break_count_252_d3},
    "f48_ssat_325_failed_bounce_count_63_d3": {"inputs": _HLC, "func": f48_ssat_325_failed_bounce_count_63_d3},
    "f48_ssat_326_bounce_fade_rate_63_d3": {"inputs": ["close"], "func": f48_ssat_326_bounce_fade_rate_63_d3},
    "f48_ssat_327_ewma_return_21_hl5_d3": {"inputs": ["close"], "func": f48_ssat_327_ewma_return_21_hl5_d3},
    "f48_ssat_328_ewma_return_63_hl21_d3": {"inputs": ["close"], "func": f48_ssat_328_ewma_return_63_hl21_d3},
    "f48_ssat_329_linearly_weighted_return_21_d3": {"inputs": ["close"], "func": f48_ssat_329_linearly_weighted_return_21_d3},
    "f48_ssat_330_linearly_weighted_return_63_d3": {"inputs": ["close"], "func": f48_ssat_330_linearly_weighted_return_63_d3},
    "f48_ssat_331_ewma_volume_21_d3": {"inputs": ["volume"], "func": f48_ssat_331_ewma_volume_21_d3},
    "f48_ssat_332_ewma_rsi_21_d3": {"inputs": ["close"], "func": f48_ssat_332_ewma_rsi_21_d3},
    "f48_ssat_333_ewma_std_returns_21_d3": {"inputs": ["close"], "func": f48_ssat_333_ewma_std_returns_21_d3},
    "f48_ssat_334_ewma_std_returns_63_d3": {"inputs": ["close"], "func": f48_ssat_334_ewma_std_returns_63_d3},
    "f48_ssat_335_cvar_95_past_63_d3": {"inputs": ["close"], "func": f48_ssat_335_cvar_95_past_63_d3},
    "f48_ssat_336_cvar_99_past_252_d3": {"inputs": ["close"], "func": f48_ssat_336_cvar_99_past_252_d3},
    "f48_ssat_337_max_drawdown_past_21_d3": {"inputs": _HC, "func": f48_ssat_337_max_drawdown_past_21_d3},
    "f48_ssat_338_max_drawdown_past_63_d3": {"inputs": _HC, "func": f48_ssat_338_max_drawdown_past_63_d3},
    "f48_ssat_339_drawdown_duration_252_d3": {"inputs": ["high", "close"], "func": f48_ssat_339_drawdown_duration_252_d3},
    "f48_ssat_340_recovery_factor_d3": {"inputs": _HC, "func": f48_ssat_340_recovery_factor_d3},
    "f48_ssat_341_downside_deviation_63_d3": {"inputs": ["close"], "func": f48_ssat_341_downside_deviation_63_d3},
    "f48_ssat_342_downside_deviation_252_d3": {"inputs": ["close"], "func": f48_ssat_342_downside_deviation_252_d3},
    "f48_ssat_343_profitable_bars_fraction_21_d3": {"inputs": ["open", "close"], "func": f48_ssat_343_profitable_bars_fraction_21_d3},
    "f48_ssat_344_profitable_bars_fraction_63_d3": {"inputs": ["open", "close"], "func": f48_ssat_344_profitable_bars_fraction_63_d3},
    "f48_ssat_345_profitable_bars_fraction_252_d3": {"inputs": ["open", "close"], "func": f48_ssat_345_profitable_bars_fraction_252_d3},
    "f48_ssat_346_up_streak_3plus_count_252_d3": {"inputs": ["close"], "func": f48_ssat_346_up_streak_3plus_count_252_d3},
    "f48_ssat_347_down_streak_3plus_count_252_d3": {"inputs": ["close"], "func": f48_ssat_347_down_streak_3plus_count_252_d3},
    "f48_ssat_348_q75_returns_past_63_d3": {"inputs": ["close"], "func": f48_ssat_348_q75_returns_past_63_d3},
    "f48_ssat_349_q25_returns_past_63_d3": {"inputs": ["close"], "func": f48_ssat_349_q25_returns_past_63_d3},
    "f48_ssat_350_iqr_returns_past_252_d3": {"inputs": ["close"], "func": f48_ssat_350_iqr_returns_past_252_d3},
    "f48_ssat_351_drawdown_var_95_past_63_d3": {"inputs": _HC, "func": f48_ssat_351_drawdown_var_95_past_63_d3},
    "f48_ssat_352_drawdown_var_99_past_252_d3": {"inputs": _HC, "func": f48_ssat_352_drawdown_var_99_past_252_d3},
    "f48_ssat_353_drawdown_cvar_past_63_d3": {"inputs": _HC, "func": f48_ssat_353_drawdown_cvar_past_63_d3},
    "f48_ssat_354_drawdown_below_10pct_streak_current_d3": {"inputs": _HC, "func": f48_ssat_354_drawdown_below_10pct_streak_current_d3},
    "f48_ssat_355_drawdown_below_50pct_streak_current_d3": {"inputs": _HC, "func": f48_ssat_355_drawdown_below_50pct_streak_current_d3},
    "f48_ssat_356_longest_drawdown_below_50pct_streak_252_d3": {"inputs": _HC, "func": f48_ssat_356_longest_drawdown_below_50pct_streak_252_d3},
    "f48_ssat_357_bars_since_drawdown_crossed_neg10_d3": {"inputs": _HC, "func": f48_ssat_357_bars_since_drawdown_crossed_neg10_d3},
    "f48_ssat_358_bars_since_drawdown_crossed_neg50_d3": {"inputs": _HC, "func": f48_ssat_358_bars_since_drawdown_crossed_neg50_d3},
    "f48_ssat_359_max_drawup_past_252_d3": {"inputs": ["low", "close"], "func": f48_ssat_359_max_drawup_past_252_d3},
    "f48_ssat_360_drawup_drawdown_ratio_252_d3": {"inputs": _HLC, "func": f48_ssat_360_drawup_drawdown_ratio_252_d3},
    "f48_ssat_361_ext_above_3_count_63_d3": {"inputs": _HLC, "func": f48_ssat_361_ext_above_3_count_63_d3},
    "f48_ssat_362_ext_above_3_then_revert_within_5_count_63_d3": {"inputs": _HLC, "func": f48_ssat_362_ext_above_3_then_revert_within_5_count_63_d3},
    "f48_ssat_363_ext_above_3_then_not_revert_within_21_count_63_d3": {"inputs": _HLC, "func": f48_ssat_363_ext_above_3_then_not_revert_within_21_count_63_d3},
    "f48_ssat_364_mean_reversion_failure_rate_252_d3": {"inputs": _HLC, "func": f48_ssat_364_mean_reversion_failure_rate_252_d3},
    "f48_ssat_365_persistent_trend_score_63_d3": {"inputs": ["close"], "func": f48_ssat_365_persistent_trend_score_63_d3},
    "f48_ssat_366_bars_since_trend_reversal_252_d3": {"inputs": ["close"], "func": f48_ssat_366_bars_since_trend_reversal_252_d3},
    "f48_ssat_367_efficiency_ratio_252_d3": {"inputs": ["close"], "func": f48_ssat_367_efficiency_ratio_252_d3},
    "f48_ssat_368_efficiency_ratio_504_d3": {"inputs": ["close"], "func": f48_ssat_368_efficiency_ratio_504_d3},
    "f48_ssat_369_vol_in_bottom_25pct_21d_range_past_63_d3": {"inputs": _HLCV, "func": f48_ssat_369_vol_in_bottom_25pct_21d_range_past_63_d3},
    "f48_ssat_370_vol_in_bottom_25pct_252d_range_past_252_d3": {"inputs": _HLCV, "func": f48_ssat_370_vol_in_bottom_25pct_252d_range_past_252_d3},
    "f48_ssat_371_vol_on_heaviest_decline_days_past_63_d3": {"inputs": _CV, "func": f48_ssat_371_vol_on_heaviest_decline_days_past_63_d3},
    "f48_ssat_372_largest_single_decline_pct_d3": {"inputs": ["close"], "func": f48_ssat_372_largest_single_decline_pct_d3},
    "f48_ssat_373_bottom_of_range_vol_concentration_252_d3": {"inputs": _HLCV, "func": f48_ssat_373_bottom_of_range_vol_concentration_252_d3},
    "f48_ssat_374_vol_below_sma200_past_63_d3": {"inputs": _CV, "func": f48_ssat_374_vol_below_sma200_past_63_d3},
    "f48_ssat_375_vol_below_sma200_past_252_d3": {"inputs": _CV, "func": f48_ssat_375_vol_below_sma200_past_252_d3},
}
