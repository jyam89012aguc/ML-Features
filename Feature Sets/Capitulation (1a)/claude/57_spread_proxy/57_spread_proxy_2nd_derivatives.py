"""
57_spread_proxy — 2nd Derivatives (Features spr_drv2_001-025)
Domain: rate of change of base spread-estimator features — velocity / acceleration
        of effective bid-ask spread proxies (Corwin-Schultz, Abdi-Ranaldi, HL%, Roll).
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _hl_spread_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(high - low, close)


def _cs_spread(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz spread, floored at 0."""
    k1 = 3.0 - 2.0 * np.sqrt(2.0)
    log_hl = (_log_safe(high) - _log_safe(low)) ** 2
    beta = log_hl + log_hl.shift(1)
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    gamma = (_log_safe(h2) - _log_safe(l2)) ** 2
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k1 - np.sqrt(gamma / k1)
    return (2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))).clip(lower=0.0)


def _ar_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Abdi-Ranaldi spread."""
    mid = 0.5 * (high + low)
    return 4.0 * (_log_safe(close) - _log_safe(mid))


def _roll_spread(close: pd.Series, w: int) -> pd.Series:
    """Roll effective spread: 2*sqrt(max(-cov,0))."""
    dc = close.diff(1)
    dc1 = dc.shift(1)
    cov = dc.rolling(w, min_periods=max(2, w // 2)).cov(dc1)
    return 2.0 * np.sqrt((-cov).clip(lower=0.0))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def spr_drv2_001_hl_spread_21d_mean_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of 21d-mean HL spread (short-term velocity of spread change)."""
    return _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON).diff(_TD_WEEK)


def spr_drv2_002_hl_spread_21d_mean_21d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """21-day diff of 21d-mean HL spread (monthly velocity)."""
    return _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON).diff(_TD_MON)


def spr_drv2_003_cs_spread_21d_mean_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21d-mean Corwin-Schultz spread (CS velocity short-term)."""
    return _rolling_mean(_cs_spread(high, low), _TD_MON).diff(_TD_WEEK)


def spr_drv2_004_cs_spread_21d_mean_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21d-mean CS spread (CS velocity monthly)."""
    return _rolling_mean(_cs_spread(high, low), _TD_MON).diff(_TD_MON)


def spr_drv2_005_ar_spread_21d_mean_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of 21d-mean |AR| spread (Abdi-Ranaldi velocity)."""
    return _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON).diff(_TD_WEEK)


def spr_drv2_006_roll_spread_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d Roll spread (covariance-model spread velocity)."""
    return _roll_spread(close, _TD_MON).diff(_TD_WEEK)


def spr_drv2_007_roll_spread_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d Roll spread (monthly velocity of Roll spread)."""
    return _roll_spread(close, _TD_MON).diff(_TD_MON)


def spr_drv2_008_hl_spread_zscore_21d_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of HL-spread 21d z-score (velocity of extremity)."""
    hl = _hl_spread_raw(high, low, close)
    z = _safe_div(hl - _rolling_mean(hl, _TD_MON), _rolling_std(hl, _TD_MON))
    return z.diff(_TD_WEEK)


def spr_drv2_009_cs_spread_zscore_63d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of CS spread 63d z-score."""
    cs = _cs_spread(high, low)
    z = _safe_div(cs - _rolling_mean(cs, _TD_QTR), _rolling_std(cs, _TD_QTR))
    return z.diff(_TD_MON)


def spr_drv2_010_hl_spread_63d_mean_21d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """21-day diff of 63d-mean HL spread (quarterly spread trend acceleration)."""
    return _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR).diff(_TD_MON)


def spr_drv2_011_gap_spread_21d_mean_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21d-mean overnight gap spread proxy."""
    gap = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return _rolling_mean(gap, _TD_MON).diff(_TD_WEEK)


def spr_drv2_012_roll_spread_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d Roll spread (medium-term Roll spread velocity)."""
    return _roll_spread(close, _TD_QTR).diff(_TD_MON)


def spr_drv2_013_composite_spread_21d_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of 21d three-way composite spread (HL+CS+|AR|)/3."""
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    cs21 = _rolling_mean(_cs_spread(high, low), _TD_MON)
    ar21 = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)
    comp = (hl21 + cs21 + ar21) / 3.0
    return comp.diff(_TD_WEEK)


def spr_drv2_014_composite_spread_21d_21d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """21-day diff of 21d three-way composite spread."""
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    cs21 = _rolling_mean(_cs_spread(high, low), _TD_MON)
    ar21 = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)
    comp = (hl21 + cs21 + ar21) / 3.0
    return comp.diff(_TD_MON)


def spr_drv2_015_hl_spread_slope_21d_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of the 21d OLS slope of HL spread (acceleration of spread trend)."""
    slope = _linslope(_hl_spread_raw(high, low, close), _TD_MON)
    return slope.diff(_TD_WEEK)


def spr_drv2_016_hl_spread_21d_vs_63d_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of (21d/63d HL spread ratio) — widening regime velocity."""
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    hl63 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR)
    return _safe_div(hl21, hl63).diff(_TD_WEEK)


def spr_drv2_017_cs_spread_21d_vs_63d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of (21d/63d CS spread ratio)."""
    cs21 = _rolling_mean(_cs_spread(high, low), _TD_MON)
    cs63 = _rolling_mean(_cs_spread(high, low), _TD_QTR)
    return _safe_div(cs21, cs63).diff(_TD_MON)


def spr_drv2_018_hl_spread_ewm21_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of EWM(21) HL spread (reactive velocity of EWM-smoothed spread)."""
    return _ewm_mean(_hl_spread_raw(high, low, close), _TD_MON).diff(_TD_WEEK)


def spr_drv2_019_spread_vol_norm_21d_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 21d mean of HL-spread/log(vol)."""
    log_vol = np.log(volume.clip(lower=1.0))
    sn = _safe_div(_hl_spread_raw(high, low, close), log_vol)
    return _rolling_mean(sn, _TD_MON).diff(_TD_WEEK)


def spr_drv2_020_tr_spread_21d_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of 21d-mean TR/close spread proxy."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    tr_spr = _safe_div(tr, close)
    return _rolling_mean(tr_spr, _TD_MON).diff(_TD_WEEK)


def spr_drv2_021_roll_spread_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d Roll spread over 63-day window (quarterly Roll trend)."""
    return _linslope(_roll_spread(close, _TD_MON), _TD_QTR)


def spr_drv2_022_hl_spread_pct_rank_63d_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of 63d percentile rank of HL spread (rank velocity)."""
    pct = _hl_spread_raw(high, low, close).rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)
    return pct.diff(_TD_WEEK)


def spr_drv2_023_cs_spread_252d_mean_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 252d-mean CS spread (annual CS spread trend velocity)."""
    return _rolling_mean(_cs_spread(high, low), _TD_YEAR).diff(_TD_MON)


def spr_drv2_024_spread_down_up_ratio_21d_5d_diff(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """5-day diff of 21d (spread-on-down-days / spread-on-up-days) ratio."""
    hl = _hl_spread_raw(high, low, close)
    ret = close.pct_change(1)
    hl_down = hl.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    hl_up   = hl.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(hl_down, hl_up)
    return ratio.diff(_TD_WEEK)


def spr_drv2_025_gap_spread_63d_mean_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63d-mean overnight gap spread proxy."""
    gap = _safe_div((open - close.shift(1)).abs(), close.shift(1))
    return _rolling_mean(gap, _TD_QTR).diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

SPREAD_PROXY_REGISTRY_2ND_DERIVATIVES = {
    "spr_drv2_001_hl_spread_21d_mean_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_001_hl_spread_21d_mean_5d_diff},
    "spr_drv2_002_hl_spread_21d_mean_21d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_002_hl_spread_21d_mean_21d_diff},
    "spr_drv2_003_cs_spread_21d_mean_5d_diff": {"inputs": ["high", "low"], "func": spr_drv2_003_cs_spread_21d_mean_5d_diff},
    "spr_drv2_004_cs_spread_21d_mean_21d_diff": {"inputs": ["high", "low"], "func": spr_drv2_004_cs_spread_21d_mean_21d_diff},
    "spr_drv2_005_ar_spread_21d_mean_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_005_ar_spread_21d_mean_5d_diff},
    "spr_drv2_006_roll_spread_21d_5d_diff": {"inputs": ["close"], "func": spr_drv2_006_roll_spread_21d_5d_diff},
    "spr_drv2_007_roll_spread_21d_21d_diff": {"inputs": ["close"], "func": spr_drv2_007_roll_spread_21d_21d_diff},
    "spr_drv2_008_hl_spread_zscore_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_008_hl_spread_zscore_21d_5d_diff},
    "spr_drv2_009_cs_spread_zscore_63d_21d_diff": {"inputs": ["high", "low"], "func": spr_drv2_009_cs_spread_zscore_63d_21d_diff},
    "spr_drv2_010_hl_spread_63d_mean_21d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_010_hl_spread_63d_mean_21d_diff},
    "spr_drv2_011_gap_spread_21d_mean_5d_diff": {"inputs": ["close", "open"], "func": spr_drv2_011_gap_spread_21d_mean_5d_diff},
    "spr_drv2_012_roll_spread_63d_21d_diff": {"inputs": ["close"], "func": spr_drv2_012_roll_spread_63d_21d_diff},
    "spr_drv2_013_composite_spread_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_013_composite_spread_21d_5d_diff},
    "spr_drv2_014_composite_spread_21d_21d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_014_composite_spread_21d_21d_diff},
    "spr_drv2_015_hl_spread_slope_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_015_hl_spread_slope_21d_5d_diff},
    "spr_drv2_016_hl_spread_21d_vs_63d_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_016_hl_spread_21d_vs_63d_5d_diff},
    "spr_drv2_017_cs_spread_21d_vs_63d_21d_diff": {"inputs": ["high", "low"], "func": spr_drv2_017_cs_spread_21d_vs_63d_21d_diff},
    "spr_drv2_018_hl_spread_ewm21_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_018_hl_spread_ewm21_5d_diff},
    "spr_drv2_019_spread_vol_norm_21d_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": spr_drv2_019_spread_vol_norm_21d_5d_diff},
    "spr_drv2_020_tr_spread_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_020_tr_spread_21d_5d_diff},
    "spr_drv2_021_roll_spread_21d_slope_63d": {"inputs": ["close"], "func": spr_drv2_021_roll_spread_21d_slope_63d},
    "spr_drv2_022_hl_spread_pct_rank_63d_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_022_hl_spread_pct_rank_63d_5d_diff},
    "spr_drv2_023_cs_spread_252d_mean_21d_diff": {"inputs": ["high", "low"], "func": spr_drv2_023_cs_spread_252d_mean_21d_diff},
    "spr_drv2_024_spread_down_up_ratio_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": spr_drv2_024_spread_down_up_ratio_21d_5d_diff},
    "spr_drv2_025_gap_spread_63d_mean_21d_diff": {"inputs": ["close", "open"], "func": spr_drv2_025_gap_spread_63d_mean_21d_diff},
}
