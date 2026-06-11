"""
31_volatility_apathy — 2nd Derivatives
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of volatility apathy metrics
def vapt_drv2_001_vol_apathy_ratio_21d_velocity(close: pd.Series) -> pd.Series:
    # Change in vol apathy intensity
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    med_v = v21.rolling(252).median()
    ratio = _safe_div(v21, med_v)
    return ratio.diff(5)


def vapt_drv2_002_consecutive_low_vol_velocity(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    med_v = v5.rolling(252).median()
    below = (v5 < med_v).astype(int)
    dur = below.groupby((below == 0).cumsum()).cumsum()
    return dur.diff(5)


def vapt_drv2_003_vol_starvation_velocity(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    q10 = v5.rolling(252).quantile(0.1)
    st = (v5 < q10).rolling(63).mean()
    return st.diff(5)


def vapt_drv2_004_vol_apathy_zscore_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    z = (v21 - v21.rolling(252).mean()) / (v21.rolling(252).std() + _EPS)
    return z.diff(5)


def vapt_drv2_005_vol_floor_proximity_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    l_v = v21.rolling(252).min()
    prox = _safe_div(v21, l_v)
    return prox.diff(5)


def vapt_drv2_006_sentiment_exhaustion_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    l = close.rolling(252).min()
    h = close.rolling(252).max()
    rf = _safe_div(close - l, h - l)
    score = _safe_div(1.0, v21 * v_rat * rf + _EPS)
    return score.diff(5)


def vapt_drv2_007_vol_void_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    med = v.rolling(252).median()
    void = (med - v).clip(lower=0).rolling(63).sum() / (v.rolling(252).mean() + _EPS)
    return void.diff(5)


def vapt_drv2_008_climax_to_apathy_ratio_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    mx = v.rolling(63).max()
    rat = _safe_div(mx, v)
    return rat.diff(5)


def vapt_drv2_009_vol_apathy_entropy_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = v.rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def vapt_drv2_010_mktcap_vol_apathy_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    rat = _safe_div(v21, v21.rolling(252).median())
    return rat.diff(5)


def vapt_drv2_011_terminal_washout_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).median())
    vol_rat = _safe_div(volume, volume.rolling(252).median())
    p_vel = np.log(close).diff(5).abs()
    score = _safe_div(1.0, v_rat * vol_rat * p_vel + _EPS)
    return score.diff(5)


def vapt_drv2_012_vol_apathy_momentum_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    roc = v.pct_change(21)
    return roc.diff(5)


def vapt_drv2_013_vol_exhaustion_prob_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    med = v21.rolling(252).median()
    is_low = (v21 < med)
    prob = (is_low & is_low.shift(1)).rolling(63).sum() / (is_low.shift(1).rolling(63).sum() + _EPS)
    return prob.diff(5)


def vapt_drv2_014_vol_apathy_to_range_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_rat = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).median())
    r = (high - low) / close
    r_rat = _safe_div(r, r.rolling(252).median())
    score = _safe_div(1.0, v_rat * r_rat + _EPS)
    return score.diff(5)


def vapt_drv2_015_vol_apathy_final_exhaustion_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vapt_150_vol_apathy_final_exhaustion_score(close, volume)
    return score.diff(5)


def vapt_drv2_016_consecutive_vol_decline_velocity(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    is_dec = (v5 < v5.shift(1)).astype(int)
    dur = is_dec.groupby((is_dec == 0).cumsum()).cumsum()
    return dur.diff(5)


def vapt_drv2_017_vol_apathy_zscore_persistence_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    z = (v21 - v21.rolling(252).mean()) / (v21.rolling(252).std() + _EPS)
    per = z.rolling(63).mean()
    return per.diff(5)


def vapt_drv2_018_vol_apathy_rank_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    rank = v21.rolling(252).rank(pct=True)
    return rank.diff(5)


def vapt_drv2_019_vol_apathy_at_earnings_velocity(close: pd.Series, surprise: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    ratio = _safe_div(v21, v21.rolling(252).median())
    val = ratio.where(surprise.abs() > 0).ffill()
    return val.diff(5)


def vapt_drv2_020_climax_to_apathy_spread_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    mx = v.rolling(63).max()
    score = (mx - v) / (mx + _EPS)
    return score.diff(5)


def vapt_drv2_021_days_under_vol_floor_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg = v21.expanding().mean()
    idx = pd.Series(np.arange(len(close)), index=close.index).where(v21 > avg).ffill()
    dur = pd.Series(np.arange(len(close)), index=close.index) - idx
    return dur.diff(5)


def vapt_drv2_022_vol_apathy_zscore_ath_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    inv_v = 1.0 / (v21 + _EPS)
    z = (inv_v - inv_v.expanding().mean()) / (inv_v.expanding().std() + _EPS)
    return z.diff(5)


def vapt_drv2_023_ratio_days_vol_low_rank_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    rank = v21.rolling(252).rank(pct=True)
    ratio = (rank < 0.10).rolling(252).mean()
    return ratio.diff(5)


def vapt_drv2_024_vol_apathy_at_ath_low_velocity(close: pd.Series) -> pd.Series:
    l = close.cummin()
    is_low = (close == l)
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    val = _safe_div(v21, v21.rolling(252).median())
    return val.where(is_low).ffill().diff(5)


def vapt_drv2_025_vol_apathy_composite_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vapt_075_vol_apathy_final_composite(close, volume)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V31_V_REGISTRY = {
    "vapt_drv2_001_vol_apathy_ratio_21d_velocity": {"inputs": ["close"], "func": vapt_drv2_001_vol_apathy_ratio_21d_velocity},
    "vapt_drv2_002_consecutive_low_vol_velocity": {"inputs": ["close"], "func": vapt_drv2_002_consecutive_low_vol_velocity},
    "vapt_drv2_003_vol_starvation_velocity": {"inputs": ["close"], "func": vapt_drv2_003_vol_starvation_velocity},
    "vapt_drv2_004_vol_apathy_zscore_velocity": {"inputs": ["close"], "func": vapt_drv2_004_vol_apathy_zscore_velocity},
    "vapt_drv2_005_vol_floor_proximity_velocity": {"inputs": ["close"], "func": vapt_drv2_005_vol_floor_proximity_velocity},
    "vapt_drv2_006_sentiment_exhaustion_velocity": {"inputs": ["close", "volume"], "func": vapt_drv2_006_sentiment_exhaustion_velocity},
    "vapt_drv2_007_vol_void_velocity": {"inputs": ["close"], "func": vapt_drv2_007_vol_void_velocity},
    "vapt_drv2_008_climax_to_apathy_ratio_velocity": {"inputs": ["close"], "func": vapt_drv2_008_climax_to_apathy_ratio_velocity},
    "vapt_drv2_009_vol_apathy_entropy_velocity": {"inputs": ["close"], "func": vapt_drv2_009_vol_apathy_entropy_velocity},
    "vapt_drv2_010_mktcap_vol_apathy_velocity": {"inputs": ["close", "sharesbas"], "func": vapt_drv2_010_mktcap_vol_apathy_velocity},
    "vapt_drv2_011_terminal_washout_velocity": {"inputs": ["close", "volume"], "func": vapt_drv2_011_terminal_washout_velocity},
    "vapt_drv2_012_vol_apathy_momentum_velocity": {"inputs": ["close"], "func": vapt_drv2_012_vol_apathy_momentum_velocity},
    "vapt_drv2_013_vol_exhaustion_prob_velocity": {"inputs": ["close"], "func": vapt_drv2_013_vol_exhaustion_prob_velocity},
    "vapt_drv2_014_vol_apathy_to_range_velocity": {"inputs": ["high", "low", "close"], "func": vapt_drv2_014_vol_apathy_to_range_velocity},
    "vapt_drv2_015_vol_apathy_final_exhaustion_velocity": {"inputs": ["close", "volume"], "func": vapt_drv2_015_vol_apathy_final_exhaustion_velocity},
    "vapt_drv2_016_consecutive_vol_decline_velocity": {"inputs": ["close"], "func": vapt_drv2_016_consecutive_vol_decline_velocity},
    "vapt_drv2_017_vol_apathy_zscore_persistence_velocity": {"inputs": ["close"], "func": vapt_drv2_017_vol_apathy_zscore_persistence_velocity},
    "vapt_drv2_018_vol_apathy_rank_velocity": {"inputs": ["close"], "func": vapt_drv2_018_vol_apathy_rank_velocity},
    "vapt_drv2_019_vol_apathy_at_earnings_velocity": {"inputs": ["close", "surprise"], "func": vapt_drv2_019_vol_apathy_at_earnings_velocity},
    "vapt_drv2_020_climax_to_apathy_spread_velocity": {"inputs": ["close"], "func": vapt_drv2_020_climax_to_apathy_spread_velocity},
    "vapt_drv2_021_days_under_vol_floor_velocity": {"inputs": ["close"], "func": vapt_drv2_021_days_under_vol_floor_velocity},
    "vapt_drv2_022_vol_apathy_zscore_ath_velocity": {"inputs": ["close"], "func": vapt_drv2_022_vol_apathy_zscore_ath_velocity},
    "vapt_drv2_023_ratio_days_vol_low_rank_velocity": {"inputs": ["close"], "func": vapt_drv2_023_ratio_days_vol_low_rank_velocity},
    "vapt_drv2_024_vol_apathy_at_ath_low_velocity": {"inputs": ["close"], "func": vapt_drv2_024_vol_apathy_at_ath_low_velocity},
    "vapt_drv2_025_vol_apathy_composite_velocity": {"inputs": ["close", "volume"], "func": vapt_drv2_025_vol_apathy_composite_velocity},
}
