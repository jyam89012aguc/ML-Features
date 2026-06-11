"""
34_velocity_inflection — Extended 2nd Derivatives (Features vif_extdrv2_001-025)
Domain: rate of change of extended velocity-inflection concepts — 5d/21d diffs and OLS
        slopes applied to: WMA/Hull/DEMA/TEMA velocity flips, volume-surge-at-flip,
        curvature magnitude, multi-span neg-velocity score, inter-flip duration,
        HL2/HLC3 velocity regime, EMA-cross features, z-score/rank transforms of
        extended-base features.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _velocity(close: pd.Series, span: int) -> pd.Series:
    """EMA-smoothed 1-day log-return (price velocity)."""
    lr = _log_safe(close).diff(1)
    return _ewm_mean(lr, span)


def _sign_flip(s: pd.Series) -> pd.Series:
    """Binary: 1 where sign of s differs from prior row."""
    sg = np.sign(s)
    return ((sg != sg.shift(1)) & sg.notna() & sg.shift(1).notna()).astype(float)


def _days_since_flip(flip: pd.Series) -> pd.Series:
    """Bars elapsed since last 1 in binary flip series (backward-looking)."""
    idx = np.arange(len(flip))
    last_flip_idx = pd.Series(np.where(flip.values == 1, idx, np.nan))
    last_flip_idx = last_flip_idx.ffill()
    result = pd.Series(idx, index=flip.index, dtype=float) - last_flip_idx.values
    result[last_flip_idx.isna().values] = np.nan
    return result


def _rolling_count(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_true(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


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
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _wma(s: pd.Series, w: int) -> pd.Series:
    """Weighted moving average (linearly-weighted)."""
    weights = np.arange(1, w + 1, dtype=float)
    def _wma_apply(x):
        if len(x) < max(1, w // 2):
            return np.nan
        wts = weights[-len(x):]
        return float(np.dot(x, wts) / wts.sum())
    return s.rolling(w, min_periods=max(1, w // 2)).apply(_wma_apply, raw=True)


def _hull_ma(s: pd.Series, w: int) -> pd.Series:
    """Hull Moving Average of s over period w."""
    half_w = max(2, w // 2)
    sqrt_w = max(2, int(round(w ** 0.5)))
    wma_half = _wma(s, half_w)
    wma_full = _wma(s, w)
    raw = 2.0 * wma_half - wma_full
    return _wma(raw, sqrt_w)


def _dema(s: pd.Series, span: int) -> pd.Series:
    """Double EMA."""
    e1 = _ewm_mean(s, span)
    e2 = _ewm_mean(e1, span)
    return 2.0 * e1 - e2


def _tema(s: pd.Series, span: int) -> pd.Series:
    """Triple EMA."""
    e1 = _ewm_mean(s, span)
    e2 = _ewm_mean(e1, span)
    e3 = _ewm_mean(e2, span)
    return 3.0 * e1 - 3.0 * e2 + e3


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────

def vif_extdrv2_001_hull5_vel_flip_count_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Hull MA(5) velocity flip count (velocity of Hull flip density)."""
    cnt = _rolling_count(_sign_flip(_hull_ma(close, _TD_WEEK).diff(1)), _TD_MON)
    return cnt.diff(_TD_WEEK)


def vif_extdrv2_002_hull21_vel_flip_count_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day Hull MA(21) velocity flip count."""
    cnt = _rolling_count(_sign_flip(_hull_ma(close, _TD_MON).diff(1)), _TD_QTR)
    return cnt.diff(_TD_MON)


def vif_extdrv2_003_wma5_vel_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of WMA-5 velocity percentile rank in 252-day window."""
    vel = _wma(close, _TD_WEEK).diff(1)
    rank = vel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vif_extdrv2_004_dema5_vel_flip_count_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day DEMA(5) velocity flip count."""
    cnt = _rolling_count(_sign_flip(_dema(close, _TD_WEEK).diff(1)), _TD_MON)
    return cnt.diff(_TD_WEEK)


def vif_extdrv2_005_tema5_vel_flip_count_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day TEMA(5) velocity flip count."""
    cnt = _rolling_count(_sign_flip(_tema(close, _TD_WEEK).diff(1)), _TD_MON)
    return cnt.diff(_TD_WEEK)


def vif_extdrv2_006_hl2_vel_ema5_flip_count_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day EMA-5 HL2 velocity flip count."""
    hl2 = (high + low) / 2.0
    cnt = _rolling_count(_sign_flip(_velocity(hl2, _TD_WEEK)), _TD_MON)
    return cnt.diff(_TD_WEEK)


def vif_extdrv2_007_hlc3_vel_ema5_flip_count_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day EMA-5 HLC3 velocity flip count."""
    hlc3 = (high + low + close) / 3.0
    cnt = _rolling_count(_sign_flip(_velocity(hlc3, _TD_WEEK)), _TD_QTR)
    return cnt.diff(_TD_MON)


def vif_extdrv2_008_vel_ema10_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-10 velocity z-score vs 252-day distribution."""
    v = _velocity(close, 10)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vif_extdrv2_009_vel_ema63_zscore_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-63 velocity z-score vs 252-day distribution."""
    v = _velocity(close, _TD_QTR)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vif_extdrv2_010_curvature_ema5_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-5 curvature z-score (velocity of curvature extremity)."""
    curv = _velocity(close, _TD_WEEK).diff(1).abs()
    m = _rolling_mean(curv, _TD_YEAR)
    s = _rolling_std(curv, _TD_YEAR)
    z = _safe_div(curv - m, s)
    return z.diff(_TD_WEEK)


def vif_extdrv2_011_curvature_ema5_pct_rank_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-5 curvature percentile rank in 252-day window."""
    curv = _velocity(close, _TD_WEEK).diff(1).abs()
    rank = curv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vif_extdrv2_012_multi_span_vel_neg_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-span negative velocity count score (EMA-5/10/21/63/126)."""
    v5 = (_velocity(close, _TD_WEEK) < 0).astype(float)
    v10 = (_velocity(close, 10) < 0).astype(float)
    v21 = (_velocity(close, _TD_MON) < 0).astype(float)
    v63 = (_velocity(close, _TD_QTR) < 0).astype(float)
    v126 = (_velocity(close, _TD_HALF) < 0).astype(float)
    score = v5 + v10 + v21 + v63 + v126
    return score.diff(_TD_WEEK)


def vif_extdrv2_013_vel_ema10_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-10 velocity percentile rank in 252-day window."""
    v = _velocity(close, 10)
    rank = v.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vif_extdrv2_014_inflection_density_ema5_126d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of EMA-5 flip count over trailing 126 days."""
    cnt = _rolling_count(_sign_flip(_velocity(close, _TD_WEEK)), _TD_HALF)
    return cnt.diff(_TD_MON)


def vif_extdrv2_015_inter_flip_duration_ema5_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of average inter-flip duration for EMA-5 over 63 days."""
    flip = _sign_flip(_velocity(close, _TD_WEEK))
    cnt = _rolling_count(flip, _TD_QTR)
    duration = _safe_div(pd.Series(_TD_QTR, index=flip.index, dtype=float), cnt)
    return duration.diff(_TD_MON)


def vif_extdrv2_016_days_since_ema10_flip_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-since-EMA-10-flip (staleness velocity for 10-span)."""
    d = _days_since_flip(_sign_flip(_velocity(close, 10)))
    return d.diff(_TD_WEEK)


def vif_extdrv2_017_days_since_hull5_flip_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-since-Hull-MA(5)-flip."""
    d = _days_since_flip(_sign_flip(_hull_ma(close, _TD_WEEK).diff(1)))
    return d.diff(_TD_WEEK)


def vif_extdrv2_018_vel_ema10_flip_count_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day EMA-10 flip count (acceleration of flip rate)."""
    cnt = _rolling_count(_sign_flip(_velocity(close, 10)), _TD_MON)
    return _linslope(cnt, _TD_MON)


def vif_extdrv2_019_curvature_ema5_ratio_252d_avg_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (current EMA-5 curvature / 252-day avg curvature) ratio."""
    curv = _velocity(close, _TD_WEEK).diff(1).abs()
    avg = _rolling_mean(curv, _TD_YEAR)
    ratio = _safe_div(curv, avg)
    return ratio.diff(_TD_WEEK)


def vif_extdrv2_020_hl2_vel_ema21_flip_count_63d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day EMA-21 HL2 velocity flip count."""
    hl2 = (high + low) / 2.0
    cnt = _rolling_count(_sign_flip(_velocity(hl2, _TD_MON)), _TD_QTR)
    return cnt.diff(_TD_MON)


def vif_extdrv2_021_consec_neg_vel_ema63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive negative EMA-63 velocity streak."""
    streak = _consec_true(_velocity(close, _TD_QTR) < 0)
    return streak.diff(_TD_WEEK)


def vif_extdrv2_022_vel_ema5_zscore_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-5 velocity z-score vs 63-day distribution."""
    v = _velocity(close, _TD_WEEK)
    m = _rolling_mean(v, _TD_QTR)
    s = _rolling_std(v, _TD_QTR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_WEEK)


def vif_extdrv2_023_vel_ema21_zscore_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of EMA-21 velocity z-score vs 63-day distribution."""
    v = _velocity(close, _TD_MON)
    m = _rolling_mean(v, _TD_QTR)
    s = _rolling_std(v, _TD_QTR)
    z = _safe_div(v - m, s)
    return z.diff(_TD_MON)


def vif_extdrv2_024_inflection_density_ema5_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of z-score of 21-day EMA-5 flip count vs 252-day distribution."""
    cnt = _rolling_count(_sign_flip(_velocity(close, _TD_WEEK)), _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    z = _safe_div(cnt - m, s)
    return z.diff(_TD_WEEK)


def vif_extdrv2_025_vel_ema126_flip_count_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day EMA-126 velocity flip count (half-year smoothing flip rate)."""
    cnt = _rolling_count(_sign_flip(_velocity(close, _TD_HALF)), _TD_YEAR)
    return cnt.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VELOCITY_INFLECTION_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "vif_extdrv2_001_hull5_vel_flip_count_21d_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_001_hull5_vel_flip_count_21d_5d_diff},
    "vif_extdrv2_002_hull21_vel_flip_count_63d_21d_diff": {"inputs": ["close"], "func": vif_extdrv2_002_hull21_vel_flip_count_63d_21d_diff},
    "vif_extdrv2_003_wma5_vel_pct_rank_252d_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_003_wma5_vel_pct_rank_252d_5d_diff},
    "vif_extdrv2_004_dema5_vel_flip_count_21d_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_004_dema5_vel_flip_count_21d_5d_diff},
    "vif_extdrv2_005_tema5_vel_flip_count_21d_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_005_tema5_vel_flip_count_21d_5d_diff},
    "vif_extdrv2_006_hl2_vel_ema5_flip_count_21d_5d_diff": {"inputs": ["high", "low"], "func": vif_extdrv2_006_hl2_vel_ema5_flip_count_21d_5d_diff},
    "vif_extdrv2_007_hlc3_vel_ema5_flip_count_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": vif_extdrv2_007_hlc3_vel_ema5_flip_count_63d_21d_diff},
    "vif_extdrv2_008_vel_ema10_zscore_252d_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_008_vel_ema10_zscore_252d_5d_diff},
    "vif_extdrv2_009_vel_ema63_zscore_252d_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_009_vel_ema63_zscore_252d_5d_diff},
    "vif_extdrv2_010_curvature_ema5_zscore_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_010_curvature_ema5_zscore_5d_diff},
    "vif_extdrv2_011_curvature_ema5_pct_rank_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_011_curvature_ema5_pct_rank_5d_diff},
    "vif_extdrv2_012_multi_span_vel_neg_count_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_012_multi_span_vel_neg_count_5d_diff},
    "vif_extdrv2_013_vel_ema10_pct_rank_252d_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_013_vel_ema10_pct_rank_252d_5d_diff},
    "vif_extdrv2_014_inflection_density_ema5_126d_21d_diff": {"inputs": ["close"], "func": vif_extdrv2_014_inflection_density_ema5_126d_21d_diff},
    "vif_extdrv2_015_inter_flip_duration_ema5_63d_21d_diff": {"inputs": ["close"], "func": vif_extdrv2_015_inter_flip_duration_ema5_63d_21d_diff},
    "vif_extdrv2_016_days_since_ema10_flip_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_016_days_since_ema10_flip_5d_diff},
    "vif_extdrv2_017_days_since_hull5_flip_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_017_days_since_hull5_flip_5d_diff},
    "vif_extdrv2_018_vel_ema10_flip_count_21d_slope_21d": {"inputs": ["close"], "func": vif_extdrv2_018_vel_ema10_flip_count_21d_slope_21d},
    "vif_extdrv2_019_curvature_ema5_ratio_252d_avg_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_019_curvature_ema5_ratio_252d_avg_5d_diff},
    "vif_extdrv2_020_hl2_vel_ema21_flip_count_63d_21d_diff": {"inputs": ["high", "low"], "func": vif_extdrv2_020_hl2_vel_ema21_flip_count_63d_21d_diff},
    "vif_extdrv2_021_consec_neg_vel_ema63_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_021_consec_neg_vel_ema63_5d_diff},
    "vif_extdrv2_022_vel_ema5_zscore_63d_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_022_vel_ema5_zscore_63d_5d_diff},
    "vif_extdrv2_023_vel_ema21_zscore_63d_21d_diff": {"inputs": ["close"], "func": vif_extdrv2_023_vel_ema21_zscore_63d_21d_diff},
    "vif_extdrv2_024_inflection_density_ema5_zscore_5d_diff": {"inputs": ["close"], "func": vif_extdrv2_024_inflection_density_ema5_zscore_5d_diff},
    "vif_extdrv2_025_vel_ema126_flip_count_252d_21d_diff": {"inputs": ["close"], "func": vif_extdrv2_025_vel_ema126_flip_count_252d_21d_diff},
}
