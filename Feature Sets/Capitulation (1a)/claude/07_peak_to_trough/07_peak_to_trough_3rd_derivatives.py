"""
07_peak_to_trough — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of the 2nd-derivative peak-to-trough features (acceleration of acceleration)
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature takes a 2nd-derivative concept and applies a further .diff(n) or slope.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def ptt_drv3_001_recovery_fraction_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252d recovery fraction) — acceleration of retracement velocity."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    drv2 = rf.diff(5)
    return drv2.diff(5)


def ptt_drv3_002_recovery_fraction_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63d recovery fraction)."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    rf = _recovery_fraction(close, pk, tr)
    drv2 = rf.diff(5)
    return drv2.diff(5)


def ptt_drv3_003_ptt_ratio_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252d peak-trough ratio) — swing expansion convexity."""
    r = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    drv2 = r.diff(5)
    return drv2.diff(5)


def ptt_drv3_004_ptt_ratio_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63d peak-trough ratio)."""
    r = _safe_div(_rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    drv2 = r.diff(5)
    return drv2.diff(5)


def ptt_drv3_005_log_ptt_span_252d_diff_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of log(252d peak/trough) span."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    log_span = _log_safe(pk) - _log_safe(tr)
    drv2 = log_span.diff(5)
    return _linslope(drv2, _TD_MON)


def ptt_drv3_006_recovery_frac_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of 252d recovery fraction."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    slope_21 = _linslope(rf, _TD_MON)
    return slope_21.diff(5)


def ptt_drv3_007_recovery_frac_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day OLS slope of 252d recovery fraction."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    slope_63 = _linslope(rf, _TD_QTR)
    return slope_63.diff(5)


def ptt_drv3_008_span_pct_252d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252d span-pct) — convexity of range expansion."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    span = _safe_div(pk - tr, tr)
    drv2 = span.diff(5)
    return drv2.diff(5)


def ptt_drv3_009_span_pct_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63d span-pct)."""
    pk = _rolling_max(close, _TD_QTR)
    tr = _rolling_min(close, _TD_QTR)
    span = _safe_div(pk - tr, tr)
    drv2 = span.diff(5)
    return drv2.diff(5)


def ptt_drv3_010_close_to_peak_ratio_252d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of close/252d-peak ratio)."""
    pk = _rolling_max(close, _TD_YEAR)
    ratio = _safe_div(close, pk)
    drv2 = ratio.diff(5)
    return drv2.diff(5)


def ptt_drv3_011_close_to_trough_ratio_252d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of close/252d-trough ratio)."""
    tr = _rolling_min(close, _TD_YEAR)
    ratio = _safe_div(close, tr)
    drv2 = ratio.diff(5)
    return drv2.diff(5)


def ptt_drv3_012_recovery_frac_expanding_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of expanding recovery fraction)."""
    pk = close.expanding(min_periods=1).max()
    tr = close.expanding(min_periods=1).min()
    rf = _recovery_fraction(close, pk, tr)
    drv2 = rf.diff(5)
    return drv2.diff(5)


def ptt_drv3_013_vol_adj_span_252d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of vol-adjusted 252d span)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    span = _safe_div(pk - tr, tr)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    va = _safe_div(span, vol)
    drv2 = va.diff(5)
    return drv2.diff(5)


def ptt_drv3_014_trough_age_fraction_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of trough-freshness fraction)."""
    tr = _rolling_min(close, _TD_YEAR)
    at_trough = (close == tr).astype(float)
    idx = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    last_tr = idx.where(at_trough.astype(bool)).ffill()
    freshness = (idx - last_tr) / float(_TD_YEAR)
    drv2 = freshness.diff(5)
    return drv2.diff(5)


def ptt_drv3_015_recovery_frac_zscore_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of rolling z-score of 252d recovery fraction)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    z = _zscore_rolling(rf, _TD_YEAR)
    drv2 = z.diff(5)
    return drv2.diff(5)


def ptt_drv3_016_composite_rf_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of composite recovery fraction)."""
    rf21 = _recovery_fraction(close, _rolling_max(close, _TD_MON), _rolling_min(close, _TD_MON))
    rf63 = _recovery_fraction(close, _rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    rf252 = _recovery_fraction(close, _rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    composite = 0.5 * rf21 + 0.3 * rf63 + 0.2 * rf252
    drv2 = composite.diff(5)
    return drv2.diff(5)


def ptt_drv3_017_ptt_span_rank_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of pct-rank of 252d span)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    span = _safe_div(pk - tr, tr)
    rank = span.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    drv2 = rank.diff(5)
    return drv2.diff(5)


def ptt_drv3_018_log_rf_252d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of log-space recovery fraction)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    num = _log_safe(close) - _log_safe(tr)
    den = _log_safe(pk) - _log_safe(tr)
    log_rf = _safe_div(num, den)
    drv2 = log_rf.diff(5)
    return drv2.diff(5)


def ptt_drv3_019_vwap_rf_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of VWAP 252d recovery fraction)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    pk = _rolling_max(vwap, _TD_YEAR)
    tr = _rolling_min(vwap, _TD_YEAR)
    rf = _recovery_fraction(vwap, pk, tr)
    drv2 = rf.diff(5)
    return drv2.diff(5)


def ptt_drv3_020_atr_span_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of ATR-normalized 252d peak-trough span)."""
    atr = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    ratio = _safe_div(pk - tr, atr)
    drv2 = ratio.diff(5)
    return drv2.diff(5)


def ptt_drv3_021_trough_mean_asym_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of trough-to-mean-to-peak asymmetry)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    mu = _rolling_mean(close, _TD_YEAR)
    asym = _safe_div(pk - mu, mu - tr)
    drv2 = asym.diff(5)
    return drv2.diff(5)


def ptt_drv3_022_rf_pct_rank_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of pct-rank of 252d recovery fraction)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    rank = rf.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    drv2 = rank.diff(5)
    return drv2.diff(5)


def ptt_drv3_023_composite_ptt_ratio_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of composite PTT ratio)."""
    r21 = _safe_div(_rolling_max(close, _TD_MON), _rolling_min(close, _TD_MON))
    r63 = _safe_div(_rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    r252 = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    composite = 0.40 * r21 + 0.35 * r63 + 0.25 * r252
    drv2 = composite.diff(5)
    return drv2.diff(5)


def ptt_drv3_024_rf_slope_21d_21d_slope(close: pd.Series) -> pd.Series:
    """21-day slope of (21-day slope of 252d recovery fraction) — curvature of retracement trend."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    slope_21 = _linslope(rf, _TD_MON)
    return _linslope(slope_21, _TD_MON)


def ptt_drv3_025_recovery_fraction_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 252d recovery fraction) — change in monthly retracement pace."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    drv2 = rf.diff(_TD_MON)
    return drv2.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

PEAK_TO_TROUGH_REGISTRY_3RD_DERIVATIVES = {
    "ptt_drv3_001_recovery_fraction_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_001_recovery_fraction_252d_5d_diff_5d_diff},
    "ptt_drv3_002_recovery_fraction_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_002_recovery_fraction_63d_5d_diff_5d_diff},
    "ptt_drv3_003_ptt_ratio_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_003_ptt_ratio_252d_5d_diff_5d_diff},
    "ptt_drv3_004_ptt_ratio_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_004_ptt_ratio_63d_5d_diff_5d_diff},
    "ptt_drv3_005_log_ptt_span_252d_diff_21d_slope": {"inputs": ["close"], "func": ptt_drv3_005_log_ptt_span_252d_diff_21d_slope},
    "ptt_drv3_006_recovery_frac_slope_21d_5d_diff": {"inputs": ["close"], "func": ptt_drv3_006_recovery_frac_slope_21d_5d_diff},
    "ptt_drv3_007_recovery_frac_slope_63d_5d_diff": {"inputs": ["close"], "func": ptt_drv3_007_recovery_frac_slope_63d_5d_diff},
    "ptt_drv3_008_span_pct_252d_5d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_008_span_pct_252d_5d_diff_5d_diff},
    "ptt_drv3_009_span_pct_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_009_span_pct_63d_5d_diff_5d_diff},
    "ptt_drv3_010_close_to_peak_ratio_252d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_010_close_to_peak_ratio_252d_diff_5d_diff},
    "ptt_drv3_011_close_to_trough_ratio_252d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_011_close_to_trough_ratio_252d_diff_5d_diff},
    "ptt_drv3_012_recovery_frac_expanding_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_012_recovery_frac_expanding_diff_5d_diff},
    "ptt_drv3_013_vol_adj_span_252d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_013_vol_adj_span_252d_diff_5d_diff},
    "ptt_drv3_014_trough_age_fraction_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_014_trough_age_fraction_diff_5d_diff},
    "ptt_drv3_015_recovery_frac_zscore_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_015_recovery_frac_zscore_diff_5d_diff},
    "ptt_drv3_016_composite_rf_5d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_016_composite_rf_5d_diff_5d_diff},
    "ptt_drv3_017_ptt_span_rank_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_017_ptt_span_rank_diff_5d_diff},
    "ptt_drv3_018_log_rf_252d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_018_log_rf_252d_diff_5d_diff},
    "ptt_drv3_019_vwap_rf_diff_5d_diff": {"inputs": ["close", "volume"], "func": ptt_drv3_019_vwap_rf_diff_5d_diff},
    "ptt_drv3_020_atr_span_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": ptt_drv3_020_atr_span_diff_5d_diff},
    "ptt_drv3_021_trough_mean_asym_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_021_trough_mean_asym_diff_5d_diff},
    "ptt_drv3_022_rf_pct_rank_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_022_rf_pct_rank_diff_5d_diff},
    "ptt_drv3_023_composite_ptt_ratio_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_023_composite_ptt_ratio_diff_5d_diff},
    "ptt_drv3_024_rf_slope_21d_21d_slope": {"inputs": ["close"], "func": ptt_drv3_024_rf_slope_21d_21d_slope},
    "ptt_drv3_025_recovery_fraction_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": ptt_drv3_025_recovery_fraction_252d_21d_diff_5d_diff},
}
