"""37_range_estimators_family d1 features 301-375 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _starc_position(close: pd.Series, high: pd.Series, low: pd.Series, n: int=MDAYS, k: float=2.0) -> pd.Series:
    m = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    atr = _atr(high, low, close, n=n)
    upper = m + k * atr
    lower = m - k * atr
    return _safe_div(close - lower, upper - lower)

def _heikin_ashi(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series):
    ha_close = (open_ + high + low + close) / 4.0
    ha_open = pd.Series(np.nan, index=close.index)
    ha_open.iloc[0] = (open_.iloc[0] + close.iloc[0]) / 2.0
    for i in range(1, len(close)):
        if np.isnan(ha_open.iat[i - 1]) or np.isnan(ha_close.iat[i - 1]):
            ha_open.iat[i] = (open_.iat[i] + close.iat[i]) / 2.0
        else:
            ha_open.iat[i] = (ha_open.iat[i - 1] + ha_close.iat[i - 1]) / 2.0
    ha_high = pd.concat([high, ha_open, ha_close], axis=1).max(axis=1)
    ha_low = pd.concat([low, ha_open, ha_close], axis=1).min(axis=1)
    return (ha_open, ha_high, ha_low, ha_close)

def _range_entropy_window(w: np.ndarray, bins: int=5) -> float:
    v = w[~np.isnan(w)]
    if v.size < 21:
        return np.nan
    q = np.linspace(0, 1, bins + 1)[1:-1]
    edges = np.quantile(v, q)
    digit = np.digitize(v, edges)
    _, cnts = np.unique(digit, return_counts=True)
    p = cnts / cnts.sum()
    return float(-(p * np.log2(p)).sum())

def _stoch(s: pd.Series, n: int) -> pd.Series:
    rmax = s.rolling(n, min_periods=max(n // 2, 2)).max()
    rmin = s.rolling(n, min_periods=max(n // 2, 2)).min()
    return _safe_div(s - rmin, rmax - rmin) * 100.0

def _near_peak_mask(close: pd.Series, lookback: int=YDAYS, tol: float=0.95) -> pd.Series:
    return close >= tol * close.rolling(lookback, min_periods=max(lookback // 3, 2)).max()

def f37_rges_301_vol_of_log_hl_21d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of log(H/L) over 21d — short-horizon range-volatility (vol-of-range)."""
    return np.log(_safe_div(high, low)).rolling(MDAYS, min_periods=WDAYS).std().diff()

def f37_rges_302_vol_of_log_hl_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of log(H/L) over 252d — annual vol-of-range."""
    return np.log(_safe_div(high, low)).rolling(YDAYS, min_periods=QDAYS).std().diff()

def f37_rges_303_vol_of_log_hl_ratio_21_252_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Vol-of-log(H/L)_21d / vol-of-log(H/L)_252d — short-vs-long vol-of-range ratio."""
    log_hl = np.log(_safe_div(high, low))
    s21 = log_hl.rolling(MDAYS, min_periods=WDAYS).std()
    s252 = log_hl.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(s21, s252).diff()

def f37_rges_304_vol_of_log_hl_z_in_504d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21d vol-of-log(H/L) in 504d distribution — vol-of-range regime extremity."""
    log_hl = np.log(_safe_div(high, low))
    s21 = log_hl.rolling(MDAYS, min_periods=WDAYS).std()
    return _rolling_zscore(s21, DDAYS_2Y, min_periods=YDAYS).diff()

def f37_rges_305_starc_position_21d_k2_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position in STARC band (SMA21 ± 2*ATR21) — 0 to 1 normalized; >1 = above upper band."""
    return _starc_position(close, high, low, MDAYS, 2.0).diff()

def f37_rges_306_starc_position_21d_k3_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position in STARC band (SMA21 ± 3*ATR21) — wider Keltner-style envelope."""
    return _starc_position(close, high, low, MDAYS, 3.0).diff()

def f37_rges_307_starc_position_63d_k2_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position in STARC band (SMA63 ± 2*ATR63) — quarter-horizon envelope position."""
    return _starc_position(close, high, low, QDAYS, 2.0).diff()

def f37_rges_308_starc_above_upper_indicator_21d_k2_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: close > SMA21 + 2*ATR21 — STARC upper-band breach (overbought)."""
    m = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    upper = m + 2.0 * atr
    return (close > upper).astype(float).where(upper.notna(), np.nan).diff()

def f37_rges_309_starc_below_lower_indicator_21d_k2_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: close < SMA21 - 2*ATR21 — STARC lower-band breach (oversold)."""
    m = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    lower = m - 2.0 * atr
    return (close < lower).astype(float).where(lower.notna(), np.nan).diff()

def f37_rges_310_donchian_20d_upper_breakout_indicator_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Indicator: close > trailing-20d max(high) (excluding today) — Donchian 20 upper breakout."""
    upper = high.rolling(20, min_periods=10).max().shift(1)
    return (close > upper).astype(float).where(upper.notna(), np.nan).diff()

def f37_rges_311_donchian_20d_lower_breakout_indicator_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: close < trailing-20d min(low) (excluding today) — Donchian 20 lower breakdown."""
    lower = low.rolling(20, min_periods=10).min().shift(1)
    return (close < lower).astype(float).where(lower.notna(), np.nan).diff()

def f37_rges_312_donchian_55d_upper_breakout_indicator_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Indicator: close > trailing-55d max(high) — turtle-trading-style longer-term breakout."""
    upper = high.rolling(55, min_periods=20).max().shift(1)
    return (close > upper).astype(float).where(upper.notna(), np.nan).diff()

def f37_rges_313_donchian_55d_lower_breakout_indicator_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: close < trailing-55d min(low) — turtle-style breakdown."""
    lower = low.rolling(55, min_periods=20).min().shift(1)
    return (close < lower).astype(float).where(lower.notna(), np.nan).diff()

def f37_rges_314_donchian_breakout_count_upper_252d_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of 20d-upper-breakouts in trailing 252d — sustained-strength frequency."""
    upper = high.rolling(20, min_periods=10).max().shift(1)
    bk = (close > upper).astype(float).where(upper.notna(), np.nan)
    return bk.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f37_rges_315_donchian_breakout_count_lower_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 20d-lower-breakdowns in trailing 252d — sustained-weakness frequency."""
    lower = low.rolling(20, min_periods=10).min().shift(1)
    bd = (close < lower).astype(float).where(lower.notna(), np.nan)
    return bd.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f37_rges_316_range_vs_volume_corr_252d_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """corr(log(H/L), log(volume)) over 252d — does range expand with volume? Positive = healthy expansion."""
    log_hl = np.log(_safe_div(high, low))
    log_vol = _safe_log(volume)
    pairs = pd.concat([log_hl.rename('r'), log_vol.rename('v')], axis=1)
    return pairs['r'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['v']).diff()

def f37_rges_317_range_divergence_with_volume_252d_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: 21d slope of log(H/L) > 0 AND 21d slope of log(volume) < 0 — range expanding while volume drops."""
    log_hl = np.log(_safe_div(high, low))
    log_vol = _safe_log(volume)
    rng_slope = _rolling_slope(log_hl, MDAYS)
    vol_slope = _rolling_slope(log_vol, MDAYS)
    return ((rng_slope > 0) & (vol_slope < 0)).astype(float).where(rng_slope.notna() & vol_slope.notna(), np.nan).diff()

def f37_rges_318_range_volume_ratio_252d_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean(log(H/L) / log(volume)) over 252d — range-per-unit-volume; high = inefficient (range-driven move)."""
    log_hl = np.log(_safe_div(high, low))
    log_vol = _safe_log(volume)
    return _safe_div(log_hl, log_vol).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f37_rges_319_range_volume_corr_at_peak_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """corr(log(H/L), log(vol)) evaluated only at near-peak bars over 252d — vol-confirmation at peak."""
    log_hl = np.log(_safe_div(high, low))
    log_vol = _safe_log(volume)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    mask = close >= 0.95 * peak
    pairs = pd.concat([log_hl.where(mask).rename('r'), log_vol.where(mask).rename('v')], axis=1)
    return pairs['r'].rolling(YDAYS, min_periods=WDAYS).corr(pairs['v']).diff()

def f37_rges_320_heikin_ashi_range_daily_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Heikin-Ashi range (HA_high - HA_low) — smoothed candle range."""
    _, hh, hl, _ = _heikin_ashi(open_, high, low, close)
    return (hh - hl).diff()

def f37_rges_321_heikin_ashi_log_range_21d_mean_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean log(HA_high / HA_low) over 21d — smoothed range over short horizon."""
    _, hh, hl, _ = _heikin_ashi(open_, high, low, close)
    return np.log(_safe_div(hh, hl)).rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f37_rges_322_heikin_ashi_body_to_range_daily_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|HA_close - HA_open| / (HA_high - HA_low) — HA body share of range; high = strong directional bar."""
    ho, hh, hl, hc = _heikin_ashi(open_, high, low, close)
    return _safe_div((hc - ho).abs(), hh - hl).diff()

def f37_rges_323_heikin_ashi_bullish_streak_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive HA bullish bars (HA_close > HA_open) — smoothed bullish streak counter."""
    ho, _, _, hc = _heikin_ashi(open_, high, low, close)
    bull = (hc > ho).values
    n = len(bull)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(hc.iat[i]) or np.isnan(ho.iat[i]):
            out[i] = np.nan
            streak = 0
        else:
            streak = streak + 1 if bull[i] else 0
            out[i] = float(streak)
    return pd.Series(out, index=close.index).diff()

def f37_rges_324_heikin_ashi_bearish_streak_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive HA bearish bars (HA_close < HA_open) — smoothed bearish streak counter."""
    ho, _, _, hc = _heikin_ashi(open_, high, low, close)
    bear = (hc < ho).values
    n = len(bear)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(hc.iat[i]) or np.isnan(ho.iat[i]):
            out[i] = np.nan
            streak = 0
        else:
            streak = streak + 1 if bear[i] else 0
            out[i] = float(streak)
    return pd.Series(out, index=close.index).diff()

def f37_rges_325_range_entropy_5bins_21d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Shannon entropy of log(H/L) (5 quantile bins) over 21d — short-horizon range-distribution diversity."""
    log_hl = np.log(_safe_div(high, low))
    return log_hl.rolling(MDAYS, min_periods=WDAYS).apply(_range_entropy_window, raw=True).diff()

def f37_rges_326_range_entropy_5bins_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Entropy of log(H/L) (5 bins) over 63d — quarterly range diversity."""
    log_hl = np.log(_safe_div(high, low))
    return log_hl.rolling(QDAYS, min_periods=MDAYS).apply(_range_entropy_window, raw=True).diff()

def f37_rges_327_range_entropy_5bins_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Entropy of log(H/L) (5 bins) over 252d — annual range diversity."""
    log_hl = np.log(_safe_div(high, low))
    return log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_range_entropy_window, raw=True).diff()

def f37_rges_328_range_entropy_10bins_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Entropy of log(H/L) (10 bins) over 252d — finer-grained range distribution."""
    log_hl = np.log(_safe_div(high, low))
    return log_hl.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _range_entropy_window(w, 10), raw=True).diff()

def f37_rges_329_range_entropy_change_21d_minus_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range entropy 21d - range entropy 252d — short vs long; positive = recent diversity > long-run."""
    log_hl = np.log(_safe_div(high, low))
    e21 = log_hl.rolling(MDAYS, min_periods=WDAYS).apply(_range_entropy_window, raw=True)
    e252 = log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_range_entropy_window, raw=True)
    return (e21 - e252).diff()

def f37_rges_330_pivot_line_slope_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d slope of (H+L+C)/3 — quarter-horizon pivot trend slope."""
    typical = (high + low + close) / 3.0
    return _rolling_slope(typical, QDAYS).diff()

def f37_rges_331_pivot_line_slope_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d slope of (H+L+C)/3 — annual pivot trend slope."""
    typical = (high + low + close) / 3.0
    return _rolling_slope(typical, YDAYS).diff()

def f37_rges_332_pivot_line_residual_std_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of residual from 63d linear fit of pivot (H+L+C)/3 — pivot-line noise."""
    typical = (high + low + close) / 3.0

    def _rs(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        x = np.arange(v.size, dtype=float)
        xm = x.mean()
        ym = v.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        b = ((x - xm) * (v - ym)).sum() / sxx
        a = ym - b * xm
        return float((v - (a + b * x)).std(ddof=1))
    return typical.rolling(QDAYS, min_periods=MDAYS).apply(_rs, raw=True).diff()

def f37_rges_333_pivot_line_r2_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """R^2 of 63d linear fit of pivot (H+L+C)/3 — how linearly does pivot trend?"""
    typical = (high + low + close) / 3.0

    def _r2(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        x = np.arange(v.size, dtype=float)
        xm = x.mean()
        ym = v.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        b = ((x - xm) * (v - ym)).sum() / sxx
        a = ym - b * xm
        yhat = a + b * x
        ssr = ((v - yhat) ** 2).sum()
        sst = ((v - ym) ** 2).sum()
        if sst == 0:
            return np.nan
        return float(1.0 - ssr / sst)
    return typical.rolling(QDAYS, min_periods=MDAYS).apply(_r2, raw=True).diff()

def f37_rges_334_log_hl_pct_rank_in_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's log(H/L) in trailing 63d distribution — short-horizon range extremity."""
    return np.log(_safe_div(high, low)).rolling(QDAYS, min_periods=MDAYS).rank(pct=True).diff()

def f37_rges_335_log_hl_pct_rank_in_1260d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's log(H/L) in trailing 1260d distribution — 5y range extremity."""
    return np.log(_safe_div(high, low)).rolling(DDAYS_5Y, min_periods=YDAYS).rank(pct=True).diff()

def f37_rges_336_log_hl_q05_in_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """5th percentile of log(H/L) in 252d — typical compressed range."""
    return np.log(_safe_div(high, low)).rolling(YDAYS, min_periods=QDAYS).quantile(0.05).diff()

def f37_rges_337_log_hl_q95_in_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """95th percentile of log(H/L) in 252d — typical expanded range."""
    return np.log(_safe_div(high, low)).rolling(YDAYS, min_periods=QDAYS).quantile(0.95).diff()

def f37_rges_338_log_hl_iqr_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """IQR (q75 - q25) of log(H/L) in 252d — interquartile range of range distribution."""
    log_hl = np.log(_safe_div(high, low))
    return (log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)).diff()

def f37_rges_339_log_hl_p90_p10_ratio_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """P90 / P10 of log(H/L) in 252d — outer-decile spread ratio."""
    log_hl = np.log(_safe_div(high, low))
    return _safe_div(log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.9), log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)).diff()

def f37_rges_340_nr4_count_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR4 occurrences in trailing 63d — quarterly compression frequency."""
    rng = high - low
    rmin4 = rng.rolling(4, min_periods=4).min()
    nr4 = (rng <= rmin4).astype(float).where(rmin4.notna(), np.nan)
    return nr4.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f37_rges_341_nr7_count_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 occurrences in trailing 252d — annual compression frequency."""
    rng = high - low
    rmin7 = rng.rolling(7, min_periods=7).min()
    nr7 = (rng <= rmin7).astype(float).where(rmin7.notna(), np.nan)
    return nr7.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f37_rges_342_wr4_count_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of WR4 in trailing 252d — annual expansion frequency."""
    rng = high - low
    rmax4 = rng.rolling(4, min_periods=4).max()
    wr4 = (rng >= rmax4).astype(float).where(rmax4.notna(), np.nan)
    return wr4.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f37_rges_343_nr_wr_ratio_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """count(NR7) / (1 + count(WR7)) in 252d — compression-vs-expansion balance."""
    rng = high - low
    rmin7 = rng.rolling(7, min_periods=7).min()
    rmax7 = rng.rolling(7, min_periods=7).max()
    nr7 = (rng <= rmin7).astype(float).where(rmin7.notna(), np.nan)
    wr7 = (rng >= rmax7).astype(float).where(rmax7.notna(), np.nan)
    return _safe_div(nr7.rolling(YDAYS, min_periods=QDAYS).sum(), 1.0 + wr7.rolling(YDAYS, min_periods=QDAYS).sum()).diff()

def f37_rges_344_log_hl_half_life_504d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Half-life (bars) of log(H/L) mean reversion over 504d — biennial range-shock decay."""
    log_hl = np.log(_safe_div(high, low))

    def _ac1(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1]
        b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ac1 = log_hl.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ac1, raw=True)
    return (-np.log(2.0) / np.log(ac1.where((ac1 > 0) & (ac1 < 1)))).diff()

def f37_rges_345_atr_acceleration_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d acceleration of ATR(21) — slope of (slope of ATR21)_63d."""
    s = _rolling_slope(_atr(high, low, close, n=MDAYS), QDAYS)
    return _rolling_slope(s, QDAYS).diff()

def f37_rges_346_log_hl_acceleration_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """63d acceleration of log(H/L) — second derivative of range."""
    s = _rolling_slope(np.log(_safe_div(high, low)), QDAYS)
    return _rolling_slope(s, QDAYS).diff()

def f37_rges_347_atr_persistence_lag5_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Autocorrelation of ATR(21) at lag 5 over 252d — weekly-spaced ATR persistence."""
    atr = _atr(high, low, close, n=MDAYS)
    pairs = pd.concat([atr.shift(5).rename('al'), atr.rename('a')], axis=1)
    return pairs['al'].rolling(YDAYS, min_periods=QDAYS).corr(pairs['a']).diff()

def f37_rges_348_kase_tqi_21d_d1(close: pd.Series) -> pd.Series:
    """Kase Trend Quality Index 21d proxy: |C_t - C_{t-21}| / sum(|delta C|) over 21d — efficient-move share."""
    net = (close - close.shift(MDAYS)).abs()
    path = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(net, path).diff()

def f37_rges_349_kase_tqi_63d_d1(close: pd.Series) -> pd.Series:
    """Kase TQI 63d proxy — quarterly trend efficiency."""
    net = (close - close.shift(QDAYS)).abs()
    path = close.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net, path).diff()

def f37_rges_350_kase_tqi_zscore_in_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of 21d Kase TQI in 252d distribution — trend-quality regime extremity."""
    net = (close - close.shift(MDAYS)).abs()
    path = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    tqi = _safe_div(net, path)
    return _rolling_zscore(tqi, YDAYS, min_periods=QDAYS).diff()

def f37_rges_351_range_stoch_14d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Stochastic (0-100) of log(H/L) over 14d — where is current range in the recent 14d distribution?"""
    return _stoch(np.log(_safe_div(high, low)), 14).diff()

def f37_rges_352_range_stoch_of_stoch_14d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Stochastic of (stochastic of log(H/L) 14d) over 14d — Schaff-style range cycle."""
    s1 = _stoch(np.log(_safe_div(high, low)), 14)
    return _stoch(s1, 14).diff()

def f37_rges_353_range_stoch_above_75_indicator_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: Schaff range cycle > 75 — overbought-range state."""
    s1 = _stoch(np.log(_safe_div(high, low)), 14)
    s2 = _stoch(s1, 14)
    return (s2 > 75.0).astype(float).where(s2.notna(), np.nan).diff()

def f37_rges_354_atr21_at_peak_mean_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21)/close evaluated at near-peak bars over 252d — typical normalized ATR at peaks."""
    atr_norm = _safe_div(_atr(high, low, close, n=MDAYS), close)
    mask = _near_peak_mask(close)
    return atr_norm.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f37_rges_355_log_hl_at_peak_mean_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean log(H/L) at near-peak bars over 252d — typical range at peaks."""
    log_hl = np.log(_safe_div(high, low))
    mask = _near_peak_mask(close)
    return log_hl.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f37_rges_356_wick_asym_at_peak_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (H-C) / (C-L) at near-peak bars over 252d — upper-wick dominance at peak (rejection)."""
    asym = _safe_div(high - close, close - low)
    mask = _near_peak_mask(close)
    return asym.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f37_rges_357_gap_count_at_peak_252d_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of gaps (|open - prior close| > ATR21) at near-peak bars in 252d."""
    pc = close.shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    flag = ((open_ - pc).abs() > atr21).astype(float).where(atr21.notna() & pc.notna(), np.nan)
    mask = _near_peak_mask(close)
    return flag.where(mask).rolling(YDAYS, min_periods=WDAYS).sum().diff()

def f37_rges_358_chop_at_peak_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CHOP(14) evaluated at near-peak bars over 252d — choppiness regime at peak."""
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(14, min_periods=7).sum()
    hi = high.rolling(14, min_periods=7).max()
    lo = low.rolling(14, min_periods=7).min()
    chop = 100.0 * np.log10(_safe_div(sum_tr, hi - lo)) / np.log10(14.0)
    mask = _near_peak_mask(close)
    return chop.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f37_rges_359_nr_wr_balance_at_peak_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """count(NR7)/count(WR7) at near-peak bars in 252d — compression-vs-expansion balance at peak."""
    rng = high - low
    rmin7 = rng.rolling(7, min_periods=7).min()
    rmax7 = rng.rolling(7, min_periods=7).max()
    nr7 = (rng <= rmin7).astype(float).where(rmin7.notna(), np.nan)
    wr7 = (rng >= rmax7).astype(float).where(rmax7.notna(), np.nan)
    mask = _near_peak_mask(close)
    return _safe_div(nr7.where(mask).rolling(YDAYS, min_periods=WDAYS).sum(), 1.0 + wr7.where(mask).rolling(YDAYS, min_periods=WDAYS).sum()).diff()

def f37_rges_360_range_skew_at_peak_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of log(H/L) at near-peak bars over 252d — peak-period range-distribution shape."""
    log_hl = np.log(_safe_div(high, low))
    mask = _near_peak_mask(close)
    sub = log_hl.where(mask)

    def _sk(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        m = v.mean()
        s = v.std(ddof=1)
        if s == 0:
            return np.nan
        return float(((v - m) ** 3).mean() / s ** 3)
    return sub.rolling(YDAYS, min_periods=WDAYS).apply(_sk, raw=True).diff()

def f37_rges_361_range_zscore_at_peak_504d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of log(H/L) in 504d distribution, evaluated only at near-peak bars — range extremity at peak."""
    log_hl = np.log(_safe_div(high, low))
    z = _rolling_zscore(log_hl, DDAYS_2Y, min_periods=YDAYS)
    mask = _near_peak_mask(close)
    return z.where(mask).diff()

def f37_rges_362_peak_blowoff_range_composite_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-blend of range-zscore-at-peak + ATR-at-peak + CHOP-at-peak (negated) — peak-blowoff range fingerprint."""
    log_hl = np.log(_safe_div(high, low))
    z_rng_full = _rolling_zscore(log_hl, DDAYS_2Y, min_periods=YDAYS)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    mask = close >= 0.95 * peak
    z_rng = z_rng_full.where(mask)
    atr_norm = _safe_div(_atr(high, low, close, n=MDAYS), close)
    atr_peak = atr_norm.where(mask).rolling(YDAYS, min_periods=WDAYS).mean()
    z_atr = _rolling_zscore(atr_peak, DDAYS_2Y, min_periods=YDAYS)
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(14, min_periods=7).sum()
    hi = high.rolling(14, min_periods=7).max()
    lo = low.rolling(14, min_periods=7).min()
    chop = 100.0 * np.log10(_safe_div(sum_tr, hi - lo)) / np.log10(14.0)
    chop_peak = chop.where(mask).rolling(YDAYS, min_periods=WDAYS).mean()
    z_chop = _rolling_zscore(-chop_peak, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_rng.rename('a'), z_atr.rename('b'), z_chop.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f37_rges_363_post_peak_breakdown_range_composite_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-blend of Donchian-55d lower-breakdown count + range slope (negated) + range entropy — post-peak breakdown profile."""
    lower = low.rolling(55, min_periods=20).min().shift(1)
    bd = (close < lower).astype(float).where(lower.notna(), np.nan)
    bd_cnt = bd.rolling(YDAYS, min_periods=QDAYS).sum()
    rng_slope = _rolling_slope(np.log(_safe_div(high, low)), MDAYS)
    log_hl = np.log(_safe_div(high, low))
    ent252 = log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_range_entropy_window, raw=True)
    z_b = _rolling_zscore(bd_cnt, DDAYS_2Y, min_periods=YDAYS)
    z_s = _rolling_zscore(-rng_slope, DDAYS_2Y, min_periods=YDAYS)
    z_e = _rolling_zscore(ent252, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_b.rename('a'), z_s.rename('b'), z_e.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f37_rges_364_compression_explosion_composite_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-blend of NR7-count + WR7-count + range-vol-of-range — compression-and-explosion alternation profile."""
    rng = high - low
    rmin7 = rng.rolling(7, min_periods=7).min()
    rmax7 = rng.rolling(7, min_periods=7).max()
    nr7 = (rng <= rmin7).astype(float).where(rmin7.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    wr7 = (rng >= rmax7).astype(float).where(rmax7.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    log_hl = np.log(_safe_div(high, low))
    vor = log_hl.rolling(MDAYS, min_periods=WDAYS).std()
    z_n = _rolling_zscore(nr7, DDAYS_2Y, min_periods=YDAYS)
    z_w = _rolling_zscore(wr7, DDAYS_2Y, min_periods=YDAYS)
    z_v = _rolling_zscore(vor, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_n.rename('a'), z_w.rename('b'), z_v.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f37_rges_365_trend_quality_decline_composite_252d_d1(close: pd.Series) -> pd.Series:
    """Z-blend of (negative) Kase TQI 63d + (negative) 63d cumret + Kase TQI z-score (negated) — declining trend-quality."""
    net = (close - close.shift(QDAYS)).abs()
    path = close.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    tqi = _safe_div(net, path)
    cum_ret = _safe_log(close).diff(QDAYS)
    z_t = _rolling_zscore(-tqi, DDAYS_2Y, min_periods=YDAYS)
    z_c = _rolling_zscore(-cum_ret, DDAYS_2Y, min_periods=YDAYS)
    z_tz = _rolling_zscore(-_rolling_zscore(tqi, YDAYS, min_periods=QDAYS), DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_t.rename('a'), z_c.rename('b'), z_tz.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f37_rges_366_starc_breach_count_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing-252d bars with close outside STARC(21, 2-ATR) band — sustained excursion frequency."""
    m = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    out_band = ((close > m + 2.0 * atr) | (close < m - 2.0 * atr)).astype(float).where(atr.notna(), np.nan)
    return out_band.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f37_rges_367_range_volume_divergence_at_peak_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: range slope > 0 AND volume slope < 0 AND at near-peak bar — range up, volume down, at peak."""
    log_hl = np.log(_safe_div(high, low))
    log_vol = _safe_log(volume)
    rs = _rolling_slope(log_hl, MDAYS)
    vs = _rolling_slope(log_vol, MDAYS)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return ((rs > 0) & (vs < 0) & near_peak).astype(float).where(rs.notna() & vs.notna(), np.nan).diff()

def f37_rges_368_heikin_ashi_bearish_persistence_252d_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars with HA bearish (HA_close < HA_open) — sustained-bearish-bar share."""
    ho, _, _, hc = _heikin_ashi(open_, high, low, close)
    bear = (hc < ho).astype(float).where(ho.notna() & hc.notna(), np.nan)
    return bear.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f37_rges_369_donchian_breakdown_severity_504d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Z-blend of 20d-down-breakouts + 55d-down-breakouts — multi-horizon-breakdown severity."""
    l20 = low.rolling(20, min_periods=10).min().shift(1)
    l55 = low.rolling(55, min_periods=20).min().shift(1)
    bd20 = (close < l20).astype(float).where(l20.notna(), np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    bd55 = (close < l55).astype(float).where(l55.notna(), np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    z20 = _rolling_zscore(bd20, DDAYS_2Y, min_periods=QDAYS)
    z55 = _rolling_zscore(bd55, DDAYS_2Y, min_periods=QDAYS)
    pieces = pd.concat([z20.rename('a'), z55.rename('b')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f37_rges_370_pivot_line_breakdown_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-blend of (negative) pivot-line slope + (negative) pivot-line R^2 — declining pivot trend."""
    typical = (high + low + close) / 3.0
    slope = _rolling_slope(typical, QDAYS)

    def _r2(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        x = np.arange(v.size, dtype=float)
        xm = x.mean()
        ym = v.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        b = ((x - xm) * (v - ym)).sum() / sxx
        a = ym - b * xm
        yhat = a + b * x
        ssr = ((v - yhat) ** 2).sum()
        sst = ((v - ym) ** 2).sum()
        if sst == 0:
            return np.nan
        return float(1.0 - ssr / sst)
    r2 = typical.rolling(QDAYS, min_periods=MDAYS).apply(_r2, raw=True)
    z_s = _rolling_zscore(-slope, DDAYS_2Y, min_periods=YDAYS)
    z_r = _rolling_zscore(-r2 * np.sign(slope), DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_s.rename('a'), z_r.rename('b')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f37_rges_371_range_distribution_extreme_composite_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-blend of log-HL P95 + log-HL IQR + log-HL P90/P10 ratio — extreme-range-distribution severity."""
    log_hl = np.log(_safe_div(high, low))
    q95 = log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    iqr = log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p9010 = _safe_div(log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.9), log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.1))
    z_q = _rolling_zscore(q95, DDAYS_2Y, min_periods=YDAYS)
    z_i = _rolling_zscore(iqr, DDAYS_2Y, min_periods=YDAYS)
    z_p = _rolling_zscore(p9010, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_q.rename('a'), z_i.rename('b'), z_p.rename('c')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f37_rges_372_schaff_range_overbought_at_peak_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Schaff-range-cycle (>75) indicator evaluated at near-peak bars over 252d — overbought-range at peak."""
    s1 = _stoch(np.log(_safe_div(high, low)), 14)
    s2 = _stoch(s1, 14)
    overbought = (s2 > 75.0).astype(float).where(s2.notna(), np.nan)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    mask = close >= 0.95 * peak
    return overbought.where(mask).rolling(YDAYS, min_periods=WDAYS).mean().diff()

def f37_rges_373_range_explosion_after_compression_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: NR7 in prior 5d AND WR7 today — coiled-then-released breakout."""
    rng = high - low
    rmin7 = rng.rolling(7, min_periods=7).min()
    rmax7 = rng.rolling(7, min_periods=7).max()
    nr7_prior = (rng <= rmin7).rolling(WDAYS, min_periods=2).max().shift(1) > 0
    wr7_today = rng >= rmax7
    return (nr7_prior & wr7_today).astype(float).where(rmin7.notna() & rmax7.notna(), np.nan).diff()

def f37_rges_374_heikin_ashi_bullish_to_bearish_flip_252d_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of HA bullish-to-bearish flips in trailing 252d — character-change-event frequency."""
    ho, _, _, hc = _heikin_ashi(open_, high, low, close)
    bull = hc > ho
    bear = hc < ho
    flip = (bear & bull.shift(1, fill_value=False)).astype(float).where(ho.notna() & hc.notna(), np.nan)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f37_rges_375_stuck_peak_full_range_composite_504d_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Master range composite for stuck-peak: peak-blowoff + post-peak-breakdown + trend-quality-decline + HA-bearish persistence."""
    log_hl = np.log(_safe_div(high, low))
    z_rng_full = _rolling_zscore(log_hl, DDAYS_2Y, min_periods=YDAYS)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    mask = close >= 0.95 * peak
    z_rng = z_rng_full.where(mask)
    lower = low.rolling(55, min_periods=20).min().shift(1)
    bd = (close < lower).astype(float).where(lower.notna(), np.nan)
    bd_cnt = bd.rolling(YDAYS, min_periods=QDAYS).sum()
    z_bd = _rolling_zscore(bd_cnt, DDAYS_2Y, min_periods=YDAYS)
    net = (close - close.shift(QDAYS)).abs()
    path = close.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    tqi = _safe_div(net, path)
    z_tq = _rolling_zscore(-tqi, DDAYS_2Y, min_periods=YDAYS)
    ho, _, _, hc = _heikin_ashi(open_, high, low, close)
    bear = (hc < ho).astype(float).where(ho.notna() & hc.notna(), np.nan)
    bear_share = bear.rolling(YDAYS, min_periods=QDAYS).mean()
    z_ha = _rolling_zscore(bear_share, DDAYS_2Y, min_periods=YDAYS)
    pieces = pd.concat([z_rng.rename('a'), z_bd.rename('b'), z_tq.rename('c'), z_ha.rename('d')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()
RANGE_ESTIMATORS_FAMILY_D1_REGISTRY_301_375 = {'f37_rges_301_vol_of_log_hl_21d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_301_vol_of_log_hl_21d_d1}, 'f37_rges_302_vol_of_log_hl_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_302_vol_of_log_hl_252d_d1}, 'f37_rges_303_vol_of_log_hl_ratio_21_252_d1': {'inputs': ['high', 'low'], 'func': f37_rges_303_vol_of_log_hl_ratio_21_252_d1}, 'f37_rges_304_vol_of_log_hl_z_in_504d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_304_vol_of_log_hl_z_in_504d_d1}, 'f37_rges_305_starc_position_21d_k2_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_305_starc_position_21d_k2_d1}, 'f37_rges_306_starc_position_21d_k3_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_306_starc_position_21d_k3_d1}, 'f37_rges_307_starc_position_63d_k2_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_307_starc_position_63d_k2_d1}, 'f37_rges_308_starc_above_upper_indicator_21d_k2_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_308_starc_above_upper_indicator_21d_k2_d1}, 'f37_rges_309_starc_below_lower_indicator_21d_k2_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_309_starc_below_lower_indicator_21d_k2_d1}, 'f37_rges_310_donchian_20d_upper_breakout_indicator_d1': {'inputs': ['close', 'high'], 'func': f37_rges_310_donchian_20d_upper_breakout_indicator_d1}, 'f37_rges_311_donchian_20d_lower_breakout_indicator_d1': {'inputs': ['close', 'low'], 'func': f37_rges_311_donchian_20d_lower_breakout_indicator_d1}, 'f37_rges_312_donchian_55d_upper_breakout_indicator_d1': {'inputs': ['close', 'high'], 'func': f37_rges_312_donchian_55d_upper_breakout_indicator_d1}, 'f37_rges_313_donchian_55d_lower_breakout_indicator_d1': {'inputs': ['close', 'low'], 'func': f37_rges_313_donchian_55d_lower_breakout_indicator_d1}, 'f37_rges_314_donchian_breakout_count_upper_252d_d1': {'inputs': ['close', 'high'], 'func': f37_rges_314_donchian_breakout_count_upper_252d_d1}, 'f37_rges_315_donchian_breakout_count_lower_252d_d1': {'inputs': ['close', 'low'], 'func': f37_rges_315_donchian_breakout_count_lower_252d_d1}, 'f37_rges_316_range_vs_volume_corr_252d_d1': {'inputs': ['high', 'low', 'volume'], 'func': f37_rges_316_range_vs_volume_corr_252d_d1}, 'f37_rges_317_range_divergence_with_volume_252d_d1': {'inputs': ['high', 'low', 'volume'], 'func': f37_rges_317_range_divergence_with_volume_252d_d1}, 'f37_rges_318_range_volume_ratio_252d_d1': {'inputs': ['high', 'low', 'volume'], 'func': f37_rges_318_range_volume_ratio_252d_d1}, 'f37_rges_319_range_volume_corr_at_peak_252d_d1': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f37_rges_319_range_volume_corr_at_peak_252d_d1}, 'f37_rges_320_heikin_ashi_range_daily_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_320_heikin_ashi_range_daily_d1}, 'f37_rges_321_heikin_ashi_log_range_21d_mean_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_321_heikin_ashi_log_range_21d_mean_d1}, 'f37_rges_322_heikin_ashi_body_to_range_daily_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_322_heikin_ashi_body_to_range_daily_d1}, 'f37_rges_323_heikin_ashi_bullish_streak_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_323_heikin_ashi_bullish_streak_d1}, 'f37_rges_324_heikin_ashi_bearish_streak_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_324_heikin_ashi_bearish_streak_d1}, 'f37_rges_325_range_entropy_5bins_21d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_325_range_entropy_5bins_21d_d1}, 'f37_rges_326_range_entropy_5bins_63d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_326_range_entropy_5bins_63d_d1}, 'f37_rges_327_range_entropy_5bins_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_327_range_entropy_5bins_252d_d1}, 'f37_rges_328_range_entropy_10bins_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_328_range_entropy_10bins_252d_d1}, 'f37_rges_329_range_entropy_change_21d_minus_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_329_range_entropy_change_21d_minus_252d_d1}, 'f37_rges_330_pivot_line_slope_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_330_pivot_line_slope_63d_d1}, 'f37_rges_331_pivot_line_slope_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_331_pivot_line_slope_252d_d1}, 'f37_rges_332_pivot_line_residual_std_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_332_pivot_line_residual_std_63d_d1}, 'f37_rges_333_pivot_line_r2_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_333_pivot_line_r2_63d_d1}, 'f37_rges_334_log_hl_pct_rank_in_63d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_334_log_hl_pct_rank_in_63d_d1}, 'f37_rges_335_log_hl_pct_rank_in_1260d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_335_log_hl_pct_rank_in_1260d_d1}, 'f37_rges_336_log_hl_q05_in_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_336_log_hl_q05_in_252d_d1}, 'f37_rges_337_log_hl_q95_in_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_337_log_hl_q95_in_252d_d1}, 'f37_rges_338_log_hl_iqr_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_338_log_hl_iqr_252d_d1}, 'f37_rges_339_log_hl_p90_p10_ratio_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_339_log_hl_p90_p10_ratio_252d_d1}, 'f37_rges_340_nr4_count_63d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_340_nr4_count_63d_d1}, 'f37_rges_341_nr7_count_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_341_nr7_count_252d_d1}, 'f37_rges_342_wr4_count_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_342_wr4_count_252d_d1}, 'f37_rges_343_nr_wr_ratio_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_343_nr_wr_ratio_252d_d1}, 'f37_rges_344_log_hl_half_life_504d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_344_log_hl_half_life_504d_d1}, 'f37_rges_345_atr_acceleration_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_345_atr_acceleration_63d_d1}, 'f37_rges_346_log_hl_acceleration_63d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_346_log_hl_acceleration_63d_d1}, 'f37_rges_347_atr_persistence_lag5_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_347_atr_persistence_lag5_252d_d1}, 'f37_rges_348_kase_tqi_21d_d1': {'inputs': ['close'], 'func': f37_rges_348_kase_tqi_21d_d1}, 'f37_rges_349_kase_tqi_63d_d1': {'inputs': ['close'], 'func': f37_rges_349_kase_tqi_63d_d1}, 'f37_rges_350_kase_tqi_zscore_in_252d_d1': {'inputs': ['close'], 'func': f37_rges_350_kase_tqi_zscore_in_252d_d1}, 'f37_rges_351_range_stoch_14d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_351_range_stoch_14d_d1}, 'f37_rges_352_range_stoch_of_stoch_14d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_352_range_stoch_of_stoch_14d_d1}, 'f37_rges_353_range_stoch_above_75_indicator_d1': {'inputs': ['high', 'low'], 'func': f37_rges_353_range_stoch_above_75_indicator_d1}, 'f37_rges_354_atr21_at_peak_mean_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_354_atr21_at_peak_mean_252d_d1}, 'f37_rges_355_log_hl_at_peak_mean_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_355_log_hl_at_peak_mean_252d_d1}, 'f37_rges_356_wick_asym_at_peak_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_356_wick_asym_at_peak_252d_d1}, 'f37_rges_357_gap_count_at_peak_252d_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_357_gap_count_at_peak_252d_d1}, 'f37_rges_358_chop_at_peak_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_358_chop_at_peak_252d_d1}, 'f37_rges_359_nr_wr_balance_at_peak_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_359_nr_wr_balance_at_peak_252d_d1}, 'f37_rges_360_range_skew_at_peak_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_360_range_skew_at_peak_252d_d1}, 'f37_rges_361_range_zscore_at_peak_504d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_361_range_zscore_at_peak_504d_d1}, 'f37_rges_362_peak_blowoff_range_composite_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_362_peak_blowoff_range_composite_252d_d1}, 'f37_rges_363_post_peak_breakdown_range_composite_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_363_post_peak_breakdown_range_composite_252d_d1}, 'f37_rges_364_compression_explosion_composite_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_364_compression_explosion_composite_252d_d1}, 'f37_rges_365_trend_quality_decline_composite_252d_d1': {'inputs': ['close'], 'func': f37_rges_365_trend_quality_decline_composite_252d_d1}, 'f37_rges_366_starc_breach_count_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_366_starc_breach_count_252d_d1}, 'f37_rges_367_range_volume_divergence_at_peak_252d_d1': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f37_rges_367_range_volume_divergence_at_peak_252d_d1}, 'f37_rges_368_heikin_ashi_bearish_persistence_252d_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_368_heikin_ashi_bearish_persistence_252d_d1}, 'f37_rges_369_donchian_breakdown_severity_504d_d1': {'inputs': ['close', 'low'], 'func': f37_rges_369_donchian_breakdown_severity_504d_d1}, 'f37_rges_370_pivot_line_breakdown_composite_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_370_pivot_line_breakdown_composite_252d_d1}, 'f37_rges_371_range_distribution_extreme_composite_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_371_range_distribution_extreme_composite_252d_d1}, 'f37_rges_372_schaff_range_overbought_at_peak_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_372_schaff_range_overbought_at_peak_252d_d1}, 'f37_rges_373_range_explosion_after_compression_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_373_range_explosion_after_compression_252d_d1}, 'f37_rges_374_heikin_ashi_bullish_to_bearish_flip_252d_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_374_heikin_ashi_bullish_to_bearish_flip_252d_d1}, 'f37_rges_375_stuck_peak_full_range_composite_504d_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_375_stuck_peak_full_range_composite_504d_d1}}