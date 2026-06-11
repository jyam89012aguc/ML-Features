"""
31_volatility_apathy — 3rd Derivatives
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing exhaustion/inflection of volatility apathy acceleration (jerk)
def vapt_drv3_001_vol_apathy_ratio_21d_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    med_v = v21.rolling(252).median()
    ratio = _safe_div(v21, med_v)
    vel = ratio.diff(5)
    return vel.diff(5)


def vapt_drv3_002_consecutive_low_vol_jerk(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    med_v = v5.rolling(252).median()
    below = (v5 < med_v).astype(int)
    dur = below.groupby((below == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vapt_drv3_003_vol_starvation_jerk(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    q10 = v5.rolling(252).quantile(0.1)
    st = (v5 < q10).rolling(63).mean()
    vel = st.diff(5)
    return vel.diff(5)


def vapt_drv3_004_vol_adjusted_dryup_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, volume.rolling(252).median())
    v = close.pct_change().rolling(63).std()
    score = _safe_div(ratio, v + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vapt_drv3_005_dollar_volume_dryup_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    rat = _safe_div(dv, dv.rolling(252).median())
    vel = rat.diff(5)
    return vel.diff(5)


def vapt_drv3_006_turnover_dryup_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    rat = _safe_div(to, to.rolling(252).median())
    vel = rat.diff(5)
    return vel.diff(5)


def vapt_drv3_007_vol_apathy_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, volume.rolling(252).median())
    p_vol = close.pct_change().rolling(63).std()
    ap = _safe_div(1.0, v_rat * p_vol + _EPS)
    vel = ap.diff(5)
    return vel.diff(5)


def vapt_drv3_008_vol_void_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    med = v.rolling(252).median()
    void = (med - v).clip(lower=0).rolling(63).sum() / (v.rolling(252).mean() + _EPS)
    vel = void.diff(5)
    return vel.diff(5)


def vapt_drv3_009_climax_to_apathy_ratio_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    mx = v.rolling(63).max()
    rat = _safe_div(mx, v)
    vel = rat.diff(5)
    return vel.diff(5)


def vapt_drv3_010_vol_apathy_entropy_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = v.rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)


def vapt_drv3_011_vol_floor_proximity_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    l = v21.rolling(252).min()
    prox = _safe_div(v21, l)
    vel = prox.diff(5)
    return vel.diff(5)


def vapt_drv3_012_vol_exhaustion_prob_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    med = v21.rolling(252).median()
    is_low = (v21 < med)
    prob = (is_low & is_low.shift(1)).rolling(63).sum() / (is_low.shift(1).rolling(63).sum() + _EPS)
    vel = prob.diff(5)
    return vel.diff(5)


def vapt_drv3_013_terminal_washout_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).median())
    vol_rat = _safe_div(volume, volume.rolling(252).median())
    p_vel = np.log(close).diff(5).abs()
    score = _safe_div(1.0, v_rat * vol_rat * p_vel + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vapt_drv3_014_mktcap_vol_starvation_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v_rat = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).median())
    score = _safe_div(np.log(mc + _EPS), v_rat + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vapt_drv3_015_vol_apathy_final_exhaustion_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    from scipy.stats import linregress
    score = vapt_150_vol_apathy_final_exhaustion_score(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vapt_drv3_016_consecutive_vol_decline_jerk(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    is_dec = (v5 < v5.shift(1)).astype(int)
    dur = is_dec.groupby((is_dec == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vapt_drv3_017_vol_apathy_zscore_persistence_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    z = (v21 - v21.rolling(252).mean()) / (v21.rolling(252).std() + _EPS)
    per = z.rolling(63).mean()
    vel = per.diff(5)
    return vel.diff(5)


def vapt_drv3_018_vol_apathy_rank_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    rank = v21.rolling(252).rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def vapt_drv3_019_vol_apathy_at_earnings_jerk(close: pd.Series, surprise: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    ratio = _safe_div(v21, v21.rolling(252).median())
    val = ratio.where(surprise.abs() > 0).ffill()
    vel = val.diff(5)
    return vel.diff(5)


def vapt_drv3_020_vol_apathy_to_range_jerk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_rat = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).median())
    r = (high - low) / close
    r_rat = _safe_div(r, r.rolling(252).median())
    score = _safe_div(1.0, v_rat * r_rat + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vapt_drv3_021_days_under_vol_floor_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg = v21.expanding().mean()
    idx = pd.Series(np.arange(len(close)), index=close.index).where(v21 > avg).ffill()
    dur = pd.Series(np.arange(len(close)), index=close.index) - idx
    vel = dur.diff(5)
    return vel.diff(5)


def vapt_drv3_022_vol_apathy_zscore_ath_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    inv_v = 1.0 / (v21 + _EPS)
    z = (inv_v - inv_v.expanding().mean()) / (inv_v.expanding().std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vapt_drv3_023_ratio_days_vol_low_rank_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    rank = v21.rolling(252).rank(pct=True)
    ratio = (rank < 0.10).rolling(252).mean()
    vel = ratio.diff(5)
    return vel.diff(5)


def vapt_drv3_024_climax_to_apathy_spread_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    mx = v.rolling(63).max()
    score = (mx - v) / (mx + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vapt_drv3_025_vol_apathy_composite_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vapt_075_vol_apathy_final_composite(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V31_A_REGISTRY = {
    "vapt_drv3_001_vol_apathy_ratio_21d_jerk": {"inputs": ["close"], "func": vapt_drv3_001_vol_apathy_ratio_21d_jerk},
    "vapt_drv3_002_consecutive_low_vol_jerk": {"inputs": ["close"], "func": vapt_drv3_002_consecutive_low_vol_jerk},
    "vapt_drv3_003_vol_starvation_jerk": {"inputs": ["close"], "func": vapt_drv3_003_vol_starvation_jerk},
    "vapt_drv3_004_vol_adjusted_dryup_jerk": {"inputs": ["close", "volume"], "func": vapt_drv3_004_vol_adjusted_dryup_jerk},
    "vapt_drv3_005_dollar_volume_dryup_jerk": {"inputs": ["close", "volume"], "func": vapt_drv3_005_dollar_volume_dryup_jerk},
    "vapt_drv3_006_turnover_dryup_jerk": {"inputs": ["volume", "sharesbas"], "func": vapt_drv3_006_turnover_dryup_jerk},
    "vapt_drv3_007_vol_apathy_jerk": {"inputs": ["close", "volume"], "func": vapt_drv3_007_vol_apathy_jerk},
    "vapt_drv3_008_vol_void_jerk": {"inputs": ["close"], "func": vapt_drv3_008_vol_void_jerk},
    "vapt_drv3_009_climax_to_apathy_ratio_jerk": {"inputs": ["close"], "func": vapt_drv3_009_climax_to_apathy_ratio_jerk},
    "vapt_drv3_010_vol_apathy_entropy_jerk": {"inputs": ["close"], "func": vapt_drv3_010_vol_apathy_entropy_jerk},
    "vapt_drv3_011_vol_floor_proximity_jerk": {"inputs": ["close"], "func": vapt_drv3_011_vol_floor_proximity_jerk},
    "vapt_drv3_012_vol_exhaustion_prob_jerk": {"inputs": ["close"], "func": vapt_drv3_012_vol_exhaustion_prob_jerk},
    "vapt_drv3_013_terminal_washout_jerk": {"inputs": ["close", "volume"], "func": vapt_drv3_013_terminal_washout_jerk},
    "vapt_drv3_014_mktcap_vol_starvation_jerk": {"inputs": ["close", "sharesbas"], "func": vapt_drv3_014_mktcap_vol_starvation_jerk},
    "vapt_drv3_015_vol_apathy_final_exhaustion_jerk": {"inputs": ["close", "volume"], "func": vapt_drv3_015_vol_apathy_final_exhaustion_jerk},
    "vapt_drv3_016_consecutive_vol_decline_jerk": {"inputs": ["close"], "func": vapt_drv3_016_consecutive_vol_decline_jerk},
    "vapt_drv3_017_vol_apathy_zscore_persistence_jerk": {"inputs": ["close"], "func": vapt_drv3_017_vol_apathy_zscore_persistence_jerk},
    "vapt_drv3_018_vol_apathy_rank_jerk": {"inputs": ["close"], "func": vapt_drv3_018_vol_apathy_rank_jerk},
    "vapt_drv3_019_vol_apathy_at_earnings_jerk": {"inputs": ["close", "surprise"], "func": vapt_drv3_019_vol_apathy_at_earnings_jerk},
    "vapt_drv3_020_vol_apathy_to_range_jerk": {"inputs": ["high", "low", "close"], "func": vapt_drv3_020_vol_apathy_to_range_jerk},
    "vapt_drv3_021_days_under_vol_floor_jerk": {"inputs": ["close"], "func": vapt_drv3_021_days_under_vol_floor_jerk},
    "vapt_drv3_022_vol_apathy_zscore_ath_jerk": {"inputs": ["close"], "func": vapt_drv3_022_vol_apathy_zscore_ath_jerk},
    "vapt_drv3_023_ratio_days_vol_low_rank_jerk": {"inputs": ["close"], "func": vapt_drv3_023_ratio_days_vol_low_rank_jerk},
    "vapt_drv3_024_climax_to_apathy_spread_jerk": {"inputs": ["close"], "func": vapt_drv3_024_climax_to_apathy_spread_jerk},
    "vapt_drv3_025_vol_apathy_composite_jerk": {"inputs": ["close", "volume"], "func": vapt_drv3_025_vol_apathy_composite_jerk},
}
