"""roc_momentum_family base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Family theme:
rate-of-change (ROC) at multiple horizons (each horizon = a different *concept*:
daily/weekly/monthly/quarterly/annual/multi-year momentum), log-returns,
ROC z-scores (parametric and robust/MAD), ROC percentile ranks, ROC asymmetry
counts/skew, multi-horizon composites/spreads/dispersion/term-structure,
ROC extremes/distance-from-max, regime/persistence/acceleration/vol-of-ROC.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
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


def _rolling_mad_zscore(s, window, min_periods=None):
    """MAD-robust z-score: (s - median) / (1.4826 * MAD)."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    mad = (s - med).abs().rolling(window, min_periods=min_periods).median()
    return (s - med) / (1.4826 * mad).replace(0, np.nan)


# ============================================================
# Bucket A — ROC at distinct horizons (001-015)
# Each horizon encodes a different *concept* of momentum:
# 1d=next-day, 2d/3d=micro, 5d=weekly, 10d=biweekly, 15d=3-week,
# 21d=monthly, 42d=2-month, 63d=quarterly, 126d=half-year,
# 189d=9-month, 252d=annual, 504d=2-year, 756d=3-year, 1260d=5-year.
# ============================================================

def f31_rcmf_001_roc_1d(close: pd.Series) -> pd.Series:
    """1-day rate of change of close — next-day momentum impulse."""
    return close.pct_change(1)


def f31_rcmf_002_roc_2d(close: pd.Series) -> pd.Series:
    """2-day ROC — micro-momentum across two sessions."""
    return close.pct_change(2)


def f31_rcmf_003_roc_3d(close: pd.Series) -> pd.Series:
    """3-day ROC — three-session impulse."""
    return close.pct_change(3)


def f31_rcmf_004_roc_5d(close: pd.Series) -> pd.Series:
    """5-day ROC — weekly momentum."""
    return close.pct_change(WDAYS)


def f31_rcmf_005_roc_10d(close: pd.Series) -> pd.Series:
    """10-day ROC — biweekly momentum."""
    return close.pct_change(10)


def f31_rcmf_006_roc_15d(close: pd.Series) -> pd.Series:
    """15-day ROC — three-week momentum (between weekly and monthly)."""
    return close.pct_change(15)


def f31_rcmf_007_roc_21d(close: pd.Series) -> pd.Series:
    """21-day ROC — monthly momentum."""
    return close.pct_change(MDAYS)


def f31_rcmf_008_roc_42d(close: pd.Series) -> pd.Series:
    """42-day ROC — two-month momentum."""
    return close.pct_change(42)


def f31_rcmf_009_roc_63d(close: pd.Series) -> pd.Series:
    """63-day ROC — quarterly momentum."""
    return close.pct_change(QDAYS)


def f31_rcmf_010_roc_126d(close: pd.Series) -> pd.Series:
    """126-day ROC — half-year momentum."""
    return close.pct_change(126)


def f31_rcmf_011_roc_189d(close: pd.Series) -> pd.Series:
    """189-day ROC — three-quarter (9-month) momentum."""
    return close.pct_change(189)


def f31_rcmf_012_roc_252d(close: pd.Series) -> pd.Series:
    """252-day ROC — annual momentum / 1-year price change."""
    return close.pct_change(YDAYS)


def f31_rcmf_013_roc_504d(close: pd.Series) -> pd.Series:
    """504-day ROC — biennial momentum / 2-year price change."""
    return close.pct_change(DDAYS_2Y)


def f31_rcmf_014_roc_756d(close: pd.Series) -> pd.Series:
    """756-day ROC — triennial momentum / 3-year price change."""
    return close.pct_change(DDAYS_3Y)


def f31_rcmf_015_roc_1260d(close: pd.Series) -> pd.Series:
    """1260-day ROC — five-year momentum / multi-cycle move."""
    return close.pct_change(DDAYS_5Y)


# ============================================================
# Bucket B — Log-returns at distinct horizons (016-030)
# Log scale is a different *measurement* hypothesis — matters at extreme moves
# (compounding-symmetric, additivity, tail behavior differs from pct_change).
# ============================================================

def f31_rcmf_016_log_return_1d(close: pd.Series) -> pd.Series:
    """1-day log return — symmetric daily impulse."""
    return _safe_log(close).diff(1)


def f31_rcmf_017_log_return_2d(close: pd.Series) -> pd.Series:
    """2-day log return."""
    return _safe_log(close).diff(2)


def f31_rcmf_018_log_return_3d(close: pd.Series) -> pd.Series:
    """3-day log return."""
    return _safe_log(close).diff(3)


def f31_rcmf_019_log_return_5d(close: pd.Series) -> pd.Series:
    """5-day log return — weekly log momentum."""
    return _safe_log(close).diff(WDAYS)


def f31_rcmf_020_log_return_10d(close: pd.Series) -> pd.Series:
    """10-day log return — biweekly log momentum."""
    return _safe_log(close).diff(10)


def f31_rcmf_021_log_return_15d(close: pd.Series) -> pd.Series:
    """15-day log return — three-week log momentum."""
    return _safe_log(close).diff(15)


def f31_rcmf_022_log_return_21d(close: pd.Series) -> pd.Series:
    """21-day log return — monthly log momentum."""
    return _safe_log(close).diff(MDAYS)


def f31_rcmf_023_log_return_42d(close: pd.Series) -> pd.Series:
    """42-day log return — two-month log momentum."""
    return _safe_log(close).diff(42)


def f31_rcmf_024_log_return_63d(close: pd.Series) -> pd.Series:
    """63-day log return — quarterly log momentum."""
    return _safe_log(close).diff(QDAYS)


def f31_rcmf_025_log_return_126d(close: pd.Series) -> pd.Series:
    """126-day log return — half-year log momentum."""
    return _safe_log(close).diff(126)


def f31_rcmf_026_log_return_189d(close: pd.Series) -> pd.Series:
    """189-day log return — three-quarter log momentum."""
    return _safe_log(close).diff(189)


def f31_rcmf_027_log_return_252d(close: pd.Series) -> pd.Series:
    """252-day log return — annual log momentum."""
    return _safe_log(close).diff(YDAYS)


def f31_rcmf_028_log_return_504d(close: pd.Series) -> pd.Series:
    """504-day log return — biennial log momentum."""
    return _safe_log(close).diff(DDAYS_2Y)


def f31_rcmf_029_log_return_756d(close: pd.Series) -> pd.Series:
    """756-day log return — triennial log momentum."""
    return _safe_log(close).diff(DDAYS_3Y)


def f31_rcmf_030_log_return_1260d(close: pd.Series) -> pd.Series:
    """1260-day log return — five-year log momentum."""
    return _safe_log(close).diff(DDAYS_5Y)


# ============================================================
# Bucket C — ROC z-scores (031-050)
# Different (short_ROC, ref_window) pairs encode different anomalousness
# hypotheses (anomalous-weekly-vs-quarter, anomalous-monthly-vs-year, etc.),
# plus MAD-robust variants for tail-resistant overbought reading.
# ============================================================

def f31_rcmf_031_roc_1d_zscore_21d(close: pd.Series) -> pd.Series:
    """Z-score of 1d ROC within trailing 21d distribution — anomalous daily move (monthly ref)."""
    r = close.pct_change(1)
    return _rolling_zscore(r, MDAYS)


def f31_rcmf_032_roc_1d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 1d ROC within trailing 63d distribution — anomalous daily move (quarterly ref)."""
    r = close.pct_change(1)
    return _rolling_zscore(r, QDAYS)


def f31_rcmf_033_roc_1d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 1d ROC within trailing 252d distribution — anomalous daily move (annual ref)."""
    r = close.pct_change(1)
    return _rolling_zscore(r, YDAYS)


def f31_rcmf_034_roc_5d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 5d ROC in trailing 63d window — weekly momentum vs quarterly distribution."""
    r = close.pct_change(WDAYS)
    return _rolling_zscore(r, QDAYS)


def f31_rcmf_035_roc_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5d ROC in trailing 252d window — weekly momentum vs annual distribution."""
    r = close.pct_change(WDAYS)
    return _rolling_zscore(r, YDAYS)


def f31_rcmf_036_roc_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d ROC in trailing 252d window — monthly momentum vs annual distribution."""
    r = close.pct_change(MDAYS)
    return _rolling_zscore(r, YDAYS)


def f31_rcmf_037_roc_21d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 21d ROC in trailing 504d window — monthly momentum vs biennial distribution."""
    r = close.pct_change(MDAYS)
    return _rolling_zscore(r, DDAYS_2Y)


def f31_rcmf_038_roc_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d ROC in trailing 252d window — quarterly momentum vs annual distribution."""
    r = close.pct_change(QDAYS)
    return _rolling_zscore(r, YDAYS)


def f31_rcmf_039_roc_63d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 63d ROC in trailing 504d window — quarterly momentum vs biennial distribution."""
    r = close.pct_change(QDAYS)
    return _rolling_zscore(r, DDAYS_2Y)


def f31_rcmf_040_roc_126d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 126d ROC in trailing 504d window — half-year momentum vs biennial distribution."""
    r = close.pct_change(126)
    return _rolling_zscore(r, DDAYS_2Y)


def f31_rcmf_041_roc_252d_zscore_756d(close: pd.Series) -> pd.Series:
    """Z-score of 252d ROC in trailing 756d window — annual momentum vs 3-year distribution."""
    r = close.pct_change(YDAYS)
    return _rolling_zscore(r, DDAYS_3Y)


def f31_rcmf_042_roc_252d_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 252d ROC in trailing 1260d window — annual momentum vs 5-year distribution."""
    r = close.pct_change(YDAYS)
    return _rolling_zscore(r, DDAYS_5Y)


def f31_rcmf_043_roc_1d_mad_zscore_63d(close: pd.Series) -> pd.Series:
    """Robust MAD z-score of 1d ROC in trailing 63d window — outlier-resistant daily move."""
    r = close.pct_change(1)
    return _rolling_mad_zscore(r, QDAYS)


def f31_rcmf_044_roc_1d_mad_zscore_252d(close: pd.Series) -> pd.Series:
    """Robust MAD z-score of 1d ROC in trailing 252d window — outlier-resistant daily move (annual ref)."""
    r = close.pct_change(1)
    return _rolling_mad_zscore(r, YDAYS)


def f31_rcmf_045_roc_5d_mad_zscore_252d(close: pd.Series) -> pd.Series:
    """Robust MAD z-score of 5d ROC in trailing 252d window — outlier-resistant weekly momentum."""
    r = close.pct_change(WDAYS)
    return _rolling_mad_zscore(r, YDAYS)


def f31_rcmf_046_roc_21d_mad_zscore_252d(close: pd.Series) -> pd.Series:
    """Robust MAD z-score of 21d ROC in trailing 252d window — outlier-resistant monthly momentum."""
    r = close.pct_change(MDAYS)
    return _rolling_mad_zscore(r, YDAYS)


def f31_rcmf_047_roc_63d_mad_zscore_504d(close: pd.Series) -> pd.Series:
    """Robust MAD z-score of 63d ROC in trailing 504d window — outlier-resistant quarterly momentum."""
    r = close.pct_change(QDAYS)
    return _rolling_mad_zscore(r, DDAYS_2Y)


def f31_rcmf_048_roc_252d_mad_zscore_1260d(close: pd.Series) -> pd.Series:
    """Robust MAD z-score of 252d ROC in trailing 1260d window — outlier-resistant annual momentum."""
    r = close.pct_change(YDAYS)
    return _rolling_mad_zscore(r, DDAYS_5Y)


def f31_rcmf_049_log_return_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d log return in trailing 252d window — anomalous monthly log-momentum."""
    r = _safe_log(close).diff(MDAYS)
    return _rolling_zscore(r, YDAYS)


def f31_rcmf_050_log_return_63d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 63d log return in trailing 504d window — anomalous quarterly log-momentum."""
    r = _safe_log(close).diff(QDAYS)
    return _rolling_zscore(r, DDAYS_2Y)


# ============================================================
# Bucket D — ROC percentile ranks (051-065)
# Empirical rank of trailing-N-day ROC in trailing-M-day window.
# Non-parametric measure — different shape hypothesis than z-score.
# ============================================================

def f31_rcmf_051_roc_1d_percentile_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 1d ROC in trailing 63d — daily-move rank vs quarter."""
    r = close.pct_change(1)
    return r.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)


def f31_rcmf_052_roc_1d_percentile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 1d ROC in trailing 252d — daily-move rank vs year."""
    r = close.pct_change(1)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f31_rcmf_053_roc_5d_percentile_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d ROC in trailing 63d — weekly-momentum rank vs quarter."""
    r = close.pct_change(WDAYS)
    return r.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)


def f31_rcmf_054_roc_5d_percentile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d ROC in trailing 252d — weekly-momentum rank vs year."""
    r = close.pct_change(WDAYS)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f31_rcmf_055_roc_21d_percentile_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d ROC in trailing 63d — monthly-momentum rank vs quarter."""
    r = close.pct_change(MDAYS)
    return r.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)


def f31_rcmf_056_roc_21d_percentile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d ROC in trailing 252d — monthly-momentum rank vs year."""
    r = close.pct_change(MDAYS)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f31_rcmf_057_roc_21d_percentile_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d ROC in trailing 504d — monthly-momentum rank vs biennial."""
    r = close.pct_change(MDAYS)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)


def f31_rcmf_058_roc_63d_percentile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d ROC in trailing 252d — quarterly-momentum rank vs year."""
    r = close.pct_change(QDAYS)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f31_rcmf_059_roc_63d_percentile_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d ROC in trailing 504d — quarterly-momentum rank vs biennial."""
    r = close.pct_change(QDAYS)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)


def f31_rcmf_060_roc_126d_percentile_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 126d ROC in trailing 504d — half-year-momentum rank vs biennial."""
    r = close.pct_change(126)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)


def f31_rcmf_061_roc_252d_percentile_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d ROC in trailing 504d — annual-momentum rank vs biennial."""
    r = close.pct_change(YDAYS)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)


def f31_rcmf_062_roc_252d_percentile_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d ROC in trailing 1260d — annual-momentum rank vs 5-year."""
    r = close.pct_change(YDAYS)
    return r.rolling(DDAYS_5Y, min_periods=YDAYS).rank(pct=True)


def f31_rcmf_063_roc_504d_percentile_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of 504d ROC in trailing 1260d — biennial-momentum rank vs 5-year."""
    r = close.pct_change(DDAYS_2Y)
    return r.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).rank(pct=True)


def f31_rcmf_064_log_return_21d_percentile_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d log return in trailing 252d — monthly log-momentum rank vs year."""
    r = _safe_log(close).diff(MDAYS)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f31_rcmf_065_log_return_63d_percentile_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d log return in trailing 504d — quarterly log-momentum rank vs biennial."""
    r = _safe_log(close).diff(QDAYS)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)


# ============================================================
# Bucket E — ROC asymmetry / skew / up-vs-down counts (066-075)
# Distinct concept: not magnitude of momentum, but *composition* — how many
# up days vs down days, biggest single up vs biggest single down, return skew.
# ============================================================

def f31_rcmf_066_count_positive_1d_returns_in_21d(close: pd.Series) -> pd.Series:
    """Count of positive 1d returns in trailing 21d — bullish-day count over the month."""
    r = close.pct_change(1)
    return (r > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f31_rcmf_067_count_negative_1d_returns_in_21d(close: pd.Series) -> pd.Series:
    """Count of negative 1d returns in trailing 21d — bearish-day count over the month."""
    r = close.pct_change(1)
    return (r < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f31_rcmf_068_count_positive_1d_returns_in_63d(close: pd.Series) -> pd.Series:
    """Count of positive 1d returns in trailing 63d — bullish-day count over the quarter."""
    r = close.pct_change(1)
    return (r > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f31_rcmf_069_count_negative_1d_returns_in_63d(close: pd.Series) -> pd.Series:
    """Count of negative 1d returns in trailing 63d — bearish-day count over the quarter."""
    r = close.pct_change(1)
    return (r < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f31_rcmf_070_count_positive_1d_returns_in_252d(close: pd.Series) -> pd.Series:
    """Count of positive 1d returns in trailing 252d — bullish-day count over the year."""
    r = close.pct_change(1)
    return (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f31_rcmf_071_max_up_1d_return_in_21d(close: pd.Series) -> pd.Series:
    """Max single-day positive 1d return in trailing 21d — biggest up-day of the month."""
    r = close.pct_change(1)
    return r.rolling(MDAYS, min_periods=WDAYS).max()


def f31_rcmf_072_max_down_1d_return_in_21d(close: pd.Series) -> pd.Series:
    """Min (most-negative) single-day 1d return in trailing 21d — worst down-day of the month."""
    r = close.pct_change(1)
    return r.rolling(MDAYS, min_periods=WDAYS).min()


def f31_rcmf_073_max_up_5d_return_in_63d(close: pd.Series) -> pd.Series:
    """Max 5d ROC over trailing 63d — best week of the quarter."""
    r = close.pct_change(WDAYS)
    return r.rolling(QDAYS, min_periods=MDAYS).max()


def f31_rcmf_074_max_down_5d_return_in_63d(close: pd.Series) -> pd.Series:
    """Min 5d ROC over trailing 63d — worst week of the quarter."""
    r = close.pct_change(WDAYS)
    return r.rolling(QDAYS, min_periods=MDAYS).min()


def f31_rcmf_075_max_up_21d_return_in_252d(close: pd.Series) -> pd.Series:
    """Max 21d ROC over trailing 252d — best month of the year."""
    r = close.pct_change(MDAYS)
    return r.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
#                         REGISTRY 001-075
# ============================================================

ROC_MOMENTUM_FAMILY_BASE_REGISTRY_001_075 = {
    "f31_rcmf_001_roc_1d": {"inputs": ["close"], "func": f31_rcmf_001_roc_1d},
    "f31_rcmf_002_roc_2d": {"inputs": ["close"], "func": f31_rcmf_002_roc_2d},
    "f31_rcmf_003_roc_3d": {"inputs": ["close"], "func": f31_rcmf_003_roc_3d},
    "f31_rcmf_004_roc_5d": {"inputs": ["close"], "func": f31_rcmf_004_roc_5d},
    "f31_rcmf_005_roc_10d": {"inputs": ["close"], "func": f31_rcmf_005_roc_10d},
    "f31_rcmf_006_roc_15d": {"inputs": ["close"], "func": f31_rcmf_006_roc_15d},
    "f31_rcmf_007_roc_21d": {"inputs": ["close"], "func": f31_rcmf_007_roc_21d},
    "f31_rcmf_008_roc_42d": {"inputs": ["close"], "func": f31_rcmf_008_roc_42d},
    "f31_rcmf_009_roc_63d": {"inputs": ["close"], "func": f31_rcmf_009_roc_63d},
    "f31_rcmf_010_roc_126d": {"inputs": ["close"], "func": f31_rcmf_010_roc_126d},
    "f31_rcmf_011_roc_189d": {"inputs": ["close"], "func": f31_rcmf_011_roc_189d},
    "f31_rcmf_012_roc_252d": {"inputs": ["close"], "func": f31_rcmf_012_roc_252d},
    "f31_rcmf_013_roc_504d": {"inputs": ["close"], "func": f31_rcmf_013_roc_504d},
    "f31_rcmf_014_roc_756d": {"inputs": ["close"], "func": f31_rcmf_014_roc_756d},
    "f31_rcmf_015_roc_1260d": {"inputs": ["close"], "func": f31_rcmf_015_roc_1260d},
    "f31_rcmf_016_log_return_1d": {"inputs": ["close"], "func": f31_rcmf_016_log_return_1d},
    "f31_rcmf_017_log_return_2d": {"inputs": ["close"], "func": f31_rcmf_017_log_return_2d},
    "f31_rcmf_018_log_return_3d": {"inputs": ["close"], "func": f31_rcmf_018_log_return_3d},
    "f31_rcmf_019_log_return_5d": {"inputs": ["close"], "func": f31_rcmf_019_log_return_5d},
    "f31_rcmf_020_log_return_10d": {"inputs": ["close"], "func": f31_rcmf_020_log_return_10d},
    "f31_rcmf_021_log_return_15d": {"inputs": ["close"], "func": f31_rcmf_021_log_return_15d},
    "f31_rcmf_022_log_return_21d": {"inputs": ["close"], "func": f31_rcmf_022_log_return_21d},
    "f31_rcmf_023_log_return_42d": {"inputs": ["close"], "func": f31_rcmf_023_log_return_42d},
    "f31_rcmf_024_log_return_63d": {"inputs": ["close"], "func": f31_rcmf_024_log_return_63d},
    "f31_rcmf_025_log_return_126d": {"inputs": ["close"], "func": f31_rcmf_025_log_return_126d},
    "f31_rcmf_026_log_return_189d": {"inputs": ["close"], "func": f31_rcmf_026_log_return_189d},
    "f31_rcmf_027_log_return_252d": {"inputs": ["close"], "func": f31_rcmf_027_log_return_252d},
    "f31_rcmf_028_log_return_504d": {"inputs": ["close"], "func": f31_rcmf_028_log_return_504d},
    "f31_rcmf_029_log_return_756d": {"inputs": ["close"], "func": f31_rcmf_029_log_return_756d},
    "f31_rcmf_030_log_return_1260d": {"inputs": ["close"], "func": f31_rcmf_030_log_return_1260d},
    "f31_rcmf_031_roc_1d_zscore_21d": {"inputs": ["close"], "func": f31_rcmf_031_roc_1d_zscore_21d},
    "f31_rcmf_032_roc_1d_zscore_63d": {"inputs": ["close"], "func": f31_rcmf_032_roc_1d_zscore_63d},
    "f31_rcmf_033_roc_1d_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_033_roc_1d_zscore_252d},
    "f31_rcmf_034_roc_5d_zscore_63d": {"inputs": ["close"], "func": f31_rcmf_034_roc_5d_zscore_63d},
    "f31_rcmf_035_roc_5d_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_035_roc_5d_zscore_252d},
    "f31_rcmf_036_roc_21d_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_036_roc_21d_zscore_252d},
    "f31_rcmf_037_roc_21d_zscore_504d": {"inputs": ["close"], "func": f31_rcmf_037_roc_21d_zscore_504d},
    "f31_rcmf_038_roc_63d_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_038_roc_63d_zscore_252d},
    "f31_rcmf_039_roc_63d_zscore_504d": {"inputs": ["close"], "func": f31_rcmf_039_roc_63d_zscore_504d},
    "f31_rcmf_040_roc_126d_zscore_504d": {"inputs": ["close"], "func": f31_rcmf_040_roc_126d_zscore_504d},
    "f31_rcmf_041_roc_252d_zscore_756d": {"inputs": ["close"], "func": f31_rcmf_041_roc_252d_zscore_756d},
    "f31_rcmf_042_roc_252d_zscore_1260d": {"inputs": ["close"], "func": f31_rcmf_042_roc_252d_zscore_1260d},
    "f31_rcmf_043_roc_1d_mad_zscore_63d": {"inputs": ["close"], "func": f31_rcmf_043_roc_1d_mad_zscore_63d},
    "f31_rcmf_044_roc_1d_mad_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_044_roc_1d_mad_zscore_252d},
    "f31_rcmf_045_roc_5d_mad_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_045_roc_5d_mad_zscore_252d},
    "f31_rcmf_046_roc_21d_mad_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_046_roc_21d_mad_zscore_252d},
    "f31_rcmf_047_roc_63d_mad_zscore_504d": {"inputs": ["close"], "func": f31_rcmf_047_roc_63d_mad_zscore_504d},
    "f31_rcmf_048_roc_252d_mad_zscore_1260d": {"inputs": ["close"], "func": f31_rcmf_048_roc_252d_mad_zscore_1260d},
    "f31_rcmf_049_log_return_21d_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_049_log_return_21d_zscore_252d},
    "f31_rcmf_050_log_return_63d_zscore_504d": {"inputs": ["close"], "func": f31_rcmf_050_log_return_63d_zscore_504d},
    "f31_rcmf_051_roc_1d_percentile_63d": {"inputs": ["close"], "func": f31_rcmf_051_roc_1d_percentile_63d},
    "f31_rcmf_052_roc_1d_percentile_252d": {"inputs": ["close"], "func": f31_rcmf_052_roc_1d_percentile_252d},
    "f31_rcmf_053_roc_5d_percentile_63d": {"inputs": ["close"], "func": f31_rcmf_053_roc_5d_percentile_63d},
    "f31_rcmf_054_roc_5d_percentile_252d": {"inputs": ["close"], "func": f31_rcmf_054_roc_5d_percentile_252d},
    "f31_rcmf_055_roc_21d_percentile_63d": {"inputs": ["close"], "func": f31_rcmf_055_roc_21d_percentile_63d},
    "f31_rcmf_056_roc_21d_percentile_252d": {"inputs": ["close"], "func": f31_rcmf_056_roc_21d_percentile_252d},
    "f31_rcmf_057_roc_21d_percentile_504d": {"inputs": ["close"], "func": f31_rcmf_057_roc_21d_percentile_504d},
    "f31_rcmf_058_roc_63d_percentile_252d": {"inputs": ["close"], "func": f31_rcmf_058_roc_63d_percentile_252d},
    "f31_rcmf_059_roc_63d_percentile_504d": {"inputs": ["close"], "func": f31_rcmf_059_roc_63d_percentile_504d},
    "f31_rcmf_060_roc_126d_percentile_504d": {"inputs": ["close"], "func": f31_rcmf_060_roc_126d_percentile_504d},
    "f31_rcmf_061_roc_252d_percentile_504d": {"inputs": ["close"], "func": f31_rcmf_061_roc_252d_percentile_504d},
    "f31_rcmf_062_roc_252d_percentile_1260d": {"inputs": ["close"], "func": f31_rcmf_062_roc_252d_percentile_1260d},
    "f31_rcmf_063_roc_504d_percentile_1260d": {"inputs": ["close"], "func": f31_rcmf_063_roc_504d_percentile_1260d},
    "f31_rcmf_064_log_return_21d_percentile_252d": {"inputs": ["close"], "func": f31_rcmf_064_log_return_21d_percentile_252d},
    "f31_rcmf_065_log_return_63d_percentile_504d": {"inputs": ["close"], "func": f31_rcmf_065_log_return_63d_percentile_504d},
    "f31_rcmf_066_count_positive_1d_returns_in_21d": {"inputs": ["close"], "func": f31_rcmf_066_count_positive_1d_returns_in_21d},
    "f31_rcmf_067_count_negative_1d_returns_in_21d": {"inputs": ["close"], "func": f31_rcmf_067_count_negative_1d_returns_in_21d},
    "f31_rcmf_068_count_positive_1d_returns_in_63d": {"inputs": ["close"], "func": f31_rcmf_068_count_positive_1d_returns_in_63d},
    "f31_rcmf_069_count_negative_1d_returns_in_63d": {"inputs": ["close"], "func": f31_rcmf_069_count_negative_1d_returns_in_63d},
    "f31_rcmf_070_count_positive_1d_returns_in_252d": {"inputs": ["close"], "func": f31_rcmf_070_count_positive_1d_returns_in_252d},
    "f31_rcmf_071_max_up_1d_return_in_21d": {"inputs": ["close"], "func": f31_rcmf_071_max_up_1d_return_in_21d},
    "f31_rcmf_072_max_down_1d_return_in_21d": {"inputs": ["close"], "func": f31_rcmf_072_max_down_1d_return_in_21d},
    "f31_rcmf_073_max_up_5d_return_in_63d": {"inputs": ["close"], "func": f31_rcmf_073_max_up_5d_return_in_63d},
    "f31_rcmf_074_max_down_5d_return_in_63d": {"inputs": ["close"], "func": f31_rcmf_074_max_down_5d_return_in_63d},
    "f31_rcmf_075_max_up_21d_return_in_252d": {"inputs": ["close"], "func": f31_rcmf_075_max_up_21d_return_in_252d},
}
