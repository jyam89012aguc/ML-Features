"""turnover_and_churn d3 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py.
Bucket A: Turnover-proxy levels (volume normalized by trailing baselines).
Bucket B: Wide-range bar identification.
Bucket C: Wide-range bar frequency / dwell.
Bucket D: Churning bars (high vol + low return).
Bucket E: Volume z-scores and percentile ranks.
Bucket F: Range expansion vs contraction.
Bucket G: Inside / outside bar dynamics.
Bucket H: Gap & range relations.

Inputs: SEP OHLCV. Self-contained helpers, PIT-clean (right-anchored rolling,
explicit min_periods, no centered windows, no .shift(N)).
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


# ============================================================
# Bucket A — Turnover-proxy levels (001-008)
# ============================================================


def f24_tnch_001_volume_over_avg_21_d3(volume: pd.Series) -> pd.Series:
    """Volume relative to 21d avg — monthly turnover ratio."""
    return (_safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())).diff().diff().diff()


def f24_tnch_002_volume_over_avg_63_d3(volume: pd.Series) -> pd.Series:
    """Volume relative to 63d avg — quarterly turnover ratio."""
    return (_safe_div(volume, volume.rolling(QDAYS, min_periods=MDAYS).mean())).diff().diff().diff()


def f24_tnch_003_volume_over_avg_252_d3(volume: pd.Series) -> pd.Series:
    """Volume relative to 252d avg — annual turnover ratio."""
    return (_safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())).diff().diff().diff()


def f24_tnch_004_volume_over_avg_504_d3(volume: pd.Series) -> pd.Series:
    """Volume relative to 504d avg — multi-year baseline turnover."""
    return (_safe_div(volume, volume.rolling(DDAYS_2Y, min_periods=YDAYS).mean())).diff().diff().diff()


def f24_tnch_005_log_volume_over_median_21_d3(volume: pd.Series) -> pd.Series:
    """log(vol / 21d median vol) — robust monthly turnover deviation."""
    return (_safe_log(_safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).median()))).diff().diff().diff()


def f24_tnch_006_log_volume_over_median_63_d3(volume: pd.Series) -> pd.Series:
    """log(vol / 63d median vol) — robust quarterly turnover deviation."""
    return (_safe_log(_safe_div(volume, volume.rolling(QDAYS, min_periods=MDAYS).median()))).diff().diff().diff()


def f24_tnch_007_log_volume_over_median_252_d3(volume: pd.Series) -> pd.Series:
    """log(vol / 252d median vol) — robust annual turnover deviation."""
    return (_safe_log(_safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).median()))).diff().diff().diff()


def f24_tnch_008_dollar_vol_over_avg_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol relative to its 252d avg — annual dollar-turnover ratio."""
    dv = close * volume
    return (_safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).mean())).diff().diff().diff()


def f24_tnch_009_tr_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """True range relative to 21d ATR — bar-range expansion ratio."""
    return (_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f24_tnch_010_tr_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """True range relative to 63d ATR — quarterly expansion ratio."""
    return (_safe_div(_true_range(high, low, close), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f24_tnch_011_tr_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """True range relative to 252d ATR — annual expansion ratio."""
    return (_safe_div(_true_range(high, low, close), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f24_tnch_012_hl_range_over_avg_21_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """High-low range vs 21d avg range — monthly expansion."""
    r = high - low
    return (_safe_div(r, r.rolling(MDAYS, min_periods=WDAYS).mean())).diff().diff().diff()


def f24_tnch_013_hl_range_over_avg_63_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """High-low range vs 63d avg range — quarterly expansion."""
    r = high - low
    return (_safe_div(r, r.rolling(QDAYS, min_periods=MDAYS).mean())).diff().diff().diff()


def f24_tnch_014_wide_range_bar_flag_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > 2x ATR21 — wide-range bar (classical)."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 2.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_015_extra_wide_bar_flag_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > 3x ATR21 — extra-wide bar (distinct severity)."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 3.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_016_extreme_wide_bar_flag_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > 5x ATR21 — extreme bar (climax-event severity)."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 5.0).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_017_bars_since_last_wide_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent wide-range bar (TR > 2x ATR21)."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return (_bars_since_true(r > 2.0)).diff().diff().diff()


def f24_tnch_018_wide_range_count_21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of wide-range bars (TR > 2x ATR21) in past 21 bars."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 2.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_019_wide_range_count_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of wide-range bars in past 63 bars."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_020_wide_range_count_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of wide-range bars."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_021_extra_wide_count_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of extra-wide bars (TR > 3x ATR21) in past 63 bars."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 3.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_022_extra_wide_count_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of extra-wide bars."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_023_fraction_wide_range_21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 21 bars that are wide-range (TR > 2x ATR21)."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 2.0).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_024_fraction_wide_range_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars that are wide-range."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_025_fraction_wide_range_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual fraction of wide-range bars."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return ((r > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_026_longest_wide_range_run_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest consecutive run of wide-range bars in past 252."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    streak = _streak_true(r > 2.0)
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_027_churn_index_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Churn index = log1p(volume) / (|return| + eps) — high when churning."""
    return (_safe_div(np.log1p(volume), close.pct_change().abs() + 1e-6)).diff().diff().diff()


def f24_tnch_028_churn_bar_flag_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if |return| < 0.5x 21d-avg|return| AND volume > 1.5x 21d avg — churning bar."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = (ar < 0.5 * ar_avg) & (volume > 1.5 * v_avg)
    return (flag.astype(float).where(ar_avg.notna() & v_avg.notna(), np.nan)).diff().diff().diff()


def f24_tnch_029_churn_bar_flag_strict_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stricter churn flag: |ret| < 0.25x avg AND volume > 2.0x avg."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = (ar < 0.25 * ar_avg) & (volume > 2.0 * v_avg)
    return (flag.astype(float).where(ar_avg.notna() & v_avg.notna(), np.nan)).diff().diff().diff()


def f24_tnch_030_churn_count_21_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of churn-bars in past 21."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((ar < 0.5 * ar_avg) & (volume > 1.5 * v_avg)).astype(float)
    return (flag.rolling(MDAYS, min_periods=WDAYS).sum().where(ar_avg.notna() & v_avg.notna(), np.nan)).diff().diff().diff()


def f24_tnch_031_churn_count_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of churn-bars in past 63."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((ar < 0.5 * ar_avg) & (volume > 1.5 * v_avg)).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum().where(ar_avg.notna() & v_avg.notna(), np.nan)).diff().diff().diff()


def f24_tnch_032_churn_count_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of churn-bars."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((ar < 0.5 * ar_avg) & (volume > 1.5 * v_avg)).astype(float)
    return (flag.rolling(YDAYS, min_periods=QDAYS).sum().where(ar_avg.notna() & v_avg.notna(), np.nan)).diff().diff().diff()


def f24_tnch_033_bars_since_last_churn_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent churn-bar."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_bars_since_true((ar < 0.5 * ar_avg) & (volume > 1.5 * v_avg))).diff().diff().diff()


def f24_tnch_034_longest_churn_run_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest consecutive churn-bar run in past 63."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    streak = _streak_true((ar < 0.5 * ar_avg) & (volume > 1.5 * v_avg))
    return (streak.rolling(QDAYS, min_periods=MDAYS).max().where(ar_avg.notna() & v_avg.notna(), np.nan)).diff().diff().diff()


def f24_tnch_035_fraction_churn_21_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 21 bars that are churn-bars."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((ar < 0.5 * ar_avg) & (volume > 1.5 * v_avg)).astype(float)
    return (flag.rolling(MDAYS, min_periods=WDAYS).mean().where(ar_avg.notna() & v_avg.notna(), np.nan)).diff().diff().diff()


def f24_tnch_036_fraction_churn_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars that are churn-bars."""
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((ar < 0.5 * ar_avg) & (volume > 1.5 * v_avg)).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).mean().where(ar_avg.notna() & v_avg.notna(), np.nan)).diff().diff().diff()


def f24_tnch_037_vol_zscore_21_d3(volume: pd.Series) -> pd.Series:
    """Volume z-score vs trailing 21d distribution."""
    return (_rolling_zscore(volume, MDAYS, min_periods=WDAYS)).diff().diff().diff()


def f24_tnch_038_vol_zscore_63_d3(volume: pd.Series) -> pd.Series:
    """Volume z-score vs trailing 63d distribution."""
    return (_rolling_zscore(volume, QDAYS, min_periods=MDAYS)).diff().diff().diff()


def f24_tnch_039_vol_zscore_252_d3(volume: pd.Series) -> pd.Series:
    """Volume z-score vs trailing 252d distribution."""
    return (_rolling_zscore(volume, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f24_tnch_040_vol_pct_rank_63_d3(volume: pd.Series) -> pd.Series:
    """Volume percentile rank vs trailing 63d distribution."""
    return (volume.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)).diff().diff().diff()


def f24_tnch_041_vol_pct_rank_252_d3(volume: pd.Series) -> pd.Series:
    """Volume percentile rank vs trailing 252d distribution."""
    return (volume.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f24_tnch_042_dollar_vol_zscore_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume z-score vs trailing 252d distribution."""
    return (_rolling_zscore(close * volume, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f24_tnch_043_dollar_vol_pct_rank_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume percentile rank vs trailing 252d distribution."""
    return ((close * volume).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f24_tnch_044_vol_above_q95_state_252_d3(volume: pd.Series) -> pd.Series:
    """1 if current volume above its trailing 252d 95th percentile — high-vol state."""
    q = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return ((volume > q).astype(float).where(q.notna(), np.nan)).diff().diff().diff()


def f24_tnch_045_vol_above_q99_state_252_d3(volume: pd.Series) -> pd.Series:
    """1 if current volume above 252d 99th percentile — extreme-vol state."""
    q = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return ((volume > q).astype(float).where(q.notna(), np.nan)).diff().diff().diff()


def f24_tnch_046_bars_since_q99_vol_252_d3(volume: pd.Series) -> pd.Series:
    """Bars since most recent vol > 252d 99th percentile event."""
    q = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return (_bars_since_true(volume > q)).diff().diff().diff()


def f24_tnch_047_range_ratio_5_over_21_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """5d avg HL range / 21d avg HL range — recent expansion vs monthly."""
    r = high - low
    return (_safe_div(r.rolling(WDAYS, min_periods=2).mean(), r.rolling(MDAYS, min_periods=WDAYS).mean())).diff().diff().diff()


def f24_tnch_048_range_ratio_21_over_63_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """21d avg range / 63d avg range — monthly vs quarterly expansion."""
    r = high - low
    return (_safe_div(r.rolling(MDAYS, min_periods=WDAYS).mean(), r.rolling(QDAYS, min_periods=MDAYS).mean())).diff().diff().diff()


def f24_tnch_049_range_ratio_21_over_252_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """21d avg range / 252d avg range — monthly vs annual."""
    r = high - low
    return (_safe_div(r.rolling(MDAYS, min_periods=WDAYS).mean(), r.rolling(YDAYS, min_periods=QDAYS).mean())).diff().diff().diff()


def f24_tnch_050_range_ratio_5max_over_21avg_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Max range in past 5 bars / 21d avg range — short-term extreme expansion."""
    r = high - low
    return (_safe_div(r.rolling(WDAYS, min_periods=2).max(), r.rolling(MDAYS, min_periods=WDAYS).mean())).diff().diff().diff()


def f24_tnch_051_range_expansion_zscore_252_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of HL range vs trailing 252d distribution."""
    return (_rolling_zscore(high - low, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f24_tnch_052_nr4_flag_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if today's range is the smallest of the past 4 bars (NR4 setup)."""
    r = high - low
    rm = r.rolling(4, min_periods=4).min()
    return ((r == rm).astype(float).where(rm.notna(), np.nan)).diff().diff().diff()


def f24_tnch_053_nr7_flag_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if today's range is the smallest of past 7 bars (NR7 — classical compression)."""
    r = high - low
    rm = r.rolling(7, min_periods=7).min()
    return ((r == rm).astype(float).where(rm.notna(), np.nan)).diff().diff().diff()


def f24_tnch_054_bars_since_last_nr7_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent NR7."""
    r = high - low
    rm = r.rolling(7, min_periods=7).min()
    return (_bars_since_true(r == rm)).diff().diff().diff()


def f24_tnch_055_nr7_count_63_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR7 count in past 63 bars."""
    r = high - low
    rm = r.rolling(7, min_periods=7).min()
    return (((r == rm).astype(float)).rolling(QDAYS, min_periods=MDAYS).sum().where(rm.notna(), np.nan)).diff().diff().diff()


def f24_tnch_056_inside_bar_flag_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if today's H < prior H AND today's L > prior L — inside bar (compression)."""
    flag = (high < high.shift(1)) & (low > low.shift(1))
    return (flag.astype(float).where(high.shift(1).notna(), np.nan)).diff().diff().diff()


def f24_tnch_057_outside_bar_flag_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if today's H > prior H AND today's L < prior L — outside bar (expansion)."""
    flag = (high > high.shift(1)) & (low < low.shift(1))
    return (flag.astype(float).where(high.shift(1).notna(), np.nan)).diff().diff().diff()


def f24_tnch_058_inside_bar_count_21_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside-bar count in past 21 bars."""
    flag = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return (flag.rolling(MDAYS, min_periods=WDAYS).sum().where(high.shift(1).notna(), np.nan)).diff().diff().diff()


def f24_tnch_059_outside_bar_count_21_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Outside-bar count in past 21 bars."""
    flag = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    return (flag.rolling(MDAYS, min_periods=WDAYS).sum().where(high.shift(1).notna(), np.nan)).diff().diff().diff()


def f24_tnch_060_inside_bar_count_63_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside-bar count in past 63 bars."""
    flag = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum().where(high.shift(1).notna(), np.nan)).diff().diff().diff()


def f24_tnch_061_outside_bar_count_63_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Outside-bar count in past 63 bars."""
    flag = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum().where(high.shift(1).notna(), np.nan)).diff().diff().diff()


def f24_tnch_062_bars_since_last_outside_bar_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent outside-bar — recency of expansion event."""
    flag = (high > high.shift(1)) & (low < low.shift(1))
    return (_bars_since_true(flag)).diff().diff().diff()


def f24_tnch_063_inside_after_wide_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today is inside-bar AND prior bar was wide-range (TR>2xATR21) — post-climax compression."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    wide_prev = r.shift(1) > 2.0
    return ((inside & wide_prev).astype(float).where(r.notna(), np.nan)).diff().diff().diff()


def f24_tnch_064_outside_close_weakness_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if outside-bar AND close in lower half of range (close < (H+L)/2) — bearish engulfing-style."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    mid = (high + low) / 2.0
    return ((outside & (close < mid)).astype(float).where(high.shift(1).notna(), np.nan)).diff().diff().diff()


def f24_tnch_065_gap_up_size_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """(Open - prior close) / prior close, clipped at zero — gap-up size."""
    return (((open_ - close.shift(1)) / close.shift(1)).clip(lower=0)).diff().diff().diff()


def f24_tnch_066_gap_down_size_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """(prior close - Open) / prior close, clipped at zero — gap-down size."""
    return (((close.shift(1) - open_) / close.shift(1)).clip(lower=0)).diff().diff().diff()


def f24_tnch_067_up_gap_count_21_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count of up-gap bars in past 21."""
    g = ((open_ - close.shift(1)) / close.shift(1))
    return ((g > 0.005).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(g.notna(), np.nan)).diff().diff().diff()


def f24_tnch_068_down_gap_count_21_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count of down-gap bars in past 21."""
    g = ((open_ - close.shift(1)) / close.shift(1))
    return ((g < -0.005).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(g.notna(), np.nan)).diff().diff().diff()


def f24_tnch_069_up_gap_count_63_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count of up-gap bars in past 63."""
    g = ((open_ - close.shift(1)) / close.shift(1))
    return ((g > 0.005).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(g.notna(), np.nan)).diff().diff().diff()


def f24_tnch_070_down_gap_count_63_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count of down-gap bars in past 63."""
    g = ((open_ - close.shift(1)) / close.shift(1))
    return ((g < -0.005).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(g.notna(), np.nan)).diff().diff().diff()


def f24_tnch_071_bars_since_last_up_gap_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent up-gap (> 0.5%)."""
    g = ((open_ - close.shift(1)) / close.shift(1))
    return (_bars_since_true(g > 0.005)).diff().diff().diff()


def f24_tnch_072_bars_since_last_down_gap_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent down-gap (> 0.5%)."""
    g = ((open_ - close.shift(1)) / close.shift(1))
    return (_bars_since_true(g < -0.005)).diff().diff().diff()


def f24_tnch_073_gap_filled_rate_21_d3(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 21 up-gap events that got 'filled' within 5 bars
    (low reached prev close). Conservative gap-fill proxy."""
    pc = close.shift(1)
    g = (open_ - pc) / pc
    up_gap = (g > 0.005)
    # gap filled if any of next 5 bars has low <= pc... but PIT-safe:
    # at bar t, check if bars t..t+4 contain a low <= pc[t]. To avoid look-ahead at evaluation time,
    # we use lookback: a bar-level historical fill, marking gap-fill at the bar it filled (lag).
    # Implementation: for each bar t, look back: was there an up_gap at t-k (k in 1..5) with pc[t-k] >= some low in [t-k+1..t]?
    fills = pd.Series(0.0, index=close.index)
    for k in range(1, 6):
        # check at current bar: did a k-bars-ago up_gap get filled by today?
        cond = up_gap.shift(k) & (pc.shift(k) >= low.rolling(k, min_periods=1).min())
        fills = fills + cond.astype(float).fillna(0.0)
    # count up_gaps in past 21 bars (any of past 21 bars had up_gap that has been observable)
    gaps_21 = up_gap.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    fills_21 = fills.rolling(MDAYS, min_periods=WDAYS).sum()
    return (_safe_div(fills_21, gaps_21)).diff().diff().diff()


def f24_tnch_074_net_gap_balance_63_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """(up-gaps - down-gaps) in past 63 bars — net gap-direction pressure."""
    pc = close.shift(1)
    g = (open_ - pc) / pc
    up = (g > 0.005).astype(float)
    dn = (g < -0.005).astype(float)
    return ((up - dn).rolling(QDAYS, min_periods=MDAYS).sum().where(g.notna(), np.nan)).diff().diff().diff()


def f24_tnch_075_gap_volatility_63_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Std of gap-pct over past 63 bars — overnight-gap volatility."""
    g = ((open_ - close.shift(1)) / close.shift(1))
    return (g.rolling(QDAYS, min_periods=MDAYS).std()).diff().diff().diff()


# ============================================================
#                         REGISTRY 001-075 (d3)
# ============================================================

_HLCV = ["high", "low", "close", "volume"]
_HLC = ["high", "low", "close"]
_HL = ["high", "low"]
_CV = ["close", "volume"]
_OC = ["open", "close"]
_OHLC = ["open", "high", "low", "close"]

TURNOVER_AND_CHURN_D3_REGISTRY_001_075 = {
    "f24_tnch_001_volume_over_avg_21_d3": {"inputs": ["volume"], "func": f24_tnch_001_volume_over_avg_21_d3},
    "f24_tnch_002_volume_over_avg_63_d3": {"inputs": ["volume"], "func": f24_tnch_002_volume_over_avg_63_d3},
    "f24_tnch_003_volume_over_avg_252_d3": {"inputs": ["volume"], "func": f24_tnch_003_volume_over_avg_252_d3},
    "f24_tnch_004_volume_over_avg_504_d3": {"inputs": ["volume"], "func": f24_tnch_004_volume_over_avg_504_d3},
    "f24_tnch_005_log_volume_over_median_21_d3": {"inputs": ["volume"], "func": f24_tnch_005_log_volume_over_median_21_d3},
    "f24_tnch_006_log_volume_over_median_63_d3": {"inputs": ["volume"], "func": f24_tnch_006_log_volume_over_median_63_d3},
    "f24_tnch_007_log_volume_over_median_252_d3": {"inputs": ["volume"], "func": f24_tnch_007_log_volume_over_median_252_d3},
    "f24_tnch_008_dollar_vol_over_avg_252_d3": {"inputs": _CV, "func": f24_tnch_008_dollar_vol_over_avg_252_d3},
    "f24_tnch_009_tr_over_atr21_d3": {"inputs": _HLC, "func": f24_tnch_009_tr_over_atr21_d3},
    "f24_tnch_010_tr_over_atr63_d3": {"inputs": _HLC, "func": f24_tnch_010_tr_over_atr63_d3},
    "f24_tnch_011_tr_over_atr252_d3": {"inputs": _HLC, "func": f24_tnch_011_tr_over_atr252_d3},
    "f24_tnch_012_hl_range_over_avg_21_d3": {"inputs": _HL, "func": f24_tnch_012_hl_range_over_avg_21_d3},
    "f24_tnch_013_hl_range_over_avg_63_d3": {"inputs": _HL, "func": f24_tnch_013_hl_range_over_avg_63_d3},
    "f24_tnch_014_wide_range_bar_flag_d3": {"inputs": _HLC, "func": f24_tnch_014_wide_range_bar_flag_d3},
    "f24_tnch_015_extra_wide_bar_flag_d3": {"inputs": _HLC, "func": f24_tnch_015_extra_wide_bar_flag_d3},
    "f24_tnch_016_extreme_wide_bar_flag_d3": {"inputs": _HLC, "func": f24_tnch_016_extreme_wide_bar_flag_d3},
    "f24_tnch_017_bars_since_last_wide_range_d3": {"inputs": _HLC, "func": f24_tnch_017_bars_since_last_wide_range_d3},
    "f24_tnch_018_wide_range_count_21_d3": {"inputs": _HLC, "func": f24_tnch_018_wide_range_count_21_d3},
    "f24_tnch_019_wide_range_count_63_d3": {"inputs": _HLC, "func": f24_tnch_019_wide_range_count_63_d3},
    "f24_tnch_020_wide_range_count_252_d3": {"inputs": _HLC, "func": f24_tnch_020_wide_range_count_252_d3},
    "f24_tnch_021_extra_wide_count_63_d3": {"inputs": _HLC, "func": f24_tnch_021_extra_wide_count_63_d3},
    "f24_tnch_022_extra_wide_count_252_d3": {"inputs": _HLC, "func": f24_tnch_022_extra_wide_count_252_d3},
    "f24_tnch_023_fraction_wide_range_21_d3": {"inputs": _HLC, "func": f24_tnch_023_fraction_wide_range_21_d3},
    "f24_tnch_024_fraction_wide_range_63_d3": {"inputs": _HLC, "func": f24_tnch_024_fraction_wide_range_63_d3},
    "f24_tnch_025_fraction_wide_range_252_d3": {"inputs": _HLC, "func": f24_tnch_025_fraction_wide_range_252_d3},
    "f24_tnch_026_longest_wide_range_run_252_d3": {"inputs": _HLC, "func": f24_tnch_026_longest_wide_range_run_252_d3},
    "f24_tnch_027_churn_index_d3": {"inputs": _CV, "func": f24_tnch_027_churn_index_d3},
    "f24_tnch_028_churn_bar_flag_d3": {"inputs": _CV, "func": f24_tnch_028_churn_bar_flag_d3},
    "f24_tnch_029_churn_bar_flag_strict_d3": {"inputs": _CV, "func": f24_tnch_029_churn_bar_flag_strict_d3},
    "f24_tnch_030_churn_count_21_d3": {"inputs": _CV, "func": f24_tnch_030_churn_count_21_d3},
    "f24_tnch_031_churn_count_63_d3": {"inputs": _CV, "func": f24_tnch_031_churn_count_63_d3},
    "f24_tnch_032_churn_count_252_d3": {"inputs": _CV, "func": f24_tnch_032_churn_count_252_d3},
    "f24_tnch_033_bars_since_last_churn_d3": {"inputs": _CV, "func": f24_tnch_033_bars_since_last_churn_d3},
    "f24_tnch_034_longest_churn_run_63_d3": {"inputs": _CV, "func": f24_tnch_034_longest_churn_run_63_d3},
    "f24_tnch_035_fraction_churn_21_d3": {"inputs": _CV, "func": f24_tnch_035_fraction_churn_21_d3},
    "f24_tnch_036_fraction_churn_63_d3": {"inputs": _CV, "func": f24_tnch_036_fraction_churn_63_d3},
    "f24_tnch_037_vol_zscore_21_d3": {"inputs": ["volume"], "func": f24_tnch_037_vol_zscore_21_d3},
    "f24_tnch_038_vol_zscore_63_d3": {"inputs": ["volume"], "func": f24_tnch_038_vol_zscore_63_d3},
    "f24_tnch_039_vol_zscore_252_d3": {"inputs": ["volume"], "func": f24_tnch_039_vol_zscore_252_d3},
    "f24_tnch_040_vol_pct_rank_63_d3": {"inputs": ["volume"], "func": f24_tnch_040_vol_pct_rank_63_d3},
    "f24_tnch_041_vol_pct_rank_252_d3": {"inputs": ["volume"], "func": f24_tnch_041_vol_pct_rank_252_d3},
    "f24_tnch_042_dollar_vol_zscore_252_d3": {"inputs": _CV, "func": f24_tnch_042_dollar_vol_zscore_252_d3},
    "f24_tnch_043_dollar_vol_pct_rank_252_d3": {"inputs": _CV, "func": f24_tnch_043_dollar_vol_pct_rank_252_d3},
    "f24_tnch_044_vol_above_q95_state_252_d3": {"inputs": ["volume"], "func": f24_tnch_044_vol_above_q95_state_252_d3},
    "f24_tnch_045_vol_above_q99_state_252_d3": {"inputs": ["volume"], "func": f24_tnch_045_vol_above_q99_state_252_d3},
    "f24_tnch_046_bars_since_q99_vol_252_d3": {"inputs": ["volume"], "func": f24_tnch_046_bars_since_q99_vol_252_d3},
    "f24_tnch_047_range_ratio_5_over_21_d3": {"inputs": _HL, "func": f24_tnch_047_range_ratio_5_over_21_d3},
    "f24_tnch_048_range_ratio_21_over_63_d3": {"inputs": _HL, "func": f24_tnch_048_range_ratio_21_over_63_d3},
    "f24_tnch_049_range_ratio_21_over_252_d3": {"inputs": _HL, "func": f24_tnch_049_range_ratio_21_over_252_d3},
    "f24_tnch_050_range_ratio_5max_over_21avg_d3": {"inputs": _HL, "func": f24_tnch_050_range_ratio_5max_over_21avg_d3},
    "f24_tnch_051_range_expansion_zscore_252_d3": {"inputs": _HL, "func": f24_tnch_051_range_expansion_zscore_252_d3},
    "f24_tnch_052_nr4_flag_d3": {"inputs": _HL, "func": f24_tnch_052_nr4_flag_d3},
    "f24_tnch_053_nr7_flag_d3": {"inputs": _HL, "func": f24_tnch_053_nr7_flag_d3},
    "f24_tnch_054_bars_since_last_nr7_d3": {"inputs": _HL, "func": f24_tnch_054_bars_since_last_nr7_d3},
    "f24_tnch_055_nr7_count_63_d3": {"inputs": _HL, "func": f24_tnch_055_nr7_count_63_d3},
    "f24_tnch_056_inside_bar_flag_d3": {"inputs": _HL, "func": f24_tnch_056_inside_bar_flag_d3},
    "f24_tnch_057_outside_bar_flag_d3": {"inputs": _HL, "func": f24_tnch_057_outside_bar_flag_d3},
    "f24_tnch_058_inside_bar_count_21_d3": {"inputs": _HL, "func": f24_tnch_058_inside_bar_count_21_d3},
    "f24_tnch_059_outside_bar_count_21_d3": {"inputs": _HL, "func": f24_tnch_059_outside_bar_count_21_d3},
    "f24_tnch_060_inside_bar_count_63_d3": {"inputs": _HL, "func": f24_tnch_060_inside_bar_count_63_d3},
    "f24_tnch_061_outside_bar_count_63_d3": {"inputs": _HL, "func": f24_tnch_061_outside_bar_count_63_d3},
    "f24_tnch_062_bars_since_last_outside_bar_d3": {"inputs": _HL, "func": f24_tnch_062_bars_since_last_outside_bar_d3},
    "f24_tnch_063_inside_after_wide_range_d3": {"inputs": _HLC, "func": f24_tnch_063_inside_after_wide_range_d3},
    "f24_tnch_064_outside_close_weakness_d3": {"inputs": _HLC, "func": f24_tnch_064_outside_close_weakness_d3},
    "f24_tnch_065_gap_up_size_d3": {"inputs": _OC, "func": f24_tnch_065_gap_up_size_d3},
    "f24_tnch_066_gap_down_size_d3": {"inputs": _OC, "func": f24_tnch_066_gap_down_size_d3},
    "f24_tnch_067_up_gap_count_21_d3": {"inputs": _OC, "func": f24_tnch_067_up_gap_count_21_d3},
    "f24_tnch_068_down_gap_count_21_d3": {"inputs": _OC, "func": f24_tnch_068_down_gap_count_21_d3},
    "f24_tnch_069_up_gap_count_63_d3": {"inputs": _OC, "func": f24_tnch_069_up_gap_count_63_d3},
    "f24_tnch_070_down_gap_count_63_d3": {"inputs": _OC, "func": f24_tnch_070_down_gap_count_63_d3},
    "f24_tnch_071_bars_since_last_up_gap_d3": {"inputs": _OC, "func": f24_tnch_071_bars_since_last_up_gap_d3},
    "f24_tnch_072_bars_since_last_down_gap_d3": {"inputs": _OC, "func": f24_tnch_072_bars_since_last_down_gap_d3},
    "f24_tnch_073_gap_filled_rate_21_d3": {"inputs": _OHLC, "func": f24_tnch_073_gap_filled_rate_21_d3},
    "f24_tnch_074_net_gap_balance_63_d3": {"inputs": _OC, "func": f24_tnch_074_net_gap_balance_63_d3},
    "f24_tnch_075_gap_volatility_63_d3": {"inputs": _OC, "func": f24_tnch_075_gap_volatility_63_d3},
}
