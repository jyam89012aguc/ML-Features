"""advance_magnitude_duration d3 features 076_150 — 3rd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff().diff() so the output is the third bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
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
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f03_amad_076_log_excess_advance_252d_vs_baseline_1260d_d3(close: pd.Series) -> pd.Series:
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    base = r252.rolling(1260, min_periods=YDAYS).median()
    return (r252 - base).diff().diff().diff()

def f03_amad_077_log_advance_252d_zscore_in_2520d_d3(close: pd.Series) -> pd.Series:
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return _rolling_zscore(r252, 2520, min_periods=YDAYS * 2).diff().diff().diff()

def f03_amad_078_log_advance_252d_pct_rank_in_2520d_d3(close: pd.Series) -> pd.Series:
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return r252.rolling(2520, min_periods=YDAYS * 2).rank(pct=True).diff().diff().diff()

def f03_amad_079_advance_horizon_ratio_252d_to_1260d_log_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    r252 = lp - lp.shift(YDAYS)
    r1260 = lp - lp.shift(1260)
    return _safe_div(r252, r1260).diff().diff().diff()

def f03_amad_080_advance_horizon_ratio_63d_to_252d_log_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    r63 = lp - lp.shift(QDAYS)
    r252 = lp - lp.shift(YDAYS)
    return _safe_div(r63, r252).diff().diff().diff()

def f03_amad_081_magnitude_horizon_slope_log_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    r5 = lp - lp.shift(WDAYS)
    r21 = lp - lp.shift(MDAYS)
    r63 = lp - lp.shift(QDAYS)
    r252 = lp - lp.shift(YDAYS)
    xs = np.array([np.log(WDAYS), np.log(MDAYS), np.log(QDAYS), np.log(YDAYS)])
    xm = xs.mean()
    den = ((xs - xm) ** 2).sum()
    ys = pd.concat([r5, r21, r63, r252], axis=1).values
    ym = ys.mean(axis=1)
    num = ((xs - xm) * (ys - ym[:, None])).sum(axis=1)
    return pd.Series(num / den, index=close.index).diff().diff().diff()

def f03_amad_082_horizon_consistency_corr_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    r5 = lp - lp.shift(WDAYS)
    r21 = lp - lp.shift(MDAYS)
    r63 = lp - lp.shift(QDAYS)
    r252 = lp - lp.shift(YDAYS)
    xs = np.array([np.log(WDAYS), np.log(MDAYS), np.log(QDAYS), np.log(YDAYS)])
    ys = pd.concat([r5, r21, r63, r252], axis=1).values
    xm = xs.mean()
    ym = ys.mean(axis=1)
    num = ((xs - xm) * (ys - ym[:, None])).sum(axis=1)
    dx = np.sqrt(((xs - xm) ** 2).sum())
    dy = np.sqrt(((ys - ym[:, None]) ** 2).sum(axis=1))
    return pd.Series(num / (dx * dy), index=close.index).replace([np.inf, -np.inf], np.nan).diff().diff().diff()

def f03_amad_083_dollar_value_growth_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (close * (_safe_div(close, rmin) - 1.0)).diff().diff().diff()

def f03_amad_084_cumulative_log_advance_during_uptrend_segments_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    masked = r.where(close > sma, 0.0)
    return masked.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_085_log_advance_normalized_by_volatility_252d_d3(close: pd.Series) -> pd.Series:
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    rv = _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(YDAYS)
    return _safe_div(r252, rv).diff().diff().diff()

def f03_amad_086_log_advance_normalized_by_parkinson_vol_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    lr = (_safe_log(high) - _safe_log(low)) ** 2
    pk = np.sqrt(lr.rolling(YDAYS, min_periods=QDAYS).mean() / (4.0 * np.log(2.0)) * YDAYS)
    return _safe_div(r252, pk).diff().diff().diff()

def f03_amad_087_advance_per_dollar_volume_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    dv = _safe_log((close * volume).rolling(YDAYS, min_periods=QDAYS).sum())
    return _safe_div(r252, dv).diff().diff().diff()

def f03_amad_088_volume_weighted_advance_intensity_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lv = _safe_log(volume)
    return ((r * lv).rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)).diff().diff().diff()

def f03_amad_089_stairstep_advance_score_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax_prior = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > rmax_prior
    held = (close / high.replace(0, np.nan) >= 0.99).rolling(WDAYS, min_periods=2).mean()
    score = (new_high & (held >= 0.6)).astype(float)
    return score.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_090_base_consolidation_count_before_advance_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    p25 = rv21.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = (rv21 < p25).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_091_longest_run_above_50pct_252d_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    flag = (pos > 0.5).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f03_amad_092_longest_run_above_75pct_252d_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    flag = (pos > 0.75).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f03_amad_093_longest_run_above_90pct_252d_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    flag = (pos > 0.9).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f03_amad_094_days_within_2pct_of_252d_high_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (close >= 0.98 * rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_095_max_consecutive_higher_close_run_252d_d3(close: pd.Series) -> pd.Series:
    up = (close > close.shift(1)).astype(int)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f03_amad_096_max_run_within_5pct_of_252d_high_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (close >= 0.95 * rmax).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f03_amad_097_days_in_top_quartile_log_close_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    p75 = lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (lp >= p75).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_098_mean_days_per_uptrend_leg_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (close >= rmax).astype(int)

    def _mean_gap(w):
        if np.isnan(w).any():
            return np.nan
        peaks = np.where(w > 0.5)[0]
        if len(peaks) < 2:
            return np.nan
        return float(np.diff(peaks).mean())
    return is_peak.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True).diff().diff().diff()

def f03_amad_099_advance_resilience_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return (1.0 - dd.rolling(YDAYS, min_periods=QDAYS).min().abs()).diff().diff().diff()

def f03_amad_100_total_continuous_holding_time_above_50pct_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    flag = (pos > 0.5).astype(int)
    grp = (flag == 0).cumsum()
    run_len = flag.groupby(grp).cumsum()
    qualifies = (run_len.groupby(grp).transform('max') >= MDAYS).astype(float)
    return (flag * qualifies).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_101_days_close_within_1pct_of_252d_max_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (close >= 0.99 * rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_102_share_252d_in_advance_phase_d3(close: pd.Series) -> pd.Series:
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    flag = ((close > s21) & (s21 > s63)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f03_amad_103_share_252d_in_distribution_phase_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = close >= 0.95 * rmax
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    flat = s21.diff(MDAYS).abs() / s21.replace(0, np.nan) < 0.01
    flag = (near & flat).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f03_amad_104_retracement_count_during_advance_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    in_pullback = dd < -0.03
    entry = in_pullback & ~in_pullback.shift(1).fillna(False)
    return entry.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_105_mean_retracement_size_during_advance_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return dd.where(dd < 0).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f03_amad_106_advance_log_x_age_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    age = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return ((_safe_log(close) - _safe_log(rmin)) * age).diff().diff().diff()

def f03_amad_107_advance_log_x_days_above_sma252_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    days = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return (adv * days).diff().diff().diff()

def f03_amad_108_advance_log_x_run_above_sma63_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    flag = (close > sma).astype(int)
    grp = (flag == 0).cumsum()
    streak_max = flag.groupby(grp).cumsum().rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return (adv * streak_max).diff().diff().diff()

def f03_amad_109_effective_advance_score_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    age = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(rmin), age + 1.0).diff().diff().diff()

def f03_amad_110_sustained_advance_strength_252d_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    pos = (_safe_log(close) - _safe_log(sma)).clip(lower=0)
    return pos.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f03_amad_111_advance_x_no_pullback_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd_share = (_safe_div(close, rmax) - 1.0).abs().rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(adv, 1.0 + dd_share).diff().diff().diff()

def f03_amad_112_magnitude_per_new_high_touch_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax_prior = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    nh = (high > rmax_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = _safe_log(rmax) - _safe_log(rmin)
    return _safe_div(rng, 1.0 + nh).diff().diff().diff()

def f03_amad_113_duration_weighted_log_advance_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    r252 = lp - lp.shift(YDAYS)
    return (r252.rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)).diff().diff().diff()

def f03_amad_114_mature_outsized_advance_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return (adv.rolling(YDAYS, min_periods=QDAYS).max() * pa).diff().diff().diff()

def f03_amad_115_fresh_outsized_advance_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return _safe_div(adv.rolling(YDAYS, min_periods=QDAYS).max(), 1.0 + pa).diff().diff().diff()

def f03_amad_116_advance_log_x_sma_stacking_days_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    stack = ((close > s21) & (s21 > s63) & (s63 > s252)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return (adv * stack).diff().diff().diff()

def f03_amad_117_advance_log_x_R2_close_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:

    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        return 1.0 - ((w - pred) ** 2).sum() / ss_tot
    r2 = close.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return (adv * r2).diff().diff().diff()

def f03_amad_118_advance_log_x_velocity_consistency_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    cons = _safe_div(r.rolling(YDAYS, min_periods=QDAYS).mean(), r.rolling(YDAYS, min_periods=QDAYS).std())
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return (adv * cons).diff().diff().diff()

def f03_amad_119_advance_log_x_position_in_range_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    adv = _safe_log(close) - _safe_log(rmin)
    return (adv * pos).diff().diff().diff()

def f03_amad_120_advance_log_x_uptrend_days_above_sma21_252d_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    days = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return (adv * days).diff().diff().diff()

def f03_amad_121_close_to_2520d_low_log_advance_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(2520, min_periods=YDAYS * 2).min()
    return (_safe_log(close) - _safe_log(rmin)).diff().diff().diff()

def f03_amad_122_close_to_2520d_high_log_distance_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(2520, min_periods=YDAYS * 2).max()
    return (_safe_log(close) - _safe_log(rmax)).diff().diff().diff()

def f03_amad_123_close_to_5y_VWAP_log_distance_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    pv = (close * volume).rolling(1260, min_periods=YDAYS).sum()
    vv = volume.rolling(1260, min_periods=YDAYS).sum()
    return (_safe_log(close) - _safe_log(_safe_div(pv, vv))).diff().diff().diff()

def f03_amad_124_days_since_5y_high_d3(high: pd.Series) -> pd.Series:

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    return high.rolling(1260, min_periods=YDAYS).apply(_pa, raw=True).diff().diff().diff()

def f03_amad_125_days_since_5y_low_d3(low: pd.Series) -> pd.Series:

    def _ta(w):
        return float(len(w) - 1 - int(np.argmin(w)))
    return low.rolling(1260, min_periods=YDAYS).apply(_ta, raw=True).diff().diff().diff()

def f03_amad_126_days_in_top_decile_log_close_5y_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    p90 = lp.rolling(1260, min_periods=YDAYS).quantile(0.9)
    return (lp >= p90).astype(float).rolling(1260, min_periods=YDAYS).sum().diff().diff().diff()

def f03_amad_127_ratio_252d_advance_to_2520d_advance_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    r252 = _safe_log(close) - _safe_log(low.rolling(YDAYS, min_periods=QDAYS).min())
    r2520 = _safe_log(close) - _safe_log(low.rolling(2520, min_periods=YDAYS * 2).min())
    return _safe_div(r252, r2520).diff().diff().diff()

def f03_amad_128_secular_uptrend_age_score_5y_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(1260, min_periods=YDAYS).mean()
    return (close > sma).astype(float).rolling(1260, min_periods=YDAYS).sum().diff().diff().diff()

def f03_amad_129_close_position_in_5y_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(1260, min_periods=YDAYS).max()
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return ((close - rmin) / rng).diff().diff().diff()

def f03_amad_130_close_position_in_10y_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(2520, min_periods=YDAYS * 2).max()
    rmin = low.rolling(2520, min_periods=YDAYS * 2).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return ((close - rmin) / rng).diff().diff().diff()

def f03_amad_131_fraction_5y_above_SMA252_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return (close > sma).astype(float).rolling(1260, min_periods=YDAYS).mean().diff().diff().diff()

def f03_amad_132_fraction_2y_above_SMA252_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return (close > sma).astype(float).rolling(504, min_periods=YDAYS).mean().diff().diff().diff()

def f03_amad_133_long_horizon_consistency_5y_d3(close: pd.Series) -> pd.Series:
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    m = r21.rolling(1260, min_periods=YDAYS).mean()
    sd = r21.rolling(1260, min_periods=YDAYS).std()
    return _safe_div(sd, m.abs()).diff().diff().diff()

def f03_amad_134_close_to_secular_anchor_VWAP_log_2520d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    pv = (close * volume).rolling(2520, min_periods=YDAYS * 2).sum()
    vv = volume.rolling(2520, min_periods=YDAYS * 2).sum()
    return (_safe_log(close) - _safe_log(_safe_div(pv, vv))).diff().diff().diff()

def f03_amad_135_advance_completeness_index_5y_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    return _safe_div(close, high.rolling(1260, min_periods=YDAYS).max()).diff().diff().diff()

def f03_amad_136_fitted_linear_angle_log_close_252d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_slope(_safe_log(close), YDAYS) * float(YDAYS)).diff().diff().diff()

def f03_amad_137_fitted_linear_angle_log_close_1260d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_slope(_safe_log(close), 1260) * 1260.0).diff().diff().diff()

def f03_amad_138_advance_curvature_log_close_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)

    def _c2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            return float(np.polyfit(x, w, 2)[0])
        except Exception:
            return np.nan
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_c2, raw=True).diff().diff().diff()

def f03_amad_139_advance_curvature_log_close_1260d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)

    def _c2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            return float(np.polyfit(x, w, 2)[0])
        except Exception:
            return np.nan
    return lp.rolling(1260, min_periods=YDAYS).apply(_c2, raw=True).diff().diff().diff()

def f03_amad_140_R2_linear_log_close_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)

    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss = ((w - w.mean()) ** 2).sum()
        if ss == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        return 1.0 - ((w - pred) ** 2).sum() / ss
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True).diff().diff().diff()

def f03_amad_141_R2_linear_log_close_1260d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)

    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss = ((w - w.mean()) ** 2).sum()
        if ss == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        return 1.0 - ((w - pred) ** 2).sum() / ss
    return lp.rolling(1260, min_periods=YDAYS).apply(_r2, raw=True).diff().diff().diff()

def f03_amad_142_advance_shape_score_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)

    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss = ((w - w.mean()) ** 2).sum()
        if ss == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        return 1.0 - ((w - pred) ** 2).sum() / ss

    def _c2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            return float(np.polyfit(x, w, 2)[0])
        except Exception:
            return np.nan
    r2 = lp.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)
    c2 = lp.rolling(YDAYS, min_periods=QDAYS).apply(_c2, raw=True)
    return (r2 * c2.clip(lower=0)).diff().diff().diff()

def f03_amad_143_advance_acceleration_ratio_first_vs_last_thirds_log_252d_d3(close: pd.Series) -> pd.Series:
    third = 252 // 3
    lp = _safe_log(close)
    last = lp - lp.shift(YDAYS - 2 * third)
    first = lp.shift(YDAYS - third) - lp.shift(YDAYS)
    return _safe_div(last, first).diff().diff().diff()

def f03_amad_144_advance_amplitude_x_age_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = _safe_log(rmax) - _safe_log(rmin)

    def _ta(w):
        return float(len(w) - 1 - int(np.argmin(w)))
    age = low.rolling(YDAYS, min_periods=QDAYS).apply(_ta, raw=True)
    return (rng * age).diff().diff().diff()

def f03_amad_145_advance_height_above_2520d_sma_log_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(2520, min_periods=YDAYS * 2).mean()
    return (_safe_log(close) - _safe_log(sma)).diff().diff().diff()

def f03_amad_146_advance_height_above_baseline_atr_units_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    atr = _atr(high, low, close, MDAYS)
    return ((close - sma) / atr.replace(0, np.nan)).diff().diff().diff()

def f03_amad_147_advance_completeness_terminal_score_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    adv = _safe_log(close) - _safe_log(rmin)

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    return (pos * adv * (1.0 + pa / float(YDAYS))).diff().diff().diff()

def f03_amad_148_secular_top_proximity_log_2520d_d3(high: pd.Series) -> pd.Series:
    rmax = high.rolling(2520, min_periods=YDAYS * 2).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff().diff()

def f03_amad_149_secular_top_proximity_ratio_252d_to_2520d_high_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    return _safe_div(close.rolling(YDAYS, min_periods=QDAYS).max(), close.rolling(2520, min_periods=YDAYS * 2).max()).diff().diff().diff()

def f03_amad_150_advance_terminal_score_composite_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    adv = _safe_log(close) - _safe_log(rmin)
    cmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd_share = (_safe_div(close, cmax) - 1.0).abs().rolling(YDAYS, min_periods=QDAYS).mean()
    return (pos * adv * (1.0 - dd_share)).diff().diff().diff()
ADVANCE_MAGNITUDE_DURATION_D3_REGISTRY_076_150 = {'f03_amad_076_log_excess_advance_252d_vs_baseline_1260d_d3': {'inputs': ['close'], 'func': f03_amad_076_log_excess_advance_252d_vs_baseline_1260d_d3}, 'f03_amad_077_log_advance_252d_zscore_in_2520d_d3': {'inputs': ['close'], 'func': f03_amad_077_log_advance_252d_zscore_in_2520d_d3}, 'f03_amad_078_log_advance_252d_pct_rank_in_2520d_d3': {'inputs': ['close'], 'func': f03_amad_078_log_advance_252d_pct_rank_in_2520d_d3}, 'f03_amad_079_advance_horizon_ratio_252d_to_1260d_log_d3': {'inputs': ['close'], 'func': f03_amad_079_advance_horizon_ratio_252d_to_1260d_log_d3}, 'f03_amad_080_advance_horizon_ratio_63d_to_252d_log_d3': {'inputs': ['close'], 'func': f03_amad_080_advance_horizon_ratio_63d_to_252d_log_d3}, 'f03_amad_081_magnitude_horizon_slope_log_d3': {'inputs': ['close'], 'func': f03_amad_081_magnitude_horizon_slope_log_d3}, 'f03_amad_082_horizon_consistency_corr_d3': {'inputs': ['close'], 'func': f03_amad_082_horizon_consistency_corr_d3}, 'f03_amad_083_dollar_value_growth_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_083_dollar_value_growth_252d_d3}, 'f03_amad_084_cumulative_log_advance_during_uptrend_segments_252d_d3': {'inputs': ['close'], 'func': f03_amad_084_cumulative_log_advance_during_uptrend_segments_252d_d3}, 'f03_amad_085_log_advance_normalized_by_volatility_252d_d3': {'inputs': ['close'], 'func': f03_amad_085_log_advance_normalized_by_volatility_252d_d3}, 'f03_amad_086_log_advance_normalized_by_parkinson_vol_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_086_log_advance_normalized_by_parkinson_vol_252d_d3}, 'f03_amad_087_advance_per_dollar_volume_252d_d3': {'inputs': ['close', 'volume'], 'func': f03_amad_087_advance_per_dollar_volume_252d_d3}, 'f03_amad_088_volume_weighted_advance_intensity_252d_d3': {'inputs': ['close', 'volume'], 'func': f03_amad_088_volume_weighted_advance_intensity_252d_d3}, 'f03_amad_089_stairstep_advance_score_252d_d3': {'inputs': ['close', 'high'], 'func': f03_amad_089_stairstep_advance_score_252d_d3}, 'f03_amad_090_base_consolidation_count_before_advance_252d_d3': {'inputs': ['close'], 'func': f03_amad_090_base_consolidation_count_before_advance_252d_d3}, 'f03_amad_091_longest_run_above_50pct_252d_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_091_longest_run_above_50pct_252d_range_d3}, 'f03_amad_092_longest_run_above_75pct_252d_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_092_longest_run_above_75pct_252d_range_d3}, 'f03_amad_093_longest_run_above_90pct_252d_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_093_longest_run_above_90pct_252d_range_d3}, 'f03_amad_094_days_within_2pct_of_252d_high_d3': {'inputs': ['close', 'high'], 'func': f03_amad_094_days_within_2pct_of_252d_high_d3}, 'f03_amad_095_max_consecutive_higher_close_run_252d_d3': {'inputs': ['close'], 'func': f03_amad_095_max_consecutive_higher_close_run_252d_d3}, 'f03_amad_096_max_run_within_5pct_of_252d_high_252d_d3': {'inputs': ['close', 'high'], 'func': f03_amad_096_max_run_within_5pct_of_252d_high_252d_d3}, 'f03_amad_097_days_in_top_quartile_log_close_252d_d3': {'inputs': ['close'], 'func': f03_amad_097_days_in_top_quartile_log_close_252d_d3}, 'f03_amad_098_mean_days_per_uptrend_leg_252d_d3': {'inputs': ['close'], 'func': f03_amad_098_mean_days_per_uptrend_leg_252d_d3}, 'f03_amad_099_advance_resilience_252d_d3': {'inputs': ['close'], 'func': f03_amad_099_advance_resilience_252d_d3}, 'f03_amad_100_total_continuous_holding_time_above_50pct_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_100_total_continuous_holding_time_above_50pct_252d_d3}, 'f03_amad_101_days_close_within_1pct_of_252d_max_d3': {'inputs': ['close'], 'func': f03_amad_101_days_close_within_1pct_of_252d_max_d3}, 'f03_amad_102_share_252d_in_advance_phase_d3': {'inputs': ['close'], 'func': f03_amad_102_share_252d_in_advance_phase_d3}, 'f03_amad_103_share_252d_in_distribution_phase_d3': {'inputs': ['close', 'high'], 'func': f03_amad_103_share_252d_in_distribution_phase_d3}, 'f03_amad_104_retracement_count_during_advance_252d_d3': {'inputs': ['close'], 'func': f03_amad_104_retracement_count_during_advance_252d_d3}, 'f03_amad_105_mean_retracement_size_during_advance_252d_d3': {'inputs': ['close'], 'func': f03_amad_105_mean_retracement_size_during_advance_252d_d3}, 'f03_amad_106_advance_log_x_age_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_106_advance_log_x_age_252d_d3}, 'f03_amad_107_advance_log_x_days_above_sma252_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_107_advance_log_x_days_above_sma252_252d_d3}, 'f03_amad_108_advance_log_x_run_above_sma63_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_108_advance_log_x_run_above_sma63_252d_d3}, 'f03_amad_109_effective_advance_score_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_109_effective_advance_score_252d_d3}, 'f03_amad_110_sustained_advance_strength_252d_d3': {'inputs': ['close'], 'func': f03_amad_110_sustained_advance_strength_252d_d3}, 'f03_amad_111_advance_x_no_pullback_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_111_advance_x_no_pullback_252d_d3}, 'f03_amad_112_magnitude_per_new_high_touch_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_112_magnitude_per_new_high_touch_252d_d3}, 'f03_amad_113_duration_weighted_log_advance_252d_d3': {'inputs': ['close'], 'func': f03_amad_113_duration_weighted_log_advance_252d_d3}, 'f03_amad_114_mature_outsized_advance_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_114_mature_outsized_advance_252d_d3}, 'f03_amad_115_fresh_outsized_advance_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_115_fresh_outsized_advance_252d_d3}, 'f03_amad_116_advance_log_x_sma_stacking_days_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_116_advance_log_x_sma_stacking_days_252d_d3}, 'f03_amad_117_advance_log_x_R2_close_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_117_advance_log_x_R2_close_252d_d3}, 'f03_amad_118_advance_log_x_velocity_consistency_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_118_advance_log_x_velocity_consistency_252d_d3}, 'f03_amad_119_advance_log_x_position_in_range_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_119_advance_log_x_position_in_range_252d_d3}, 'f03_amad_120_advance_log_x_uptrend_days_above_sma21_252d_d3': {'inputs': ['close', 'low'], 'func': f03_amad_120_advance_log_x_uptrend_days_above_sma21_252d_d3}, 'f03_amad_121_close_to_2520d_low_log_advance_d3': {'inputs': ['close', 'low'], 'func': f03_amad_121_close_to_2520d_low_log_advance_d3}, 'f03_amad_122_close_to_2520d_high_log_distance_d3': {'inputs': ['close', 'high'], 'func': f03_amad_122_close_to_2520d_high_log_distance_d3}, 'f03_amad_123_close_to_5y_VWAP_log_distance_d3': {'inputs': ['close', 'volume'], 'func': f03_amad_123_close_to_5y_VWAP_log_distance_d3}, 'f03_amad_124_days_since_5y_high_d3': {'inputs': ['high'], 'func': f03_amad_124_days_since_5y_high_d3}, 'f03_amad_125_days_since_5y_low_d3': {'inputs': ['low'], 'func': f03_amad_125_days_since_5y_low_d3}, 'f03_amad_126_days_in_top_decile_log_close_5y_d3': {'inputs': ['close'], 'func': f03_amad_126_days_in_top_decile_log_close_5y_d3}, 'f03_amad_127_ratio_252d_advance_to_2520d_advance_d3': {'inputs': ['close', 'low'], 'func': f03_amad_127_ratio_252d_advance_to_2520d_advance_d3}, 'f03_amad_128_secular_uptrend_age_score_5y_d3': {'inputs': ['close'], 'func': f03_amad_128_secular_uptrend_age_score_5y_d3}, 'f03_amad_129_close_position_in_5y_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_129_close_position_in_5y_range_d3}, 'f03_amad_130_close_position_in_10y_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_130_close_position_in_10y_range_d3}, 'f03_amad_131_fraction_5y_above_SMA252_d3': {'inputs': ['close'], 'func': f03_amad_131_fraction_5y_above_SMA252_d3}, 'f03_amad_132_fraction_2y_above_SMA252_d3': {'inputs': ['close'], 'func': f03_amad_132_fraction_2y_above_SMA252_d3}, 'f03_amad_133_long_horizon_consistency_5y_d3': {'inputs': ['close'], 'func': f03_amad_133_long_horizon_consistency_5y_d3}, 'f03_amad_134_close_to_secular_anchor_VWAP_log_2520d_d3': {'inputs': ['close', 'volume'], 'func': f03_amad_134_close_to_secular_anchor_VWAP_log_2520d_d3}, 'f03_amad_135_advance_completeness_index_5y_d3': {'inputs': ['close', 'high'], 'func': f03_amad_135_advance_completeness_index_5y_d3}, 'f03_amad_136_fitted_linear_angle_log_close_252d_d3': {'inputs': ['close'], 'func': f03_amad_136_fitted_linear_angle_log_close_252d_d3}, 'f03_amad_137_fitted_linear_angle_log_close_1260d_d3': {'inputs': ['close'], 'func': f03_amad_137_fitted_linear_angle_log_close_1260d_d3}, 'f03_amad_138_advance_curvature_log_close_252d_d3': {'inputs': ['close'], 'func': f03_amad_138_advance_curvature_log_close_252d_d3}, 'f03_amad_139_advance_curvature_log_close_1260d_d3': {'inputs': ['close'], 'func': f03_amad_139_advance_curvature_log_close_1260d_d3}, 'f03_amad_140_R2_linear_log_close_252d_d3': {'inputs': ['close'], 'func': f03_amad_140_R2_linear_log_close_252d_d3}, 'f03_amad_141_R2_linear_log_close_1260d_d3': {'inputs': ['close'], 'func': f03_amad_141_R2_linear_log_close_1260d_d3}, 'f03_amad_142_advance_shape_score_252d_d3': {'inputs': ['close'], 'func': f03_amad_142_advance_shape_score_252d_d3}, 'f03_amad_143_advance_acceleration_ratio_first_vs_last_thirds_log_252d_d3': {'inputs': ['close'], 'func': f03_amad_143_advance_acceleration_ratio_first_vs_last_thirds_log_252d_d3}, 'f03_amad_144_advance_amplitude_x_age_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_144_advance_amplitude_x_age_252d_d3}, 'f03_amad_145_advance_height_above_2520d_sma_log_d3': {'inputs': ['close'], 'func': f03_amad_145_advance_height_above_2520d_sma_log_d3}, 'f03_amad_146_advance_height_above_baseline_atr_units_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_146_advance_height_above_baseline_atr_units_252d_d3}, 'f03_amad_147_advance_completeness_terminal_score_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_147_advance_completeness_terminal_score_d3}, 'f03_amad_148_secular_top_proximity_log_2520d_d3': {'inputs': ['high'], 'func': f03_amad_148_secular_top_proximity_log_2520d_d3}, 'f03_amad_149_secular_top_proximity_ratio_252d_to_2520d_high_d3': {'inputs': ['close', 'high'], 'func': f03_amad_149_secular_top_proximity_ratio_252d_to_2520d_high_d3}, 'f03_amad_150_advance_terminal_score_composite_d3': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_150_advance_terminal_score_composite_d3}}
