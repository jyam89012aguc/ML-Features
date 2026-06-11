"""macd_topping_dynamics base features 076-150 — Pipeline 1b-technical.

Continues 001-075 with:
I: MACD / ATR-normalized variants (vol-comparable across stocks/regimes).
J: MACD × price-level interactions (failure at price highs).
K: distribution-based MACD statistics (z-score, percentile, skew, kurtosis).
L: histogram bar-by-bar pattern detectors (consecutive runs, swing-lows).
M: stationarity / detrending of MACD.
N: time-since composite events (different reference points than 001-075).
O: acceleration / second-order dynamics.
P: long-horizon MACD (50/200/30 config) for slow-cycle topping.
Q: composite topping scores.

Inputs: SEP OHLCV (close primarily). PIT-clean. Self-contained helpers.
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()


def _macd(close, fast=12, slow=26, signal=9):
    macd = _ema(close, fast) - _ema(close, slow)
    sig = _ema(macd, signal)
    histo = macd - sig
    return macd, sig, histo


def _ppo(close, fast=12, slow=26, signal=9):
    ef = _ema(close, fast)
    es = _ema(close, slow)
    ppo = 100.0 * _safe_div(ef - es, es)
    sig = _ema(ppo, signal)
    histo = ppo - sig
    return ppo, sig, histo


def _bars_since_true(mask: pd.Series) -> pd.Series:
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


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# Bucket I — MACD / ATR-normalized variants (076-082)
# ============================================================

def f27_mcdt_076_macd_norm_atr_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD line / ATR(21) — vol-normalized MACD magnitude (cross-regime comparable)."""
    m, _, _ = _macd(close)
    return _safe_div(m, _atr(high, low, close, MDAYS))


def f27_mcdt_077_macd_norm_close(close: pd.Series) -> pd.Series:
    """MACD line / close — price-normalized MACD magnitude."""
    m, _, _ = _macd(close)
    return _safe_div(m, close)


def f27_mcdt_078_macd_norm_atr_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD line / ATR(63) — quarterly-vol-normalized MACD."""
    m, _, _ = _macd(close)
    return _safe_div(m, _atr(high, low, close, QDAYS))


def f27_mcdt_079_histogram_norm_atr_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Histogram / ATR(21) — vol-normalized momentum-of-momentum."""
    _, _, h = _macd(close)
    return _safe_div(h, _atr(high, low, close, MDAYS))


def f27_mcdt_080_histogram_norm_close(close: pd.Series) -> pd.Series:
    """Histogram / close — price-normalized histogram."""
    _, _, h = _macd(close)
    return _safe_div(h, close)


def f27_mcdt_081_histogram_to_macd_line_abs_ratio(close: pd.Series) -> pd.Series:
    """|histogram / MACD line| — relative magnitude of histogram to line
    (high = momentum-of-momentum dominates, often near peaks)."""
    m, _, h = _macd(close)
    return _safe_div(h.abs(), m.abs())


def f27_mcdt_082_ppo_norm_atr_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """PPO / (ATR21 / close) — PPO vol-normalized via ATR%."""
    p, _, _ = _ppo(close)
    atr_pct = _safe_div(_atr(high, low, close, MDAYS), close)
    return _safe_div(p, atr_pct)


# ============================================================
# Bucket J — MACD × price-level interactions (083-090)
# ============================================================

def f27_mcdt_083_macd_pos_at_252_high_state(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND price at its 252d max — bullish-momentum-at-peak state."""
    m, _, _ = _macd(close)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((m > 0) & at_max).astype(float).where(m.notna(), np.nan)


def f27_mcdt_084_macd_failing_at_close_21d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close = 21d max AND MACD below its prior 21d MACD-max — momentum failing at price peak."""
    m, _, _ = _macd(close)
    at_max = close == close.rolling(MDAYS, min_periods=WDAYS).max()
    m_below = m < m.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return (at_max & m_below).astype(float).where(m.notna(), np.nan)


def f27_mcdt_085_histogram_negative_with_close_at_252_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if MACD histogram < 0 AND close at 252d max — strong bearish-internals at price peak."""
    _, _, h = _macd(close)
    at_max = close == close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((h < 0) & at_max).astype(float).where(h.notna(), np.nan)


def f27_mcdt_086_ppo_overstretched_at_price_high_state(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if PPO above 252d 90th-percentile AND price at 252d max — distribution-OB confluence."""
    p, _, _ = _ppo(close)
    q = p.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((p > q) & at_max).astype(float).where(p.notna() & q.notna(), np.nan)


def f27_mcdt_087_histogram_minus_close_pct_extension(close: pd.Series) -> pd.Series:
    """Histogram / close — close pct-change(21) — disagreement between momentum-of-momentum and price extension."""
    _, _, h = _macd(close)
    px = close.pct_change(MDAYS)
    return _safe_div(h, close) - px


def f27_mcdt_088_signal_cross_failure_at_top_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if a bullish MACD/signal cross occurred but failed within 21 bars (bearish cross fired),
    AND price was at 252d max during the bullish cross — failed bullish trigger at peak."""
    m, s, _ = _macd(close)
    d = m - s
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    at_max = (high == high.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    bu_at_max_21_ago = (bu * at_max).shift(MDAYS)
    be_in_21 = be.rolling(MDAYS, min_periods=1).sum()
    return ((bu_at_max_21_ago > 0) & (be_in_21 > 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_089_macd_decoupled_from_price_indicator_63(close: pd.Series) -> pd.Series:
    """1 if rolling 63d correlation(close, MACD) drops below 0.3 — momentum decoupled from price."""
    m, _, _ = _macd(close)
    c = close.rolling(QDAYS, min_periods=MDAYS).corr(m)
    return (c < 0.3).astype(float).where(c.notna(), np.nan)


def f27_mcdt_090_macd_neg_slope_while_price_at_252_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d slope of MACD is negative AND price at 252d max — momentum-falling-at-price-peak."""
    m, _, _ = _macd(close)
    sl = _rolling_slope(m, MDAYS)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((sl < 0) & at_max).astype(float).where(m.notna() & sl.notna(), np.nan)


# ============================================================
# Bucket K — distribution-based MACD statistics (091-100)
# ============================================================

def f27_mcdt_091_macd_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of MACD line over 252d — distribution-relative MACD position."""
    m, _, _ = _macd(close)
    return _rolling_zscore(m, YDAYS, min_periods=QDAYS)


def f27_mcdt_092_macd_zscore_504(close: pd.Series) -> pd.Series:
    """Z-score of MACD over 504d (2y) — multi-year MACD position."""
    m, _, _ = _macd(close)
    return _rolling_zscore(m, DDAYS_2Y, min_periods=YDAYS)


def f27_mcdt_093_macd_pct_rank_252(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of MACD."""
    m, _, _ = _macd(close)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f27_mcdt_094_macd_above_q90_distribution_252(close: pd.Series) -> pd.Series:
    """1 if MACD above trailing 252d 90th percentile — distribution-based MACD OB."""
    m, _, _ = _macd(close)
    q = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (m > q).astype(float).where(m.notna() & q.notna(), np.nan)


def f27_mcdt_095_macd_above_q99_distribution_252(close: pd.Series) -> pd.Series:
    """1 if MACD above 252d 99th percentile — extreme distribution-MACD OB."""
    m, _, _ = _macd(close)
    q = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return (m > q).astype(float).where(m.notna() & q.notna(), np.nan)


def f27_mcdt_096_macd_skew_63(close: pd.Series) -> pd.Series:
    """Skewness of MACD line over 63 bars — distribution asymmetry."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).skew()


def f27_mcdt_097_macd_kurtosis_63(close: pd.Series) -> pd.Series:
    """Excess kurtosis of MACD over 63 bars — tail behavior of momentum."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).kurt()


def f27_mcdt_098_macd_robust_zscore_mad_252(close: pd.Series) -> pd.Series:
    """Robust z-score: (MACD - median) / (1.4826 * MAD) over 252d — outlier-resistant MACD position."""
    m, _, _ = _macd(close)
    med = m.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (m - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(m - med, 1.4826 * mad)


def f27_mcdt_099_macd_range_high_minus_low_63(close: pd.Series) -> pd.Series:
    """MACD 63d max - 63d min — quarterly MACD range (compression vs expansion)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).max() - m.rolling(QDAYS, min_periods=MDAYS).min()


def f27_mcdt_100_macd_vol_63(close: pd.Series) -> pd.Series:
    """Std of MACD over 63 bars — quarterly MACD volatility."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).std()


# ============================================================
# Bucket L — histogram bar-by-bar pattern detectors (101-110)
# ============================================================

def f27_mcdt_101_histo_4_consecutive_lower_bars_indicator(close: pd.Series) -> pd.Series:
    """1 if histogram declined for 4 consecutive bars — classical 'momentum cooling' pattern."""
    _, _, h = _macd(close)
    falling = (h < h.shift(1)).astype(float)
    return (falling.rolling(4, min_periods=4).sum() == 4).astype(float).where(h.notna(), np.nan)


def f27_mcdt_102_histo_3_consecutive_neg_smaller_neg_pattern(close: pd.Series) -> pd.Series:
    """1 if last 3 bars: all histo < 0 AND each successively closer to zero — 'bottoming' pattern in histo."""
    _, _, h = _macd(close)
    cond = (h < 0) & (h.shift(1) < 0) & (h.shift(2) < 0) & (h > h.shift(1)) & (h.shift(1) > h.shift(2))
    return cond.astype(float).where(h.notna(), np.nan)


def f27_mcdt_103_histo_swing_low_count_63(close: pd.Series) -> pd.Series:
    """Count of local-min histogram swings (h_prev < h_curr AND h_curr > h_next) in past 63 bars."""
    _, _, h = _macd(close)
    swing = (h.shift(1) > h) & (h > h.shift(1))
    # Using .shift(1) is forward-peek; replace with strict past-only definition:
    # local min at bar t-1: h[t-2] > h[t-1] AND h[t-1] < h[t]
    swing_pit = (h.shift(2) > h.shift(1)) & (h.shift(1) < h)
    return swing_pit.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(h.notna(), np.nan)


def f27_mcdt_104_histo_amplitude_decay_63(close: pd.Series) -> pd.Series:
    """(63d rolling max of h) - (h max from 63 bars ago) — quarterly histogram amplitude decay
    (negative = decaying peaks)."""
    _, _, h = _macd(close)
    pmax = h.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f27_mcdt_105_histo_sign_flip_count_63(close: pd.Series) -> pd.Series:
    """Count of histogram sign flips (zero crosses) in past 63 — chop / instability of momentum-of-momentum."""
    _, _, h = _macd(close)
    flip = (h * h.shift(1)) < 0
    return flip.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(h.notna(), np.nan)


def f27_mcdt_106_histo_current_positive_streak(close: pd.Series) -> pd.Series:
    """Current consecutive run of histogram > 0 — bullish-momentum-of-momentum streak."""
    _, _, h = _macd(close)
    return _streak_true(h > 0).where(h.notna(), np.nan)


def f27_mcdt_107_histo_consecutive_lower_run_max_63(close: pd.Series) -> pd.Series:
    """Longest run of consecutive lower-histo bars in past 63 — strongest cooling-run length."""
    _, _, h = _macd(close)
    falling = (h < h.shift(1)).astype(bool)
    streak = _streak_true(falling)
    return streak.rolling(QDAYS, min_periods=MDAYS).max().where(h.notna(), np.nan)


def f27_mcdt_108_histo_low_amplitude_indicator_21(close: pd.Series) -> pd.Series:
    """1 if 21d std of histogram below its 252d 10th percentile — flatlining momentum-of-momentum (squeeze)."""
    _, _, h = _macd(close)
    sd = h.rolling(MDAYS, min_periods=WDAYS).std()
    q = sd.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return (sd < q).astype(float).where(sd.notna() & q.notna(), np.nan)


def f27_mcdt_109_histo_range_to_macd_range_ratio_63(close: pd.Series) -> pd.Series:
    """(63d histo range) / (63d MACD line range) — relative amplitude of histo vs line."""
    m, _, h = _macd(close)
    h_rng = h.rolling(QDAYS, min_periods=MDAYS).max() - h.rolling(QDAYS, min_periods=MDAYS).min()
    m_rng = m.rolling(QDAYS, min_periods=MDAYS).max() - m.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(h_rng, m_rng)


def f27_mcdt_110_histo_skew_63(close: pd.Series) -> pd.Series:
    """Skewness of histogram over 63 bars."""
    _, _, h = _macd(close)
    return h.rolling(QDAYS, min_periods=MDAYS).skew()


# ============================================================
# Bucket M — stationarity / detrending of MACD (111-118)
# ============================================================

def f27_mcdt_111_macd_minus_252d_mean(close: pd.Series) -> pd.Series:
    """MACD - its rolling 252d mean — annual centered deviation."""
    m, _, _ = _macd(close)
    return m - m.rolling(YDAYS, min_periods=QDAYS).mean()


def f27_mcdt_112_macd_minus_504d_mean(close: pd.Series) -> pd.Series:
    """MACD - its rolling 504d mean — bi-annual centered deviation."""
    m, _, _ = _macd(close)
    return m - m.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f27_mcdt_113_macd_dpo_proxy_21(close: pd.Series) -> pd.Series:
    """MACD - SMA21(MACD) shifted back 11 bars — DPO-style detrended MACD (right-anchored shift only)."""
    m, _, _ = _macd(close)
    sma21 = m.rolling(MDAYS, min_periods=WDAYS).mean()
    return m - sma21.shift(11)


def f27_mcdt_114_macd_residual_vs_ema21(close: pd.Series) -> pd.Series:
    """MACD minus EMA(21)(MACD) — short-smoothed residual."""
    m, _, _ = _macd(close)
    return m - _ema(m, MDAYS)


def f27_mcdt_115_macd_residual_zscore_63(close: pd.Series) -> pd.Series:
    """Z-score (63d window) of (MACD - EMA21 MACD) — distribution-normalized smoothing residual."""
    m, _, _ = _macd(close)
    res = m - _ema(m, MDAYS)
    return _rolling_zscore(res, QDAYS, min_periods=MDAYS)


def f27_mcdt_116_macd_persistence_of_sign_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where sign(MACD) equals current sign — sign-persistence measure."""
    m, _, _ = _macd(close)
    cur_sign = np.sign(m)
    same = (np.sign(m) == cur_sign).astype(float)
    return same.rolling(YDAYS, min_periods=QDAYS).mean().where(m.notna(), np.nan)


def f27_mcdt_117_ppo_minus_252d_mean(close: pd.Series) -> pd.Series:
    """PPO - its rolling 252d mean — normalized-MACD centered deviation."""
    p, _, _ = _ppo(close)
    return p - p.rolling(YDAYS, min_periods=QDAYS).mean()


def f27_mcdt_118_macd_ar1_residual_proxy_21(close: pd.Series) -> pd.Series:
    """MACD - lag(1) of MACD smoothed by EMA(21) — AR(1)-style innovation proxy."""
    m, _, _ = _macd(close)
    return m - _ema(m.shift(1), MDAYS)


# ============================================================
# Bucket N — time-since composite events (different references) (119-128)
# ============================================================

def f27_mcdt_119_bars_since_macd_above_q95_dist(close: pd.Series) -> pd.Series:
    """Bars since MACD was above its 252d 95th-percentile — distribution-MACD extreme recency."""
    m, _, _ = _macd(close)
    q = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return _bars_since_true(m > q)


def f27_mcdt_120_bars_since_histo_above_q95_dist(close: pd.Series) -> pd.Series:
    """Bars since histogram was above its 252d 95th-percentile — extreme histo recency."""
    _, _, h = _macd(close)
    q = h.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return _bars_since_true(h > q)


def f27_mcdt_121_bars_since_macd_252_max(close: pd.Series) -> pd.Series:
    """Bars since MACD hit its 252d max — annual-MACD peak recency."""
    m, _, _ = _macd(close)
    at_max = m == m.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f27_mcdt_122_bars_since_histo_252_max(close: pd.Series) -> pd.Series:
    """Bars since histogram hit its 252d max."""
    _, _, h = _macd(close)
    at_max = h == h.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f27_mcdt_123_bars_since_ppo_252_max(close: pd.Series) -> pd.Series:
    """Bars since PPO hit its 252d max."""
    p, _, _ = _ppo(close)
    at_max = p == p.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f27_mcdt_124_bars_since_signal_bearish_cross_above_zero(close: pd.Series) -> pd.Series:
    """Bars since a bearish MACD/signal cross fired while MACD > 0 — premium-signal recency."""
    m, s, _ = _macd(close)
    d = m - s
    ev = (d.shift(1) > 0) & (d <= 0) & (m > 0)
    return _bars_since_true(ev)


def f27_mcdt_125_bars_since_first_macd_div_in_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the first bearish MACD divergence event in the trailing 252d window."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    ev = (p_new & (m < prior_max)).astype(float)
    has_ev = ev.rolling(YDAYS, min_periods=QDAYS).max() > 0
    first_ev_age = _bars_since_true(ev.astype(bool))
    return first_ev_age.where(has_ev, np.nan)


def f27_mcdt_126_bars_since_macd_slope_252_max(close: pd.Series) -> pd.Series:
    """Bars since the 21d-slope of MACD reached its 252d max — slope-peak recency."""
    m, _, _ = _macd(close)
    sl = _rolling_slope(m, MDAYS)
    at_max = sl == sl.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f27_mcdt_127_age_current_macd_below_zero_episode(close: pd.Series) -> pd.Series:
    """Live age of the current MACD < 0 episode (resets on cross above zero)."""
    m, _, _ = _macd(close)
    return _streak_true(m < 0).where(m.notna(), np.nan)


def f27_mcdt_128_age_current_histo_negative_episode(close: pd.Series) -> pd.Series:
    """Live age of the current histogram < 0 episode."""
    _, _, h = _macd(close)
    return _streak_true(h < 0).where(h.notna(), np.nan)


# ============================================================
# Bucket O — acceleration / second-order dynamics (129-135)
# ============================================================

def f27_mcdt_129_macd_acceleration_21(close: pd.Series) -> pd.Series:
    """First diff of 21d MACD slope — monthly MACD acceleration."""
    m, _, _ = _macd(close)
    return _rolling_slope(m, MDAYS).diff()


def f27_mcdt_130_macd_acceleration_63(close: pd.Series) -> pd.Series:
    """First diff of 63d MACD slope — quarterly MACD acceleration."""
    m, _, _ = _macd(close)
    return _rolling_slope(m, QDAYS).diff()


def f27_mcdt_131_histo_acceleration_21(close: pd.Series) -> pd.Series:
    """First diff of 21d histogram slope — histogram acceleration."""
    _, _, h = _macd(close)
    return _rolling_slope(h, MDAYS).diff()


def f27_mcdt_132_macd_second_derivative_5(close: pd.Series) -> pd.Series:
    """Second diff of MACD line (raw two-step diff) — bar-level acceleration."""
    m, _, _ = _macd(close)
    return m.diff().diff()


def f27_mcdt_133_histo_double_smoothed_residual_5(close: pd.Series) -> pd.Series:
    """Histogram minus its 5-bar EMA twice-smoothed — double-smoothing residual (high-frequency component)."""
    _, _, h = _macd(close)
    e1 = _ema(h, WDAYS)
    e2 = _ema(e1, WDAYS)
    return h - e2


def f27_mcdt_134_histo_curvature_proxy_21(close: pd.Series) -> pd.Series:
    """h - 2*lag(11) + lag(21) — discrete second-difference curvature of histogram (right-anchored only)."""
    _, _, h = _macd(close)
    return h - 2.0 * h.shift(11) + h.shift(21)


def f27_mcdt_135_macd_slope_inflection_count_63(close: pd.Series) -> pd.Series:
    """Count of bars where 5d-slope sign flips in past 63 bars — slope-sign inflection count."""
    m, _, _ = _macd(close)
    sl = _rolling_slope(m, WDAYS)
    flip = (sl * sl.shift(1)) < 0
    return flip.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna(), np.nan)


# ============================================================
# Bucket P — long-horizon MACD (50/200/30 config) (136-145)
# ============================================================

def f27_mcdt_136_macd_long_50_200(close: pd.Series) -> pd.Series:
    """Long-cycle MACD (EMA50 - EMA200) — multi-quarter trend signal."""
    return _ema(close, 50) - _ema(close, 200)


def f27_mcdt_137_macd_long_50_200_signal_30(close: pd.Series) -> pd.Series:
    """Long-cycle MACD signal (EMA30 of long MACD)."""
    return _ema(_ema(close, 50) - _ema(close, 200), 30)


def f27_mcdt_138_macd_long_50_200_histogram(close: pd.Series) -> pd.Series:
    """Long-cycle histogram = long-MACD - long-signal — slow momentum-of-momentum."""
    m = _ema(close, 50) - _ema(close, 200)
    return m - _ema(m, 30)


def f27_mcdt_139_macd_long_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if long MACD > 0 — multi-quarter bullish regime state."""
    m = _ema(close, 50) - _ema(close, 200)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f27_mcdt_140_macd_long_bearish_cross_indicator(close: pd.Series) -> pd.Series:
    """1 if long MACD crossed below long signal — slow bearish cross trigger."""
    m = _ema(close, 50) - _ema(close, 200)
    s = _ema(m, 30)
    d = m - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_141_macd_long_persistence_above_zero_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with long MACD > 0 — long-bullish-regime dwell."""
    m = _ema(close, 50) - _ema(close, 200)
    return (m > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(m.notna(), np.nan)


def f27_mcdt_142_macd_long_minus_classical_at_top(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where price = 252d max: (long MACD - classical MACD). Else NaN. Cycle gap at peak."""
    long_m = _ema(close, 50) - _ema(close, 200)
    c, _, _ = _macd(close, 12, 26, 9)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return (long_m - c).where(at_max, np.nan)


def f27_mcdt_143_macd_long_div_vs_price_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using long-cycle MACD over annual horizon: price new 252d high but long MACD below prior 252d max."""
    long_m = _ema(close, 50) - _ema(close, 200)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    m_below = long_m < long_m.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & m_below).astype(float).where(long_m.notna(), np.nan)


def f27_mcdt_144_macd_long_decay_velocity_63(close: pd.Series) -> pd.Series:
    """(63d long MACD max) - long MACD now — quarterly decay since long-MACD peak."""
    long_m = _ema(close, 50) - _ema(close, 200)
    return long_m.rolling(QDAYS, min_periods=MDAYS).max() - long_m


def f27_mcdt_145_macd_long_slope_252(close: pd.Series) -> pd.Series:
    """252d linear slope of long MACD — annual slow-trend direction rate."""
    long_m = _ema(close, 50) - _ema(close, 200)
    return _rolling_slope(long_m, YDAYS)


# ============================================================
# Bucket Q — composite topping (146-150)
# ============================================================

def f27_mcdt_146_topping_score_at_price_peak(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where price = 252d max: sum of {MACD div, histo decline, slope<0, signal cross<21d, PPO>q90}.
    Else NaN. Composite topping count at peak."""
    m, s, h = _macd(close)
    p_new = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div = (m < prior_max).astype(float).fillna(0)
    hdec = (h < h.shift(WDAYS)).astype(float).fillna(0)
    sl = _rolling_slope(m, MDAYS)
    sln = (sl < 0).astype(float).fillna(0)
    d = m - s
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    sc21 = (be.rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    p, _, _ = _ppo(close)
    q = p.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    ph = (p > q).astype(float).fillna(0)
    score = div + hdec + sln + sc21 + ph
    return score.where(p_new, np.nan)


def f27_mcdt_147_macd_failure_breadth_count(close: pd.Series) -> pd.Series:
    """Count of MACD failure indicators currently active across configs:
    {fast<0, classical<0, slow<0, long<0, all-three histos negative}."""
    f = _ema(close, 5) - _ema(close, 35)
    c, _, ch = _macd(close, 12, 26, 9)
    sl = _ema(close, 19) - _ema(close, 39)
    long_m = _ema(close, 50) - _ema(close, 200)
    all_h = (ch < 0).astype(float).fillna(0)
    return ((f < 0).astype(float).fillna(0)
            + (c < 0).astype(float).fillna(0)
            + (sl < 0).astype(float).fillna(0)
            + (long_m < 0).astype(float).fillna(0)
            + all_h).where(c.notna(), np.nan)


def f27_mcdt_148_macd_blowoff_then_collapse_indicator(close: pd.Series) -> pd.Series:
    """1 if MACD reached its 252d max within last 63 bars AND has since dropped by > 50% of that peak's magnitude."""
    m, _, _ = _macd(close)
    rmax252 = m.rolling(YDAYS, min_periods=QDAYS).max()
    bars_since = _bars_since_true(m == rmax252)
    drop = (rmax252 - m) > 0.5 * rmax252.abs()
    return ((bars_since <= QDAYS) & drop).astype(float).where(m.notna(), np.nan)


def f27_mcdt_149_macd_persist_then_div_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if MACD was > 0 for > 50% of past 252 bars AND a bearish divergence fired within last 21 bars
    — long bullish-regime followed by div = classic topping setup."""
    m, _, _ = _macd(close)
    persist = (m > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean() > 0.5
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div_ev = (p_new & (m < prior_max)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return (persist & div_ev).astype(float).where(m.notna(), np.nan)


def f27_mcdt_150_macd_terminal_pattern_aggregate_score(high: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate terminal-pattern score: sum of {blowoff-then-collapse, multi-config-bearish-cross-in-21d,
    long-MACD bearish cross, MACD-div in 21d, PPO above q90 in 21d}."""
    m, s, _ = _macd(close)
    rmax252 = m.rolling(YDAYS, min_periods=QDAYS).max()
    bars_since = _bars_since_true(m == rmax252)
    drop = (rmax252 - m) > 0.5 * rmax252.abs()
    a = ((bars_since <= QDAYS) & drop).astype(float).fillna(0)
    # multi-config bearish in 21d
    cnt = pd.Series(0.0, index=close.index)
    for f, sl, sg in [(5, 35, 5), (12, 26, 9), (19, 39, 9)]:
        m2, s2, _ = _macd(close, f, sl, sg)
        d2 = m2 - s2
        ev = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
        cnt = cnt + (ev.rolling(MDAYS, min_periods=1).sum() > 0).astype(float)
    b = (cnt >= 2.0).astype(float).fillna(0)
    # long bearish cross
    long_m = _ema(close, 50) - _ema(close, 200)
    long_s = _ema(long_m, 30)
    ld = long_m - long_s
    c = (((ld.shift(1) > 0) & (ld <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    # MACD div in 21d
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    d_ev = (p_new & (m < prior_max)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    d = d_ev.astype(float).fillna(0)
    # PPO above q90 in 21d
    p, _, _ = _ppo(close)
    q = p.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    e = ((p > q).astype(float).rolling(MDAYS, min_periods=1).sum() > 0).astype(float).fillna(0)
    return (a + b + c + d + e).where(m.notna(), np.nan)


# ============================================================
#                         REGISTRY 076-150
# ============================================================

MACD_TOPPING_DYNAMICS_BASE_REGISTRY_076_150 = {
    "f27_mcdt_076_macd_norm_atr_21": {"inputs": ["high", "low", "close"], "func": f27_mcdt_076_macd_norm_atr_21},
    "f27_mcdt_077_macd_norm_close": {"inputs": ["close"], "func": f27_mcdt_077_macd_norm_close},
    "f27_mcdt_078_macd_norm_atr_63": {"inputs": ["high", "low", "close"], "func": f27_mcdt_078_macd_norm_atr_63},
    "f27_mcdt_079_histogram_norm_atr_21": {"inputs": ["high", "low", "close"], "func": f27_mcdt_079_histogram_norm_atr_21},
    "f27_mcdt_080_histogram_norm_close": {"inputs": ["close"], "func": f27_mcdt_080_histogram_norm_close},
    "f27_mcdt_081_histogram_to_macd_line_abs_ratio": {"inputs": ["close"], "func": f27_mcdt_081_histogram_to_macd_line_abs_ratio},
    "f27_mcdt_082_ppo_norm_atr_proxy": {"inputs": ["high", "low", "close"], "func": f27_mcdt_082_ppo_norm_atr_proxy},
    "f27_mcdt_083_macd_pos_at_252_high_state": {"inputs": ["high", "close"], "func": f27_mcdt_083_macd_pos_at_252_high_state},
    "f27_mcdt_084_macd_failing_at_close_21d_high": {"inputs": ["high", "close"], "func": f27_mcdt_084_macd_failing_at_close_21d_high},
    "f27_mcdt_085_histogram_negative_with_close_at_252_high": {"inputs": ["high", "close"], "func": f27_mcdt_085_histogram_negative_with_close_at_252_high},
    "f27_mcdt_086_ppo_overstretched_at_price_high_state": {"inputs": ["high", "close"], "func": f27_mcdt_086_ppo_overstretched_at_price_high_state},
    "f27_mcdt_087_histogram_minus_close_pct_extension": {"inputs": ["close"], "func": f27_mcdt_087_histogram_minus_close_pct_extension},
    "f27_mcdt_088_signal_cross_failure_at_top_indicator": {"inputs": ["high", "close"], "func": f27_mcdt_088_signal_cross_failure_at_top_indicator},
    "f27_mcdt_089_macd_decoupled_from_price_indicator_63": {"inputs": ["close"], "func": f27_mcdt_089_macd_decoupled_from_price_indicator_63},
    "f27_mcdt_090_macd_neg_slope_while_price_at_252_high": {"inputs": ["high", "close"], "func": f27_mcdt_090_macd_neg_slope_while_price_at_252_high},
    "f27_mcdt_091_macd_zscore_252": {"inputs": ["close"], "func": f27_mcdt_091_macd_zscore_252},
    "f27_mcdt_092_macd_zscore_504": {"inputs": ["close"], "func": f27_mcdt_092_macd_zscore_504},
    "f27_mcdt_093_macd_pct_rank_252": {"inputs": ["close"], "func": f27_mcdt_093_macd_pct_rank_252},
    "f27_mcdt_094_macd_above_q90_distribution_252": {"inputs": ["close"], "func": f27_mcdt_094_macd_above_q90_distribution_252},
    "f27_mcdt_095_macd_above_q99_distribution_252": {"inputs": ["close"], "func": f27_mcdt_095_macd_above_q99_distribution_252},
    "f27_mcdt_096_macd_skew_63": {"inputs": ["close"], "func": f27_mcdt_096_macd_skew_63},
    "f27_mcdt_097_macd_kurtosis_63": {"inputs": ["close"], "func": f27_mcdt_097_macd_kurtosis_63},
    "f27_mcdt_098_macd_robust_zscore_mad_252": {"inputs": ["close"], "func": f27_mcdt_098_macd_robust_zscore_mad_252},
    "f27_mcdt_099_macd_range_high_minus_low_63": {"inputs": ["close"], "func": f27_mcdt_099_macd_range_high_minus_low_63},
    "f27_mcdt_100_macd_vol_63": {"inputs": ["close"], "func": f27_mcdt_100_macd_vol_63},
    "f27_mcdt_101_histo_4_consecutive_lower_bars_indicator": {"inputs": ["close"], "func": f27_mcdt_101_histo_4_consecutive_lower_bars_indicator},
    "f27_mcdt_102_histo_3_consecutive_neg_smaller_neg_pattern": {"inputs": ["close"], "func": f27_mcdt_102_histo_3_consecutive_neg_smaller_neg_pattern},
    "f27_mcdt_103_histo_swing_low_count_63": {"inputs": ["close"], "func": f27_mcdt_103_histo_swing_low_count_63},
    "f27_mcdt_104_histo_amplitude_decay_63": {"inputs": ["close"], "func": f27_mcdt_104_histo_amplitude_decay_63},
    "f27_mcdt_105_histo_sign_flip_count_63": {"inputs": ["close"], "func": f27_mcdt_105_histo_sign_flip_count_63},
    "f27_mcdt_106_histo_current_positive_streak": {"inputs": ["close"], "func": f27_mcdt_106_histo_current_positive_streak},
    "f27_mcdt_107_histo_consecutive_lower_run_max_63": {"inputs": ["close"], "func": f27_mcdt_107_histo_consecutive_lower_run_max_63},
    "f27_mcdt_108_histo_low_amplitude_indicator_21": {"inputs": ["close"], "func": f27_mcdt_108_histo_low_amplitude_indicator_21},
    "f27_mcdt_109_histo_range_to_macd_range_ratio_63": {"inputs": ["close"], "func": f27_mcdt_109_histo_range_to_macd_range_ratio_63},
    "f27_mcdt_110_histo_skew_63": {"inputs": ["close"], "func": f27_mcdt_110_histo_skew_63},
    "f27_mcdt_111_macd_minus_252d_mean": {"inputs": ["close"], "func": f27_mcdt_111_macd_minus_252d_mean},
    "f27_mcdt_112_macd_minus_504d_mean": {"inputs": ["close"], "func": f27_mcdt_112_macd_minus_504d_mean},
    "f27_mcdt_113_macd_dpo_proxy_21": {"inputs": ["close"], "func": f27_mcdt_113_macd_dpo_proxy_21},
    "f27_mcdt_114_macd_residual_vs_ema21": {"inputs": ["close"], "func": f27_mcdt_114_macd_residual_vs_ema21},
    "f27_mcdt_115_macd_residual_zscore_63": {"inputs": ["close"], "func": f27_mcdt_115_macd_residual_zscore_63},
    "f27_mcdt_116_macd_persistence_of_sign_252": {"inputs": ["close"], "func": f27_mcdt_116_macd_persistence_of_sign_252},
    "f27_mcdt_117_ppo_minus_252d_mean": {"inputs": ["close"], "func": f27_mcdt_117_ppo_minus_252d_mean},
    "f27_mcdt_118_macd_ar1_residual_proxy_21": {"inputs": ["close"], "func": f27_mcdt_118_macd_ar1_residual_proxy_21},
    "f27_mcdt_119_bars_since_macd_above_q95_dist": {"inputs": ["close"], "func": f27_mcdt_119_bars_since_macd_above_q95_dist},
    "f27_mcdt_120_bars_since_histo_above_q95_dist": {"inputs": ["close"], "func": f27_mcdt_120_bars_since_histo_above_q95_dist},
    "f27_mcdt_121_bars_since_macd_252_max": {"inputs": ["close"], "func": f27_mcdt_121_bars_since_macd_252_max},
    "f27_mcdt_122_bars_since_histo_252_max": {"inputs": ["close"], "func": f27_mcdt_122_bars_since_histo_252_max},
    "f27_mcdt_123_bars_since_ppo_252_max": {"inputs": ["close"], "func": f27_mcdt_123_bars_since_ppo_252_max},
    "f27_mcdt_124_bars_since_signal_bearish_cross_above_zero": {"inputs": ["close"], "func": f27_mcdt_124_bars_since_signal_bearish_cross_above_zero},
    "f27_mcdt_125_bars_since_first_macd_div_in_252": {"inputs": ["high", "close"], "func": f27_mcdt_125_bars_since_first_macd_div_in_252},
    "f27_mcdt_126_bars_since_macd_slope_252_max": {"inputs": ["close"], "func": f27_mcdt_126_bars_since_macd_slope_252_max},
    "f27_mcdt_127_age_current_macd_below_zero_episode": {"inputs": ["close"], "func": f27_mcdt_127_age_current_macd_below_zero_episode},
    "f27_mcdt_128_age_current_histo_negative_episode": {"inputs": ["close"], "func": f27_mcdt_128_age_current_histo_negative_episode},
    "f27_mcdt_129_macd_acceleration_21": {"inputs": ["close"], "func": f27_mcdt_129_macd_acceleration_21},
    "f27_mcdt_130_macd_acceleration_63": {"inputs": ["close"], "func": f27_mcdt_130_macd_acceleration_63},
    "f27_mcdt_131_histo_acceleration_21": {"inputs": ["close"], "func": f27_mcdt_131_histo_acceleration_21},
    "f27_mcdt_132_macd_second_derivative_5": {"inputs": ["close"], "func": f27_mcdt_132_macd_second_derivative_5},
    "f27_mcdt_133_histo_double_smoothed_residual_5": {"inputs": ["close"], "func": f27_mcdt_133_histo_double_smoothed_residual_5},
    "f27_mcdt_134_histo_curvature_proxy_21": {"inputs": ["close"], "func": f27_mcdt_134_histo_curvature_proxy_21},
    "f27_mcdt_135_macd_slope_inflection_count_63": {"inputs": ["close"], "func": f27_mcdt_135_macd_slope_inflection_count_63},
    "f27_mcdt_136_macd_long_50_200": {"inputs": ["close"], "func": f27_mcdt_136_macd_long_50_200},
    "f27_mcdt_137_macd_long_50_200_signal_30": {"inputs": ["close"], "func": f27_mcdt_137_macd_long_50_200_signal_30},
    "f27_mcdt_138_macd_long_50_200_histogram": {"inputs": ["close"], "func": f27_mcdt_138_macd_long_50_200_histogram},
    "f27_mcdt_139_macd_long_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_139_macd_long_above_zero_state},
    "f27_mcdt_140_macd_long_bearish_cross_indicator": {"inputs": ["close"], "func": f27_mcdt_140_macd_long_bearish_cross_indicator},
    "f27_mcdt_141_macd_long_persistence_above_zero_252": {"inputs": ["close"], "func": f27_mcdt_141_macd_long_persistence_above_zero_252},
    "f27_mcdt_142_macd_long_minus_classical_at_top": {"inputs": ["high", "close"], "func": f27_mcdt_142_macd_long_minus_classical_at_top},
    "f27_mcdt_143_macd_long_div_vs_price_252": {"inputs": ["high", "close"], "func": f27_mcdt_143_macd_long_div_vs_price_252},
    "f27_mcdt_144_macd_long_decay_velocity_63": {"inputs": ["close"], "func": f27_mcdt_144_macd_long_decay_velocity_63},
    "f27_mcdt_145_macd_long_slope_252": {"inputs": ["close"], "func": f27_mcdt_145_macd_long_slope_252},
    "f27_mcdt_146_topping_score_at_price_peak": {"inputs": ["high", "close"], "func": f27_mcdt_146_topping_score_at_price_peak},
    "f27_mcdt_147_macd_failure_breadth_count": {"inputs": ["close"], "func": f27_mcdt_147_macd_failure_breadth_count},
    "f27_mcdt_148_macd_blowoff_then_collapse_indicator": {"inputs": ["close"], "func": f27_mcdt_148_macd_blowoff_then_collapse_indicator},
    "f27_mcdt_149_macd_persist_then_div_indicator": {"inputs": ["high", "close"], "func": f27_mcdt_149_macd_persist_then_div_indicator},
    "f27_mcdt_150_macd_terminal_pattern_aggregate_score": {"inputs": ["high", "close"], "func": f27_mcdt_150_macd_terminal_pattern_aggregate_score},
}


# === D3 wrappers + registry (076_150) ===
def f27_mcdt_076_macd_norm_atr_21_d3(high, low, close): return f27_mcdt_076_macd_norm_atr_21(high, low, close).diff().diff().diff()
def f27_mcdt_077_macd_norm_close_d3(close): return f27_mcdt_077_macd_norm_close(close).diff().diff().diff()
def f27_mcdt_078_macd_norm_atr_63_d3(high, low, close): return f27_mcdt_078_macd_norm_atr_63(high, low, close).diff().diff().diff()
def f27_mcdt_079_histogram_norm_atr_21_d3(high, low, close): return f27_mcdt_079_histogram_norm_atr_21(high, low, close).diff().diff().diff()
def f27_mcdt_080_histogram_norm_close_d3(close): return f27_mcdt_080_histogram_norm_close(close).diff().diff().diff()
def f27_mcdt_081_histogram_to_macd_line_abs_ratio_d3(close): return f27_mcdt_081_histogram_to_macd_line_abs_ratio(close).diff().diff().diff()
def f27_mcdt_082_ppo_norm_atr_proxy_d3(high, low, close): return f27_mcdt_082_ppo_norm_atr_proxy(high, low, close).diff().diff().diff()
def f27_mcdt_083_macd_pos_at_252_high_state_d3(high, close): return f27_mcdt_083_macd_pos_at_252_high_state(high, close).diff().diff().diff()
def f27_mcdt_084_macd_failing_at_close_21d_high_d3(high, close): return f27_mcdt_084_macd_failing_at_close_21d_high(high, close).diff().diff().diff()
def f27_mcdt_085_histogram_negative_with_close_at_252_high_d3(high, close): return f27_mcdt_085_histogram_negative_with_close_at_252_high(high, close).diff().diff().diff()
def f27_mcdt_086_ppo_overstretched_at_price_high_state_d3(high, close): return f27_mcdt_086_ppo_overstretched_at_price_high_state(high, close).diff().diff().diff()
def f27_mcdt_087_histogram_minus_close_pct_extension_d3(close): return f27_mcdt_087_histogram_minus_close_pct_extension(close).diff().diff().diff()
def f27_mcdt_088_signal_cross_failure_at_top_indicator_d3(high, close): return f27_mcdt_088_signal_cross_failure_at_top_indicator(high, close).diff().diff().diff()
def f27_mcdt_089_macd_decoupled_from_price_indicator_63_d3(close): return f27_mcdt_089_macd_decoupled_from_price_indicator_63(close).diff().diff().diff()
def f27_mcdt_090_macd_neg_slope_while_price_at_252_high_d3(high, close): return f27_mcdt_090_macd_neg_slope_while_price_at_252_high(high, close).diff().diff().diff()
def f27_mcdt_091_macd_zscore_252_d3(close): return f27_mcdt_091_macd_zscore_252(close).diff().diff().diff()
def f27_mcdt_092_macd_zscore_504_d3(close): return f27_mcdt_092_macd_zscore_504(close).diff().diff().diff()
def f27_mcdt_093_macd_pct_rank_252_d3(close): return f27_mcdt_093_macd_pct_rank_252(close).diff().diff().diff()
def f27_mcdt_094_macd_above_q90_distribution_252_d3(close): return f27_mcdt_094_macd_above_q90_distribution_252(close).diff().diff().diff()
def f27_mcdt_095_macd_above_q99_distribution_252_d3(close): return f27_mcdt_095_macd_above_q99_distribution_252(close).diff().diff().diff()
def f27_mcdt_096_macd_skew_63_d3(close): return f27_mcdt_096_macd_skew_63(close).diff().diff().diff()
def f27_mcdt_097_macd_kurtosis_63_d3(close): return f27_mcdt_097_macd_kurtosis_63(close).diff().diff().diff()
def f27_mcdt_098_macd_robust_zscore_mad_252_d3(close): return f27_mcdt_098_macd_robust_zscore_mad_252(close).diff().diff().diff()
def f27_mcdt_099_macd_range_high_minus_low_63_d3(close): return f27_mcdt_099_macd_range_high_minus_low_63(close).diff().diff().diff()
def f27_mcdt_100_macd_vol_63_d3(close): return f27_mcdt_100_macd_vol_63(close).diff().diff().diff()
def f27_mcdt_101_histo_4_consecutive_lower_bars_indicator_d3(close): return f27_mcdt_101_histo_4_consecutive_lower_bars_indicator(close).diff().diff().diff()
def f27_mcdt_102_histo_3_consecutive_neg_smaller_neg_pattern_d3(close): return f27_mcdt_102_histo_3_consecutive_neg_smaller_neg_pattern(close).diff().diff().diff()
def f27_mcdt_103_histo_swing_low_count_63_d3(close): return f27_mcdt_103_histo_swing_low_count_63(close).diff().diff().diff()
def f27_mcdt_104_histo_amplitude_decay_63_d3(close): return f27_mcdt_104_histo_amplitude_decay_63(close).diff().diff().diff()
def f27_mcdt_105_histo_sign_flip_count_63_d3(close): return f27_mcdt_105_histo_sign_flip_count_63(close).diff().diff().diff()
def f27_mcdt_106_histo_current_positive_streak_d3(close): return f27_mcdt_106_histo_current_positive_streak(close).diff().diff().diff()
def f27_mcdt_107_histo_consecutive_lower_run_max_63_d3(close): return f27_mcdt_107_histo_consecutive_lower_run_max_63(close).diff().diff().diff()
def f27_mcdt_108_histo_low_amplitude_indicator_21_d3(close): return f27_mcdt_108_histo_low_amplitude_indicator_21(close).diff().diff().diff()
def f27_mcdt_109_histo_range_to_macd_range_ratio_63_d3(close): return f27_mcdt_109_histo_range_to_macd_range_ratio_63(close).diff().diff().diff()
def f27_mcdt_110_histo_skew_63_d3(close): return f27_mcdt_110_histo_skew_63(close).diff().diff().diff()
def f27_mcdt_111_macd_minus_252d_mean_d3(close): return f27_mcdt_111_macd_minus_252d_mean(close).diff().diff().diff()
def f27_mcdt_112_macd_minus_504d_mean_d3(close): return f27_mcdt_112_macd_minus_504d_mean(close).diff().diff().diff()
def f27_mcdt_113_macd_dpo_proxy_21_d3(close): return f27_mcdt_113_macd_dpo_proxy_21(close).diff().diff().diff()
def f27_mcdt_114_macd_residual_vs_ema21_d3(close): return f27_mcdt_114_macd_residual_vs_ema21(close).diff().diff().diff()
def f27_mcdt_115_macd_residual_zscore_63_d3(close): return f27_mcdt_115_macd_residual_zscore_63(close).diff().diff().diff()
def f27_mcdt_116_macd_persistence_of_sign_252_d3(close): return f27_mcdt_116_macd_persistence_of_sign_252(close).diff().diff().diff()
def f27_mcdt_117_ppo_minus_252d_mean_d3(close): return f27_mcdt_117_ppo_minus_252d_mean(close).diff().diff().diff()
def f27_mcdt_118_macd_ar1_residual_proxy_21_d3(close): return f27_mcdt_118_macd_ar1_residual_proxy_21(close).diff().diff().diff()
def f27_mcdt_119_bars_since_macd_above_q95_dist_d3(close): return f27_mcdt_119_bars_since_macd_above_q95_dist(close).diff().diff().diff()
def f27_mcdt_120_bars_since_histo_above_q95_dist_d3(close): return f27_mcdt_120_bars_since_histo_above_q95_dist(close).diff().diff().diff()
def f27_mcdt_121_bars_since_macd_252_max_d3(close): return f27_mcdt_121_bars_since_macd_252_max(close).diff().diff().diff()
def f27_mcdt_122_bars_since_histo_252_max_d3(close): return f27_mcdt_122_bars_since_histo_252_max(close).diff().diff().diff()
def f27_mcdt_123_bars_since_ppo_252_max_d3(close): return f27_mcdt_123_bars_since_ppo_252_max(close).diff().diff().diff()
def f27_mcdt_124_bars_since_signal_bearish_cross_above_zero_d3(close): return f27_mcdt_124_bars_since_signal_bearish_cross_above_zero(close).diff().diff().diff()
def f27_mcdt_125_bars_since_first_macd_div_in_252_d3(high, close): return f27_mcdt_125_bars_since_first_macd_div_in_252(high, close).diff().diff().diff()
def f27_mcdt_126_bars_since_macd_slope_252_max_d3(close): return f27_mcdt_126_bars_since_macd_slope_252_max(close).diff().diff().diff()
def f27_mcdt_127_age_current_macd_below_zero_episode_d3(close): return f27_mcdt_127_age_current_macd_below_zero_episode(close).diff().diff().diff()
def f27_mcdt_128_age_current_histo_negative_episode_d3(close): return f27_mcdt_128_age_current_histo_negative_episode(close).diff().diff().diff()
def f27_mcdt_129_macd_acceleration_21_d3(close): return f27_mcdt_129_macd_acceleration_21(close).diff().diff().diff()
def f27_mcdt_130_macd_acceleration_63_d3(close): return f27_mcdt_130_macd_acceleration_63(close).diff().diff().diff()
def f27_mcdt_131_histo_acceleration_21_d3(close): return f27_mcdt_131_histo_acceleration_21(close).diff().diff().diff()
def f27_mcdt_132_macd_second_derivative_5_d3(close): return f27_mcdt_132_macd_second_derivative_5(close).diff().diff().diff()
def f27_mcdt_133_histo_double_smoothed_residual_5_d3(close): return f27_mcdt_133_histo_double_smoothed_residual_5(close).diff().diff().diff()
def f27_mcdt_134_histo_curvature_proxy_21_d3(close): return f27_mcdt_134_histo_curvature_proxy_21(close).diff().diff().diff()
def f27_mcdt_135_macd_slope_inflection_count_63_d3(close): return f27_mcdt_135_macd_slope_inflection_count_63(close).diff().diff().diff()
def f27_mcdt_136_macd_long_50_200_d3(close): return f27_mcdt_136_macd_long_50_200(close).diff().diff().diff()
def f27_mcdt_137_macd_long_50_200_signal_30_d3(close): return f27_mcdt_137_macd_long_50_200_signal_30(close).diff().diff().diff()
def f27_mcdt_138_macd_long_50_200_histogram_d3(close): return f27_mcdt_138_macd_long_50_200_histogram(close).diff().diff().diff()
def f27_mcdt_139_macd_long_above_zero_state_d3(close): return f27_mcdt_139_macd_long_above_zero_state(close).diff().diff().diff()
def f27_mcdt_140_macd_long_bearish_cross_indicator_d3(close): return f27_mcdt_140_macd_long_bearish_cross_indicator(close).diff().diff().diff()
def f27_mcdt_141_macd_long_persistence_above_zero_252_d3(close): return f27_mcdt_141_macd_long_persistence_above_zero_252(close).diff().diff().diff()
def f27_mcdt_142_macd_long_minus_classical_at_top_d3(high, close): return f27_mcdt_142_macd_long_minus_classical_at_top(high, close).diff().diff().diff()
def f27_mcdt_143_macd_long_div_vs_price_252_d3(high, close): return f27_mcdt_143_macd_long_div_vs_price_252(high, close).diff().diff().diff()
def f27_mcdt_144_macd_long_decay_velocity_63_d3(close): return f27_mcdt_144_macd_long_decay_velocity_63(close).diff().diff().diff()
def f27_mcdt_145_macd_long_slope_252_d3(close): return f27_mcdt_145_macd_long_slope_252(close).diff().diff().diff()
def f27_mcdt_146_topping_score_at_price_peak_d3(high, close): return f27_mcdt_146_topping_score_at_price_peak(high, close).diff().diff().diff()
def f27_mcdt_147_macd_failure_breadth_count_d3(close): return f27_mcdt_147_macd_failure_breadth_count(close).diff().diff().diff()
def f27_mcdt_148_macd_blowoff_then_collapse_indicator_d3(close): return f27_mcdt_148_macd_blowoff_then_collapse_indicator(close).diff().diff().diff()
def f27_mcdt_149_macd_persist_then_div_indicator_d3(high, close): return f27_mcdt_149_macd_persist_then_div_indicator(high, close).diff().diff().diff()
def f27_mcdt_150_macd_terminal_pattern_aggregate_score_d3(high, close): return f27_mcdt_150_macd_terminal_pattern_aggregate_score(high, close).diff().diff().diff()

MACD_TOPPING_DYNAMICS_D3_REGISTRY_076_150 = {
    "f27_mcdt_076_macd_norm_atr_21_d3": {"inputs": ["high", "low", "close"], "func": f27_mcdt_076_macd_norm_atr_21_d3},
    "f27_mcdt_077_macd_norm_close_d3": {"inputs": ["close"], "func": f27_mcdt_077_macd_norm_close_d3},
    "f27_mcdt_078_macd_norm_atr_63_d3": {"inputs": ["high", "low", "close"], "func": f27_mcdt_078_macd_norm_atr_63_d3},
    "f27_mcdt_079_histogram_norm_atr_21_d3": {"inputs": ["high", "low", "close"], "func": f27_mcdt_079_histogram_norm_atr_21_d3},
    "f27_mcdt_080_histogram_norm_close_d3": {"inputs": ["close"], "func": f27_mcdt_080_histogram_norm_close_d3},
    "f27_mcdt_081_histogram_to_macd_line_abs_ratio_d3": {"inputs": ["close"], "func": f27_mcdt_081_histogram_to_macd_line_abs_ratio_d3},
    "f27_mcdt_082_ppo_norm_atr_proxy_d3": {"inputs": ["high", "low", "close"], "func": f27_mcdt_082_ppo_norm_atr_proxy_d3},
    "f27_mcdt_083_macd_pos_at_252_high_state_d3": {"inputs": ["high", "close"], "func": f27_mcdt_083_macd_pos_at_252_high_state_d3},
    "f27_mcdt_084_macd_failing_at_close_21d_high_d3": {"inputs": ["high", "close"], "func": f27_mcdt_084_macd_failing_at_close_21d_high_d3},
    "f27_mcdt_085_histogram_negative_with_close_at_252_high_d3": {"inputs": ["high", "close"], "func": f27_mcdt_085_histogram_negative_with_close_at_252_high_d3},
    "f27_mcdt_086_ppo_overstretched_at_price_high_state_d3": {"inputs": ["high", "close"], "func": f27_mcdt_086_ppo_overstretched_at_price_high_state_d3},
    "f27_mcdt_087_histogram_minus_close_pct_extension_d3": {"inputs": ["close"], "func": f27_mcdt_087_histogram_minus_close_pct_extension_d3},
    "f27_mcdt_088_signal_cross_failure_at_top_indicator_d3": {"inputs": ["high", "close"], "func": f27_mcdt_088_signal_cross_failure_at_top_indicator_d3},
    "f27_mcdt_089_macd_decoupled_from_price_indicator_63_d3": {"inputs": ["close"], "func": f27_mcdt_089_macd_decoupled_from_price_indicator_63_d3},
    "f27_mcdt_090_macd_neg_slope_while_price_at_252_high_d3": {"inputs": ["high", "close"], "func": f27_mcdt_090_macd_neg_slope_while_price_at_252_high_d3},
    "f27_mcdt_091_macd_zscore_252_d3": {"inputs": ["close"], "func": f27_mcdt_091_macd_zscore_252_d3},
    "f27_mcdt_092_macd_zscore_504_d3": {"inputs": ["close"], "func": f27_mcdt_092_macd_zscore_504_d3},
    "f27_mcdt_093_macd_pct_rank_252_d3": {"inputs": ["close"], "func": f27_mcdt_093_macd_pct_rank_252_d3},
    "f27_mcdt_094_macd_above_q90_distribution_252_d3": {"inputs": ["close"], "func": f27_mcdt_094_macd_above_q90_distribution_252_d3},
    "f27_mcdt_095_macd_above_q99_distribution_252_d3": {"inputs": ["close"], "func": f27_mcdt_095_macd_above_q99_distribution_252_d3},
    "f27_mcdt_096_macd_skew_63_d3": {"inputs": ["close"], "func": f27_mcdt_096_macd_skew_63_d3},
    "f27_mcdt_097_macd_kurtosis_63_d3": {"inputs": ["close"], "func": f27_mcdt_097_macd_kurtosis_63_d3},
    "f27_mcdt_098_macd_robust_zscore_mad_252_d3": {"inputs": ["close"], "func": f27_mcdt_098_macd_robust_zscore_mad_252_d3},
    "f27_mcdt_099_macd_range_high_minus_low_63_d3": {"inputs": ["close"], "func": f27_mcdt_099_macd_range_high_minus_low_63_d3},
    "f27_mcdt_100_macd_vol_63_d3": {"inputs": ["close"], "func": f27_mcdt_100_macd_vol_63_d3},
    "f27_mcdt_101_histo_4_consecutive_lower_bars_indicator_d3": {"inputs": ["close"], "func": f27_mcdt_101_histo_4_consecutive_lower_bars_indicator_d3},
    "f27_mcdt_102_histo_3_consecutive_neg_smaller_neg_pattern_d3": {"inputs": ["close"], "func": f27_mcdt_102_histo_3_consecutive_neg_smaller_neg_pattern_d3},
    "f27_mcdt_103_histo_swing_low_count_63_d3": {"inputs": ["close"], "func": f27_mcdt_103_histo_swing_low_count_63_d3},
    "f27_mcdt_104_histo_amplitude_decay_63_d3": {"inputs": ["close"], "func": f27_mcdt_104_histo_amplitude_decay_63_d3},
    "f27_mcdt_105_histo_sign_flip_count_63_d3": {"inputs": ["close"], "func": f27_mcdt_105_histo_sign_flip_count_63_d3},
    "f27_mcdt_106_histo_current_positive_streak_d3": {"inputs": ["close"], "func": f27_mcdt_106_histo_current_positive_streak_d3},
    "f27_mcdt_107_histo_consecutive_lower_run_max_63_d3": {"inputs": ["close"], "func": f27_mcdt_107_histo_consecutive_lower_run_max_63_d3},
    "f27_mcdt_108_histo_low_amplitude_indicator_21_d3": {"inputs": ["close"], "func": f27_mcdt_108_histo_low_amplitude_indicator_21_d3},
    "f27_mcdt_109_histo_range_to_macd_range_ratio_63_d3": {"inputs": ["close"], "func": f27_mcdt_109_histo_range_to_macd_range_ratio_63_d3},
    "f27_mcdt_110_histo_skew_63_d3": {"inputs": ["close"], "func": f27_mcdt_110_histo_skew_63_d3},
    "f27_mcdt_111_macd_minus_252d_mean_d3": {"inputs": ["close"], "func": f27_mcdt_111_macd_minus_252d_mean_d3},
    "f27_mcdt_112_macd_minus_504d_mean_d3": {"inputs": ["close"], "func": f27_mcdt_112_macd_minus_504d_mean_d3},
    "f27_mcdt_113_macd_dpo_proxy_21_d3": {"inputs": ["close"], "func": f27_mcdt_113_macd_dpo_proxy_21_d3},
    "f27_mcdt_114_macd_residual_vs_ema21_d3": {"inputs": ["close"], "func": f27_mcdt_114_macd_residual_vs_ema21_d3},
    "f27_mcdt_115_macd_residual_zscore_63_d3": {"inputs": ["close"], "func": f27_mcdt_115_macd_residual_zscore_63_d3},
    "f27_mcdt_116_macd_persistence_of_sign_252_d3": {"inputs": ["close"], "func": f27_mcdt_116_macd_persistence_of_sign_252_d3},
    "f27_mcdt_117_ppo_minus_252d_mean_d3": {"inputs": ["close"], "func": f27_mcdt_117_ppo_minus_252d_mean_d3},
    "f27_mcdt_118_macd_ar1_residual_proxy_21_d3": {"inputs": ["close"], "func": f27_mcdt_118_macd_ar1_residual_proxy_21_d3},
    "f27_mcdt_119_bars_since_macd_above_q95_dist_d3": {"inputs": ["close"], "func": f27_mcdt_119_bars_since_macd_above_q95_dist_d3},
    "f27_mcdt_120_bars_since_histo_above_q95_dist_d3": {"inputs": ["close"], "func": f27_mcdt_120_bars_since_histo_above_q95_dist_d3},
    "f27_mcdt_121_bars_since_macd_252_max_d3": {"inputs": ["close"], "func": f27_mcdt_121_bars_since_macd_252_max_d3},
    "f27_mcdt_122_bars_since_histo_252_max_d3": {"inputs": ["close"], "func": f27_mcdt_122_bars_since_histo_252_max_d3},
    "f27_mcdt_123_bars_since_ppo_252_max_d3": {"inputs": ["close"], "func": f27_mcdt_123_bars_since_ppo_252_max_d3},
    "f27_mcdt_124_bars_since_signal_bearish_cross_above_zero_d3": {"inputs": ["close"], "func": f27_mcdt_124_bars_since_signal_bearish_cross_above_zero_d3},
    "f27_mcdt_125_bars_since_first_macd_div_in_252_d3": {"inputs": ["high", "close"], "func": f27_mcdt_125_bars_since_first_macd_div_in_252_d3},
    "f27_mcdt_126_bars_since_macd_slope_252_max_d3": {"inputs": ["close"], "func": f27_mcdt_126_bars_since_macd_slope_252_max_d3},
    "f27_mcdt_127_age_current_macd_below_zero_episode_d3": {"inputs": ["close"], "func": f27_mcdt_127_age_current_macd_below_zero_episode_d3},
    "f27_mcdt_128_age_current_histo_negative_episode_d3": {"inputs": ["close"], "func": f27_mcdt_128_age_current_histo_negative_episode_d3},
    "f27_mcdt_129_macd_acceleration_21_d3": {"inputs": ["close"], "func": f27_mcdt_129_macd_acceleration_21_d3},
    "f27_mcdt_130_macd_acceleration_63_d3": {"inputs": ["close"], "func": f27_mcdt_130_macd_acceleration_63_d3},
    "f27_mcdt_131_histo_acceleration_21_d3": {"inputs": ["close"], "func": f27_mcdt_131_histo_acceleration_21_d3},
    "f27_mcdt_132_macd_second_derivative_5_d3": {"inputs": ["close"], "func": f27_mcdt_132_macd_second_derivative_5_d3},
    "f27_mcdt_133_histo_double_smoothed_residual_5_d3": {"inputs": ["close"], "func": f27_mcdt_133_histo_double_smoothed_residual_5_d3},
    "f27_mcdt_134_histo_curvature_proxy_21_d3": {"inputs": ["close"], "func": f27_mcdt_134_histo_curvature_proxy_21_d3},
    "f27_mcdt_135_macd_slope_inflection_count_63_d3": {"inputs": ["close"], "func": f27_mcdt_135_macd_slope_inflection_count_63_d3},
    "f27_mcdt_136_macd_long_50_200_d3": {"inputs": ["close"], "func": f27_mcdt_136_macd_long_50_200_d3},
    "f27_mcdt_137_macd_long_50_200_signal_30_d3": {"inputs": ["close"], "func": f27_mcdt_137_macd_long_50_200_signal_30_d3},
    "f27_mcdt_138_macd_long_50_200_histogram_d3": {"inputs": ["close"], "func": f27_mcdt_138_macd_long_50_200_histogram_d3},
    "f27_mcdt_139_macd_long_above_zero_state_d3": {"inputs": ["close"], "func": f27_mcdt_139_macd_long_above_zero_state_d3},
    "f27_mcdt_140_macd_long_bearish_cross_indicator_d3": {"inputs": ["close"], "func": f27_mcdt_140_macd_long_bearish_cross_indicator_d3},
    "f27_mcdt_141_macd_long_persistence_above_zero_252_d3": {"inputs": ["close"], "func": f27_mcdt_141_macd_long_persistence_above_zero_252_d3},
    "f27_mcdt_142_macd_long_minus_classical_at_top_d3": {"inputs": ["high", "close"], "func": f27_mcdt_142_macd_long_minus_classical_at_top_d3},
    "f27_mcdt_143_macd_long_div_vs_price_252_d3": {"inputs": ["high", "close"], "func": f27_mcdt_143_macd_long_div_vs_price_252_d3},
    "f27_mcdt_144_macd_long_decay_velocity_63_d3": {"inputs": ["close"], "func": f27_mcdt_144_macd_long_decay_velocity_63_d3},
    "f27_mcdt_145_macd_long_slope_252_d3": {"inputs": ["close"], "func": f27_mcdt_145_macd_long_slope_252_d3},
    "f27_mcdt_146_topping_score_at_price_peak_d3": {"inputs": ["high", "close"], "func": f27_mcdt_146_topping_score_at_price_peak_d3},
    "f27_mcdt_147_macd_failure_breadth_count_d3": {"inputs": ["close"], "func": f27_mcdt_147_macd_failure_breadth_count_d3},
    "f27_mcdt_148_macd_blowoff_then_collapse_indicator_d3": {"inputs": ["close"], "func": f27_mcdt_148_macd_blowoff_then_collapse_indicator_d3},
    "f27_mcdt_149_macd_persist_then_div_indicator_d3": {"inputs": ["high", "close"], "func": f27_mcdt_149_macd_persist_then_div_indicator_d3},
    "f27_mcdt_150_macd_terminal_pattern_aggregate_score_d3": {"inputs": ["high", "close"], "func": f27_mcdt_150_macd_terminal_pattern_aggregate_score_d3},
}
