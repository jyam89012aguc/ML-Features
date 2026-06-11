"""
07_peak_to_trough — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change / slope of base peak-to-trough and recovery-fraction concepts
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes a .diff(n) or slope/pct-change of a base-feature concept.
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        xm = x.mean()
        num = ((xi - xi_m) * (x - xm)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _recovery_fraction(close: pd.Series, peak: pd.Series, trough: pd.Series) -> pd.Series:
    span = peak - trough
    return _safe_div(close - trough, span)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def ptt_drv2_001_recovery_fraction_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252d recovery fraction (velocity of retracement change)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    return rf.diff(5)


def ptt_drv2_002_recovery_fraction_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d recovery fraction."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    rf = _recovery_fraction(close, pk, tr)
    return rf.diff(5)


def ptt_drv2_003_ptt_ratio_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day peak-trough ratio (rate of swing expansion/contraction)."""
    r = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return r.diff(5)


def ptt_drv2_004_ptt_ratio_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day peak-trough ratio."""
    r = _safe_div(_rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return r.diff(5)


def ptt_drv2_005_log_ptt_span_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of log(252d peak/trough) — log-scale amplitude velocity."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    log_span = _log_safe(pk) - _log_safe(tr)
    return log_span.diff(5)


def ptt_drv2_006_recovery_fraction_252d_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 252d recovery fraction over trailing 21 days."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    return _linslope(rf, _TD_MON)


def ptt_drv2_007_recovery_fraction_252d_63d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 252d recovery fraction over trailing 63 days."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    return _linslope(rf, _TD_QTR)


def ptt_drv2_008_span_pct_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day (peak-trough)/trough percent span."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    span = _safe_div(pk - tr, tr)
    return span.diff(5)


def ptt_drv2_009_span_pct_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day peak-trough percent span."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    span = _safe_div(pk - tr, tr)
    return span.diff(5)


def ptt_drv2_010_close_to_peak_ratio_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close/252d-peak ratio (speed of peak erosion)."""
    pk = _rolling_max(close, _TD_YEAR)
    ratio = _safe_div(close, pk)
    return ratio.diff(5)


def ptt_drv2_011_close_to_trough_ratio_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close/252d-trough ratio (speed of trough bounce)."""
    tr = _rolling_min(close, _TD_YEAR)
    ratio = _safe_div(close, tr)
    return ratio.diff(5)


def ptt_drv2_012_recovery_fraction_expanding_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of all-time (expanding) recovery fraction."""
    pk = close.expanding(min_periods=1).max()
    tr = close.expanding(min_periods=1).min()
    rf = _recovery_fraction(close, pk, tr)
    return rf.diff(5)


def ptt_drv2_013_ptt_ratio_expanding_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of all-time (expanding) peak-trough ratio."""
    pk = close.expanding(min_periods=1).max()
    tr = close.expanding(min_periods=1).min()
    r = _safe_div(pk, tr)
    return r.diff(5)


def ptt_drv2_014_recovery_fraction_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252d recovery fraction (monthly retracement pace)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    return rf.diff(_TD_MON)


def ptt_drv2_015_vol_adj_span_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of vol-adjusted 252d peak-trough span."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    span = _safe_div(pk - tr, tr)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    va = _safe_div(span, vol)
    return va.diff(5)


def ptt_drv2_016_trough_age_fraction_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of trough-freshness fraction (days-since-trough / 252)."""
    tr = _rolling_min(close, _TD_YEAR)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    last_tr = idx.where(at_trough.astype(bool)).ffill()
    freshness = (idx - last_tr) / float(_TD_YEAR)
    return freshness.diff(5)


def ptt_drv2_017_recovery_fraction_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of rolling z-score of 252d recovery fraction."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    z = _zscore_rolling(rf, _TD_YEAR)
    return z.diff(5)


def ptt_drv2_018_composite_recovery_frac_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite recovery fraction (50% 21d + 30% 63d + 20% 252d)."""
    rf21 = _recovery_fraction(close, _rolling_max(close, _TD_MON), _rolling_min(close, _TD_MON))
    rf63 = _recovery_fraction(close, _rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    rf252 = _recovery_fraction(close, _rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    composite = 0.5 * rf21 + 0.3 * rf63 + 0.2 * rf252
    return composite.diff(5)


def ptt_drv2_019_ptt_span_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of 252d peak-trough span."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    span = _safe_div(pk - tr, tr)
    rank = span.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(5)


def ptt_drv2_020_log_recovery_fraction_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of log-space recovery fraction (log(close/trough)/log(peak/trough))."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    num = _log_safe(close) - _log_safe(tr)
    den = _log_safe(pk) - _log_safe(tr)
    log_rf = _safe_div(num, den)
    return log_rf.diff(5)


def ptt_drv2_021_vwap_recovery_frac_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 252d VWAP recovery fraction."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    pk = _rolling_max(vwap, _TD_YEAR)
    tr = _rolling_min(vwap, _TD_YEAR)
    rf = _recovery_fraction(vwap, pk, tr)
    return rf.diff(5)


def ptt_drv2_022_atr_normalized_span_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR-normalized 252d peak-trough span."""
    atr = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    ratio = _safe_div(pk - tr, atr)
    return ratio.diff(5)


def ptt_drv2_023_trough_to_mean_balance_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of trough-to-mean-to-peak asymmetry ratio."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    mu = _rolling_mean(close, _TD_YEAR)
    asym = _safe_div(pk - mu, mu - tr)
    return asym.diff(5)


def ptt_drv2_024_recovery_fraction_pct_rank_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of 252d recovery fraction."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    rank = rf.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(5)


def ptt_drv2_025_multi_window_ptt_composite_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite PTT ratio (40% 21d + 35% 63d + 25% 252d)."""
    r21 = _safe_div(_rolling_max(close, _TD_MON), _rolling_min(close, _TD_MON))
    r63 = _safe_div(_rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    r252 = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    composite = 0.40 * r21 + 0.35 * r63 + 0.25 * r252
    return composite.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

PEAK_TO_TROUGH_REGISTRY_2ND_DERIVATIVES = {
    "ptt_drv2_001_recovery_fraction_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_001_recovery_fraction_252d_5d_diff},
    "ptt_drv2_002_recovery_fraction_63d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_002_recovery_fraction_63d_5d_diff},
    "ptt_drv2_003_ptt_ratio_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_003_ptt_ratio_252d_5d_diff},
    "ptt_drv2_004_ptt_ratio_63d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_004_ptt_ratio_63d_5d_diff},
    "ptt_drv2_005_log_ptt_span_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_005_log_ptt_span_252d_5d_diff},
    "ptt_drv2_006_recovery_fraction_252d_21d_slope": {"inputs": ["close"], "func": ptt_drv2_006_recovery_fraction_252d_21d_slope},
    "ptt_drv2_007_recovery_fraction_252d_63d_slope": {"inputs": ["close"], "func": ptt_drv2_007_recovery_fraction_252d_63d_slope},
    "ptt_drv2_008_span_pct_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_008_span_pct_252d_5d_diff},
    "ptt_drv2_009_span_pct_63d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_009_span_pct_63d_5d_diff},
    "ptt_drv2_010_close_to_peak_ratio_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_010_close_to_peak_ratio_252d_5d_diff},
    "ptt_drv2_011_close_to_trough_ratio_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_011_close_to_trough_ratio_252d_5d_diff},
    "ptt_drv2_012_recovery_fraction_expanding_5d_diff": {"inputs": ["close"], "func": ptt_drv2_012_recovery_fraction_expanding_5d_diff},
    "ptt_drv2_013_ptt_ratio_expanding_5d_diff": {"inputs": ["close"], "func": ptt_drv2_013_ptt_ratio_expanding_5d_diff},
    "ptt_drv2_014_recovery_fraction_252d_21d_diff": {"inputs": ["close"], "func": ptt_drv2_014_recovery_fraction_252d_21d_diff},
    "ptt_drv2_015_vol_adj_span_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_015_vol_adj_span_252d_5d_diff},
    "ptt_drv2_016_trough_age_fraction_5d_diff": {"inputs": ["close"], "func": ptt_drv2_016_trough_age_fraction_5d_diff},
    "ptt_drv2_017_recovery_fraction_zscore_5d_diff": {"inputs": ["close"], "func": ptt_drv2_017_recovery_fraction_zscore_5d_diff},
    "ptt_drv2_018_composite_recovery_frac_5d_diff": {"inputs": ["close"], "func": ptt_drv2_018_composite_recovery_frac_5d_diff},
    "ptt_drv2_019_ptt_span_pct_rank_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_019_ptt_span_pct_rank_252d_5d_diff},
    "ptt_drv2_020_log_recovery_fraction_252d_5d_diff": {"inputs": ["close"], "func": ptt_drv2_020_log_recovery_fraction_252d_5d_diff},
    "ptt_drv2_021_vwap_recovery_frac_5d_diff": {"inputs": ["close", "volume"], "func": ptt_drv2_021_vwap_recovery_frac_5d_diff},
    "ptt_drv2_022_atr_normalized_span_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": ptt_drv2_022_atr_normalized_span_252d_5d_diff},
    "ptt_drv2_023_trough_to_mean_balance_5d_diff": {"inputs": ["close"], "func": ptt_drv2_023_trough_to_mean_balance_5d_diff},
    "ptt_drv2_024_recovery_fraction_pct_rank_5d_diff": {"inputs": ["close"], "func": ptt_drv2_024_recovery_fraction_pct_rank_5d_diff},
    "ptt_drv2_025_multi_window_ptt_composite_5d_diff": {"inputs": ["close"], "func": ptt_drv2_025_multi_window_ptt_composite_5d_diff},
}
