"""
118_drawdown_recovery_asymmetry — 2nd Derivatives (Features dra_drv2_001-025)
Domain: rate of change of base drawdown-recovery asymmetry features —
        velocity of asymmetry metrics (gain/loss ratio change, vol-asymmetry
        acceleration, streak-ratio velocity, speed-asymmetry momentum).
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
        x_m = x[~np.isnan(x)].mean() if np.any(~np.isnan(x)) else np.nan
        if np.isnan(x_m):
            return np.nan
        x_filled = np.where(np.isnan(x), x_m, x)
        num = ((xi - xi_m) * (x_filled - x_filled.mean())).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)


def _gain_loss_ratio(close: pd.Series, w: int) -> pd.Series:
    """Rolling gain/loss ratio over window w."""
    ret = close.pct_change(1)
    up = _rolling_sum(ret.clip(lower=0.0), w)
    dn = _rolling_sum((-ret).clip(lower=0.0), w)
    return _safe_div(up, dn.replace(0, np.nan))


def _vol_asym_ratio(close: pd.Series, w: int) -> pd.Series:
    """Rolling downside/upside vol ratio over window w."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(w, min_periods=max(1, w // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(w, min_periods=max(1, w // 2)).std()
    return _safe_div(dn_vol, up_vol.replace(0, np.nan))


def _speed_asym_ratio(close: pd.Series, w: int) -> pd.Series:
    """Rolling dn-speed / up-speed ratio over window w."""
    ret = close.pct_change(1)
    dn_sum = _rolling_sum((-ret).clip(lower=0.0), w)
    dn_cnt = _rolling_sum((ret < 0).astype(float), w).replace(0, np.nan)
    up_sum = _rolling_sum(ret.clip(lower=0.0), w)
    up_cnt = _rolling_sum((ret > 0).astype(float), w).replace(0, np.nan)
    dn_spd = _safe_div(dn_sum, dn_cnt)
    up_spd = _safe_div(up_sum, up_cnt)
    return _safe_div(dn_spd, up_spd.replace(0, np.nan))


def _dn_participation_rate(close: pd.Series, w: int) -> pd.Series:
    """Rolling downside participation rate over window w."""
    ret = close.pct_change(1)
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, w)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, w)
    return _safe_div(dn_sq, dn_sq + up_sq + _EPS)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def dra_drv2_001_gain_loss_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d gain/loss ratio (velocity of gain/loss ratio change)."""
    return _gain_loss_ratio(close, _TD_MON).diff(_TD_WEEK)


def dra_drv2_002_gain_loss_ratio_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d gain/loss ratio (monthly velocity of gain/loss ratio)."""
    return _gain_loss_ratio(close, _TD_MON).diff(_TD_MON)


def dra_drv2_003_vol_asym_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d vol-asymmetry ratio (vol-asymmetry velocity)."""
    return _vol_asym_ratio(close, _TD_MON).diff(_TD_WEEK)


def dra_drv2_004_vol_asym_ratio_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d vol-asymmetry ratio."""
    return _vol_asym_ratio(close, _TD_MON).diff(_TD_MON)


def dra_drv2_005_speed_asym_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d speed-asymmetry ratio (speed-asymmetry velocity)."""
    return _speed_asym_ratio(close, _TD_MON).diff(_TD_WEEK)


def dra_drv2_006_speed_asym_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d speed-asymmetry ratio."""
    return _speed_asym_ratio(close, _TD_QTR).diff(_TD_WEEK)


def dra_drv2_007_dn_participation_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d downside-participation rate (participation-rate velocity)."""
    return _dn_participation_rate(close, _TD_MON).diff(_TD_WEEK)


def dra_drv2_008_dn_participation_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d downside-participation rate."""
    return _dn_participation_rate(close, _TD_MON).diff(_TD_MON)


def dra_drv2_009_up_dn_avg_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d up/dn average-return ratio (mean-size asymmetry velocity)."""
    ret = close.pct_change(1)
    up = ret.clip(lower=0.0)
    dn = (-ret).clip(lower=0.0)
    avg_up = up.where(up > 0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    avg_dn = dn.where(dn > 0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    ratio = _safe_div(avg_up, avg_dn.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def dra_drv2_010_streak_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d dn/up streak ratio (streak-asymmetry velocity)."""
    ret = close.pct_change(1)
    dn_st = _consec_streak(ret < 0)
    up_st = _consec_streak(ret > 0)
    max_dn = dn_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    max_up = up_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    ratio = _safe_div(max_dn, max_up.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def dra_drv2_011_dn_count_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d down-day count (velocity of down-day accumulation)."""
    dn_cnt = _rolling_sum((close.pct_change(1) < 0).astype(float), _TD_MON)
    return dn_cnt.diff(_TD_WEEK)


def dra_drv2_012_ratchet_score_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d ratchet score (ratchet velocity)."""
    ret = close.pct_change(1)
    prev_up = ret.clip(lower=0.0).shift(1)
    dn = (-ret).clip(lower=0.0)
    ratchet = _rolling_sum((dn - prev_up).clip(lower=0.0), _TD_MON)
    return ratchet.diff(_TD_WEEK)


def dra_drv2_013_path_tortuosity_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d path tortuosity (velocity of tortuosity change)."""
    gross = _rolling_sum(close.pct_change(1).abs(), _TD_MON)
    net = close.pct_change(_TD_MON).abs()
    tortuosity = _safe_div(gross, net.replace(0, np.nan))
    return tortuosity.diff(_TD_WEEK)


def dra_drv2_014_dn_tortuosity_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d down-path tortuosity."""
    gross_dn = _rolling_sum((-close.pct_change(1)).clip(lower=0.0), _TD_MON)
    net_dn = (-close.pct_change(_TD_MON)).clip(lower=0.0)
    tort = _safe_div(gross_dn, net_dn.replace(0, np.nan))
    return tort.diff(_TD_WEEK)


def dra_drv2_015_vol_asym_ratio_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d vol-asymmetry ratio."""
    return _vol_asym_ratio(close, _TD_QTR).diff(_TD_WEEK)


def dra_drv2_016_gain_loss_ratio_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d gain/loss ratio."""
    return _gain_loss_ratio(close, _TD_QTR).diff(_TD_WEEK)


def dra_drv2_017_max_dn_ret_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d maximum down-day return (velocity of worst-day deepening)."""
    max_dn = _rolling_max((-close.pct_change(1)).clip(lower=0.0), _TD_MON)
    return max_dn.diff(_TD_WEEK)


def dra_drv2_018_max_up_ret_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d maximum up-day return."""
    max_up = _rolling_max(close.pct_change(1).clip(lower=0.0), _TD_MON)
    return max_up.diff(_TD_WEEK)


def dra_drv2_019_dn_participation_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63d downside-participation rate."""
    return _dn_participation_rate(close, _TD_QTR).diff(_TD_WEEK)


def dra_drv2_020_gain_loss_ratio_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21d gain/loss ratio (trend of asymmetry)."""
    return _linslope(_gain_loss_ratio(close, _TD_MON), _TD_MON)


def dra_drv2_021_vol_asym_ratio_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21d vol-asymmetry ratio."""
    return _linslope(_vol_asym_ratio(close, _TD_MON), _TD_MON)


def dra_drv2_022_speed_asym_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21d speed-asymmetry ratio."""
    return _linslope(_speed_asym_ratio(close, _TD_MON), _TD_MON)


def dra_drv2_023_streak_ratio_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21d dn/up streak ratio."""
    ret = close.pct_change(1)
    dn_st = _consec_streak(ret < 0)
    up_st = _consec_streak(ret > 0)
    max_dn = dn_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    max_up = up_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    ratio = _safe_div(max_dn, max_up.replace(0, np.nan))
    return _linslope(ratio, _TD_MON)


def dra_drv2_024_dn_participation_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21d downside-participation rate."""
    return _linslope(_dn_participation_rate(close, _TD_MON), _TD_MON)


def dra_drv2_025_asymmetry_composite_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21d composite asymmetry index (velocity of composite)."""
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
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_RECOVERY_ASYMMETRY_REGISTRY_2ND_DERIVATIVES = {
    "dra_drv2_001_gain_loss_ratio_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_001_gain_loss_ratio_21d_5d_diff},
    "dra_drv2_002_gain_loss_ratio_21d_21d_diff": {"inputs": ["close"], "func": dra_drv2_002_gain_loss_ratio_21d_21d_diff},
    "dra_drv2_003_vol_asym_ratio_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_003_vol_asym_ratio_21d_5d_diff},
    "dra_drv2_004_vol_asym_ratio_21d_21d_diff": {"inputs": ["close"], "func": dra_drv2_004_vol_asym_ratio_21d_21d_diff},
    "dra_drv2_005_speed_asym_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_005_speed_asym_21d_5d_diff},
    "dra_drv2_006_speed_asym_63d_5d_diff": {"inputs": ["close"], "func": dra_drv2_006_speed_asym_63d_5d_diff},
    "dra_drv2_007_dn_participation_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_007_dn_participation_21d_5d_diff},
    "dra_drv2_008_dn_participation_21d_21d_diff": {"inputs": ["close"], "func": dra_drv2_008_dn_participation_21d_21d_diff},
    "dra_drv2_009_up_dn_avg_ratio_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_009_up_dn_avg_ratio_21d_5d_diff},
    "dra_drv2_010_streak_ratio_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_010_streak_ratio_21d_5d_diff},
    "dra_drv2_011_dn_count_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_011_dn_count_21d_5d_diff},
    "dra_drv2_012_ratchet_score_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_012_ratchet_score_21d_5d_diff},
    "dra_drv2_013_path_tortuosity_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_013_path_tortuosity_21d_5d_diff},
    "dra_drv2_014_dn_tortuosity_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_014_dn_tortuosity_21d_5d_diff},
    "dra_drv2_015_vol_asym_ratio_63d_5d_diff": {"inputs": ["close"], "func": dra_drv2_015_vol_asym_ratio_63d_5d_diff},
    "dra_drv2_016_gain_loss_ratio_63d_5d_diff": {"inputs": ["close"], "func": dra_drv2_016_gain_loss_ratio_63d_5d_diff},
    "dra_drv2_017_max_dn_ret_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_017_max_dn_ret_21d_5d_diff},
    "dra_drv2_018_max_up_ret_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_018_max_up_ret_21d_5d_diff},
    "dra_drv2_019_dn_participation_63d_5d_diff": {"inputs": ["close"], "func": dra_drv2_019_dn_participation_63d_5d_diff},
    "dra_drv2_020_gain_loss_ratio_21d_slope_21d": {"inputs": ["close"], "func": dra_drv2_020_gain_loss_ratio_21d_slope_21d},
    "dra_drv2_021_vol_asym_ratio_21d_slope_21d": {"inputs": ["close"], "func": dra_drv2_021_vol_asym_ratio_21d_slope_21d},
    "dra_drv2_022_speed_asym_21d_slope_21d": {"inputs": ["close"], "func": dra_drv2_022_speed_asym_21d_slope_21d},
    "dra_drv2_023_streak_ratio_21d_slope_21d": {"inputs": ["close"], "func": dra_drv2_023_streak_ratio_21d_slope_21d},
    "dra_drv2_024_dn_participation_21d_slope_21d": {"inputs": ["close"], "func": dra_drv2_024_dn_participation_21d_slope_21d},
    "dra_drv2_025_asymmetry_composite_21d_5d_diff": {"inputs": ["close"], "func": dra_drv2_025_asymmetry_composite_21d_5d_diff},
}
