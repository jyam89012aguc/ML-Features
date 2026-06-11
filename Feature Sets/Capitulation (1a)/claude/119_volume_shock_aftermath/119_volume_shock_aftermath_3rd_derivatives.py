"""
119_volume_shock_aftermath — 3rd Derivatives (Features vsa_drv3_001-025)
Domain: rate of change of 2nd-derivative volume-shock-aftermath features —
        acceleration of shock aftermath velocity (jerk in vol z-score, acceleration
        of decay rates, shock density acceleration, OBV momentum jerk)
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vsa_drv3_001_vol_zscore_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day vol z-score (acceleration of shock velocity)."""
    vel = _vol_zscore(volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_002_vol_zscore_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day vol z-score (acceleration of 63d shock velocity)."""
    vel = _vol_zscore(volume, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_003_vol_zscore_21d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of vol z-score (jerk in monthly shock change)."""
    vel21 = _vol_zscore(volume, _TD_MON).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vsa_drv3_004_shock_count_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day shock count (acceleration of shock accumulation)."""
    cnt = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_005_price_return_since_shock_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of return-since-shock (acceleration of price drift velocity)."""
    ret = _price_return_since_shock(close, volume, _TD_MON, 2.0)
    vel = ret.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_006_price_return_since_shock_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of return-since-shock (jerk)."""
    ret = _price_return_since_shock(close, volume, _TD_QTR, 2.0)
    vel21 = ret.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vsa_drv3_007_vol_decay_ratio_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol/shock-vol decay ratio (jerk in decay speed)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    ratio = _safe_div(volume, shock_vol.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_008_shock_density_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day shock density (acceleration of density change)."""
    density = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_MON) / _TD_MON
    vel = density.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_009_neg_vol_fraction_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of down-day volume fraction."""
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    frac = _safe_div(dn_vol, total_vol.clip(lower=_EPS))
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_010_obv_5d_change_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day OBV change (jerk in OBV momentum)."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    vel1 = obv.diff(_TD_WEEK)
    vel2 = vel1.diff(_TD_WEEK)
    return vel2.diff(_TD_WEEK)


def vsa_drv3_011_vol_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of volume/21d-mean ratio (acceleration of relative vol change)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_012_shock_intensity_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day shock intensity sum."""
    intensity = _rolling_sum(_vol_zscore(volume, _TD_MON).clip(lower=0.0), _TD_MON)
    vel = intensity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_013_vol_cv_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume CV (jerk in vol variability)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    cv = _safe_div(s, m.clip(lower=_EPS))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_014_vol_21d_mean_vs_252d_mean_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/252d mean volume ratio (regime shift jerk)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON),
                      _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_015_shock_count_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day shock count (jerk in monthly shock change)."""
    cnt = _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vsa_drv3_016_vol_spike_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day max/mean vol ratio (acceleration of spike factor)."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON),
                      _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_017_up_down_vol_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of up/down volume ratio."""
    up_vol = _rolling_sum((close.diff(1) > 0.0).astype(float) * volume, _TD_MON)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    ratio = _safe_div(up_vol, dn_vol.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_018_vol_zscore_21d_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of vol z-score (rate of trend change)."""
    z = _vol_zscore(volume, _TD_MON)
    slope = _linslope(z, _TD_MON)
    return slope.diff(_TD_WEEK)


def vsa_drv3_019_vol_zscore_21d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of vol z-score."""
    vel = _vol_zscore(volume, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vsa_drv3_020_shock_intensity_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day shock intensity."""
    intensity = _rolling_sum(_vol_zscore(volume, _TD_QTR).clip(lower=0.0), _TD_QTR)
    vel21 = intensity.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vsa_drv3_021_vol_dry_up_consec_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive dry-up streak (jerk in dry-up acceleration)."""
    streak = _consec_streak(
        (_safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS)) < 0.7).astype(bool)
    )
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsa_drv3_022_vol_zscore_21d_21d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day velocity of vol z-score."""
    vel21 = _vol_zscore(volume, _TD_MON).diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def vsa_drv3_023_obv_21d_change_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day OBV change (jerk in monthly flow velocity)."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    vel21 = obv.diff(_TD_MON)
    vel2 = vel21.diff(_TD_WEEK)
    return vel2.diff(_TD_WEEK)


def vsa_drv3_024_neg_vol_fraction_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day down-day volume fraction."""
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    frac = _safe_div(dn_vol, total_vol.clip(lower=_EPS))
    return _linslope(frac, _TD_MON)


def vsa_drv3_025_vol_elevated_days_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of elevated-volume day count in 21d (jerk in elevation change)."""
    elevated = (_safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS)) > 1.5).astype(float)
    cnt = _rolling_sum(elevated, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_SHOCK_AFTERMATH_REGISTRY_3RD_DERIVATIVES = {
    "vsa_drv3_001_vol_zscore_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_001_vol_zscore_21d_5d_diff_5d_diff},
    "vsa_drv3_002_vol_zscore_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_002_vol_zscore_63d_5d_diff_5d_diff},
    "vsa_drv3_003_vol_zscore_21d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_003_vol_zscore_21d_21d_diff_5d_diff},
    "vsa_drv3_004_shock_count_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_004_shock_count_21d_5d_diff_5d_diff},
    "vsa_drv3_005_price_return_since_shock_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_005_price_return_since_shock_5d_diff_5d_diff},
    "vsa_drv3_006_price_return_since_shock_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_006_price_return_since_shock_21d_diff_5d_diff},
    "vsa_drv3_007_vol_decay_ratio_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_007_vol_decay_ratio_5d_diff_5d_diff},
    "vsa_drv3_008_shock_density_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_008_shock_density_21d_5d_diff_5d_diff},
    "vsa_drv3_009_neg_vol_fraction_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_009_neg_vol_fraction_21d_5d_diff_5d_diff},
    "vsa_drv3_010_obv_5d_change_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_010_obv_5d_change_5d_diff_5d_diff},
    "vsa_drv3_011_vol_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_011_vol_ratio_21d_5d_diff_5d_diff},
    "vsa_drv3_012_shock_intensity_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_012_shock_intensity_21d_5d_diff_5d_diff},
    "vsa_drv3_013_vol_cv_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_013_vol_cv_21d_5d_diff_5d_diff},
    "vsa_drv3_014_vol_21d_mean_vs_252d_mean_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_014_vol_21d_mean_vs_252d_mean_5d_diff_5d_diff},
    "vsa_drv3_015_shock_count_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_015_shock_count_63d_21d_diff_5d_diff},
    "vsa_drv3_016_vol_spike_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_016_vol_spike_ratio_21d_5d_diff_5d_diff},
    "vsa_drv3_017_up_down_vol_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_017_up_down_vol_ratio_21d_5d_diff_5d_diff},
    "vsa_drv3_018_vol_zscore_21d_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_018_vol_zscore_21d_slope_21d_5d_diff},
    "vsa_drv3_019_vol_zscore_21d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vsa_drv3_019_vol_zscore_21d_5d_diff_slope_21d},
    "vsa_drv3_020_shock_intensity_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_020_shock_intensity_63d_21d_diff_5d_diff},
    "vsa_drv3_021_vol_dry_up_consec_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_021_vol_dry_up_consec_5d_diff_5d_diff},
    "vsa_drv3_022_vol_zscore_21d_21d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vsa_drv3_022_vol_zscore_21d_21d_diff_slope_21d},
    "vsa_drv3_023_obv_21d_change_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_023_obv_21d_change_5d_diff_5d_diff},
    "vsa_drv3_024_neg_vol_fraction_21d_slope_21d": {"inputs": ["close", "volume"], "func": vsa_drv3_024_neg_vol_fraction_21d_slope_21d},
    "vsa_drv3_025_vol_elevated_days_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vsa_drv3_025_vol_elevated_days_21d_5d_diff_5d_diff},
}
