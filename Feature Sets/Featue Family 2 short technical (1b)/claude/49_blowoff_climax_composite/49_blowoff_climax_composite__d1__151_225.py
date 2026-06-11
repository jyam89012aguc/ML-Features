"""blowoff_climax_composite d1 features 151-225 — Pipeline 1b-technical.

Gap-fill extension. New angles distinct from 001-150:
- pre-climax compression/squeeze-and-release composites (BB squeeze, low-vol-then-spike)
- multi-day climax sequences (3-day / 5-day cumulative blowoff bars)
- candle-pattern composites at peak (shooting star, gravestone doji, etc.)
- statistical extreme composites (z-score-based, percentile-based)
- sentiment / FOMO composites (extreme up-bias, gap clusters)
- failed-climax / reversal patterns (failed breakouts, false new highs)
- cross-indicator divergence composites (RSI div + AD div + new high)
- new final composite metrics

Bucket O: Pre-climax setup (151-160).
Bucket P: Multi-day climax patterns (161-170).
Bucket Q: Candle-pattern composites at climax (171-180).
Bucket R: Statistical extreme composites (181-189).
Bucket S: Sentiment / FOMO composites (190-199).
Bucket T: Failed-climax / reversal patterns (200-210).
Bucket U: Cross-indicator composites (211-220).
Bucket V: Final composite metrics (221-225).

Inputs: SEP OHLCV. Self-contained; PIT-clean.
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


def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0); dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(au, ad))


def _clv(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _new_high_21(high):
    return high >= high.rolling(MDAYS, min_periods=WDAYS).max()


def _new_high_63(high):
    return high >= high.rolling(QDAYS, min_periods=MDAYS).max()


def _new_high_252(high):
    return high >= high.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket O — Pre-climax setup (151-160)
# ============================================================


def f49_bcco_151_bb_squeeze_lowest_decile_then_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if BB bandwidth was in lowest 10% past 252d at any point in past 10 bars AND new 21d high today — squeeze-then-breakout."""
    sd = close.rolling(20, min_periods=10).std()
    bw = sd * 4.0
    q10 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    squeeze_recent = (bw <= q10).astype(float).rolling(10, min_periods=1).max() > 0
    return ((squeeze_recent & _new_high_21(high)).astype(float).where(q10.notna(), np.nan)).diff()


def f49_bcco_152_bb_squeeze_lowest_5pct_then_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Extreme squeeze (5th-pct bandwidth) in past 10 bars AND new 21d high — extreme squeeze-and-go."""
    sd = close.rolling(20, min_periods=10).std()
    bw = sd * 4.0
    q5 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    squeeze_recent = (bw <= q5).astype(float).rolling(10, min_periods=1).max() > 0
    return ((squeeze_recent & _new_high_21(high)).astype(float).where(q5.notna(), np.nan)).diff()


def f49_bcco_153_5plus_nr7_in_21_then_breakout_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if 5+ NR7 bars in past 21 AND new 21d high today — extended-compression-then-breakout."""
    r = high - low
    rm = r.rolling(7, min_periods=7).min()
    nr7_count = (r == rm).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return (((nr7_count >= 5) & _new_high_21(high)).astype(float).where(rm.notna(), np.nan)).diff()


def f49_bcco_154_21d_vol_lowest_quartile_then_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d return-std was in lowest quartile of 252d AND new 252d high today — quiet-then-loud breakout."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    q25 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (((rv <= q25) & _new_high_252(high)).astype(float).where(q25.notna(), np.nan)).diff()


def f49_bcco_155_ttm_squeeze_release_with_new_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TTM-squeeze active 5+ bars ago AND today BB exits Keltner AND new 21d high — TTM-release climax."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    e = _ema(close, 20)
    a = _atr(high, low, close, 20)
    bb_u = m + 2.0 * sd; bb_l = m - 2.0 * sd
    k_u = e + 2.0 * a; k_l = e - 2.0 * a
    squeeze = (bb_u < k_u) & (bb_l > k_l)
    squeeze_5_ago = squeeze.shift(5).rolling(5, min_periods=1).max() > 0
    released_now = ~squeeze
    return ((squeeze_5_ago & released_now & _new_high_21(high)).astype(float).where(sd.notna() & a.notna(), np.nan)).diff()


def f49_bcco_156_5bar_vol_zscore_over_3_and_new_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 5-bar volume sum z-score (252d) > 3 AND new 21d high — sudden vol surge with breakout."""
    v5 = volume.rolling(WDAYS, min_periods=2).sum()
    vz = _rolling_zscore(v5, YDAYS, min_periods=QDAYS)
    return (((vz > 3.0) & _new_high_21(high)).astype(float).where(vz.notna(), np.nan)).diff()


def f49_bcco_157_5d_return_zscore_over_2_and_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5d return z-score (252d) > 2 AND new 21d high — extreme-weekly-gain breakout."""
    r5 = close.pct_change(WDAYS)
    rz = _rolling_zscore(r5, YDAYS, min_periods=QDAYS)
    return (((rz > 2.0) & _new_high_21(high)).astype(float).where(rz.notna(), np.nan)).diff()


def f49_bcco_158_runaway_gap_with_new_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if gap-up > 2% AND close in top-25% of day's range AND new 252d high — runaway-gap climax."""
    pc = close.shift(1)
    gap = _safe_div(open_ - pc, pc)
    pos = _safe_div(close - low, high - low)
    return (((gap > 0.02) & (pos > 0.75) & _new_high_252(high)).astype(float).where(gap.notna(), np.nan)).diff()


def f49_bcco_159_inside_day_before_new_252d_high_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if prior bar was an inside day (H<H_prev, L>L_prev) AND today is new 252d high — compression-to-breakout."""
    inside = (high.shift(1) < high.shift(2)) & (low.shift(1) > low.shift(2))
    return ((inside & _new_high_252(high)).astype(float).where(high.shift(2).notna(), np.nan)).diff()


def f49_bcco_160_5bar_vol_sum_zscore_and_5bar_return_z_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 5-bar vol sum z > 2 AND 5-bar return z > 2 — joint vol+return-spike pre-climax."""
    v5 = volume.rolling(WDAYS, min_periods=2).sum()
    r5 = close.pct_change(WDAYS)
    vz = _rolling_zscore(v5, YDAYS, min_periods=QDAYS)
    rz = _rolling_zscore(r5, YDAYS, min_periods=QDAYS)
    return (((vz > 2.0) & (rz > 2.0)).astype(float).where(vz.notna() & rz.notna(), np.nan)).diff()


def f49_bcco_161_3_consecutive_new_252d_highs_d1(high: pd.Series) -> pd.Series:
    """1 if today, yesterday, and day before yesterday were all new 252d highs."""
    nh = _new_high_252(high)
    return ((nh & nh.shift(1) & nh.shift(2)).astype(float).where(nh.notna(), np.nan)).diff()


def f49_bcco_162_5_consecutive_new_252d_highs_d1(high: pd.Series) -> pd.Series:
    """1 if 5 consecutive new 252d highs — sustained-breakout climax."""
    nh = _new_high_252(high)
    return ((nh & nh.shift(1) & nh.shift(2) & nh.shift(3) & nh.shift(4)).astype(float).where(nh.notna(), np.nan)).diff()


def f49_bcco_163_3_consecutive_wide_range_and_new_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3 consecutive TR > 2*ATR21 bars AND new 21d high today — sustained-wide-range climax."""
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    wide_3 = (rng_ratio > 2.0) & (rng_ratio.shift(1) > 2.0) & (rng_ratio.shift(2) > 2.0)
    return ((wide_3 & _new_high_21(high)).astype(float).where(rng_ratio.notna(), np.nan)).diff()


def f49_bcco_164_3day_climax_each_bar_3plus_signals_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if each of past 3 bars had >= 3 of {new 21d high, vol>2x avg, RSI>70, TR>2*ATR21, CLV>0.5} signals firing."""
    r = _rsi(close, 14)
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    s = ((_new_high_21(high).astype(float).fillna(0))
         + ((v_ratio > 2.0).astype(float).fillna(0))
         + ((r > 70.0).astype(float).fillna(0))
         + ((rng_ratio > 2.0).astype(float).fillna(0))
         + ((_clv(high, low, close) > 0.5).astype(float).fillna(0)))
    return (((s >= 3) & (s.shift(1) >= 3) & (s.shift(2) >= 3)).astype(float).where(r.notna(), np.nan)).diff()


def f49_bcco_165_5day_climax_each_bar_3plus_signals_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if each of past 5 bars had >= 3 multi-signals — 5-day sustained climax regime."""
    r = _rsi(close, 14)
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    s = ((_new_high_21(high).astype(float).fillna(0))
         + ((v_ratio > 2.0).astype(float).fillna(0))
         + ((r > 70.0).astype(float).fillna(0))
         + ((rng_ratio > 2.0).astype(float).fillna(0))
         + ((_clv(high, low, close) > 0.5).astype(float).fillna(0)))
    return (((s >= 3) & (s.shift(1) >= 3) & (s.shift(2) >= 3) & (s.shift(3) >= 3) & (s.shift(4) >= 3)).astype(float).where(r.notna(), np.nan)).diff()


def f49_bcco_166_10day_cum_return_over_50pct_d1(close: pd.Series) -> pd.Series:
    """1 if 10-day cumulative return > 50% — extreme weekly run."""
    return ((close.pct_change(10) > 0.50).astype(float).where(close.pct_change(10).notna(), np.nan)).diff()


def f49_bcco_167_10day_cum_return_over_100pct_d1(close: pd.Series) -> pd.Series:
    """1 if 10-day cumulative return > 100% — climax-level run (rare)."""
    return ((close.pct_change(10) > 1.0).astype(float).where(close.pct_change(10).notna(), np.nan)).diff()


def f49_bcco_168_21day_cum_return_over_50pct_with_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d cum return > 50% AND new 252d high — monthly-strength + annual-peak."""
    r21 = close.pct_change(MDAYS)
    return (((r21 > 0.50) & _new_high_252(high)).astype(float).where(r21.notna(), np.nan)).diff()


def f49_bcco_169_vol_acceleration_5bar_over_prior_5bar_d1(volume: pd.Series) -> pd.Series:
    """1 if 5-bar vol sum > prior-5-bar vol sum > prior-prior-5-bar vol sum — vol acceleration."""
    v5 = volume.rolling(WDAYS, min_periods=2).sum()
    return (((v5 > v5.shift(WDAYS)) & (v5.shift(WDAYS) > v5.shift(2 * WDAYS))).astype(float).where(v5.shift(2 * WDAYS).notna(), np.nan)).diff()


def f49_bcco_170_3_consecutive_strong_close_and_new_21d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if past 3 bars all had CLV > 0.7 AND today is new 21d high — sustained-close-strength + breakout."""
    cl = _clv(high, low, close)
    s3 = (cl > 0.7) & (cl.shift(1) > 0.7) & (cl.shift(2) > 0.7)
    return ((s3 & _new_high_21(high)).astype(float).where(cl.notna(), np.nan)).diff()


def f49_bcco_171_shooting_star_at_new_21d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high AND small body (|C-O| < 0.3 * (H-L)) AND long upper shadow (H - max(C,O) > 2*body)."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    upper = high - pd.concat([open_, close], axis=1).max(axis=1)
    small_body = body < 0.3 * rng
    long_upper = upper > 2.0 * body
    return ((_new_high_21(high) & small_body & long_upper).astype(float).where(rng.notna(), np.nan)).diff()


def f49_bcco_172_hanging_man_at_new_21d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high AND small body AND long lower shadow > 2*body (hanging-man pattern at top)."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    lower = pd.concat([open_, close], axis=1).min(axis=1) - low
    small_body = body < 0.3 * rng
    long_lower = lower > 2.0 * body
    return ((_new_high_21(high) & small_body & long_lower).astype(float).where(rng.notna(), np.nan)).diff()


def f49_bcco_173_dark_cloud_cover_after_new_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high (bullish), today opens above prior high, and closes below prior bar's midpoint."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax_prev)
    prior_bullish = close.shift(1) > open_.shift(1)
    open_above = open_ > high.shift(1)
    prior_mid = (high.shift(1) + low.shift(1)) / 2.0
    return ((prior_new_high & prior_bullish & open_above & (close < prior_mid)).astype(float).where(rmax_prev.notna(), np.nan)).diff()


def f49_bcco_174_evening_star_at_new_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """3-bar evening star: bar t-2 strong-bull, bar t-1 doji/small-body AT new high, bar t bearish-wide closing below t-2 midpoint."""
    body2 = (close.shift(2) - open_.shift(2))
    body1 = (close.shift(1) - open_.shift(1)).abs()
    rng1 = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    rmax2 = high.shift(2).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax2)
    bull_2 = body2 > 0.5 * (high.shift(2) - low.shift(2))
    small_1 = body1 < 0.3 * rng1
    mid_2 = (high.shift(2) + low.shift(2)) / 2.0
    bear_now = (close < open_) & (close < mid_2)
    return ((bull_2 & small_1 & prior_new_high & bear_now).astype(float).where(rng1.notna(), np.nan)).diff()


def f49_bcco_175_bearish_harami_at_new_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high (bullish), today is bearish AND today's body is inside prior bar's body."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax_prev)
    prior_bullish = close.shift(1) > open_.shift(1)
    bear_today = close < open_
    today_inside_prior_body = (open_ < close.shift(1)) & (close > open_.shift(1))
    return ((prior_new_high & prior_bullish & bear_today & today_inside_prior_body).astype(float).where(rmax_prev.notna(), np.nan)).diff()


def f49_bcco_176_tweezer_top_2bar_d1(high: pd.Series) -> pd.Series:
    """1 if today's high equals prior bar's high (tolerance 0.5%) — tweezer-top reversal level."""
    h_diff = (high - high.shift(1)).abs() / high.shift(1)
    return ((h_diff < 0.005).astype(float).where(high.shift(1).notna(), np.nan)).diff()


def f49_bcco_177_long_upper_shadow_3x_body_at_new_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND upper shadow > 3x body — strong-rejection candle at peak."""
    body = (close - open_).abs()
    upper = high - pd.concat([open_, close], axis=1).max(axis=1)
    return ((_new_high_252(high) & (upper > 3.0 * body)).astype(float).where(body.notna(), np.nan)).diff()


def f49_bcco_178_gravestone_doji_at_new_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND open=close=low (within 1% tolerance) — gravestone doji top signature."""
    body_pct = (close - open_).abs() / close
    low_pct = (open_ - low) / close
    cond = (body_pct < 0.005) & (low_pct < 0.005)
    return ((_new_high_252(high) & cond).astype(float).where(low.notna(), np.nan)).diff()


def f49_bcco_179_three_white_soldiers_then_bearish_d1(open_: pd.Series, close: pd.Series) -> pd.Series:
    """1 if past 3 bars all strong-bullish (C>O AND body>0.5x prior body) AND today bearish (C<O) — 3WS then reversal."""
    body3 = (close.shift(3) - open_.shift(3))
    body2 = (close.shift(2) - open_.shift(2))
    body1 = (close.shift(1) - open_.shift(1))
    three_white = (body3 > 0) & (body2 > body3 * 0.5) & (body1 > body2 * 0.5)
    bear_today = close < open_
    return ((three_white & bear_today).astype(float).where(body3.notna(), np.nan)).diff()


def f49_bcco_180_inverted_hammer_at_new_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND small body near low of bar AND long upper wick — inverted hammer (rejection)."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    upper = high - pd.concat([open_, close], axis=1).max(axis=1)
    lower = pd.concat([open_, close], axis=1).min(axis=1) - low
    small_body = body < 0.3 * rng
    body_near_low = lower < 0.5 * body
    long_upper = upper > 2.0 * body
    return ((_new_high_252(high) & small_body & body_near_low & long_upper).astype(float).where(rng.notna(), np.nan)).diff()


def f49_bcco_181_21d_return_zscore_over_3_and_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if z-score (252d) of 21d return > 3 AND new 252d high — extreme-monthly-strength + peak."""
    rz = _rolling_zscore(close.pct_change(MDAYS), YDAYS, min_periods=QDAYS)
    return (((rz > 3.0) & _new_high_252(high)).astype(float).where(rz.notna(), np.nan)).diff()


def f49_bcco_182_5d_vol_zscore_over_3_and_new_252d_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if z-score (252d) of 5-bar vol sum > 3 AND new 252d high."""
    vz = _rolling_zscore(volume.rolling(WDAYS, min_periods=2).sum(), YDAYS, min_periods=QDAYS)
    return (((vz > 3.0) & _new_high_252(high)).astype(float).where(vz.notna(), np.nan)).diff()


def f49_bcco_183_sharpe_3_and_atr_pct_rank_90_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d sharpe > 3 AND ATR21 pct rank > 90 (vol high too) — high-return + high-vol regime."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    sh = _safe_div(mn, sd)
    apr = _atr(high, low, close, MDAYS).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (((sh > 3.0) & (apr > 0.90)).astype(float).where(sh.notna() & apr.notna(), np.nan)).diff()


def f49_bcco_184_rsi_over_95_and_vol_z_over_2_and_new_high_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if RSI > 95 AND vol z > 2 AND new 252d high — peak-momentum + peak-vol composite."""
    return (((_rsi(close, 14) > 95.0)
            & (_rolling_zscore(volume, YDAYS, min_periods=QDAYS) > 2.0)
            & _new_high_252(high)).astype(float)).diff()


def f49_bcco_185_4_sigma_return_and_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 1-bar return > 4*sigma (rolling 252d std of returns) AND new 252d high — panic-buying."""
    r = close.pct_change()
    s = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (((r > 4.0 * s) & _new_high_252(high)).astype(float).where(s.notna(), np.nan)).diff()


def f49_bcco_186_21d_return_at_252d_max_and_rsi_at_252d_max_d1(close: pd.Series) -> pd.Series:
    """1 if 21d return at 252d max AND RSI at 252d max — joint-peak momentum & return."""
    r21 = close.pct_change(MDAYS)
    rsi = _rsi(close, 14)
    return (((r21 >= r21.rolling(YDAYS, min_periods=QDAYS).max())

            & (rsi >= rsi.rolling(YDAYS, min_periods=QDAYS).max())).astype(float).where(r21.notna() & rsi.notna(), np.nan)).diff()


def f49_bcco_187_63d_return_max_and_atr_max_and_vol_z_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 63d return at 252d max AND ATR21 at 252d max AND vol z > 2 — quarterly-peak triple confluence."""
    r63 = close.pct_change(QDAYS)
    a = _atr(high, low, close, MDAYS)
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return (((r63 >= r63.rolling(YDAYS, min_periods=QDAYS).max())
            & (a >= a.rolling(YDAYS, min_periods=QDAYS).max())
            & (vz > 2.0)).astype(float)).diff()


def f49_bcco_188_63d_return_pct_rank_504_over_99_and_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 63d return is in top-1% of 504d distribution AND new 252d high."""
    r63 = close.pct_change(QDAYS)
    pr = r63.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)
    return (((pr > 0.99) & _new_high_252(high)).astype(float).where(pr.notna(), np.nan)).diff()


def f49_bcco_189_returns_skew_252_positive_extreme_and_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 252d returns-skew > 1.5 (extreme right-tail) AND new 252d high — right-fat-tail climax."""
    sk = close.pct_change().rolling(YDAYS, min_periods=QDAYS).skew()
    return (((sk > 1.5) & _new_high_252(high)).astype(float).where(sk.notna(), np.nan)).diff()


def f49_bcco_190_7plus_new_21d_highs_in_10_with_vol_declining_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 7+ new 21d highs in past 10 bars AND vol 10d-avg < vol 21d-avg — sustained breakouts on thinning vol (FOMO)."""
    nh_count = _new_high_21(high).astype(float).rolling(10, min_periods=3).sum()
    v_decl = volume.rolling(10, min_periods=3).mean() < volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return (((nh_count >= 7) & v_decl).astype(float).where(volume.notna(), np.nan)).diff()


def f49_bcco_191_up_down_day_ratio_21_over_4_and_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if up-day count / (down-day count + 1) > 4 past 21 AND new 252d high — extreme-bias + breakout."""
    up = (close > close.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = (close < close.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return (((_safe_div(up, dn + 1.0) > 4.0) & _new_high_252(high)).astype(float)).diff()


def f49_bcco_192_up_down_vol_ratio_21_over_5_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if up-vol / down-vol past 21 > 5 — extreme buying pressure."""
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    uv = (up * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    dv = (dn * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((_safe_div(uv, dv + 1.0) > 5.0).astype(float).where(uv.notna(), np.nan)).diff()


def f49_bcco_193_21d_pos_return_count_ge_14_d1(close: pd.Series) -> pd.Series:
    """1 if past 21 days had >= 14 positive returns — extreme up-bias month."""
    return (((close.pct_change() > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum() >= 14).astype(float).where(close.shift(1).notna(), np.nan)).diff()


def f49_bcco_194_5bar_cum_return_over_25pct_d1(close: pd.Series) -> pd.Series:
    """1 if 5-bar cumulative return > 25% — extreme weekly gain."""
    return ((close.pct_change(WDAYS) > 0.25).astype(float).where(close.pct_change(WDAYS).notna(), np.nan)).diff()


def f49_bcco_195_close_above_vwap21_persistent_21bars_and_new_high_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close > rolling-VWAP21 for 21+ consecutive bars AND new 252d high."""
    num = (close * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    den = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    vwap21 = _safe_div(num, den)
    streak = _streak_true(close > vwap21)
    return (((streak >= MDAYS) & _new_high_252(high)).astype(float).where(vwap21.notna(), np.nan)).diff()


def f49_bcco_196_all_ohlc_above_21bars_ago_for_5bars_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if open, high, low, close all above their values 21 bars ago for past 5 consecutive bars — full-OHLC-up streak."""
    cond = (open_ > open_.shift(MDAYS)) & (high > high.shift(MDAYS)) & (low > low.shift(MDAYS)) & (close > close.shift(MDAYS))
    return ((cond & cond.shift(1) & cond.shift(2) & cond.shift(3) & cond.shift(4)).astype(float).where(close.shift(MDAYS + 4).notna(), np.nan)).diff()


def f49_bcco_197_upper_shadow_extreme_after_5_strong_close_d1(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """1 if past 5 bars all had CLV > 0.5 AND today's upper shadow > 2*body — rejection after sustained-strong-close run."""
    cl = _clv(high, low, close)
    strong_5 = (cl.shift(1) > 0.5) & (cl.shift(2) > 0.5) & (cl.shift(3) > 0.5) & (cl.shift(4) > 0.5) & (cl.shift(5) > 0.5)
    body = (close - open_).abs()
    upper = high - pd.concat([open_, close], axis=1).max(axis=1)
    return ((strong_5 & (upper > 2.0 * body)).astype(float).where(cl.notna(), np.nan)).diff()


def f49_bcco_198_bullish_breakaway_gap_5pct_and_new_252d_high_d1(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """1 if open-gap > 5% AND new 252d high — strong-breakaway-gap climax."""
    pc = close.shift(1)
    gap = _safe_div(open_ - pc, pc)
    return (((gap > 0.05) & _new_high_252(high)).astype(float).where(gap.notna(), np.nan)).diff()


def f49_bcco_199_exhaustion_gap_5pct_and_new_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if gap > 5% AND small body (<0.3 range) AND new 252d high — exhaustion gap signature."""
    pc = close.shift(1)
    gap = _safe_div(open_ - pc, pc)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    return (((gap > 0.05) & (body < 0.3 * rng) & _new_high_252(high)).astype(float).where(gap.notna() & rng.notna(), np.nan)).diff()


def f49_bcco_200_new_252d_high_then_1bar_return_below_neg10pct_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high AND today's 1-bar return < -10% — post-peak crash."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax_prev)
    return ((prior_new_high & (close.pct_change() < -0.10)).astype(float).where(rmax_prev.notna(), np.nan)).diff()


def f49_bcco_201_prior_new_high_then_gap_down_over_2pct_d1(open_: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high AND today's open < prior close by > 2% — gap-down rejection."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax_prev)
    gap = _safe_div(open_ - close.shift(1), close.shift(1))
    return ((prior_new_high & (gap < -0.02)).astype(float).where(rmax_prev.notna(), np.nan)).diff()


def f49_bcco_202_prior_new_high_then_close_below_prior_midpoint_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high AND today's close < prior bar's midpoint — bearish follow-through."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax_prev)
    mid_prev = (high.shift(1) + low.shift(1)) / 2.0
    return ((prior_new_high & (close < mid_prev)).astype(float).where(rmax_prev.notna(), np.nan)).diff()


def f49_bcco_203_new_high_cluster_then_immediate_5bar_decline_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5+ new 21d highs in past 5 bars (cluster) AND 5d cum return is now negative — cluster-then-fade."""
    nh = _new_high_21(high).astype(float).rolling(WDAYS, min_periods=2).sum() >= 5
    return ((nh.shift(WDAYS) & (close.pct_change(WDAYS) < 0)).astype(float).where(nh.shift(WDAYS).notna(), np.nan)).diff()


def f49_bcco_204_3bar_reversal_new_high_doji_widedown_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 2 bars ago new 252d high, 1 bar ago doji (small body), today wide-down (close<open AND TR > 2*ATR21)."""
    rmax_2 = high.shift(2).rolling(YDAYS, min_periods=QDAYS).max()
    nh_2_ago = (high.shift(2) >= rmax_2)
    body_1 = (close.shift(1) - open_.shift(1)).abs()
    rng_1 = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    doji_1 = body_1 < 0.1 * rng_1
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    wide_down_now = (close < open_) & (rng_ratio > 2.0)
    return ((nh_2_ago & doji_1 & wide_down_now).astype(float).where(rng_1.notna() & rng_ratio.notna(), np.nan)).diff()


def f49_bcco_205_bearish_engulfing_of_new_252d_high_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high (bullish) AND today's body engulfs prior body bearishly."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax_prev)
    prior_bull = close.shift(1) > open_.shift(1)
    open_above_prior_close = open_ > close.shift(1)
    close_below_prior_open = close < open_.shift(1)
    body_eng = (open_ - close).abs() > (close.shift(1) - open_.shift(1)).abs()
    return ((prior_new_high & prior_bull & open_above_prior_close & close_below_prior_open & body_eng).astype(float).where(rmax_prev.notna(), np.nan)).diff()


def f49_bcco_206_new_high_rsi_div_and_vol_div_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND RSI < prior 63d RSI max AND volume < prior 63d vol max — joint RSI+vol bearish divergence at peak."""
    r = _rsi(close, 14)
    r_div = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    v_div = volume < volume.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((_new_high_252(high) & r_div & v_div).astype(float).where(r.notna(), np.nan)).diff()


def f49_bcco_207_new_high_then_macd_bearish_cross_within_5_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """1 if 5 bars ago was new 252d high AND today MACD just crossed below its signal (PIT-safe post-bar look)."""
    rmax_5 = high.shift(WDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    nh_5_ago = (high.shift(WDAYS) >= rmax_5)
    macd = _ema(close, 12) - _ema(close, 26)
    sig = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    diff = macd - sig
    cross = (diff.shift(1) > 0) & (diff <= 0)
    return ((nh_5_ago & cross).astype(float).where(rmax_5.notna() & diff.notna(), np.nan)).diff()


def f49_bcco_208_new_21d_high_then_close_below_prior_low_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today is new 21d high AND today's close < prior bar's low — key reversal day."""
    return ((_new_high_21(high) & (close < low.shift(1))).astype(float).where(low.shift(1).notna(), np.nan)).diff()


def f49_bcco_209_failed_breakout_21bars_post_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21 bars ago was new 252d high AND today close < that breakout level — failed-breakout 21 bars later."""
    bo_level = high.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    bo_at_t_minus_21 = (high.shift(MDAYS) >= bo_level)
    return ((bo_at_t_minus_21 & (close < high.shift(MDAYS))).astype(float).where(bo_level.notna(), np.nan)).diff()


def f49_bcco_210_failed_breakout_count_252_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of failed-breakout events (new 21d high then within 5 bars close back below)."""
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    nh = (high == rmax_21)
    # at bar t: did a new 21d high occur in past 5 bars AND close[t] < that high?
    nh_5_ago = nh.shift(WDAYS)
    high_5_ago = high.shift(WDAYS)
    fail_now = nh_5_ago & (close < high_5_ago)
    return (fail_now.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(high_5_ago.notna(), np.nan)).diff()


def f49_bcco_211_new_high_rsi_div_ad_div_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND RSI bearish div AND AD-line bearish div — triple-confirm bearish divergence at peak."""
    r = _rsi(close, 14)
    ad = (_clv(high, low, close) * volume).cumsum()
    r_div = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    ad_div = ad < ad.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((_new_high_252(high) & r_div & ad_div).astype(float).where(r.notna() & ad.notna(), np.nan)).diff()


def f49_bcco_212_new_high_rsi_div_vol_decline_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND RSI bearish div AND vol declining (21d slope < 0)."""
    r = _rsi(close, 14)
    r_div = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    v_sl = _rolling_slope(volume, MDAYS)
    return ((_new_high_252(high) & r_div & (v_sl < 0)).astype(float).where(r.notna() & v_sl.notna(), np.nan)).diff()


def f49_bcco_213_new_high_macd_hist_top_decile_rsi_over_80_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """1 if new 252d high AND MACD-hist > 252d 90th pct AND RSI > 80 — momentum saturation triple."""
    macd = _ema(close, 12) - _ema(close, 26)
    sig = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    hist = macd - sig
    q90 = hist.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((_new_high_252(high) & (hist > q90) & (_rsi(close, 14) > 80.0)).astype(float).where(q90.notna(), np.nan)).diff()


def f49_bcco_214_new_high_roc63_over_100_and_vol_z_over_2_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND 63d return > 100% AND vol z > 2 — parabolic + vol-spike."""
    return ((_new_high_252(high)
            & (close.pct_change(QDAYS) > 1.0)
            & (_rolling_zscore(volume, YDAYS, min_periods=QDAYS) > 2.0)).astype(float)).diff()


def f49_bcco_215_new_high_close_over_2x_sma200_and_rsi_over_80_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND close > 2 * SMA200 (price doubled vs long MA) AND RSI > 80."""
    return ((_new_high_252(high) & (close > 2.0 * _sma(close, 200)) & (_rsi(close, 14) > 80.0)).astype(float).where(_sma(close, 200).notna(), np.nan)).diff()


def f49_bcco_216_new_high_close_over_2x_vwap252_and_vol_z_over_1_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND close > 2 * VWAP252 AND vol z > 1 — far-above-VWAP + vol-spike."""
    num = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    den = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vwap252 = _safe_div(num, den)
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return ((_new_high_252(high) & (close > 2.0 * vwap252) & (vz > 1.0)).astype(float).where(vwap252.notna(), np.nan)).diff()


def f49_bcco_217_new_high_atr_expansion_and_rsi_over_90_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND ATR21 > 2x ATR252 AND RSI > 90 — vol explosion + extreme momentum."""
    expansion = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS))
    return ((_new_high_252(high) & (expansion > 2.0) & (_rsi(close, 14) > 90.0)).astype(float).where(expansion.notna(), np.nan)).diff()


def f49_bcco_218_new_high_21d_log_ret_over_30_and_5d_vol_z_over_2_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND 21d log-return > 0.30 AND 5d vol-sum z > 2."""
    lr21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    vz5 = _rolling_zscore(volume.rolling(WDAYS, min_periods=2).sum(), YDAYS, min_periods=QDAYS)
    return ((_new_high_252(high) & (lr21 > 0.30) & (vz5 > 2.0)).astype(float).where(lr21.notna() & vz5.notna(), np.nan)).diff()


def f49_bcco_219_new_high_body_over_70_range_and_vol_z_over_2_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND body/range > 0.7 AND vol z > 2 — strong-body + vol-spike climax."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_ratio = body / rng
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return ((_new_high_252(high) & (body_ratio > 0.7) & (vz > 2.0)).astype(float).where(body_ratio.notna() & vz.notna(), np.nan)).diff()


def f49_bcco_220_new_high_hl_range_over_10_pct_close_and_vol_z_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND (high-low)/close > 10% AND vol z > 2 — extreme intra-bar range + vol."""
    rng_pct = _safe_div(high - low, close)
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return ((_new_high_252(high) & (rng_pct > 0.10) & (vz > 2.0)).astype(float).where(rng_pct.notna() & vz.notna(), np.nan)).diff()


def f49_bcco_221_composite_climax_index_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted climax index: 0.3*(parabolic_z) + 0.3*(vol_z) + 0.2*(rsi_norm) + 0.2*(range_z), all clipped."""
    par_z = _rolling_zscore(close.pct_change(QDAYS), YDAYS, min_periods=QDAYS).clip(-3, 3)
    vol_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).clip(-3, 3)
    rsi_n = (_rsi(close, 14) - 50.0) / 50.0
    rng_z = _rolling_zscore(_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)), YDAYS, min_periods=QDAYS).clip(-3, 3)
    return (0.3 * par_z + 0.3 * vol_z + 0.2 * rsi_n + 0.2 * rng_z).diff()


def f49_bcco_222_composite_climax_above_2_dwell_5_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction past 5 bars with composite_climax_index > 2."""
    par_z = _rolling_zscore(close.pct_change(QDAYS), YDAYS, min_periods=QDAYS).clip(-3, 3)
    vol_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).clip(-3, 3)
    rsi_n = (_rsi(close, 14) - 50.0) / 50.0
    rng_z = _rolling_zscore(_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)), YDAYS, min_periods=QDAYS).clip(-3, 3)
    idx = 0.3 * par_z + 0.3 * vol_z + 0.2 * rsi_n + 0.2 * rng_z
    return ((idx > 2.0).astype(float).rolling(WDAYS, min_periods=2).mean()).diff()


def f49_bcco_223_composite_climax_above_2_dwell_21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction past 21 bars with composite_climax_index > 2 — monthly climax-intensity dwell."""
    par_z = _rolling_zscore(close.pct_change(QDAYS), YDAYS, min_periods=QDAYS).clip(-3, 3)
    vol_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).clip(-3, 3)
    rsi_n = (_rsi(close, 14) - 50.0) / 50.0
    rng_z = _rolling_zscore(_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)), YDAYS, min_periods=QDAYS).clip(-3, 3)
    idx = 0.3 * par_z + 0.3 * vol_z + 0.2 * rsi_n + 0.2 * rng_z
    return ((idx > 2.0).astype(float).rolling(MDAYS, min_periods=WDAYS).mean()).diff()


def f49_bcco_224_max_composite_climax_past_5_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max composite climax index past 5 bars — peak short-term intensity."""
    par_z = _rolling_zscore(close.pct_change(QDAYS), YDAYS, min_periods=QDAYS).clip(-3, 3)
    vol_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).clip(-3, 3)
    rsi_n = (_rsi(close, 14) - 50.0) / 50.0
    rng_z = _rolling_zscore(_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)), YDAYS, min_periods=QDAYS).clip(-3, 3)
    idx = 0.3 * par_z + 0.3 * vol_z + 0.2 * rsi_n + 0.2 * rng_z
    return (idx.rolling(WDAYS, min_periods=2).max()).diff()


def f49_bcco_225_terminal_blowoff_confidence_3day_3of5_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if each of past 3 bars had >= 3 of 5 blowoff signals AND new 252d high in that window — terminal-blowoff confidence."""
    r = _rsi(close, 14)
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    nh = _new_high_252(high)
    s = ((nh.astype(float).fillna(0))
         + ((v_ratio > 2.0).astype(float).fillna(0))
         + ((r > 80.0).astype(float).fillna(0))
         + ((rng_ratio > 2.0).astype(float).fillna(0))
         + ((_clv(high, low, close) > 0.5).astype(float).fillna(0)))
    three_day = (s >= 3) & (s.shift(1) >= 3) & (s.shift(2) >= 3)
    nh_window = nh.rolling(3, min_periods=1).max() > 0
    return ((three_day & nh_window).astype(float).where(r.notna(), np.nan)).diff()


# ============================================================
#                         REGISTRY 151-225 (d1)
# ============================================================

_HV = ["high", "volume"]
_HC = ["high", "close"]
_HCV = ["high", "close", "volume"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_HL = ["high", "low"]
_OC = ["open", "close"]
_CV = ["close", "volume"]
_OHLC = ["open", "high", "low", "close"]
_OHLCV = ["open", "high", "low", "close", "volume"]

BLOWOFF_CLIMAX_COMPOSITE_D1_REGISTRY_151_225 = {
    "f49_bcco_151_bb_squeeze_lowest_decile_then_new_high_d1": {"inputs": _HC, "func": f49_bcco_151_bb_squeeze_lowest_decile_then_new_high_d1},
    "f49_bcco_152_bb_squeeze_lowest_5pct_then_new_high_d1": {"inputs": _HC, "func": f49_bcco_152_bb_squeeze_lowest_5pct_then_new_high_d1},
    "f49_bcco_153_5plus_nr7_in_21_then_breakout_d1": {"inputs": _HL, "func": f49_bcco_153_5plus_nr7_in_21_then_breakout_d1},
    "f49_bcco_154_21d_vol_lowest_quartile_then_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_154_21d_vol_lowest_quartile_then_new_252d_high_d1},
    "f49_bcco_155_ttm_squeeze_release_with_new_high_d1": {"inputs": _HLC, "func": f49_bcco_155_ttm_squeeze_release_with_new_high_d1},
    "f49_bcco_156_5bar_vol_zscore_over_3_and_new_high_d1": {"inputs": _HV, "func": f49_bcco_156_5bar_vol_zscore_over_3_and_new_high_d1},
    "f49_bcco_157_5d_return_zscore_over_2_and_new_high_d1": {"inputs": _HC, "func": f49_bcco_157_5d_return_zscore_over_2_and_new_high_d1},
    "f49_bcco_158_runaway_gap_with_new_high_d1": {"inputs": _OHLC, "func": f49_bcco_158_runaway_gap_with_new_high_d1},
    "f49_bcco_159_inside_day_before_new_252d_high_d1": {"inputs": _HL, "func": f49_bcco_159_inside_day_before_new_252d_high_d1},
    "f49_bcco_160_5bar_vol_sum_zscore_and_5bar_return_z_d1": {"inputs": _HCV, "func": f49_bcco_160_5bar_vol_sum_zscore_and_5bar_return_z_d1},
    "f49_bcco_161_3_consecutive_new_252d_highs_d1": {"inputs": ["high"], "func": f49_bcco_161_3_consecutive_new_252d_highs_d1},
    "f49_bcco_162_5_consecutive_new_252d_highs_d1": {"inputs": ["high"], "func": f49_bcco_162_5_consecutive_new_252d_highs_d1},
    "f49_bcco_163_3_consecutive_wide_range_and_new_high_d1": {"inputs": _HLC, "func": f49_bcco_163_3_consecutive_wide_range_and_new_high_d1},
    "f49_bcco_164_3day_climax_each_bar_3plus_signals_d1": {"inputs": _HLCV, "func": f49_bcco_164_3day_climax_each_bar_3plus_signals_d1},
    "f49_bcco_165_5day_climax_each_bar_3plus_signals_d1": {"inputs": _HLCV, "func": f49_bcco_165_5day_climax_each_bar_3plus_signals_d1},
    "f49_bcco_166_10day_cum_return_over_50pct_d1": {"inputs": ["close"], "func": f49_bcco_166_10day_cum_return_over_50pct_d1},
    "f49_bcco_167_10day_cum_return_over_100pct_d1": {"inputs": ["close"], "func": f49_bcco_167_10day_cum_return_over_100pct_d1},
    "f49_bcco_168_21day_cum_return_over_50pct_with_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_168_21day_cum_return_over_50pct_with_new_252d_high_d1},
    "f49_bcco_169_vol_acceleration_5bar_over_prior_5bar_d1": {"inputs": ["volume"], "func": f49_bcco_169_vol_acceleration_5bar_over_prior_5bar_d1},
    "f49_bcco_170_3_consecutive_strong_close_and_new_21d_high_d1": {"inputs": _HLC, "func": f49_bcco_170_3_consecutive_strong_close_and_new_21d_high_d1},
    "f49_bcco_171_shooting_star_at_new_21d_high_d1": {"inputs": _OHLC, "func": f49_bcco_171_shooting_star_at_new_21d_high_d1},
    "f49_bcco_172_hanging_man_at_new_21d_high_d1": {"inputs": _OHLC, "func": f49_bcco_172_hanging_man_at_new_21d_high_d1},
    "f49_bcco_173_dark_cloud_cover_after_new_252d_high_d1": {"inputs": _OHLC, "func": f49_bcco_173_dark_cloud_cover_after_new_252d_high_d1},
    "f49_bcco_174_evening_star_at_new_252d_high_d1": {"inputs": _OHLC, "func": f49_bcco_174_evening_star_at_new_252d_high_d1},
    "f49_bcco_175_bearish_harami_at_new_252d_high_d1": {"inputs": _OHLC, "func": f49_bcco_175_bearish_harami_at_new_252d_high_d1},
    "f49_bcco_176_tweezer_top_2bar_d1": {"inputs": ["high"], "func": f49_bcco_176_tweezer_top_2bar_d1},
    "f49_bcco_177_long_upper_shadow_3x_body_at_new_252d_high_d1": {"inputs": _OHLC, "func": f49_bcco_177_long_upper_shadow_3x_body_at_new_252d_high_d1},
    "f49_bcco_178_gravestone_doji_at_new_252d_high_d1": {"inputs": _OHLC, "func": f49_bcco_178_gravestone_doji_at_new_252d_high_d1},
    "f49_bcco_179_three_white_soldiers_then_bearish_d1": {"inputs": _OC, "func": f49_bcco_179_three_white_soldiers_then_bearish_d1},
    "f49_bcco_180_inverted_hammer_at_new_252d_high_d1": {"inputs": _OHLC, "func": f49_bcco_180_inverted_hammer_at_new_252d_high_d1},
    "f49_bcco_181_21d_return_zscore_over_3_and_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_181_21d_return_zscore_over_3_and_new_252d_high_d1},
    "f49_bcco_182_5d_vol_zscore_over_3_and_new_252d_high_d1": {"inputs": _HV, "func": f49_bcco_182_5d_vol_zscore_over_3_and_new_252d_high_d1},
    "f49_bcco_183_sharpe_3_and_atr_pct_rank_90_d1": {"inputs": _HLC, "func": f49_bcco_183_sharpe_3_and_atr_pct_rank_90_d1},
    "f49_bcco_184_rsi_over_95_and_vol_z_over_2_and_new_high_d1": {"inputs": _HCV, "func": f49_bcco_184_rsi_over_95_and_vol_z_over_2_and_new_high_d1},
    "f49_bcco_185_4_sigma_return_and_new_high_d1": {"inputs": _HC, "func": f49_bcco_185_4_sigma_return_and_new_high_d1},
    "f49_bcco_186_21d_return_at_252d_max_and_rsi_at_252d_max_d1": {"inputs": ["close"], "func": f49_bcco_186_21d_return_at_252d_max_and_rsi_at_252d_max_d1},
    "f49_bcco_187_63d_return_max_and_atr_max_and_vol_z_d1": {"inputs": _HLCV, "func": f49_bcco_187_63d_return_max_and_atr_max_and_vol_z_d1},
    "f49_bcco_188_63d_return_pct_rank_504_over_99_and_new_high_d1": {"inputs": _HC, "func": f49_bcco_188_63d_return_pct_rank_504_over_99_and_new_high_d1},
    "f49_bcco_189_returns_skew_252_positive_extreme_and_new_high_d1": {"inputs": _HC, "func": f49_bcco_189_returns_skew_252_positive_extreme_and_new_high_d1},
    "f49_bcco_190_7plus_new_21d_highs_in_10_with_vol_declining_d1": {"inputs": _HV, "func": f49_bcco_190_7plus_new_21d_highs_in_10_with_vol_declining_d1},
    "f49_bcco_191_up_down_day_ratio_21_over_4_and_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_191_up_down_day_ratio_21_over_4_and_new_252d_high_d1},
    "f49_bcco_192_up_down_vol_ratio_21_over_5_d1": {"inputs": _CV, "func": f49_bcco_192_up_down_vol_ratio_21_over_5_d1},
    "f49_bcco_193_21d_pos_return_count_ge_14_d1": {"inputs": ["close"], "func": f49_bcco_193_21d_pos_return_count_ge_14_d1},
    "f49_bcco_194_5bar_cum_return_over_25pct_d1": {"inputs": ["close"], "func": f49_bcco_194_5bar_cum_return_over_25pct_d1},
    "f49_bcco_195_close_above_vwap21_persistent_21bars_and_new_high_d1": {"inputs": _HCV, "func": f49_bcco_195_close_above_vwap21_persistent_21bars_and_new_high_d1},
    "f49_bcco_196_all_ohlc_above_21bars_ago_for_5bars_d1": {"inputs": _OHLC, "func": f49_bcco_196_all_ohlc_above_21bars_ago_for_5bars_d1},
    "f49_bcco_197_upper_shadow_extreme_after_5_strong_close_d1": {"inputs": _OHLC, "func": f49_bcco_197_upper_shadow_extreme_after_5_strong_close_d1},
    "f49_bcco_198_bullish_breakaway_gap_5pct_and_new_252d_high_d1": {"inputs": ["open", "close", "high"], "func": f49_bcco_198_bullish_breakaway_gap_5pct_and_new_252d_high_d1},
    "f49_bcco_199_exhaustion_gap_5pct_and_new_252d_high_d1": {"inputs": _OHLC, "func": f49_bcco_199_exhaustion_gap_5pct_and_new_252d_high_d1},
    "f49_bcco_200_new_252d_high_then_1bar_return_below_neg10pct_d1": {"inputs": _HC, "func": f49_bcco_200_new_252d_high_then_1bar_return_below_neg10pct_d1},
    "f49_bcco_201_prior_new_high_then_gap_down_over_2pct_d1": {"inputs": ["open", "high", "close"], "func": f49_bcco_201_prior_new_high_then_gap_down_over_2pct_d1},
    "f49_bcco_202_prior_new_high_then_close_below_prior_midpoint_d1": {"inputs": _HLC, "func": f49_bcco_202_prior_new_high_then_close_below_prior_midpoint_d1},
    "f49_bcco_203_new_high_cluster_then_immediate_5bar_decline_d1": {"inputs": _HC, "func": f49_bcco_203_new_high_cluster_then_immediate_5bar_decline_d1},
    "f49_bcco_204_3bar_reversal_new_high_doji_widedown_d1": {"inputs": _OHLC, "func": f49_bcco_204_3bar_reversal_new_high_doji_widedown_d1},
    "f49_bcco_205_bearish_engulfing_of_new_252d_high_d1": {"inputs": _OHLC, "func": f49_bcco_205_bearish_engulfing_of_new_252d_high_d1},
    "f49_bcco_206_new_high_rsi_div_and_vol_div_d1": {"inputs": _HCV, "func": f49_bcco_206_new_high_rsi_div_and_vol_div_d1},
    "f49_bcco_207_new_high_then_macd_bearish_cross_within_5_d1": {"inputs": _HC, "func": f49_bcco_207_new_high_then_macd_bearish_cross_within_5_d1},
    "f49_bcco_208_new_21d_high_then_close_below_prior_low_d1": {"inputs": _HLC, "func": f49_bcco_208_new_21d_high_then_close_below_prior_low_d1},
    "f49_bcco_209_failed_breakout_21bars_post_d1": {"inputs": _HC, "func": f49_bcco_209_failed_breakout_21bars_post_d1},
    "f49_bcco_210_failed_breakout_count_252_d1": {"inputs": _HC, "func": f49_bcco_210_failed_breakout_count_252_d1},
    "f49_bcco_211_new_high_rsi_div_ad_div_d1": {"inputs": _HLCV, "func": f49_bcco_211_new_high_rsi_div_ad_div_d1},
    "f49_bcco_212_new_high_rsi_div_vol_decline_d1": {"inputs": _HCV, "func": f49_bcco_212_new_high_rsi_div_vol_decline_d1},
    "f49_bcco_213_new_high_macd_hist_top_decile_rsi_over_80_d1": {"inputs": _HC, "func": f49_bcco_213_new_high_macd_hist_top_decile_rsi_over_80_d1},
    "f49_bcco_214_new_high_roc63_over_100_and_vol_z_over_2_d1": {"inputs": _HCV, "func": f49_bcco_214_new_high_roc63_over_100_and_vol_z_over_2_d1},
    "f49_bcco_215_new_high_close_over_2x_sma200_and_rsi_over_80_d1": {"inputs": _HC, "func": f49_bcco_215_new_high_close_over_2x_sma200_and_rsi_over_80_d1},
    "f49_bcco_216_new_high_close_over_2x_vwap252_and_vol_z_over_1_d1": {"inputs": _HCV, "func": f49_bcco_216_new_high_close_over_2x_vwap252_and_vol_z_over_1_d1},
    "f49_bcco_217_new_high_atr_expansion_and_rsi_over_90_d1": {"inputs": _HLC, "func": f49_bcco_217_new_high_atr_expansion_and_rsi_over_90_d1},
    "f49_bcco_218_new_high_21d_log_ret_over_30_and_5d_vol_z_over_2_d1": {"inputs": _HCV, "func": f49_bcco_218_new_high_21d_log_ret_over_30_and_5d_vol_z_over_2_d1},
    "f49_bcco_219_new_high_body_over_70_range_and_vol_z_over_2_d1": {"inputs": _OHLCV, "func": f49_bcco_219_new_high_body_over_70_range_and_vol_z_over_2_d1},
    "f49_bcco_220_new_high_hl_range_over_10_pct_close_and_vol_z_d1": {"inputs": _HLCV, "func": f49_bcco_220_new_high_hl_range_over_10_pct_close_and_vol_z_d1},
    "f49_bcco_221_composite_climax_index_d1": {"inputs": _HLCV, "func": f49_bcco_221_composite_climax_index_d1},
    "f49_bcco_222_composite_climax_above_2_dwell_5_d1": {"inputs": _HLCV, "func": f49_bcco_222_composite_climax_above_2_dwell_5_d1},
    "f49_bcco_223_composite_climax_above_2_dwell_21_d1": {"inputs": _HLCV, "func": f49_bcco_223_composite_climax_above_2_dwell_21_d1},
    "f49_bcco_224_max_composite_climax_past_5_d1": {"inputs": _HLCV, "func": f49_bcco_224_max_composite_climax_past_5_d1},
    "f49_bcco_225_terminal_blowoff_confidence_3day_3of5_d1": {"inputs": _HLCV, "func": f49_bcco_225_terminal_blowoff_confidence_3day_3of5_d1},
}
