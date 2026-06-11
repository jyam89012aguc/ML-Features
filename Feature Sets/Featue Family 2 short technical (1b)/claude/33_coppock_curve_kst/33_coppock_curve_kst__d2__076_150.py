"""coppock_curve_kst d2 features 076-150 — Pipeline 1b-technical.

This file extends __base__001_075.py with multi-horizon KST stacking, Coppock+KST
composites, plateau/topping-shape detection, distance-from-prior-peak metrics,
sign-stability/regime indicators, d² acceleration, smoothed-momentum exhaustion at
price highs, and Pring-variant composites.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


# ---------------------------- Coppock / KST helpers ----------------------------

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


def _coppock_exponential(close):
    """Exponential-weighted Coppock variant: EMA replaces WMA — distinct smoother."""
    return _ema(_roc_pct(close, 294) + _roc_pct(close, 231), 105)


def _kst(close):
    return (1.0 * _sma(_roc_pct(close, 10), 10)
            + 2.0 * _sma(_roc_pct(close, 15), 10)
            + 3.0 * _sma(_roc_pct(close, 20), 10)
            + 4.0 * _sma(_roc_pct(close, 30), 15))


def _kst_short_term(close):
    return (1.0 * _sma(_roc_pct(close, 5), 5)
            + 2.0 * _sma(_roc_pct(close, 8), 5)
            + 3.0 * _sma(_roc_pct(close, 12), 5)
            + 4.0 * _sma(_roc_pct(close, 18), 8))


def _kst_intermediate(close):
    """Intermediate KST (between short and long): horizons 20/30/40/65, SMA 10/10/10/15."""
    return (1.0 * _sma(_roc_pct(close, 20), 10)
            + 2.0 * _sma(_roc_pct(close, 30), 10)
            + 3.0 * _sma(_roc_pct(close, 40), 10)
            + 4.0 * _sma(_roc_pct(close, 65), 15))


def _kst_long_term(close):
    return (1.0 * _sma(_roc_pct(close, 65), 21)
            + 2.0 * _sma(_roc_pct(close, 130), 21)
            + 3.0 * _sma(_roc_pct(close, 195), 21)
            + 4.0 * _sma(_roc_pct(close, 260), 42))


def _kst_signal(close, n_sig=9):
    return _sma(_kst(close), n_sig)


# ============================================================
# Bucket I — Multi-horizon KST stacking (076-085)
# ============================================================

def f33_cpkt_076_kst_short_inter_long_all_up_indicator(close: pd.Series) -> pd.Series:
    """+1 when short/intermediate/long-term KST are ALL > 0 (consensus bullish regime)."""
    s = (_kst_short_term(close) > 0).astype(float)
    i = (_kst_intermediate(close) > 0).astype(float)
    l = (_kst_long_term(close) > 0).astype(float)
    return (s * i * l).where(s.notna() & i.notna() & l.notna(), np.nan)


def f33_cpkt_077_kst_short_inter_long_all_down_indicator(close: pd.Series) -> pd.Series:
    """+1 when short/intermediate/long-term KST are ALL < 0."""
    s = (_kst_short_term(close) < 0).astype(float)
    i = (_kst_intermediate(close) < 0).astype(float)
    l = (_kst_long_term(close) < 0).astype(float)
    return (s * i * l).where(s.notna() & i.notna() & l.notna(), np.nan)


def f33_cpkt_078_kst_count_up_3horizons(close: pd.Series) -> pd.Series:
    """Count (0..3) of short/intermediate/long KST > 0."""
    s = (_kst_short_term(close) > 0).astype(float)
    i = (_kst_intermediate(close) > 0).astype(float)
    l = (_kst_long_term(close) > 0).astype(float)
    return s.fillna(0) + i.fillna(0) + l.fillna(0)


def f33_cpkt_079_kst_short_inter_long_fraction_up(close: pd.Series) -> pd.Series:
    """Fraction (0..1) of short/intermediate/long KST > 0."""
    s = (_kst_short_term(close) > 0).astype(float)
    i = (_kst_intermediate(close) > 0).astype(float)
    l = (_kst_long_term(close) > 0).astype(float)
    return (s.fillna(0) + i.fillna(0) + l.fillna(0)) / 3.0


def f33_cpkt_080_kst_short_minus_long_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (short-term KST - long-term KST) over 252d — horizon-disagreement gauge."""
    return _rolling_zscore(_kst_short_term(close) - _kst_long_term(close), YDAYS)


def f33_cpkt_081_kst_short_above_long_indicator(close: pd.Series) -> pd.Series:
    """+1 when short-term KST > long-term KST (acute > secular)."""
    s = _kst_short_term(close); l = _kst_long_term(close)
    return (s > l).astype(float).where(s.notna() & l.notna(), np.nan)


def f33_cpkt_082_kst_consensus_bull_to_bear_flip_indicator(close: pd.Series) -> pd.Series:
    """+1 on the bar where 'all 3 up' just transitioned to 'not all 3 up'."""
    s = (_kst_short_term(close) > 0).astype(float)
    i = (_kst_intermediate(close) > 0).astype(float)
    l = (_kst_long_term(close) > 0).astype(float)
    cons = (s * i * l)
    return ((cons.shift(1) == 1) & (cons != 1)).astype(float).where(cons.notna() & cons.shift(1).notna(), np.nan)


def f33_cpkt_083_kst_short_falling_long_rising_indicator(close: pd.Series) -> pd.Series:
    """+1 when short-KST slope < 0 AND long-KST slope > 0 — acute weakness within secular trend (topping)."""
    ss = _rolling_slope(_kst_short_term(close), MDAYS)
    sl = _rolling_slope(_kst_long_term(close), QDAYS)
    return ((ss < 0) & (sl > 0)).astype(float).where(ss.notna() & sl.notna(), np.nan)


def f33_cpkt_084_kst_horizons_disagreement_score(close: pd.Series) -> pd.Series:
    """Std across the 3 KST horizon values at each bar (normalized by mean-abs) — disagreement gauge."""
    s = _kst_short_term(close); i = _kst_intermediate(close); l = _kst_long_term(close)
    df = pd.concat([s.rename("s"), i.rename("i"), l.rename("l")], axis=1)
    return _safe_div(df.std(axis=1), df.abs().mean(axis=1))


def f33_cpkt_085_kst_horizon_zscore_dispersion_252d(close: pd.Series) -> pd.Series:
    """Std across z-scored (over 252d) KST horizon values — dispersion of normalized regime states."""
    zs = _rolling_zscore(_kst_short_term(close), YDAYS)
    zi = _rolling_zscore(_kst_intermediate(close), YDAYS)
    zl = _rolling_zscore(_kst_long_term(close), YDAYS)
    return pd.concat([zs.rename("zs"), zi.rename("zi"), zl.rename("zl")], axis=1).std(axis=1)


# ============================================================
# Bucket J — Coppock + KST composites (086-095)
# ============================================================

def f33_cpkt_086_coppock_kst_both_falling_indicator(close: pd.Series) -> pd.Series:
    """+1 when 63d-slope of annual Coppock AND 63d-slope of KST are BOTH negative."""
    sc = _rolling_slope(_coppock_annual(close), QDAYS)
    sk = _rolling_slope(_kst(close), QDAYS)
    return ((sc < 0) & (sk < 0)).astype(float).where(sc.notna() & sk.notna(), np.nan)


def f33_cpkt_087_coppock_kst_both_peaking_indicator(close: pd.Series) -> pd.Series:
    """+1 when both Coppock-annual AND KST flagged as local 21d-peaks in last 5 bars."""
    c = _coppock_annual(close); k = _kst(close)
    pc = ((c == c.rolling(MDAYS, min_periods=WDAYS).max()) & (c > c.shift(3))).astype(float)
    pk = ((k == k.rolling(MDAYS, min_periods=WDAYS).max()) & (k > k.shift(3))).astype(float)
    pc_recent = pc.rolling(WDAYS, min_periods=1).max()
    pk_recent = pk.rolling(WDAYS, min_periods=1).max()
    return (pc_recent * pk_recent).where(c.notna() & k.notna(), np.nan)


def f33_cpkt_088_coppock_kst_topping_score_composite(close: pd.Series) -> pd.Series:
    """Weighted topping score: 0.5*z(Coppock annual,252) + 0.5*z(KST,252), gated by 'both falling'."""
    zc = _rolling_zscore(_coppock_annual(close), YDAYS)
    zk = _rolling_zscore(_kst(close), YDAYS)
    sc = _rolling_slope(_coppock_annual(close), QDAYS)
    sk = _rolling_slope(_kst(close), QDAYS)
    falling = ((sc < 0) & (sk < 0)).astype(float)
    return (0.5 * zc + 0.5 * zk) * falling


def f33_cpkt_089_coppock_kst_zsum_252d(close: pd.Series) -> pd.Series:
    """Sum of z-scored Coppock-annual and KST over 252d — composite long-momentum z."""
    return _rolling_zscore(_coppock_annual(close), YDAYS) + _rolling_zscore(_kst(close), YDAYS)


def f33_cpkt_090_coppock_kst_correlation_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d Pearson corr between annual Coppock and KST — co-movement check."""
    c = _coppock_annual(close); k = _kst(close)
    return c.rolling(YDAYS, min_periods=QDAYS).corr(k)


def f33_cpkt_091_coppock_kst_disagreement_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where Coppock-annual sign != KST sign."""
    c = _coppock_annual(close); k = _kst(close)
    flag = ((np.sign(c) != np.sign(k)) & c.notna() & k.notna()).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean()


def f33_cpkt_092_days_since_coppock_AND_kst_joint_bearish_cross(close: pd.Series) -> pd.Series:
    """Bars since the last bar where BOTH Coppock and KST were on bearish slope-sign flip within 21d."""
    sc = _rolling_slope(_coppock_annual(close), QDAYS)
    sk = _rolling_slope(_kst(close), QDAYS)
    cflip = ((sc.shift(1) > 0) & (sc <= 0)).astype(float)
    kflip = ((sk.shift(1) > 0) & (sk <= 0)).astype(float)
    cflip_recent = cflip.rolling(MDAYS, min_periods=1).max()
    kflip_recent = kflip.rolling(MDAYS, min_periods=1).max()
    joint = (cflip_recent * kflip_recent)
    return _bars_since_true(joint)


def f33_cpkt_093_coppock_kst_joint_bearish_div_63d_close(close: pd.Series) -> pd.Series:
    """+1 if Coppock-annual AND KST both show 63d bearish slope-divergence vs log-close."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    sc = _rolling_slope(_coppock_annual(close), QDAYS)
    sk = _rolling_slope(_kst(close), QDAYS)
    c_div = ((ps > 0) & (sc < 0)).astype(float)
    k_div = ((ps > 0) & (sk < 0)).astype(float)
    return (c_div * k_div).where(ps.notna() & sc.notna() & sk.notna(), np.nan)


def f33_cpkt_094_long_smoothed_momentum_breadth_4indicators(close: pd.Series) -> pd.Series:
    """Fraction (0..1) of 4 long-smoothed momentum indicators that are 'bearish' (current value < trailing-252d-median):
    annual-Coppock, quarterly-Coppock, KST, long-term-KST."""
    indicators = [_coppock_annual(close), _coppock_quarterly(close), _kst(close), _kst_long_term(close)]
    flags = []
    for i, ind in enumerate(indicators):
        med = ind.rolling(YDAYS, min_periods=QDAYS).median()
        flags.append((ind < med).astype(float).rename(f"f{i}"))
    return pd.concat(flags, axis=1).mean(axis=1)


def f33_cpkt_095_long_smoothed_momentum_combined_zscore_252d(close: pd.Series) -> pd.Series:
    """Mean of z-scored Coppock-annual + KST + KST-long over 252d — composite long-momentum z."""
    return (_rolling_zscore(_coppock_annual(close), YDAYS)
            + _rolling_zscore(_kst(close), YDAYS)
            + _rolling_zscore(_kst_long_term(close), YDAYS)) / 3.0


# ============================================================
# Bucket K — Plateau / topping shape (096-105)
# ============================================================

def f33_cpkt_096_coppock_plateau_dwell_at_252d_max_21d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d where annual Coppock was within 1% (in atr-norm units) of its 252d max."""
    c = _coppock_annual(close)
    mx = c.rolling(YDAYS, min_periods=QDAYS).max()
    near = ((mx - c).abs() <= 0.01 * mx.abs()).astype(float)
    return near.rolling(MDAYS, min_periods=WDAYS).sum()


def f33_cpkt_097_coppock_plateau_width_at_max_63d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 63d within 5% of the 63d-max of Coppock (plateau width)."""
    c = _coppock_annual(close)
    mx = c.rolling(QDAYS, min_periods=MDAYS).max()
    near = ((mx - c).abs() <= 0.05 * mx.abs()).astype(float)
    return near.rolling(QDAYS, min_periods=MDAYS).sum()


def f33_cpkt_098_coppock_curvature_21d(close: pd.Series) -> pd.Series:
    """Magnitude of 2nd derivative of annual Coppock (slope of 5d-slope of 21d-slope) — curvature gauge."""
    c = _coppock_annual(close)
    slope = _rolling_slope(c, MDAYS)
    return _rolling_slope(slope, WDAYS).abs()


def f33_cpkt_099_coppock_post_plateau_breakdown_velocity(close: pd.Series) -> pd.Series:
    """If plateau detected in last 21d AND current slope negative: |slope|; else 0 — post-plateau velocity."""
    c = _coppock_annual(close)
    mx = c.rolling(YDAYS, min_periods=QDAYS).max()
    near = ((mx - c).abs() <= 0.01 * mx.abs()).astype(float)
    plateau_recent = near.rolling(MDAYS, min_periods=WDAYS).sum() >= 5
    slope = _rolling_slope(c, MDAYS)
    return (slope.abs().where(plateau_recent & (slope < 0), 0.0)).where(c.notna(), np.nan)


def f33_cpkt_100_kst_plateau_dwell_at_252d_max_21d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d where KST was within 1% of its 252d max."""
    k = _kst(close)
    mx = k.rolling(YDAYS, min_periods=QDAYS).max()
    near = ((mx - k).abs() <= 0.01 * mx.abs()).astype(float)
    return near.rolling(MDAYS, min_periods=WDAYS).sum()


def f33_cpkt_101_kst_plateau_width_at_max_63d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 63d within 5% of KST 63d-max — KST plateau width."""
    k = _kst(close)
    mx = k.rolling(QDAYS, min_periods=MDAYS).max()
    near = ((mx - k).abs() <= 0.05 * mx.abs()).astype(float)
    return near.rolling(QDAYS, min_periods=MDAYS).sum()


def f33_cpkt_102_kst_curvature_21d(close: pd.Series) -> pd.Series:
    """Magnitude of KST 2nd derivative (slope-of-slope) — curvature gauge."""
    k = _kst(close)
    slope = _rolling_slope(k, MDAYS)
    return _rolling_slope(slope, WDAYS).abs()


def f33_cpkt_103_kst_post_plateau_breakdown_velocity(close: pd.Series) -> pd.Series:
    """If KST plateau detected last 21d AND current slope negative: |slope|; else 0."""
    k = _kst(close)
    mx = k.rolling(YDAYS, min_periods=QDAYS).max()
    near = ((mx - k).abs() <= 0.01 * mx.abs()).astype(float)
    plateau_recent = near.rolling(MDAYS, min_periods=WDAYS).sum() >= 5
    slope = _rolling_slope(k, MDAYS)
    return (slope.abs().where(plateau_recent & (slope < 0), 0.0)).where(k.notna(), np.nan)


def f33_cpkt_104_coppock_kst_joint_plateau_indicator(close: pd.Series) -> pd.Series:
    """+1 when BOTH Coppock-annual and KST show plateau (>= 10 of last 21 bars within 1% of 252d max)."""
    c = _coppock_annual(close); k = _kst(close)
    nc = ((c.rolling(YDAYS, min_periods=QDAYS).max() - c).abs() <= 0.01 * c.rolling(YDAYS, min_periods=QDAYS).max().abs()).astype(float)
    nk = ((k.rolling(YDAYS, min_periods=QDAYS).max() - k).abs() <= 0.01 * k.rolling(YDAYS, min_periods=QDAYS).max().abs()).astype(float)
    pc = (nc.rolling(MDAYS, min_periods=WDAYS).sum() >= 10).astype(float)
    pk = (nk.rolling(MDAYS, min_periods=WDAYS).sum() >= 10).astype(float)
    return (pc * pk).where(c.notna() & k.notna(), np.nan)


def f33_cpkt_105_smoothed_momentum_topping_shape_composite(close: pd.Series) -> pd.Series:
    """Composite topping shape: |Coppock curvature 21d| + |KST curvature 21d|, normalized by stdev each."""
    cc = f33_cpkt_098_coppock_curvature_21d(close)
    kc = f33_cpkt_102_kst_curvature_21d(close)
    return (_rolling_zscore(cc, YDAYS) + _rolling_zscore(kc, YDAYS)) / 2.0


# ============================================================
# Bucket L — Distance from prior-cycle peak (106-115)
# ============================================================

def f33_cpkt_106_coppock_dist_from_prior_cycle_peak_pct(close: pd.Series) -> pd.Series:
    """Distance (% of |peak|) of current Coppock-annual from its prior-cycle peak (504d max ending 63d ago)."""
    c = _coppock_annual(close)
    prior_peak = c.shift(QDAYS).rolling(DDAYS_2Y - QDAYS, min_periods=YDAYS).max()
    return _safe_div(c - prior_peak, prior_peak.abs())


def f33_cpkt_107_coppock_ratio_to_prior_cycle_peak(close: pd.Series) -> pd.Series:
    """Ratio current Coppock / prior-cycle peak — values > 1 = secular advance, < 1 = lower-high."""
    c = _coppock_annual(close)
    prior_peak = c.shift(QDAYS).rolling(DDAYS_2Y - QDAYS, min_periods=YDAYS).max()
    return _safe_div(c, prior_peak)


def f33_cpkt_108_coppock_log_dist_from_prior_cycle_peak(close: pd.Series) -> pd.Series:
    """Signed |c - prior_peak|, normalized by trailing-252d std of c."""
    c = _coppock_annual(close)
    prior_peak = c.shift(QDAYS).rolling(DDAYS_2Y - QDAYS, min_periods=YDAYS).max()
    sd = c.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(c - prior_peak, sd)


def f33_cpkt_109_coppock_time_since_prior_cycle_peak_252d(close: pd.Series) -> pd.Series:
    """Bars since the prior 504d-Coppock-peak (peak found in c.shift(63).rolling(441))."""
    c = _coppock_annual(close)
    flag_pk = (c.shift(QDAYS) == c.shift(QDAYS).rolling(DDAYS_2Y - QDAYS, min_periods=YDAYS).max()).astype(float)
    return _bars_since_true(flag_pk)


def f33_cpkt_110_coppock_prior_cycle_peak_was_higher_indicator(close: pd.Series) -> pd.Series:
    """+1 when prior-cycle Coppock peak was higher than current 21d-max — lower-high structure."""
    c = _coppock_annual(close)
    prior_peak = c.shift(QDAYS).rolling(DDAYS_2Y - QDAYS, min_periods=YDAYS).max()
    cur_max = c.rolling(MDAYS, min_periods=WDAYS).max()
    return (prior_peak > cur_max).astype(float).where(prior_peak.notna() & cur_max.notna(), np.nan)


def f33_cpkt_111_kst_dist_from_prior_cycle_peak_pct(close: pd.Series) -> pd.Series:
    """Distance (% of |peak|) of current KST from its prior-cycle peak (504d max ending 63d ago)."""
    k = _kst(close)
    prior_peak = k.shift(QDAYS).rolling(DDAYS_2Y - QDAYS, min_periods=YDAYS).max()
    return _safe_div(k - prior_peak, prior_peak.abs())


def f33_cpkt_112_kst_time_since_prior_cycle_peak_252d(close: pd.Series) -> pd.Series:
    """Bars since the prior 504d-KST-peak."""
    k = _kst(close)
    flag_pk = (k.shift(QDAYS) == k.shift(QDAYS).rolling(DDAYS_2Y - QDAYS, min_periods=YDAYS).max()).astype(float)
    return _bars_since_true(flag_pk)


def f33_cpkt_113_kst_prior_cycle_peak_was_higher_indicator(close: pd.Series) -> pd.Series:
    """+1 if prior 504d-KST-peak was higher than current 21d-max — lower-high structure."""
    k = _kst(close)
    prior_peak = k.shift(QDAYS).rolling(DDAYS_2Y - QDAYS, min_periods=YDAYS).max()
    cur_max = k.rolling(MDAYS, min_periods=WDAYS).max()
    return (prior_peak > cur_max).astype(float).where(prior_peak.notna() & cur_max.notna(), np.nan)


def f33_cpkt_114_coppock_lower_high_count_252d(close: pd.Series) -> pd.Series:
    """Count of 21d-local-peak bars in trailing 252d where Coppock-annual peak was lower than the previous peak."""
    c = _coppock_annual(close)
    pk = ((c == c.rolling(MDAYS, min_periods=WDAYS).max()) & (c > c.shift(3))).astype(float)
    pk_val = c.where(pk == 1, np.nan).ffill()
    lower = (pk_val < pk_val.shift(1)).astype(float)
    return lower.rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_115_kst_lower_high_count_252d(close: pd.Series) -> pd.Series:
    """Count of 21d-local-peak bars in trailing 252d where KST peak was lower than the previous peak."""
    k = _kst(close)
    pk = ((k == k.rolling(MDAYS, min_periods=WDAYS).max()) & (k > k.shift(3))).astype(float)
    pk_val = k.where(pk == 1, np.nan).ffill()
    lower = (pk_val < pk_val.shift(1)).astype(float)
    return lower.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket M — Sign-stability / regime (116-125)
# ============================================================

def f33_cpkt_116_coppock_fraction_positive_1260d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 1260d (5y) bars with positive annual Coppock — secular regime density."""
    c = _coppock_annual(close)
    return (c > 0).astype(float).rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f33_cpkt_117_kst_fraction_positive_1260d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 1260d bars with positive KST."""
    k = _kst(close)
    return (k > 0).astype(float).rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f33_cpkt_118_coppock_regime_entropy_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of binary positive/negative Coppock states over trailing 252d (0..1)."""
    c = _coppock_annual(close)
    p = (c > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    q = 1.0 - p
    e = -(p * np.log2(p.replace(0, np.nan)) + q * np.log2(q.replace(0, np.nan)))
    return e.fillna(0.0).where(p.notna(), np.nan)


def f33_cpkt_119_kst_regime_entropy_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of binary positive/negative KST states over 252d."""
    k = _kst(close)
    p = (k > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    q = 1.0 - p
    e = -(p * np.log2(p.replace(0, np.nan)) + q * np.log2(q.replace(0, np.nan)))
    return e.fillna(0.0).where(p.notna(), np.nan)


def f33_cpkt_120_coppock_regime_persistence_index(close: pd.Series) -> pd.Series:
    """1 - normalized-cross-count: high values = stable regime, low = thrashing."""
    c = _coppock_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    cross_freq = flag.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS
    return 1.0 - cross_freq


def f33_cpkt_121_coppock_neg_to_pos_flip_count_504d(close: pd.Series) -> pd.Series:
    """Bullish zero-cross count in trailing 504d."""
    c = _coppock_annual(close)
    flag = ((c.shift(1) < 0) & (c >= 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f33_cpkt_122_kst_neg_to_pos_flip_count_504d(close: pd.Series) -> pd.Series:
    """Bullish zero-cross count of KST in trailing 504d."""
    k = _kst(close)
    flag = ((k.shift(1) < 0) & (k >= 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f33_cpkt_123_coppock_pos_regime_z_strength(close: pd.Series) -> pd.Series:
    """Mean of Coppock over the trailing 252d, conditional on positive values only — strength of positive regime."""
    c = _coppock_annual(close)
    pos = c.where(c > 0)
    return pos.rolling(YDAYS, min_periods=QDAYS).mean()


def f33_cpkt_124_coppock_sign_change_irregularity_index(close: pd.Series) -> pd.Series:
    """Std deviation of inter-sign-change gap lengths within trailing 504d — irregularity gauge."""
    c = _coppock_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(int)
    idx = pd.Series(np.arange(len(c)), index=c.index)
    last_cross_idx = idx.where(flag == 1, np.nan).ffill()
    gaps = idx - last_cross_idx
    return gaps.rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f33_cpkt_125_combined_coppock_kst_regime_classification(close: pd.Series) -> pd.Series:
    """Integer regime: 2*sign(Coppock annual) + 1*sign(KST). Range {-3..+3} mapping the joint quadrant."""
    c = np.sign(_coppock_annual(close)).fillna(0)
    k = np.sign(_kst(close)).fillna(0)
    return 2.0 * c + 1.0 * k


# ============================================================
# Bucket N — Acceleration / d² (126-135)
# ============================================================

def f33_cpkt_126_coppock_d2_21d(close: pd.Series) -> pd.Series:
    """Slope-of-slope of annual Coppock over 21d (acceleration)."""
    c = _coppock_annual(close)
    return _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)


def f33_cpkt_127_coppock_d2_63d(close: pd.Series) -> pd.Series:
    """Slope-of-slope of annual Coppock over 63d (medium-cycle acceleration)."""
    c = _coppock_annual(close)
    return _rolling_slope(_rolling_slope(c, QDAYS), QDAYS)


def f33_cpkt_128_coppock_d2_sign_change_bearish_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where d²Coppock crossed from positive to negative — inflection point."""
    c = _coppock_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan)


def f33_cpkt_129_kst_d2_21d(close: pd.Series) -> pd.Series:
    """Slope-of-slope of KST over 21d."""
    k = _kst(close)
    return _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)


def f33_cpkt_130_kst_d2_63d(close: pd.Series) -> pd.Series:
    """Slope-of-slope of KST over 63d."""
    k = _kst(close)
    return _rolling_slope(_rolling_slope(k, QDAYS), QDAYS)


def f33_cpkt_131_kst_d2_sign_change_bearish_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where d²KST crossed positive→negative — KST inflection."""
    k = _kst(close)
    d2 = _rolling_slope(_rolling_slope(k, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan)


def f33_cpkt_132_coppock_velocity_decay_post_peak_63d(close: pd.Series) -> pd.Series:
    """Coppock 21d-slope today divided by Coppock 21d-slope at last 63d-peak — velocity decay."""
    c = _coppock_annual(close)
    slope = _rolling_slope(c, MDAYS)
    is_pk = (c == c.rolling(QDAYS, min_periods=MDAYS).max()).astype(float)
    slope_at_pk = slope.where(is_pk == 1, np.nan).ffill()
    return _safe_div(slope, slope_at_pk)


def f33_cpkt_133_kst_velocity_decay_post_peak_63d(close: pd.Series) -> pd.Series:
    """KST 21d-slope today divided by KST 21d-slope at last 63d-peak — velocity decay."""
    k = _kst(close)
    slope = _rolling_slope(k, MDAYS)
    is_pk = (k == k.rolling(QDAYS, min_periods=MDAYS).max()).astype(float)
    slope_at_pk = slope.where(is_pk == 1, np.nan).ffill()
    return _safe_div(slope, slope_at_pk)


def f33_cpkt_134_coppock_inflection_point_indicator(close: pd.Series) -> pd.Series:
    """+1 when Coppock 21d-slope sign just flipped AND |d²Coppock| > z=1 (in 252d) — strong inflection."""
    c = _coppock_annual(close)
    s = _rolling_slope(c, MDAYS)
    flip = ((np.sign(s.shift(1)) != np.sign(s)) & s.notna() & s.shift(1).notna()).astype(float)
    d2 = _rolling_slope(s, MDAYS).abs()
    strong = (_rolling_zscore(d2, YDAYS) > 1.0).astype(float)
    return (flip * strong).where(s.notna(), np.nan)


def f33_cpkt_135_kst_inflection_point_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST 21d-slope sign just flipped AND |d²KST| > z=1 — strong KST inflection."""
    k = _kst(close)
    s = _rolling_slope(k, MDAYS)
    flip = ((np.sign(s.shift(1)) != np.sign(s)) & s.notna() & s.shift(1).notna()).astype(float)
    d2 = _rolling_slope(s, MDAYS).abs()
    strong = (_rolling_zscore(d2, YDAYS) > 1.0).astype(float)
    return (flip * strong).where(s.notna(), np.nan)


# ============================================================
# Bucket O — Smoothed-momentum exhaustion at price highs (136-145)
# ============================================================

def f33_cpkt_136_coppock_high_zscore_x_price_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when annual Coppock z(252) > 1.5 AND close within 1% of 252d max."""
    z = _rolling_zscore(_coppock_annual(close), YDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((z > 1.5) & (near == 1)).astype(float).where(z.notna() & near.notna(), np.nan)


def f33_cpkt_137_kst_high_zscore_x_price_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST z(252) > 1.5 AND close within 1% of 252d max."""
    z = _rolling_zscore(_kst(close), YDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((z > 1.5) & (near == 1)).astype(float).where(z.notna() & near.notna(), np.nan)


def f33_cpkt_138_coppock_negative_x_price_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when annual Coppock < 0 AND close at 252d new-high — severe long-momentum failure at price high."""
    c = _coppock_annual(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((c < 0) & (near == 1)).astype(float).where(c.notna() & near.notna(), np.nan)


def f33_cpkt_139_kst_below_signal_x_price_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST < signal line AND close within 1% of 252d max."""
    diff = _kst(close) - _kst_signal(close, 9)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((diff < 0) & (near == 1)).astype(float).where(diff.notna() & near.notna(), np.nan)


def f33_cpkt_140_coppock_peaking_x_price_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when annual Coppock 21d-slope just flipped negative AND close within 2% of 1260d max."""
    c = _coppock_annual(close)
    s = _rolling_slope(c, MDAYS)
    flip = ((s.shift(1) > 0) & (s <= 0)).astype(float)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (flip * near).where(s.notna() & near.notna(), np.nan)


def f33_cpkt_141_kst_peaking_x_price_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST 21d-slope just flipped negative AND close within 2% of 1260d max."""
    k = _kst(close)
    s = _rolling_slope(k, MDAYS)
    flip = ((s.shift(1) > 0) & (s <= 0)).astype(float)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (flip * near).where(s.notna() & near.notna(), np.nan)


def f33_cpkt_142_coppock_topping_pressure_score(close: pd.Series) -> pd.Series:
    """Composite: 0.4 * z(Coppock,252) + 0.3 * |slope-decay| + 0.3 * close-pct-rank-1260d."""
    z = _rolling_zscore(_coppock_annual(close), YDAYS)
    decay = f33_cpkt_132_coppock_velocity_decay_post_peak_63d(close).clip(lower=-3.0, upper=3.0)
    px_rank = _pct_rank(close, DDAYS_5Y)
    return 0.4 * z + 0.3 * (1.0 - decay.abs()).clip(lower=0.0) + 0.3 * px_rank


def f33_cpkt_143_kst_topping_pressure_score(close: pd.Series) -> pd.Series:
    """Composite: 0.4*z(KST,252) + 0.3 * |kst-velocity-decay| + 0.3 * close-pct-rank-1260d."""
    z = _rolling_zscore(_kst(close), YDAYS)
    decay = f33_cpkt_133_kst_velocity_decay_post_peak_63d(close).clip(lower=-3.0, upper=3.0)
    px_rank = _pct_rank(close, DDAYS_5Y)
    return 0.4 * z + 0.3 * (1.0 - decay.abs()).clip(lower=0.0) + 0.3 * px_rank


def f33_cpkt_144_combined_smoothed_momentum_exhaustion_score(close: pd.Series) -> pd.Series:
    """Average of Coppock + KST topping scores."""
    return (f33_cpkt_142_coppock_topping_pressure_score(close)
            + f33_cpkt_143_kst_topping_pressure_score(close)) / 2.0


def f33_cpkt_145_coppock_kst_at_high_bearish_breadth(close: pd.Series) -> pd.Series:
    """Fraction of 4 conditions met: Coppock falling, KST falling, KST<signal, close near 252d high."""
    sc = _rolling_slope(_coppock_annual(close), MDAYS)
    sk = _rolling_slope(_kst(close), MDAYS)
    diff = _kst(close) - _kst_signal(close, 9)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99)
    a = (sc < 0).astype(float).fillna(0)
    b = (sk < 0).astype(float).fillna(0)
    c = (diff < 0).astype(float).fillna(0)
    d = near.astype(float).fillna(0)
    return (a + b + c + d) / 4.0


# ============================================================
# Bucket P — Pring variants & composites (146-150)
# ============================================================

def f33_cpkt_146_pring_long_inter_short_kst_stack_bearish_indicator(close: pd.Series) -> pd.Series:
    """+1 when long-term KST < 0 AND intermediate KST < 0 AND short-term KST < 0 (all-bearish stack)."""
    return f33_cpkt_077_kst_short_inter_long_all_down_indicator(close)


def f33_cpkt_147_coppock_smoothed_close_short_cycle_value(close: pd.Series) -> pd.Series:
    """Quarterly Coppock computed on a 5d-SMA-smoothed close — denoised short-cycle variant."""
    smoothed = _sma(close, WDAYS)
    return _coppock(smoothed, QDAYS, 42, MDAYS)


def f33_cpkt_148_kst_smoothed_close_short_cycle_value(close: pd.Series) -> pd.Series:
    """Standard KST computed on a 5d-SMA-smoothed close — denoised KST variant."""
    smoothed = _sma(close, WDAYS)
    return _kst(smoothed)


def f33_cpkt_149_coppock_exponential_value(close: pd.Series) -> pd.Series:
    """Exponential-weighted Coppock (EMA-105 replaces WMA-210) — distinct smoother hypothesis."""
    return _coppock_exponential(close)


def f33_cpkt_150_trix_coppock_style_long_smoothed_topping_composite(close: pd.Series) -> pd.Series:
    """Composite topping signal: TRIX(63)-style triple-EMA of close, percent-rank in 252d, weighted with annual Coppock z."""
    e1 = _ema(close, QDAYS); e2 = _ema(e1, QDAYS); e3 = _ema(e2, QDAYS)
    trix_long = e3.pct_change() * 100.0
    trix_rank = _pct_rank(trix_long, YDAYS)
    z_cop = _rolling_zscore(_coppock_annual(close), YDAYS)
    return 0.5 * trix_rank + 0.5 * z_cop


# ============================================================
# REGISTRY
# ============================================================



def f33_cpkt_076_kst_short_inter_long_all_up_indicator_d2(close):
    return f33_cpkt_076_kst_short_inter_long_all_up_indicator(close).diff().diff()


def f33_cpkt_077_kst_short_inter_long_all_down_indicator_d2(close):
    return f33_cpkt_077_kst_short_inter_long_all_down_indicator(close).diff().diff()


def f33_cpkt_078_kst_count_up_3horizons_d2(close):
    return f33_cpkt_078_kst_count_up_3horizons(close).diff().diff()


def f33_cpkt_079_kst_short_inter_long_fraction_up_d2(close):
    return f33_cpkt_079_kst_short_inter_long_fraction_up(close).diff().diff()


def f33_cpkt_080_kst_short_minus_long_zscore_252d_d2(close):
    return f33_cpkt_080_kst_short_minus_long_zscore_252d(close).diff().diff()


def f33_cpkt_081_kst_short_above_long_indicator_d2(close):
    return f33_cpkt_081_kst_short_above_long_indicator(close).diff().diff()


def f33_cpkt_082_kst_consensus_bull_to_bear_flip_indicator_d2(close):
    return f33_cpkt_082_kst_consensus_bull_to_bear_flip_indicator(close).diff().diff()


def f33_cpkt_083_kst_short_falling_long_rising_indicator_d2(close):
    return f33_cpkt_083_kst_short_falling_long_rising_indicator(close).diff().diff()


def f33_cpkt_084_kst_horizons_disagreement_score_d2(close):
    return f33_cpkt_084_kst_horizons_disagreement_score(close).diff().diff()


def f33_cpkt_085_kst_horizon_zscore_dispersion_252d_d2(close):
    return f33_cpkt_085_kst_horizon_zscore_dispersion_252d(close).diff().diff()


def f33_cpkt_086_coppock_kst_both_falling_indicator_d2(close):
    return f33_cpkt_086_coppock_kst_both_falling_indicator(close).diff().diff()


def f33_cpkt_087_coppock_kst_both_peaking_indicator_d2(close):
    return f33_cpkt_087_coppock_kst_both_peaking_indicator(close).diff().diff()


def f33_cpkt_088_coppock_kst_topping_score_composite_d2(close):
    return f33_cpkt_088_coppock_kst_topping_score_composite(close).diff().diff()


def f33_cpkt_089_coppock_kst_zsum_252d_d2(close):
    return f33_cpkt_089_coppock_kst_zsum_252d(close).diff().diff()


def f33_cpkt_090_coppock_kst_correlation_252d_d2(close):
    return f33_cpkt_090_coppock_kst_correlation_252d(close).diff().diff()


def f33_cpkt_091_coppock_kst_disagreement_252d_d2(close):
    return f33_cpkt_091_coppock_kst_disagreement_252d(close).diff().diff()


def f33_cpkt_092_days_since_coppock_AND_kst_joint_bearish_cross_d2(close):
    return f33_cpkt_092_days_since_coppock_AND_kst_joint_bearish_cross(close).diff().diff()


def f33_cpkt_093_coppock_kst_joint_bearish_div_63d_close_d2(close):
    return f33_cpkt_093_coppock_kst_joint_bearish_div_63d_close(close).diff().diff()


def f33_cpkt_094_long_smoothed_momentum_breadth_4indicators_d2(close):
    return f33_cpkt_094_long_smoothed_momentum_breadth_4indicators(close).diff().diff()


def f33_cpkt_095_long_smoothed_momentum_combined_zscore_252d_d2(close):
    return f33_cpkt_095_long_smoothed_momentum_combined_zscore_252d(close).diff().diff()


def f33_cpkt_096_coppock_plateau_dwell_at_252d_max_21d_d2(close):
    return f33_cpkt_096_coppock_plateau_dwell_at_252d_max_21d(close).diff().diff()


def f33_cpkt_097_coppock_plateau_width_at_max_63d_d2(close):
    return f33_cpkt_097_coppock_plateau_width_at_max_63d(close).diff().diff()


def f33_cpkt_098_coppock_curvature_21d_d2(close):
    return f33_cpkt_098_coppock_curvature_21d(close).diff().diff()


def f33_cpkt_099_coppock_post_plateau_breakdown_velocity_d2(close):
    return f33_cpkt_099_coppock_post_plateau_breakdown_velocity(close).diff().diff()


def f33_cpkt_100_kst_plateau_dwell_at_252d_max_21d_d2(close):
    return f33_cpkt_100_kst_plateau_dwell_at_252d_max_21d(close).diff().diff()


def f33_cpkt_101_kst_plateau_width_at_max_63d_d2(close):
    return f33_cpkt_101_kst_plateau_width_at_max_63d(close).diff().diff()


def f33_cpkt_102_kst_curvature_21d_d2(close):
    return f33_cpkt_102_kst_curvature_21d(close).diff().diff()


def f33_cpkt_103_kst_post_plateau_breakdown_velocity_d2(close):
    return f33_cpkt_103_kst_post_plateau_breakdown_velocity(close).diff().diff()


def f33_cpkt_104_coppock_kst_joint_plateau_indicator_d2(close):
    return f33_cpkt_104_coppock_kst_joint_plateau_indicator(close).diff().diff()


def f33_cpkt_105_smoothed_momentum_topping_shape_composite_d2(close):
    return f33_cpkt_105_smoothed_momentum_topping_shape_composite(close).diff().diff()


def f33_cpkt_106_coppock_dist_from_prior_cycle_peak_pct_d2(close):
    return f33_cpkt_106_coppock_dist_from_prior_cycle_peak_pct(close).diff().diff()


def f33_cpkt_107_coppock_ratio_to_prior_cycle_peak_d2(close):
    return f33_cpkt_107_coppock_ratio_to_prior_cycle_peak(close).diff().diff()


def f33_cpkt_108_coppock_log_dist_from_prior_cycle_peak_d2(close):
    return f33_cpkt_108_coppock_log_dist_from_prior_cycle_peak(close).diff().diff()


def f33_cpkt_109_coppock_time_since_prior_cycle_peak_252d_d2(close):
    return f33_cpkt_109_coppock_time_since_prior_cycle_peak_252d(close).diff().diff()


def f33_cpkt_110_coppock_prior_cycle_peak_was_higher_indicator_d2(close):
    return f33_cpkt_110_coppock_prior_cycle_peak_was_higher_indicator(close).diff().diff()


def f33_cpkt_111_kst_dist_from_prior_cycle_peak_pct_d2(close):
    return f33_cpkt_111_kst_dist_from_prior_cycle_peak_pct(close).diff().diff()


def f33_cpkt_112_kst_time_since_prior_cycle_peak_252d_d2(close):
    return f33_cpkt_112_kst_time_since_prior_cycle_peak_252d(close).diff().diff()


def f33_cpkt_113_kst_prior_cycle_peak_was_higher_indicator_d2(close):
    return f33_cpkt_113_kst_prior_cycle_peak_was_higher_indicator(close).diff().diff()


def f33_cpkt_114_coppock_lower_high_count_252d_d2(close):
    return f33_cpkt_114_coppock_lower_high_count_252d(close).diff().diff()


def f33_cpkt_115_kst_lower_high_count_252d_d2(close):
    return f33_cpkt_115_kst_lower_high_count_252d(close).diff().diff()


def f33_cpkt_116_coppock_fraction_positive_1260d_d2(close):
    return f33_cpkt_116_coppock_fraction_positive_1260d(close).diff().diff()


def f33_cpkt_117_kst_fraction_positive_1260d_d2(close):
    return f33_cpkt_117_kst_fraction_positive_1260d(close).diff().diff()


def f33_cpkt_118_coppock_regime_entropy_252d_d2(close):
    return f33_cpkt_118_coppock_regime_entropy_252d(close).diff().diff()


def f33_cpkt_119_kst_regime_entropy_252d_d2(close):
    return f33_cpkt_119_kst_regime_entropy_252d(close).diff().diff()


def f33_cpkt_120_coppock_regime_persistence_index_d2(close):
    return f33_cpkt_120_coppock_regime_persistence_index(close).diff().diff()


def f33_cpkt_121_coppock_neg_to_pos_flip_count_504d_d2(close):
    return f33_cpkt_121_coppock_neg_to_pos_flip_count_504d(close).diff().diff()


def f33_cpkt_122_kst_neg_to_pos_flip_count_504d_d2(close):
    return f33_cpkt_122_kst_neg_to_pos_flip_count_504d(close).diff().diff()


def f33_cpkt_123_coppock_pos_regime_z_strength_d2(close):
    return f33_cpkt_123_coppock_pos_regime_z_strength(close).diff().diff()


def f33_cpkt_124_coppock_sign_change_irregularity_index_d2(close):
    return f33_cpkt_124_coppock_sign_change_irregularity_index(close).diff().diff()


def f33_cpkt_125_combined_coppock_kst_regime_classification_d2(close):
    return f33_cpkt_125_combined_coppock_kst_regime_classification(close).diff().diff()


def f33_cpkt_126_coppock_d2_21d_d2(close):
    return f33_cpkt_126_coppock_d2_21d(close).diff().diff()


def f33_cpkt_127_coppock_d2_63d_d2(close):
    return f33_cpkt_127_coppock_d2_63d(close).diff().diff()


def f33_cpkt_128_coppock_d2_sign_change_bearish_indicator_d2(close):
    return f33_cpkt_128_coppock_d2_sign_change_bearish_indicator(close).diff().diff()


def f33_cpkt_129_kst_d2_21d_d2(close):
    return f33_cpkt_129_kst_d2_21d(close).diff().diff()


def f33_cpkt_130_kst_d2_63d_d2(close):
    return f33_cpkt_130_kst_d2_63d(close).diff().diff()


def f33_cpkt_131_kst_d2_sign_change_bearish_indicator_d2(close):
    return f33_cpkt_131_kst_d2_sign_change_bearish_indicator(close).diff().diff()


def f33_cpkt_132_coppock_velocity_decay_post_peak_63d_d2(close):
    return f33_cpkt_132_coppock_velocity_decay_post_peak_63d(close).diff().diff()


def f33_cpkt_133_kst_velocity_decay_post_peak_63d_d2(close):
    return f33_cpkt_133_kst_velocity_decay_post_peak_63d(close).diff().diff()


def f33_cpkt_134_coppock_inflection_point_indicator_d2(close):
    return f33_cpkt_134_coppock_inflection_point_indicator(close).diff().diff()


def f33_cpkt_135_kst_inflection_point_indicator_d2(close):
    return f33_cpkt_135_kst_inflection_point_indicator(close).diff().diff()


def f33_cpkt_136_coppock_high_zscore_x_price_252d_high_indicator_d2(close):
    return f33_cpkt_136_coppock_high_zscore_x_price_252d_high_indicator(close).diff().diff()


def f33_cpkt_137_kst_high_zscore_x_price_252d_high_indicator_d2(close):
    return f33_cpkt_137_kst_high_zscore_x_price_252d_high_indicator(close).diff().diff()


def f33_cpkt_138_coppock_negative_x_price_252d_high_indicator_d2(close):
    return f33_cpkt_138_coppock_negative_x_price_252d_high_indicator(close).diff().diff()


def f33_cpkt_139_kst_below_signal_x_price_252d_high_indicator_d2(close):
    return f33_cpkt_139_kst_below_signal_x_price_252d_high_indicator(close).diff().diff()


def f33_cpkt_140_coppock_peaking_x_price_1260d_high_indicator_d2(close):
    return f33_cpkt_140_coppock_peaking_x_price_1260d_high_indicator(close).diff().diff()


def f33_cpkt_141_kst_peaking_x_price_1260d_high_indicator_d2(close):
    return f33_cpkt_141_kst_peaking_x_price_1260d_high_indicator(close).diff().diff()


def f33_cpkt_142_coppock_topping_pressure_score_d2(close):
    return f33_cpkt_142_coppock_topping_pressure_score(close).diff().diff()


def f33_cpkt_143_kst_topping_pressure_score_d2(close):
    return f33_cpkt_143_kst_topping_pressure_score(close).diff().diff()


def f33_cpkt_144_combined_smoothed_momentum_exhaustion_score_d2(close):
    return f33_cpkt_144_combined_smoothed_momentum_exhaustion_score(close).diff().diff()


def f33_cpkt_145_coppock_kst_at_high_bearish_breadth_d2(close):
    return f33_cpkt_145_coppock_kst_at_high_bearish_breadth(close).diff().diff()


def f33_cpkt_146_pring_long_inter_short_kst_stack_bearish_indicator_d2(close):
    return f33_cpkt_146_pring_long_inter_short_kst_stack_bearish_indicator(close).diff().diff()


def f33_cpkt_147_coppock_smoothed_close_short_cycle_value_d2(close):
    return f33_cpkt_147_coppock_smoothed_close_short_cycle_value(close).diff().diff()


def f33_cpkt_148_kst_smoothed_close_short_cycle_value_d2(close):
    return f33_cpkt_148_kst_smoothed_close_short_cycle_value(close).diff().diff()


def f33_cpkt_149_coppock_exponential_value_d2(close):
    return f33_cpkt_149_coppock_exponential_value(close).diff().diff()


def f33_cpkt_150_trix_coppock_style_long_smoothed_topping_composite_d2(close):
    return f33_cpkt_150_trix_coppock_style_long_smoothed_topping_composite(close).diff().diff()


COPPOCK_CURVE_KST_D2_REGISTRY_076_150 = {
    "f33_cpkt_076_kst_short_inter_long_all_up_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_076_kst_short_inter_long_all_up_indicator_d2},
    "f33_cpkt_077_kst_short_inter_long_all_down_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_077_kst_short_inter_long_all_down_indicator_d2},
    "f33_cpkt_078_kst_count_up_3horizons_d2": {"inputs": ["close"], "func": f33_cpkt_078_kst_count_up_3horizons_d2},
    "f33_cpkt_079_kst_short_inter_long_fraction_up_d2": {"inputs": ["close"], "func": f33_cpkt_079_kst_short_inter_long_fraction_up_d2},
    "f33_cpkt_080_kst_short_minus_long_zscore_252d_d2": {"inputs": ["close"], "func": f33_cpkt_080_kst_short_minus_long_zscore_252d_d2},
    "f33_cpkt_081_kst_short_above_long_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_081_kst_short_above_long_indicator_d2},
    "f33_cpkt_082_kst_consensus_bull_to_bear_flip_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_082_kst_consensus_bull_to_bear_flip_indicator_d2},
    "f33_cpkt_083_kst_short_falling_long_rising_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_083_kst_short_falling_long_rising_indicator_d2},
    "f33_cpkt_084_kst_horizons_disagreement_score_d2": {"inputs": ["close"], "func": f33_cpkt_084_kst_horizons_disagreement_score_d2},
    "f33_cpkt_085_kst_horizon_zscore_dispersion_252d_d2": {"inputs": ["close"], "func": f33_cpkt_085_kst_horizon_zscore_dispersion_252d_d2},
    "f33_cpkt_086_coppock_kst_both_falling_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_086_coppock_kst_both_falling_indicator_d2},
    "f33_cpkt_087_coppock_kst_both_peaking_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_087_coppock_kst_both_peaking_indicator_d2},
    "f33_cpkt_088_coppock_kst_topping_score_composite_d2": {"inputs": ["close"], "func": f33_cpkt_088_coppock_kst_topping_score_composite_d2},
    "f33_cpkt_089_coppock_kst_zsum_252d_d2": {"inputs": ["close"], "func": f33_cpkt_089_coppock_kst_zsum_252d_d2},
    "f33_cpkt_090_coppock_kst_correlation_252d_d2": {"inputs": ["close"], "func": f33_cpkt_090_coppock_kst_correlation_252d_d2},
    "f33_cpkt_091_coppock_kst_disagreement_252d_d2": {"inputs": ["close"], "func": f33_cpkt_091_coppock_kst_disagreement_252d_d2},
    "f33_cpkt_092_days_since_coppock_AND_kst_joint_bearish_cross_d2": {"inputs": ["close"], "func": f33_cpkt_092_days_since_coppock_AND_kst_joint_bearish_cross_d2},
    "f33_cpkt_093_coppock_kst_joint_bearish_div_63d_close_d2": {"inputs": ["close"], "func": f33_cpkt_093_coppock_kst_joint_bearish_div_63d_close_d2},
    "f33_cpkt_094_long_smoothed_momentum_breadth_4indicators_d2": {"inputs": ["close"], "func": f33_cpkt_094_long_smoothed_momentum_breadth_4indicators_d2},
    "f33_cpkt_095_long_smoothed_momentum_combined_zscore_252d_d2": {"inputs": ["close"], "func": f33_cpkt_095_long_smoothed_momentum_combined_zscore_252d_d2},
    "f33_cpkt_096_coppock_plateau_dwell_at_252d_max_21d_d2": {"inputs": ["close"], "func": f33_cpkt_096_coppock_plateau_dwell_at_252d_max_21d_d2},
    "f33_cpkt_097_coppock_plateau_width_at_max_63d_d2": {"inputs": ["close"], "func": f33_cpkt_097_coppock_plateau_width_at_max_63d_d2},
    "f33_cpkt_098_coppock_curvature_21d_d2": {"inputs": ["close"], "func": f33_cpkt_098_coppock_curvature_21d_d2},
    "f33_cpkt_099_coppock_post_plateau_breakdown_velocity_d2": {"inputs": ["close"], "func": f33_cpkt_099_coppock_post_plateau_breakdown_velocity_d2},
    "f33_cpkt_100_kst_plateau_dwell_at_252d_max_21d_d2": {"inputs": ["close"], "func": f33_cpkt_100_kst_plateau_dwell_at_252d_max_21d_d2},
    "f33_cpkt_101_kst_plateau_width_at_max_63d_d2": {"inputs": ["close"], "func": f33_cpkt_101_kst_plateau_width_at_max_63d_d2},
    "f33_cpkt_102_kst_curvature_21d_d2": {"inputs": ["close"], "func": f33_cpkt_102_kst_curvature_21d_d2},
    "f33_cpkt_103_kst_post_plateau_breakdown_velocity_d2": {"inputs": ["close"], "func": f33_cpkt_103_kst_post_plateau_breakdown_velocity_d2},
    "f33_cpkt_104_coppock_kst_joint_plateau_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_104_coppock_kst_joint_plateau_indicator_d2},
    "f33_cpkt_105_smoothed_momentum_topping_shape_composite_d2": {"inputs": ["close"], "func": f33_cpkt_105_smoothed_momentum_topping_shape_composite_d2},
    "f33_cpkt_106_coppock_dist_from_prior_cycle_peak_pct_d2": {"inputs": ["close"], "func": f33_cpkt_106_coppock_dist_from_prior_cycle_peak_pct_d2},
    "f33_cpkt_107_coppock_ratio_to_prior_cycle_peak_d2": {"inputs": ["close"], "func": f33_cpkt_107_coppock_ratio_to_prior_cycle_peak_d2},
    "f33_cpkt_108_coppock_log_dist_from_prior_cycle_peak_d2": {"inputs": ["close"], "func": f33_cpkt_108_coppock_log_dist_from_prior_cycle_peak_d2},
    "f33_cpkt_109_coppock_time_since_prior_cycle_peak_252d_d2": {"inputs": ["close"], "func": f33_cpkt_109_coppock_time_since_prior_cycle_peak_252d_d2},
    "f33_cpkt_110_coppock_prior_cycle_peak_was_higher_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_110_coppock_prior_cycle_peak_was_higher_indicator_d2},
    "f33_cpkt_111_kst_dist_from_prior_cycle_peak_pct_d2": {"inputs": ["close"], "func": f33_cpkt_111_kst_dist_from_prior_cycle_peak_pct_d2},
    "f33_cpkt_112_kst_time_since_prior_cycle_peak_252d_d2": {"inputs": ["close"], "func": f33_cpkt_112_kst_time_since_prior_cycle_peak_252d_d2},
    "f33_cpkt_113_kst_prior_cycle_peak_was_higher_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_113_kst_prior_cycle_peak_was_higher_indicator_d2},
    "f33_cpkt_114_coppock_lower_high_count_252d_d2": {"inputs": ["close"], "func": f33_cpkt_114_coppock_lower_high_count_252d_d2},
    "f33_cpkt_115_kst_lower_high_count_252d_d2": {"inputs": ["close"], "func": f33_cpkt_115_kst_lower_high_count_252d_d2},
    "f33_cpkt_116_coppock_fraction_positive_1260d_d2": {"inputs": ["close"], "func": f33_cpkt_116_coppock_fraction_positive_1260d_d2},
    "f33_cpkt_117_kst_fraction_positive_1260d_d2": {"inputs": ["close"], "func": f33_cpkt_117_kst_fraction_positive_1260d_d2},
    "f33_cpkt_118_coppock_regime_entropy_252d_d2": {"inputs": ["close"], "func": f33_cpkt_118_coppock_regime_entropy_252d_d2},
    "f33_cpkt_119_kst_regime_entropy_252d_d2": {"inputs": ["close"], "func": f33_cpkt_119_kst_regime_entropy_252d_d2},
    "f33_cpkt_120_coppock_regime_persistence_index_d2": {"inputs": ["close"], "func": f33_cpkt_120_coppock_regime_persistence_index_d2},
    "f33_cpkt_121_coppock_neg_to_pos_flip_count_504d_d2": {"inputs": ["close"], "func": f33_cpkt_121_coppock_neg_to_pos_flip_count_504d_d2},
    "f33_cpkt_122_kst_neg_to_pos_flip_count_504d_d2": {"inputs": ["close"], "func": f33_cpkt_122_kst_neg_to_pos_flip_count_504d_d2},
    "f33_cpkt_123_coppock_pos_regime_z_strength_d2": {"inputs": ["close"], "func": f33_cpkt_123_coppock_pos_regime_z_strength_d2},
    "f33_cpkt_124_coppock_sign_change_irregularity_index_d2": {"inputs": ["close"], "func": f33_cpkt_124_coppock_sign_change_irregularity_index_d2},
    "f33_cpkt_125_combined_coppock_kst_regime_classification_d2": {"inputs": ["close"], "func": f33_cpkt_125_combined_coppock_kst_regime_classification_d2},
    "f33_cpkt_126_coppock_d2_21d_d2": {"inputs": ["close"], "func": f33_cpkt_126_coppock_d2_21d_d2},
    "f33_cpkt_127_coppock_d2_63d_d2": {"inputs": ["close"], "func": f33_cpkt_127_coppock_d2_63d_d2},
    "f33_cpkt_128_coppock_d2_sign_change_bearish_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_128_coppock_d2_sign_change_bearish_indicator_d2},
    "f33_cpkt_129_kst_d2_21d_d2": {"inputs": ["close"], "func": f33_cpkt_129_kst_d2_21d_d2},
    "f33_cpkt_130_kst_d2_63d_d2": {"inputs": ["close"], "func": f33_cpkt_130_kst_d2_63d_d2},
    "f33_cpkt_131_kst_d2_sign_change_bearish_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_131_kst_d2_sign_change_bearish_indicator_d2},
    "f33_cpkt_132_coppock_velocity_decay_post_peak_63d_d2": {"inputs": ["close"], "func": f33_cpkt_132_coppock_velocity_decay_post_peak_63d_d2},
    "f33_cpkt_133_kst_velocity_decay_post_peak_63d_d2": {"inputs": ["close"], "func": f33_cpkt_133_kst_velocity_decay_post_peak_63d_d2},
    "f33_cpkt_134_coppock_inflection_point_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_134_coppock_inflection_point_indicator_d2},
    "f33_cpkt_135_kst_inflection_point_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_135_kst_inflection_point_indicator_d2},
    "f33_cpkt_136_coppock_high_zscore_x_price_252d_high_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_136_coppock_high_zscore_x_price_252d_high_indicator_d2},
    "f33_cpkt_137_kst_high_zscore_x_price_252d_high_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_137_kst_high_zscore_x_price_252d_high_indicator_d2},
    "f33_cpkt_138_coppock_negative_x_price_252d_high_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_138_coppock_negative_x_price_252d_high_indicator_d2},
    "f33_cpkt_139_kst_below_signal_x_price_252d_high_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_139_kst_below_signal_x_price_252d_high_indicator_d2},
    "f33_cpkt_140_coppock_peaking_x_price_1260d_high_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_140_coppock_peaking_x_price_1260d_high_indicator_d2},
    "f33_cpkt_141_kst_peaking_x_price_1260d_high_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_141_kst_peaking_x_price_1260d_high_indicator_d2},
    "f33_cpkt_142_coppock_topping_pressure_score_d2": {"inputs": ["close"], "func": f33_cpkt_142_coppock_topping_pressure_score_d2},
    "f33_cpkt_143_kst_topping_pressure_score_d2": {"inputs": ["close"], "func": f33_cpkt_143_kst_topping_pressure_score_d2},
    "f33_cpkt_144_combined_smoothed_momentum_exhaustion_score_d2": {"inputs": ["close"], "func": f33_cpkt_144_combined_smoothed_momentum_exhaustion_score_d2},
    "f33_cpkt_145_coppock_kst_at_high_bearish_breadth_d2": {"inputs": ["close"], "func": f33_cpkt_145_coppock_kst_at_high_bearish_breadth_d2},
    "f33_cpkt_146_pring_long_inter_short_kst_stack_bearish_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_146_pring_long_inter_short_kst_stack_bearish_indicator_d2},
    "f33_cpkt_147_coppock_smoothed_close_short_cycle_value_d2": {"inputs": ["close"], "func": f33_cpkt_147_coppock_smoothed_close_short_cycle_value_d2},
    "f33_cpkt_148_kst_smoothed_close_short_cycle_value_d2": {"inputs": ["close"], "func": f33_cpkt_148_kst_smoothed_close_short_cycle_value_d2},
    "f33_cpkt_149_coppock_exponential_value_d2": {"inputs": ["close"], "func": f33_cpkt_149_coppock_exponential_value_d2},
    "f33_cpkt_150_trix_coppock_style_long_smoothed_topping_composite_d2": {"inputs": ["close"], "func": f33_cpkt_150_trix_coppock_style_long_smoothed_topping_composite_d2},
}
