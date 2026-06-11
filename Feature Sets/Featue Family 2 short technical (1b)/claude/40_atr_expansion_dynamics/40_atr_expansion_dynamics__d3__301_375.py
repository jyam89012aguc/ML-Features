"""40_atr_expansion_dynamics d3 features 301-375 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import math
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

def _ema(s, n):
    return s.ewm(span=n, min_periods=n, adjust=False).mean()

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

def _bars_since(ind):
    arr = ind.fillna(0).astype(int).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, x in enumerate(arr):
        if x:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=ind.index)

def f40_atxd_301_tr_at_252d_high_event_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR on bars where close hits 252d-high, over 252d window."""
    tr = _true_range(high, low, close)
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return tr.where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_302_tr_at_252d_low_event_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR on bars where close hits 252d-low, over 252d."""
    tr = _true_range(high, low, close)
    new_low = close <= close.rolling(YDAYS, min_periods=QDAYS).min()
    return tr.where(new_low, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_303_mean_tr_5d_before_252d_high_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR in 5 bars before 252d-high events, over 252d."""
    tr = _true_range(high, low, close)
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    pre_mean = tr.rolling(WDAYS, min_periods=2).mean().shift(1)
    return pre_mean.where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_304_mean_tr_5d_after_252d_high_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR in 5 bars after 252d-high events, over 252d (causal lag)."""
    tr = _true_range(high, low, close)
    new_high_lag = close.shift(WDAYS) >= close.shift(WDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    post_mean = tr.rolling(WDAYS, min_periods=2).mean()
    return post_mean.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_305_atr_change_before_252d_high_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / ATR(21).shift(21) at 252d-high events, mean over 252d."""
    a = _atr(high, low, close, MDAYS)
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    ratio = _safe_div(a, a.shift(MDAYS))
    return ratio.where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_306_atr_change_after_252d_high_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / ATR(21).shift(21) on bars 21d after 252d-high events, mean over 252d."""
    a = _atr(high, low, close, MDAYS)
    new_high_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    ratio = _safe_div(a, a.shift(MDAYS))
    return ratio.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_307_tr_vs_atr_at_252d_high_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR / ATR(21) ratio on bars at 252d-high, mean over 252d."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS)
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(tr, atr).where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_308_high_volume_count_near_252d_high_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of top-decile-volume bars within 5d window of 252d-high events, over 252d."""
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    near_event = new_high.rolling(WDAYS, min_periods=1).max().astype(bool)
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return (near_event & (volume > p90)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_309_natr_at_252d_high_vs_avg_ratio_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(21) at 252d-high event / mean NATR(21) over past 252d, mean over 252d."""
    natr = _safe_div(_atr(high, low, close, MDAYS), close)
    avg_natr = natr.rolling(YDAYS, min_periods=QDAYS).mean()
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(natr, avg_natr).where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_310_atr5_atr252_ratio_at_252d_high_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(5)/ATR(252) at 252d-high events over 252d (term-structure at peak)."""
    ratio = _safe_div(_atr(high, low, close, WDAYS), _atr(high, low, close, YDAYS))
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return ratio.where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_311_bars_since_atr5_top_decile_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since ATR(5) was last in top-decile of trailing 252d distribution."""
    a = _atr(high, low, close, WDAYS)
    p90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return _bars_since((a > p90).astype(float)).diff().diff().diff()

def f40_atxd_312_bars_since_atr63_top_decile_1260d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since ATR(63) was last in top-decile of trailing 1260d distribution."""
    a = _atr(high, low, close, QDAYS)
    p90 = a.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).quantile(0.9).shift(1)
    return _bars_since((a > p90).astype(float)).diff().diff().diff()

def f40_atxd_313_atr_pctrank_crossings_05_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ATR(21)-percentile-rank crossings of 0.5 within trailing 63d."""
    a = _atr(high, low, close, MDAYS)
    rk = a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    above = (rk > 0.5).astype(float)
    return above.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_314_atr_pctrank_rate_of_change_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d change in ATR(21)-percentile-rank (rank velocity)."""
    a = _atr(high, low, close, MDAYS)
    rk = a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    return (rk - rk.shift(MDAYS)).diff().diff().diff()

def f40_atxd_315_short_vs_long_pctrank_divergence_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank(ATR(5), 252d) − pct-rank(ATR(63), 252d) — short-horizon vs long divergence."""
    a5 = _atr(high, low, close, WDAYS)
    a63 = _atr(high, low, close, QDAYS)
    r5 = a5.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    r63 = a63.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    return (r5 - r63).diff().diff().diff()

def f40_atxd_316_atr_pctrank_dispersion_across_horizons_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of ATR-pct-rank across horizons {5, 21, 63, 252} at each bar (cone-position dispersion)."""
    ranks = []
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        a = _atr(high, low, close, n)
        rk = a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
        ranks.append(rk)
    return pd.concat(ranks, axis=1).std(axis=1).diff().diff().diff()

def f40_atxd_317_atr_pctrank_concordance_horizons_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: all ATR-pct-ranks (5,21,63,252) > 0.75 (consensus extreme-high regime)."""
    ranks = []
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        a = _atr(high, low, close, n)
        rk = a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
        ranks.append(rk)
    df = pd.concat(ranks, axis=1)
    return (df > 0.75).all(axis=1).astype(float).diff().diff().diff()

def f40_atxd_318_atr_pctrank_trend_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21d slope of ATR(21)-percentile-rank (rank trend velocity)."""
    a = _atr(high, low, close, MDAYS)
    rk = a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    return _rolling_slope(rk, MDAYS).diff().diff().diff()

def f40_atxd_319_vidya_atr_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VIDYA-style ATR: TR-ema with α scaled by momentum-CMO absolute."""
    tr = _true_range(high, low, close)
    r = close.diff()
    cmo = _safe_div(r.rolling(21, min_periods=WDAYS).sum().abs(), r.abs().rolling(21, min_periods=WDAYS).sum())
    alpha = 2.0 / (MDAYS + 1) * cmo.abs().clip(upper=1.0, lower=0.05)
    out = pd.Series(np.nan, index=close.index)
    val = np.nan
    for i in range(len(tr)):
        if np.isnan(tr.iloc[i]) or np.isnan(alpha.iloc[i]):
            out.iloc[i] = val
            continue
        if np.isnan(val):
            val = tr.iloc[i]
        else:
            val = alpha.iloc[i] * tr.iloc[i] + (1 - alpha.iloc[i]) * val
        out.iloc[i] = val
    return out.diff().diff().diff()

def f40_atxd_320_tma_tr_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Triangular MA of TR over 21d (SMA of SMA)."""
    tr = _true_range(high, low, close)
    n = MDAYS
    sma1 = tr.rolling(n, min_periods=max(n // 3, 2)).mean()
    return sma1.rolling(n, min_periods=max(n // 3, 2)).mean().diff().diff().diff()

def f40_atxd_321_hma_tr_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hull MA of TR over 21d (Alan Hull's HMA)."""
    tr = _true_range(high, low, close)
    n = MDAYS
    h = n // 2
    sqn = int(np.sqrt(n))
    raw = 2 * tr.ewm(span=h, min_periods=h, adjust=False).mean() - tr.ewm(span=n, min_periods=n, adjust=False).mean()
    return raw.ewm(span=sqn, min_periods=sqn, adjust=False).mean().diff().diff().diff()

def f40_atxd_322_t3_tr_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Tilson T3 smoothing of TR over 21d (b=0.7)."""
    tr = _true_range(high, low, close)
    b = 0.7
    n = MDAYS
    e1 = tr.ewm(span=n, min_periods=n, adjust=False).mean()
    e2 = e1.ewm(span=n, min_periods=n, adjust=False).mean()
    e3 = e2.ewm(span=n, min_periods=n, adjust=False).mean()
    e4 = e3.ewm(span=n, min_periods=n, adjust=False).mean()
    e5 = e4.ewm(span=n, min_periods=n, adjust=False).mean()
    e6 = e5.ewm(span=n, min_periods=n, adjust=False).mean()
    c1 = -b ** 3
    c2 = 3 * b ** 2 + 3 * b ** 3
    c3 = -6 * b ** 2 - 3 * b - 3 * b ** 3
    c4 = 1 + 3 * b + 3 * b ** 2 + b ** 3
    return (c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3).diff().diff().diff()

def f40_atxd_323_alma_tr_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ALMA (Arnaud Legoux MA) of TR over 21d: Gaussian-weighted MA with offset 0.85, σ=6."""
    tr = _true_range(high, low, close).values
    n = MDAYS
    offset = 0.85
    sigma = 6.0
    m = offset * (n - 1)
    s = n / sigma
    weights = np.array([np.exp(-(i - m) ** 2 / (2 * s ** 2)) for i in range(n)])
    weights = weights / weights.sum()
    out = np.full(len(tr), np.nan)
    for i in range(n - 1, len(tr)):
        window = tr[i - n + 1:i + 1]
        if np.any(np.isnan(window)):
            continue
        out[i] = float(np.dot(window, weights))
    return pd.Series(out, index=close.index).diff().diff().diff()

def f40_atxd_324_jurik_proxy_tr_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jurik MA proxy: double-smoothed adaptive EMA of TR over 21d."""
    tr = _true_range(high, low, close)
    n = MDAYS
    alpha = 2.0 / (n + 1)
    e1 = tr.ewm(alpha=alpha, min_periods=n, adjust=False).mean()
    e2 = e1.ewm(alpha=alpha, min_periods=n, adjust=False).mean()
    return (e1 + (e1 - e2)).diff().diff().diff()

def f40_atxd_325_nr4_bullish_close_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NR4 + close > open count over 63d."""
    rng = high - low
    nr4 = rng == rng.rolling(4, min_periods=4).min()
    bull = close > close.shift(1)
    return (nr4 & bull).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_326_nr4_bearish_close_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NR4 + close < open count over 63d."""
    rng = high - low
    nr4 = rng == rng.rolling(4, min_periods=4).min()
    bear = close < close.shift(1)
    return (nr4 & bear).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_327_wr7_bullish_close_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WR7 + close > prev_close count over 63d (climactic up-bar)."""
    rng = high - low
    wr7 = rng == rng.rolling(7, min_periods=7).max()
    bull = close > close.shift(1)
    return (wr7 & bull).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_328_wr7_bearish_close_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WR7 + close < prev_close count over 63d (climactic down-bar)."""
    rng = high - low
    wr7 = rng == rng.rolling(7, min_periods=7).max()
    bear = close < close.shift(1)
    return (wr7 & bear).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_329_nr4_followed_by_gap_up_count_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NR4 followed by gap-up (next bar) count over 252d."""
    rng = high - low
    nr4_lag = (rng.shift(1) == rng.rolling(4, min_periods=4).min().shift(1)).fillna(False)
    gap_up = open > close.shift(1) * 1.005
    return (nr4_lag & gap_up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_330_nr4_followed_by_gap_down_count_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NR4 followed by gap-down count over 252d."""
    rng = high - low
    nr4_lag = (rng.shift(1) == rng.rolling(4, min_periods=4).min().shift(1)).fillna(False)
    gap_dn = open < close.shift(1) * 0.995
    return (nr4_lag & gap_dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_331_3_nr_in_row_count_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 3-consecutive-NR7 patterns over 252d (extreme compression)."""
    rng = high - low
    nr7 = rng == rng.rolling(7, min_periods=7).min()
    three_in_row = (nr7 & nr7.shift(1).fillna(False) & nr7.shift(2).fillna(False)).astype(float)
    return three_in_row.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_332_3_wr_in_row_count_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 3-consecutive-WR7 patterns over 252d (extreme expansion)."""
    rng = high - low
    wr7 = rng == rng.rolling(7, min_periods=7).max()
    three_in_row = (wr7 & wr7.shift(1).fillna(False) & wr7.shift(2).fillna(False)).astype(float)
    return three_in_row.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_333_mean_tr_top_vol_decile_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean TR on top-decile-volume bars over 252d (high-conviction range bars)."""
    tr = _true_range(high, low, close)
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return tr.where(volume > p90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_334_mean_tr_bot_vol_decile_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean TR on bottom-decile-volume bars over 252d (low-conviction range bars)."""
    tr = _true_range(high, low, close)
    p10 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.1).shift(1)
    return tr.where(volume < p10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_335_tr_vol_corr_high_vol_regime_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(TR, log(volume)) restricted to bars with σ_21 > 252d-p75 over 252d."""
    tr = _true_range(high, low, close)
    s = (close - close.shift(1)).abs().rolling(MDAYS, min_periods=WDAYS).std()
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    hi = s > p75
    return tr.where(hi, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(volume).where(hi, np.nan)).diff().diff().diff()

def f40_atxd_336_tr_vol_corr_low_vol_regime_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(TR, log(volume)) restricted to bars with σ_21 < 252d-p25 over 252d."""
    tr = _true_range(high, low, close)
    s = (close - close.shift(1)).abs().rolling(MDAYS, min_periods=WDAYS).std()
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    lo = s < p25
    return tr.where(lo, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(volume).where(lo, np.nan)).diff().diff().diff()

def f40_atxd_337_mean_tr_minus_avg_on_high_vol_days_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean (TR − rolling 21d mean TR) on top-decile-volume days, over 252d."""
    tr = _true_range(high, low, close)
    avg_tr = tr.rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return (tr - avg_tr).where(volume > p90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_338_wide_bar_then_inside_count_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR7 followed by inside-bar (range engulfed) count over 252d."""
    rng = high - low
    wr7_lag = (rng.shift(1) == rng.rolling(7, min_periods=7).max().shift(1)).fillna(False)
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return (wr7_lag & inside).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_339_climax_bar_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Climax bar count: WR7 + new 21d-high, over 252d."""
    rng = high - low
    wr7 = rng == rng.rolling(7, min_periods=7).max()
    new_high_21 = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (wr7 & new_high_21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_340_capitulation_bar_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Capitulation bar count: WR7 + new 21d-low, over 252d."""
    rng = high - low
    wr7 = rng == rng.rolling(7, min_periods=7).max()
    new_low_21 = low <= low.rolling(MDAYS, min_periods=WDAYS).min()
    return (wr7 & new_low_21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_341_climax_then_fade_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Climax bar followed by 3 bars all closing below climax close, over 252d."""
    rng = high - low
    wr7 = rng == rng.rolling(7, min_periods=7).max()
    new_high_21 = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    climax_lag3 = (wr7 & new_high_21).shift(3).fillna(False)
    climax_close_lag3 = close.shift(3)
    fade = (close.shift(2) < climax_close_lag3) & (close.shift(1) < climax_close_lag3) & (close < climax_close_lag3)
    return (climax_lag3 & fade).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_342_capitulation_then_bounce_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Capitulation bar followed by 3 bars all closing above capitulation close, over 252d."""
    rng = high - low
    wr7 = rng == rng.rolling(7, min_periods=7).max()
    new_low_21 = low <= low.rolling(MDAYS, min_periods=WDAYS).min()
    capit_lag3 = (wr7 & new_low_21).shift(3).fillna(False)
    capit_close_lag3 = close.shift(3)
    bounce = (close.shift(2) > capit_close_lag3) & (close.shift(1) > capit_close_lag3) & (close > capit_close_lag3)
    return (capit_lag3 & bounce).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_343_three_day_range_volume_expansion_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """3 consecutive bars all with vol_z > 2 AND TR > 2·ATR.shift(1), count over 63d."""
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    flag = (vz > 2.0) & (tr > 2 * atr_lag)
    three_in_row = (flag & flag.shift(1) & flag.shift(2)).astype(float)
    return three_in_row.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_344_range_volume_rocket_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rocket bar: TR > 3·ATR AND vol_z > 3 same day, count over 252d."""
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    return ((tr > 3 * atr_lag) & (vz > 3.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_345_range_volume_flush_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flush bar: TR > 3·ATR AND close in bottom 10% of bar, count over 252d."""
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    pos = _safe_div(close - low, high - low)
    return ((tr > 3 * atr_lag) & (pos <= 0.1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_346_full_expansion_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR(5/21/63/252) all > respective rolling 252d medians (full expansion regime)."""
    aligned = pd.Series(True, index=close.index)
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        a = _atr(high, low, close, n)
        med = a.rolling(YDAYS, min_periods=QDAYS).median()
        aligned = aligned & (a > med)
    return aligned.astype(float).diff().diff().diff()

def f40_atxd_347_full_compression_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR(5/21/63/252) all < respective rolling 252d medians (full compression regime)."""
    aligned = pd.Series(True, index=close.index)
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        a = _atr(high, low, close, n)
        med = a.rolling(YDAYS, min_periods=QDAYS).median()
        aligned = aligned & (a < med)
    return aligned.astype(float).diff().diff().diff()

def f40_atxd_348_atr_cone_uniformity_var_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of ATR-cone-position across horizons {5,21,63,252} at each bar (lower = aligned)."""
    pcts = []
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        a = _atr(high, low, close, n)
        rk = a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
        pcts.append(rk)
    return pd.concat(pcts, axis=1).var(axis=1).diff().diff().diff()

def f40_atxd_349_atr_mad_across_horizons_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean absolute deviation of ATR/close across horizons {5,21,63,252} at each bar."""
    natrs = []
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        natrs.append(_safe_div(_atr(high, low, close, n), close))
    df = pd.concat(natrs, axis=1)
    med = df.median(axis=1)
    return df.sub(med, axis=0).abs().mean(axis=1).diff().diff().diff()

def f40_atxd_350_atr_slope_alignment_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars where all ATR(5/21/63/252) slopes are positive (full-vol-trend-up), summed 63d."""
    aligned = pd.Series(True, index=close.index)
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        a = _atr(high, low, close, n)
        aligned = aligned & (_rolling_slope(a, MDAYS) > 0)
    return aligned.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_351_atr_up_volume_down_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count: 5d ATR change > 0 AND 5d volume change < 0, summed 63d."""
    a = _atr(high, low, close, MDAYS)
    atr_chg = a - a.shift(WDAYS)
    vol_chg = volume.rolling(WDAYS, min_periods=2).mean() - volume.rolling(WDAYS, min_periods=2).mean().shift(WDAYS)
    return ((atr_chg > 0) & (vol_chg < 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_352_atr_down_volume_up_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count: 5d ATR change < 0 AND 5d volume change > 0, summed 63d."""
    a = _atr(high, low, close, MDAYS)
    atr_chg = a - a.shift(WDAYS)
    vol_chg = volume.rolling(WDAYS, min_periods=2).mean() - volume.rolling(WDAYS, min_periods=2).mean().shift(WDAYS)
    return ((atr_chg < 0) & (vol_chg > 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_353_persistent_atr_vol_divergence_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """3+ consecutive days of ATR-volume divergence, count over 63d."""
    a = _atr(high, low, close, MDAYS)
    atr_chg = a - a.shift(WDAYS)
    vol_chg = volume.rolling(WDAYS, min_periods=2).mean() - volume.rolling(WDAYS, min_periods=2).mean().shift(WDAYS)
    div = (atr_chg > 0) & (vol_chg < 0) | (atr_chg < 0) & (vol_chg > 0)
    three_in_row = (div & div.shift(1) & div.shift(2)).astype(float)
    return three_in_row.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f40_atxd_354_atr_vol_divergence_after_252d_high_count_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ATR-up-volume-down divergence within 21d after 252d-high events, count over 252d."""
    a = _atr(high, low, close, MDAYS)
    atr_chg = a - a.shift(WDAYS)
    vol_chg = volume.rolling(WDAYS, min_periods=2).mean() - volume.rolling(WDAYS, min_periods=2).mean().shift(WDAYS)
    div = (atr_chg > 0) & (vol_chg < 0)
    new_high_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    return (div & new_high_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_355_inside_bar_pct_21d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of inside-bars over 21d."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return inside.astype(float).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f40_atxd_356_outside_bar_pct_21d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of outside-bars over 21d."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    return outside.astype(float).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f40_atxd_357_inside_bar_streak_max_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive inside-bar streak over 63d."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float).fillna(0.0)

    def _run(w):
        m = 0
        c = 0
        for v in w:
            if v > 0.5:
                c += 1
                m = c if c > m else m
            else:
                c = 0
        return float(m)
    return inside.rolling(QDAYS, min_periods=MDAYS).apply(_run, raw=True).diff().diff().diff()

def f40_atxd_358_outside_bar_streak_max_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive outside-bar streak over 63d."""
    outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float).fillna(0.0)

    def _run(w):
        m = 0
        c = 0
        for v in w:
            if v > 0.5:
                c += 1
                m = c if c > m else m
            else:
                c = 0
        return float(m)
    return outside.rolling(QDAYS, min_periods=MDAYS).apply(_run, raw=True).diff().diff().diff()

def f40_atxd_359_inside_after_outside_count_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside-bar immediately after outside-bar count over 252d (compression after expansion)."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    outside_prev = ((high.shift(1) > high.shift(2)) & (low.shift(1) < low.shift(2))).fillna(False)
    return (inside & outside_prev).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_360_tr_cv_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CV of TR over 21d."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.rolling(MDAYS, min_periods=WDAYS).std(), tr.rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff().diff()

def f40_atxd_361_tr_mad_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median absolute deviation of TR over 21d."""
    tr = _true_range(high, low, close)
    med = tr.rolling(MDAYS, min_periods=WDAYS).median()
    return (tr - med).abs().rolling(MDAYS, min_periods=WDAYS).median().diff().diff().diff()

def f40_atxd_362_tr_stability_score_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 − CV(TR) over 63d (higher = more stable range process)."""
    tr = _true_range(high, low, close)
    return (1.0 - _safe_div(tr.rolling(QDAYS, min_periods=MDAYS).std(), tr.rolling(QDAYS, min_periods=MDAYS).mean())).diff().diff().diff()

def f40_atxd_363_tr_mad_around_252d_mean_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |TR − 252d-mean(TR)| over 252d."""
    tr = _true_range(high, low, close)
    mean252 = tr.rolling(YDAYS, min_periods=QDAYS).mean()
    return (tr - mean252).abs().rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_364_tr_range_max_minus_min_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max TR − min TR over 63d (range of single-bar ranges)."""
    tr = _true_range(high, low, close)
    return (tr.rolling(QDAYS, min_periods=MDAYS).max() - tr.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff().diff()

def f40_atxd_365_tr_fractal_dim_box_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Box-counting fractal dimension of TR series over 252d (simple grid-based)."""
    tr = _true_range(high, low, close)

    def _bc(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        norm = (ww - ww.min()) / (ww.max() - ww.min() + 1e-12)
        scales = [4, 8, 16, 32]
        counts = []
        for s in scales:
            n_boxes = max(n // s, 2)
            boxes = set()
            for i in range(n):
                box_x = i // s
                box_y = int(norm[i] * (n_boxes - 1))
                boxes.add((box_x, box_y))
            counts.append(len(boxes))
        lx = np.log(scales)
        ly = np.log(counts)
        xm = lx.mean()
        ym = ly.mean()
        d = ((lx - xm) ** 2).sum()
        return float(-((lx - xm) * (ly - ym)).sum() / d) if d > 0 else np.nan
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_bc, raw=True).diff().diff().diff()

def f40_atxd_366_tr_change_point_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR-EWMA(21d) crosses TR-EWMA(63d) over 252d — simple change-point proxy."""
    tr = _true_range(high, low, close)
    ema21 = tr.ewm(span=MDAYS, min_periods=MDAYS, adjust=False).mean()
    ema63 = tr.ewm(span=QDAYS, min_periods=QDAYS, adjust=False).mean()
    above = (ema21 > ema63).astype(float)
    return above.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_367_tr_5day_seasonality_corr_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(TR, TR.shift(5)) over 252d — 5-day periodicity in range process."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(WDAYS)).diff().diff().diff()

def f40_atxd_368_tr_autocorr_lag21_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(TR, TR.shift(21)) over 252d — monthly-lag TR persistence."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(MDAYS)).diff().diff().diff()

def f40_atxd_369_vol_of_atr21_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of ATR(21) over 252d — vol-of-ATR."""
    return _atr(high, low, close, MDAYS).rolling(YDAYS, min_periods=QDAYS).std().diff().diff().diff()

def f40_atxd_370_skew_atr21_504d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of ATR(21) over 504d distribution."""
    return _atr(high, low, close, MDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).skew().diff().diff().diff()

def f40_atxd_371_kurt_atr21_504d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kurt of ATR(21) over 504d distribution."""
    return _atr(high, low, close, MDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).kurt().diff().diff().diff()

def f40_atxd_372_atr21_outlier_z_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(21) z-score > 3 within 252d window."""
    a = _atr(high, low, close, MDAYS)
    z = _rolling_zscore(a, YDAYS)
    return (z.abs() > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_373_atr21_breakout_above_5d_max_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR(21) > rolling 5d max of ATR(21) (excluding today via shift)."""
    a = _atr(high, low, close, MDAYS)
    return (a > a.shift(1).rolling(WDAYS, min_periods=2).max()).astype(float).diff().diff().diff()

def f40_atxd_374_atr21_breakdown_below_5d_min_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR(21) < rolling 5d min of ATR(21) (excluding today)."""
    a = _atr(high, low, close, MDAYS)
    return (a < a.shift(1).rolling(WDAYS, min_periods=2).min()).astype(float).diff().diff().diff()

def f40_atxd_375_atr21_in_middle_consolidation_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(21) is in [p40, p60] of trailing 63d distribution (consolidation)."""
    a = _atr(high, low, close, MDAYS)
    p40 = a.rolling(QDAYS, min_periods=MDAYS).quantile(0.4)
    p60 = a.rolling(QDAYS, min_periods=MDAYS).quantile(0.6)
    return ((a >= p40) & (a <= p60)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()
ATR_EXPANSION_DYNAMICS_D3_REGISTRY_301_375 = {'f40_atxd_301_tr_at_252d_high_event_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_301_tr_at_252d_high_event_252d_d3}, 'f40_atxd_302_tr_at_252d_low_event_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_302_tr_at_252d_low_event_252d_d3}, 'f40_atxd_303_mean_tr_5d_before_252d_high_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_303_mean_tr_5d_before_252d_high_d3}, 'f40_atxd_304_mean_tr_5d_after_252d_high_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_304_mean_tr_5d_after_252d_high_d3}, 'f40_atxd_305_atr_change_before_252d_high_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_305_atr_change_before_252d_high_252d_d3}, 'f40_atxd_306_atr_change_after_252d_high_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_306_atr_change_after_252d_high_252d_d3}, 'f40_atxd_307_tr_vs_atr_at_252d_high_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_307_tr_vs_atr_at_252d_high_252d_d3}, 'f40_atxd_308_high_volume_count_near_252d_high_252d_d3': {'inputs': ['close', 'volume'], 'func': f40_atxd_308_high_volume_count_near_252d_high_252d_d3}, 'f40_atxd_309_natr_at_252d_high_vs_avg_ratio_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_309_natr_at_252d_high_vs_avg_ratio_252d_d3}, 'f40_atxd_310_atr5_atr252_ratio_at_252d_high_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_310_atr5_atr252_ratio_at_252d_high_252d_d3}, 'f40_atxd_311_bars_since_atr5_top_decile_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_311_bars_since_atr5_top_decile_252d_d3}, 'f40_atxd_312_bars_since_atr63_top_decile_1260d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_312_bars_since_atr63_top_decile_1260d_d3}, 'f40_atxd_313_atr_pctrank_crossings_05_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_313_atr_pctrank_crossings_05_63d_d3}, 'f40_atxd_314_atr_pctrank_rate_of_change_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_314_atr_pctrank_rate_of_change_21d_d3}, 'f40_atxd_315_short_vs_long_pctrank_divergence_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_315_short_vs_long_pctrank_divergence_d3}, 'f40_atxd_316_atr_pctrank_dispersion_across_horizons_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_316_atr_pctrank_dispersion_across_horizons_d3}, 'f40_atxd_317_atr_pctrank_concordance_horizons_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_317_atr_pctrank_concordance_horizons_d3}, 'f40_atxd_318_atr_pctrank_trend_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_318_atr_pctrank_trend_21d_d3}, 'f40_atxd_319_vidya_atr_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_319_vidya_atr_21d_d3}, 'f40_atxd_320_tma_tr_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_320_tma_tr_21d_d3}, 'f40_atxd_321_hma_tr_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_321_hma_tr_21d_d3}, 'f40_atxd_322_t3_tr_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_322_t3_tr_21d_d3}, 'f40_atxd_323_alma_tr_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_323_alma_tr_21d_d3}, 'f40_atxd_324_jurik_proxy_tr_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_324_jurik_proxy_tr_21d_d3}, 'f40_atxd_325_nr4_bullish_close_count_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_325_nr4_bullish_close_count_63d_d3}, 'f40_atxd_326_nr4_bearish_close_count_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_326_nr4_bearish_close_count_63d_d3}, 'f40_atxd_327_wr7_bullish_close_count_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_327_wr7_bullish_close_count_63d_d3}, 'f40_atxd_328_wr7_bearish_close_count_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_328_wr7_bearish_close_count_63d_d3}, 'f40_atxd_329_nr4_followed_by_gap_up_count_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f40_atxd_329_nr4_followed_by_gap_up_count_252d_d3}, 'f40_atxd_330_nr4_followed_by_gap_down_count_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f40_atxd_330_nr4_followed_by_gap_down_count_252d_d3}, 'f40_atxd_331_3_nr_in_row_count_252d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_331_3_nr_in_row_count_252d_d3}, 'f40_atxd_332_3_wr_in_row_count_252d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_332_3_wr_in_row_count_252d_d3}, 'f40_atxd_333_mean_tr_top_vol_decile_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_333_mean_tr_top_vol_decile_252d_d3}, 'f40_atxd_334_mean_tr_bot_vol_decile_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_334_mean_tr_bot_vol_decile_252d_d3}, 'f40_atxd_335_tr_vol_corr_high_vol_regime_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_335_tr_vol_corr_high_vol_regime_252d_d3}, 'f40_atxd_336_tr_vol_corr_low_vol_regime_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_336_tr_vol_corr_low_vol_regime_252d_d3}, 'f40_atxd_337_mean_tr_minus_avg_on_high_vol_days_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_337_mean_tr_minus_avg_on_high_vol_days_252d_d3}, 'f40_atxd_338_wide_bar_then_inside_count_252d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_338_wide_bar_then_inside_count_252d_d3}, 'f40_atxd_339_climax_bar_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_339_climax_bar_count_252d_d3}, 'f40_atxd_340_capitulation_bar_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_340_capitulation_bar_count_252d_d3}, 'f40_atxd_341_climax_then_fade_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_341_climax_then_fade_count_252d_d3}, 'f40_atxd_342_capitulation_then_bounce_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_342_capitulation_then_bounce_count_252d_d3}, 'f40_atxd_343_three_day_range_volume_expansion_63d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_343_three_day_range_volume_expansion_63d_d3}, 'f40_atxd_344_range_volume_rocket_count_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_344_range_volume_rocket_count_252d_d3}, 'f40_atxd_345_range_volume_flush_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_345_range_volume_flush_count_252d_d3}, 'f40_atxd_346_full_expansion_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_346_full_expansion_indicator_d3}, 'f40_atxd_347_full_compression_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_347_full_compression_indicator_d3}, 'f40_atxd_348_atr_cone_uniformity_var_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_348_atr_cone_uniformity_var_d3}, 'f40_atxd_349_atr_mad_across_horizons_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_349_atr_mad_across_horizons_d3}, 'f40_atxd_350_atr_slope_alignment_count_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_350_atr_slope_alignment_count_63d_d3}, 'f40_atxd_351_atr_up_volume_down_count_63d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_351_atr_up_volume_down_count_63d_d3}, 'f40_atxd_352_atr_down_volume_up_count_63d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_352_atr_down_volume_up_count_63d_d3}, 'f40_atxd_353_persistent_atr_vol_divergence_63d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_353_persistent_atr_vol_divergence_63d_d3}, 'f40_atxd_354_atr_vol_divergence_after_252d_high_count_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_354_atr_vol_divergence_after_252d_high_count_d3}, 'f40_atxd_355_inside_bar_pct_21d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_355_inside_bar_pct_21d_d3}, 'f40_atxd_356_outside_bar_pct_21d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_356_outside_bar_pct_21d_d3}, 'f40_atxd_357_inside_bar_streak_max_63d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_357_inside_bar_streak_max_63d_d3}, 'f40_atxd_358_outside_bar_streak_max_63d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_358_outside_bar_streak_max_63d_d3}, 'f40_atxd_359_inside_after_outside_count_252d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_359_inside_after_outside_count_252d_d3}, 'f40_atxd_360_tr_cv_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_360_tr_cv_21d_d3}, 'f40_atxd_361_tr_mad_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_361_tr_mad_21d_d3}, 'f40_atxd_362_tr_stability_score_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_362_tr_stability_score_63d_d3}, 'f40_atxd_363_tr_mad_around_252d_mean_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_363_tr_mad_around_252d_mean_d3}, 'f40_atxd_364_tr_range_max_minus_min_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_364_tr_range_max_minus_min_63d_d3}, 'f40_atxd_365_tr_fractal_dim_box_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_365_tr_fractal_dim_box_count_252d_d3}, 'f40_atxd_366_tr_change_point_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_366_tr_change_point_count_252d_d3}, 'f40_atxd_367_tr_5day_seasonality_corr_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_367_tr_5day_seasonality_corr_252d_d3}, 'f40_atxd_368_tr_autocorr_lag21_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_368_tr_autocorr_lag21_252d_d3}, 'f40_atxd_369_vol_of_atr21_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_369_vol_of_atr21_252d_d3}, 'f40_atxd_370_skew_atr21_504d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_370_skew_atr21_504d_d3}, 'f40_atxd_371_kurt_atr21_504d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_371_kurt_atr21_504d_d3}, 'f40_atxd_372_atr21_outlier_z_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_372_atr21_outlier_z_count_252d_d3}, 'f40_atxd_373_atr21_breakout_above_5d_max_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_373_atr21_breakout_above_5d_max_d3}, 'f40_atxd_374_atr21_breakdown_below_5d_min_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_374_atr21_breakdown_below_5d_min_d3}, 'f40_atxd_375_atr21_in_middle_consolidation_count_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_375_atr21_in_middle_consolidation_count_63d_d3}}