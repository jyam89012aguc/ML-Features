"""
119_volume_shock_aftermath — 2nd Derivatives (Features vsa_drv2_001-025)
Domain: rate of change of base volume-shock-aftermath features — velocity of
        shock aftermath dynamics (how fast volume decay accelerates, how rapidly
        days-since-shock changes, price drift velocity after shocks)
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _vol_zscore(volume: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(volume, w)
    s = _rolling_std(volume, w)
    return _safe_div(volume - m, s.clip(lower=_EPS))


def _shock_flag(volume: pd.Series, w: int, z_thresh: float = 2.0) -> pd.Series:
    return (_vol_zscore(volume, w) > z_thresh).astype(float)


def _days_since_last_shock(volume: pd.Series, w: int, z_thresh: float = 2.0) -> pd.Series:
    flag = _shock_flag(volume, w, z_thresh)
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag == 1.0).ffill().fillna(-1.0)
    elapsed = idx - last
    return elapsed.where(last >= 0.0, np.nan)


def _price_return_since_shock(close: pd.Series, volume: pd.Series,
                               w: int, z_thresh: float = 2.0) -> pd.Series:
    flag = _shock_flag(volume, w, z_thresh)
    shock_close = close.where(flag == 1.0).ffill()
    return _safe_div(close - shock_close, shock_close.clip(lower=_EPS))


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vsa_drv2_001_vol_zscore_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day vol z-score (velocity of vol shock indicator)."""
    return _vol_zscore(volume, _TD_MON).diff(_TD_WEEK)


def vsa_drv2_002_vol_zscore_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day vol z-score."""
    return _vol_zscore(volume, _TD_QTR).diff(_TD_WEEK)


def vsa_drv2_003_vol_zscore_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day vol z-score (monthly velocity of shock indicator)."""
    return _vol_zscore(volume, _TD_MON).diff(_TD_MON)


def vsa_drv2_004_shock_count_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day shock count (velocity of shock accumulation)."""
    cnt = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON)
    return cnt.diff(_TD_WEEK)


def vsa_drv2_005_shock_count_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day shock count."""
    cnt = _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_QTR)
    return cnt.diff(_TD_WEEK)


def vsa_drv2_006_days_since_shock_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of days-since-shock (21d/z2); -5 = shock receding by 5 days/week."""
    d = _days_since_last_shock(volume, _TD_MON, 2.0)
    return d.diff(_TD_WEEK)


def vsa_drv2_007_price_return_since_shock_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of cumulative return since shock (velocity of price drift)."""
    ret = _price_return_since_shock(close, volume, _TD_MON, 2.0)
    return ret.diff(_TD_WEEK)


def vsa_drv2_008_price_return_since_shock_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of cumulative return since shock (monthly drift velocity)."""
    ret = _price_return_since_shock(close, volume, _TD_QTR, 2.0)
    return ret.diff(_TD_MON)


def vsa_drv2_009_vol_decay_ratio_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of vol/shock-vol ratio (acceleration of volume decay)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    ratio = _safe_div(volume, shock_vol.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def vsa_drv2_010_shock_density_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day shock density (fraction of days that are shocks)."""
    density = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON) / _TD_MON
    return density.diff(_TD_WEEK)


def vsa_drv2_011_vol_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume/21d-mean ratio (velocity of relative volume change)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def vsa_drv2_012_shock_intensity_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day shock intensity (sum of z-scores)."""
    intensity = _rolling_sum(_vol_zscore(volume, _TD_MON).clip(lower=0.0), _TD_MON)
    return intensity.diff(_TD_WEEK)


def vsa_drv2_013_neg_vol_fraction_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day down-day volume fraction."""
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    frac = _safe_div(dn_vol, total_vol.clip(lower=_EPS))
    return frac.diff(_TD_WEEK)


def vsa_drv2_014_up_down_vol_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day up/down volume ratio."""
    up_vol = _rolling_sum((close.diff(1) > 0.0).astype(float) * volume, _TD_MON)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    ratio = _safe_div(up_vol, dn_vol.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def vsa_drv2_015_obv_5d_change_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day OBV change (acceleration of OBV momentum)."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    obv5 = obv.diff(_TD_WEEK)
    return obv5.diff(_TD_WEEK)


def vsa_drv2_016_obv_21d_change_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day OBV change."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    obv21 = obv.diff(_TD_MON)
    return obv21.diff(_TD_WEEK)


def vsa_drv2_017_vol_cv_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume coefficient of variation."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    cv = _safe_div(s, m.clip(lower=_EPS))
    return cv.diff(_TD_WEEK)


def vsa_drv2_018_vol_21d_mean_vs_252d_mean_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21d/252d volume mean ratio (regime shift velocity)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON),
                      _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def vsa_drv2_019_vol_zscore_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day vol z-score (trend in shock indicator)."""
    z = _vol_zscore(volume, _TD_MON)
    return _linslope(z, _TD_MON)


def vsa_drv2_020_shock_count_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day shock count (monthly change in shock accumulation)."""
    cnt = _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_QTR)
    return cnt.diff(_TD_MON)


def vsa_drv2_021_vol_spike_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day max/mean volume ratio (spike factor velocity)."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON),
                      _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def vsa_drv2_022_vol_elevated_days_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of count of elevated-volume days in 21d window."""
    elevated = (_safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS)) > 1.5).astype(float)
    cnt = _rolling_sum(elevated, _TD_MON)
    return cnt.diff(_TD_WEEK)


def vsa_drv2_023_vol_dry_up_consec_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of consecutive dry-up days (velocity of volume drying up)."""
    streak = _consec_streak(
        (_safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS)) < 0.7).astype(bool)
    )
    return streak.diff(_TD_WEEK)


def vsa_drv2_024_shock_intensity_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day shock intensity."""
    intensity = _rolling_sum(_vol_zscore(volume, _TD_QTR).clip(lower=0.0), _TD_QTR)
    return intensity.diff(_TD_MON)


def vsa_drv2_025_vol_percentile_rank_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day volume percentile rank (velocity of rank movement)."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_SHOCK_AFTERMATH_REGISTRY_2ND_DERIVATIVES = {
    "vsa_drv2_001_vol_zscore_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_001_vol_zscore_21d_5d_diff},
    "vsa_drv2_002_vol_zscore_63d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_002_vol_zscore_63d_5d_diff},
    "vsa_drv2_003_vol_zscore_21d_21d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_003_vol_zscore_21d_21d_diff},
    "vsa_drv2_004_shock_count_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_004_shock_count_21d_5d_diff},
    "vsa_drv2_005_shock_count_63d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_005_shock_count_63d_5d_diff},
    "vsa_drv2_006_days_since_shock_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_006_days_since_shock_5d_diff},
    "vsa_drv2_007_price_return_since_shock_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_007_price_return_since_shock_5d_diff},
    "vsa_drv2_008_price_return_since_shock_21d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_008_price_return_since_shock_21d_diff},
    "vsa_drv2_009_vol_decay_ratio_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_009_vol_decay_ratio_5d_diff},
    "vsa_drv2_010_shock_density_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_010_shock_density_21d_5d_diff},
    "vsa_drv2_011_vol_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_011_vol_ratio_21d_5d_diff},
    "vsa_drv2_012_shock_intensity_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_012_shock_intensity_21d_5d_diff},
    "vsa_drv2_013_neg_vol_fraction_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_013_neg_vol_fraction_21d_5d_diff},
    "vsa_drv2_014_up_down_vol_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_014_up_down_vol_ratio_21d_5d_diff},
    "vsa_drv2_015_obv_5d_change_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_015_obv_5d_change_5d_diff},
    "vsa_drv2_016_obv_21d_change_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_016_obv_21d_change_5d_diff},
    "vsa_drv2_017_vol_cv_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_017_vol_cv_21d_5d_diff},
    "vsa_drv2_018_vol_21d_mean_vs_252d_mean_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_018_vol_21d_mean_vs_252d_mean_5d_diff},
    "vsa_drv2_019_vol_zscore_21d_slope_21d": {"inputs": ["close", "volume"], "func": vsa_drv2_019_vol_zscore_21d_slope_21d},
    "vsa_drv2_020_shock_count_63d_21d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_020_shock_count_63d_21d_diff},
    "vsa_drv2_021_vol_spike_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_021_vol_spike_ratio_21d_5d_diff},
    "vsa_drv2_022_vol_elevated_days_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_022_vol_elevated_days_21d_5d_diff},
    "vsa_drv2_023_vol_dry_up_consec_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_023_vol_dry_up_consec_5d_diff},
    "vsa_drv2_024_shock_intensity_63d_21d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_024_shock_intensity_63d_21d_diff},
    "vsa_drv2_025_vol_percentile_rank_63d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv2_025_vol_percentile_rank_63d_5d_diff},
}
