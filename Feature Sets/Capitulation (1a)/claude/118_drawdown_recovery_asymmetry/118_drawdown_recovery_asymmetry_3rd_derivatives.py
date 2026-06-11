"""
118_drawdown_recovery_asymmetry — 3rd Derivatives (Features dra_drv3_001-025)
Domain: rate of change of 2nd-derivative asymmetry features — acceleration of
        asymmetry velocity (gain/loss ratio jerk, vol-asymmetry acceleration,
        speed-asymmetry second derivative, streak-ratio higher-order change).
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        valid = ~np.isnan(x)
        if valid.sum() < 2:
            return np.nan
        x_m = x[valid].mean()
        x_filled = np.where(np.isnan(x), x_m, x)
        num = ((xi - xi_m) * (x_filled - x_filled.mean())).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)


def _gain_loss_ratio(close: pd.Series, w: int) -> pd.Series:
    ret = close.pct_change(1)
    up = _rolling_sum(ret.clip(lower=0.0), w)
    dn = _rolling_sum((-ret).clip(lower=0.0), w)
    return _safe_div(up, dn.replace(0, np.nan))


def _vol_asym_ratio(close: pd.Series, w: int) -> pd.Series:
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(w, min_periods=max(1, w // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(w, min_periods=max(1, w // 2)).std()
    return _safe_div(dn_vol, up_vol.replace(0, np.nan))


def _speed_asym_ratio(close: pd.Series, w: int) -> pd.Series:
    ret = close.pct_change(1)
    dn_sum = _rolling_sum((-ret).clip(lower=0.0), w)
    dn_cnt = _rolling_sum((ret < 0).astype(float), w).replace(0, np.nan)
    up_sum = _rolling_sum(ret.clip(lower=0.0), w)
    up_cnt = _rolling_sum((ret > 0).astype(float), w).replace(0, np.nan)
    return _safe_div(_safe_div(dn_sum, dn_cnt), _safe_div(up_sum, up_cnt))


def _dn_participation_rate(close: pd.Series, w: int) -> pd.Series:
    ret = close.pct_change(1)
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, w)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, w)
    return _safe_div(dn_sq, dn_sq + up_sq + _EPS)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def dra_drv3_001_gain_loss_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d gain/loss ratio (acceleration of ratio velocity)."""
    vel = _gain_loss_ratio(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_002_gain_loss_ratio_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 21d gain/loss ratio (jerk)."""
    vel21 = _gain_loss_ratio(close, _TD_MON).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dra_drv3_003_vol_asym_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d vol-asymmetry ratio (acceleration of vol-asym velocity)."""
    vel = _vol_asym_ratio(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_004_speed_asym_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d speed-asymmetry ratio (acceleration of speed-asym)."""
    vel = _speed_asym_ratio(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_005_dn_participation_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d dn-participation rate (acceleration of participation)."""
    vel = _dn_participation_rate(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_006_streak_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d dn/up streak ratio (acceleration of streak-asymmetry)."""
    ret = close.pct_change(1)
    dn_st = _consec_streak(ret < 0)
    up_st = _consec_streak(ret > 0)
    max_dn = dn_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    max_up = up_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    ratio = _safe_div(max_dn, max_up.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_007_ratchet_score_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d ratchet score (acceleration of ratchet velocity)."""
    ret = close.pct_change(1)
    prev_up = ret.clip(lower=0.0).shift(1)
    dn = (-ret).clip(lower=0.0)
    ratchet = _rolling_sum((dn - prev_up).clip(lower=0.0), _TD_MON)
    vel = ratchet.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_008_path_tortuosity_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d path tortuosity (acceleration of tortuosity change)."""
    gross = _rolling_sum(close.pct_change(1).abs(), _TD_MON)
    net = close.pct_change(_TD_MON).abs()
    tort = _safe_div(gross, net.replace(0, np.nan))
    vel = tort.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_009_gain_loss_ratio_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d gain/loss ratio (acceleration of quarterly asymmetry)."""
    vel = _gain_loss_ratio(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_010_vol_asym_ratio_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d vol-asymmetry ratio."""
    vel = _vol_asym_ratio(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_011_speed_asym_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d speed-asymmetry ratio."""
    vel = _speed_asym_ratio(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_012_dn_participation_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 21d dn-participation rate (jerk)."""
    vel21 = _dn_participation_rate(close, _TD_MON).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dra_drv3_013_vol_asym_ratio_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of vol-asymmetry ratio."""
    vel21 = _vol_asym_ratio(close, _TD_MON).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dra_drv3_014_speed_asym_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21d speed-asymmetry ratio."""
    vel = _speed_asym_ratio(close, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dra_drv3_015_gain_loss_ratio_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21d gain/loss ratio."""
    vel = _gain_loss_ratio(close, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dra_drv3_016_vol_asym_ratio_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21d vol-asymmetry ratio."""
    vel = _vol_asym_ratio(close, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dra_drv3_017_dn_participation_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21d dn-participation rate."""
    vel = _dn_participation_rate(close, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dra_drv3_018_streak_ratio_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of streak-asymmetry ratio."""
    ret = close.pct_change(1)
    dn_st = _consec_streak(ret < 0)
    up_st = _consec_streak(ret > 0)
    max_dn = dn_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    max_up = up_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    ratio = _safe_div(max_dn, max_up.replace(0, np.nan))
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dra_drv3_019_ratchet_score_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21d ratchet score."""
    ret = close.pct_change(1)
    prev_up = ret.clip(lower=0.0).shift(1)
    dn = (-ret).clip(lower=0.0)
    ratchet = _rolling_sum((dn - prev_up).clip(lower=0.0), _TD_MON)
    vel = ratchet.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dra_drv3_020_gain_loss_ratio_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63d gain/loss ratio."""
    vel21 = _gain_loss_ratio(close, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dra_drv3_021_vol_asym_ratio_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63d vol-asymmetry ratio."""
    vel21 = _vol_asym_ratio(close, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dra_drv3_022_asymmetry_composite_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d composite asymmetry index (acceleration of composite)."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    vol_asym = _safe_div(dn_vol, up_vol + _EPS)
    dn_sum = _rolling_sum((-ret).clip(lower=0.0), _TD_MON)
    up_sum = _rolling_sum(ret.clip(lower=0.0), _TD_MON)
    gl_inv = _safe_div(dn_sum, up_sum + _EPS)
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_MON)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_MON)
    dn_part = _safe_div(dn_sq, dn_sq + up_sq + _EPS)
    dn_cnt = _rolling_sum((ret < 0).astype(float), _TD_MON)
    up_cnt = _rolling_sum((ret > 0).astype(float), _TD_MON)
    dn_spd = _safe_div(dn_sum, dn_cnt.replace(0, np.nan))
    up_spd = _safe_div(up_sum, up_cnt.replace(0, np.nan))
    spd_asym = _safe_div(dn_spd, up_spd + _EPS)
    composite = (vol_asym.fillna(1.0) + gl_inv.fillna(1.0) +
                 dn_part.fillna(0.5) * 2 + spd_asym.fillna(1.0)) / 4.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_023_dn_tortuosity_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d down-path tortuosity (acceleration of tortuosity)."""
    gross_dn = _rolling_sum((-close.pct_change(1)).clip(lower=0.0), _TD_MON)
    net_dn = (-close.pct_change(_TD_MON)).clip(lower=0.0)
    tort = _safe_div(gross_dn, net_dn.replace(0, np.nan))
    vel = tort.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dra_drv3_024_gain_loss_ratio_21d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of 21d gain/loss ratio (slope-of-slope velocity)."""
    slope21 = _linslope(_gain_loss_ratio(close, _TD_MON), _TD_MON)
    return slope21.diff(_TD_WEEK)


def dra_drv3_025_speed_asym_21d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of 21d speed-asymmetry ratio."""
    slope21 = _linslope(_speed_asym_ratio(close, _TD_MON), _TD_MON)
    return slope21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_RECOVERY_ASYMMETRY_REGISTRY_3RD_DERIVATIVES = {
    "dra_drv3_001_gain_loss_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_001_gain_loss_ratio_21d_5d_diff_5d_diff},
    "dra_drv3_002_gain_loss_ratio_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_002_gain_loss_ratio_21d_21d_diff_5d_diff},
    "dra_drv3_003_vol_asym_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_003_vol_asym_ratio_21d_5d_diff_5d_diff},
    "dra_drv3_004_speed_asym_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_004_speed_asym_21d_5d_diff_5d_diff},
    "dra_drv3_005_dn_participation_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_005_dn_participation_21d_5d_diff_5d_diff},
    "dra_drv3_006_streak_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_006_streak_ratio_21d_5d_diff_5d_diff},
    "dra_drv3_007_ratchet_score_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_007_ratchet_score_21d_5d_diff_5d_diff},
    "dra_drv3_008_path_tortuosity_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_008_path_tortuosity_21d_5d_diff_5d_diff},
    "dra_drv3_009_gain_loss_ratio_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_009_gain_loss_ratio_63d_5d_diff_5d_diff},
    "dra_drv3_010_vol_asym_ratio_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_010_vol_asym_ratio_63d_5d_diff_5d_diff},
    "dra_drv3_011_speed_asym_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_011_speed_asym_63d_5d_diff_5d_diff},
    "dra_drv3_012_dn_participation_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_012_dn_participation_21d_21d_diff_5d_diff},
    "dra_drv3_013_vol_asym_ratio_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_013_vol_asym_ratio_21d_21d_diff_5d_diff},
    "dra_drv3_014_speed_asym_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dra_drv3_014_speed_asym_21d_5d_diff_slope_21d},
    "dra_drv3_015_gain_loss_ratio_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dra_drv3_015_gain_loss_ratio_21d_5d_diff_slope_21d},
    "dra_drv3_016_vol_asym_ratio_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dra_drv3_016_vol_asym_ratio_21d_5d_diff_slope_21d},
    "dra_drv3_017_dn_participation_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dra_drv3_017_dn_participation_21d_5d_diff_slope_21d},
    "dra_drv3_018_streak_ratio_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dra_drv3_018_streak_ratio_21d_5d_diff_slope_21d},
    "dra_drv3_019_ratchet_score_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dra_drv3_019_ratchet_score_21d_5d_diff_slope_21d},
    "dra_drv3_020_gain_loss_ratio_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_020_gain_loss_ratio_63d_21d_diff_5d_diff},
    "dra_drv3_021_vol_asym_ratio_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_021_vol_asym_ratio_63d_21d_diff_5d_diff},
    "dra_drv3_022_asymmetry_composite_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_022_asymmetry_composite_21d_5d_diff_5d_diff},
    "dra_drv3_023_dn_tortuosity_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dra_drv3_023_dn_tortuosity_21d_5d_diff_5d_diff},
    "dra_drv3_024_gain_loss_ratio_21d_slope_21d_5d_diff": {"inputs": ["close"], "func": dra_drv3_024_gain_loss_ratio_21d_slope_21d_5d_diff},
    "dra_drv3_025_speed_asym_21d_slope_21d_5d_diff": {"inputs": ["close"], "func": dra_drv3_025_speed_asym_21d_slope_21d_5d_diff},
}
