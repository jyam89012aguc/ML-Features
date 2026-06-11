"""38_jump_detection_signature d3 features 301-375 — order-3 difference of corresponding base features.

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

def _log_ret(close):
    return _safe_log(close).diff()

def _sigma_prior(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std().shift(1)

def _bars_since(ind: pd.Series) -> pd.Series:
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

def f38_jpdt_301_jump_count_when_top5_of_252d_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Jump count restricted to bars where close is in top 5% of trailing 252d range."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    in_top5 = pos >= 0.95
    return (jump & in_top5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_302_jump_count_when_top10_of_252d_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Jump count restricted to bars where close is in top 10% of trailing 252d range."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    return (jump & (pos >= 0.9)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_303_mean_abs_r_near_252d_high_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean |log-ret| restricted to bars within 5% of 252d-high, over 252d window."""
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = close >= 0.95 * h252
    sel = _log_ret(close).abs().where(near, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f38_jpdt_304_neg_jump_count_near_252d_high_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Negative-jump count restricted to bars within 5% of 252d-high — distribution signature."""
    r = _log_ret(close)
    neg_jump = r < -3 * _sigma_prior(r, MDAYS)
    near = close >= 0.95 * high.rolling(YDAYS, min_periods=QDAYS).max()
    return (neg_jump & near).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_305_jump_asymmetry_in_top_decile_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Up-jump minus down-jump counts within top-decile-of-range bars over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    top = pos >= 0.9
    up = ((r > 3 * sig) & top).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = ((r < -3 * sig) & top).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (up - dn).diff().diff().diff()

def f38_jpdt_306_bars_since_first_jump_near_peak_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since first 3σ_21d jump within 5% of 252d-high in trailing 252d window."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    near = close >= 0.95 * high.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since((jump & near).astype(float)).diff().diff().diff()

def f38_jpdt_307_max_neg_r_within_21d_after_252d_high_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Max negative log-ret in 21 bars after a 252d-high event, over 252d (causal: shift first)."""
    r = _log_ret(close)
    h252_lag = high.rolling(YDAYS, min_periods=QDAYS).max().shift(MDAYS)
    was_at_high = high.shift(MDAYS) >= h252_lag * 0.999
    sel = r.where(was_at_high, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).min().diff().diff().diff()

def f38_jpdt_308_sum_abs_r_within_5d_of_252d_high_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Sum of |log-ret| on bars within 5 days of a 252d-high event, over 252d."""
    high_event = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    near_event = high_event.rolling(WDAYS, min_periods=1).max().astype(bool)
    sel = _log_ret(close).abs().where(near_event, 0.0)
    return sel.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_309_jump_count_in_21d_after_252d_high_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Jump count in 21 bars following a 252d-high event, over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    high_event_lag = high.shift(MDAYS) >= high.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    near_event_post = high_event_lag.rolling(MDAYS, min_periods=1).max().astype(bool)
    return (jump & near_event_post).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_310_post_peak_jump_intensity_ratio_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Ratio: jump-intensity in 21d after 252d-high event vs in 252d window — post-peak surge ratio."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    high_event_lag = high.shift(MDAYS) >= high.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    near_event_post = high_event_lag.rolling(MDAYS, min_periods=1).max().astype(bool)
    post_count = jump.where(near_event_post, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    total_count = jump.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(post_count, total_count).diff().diff().diff()

def f38_jpdt_311_jump_count_high_vol_regime_252d_d3(close: pd.Series) -> pd.Series:
    """Jump count restricted to high-vol regime (σ_21 > 252d p75) over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (jump & (s > p75)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_312_jump_count_low_vol_regime_252d_d3(close: pd.Series) -> pd.Series:
    """Jump count restricted to low-vol regime (σ_21 < 252d p25) over 252d — surprise jumps."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (jump & (s < p25)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_313_mean_abs_r_jump_high_vol_252d_d3(close: pd.Series) -> pd.Series:
    """Mean |r| on jump days in high-vol regime (σ_21 > 252d p75) over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    sel = r.abs().where(jump & (s > p75), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f38_jpdt_314_mean_abs_r_jump_low_vol_252d_d3(close: pd.Series) -> pd.Series:
    """Mean |r| on jump days in low-vol regime (σ_21 < 252d p25) over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    sel = r.abs().where(jump & (s < p25), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f38_jpdt_315_ratio_high_vs_low_vol_jumps_252d_d3(close: pd.Series) -> pd.Series:
    """Ratio: high-vol-regime jump count / low-vol-regime jump count over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    hi = (jump & (s > p75)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    lo = (jump & (s < p25)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(hi, lo).diff().diff().diff()

def f38_jpdt_316_mean_sigma_rank_at_jump_252d_d3(close: pd.Series) -> pd.Series:
    """Mean σ_21 percentile rank (in 252d) on jump days, mean over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    rk = s.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    return rk.where(jump, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f38_jpdt_317_jump_then_vol_spike_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of bars where jump on day t AND σ_21 enters top quartile within next 5 days, over 252d (causal lag)."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    p75 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    jump_lag = (r.abs() > 3 * _sigma_prior(r, MDAYS)).shift(WDAYS).fillna(False)
    vol_spike_now = sig > p75
    return (jump_lag & vol_spike_now).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_318_jump_then_vol_collapse_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count: jump on day t-5 AND σ_21 now in bottom quartile, over 252d (post-jump vol collapse)."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    p25 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    jump_lag = (r.abs() > 3 * _sigma_prior(r, MDAYS)).shift(WDAYS).fillna(False)
    vol_low_now = sig < p25
    return (jump_lag & vol_low_now).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_319_jump_count_top_decile_volume_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Jump count restricted to top-decile-volume bars (vs trailing 252d) over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return (jump & (volume > p90)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_320_jump_count_bottom_decile_volume_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Jump count restricted to bottom-decile-volume bars over 252d — silent-shock count."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    p10 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.1).shift(1)
    return (jump & (volume < p10)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_321_ratio_high_low_volume_jumps_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio high-volume-jumps / low-volume-jumps over 252d (volume-conviction asymmetry)."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    p10 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.1).shift(1)
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    hi = (jump & (volume > p90)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    lo = (jump & (volume < p10)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(hi, lo).diff().diff().diff()

def f38_jpdt_322_mean_volume_neg_jump_days_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on negative-jump days (r < -3σ_21d) over 252d."""
    r = _log_ret(close)
    neg = r < -3 * _sigma_prior(r, MDAYS)
    return volume.where(neg, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f38_jpdt_323_mean_volume_pos_jump_days_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on positive-jump days (r > +3σ_21d) over 252d."""
    r = _log_ret(close)
    pos = r > 3 * _sigma_prior(r, MDAYS)
    return volume.where(pos, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f38_jpdt_324_gap_and_go_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-and-go: open above prev close AND close in top quintile of bar's range (single-bar flag)."""
    gap_up = open > close.shift(1) * 1.005
    pos = _safe_div(close - low, high - low)
    return (gap_up & (pos >= 0.8)).astype(float).diff().diff().diff()

def f38_jpdt_325_gap_and_fade_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-and-fade: open above prev close AND close in bottom quintile of bar's range (single-bar flag)."""
    gap_up = open > close.shift(1) * 1.005
    pos = _safe_div(close - low, high - low)
    return (gap_up & (pos <= 0.2)).astype(float).diff().diff().diff()

def f38_jpdt_326_gap_and_go_count_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-and-go count over 63d."""
    gap_up = open > close.shift(1) * 1.005
    pos = _safe_div(close - low, high - low)
    return (gap_up & (pos >= 0.8)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f38_jpdt_327_gap_and_fade_count_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-and-fade count over 63d (gap-up that fades is bearish climax signal)."""
    gap_up = open > close.shift(1) * 1.005
    pos = _safe_div(close - low, high - low)
    return (gap_up & (pos <= 0.2)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f38_jpdt_328_reversal_bar_count_252d_d3(close: pd.Series) -> pd.Series:
    """Reversal-bar count: large body but opposite sign of prior 3-bar trend, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    big_body = r.abs() > 2 * sig
    prior_trend = np.sign(r.shift(1) + r.shift(2) + r.shift(3))
    opposite = np.sign(r) != prior_trend
    return (big_body & opposite).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_329_outside_day_count_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Outside-day count: today's range engulfs prior day's range entirely, over 252d."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    return outside.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_330_inside_after_big_range_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inside-bar after a big-range bar (TR > 2·ATR21_prior) count over 252d."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    big = (_true_range(high, low, close) > 2 * _atr(high, low, close, MDAYS).shift(1)).shift(1).fillna(False)
    return (inside & big).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_331_two_bar_reversal_count_252d_d3(close: pd.Series) -> pd.Series:
    """Two-bar reversal: bar t has |r|>σ AND prior 2-bar net move opposite-sign exceeding it, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    big = r.abs() > sig
    prior2 = r.shift(1) + r.shift(2)
    opposite = (np.sign(r) != np.sign(prior2)) & (r.abs() > prior2.abs())
    return (big & opposite).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_332_failure_pattern_count_252d_d3(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Failure pattern: new 21d-high + close < open within 252d."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    bearish = close < open
    return (new_high & bearish).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_333_failure_at_252d_high_count_252d_d3(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Failure at 252d-high: bar within 1% of 252d-high AND closes below open, over 252d."""
    at_high = high >= 0.99 * high.rolling(YDAYS, min_periods=QDAYS).max()
    bearish = close < open
    return (at_high & bearish).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_334_distribution_day_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution day count: close down AND volume in top quartile AND TR > median TR, over 252d."""
    pv75 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    tr = _true_range(high, low, close)
    med_tr = tr.rolling(YDAYS, min_periods=QDAYS).median().shift(1)
    dn = close < close.shift(1)
    return (dn & (volume > pv75) & (tr > med_tr)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_335_ad_divergence_signal_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acc/Dist line divergence: corr between OBV slope and close slope (negative = bearish divergence) over 252d."""
    r = _log_ret(close)
    obv = (np.sign(r) * volume).cumsum()
    obv_slope = _rolling_slope(obv, MDAYS)
    close_slope = _rolling_slope(close, MDAYS)
    return obv_slope.rolling(YDAYS, min_periods=QDAYS).corr(close_slope).diff().diff().diff()

def f38_jpdt_336_bars_since_last_gap_up_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last >1% gap-up event."""
    return _bars_since((open > close.shift(1) * 1.01).astype(float)).diff().diff().diff()

def f38_jpdt_337_bars_since_last_gap_down_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last >1% gap-down event."""
    return _bars_since((open < close.shift(1) * 0.99).astype(float)).diff().diff().diff()

def f38_jpdt_338_bars_since_last_nr4_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since last NR4 (today's range narrowest of last 4)."""
    rng = high - low
    nr4 = (rng == rng.rolling(4, min_periods=4).min()).astype(float)
    return _bars_since(nr4).diff().diff().diff()

def f38_jpdt_339_bars_since_last_wr7_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since last WR7 (today's range widest of last 7) — climax recency."""
    rng = high - low
    wr7 = (rng == rng.rolling(7, min_periods=7).max()).astype(float)
    return _bars_since(wr7).diff().diff().diff()

def f38_jpdt_340_bars_since_close_near_bar_low_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since close was in bottom 10% of bar's range."""
    pos = _safe_div(close - low, high - low)
    return _bars_since((pos <= 0.1).astype(float)).diff().diff().diff()

def f38_jpdt_341_bars_since_252d_high_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since close last hit its 252d-high."""
    return _bars_since((close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.999).astype(float)).diff().diff().diff()

def f38_jpdt_342_bars_since_large_range_bar_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last large-range bar (TR > 2·ATR_21d_prior)."""
    tr = _true_range(high, low, close)
    atr_prior = _atr(high, low, close, MDAYS).shift(1)
    return _bars_since((tr > 2 * atr_prior).astype(float)).diff().diff().diff()

def f38_jpdt_343_bars_since_alltime_high_d3(close: pd.Series) -> pd.Series:
    """Bars since close last printed its all-time-high (expanding max)."""
    expanding_max = close.expanding(min_periods=1).max()
    return _bars_since((close >= expanding_max * 0.999).astype(float)).diff().diff().diff()

def f38_jpdt_344_cum_thrust_21d_d3(close: pd.Series) -> pd.Series:
    """Sum of positive log-returns over 21d (cumulative thrust)."""
    r = _log_ret(close)
    return r.where(r > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f38_jpdt_345_cum_pullback_21d_d3(close: pd.Series) -> pd.Series:
    """Sum of negative log-returns over 21d (cumulative pullback magnitude, negative)."""
    r = _log_ret(close)
    return r.where(r < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f38_jpdt_346_up_down_day_ratio_21d_d3(close: pd.Series) -> pd.Series:
    """Up-day count / down-day count over 21d."""
    r = _log_ret(close)
    up = (r > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = (r < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(up, dn).diff().diff().diff()

def f38_jpdt_347_max_pullback_63d_d3(close: pd.Series) -> pd.Series:
    """Max drawdown depth within trailing 63d window."""

    def _dd(w):
        ww = w[~np.isnan(w)]
        if len(ww) < WDAYS:
            return np.nan
        peak = np.maximum.accumulate(ww)
        return float(np.max(1.0 - ww / peak))
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_dd, raw=True).diff().diff().diff()

def f38_jpdt_348_pullback_to_thrust_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """|cum-pullback| / cum-thrust over 252d — bearish pressure share."""
    r = _log_ret(close)
    up = r.where(r > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = r.where(r < 0, 0.0).abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(dn, up).diff().diff().diff()

def f38_jpdt_349_counter_trend_bar_count_21d_d3(close: pd.Series) -> pd.Series:
    """Counter-trend bar count: r-sign opposite of 21d-trend, in last 21d."""
    r = _log_ret(close)
    trend = np.sign(close - close.shift(MDAYS))
    counter = (np.sign(r) != trend) & (np.sign(r) != 0)
    return counter.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f38_jpdt_350_with_trend_bar_count_21d_d3(close: pd.Series) -> pd.Series:
    """With-trend bar count: r-sign matches 21d-trend, in last 21d."""
    r = _log_ret(close)
    trend = np.sign(close - close.shift(MDAYS))
    with_trend = (np.sign(r) == trend) & (np.sign(r) != 0)
    return with_trend.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f38_jpdt_351_efficiency_ratio_signed_21d_d3(close: pd.Series) -> pd.Series:
    """Net Σ r over 21d / Σ |r| over 21d — Kaufman ER-on-returns (-1..+1)."""
    r = _log_ret(close)
    return _safe_div(r.rolling(MDAYS, min_periods=WDAYS).sum(), r.abs().rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff().diff()

def f38_jpdt_352_signed_momentum_1bar_d3(close: pd.Series) -> pd.Series:
    """Sign-weighted 1-bar momentum: |r|·sign(r) = r itself but explicit naming for ML."""
    return _log_ret(close).diff().diff().diff()

def f38_jpdt_353_log_return_5d_d3(close: pd.Series) -> pd.Series:
    """5-bar trailing log-return."""
    return (_safe_log(close) - _safe_log(close.shift(WDAYS))).diff().diff().diff()

def f38_jpdt_354_log_return_10d_d3(close: pd.Series) -> pd.Series:
    """10-bar trailing log-return."""
    return (_safe_log(close) - _safe_log(close.shift(10))).diff().diff().diff()

def f38_jpdt_355_ratio_5d_21d_logret_d3(close: pd.Series) -> pd.Series:
    """Ratio 5d log-return / 21d log-return — short-vs-medium momentum alignment."""
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    return _safe_div(r5, r21).diff().diff().diff()

def f38_jpdt_356_momentum_mismatch_5_21_d3(close: pd.Series) -> pd.Series:
    """Sign(5d r) - sign(21d r) ∈ {-2,0,+2} — momentum-mismatch flag."""
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    return (np.sign(r5) - np.sign(r21)).diff().diff().diff()

def f38_jpdt_357_ret_per_unit_sigma_5d_d3(close: pd.Series) -> pd.Series:
    """5d log-return / 5d std of daily returns — return per unit of volatility (5d Sharpe)."""
    r = _log_ret(close)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    s5 = r.rolling(WDAYS, min_periods=2).std()
    return _safe_div(r5, s5 * np.sqrt(WDAYS)).diff().diff().diff()

def f38_jpdt_358_bull_trap_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bull-trap count: new 21d-high + close in lower quartile of bar's range, over 252d."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    pos = _safe_div(close - low, high - low)
    return (new_high & (pos < 0.25)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_359_bear_trap_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bear-trap count: new 21d-low + close in upper quartile, over 252d."""
    new_low = low <= low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - low, high - low)
    return (new_low & (pos > 0.75)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_360_failed_breakout_count_252d_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Failed-breakout: bar's high > 21d-high but close <= 21d-high, over 252d."""
    h21_prior = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    pierce = high > h21_prior
    rejected = close <= h21_prior
    return (pierce & rejected).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_361_failed_breakdown_count_252d_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Failed-breakdown: bar's low < 21d-low but close >= 21d-low, over 252d."""
    l21_prior = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    pierce = low < l21_prior
    rejected = close >= l21_prior
    return (pierce & rejected).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_362_exhaustion_gap_count_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Exhaustion gap: gap-up + close in bottom 30% of bar + range in top decile of 252d, over 252d."""
    gap_up = open > close.shift(1) * 1.005
    pos = _safe_div(close - low, high - low)
    rng = high - low
    big_range = rng > rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return (gap_up & (pos < 0.3) & big_range).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_363_breakaway_gap_count_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Breakaway gap: gap-up + close in top 30% of bar + new 21d-high + range top decile, over 252d."""
    gap_up = open > close.shift(1) * 1.005
    pos = _safe_div(close - low, high - low)
    new_21d_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    rng = high - low
    big_range = rng > rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return (gap_up & (pos > 0.7) & new_21d_high & big_range).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_364_three_bar_consolidation_count_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """3-bar consolidation: all 3 bars overlap each other (range intersect non-empty for all), over 252d."""
    h1 = high
    l1 = low
    h2 = high.shift(1)
    l2 = low.shift(1)
    h3 = high.shift(2)
    l3 = low.shift(2)
    overlap12 = pd.concat([h1, h2], axis=1).min(axis=1) > pd.concat([l1, l2], axis=1).max(axis=1)
    overlap13 = pd.concat([h1, h3], axis=1).min(axis=1) > pd.concat([l1, l3], axis=1).max(axis=1)
    overlap23 = pd.concat([h2, h3], axis=1).min(axis=1) > pd.concat([l2, l3], axis=1).max(axis=1)
    return (overlap12 & overlap13 & overlap23).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_365_three_bar_trend_count_252d_d3(close: pd.Series) -> pd.Series:
    """3-bar trend count: 3 consecutive bars all same sign, over 252d."""
    r = _log_ret(close)
    up3 = (r > 0) & (r.shift(1) > 0) & (r.shift(2) > 0)
    dn3 = (r < 0) & (r.shift(1) < 0) & (r.shift(2) < 0)
    return (up3 | dn3).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f38_jpdt_366_vol_thrust_price_thrust_count_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-thrust + price-thrust co-event: vol_z>2 AND |r|>σ_21_prior, summed 63d."""
    r = _log_ret(close)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    return ((vz > 2.0) & (r.abs() > _sigma_prior(r, MDAYS))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f38_jpdt_367_volume_divergence_count_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-divergence: vol_z>2 but |r|<0.5·σ_21_prior, summed 63d (decoupled vol)."""
    r = _log_ret(close)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    return ((vz > 2.0) & (r.abs() < 0.5 * _sigma_prior(r, MDAYS))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f38_jpdt_368_volume_drying_count_63d_d3(volume: pd.Series) -> pd.Series:
    """Volume-drying days: 5d-mean-volume < 50% of 252d-mean-volume, summed 63d."""
    short = volume.rolling(WDAYS, min_periods=2).mean()
    long_ = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (short < 0.5 * long_).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f38_jpdt_369_volume_explosion_count_63d_d3(volume: pd.Series) -> pd.Series:
    """Volume-explosion days: 5d-mean-volume > 2x 252d-mean-volume, summed 63d."""
    short = volume.rolling(WDAYS, min_periods=2).mean()
    long_ = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (short > 2.0 * long_).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f38_jpdt_370_sustained_volume_run_252d_d3(volume: pd.Series) -> pd.Series:
    """Longest consecutive run of vol_z > 1 within 252d window."""
    vz = _rolling_zscore(volume, QDAYS)
    hi = (vz > 1.0).astype(float).fillna(0.0)

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
    return hi.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True).diff().diff().diff()

def f38_jpdt_371_jvar_over_bv_21d_d3(close: pd.Series) -> pd.Series:
    """Jump variation (max(0, RV-BV)) / bipower variation at 21d — jump-to-continuous-variance ratio."""
    r = _log_ret(close)
    rv = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    pr = r.abs() * r.abs().shift(1)
    bv = np.pi / 2.0 * pr.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div((rv - bv).clip(lower=0.0), bv).diff().diff().diff()

def f38_jpdt_372_truncated_return_indicator_d3(close: pd.Series) -> pd.Series:
    """Truncated return: r when |r| < 2·σ_21_prior, else 0 (continuous component)."""
    r = _log_ret(close)
    return r.where(r.abs() < 2 * _sigma_prior(r, MDAYS), 0.0).diff().diff().diff()

def f38_jpdt_373_sum_truncated_returns_21d_d3(close: pd.Series) -> pd.Series:
    """Σ of |r| restricted to |r|<2σ_21_prior over 21d — continuous-component sum (absolute)."""
    r = _log_ret(close)
    trunc = r.abs().where(r.abs() < 2 * _sigma_prior(r, MDAYS), 0.0)
    return trunc.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f38_jpdt_374_sum_jump_returns_21d_d3(close: pd.Series) -> pd.Series:
    """Σ of |r| restricted to |r|≥2σ_21_prior over 21d — jump-component sum (absolute)."""
    r = _log_ret(close)
    jump = r.abs().where(r.abs() >= 2 * _sigma_prior(r, MDAYS), 0.0)
    return jump.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f38_jpdt_375_var_returns_on_jump_days_252d_d3(close: pd.Series) -> pd.Series:
    """Variance of r on 3σ_21d jump days only over 252d (within-jump-day return dispersion)."""
    r = _log_ret(close)
    jmask = r.abs() > 3 * _sigma_prior(r, MDAYS)
    return r.where(jmask, np.nan).rolling(YDAYS, min_periods=QDAYS).var().diff().diff().diff()
JUMP_DETECTION_SIGNATURE_D3_REGISTRY_301_375 = {'f38_jpdt_301_jump_count_when_top5_of_252d_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_301_jump_count_when_top5_of_252d_range_d3}, 'f38_jpdt_302_jump_count_when_top10_of_252d_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_302_jump_count_when_top10_of_252d_range_d3}, 'f38_jpdt_303_mean_abs_r_near_252d_high_d3': {'inputs': ['close', 'high'], 'func': f38_jpdt_303_mean_abs_r_near_252d_high_d3}, 'f38_jpdt_304_neg_jump_count_near_252d_high_d3': {'inputs': ['close', 'high'], 'func': f38_jpdt_304_neg_jump_count_near_252d_high_d3}, 'f38_jpdt_305_jump_asymmetry_in_top_decile_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_305_jump_asymmetry_in_top_decile_252d_d3}, 'f38_jpdt_306_bars_since_first_jump_near_peak_d3': {'inputs': ['close', 'high'], 'func': f38_jpdt_306_bars_since_first_jump_near_peak_d3}, 'f38_jpdt_307_max_neg_r_within_21d_after_252d_high_d3': {'inputs': ['close', 'high'], 'func': f38_jpdt_307_max_neg_r_within_21d_after_252d_high_d3}, 'f38_jpdt_308_sum_abs_r_within_5d_of_252d_high_252d_d3': {'inputs': ['close', 'high'], 'func': f38_jpdt_308_sum_abs_r_within_5d_of_252d_high_252d_d3}, 'f38_jpdt_309_jump_count_in_21d_after_252d_high_d3': {'inputs': ['close', 'high'], 'func': f38_jpdt_309_jump_count_in_21d_after_252d_high_d3}, 'f38_jpdt_310_post_peak_jump_intensity_ratio_252d_d3': {'inputs': ['close', 'high'], 'func': f38_jpdt_310_post_peak_jump_intensity_ratio_252d_d3}, 'f38_jpdt_311_jump_count_high_vol_regime_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_311_jump_count_high_vol_regime_252d_d3}, 'f38_jpdt_312_jump_count_low_vol_regime_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_312_jump_count_low_vol_regime_252d_d3}, 'f38_jpdt_313_mean_abs_r_jump_high_vol_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_313_mean_abs_r_jump_high_vol_252d_d3}, 'f38_jpdt_314_mean_abs_r_jump_low_vol_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_314_mean_abs_r_jump_low_vol_252d_d3}, 'f38_jpdt_315_ratio_high_vs_low_vol_jumps_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_315_ratio_high_vs_low_vol_jumps_252d_d3}, 'f38_jpdt_316_mean_sigma_rank_at_jump_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_316_mean_sigma_rank_at_jump_252d_d3}, 'f38_jpdt_317_jump_then_vol_spike_count_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_317_jump_then_vol_spike_count_252d_d3}, 'f38_jpdt_318_jump_then_vol_collapse_count_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_318_jump_then_vol_collapse_count_252d_d3}, 'f38_jpdt_319_jump_count_top_decile_volume_252d_d3': {'inputs': ['close', 'volume'], 'func': f38_jpdt_319_jump_count_top_decile_volume_252d_d3}, 'f38_jpdt_320_jump_count_bottom_decile_volume_252d_d3': {'inputs': ['close', 'volume'], 'func': f38_jpdt_320_jump_count_bottom_decile_volume_252d_d3}, 'f38_jpdt_321_ratio_high_low_volume_jumps_252d_d3': {'inputs': ['close', 'volume'], 'func': f38_jpdt_321_ratio_high_low_volume_jumps_252d_d3}, 'f38_jpdt_322_mean_volume_neg_jump_days_252d_d3': {'inputs': ['close', 'volume'], 'func': f38_jpdt_322_mean_volume_neg_jump_days_252d_d3}, 'f38_jpdt_323_mean_volume_pos_jump_days_252d_d3': {'inputs': ['close', 'volume'], 'func': f38_jpdt_323_mean_volume_pos_jump_days_252d_d3}, 'f38_jpdt_324_gap_and_go_indicator_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_324_gap_and_go_indicator_d3}, 'f38_jpdt_325_gap_and_fade_indicator_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_325_gap_and_fade_indicator_d3}, 'f38_jpdt_326_gap_and_go_count_63d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_326_gap_and_go_count_63d_d3}, 'f38_jpdt_327_gap_and_fade_count_63d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_327_gap_and_fade_count_63d_d3}, 'f38_jpdt_328_reversal_bar_count_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_328_reversal_bar_count_252d_d3}, 'f38_jpdt_329_outside_day_count_252d_d3': {'inputs': ['high', 'low'], 'func': f38_jpdt_329_outside_day_count_252d_d3}, 'f38_jpdt_330_inside_after_big_range_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_330_inside_after_big_range_count_252d_d3}, 'f38_jpdt_331_two_bar_reversal_count_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_331_two_bar_reversal_count_252d_d3}, 'f38_jpdt_332_failure_pattern_count_252d_d3': {'inputs': ['open', 'high', 'close'], 'func': f38_jpdt_332_failure_pattern_count_252d_d3}, 'f38_jpdt_333_failure_at_252d_high_count_252d_d3': {'inputs': ['open', 'high', 'close'], 'func': f38_jpdt_333_failure_at_252d_high_count_252d_d3}, 'f38_jpdt_334_distribution_day_count_252d_d3': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f38_jpdt_334_distribution_day_count_252d_d3}, 'f38_jpdt_335_ad_divergence_signal_252d_d3': {'inputs': ['close', 'volume'], 'func': f38_jpdt_335_ad_divergence_signal_252d_d3}, 'f38_jpdt_336_bars_since_last_gap_up_d3': {'inputs': ['open', 'close'], 'func': f38_jpdt_336_bars_since_last_gap_up_d3}, 'f38_jpdt_337_bars_since_last_gap_down_d3': {'inputs': ['open', 'close'], 'func': f38_jpdt_337_bars_since_last_gap_down_d3}, 'f38_jpdt_338_bars_since_last_nr4_d3': {'inputs': ['high', 'low'], 'func': f38_jpdt_338_bars_since_last_nr4_d3}, 'f38_jpdt_339_bars_since_last_wr7_d3': {'inputs': ['high', 'low'], 'func': f38_jpdt_339_bars_since_last_wr7_d3}, 'f38_jpdt_340_bars_since_close_near_bar_low_d3': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_340_bars_since_close_near_bar_low_d3}, 'f38_jpdt_341_bars_since_252d_high_d3': {'inputs': ['close', 'high'], 'func': f38_jpdt_341_bars_since_252d_high_d3}, 'f38_jpdt_342_bars_since_large_range_bar_d3': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_342_bars_since_large_range_bar_d3}, 'f38_jpdt_343_bars_since_alltime_high_d3': {'inputs': ['close'], 'func': f38_jpdt_343_bars_since_alltime_high_d3}, 'f38_jpdt_344_cum_thrust_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_344_cum_thrust_21d_d3}, 'f38_jpdt_345_cum_pullback_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_345_cum_pullback_21d_d3}, 'f38_jpdt_346_up_down_day_ratio_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_346_up_down_day_ratio_21d_d3}, 'f38_jpdt_347_max_pullback_63d_d3': {'inputs': ['close'], 'func': f38_jpdt_347_max_pullback_63d_d3}, 'f38_jpdt_348_pullback_to_thrust_ratio_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_348_pullback_to_thrust_ratio_252d_d3}, 'f38_jpdt_349_counter_trend_bar_count_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_349_counter_trend_bar_count_21d_d3}, 'f38_jpdt_350_with_trend_bar_count_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_350_with_trend_bar_count_21d_d3}, 'f38_jpdt_351_efficiency_ratio_signed_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_351_efficiency_ratio_signed_21d_d3}, 'f38_jpdt_352_signed_momentum_1bar_d3': {'inputs': ['close'], 'func': f38_jpdt_352_signed_momentum_1bar_d3}, 'f38_jpdt_353_log_return_5d_d3': {'inputs': ['close'], 'func': f38_jpdt_353_log_return_5d_d3}, 'f38_jpdt_354_log_return_10d_d3': {'inputs': ['close'], 'func': f38_jpdt_354_log_return_10d_d3}, 'f38_jpdt_355_ratio_5d_21d_logret_d3': {'inputs': ['close'], 'func': f38_jpdt_355_ratio_5d_21d_logret_d3}, 'f38_jpdt_356_momentum_mismatch_5_21_d3': {'inputs': ['close'], 'func': f38_jpdt_356_momentum_mismatch_5_21_d3}, 'f38_jpdt_357_ret_per_unit_sigma_5d_d3': {'inputs': ['close'], 'func': f38_jpdt_357_ret_per_unit_sigma_5d_d3}, 'f38_jpdt_358_bull_trap_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_358_bull_trap_count_252d_d3}, 'f38_jpdt_359_bear_trap_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_359_bear_trap_count_252d_d3}, 'f38_jpdt_360_failed_breakout_count_252d_d3': {'inputs': ['high', 'close'], 'func': f38_jpdt_360_failed_breakout_count_252d_d3}, 'f38_jpdt_361_failed_breakdown_count_252d_d3': {'inputs': ['low', 'close'], 'func': f38_jpdt_361_failed_breakdown_count_252d_d3}, 'f38_jpdt_362_exhaustion_gap_count_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_362_exhaustion_gap_count_252d_d3}, 'f38_jpdt_363_breakaway_gap_count_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_363_breakaway_gap_count_252d_d3}, 'f38_jpdt_364_three_bar_consolidation_count_252d_d3': {'inputs': ['high', 'low'], 'func': f38_jpdt_364_three_bar_consolidation_count_252d_d3}, 'f38_jpdt_365_three_bar_trend_count_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_365_three_bar_trend_count_252d_d3}, 'f38_jpdt_366_vol_thrust_price_thrust_count_63d_d3': {'inputs': ['close', 'volume'], 'func': f38_jpdt_366_vol_thrust_price_thrust_count_63d_d3}, 'f38_jpdt_367_volume_divergence_count_63d_d3': {'inputs': ['close', 'volume'], 'func': f38_jpdt_367_volume_divergence_count_63d_d3}, 'f38_jpdt_368_volume_drying_count_63d_d3': {'inputs': ['volume'], 'func': f38_jpdt_368_volume_drying_count_63d_d3}, 'f38_jpdt_369_volume_explosion_count_63d_d3': {'inputs': ['volume'], 'func': f38_jpdt_369_volume_explosion_count_63d_d3}, 'f38_jpdt_370_sustained_volume_run_252d_d3': {'inputs': ['volume'], 'func': f38_jpdt_370_sustained_volume_run_252d_d3}, 'f38_jpdt_371_jvar_over_bv_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_371_jvar_over_bv_21d_d3}, 'f38_jpdt_372_truncated_return_indicator_d3': {'inputs': ['close'], 'func': f38_jpdt_372_truncated_return_indicator_d3}, 'f38_jpdt_373_sum_truncated_returns_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_373_sum_truncated_returns_21d_d3}, 'f38_jpdt_374_sum_jump_returns_21d_d3': {'inputs': ['close'], 'func': f38_jpdt_374_sum_jump_returns_21d_d3}, 'f38_jpdt_375_var_returns_on_jump_days_252d_d3': {'inputs': ['close'], 'func': f38_jpdt_375_var_returns_on_jump_days_252d_d3}}