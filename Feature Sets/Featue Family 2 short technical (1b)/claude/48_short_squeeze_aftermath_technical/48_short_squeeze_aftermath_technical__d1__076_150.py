"""short_squeeze_aftermath_technical d1 features 076-150 — Pipeline 1b-technical.

Continuation of the 150-hypothesis family.
Bucket G: NSIR-vs-price signatures (joint NSIR + price conditions).
Bucket H: Post-peak technical breakdown (regime breaks, support violations).
Bucket I: Volume after peak (dry-vol, vol-of-vol, vol decay).
Bucket J: Range / volatility dynamics (ATR ratios, jumps, downside vol).
Bucket K: Trend reversal / momentum decay.
Bucket L: Composite squeeze-aftermath signals.

Inputs: SEP OHLCV (always) + NSIR (NaN-stubbed when absent). Self-contained
helpers; PIT-clean.
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


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


# ============================================================
# Bucket G — NSIR-vs-price signatures (076-088)
# ============================================================


def f48_ssat_076_si_down_price_down_flag_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SI declining (21d) AND price declining (21d) — distressed unwind/capitulation signal."""
    si21 = shortinterest.astype(float).diff(MDAYS)
    pr21 = close.pct_change(MDAYS)
    return (((si21 < 0) & (pr21 < 0)).astype(float).where(si21.notna() & pr21.notna(), np.nan)).diff()


def f48_ssat_077_si_down_price_up_flag_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SI declining AND price rising — classical short-cover squeeze."""
    si21 = shortinterest.astype(float).diff(MDAYS)
    pr21 = close.pct_change(MDAYS)
    return (((si21 < 0) & (pr21 > 0)).astype(float).where(si21.notna() & pr21.notna(), np.nan)).diff()


def f48_ssat_078_si_up_price_down_flag_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SI rising AND price falling — building bearish bet (pre-collapse setup)."""
    si21 = shortinterest.astype(float).diff(MDAYS)
    pr21 = close.pct_change(MDAYS)
    return (((si21 > 0) & (pr21 < 0)).astype(float).where(si21.notna() & pr21.notna(), np.nan)).diff()


def f48_ssat_079_dtc_up_price_up_flag_d1(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    """1 if daystocover rising (21d slope > 0) AND price rising (21d) — setup risk."""
    dtc_slope = _rolling_slope(daystocover.astype(float), MDAYS)
    pr21 = close.pct_change(MDAYS)
    return (((dtc_slope > 0) & (pr21 > 0)).astype(float).where(dtc_slope.notna() & pr21.notna(), np.nan)).diff()


def f48_ssat_080_shortpctfloat_over_21d_avgvol_ratio_d1(shortpctfloat: pd.Series, volume: pd.Series) -> pd.Series:
    """Short %-float / 21d avg volume — proxy for unwind-time pressure (lower vol = harder to cover)."""
    return (_safe_div(shortpctfloat.astype(float), volume.rolling(MDAYS, min_periods=WDAYS).mean())).diff()


def f48_ssat_081_bars_since_shortpctfloat_252d_max_d1(shortpctfloat: pd.Series) -> pd.Series:
    """Bars since short %-float reached 252d maximum."""
    p = shortpctfloat.astype(float)
    return (_bars_since_true(p == p.rolling(YDAYS, min_periods=QDAYS).max())).diff()


def f48_ssat_082_si_over_21d_total_volume_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """Short interest / 21d total volume — short interest as fraction of monthly traded shares."""
    return (_safe_div(shortinterest.astype(float), volume.rolling(MDAYS, min_periods=WDAYS).sum())).diff()


def f48_ssat_083_si_over_63d_total_volume_d1(shortinterest: pd.Series, volume: pd.Series) -> pd.Series:
    """Short interest / 63d total volume — quarterly horizon variant."""
    return (_safe_div(shortinterest.astype(float), volume.rolling(QDAYS, min_periods=MDAYS).sum())).diff()


def f48_ssat_084_ret21_minus_si_chg21_proxy_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """21d price return - 21d SI %-change — divergence proxy (positive = price up, SI down: squeeze)."""
    return (close.pct_change(MDAYS) - shortinterest.astype(float).pct_change(MDAYS)).diff()


def f48_ssat_085_dtc_above_3_and_above_sma200_flag_d1(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    """1 if daystocover > 3 AND close > SMA200 — squeeze setup in uptrend."""
    sma = _sma(close, 200)
    return (((daystocover.astype(float) > 3.0) & (close > sma)).astype(float).where(sma.notna() & daystocover.notna(), np.nan)).diff()


def f48_ssat_086_shortpctfloat_above_20_and_new_252d_high_d1(shortpctfloat: pd.Series, high: pd.Series) -> pd.Series:
    """1 if short %-float > 20% AND price at new 252d high — heavy short interest at top."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((shortpctfloat.astype(float) > 20.0) & (high >= rmax)).astype(float).where(rmax.notna() & shortpctfloat.notna(), np.nan)).diff()


def f48_ssat_087_si_fell_50pct_state_d1(shortinterest: pd.Series) -> pd.Series:
    """1 if SI has fallen more than 50% from its trailing 252d max — post-squeeze unwind state."""
    s = shortinterest.astype(float)
    return ((s < 0.5 * s.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(s.notna(), np.nan)).diff()


def f48_ssat_088_si_fell_75pct_extreme_d1(shortinterest: pd.Series) -> pd.Series:
    """1 if SI has fallen more than 75% from trailing 252d max — extreme unwind state."""
    s = shortinterest.astype(float)
    return ((s < 0.25 * s.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(s.notna(), np.nan)).diff()


def f48_ssat_089_break_below_sma21_after_60d_above_flag_d1(close: pd.Series) -> pd.Series:
    """1 if close < SMA21 now AND was above SMA21 for 60+ prior bars — regime break."""
    sma = _sma(close, MDAYS)
    above = (close > sma)
    streak_prev = _streak_true(above).shift(1)
    return (((close < sma) & (streak_prev >= 60)).astype(float).where(sma.notna(), np.nan)).diff()


def f48_ssat_090_break_below_sma200_after_252d_above_flag_d1(close: pd.Series) -> pd.Series:
    """1 if close < SMA200 now AND was above SMA200 for 252+ prior bars — long-term regime break."""
    sma = _sma(close, 200)
    above = (close > sma)
    streak_prev = _streak_true(above).shift(1)
    return (((close < sma) & (streak_prev >= YDAYS)).astype(float).where(sma.notna(), np.nan)).diff()


def f48_ssat_091_sma21_cross_below_sma63_after_parabolic_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SMA21 < SMA63 today, SMA21 >= SMA63 yesterday, AND 252d-max-of-63d-return > 100%."""
    s21 = _sma(close, MDAYS); s63 = _sma(close, QDAYS)
    cross = (s21.shift(1) >= s63.shift(1)) & (s21 < s63)
    had_parabolic = (close.pct_change(QDAYS).rolling(YDAYS, min_periods=QDAYS).max() > 1.0)
    return ((cross & had_parabolic).astype(float).where(s21.notna() & s63.notna(), np.nan)).diff()


def f48_ssat_092_death_cross_after_100pct_run_flag_d1(close: pd.Series) -> pd.Series:
    """1 if SMA50 crossed below SMA200 today AND past-252d 63d-return-max > 100%."""
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    cross = (s50.shift(1) >= s200.shift(1)) & (s50 < s200)
    had_parabolic = (close.pct_change(QDAYS).rolling(YDAYS, min_periods=QDAYS).max() > 1.0)
    return ((cross & had_parabolic).astype(float).where(s50.notna() & s200.notna(), np.nan)).diff()


def f48_ssat_093_higher_low_fail_count_63_d1(low: pd.Series) -> pd.Series:
    """Count past 63 bars where today's 21d-low is below 21d-low 21 bars ago — failed-higher-low count."""
    lm = low.rolling(MDAYS, min_periods=WDAYS).min()
    failed = (lm < lm.shift(MDAYS)).astype(float)
    return (failed.rolling(QDAYS, min_periods=MDAYS).sum().where(lm.notna() & lm.shift(MDAYS).notna(), np.nan)).diff()


def f48_ssat_094_close_below_52wk_low_flag_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close < trailing 252d low — broken-support flag."""
    lmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return ((close < lmin).astype(float).where(lmin.notna(), np.nan)).diff()


def f48_ssat_095_close_in_lower_25pct_of_252d_range_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close is in lower-25% of trailing-252d (high - low) range."""
    hmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    lmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lmin, hmax - lmin)
    return ((pos < 0.25).astype(float).where(pos.notna(), np.nan)).diff()


def f48_ssat_096_close_in_lower_10pct_of_252d_range_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close is in lower-10% of trailing-252d range — deep-in-range bottom."""
    hmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    lmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lmin, hmax - lmin)
    return ((pos < 0.10).astype(float).where(pos.notna(), np.nan)).diff()


def f48_ssat_097_close_below_50pct_retracement_state_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close < midpoint of 252d (high - low) range — below 50% Fibonacci retracement."""
    hmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    lmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    mid = (hmax + lmin) / 2.0
    return ((close < mid).astype(float).where(mid.notna(), np.nan)).diff()


def f48_ssat_098_close_below_618_retracement_state_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close < 0.382 * range + low (i.e., below 61.8% retracement from high)."""
    hmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    lmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = lmin + 0.382 * (hmax - lmin)
    return ((close < fib).astype(float).where(fib.notna(), np.nan)).diff()


def f48_ssat_099_close_below_786_retracement_state_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close < 0.214 * range + low (below 78.6% deep Fibonacci retracement)."""
    hmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    lmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = lmin + 0.214 * (hmax - lmin)
    return ((close < fib).astype(float).where(fib.notna(), np.nan)).diff()


def f48_ssat_100_21d_close_range_below_third_of_21d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """21d close range / 21d high < 1/3 — close-range compressed deep below high."""
    crange = close.rolling(MDAYS, min_periods=WDAYS).max() - close.rolling(MDAYS, min_periods=WDAYS).min()
    hmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    return ((_safe_div(crange, hmax) < (1.0 / 3.0)).astype(float).where(hmax.notna(), np.nan)).diff()


def f48_ssat_101_avg_vol_21_over_avg_vol_252_lagged_63_d1(volume: pd.Series) -> pd.Series:
    """21d-avg vol / 21d-avg vol from 63 bars ago — recent vs prior monthly vol (drying or not)."""
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(v21, v21.shift(QDAYS))).diff()


def f48_ssat_102_avg_vol_63_over_avg_vol_252_lagged_252_d1(volume: pd.Series) -> pd.Series:
    """63d-avg vol / 63d-avg vol from 252 bars ago — quarterly vol-trend over a year."""
    v63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return (_safe_div(v63, v63.shift(YDAYS))).diff()


def f48_ssat_103_vol_zscore_252_after_252d_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z-score (252d) on bars where bars-since-252d-high > 21 — post-peak vol-anomaly."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return (vz.where(bs > MDAYS, np.nan)).diff()


def f48_ssat_104_longest_dry_vol_streak_63_d1(volume: pd.Series) -> pd.Series:
    """Longest consecutive run of vol < 50% of 252d median, past 63 — drought streak."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    streak = _streak_true(volume < 0.5 * med)
    return (streak.rolling(QDAYS, min_periods=MDAYS).max().where(med.notna(), np.nan)).diff()


def f48_ssat_105_dry_vol_bar_count_21_d1(volume: pd.Series) -> pd.Series:
    """Count past 21 of bars with vol < 50% of 252d median — short-term drought count."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((volume < 0.5 * med).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(med.notna(), np.nan)).diff()


def f48_ssat_106_dry_vol_bar_count_63_d1(volume: pd.Series) -> pd.Series:
    """Count past 63 of bars with vol < 50% of 252d median."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((volume < 0.5 * med).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(med.notna(), np.nan)).diff()


def f48_ssat_107_vol_pct_rank_252_d1(volume: pd.Series) -> pd.Series:
    """Vol percentile rank vs trailing 252d — low = drought; high = panic."""
    return (volume.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()


def f48_ssat_108_vol_of_vol_past_63_d1(volume: pd.Series) -> pd.Series:
    """Std of log-volume past 63 — volume volatility."""
    return (_safe_log(volume).rolling(QDAYS, min_periods=MDAYS).std()).diff()


def f48_ssat_109_vol_decline_pct_63_over_lagged_63_d1(volume: pd.Series) -> pd.Series:
    """(63d-avg vol now / 63d-avg vol 63 bars ago) - 1 — quarterly vol %-decline."""
    v63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return (_safe_div(v63, v63.shift(QDAYS)) - 1.0).diff()


def f48_ssat_110_corr_vol_price_signed_63_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d corr(close-pct-change, volume) — sign-sensitive vol-vs-price corr. Low when price down on low vol."""
    return (close.pct_change().rolling(QDAYS, min_periods=MDAYS).corr(volume)).diff()


def f48_ssat_111_atr21_over_atr252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21 / ATR252 — recent vol vs annual vol (>1 = vol expansion)."""
    return (_safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS))).diff()


def f48_ssat_112_atr63_over_atr252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR63 / ATR252 — quarterly vs annual vol."""
    return (_safe_div(_atr(high, low, close, QDAYS), _atr(high, low, close, YDAYS))).diff()


def f48_ssat_113_atr_pct_rank_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21 percentile rank vs trailing 252d — extreme-high = crisis."""
    return (_atr(high, low, close, MDAYS).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()


def f48_ssat_114_atr_expansion_event_count_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars where ATR21 > 1.5x ATR63 — atr-expansion events."""
    r = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, QDAYS))
    return ((r > 1.5).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna(), np.nan)).diff()


def f48_ssat_115_realized_vol_21_d1(close: pd.Series) -> pd.Series:
    """21d realized volatility (std of returns, annualized)."""
    return (close.pct_change().rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(YDAYS)).diff()


def f48_ssat_116_realized_vol_63_d1(close: pd.Series) -> pd.Series:
    """63d realized volatility (annualized)."""
    return (close.pct_change().rolling(QDAYS, min_periods=MDAYS).std() * np.sqrt(YDAYS)).diff()


def f48_ssat_117_vol_of_realized_vol_63_d1(close: pd.Series) -> pd.Series:
    """Std of 21d realized-vol past 63 — vol-of-vol expansion."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return (rv.rolling(QDAYS, min_periods=MDAYS).std()).diff()


def f48_ssat_118_downside_vol_21_d1(close: pd.Series) -> pd.Series:
    """Std of negative returns past 21 (downside-only)."""
    r = close.pct_change()
    neg = r.where(r < 0)
    return (neg.rolling(MDAYS, min_periods=WDAYS).std()).diff()


def f48_ssat_119_downside_vol_63_d1(close: pd.Series) -> pd.Series:
    """Std of negative returns past 63."""
    r = close.pct_change()
    neg = r.where(r < 0)
    return (neg.rolling(QDAYS, min_periods=MDAYS).std()).diff()


def f48_ssat_120_downside_over_upside_vol_ratio_63_d1(close: pd.Series) -> pd.Series:
    """Downside vol / upside vol past 63 — asymmetry indicator (>1 = bearish skew)."""
    r = close.pct_change()
    dv = r.where(r < 0).rolling(QDAYS, min_periods=MDAYS).std()
    uv = r.where(r > 0).rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(dv, uv)).diff()


def f48_ssat_121_jump_count_63_d1(close: pd.Series) -> pd.Series:
    """Count past 63 of bars where |return| > 4 * 21d std of returns — jump count."""
    r = close.pct_change()
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    return ((r.abs() > 4.0 * s).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(s.notna(), np.nan)).diff()


def f48_ssat_122_jump_count_252_d1(close: pd.Series) -> pd.Series:
    """Annual jump count."""
    r = close.pct_change()
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    return ((r.abs() > 4.0 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(s.notna(), np.nan)).diff()


def f48_ssat_123_21d_reversal_after_parabolic_flag_d1(close: pd.Series) -> pd.Series:
    """1 if 21d return < 0 AND past-252d 252d-return-max > 100% — reversal after big run."""
    r21 = close.pct_change(MDAYS)
    had_parabolic = (close.pct_change(YDAYS).rolling(YDAYS, min_periods=QDAYS).max() > 1.0)
    return (((r21 < 0) & had_parabolic).astype(float).where(r21.notna(), np.nan)).diff()


def f48_ssat_124_ret21_minus_ret63_d1(close: pd.Series) -> pd.Series:
    """21d return - 63d return — momentum convergence (>0 = recent acceleration)."""
    return (close.pct_change(MDAYS) - close.pct_change(QDAYS)).diff()


def f48_ssat_125_ret63_minus_ret252_d1(close: pd.Series) -> pd.Series:
    """63d return - 252d return — quarterly vs annual momentum gap."""
    return (close.pct_change(QDAYS) - close.pct_change(YDAYS)).diff()


def f48_ssat_126_ret21_zscore_in_252_distribution_d1(close: pd.Series) -> pd.Series:
    """Z-score of current 21d return vs trailing 252d distribution of 21d returns."""
    return (_rolling_zscore(close.pct_change(MDAYS), YDAYS, min_periods=QDAYS)).diff()


def f48_ssat_127_ret63_pct_rank_in_252_distribution_d1(close: pd.Series) -> pd.Series:
    """Pct-rank of current 63d return vs trailing 252d distribution of 63d returns."""
    return (close.pct_change(QDAYS).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()


def f48_ssat_128_negative_weekly_ret_streak_d1(close: pd.Series) -> pd.Series:
    """Current consecutive run of negative 5-bar returns (rolling)."""
    r5 = close.pct_change(WDAYS)
    return (_streak_true(r5 < 0)).diff()


def f48_ssat_129_longest_negative_weekly_streak_63_d1(close: pd.Series) -> pd.Series:
    """Longest consecutive run of negative 5-bar returns in past 63."""
    r5 = close.pct_change(WDAYS)
    s = _streak_true(r5 < 0)
    return (s.rolling(QDAYS, min_periods=MDAYS).max().where(r5.notna(), np.nan)).diff()


def f48_ssat_130_longest_negative_monthly_streak_252_d1(close: pd.Series) -> pd.Series:
    """Longest consecutive run of negative 21-bar returns in past 252."""
    r21 = close.pct_change(MDAYS)
    s = _streak_true(r21 < 0)
    return (s.rolling(YDAYS, min_periods=QDAYS).max().where(r21.notna(), np.nan)).diff()


def f48_ssat_131_sum_log_returns_past_21_d1(close: pd.Series) -> pd.Series:
    """Sum of log returns past 21 — monthly net log-return."""
    return ((_safe_log(close) - _safe_log(close.shift(1))).rolling(MDAYS, min_periods=WDAYS).sum()).diff()


def f48_ssat_132_sum_log_returns_past_63_d1(close: pd.Series) -> pd.Series:
    """Sum of log returns past 63 — quarterly net log-return."""
    return ((_safe_log(close) - _safe_log(close.shift(1))).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f48_ssat_133_sum_log_returns_past_252_d1(close: pd.Series) -> pd.Series:
    """Sum of log returns past 252 — annual net log-return."""
    return ((_safe_log(close) - _safe_log(close.shift(1))).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f48_ssat_134_sum_log_returns_past_504_d1(close: pd.Series) -> pd.Series:
    """Sum of log returns past 504 — multi-year net log-return."""
    return ((_safe_log(close) - _safe_log(close.shift(1))).rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff()


def f48_ssat_135_cum_log_ret_minus_252d_cummax_d1(close: pd.Series) -> pd.Series:
    """Cumulative log-return - its trailing 252d cummax — log-units below peak (drawdown in log space)."""
    lr_cum = (_safe_log(close) - _safe_log(close.shift(1))).cumsum()
    return (lr_cum - lr_cum.rolling(YDAYS, min_periods=QDAYS).max()).diff()


def f48_ssat_136_composite_si_unwound_price_crashed_capit_d1(shortinterest: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if SI fell >50% from peak AND drawdown >50% from 252d high AND capit-bar in past 21."""
    s = shortinterest.astype(float)
    si_unwound = s < 0.5 * s.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float)
    capit_21 = capit.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    return ((si_unwound & (dd <= -0.5) & capit_21).astype(float).where(s.notna() & dd.notna(), np.nan)).diff()


def f48_ssat_137_composite_si_unwound_price_weak_vol_dry_d1(shortinterest: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if SI fell >50% from peak AND close < SMA63 AND vol < 50% of 252d median."""
    s = shortinterest.astype(float)
    si_unwound = s < 0.5 * s.rolling(YDAYS, min_periods=QDAYS).max()
    sma = _sma(close, QDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((si_unwound & (close < sma) & (volume < 0.5 * med)).astype(float).where(s.notna() & sma.notna() & med.notna(), np.nan)).diff()


def f48_ssat_138_composite_parabolic_dd50_capit_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if past-252d max 63d-return > 100% AND drawdown <=-50% AND capit bar in past 21."""
    had_parabolic = close.pct_change(QDAYS).rolling(YDAYS, min_periods=QDAYS).max() > 1.0
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float)
    capit_21 = capit.rolling(MDAYS, min_periods=WDAYS).sum() > 0
    return ((had_parabolic & (dd <= -0.5) & capit_21).astype(float).where(dd.notna() & a.notna(), np.nan)).diff()


def f48_ssat_139_high_dtc_prior_plus_bearish_cross_d1(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    """1 if daystocover > 5 at any point past 252 AND SMA50 just crossed below SMA200."""
    dtc = daystocover.astype(float)
    had_high_dtc = ((dtc > 5.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() > 0)
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    cross = (s50.shift(1) >= s200.shift(1)) & (s50 < s200)
    return ((had_high_dtc & cross).astype(float).where(dtc.notna() & s50.notna() & s200.notna(), np.nan)).diff()


def f48_ssat_140_post_squeeze_regime_indicator_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """log(bars-since-NSIR-252d-max + 1) on bars where close < SMA200; else NaN."""
    s = shortinterest.astype(float)
    bs = _bars_since_true(s == s.rolling(YDAYS, min_periods=QDAYS).max())
    sma = _sma(close, 200)
    out = np.log1p(bs.where(close < sma, np.nan))
    return (out).diff()


def f48_ssat_141_count_dd20_capit_regimebrk_past_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 63 of bars satisfying any of: drawdown <-20% from 252d high, capit-bar, regime-break."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    sma = _sma(close, MDAYS)
    above = (close > sma)
    streak_prev = _streak_true(above).shift(1)
    regime_brk = (close < sma) & (streak_prev >= 60)
    any_cond = ((dd <= -0.20) | capit | regime_brk).astype(float)
    return (any_cond.rolling(QDAYS, min_periods=MDAYS).sum().where(dd.notna(), np.nan)).diff()


def f48_ssat_142_squeeze_prelude_conditions_count_d1(shortpctfloat: pd.Series, daystocover: pd.Series, close: pd.Series) -> pd.Series:
    """Count of squeeze-prelude conditions: {short %-float > 20, daystocover > 5, RSI(14)>70}."""
    delta = close.diff()
    up = delta.clip(lower=0); dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    ad = dn.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    rsi = 100.0 - 100.0 / (1.0 + _safe_div(au, ad))
    c = ((shortpctfloat.astype(float) > 20).astype(float).fillna(0)
         + (daystocover.astype(float) > 5).astype(float).fillna(0)
         + (rsi > 70).astype(float).fillna(0))
    return (c).diff()


def f48_ssat_143_aftermath_score_si_decline_x_dd_d1(shortinterest: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """(SI %-decline-from-252d-max) * (|drawdown-from-252d-high|) — aftermath intensity proxy."""
    s = shortinterest.astype(float)
    smax = s.rolling(YDAYS, min_periods=QDAYS).max()
    si_dec_pct = _safe_div(smax - s, smax)
    dd = (_safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0).abs()
    return (si_dec_pct * dd).diff()


def f48_ssat_144_aftermath_score_capit21_plus_dd50_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(capit-count past 21) + 5 * (drawdown <=-50% flag) — composite score."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float)
    cnt_21 = capit.rolling(MDAYS, min_periods=WDAYS).sum()
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (cnt_21 + 5.0 * (dd <= -0.5).astype(float)).diff()


def f48_ssat_145_days_since_peak_vol_over_total_bars_d1(volume: pd.Series) -> pd.Series:
    """Bars since 252d max volume / 252 — normalized recency-since-blowoff (0..1)."""
    at_max = volume == volume.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max) / float(YDAYS)).diff()


def f48_ssat_146_daystocover_slope_21_d1(daystocover: pd.Series) -> pd.Series:
    """21d rolling slope of daystocover — building-risk indicator when positive."""
    return (_rolling_slope(daystocover.astype(float), MDAYS)).diff()


def f48_ssat_147_shortpctfloat_slope_21_d1(shortpctfloat: pd.Series) -> pd.Series:
    """21d rolling slope of short %-float — building-risk indicator when positive."""
    return (_rolling_slope(shortpctfloat.astype(float), MDAYS)).diff()


def f48_ssat_148_squeeze_vulnerability_index_d1(shortpctfloat: pd.Series, close: pd.Series) -> pd.Series:
    """short %-float * (1 + 21d return) — squeeze-vulnerability index (high SI on rising price)."""
    r21 = close.pct_change(MDAYS)
    return (shortpctfloat.astype(float) * (1.0 + r21)).diff()


def f48_ssat_149_post_blowoff_dwell_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since drawdown first crossed below -50% (after a 100%+ 63d run occurred in past 504 bars)."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    had_parabolic = (close.pct_change(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).max() > 1.0)
    cond = (dd <= -0.5) & had_parabolic
    return (_bars_since_true(cond)).diff()


def f48_ssat_150_terminal_decline_composite_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: (|dd from 252d high|) + (1 - ATR21/ATR252) clipped[0,1] + (1 - vol/252d-median) clipped[0,1]."""
    dd_mag = (_safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0).abs()
    atr_decline = (1.0 - _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS))).clip(0, 1)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_dry = (1.0 - _safe_div(volume, med)).clip(0, 1)
    return (dd_mag + atr_decline + vol_dry).diff()


# ============================================================
#                         REGISTRY 076-150 (d1)
# ============================================================

_HC = ["high", "close"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_CV = ["close", "volume"]
_HCV = ["high", "close", "volume"]
_LC = ["low", "close"]

SHORT_SQUEEZE_AFTERMATH_TECHNICAL_D1_REGISTRY_076_150 = {
    "f48_ssat_076_si_down_price_down_flag_d1": {"inputs": ["shortinterest", "close"], "func": f48_ssat_076_si_down_price_down_flag_d1},
    "f48_ssat_077_si_down_price_up_flag_d1": {"inputs": ["shortinterest", "close"], "func": f48_ssat_077_si_down_price_up_flag_d1},
    "f48_ssat_078_si_up_price_down_flag_d1": {"inputs": ["shortinterest", "close"], "func": f48_ssat_078_si_up_price_down_flag_d1},
    "f48_ssat_079_dtc_up_price_up_flag_d1": {"inputs": ["daystocover", "close"], "func": f48_ssat_079_dtc_up_price_up_flag_d1},
    "f48_ssat_080_shortpctfloat_over_21d_avgvol_ratio_d1": {"inputs": ["shortpctfloat", "volume"], "func": f48_ssat_080_shortpctfloat_over_21d_avgvol_ratio_d1},
    "f48_ssat_081_bars_since_shortpctfloat_252d_max_d1": {"inputs": ["shortpctfloat"], "func": f48_ssat_081_bars_since_shortpctfloat_252d_max_d1},
    "f48_ssat_082_si_over_21d_total_volume_d1": {"inputs": ["shortinterest", "volume"], "func": f48_ssat_082_si_over_21d_total_volume_d1},
    "f48_ssat_083_si_over_63d_total_volume_d1": {"inputs": ["shortinterest", "volume"], "func": f48_ssat_083_si_over_63d_total_volume_d1},
    "f48_ssat_084_ret21_minus_si_chg21_proxy_d1": {"inputs": ["shortinterest", "close"], "func": f48_ssat_084_ret21_minus_si_chg21_proxy_d1},
    "f48_ssat_085_dtc_above_3_and_above_sma200_flag_d1": {"inputs": ["daystocover", "close"], "func": f48_ssat_085_dtc_above_3_and_above_sma200_flag_d1},
    "f48_ssat_086_shortpctfloat_above_20_and_new_252d_high_d1": {"inputs": ["shortpctfloat", "high"], "func": f48_ssat_086_shortpctfloat_above_20_and_new_252d_high_d1},
    "f48_ssat_087_si_fell_50pct_state_d1": {"inputs": ["shortinterest"], "func": f48_ssat_087_si_fell_50pct_state_d1},
    "f48_ssat_088_si_fell_75pct_extreme_d1": {"inputs": ["shortinterest"], "func": f48_ssat_088_si_fell_75pct_extreme_d1},
    "f48_ssat_089_break_below_sma21_after_60d_above_flag_d1": {"inputs": ["close"], "func": f48_ssat_089_break_below_sma21_after_60d_above_flag_d1},
    "f48_ssat_090_break_below_sma200_after_252d_above_flag_d1": {"inputs": ["close"], "func": f48_ssat_090_break_below_sma200_after_252d_above_flag_d1},
    "f48_ssat_091_sma21_cross_below_sma63_after_parabolic_d1": {"inputs": _HLC, "func": f48_ssat_091_sma21_cross_below_sma63_after_parabolic_d1},
    "f48_ssat_092_death_cross_after_100pct_run_flag_d1": {"inputs": ["close"], "func": f48_ssat_092_death_cross_after_100pct_run_flag_d1},
    "f48_ssat_093_higher_low_fail_count_63_d1": {"inputs": ["low"], "func": f48_ssat_093_higher_low_fail_count_63_d1},
    "f48_ssat_094_close_below_52wk_low_flag_d1": {"inputs": _LC, "func": f48_ssat_094_close_below_52wk_low_flag_d1},
    "f48_ssat_095_close_in_lower_25pct_of_252d_range_d1": {"inputs": _HLC, "func": f48_ssat_095_close_in_lower_25pct_of_252d_range_d1},
    "f48_ssat_096_close_in_lower_10pct_of_252d_range_d1": {"inputs": _HLC, "func": f48_ssat_096_close_in_lower_10pct_of_252d_range_d1},
    "f48_ssat_097_close_below_50pct_retracement_state_d1": {"inputs": _HLC, "func": f48_ssat_097_close_below_50pct_retracement_state_d1},
    "f48_ssat_098_close_below_618_retracement_state_d1": {"inputs": _HLC, "func": f48_ssat_098_close_below_618_retracement_state_d1},
    "f48_ssat_099_close_below_786_retracement_state_d1": {"inputs": _HLC, "func": f48_ssat_099_close_below_786_retracement_state_d1},
    "f48_ssat_100_21d_close_range_below_third_of_21d_high_d1": {"inputs": _HC, "func": f48_ssat_100_21d_close_range_below_third_of_21d_high_d1},
    "f48_ssat_101_avg_vol_21_over_avg_vol_252_lagged_63_d1": {"inputs": ["volume"], "func": f48_ssat_101_avg_vol_21_over_avg_vol_252_lagged_63_d1},
    "f48_ssat_102_avg_vol_63_over_avg_vol_252_lagged_252_d1": {"inputs": ["volume"], "func": f48_ssat_102_avg_vol_63_over_avg_vol_252_lagged_252_d1},
    "f48_ssat_103_vol_zscore_252_after_252d_high_d1": {"inputs": ["high", "volume"], "func": f48_ssat_103_vol_zscore_252_after_252d_high_d1},
    "f48_ssat_104_longest_dry_vol_streak_63_d1": {"inputs": ["volume"], "func": f48_ssat_104_longest_dry_vol_streak_63_d1},
    "f48_ssat_105_dry_vol_bar_count_21_d1": {"inputs": ["volume"], "func": f48_ssat_105_dry_vol_bar_count_21_d1},
    "f48_ssat_106_dry_vol_bar_count_63_d1": {"inputs": ["volume"], "func": f48_ssat_106_dry_vol_bar_count_63_d1},
    "f48_ssat_107_vol_pct_rank_252_d1": {"inputs": ["volume"], "func": f48_ssat_107_vol_pct_rank_252_d1},
    "f48_ssat_108_vol_of_vol_past_63_d1": {"inputs": ["volume"], "func": f48_ssat_108_vol_of_vol_past_63_d1},
    "f48_ssat_109_vol_decline_pct_63_over_lagged_63_d1": {"inputs": ["volume"], "func": f48_ssat_109_vol_decline_pct_63_over_lagged_63_d1},
    "f48_ssat_110_corr_vol_price_signed_63_d1": {"inputs": _CV, "func": f48_ssat_110_corr_vol_price_signed_63_d1},
    "f48_ssat_111_atr21_over_atr252_d1": {"inputs": _HLC, "func": f48_ssat_111_atr21_over_atr252_d1},
    "f48_ssat_112_atr63_over_atr252_d1": {"inputs": _HLC, "func": f48_ssat_112_atr63_over_atr252_d1},
    "f48_ssat_113_atr_pct_rank_252_d1": {"inputs": _HLC, "func": f48_ssat_113_atr_pct_rank_252_d1},
    "f48_ssat_114_atr_expansion_event_count_63_d1": {"inputs": _HLC, "func": f48_ssat_114_atr_expansion_event_count_63_d1},
    "f48_ssat_115_realized_vol_21_d1": {"inputs": ["close"], "func": f48_ssat_115_realized_vol_21_d1},
    "f48_ssat_116_realized_vol_63_d1": {"inputs": ["close"], "func": f48_ssat_116_realized_vol_63_d1},
    "f48_ssat_117_vol_of_realized_vol_63_d1": {"inputs": ["close"], "func": f48_ssat_117_vol_of_realized_vol_63_d1},
    "f48_ssat_118_downside_vol_21_d1": {"inputs": ["close"], "func": f48_ssat_118_downside_vol_21_d1},
    "f48_ssat_119_downside_vol_63_d1": {"inputs": ["close"], "func": f48_ssat_119_downside_vol_63_d1},
    "f48_ssat_120_downside_over_upside_vol_ratio_63_d1": {"inputs": ["close"], "func": f48_ssat_120_downside_over_upside_vol_ratio_63_d1},
    "f48_ssat_121_jump_count_63_d1": {"inputs": ["close"], "func": f48_ssat_121_jump_count_63_d1},
    "f48_ssat_122_jump_count_252_d1": {"inputs": ["close"], "func": f48_ssat_122_jump_count_252_d1},
    "f48_ssat_123_21d_reversal_after_parabolic_flag_d1": {"inputs": ["close"], "func": f48_ssat_123_21d_reversal_after_parabolic_flag_d1},
    "f48_ssat_124_ret21_minus_ret63_d1": {"inputs": ["close"], "func": f48_ssat_124_ret21_minus_ret63_d1},
    "f48_ssat_125_ret63_minus_ret252_d1": {"inputs": ["close"], "func": f48_ssat_125_ret63_minus_ret252_d1},
    "f48_ssat_126_ret21_zscore_in_252_distribution_d1": {"inputs": ["close"], "func": f48_ssat_126_ret21_zscore_in_252_distribution_d1},
    "f48_ssat_127_ret63_pct_rank_in_252_distribution_d1": {"inputs": ["close"], "func": f48_ssat_127_ret63_pct_rank_in_252_distribution_d1},
    "f48_ssat_128_negative_weekly_ret_streak_d1": {"inputs": ["close"], "func": f48_ssat_128_negative_weekly_ret_streak_d1},
    "f48_ssat_129_longest_negative_weekly_streak_63_d1": {"inputs": ["close"], "func": f48_ssat_129_longest_negative_weekly_streak_63_d1},
    "f48_ssat_130_longest_negative_monthly_streak_252_d1": {"inputs": ["close"], "func": f48_ssat_130_longest_negative_monthly_streak_252_d1},
    "f48_ssat_131_sum_log_returns_past_21_d1": {"inputs": ["close"], "func": f48_ssat_131_sum_log_returns_past_21_d1},
    "f48_ssat_132_sum_log_returns_past_63_d1": {"inputs": ["close"], "func": f48_ssat_132_sum_log_returns_past_63_d1},
    "f48_ssat_133_sum_log_returns_past_252_d1": {"inputs": ["close"], "func": f48_ssat_133_sum_log_returns_past_252_d1},
    "f48_ssat_134_sum_log_returns_past_504_d1": {"inputs": ["close"], "func": f48_ssat_134_sum_log_returns_past_504_d1},
    "f48_ssat_135_cum_log_ret_minus_252d_cummax_d1": {"inputs": ["close"], "func": f48_ssat_135_cum_log_ret_minus_252d_cummax_d1},
    "f48_ssat_136_composite_si_unwound_price_crashed_capit_d1": {"inputs": ["shortinterest", "high", "low", "close", "volume"], "func": f48_ssat_136_composite_si_unwound_price_crashed_capit_d1},
    "f48_ssat_137_composite_si_unwound_price_weak_vol_dry_d1": {"inputs": ["shortinterest", "close", "volume"], "func": f48_ssat_137_composite_si_unwound_price_weak_vol_dry_d1},
    "f48_ssat_138_composite_parabolic_dd50_capit_d1": {"inputs": _HLCV, "func": f48_ssat_138_composite_parabolic_dd50_capit_d1},
    "f48_ssat_139_high_dtc_prior_plus_bearish_cross_d1": {"inputs": ["daystocover", "close"], "func": f48_ssat_139_high_dtc_prior_plus_bearish_cross_d1},
    "f48_ssat_140_post_squeeze_regime_indicator_d1": {"inputs": ["shortinterest", "close"], "func": f48_ssat_140_post_squeeze_regime_indicator_d1},
    "f48_ssat_141_count_dd20_capit_regimebrk_past_63_d1": {"inputs": _HLCV, "func": f48_ssat_141_count_dd20_capit_regimebrk_past_63_d1},
    "f48_ssat_142_squeeze_prelude_conditions_count_d1": {"inputs": ["shortpctfloat", "daystocover", "close"], "func": f48_ssat_142_squeeze_prelude_conditions_count_d1},
    "f48_ssat_143_aftermath_score_si_decline_x_dd_d1": {"inputs": ["shortinterest", "high", "close"], "func": f48_ssat_143_aftermath_score_si_decline_x_dd_d1},
    "f48_ssat_144_aftermath_score_capit21_plus_dd50_d1": {"inputs": _HLCV, "func": f48_ssat_144_aftermath_score_capit21_plus_dd50_d1},
    "f48_ssat_145_days_since_peak_vol_over_total_bars_d1": {"inputs": ["volume"], "func": f48_ssat_145_days_since_peak_vol_over_total_bars_d1},
    "f48_ssat_146_daystocover_slope_21_d1": {"inputs": ["daystocover"], "func": f48_ssat_146_daystocover_slope_21_d1},
    "f48_ssat_147_shortpctfloat_slope_21_d1": {"inputs": ["shortpctfloat"], "func": f48_ssat_147_shortpctfloat_slope_21_d1},
    "f48_ssat_148_squeeze_vulnerability_index_d1": {"inputs": ["shortpctfloat", "close"], "func": f48_ssat_148_squeeze_vulnerability_index_d1},
    "f48_ssat_149_post_blowoff_dwell_d1": {"inputs": _HC, "func": f48_ssat_149_post_blowoff_dwell_d1},
    "f48_ssat_150_terminal_decline_composite_d1": {"inputs": _HLCV, "func": f48_ssat_150_terminal_decline_composite_d1},
}
