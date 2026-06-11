"""38_jump_detection_signature d2 features 526-600 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def f38_jpdt_526_reversal_rate_lag1_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of bars where sign(r_t) ≠ sign(r_{t-1}) over 252d — daily reversal rate."""
    r = _log_ret(close)
    rev = (np.sign(r) != np.sign(r.shift(1))) & (np.sign(r) != 0)
    return rev.astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_527_continuation_rate_lag1_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of bars where sign(r_t) == sign(r_{t-1}) over 252d — daily continuation rate."""
    r = _log_ret(close)
    cont = (np.sign(r) == np.sign(r.shift(1))) & (np.sign(r) != 0)
    return cont.astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_528_mean_counter_trend_magnitude_252d_d2(close: pd.Series) -> pd.Series:
    """Mean |r| on bars where sign(r) opposite of 21d-trend, over 252d."""
    r = _log_ret(close)
    trend = np.sign(close - close.shift(MDAYS))
    counter = (np.sign(r) != trend) & (np.sign(r) != 0)
    return r.abs().where(counter, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_529_mean_with_trend_magnitude_252d_d2(close: pd.Series) -> pd.Series:
    """Mean |r| on bars where sign(r) matches 21d-trend, over 252d."""
    r = _log_ret(close)
    trend = np.sign(close - close.shift(MDAYS))
    with_t = (np.sign(r) == trend) & (np.sign(r) != 0)
    return r.abs().where(with_t, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_530_mean_abs_r_within_5pct_252d_high_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean |r| restricted to bars within 5% of 252d-high, over 252d."""
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_high = close >= 0.95 * h252
    return _log_ret(close).abs().where(near_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_531_mean_abs_r_within_5pct_252d_low_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    """Mean |r| restricted to bars within 5% of 252d-low, over 252d."""
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    near_low = close <= 1.05 * l252
    return _log_ret(close).abs().where(near_low, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_532_p_up_given_down_prior_252d_d2(close: pd.Series) -> pd.Series:
    """P(up-day | prior down-day) over 252d — bounce-back rate."""
    r = _log_ret(close)
    dn_prior = r.shift(1) < 0
    up = r > 0
    joint = (dn_prior & up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = dn_prior.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(joint, marg).diff().diff()

def f38_jpdt_533_p_up_given_up_prior_252d_d2(close: pd.Series) -> pd.Series:
    """P(up-day | prior up-day) over 252d — momentum continuation rate."""
    r = _log_ret(close)
    up_prior = r.shift(1) > 0
    up = r > 0
    joint = (up_prior & up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = up_prior.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(joint, marg).diff().diff()

def f38_jpdt_534_mean_r5d_given_prior_r5d_pos_252d_d2(close: pd.Series) -> pd.Series:
    """Mean 5d log-return given prior 5d log-return > 0 over 252d."""
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    prior_pos = r5.shift(WDAYS) > 0
    return r5.where(prior_pos, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_535_mean_r5d_given_prior_r5d_neg_252d_d2(close: pd.Series) -> pd.Series:
    """Mean 5d log-return given prior 5d log-return < 0 over 252d."""
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    prior_neg = r5.shift(WDAYS) < 0
    return r5.where(prior_neg, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_536_extreme_pos_density_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of bars with r > p99 of 252d distribution (extreme-positive density)."""
    r = _log_ret(close)
    p99 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    return (r > p99).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_537_extreme_neg_density_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of bars with r < p1 of 252d distribution (extreme-negative density)."""
    r = _log_ret(close)
    p1 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.01).shift(1)
    return (r < p1).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_538_bimodality_coef_returns_252d_d2(close: pd.Series) -> pd.Series:
    """Bimodality coefficient (skew²+1)/(kurt+correction) of returns over 252d."""
    r = _log_ret(close)
    sk = r.rolling(YDAYS, min_periods=QDAYS).skew()
    kt = r.rolling(YDAYS, min_periods=QDAYS).kurt()
    n = YDAYS
    corr = 3.0 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    return ((sk ** 2 + 1.0) / (kt + corr)).diff().diff()

def f38_jpdt_539_median_mean_distance_abs_r_252d_d2(close: pd.Series) -> pd.Series:
    """|median(|r|) − mean(|r|)| over 252d — distributional asymmetry of magnitude."""
    a = _log_ret(close).abs()
    return (a.rolling(YDAYS, min_periods=QDAYS).median() - a.rolling(YDAYS, min_periods=QDAYS).mean()).abs().diff().diff()

def f38_jpdt_540_pearson_skewness_252d_d2(close: pd.Series) -> pd.Series:
    """Pearson skewness coefficient: 3·(mean − median) / std of r over 252d."""
    r = _log_ret(close)
    mean = r.rolling(YDAYS, min_periods=QDAYS).mean()
    median = r.rolling(YDAYS, min_periods=QDAYS).median()
    std = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(3.0 * (mean - median), std).diff().diff()

def f38_jpdt_541_p10_p90_range_252d_d2(close: pd.Series) -> pd.Series:
    """(p90 - p10) of r over 252d — central-tendency range."""
    r = _log_ret(close)
    return (r.rolling(YDAYS, min_periods=QDAYS).quantile(0.9) - r.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)).diff().diff()

def f38_jpdt_542_iqr_returns_252d_d2(close: pd.Series) -> pd.Series:
    """Interquartile range (p75 - p25) of r over 252d."""
    r = _log_ret(close)
    return (r.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - r.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)).diff().diff()

def f38_jpdt_543_tail_share_above_p90_252d_d2(close: pd.Series) -> pd.Series:
    """Σ|r| restricted to |r| > p90 / total Σ|r| over 252d."""
    a = _log_ret(close).abs()
    p90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    tail = a.where(a > p90, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    total = a.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(tail, total).diff().diff()

def f38_jpdt_544_center_share_p25_p75_252d_d2(close: pd.Series) -> pd.Series:
    """Σ|r| restricted to |r| in [p25, p75] / total Σ|r| over 252d."""
    a = _log_ret(close).abs()
    p25 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25).shift(1)
    p75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    center = a.where((a >= p25) & (a <= p75), 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    total = a.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(center, total).diff().diff()

def f38_jpdt_545_extreme_share_above_p99_252d_d2(close: pd.Series) -> pd.Series:
    """Σ|r| restricted to |r| > p99 / total Σ|r| over 252d."""
    a = _log_ret(close).abs()
    p99 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    tail = a.where(a > p99, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    total = a.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(tail, total).diff().diff()

def f38_jpdt_546_gap_up_after_3down_count_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-up (>1%) after 3+ consecutive down-days, count over 252d."""
    r = _log_ret(close)
    three_dn = (r.shift(1) < 0) & (r.shift(2) < 0) & (r.shift(3) < 0)
    gap_up = open > close.shift(1) * 1.01
    return (gap_up & three_dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_547_gap_down_after_3up_count_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-down (>1%) after 3+ consecutive up-days, count over 252d."""
    r = _log_ret(close)
    three_up = (r.shift(1) > 0) & (r.shift(2) > 0) & (r.shift(3) > 0)
    gap_dn = open < close.shift(1) * 0.99
    return (gap_dn & three_up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_548_gap_and_go_holds_count_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-up + close above gap + next bar's low stays above gap, count over 252d."""
    gap_up = open > close.shift(1) * 1.005
    above_gap = close > close.shift(1) * 1.005
    next_holds = low.shift(1) > close.shift(1) * 1.005
    gap_up_lag = open.shift(1) > close.shift(2) * 1.005
    above_gap_lag = close.shift(1) > close.shift(2) * 1.005
    holds_now = low > close.shift(2) * 1.005
    return (gap_up_lag & above_gap_lag & holds_now).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_549_gap_down_no_fill_count_252d_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-down + next bar's high < prior close (gap NOT filled), count over 252d (causal lag form)."""
    gap_dn_lag = open.shift(1) < close.shift(2) * 0.995
    no_fill_now = high < close.shift(2)
    return (gap_dn_lag & no_fill_now).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_550_gap_down_high_volume_count_252d_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gap-down on top-decile-volume days count over 252d."""
    gap_dn = open < close.shift(1) * 0.99
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    big_vol = volume > p90
    return (gap_dn & big_vol).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_551_gap_up_high_volume_count_252d_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gap-up on top-decile-volume days count over 252d."""
    gap_up = open > close.shift(1) * 1.01
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    big_vol = volume > p90
    return (gap_up & big_vol).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_552_gap_down_near_high_magnitude_252d_d2(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean gap-down magnitude on bars within 5% of 252d-high, over 252d."""
    gap = (open - close.shift(1)) / close.shift(1)
    near_high = close.shift(1) >= 0.95 * close.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return gap.abs().where((gap < 0) & near_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_553_mean_gap_size_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |gap| (open - prev close) / prev close over 21d."""
    gap = ((open - close.shift(1)) / close.shift(1)).abs()
    return gap.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_554_std_gap_size_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Std of |gap| over 21d."""
    gap = ((open - close.shift(1)) / close.shift(1)).abs()
    return gap.rolling(MDAYS, min_periods=WDAYS).std().diff().diff()

def f38_jpdt_555_largest_single_gap_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Max |gap|/close in trailing 63d (worst single gap)."""
    gap = ((open - close.shift(1)) / close).abs()
    return gap.rolling(QDAYS, min_periods=MDAYS).max().diff().diff()

def f38_jpdt_556_tick_direction_proxy_21d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean sign(close - bar midpoint) over 21d (tick-direction proxy)."""
    mid = (high + low) / 2.0
    return np.sign(close - mid).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_557_tick_imbalance_proxy_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ sign(close - midpoint) over 63d (cumulative tick-imbalance proxy)."""
    mid = (high + low) / 2.0
    return np.sign(close - mid).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f38_jpdt_558_oc_vs_hl_used_21d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |close - open| / (high - low) over 21d — intraday-range used by net move."""
    return _safe_div((close - open).abs(), high - low).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_559_oc_vs_gap_magnitude_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |close - open| / |gap| over 21d — intraday move vs overnight-gap share."""
    gap = (open - close.shift(1)).abs()
    return _safe_div((close - open).abs(), gap).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_560_selling_into_strength_21d_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (high - open) / (close - open) restricted to bullish bars (close > open), 21d."""
    bull = close > open
    ratio = _safe_div(high - open, close - open)
    return ratio.where(bull, np.nan).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_561_buying_on_weakness_21d_d2(open: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (close - low) / (close - open) restricted to bullish bars over 21d (close recovered from low)."""
    bull = close > open
    ratio = _safe_div(close - low, close - open)
    return ratio.where(bull, np.nan).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_562_persistent_intra_bar_pattern_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 5+ consecutive bars all closing in top quartile of bar, over 252d."""
    pos = _safe_div(close - low, high - low)
    top = pos > 0.75
    five_seq = top & top.shift(1).fillna(False) & top.shift(2).fillna(False) & top.shift(3).fillna(False) & top.shift(4).fillna(False)
    return five_seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_563_open_strength_21d_d2(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (open - prev_close) / (high - low) over 21d — open-position-in-range proxy."""
    rng = (high - low).replace(0, np.nan)
    return _safe_div(open - close.shift(1), rng).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_564_close_strength_vs_midpoint_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (close - midpoint) / (high - low) over 21d — close-strength proxy."""
    mid = (high + low) / 2.0
    rng = (high - low).replace(0, np.nan)
    return _safe_div(close - mid, rng).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_565_avg_bar_shape_score_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Avg bar-shape score: |C-O|/range minus mean(upper-shadow + lower-shadow)/range over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_share = (close - open).abs() / rng
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    shadow_share = (high - body_hi + (body_lo - low)) / rng
    return (body_share - shadow_share).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_566_vertical_rise_5d_count_252d_d2(close: pd.Series) -> pd.Series:
    """5+ consecutive up-days each with |r| > σ_21_prior, count over 252d (vertical-rise climax)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    big_up = r > sig
    five_seq = big_up & big_up.shift(1).fillna(False) & big_up.shift(2).fillna(False) & big_up.shift(3).fillna(False) & big_up.shift(4).fillna(False)
    return five_seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_567_vertical_drop_5d_count_252d_d2(close: pd.Series) -> pd.Series:
    """5+ consecutive down-days each with |r| > σ_21_prior, count over 252d (capitulation)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    big_dn = r < -sig
    five_seq = big_dn & big_dn.shift(1).fillna(False) & big_dn.shift(2).fillna(False) & big_dn.shift(3).fillna(False) & big_dn.shift(4).fillna(False)
    return five_seq.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_568_sequential_new_5d_highs_count_252d_d2(high: pd.Series) -> pd.Series:
    """Count of bars making a new 5d-high (sequential high-prints) over 252d."""
    new_5d_high = high >= high.rolling(WDAYS, min_periods=2).max()
    return new_5d_high.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_569_sequential_new_5d_lows_count_252d_d2(low: pd.Series) -> pd.Series:
    """Count of bars making a new 5d-low over 252d."""
    new_5d_low = low <= low.rolling(WDAYS, min_periods=2).min()
    return new_5d_low.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_570_acceleration_to_peak_5d_vs_21d_252d_d2(close: pd.Series) -> pd.Series:
    """Mean (5d-return / 21d-return) restricted to bars at 21d-high (acceleration into peak), 252d."""
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    at_peak = close >= close.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(r5, r21).where(at_peak, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_571_deceleration_after_peak_252d_d2(close: pd.Series) -> pd.Series:
    """Mean (5d trailing post-peak / 21d trailing post-peak) restricted to 21d after a 21d-high, 252d."""
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    at_peak_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(r5, r21).where(at_peak_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_572_volume_escalation_count_252d_d2(volume: pd.Series) -> pd.Series:
    """Count of bars where last-5-days vol mean > each prior 5d vol mean, over 252d (escalating volume)."""
    v5 = volume.rolling(WDAYS, min_periods=2).mean()
    escalating = v5 > v5.shift(WDAYS)
    five_in_row = escalating & escalating.shift(1).fillna(False) & escalating.shift(2).fillna(False) & escalating.shift(3).fillna(False) & escalating.shift(4).fillna(False)
    return five_in_row.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_573_range_escalation_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where last 5 days each had TR > prior bar's TR (escalating range), 252d."""
    tr = _true_range(high, low, close)
    escalating = tr > tr.shift(1)
    five_in_row = escalating & escalating.shift(1).fillna(False) & escalating.shift(2).fillna(False) & escalating.shift(3).fillna(False) & escalating.shift(4).fillna(False)
    return five_in_row.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_574_full_climax_combo_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Higher-high AND higher-low AND higher-volume AND higher-range simultaneously, count over 252d."""
    hh = high > high.shift(1)
    hl = low > low.shift(1)
    hv = volume > volume.shift(1)
    hr = high - low > high.shift(1) - low.shift(1)
    return (hh & hl & hv & hr).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_575_climax_divergence_count_252d_d2(close: pd.Series) -> pd.Series:
    """New 21d-high BUT 14d momentum (close - 14d-ago) is LOWER than at prior 21d-high, count 252d."""
    new_high = close >= close.rolling(MDAYS, min_periods=WDAYS).max()
    mom14 = close - close.shift(14)
    mom_at_prior_high = mom14.where(new_high.shift(1).fillna(False)).ffill()
    divergence = new_high & (mom14 < mom_at_prior_high)
    return divergence.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_576_jump_at_top5_range_pos_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Pos jump (r>3σ) AND close in top 5% of 252d range, count over 252d (climax-jump strict)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    return ((r > 3 * sig) & (pos >= 0.95)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_577_jump_at_bottom5_range_pos_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Neg jump AND close in bottom 5% of 252d range count over 252d (capitulation-jump strict)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    return ((r < -3 * sig) & (pos <= 0.05)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_578_dn_close_count_after_252d_high_252d_d2(close: pd.Series) -> pd.Series:
    """Down-close count in 21d after a 252d-high event over 252d (post-peak distribution)."""
    dn = close < close.shift(1)
    new_high_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    return (dn & new_high_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_579_up_close_count_after_252d_low_252d_d2(close: pd.Series) -> pd.Series:
    """Up-close count in 21d after a 252d-low event over 252d (post-trough accumulation)."""
    up = close > close.shift(1)
    new_low_lag = close.shift(MDAYS) <= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).min()
    return (up & new_low_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_580_max_consec_dn_after_252d_high_252d_d2(close: pd.Series) -> pd.Series:
    """Max consecutive down-day streak in 21d after a 252d-high event, mean over 252d."""
    r = _log_ret(close)
    new_high_lag21 = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()

    def _max_dn_streak(w):
        cur = 0
        mx = 0
        for v in w:
            if v < 0:
                cur += 1
                mx = cur if cur > mx else mx
            else:
                cur = 0
        return float(mx)
    streak21 = r.rolling(MDAYS, min_periods=WDAYS).apply(_max_dn_streak, raw=True)
    return streak21.where(new_high_lag21, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_581_pct_negative_post_peak_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of bars in 21d after a 252d-high event with r<0, over 252d."""
    r = _log_ret(close)
    new_high_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    return (r < 0).where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_582_mean_abs_r_post_peak_252d_d2(close: pd.Series) -> pd.Series:
    """Mean |r| in 21d after a 252d-high event, over 252d (post-peak vol)."""
    a = _log_ret(close).abs()
    new_high_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    return a.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_583_max_dd_within_21d_post_peak_252d_d2(close: pd.Series) -> pd.Series:
    """Max drawdown within 21d after a 252d-high event, mean over 252d."""
    new_high_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()

    def _dd(w):
        ww = w[~np.isnan(w)]
        if len(ww) < WDAYS:
            return np.nan
        peak = np.maximum.accumulate(ww)
        return float(np.max(1.0 - ww / peak))
    dd21 = close.rolling(MDAYS, min_periods=WDAYS).apply(_dd, raw=True)
    return dd21.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_584_post_peak_volume_z_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume z-score in 21d after a 252d-high event, over 252d."""
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    new_high_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    return vz.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_585_failure_at_old_high_count_252d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars where close approaches 252d-high (within 1%) but fails (close < high), over 252d."""
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_high = close >= 0.99 * h252
    failed = close < high
    return (near_high & failed).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_586_consecutive_lower_close_after_peak_252d_d2(close: pd.Series) -> pd.Series:
    """Mean count of consecutive lower-closes after most recent 252d-high event."""
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    arr_h = new_high.astype(int).fillna(0).values
    arr_close = close.values
    out = np.full(len(arr_close), np.nan)
    bars_since_high = np.nan
    last_high_close = np.nan
    for i in range(len(arr_close)):
        if arr_h[i] == 1:
            bars_since_high = 0
            last_high_close = arr_close[i]
        elif np.isfinite(bars_since_high):
            bars_since_high += 1
        if np.isfinite(bars_since_high) and bars_since_high > 0:
            cnt = 0
            for j in range(i, max(i - int(bars_since_high), -1), -1):
                if j < 1:
                    break
                if arr_close[j] < arr_close[j - 1]:
                    cnt += 1
                else:
                    break
            out[i] = float(cnt)
    return pd.Series(out, index=close.index).diff().diff()

def f38_jpdt_587_abs_r_skew_252d_excluding_jumps_d2(close: pd.Series) -> pd.Series:
    """Skew of |r| restricted to non-jump bars (|r| ≤ 2σ_prior), over 252d (continuous-component skew)."""
    r = _log_ret(close)
    a = r.abs()
    sig = _sigma_prior(r, MDAYS)
    return a.where(a <= 2 * sig, np.nan).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff()

def f38_jpdt_588_mean_5d_return_after_climax_jump_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean 5d trailing return on bars 5d after climax-jump (jump + top 5% range), over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    climax_lag = (r.shift(WDAYS) > 3 * sig.shift(WDAYS)) & (pos.shift(WDAYS) >= 0.95)
    trail5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    return trail5.where(climax_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_589_volume_drying_count_after_252d_high_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume drying days (5d-mean-vol < 50% of 252d-mean-vol) within 21d after 252d-high, over 252d."""
    short_vol = volume.rolling(WDAYS, min_periods=2).mean()
    long_vol = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    drying = short_vol < 0.5 * long_vol
    new_high_lag = close.shift(MDAYS) >= close.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    return (drying & new_high_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_590_corr_volume_with_neg_r_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr(volume, r restricted to r<0) — sell-volume coupling."""
    r = _log_ret(close)
    r_neg = r.where(r < 0, np.nan)
    return volume.rolling(YDAYS, min_periods=QDAYS).corr(r_neg).diff().diff()

def f38_jpdt_591_corr_volume_with_pos_r_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr(volume, r restricted to r>0) — buy-volume coupling."""
    r = _log_ret(close)
    r_pos = r.where(r > 0, np.nan)
    return volume.rolling(YDAYS, min_periods=QDAYS).corr(r_pos).diff().diff()

def f38_jpdt_592_volume_negative_skew_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Skew of volume on days with r < 0, over 252d (sell-volume distribution)."""
    r = _log_ret(close)
    return volume.where(r < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff()

def f38_jpdt_593_volume_positive_skew_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Skew of volume on days with r > 0, over 252d (buy-volume distribution)."""
    r = _log_ret(close)
    return volume.where(r > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff()

def f38_jpdt_594_max_consecutive_down_streak_252d_d2(close: pd.Series) -> pd.Series:
    """Max consecutive down-day streak within 252d window."""
    r = _log_ret(close)
    dn = (r < 0).astype(float).fillna(0.0)

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
    return dn.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True).diff().diff()

def f38_jpdt_595_max_consecutive_up_streak_252d_d2(close: pd.Series) -> pd.Series:
    """Max consecutive up-day streak within 252d window."""
    r = _log_ret(close)
    up = (r > 0).astype(float).fillna(0.0)

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
    return up.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True).diff().diff()

def f38_jpdt_596_dn_close_pct_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of bars with r<0 over 252d (bearish-day frequency)."""
    return (_log_ret(close) < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_597_mean_dn_day_magnitude_252d_d2(close: pd.Series) -> pd.Series:
    """Mean |r| on r<0 days over 252d (down-day average magnitude)."""
    r = _log_ret(close)
    return r.abs().where(r < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_598_mean_up_day_magnitude_252d_d2(close: pd.Series) -> pd.Series:
    """Mean |r| on r>0 days over 252d (up-day average magnitude)."""
    r = _log_ret(close)
    return r.abs().where(r > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_599_dn_up_magnitude_ratio_252d_d2(close: pd.Series) -> pd.Series:
    """Mean dn-day |r| / mean up-day |r| over 252d (negative-bias magnitude ratio)."""
    r = _log_ret(close)
    dn = r.abs().where(r < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    up = r.abs().where(r > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(dn, up).diff().diff()

def f38_jpdt_600_corr_r_volume_zscore_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr(r, volume z-score) — return-volume sign-amplification."""
    r = _log_ret(close)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    return r.rolling(QDAYS, min_periods=MDAYS).corr(vz).diff().diff()
JUMP_DETECTION_SIGNATURE_D2_REGISTRY_526_600 = {'f38_jpdt_526_reversal_rate_lag1_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_526_reversal_rate_lag1_252d_d2}, 'f38_jpdt_527_continuation_rate_lag1_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_527_continuation_rate_lag1_252d_d2}, 'f38_jpdt_528_mean_counter_trend_magnitude_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_528_mean_counter_trend_magnitude_252d_d2}, 'f38_jpdt_529_mean_with_trend_magnitude_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_529_mean_with_trend_magnitude_252d_d2}, 'f38_jpdt_530_mean_abs_r_within_5pct_252d_high_d2': {'inputs': ['close', 'high'], 'func': f38_jpdt_530_mean_abs_r_within_5pct_252d_high_d2}, 'f38_jpdt_531_mean_abs_r_within_5pct_252d_low_d2': {'inputs': ['close', 'low'], 'func': f38_jpdt_531_mean_abs_r_within_5pct_252d_low_d2}, 'f38_jpdt_532_p_up_given_down_prior_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_532_p_up_given_down_prior_252d_d2}, 'f38_jpdt_533_p_up_given_up_prior_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_533_p_up_given_up_prior_252d_d2}, 'f38_jpdt_534_mean_r5d_given_prior_r5d_pos_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_534_mean_r5d_given_prior_r5d_pos_252d_d2}, 'f38_jpdt_535_mean_r5d_given_prior_r5d_neg_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_535_mean_r5d_given_prior_r5d_neg_252d_d2}, 'f38_jpdt_536_extreme_pos_density_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_536_extreme_pos_density_252d_d2}, 'f38_jpdt_537_extreme_neg_density_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_537_extreme_neg_density_252d_d2}, 'f38_jpdt_538_bimodality_coef_returns_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_538_bimodality_coef_returns_252d_d2}, 'f38_jpdt_539_median_mean_distance_abs_r_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_539_median_mean_distance_abs_r_252d_d2}, 'f38_jpdt_540_pearson_skewness_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_540_pearson_skewness_252d_d2}, 'f38_jpdt_541_p10_p90_range_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_541_p10_p90_range_252d_d2}, 'f38_jpdt_542_iqr_returns_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_542_iqr_returns_252d_d2}, 'f38_jpdt_543_tail_share_above_p90_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_543_tail_share_above_p90_252d_d2}, 'f38_jpdt_544_center_share_p25_p75_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_544_center_share_p25_p75_252d_d2}, 'f38_jpdt_545_extreme_share_above_p99_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_545_extreme_share_above_p99_252d_d2}, 'f38_jpdt_546_gap_up_after_3down_count_252d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_546_gap_up_after_3down_count_252d_d2}, 'f38_jpdt_547_gap_down_after_3up_count_252d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_547_gap_down_after_3up_count_252d_d2}, 'f38_jpdt_548_gap_and_go_holds_count_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_548_gap_and_go_holds_count_252d_d2}, 'f38_jpdt_549_gap_down_no_fill_count_252d_d2': {'inputs': ['open', 'high', 'close'], 'func': f38_jpdt_549_gap_down_no_fill_count_252d_d2}, 'f38_jpdt_550_gap_down_high_volume_count_252d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f38_jpdt_550_gap_down_high_volume_count_252d_d2}, 'f38_jpdt_551_gap_up_high_volume_count_252d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f38_jpdt_551_gap_up_high_volume_count_252d_d2}, 'f38_jpdt_552_gap_down_near_high_magnitude_252d_d2': {'inputs': ['open', 'close', 'high'], 'func': f38_jpdt_552_gap_down_near_high_magnitude_252d_d2}, 'f38_jpdt_553_mean_gap_size_21d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_553_mean_gap_size_21d_d2}, 'f38_jpdt_554_std_gap_size_21d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_554_std_gap_size_21d_d2}, 'f38_jpdt_555_largest_single_gap_63d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_555_largest_single_gap_63d_d2}, 'f38_jpdt_556_tick_direction_proxy_21d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_556_tick_direction_proxy_21d_d2}, 'f38_jpdt_557_tick_imbalance_proxy_63d_d2': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_557_tick_imbalance_proxy_63d_d2}, 'f38_jpdt_558_oc_vs_hl_used_21d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_558_oc_vs_hl_used_21d_d2}, 'f38_jpdt_559_oc_vs_gap_magnitude_21d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_559_oc_vs_gap_magnitude_21d_d2}, 'f38_jpdt_560_selling_into_strength_21d_d2': {'inputs': ['open', 'high', 'close'], 'func': f38_jpdt_560_selling_into_strength_21d_d2}, 'f38_jpdt_561_buying_on_weakness_21d_d2': {'inputs': ['open', 'low', 'close'], 'func': f38_jpdt_561_buying_on_weakness_21d_d2}, 'f38_jpdt_562_persistent_intra_bar_pattern_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_562_persistent_intra_bar_pattern_252d_d2}, 'f38_jpdt_563_open_strength_21d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f38_jpdt_563_open_strength_21d_d2}, 'f38_jpdt_564_close_strength_vs_midpoint_21d_d2': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_564_close_strength_vs_midpoint_21d_d2}, 'f38_jpdt_565_avg_bar_shape_score_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_565_avg_bar_shape_score_252d_d2}, 'f38_jpdt_566_vertical_rise_5d_count_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_566_vertical_rise_5d_count_252d_d2}, 'f38_jpdt_567_vertical_drop_5d_count_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_567_vertical_drop_5d_count_252d_d2}, 'f38_jpdt_568_sequential_new_5d_highs_count_252d_d2': {'inputs': ['high'], 'func': f38_jpdt_568_sequential_new_5d_highs_count_252d_d2}, 'f38_jpdt_569_sequential_new_5d_lows_count_252d_d2': {'inputs': ['low'], 'func': f38_jpdt_569_sequential_new_5d_lows_count_252d_d2}, 'f38_jpdt_570_acceleration_to_peak_5d_vs_21d_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_570_acceleration_to_peak_5d_vs_21d_252d_d2}, 'f38_jpdt_571_deceleration_after_peak_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_571_deceleration_after_peak_252d_d2}, 'f38_jpdt_572_volume_escalation_count_252d_d2': {'inputs': ['volume'], 'func': f38_jpdt_572_volume_escalation_count_252d_d2}, 'f38_jpdt_573_range_escalation_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_573_range_escalation_count_252d_d2}, 'f38_jpdt_574_full_climax_combo_count_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f38_jpdt_574_full_climax_combo_count_252d_d2}, 'f38_jpdt_575_climax_divergence_count_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_575_climax_divergence_count_252d_d2}, 'f38_jpdt_576_jump_at_top5_range_pos_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_576_jump_at_top5_range_pos_252d_d2}, 'f38_jpdt_577_jump_at_bottom5_range_pos_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_577_jump_at_bottom5_range_pos_252d_d2}, 'f38_jpdt_578_dn_close_count_after_252d_high_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_578_dn_close_count_after_252d_high_252d_d2}, 'f38_jpdt_579_up_close_count_after_252d_low_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_579_up_close_count_after_252d_low_252d_d2}, 'f38_jpdt_580_max_consec_dn_after_252d_high_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_580_max_consec_dn_after_252d_high_252d_d2}, 'f38_jpdt_581_pct_negative_post_peak_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_581_pct_negative_post_peak_252d_d2}, 'f38_jpdt_582_mean_abs_r_post_peak_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_582_mean_abs_r_post_peak_252d_d2}, 'f38_jpdt_583_max_dd_within_21d_post_peak_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_583_max_dd_within_21d_post_peak_252d_d2}, 'f38_jpdt_584_post_peak_volume_z_252d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_584_post_peak_volume_z_252d_d2}, 'f38_jpdt_585_failure_at_old_high_count_252d_d2': {'inputs': ['close', 'high'], 'func': f38_jpdt_585_failure_at_old_high_count_252d_d2}, 'f38_jpdt_586_consecutive_lower_close_after_peak_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_586_consecutive_lower_close_after_peak_252d_d2}, 'f38_jpdt_587_abs_r_skew_252d_excluding_jumps_d2': {'inputs': ['close'], 'func': f38_jpdt_587_abs_r_skew_252d_excluding_jumps_d2}, 'f38_jpdt_588_mean_5d_return_after_climax_jump_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_588_mean_5d_return_after_climax_jump_252d_d2}, 'f38_jpdt_589_volume_drying_count_after_252d_high_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_589_volume_drying_count_after_252d_high_d2}, 'f38_jpdt_590_corr_volume_with_neg_r_252d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_590_corr_volume_with_neg_r_252d_d2}, 'f38_jpdt_591_corr_volume_with_pos_r_252d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_591_corr_volume_with_pos_r_252d_d2}, 'f38_jpdt_592_volume_negative_skew_252d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_592_volume_negative_skew_252d_d2}, 'f38_jpdt_593_volume_positive_skew_252d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_593_volume_positive_skew_252d_d2}, 'f38_jpdt_594_max_consecutive_down_streak_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_594_max_consecutive_down_streak_252d_d2}, 'f38_jpdt_595_max_consecutive_up_streak_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_595_max_consecutive_up_streak_252d_d2}, 'f38_jpdt_596_dn_close_pct_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_596_dn_close_pct_252d_d2}, 'f38_jpdt_597_mean_dn_day_magnitude_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_597_mean_dn_day_magnitude_252d_d2}, 'f38_jpdt_598_mean_up_day_magnitude_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_598_mean_up_day_magnitude_252d_d2}, 'f38_jpdt_599_dn_up_magnitude_ratio_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_599_dn_up_magnitude_ratio_252d_d2}, 'f38_jpdt_600_corr_r_volume_zscore_63d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_600_corr_r_volume_zscore_63d_d2}}