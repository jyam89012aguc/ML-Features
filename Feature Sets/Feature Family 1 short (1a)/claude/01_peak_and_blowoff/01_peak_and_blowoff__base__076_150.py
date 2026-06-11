"""peak_and_blowoff base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py. Inputs: SEP OHLCV only.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows, no .shift(-N).
"""
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


# ============================================================
#                    FEATURES 076-150
# ============================================================

def f01_pab_076_gap_up_count_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in last 21 where open > prior close (open gap up)."""
    return (open_ > close.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_077_gap_up_total_magnitude_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of (open-prior_close)/prior_close on gap-up bars in last 21."""
    pc = close.shift(1)
    sz = ((open_ - pc) / pc.replace(0, np.nan)).where(open_ > pc, 0.0)
    return sz.rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_078_gap_up_filled_count_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-up bars in last 21 that closed below their open (intraday fill)."""
    pc = close.shift(1)
    flag = (open_ > pc) & (close < open_)
    return flag.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_079_gap_down_count_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in last 21 where open < prior close (gap down)."""
    return (open_ < close.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_080_exhaustion_gap_signature_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Big-gap-up + bearish close + above-avg volume bars in last 21d."""
    pc = close.shift(1)
    atr = _atr(high, low, close, MDAYS)
    big_gap = (open_ - pc) > atr
    reversal = close < open_
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    high_vol = volume > 1.5 * v21
    return (big_gap & reversal & high_vol).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_081_breakaway_gap_count_63d(open_: pd.Series, high: pd.Series) -> pd.Series:
    """Bars in last 63 where open > prior high (true price gap)."""
    return (open_ > high.shift(1)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_082_runaway_gap_streak_max_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Longest streak of consecutive gap-up days in last 21."""
    gap_up = (open_ > close.shift(1)).astype(int)
    grp = (gap_up == 0).cumsum()
    streak = gap_up.groupby(grp).cumsum()
    return streak.rolling(MDAYS, min_periods=WDAYS).max()


def f01_pab_083_island_top_count_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Island-top pattern (gap up within 5 bars, then gap down) count in 252d."""
    pc = close.shift(1)
    gap_up = (open_ > pc).astype(float)
    gap_down = open_ < pc
    had_recent_gap_up = gap_up.shift(1).rolling(5, min_periods=1).max() >= 1
    island = (had_recent_gap_up & gap_down).astype(float)
    return island.rolling(YDAYS, min_periods=QDAYS).sum()


def f01_pab_084_gap_volume_intensity_21d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on gap-up bars / mean on non-gap bars over 21d."""
    pc = close.shift(1)
    gap = open_ > pc
    gv = volume.where(gap, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    nv = volume.where(~gap, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(gv, nv)


def f01_pab_085_gap_fill_into_prior_range_count_21d(open_: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-up bars whose low pulled back below prior close (gap filled), last 21d."""
    pc = close.shift(1)
    flag = (open_ > pc) & (low < pc)
    return flag.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_086_swing_high_count_pivot3_252d(high: pd.Series) -> pd.Series:
    """3-bar pivot-high count in last 252d (causal: confirmed one bar after)."""
    pivot = (high.shift(2) < high.shift(1)) & (high.shift(1) > high)
    return pivot.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f01_pab_087_swing_low_count_pivot3_252d(low: pd.Series) -> pd.Series:
    """3-bar pivot-low count in last 252d (causal)."""
    pivot = (low.shift(2) > low.shift(1)) & (low.shift(1) < low)
    return pivot.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f01_pab_088_higher_high_count_63d(high: pd.Series) -> pd.Series:
    """Consecutive higher-high bars (3-bar) count in last 63d."""
    hh = (high > high.shift(1)) & (high.shift(1) > high.shift(2))
    return hh.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_089_lower_high_count_63d(high: pd.Series) -> pd.Series:
    """Pivot highs below the prior 63d high — failed re-tests, count last 63d."""
    pivot = (high.shift(2) < high.shift(1)) & (high.shift(1) > high)
    prior_max = high.shift(2).rolling(QDAYS, min_periods=MDAYS).max()
    lh = pivot & (high.shift(1) < prior_max)
    return lh.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_090_higher_low_count_63d(low: pd.Series) -> pd.Series:
    """Pivot lows above the prior 63d low — bullish structure, count last 63d."""
    pivot = (low.shift(2) > low.shift(1)) & (low.shift(1) < low)
    prior_min = low.shift(2).rolling(QDAYS, min_periods=MDAYS).min()
    hl = pivot & (low.shift(1) > prior_min)
    return hl.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_091_lower_low_count_63d(low: pd.Series) -> pd.Series:
    """Pivot lows below the prior 63d low — bearish structure, count last 63d."""
    pivot = (low.shift(2) > low.shift(1)) & (low.shift(1) < low)
    prior_min = low.shift(2).rolling(QDAYS, min_periods=MDAYS).min()
    ll = pivot & (low.shift(1) < prior_min)
    return ll.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_092_swing_amplitude_decay_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21d (max-min) range / 63d (max-min) range — recent amplitude vs longer window."""
    rng21 = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    rng63 = high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(rng21, rng63)


def f01_pab_093_zigzag_compression_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of close over 63d — compression measure."""
    s = close.rolling(QDAYS, min_periods=MDAYS).std()
    m = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return s / m.replace(0, np.nan)


def f01_pab_094_trend_change_count_63d(close: pd.Series) -> pd.Series:
    """Sign flips of 21d log-return over last 63 bars — trend instability."""
    r21 = _safe_log(close).diff(MDAYS)
    sign = np.sign(r21)
    flip = (sign != sign.shift(1)) & sign.notna() & sign.shift(1).notna()
    return flip.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_095_swing_skew_to_down_63d(close: pd.Series) -> pd.Series:
    """(Down-day count - up-day count) over 63d — directional skew."""
    r = close.diff()
    up = (r > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    down = (r < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return down - up


def f01_pab_096_drawdown_from_252d_max(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close / 252d max - 1 — current drawdown depth from annual peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(close, rmax) - 1.0


def f01_pab_097_drawdown_from_63d_max(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close / 63d max - 1 — quarterly drawdown."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return _safe_div(close, rmax) - 1.0


def f01_pab_098_drawdown_from_1260d_max(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close / 5y max - 1 — multi-year drawdown."""
    rmax = high.rolling(1260, min_periods=YDAYS).max()
    return _safe_div(close, rmax) - 1.0


def f01_pab_099_days_in_drawdown_5pct_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of last 252 bars with close > 5% off the 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_dd = (close / rmax.replace(0, np.nan) < 0.95).astype(float)
    return in_dd.rolling(YDAYS, min_periods=QDAYS).sum()


def f01_pab_100_max_drawdown_to_max_runup_ratio_252d(close: pd.Series) -> pd.Series:
    """|max drawdown| / max runup over 252d — asymmetry of swings."""
    def _ratio(w):
        if np.isnan(w).any() or len(w) < MDAYS:
            return np.nan
        run_max = np.maximum.accumulate(w)
        run_min = np.minimum.accumulate(w)
        max_dd = ((w - run_max) / run_max).min()
        max_ru = ((w - run_min) / run_min).max()
        if max_ru == 0:
            return np.nan
        return abs(max_dd) / max_ru
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_ratio, raw=True)


def f01_pab_101_recovery_speed_from_63d_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """(Close - 63d_min) / (63d_min × (1 + bars_since_min)) — per-bar recovery rate."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    def _bsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    bars = low.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)
    return _safe_div(close - rmin, rmin * (bars + 1.0))


def f01_pab_102_drawdown_velocity_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """21d slope of (close/252d_max - 1) — drawdown rate."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return _rolling_slope(dd, MDAYS)


def f01_pab_103_trough_to_close_distance_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close / 63d_min - 1 — how far above recent trough."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(close, rmin) - 1.0


def f01_pab_104_drawdown_depth_zscore_504d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Current drawdown depth z-scored vs 504d historical drawdown distribution."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return _rolling_zscore(dd, 504, min_periods=YDAYS)


def f01_pab_105_underwater_curve_area_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Integral of |drawdown| over 252d — cumulative time-weighted underwater area."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    underwater = (-dd).clip(lower=0.0)
    return underwater.rolling(YDAYS, min_periods=QDAYS).sum()


def f01_pab_106_rsi14_value(close: pd.Series) -> pd.Series:
    """14-day RSI."""
    delta = close.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = (-delta).where(delta < 0, 0.0)
    avg_gain = gain.rolling(14, min_periods=WDAYS).mean()
    avg_loss = loss.rolling(14, min_periods=WDAYS).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100.0 - (100.0 / (1.0 + rs))


def f01_pab_107_rsi14_overbought_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars in last 63d with RSI(14) > 70."""
    rsi = f01_pab_106_rsi14_value(close)
    return (rsi > 70).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_108_rsi_bearish_divergence_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars with new 21d price high but RSI below 21d-prior RSI max — bearish divergence."""
    rsi = f01_pab_106_rsi14_value(close)
    px_new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    rsi_lower = rsi < rsi.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    div = (px_new_high & rsi_lower).astype(float)
    return div.rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_109_stochastic_k_value_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """14-day Stochastic %K."""
    h14 = high.rolling(14, min_periods=WDAYS).max()
    l14 = low.rolling(14, min_periods=WDAYS).min()
    return 100.0 * _safe_div(close - l14, h14 - l14)


def f01_pab_110_stochastic_overbought_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 63d with Stochastic %K > 80."""
    k = f01_pab_109_stochastic_k_value_14d(high, low, close)
    return (k > 80).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_111_williams_r_value_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """14-day Williams %R."""
    h14 = high.rolling(14, min_periods=WDAYS).max()
    l14 = low.rolling(14, min_periods=WDAYS).min()
    return -100.0 * _safe_div(h14 - close, h14 - l14)


def f01_pab_112_cci20_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """20-day Commodity Channel Index."""
    tp = (high + low + close) / 3.0
    sma_tp = tp.rolling(20, min_periods=WDAYS).mean()
    mad = (tp - sma_tp).abs().rolling(20, min_periods=WDAYS).mean()
    return (tp - sma_tp) / (0.015 * mad.replace(0, np.nan))


def f01_pab_113_roc21_zscore_252d(close: pd.Series) -> pd.Series:
    """21d rate-of-change z-scored vs 252d distribution."""
    roc = _safe_div(close, close.shift(MDAYS)) - 1.0
    return _rolling_zscore(roc, YDAYS)


def f01_pab_114_bb_top_break_count_252d(close: pd.Series) -> pd.Series:
    """Bars in last 252 where close exceeded SMA20 + 2σ — Bollinger top breaks."""
    sma = close.rolling(20, min_periods=WDAYS).mean()
    sd = close.rolling(20, min_periods=WDAYS).std()
    return (close > sma + 2.0 * sd).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f01_pab_115_macd_histogram_value(close: pd.Series) -> pd.Series:
    """Standard MACD histogram (12/26/9 EMAs)."""
    e12 = close.ewm(span=12, adjust=False, min_periods=WDAYS).mean()
    e26 = close.ewm(span=26, adjust=False, min_periods=WDAYS).mean()
    macd = e12 - e26
    signal = macd.ewm(span=9, adjust=False, min_periods=WDAYS).mean()
    return macd - signal


def f01_pab_116_realized_skew_63d(close: pd.Series) -> pd.Series:
    """63d skewness of daily log returns."""
    r = _safe_log(close).diff()
    return r.rolling(QDAYS, min_periods=MDAYS).skew()


def f01_pab_117_realized_kurtosis_63d(close: pd.Series) -> pd.Series:
    """63d excess kurtosis of daily log returns."""
    r = _safe_log(close).diff()
    return r.rolling(QDAYS, min_periods=MDAYS).kurt()


def f01_pab_118_jarque_bera_proxy_63d(close: pd.Series) -> pd.Series:
    """Jarque-Bera test statistic on 63d log returns — normality deviation."""
    r = _safe_log(close).diff()
    skew = r.rolling(QDAYS, min_periods=MDAYS).skew()
    kurt = r.rolling(QDAYS, min_periods=MDAYS).kurt()
    return (QDAYS / 6.0) * (skew ** 2 + (kurt ** 2) / 4.0)


def f01_pab_119_autocorr_lag5_returns_63d(close: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of daily log returns over 63d (weekly cycle)."""
    r = _safe_log(close).diff()
    def _ac5(w):
        if np.isnan(w).any() or len(w) < 7:
            return np.nan
        a, b = w[:-5], w[5:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_ac5, raw=True)


def f01_pab_120_variance_ratio_5_21(close: pd.Series) -> pd.Series:
    """Lo-MacKinlay variance ratio var(5d)/(5×var(1d)) over 252d — momentum vs mean-rev."""
    r1 = _safe_log(close).diff()
    r5 = _safe_log(close).diff(WDAYS)
    var_1 = r1.rolling(YDAYS, min_periods=QDAYS).var()
    var_5 = r5.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(var_5, 5.0 * var_1)


def f01_pab_121_hurst_exponent_proxy_63d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent proxy on 63d log returns."""
    r = _safe_log(close).diff()
    def _hurst(w):
        if np.isnan(w).any():
            return np.nan
        ws = w - w.mean()
        cw = np.cumsum(ws)
        R = cw.max() - cw.min()
        S = w.std()
        if S == 0 or R == 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(w)))
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_hurst, raw=True)


def f01_pab_122_tail_ratio_99_to_1_63d(close: pd.Series) -> pd.Series:
    """ret_99th_percentile / |ret_1st_percentile| over 63d."""
    r = _safe_log(close).diff()
    p99 = r.rolling(QDAYS, min_periods=MDAYS).quantile(0.99)
    p01 = r.rolling(QDAYS, min_periods=MDAYS).quantile(0.01)
    return _safe_div(p99, p01.abs())


def f01_pab_123_expected_shortfall_5pct_63d(close: pd.Series) -> pd.Series:
    """Mean of worst 5% of 63d daily log returns."""
    r = _safe_log(close).diff()
    def _es(w):
        if np.isnan(w).any():
            return np.nan
        thresh = np.quantile(w, 0.05)
        tail = w[w <= thresh]
        if len(tail) == 0:
            return np.nan
        return float(tail.mean())
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_es, raw=True)


def f01_pab_124_arch_test_proxy_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of SQUARED log returns over 63d — ARCH/volatility-clustering."""
    r2 = (_safe_log(close).diff()) ** 2
    def _ac1(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        a, b = w[:-1], w[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return r2.rolling(QDAYS, min_periods=MDAYS).apply(_ac1, raw=True)


def f01_pab_125_left_tail_dominance_63d(close: pd.Series) -> pd.Series:
    """Sum |negative returns| / sum |all returns| over 63d — downside concentration."""
    r = _safe_log(close).diff()
    neg = (-r).where(r < 0, 0.0)
    return _safe_div(neg.rolling(QDAYS, min_periods=MDAYS).sum(), r.abs().rolling(QDAYS, min_periods=MDAYS).sum())


def f01_pab_126_blowoff_top_composite_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max 21d-rolling 0-4 composite score: at high + vol spike + range expand + weak close."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_high = (high / rmax.replace(0, np.nan) >= 0.98).astype(float)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_spike = (volume > 2.0 * v21).astype(float)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS)
    range_exp = (tr > 2.0 * atr).astype(float)
    rng = (high - low).replace(0, np.nan)
    weak_close = (((high - close) / rng) > 0.5).astype(float)
    score = near_high + vol_spike + range_exp + weak_close
    return score.rolling(MDAYS, min_periods=WDAYS).max()


def f01_pab_127_exhaustion_signature_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 63d of (RSI>70) + (vol_21<vol_252) — exhaustion bar count."""
    rsi = f01_pab_106_rsi14_value(close)
    high_rsi = (rsi > 70).astype(float)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    vol_decay = (v21 < v252).astype(float)
    score = high_rsi + vol_decay
    return score.rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_128_price_volume_divergence_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """|z-score(close, 252d) - z-score(OBV, 252d)| — absolute price-vs-OBV divergence."""
    direction = np.sign(close.diff()).fillna(0.0)
    obv = (direction * volume).cumsum()
    return (_rolling_zscore(close, YDAYS) - _rolling_zscore(obv, YDAYS)).abs()


def f01_pab_129_failed_breakout_close_below_count_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars where prior bar closed above 252d max but today closes back below — failed breakout."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    closed_above_yesterday = (close.shift(1) > prior_max.shift(1))
    below_today = (close < prior_max)
    return (closed_above_yesterday & below_today).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_130_churn_index_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of TR over 21d / |net 21d move| — high churn = high range, low displacement."""
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(MDAYS, min_periods=WDAYS).sum()
    net = (close - close.shift(MDAYS)).abs()
    return _safe_div(sum_tr, net)


def f01_pab_131_running_max_consolidation_days_21d(high: pd.Series) -> pd.Series:
    """Current streak of bars where the 21d rolling max has not advanced."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    same = (rmax21 == rmax21.shift(1)).astype(float)
    grp = (same == 0).cumsum()
    return same.groupby(grp).cumsum()


def f01_pab_132_distribution_volume_intensity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (252d) of down-day volume share over 63d."""
    down = (close.diff() < 0).astype(float)
    down_vol = (down * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    total = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_zscore(_safe_div(down_vol, total), YDAYS)


def f01_pab_133_accumulation_distribution_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-day volume sum / down-day volume sum over 252d."""
    diff = close.diff()
    up_vol = (volume.where(diff > 0, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    down_vol = (volume.where(diff < 0, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(up_vol, down_vol)


def f01_pab_134_drawdown_curve_convexity_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Quadratic coefficient of drawdown-curve polyfit over 63d — concave=accelerating-fall."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    def _curv(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            c2 = np.polyfit(x, w, 2)[0]
        except Exception:
            return np.nan
        return c2
    return dd.rolling(QDAYS, min_periods=MDAYS).apply(_curv, raw=True)


def f01_pab_135_peak_proximity_decay_rate_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Daily change in (close / 252d_max), averaged over 21d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    proximity = close / rmax.replace(0, np.nan)
    return proximity.diff(MDAYS) / MDAYS


def f01_pab_136_above_avg_volume_share_63d(volume: pd.Series) -> pd.Series:
    """Share of last 63 bars with volume above own 21d SMA."""
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return (volume > v21).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f01_pab_137_range_expansion_skew_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d skew of True Range distribution — heavy upper tail = recent expansion."""
    tr = _true_range(high, low, close)
    return tr.rolling(MDAYS, min_periods=WDAYS).skew()


def f01_pab_138_velocity_at_high_zscore_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """21d close-slope z-score conditioned on near-252d-high bars only."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    slope = close.diff(MDAYS) / MDAYS
    slope_near = slope.where(near, np.nan)
    return _rolling_zscore(slope_near, YDAYS, min_periods=QDAYS)


def f01_pab_139_opening_range_breakdown_count_21d(open_: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in last 21 where open > prior high (real gap) AND close < open (intraday reversal)."""
    ph = high.shift(1)
    flag = (open_ > ph) & (close < open_)
    return flag.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_140_close_below_open_after_new_high_count_21d(open_: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in last 21 that set a new 252d high but closed below their open."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    bearish = close < open_
    return (new_high & bearish).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_141_truncation_index_21_vs_63d(close: pd.Series) -> pd.Series:
    """Close-only 21d range / 63d range — recent rally truncation."""
    r21 = close.rolling(MDAYS, min_periods=WDAYS).max() - close.rolling(MDAYS, min_periods=WDAYS).min()
    r63 = close.rolling(QDAYS, min_periods=MDAYS).max() - close.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(r21, r63)


def f01_pab_142_log_return_skew_sign_63d(close: pd.Series) -> pd.Series:
    """Sign of 63d log-return skewness — directional asymmetry indicator."""
    r = _safe_log(close).diff()
    return np.sign(r.rolling(QDAYS, min_periods=MDAYS).skew())


def f01_pab_143_kaufman_efficiency_ratio_63d(close: pd.Series) -> pd.Series:
    """|close - close[63 ago]| / Σ |daily changes| over 63d — Kaufman Efficiency Ratio."""
    net = (close - close.shift(QDAYS)).abs()
    moves = close.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net, moves)


def f01_pab_144_trend_resistance_score_63d(close: pd.Series) -> pd.Series:
    """Count over 63d of bars where 63d trend is up but close is below 21d max — resistance hits."""
    trend_up = (close > close.shift(QDAYS)).astype(float)
    below_21_max = (close < close.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    return (trend_up * below_21_max).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_145_selling_pressure_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Σ(vol × |neg-return|) / Σ(vol × pos-return) over 21d."""
    r = close.pct_change()
    neg = (volume * r.where(r < 0, 0.0).abs()).rolling(MDAYS, min_periods=WDAYS).sum()
    pos = (volume * r.where(r > 0, 0.0)).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(neg, pos)


def f01_pab_146_cumulative_volume_post_peak_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21d volume occurring AFTER the within-window peak-vol bar (causal)."""
    def _share(w):
        if np.isnan(w).any():
            return np.nan
        idx_peak = int(np.argmax(w))
        total = w.sum()
        if total == 0:
            return np.nan
        return float(w[idx_peak + 1:].sum() / total)
    return volume.rolling(MDAYS, min_periods=WDAYS).apply(_share, raw=True)


def f01_pab_147_drawdown_new_low_count_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Number of running-min advances of drawdown depth within 252d window."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    def _count(w):
        if np.isnan(w).any() or len(w) < MDAYS:
            return np.nan
        return float((w == np.minimum.accumulate(w)).sum() - 1.0)
    return dd.rolling(YDAYS, min_periods=QDAYS).apply(_count, raw=True)


def f01_pab_148_log_price_acceleration_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 2nd-diff of log-price over 63d distribution."""
    d2 = _safe_log(close).diff().diff()
    return _rolling_zscore(d2, QDAYS)


def f01_pab_149_terminal_thrust_count_21d(close: pd.Series) -> pd.Series:
    """Bars in last 21 with daily log return > 2× (252d std of log returns) — blowoff thrusts."""
    r = _safe_log(close).diff()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    thrust = (r > 2.0 * sd).astype(float)
    return thrust.rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_150_blowoff_climax_aggregate_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max 21d-rolling 0-5 climax score: at high + vol spike + range expand + up close + upper wick."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = (high / rmax.replace(0, np.nan) >= 0.99).astype(float)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    vol_spike = (volume > 2.0 * v21).astype(float)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS)
    big_range = (tr > 1.5 * atr).astype(float)
    up_close = (close > close.shift(1)).astype(float)
    rng = (high - low).replace(0, np.nan)
    upper_wick_dom = (((high - close) / rng) > 0.4).astype(float)
    score = at_high + vol_spike + big_range + up_close + upper_wick_dom
    return score.rolling(MDAYS, min_periods=WDAYS).max()


# ============================================================
#                        REGISTRY
# ============================================================

PEAK_AND_BLOWOFF_BASE_REGISTRY_076_150 = {
    "f01_pab_076_gap_up_count_21d": {"inputs": ["open", "close"], "func": f01_pab_076_gap_up_count_21d},
    "f01_pab_077_gap_up_total_magnitude_21d": {"inputs": ["open", "close"], "func": f01_pab_077_gap_up_total_magnitude_21d},
    "f01_pab_078_gap_up_filled_count_21d": {"inputs": ["open", "close"], "func": f01_pab_078_gap_up_filled_count_21d},
    "f01_pab_079_gap_down_count_21d": {"inputs": ["open", "close"], "func": f01_pab_079_gap_down_count_21d},
    "f01_pab_080_exhaustion_gap_signature_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f01_pab_080_exhaustion_gap_signature_21d},
    "f01_pab_081_breakaway_gap_count_63d": {"inputs": ["open", "high"], "func": f01_pab_081_breakaway_gap_count_63d},
    "f01_pab_082_runaway_gap_streak_max_21d": {"inputs": ["open", "close"], "func": f01_pab_082_runaway_gap_streak_max_21d},
    "f01_pab_083_island_top_count_252d": {"inputs": ["open", "close"], "func": f01_pab_083_island_top_count_252d},
    "f01_pab_084_gap_volume_intensity_21d": {"inputs": ["open", "close", "volume"], "func": f01_pab_084_gap_volume_intensity_21d},
    "f01_pab_085_gap_fill_into_prior_range_count_21d": {"inputs": ["open", "low", "close"], "func": f01_pab_085_gap_fill_into_prior_range_count_21d},
    "f01_pab_086_swing_high_count_pivot3_252d": {"inputs": ["high"], "func": f01_pab_086_swing_high_count_pivot3_252d},
    "f01_pab_087_swing_low_count_pivot3_252d": {"inputs": ["low"], "func": f01_pab_087_swing_low_count_pivot3_252d},
    "f01_pab_088_higher_high_count_63d": {"inputs": ["high"], "func": f01_pab_088_higher_high_count_63d},
    "f01_pab_089_lower_high_count_63d": {"inputs": ["high"], "func": f01_pab_089_lower_high_count_63d},
    "f01_pab_090_higher_low_count_63d": {"inputs": ["low"], "func": f01_pab_090_higher_low_count_63d},
    "f01_pab_091_lower_low_count_63d": {"inputs": ["low"], "func": f01_pab_091_lower_low_count_63d},
    "f01_pab_092_swing_amplitude_decay_63d": {"inputs": ["high", "low"], "func": f01_pab_092_swing_amplitude_decay_63d},
    "f01_pab_093_zigzag_compression_63d": {"inputs": ["close"], "func": f01_pab_093_zigzag_compression_63d},
    "f01_pab_094_trend_change_count_63d": {"inputs": ["close"], "func": f01_pab_094_trend_change_count_63d},
    "f01_pab_095_swing_skew_to_down_63d": {"inputs": ["close"], "func": f01_pab_095_swing_skew_to_down_63d},
    "f01_pab_096_drawdown_from_252d_max": {"inputs": ["close", "high"], "func": f01_pab_096_drawdown_from_252d_max},
    "f01_pab_097_drawdown_from_63d_max": {"inputs": ["close", "high"], "func": f01_pab_097_drawdown_from_63d_max},
    "f01_pab_098_drawdown_from_1260d_max": {"inputs": ["close", "high"], "func": f01_pab_098_drawdown_from_1260d_max},
    "f01_pab_099_days_in_drawdown_5pct_252d": {"inputs": ["close", "high"], "func": f01_pab_099_days_in_drawdown_5pct_252d},
    "f01_pab_100_max_drawdown_to_max_runup_ratio_252d": {"inputs": ["close"], "func": f01_pab_100_max_drawdown_to_max_runup_ratio_252d},
    "f01_pab_101_recovery_speed_from_63d_min": {"inputs": ["close", "low"], "func": f01_pab_101_recovery_speed_from_63d_min},
    "f01_pab_102_drawdown_velocity_21d": {"inputs": ["close", "high"], "func": f01_pab_102_drawdown_velocity_21d},
    "f01_pab_103_trough_to_close_distance_63d": {"inputs": ["close", "low"], "func": f01_pab_103_trough_to_close_distance_63d},
    "f01_pab_104_drawdown_depth_zscore_504d": {"inputs": ["close", "high"], "func": f01_pab_104_drawdown_depth_zscore_504d},
    "f01_pab_105_underwater_curve_area_252d": {"inputs": ["close", "high"], "func": f01_pab_105_underwater_curve_area_252d},
    "f01_pab_106_rsi14_value": {"inputs": ["close"], "func": f01_pab_106_rsi14_value},
    "f01_pab_107_rsi14_overbought_count_63d": {"inputs": ["close"], "func": f01_pab_107_rsi14_overbought_count_63d},
    "f01_pab_108_rsi_bearish_divergence_count_63d": {"inputs": ["close", "high"], "func": f01_pab_108_rsi_bearish_divergence_count_63d},
    "f01_pab_109_stochastic_k_value_14d": {"inputs": ["high", "low", "close"], "func": f01_pab_109_stochastic_k_value_14d},
    "f01_pab_110_stochastic_overbought_count_63d": {"inputs": ["high", "low", "close"], "func": f01_pab_110_stochastic_overbought_count_63d},
    "f01_pab_111_williams_r_value_14d": {"inputs": ["high", "low", "close"], "func": f01_pab_111_williams_r_value_14d},
    "f01_pab_112_cci20_value": {"inputs": ["high", "low", "close"], "func": f01_pab_112_cci20_value},
    "f01_pab_113_roc21_zscore_252d": {"inputs": ["close"], "func": f01_pab_113_roc21_zscore_252d},
    "f01_pab_114_bb_top_break_count_252d": {"inputs": ["close"], "func": f01_pab_114_bb_top_break_count_252d},
    "f01_pab_115_macd_histogram_value": {"inputs": ["close"], "func": f01_pab_115_macd_histogram_value},
    "f01_pab_116_realized_skew_63d": {"inputs": ["close"], "func": f01_pab_116_realized_skew_63d},
    "f01_pab_117_realized_kurtosis_63d": {"inputs": ["close"], "func": f01_pab_117_realized_kurtosis_63d},
    "f01_pab_118_jarque_bera_proxy_63d": {"inputs": ["close"], "func": f01_pab_118_jarque_bera_proxy_63d},
    "f01_pab_119_autocorr_lag5_returns_63d": {"inputs": ["close"], "func": f01_pab_119_autocorr_lag5_returns_63d},
    "f01_pab_120_variance_ratio_5_21": {"inputs": ["close"], "func": f01_pab_120_variance_ratio_5_21},
    "f01_pab_121_hurst_exponent_proxy_63d": {"inputs": ["close"], "func": f01_pab_121_hurst_exponent_proxy_63d},
    "f01_pab_122_tail_ratio_99_to_1_63d": {"inputs": ["close"], "func": f01_pab_122_tail_ratio_99_to_1_63d},
    "f01_pab_123_expected_shortfall_5pct_63d": {"inputs": ["close"], "func": f01_pab_123_expected_shortfall_5pct_63d},
    "f01_pab_124_arch_test_proxy_63d": {"inputs": ["close"], "func": f01_pab_124_arch_test_proxy_63d},
    "f01_pab_125_left_tail_dominance_63d": {"inputs": ["close"], "func": f01_pab_125_left_tail_dominance_63d},
    "f01_pab_126_blowoff_top_composite_21d": {"inputs": ["high", "low", "close", "volume"], "func": f01_pab_126_blowoff_top_composite_21d},
    "f01_pab_127_exhaustion_signature_score_63d": {"inputs": ["close", "volume"], "func": f01_pab_127_exhaustion_signature_score_63d},
    "f01_pab_128_price_volume_divergence_zscore_63d": {"inputs": ["close", "volume"], "func": f01_pab_128_price_volume_divergence_zscore_63d},
    "f01_pab_129_failed_breakout_close_below_count_21d": {"inputs": ["close", "high"], "func": f01_pab_129_failed_breakout_close_below_count_21d},
    "f01_pab_130_churn_index_21d": {"inputs": ["high", "low", "close"], "func": f01_pab_130_churn_index_21d},
    "f01_pab_131_running_max_consolidation_days_21d": {"inputs": ["high"], "func": f01_pab_131_running_max_consolidation_days_21d},
    "f01_pab_132_distribution_volume_intensity_63d": {"inputs": ["close", "volume"], "func": f01_pab_132_distribution_volume_intensity_63d},
    "f01_pab_133_accumulation_distribution_ratio_252d": {"inputs": ["close", "volume"], "func": f01_pab_133_accumulation_distribution_ratio_252d},
    "f01_pab_134_drawdown_curve_convexity_63d": {"inputs": ["close", "high"], "func": f01_pab_134_drawdown_curve_convexity_63d},
    "f01_pab_135_peak_proximity_decay_rate_21d": {"inputs": ["close", "high"], "func": f01_pab_135_peak_proximity_decay_rate_21d},
    "f01_pab_136_above_avg_volume_share_63d": {"inputs": ["volume"], "func": f01_pab_136_above_avg_volume_share_63d},
    "f01_pab_137_range_expansion_skew_21d": {"inputs": ["high", "low", "close"], "func": f01_pab_137_range_expansion_skew_21d},
    "f01_pab_138_velocity_at_high_zscore_63d": {"inputs": ["close", "high"], "func": f01_pab_138_velocity_at_high_zscore_63d},
    "f01_pab_139_opening_range_breakdown_count_21d": {"inputs": ["open", "high", "close"], "func": f01_pab_139_opening_range_breakdown_count_21d},
    "f01_pab_140_close_below_open_after_new_high_count_21d": {"inputs": ["open", "high", "close"], "func": f01_pab_140_close_below_open_after_new_high_count_21d},
    "f01_pab_141_truncation_index_21_vs_63d": {"inputs": ["close"], "func": f01_pab_141_truncation_index_21_vs_63d},
    "f01_pab_142_log_return_skew_sign_63d": {"inputs": ["close"], "func": f01_pab_142_log_return_skew_sign_63d},
    "f01_pab_143_kaufman_efficiency_ratio_63d": {"inputs": ["close"], "func": f01_pab_143_kaufman_efficiency_ratio_63d},
    "f01_pab_144_trend_resistance_score_63d": {"inputs": ["close"], "func": f01_pab_144_trend_resistance_score_63d},
    "f01_pab_145_selling_pressure_intensity_21d": {"inputs": ["close", "volume"], "func": f01_pab_145_selling_pressure_intensity_21d},
    "f01_pab_146_cumulative_volume_post_peak_share_21d": {"inputs": ["volume"], "func": f01_pab_146_cumulative_volume_post_peak_share_21d},
    "f01_pab_147_drawdown_new_low_count_252d": {"inputs": ["close", "high"], "func": f01_pab_147_drawdown_new_low_count_252d},
    "f01_pab_148_log_price_acceleration_zscore_63d": {"inputs": ["close"], "func": f01_pab_148_log_price_acceleration_zscore_63d},
    "f01_pab_149_terminal_thrust_count_21d": {"inputs": ["close"], "func": f01_pab_149_terminal_thrust_count_21d},
    "f01_pab_150_blowoff_climax_aggregate_21d": {"inputs": ["high", "low", "close", "volume"], "func": f01_pab_150_blowoff_climax_aggregate_21d},
}
