"""session_open_close_dynamics d3 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d3__076_150.py. Each
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


def f46_socd_001_overnight_log_gap_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_log(open) - _safe_log(close.shift(1))
    return out.diff().diff().diff()


def f46_socd_002_overnight_gap_atr_norm_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    g = open - close.shift(1)
    out = _safe_div(g, _atr(high, low, close, n=21))
    return out.diff().diff().diff()


def f46_socd_003_gap_up_1pct_indicator_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = (g > 0.01).astype(float).where(g.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_004_gap_down_1pct_indicator_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = (g < -0.01).astype(float).where(g.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_005_abs_overnight_gap_atr_5d_mean_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    g = open - close.shift(1)
    ag = _safe_div(g.abs(), _atr(high, low, close, n=21))
    out = ag.rolling(5, min_periods=2).mean()
    return out.diff().diff().diff()


def f46_socd_006_overnight_gap_21d_mean_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f46_socd_007_overnight_gap_63d_mean_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f46_socd_008_cum_pos_overnight_gap_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.clip(lower=0).rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_009_cum_neg_overnight_gap_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.clip(upper=0).rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_010_net_overnight_gap_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = (g.clip(lower=0) - g.clip(upper=0).abs()).rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_011_overnight_gap_std_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.rolling(21, min_periods=7).std()
    return out.diff().diff().diff()


def f46_socd_012_overnight_gap_std_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.rolling(63, min_periods=21).std()
    return out.diff().diff().diff()


def f46_socd_013_overnight_gap_zscore_1d_in_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = _rolling_zscore(g, 63, min_periods=21)
    return out.diff().diff().diff()


def f46_socd_014_overnight_gap_zscore_1d_in_252d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = _rolling_zscore(g, 252, min_periods=84)
    return out.diff().diff().diff()


def f46_socd_015_abs_overnight_gap_pct_rank_252d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    out = _rolling_pct_rank(g, 252, min_periods=84)
    return out.diff().diff().diff()


def f46_socd_016_close_pos_in_1d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div(close - low, high - low)
    return out.diff().diff().diff()


def f46_socd_017_close_pos_21d_mean_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = p.rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f46_socd_018_close_pos_63d_mean_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = p.rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f46_socd_019_close_pos_252d_mean_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = p.rolling(252, min_periods=84).mean()
    return out.diff().diff().diff()


def f46_socd_020_close_in_top_quintile_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = (p > 0.8).astype(float).where(p.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_021_close_in_bottom_quintile_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = (p < 0.2).astype(float).where(p.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_022_frac_close_top_quintile_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    t = (p > 0.8).astype(float).where(p.notna(), np.nan)
    out = t.rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f46_socd_023_frac_close_top_quintile_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    t = (p > 0.8).astype(float).where(p.notna(), np.nan)
    out = t.rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f46_socd_024_frac_close_bottom_quintile_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    b = (p < 0.2).astype(float).where(p.notna(), np.nan)
    out = b.rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f46_socd_025_top_minus_bottom_quintile_frac_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    t = (p > 0.8).astype(float).where(p.notna(), np.nan).rolling(63, min_periods=21).mean()
    b = (p < 0.2).astype(float).where(p.notna(), np.nan).rolling(63, min_periods=21).mean()
    out = t - b
    return out.diff().diff().diff()


def f46_socd_026_close_dist_below_high_pct_range_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div(high - close, high - low)
    return out.diff().diff().diff()


def f46_socd_027_close_dist_above_low_pct_range_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div(close - low, high - low)
    return out.diff().diff().diff()


def f46_socd_028_close_pos_centered_atr_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low) - 0.5
    out = p
    return out.diff().diff().diff()


def f46_socd_029_close_pos_slope_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = _rolling_slope(p, 21, min_periods=7)
    return out.diff().diff().diff()


def f46_socd_030_close_pos_21d_mean_pct_rank_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low).rolling(21, min_periods=7).mean()
    out = _rolling_pct_rank(p, 252, min_periods=84)
    return out.diff().diff().diff()


def f46_socd_031_gap_up_bear_close_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1)).astype(float)
    bear = (close < open).astype(float)
    out = (g_up * bear).where(g_up.notna() & bear.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_032_gap_down_bull_close_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g_dn = (open < close.shift(1)).astype(float)
    bull = (close > open).astype(float)
    out = (g_dn * bull).where(g_dn.notna() & bull.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_033_outside_bear_reversal_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out_d = ((high > high.shift(1)) & (low < low.shift(1)) & (close < open)).astype(float).where(high.shift(1).notna() & low.shift(1).notna(), np.nan)
    out = out_d
    return out.diff().diff().diff()


def f46_socd_034_outside_bull_reversal_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out_d = ((high > high.shift(1)) & (low < low.shift(1)) & (close > open)).astype(float).where(high.shift(1).notna() & low.shift(1).notna(), np.nan)
    out = out_d
    return out.diff().diff().diff()


def f46_socd_035_strong_bearish_intraday_reversal_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (open - close).abs()
    rng = high - low
    strong = ((_safe_div(body, rng) > 0.7) & (close < open)).astype(float)
    out = strong.where(rng.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_036_bearish_intraday_reversal_count_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    rev = ((open > close.shift(1)) & (close < open)).astype(float).where(open.notna() & close.notna() & close.shift(1).notna(), np.nan)
    out = rev.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_037_bearish_intraday_reversal_count_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    rev = ((open > close.shift(1)) & (close < open)).astype(float).where(open.notna() & close.notna() & close.shift(1).notna(), np.nan)
    out = rev.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f46_socd_038_bullish_intraday_reversal_count_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    rev = ((open < close.shift(1)) & (close > open)).astype(float).where(open.notna() & close.notna() & close.shift(1).notna(), np.nan)
    out = rev.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f46_socd_039_bear_minus_bull_reversal_count_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    br = ((open > close.shift(1)) & (close < open)).astype(float)
    bu = ((open < close.shift(1)) & (close > open)).astype(float)
    out = br.rolling(63, min_periods=21).sum() - bu.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f46_socd_040_intraday_range_pct_close_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div(high - low, close)
    return out.diff().diff().diff()


def f46_socd_041_large_range_bull_day_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    atr = _atr(high, low, close, n=21)
    big = (rng > 2.0 * atr).astype(float)
    bull = (close > close.shift(1)).astype(float)
    out = (big * bull).where(atr.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_042_large_range_bear_day_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    atr = _atr(high, low, close, n=21)
    big = (rng > 2.0 * atr).astype(float)
    bear = (close < close.shift(1)).astype(float)
    out = (big * bear).where(atr.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_043_narrow_range_day_half_atr_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    atr = _atr(high, low, close, n=21)
    out = (rng < 0.5 * atr).astype(float).where(atr.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_044_narrow_then_large_range_1d_in_5d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    atr = _atr(high, low, close, n=21)
    big_now = (rng > 2.0 * atr).astype(float)
    nar_prior = (rng < 0.5 * atr).astype(float).rolling(5, min_periods=2).max()
    out = (big_now * nar_prior.shift(1)).where(atr.notna() & nar_prior.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_045_high_dist_over_low_dist_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    out = _safe_div(high - close, (close - low).replace(0, np.nan))
    return out.diff().diff().diff()


def f46_socd_046_close_pos_in_5d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(5, min_periods=2).min()
    rmax = high.rolling(5, min_periods=2).max()
    out = _safe_div(close - rmin, rmax - rmin)
    return out.diff().diff().diff()


def f46_socd_047_close_pos_in_21d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(21, min_periods=7).min()
    rmax = high.rolling(21, min_periods=7).max()
    out = _safe_div(close - rmin, rmax - rmin)
    return out.diff().diff().diff()


def f46_socd_048_close_pos_in_63d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(63, min_periods=21).min()
    rmax = high.rolling(63, min_periods=21).max()
    out = _safe_div(close - rmin, rmax - rmin)
    return out.diff().diff().diff()


def f46_socd_049_close_pos_in_252d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(252, min_periods=84).min()
    rmax = high.rolling(252, min_periods=84).max()
    out = _safe_div(close - rmin, rmax - rmin)
    return out.diff().diff().diff()


def f46_socd_050_close_top_decile_252d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(252, min_periods=84).min()
    rmax = high.rolling(252, min_periods=84).max()
    p = _safe_div(close - rmin, rmax - rmin)
    out = (p > 0.9).astype(float).where(p.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_051_close_bottom_decile_252d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(252, min_periods=84).min()
    rmax = high.rolling(252, min_periods=84).max()
    p = _safe_div(close - rmin, rmax - rmin)
    out = (p < 0.1).astype(float).where(p.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_052_frac_close_top_decile_252d_range_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(252, min_periods=84).min()
    rmax = high.rolling(252, min_periods=84).max()
    p = _safe_div(close - rmin, rmax - rmin)
    t = (p > 0.9).astype(float).where(p.notna(), np.nan)
    out = t.rolling(63, min_periods=21).mean()
    return out.diff().diff().diff()


def f46_socd_053_monotonic_close_pos_rise_streak_63d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(63, min_periods=21).min()
    rmax = high.rolling(63, min_periods=21).max()
    p = _safe_div(close - rmin, rmax - rmin)
    rise = (p > p.shift(1)).astype(int).where(p.notna() & p.shift(1).notna(), 0)
    block = (rise != rise.shift(1)).fillna(False).cumsum()
    st = rise.groupby(block).cumcount().astype(float)
    out = (st * (rise > 0)).where(p.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_054_close_pos_63d_range_21d_mean_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(63, min_periods=21).min()
    rmax = high.rolling(63, min_periods=21).max()
    p = _safe_div(close - rmin, rmax - rmin)
    out = p.rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f46_socd_055_close_pos_21_vs_252_diff_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin21 = low.rolling(21, min_periods=7).min(); rmax21 = high.rolling(21, min_periods=7).max()
    rmin252 = low.rolling(252, min_periods=84).min(); rmax252 = high.rolling(252, min_periods=84).max()
    p21 = _safe_div(close - rmin21, rmax21 - rmin21)
    p252 = _safe_div(close - rmin252, rmax252 - rmin252)
    out = p21 - p252
    return out.diff().diff().diff()


def f46_socd_056_frac_close_above_95_252d_range_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(252, min_periods=84).min(); rmax = high.rolling(252, min_periods=84).max()
    p = _safe_div(close - rmin, rmax - rmin)
    t = (p > 0.95).astype(float).where(p.notna(), np.nan)
    out = t.rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f46_socd_057_close_pos_1d_std_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = p.rolling(21, min_periods=7).std()
    return out.diff().diff().diff()


def f46_socd_058_consec_top_quintile_streak_1d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    t = (p > 0.8).astype(int).where(p.notna(), 0)
    block = (t != t.shift(1)).fillna(False).cumsum()
    st = t.groupby(block).cumcount().astype(float)
    out = (st * (t > 0)).where(p.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_059_close_pos_1d_pct_rank_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = _safe_div(close - low, high - low)
    out = _rolling_pct_rank(p, 63, min_periods=21)
    return out.diff().diff().diff()


def f46_socd_060_close_5d_low_at_252d_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin5 = close.rolling(5, min_periods=2).min()
    at_5d_low = (close <= rmin5).astype(float)
    rmax252 = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax252).astype(float)
    out = (at_5d_low * at_high).where(rmax252.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_061_gap_up_1pct_count_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    u = (g > 0.01).astype(float).where(g.notna(), np.nan)
    out = u.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_062_gap_down_1pct_count_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    d = (g < -0.01).astype(float).where(g.notna(), np.nan)
    out = d.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_063_gap_up_minus_down_count_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    u = (g > 0.01).astype(float); d = (g < -0.01).astype(float)
    out = u.rolling(63, min_periods=21).sum() - d.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f46_socd_064_gap_up_fill_indicator_1d_d3(open: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1)).astype(float)
    filled = (low < close.shift(1)).astype(float)
    out = (g_up * filled).where(close.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_065_gap_down_fill_indicator_1d_d3(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    g_dn = (open < close.shift(1)).astype(float)
    filled = (high > close.shift(1)).astype(float)
    out = (g_dn * filled).where(close.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_066_gap_up_unfilled_1d_d3(open: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    held = (low > close.shift(1)).astype(float)
    out = (g_up * held).where(close.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_067_gap_up_unfilled_share_63d_d3(open: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    held = (low > close.shift(1)).astype(float)
    unfilled = (g_up * held)
    total = g_up
    out = _safe_div(unfilled.rolling(63, min_periods=21).sum(), total.rolling(63, min_periods=21).sum())
    return out.diff().diff().diff()


def f46_socd_068_gap_down_unfilled_share_63d_d3(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    g_dn = (open < close.shift(1) * 0.995).astype(float)
    held = (high < close.shift(1)).astype(float)
    unfilled = (g_dn * held)
    total = g_dn
    out = _safe_div(unfilled.rolling(63, min_periods=21).sum(), total.rolling(63, min_periods=21).sum())
    return out.diff().diff().diff()


def f46_socd_069_max_gap_up_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.clip(lower=0).rolling(21, min_periods=7).max()
    return out.diff().diff().diff()


def f46_socd_070_max_gap_down_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.clip(upper=0).rolling(21, min_periods=7).min()
    return out.diff().diff().diff()


def f46_socd_071_fade_gap_up_indicator_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    fade = (close < open).astype(float)
    out = (g_up * fade).where(close.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_072_fade_gap_down_indicator_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g_dn = (open < close.shift(1) * 0.995).astype(float)
    fade = (close > open).astype(float)
    out = (g_dn * fade).where(close.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_073_fade_gap_up_share_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g_up = (open > close.shift(1) * 1.005).astype(float)
    fade = (close < open).astype(float)
    faded = (g_up * fade)
    total = g_up
    out = _safe_div(faded.rolling(63, min_periods=21).sum(), total.rolling(63, min_periods=21).sum())
    return out.diff().diff().diff()


def f46_socd_074_net_signed_gap_magnitude_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open) - _safe_log(close.shift(1))
    out = g.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_075_gap_over_bar_range_21d_mean_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    g = open - close.shift(1)
    rng = high - low
    out = _safe_div(g.abs(), rng).rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d3)
# ============================================================

SESSION_OPEN_CLOSE_DYNAMICS_D3_REGISTRY_001_075 = {
    "f46_socd_001_overnight_log_gap_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_001_overnight_log_gap_1d_d3},
    "f46_socd_002_overnight_gap_atr_norm_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_002_overnight_gap_atr_norm_1d_d3},
    "f46_socd_003_gap_up_1pct_indicator_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_003_gap_up_1pct_indicator_1d_d3},
    "f46_socd_004_gap_down_1pct_indicator_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_004_gap_down_1pct_indicator_1d_d3},
    "f46_socd_005_abs_overnight_gap_atr_5d_mean_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_005_abs_overnight_gap_atr_5d_mean_d3},
    "f46_socd_006_overnight_gap_21d_mean_d3": {"inputs": ["open", "close"], "func": f46_socd_006_overnight_gap_21d_mean_d3},
    "f46_socd_007_overnight_gap_63d_mean_d3": {"inputs": ["open", "close"], "func": f46_socd_007_overnight_gap_63d_mean_d3},
    "f46_socd_008_cum_pos_overnight_gap_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_008_cum_pos_overnight_gap_21d_d3},
    "f46_socd_009_cum_neg_overnight_gap_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_009_cum_neg_overnight_gap_21d_d3},
    "f46_socd_010_net_overnight_gap_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_010_net_overnight_gap_21d_d3},
    "f46_socd_011_overnight_gap_std_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_011_overnight_gap_std_21d_d3},
    "f46_socd_012_overnight_gap_std_63d_d3": {"inputs": ["open", "close"], "func": f46_socd_012_overnight_gap_std_63d_d3},
    "f46_socd_013_overnight_gap_zscore_1d_in_63d_d3": {"inputs": ["open", "close"], "func": f46_socd_013_overnight_gap_zscore_1d_in_63d_d3},
    "f46_socd_014_overnight_gap_zscore_1d_in_252d_d3": {"inputs": ["open", "close"], "func": f46_socd_014_overnight_gap_zscore_1d_in_252d_d3},
    "f46_socd_015_abs_overnight_gap_pct_rank_252d_d3": {"inputs": ["open", "close"], "func": f46_socd_015_abs_overnight_gap_pct_rank_252d_d3},
    "f46_socd_016_close_pos_in_1d_range_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_016_close_pos_in_1d_range_d3},
    "f46_socd_017_close_pos_21d_mean_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_017_close_pos_21d_mean_d3},
    "f46_socd_018_close_pos_63d_mean_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_018_close_pos_63d_mean_d3},
    "f46_socd_019_close_pos_252d_mean_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_019_close_pos_252d_mean_d3},
    "f46_socd_020_close_in_top_quintile_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_020_close_in_top_quintile_1d_d3},
    "f46_socd_021_close_in_bottom_quintile_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_021_close_in_bottom_quintile_1d_d3},
    "f46_socd_022_frac_close_top_quintile_21d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_022_frac_close_top_quintile_21d_d3},
    "f46_socd_023_frac_close_top_quintile_63d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_023_frac_close_top_quintile_63d_d3},
    "f46_socd_024_frac_close_bottom_quintile_63d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_024_frac_close_bottom_quintile_63d_d3},
    "f46_socd_025_top_minus_bottom_quintile_frac_63d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_025_top_minus_bottom_quintile_frac_63d_d3},
    "f46_socd_026_close_dist_below_high_pct_range_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_026_close_dist_below_high_pct_range_1d_d3},
    "f46_socd_027_close_dist_above_low_pct_range_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_027_close_dist_above_low_pct_range_1d_d3},
    "f46_socd_028_close_pos_centered_atr_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_028_close_pos_centered_atr_1d_d3},
    "f46_socd_029_close_pos_slope_21d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_029_close_pos_slope_21d_d3},
    "f46_socd_030_close_pos_21d_mean_pct_rank_252d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_030_close_pos_21d_mean_pct_rank_252d_d3},
    "f46_socd_031_gap_up_bear_close_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_031_gap_up_bear_close_1d_d3},
    "f46_socd_032_gap_down_bull_close_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_032_gap_down_bull_close_1d_d3},
    "f46_socd_033_outside_bear_reversal_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_033_outside_bear_reversal_1d_d3},
    "f46_socd_034_outside_bull_reversal_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_034_outside_bull_reversal_1d_d3},
    "f46_socd_035_strong_bearish_intraday_reversal_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_035_strong_bearish_intraday_reversal_1d_d3},
    "f46_socd_036_bearish_intraday_reversal_count_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_036_bearish_intraday_reversal_count_21d_d3},
    "f46_socd_037_bearish_intraday_reversal_count_63d_d3": {"inputs": ["open", "close"], "func": f46_socd_037_bearish_intraday_reversal_count_63d_d3},
    "f46_socd_038_bullish_intraday_reversal_count_63d_d3": {"inputs": ["open", "close"], "func": f46_socd_038_bullish_intraday_reversal_count_63d_d3},
    "f46_socd_039_bear_minus_bull_reversal_count_63d_d3": {"inputs": ["open", "close"], "func": f46_socd_039_bear_minus_bull_reversal_count_63d_d3},
    "f46_socd_040_intraday_range_pct_close_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_040_intraday_range_pct_close_1d_d3},
    "f46_socd_041_large_range_bull_day_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_041_large_range_bull_day_1d_d3},
    "f46_socd_042_large_range_bear_day_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_042_large_range_bear_day_1d_d3},
    "f46_socd_043_narrow_range_day_half_atr_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_043_narrow_range_day_half_atr_1d_d3},
    "f46_socd_044_narrow_then_large_range_1d_in_5d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_044_narrow_then_large_range_1d_in_5d_d3},
    "f46_socd_045_high_dist_over_low_dist_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_045_high_dist_over_low_dist_1d_d3},
    "f46_socd_046_close_pos_in_5d_range_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_046_close_pos_in_5d_range_d3},
    "f46_socd_047_close_pos_in_21d_range_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_047_close_pos_in_21d_range_d3},
    "f46_socd_048_close_pos_in_63d_range_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_048_close_pos_in_63d_range_d3},
    "f46_socd_049_close_pos_in_252d_range_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_049_close_pos_in_252d_range_d3},
    "f46_socd_050_close_top_decile_252d_range_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_050_close_top_decile_252d_range_d3},
    "f46_socd_051_close_bottom_decile_252d_range_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_051_close_bottom_decile_252d_range_d3},
    "f46_socd_052_frac_close_top_decile_252d_range_63d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_052_frac_close_top_decile_252d_range_63d_d3},
    "f46_socd_053_monotonic_close_pos_rise_streak_63d_range_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_053_monotonic_close_pos_rise_streak_63d_range_d3},
    "f46_socd_054_close_pos_63d_range_21d_mean_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_054_close_pos_63d_range_21d_mean_d3},
    "f46_socd_055_close_pos_21_vs_252_diff_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_055_close_pos_21_vs_252_diff_d3},
    "f46_socd_056_frac_close_above_95_252d_range_21d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_056_frac_close_above_95_252d_range_21d_d3},
    "f46_socd_057_close_pos_1d_std_21d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_057_close_pos_1d_std_21d_d3},
    "f46_socd_058_consec_top_quintile_streak_1d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_058_consec_top_quintile_streak_1d_d3},
    "f46_socd_059_close_pos_1d_pct_rank_63d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_059_close_pos_1d_pct_rank_63d_d3},
    "f46_socd_060_close_5d_low_at_252d_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_060_close_5d_low_at_252d_high_indicator_d3},
    "f46_socd_061_gap_up_1pct_count_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_061_gap_up_1pct_count_21d_d3},
    "f46_socd_062_gap_down_1pct_count_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_062_gap_down_1pct_count_21d_d3},
    "f46_socd_063_gap_up_minus_down_count_63d_d3": {"inputs": ["open", "close"], "func": f46_socd_063_gap_up_minus_down_count_63d_d3},
    "f46_socd_064_gap_up_fill_indicator_1d_d3": {"inputs": ["open", "low", "close"], "func": f46_socd_064_gap_up_fill_indicator_1d_d3},
    "f46_socd_065_gap_down_fill_indicator_1d_d3": {"inputs": ["open", "high", "close"], "func": f46_socd_065_gap_down_fill_indicator_1d_d3},
    "f46_socd_066_gap_up_unfilled_1d_d3": {"inputs": ["open", "low", "close"], "func": f46_socd_066_gap_up_unfilled_1d_d3},
    "f46_socd_067_gap_up_unfilled_share_63d_d3": {"inputs": ["open", "low", "close"], "func": f46_socd_067_gap_up_unfilled_share_63d_d3},
    "f46_socd_068_gap_down_unfilled_share_63d_d3": {"inputs": ["open", "high", "close"], "func": f46_socd_068_gap_down_unfilled_share_63d_d3},
    "f46_socd_069_max_gap_up_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_069_max_gap_up_21d_d3},
    "f46_socd_070_max_gap_down_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_070_max_gap_down_21d_d3},
    "f46_socd_071_fade_gap_up_indicator_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_071_fade_gap_up_indicator_1d_d3},
    "f46_socd_072_fade_gap_down_indicator_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_072_fade_gap_down_indicator_1d_d3},
    "f46_socd_073_fade_gap_up_share_63d_d3": {"inputs": ["open", "close"], "func": f46_socd_073_fade_gap_up_share_63d_d3},
    "f46_socd_074_net_signed_gap_magnitude_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_074_net_signed_gap_magnitude_21d_d3},
    "f46_socd_075_gap_over_bar_range_21d_mean_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_075_gap_over_bar_range_21d_mean_d3},
}
