"""rsi_exhaustion_family d3 features 076-150 — Pipeline 1b-technical.

Continuation of the 150-hypothesis family.
Bucket J: Smoothed / transformed RSI variants.
Bucket K: RSI level deviation / robust stats.
Bucket L: Multi-horizon RSI consensus / stacking.
Bucket M: RSI extreme-events recency / clusters.
Bucket N: Cutler / SMA-based RSI dynamics.
Bucket O: Connors-style PercentRank RSI variants.
Bucket P: Composite RSI-exhaustion measures.
Bucket Q: Final composite exhaustion-trigger features.

Inputs: SEP close (+ high for divergence-based features). Self-contained helpers,
PIT-clean.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

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


def _rsi_wilder(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)


def _rsi_cutler(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.rolling(n, min_periods=max(n // 3, 2)).mean()
    ad = dn.rolling(n, min_periods=max(n // 3, 2)).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)


def _percent_rank_return(close, n_ret=1, n_window=100):
    r = close.pct_change(n_ret)
    return r.rolling(n_window, min_periods=max(n_window // 3, 5)).rank(pct=True) * 100.0


# ============================================================
# Bucket J — Smoothed / transformed RSI variants (076-084)
# ============================================================


def f25_rsxh_076_fisher_transform_rsi_d3(close: pd.Series) -> pd.Series:
    """Fisher transform of normalized RSI(14): 0.5 ln((1+x)/(1-x)) with x=(RSI-50)/50, clipped."""
    r = _rsi_wilder(close, 14)
    x = ((r - 50.0) / 50.0).clip(-0.999, 0.999)
    return (0.5 * np.log((1 + x) / (1 - x))).diff().diff().diff()


def f25_rsxh_077_fisher_transform_rsi_smoothed_5_d3(close: pd.Series) -> pd.Series:
    """Fisher transform of EMA5-smoothed RSI(14) — smoothed Fisher of RSI."""
    r = _rsi_wilder(close, 14)
    rs = r.ewm(span=5, adjust=False, min_periods=5).mean()
    x = ((rs - 50.0) / 50.0).clip(-0.999, 0.999)
    return (0.5 * np.log((1 + x) / (1 - x))).diff().diff().diff()


def f25_rsxh_078_rsi14_sma5_d3(close: pd.Series) -> pd.Series:
    """5-bar SMA of RSI(14) — short-term smoothed RSI."""
    return (_rsi_wilder(close, 14).rolling(5, min_periods=2).mean()).diff().diff().diff()


def f25_rsxh_079_rsi14_ema21_d3(close: pd.Series) -> pd.Series:
    """21-bar EMA of RSI(14) — monthly-smoothed RSI."""
    return (_rsi_wilder(close, 14).ewm(span=MDAYS, adjust=False, min_periods=MDAYS).mean()).diff().diff().diff()


def f25_rsxh_080_rsi14_ema63_d3(close: pd.Series) -> pd.Series:
    """63-bar EMA of RSI(14) — quarterly-smoothed RSI."""
    return (_rsi_wilder(close, 14).ewm(span=QDAYS, adjust=False, min_periods=QDAYS).mean()).diff().diff().diff()


def f25_rsxh_081_rsi14_first_diff_d3(close: pd.Series) -> pd.Series:
    """RSI(14) gradient: RSI(t) - RSI(t-1) — single-bar RSI change."""
    return (_rsi_wilder(close, 14).diff()).diff().diff().diff()


def f25_rsxh_082_rsi14_second_diff_d3(close: pd.Series) -> pd.Series:
    """RSI(14) second difference — RSI acceleration."""
    return (_rsi_wilder(close, 14).diff().diff()).diff().diff().diff()


def f25_rsxh_083_rsi14_minus_sma21_of_self_d3(close: pd.Series) -> pd.Series:
    """RSI(14) minus its 21d SMA — distance of current RSI above its own monthly mean."""
    r = _rsi_wilder(close, 14)
    return (r - r.rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff().diff()


def f25_rsxh_084_rsi14_minus_sma63_of_self_d3(close: pd.Series) -> pd.Series:
    """RSI(14) minus its 63d SMA — distance from quarterly mean."""
    r = _rsi_wilder(close, 14)
    return (r - r.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()


def f25_rsxh_085_rsi14_deviation_from_50_d3(close: pd.Series) -> pd.Series:
    """RSI(14) - 50 — signed deviation from neutral."""
    return (_rsi_wilder(close, 14) - 50.0).diff().diff().diff()


def f25_rsxh_086_rsi14_abs_deviation_from_50_d3(close: pd.Series) -> pd.Series:
    """|RSI(14) - 50| — magnitude of deviation from neutral."""
    return ((_rsi_wilder(close, 14) - 50.0).abs()).diff().diff().diff()


def f25_rsxh_087_rsi14_pct_rank_63_d3(close: pd.Series) -> pd.Series:
    """RSI(14) percentile rank vs trailing 63d distribution."""
    return (_rsi_wilder(close, 14).rolling(QDAYS, min_periods=MDAYS).rank(pct=True)).diff().diff().diff()


def f25_rsxh_088_rsi14_pct_rank_252_d3(close: pd.Series) -> pd.Series:
    """RSI(14) percentile rank vs trailing 252d distribution."""
    return (_rsi_wilder(close, 14).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f25_rsxh_089_rsi14_zscore_63_d3(close: pd.Series) -> pd.Series:
    """Z-score of RSI(14) vs trailing 63d."""
    return (_rolling_zscore(_rsi_wilder(close, 14), QDAYS, min_periods=MDAYS)).diff().diff().diff()


def f25_rsxh_090_rsi14_zscore_252_d3(close: pd.Series) -> pd.Series:
    """Z-score of RSI(14) vs trailing 252d."""
    return (_rolling_zscore(_rsi_wilder(close, 14), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f25_rsxh_091_rsi14_rolling_q90_63_d3(close: pd.Series) -> pd.Series:
    """Trailing 63d 90th percentile of RSI(14) — own quarterly upper-band level."""
    return (_rsi_wilder(close, 14).rolling(QDAYS, min_periods=MDAYS).quantile(0.90)).diff().diff().diff()


def f25_rsxh_092_rsi14_rolling_q95_252_d3(close: pd.Series) -> pd.Series:
    """Trailing 252d 95th percentile of RSI(14) — own annual upper-band level."""
    return (_rsi_wilder(close, 14).rolling(YDAYS, min_periods=QDAYS).quantile(0.95)).diff().diff().diff()


def f25_rsxh_093_rsi14_skew_252_d3(close: pd.Series) -> pd.Series:
    """Skewness of RSI(14) distribution past 252 — asymmetry of momentum regime."""
    return (_rsi_wilder(close, 14).rolling(YDAYS, min_periods=QDAYS).skew()).diff().diff().diff()


def f25_rsxh_094_rsi7_minus_rsi21_d3(close: pd.Series) -> pd.Series:
    """RSI(7) - RSI(21) — short-vs-monthly RSI divergence."""
    return (_rsi_wilder(close, 7) - _rsi_wilder(close, MDAYS)).diff().diff().diff()


def f25_rsxh_095_rsi21_minus_rsi63_d3(close: pd.Series) -> pd.Series:
    """RSI(21) - RSI(63) — monthly-vs-quarterly RSI divergence."""
    return (_rsi_wilder(close, MDAYS) - _rsi_wilder(close, QDAYS)).diff().diff().diff()


def f25_rsxh_096_rsi63_minus_rsi252_d3(close: pd.Series) -> pd.Series:
    """RSI(63) - RSI(252) — quarterly-vs-annual RSI divergence."""
    return (_rsi_wilder(close, QDAYS) - _rsi_wilder(close, YDAYS)).diff().diff().diff()


def f25_rsxh_097_count_all_horizons_ob70_d3(close: pd.Series) -> pd.Series:
    """Count of horizons {7, 14, 21, 63} with RSI > 70 — multi-horizon OB consensus."""
    a = (_rsi_wilder(close, 7) > 70.0).astype(float)
    b = (_rsi_wilder(close, 14) > 70.0).astype(float)
    c = (_rsi_wilder(close, MDAYS) > 70.0).astype(float)
    d = (_rsi_wilder(close, QDAYS) > 70.0).astype(float)
    return (a.fillna(0) + b.fillna(0) + c.fillna(0) + d.fillna(0)).diff().diff().diff()


def f25_rsxh_098_count_horizons_extreme_ob80_d3(close: pd.Series) -> pd.Series:
    """Count of horizons {14, 63, 252} with RSI > 80 — extreme multi-horizon OB."""
    a = (_rsi_wilder(close, 14) > 80.0).astype(float)
    b = (_rsi_wilder(close, QDAYS) > 80.0).astype(float)
    c = (_rsi_wilder(close, YDAYS) > 80.0).astype(float)
    return (a.fillna(0) + b.fillna(0) + c.fillna(0)).diff().diff().diff()


def f25_rsxh_099_count_horizons_below_50_d3(close: pd.Series) -> pd.Series:
    """Count of horizons {7, 14, 21, 63} with RSI < 50 — bearish-bias consensus."""
    a = (_rsi_wilder(close, 7) < 50.0).astype(float)
    b = (_rsi_wilder(close, 14) < 50.0).astype(float)
    c = (_rsi_wilder(close, MDAYS) < 50.0).astype(float)
    d = (_rsi_wilder(close, QDAYS) < 50.0).astype(float)
    return (a.fillna(0) + b.fillna(0) + c.fillna(0) + d.fillna(0)).diff().diff().diff()


def f25_rsxh_100_rsi14_and_rsi63_both_ob_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 70 AND RSI(63) > 70 — short + medium OB confirmed."""
    a = _rsi_wilder(close, 14)
    b = _rsi_wilder(close, QDAYS)
    return (((a > 70.0) & (b > 70.0)).astype(float).where(a.notna() & b.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_101_rsi_stack_bullish_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > RSI(63) > RSI(252) — bullish-momentum stack."""
    a = _rsi_wilder(close, 14)
    b = _rsi_wilder(close, QDAYS)
    c = _rsi_wilder(close, YDAYS)
    return (((a > b) & (b > c)).astype(float).where(a.notna() & b.notna() & c.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_102_rsi_stack_bearish_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(14) < RSI(63) < RSI(252) — cooling-across-horizons stack."""
    a = _rsi_wilder(close, 14)
    b = _rsi_wilder(close, QDAYS)
    c = _rsi_wilder(close, YDAYS)
    return (((a < b) & (b < c)).astype(float).where(a.notna() & b.notna() & c.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_103_bars_since_rsi14_above_95_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent RSI(14) > 95 event — recency of extreme OB."""
    r = _rsi_wilder(close, 14)
    return (_bars_since_true(r > 95.0)).diff().diff().diff()


def f25_rsxh_104_bars_since_rsi14_below_5_d3(close: pd.Series) -> pd.Series:
    """Bars since RSI(14) < 5 event — recency of extreme OS (for symmetry context)."""
    r = _rsi_wilder(close, 14)
    return (_bars_since_true(r < 5.0)).diff().diff().diff()


def f25_rsxh_105_count_rsi_above_80_events_252_d3(close: pd.Series) -> pd.Series:
    """Count of RSI(14) > 80 'entry' events past 252 — count of strong-OB entries."""
    r = _rsi_wilder(close, 14)
    ev = ((r.shift(1) <= 80.0) & (r > 80.0)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_106_count_rsi_below_20_events_252_d3(close: pd.Series) -> pd.Series:
    """Count of RSI(14) < 20 'entry' events past 252 — count of OS entries."""
    r = _rsi_wilder(close, 14)
    ev = ((r.shift(1) >= 20.0) & (r < 20.0)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_107_rsi_ob_exit_cluster_3_in_21_d3(close: pd.Series) -> pd.Series:
    """1 if 3+ RSI OB70-exit events in past 21 bars — cluster signal."""
    r = _rsi_wilder(close, 14)
    ev = ((r.shift(1) > 70.0) & (r <= 70.0)).astype(float)
    cnt = ev.rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 3).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_108_days_at_252d_rsi_max_d3(close: pd.Series) -> pd.Series:
    """Count of bars in past 21 where RSI(14) equals its trailing 252d max — saturation dwell."""
    r = _rsi_wilder(close, 14)
    rmax = r.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = (r == rmax).astype(float)
    return (at_max.rolling(MDAYS, min_periods=WDAYS).sum().where(rmax.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_109_bars_since_rsi14_504d_max_d3(close: pd.Series) -> pd.Series:
    """Bars since RSI(14) reached its trailing 504d (2y) max."""
    r = _rsi_wilder(close, 14)
    at_max = r == r.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return (_bars_since_true(at_max)).diff().diff().diff()


def f25_rsxh_110_longest_streak_below_30_d3(close: pd.Series) -> pd.Series:
    """Longest consecutive run of RSI(14) < 30 in past 252 — sustained-OS regime measure."""
    r = _rsi_wilder(close, 14)
    s = _streak_true(r < 30.0)
    return (s.rolling(YDAYS, min_periods=QDAYS).max().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_111_stuck_above_70_10bar_episodes_252_d3(close: pd.Series) -> pd.Series:
    """Count of distinct OB70 episodes in past 252 that lasted 10+ bars — major-OB count."""
    r = _rsi_wilder(close, 14)
    in_ob = (r > 70.0)
    # mark exit bars where prior OB-streak >= 10
    streak = _streak_true(in_ob)
    exits_with_len = ((r.shift(1) > 70.0) & (r <= 70.0) & (streak.shift(1) >= 10)).astype(float)
    return (exits_with_len.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_112_cutler_minus_wilder_rsi14_d3(close: pd.Series) -> pd.Series:
    """Cutler RSI(14) - Wilder RSI(14) — smoothing-method gap."""
    return (_rsi_cutler(close, 14) - _rsi_wilder(close, 14)).diff().diff().diff()


def f25_rsxh_113_cutler_rsi14_above_70_state_d3(close: pd.Series) -> pd.Series:
    """1 if Cutler RSI(14) > 70 — SMA-based OB state."""
    c = _rsi_cutler(close, 14)
    return ((c > 70.0).astype(float).where(c.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_114_cutler_rsi63_above_70_state_d3(close: pd.Series) -> pd.Series:
    """1 if Cutler RSI(63) > 70 — SMA-based quarterly OB."""
    c = _rsi_cutler(close, QDAYS)
    return ((c > 70.0).astype(float).where(c.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_115_cutler_rsi_bearish_div_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using Cutler RSI (SMA-based) over 63d."""
    c = _rsi_cutler(close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    c_below = c < c.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & c_below).astype(float).where(c.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_116_cutler_rsi_peak_decay_63_d3(close: pd.Series) -> pd.Series:
    """63d max of Cutler RSI minus its value 63 bars ago — Cutler peak decay."""
    c = _rsi_cutler(close, 14)
    pmax = c.rolling(QDAYS, min_periods=MDAYS).max()
    return (pmax - pmax.shift(QDAYS)).diff().diff().diff()


def f25_rsxh_117_sma_ema_rsi_cross_event_d3(close: pd.Series) -> pd.Series:
    """1 if Cutler RSI(14) crosses below Wilder RSI(14) this bar — SMA-faster-than-EMA cooling."""
    diff = _rsi_cutler(close, 14) - _rsi_wilder(close, 14)
    return (((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_118_cutler_rsi_just_exited_ob70_d3(close: pd.Series) -> pd.Series:
    """Cutler RSI(14) OB70-exit trigger."""
    c = _rsi_cutler(close, 14)
    return (((c.shift(1) > 70.0) & (c <= 70.0)).astype(float).where(c.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_119_cutler_rsi_dwell_ob70_63_d3(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars Cutler RSI(14) > 70 — SMA-RSI OB dwell."""
    c = _rsi_cutler(close, 14)
    return ((c > 70.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_120_cutler_rsi_zscore_252_d3(close: pd.Series) -> pd.Series:
    """Z-score of Cutler RSI(14) vs trailing 252d."""
    return (_rolling_zscore(_rsi_cutler(close, 14), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f25_rsxh_121_percent_rank_return_1_over_50_d3(close: pd.Series) -> pd.Series:
    """PercentRank of 1-bar return over 50 bars — short-window Connors percentrank."""
    return (_percent_rank_return(close, 1, 50)).diff().diff().diff()


def f25_rsxh_122_percent_rank_return_5_over_100_d3(close: pd.Series) -> pd.Series:
    """PercentRank of 5-bar return over 100 bars — weekly-return rank."""
    return (_percent_rank_return(close, 5, 100)).diff().diff().diff()


def f25_rsxh_123_percent_rank_return_21_over_252_d3(close: pd.Series) -> pd.Series:
    """PercentRank of 21-bar return over 252 bars — monthly-return rank."""
    return (_percent_rank_return(close, MDAYS, YDAYS)).diff().diff().diff()


def f25_rsxh_124_percent_rank_above_90_state_d3(close: pd.Series) -> pd.Series:
    """1 if PercentRank(1, 100) > 90 — Connors-strategy OB."""
    p = _percent_rank_return(close, 1, 100)
    return ((p > 90.0).astype(float).where(p.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_125_percent_rank_above_95_extreme_d3(close: pd.Series) -> pd.Series:
    """1 if PercentRank(1, 100) > 95 — extreme Connors-OB."""
    p = _percent_rank_return(close, 1, 100)
    return ((p > 95.0).astype(float).where(p.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_126_bars_since_percent_rank_above_90_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent PercentRank > 90 event."""
    p = _percent_rank_return(close, 1, 100)
    return (_bars_since_true(p > 90.0)).diff().diff().diff()


def f25_rsxh_127_percent_rank_above_90_count_63_d3(close: pd.Series) -> pd.Series:
    """Count of PercentRank > 90 events past 63."""
    p = _percent_rank_return(close, 1, 100)
    return ((p > 90.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(p.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_128_rsi_2_connors_d3(close: pd.Series) -> pd.Series:
    """Wilder RSI(2) — Connors's 2-period RSI mean-reversion oscillator."""
    return (_rsi_wilder(close, 2)).diff().diff().diff()


def f25_rsxh_129_rsi_2_above_90_state_d3(close: pd.Series) -> pd.Series:
    """1 if RSI(2) > 90 — Connors-strategy extreme-OB entry rule."""
    r = _rsi_wilder(close, 2)
    return ((r > 90.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_130_rsi_price_corr_252_d3(close: pd.Series) -> pd.Series:
    """Rolling 252d correlation(RSI(14), close) — annual decoupling indicator."""
    r = _rsi_wilder(close, 14)
    return (close.rolling(YDAYS, min_periods=QDAYS).corr(r)).diff().diff().diff()


def f25_rsxh_131_rsi_vs_price_slope_disagree_63_d3(close: pd.Series) -> pd.Series:
    """Sign(slope(close, 63)) - sign(slope(RSI(14), 63)) — quarterly RSI/price disagreement."""
    pslope = _rolling_slope(close, QDAYS)
    rslope = _rolling_slope(_rsi_wilder(close, 14), QDAYS)
    return (np.sign(pslope) - np.sign(rslope)).diff().diff().diff()


def f25_rsxh_132_rsi_ob_area_63_d3(close: pd.Series) -> pd.Series:
    """Sum of (RSI - 70) over OB bars past 63 — quarterly OB-area saturation."""
    r = _rsi_wilder(close, 14)
    area = (r - 70.0).clip(lower=0).where(r.notna(), np.nan)
    return (area.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


def f25_rsxh_133_rsi_normalized_momentum_mean_21_d3(close: pd.Series) -> pd.Series:
    """Mean of (RSI - 50)/50 past 21 — normalized-momentum monthly bias."""
    r = _rsi_wilder(close, 14)
    nm = (r - 50.0) / 50.0
    return (nm.rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff().diff()


def f25_rsxh_134_rsi_normalized_momentum_mean_63_d3(close: pd.Series) -> pd.Series:
    """Mean of (RSI - 50)/50 past 63 — quarterly bias."""
    r = _rsi_wilder(close, 14)
    nm = (r - 50.0) / 50.0
    return (nm.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()


def f25_rsxh_135_rsi_normalized_momentum_mean_252_d3(close: pd.Series) -> pd.Series:
    """Mean of (RSI - 50)/50 past 252 — annual bias."""
    r = _rsi_wilder(close, 14)
    nm = (r - 50.0) / 50.0
    return (nm.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f25_rsxh_136_rsi_entropy_5bin_252_d3(close: pd.Series) -> pd.Series:
    """Normalized Shannon entropy of RSI distribution past 252 (5 bins)."""
    def _ent(w):
        arr = w[~np.isnan(w)]
        if arr.size < 30: return np.nan
        hist, _ = np.histogram(arr, bins=[0, 20, 40, 60, 80, 100])
        s = hist.sum()
        if s == 0: return (np.nan).diff().diff().diff()
        p = hist / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(5))
    return _rsi_wilder(close, 14).rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f25_rsxh_137_rsi_kurt_252_d3(close: pd.Series) -> pd.Series:
    """Kurtosis of RSI(14) distribution past 252 — tail-shape of RSI regime."""
    return (_rsi_wilder(close, 14).rolling(YDAYS, min_periods=QDAYS).kurt()).diff().diff().diff()


def f25_rsxh_138_mean_rsi_at_new_252d_high_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean RSI(14) on past 63 bars that were new 252d highs — RSI level at fresh tops."""
    r = _rsi_wilder(close, 14)
    new_high = (high >= high.rolling(YDAYS, min_periods=QDAYS).max())
    r_at_high = r.where(new_high, np.nan)
    return (r_at_high.rolling(QDAYS, min_periods=WDAYS).mean()).diff().diff().diff()


def f25_rsxh_139_rsi_above_70_at_new_high_count_252_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in past 252 that were new 252d highs AND had RSI > 70 — confirmed-OB-at-top count."""
    r = _rsi_wilder(close, 14)
    new_high = (high >= high.rolling(YDAYS, min_periods=QDAYS).max())
    ev = (new_high & (r > 70.0)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_140_rsi_below_70_at_new_high_count_252_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars that were new 252d highs AND had RSI <= 70 — unconfirmed-tops count (bearish)."""
    r = _rsi_wilder(close, 14)
    new_high = (high >= high.rolling(YDAYS, min_periods=QDAYS).max())
    ev = (new_high & (r <= 70.0)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_141_composite_exhaustion_flag_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RSI > 80 AND RSI just exited OB70 within past 5 bars AND a bearish-div fired in past 21 — full exhaustion."""
    r = _rsi_wilder(close, 14)
    ob80 = (r > 80.0)
    exit_ob = (r.shift(1) > 70.0) & (r <= 70.0)
    exit_recent = exit_ob.rolling(WDAYS, min_periods=1).sum() > 0
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    div = (p_new & (r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max())).astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    return ((ob80 & exit_recent & div).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_142_composite_exhaustion_count_63_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of composite-exhaustion-flag bars in past 63."""
    r = _rsi_wilder(close, 14)
    ob80 = (r > 80.0)
    exit_ob = (r.shift(1) > 70.0) & (r <= 70.0)
    exit_recent = exit_ob.rolling(WDAYS, min_periods=1).sum() > 0
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    div = (p_new & (r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max())).astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    flag = (ob80 & exit_recent & div).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_143_composite_exhaustion_count_252_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of composite-exhaustion-flag bars."""
    r = _rsi_wilder(close, 14)
    ob80 = (r > 80.0)
    exit_ob = (r.shift(1) > 70.0) & (r <= 70.0)
    exit_recent = exit_ob.rolling(WDAYS, min_periods=1).sum() > 0
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    div = (p_new & (r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max())).astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    flag = (ob80 & exit_recent & div).astype(float)
    return (flag.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_144_count_lower_ob_peaks_63_d3(close: pd.Series) -> pd.Series:
    """Count of OB70-exit events past 63 where the RSI peak before exit was lower than the prior 63d RSI max."""
    r = _rsi_wilder(close, 14)
    rmax_prev = r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    just_exited = (r.shift(1) > 70.0) & (r <= 70.0)
    lh = (r.shift(1) < rmax_prev) & just_exited
    return (lh.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_145_count_lower_ob_peaks_252_d3(close: pd.Series) -> pd.Series:
    """Annual count of OB-exit events with lower-than-prior 252d RSI peak."""
    r = _rsi_wilder(close, 14)
    rmax_prev = r.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    just_exited = (r.shift(1) > 70.0) & (r <= 70.0)
    lh = (r.shift(1) < rmax_prev) & just_exited
    return (lh.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_146_rsi_top_tercile_frac_252_d3(close: pd.Series) -> pd.Series:
    """Annual fraction of bars with RSI(14) > 70 — top-tercile dwell at multi-year scale."""
    r = _rsi_wilder(close, 14)
    return ((r > 70.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_147_rsi_bottom_tercile_frac_252_d3(close: pd.Series) -> pd.Series:
    """Annual fraction of bars with RSI(14) < 30 — bottom-tercile dwell."""
    r = _rsi_wilder(close, 14)
    return ((r < 30.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f25_rsxh_148_rsi_median_252_d3(close: pd.Series) -> pd.Series:
    """Median RSI(14) past 252 — annual momentum-regime indicator."""
    return (_rsi_wilder(close, 14).rolling(YDAYS, min_periods=QDAYS).median()).diff().diff().diff()


def f25_rsxh_149_rsi_minus_q95_self_252_d3(close: pd.Series) -> pd.Series:
    """RSI(14) - its trailing 252d 95th-pct — current RSI gap above own annual upper-band."""
    r = _rsi_wilder(close, 14)
    q = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return (r - q).diff().diff().diff()


def f25_rsxh_150_cum_rsi_deviation_from_50_252_d3(close: pd.Series) -> pd.Series:
    """Sum of (RSI - 50) over past 252 — net annual deviation from neutral (cumulative bias)."""
    return ((_rsi_wilder(close, 14) - 50.0).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


# ============================================================
#                         REGISTRY 076-150 (d3)
# ============================================================

_HC = ["high", "close"]

RSI_EXHAUSTION_FAMILY_D3_REGISTRY_076_150 = {
    "f25_rsxh_076_fisher_transform_rsi_d3": {"inputs": ["close"], "func": f25_rsxh_076_fisher_transform_rsi_d3},
    "f25_rsxh_077_fisher_transform_rsi_smoothed_5_d3": {"inputs": ["close"], "func": f25_rsxh_077_fisher_transform_rsi_smoothed_5_d3},
    "f25_rsxh_078_rsi14_sma5_d3": {"inputs": ["close"], "func": f25_rsxh_078_rsi14_sma5_d3},
    "f25_rsxh_079_rsi14_ema21_d3": {"inputs": ["close"], "func": f25_rsxh_079_rsi14_ema21_d3},
    "f25_rsxh_080_rsi14_ema63_d3": {"inputs": ["close"], "func": f25_rsxh_080_rsi14_ema63_d3},
    "f25_rsxh_081_rsi14_first_diff_d3": {"inputs": ["close"], "func": f25_rsxh_081_rsi14_first_diff_d3},
    "f25_rsxh_082_rsi14_second_diff_d3": {"inputs": ["close"], "func": f25_rsxh_082_rsi14_second_diff_d3},
    "f25_rsxh_083_rsi14_minus_sma21_of_self_d3": {"inputs": ["close"], "func": f25_rsxh_083_rsi14_minus_sma21_of_self_d3},
    "f25_rsxh_084_rsi14_minus_sma63_of_self_d3": {"inputs": ["close"], "func": f25_rsxh_084_rsi14_minus_sma63_of_self_d3},
    "f25_rsxh_085_rsi14_deviation_from_50_d3": {"inputs": ["close"], "func": f25_rsxh_085_rsi14_deviation_from_50_d3},
    "f25_rsxh_086_rsi14_abs_deviation_from_50_d3": {"inputs": ["close"], "func": f25_rsxh_086_rsi14_abs_deviation_from_50_d3},
    "f25_rsxh_087_rsi14_pct_rank_63_d3": {"inputs": ["close"], "func": f25_rsxh_087_rsi14_pct_rank_63_d3},
    "f25_rsxh_088_rsi14_pct_rank_252_d3": {"inputs": ["close"], "func": f25_rsxh_088_rsi14_pct_rank_252_d3},
    "f25_rsxh_089_rsi14_zscore_63_d3": {"inputs": ["close"], "func": f25_rsxh_089_rsi14_zscore_63_d3},
    "f25_rsxh_090_rsi14_zscore_252_d3": {"inputs": ["close"], "func": f25_rsxh_090_rsi14_zscore_252_d3},
    "f25_rsxh_091_rsi14_rolling_q90_63_d3": {"inputs": ["close"], "func": f25_rsxh_091_rsi14_rolling_q90_63_d3},
    "f25_rsxh_092_rsi14_rolling_q95_252_d3": {"inputs": ["close"], "func": f25_rsxh_092_rsi14_rolling_q95_252_d3},
    "f25_rsxh_093_rsi14_skew_252_d3": {"inputs": ["close"], "func": f25_rsxh_093_rsi14_skew_252_d3},
    "f25_rsxh_094_rsi7_minus_rsi21_d3": {"inputs": ["close"], "func": f25_rsxh_094_rsi7_minus_rsi21_d3},
    "f25_rsxh_095_rsi21_minus_rsi63_d3": {"inputs": ["close"], "func": f25_rsxh_095_rsi21_minus_rsi63_d3},
    "f25_rsxh_096_rsi63_minus_rsi252_d3": {"inputs": ["close"], "func": f25_rsxh_096_rsi63_minus_rsi252_d3},
    "f25_rsxh_097_count_all_horizons_ob70_d3": {"inputs": ["close"], "func": f25_rsxh_097_count_all_horizons_ob70_d3},
    "f25_rsxh_098_count_horizons_extreme_ob80_d3": {"inputs": ["close"], "func": f25_rsxh_098_count_horizons_extreme_ob80_d3},
    "f25_rsxh_099_count_horizons_below_50_d3": {"inputs": ["close"], "func": f25_rsxh_099_count_horizons_below_50_d3},
    "f25_rsxh_100_rsi14_and_rsi63_both_ob_d3": {"inputs": ["close"], "func": f25_rsxh_100_rsi14_and_rsi63_both_ob_d3},
    "f25_rsxh_101_rsi_stack_bullish_d3": {"inputs": ["close"], "func": f25_rsxh_101_rsi_stack_bullish_d3},
    "f25_rsxh_102_rsi_stack_bearish_d3": {"inputs": ["close"], "func": f25_rsxh_102_rsi_stack_bearish_d3},
    "f25_rsxh_103_bars_since_rsi14_above_95_d3": {"inputs": ["close"], "func": f25_rsxh_103_bars_since_rsi14_above_95_d3},
    "f25_rsxh_104_bars_since_rsi14_below_5_d3": {"inputs": ["close"], "func": f25_rsxh_104_bars_since_rsi14_below_5_d3},
    "f25_rsxh_105_count_rsi_above_80_events_252_d3": {"inputs": ["close"], "func": f25_rsxh_105_count_rsi_above_80_events_252_d3},
    "f25_rsxh_106_count_rsi_below_20_events_252_d3": {"inputs": ["close"], "func": f25_rsxh_106_count_rsi_below_20_events_252_d3},
    "f25_rsxh_107_rsi_ob_exit_cluster_3_in_21_d3": {"inputs": ["close"], "func": f25_rsxh_107_rsi_ob_exit_cluster_3_in_21_d3},
    "f25_rsxh_108_days_at_252d_rsi_max_d3": {"inputs": ["close"], "func": f25_rsxh_108_days_at_252d_rsi_max_d3},
    "f25_rsxh_109_bars_since_rsi14_504d_max_d3": {"inputs": ["close"], "func": f25_rsxh_109_bars_since_rsi14_504d_max_d3},
    "f25_rsxh_110_longest_streak_below_30_d3": {"inputs": ["close"], "func": f25_rsxh_110_longest_streak_below_30_d3},
    "f25_rsxh_111_stuck_above_70_10bar_episodes_252_d3": {"inputs": ["close"], "func": f25_rsxh_111_stuck_above_70_10bar_episodes_252_d3},
    "f25_rsxh_112_cutler_minus_wilder_rsi14_d3": {"inputs": ["close"], "func": f25_rsxh_112_cutler_minus_wilder_rsi14_d3},
    "f25_rsxh_113_cutler_rsi14_above_70_state_d3": {"inputs": ["close"], "func": f25_rsxh_113_cutler_rsi14_above_70_state_d3},
    "f25_rsxh_114_cutler_rsi63_above_70_state_d3": {"inputs": ["close"], "func": f25_rsxh_114_cutler_rsi63_above_70_state_d3},
    "f25_rsxh_115_cutler_rsi_bearish_div_63_d3": {"inputs": _HC, "func": f25_rsxh_115_cutler_rsi_bearish_div_63_d3},
    "f25_rsxh_116_cutler_rsi_peak_decay_63_d3": {"inputs": ["close"], "func": f25_rsxh_116_cutler_rsi_peak_decay_63_d3},
    "f25_rsxh_117_sma_ema_rsi_cross_event_d3": {"inputs": ["close"], "func": f25_rsxh_117_sma_ema_rsi_cross_event_d3},
    "f25_rsxh_118_cutler_rsi_just_exited_ob70_d3": {"inputs": ["close"], "func": f25_rsxh_118_cutler_rsi_just_exited_ob70_d3},
    "f25_rsxh_119_cutler_rsi_dwell_ob70_63_d3": {"inputs": ["close"], "func": f25_rsxh_119_cutler_rsi_dwell_ob70_63_d3},
    "f25_rsxh_120_cutler_rsi_zscore_252_d3": {"inputs": ["close"], "func": f25_rsxh_120_cutler_rsi_zscore_252_d3},
    "f25_rsxh_121_percent_rank_return_1_over_50_d3": {"inputs": ["close"], "func": f25_rsxh_121_percent_rank_return_1_over_50_d3},
    "f25_rsxh_122_percent_rank_return_5_over_100_d3": {"inputs": ["close"], "func": f25_rsxh_122_percent_rank_return_5_over_100_d3},
    "f25_rsxh_123_percent_rank_return_21_over_252_d3": {"inputs": ["close"], "func": f25_rsxh_123_percent_rank_return_21_over_252_d3},
    "f25_rsxh_124_percent_rank_above_90_state_d3": {"inputs": ["close"], "func": f25_rsxh_124_percent_rank_above_90_state_d3},
    "f25_rsxh_125_percent_rank_above_95_extreme_d3": {"inputs": ["close"], "func": f25_rsxh_125_percent_rank_above_95_extreme_d3},
    "f25_rsxh_126_bars_since_percent_rank_above_90_d3": {"inputs": ["close"], "func": f25_rsxh_126_bars_since_percent_rank_above_90_d3},
    "f25_rsxh_127_percent_rank_above_90_count_63_d3": {"inputs": ["close"], "func": f25_rsxh_127_percent_rank_above_90_count_63_d3},
    "f25_rsxh_128_rsi_2_connors_d3": {"inputs": ["close"], "func": f25_rsxh_128_rsi_2_connors_d3},
    "f25_rsxh_129_rsi_2_above_90_state_d3": {"inputs": ["close"], "func": f25_rsxh_129_rsi_2_above_90_state_d3},
    "f25_rsxh_130_rsi_price_corr_252_d3": {"inputs": ["close"], "func": f25_rsxh_130_rsi_price_corr_252_d3},
    "f25_rsxh_131_rsi_vs_price_slope_disagree_63_d3": {"inputs": ["close"], "func": f25_rsxh_131_rsi_vs_price_slope_disagree_63_d3},
    "f25_rsxh_132_rsi_ob_area_63_d3": {"inputs": ["close"], "func": f25_rsxh_132_rsi_ob_area_63_d3},
    "f25_rsxh_133_rsi_normalized_momentum_mean_21_d3": {"inputs": ["close"], "func": f25_rsxh_133_rsi_normalized_momentum_mean_21_d3},
    "f25_rsxh_134_rsi_normalized_momentum_mean_63_d3": {"inputs": ["close"], "func": f25_rsxh_134_rsi_normalized_momentum_mean_63_d3},
    "f25_rsxh_135_rsi_normalized_momentum_mean_252_d3": {"inputs": ["close"], "func": f25_rsxh_135_rsi_normalized_momentum_mean_252_d3},
    "f25_rsxh_136_rsi_entropy_5bin_252_d3": {"inputs": ["close"], "func": f25_rsxh_136_rsi_entropy_5bin_252_d3},
    "f25_rsxh_137_rsi_kurt_252_d3": {"inputs": ["close"], "func": f25_rsxh_137_rsi_kurt_252_d3},
    "f25_rsxh_138_mean_rsi_at_new_252d_high_d3": {"inputs": _HC, "func": f25_rsxh_138_mean_rsi_at_new_252d_high_d3},
    "f25_rsxh_139_rsi_above_70_at_new_high_count_252_d3": {"inputs": _HC, "func": f25_rsxh_139_rsi_above_70_at_new_high_count_252_d3},
    "f25_rsxh_140_rsi_below_70_at_new_high_count_252_d3": {"inputs": _HC, "func": f25_rsxh_140_rsi_below_70_at_new_high_count_252_d3},
    "f25_rsxh_141_composite_exhaustion_flag_d3": {"inputs": _HC, "func": f25_rsxh_141_composite_exhaustion_flag_d3},
    "f25_rsxh_142_composite_exhaustion_count_63_d3": {"inputs": _HC, "func": f25_rsxh_142_composite_exhaustion_count_63_d3},
    "f25_rsxh_143_composite_exhaustion_count_252_d3": {"inputs": _HC, "func": f25_rsxh_143_composite_exhaustion_count_252_d3},
    "f25_rsxh_144_count_lower_ob_peaks_63_d3": {"inputs": ["close"], "func": f25_rsxh_144_count_lower_ob_peaks_63_d3},
    "f25_rsxh_145_count_lower_ob_peaks_252_d3": {"inputs": ["close"], "func": f25_rsxh_145_count_lower_ob_peaks_252_d3},
    "f25_rsxh_146_rsi_top_tercile_frac_252_d3": {"inputs": ["close"], "func": f25_rsxh_146_rsi_top_tercile_frac_252_d3},
    "f25_rsxh_147_rsi_bottom_tercile_frac_252_d3": {"inputs": ["close"], "func": f25_rsxh_147_rsi_bottom_tercile_frac_252_d3},
    "f25_rsxh_148_rsi_median_252_d3": {"inputs": ["close"], "func": f25_rsxh_148_rsi_median_252_d3},
    "f25_rsxh_149_rsi_minus_q95_self_252_d3": {"inputs": ["close"], "func": f25_rsxh_149_rsi_minus_q95_self_252_d3},
    "f25_rsxh_150_cum_rsi_deviation_from_50_252_d3": {"inputs": ["close"], "func": f25_rsxh_150_cum_rsi_deviation_from_50_252_d3},
}
