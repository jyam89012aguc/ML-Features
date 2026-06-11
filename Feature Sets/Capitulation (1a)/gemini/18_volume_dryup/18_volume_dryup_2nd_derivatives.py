"""
18_volume_dryup — 2nd Derivatives
Domain: rate of change of base features — captures acceleration of decline/distress
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

# 25 features capturing acceleration of volume dry-up metrics
def vdry_drv2_001_dryup_ratio_21d_velocity(volume: pd.Series) -> pd.Series:
    # Change in dry-up intensity
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    return v_rat.diff(5)


def vdry_drv2_002_consecutive_low_volume_velocity(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    below = (volume < med).astype(int)
    dur = below.groupby((below == 0).cumsum()).cumsum()
    return dur.diff(5)


def vdry_drv2_003_volume_starvation_velocity(volume: pd.Series) -> pd.Series:
    q10 = volume.rolling(252).quantile(0.1)
    st = (volume < q10).rolling(63).mean()
    return st.diff(5)


def vdry_drv2_004_vol_adjusted_dryup_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, _rolling_median(volume, 63))
    v = close.pct_change().rolling(63).std()
    score = _safe_div(ratio, v)
    return score.diff(5)


def vdry_drv2_005_dollar_volume_dryup_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    rat = _safe_div(dv, _rolling_median(dv, 252))
    return rat.diff(5)


def vdry_drv2_006_turnover_dryup_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    rat = _safe_div(to, _rolling_median(to, 252))
    return rat.diff(5)


def vdry_drv2_007_volume_apathy_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    p_vol = close.pct_change().rolling(63).std()
    ap = _safe_div(1.0, v_rat * p_vol + _EPS)
    return ap.diff(5)


def vdry_drv2_008_volume_void_velocity(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    void = (med - volume).clip(lower=0).rolling(63).sum() / _rolling_mean(volume, 252)
    return void.diff(5)


def vdry_drv2_009_climax_to_dryup_ratio_velocity(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(63).max()
    rat = _safe_div(mx, volume)
    return rat.diff(5)


def vdry_drv2_010_volume_entropy_dryup_velocity(volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = volume.rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def vdry_drv2_011_volume_floor_proximity_velocity(volume: pd.Series) -> pd.Series:
    l = volume.rolling(252).min()
    prox = _safe_div(volume, l)
    return prox.diff(5)


def vdry_drv2_012_volume_exhaustion_prob_velocity(volume: pd.Series) -> pd.Series:
    is_low = (volume < _rolling_median(volume, 252))
    prob = (is_low & is_low.shift(1)).rolling(63).sum() / (is_low.shift(1).rolling(63).sum() + _EPS)
    return prob.diff(5)


def vdry_drv2_013_terminal_apathy_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    p_vel = np.log(close).diff(5).abs()
    score = _safe_div(1.0, v_rat * p_vel + _EPS)
    return score.diff(5)


def vdry_drv2_014_mktcap_volume_starvation_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    score = _safe_div(np.log(mc + _EPS), v_rat + _EPS)
    return score.diff(5)


def vdry_drv2_015_volume_dryup_final_exhaustion_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_per = (volume < _rolling_median(volume, 252)).rolling(63).mean()
    r = (close.rolling(21).max() - close.rolling(21).min()) / (close.rolling(21).mean() + _EPS)
    score = _safe_div(v_per, r + _EPS)
    return score.diff(5)


def vdry_drv2_016_consecutive_volume_decline_velocity(volume: pd.Series) -> pd.Series:
    is_dec = (volume < volume.shift(1)).astype(int)
    dur = is_dec.groupby((is_dec == 0).cumsum()).cumsum()
    return dur.diff(5)


def vdry_drv2_017_volume_dryup_zscore_persistence_velocity(volume: pd.Series) -> pd.Series:
    z = (volume - _rolling_mean(volume, 252)) / (volume.rolling(252).std() + _EPS)
    per = z.rolling(63).mean()
    return per.diff(5)


def vdry_drv2_018_volume_dryup_rank_velocity(volume: pd.Series) -> pd.Series:
    rank = volume.rolling(252).rank(pct=True)
    return rank.diff(5)


def vdry_drv2_019_volume_dryup_at_earnings_velocity(volume: pd.Series, surprise: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, _rolling_median(volume, 252))
    val = ratio.where(surprise.abs() > 0).ffill()
    return val.diff(5)


def vdry_drv2_020_volume_dryup_to_range_velocity(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    r_rat = _safe_div(high - low, _rolling_median(high - low, 21))
    score = _safe_div(1.0, v_rat * r_rat + _EPS)
    return score.diff(5)


def vdry_drv2_021_days_under_volume_floor_velocity(volume: pd.Series) -> pd.Series:
    avg = volume.expanding().mean()
    idx = pd.Series(np.arange(len(volume)), index=volume.index).where(volume > avg).ffill()
    dur = pd.Series(np.arange(len(volume)), index=volume.index) - idx
    return dur.diff(5)


def vdry_drv2_022_volume_apathy_zscore_velocity(volume: pd.Series) -> pd.Series:
    inv_v = 1.0 / (volume + 1.0)
    z = (inv_v - inv_v.rolling(252).mean()) / inv_v.rolling(252).std()
    return z.diff(5)


def vdry_drv2_023_ratio_days_low_rank_velocity(volume: pd.Series) -> pd.Series:
    rank = volume.rolling(252).rank(pct=True)
    ratio = (rank < 0.10).rolling(252).mean()
    return ratio.diff(5)


def vdry_drv2_024_climax_to_dryup_spread_velocity(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(63).max()
    score = (mx - volume) / (mx + _EPS)
    return score.diff(5)


def vdry_drv2_025_volume_dryup_composite_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ap = _safe_div(1.0, (_safe_div(volume, _rolling_median(volume, 63)) * close.pct_change().rolling(63).std()) + _EPS)
    st = (volume < volume.rolling(252).quantile(0.1)).rolling(63).mean()
    cd = _safe_div((volume < _rolling_median(volume, 21)).astype(int).groupby((volume < _rolling_median(volume, 21)) == 0).cumsum(), 21.0)
    score = (0.4 * ap + 0.3 * st + 0.3 * cd.clip(0,1))
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V18_V_REGISTRY = {
    "vdry_drv2_001_dryup_ratio_21d_velocity": {"inputs": ["volume"], "func": vdry_drv2_001_dryup_ratio_21d_velocity},
    "vdry_drv2_002_consecutive_low_volume_velocity": {"inputs": ["volume"], "func": vdry_drv2_002_consecutive_low_volume_velocity},
    "vdry_drv2_003_volume_starvation_velocity": {"inputs": ["volume"], "func": vdry_drv2_003_volume_starvation_velocity},
    "vdry_drv2_004_vol_adjusted_dryup_velocity": {"inputs": ["close", "volume"], "func": vdry_drv2_004_vol_adjusted_dryup_velocity},
    "vdry_drv2_005_dollar_volume_dryup_velocity": {"inputs": ["close", "volume"], "func": vdry_drv2_005_dollar_volume_dryup_velocity},
    "vdry_drv2_006_turnover_dryup_velocity": {"inputs": ["volume", "sharesbas"], "func": vdry_drv2_006_turnover_dryup_velocity},
    "vdry_drv2_007_volume_apathy_velocity": {"inputs": ["close", "volume"], "func": vdry_drv2_007_volume_apathy_velocity},
    "vdry_drv2_008_volume_void_velocity": {"inputs": ["volume"], "func": vdry_drv2_008_volume_void_velocity},
    "vdry_drv2_009_climax_to_dryup_ratio_velocity": {"inputs": ["volume"], "func": vdry_drv2_009_climax_to_dryup_ratio_velocity},
    "vdry_drv2_010_volume_entropy_dryup_velocity": {"inputs": ["volume"], "func": vdry_drv2_010_volume_entropy_dryup_velocity},
    "vdry_drv2_011_volume_floor_proximity_velocity": {"inputs": ["volume"], "func": vdry_drv2_011_volume_floor_proximity_velocity},
    "vdry_drv2_012_volume_exhaustion_prob_velocity": {"inputs": ["volume"], "func": vdry_drv2_012_volume_exhaustion_prob_velocity},
    "vdry_drv2_013_terminal_apathy_velocity": {"inputs": ["close", "volume"], "func": vdry_drv2_013_terminal_apathy_velocity},
    "vdry_drv2_014_mktcap_volume_starvation_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vdry_drv2_014_mktcap_volume_starvation_velocity},
    "vdry_drv2_015_volume_dryup_final_exhaustion_velocity": {"inputs": ["close", "volume"], "func": vdry_drv2_015_volume_dryup_final_exhaustion_velocity},
    "vdry_drv2_016_consecutive_volume_decline_velocity": {"inputs": ["volume"], "func": vdry_drv2_016_consecutive_volume_decline_velocity},
    "vdry_drv2_017_volume_dryup_zscore_persistence_velocity": {"inputs": ["volume"], "func": vdry_drv2_017_volume_dryup_zscore_persistence_velocity},
    "vdry_drv2_018_volume_dryup_rank_velocity": {"inputs": ["volume"], "func": vdry_drv2_018_volume_dryup_rank_velocity},
    "vdry_drv2_019_volume_dryup_at_earnings_velocity": {"inputs": ["volume", "surprise"], "func": vdry_drv2_019_volume_dryup_at_earnings_velocity},
    "vdry_drv2_020_volume_dryup_to_range_velocity": {"inputs": ["high", "low", "volume"], "func": vdry_drv2_020_volume_dryup_to_range_velocity},
    "vdry_drv2_021_days_under_volume_floor_velocity": {"inputs": ["volume"], "func": vdry_drv2_021_days_under_volume_floor_velocity},
    "vdry_drv2_022_volume_apathy_zscore_velocity": {"inputs": ["volume"], "func": vdry_drv2_022_volume_apathy_zscore_velocity},
    "vdry_drv2_023_ratio_days_low_rank_velocity": {"inputs": ["volume"], "func": vdry_drv2_023_ratio_days_low_rank_velocity},
    "vdry_drv2_024_climax_to_dryup_spread_velocity": {"inputs": ["volume"], "func": vdry_drv2_024_climax_to_dryup_spread_velocity},
    "vdry_drv2_025_volume_dryup_composite_velocity": {"inputs": ["close", "volume"], "func": vdry_drv2_025_volume_dryup_composite_velocity},
}
