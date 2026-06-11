"""
18_volume_dryup — 3rd Derivatives
Domain: rate of change of 2nd derivatives — captures exhaustion/inflection of acceleration
Asset class: US equities | Daily OHLCV + Sharadar fundamentals
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
TRADING_DAYS_YEAR = 252
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
_EPS = 1e-9


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing exhaustion/inflection of volume dry-up acceleration (jerk)
def vdry_drv3_001_dryup_ratio_21d_jerk(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    vel = v_rat.diff(5)
    return vel.diff(5)


def vdry_drv3_002_consecutive_low_volume_jerk(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    below = (volume < med).astype(int)
    dur = below.groupby((below == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vdry_drv3_003_volume_starvation_jerk(volume: pd.Series) -> pd.Series:
    q10 = volume.rolling(252).quantile(0.1)
    st = (volume < q10).rolling(63).mean()
    vel = st.diff(5)
    return vel.diff(5)


def vdry_drv3_004_vol_adjusted_dryup_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, _rolling_median(volume, 63))
    v = close.pct_change().rolling(63).std()
    score = _safe_div(ratio, v)
    vel = score.diff(5)
    return vel.diff(5)


def vdry_drv3_005_dollar_volume_dryup_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    rat = _safe_div(dv, _rolling_median(dv, 252))
    vel = rat.diff(5)
    return vel.diff(5)


def vdry_drv3_006_turnover_dryup_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    rat = _safe_div(to, _rolling_median(to, 252))
    vel = rat.diff(5)
    return vel.diff(5)


def vdry_drv3_007_volume_apathy_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    p_vol = close.pct_change().rolling(63).std()
    ap = _safe_div(1.0, v_rat * p_vol + _EPS)
    vel = ap.diff(5)
    return vel.diff(5)


def vdry_drv3_008_volume_void_jerk(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    void = (med - volume).clip(lower=0).rolling(63).sum() / (volume.rolling(252).mean() + _EPS)
    vel = void.diff(5)
    return vel.diff(5)


def vdry_drv3_009_climax_to_dryup_ratio_jerk(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(63).max()
    rat = _safe_div(mx, volume)
    vel = rat.diff(5)
    return vel.diff(5)


def vdry_drv3_010_volume_entropy_dryup_jerk(volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = volume.rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)


def vdry_drv3_011_volume_floor_proximity_jerk(volume: pd.Series) -> pd.Series:
    l = volume.rolling(252).min()
    prox = _safe_div(volume, l)
    vel = prox.diff(5)
    return vel.diff(5)


def vdry_drv3_012_volume_exhaustion_prob_jerk(volume: pd.Series) -> pd.Series:
    is_low = (volume < _rolling_median(volume, 252))
    prob = (is_low & is_low.shift(1)).rolling(63).sum() / (is_low.shift(1).rolling(63).sum() + _EPS)
    vel = prob.diff(5)
    return vel.diff(5)


def vdry_drv3_013_terminal_apathy_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    p_vel = np.log(close).diff(5).abs()
    score = _safe_div(1.0, v_rat * p_vel + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vdry_drv3_014_mktcap_volume_starvation_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    score = _safe_div(np.log(mc + _EPS), v_rat + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vdry_drv3_015_volume_dryup_final_exhaustion_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_per = (volume < _rolling_median(volume, 252)).rolling(63).mean()
    r = (close.rolling(21).max() - close.rolling(21).min()) / (close.rolling(21).mean() + _EPS)
    score = _safe_div(v_per, r + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vdry_drv3_016_consecutive_volume_decline_jerk(volume: pd.Series) -> pd.Series:
    is_dec = (volume < volume.shift(1)).astype(int)
    dur = is_dec.groupby((is_dec == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vdry_drv3_017_volume_dryup_zscore_persistence_jerk(volume: pd.Series) -> pd.Series:
    z = (volume - _rolling_mean(volume, 252)) / (volume.rolling(252).std() + _EPS)
    per = z.rolling(63).mean()
    vel = per.diff(5)
    return vel.diff(5)


def vdry_drv3_018_volume_dryup_rank_jerk(volume: pd.Series) -> pd.Series:
    rank = volume.rolling(252).rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def vdry_drv3_019_volume_dryup_at_earnings_jerk(volume: pd.Series, surprise: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, _rolling_median(volume, 252))
    val = ratio.where(surprise.abs() > 0).ffill()
    vel = val.diff(5)
    return vel.diff(5)


def vdry_drv3_020_volume_dryup_to_range_jerk(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    r_rat = _safe_div(high - low, _rolling_median(high - low, 21))
    score = _safe_div(1.0, v_rat * r_rat + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vdry_drv3_021_days_under_volume_floor_jerk(volume: pd.Series) -> pd.Series:
    avg = volume.expanding().mean()
    idx = pd.Series(np.arange(len(volume)), index=volume.index).where(volume > avg).ffill()
    dur = pd.Series(np.arange(len(volume)), index=volume.index) - idx
    vel = dur.diff(5)
    return vel.diff(5)


def vdry_drv3_022_volume_apathy_zscore_jerk(volume: pd.Series) -> pd.Series:
    inv_v = 1.0 / (volume + 1.0)
    z = (inv_v - inv_v.rolling(252).mean()) / (inv_v.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vdry_drv3_023_ratio_days_low_rank_jerk(volume: pd.Series) -> pd.Series:
    rank = volume.rolling(252).rank(pct=True)
    ratio = (rank < 0.10).rolling(252).mean()
    vel = ratio.diff(5)
    return vel.diff(5)


def vdry_drv3_024_climax_to_dryup_spread_jerk(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(63).max()
    score = (mx - volume) / (mx + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vdry_drv3_025_volume_dryup_composite_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    from scipy.stats import linregress
    ap = _safe_div(1.0, (_safe_div(volume, _rolling_median(volume, 63)) * close.pct_change().rolling(63).std()) + _EPS)
    st = (volume < volume.rolling(252).quantile(0.1)).rolling(63).mean()
    score = (0.4 * ap + 0.3 * st)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V18_A_REGISTRY = {
    "vdry_drv3_001_dryup_ratio_21d_jerk": {"inputs": ["volume"], "func": vdry_drv3_001_dryup_ratio_21d_jerk},
    "vdry_drv3_002_consecutive_low_volume_jerk": {"inputs": ["volume"], "func": vdry_drv3_002_consecutive_low_volume_jerk},
    "vdry_drv3_003_volume_starvation_jerk": {"inputs": ["volume"], "func": vdry_drv3_003_volume_starvation_jerk},
    "vdry_drv3_004_vol_adjusted_dryup_jerk": {"inputs": ["close", "volume"], "func": vdry_drv3_004_vol_adjusted_dryup_jerk},
    "vdry_drv3_005_dollar_volume_dryup_jerk": {"inputs": ["close", "volume"], "func": vdry_drv3_005_dollar_volume_dryup_jerk},
    "vdry_drv3_006_turnover_dryup_jerk": {"inputs": ["volume", "sharesbas"], "func": vdry_drv3_006_turnover_dryup_jerk},
    "vdry_drv3_007_volume_apathy_jerk": {"inputs": ["close", "volume"], "func": vdry_drv3_007_volume_apathy_jerk},
    "vdry_drv3_008_volume_void_jerk": {"inputs": ["volume"], "func": vdry_drv3_008_volume_void_jerk},
    "vdry_drv3_009_climax_to_dryup_ratio_jerk": {"inputs": ["volume"], "func": vdry_drv3_009_climax_to_dryup_ratio_jerk},
    "vdry_drv3_010_volume_entropy_dryup_jerk": {"inputs": ["volume"], "func": vdry_drv3_010_volume_entropy_dryup_jerk},
    "vdry_drv3_011_volume_floor_proximity_jerk": {"inputs": ["volume"], "func": vdry_drv3_011_volume_floor_proximity_jerk},
    "vdry_drv3_012_volume_exhaustion_prob_jerk": {"inputs": ["volume"], "func": vdry_drv3_012_volume_exhaustion_prob_jerk},
    "vdry_drv3_013_terminal_apathy_jerk": {"inputs": ["close", "volume"], "func": vdry_drv3_013_terminal_apathy_jerk},
    "vdry_drv3_014_mktcap_volume_starvation_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vdry_drv3_014_mktcap_volume_starvation_jerk},
    "vdry_drv3_015_volume_dryup_final_exhaustion_jerk": {"inputs": ["close", "volume"], "func": vdry_drv3_015_volume_dryup_final_exhaustion_jerk},
    "vdry_drv3_016_consecutive_volume_decline_jerk": {"inputs": ["volume"], "func": vdry_drv3_016_consecutive_volume_decline_jerk},
    "vdry_drv3_017_volume_dryup_zscore_persistence_jerk": {"inputs": ["volume"], "func": vdry_drv3_017_volume_dryup_zscore_persistence_jerk},
    "vdry_drv3_018_volume_dryup_rank_jerk": {"inputs": ["volume"], "func": vdry_drv3_018_volume_dryup_rank_jerk},
    "vdry_drv3_019_volume_dryup_at_earnings_jerk": {"inputs": ["volume", "surprise"], "func": vdry_drv3_019_volume_dryup_at_earnings_jerk},
    "vdry_drv3_020_volume_dryup_to_range_jerk": {"inputs": ["high", "low", "volume"], "func": vdry_drv3_020_volume_dryup_to_range_jerk},
    "vdry_drv3_021_days_under_volume_floor_jerk": {"inputs": ["volume"], "func": vdry_drv3_021_days_under_volume_floor_jerk},
    "vdry_drv3_022_volume_apathy_zscore_jerk": {"inputs": ["volume"], "func": vdry_drv3_022_volume_apathy_zscore_jerk},
    "vdry_drv3_023_ratio_days_low_rank_jerk": {"inputs": ["volume"], "func": vdry_drv3_023_ratio_days_low_rank_jerk},
    "vdry_drv3_024_climax_to_dryup_spread_jerk": {"inputs": ["volume"], "func": vdry_drv3_024_climax_to_dryup_spread_jerk},
    "vdry_drv3_025_volume_dryup_composite_jerk": {"inputs": ["close", "volume"], "func": vdry_drv3_025_volume_dryup_composite_jerk},
}
