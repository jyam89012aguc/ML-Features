"""session_open_close_dynamics d2 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d2__001_075.py. Each
feature encodes a different concept in the open/close/intraday-session theme:
gap dynamics / close-in-range / intraday reversal / body-wick / asymmetry /
distribution-day / session composites.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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


def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def f46_socd_076_body_share_of_range_1d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div(close - open, high - low)
    return out.diff().diff()


def f46_socd_077_body_share_of_range_21d_mean_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    b = _safe_div(close - open, high - low)
    out = b.rolling(21, min_periods=7).mean()
    return out.diff().diff()


def f46_socd_078_body_share_of_range_63d_mean_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    b = _safe_div(close - open, high - low)
    out = b.rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f46_socd_079_abs_body_share_of_range_1d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div((close - open).abs(), high - low)
    return out.diff().diff()


def f46_socd_080_intraday_log_return_1d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_log(close) - _safe_log(open)
    return out.diff().diff()


def f46_socd_081_cum_intraday_log_return_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    ir = _safe_log(close) - _safe_log(open)
    out = ir.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_082_cum_intraday_log_return_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    ir = _safe_log(close) - _safe_log(open)
    out = ir.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f46_socd_083_intraday_minus_overnight_drift_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    ir = _safe_log(close) - _safe_log(open)
    og = _safe_log(open) - _safe_log(close.shift(1))
    out = ir.rolling(63, min_periods=21).sum() - og.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f46_socd_084_intraday_log_return_std_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    ir = _safe_log(close) - _safe_log(open)
    out = ir.rolling(63, min_periods=21).std()
    return out.diff().diff()


def f46_socd_085_overnight_log_return_std_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    og = _safe_log(open) - _safe_log(close.shift(1))
    out = og.rolling(63, min_periods=21).std()
    return out.diff().diff()


def f46_socd_086_intraday_over_overnight_vol_ratio_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    ir = _safe_log(close) - _safe_log(open)
    og = _safe_log(open) - _safe_log(close.shift(1))
    out = _safe_div(ir.rolling(63, min_periods=21).std(), og.rolling(63, min_periods=21).std())
    return out.diff().diff()


def f46_socd_087_bullish_body_count_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    b = (close > open).astype(float).where(open.notna() & close.notna(), np.nan)
    out = b.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_088_bearish_body_count_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    b = (close < open).astype(float).where(open.notna() & close.notna(), np.nan)
    out = b.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_089_bull_minus_bear_body_count_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    bu = (close > open).astype(float); be = (close < open).astype(float)
    out = bu.rolling(63, min_periods=21).sum() - be.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f46_socd_090_mean_abs_body_pct_close_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    b = _safe_div((close - open).abs(), close)
    out = b.rolling(21, min_periods=7).mean()
    return out.diff().diff()


def f46_socd_091_upper_wick_1d_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    ub = pd.concat([open, close], axis=1).max(axis=1)
    out = high - ub
    return out.diff().diff()


def f46_socd_092_lower_wick_1d_d2(open: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lb = pd.concat([open, close], axis=1).min(axis=1)
    out = lb - low
    return out.diff().diff()


def f46_socd_093_upper_wick_share_of_range_1d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ub = pd.concat([open, close], axis=1).max(axis=1)
    out = _safe_div(high - ub, high - low)
    return out.diff().diff()


def f46_socd_094_lower_wick_share_of_range_1d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lb = pd.concat([open, close], axis=1).min(axis=1)
    out = _safe_div(lb - low, high - low)
    return out.diff().diff()


def f46_socd_095_long_upper_wick_indicator_1d_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    ub = pd.concat([open, close], axis=1).max(axis=1)
    uw = high - ub
    body = (close - open).abs()
    out = (uw > 2.0 * body).astype(float).where(body.notna(), np.nan)
    return out.diff().diff()


def f46_socd_096_long_lower_wick_indicator_1d_d2(open: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lb = pd.concat([open, close], axis=1).min(axis=1)
    lw = lb - low
    body = (close - open).abs()
    out = (lw > 2.0 * body).astype(float).where(body.notna(), np.nan)
    return out.diff().diff()


def f46_socd_097_doji_indicator_1d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs()
    rng = high - low
    out = (_safe_div(body, rng) < 0.1).astype(float).where(rng.notna(), np.nan)
    return out.diff().diff()


def f46_socd_098_shooting_star_indicator_1d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs()
    rng = high - low
    ub = pd.concat([open, close], axis=1).max(axis=1)
    uw = high - ub
    out = ((_safe_div(body, rng) < 0.3) & (uw > 2.0 * body) & (close < open)).astype(float).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff()


def f46_socd_099_hammer_indicator_1d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs()
    rng = high - low
    lb = pd.concat([open, close], axis=1).min(axis=1)
    lw = lb - low
    out = ((_safe_div(body, rng) < 0.3) & (lw > 2.0 * body)).astype(float).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff()


def f46_socd_100_shooting_star_count_63d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs()
    rng = high - low
    ub = pd.concat([open, close], axis=1).max(axis=1)
    uw = high - ub
    ss = ((_safe_div(body, rng) < 0.3) & (uw > 2.0 * body) & (close < open)).astype(float).where(rng.notna() & body.notna(), np.nan)
    out = ss.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f46_socd_101_doji_count_63d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs()
    rng = high - low
    out = (_safe_div(body, rng) < 0.1).astype(float).where(rng.notna(), np.nan).rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f46_socd_102_mean_upper_wick_pct_range_21d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ub = pd.concat([open, close], axis=1).max(axis=1)
    uw = _safe_div(high - ub, high - low)
    out = uw.rolling(21, min_periods=7).mean()
    return out.diff().diff()


def f46_socd_103_mean_lower_wick_pct_range_21d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lb = pd.concat([open, close], axis=1).min(axis=1)
    lw = _safe_div(lb - low, high - low)
    out = lw.rolling(21, min_periods=7).mean()
    return out.diff().diff()


def f46_socd_104_upper_minus_lower_wick_pct_range_21d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ub = pd.concat([open, close], axis=1).max(axis=1)
    lb = pd.concat([open, close], axis=1).min(axis=1)
    uw = _safe_div(high - ub, high - low).rolling(21, min_periods=7).mean()
    lw = _safe_div(lb - low, high - low).rolling(21, min_periods=7).mean()
    out = uw - lw
    return out.diff().diff()


def f46_socd_105_upper_wick_dominance_regime_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ub = pd.concat([open, close], axis=1).max(axis=1)
    lb = pd.concat([open, close], axis=1).min(axis=1)
    im = _safe_div(high - ub, high - low) - _safe_div(lb - low, high - low)
    sd = im.rolling(252, min_periods=84).std()
    out = (im > 2.0 * sd).astype(float).where(sd.notna(), np.nan)
    return out.diff().diff()


def f46_socd_106_gap_up_bear_close_distribution_indicator_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    bear = (close < open).astype(float)
    out = (g_up * bear).where(close.shift(1).notna(), np.nan)
    return out.diff().diff()


def f46_socd_107_gap_up_bear_count_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    bear = (close < open).astype(float)
    ev = (g_up * bear).where(close.shift(1).notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_108_gap_up_bear_count_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    bear = (close < open).astype(float)
    ev = (g_up * bear).where(close.shift(1).notna(), np.nan)
    out = ev.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f46_socd_109_open_above_prior_high_bear_close_1d_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    ev = ((open > high.shift(1)) & (close < open)).astype(float).where(high.shift(1).notna() & open.notna(), np.nan)
    out = ev
    return out.diff().diff()


def f46_socd_110_open_above_prior_high_bear_close_count_21d_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    ev = ((open > high.shift(1)) & (close < open)).astype(float).where(high.shift(1).notna() & open.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_111_open_below_prior_low_bull_close_1d_d2(open: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ev = ((open < low.shift(1)) & (close > open)).astype(float).where(low.shift(1).notna() & open.notna(), np.nan)
    out = ev
    return out.diff().diff()


def f46_socd_112_strong_open_weak_close_1d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    op_pos = _safe_div(open - low, high - low)
    cl_pos = _safe_div(close - low, high - low)
    out = ((op_pos > 0.8) & (cl_pos < 0.2)).astype(float).where(op_pos.notna() & cl_pos.notna(), np.nan)
    return out.diff().diff()


def f46_socd_113_strong_open_weak_close_count_21d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    op_pos = _safe_div(open - low, high - low)
    cl_pos = _safe_div(close - low, high - low)
    ev = ((op_pos > 0.8) & (cl_pos < 0.2)).astype(float).where(op_pos.notna() & cl_pos.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_114_weak_open_strong_close_count_21d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    op_pos = _safe_div(open - low, high - low)
    cl_pos = _safe_div(close - low, high - low)
    ev = ((op_pos < 0.2) & (cl_pos > 0.8)).astype(float).where(op_pos.notna() & cl_pos.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_115_strong_open_weak_close_minus_inverse_63d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    op_pos = _safe_div(open - low, high - low)
    cl_pos = _safe_div(close - low, high - low)
    sw = ((op_pos > 0.8) & (cl_pos < 0.2)).astype(float)
    ws = ((op_pos < 0.2) & (cl_pos > 0.8)).astype(float)
    out = sw.rolling(63, min_periods=21).sum() - ws.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f46_socd_116_close_eq_low_indicator_1d_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    out = (close <= low * 1.001).astype(float).where(low.notna() & close.notna(), np.nan)
    return out.diff().diff()


def f46_socd_117_close_eq_high_indicator_1d_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    out = (close >= high * 0.999).astype(float).where(high.notna() & close.notna(), np.nan)
    return out.diff().diff()


def f46_socd_118_close_eq_low_count_21d_d2(low: pd.Series, close: pd.Series) -> pd.Series:
    ev = (close <= low * 1.001).astype(float).where(low.notna() & close.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_119_close_eq_high_count_21d_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    ev = (close >= high * 0.999).astype(float).where(high.notna() & close.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_120_close_at_low_minus_high_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cl_low = (close <= low * 1.001).astype(float).rolling(63, min_periods=21).sum()
    cl_high = (close >= high * 0.999).astype(float).rolling(63, min_periods=21).sum()
    out = cl_low - cl_high
    return out.diff().diff()


def f46_socd_121_distribution_score_21d_gap_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    g_dn = (open < close.shift(1) * 0.995).astype(float)
    bear = (close < open).astype(float); bull = (close > open).astype(float)
    dist = (g_up * bear).rolling(21, min_periods=7).sum()
    acc = (g_dn * bull).rolling(21, min_periods=7).sum()
    out = dist - acc
    return out.diff().diff()


def f46_socd_122_distribution_score_63d_gap_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    g_dn = (open < close.shift(1) * 0.995).astype(float)
    bear = (close < open).astype(float); bull = (close > open).astype(float)
    dist = (g_up * bear).rolling(63, min_periods=21).sum()
    acc = (g_dn * bull).rolling(63, min_periods=21).sum()
    out = dist - acc
    return out.diff().diff()


def f46_socd_123_min_close_pos_in_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = p.rolling(63, min_periods=21).min()
    return out.diff().diff()


def f46_socd_124_max_close_pos_in_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = p.rolling(63, min_periods=21).max()
    return out.diff().diff()


def f46_socd_125_close_pos_range_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = p.rolling(63, min_periods=21).max() - p.rolling(63, min_periods=21).min()
    return out.diff().diff()


def f46_socd_126_intraday_range_pct_close_63d_mean_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _safe_div(high - low, close)
    out = rp.rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f46_socd_127_body_share_of_range_std_63d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    b = _safe_div(close - open, high - low)
    out = b.rolling(63, min_periods=21).std()
    return out.diff().diff()


def f46_socd_128_cum_bear_body_magnitude_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    b = (open - close).clip(lower=0)
    out = b.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_129_cum_bull_body_magnitude_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    b = (close - open).clip(lower=0)
    out = b.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f46_socd_130_bear_over_bull_body_ratio_21d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    bear = (open - close).clip(lower=0).rolling(21, min_periods=7).sum()
    bull = (close - open).clip(lower=0).rolling(21, min_periods=7).sum()
    out = _safe_div(bear, bull)
    return out.diff().diff()


def f46_socd_131_consec_bearish_close_streak_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    b = (close < open).astype(int).where(close.notna() & open.notna(), 0)
    block = (b != b.shift(1)).fillna(False).cumsum()
    st = b.groupby(block).cumcount().astype(float)
    out = (st * (b > 0)).where(close.notna(), np.nan)
    return out.diff().diff()


def f46_socd_132_consec_bullish_close_streak_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    b = (close > open).astype(int).where(close.notna() & open.notna(), 0)
    block = (b != b.shift(1)).fillna(False).cumsum()
    st = b.groupby(block).cumcount().astype(float)
    out = (st * (b > 0)).where(close.notna(), np.nan)
    return out.diff().diff()


def f46_socd_133_strong_bear_day_rate_63d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (open - close).clip(lower=0)
    rng = high - low
    large = (_safe_div(body, rng) > 0.6).astype(float)
    at_low = (close <= low * 1.005).astype(float)
    out = (large * at_low).where(rng.notna(), np.nan).rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f46_socd_134_strong_bull_day_rate_63d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).clip(lower=0)
    rng = high - low
    large = (_safe_div(body, rng) > 0.6).astype(float)
    at_high = (close >= high * 0.995).astype(float)
    out = (large * at_high).where(rng.notna(), np.nan).rolling(63, min_periods=21).mean()
    return out.diff().diff()


def f46_socd_135_strong_bear_minus_strong_bull_rate_63d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (open - close).clip(lower=0)
    rng = high - low
    large_b = (_safe_div(body, rng) > 0.6).astype(float)
    at_low = (close <= low * 1.005).astype(float)
    sb = (large_b * at_low).where(rng.notna(), np.nan).rolling(63, min_periods=21).mean()
    body_u = (close - open).clip(lower=0)
    large_u = (_safe_div(body_u, rng) > 0.6).astype(float)
    at_high = (close >= high * 0.995).astype(float)
    ss = (large_u * at_high).where(rng.notna(), np.nan).rolling(63, min_periods=21).mean()
    out = sb - ss
    return out.diff().diff()


def f46_socd_136_distribution_day_at_252d_high_composite_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    bear = (close < open).astype(float)
    dd = (g_up * bear).where(close.shift(1).notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (dd * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_137_three_plus_dist_days_21d_at_high_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    bear = (close < open).astype(float)
    dd = (g_up * bear).where(close.shift(1).notna(), np.nan)
    cnt = dd.rolling(21, min_periods=7).sum()
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = ((cnt >= 3).astype(float) * at_high).where(cnt.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_138_gap_up_faded_at_252d_high_composite_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    fade = (close < open).astype(float)
    f = (g_up * fade).where(close.shift(1).notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (f * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_139_unfilled_gap_up_at_high_composite_d2(open: pd.Series, low: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    held = (low > close.shift(1)).astype(float)
    u = (g_up * held).where(close.shift(1).notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (u * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_140_shooting_star_at_high_composite_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs()
    rng = high - low
    ub = pd.concat([open, close], axis=1).max(axis=1)
    uw = high - ub
    ss = ((_safe_div(body, rng) < 0.3) & (uw > 2.0 * body) & (close < open)).astype(float).where(rng.notna() & body.notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (ss * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_141_doji_at_252d_high_composite_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs()
    rng = high - low
    do = (_safe_div(body, rng) < 0.1).astype(float).where(rng.notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (do * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_142_long_upper_wick_at_252d_high_composite_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ub = pd.concat([open, close], axis=1).max(axis=1)
    uw = high - ub
    body = (close - open).abs()
    long = (uw > 2.0 * body).astype(float).where(body.notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (long * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_143_close_at_low_at_252d_high_composite_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    at_lo = (close <= low * 1.005).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (at_lo * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_144_strong_open_weak_close_at_high_composite_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    op = _safe_div(open - low, high - low)
    cl = _safe_div(close - low, high - low)
    sw = ((op > 0.8) & (cl < 0.2)).astype(float).where(op.notna() & cl.notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (sw * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_145_multi_bear_at_top_composite_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    at_lo = (close <= low * 1.005).astype(float)
    ub = pd.concat([open, close], axis=1).max(axis=1)
    uw = high - ub
    body = (close - open).abs()
    long_uw = (uw > 2.0 * body).astype(float).where(body.notna(), np.nan)
    g_up = (open > close.shift(1) * 1.005).astype(float)
    fade = (close < open).astype(float)
    gfa = (g_up * fade)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = ((at_lo + long_uw + gfa) * at_high).where(rmax.notna() & body.notna(), np.nan)
    return out.diff().diff()


def f46_socd_146_consec_3plus_bear_close_at_high_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    b = (close < open).astype(int).where(close.notna() & open.notna(), 0)
    block = (b != b.shift(1)).fillna(False).cumsum()
    st = b.groupby(block).cumcount().astype(float)
    long_streak = ((st * (b > 0)) >= 3).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (long_streak * at_high).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_147_gap_down_after_close_at_high_d2(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    at_hi_prior = (close.shift(1) >= high.shift(1) * 0.999).astype(float)
    g_dn = (open < close.shift(1) * 0.99).astype(float)
    out = (at_hi_prior * g_dn).where(close.shift(1).notna() & high.shift(1).notna(), np.nan)
    return out.diff().diff()


def f46_socd_148_dist_day_rate_top_quintile_63d_in_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    bear = (close < open).astype(float)
    dd = (g_up * bear).where(close.shift(1).notna(), np.nan)
    rate = dd.rolling(63, min_periods=21).mean()
    rk = _rolling_pct_rank(rate, 252, min_periods=84)
    out = (rk > 0.8).astype(float).where(rk.notna(), np.nan)
    return out.diff().diff()


def f46_socd_149_min_close_pos_below_005_at_high_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    mn = p.rolling(63, min_periods=21).min()
    wk = (mn < 0.05).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (wk * at_high).where(mn.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f46_socd_150_comp_ultimate_session_distribution_at_high_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    bear = (close < open).astype(float)
    dd = (g_up * bear).where(close.shift(1).notna(), np.nan)
    at_lo = (close <= low * 1.005).astype(float)
    ub = pd.concat([open, close], axis=1).max(axis=1)
    uw = high - ub
    body = (close - open).abs()
    long_uw = (uw > 2.0 * body).astype(float).where(body.notna(), np.nan)
    op = _safe_div(open - low, high - low)
    cl = _safe_div(close - low, high - low)
    sw = ((op > 0.8) & (cl < 0.2)).astype(float).where(op.notna() & cl.notna(), np.nan)
    star_body = (close - open).abs()
    star_rng = high - low
    ss = ((_safe_div(star_body, star_rng) < 0.3) & (uw > 2.0 * star_body) & (close < open)).astype(float).where(star_rng.notna() & star_body.notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = ((dd + at_lo + long_uw + sw + ss) * at_high).where(rmax.notna() & body.notna(), np.nan)
    return out.diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d2)
# ============================================================

SESSION_OPEN_CLOSE_DYNAMICS_D2_REGISTRY_076_150 = {
    "f46_socd_076_body_share_of_range_1d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_076_body_share_of_range_1d_d2},
    "f46_socd_077_body_share_of_range_21d_mean_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_077_body_share_of_range_21d_mean_d2},
    "f46_socd_078_body_share_of_range_63d_mean_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_078_body_share_of_range_63d_mean_d2},
    "f46_socd_079_abs_body_share_of_range_1d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_079_abs_body_share_of_range_1d_d2},
    "f46_socd_080_intraday_log_return_1d_d2": {"inputs": ["open", "close"], "func": f46_socd_080_intraday_log_return_1d_d2},
    "f46_socd_081_cum_intraday_log_return_21d_d2": {"inputs": ["open", "close"], "func": f46_socd_081_cum_intraday_log_return_21d_d2},
    "f46_socd_082_cum_intraday_log_return_63d_d2": {"inputs": ["open", "close"], "func": f46_socd_082_cum_intraday_log_return_63d_d2},
    "f46_socd_083_intraday_minus_overnight_drift_63d_d2": {"inputs": ["open", "close"], "func": f46_socd_083_intraday_minus_overnight_drift_63d_d2},
    "f46_socd_084_intraday_log_return_std_63d_d2": {"inputs": ["open", "close"], "func": f46_socd_084_intraday_log_return_std_63d_d2},
    "f46_socd_085_overnight_log_return_std_63d_d2": {"inputs": ["open", "close"], "func": f46_socd_085_overnight_log_return_std_63d_d2},
    "f46_socd_086_intraday_over_overnight_vol_ratio_63d_d2": {"inputs": ["open", "close"], "func": f46_socd_086_intraday_over_overnight_vol_ratio_63d_d2},
    "f46_socd_087_bullish_body_count_21d_d2": {"inputs": ["open", "close"], "func": f46_socd_087_bullish_body_count_21d_d2},
    "f46_socd_088_bearish_body_count_21d_d2": {"inputs": ["open", "close"], "func": f46_socd_088_bearish_body_count_21d_d2},
    "f46_socd_089_bull_minus_bear_body_count_63d_d2": {"inputs": ["open", "close"], "func": f46_socd_089_bull_minus_bear_body_count_63d_d2},
    "f46_socd_090_mean_abs_body_pct_close_21d_d2": {"inputs": ["open", "close"], "func": f46_socd_090_mean_abs_body_pct_close_21d_d2},
    "f46_socd_091_upper_wick_1d_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_091_upper_wick_1d_d2},
    "f46_socd_092_lower_wick_1d_d2": {"inputs": ["open", "low", "close"], "func": f46_socd_092_lower_wick_1d_d2},
    "f46_socd_093_upper_wick_share_of_range_1d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_093_upper_wick_share_of_range_1d_d2},
    "f46_socd_094_lower_wick_share_of_range_1d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_094_lower_wick_share_of_range_1d_d2},
    "f46_socd_095_long_upper_wick_indicator_1d_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_095_long_upper_wick_indicator_1d_d2},
    "f46_socd_096_long_lower_wick_indicator_1d_d2": {"inputs": ["open", "low", "close"], "func": f46_socd_096_long_lower_wick_indicator_1d_d2},
    "f46_socd_097_doji_indicator_1d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_097_doji_indicator_1d_d2},
    "f46_socd_098_shooting_star_indicator_1d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_098_shooting_star_indicator_1d_d2},
    "f46_socd_099_hammer_indicator_1d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_099_hammer_indicator_1d_d2},
    "f46_socd_100_shooting_star_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_100_shooting_star_count_63d_d2},
    "f46_socd_101_doji_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_101_doji_count_63d_d2},
    "f46_socd_102_mean_upper_wick_pct_range_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_102_mean_upper_wick_pct_range_21d_d2},
    "f46_socd_103_mean_lower_wick_pct_range_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_103_mean_lower_wick_pct_range_21d_d2},
    "f46_socd_104_upper_minus_lower_wick_pct_range_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_104_upper_minus_lower_wick_pct_range_21d_d2},
    "f46_socd_105_upper_wick_dominance_regime_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_105_upper_wick_dominance_regime_indicator_d2},
    "f46_socd_106_gap_up_bear_close_distribution_indicator_d2": {"inputs": ["open", "close"], "func": f46_socd_106_gap_up_bear_close_distribution_indicator_d2},
    "f46_socd_107_gap_up_bear_count_21d_d2": {"inputs": ["open", "close"], "func": f46_socd_107_gap_up_bear_count_21d_d2},
    "f46_socd_108_gap_up_bear_count_63d_d2": {"inputs": ["open", "close"], "func": f46_socd_108_gap_up_bear_count_63d_d2},
    "f46_socd_109_open_above_prior_high_bear_close_1d_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_109_open_above_prior_high_bear_close_1d_d2},
    "f46_socd_110_open_above_prior_high_bear_close_count_21d_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_110_open_above_prior_high_bear_close_count_21d_d2},
    "f46_socd_111_open_below_prior_low_bull_close_1d_d2": {"inputs": ["open", "low", "close"], "func": f46_socd_111_open_below_prior_low_bull_close_1d_d2},
    "f46_socd_112_strong_open_weak_close_1d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_112_strong_open_weak_close_1d_d2},
    "f46_socd_113_strong_open_weak_close_count_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_113_strong_open_weak_close_count_21d_d2},
    "f46_socd_114_weak_open_strong_close_count_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_114_weak_open_strong_close_count_21d_d2},
    "f46_socd_115_strong_open_weak_close_minus_inverse_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_115_strong_open_weak_close_minus_inverse_63d_d2},
    "f46_socd_116_close_eq_low_indicator_1d_d2": {"inputs": ["low", "close"], "func": f46_socd_116_close_eq_low_indicator_1d_d2},
    "f46_socd_117_close_eq_high_indicator_1d_d2": {"inputs": ["high", "close"], "func": f46_socd_117_close_eq_high_indicator_1d_d2},
    "f46_socd_118_close_eq_low_count_21d_d2": {"inputs": ["low", "close"], "func": f46_socd_118_close_eq_low_count_21d_d2},
    "f46_socd_119_close_eq_high_count_21d_d2": {"inputs": ["high", "close"], "func": f46_socd_119_close_eq_high_count_21d_d2},
    "f46_socd_120_close_at_low_minus_high_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f46_socd_120_close_at_low_minus_high_count_63d_d2},
    "f46_socd_121_distribution_score_21d_gap_d2": {"inputs": ["open", "close"], "func": f46_socd_121_distribution_score_21d_gap_d2},
    "f46_socd_122_distribution_score_63d_gap_d2": {"inputs": ["open", "close"], "func": f46_socd_122_distribution_score_63d_gap_d2},
    "f46_socd_123_min_close_pos_in_63d_d2": {"inputs": ["high", "low", "close"], "func": f46_socd_123_min_close_pos_in_63d_d2},
    "f46_socd_124_max_close_pos_in_63d_d2": {"inputs": ["high", "low", "close"], "func": f46_socd_124_max_close_pos_in_63d_d2},
    "f46_socd_125_close_pos_range_63d_d2": {"inputs": ["high", "low", "close"], "func": f46_socd_125_close_pos_range_63d_d2},
    "f46_socd_126_intraday_range_pct_close_63d_mean_d2": {"inputs": ["high", "low", "close"], "func": f46_socd_126_intraday_range_pct_close_63d_mean_d2},
    "f46_socd_127_body_share_of_range_std_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_127_body_share_of_range_std_63d_d2},
    "f46_socd_128_cum_bear_body_magnitude_21d_d2": {"inputs": ["open", "close"], "func": f46_socd_128_cum_bear_body_magnitude_21d_d2},
    "f46_socd_129_cum_bull_body_magnitude_21d_d2": {"inputs": ["open", "close"], "func": f46_socd_129_cum_bull_body_magnitude_21d_d2},
    "f46_socd_130_bear_over_bull_body_ratio_21d_d2": {"inputs": ["open", "close"], "func": f46_socd_130_bear_over_bull_body_ratio_21d_d2},
    "f46_socd_131_consec_bearish_close_streak_d2": {"inputs": ["open", "close"], "func": f46_socd_131_consec_bearish_close_streak_d2},
    "f46_socd_132_consec_bullish_close_streak_d2": {"inputs": ["open", "close"], "func": f46_socd_132_consec_bullish_close_streak_d2},
    "f46_socd_133_strong_bear_day_rate_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_133_strong_bear_day_rate_63d_d2},
    "f46_socd_134_strong_bull_day_rate_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_134_strong_bull_day_rate_63d_d2},
    "f46_socd_135_strong_bear_minus_strong_bull_rate_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_135_strong_bear_minus_strong_bull_rate_63d_d2},
    "f46_socd_136_distribution_day_at_252d_high_composite_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_136_distribution_day_at_252d_high_composite_d2},
    "f46_socd_137_three_plus_dist_days_21d_at_high_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_137_three_plus_dist_days_21d_at_high_d2},
    "f46_socd_138_gap_up_faded_at_252d_high_composite_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_138_gap_up_faded_at_252d_high_composite_d2},
    "f46_socd_139_unfilled_gap_up_at_high_composite_d2": {"inputs": ["open", "low", "high", "close"], "func": f46_socd_139_unfilled_gap_up_at_high_composite_d2},
    "f46_socd_140_shooting_star_at_high_composite_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_140_shooting_star_at_high_composite_d2},
    "f46_socd_141_doji_at_252d_high_composite_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_141_doji_at_252d_high_composite_d2},
    "f46_socd_142_long_upper_wick_at_252d_high_composite_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_142_long_upper_wick_at_252d_high_composite_d2},
    "f46_socd_143_close_at_low_at_252d_high_composite_d2": {"inputs": ["high", "low", "close"], "func": f46_socd_143_close_at_low_at_252d_high_composite_d2},
    "f46_socd_144_strong_open_weak_close_at_high_composite_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_144_strong_open_weak_close_at_high_composite_d2},
    "f46_socd_145_multi_bear_at_top_composite_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_145_multi_bear_at_top_composite_d2},
    "f46_socd_146_consec_3plus_bear_close_at_high_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_146_consec_3plus_bear_close_at_high_d2},
    "f46_socd_147_gap_down_after_close_at_high_d2": {"inputs": ["open", "high", "close"], "func": f46_socd_147_gap_down_after_close_at_high_d2},
    "f46_socd_148_dist_day_rate_top_quintile_63d_in_252d_d2": {"inputs": ["open", "close"], "func": f46_socd_148_dist_day_rate_top_quintile_63d_in_252d_d2},
    "f46_socd_149_min_close_pos_below_005_at_high_63d_d2": {"inputs": ["high", "low", "close"], "func": f46_socd_149_min_close_pos_below_005_at_high_63d_d2},
    "f46_socd_150_comp_ultimate_session_distribution_at_high_d2": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_150_comp_ultimate_session_distribution_at_high_d2},
}
