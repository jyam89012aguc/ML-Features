"""atr_expansion_dynamics d3 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the ATR / true-range expansion theme:
ATR ratios across timeframes, percentile-rank regimes, NATR levels and z-scores,
expansion velocity, ATR-at-peak signatures, TR outlier counts, ATR vs other
volatility-estimators, range-of-range, ATR cone position, compression-then-
expansion, ATR cross-overs, gap-vs-intraday TR decomposition.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). "ATR at peak" features use high.rolling(N).max()
which is right-anchored — no forward confirmation of the peak. Self-contained
helpers — no cross-family imports.
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


# ============================================================
# Bucket A — ATR ratios across timeframes (001-010)
# Each ratio = a distinct regime/term-structure hypothesis
# ============================================================

def f40_atxd_001_atr5_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast-vs-medium ATR ratio: ATR(5) / ATR(21) — short-term shock-release detector."""
    return _safe_div(_atr(high, low, close, WDAYS), _atr(high, low, close, MDAYS))


def f40_atxd_002_atr21_over_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Medium-vs-intermediate ATR ratio: ATR(21) / ATR(63)."""
    return _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, QDAYS))


def f40_atxd_003_atr63_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Intermediate-vs-annual ATR ratio: ATR(63) / ATR(252) — multi-cycle compression."""
    return _safe_div(_atr(high, low, close, QDAYS), _atr(high, low, close, YDAYS))


def f40_atxd_004_atr5_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast-vs-annual ATR ratio: ATR(5) / ATR(252) — extreme-multi-scale expansion."""
    return _safe_div(_atr(high, low, close, WDAYS), _atr(high, low, close, YDAYS))


def f40_atxd_005_log_atr5_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log of fast-vs-annual ATR ratio."""
    return _safe_log(_atr(high, low, close, WDAYS)) - _safe_log(_atr(high, low, close, YDAYS))


def f40_atxd_006_atr10_over_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(10) / ATR(63) — 2-week-vs-quarter expansion detector."""
    return _safe_div(_atr(high, low, close, 10), _atr(high, low, close, QDAYS))


def f40_atxd_007_atr5_minus_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute differential: ATR(5) − ATR(21) — short-vs-medium ATR gap."""
    return _atr(high, low, close, WDAYS) - _atr(high, low, close, MDAYS)


def f40_atxd_008_atr21_minus_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute differential: ATR(21) − ATR(63) — medium-vs-intermediate ATR gap."""
    return _atr(high, low, close, MDAYS) - _atr(high, low, close, QDAYS)


def f40_atxd_009_rel_diff_atr5_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relative differential: (ATR(5) − ATR(21)) / ATR(21)."""
    return _safe_div(_atr(high, low, close, WDAYS) - _atr(high, low, close, MDAYS),
                     _atr(high, low, close, MDAYS))


def f40_atxd_010_atr63_minus_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-end term-structure delta: ATR(63) − ATR(252)."""
    return _atr(high, low, close, QDAYS) - _atr(high, low, close, YDAYS)


# ============================================================
# Bucket B — ATR percentile rank (011-018)
# ============================================================

def _pct_rank(s: pd.Series, n: int, min_periods: int) -> pd.Series:
    return s.rolling(n, min_periods=min_periods).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan,
        raw=True,
    )


def f40_atxd_011_atr21_pctrank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of ATR(21) within own past 252d distribution — 1-year extreme."""
    return _pct_rank(_atr(high, low, close, MDAYS), YDAYS, QDAYS)


def f40_atxd_012_atr21_pctrank_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of ATR(21) within own past 504d distribution — 2-year extreme."""
    return _pct_rank(_atr(high, low, close, MDAYS), DDAYS_2Y, YDAYS)


def f40_atxd_013_atr21_pctrank_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of ATR(21) within own past 1260d distribution — 5-year extreme."""
    return _pct_rank(_atr(high, low, close, MDAYS), DDAYS_5Y, DDAYS_2Y)


def f40_atxd_014_atr63_pctrank_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of ATR(63) within own past 1260d distribution."""
    return _pct_rank(_atr(high, low, close, QDAYS), DDAYS_5Y, DDAYS_2Y)


def f40_atxd_015_atr5_pctrank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of ATR(5) within own past 252d distribution."""
    return _pct_rank(_atr(high, low, close, WDAYS), YDAYS, QDAYS)


def f40_atxd_016_atr252_pctrank_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of ATR(252) within own past 1260d — annual ATR at multi-year extreme."""
    return _pct_rank(_atr(high, low, close, YDAYS), DDAYS_5Y, DDAYS_2Y)


def f40_atxd_017_natr21_pctrank_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of NATR(21)=ATR/close within own past 504d distribution."""
    return _pct_rank(_safe_div(_atr(high, low, close, MDAYS), close), DDAYS_2Y, YDAYS)


def f40_atxd_018_atr21_zscore_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of ATR(21) within own past 504d distribution."""
    return _rolling_zscore(_atr(high, low, close, MDAYS), DDAYS_2Y)


# ============================================================
# Bucket C — Normalized ATR / NATR (019-026)
# ============================================================

def f40_atxd_019_natr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(21) = ATR(21) / close — close-normalized ATR (vol-as-fraction-of-price)."""
    return _safe_div(_atr(high, low, close, MDAYS), close)


def f40_atxd_020_natr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(63) = ATR(63) / close — intermediate-horizon normalized ATR."""
    return _safe_div(_atr(high, low, close, QDAYS), close)


def f40_atxd_021_natr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(252) = ATR(252) / close — annual-horizon normalized ATR."""
    return _safe_div(_atr(high, low, close, YDAYS), close)


def f40_atxd_022_log_natr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(ATR(21) / close) — log-scale NATR."""
    return _safe_log(_atr(high, low, close, MDAYS)) - _safe_log(close)


def f40_atxd_023_natr21_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d z-score of NATR(21) within own distribution."""
    return _rolling_zscore(_safe_div(_atr(high, low, close, MDAYS), close), YDAYS)


def f40_atxd_024_natr21_zscore_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 1260d z-score of NATR(21) within own distribution — multi-year anomaly."""
    return _rolling_zscore(_safe_div(_atr(high, low, close, MDAYS), close), DDAYS_5Y)


def f40_atxd_025_natr21_pctrank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of NATR(21) within own past 252d distribution."""
    return _pct_rank(_safe_div(_atr(high, low, close, MDAYS), close), YDAYS, QDAYS)


def f40_atxd_026_natr21_anchor_deviation_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(21) anchoring: NATR(21) − rolling 252d mean of NATR(21)."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    return n - n.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket D — ATR expansion velocity (027-034)
# ============================================================

def f40_atxd_027_atr21_change_lag21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Monthly ATR Δ: ATR(21) − ATR(21).shift(21)."""
    a = _atr(high, low, close, MDAYS)
    return a - a.shift(MDAYS)


def f40_atxd_028_atr21_change_lag63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Quarterly ATR Δ: ATR(21) − ATR(21).shift(63)."""
    a = _atr(high, low, close, MDAYS)
    return a - a.shift(QDAYS)


def f40_atxd_029_atr21_pct_change_lag21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relative monthly ATR change: ATR(21).pct_change(21)."""
    a = _atr(high, low, close, MDAYS)
    return a.pct_change(MDAYS)


def f40_atxd_030_atr21_pct_change_lag63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relative quarterly ATR change: ATR(21).pct_change(63)."""
    a = _atr(high, low, close, MDAYS)
    return a.pct_change(QDAYS)


def f40_atxd_031_log_atr21_ratio_lag63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log quarterly ATR ratio: log(ATR(21) / ATR(21).shift(63))."""
    a = _atr(high, low, close, MDAYS)
    return _safe_log(a) - _safe_log(a.shift(QDAYS))


def f40_atxd_032_slope_atr21_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d slope of ATR(21) — quarterly trend of ATR."""
    return _rolling_slope(_atr(high, low, close, MDAYS), QDAYS)


def f40_atxd_033_slope_atr21_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d slope of ATR(21) — annual trend of ATR."""
    return _rolling_slope(_atr(high, low, close, MDAYS), YDAYS)


def f40_atxd_034_slope_log_atr21_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d slope of log(ATR(21)) — log-scale annual trend."""
    return _rolling_slope(_safe_log(_atr(high, low, close, MDAYS)), YDAYS)


# ============================================================
# Bucket E — ATR-at-peak signatures (035-042)
# Right-anchored: peak is the trailing rolling-max of high.
# ============================================================

def _value_at_252d_peak(s: pd.Series, high: pd.Series) -> pd.Series:
    """Value of s at the bar where high attained its trailing-252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = (high == rmax)
    # Forward-fill s on bars marked as peak — but use causal mask:
    s_peak = s.where(at_peak)
    return s_peak.ffill()


def f40_atxd_035_atr21_over_atr21_at_252d_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) now / ATR(21) at most recent 252d-high — ATR expansion vs peak baseline."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a, _value_at_252d_peak(a, high))


def f40_atxd_036_atr21_over_atr21_at_63d_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) now / ATR(21) at most recent 63d-high."""
    a = _atr(high, low, close, MDAYS)
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return _safe_div(a, a.where(high == rmax).ffill())


def f40_atxd_037_atr21_at_252d_peak_level(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) value at the most recent 252d-high bar (level snapshot)."""
    return _value_at_252d_peak(_atr(high, low, close, MDAYS), high)


def f40_atxd_038_log_atr21_over_at_252d_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(ATR(21) / ATR(21) at last 252d-high)."""
    a = _atr(high, low, close, MDAYS)
    return _safe_log(a) - _safe_log(_value_at_252d_peak(a, high))


def f40_atxd_039_atr63_over_atr63_at_252d_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(63) now / ATR(63) at most recent 252d-high."""
    a = _atr(high, low, close, QDAYS)
    return _safe_div(a, _value_at_252d_peak(a, high))


def f40_atxd_040_natr21_over_at_252d_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(21) now / NATR(21) at most recent 252d-high."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    return _safe_div(n, _value_at_252d_peak(n, high))


def f40_atxd_041_atr21_zscore_since_252d_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of current ATR(21) relative to its distribution since most-recent 252d-high."""
    a = _atr(high, low, close, MDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bars_since = (high != rmax).astype(int)
    bars_since = bars_since.groupby((high == rmax).cumsum()).cumsum()
    # Use a fallback window of 21 to avoid degenerate windows
    win = bars_since.clip(lower=WDAYS, upper=YDAYS).astype(int)

    def _z(arr_atr, arr_win):
        out = np.full(len(arr_atr), np.nan)
        for i in range(len(arr_atr)):
            n = int(arr_win[i])
            if i < n or n < WDAYS:
                continue
            seg = arr_atr[i - n + 1: i + 1]
            sd = seg.std()
            if sd == 0 or np.isnan(sd):
                continue
            out[i] = (arr_atr[i] - seg.mean()) / sd
        return out
    return pd.Series(_z(a.values, win.values), index=close.index)


def f40_atxd_042_bars_above_atr_at_252d_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(21) > ATR(21) at last 252d-high, since that high."""
    a = _atr(high, low, close, MDAYS)
    a_peak = _value_at_252d_peak(a, high)
    above = (a > a_peak).astype(float)
    # Reset cumulative count at each new peak event
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    reset = (high == rmax).astype(int).cumsum()
    return above.groupby(reset).cumsum()


# ============================================================
# Bucket F — True-range outlier counts (043-048)
# ============================================================

def f40_atxd_043_count_tr_above_2atr21_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR > 2·ATR(21).shift(1) within 21d — single-bar shock count short."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS).shift(1)
    return (tr > 2 * atr).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f40_atxd_044_count_tr_above_3atr21_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR > 3·ATR(21).shift(1) within 63d."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS).shift(1)
    return (tr > 3 * atr).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_045_count_tr_above_4atr63_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR > 4·ATR(63).shift(1) within 252d — annual extreme."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, QDAYS).shift(1)
    return (tr > 4 * atr).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def _longest_run(w: np.ndarray) -> float:
    m = 0; c = 0
    for v in w:
        if v > 0.5:
            c += 1; m = c if c > m else m
        else:
            c = 0
    return float(m)


def f40_atxd_046_longest_tr_above_atr21_run_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest streak of consecutive TR > ATR(21).shift(1) within 63d."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS).shift(1)
    return (tr > atr).astype(float).fillna(0.0).rolling(QDAYS, min_periods=MDAYS).apply(_longest_run, raw=True)


def f40_atxd_047_count_tr_top_decile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR is in top decile of its own past 252d distribution."""
    tr = _true_range(high, low, close)
    p90 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.90).shift(1)
    return (tr > p90).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_048_count_tr_top5pct_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR is in top 5% of its own past 1260d distribution."""
    tr = _true_range(high, low, close)
    p95 = tr.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).quantile(0.95).shift(1)
    return (tr > p95).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket G — ATR vs other vol-estimators (049-052)
# ============================================================

def _garman_klass(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, n: int = 21) -> pd.Series:
    a = 0.5 * (_safe_log(high) - _safe_log(low)) ** 2
    b = (2.0 * np.log(2.0) - 1.0) * (_safe_log(close) - _safe_log(open)) ** 2
    return np.sqrt((a - b).rolling(n, min_periods=max(n // 3, 2)).mean())


def _parkinson(high: pd.Series, low: pd.Series, n: int = 21) -> pd.Series:
    return np.sqrt(((_safe_log(high) - _safe_log(low)) ** 2 / (4.0 * np.log(2.0)))
                   .rolling(n, min_periods=max(n // 3, 2)).mean())


def _rogers_satchell(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, n: int = 21) -> pd.Series:
    a = (_safe_log(high) - _safe_log(close)) * (_safe_log(high) - _safe_log(open))
    b = (_safe_log(low) - _safe_log(close)) * (_safe_log(low) - _safe_log(open))
    return np.sqrt((a + b).rolling(n, min_periods=max(n // 3, 2)).mean())


def f40_atxd_049_gk_over_atr21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass vol / ATR(21) over 21d — GK-to-ATR ratio."""
    return _safe_div(_garman_klass(high, low, open, close, MDAYS), _atr(high, low, close, MDAYS))


def f40_atxd_050_yz_over_atr21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang vol / ATR(21): combines overnight + open-to-close + RS over 21d."""
    n = MDAYS
    log_oc1 = _safe_log(open) - _safe_log(close.shift(1))
    log_co = _safe_log(close) - _safe_log(open)
    sig_o = log_oc1.rolling(n, min_periods=max(n // 3, 2)).var()
    sig_c = log_co.rolling(n, min_periods=max(n // 3, 2)).var()
    rs = _rogers_satchell(high, low, open, close, n) ** 2
    k = 0.34 / (1.34 + (n + 1) / (n - 1))
    yz = np.sqrt(sig_o + k * sig_c + (1 - k) * rs)
    return _safe_div(yz, _atr(high, low, close, n))


def f40_atxd_051_rs_over_atr21(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell vol / ATR(21) — RS-to-ATR ratio."""
    return _safe_div(_rogers_satchell(high, low, open, close, MDAYS), _atr(high, low, close, MDAYS))


def f40_atxd_052_atr21_over_parkinson(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / Parkinson(21): TR-based vs HL-only vol estimator."""
    return _safe_div(_atr(high, low, close, MDAYS), _parkinson(high, low, MDAYS))


# ============================================================
# Bucket H — Range-of-range (053-058)
# ============================================================

def f40_atxd_053_std_tr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21d std of true-range — short-horizon range-of-range."""
    return _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).std()


def f40_atxd_054_std_tr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d std of true-range."""
    return _true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).std()


def f40_atxd_055_std_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d std of true-range — annual range-of-range."""
    return _true_range(high, low, close).rolling(YDAYS, min_periods=QDAYS).std()


def f40_atxd_056_cv_tr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CV (std/mean) of TR over 21d — short-horizon range-coefficient-of-variation."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.rolling(MDAYS, min_periods=WDAYS).std(),
                     tr.rolling(MDAYS, min_periods=WDAYS).mean())


def f40_atxd_057_cv_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CV of TR over 252d — annual range-coefficient-of-variation."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.rolling(YDAYS, min_periods=QDAYS).std(),
                     tr.rolling(YDAYS, min_periods=QDAYS).mean())


def f40_atxd_058_skew_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d skew of TR — range-asymmetry."""
    return _true_range(high, low, close).rolling(YDAYS, min_periods=QDAYS).skew()


# ============================================================
# Bucket I — ATR cone position (059-064)
# ============================================================

def f40_atxd_059_atr21_above_p10_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) > trailing-252d 10th-pct of ATR(21)."""
    a = _atr(high, low, close, MDAYS)
    return (a > a.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)).astype(float)


def f40_atxd_060_atr21_above_p25_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) > trailing-252d 25th-pct of ATR(21)."""
    a = _atr(high, low, close, MDAYS)
    return (a > a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)).astype(float)


def f40_atxd_061_atr21_above_p75_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) > trailing-252d 75th-pct of ATR(21)."""
    a = _atr(high, low, close, MDAYS)
    return (a > a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)).astype(float)


def f40_atxd_062_atr21_above_p90_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) > trailing-252d 90th-pct of ATR(21)."""
    a = _atr(high, low, close, MDAYS)
    return (a > a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)).astype(float)


def f40_atxd_063_atr21_in_iqr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) within trailing-252d inter-quartile range [p25,p75]."""
    a = _atr(high, low, close, MDAYS)
    p25 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return ((a >= p25) & (a <= p75)).astype(float)


def f40_atxd_064_atr21_outside_cone_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) outside trailing-252d [p10,p90] cone (extreme-regime flag)."""
    a = _atr(high, low, close, MDAYS)
    p10 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    p90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((a < p10) | (a > p90)).astype(float)


# ============================================================
# Bucket J — ATR compression-then-expansion (065-068)
# ============================================================

def f40_atxd_065_atr21_over_min_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Compression release: ATR(21) / min(ATR(21), past 63d) — magnitude of expansion vs recent floor."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a, a.rolling(QDAYS, min_periods=MDAYS).min())


def f40_atxd_066_atr21_over_min_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual compression release: ATR(21) / min(ATR(21), past 252d)."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a, a.rolling(YDAYS, min_periods=QDAYS).min())


def f40_atxd_067_log_atr21_over_min_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log compression release: log(ATR(21) / min(ATR(21), past 63d))."""
    a = _atr(high, low, close, MDAYS)
    return _safe_log(a) - _safe_log(a.rolling(QDAYS, min_periods=MDAYS).min())


def f40_atxd_068_bars_since_atr21_63d_min(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since ATR(21) last printed its 63d minimum (recency of compression)."""
    a = _atr(high, low, close, MDAYS)
    mn = a.rolling(QDAYS, min_periods=MDAYS).min()
    at_min = (a == mn).astype(int).fillna(0).values
    out = np.full(len(at_min), np.nan)
    bars = np.nan
    for i, v in enumerate(at_min):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket K — ATR cross-overs (069-072)
# ============================================================

def f40_atxd_069_atr5_above_atr63_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(5) > ATR(63) — fast-vol regime flag."""
    return (_atr(high, low, close, WDAYS) > _atr(high, low, close, QDAYS)).astype(float)


def f40_atxd_070_count_atr5_cross_above_atr63_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (ATR(5) crossing ABOVE ATR(63)) events within 63d."""
    a5 = _atr(high, low, close, WDAYS)
    a63 = _atr(high, low, close, QDAYS)
    above = (a5 > a63).astype(int)
    cross = ((above == 1) & (above.shift(1) == 0)).astype(float)
    return cross.rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_071_bars_since_atr5_above_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bar where ATR(5) > ATR(63)."""
    above = (_atr(high, low, close, WDAYS) > _atr(high, low, close, QDAYS)).astype(int).fillna(0).values
    out = np.full(len(above), np.nan)
    bars = np.nan
    for i, v in enumerate(above):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index)


def f40_atxd_072_bars_since_atr21_cross_above_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last ATR(21) upward-crossing of ATR(63)."""
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    above = (a21 > a63).astype(int)
    cross = ((above == 1) & (above.shift(1) == 0)).astype(int).fillna(0).values
    out = np.full(len(cross), np.nan)
    bars = np.nan
    for i, v in enumerate(cross):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket L — Range expansion vs gap expansion (073-075)
# ============================================================

def f40_atxd_073_gap_component_mean_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean overnight |gap| component (|open − prev_close|) over 21d."""
    return (open - close.shift(1)).abs().rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_074_body_component_mean_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean intraday body component (high − low) over 21d."""
    return (high - low).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_075_ratio_gap_body_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio mean |gap| / mean (high−low) over 63d — overnight share of TR."""
    g = (open - close.shift(1)).abs().rolling(QDAYS, min_periods=MDAYS).mean()
    b = (high - low).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(g, b)


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f40_atxd_001_atr5_over_atr21_d3(high, low, close):
    return f40_atxd_001_atr5_over_atr21(high, low, close).diff().diff().diff()


def f40_atxd_002_atr21_over_atr63_d3(high, low, close):
    return f40_atxd_002_atr21_over_atr63(high, low, close).diff().diff().diff()


def f40_atxd_003_atr63_over_atr252_d3(high, low, close):
    return f40_atxd_003_atr63_over_atr252(high, low, close).diff().diff().diff()


def f40_atxd_004_atr5_over_atr252_d3(high, low, close):
    return f40_atxd_004_atr5_over_atr252(high, low, close).diff().diff().diff()


def f40_atxd_005_log_atr5_over_atr252_d3(high, low, close):
    return f40_atxd_005_log_atr5_over_atr252(high, low, close).diff().diff().diff()


def f40_atxd_006_atr10_over_atr63_d3(high, low, close):
    return f40_atxd_006_atr10_over_atr63(high, low, close).diff().diff().diff()


def f40_atxd_007_atr5_minus_atr21_d3(high, low, close):
    return f40_atxd_007_atr5_minus_atr21(high, low, close).diff().diff().diff()


def f40_atxd_008_atr21_minus_atr63_d3(high, low, close):
    return f40_atxd_008_atr21_minus_atr63(high, low, close).diff().diff().diff()


def f40_atxd_009_rel_diff_atr5_atr21_d3(high, low, close):
    return f40_atxd_009_rel_diff_atr5_atr21(high, low, close).diff().diff().diff()


def f40_atxd_010_atr63_minus_atr252_d3(high, low, close):
    return f40_atxd_010_atr63_minus_atr252(high, low, close).diff().diff().diff()


def f40_atxd_011_atr21_pctrank_252d_d3(high, low, close):
    return f40_atxd_011_atr21_pctrank_252d(high, low, close).diff().diff().diff()


def f40_atxd_012_atr21_pctrank_504d_d3(high, low, close):
    return f40_atxd_012_atr21_pctrank_504d(high, low, close).diff().diff().diff()


def f40_atxd_013_atr21_pctrank_1260d_d3(high, low, close):
    return f40_atxd_013_atr21_pctrank_1260d(high, low, close).diff().diff().diff()


def f40_atxd_014_atr63_pctrank_1260d_d3(high, low, close):
    return f40_atxd_014_atr63_pctrank_1260d(high, low, close).diff().diff().diff()


def f40_atxd_015_atr5_pctrank_252d_d3(high, low, close):
    return f40_atxd_015_atr5_pctrank_252d(high, low, close).diff().diff().diff()


def f40_atxd_016_atr252_pctrank_1260d_d3(high, low, close):
    return f40_atxd_016_atr252_pctrank_1260d(high, low, close).diff().diff().diff()


def f40_atxd_017_natr21_pctrank_504d_d3(high, low, close):
    return f40_atxd_017_natr21_pctrank_504d(high, low, close).diff().diff().diff()


def f40_atxd_018_atr21_zscore_504d_d3(high, low, close):
    return f40_atxd_018_atr21_zscore_504d(high, low, close).diff().diff().diff()


def f40_atxd_019_natr21_d3(high, low, close):
    return f40_atxd_019_natr21(high, low, close).diff().diff().diff()


def f40_atxd_020_natr63_d3(high, low, close):
    return f40_atxd_020_natr63(high, low, close).diff().diff().diff()


def f40_atxd_021_natr252_d3(high, low, close):
    return f40_atxd_021_natr252(high, low, close).diff().diff().diff()


def f40_atxd_022_log_natr21_d3(high, low, close):
    return f40_atxd_022_log_natr21(high, low, close).diff().diff().diff()


def f40_atxd_023_natr21_zscore_252d_d3(high, low, close):
    return f40_atxd_023_natr21_zscore_252d(high, low, close).diff().diff().diff()


def f40_atxd_024_natr21_zscore_1260d_d3(high, low, close):
    return f40_atxd_024_natr21_zscore_1260d(high, low, close).diff().diff().diff()


def f40_atxd_025_natr21_pctrank_252d_d3(high, low, close):
    return f40_atxd_025_natr21_pctrank_252d(high, low, close).diff().diff().diff()


def f40_atxd_026_natr21_anchor_deviation_252d_d3(high, low, close):
    return f40_atxd_026_natr21_anchor_deviation_252d(high, low, close).diff().diff().diff()


def f40_atxd_027_atr21_change_lag21_d3(high, low, close):
    return f40_atxd_027_atr21_change_lag21(high, low, close).diff().diff().diff()


def f40_atxd_028_atr21_change_lag63_d3(high, low, close):
    return f40_atxd_028_atr21_change_lag63(high, low, close).diff().diff().diff()


def f40_atxd_029_atr21_pct_change_lag21_d3(high, low, close):
    return f40_atxd_029_atr21_pct_change_lag21(high, low, close).diff().diff().diff()


def f40_atxd_030_atr21_pct_change_lag63_d3(high, low, close):
    return f40_atxd_030_atr21_pct_change_lag63(high, low, close).diff().diff().diff()


def f40_atxd_031_log_atr21_ratio_lag63_d3(high, low, close):
    return f40_atxd_031_log_atr21_ratio_lag63(high, low, close).diff().diff().diff()


def f40_atxd_032_slope_atr21_63d_d3(high, low, close):
    return f40_atxd_032_slope_atr21_63d(high, low, close).diff().diff().diff()


def f40_atxd_033_slope_atr21_252d_d3(high, low, close):
    return f40_atxd_033_slope_atr21_252d(high, low, close).diff().diff().diff()


def f40_atxd_034_slope_log_atr21_252d_d3(high, low, close):
    return f40_atxd_034_slope_log_atr21_252d(high, low, close).diff().diff().diff()


def f40_atxd_035_atr21_over_atr21_at_252d_peak_d3(high, low, close):
    return f40_atxd_035_atr21_over_atr21_at_252d_peak(high, low, close).diff().diff().diff()


def f40_atxd_036_atr21_over_atr21_at_63d_peak_d3(high, low, close):
    return f40_atxd_036_atr21_over_atr21_at_63d_peak(high, low, close).diff().diff().diff()


def f40_atxd_037_atr21_at_252d_peak_level_d3(high, low, close):
    return f40_atxd_037_atr21_at_252d_peak_level(high, low, close).diff().diff().diff()


def f40_atxd_038_log_atr21_over_at_252d_peak_d3(high, low, close):
    return f40_atxd_038_log_atr21_over_at_252d_peak(high, low, close).diff().diff().diff()


def f40_atxd_039_atr63_over_atr63_at_252d_peak_d3(high, low, close):
    return f40_atxd_039_atr63_over_atr63_at_252d_peak(high, low, close).diff().diff().diff()


def f40_atxd_040_natr21_over_at_252d_peak_d3(high, low, close):
    return f40_atxd_040_natr21_over_at_252d_peak(high, low, close).diff().diff().diff()


def f40_atxd_041_atr21_zscore_since_252d_peak_d3(high, low, close):
    return f40_atxd_041_atr21_zscore_since_252d_peak(high, low, close).diff().diff().diff()


def f40_atxd_042_bars_above_atr_at_252d_peak_d3(high, low, close):
    return f40_atxd_042_bars_above_atr_at_252d_peak(high, low, close).diff().diff().diff()


def f40_atxd_043_count_tr_above_2atr21_21d_d3(high, low, close):
    return f40_atxd_043_count_tr_above_2atr21_21d(high, low, close).diff().diff().diff()


def f40_atxd_044_count_tr_above_3atr21_63d_d3(high, low, close):
    return f40_atxd_044_count_tr_above_3atr21_63d(high, low, close).diff().diff().diff()


def f40_atxd_045_count_tr_above_4atr63_252d_d3(high, low, close):
    return f40_atxd_045_count_tr_above_4atr63_252d(high, low, close).diff().diff().diff()


def f40_atxd_046_longest_tr_above_atr21_run_63d_d3(high, low, close):
    return f40_atxd_046_longest_tr_above_atr21_run_63d(high, low, close).diff().diff().diff()


def f40_atxd_047_count_tr_top_decile_252d_d3(high, low, close):
    return f40_atxd_047_count_tr_top_decile_252d(high, low, close).diff().diff().diff()


def f40_atxd_048_count_tr_top5pct_1260d_d3(high, low, close):
    return f40_atxd_048_count_tr_top5pct_1260d(high, low, close).diff().diff().diff()


def f40_atxd_049_gk_over_atr21_d3(open, high, low, close):
    return f40_atxd_049_gk_over_atr21(open, high, low, close).diff().diff().diff()


def f40_atxd_050_yz_over_atr21_d3(open, high, low, close):
    return f40_atxd_050_yz_over_atr21(open, high, low, close).diff().diff().diff()


def f40_atxd_051_rs_over_atr21_d3(open, high, low, close):
    return f40_atxd_051_rs_over_atr21(open, high, low, close).diff().diff().diff()


def f40_atxd_052_atr21_over_parkinson_d3(high, low, close):
    return f40_atxd_052_atr21_over_parkinson(high, low, close).diff().diff().diff()


def f40_atxd_053_std_tr_21d_d3(high, low, close):
    return f40_atxd_053_std_tr_21d(high, low, close).diff().diff().diff()


def f40_atxd_054_std_tr_63d_d3(high, low, close):
    return f40_atxd_054_std_tr_63d(high, low, close).diff().diff().diff()


def f40_atxd_055_std_tr_252d_d3(high, low, close):
    return f40_atxd_055_std_tr_252d(high, low, close).diff().diff().diff()


def f40_atxd_056_cv_tr_21d_d3(high, low, close):
    return f40_atxd_056_cv_tr_21d(high, low, close).diff().diff().diff()


def f40_atxd_057_cv_tr_252d_d3(high, low, close):
    return f40_atxd_057_cv_tr_252d(high, low, close).diff().diff().diff()


def f40_atxd_058_skew_tr_252d_d3(high, low, close):
    return f40_atxd_058_skew_tr_252d(high, low, close).diff().diff().diff()


def f40_atxd_059_atr21_above_p10_252d_d3(high, low, close):
    return f40_atxd_059_atr21_above_p10_252d(high, low, close).diff().diff().diff()


def f40_atxd_060_atr21_above_p25_252d_d3(high, low, close):
    return f40_atxd_060_atr21_above_p25_252d(high, low, close).diff().diff().diff()


def f40_atxd_061_atr21_above_p75_252d_d3(high, low, close):
    return f40_atxd_061_atr21_above_p75_252d(high, low, close).diff().diff().diff()


def f40_atxd_062_atr21_above_p90_252d_d3(high, low, close):
    return f40_atxd_062_atr21_above_p90_252d(high, low, close).diff().diff().diff()


def f40_atxd_063_atr21_in_iqr_252d_d3(high, low, close):
    return f40_atxd_063_atr21_in_iqr_252d(high, low, close).diff().diff().diff()


def f40_atxd_064_atr21_outside_cone_252d_d3(high, low, close):
    return f40_atxd_064_atr21_outside_cone_252d(high, low, close).diff().diff().diff()


def f40_atxd_065_atr21_over_min_63d_d3(high, low, close):
    return f40_atxd_065_atr21_over_min_63d(high, low, close).diff().diff().diff()


def f40_atxd_066_atr21_over_min_252d_d3(high, low, close):
    return f40_atxd_066_atr21_over_min_252d(high, low, close).diff().diff().diff()


def f40_atxd_067_log_atr21_over_min_63d_d3(high, low, close):
    return f40_atxd_067_log_atr21_over_min_63d(high, low, close).diff().diff().diff()


def f40_atxd_068_bars_since_atr21_63d_min_d3(high, low, close):
    return f40_atxd_068_bars_since_atr21_63d_min(high, low, close).diff().diff().diff()


def f40_atxd_069_atr5_above_atr63_indicator_d3(high, low, close):
    return f40_atxd_069_atr5_above_atr63_indicator(high, low, close).diff().diff().diff()


def f40_atxd_070_count_atr5_cross_above_atr63_63d_d3(high, low, close):
    return f40_atxd_070_count_atr5_cross_above_atr63_63d(high, low, close).diff().diff().diff()


def f40_atxd_071_bars_since_atr5_above_atr63_d3(high, low, close):
    return f40_atxd_071_bars_since_atr5_above_atr63(high, low, close).diff().diff().diff()


def f40_atxd_072_bars_since_atr21_cross_above_atr63_d3(high, low, close):
    return f40_atxd_072_bars_since_atr21_cross_above_atr63(high, low, close).diff().diff().diff()


def f40_atxd_073_gap_component_mean_21d_d3(open, close):
    return f40_atxd_073_gap_component_mean_21d(open, close).diff().diff().diff()


def f40_atxd_074_body_component_mean_21d_d3(high, low):
    return f40_atxd_074_body_component_mean_21d(high, low).diff().diff().diff()


def f40_atxd_075_ratio_gap_body_63d_d3(open, high, low, close):
    return f40_atxd_075_ratio_gap_body_63d(open, high, low, close).diff().diff().diff()


ATR_EXPANSION_DYNAMICS_D3_REGISTRY_001_075 = {
    "f40_atxd_001_atr5_over_atr21_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_001_atr5_over_atr21_d3},
    "f40_atxd_002_atr21_over_atr63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_002_atr21_over_atr63_d3},
    "f40_atxd_003_atr63_over_atr252_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_003_atr63_over_atr252_d3},
    "f40_atxd_004_atr5_over_atr252_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_004_atr5_over_atr252_d3},
    "f40_atxd_005_log_atr5_over_atr252_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_005_log_atr5_over_atr252_d3},
    "f40_atxd_006_atr10_over_atr63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_006_atr10_over_atr63_d3},
    "f40_atxd_007_atr5_minus_atr21_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_007_atr5_minus_atr21_d3},
    "f40_atxd_008_atr21_minus_atr63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_008_atr21_minus_atr63_d3},
    "f40_atxd_009_rel_diff_atr5_atr21_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_009_rel_diff_atr5_atr21_d3},
    "f40_atxd_010_atr63_minus_atr252_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_010_atr63_minus_atr252_d3},
    "f40_atxd_011_atr21_pctrank_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_011_atr21_pctrank_252d_d3},
    "f40_atxd_012_atr21_pctrank_504d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_012_atr21_pctrank_504d_d3},
    "f40_atxd_013_atr21_pctrank_1260d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_013_atr21_pctrank_1260d_d3},
    "f40_atxd_014_atr63_pctrank_1260d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_014_atr63_pctrank_1260d_d3},
    "f40_atxd_015_atr5_pctrank_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_015_atr5_pctrank_252d_d3},
    "f40_atxd_016_atr252_pctrank_1260d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_016_atr252_pctrank_1260d_d3},
    "f40_atxd_017_natr21_pctrank_504d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_017_natr21_pctrank_504d_d3},
    "f40_atxd_018_atr21_zscore_504d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_018_atr21_zscore_504d_d3},
    "f40_atxd_019_natr21_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_019_natr21_d3},
    "f40_atxd_020_natr63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_020_natr63_d3},
    "f40_atxd_021_natr252_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_021_natr252_d3},
    "f40_atxd_022_log_natr21_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_022_log_natr21_d3},
    "f40_atxd_023_natr21_zscore_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_023_natr21_zscore_252d_d3},
    "f40_atxd_024_natr21_zscore_1260d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_024_natr21_zscore_1260d_d3},
    "f40_atxd_025_natr21_pctrank_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_025_natr21_pctrank_252d_d3},
    "f40_atxd_026_natr21_anchor_deviation_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_026_natr21_anchor_deviation_252d_d3},
    "f40_atxd_027_atr21_change_lag21_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_027_atr21_change_lag21_d3},
    "f40_atxd_028_atr21_change_lag63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_028_atr21_change_lag63_d3},
    "f40_atxd_029_atr21_pct_change_lag21_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_029_atr21_pct_change_lag21_d3},
    "f40_atxd_030_atr21_pct_change_lag63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_030_atr21_pct_change_lag63_d3},
    "f40_atxd_031_log_atr21_ratio_lag63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_031_log_atr21_ratio_lag63_d3},
    "f40_atxd_032_slope_atr21_63d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_032_slope_atr21_63d_d3},
    "f40_atxd_033_slope_atr21_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_033_slope_atr21_252d_d3},
    "f40_atxd_034_slope_log_atr21_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_034_slope_log_atr21_252d_d3},
    "f40_atxd_035_atr21_over_atr21_at_252d_peak_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_035_atr21_over_atr21_at_252d_peak_d3},
    "f40_atxd_036_atr21_over_atr21_at_63d_peak_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_036_atr21_over_atr21_at_63d_peak_d3},
    "f40_atxd_037_atr21_at_252d_peak_level_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_037_atr21_at_252d_peak_level_d3},
    "f40_atxd_038_log_atr21_over_at_252d_peak_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_038_log_atr21_over_at_252d_peak_d3},
    "f40_atxd_039_atr63_over_atr63_at_252d_peak_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_039_atr63_over_atr63_at_252d_peak_d3},
    "f40_atxd_040_natr21_over_at_252d_peak_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_040_natr21_over_at_252d_peak_d3},
    "f40_atxd_041_atr21_zscore_since_252d_peak_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_041_atr21_zscore_since_252d_peak_d3},
    "f40_atxd_042_bars_above_atr_at_252d_peak_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_042_bars_above_atr_at_252d_peak_d3},
    "f40_atxd_043_count_tr_above_2atr21_21d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_043_count_tr_above_2atr21_21d_d3},
    "f40_atxd_044_count_tr_above_3atr21_63d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_044_count_tr_above_3atr21_63d_d3},
    "f40_atxd_045_count_tr_above_4atr63_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_045_count_tr_above_4atr63_252d_d3},
    "f40_atxd_046_longest_tr_above_atr21_run_63d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_046_longest_tr_above_atr21_run_63d_d3},
    "f40_atxd_047_count_tr_top_decile_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_047_count_tr_top_decile_252d_d3},
    "f40_atxd_048_count_tr_top5pct_1260d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_048_count_tr_top5pct_1260d_d3},
    "f40_atxd_049_gk_over_atr21_d3": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_049_gk_over_atr21_d3},
    "f40_atxd_050_yz_over_atr21_d3": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_050_yz_over_atr21_d3},
    "f40_atxd_051_rs_over_atr21_d3": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_051_rs_over_atr21_d3},
    "f40_atxd_052_atr21_over_parkinson_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_052_atr21_over_parkinson_d3},
    "f40_atxd_053_std_tr_21d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_053_std_tr_21d_d3},
    "f40_atxd_054_std_tr_63d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_054_std_tr_63d_d3},
    "f40_atxd_055_std_tr_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_055_std_tr_252d_d3},
    "f40_atxd_056_cv_tr_21d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_056_cv_tr_21d_d3},
    "f40_atxd_057_cv_tr_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_057_cv_tr_252d_d3},
    "f40_atxd_058_skew_tr_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_058_skew_tr_252d_d3},
    "f40_atxd_059_atr21_above_p10_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_059_atr21_above_p10_252d_d3},
    "f40_atxd_060_atr21_above_p25_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_060_atr21_above_p25_252d_d3},
    "f40_atxd_061_atr21_above_p75_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_061_atr21_above_p75_252d_d3},
    "f40_atxd_062_atr21_above_p90_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_062_atr21_above_p90_252d_d3},
    "f40_atxd_063_atr21_in_iqr_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_063_atr21_in_iqr_252d_d3},
    "f40_atxd_064_atr21_outside_cone_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_064_atr21_outside_cone_252d_d3},
    "f40_atxd_065_atr21_over_min_63d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_065_atr21_over_min_63d_d3},
    "f40_atxd_066_atr21_over_min_252d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_066_atr21_over_min_252d_d3},
    "f40_atxd_067_log_atr21_over_min_63d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_067_log_atr21_over_min_63d_d3},
    "f40_atxd_068_bars_since_atr21_63d_min_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_068_bars_since_atr21_63d_min_d3},
    "f40_atxd_069_atr5_above_atr63_indicator_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_069_atr5_above_atr63_indicator_d3},
    "f40_atxd_070_count_atr5_cross_above_atr63_63d_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_070_count_atr5_cross_above_atr63_63d_d3},
    "f40_atxd_071_bars_since_atr5_above_atr63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_071_bars_since_atr5_above_atr63_d3},
    "f40_atxd_072_bars_since_atr21_cross_above_atr63_d3": {"inputs": ["high", "low", "close"], "func": f40_atxd_072_bars_since_atr21_cross_above_atr63_d3},
    "f40_atxd_073_gap_component_mean_21d_d3": {"inputs": ["open", "close"], "func": f40_atxd_073_gap_component_mean_21d_d3},
    "f40_atxd_074_body_component_mean_21d_d3": {"inputs": ["high", "low"], "func": f40_atxd_074_body_component_mean_21d_d3},
    "f40_atxd_075_ratio_gap_body_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_075_ratio_gap_body_63d_d3},
}
