"""coppock_curve_kst d1 features 226-300 — Pipeline 1b-technical (gap-fill extension).

Extends 001-225 with acceleration-crossover events (d²Coppock / d²KST zero-cross),
multi-horizon smoothed-momentum breadth, rounded-top / plateau shape detection,
long-cycle momentum confirmation at price extremes, multi-indicator alignment
composites, cycle-length analysis, and master long-cycle topping scores.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260


# ---------------------------- standard helpers ----------------------------

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


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _wma(s, n):
    weights = np.arange(1, n + 1, dtype=float)
    wsum = weights.sum()
    def _ww(w):
        if np.isnan(w).any():
            return np.nan
        return float(np.dot(w, weights) / wsum)
    return s.rolling(n, min_periods=n).apply(_ww, raw=True)


def _roc_pct(s, n):
    return s.pct_change(n) * 100.0


# ---------------------------- Coppock / KST helpers ----------------------------

def _coppock(close, n_long, n_short, n_wma):
    return _wma(_roc_pct(close, n_long) + _roc_pct(close, n_short), n_wma)


def _coppock_annual(close):
    return _coppock(close, 294, 231, 210)


def _coppock_biennial(close):
    return _coppock(close, DDAYS_2Y, 378, 210)


def _coppock_semi_annual(close):
    return _coppock(close, 126, 84, 42)


def _coppock_quarterly(close):
    return _coppock(close, QDAYS, 42, MDAYS)


def _kst(close):
    return (1.0 * _sma(_roc_pct(close, 10), 10)
            + 2.0 * _sma(_roc_pct(close, 15), 10)
            + 3.0 * _sma(_roc_pct(close, 20), 10)
            + 4.0 * _sma(_roc_pct(close, 30), 15))


def _kst_long_term(close):
    return (1.0 * _sma(_roc_pct(close, 65), 21)
            + 2.0 * _sma(_roc_pct(close, 130), 21)
            + 3.0 * _sma(_roc_pct(close, 195), 21)
            + 4.0 * _sma(_roc_pct(close, 260), 42))


def _kst_signal(close, n_sig=9):
    return _sma(_kst(close), n_sig)


# ============================================================
# Bucket ZZ — Coppock acceleration crossover events (226-235)
# ============================================================

def f33_cpkt_226_coppock_d2_zero_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where d²Coppock-annual crosses + → - (acceleration rollover event)."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan)


def f33_cpkt_227_coppock_d2_zero_cross_bullish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where d²Coppock-annual crosses - → + (acceleration bottoming)."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) < 0) & (d2 >= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan)


def f33_cpkt_228_days_since_coppock_d2_bearish_event(close: pd.Series) -> pd.Series:
    """Bars since most recent d²Coppock-annual bearish acceleration crossover."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_229_coppock_d2_zero_cross_count_252d(close: pd.Series) -> pd.Series:
    """Count of d²Coppock-annual bearish acceleration crossovers in trailing 252d."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_230_coppock_d2_zero_cross_count_504d(close: pd.Series) -> pd.Series:
    """Count of d²Coppock bearish acceleration events in trailing 504d."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f33_cpkt_231_coppock_quarterly_d2_zero_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where d²Coppock-quarterly crosses + → - (short-cycle acceleration rollover)."""
    c = _coppock_quarterly(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan)


def f33_cpkt_232_coppock_d2_at_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when d²Coppock bearish event fires AND close within 1% of 252d max."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (flag * near).where(flag.notna() & near.notna(), np.nan)


def f33_cpkt_233_coppock_d2_magnitude_at_event_held_forward(close: pd.Series) -> pd.Series:
    """d²Coppock value at the moment of each bearish event, held forward — recent acceleration shock magnitude."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0))
    return d2.where(flag, np.nan).ffill().abs()


def f33_cpkt_234_coppock_jerk_d3_value_21d(close: pd.Series) -> pd.Series:
    """d³Coppock-annual (third derivative) — jerk / change-in-acceleration."""
    c = _coppock_annual(close)
    return _rolling_slope(_rolling_slope(_rolling_slope(c, MDAYS), MDAYS), MDAYS)


def f33_cpkt_235_coppock_jerk_above_threshold_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of |d³Coppock| in trailing 252d — jerk-intensity ranking."""
    c = _coppock_annual(close)
    j = _rolling_slope(_rolling_slope(_rolling_slope(c, MDAYS), MDAYS), MDAYS).abs()
    return _pct_rank(j, YDAYS)


# ============================================================
# Bucket AAA — KST acceleration crossover events (236-245)
# ============================================================

def f33_cpkt_236_kst_d2_zero_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where d²KST crosses + → -."""
    k = _kst(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan)


def f33_cpkt_237_kst_d2_zero_cross_bullish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where d²KST crosses - → +."""
    k = _kst(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    return ((d2.shift(1) < 0) & (d2 >= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan)


def f33_cpkt_238_days_since_kst_d2_bearish_event(close: pd.Series) -> pd.Series:
    """Bars since most recent d²KST bearish acceleration crossover."""
    k = _kst(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_239_kst_d2_zero_cross_count_252d(close: pd.Series) -> pd.Series:
    """Count of d²KST bearish acceleration events in trailing 252d."""
    k = _kst(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_240_kst_long_term_d2_zero_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where d²(long-term KST) crosses + → -."""
    k = _kst_long_term(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan)


def f33_cpkt_241_kst_d2_at_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when d²KST bearish event fires AND close near 252d max."""
    k = _kst(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (flag * near).where(flag.notna() & near.notna(), np.nan)


def f33_cpkt_242_kst_jerk_d3_value_21d(close: pd.Series) -> pd.Series:
    """d³KST (jerk)."""
    k = _kst(close)
    return _rolling_slope(_rolling_slope(_rolling_slope(k, MDAYS), MDAYS), MDAYS)


def f33_cpkt_243_kst_jerk_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of |d³KST| in trailing 252d."""
    k = _kst(close)
    j = _rolling_slope(_rolling_slope(_rolling_slope(k, MDAYS), MDAYS), MDAYS).abs()
    return _pct_rank(j, YDAYS)


def f33_cpkt_244_coppock_AND_kst_d2_joint_bearish_event(close: pd.Series) -> pd.Series:
    """+1 when BOTH Coppock-annual and KST d²-zero-cross bearish events fire within last 5 bars."""
    c = _coppock_annual(close); k = _kst(close)
    d2c = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    d2k = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    flag_c = ((d2c.shift(1) > 0) & (d2c <= 0)).astype(float).rolling(WDAYS, min_periods=1).max()
    flag_k = ((d2k.shift(1) > 0) & (d2k <= 0)).astype(float).rolling(WDAYS, min_periods=1).max()
    return (flag_c * flag_k).where(d2c.notna() & d2k.notna(), np.nan)


def f33_cpkt_245_acceleration_disagreement_indicator_63d(close: pd.Series) -> pd.Series:
    """+1 when d²Coppock-annual > 0 (accelerating up) AND d²KST < 0 (accelerating down) — disagreement signal."""
    c = _coppock_annual(close); k = _kst(close)
    d2c = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    d2k = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    return ((d2c > 0) & (d2k < 0)).astype(float).where(d2c.notna() & d2k.notna(), np.nan)


# ============================================================
# Bucket BBB — Multi-horizon smoothed-momentum breadth (246-255)
# ============================================================

def f33_cpkt_246_4cycle_coppock_all_positive_indicator(close: pd.Series) -> pd.Series:
    """+1 when ALL 4 Coppock variants (quarterly/semi/annual/biennial) > 0."""
    parts = [
        (_coppock_quarterly(close) > 0).astype(float),
        (_coppock_semi_annual(close) > 0).astype(float),
        (_coppock_annual(close) > 0).astype(float),
        (_coppock_biennial(close) > 0).astype(float),
    ]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return (df.sum(axis=1) == 4).astype(float)


def f33_cpkt_247_4cycle_coppock_all_negative_indicator(close: pd.Series) -> pd.Series:
    """+1 when ALL 4 Coppock variants < 0."""
    parts = [
        (_coppock_quarterly(close) < 0).astype(float),
        (_coppock_semi_annual(close) < 0).astype(float),
        (_coppock_annual(close) < 0).astype(float),
        (_coppock_biennial(close) < 0).astype(float),
    ]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return (df.sum(axis=1) == 4).astype(float)


def f33_cpkt_248_4cycle_coppock_fraction_positive(close: pd.Series) -> pd.Series:
    """Fraction (0..1) of 4 Coppock variants currently > 0."""
    parts = [
        (_coppock_quarterly(close) > 0).astype(float),
        (_coppock_semi_annual(close) > 0).astype(float),
        (_coppock_annual(close) > 0).astype(float),
        (_coppock_biennial(close) > 0).astype(float),
    ]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def f33_cpkt_249_4cycle_coppock_fraction_falling_21d(close: pd.Series) -> pd.Series:
    """Fraction of 4 Coppock variants with negative 21d-slope."""
    parts = [
        (_rolling_slope(_coppock_quarterly(close), MDAYS) < 0).astype(float),
        (_rolling_slope(_coppock_semi_annual(close), MDAYS) < 0).astype(float),
        (_rolling_slope(_coppock_annual(close), MDAYS) < 0).astype(float),
        (_rolling_slope(_coppock_biennial(close), MDAYS) < 0).astype(float),
    ]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def f33_cpkt_250_4cycle_coppock_consensus_bearish_rollover_indicator(close: pd.Series) -> pd.Series:
    """+1 when fraction-falling-21d == 1.0 (all 4 Coppock variants rolling over simultaneously)."""
    return (f33_cpkt_249_4cycle_coppock_fraction_falling_21d(close) == 1.0).astype(float)


def f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close: pd.Series) -> pd.Series:
    """Fraction (0..1) of 8 smoothed-momentum indicators currently > 0:
    4 Coppock + KST std + KST long-term + KST signal-positive + DPO63."""
    parts = [
        (_coppock_quarterly(close) > 0).astype(float),
        (_coppock_semi_annual(close) > 0).astype(float),
        (_coppock_annual(close) > 0).astype(float),
        (_coppock_biennial(close) > 0).astype(float),
        (_kst(close) > 0).astype(float),
        (_kst_long_term(close) > 0).astype(float),
        (_kst(close) > _kst_signal(close, 9)).astype(float),
        ((close - _sma(close, QDAYS)) > 0).astype(float),
    ]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def f33_cpkt_252_smoothed_momentum_breadth_change_over_21d(close: pd.Series) -> pd.Series:
    """21d change in 8-indicator-breadth — is momentum-bullishness expanding or contracting?"""
    b = f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close)
    return b - b.shift(MDAYS)


def f33_cpkt_253_smoothed_momentum_breadth_below_threshold_at_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when 8-indicator-breadth drops below 0.5 AND close within 1% of 252d max (breadth collapse at high)."""
    b = f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((b < 0.5) & (near == 1)).astype(float).where(b.notna() & near.notna(), np.nan)


def f33_cpkt_254_smoothed_momentum_breadth_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 8-indicator-breadth over 252d."""
    return _rolling_zscore(f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close), YDAYS)


def f33_cpkt_255_smoothed_momentum_breadth_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 8-indicator-breadth in trailing 252d."""
    return _pct_rank(f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close), YDAYS)


# ============================================================
# Bucket CCC — Rounded-top / plateau shape detection (256-265)
# ============================================================

def f33_cpkt_256_coppock_rounded_top_shape_252d(close: pd.Series) -> pd.Series:
    """Rounded-top score: stddev of Coppock-annual values in trailing 21d, normalized by stddev in trailing 252d.
    Low ratio = flat/rounded top; high ratio = sharp peak."""
    c = _coppock_annual(close)
    sd21 = c.rolling(MDAYS, min_periods=WDAYS).std()
    sd252 = c.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(sd21, sd252)


def f33_cpkt_257_kst_rounded_top_shape_252d(close: pd.Series) -> pd.Series:
    """KST rounded-top score (std-ratio 21d / 252d)."""
    k = _kst(close)
    sd21 = k.rolling(MDAYS, min_periods=WDAYS).std()
    sd252 = k.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(sd21, sd252)


def f33_cpkt_258_coppock_curvature_negative_persistence_21d(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where d²Coppock-annual < 0 (concave-down persistence)."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return (d2 < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f33_cpkt_259_kst_curvature_negative_persistence_21d(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where d²KST < 0."""
    k = _kst(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    return (d2 < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f33_cpkt_260_coppock_max_minus_min_range_21d(close: pd.Series) -> pd.Series:
    """Coppock-annual 21d-range (max - min) — low range near top = plateau."""
    c = _coppock_annual(close)
    return c.rolling(MDAYS, min_periods=WDAYS).max() - c.rolling(MDAYS, min_periods=WDAYS).min()


def f33_cpkt_261_coppock_plateau_x_breakdown_velocity(close: pd.Series) -> pd.Series:
    """Conditional: if rounded-top score 256 < 0.3 AND current 5d-slope < 0, return |slope|; else 0."""
    shape = f33_cpkt_256_coppock_rounded_top_shape_252d(close)
    slope5 = _rolling_slope(_coppock_annual(close), WDAYS)
    return (slope5.abs().where((shape < 0.3) & (slope5 < 0), 0.0)).where(shape.notna() & slope5.notna(), np.nan)


def f33_cpkt_262_kst_plateau_x_breakdown_velocity(close: pd.Series) -> pd.Series:
    """KST equivalent of 261."""
    shape = f33_cpkt_257_kst_rounded_top_shape_252d(close)
    slope5 = _rolling_slope(_kst(close), WDAYS)
    return (slope5.abs().where((shape < 0.3) & (slope5 < 0), 0.0)).where(shape.notna() & slope5.notna(), np.nan)


def f33_cpkt_263_coppock_concave_down_streak_length(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where d²Coppock-annual < 0."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = (d2 < 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f33_cpkt_264_kst_concave_down_streak_length(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where d²KST < 0."""
    k = _kst(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    flag = (d2 < 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f33_cpkt_265_plateau_x_at_252d_high_indicator_coppock(close: pd.Series) -> pd.Series:
    """+1 when Coppock rounded-top score < 0.3 AND close within 1% of 252d max."""
    shape = f33_cpkt_256_coppock_rounded_top_shape_252d(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((shape < 0.3) & (near == 1)).astype(float).where(shape.notna() & near.notna(), np.nan)


# ============================================================
# Bucket DDD — Confirmation at price extremes (266-275)
# ============================================================

def f33_cpkt_266_coppock_negative_x_close_at_504d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when annual Coppock < 0 AND close within 1.5% of 504d max."""
    c = _coppock_annual(close)
    near = (close >= close.rolling(DDAYS_2Y, min_periods=YDAYS).max() * 0.985).astype(float)
    return ((c < 0) & (near == 1)).astype(float).where(c.notna() & near.notna(), np.nan)


def f33_cpkt_267_kst_below_zero_x_close_at_504d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST < 0 AND close within 1.5% of 504d max."""
    k = _kst(close)
    near = (close >= close.rolling(DDAYS_2Y, min_periods=YDAYS).max() * 0.985).astype(float)
    return ((k < 0) & (near == 1)).astype(float).where(k.notna() & near.notna(), np.nan)


def f33_cpkt_268_long_term_kst_negative_x_close_at_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when long-term KST < 0 AND close within 2% of 1260d max (severe secular failure at all-time high)."""
    lk = _kst_long_term(close)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return ((lk < 0) & (near == 1)).astype(float).where(lk.notna() & near.notna(), np.nan)


def f33_cpkt_269_4cycle_coppock_split_indicator_at_high(close: pd.Series) -> pd.Series:
    """+1 when fraction-of-4-cycle-Coppock-positive is between 0.25 and 0.75 (split regime) AND close near 252d max."""
    frac = f33_cpkt_248_4cycle_coppock_fraction_positive(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((frac >= 0.25) & (frac <= 0.75) & (near == 1)).astype(float).where(frac.notna() & near.notna(), np.nan)


def f33_cpkt_270_kst_below_signal_persistence_x_at_high(close: pd.Series) -> pd.Series:
    """Streak length of KST below signal line, masked to bars where close > 252d-max × 0.95."""
    diff = _kst(close) - _kst_signal(close, 9)
    flag = (diff < 0).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum().astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.95).astype(float)
    return (streak * near).where(diff.notna() & near.notna(), np.nan)


def f33_cpkt_271_coppock_fraction_negative_252d_x_at_high(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars with Coppock-annual < 0, masked to bars where close near 252d max."""
    c = _coppock_annual(close)
    frac_neg = (c < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (frac_neg * near).where(c.notna() & near.notna(), np.nan)


def f33_cpkt_272_kst_long_term_slope_negative_at_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when long-term KST 63d-slope < 0 AND close within 2% of 1260d max (secular momentum failure at peak)."""
    s = _rolling_slope(_kst_long_term(close), QDAYS)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return ((s < 0) & (near == 1)).astype(float).where(s.notna() & near.notna(), np.nan)


def f33_cpkt_273_4cycle_coppock_lower_high_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d local-21d peaks where annual Coppock peak was lower than its preceding 21d peak."""
    c = _coppock_annual(close)
    pk = ((c == c.rolling(MDAYS, min_periods=WDAYS).max()) & (c > c.shift(3))).astype(float)
    pk_val = c.where(pk == 1, np.nan).ffill()
    lower = (pk_val < pk_val.shift(1)).astype(float)
    return lower.rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_274_kst_long_term_dist_from_252d_max(close: pd.Series) -> pd.Series:
    """Long-term KST minus its trailing 252d max — distance below secular peak."""
    lk = _kst_long_term(close)
    return lk - lk.rolling(YDAYS, min_periods=QDAYS).max()


def f33_cpkt_275_4cycle_coppock_disagreement_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where fraction-positive ∈ [0.25, 0.75] (regime tension density)."""
    frac = f33_cpkt_248_4cycle_coppock_fraction_positive(close)
    flag = ((frac >= 0.25) & (frac <= 0.75)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket EEE — Multi-indicator alignment composites (276-285)
# ============================================================

def f33_cpkt_276_coppock_kst_long_kst_all_falling_indicator(close: pd.Series) -> pd.Series:
    """+1 when 21d slopes of Coppock-annual AND KST AND long-term-KST are ALL negative (triple-rollover)."""
    sc = _rolling_slope(_coppock_annual(close), MDAYS)
    sk = _rolling_slope(_kst(close), MDAYS)
    sl = _rolling_slope(_kst_long_term(close), MDAYS)
    return ((sc < 0) & (sk < 0) & (sl < 0)).astype(float).where(sc.notna() & sk.notna() & sl.notna(), np.nan)


def f33_cpkt_277_kst_short_long_term_divergence_252d(close: pd.Series) -> pd.Series:
    """Std-KST minus long-term-KST, z-scored over 252d — short-vs-long disagreement gauge."""
    return _rolling_zscore(_kst(close) - _kst_long_term(close), YDAYS)


def f33_cpkt_278_4cycle_coppock_xor_short_vs_long(close: pd.Series) -> pd.Series:
    """+1 when (quarterly Coppock > 0 XOR biennial Coppock > 0) — short-long regime split."""
    q = (_coppock_quarterly(close) > 0).astype(float).fillna(0)
    b = (_coppock_biennial(close) > 0).astype(float).fillna(0)
    return (q != b).astype(float).where(_coppock_quarterly(close).notna() & _coppock_biennial(close).notna(), np.nan)


def f33_cpkt_279_alignment_score_composite_4cycle(close: pd.Series) -> pd.Series:
    """Alignment composite: 4 - 2 × dispersion-of-4-Coppock-signs."""
    df = pd.concat([
        np.sign(_coppock_quarterly(close)).rename("a"),
        np.sign(_coppock_semi_annual(close)).rename("b"),
        np.sign(_coppock_annual(close)).rename("c"),
        np.sign(_coppock_biennial(close)).rename("d"),
    ], axis=1)
    return 4.0 - 2.0 * df.std(axis=1)


def f33_cpkt_280_alignment_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of alignment composite over 252d."""
    return _rolling_zscore(f33_cpkt_279_alignment_score_composite_4cycle(close), YDAYS)


def f33_cpkt_281_alignment_break_event_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where alignment-score drops by >= 1.0 over 21d (regime-cohesion break)."""
    a = f33_cpkt_279_alignment_score_composite_4cycle(close)
    return ((a - a.shift(MDAYS)) <= -1.0).astype(float).where(a.notna(), np.nan)


def f33_cpkt_282_all_smoothers_positive_indicator(close: pd.Series) -> pd.Series:
    """+1 when 8-indicator breadth == 1.0 (everything bullish — extreme bullish regime)."""
    return (f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close) == 1.0).astype(float)


def f33_cpkt_283_all_smoothers_positive_persistence_63d(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where 8-indicator breadth == 1.0."""
    return (f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close) == 1.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f33_cpkt_284_smoothers_breadth_loss_from_max_21d(close: pd.Series) -> pd.Series:
    """8-indicator breadth minus its trailing 21d max — distance below recent peak breadth."""
    b = f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close)
    return b - b.rolling(MDAYS, min_periods=WDAYS).max()


def f33_cpkt_285_quad_long_indicator_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """0.25 × each of: sign(Coppock-annual), sign(KST), sign(KST-long), sign(close - SMA63).
    Result in [-1, +1]."""
    return 0.25 * (np.sign(_coppock_annual(close)).fillna(0)
                   + np.sign(_kst(close)).fillna(0)
                   + np.sign(_kst_long_term(close)).fillna(0)
                   + np.sign(close - _sma(close, QDAYS)).fillna(0))


# ============================================================
# Bucket FFF — Cycle-length / period analysis (286-295)
# ============================================================

def f33_cpkt_286_coppock_zero_cross_period_mean_504d(close: pd.Series) -> pd.Series:
    """Mean bar-gap between consecutive zero-crossings of annual Coppock in trailing 504d (cycle period estimate)."""
    c = _coppock_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(int)
    idx = pd.Series(np.arange(len(c)), index=c.index)
    last_x = idx.where(flag == 1, np.nan).ffill()
    gap = idx - last_x
    return gap.where(flag == 1, np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f33_cpkt_287_coppock_zero_cross_period_std_504d(close: pd.Series) -> pd.Series:
    """Std of bar-gap between zero-crossings of annual Coppock in 504d (cycle irregularity)."""
    c = _coppock_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(int)
    idx = pd.Series(np.arange(len(c)), index=c.index)
    last_x = idx.where(flag == 1, np.nan).ffill()
    gap = idx - last_x
    return gap.where(flag == 1, np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f33_cpkt_288_kst_zero_cross_period_mean_504d(close: pd.Series) -> pd.Series:
    """Mean bar-gap between zero-crossings of KST in 504d."""
    k = _kst(close)
    flag = ((np.sign(k.shift(1)) != np.sign(k)) & k.notna() & k.shift(1).notna()).astype(int)
    idx = pd.Series(np.arange(len(k)), index=k.index)
    last_x = idx.where(flag == 1, np.nan).ffill()
    gap = idx - last_x
    return gap.where(flag == 1, np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f33_cpkt_289_coppock_current_regime_age_normalized(close: pd.Series) -> pd.Series:
    """Bars-since-last-zero-cross divided by mean-cycle-period (286) — normalized age of current Coppock regime."""
    c = _coppock_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(int)
    age = _bars_since_true(flag.astype(float))
    period = f33_cpkt_286_coppock_zero_cross_period_mean_504d(close)
    return _safe_div(age, period)


def f33_cpkt_290_kst_current_regime_age_normalized(close: pd.Series) -> pd.Series:
    """Same as 289 for KST."""
    k = _kst(close)
    flag = ((np.sign(k.shift(1)) != np.sign(k)) & k.notna() & k.shift(1).notna()).astype(int)
    age = _bars_since_true(flag.astype(float))
    period = f33_cpkt_288_kst_zero_cross_period_mean_504d(close)
    return _safe_div(age, period)


def f33_cpkt_291_coppock_cycle_amplitude_504d(close: pd.Series) -> pd.Series:
    """Trailing 504d range (max - min) of annual Coppock — long-cycle amplitude."""
    c = _coppock_annual(close)
    return c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()


def f33_cpkt_292_kst_cycle_amplitude_504d(close: pd.Series) -> pd.Series:
    """Trailing 504d range of KST."""
    k = _kst(close)
    return k.rolling(DDAYS_2Y, min_periods=YDAYS).max() - k.rolling(DDAYS_2Y, min_periods=YDAYS).min()


def f33_cpkt_293_coppock_amplitude_decay_252d_vs_504d(close: pd.Series) -> pd.Series:
    """Ratio: trailing 252d amplitude / trailing 504d amplitude — decay if < 1 (cycle compressing)."""
    c = _coppock_annual(close)
    a252 = c.rolling(YDAYS, min_periods=QDAYS).max() - c.rolling(YDAYS, min_periods=QDAYS).min()
    a504 = c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(a252, a504)


def f33_cpkt_294_kst_amplitude_decay_252d_vs_504d(close: pd.Series) -> pd.Series:
    """KST amplitude decay ratio (252d/504d)."""
    k = _kst(close)
    a252 = k.rolling(YDAYS, min_periods=QDAYS).max() - k.rolling(YDAYS, min_periods=QDAYS).min()
    a504 = k.rolling(DDAYS_2Y, min_periods=YDAYS).max() - k.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(a252, a504)


def f33_cpkt_295_coppock_value_relative_to_amplitude(close: pd.Series) -> pd.Series:
    """Current Coppock-annual / (504d-amplitude / 2) — normalized position within cycle range."""
    c = _coppock_annual(close)
    amp = (c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()) / 2.0
    return _safe_div(c, amp)


# ============================================================
# Bucket GGG — Master long-cycle topping composites (296-300)
# ============================================================

def f33_cpkt_296_master_long_momentum_topping_index_v1(close: pd.Series) -> pd.Series:
    """Master v1: 0.25*z(Coppock-annual,252) + 0.20*z(KST,252) + 0.15*z(KST-long,252)
    + 0.15*fraction-positive(4cycle) + 0.10*(1 - alignment-score/4) + 0.15*close-pct-rank-1260d."""
    z_cop = _rolling_zscore(_coppock_annual(close), YDAYS)
    z_kst = _rolling_zscore(_kst(close), YDAYS)
    z_lkst = _rolling_zscore(_kst_long_term(close), YDAYS)
    frac = f33_cpkt_248_4cycle_coppock_fraction_positive(close)
    align = f33_cpkt_279_alignment_score_composite_4cycle(close) / 4.0
    px_rank = _pct_rank(close, DDAYS_5Y)
    return (0.25 * z_cop + 0.20 * z_kst + 0.15 * z_lkst
            + 0.15 * frac + 0.10 * (1.0 - align) + 0.15 * px_rank)


def f33_cpkt_297_master_long_momentum_topping_index_v2_rollover_weighted(close: pd.Series) -> pd.Series:
    """Master v2: emphasizes rollover events.
    0.30*(neg-slope-fraction-4cycle) + 0.25*(d²Coppock-bearish-count-252d normalized) + 0.20*(KST-below-signal-streak/63)
    + 0.15*close-pct-rank-1260d + 0.10*(breadth-loss-from-max-21d × -1)."""
    falling = f33_cpkt_249_4cycle_coppock_fraction_falling_21d(close)
    d2_cnt = f33_cpkt_229_coppock_d2_zero_cross_count_252d(close) / 10.0
    diff = _kst(close) - _kst_signal(close, 9)
    flag = (diff < 0).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum().astype(float) / float(QDAYS)
    px_rank = _pct_rank(close, DDAYS_5Y)
    bloss = -f33_cpkt_284_smoothers_breadth_loss_from_max_21d(close)
    return (0.30 * falling + 0.25 * d2_cnt + 0.20 * streak.clip(upper=1.0)
            + 0.15 * px_rank + 0.10 * bloss)


def _coppock_div_breadth_4cycles_local(close: pd.Series) -> pd.Series:
    """Helper (private) — fraction of 4 Coppock variants showing 63d bearish slope-div vs log-close.
    Same definition as f33_cpkt_174 in the 151-225 file but as a private helper for self-containment."""
    def _div(price, osc, n):
        ps = _rolling_slope(_safe_log(price), n); osl = _rolling_slope(osc, n)
        return ((ps > 0) & (osl < 0)).astype(float).where(ps.notna() & osl.notna(), np.nan)
    parts = [
        _div(close, _coppock_quarterly(close), QDAYS).rename("a"),
        _div(close, _coppock_semi_annual(close), QDAYS).rename("b"),
        _div(close, _coppock_annual(close), QDAYS).rename("c"),
        _div(close, _coppock_biennial(close), QDAYS).rename("d"),
    ]
    return pd.concat(parts, axis=1).mean(axis=1)


def f33_cpkt_298_master_long_momentum_topping_index_v3_divergence_weighted(close: pd.Series) -> pd.Series:
    """Master v3: emphasizes long-momentum divergence.
    0.30*(div-breadth-4-Coppock-cycles-63d) + 0.25*(KST-shift-div-count-252d/20)
    + 0.20*z(Coppock-annual,252) + 0.25*close-pct-rank-1260d."""
    div_brd = _coppock_div_breadth_4cycles_local(close)
    kst_div_cnt = (((close > close.shift(MDAYS)) & (_kst(close) < _kst(close).shift(MDAYS))).astype(float)
                   .fillna(0).rolling(YDAYS, min_periods=QDAYS).sum() / 20.0)
    z_cop = _rolling_zscore(_coppock_annual(close), YDAYS)
    px_rank = _pct_rank(close, DDAYS_5Y)
    return 0.30 * div_brd + 0.25 * kst_div_cnt.clip(upper=2.0) + 0.20 * z_cop + 0.25 * px_rank


def f33_cpkt_299_master_long_momentum_topping_average(close: pd.Series) -> pd.Series:
    """Average of v1 + v2 + v3 master topping scores."""
    a = f33_cpkt_296_master_long_momentum_topping_index_v1(close)
    b = f33_cpkt_297_master_long_momentum_topping_index_v2_rollover_weighted(close)
    c = f33_cpkt_298_master_long_momentum_topping_index_v3_divergence_weighted(close)
    return (a + b + c) / 3.0


def f33_cpkt_300_master_long_momentum_topping_x_at_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when master-topping-average z-scored over 252d > 1.0 AND close within 2% of 1260d max."""
    score = f33_cpkt_299_master_long_momentum_topping_average(close)
    z = _rolling_zscore(score, YDAYS)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return ((z > 1.0) & (near == 1)).astype(float).where(z.notna() & near.notna(), np.nan)


# ============================================================
# REGISTRY
# ============================================================



def f33_cpkt_226_coppock_d2_zero_cross_bearish_event_d1(close):
    return f33_cpkt_226_coppock_d2_zero_cross_bearish_event(close).diff()


def f33_cpkt_227_coppock_d2_zero_cross_bullish_event_d1(close):
    return f33_cpkt_227_coppock_d2_zero_cross_bullish_event(close).diff()


def f33_cpkt_228_days_since_coppock_d2_bearish_event_d1(close):
    return f33_cpkt_228_days_since_coppock_d2_bearish_event(close).diff()


def f33_cpkt_229_coppock_d2_zero_cross_count_252d_d1(close):
    return f33_cpkt_229_coppock_d2_zero_cross_count_252d(close).diff()


def f33_cpkt_230_coppock_d2_zero_cross_count_504d_d1(close):
    return f33_cpkt_230_coppock_d2_zero_cross_count_504d(close).diff()


def f33_cpkt_231_coppock_quarterly_d2_zero_cross_bearish_event_d1(close):
    return f33_cpkt_231_coppock_quarterly_d2_zero_cross_bearish_event(close).diff()


def f33_cpkt_232_coppock_d2_at_high_indicator_d1(close):
    return f33_cpkt_232_coppock_d2_at_high_indicator(close).diff()


def f33_cpkt_233_coppock_d2_magnitude_at_event_held_forward_d1(close):
    return f33_cpkt_233_coppock_d2_magnitude_at_event_held_forward(close).diff()


def f33_cpkt_234_coppock_jerk_d3_value_21d_d1(close):
    return f33_cpkt_234_coppock_jerk_d3_value_21d(close).diff()


def f33_cpkt_235_coppock_jerk_above_threshold_pct_rank_252d_d1(close):
    return f33_cpkt_235_coppock_jerk_above_threshold_pct_rank_252d(close).diff()


def f33_cpkt_236_kst_d2_zero_cross_bearish_event_d1(close):
    return f33_cpkt_236_kst_d2_zero_cross_bearish_event(close).diff()


def f33_cpkt_237_kst_d2_zero_cross_bullish_event_d1(close):
    return f33_cpkt_237_kst_d2_zero_cross_bullish_event(close).diff()


def f33_cpkt_238_days_since_kst_d2_bearish_event_d1(close):
    return f33_cpkt_238_days_since_kst_d2_bearish_event(close).diff()


def f33_cpkt_239_kst_d2_zero_cross_count_252d_d1(close):
    return f33_cpkt_239_kst_d2_zero_cross_count_252d(close).diff()


def f33_cpkt_240_kst_long_term_d2_zero_cross_bearish_event_d1(close):
    return f33_cpkt_240_kst_long_term_d2_zero_cross_bearish_event(close).diff()


def f33_cpkt_241_kst_d2_at_high_indicator_d1(close):
    return f33_cpkt_241_kst_d2_at_high_indicator(close).diff()


def f33_cpkt_242_kst_jerk_d3_value_21d_d1(close):
    return f33_cpkt_242_kst_jerk_d3_value_21d(close).diff()


def f33_cpkt_243_kst_jerk_pct_rank_252d_d1(close):
    return f33_cpkt_243_kst_jerk_pct_rank_252d(close).diff()


def f33_cpkt_244_coppock_AND_kst_d2_joint_bearish_event_d1(close):
    return f33_cpkt_244_coppock_AND_kst_d2_joint_bearish_event(close).diff()


def f33_cpkt_245_acceleration_disagreement_indicator_63d_d1(close):
    return f33_cpkt_245_acceleration_disagreement_indicator_63d(close).diff()


def f33_cpkt_246_4cycle_coppock_all_positive_indicator_d1(close):
    return f33_cpkt_246_4cycle_coppock_all_positive_indicator(close).diff()


def f33_cpkt_247_4cycle_coppock_all_negative_indicator_d1(close):
    return f33_cpkt_247_4cycle_coppock_all_negative_indicator(close).diff()


def f33_cpkt_248_4cycle_coppock_fraction_positive_d1(close):
    return f33_cpkt_248_4cycle_coppock_fraction_positive(close).diff()


def f33_cpkt_249_4cycle_coppock_fraction_falling_21d_d1(close):
    return f33_cpkt_249_4cycle_coppock_fraction_falling_21d(close).diff()


def f33_cpkt_250_4cycle_coppock_consensus_bearish_rollover_indicator_d1(close):
    return f33_cpkt_250_4cycle_coppock_consensus_bearish_rollover_indicator(close).diff()


def f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d_d1(close):
    return f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d(close).diff()


def f33_cpkt_252_smoothed_momentum_breadth_change_over_21d_d1(close):
    return f33_cpkt_252_smoothed_momentum_breadth_change_over_21d(close).diff()


def f33_cpkt_253_smoothed_momentum_breadth_below_threshold_at_high_indicator_d1(close):
    return f33_cpkt_253_smoothed_momentum_breadth_below_threshold_at_high_indicator(close).diff()


def f33_cpkt_254_smoothed_momentum_breadth_zscore_252d_d1(close):
    return f33_cpkt_254_smoothed_momentum_breadth_zscore_252d(close).diff()


def f33_cpkt_255_smoothed_momentum_breadth_pct_rank_252d_d1(close):
    return f33_cpkt_255_smoothed_momentum_breadth_pct_rank_252d(close).diff()


def f33_cpkt_256_coppock_rounded_top_shape_252d_d1(close):
    return f33_cpkt_256_coppock_rounded_top_shape_252d(close).diff()


def f33_cpkt_257_kst_rounded_top_shape_252d_d1(close):
    return f33_cpkt_257_kst_rounded_top_shape_252d(close).diff()


def f33_cpkt_258_coppock_curvature_negative_persistence_21d_d1(close):
    return f33_cpkt_258_coppock_curvature_negative_persistence_21d(close).diff()


def f33_cpkt_259_kst_curvature_negative_persistence_21d_d1(close):
    return f33_cpkt_259_kst_curvature_negative_persistence_21d(close).diff()


def f33_cpkt_260_coppock_max_minus_min_range_21d_d1(close):
    return f33_cpkt_260_coppock_max_minus_min_range_21d(close).diff()


def f33_cpkt_261_coppock_plateau_x_breakdown_velocity_d1(close):
    return f33_cpkt_261_coppock_plateau_x_breakdown_velocity(close).diff()


def f33_cpkt_262_kst_plateau_x_breakdown_velocity_d1(close):
    return f33_cpkt_262_kst_plateau_x_breakdown_velocity(close).diff()


def f33_cpkt_263_coppock_concave_down_streak_length_d1(close):
    return f33_cpkt_263_coppock_concave_down_streak_length(close).diff()


def f33_cpkt_264_kst_concave_down_streak_length_d1(close):
    return f33_cpkt_264_kst_concave_down_streak_length(close).diff()


def f33_cpkt_265_plateau_x_at_252d_high_indicator_coppock_d1(close):
    return f33_cpkt_265_plateau_x_at_252d_high_indicator_coppock(close).diff()


def f33_cpkt_266_coppock_negative_x_close_at_504d_high_indicator_d1(close):
    return f33_cpkt_266_coppock_negative_x_close_at_504d_high_indicator(close).diff()


def f33_cpkt_267_kst_below_zero_x_close_at_504d_high_indicator_d1(close):
    return f33_cpkt_267_kst_below_zero_x_close_at_504d_high_indicator(close).diff()


def f33_cpkt_268_long_term_kst_negative_x_close_at_1260d_high_indicator_d1(close):
    return f33_cpkt_268_long_term_kst_negative_x_close_at_1260d_high_indicator(close).diff()


def f33_cpkt_269_4cycle_coppock_split_indicator_at_high_d1(close):
    return f33_cpkt_269_4cycle_coppock_split_indicator_at_high(close).diff()


def f33_cpkt_270_kst_below_signal_persistence_x_at_high_d1(close):
    return f33_cpkt_270_kst_below_signal_persistence_x_at_high(close).diff()


def f33_cpkt_271_coppock_fraction_negative_252d_x_at_high_d1(close):
    return f33_cpkt_271_coppock_fraction_negative_252d_x_at_high(close).diff()


def f33_cpkt_272_kst_long_term_slope_negative_at_high_indicator_d1(close):
    return f33_cpkt_272_kst_long_term_slope_negative_at_high_indicator(close).diff()


def f33_cpkt_273_4cycle_coppock_lower_high_count_252d_d1(close):
    return f33_cpkt_273_4cycle_coppock_lower_high_count_252d(close).diff()


def f33_cpkt_274_kst_long_term_dist_from_252d_max_d1(close):
    return f33_cpkt_274_kst_long_term_dist_from_252d_max(close).diff()


def f33_cpkt_275_4cycle_coppock_disagreement_count_252d_d1(close):
    return f33_cpkt_275_4cycle_coppock_disagreement_count_252d(close).diff()


def f33_cpkt_276_coppock_kst_long_kst_all_falling_indicator_d1(close):
    return f33_cpkt_276_coppock_kst_long_kst_all_falling_indicator(close).diff()


def f33_cpkt_277_kst_short_long_term_divergence_252d_d1(close):
    return f33_cpkt_277_kst_short_long_term_divergence_252d(close).diff()


def f33_cpkt_278_4cycle_coppock_xor_short_vs_long_d1(close):
    return f33_cpkt_278_4cycle_coppock_xor_short_vs_long(close).diff()


def f33_cpkt_279_alignment_score_composite_4cycle_d1(close):
    return f33_cpkt_279_alignment_score_composite_4cycle(close).diff()


def f33_cpkt_280_alignment_zscore_252d_d1(close):
    return f33_cpkt_280_alignment_zscore_252d(close).diff()


def f33_cpkt_281_alignment_break_event_indicator_d1(close):
    return f33_cpkt_281_alignment_break_event_indicator(close).diff()


def f33_cpkt_282_all_smoothers_positive_indicator_d1(close):
    return f33_cpkt_282_all_smoothers_positive_indicator(close).diff()


def f33_cpkt_283_all_smoothers_positive_persistence_63d_d1(close):
    return f33_cpkt_283_all_smoothers_positive_persistence_63d(close).diff()


def f33_cpkt_284_smoothers_breadth_loss_from_max_21d_d1(close):
    return f33_cpkt_284_smoothers_breadth_loss_from_max_21d(close).diff()


def f33_cpkt_285_quad_long_indicator_score_d1(close, volume):
    return f33_cpkt_285_quad_long_indicator_score(close, volume).diff()


def f33_cpkt_286_coppock_zero_cross_period_mean_504d_d1(close):
    return f33_cpkt_286_coppock_zero_cross_period_mean_504d(close).diff()


def f33_cpkt_287_coppock_zero_cross_period_std_504d_d1(close):
    return f33_cpkt_287_coppock_zero_cross_period_std_504d(close).diff()


def f33_cpkt_288_kst_zero_cross_period_mean_504d_d1(close):
    return f33_cpkt_288_kst_zero_cross_period_mean_504d(close).diff()


def f33_cpkt_289_coppock_current_regime_age_normalized_d1(close):
    return f33_cpkt_289_coppock_current_regime_age_normalized(close).diff()


def f33_cpkt_290_kst_current_regime_age_normalized_d1(close):
    return f33_cpkt_290_kst_current_regime_age_normalized(close).diff()


def f33_cpkt_291_coppock_cycle_amplitude_504d_d1(close):
    return f33_cpkt_291_coppock_cycle_amplitude_504d(close).diff()


def f33_cpkt_292_kst_cycle_amplitude_504d_d1(close):
    return f33_cpkt_292_kst_cycle_amplitude_504d(close).diff()


def f33_cpkt_293_coppock_amplitude_decay_252d_vs_504d_d1(close):
    return f33_cpkt_293_coppock_amplitude_decay_252d_vs_504d(close).diff()


def f33_cpkt_294_kst_amplitude_decay_252d_vs_504d_d1(close):
    return f33_cpkt_294_kst_amplitude_decay_252d_vs_504d(close).diff()


def f33_cpkt_295_coppock_value_relative_to_amplitude_d1(close):
    return f33_cpkt_295_coppock_value_relative_to_amplitude(close).diff()


def f33_cpkt_296_master_long_momentum_topping_index_v1_d1(close):
    return f33_cpkt_296_master_long_momentum_topping_index_v1(close).diff()


def f33_cpkt_297_master_long_momentum_topping_index_v2_rollover_weighted_d1(close):
    return f33_cpkt_297_master_long_momentum_topping_index_v2_rollover_weighted(close).diff()


def f33_cpkt_298_master_long_momentum_topping_index_v3_divergence_weighted_d1(close):
    return f33_cpkt_298_master_long_momentum_topping_index_v3_divergence_weighted(close).diff()


def f33_cpkt_299_master_long_momentum_topping_average_d1(close):
    return f33_cpkt_299_master_long_momentum_topping_average(close).diff()


def f33_cpkt_300_master_long_momentum_topping_x_at_1260d_high_indicator_d1(close):
    return f33_cpkt_300_master_long_momentum_topping_x_at_1260d_high_indicator(close).diff()


COPPOCK_CURVE_KST_D1_REGISTRY_226_300 = {
    "f33_cpkt_226_coppock_d2_zero_cross_bearish_event_d1": {"inputs": ["close"], "func": f33_cpkt_226_coppock_d2_zero_cross_bearish_event_d1},
    "f33_cpkt_227_coppock_d2_zero_cross_bullish_event_d1": {"inputs": ["close"], "func": f33_cpkt_227_coppock_d2_zero_cross_bullish_event_d1},
    "f33_cpkt_228_days_since_coppock_d2_bearish_event_d1": {"inputs": ["close"], "func": f33_cpkt_228_days_since_coppock_d2_bearish_event_d1},
    "f33_cpkt_229_coppock_d2_zero_cross_count_252d_d1": {"inputs": ["close"], "func": f33_cpkt_229_coppock_d2_zero_cross_count_252d_d1},
    "f33_cpkt_230_coppock_d2_zero_cross_count_504d_d1": {"inputs": ["close"], "func": f33_cpkt_230_coppock_d2_zero_cross_count_504d_d1},
    "f33_cpkt_231_coppock_quarterly_d2_zero_cross_bearish_event_d1": {"inputs": ["close"], "func": f33_cpkt_231_coppock_quarterly_d2_zero_cross_bearish_event_d1},
    "f33_cpkt_232_coppock_d2_at_high_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_232_coppock_d2_at_high_indicator_d1},
    "f33_cpkt_233_coppock_d2_magnitude_at_event_held_forward_d1": {"inputs": ["close"], "func": f33_cpkt_233_coppock_d2_magnitude_at_event_held_forward_d1},
    "f33_cpkt_234_coppock_jerk_d3_value_21d_d1": {"inputs": ["close"], "func": f33_cpkt_234_coppock_jerk_d3_value_21d_d1},
    "f33_cpkt_235_coppock_jerk_above_threshold_pct_rank_252d_d1": {"inputs": ["close"], "func": f33_cpkt_235_coppock_jerk_above_threshold_pct_rank_252d_d1},
    "f33_cpkt_236_kst_d2_zero_cross_bearish_event_d1": {"inputs": ["close"], "func": f33_cpkt_236_kst_d2_zero_cross_bearish_event_d1},
    "f33_cpkt_237_kst_d2_zero_cross_bullish_event_d1": {"inputs": ["close"], "func": f33_cpkt_237_kst_d2_zero_cross_bullish_event_d1},
    "f33_cpkt_238_days_since_kst_d2_bearish_event_d1": {"inputs": ["close"], "func": f33_cpkt_238_days_since_kst_d2_bearish_event_d1},
    "f33_cpkt_239_kst_d2_zero_cross_count_252d_d1": {"inputs": ["close"], "func": f33_cpkt_239_kst_d2_zero_cross_count_252d_d1},
    "f33_cpkt_240_kst_long_term_d2_zero_cross_bearish_event_d1": {"inputs": ["close"], "func": f33_cpkt_240_kst_long_term_d2_zero_cross_bearish_event_d1},
    "f33_cpkt_241_kst_d2_at_high_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_241_kst_d2_at_high_indicator_d1},
    "f33_cpkt_242_kst_jerk_d3_value_21d_d1": {"inputs": ["close"], "func": f33_cpkt_242_kst_jerk_d3_value_21d_d1},
    "f33_cpkt_243_kst_jerk_pct_rank_252d_d1": {"inputs": ["close"], "func": f33_cpkt_243_kst_jerk_pct_rank_252d_d1},
    "f33_cpkt_244_coppock_AND_kst_d2_joint_bearish_event_d1": {"inputs": ["close"], "func": f33_cpkt_244_coppock_AND_kst_d2_joint_bearish_event_d1},
    "f33_cpkt_245_acceleration_disagreement_indicator_63d_d1": {"inputs": ["close"], "func": f33_cpkt_245_acceleration_disagreement_indicator_63d_d1},
    "f33_cpkt_246_4cycle_coppock_all_positive_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_246_4cycle_coppock_all_positive_indicator_d1},
    "f33_cpkt_247_4cycle_coppock_all_negative_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_247_4cycle_coppock_all_negative_indicator_d1},
    "f33_cpkt_248_4cycle_coppock_fraction_positive_d1": {"inputs": ["close"], "func": f33_cpkt_248_4cycle_coppock_fraction_positive_d1},
    "f33_cpkt_249_4cycle_coppock_fraction_falling_21d_d1": {"inputs": ["close"], "func": f33_cpkt_249_4cycle_coppock_fraction_falling_21d_d1},
    "f33_cpkt_250_4cycle_coppock_consensus_bearish_rollover_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_250_4cycle_coppock_consensus_bearish_rollover_indicator_d1},
    "f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d_d1": {"inputs": ["close"], "func": f33_cpkt_251_smoothed_momentum_breadth_8indicators_63d_d1},
    "f33_cpkt_252_smoothed_momentum_breadth_change_over_21d_d1": {"inputs": ["close"], "func": f33_cpkt_252_smoothed_momentum_breadth_change_over_21d_d1},
    "f33_cpkt_253_smoothed_momentum_breadth_below_threshold_at_high_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_253_smoothed_momentum_breadth_below_threshold_at_high_indicator_d1},
    "f33_cpkt_254_smoothed_momentum_breadth_zscore_252d_d1": {"inputs": ["close"], "func": f33_cpkt_254_smoothed_momentum_breadth_zscore_252d_d1},
    "f33_cpkt_255_smoothed_momentum_breadth_pct_rank_252d_d1": {"inputs": ["close"], "func": f33_cpkt_255_smoothed_momentum_breadth_pct_rank_252d_d1},
    "f33_cpkt_256_coppock_rounded_top_shape_252d_d1": {"inputs": ["close"], "func": f33_cpkt_256_coppock_rounded_top_shape_252d_d1},
    "f33_cpkt_257_kst_rounded_top_shape_252d_d1": {"inputs": ["close"], "func": f33_cpkt_257_kst_rounded_top_shape_252d_d1},
    "f33_cpkt_258_coppock_curvature_negative_persistence_21d_d1": {"inputs": ["close"], "func": f33_cpkt_258_coppock_curvature_negative_persistence_21d_d1},
    "f33_cpkt_259_kst_curvature_negative_persistence_21d_d1": {"inputs": ["close"], "func": f33_cpkt_259_kst_curvature_negative_persistence_21d_d1},
    "f33_cpkt_260_coppock_max_minus_min_range_21d_d1": {"inputs": ["close"], "func": f33_cpkt_260_coppock_max_minus_min_range_21d_d1},
    "f33_cpkt_261_coppock_plateau_x_breakdown_velocity_d1": {"inputs": ["close"], "func": f33_cpkt_261_coppock_plateau_x_breakdown_velocity_d1},
    "f33_cpkt_262_kst_plateau_x_breakdown_velocity_d1": {"inputs": ["close"], "func": f33_cpkt_262_kst_plateau_x_breakdown_velocity_d1},
    "f33_cpkt_263_coppock_concave_down_streak_length_d1": {"inputs": ["close"], "func": f33_cpkt_263_coppock_concave_down_streak_length_d1},
    "f33_cpkt_264_kst_concave_down_streak_length_d1": {"inputs": ["close"], "func": f33_cpkt_264_kst_concave_down_streak_length_d1},
    "f33_cpkt_265_plateau_x_at_252d_high_indicator_coppock_d1": {"inputs": ["close"], "func": f33_cpkt_265_plateau_x_at_252d_high_indicator_coppock_d1},
    "f33_cpkt_266_coppock_negative_x_close_at_504d_high_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_266_coppock_negative_x_close_at_504d_high_indicator_d1},
    "f33_cpkt_267_kst_below_zero_x_close_at_504d_high_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_267_kst_below_zero_x_close_at_504d_high_indicator_d1},
    "f33_cpkt_268_long_term_kst_negative_x_close_at_1260d_high_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_268_long_term_kst_negative_x_close_at_1260d_high_indicator_d1},
    "f33_cpkt_269_4cycle_coppock_split_indicator_at_high_d1": {"inputs": ["close"], "func": f33_cpkt_269_4cycle_coppock_split_indicator_at_high_d1},
    "f33_cpkt_270_kst_below_signal_persistence_x_at_high_d1": {"inputs": ["close"], "func": f33_cpkt_270_kst_below_signal_persistence_x_at_high_d1},
    "f33_cpkt_271_coppock_fraction_negative_252d_x_at_high_d1": {"inputs": ["close"], "func": f33_cpkt_271_coppock_fraction_negative_252d_x_at_high_d1},
    "f33_cpkt_272_kst_long_term_slope_negative_at_high_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_272_kst_long_term_slope_negative_at_high_indicator_d1},
    "f33_cpkt_273_4cycle_coppock_lower_high_count_252d_d1": {"inputs": ["close"], "func": f33_cpkt_273_4cycle_coppock_lower_high_count_252d_d1},
    "f33_cpkt_274_kst_long_term_dist_from_252d_max_d1": {"inputs": ["close"], "func": f33_cpkt_274_kst_long_term_dist_from_252d_max_d1},
    "f33_cpkt_275_4cycle_coppock_disagreement_count_252d_d1": {"inputs": ["close"], "func": f33_cpkt_275_4cycle_coppock_disagreement_count_252d_d1},
    "f33_cpkt_276_coppock_kst_long_kst_all_falling_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_276_coppock_kst_long_kst_all_falling_indicator_d1},
    "f33_cpkt_277_kst_short_long_term_divergence_252d_d1": {"inputs": ["close"], "func": f33_cpkt_277_kst_short_long_term_divergence_252d_d1},
    "f33_cpkt_278_4cycle_coppock_xor_short_vs_long_d1": {"inputs": ["close"], "func": f33_cpkt_278_4cycle_coppock_xor_short_vs_long_d1},
    "f33_cpkt_279_alignment_score_composite_4cycle_d1": {"inputs": ["close"], "func": f33_cpkt_279_alignment_score_composite_4cycle_d1},
    "f33_cpkt_280_alignment_zscore_252d_d1": {"inputs": ["close"], "func": f33_cpkt_280_alignment_zscore_252d_d1},
    "f33_cpkt_281_alignment_break_event_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_281_alignment_break_event_indicator_d1},
    "f33_cpkt_282_all_smoothers_positive_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_282_all_smoothers_positive_indicator_d1},
    "f33_cpkt_283_all_smoothers_positive_persistence_63d_d1": {"inputs": ["close"], "func": f33_cpkt_283_all_smoothers_positive_persistence_63d_d1},
    "f33_cpkt_284_smoothers_breadth_loss_from_max_21d_d1": {"inputs": ["close"], "func": f33_cpkt_284_smoothers_breadth_loss_from_max_21d_d1},
    "f33_cpkt_285_quad_long_indicator_score_d1": {"inputs": ["close", "volume"], "func": f33_cpkt_285_quad_long_indicator_score_d1},
    "f33_cpkt_286_coppock_zero_cross_period_mean_504d_d1": {"inputs": ["close"], "func": f33_cpkt_286_coppock_zero_cross_period_mean_504d_d1},
    "f33_cpkt_287_coppock_zero_cross_period_std_504d_d1": {"inputs": ["close"], "func": f33_cpkt_287_coppock_zero_cross_period_std_504d_d1},
    "f33_cpkt_288_kst_zero_cross_period_mean_504d_d1": {"inputs": ["close"], "func": f33_cpkt_288_kst_zero_cross_period_mean_504d_d1},
    "f33_cpkt_289_coppock_current_regime_age_normalized_d1": {"inputs": ["close"], "func": f33_cpkt_289_coppock_current_regime_age_normalized_d1},
    "f33_cpkt_290_kst_current_regime_age_normalized_d1": {"inputs": ["close"], "func": f33_cpkt_290_kst_current_regime_age_normalized_d1},
    "f33_cpkt_291_coppock_cycle_amplitude_504d_d1": {"inputs": ["close"], "func": f33_cpkt_291_coppock_cycle_amplitude_504d_d1},
    "f33_cpkt_292_kst_cycle_amplitude_504d_d1": {"inputs": ["close"], "func": f33_cpkt_292_kst_cycle_amplitude_504d_d1},
    "f33_cpkt_293_coppock_amplitude_decay_252d_vs_504d_d1": {"inputs": ["close"], "func": f33_cpkt_293_coppock_amplitude_decay_252d_vs_504d_d1},
    "f33_cpkt_294_kst_amplitude_decay_252d_vs_504d_d1": {"inputs": ["close"], "func": f33_cpkt_294_kst_amplitude_decay_252d_vs_504d_d1},
    "f33_cpkt_295_coppock_value_relative_to_amplitude_d1": {"inputs": ["close"], "func": f33_cpkt_295_coppock_value_relative_to_amplitude_d1},
    "f33_cpkt_296_master_long_momentum_topping_index_v1_d1": {"inputs": ["close"], "func": f33_cpkt_296_master_long_momentum_topping_index_v1_d1},
    "f33_cpkt_297_master_long_momentum_topping_index_v2_rollover_weighted_d1": {"inputs": ["close"], "func": f33_cpkt_297_master_long_momentum_topping_index_v2_rollover_weighted_d1},
    "f33_cpkt_298_master_long_momentum_topping_index_v3_divergence_weighted_d1": {"inputs": ["close"], "func": f33_cpkt_298_master_long_momentum_topping_index_v3_divergence_weighted_d1},
    "f33_cpkt_299_master_long_momentum_topping_average_d1": {"inputs": ["close"], "func": f33_cpkt_299_master_long_momentum_topping_average_d1},
    "f33_cpkt_300_master_long_momentum_topping_x_at_1260d_high_indicator_d1": {"inputs": ["close"], "func": f33_cpkt_300_master_long_momentum_topping_x_at_1260d_high_indicator_d1},
}
