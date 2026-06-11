"""
25_realized_volatility — 3rd Derivatives
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


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing exhaustion/inflection of realized volatility acceleration (jerk)
def rvl_drv3_001_realized_vol_21d_jerk(close: pd.Series) -> pd.Series:
    # Rate of change of volatility velocity
    v = np.log(close / close.shift(1)).rolling(21).std() * np.sqrt(252)
    vel = v.diff(5)
    return vel.diff(5)


def rvl_drv3_002_parkinson_vol_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    v = np.sqrt((1 / (4 * np.log(2))) * (np.log(high / low)**2)).rolling(21).mean() * np.sqrt(252)
    vel = v.diff(5)
    return vel.diff(5)


def rvl_drv3_003_vol_zscore_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    z = (v - v.rolling(252).mean()) / (v.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def rvl_drv3_004_vol_expansion_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    ratio = _safe_div(v21, v21.rolling(252).mean())
    vel = ratio.diff(5)
    return vel.diff(5)


def rvl_drv3_005_volatility_climax_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(volume, volume.rolling(252).median())
    vel = (v * vs).diff(5)
    return vel.diff(5)


def rvl_drv3_006_vol_of_vol_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    vov = v.rolling(63).std()
    vel = vov.diff(5)
    return vel.diff(5)


def rvl_drv3_007_ud_vol_ratio_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    ratio = _safe_div(ret.where(ret < 0).rolling(63).std(), ret.where(ret > 0).rolling(63).std())
    vel = ratio.diff(5)
    return vel.diff(5)


def rvl_drv3_008_vol_persistence_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    per = (v21 > v21.rolling(252).mean()).rolling(63).mean()
    vel = per.diff(5)
    return vel.diff(5)


def rvl_drv3_009_vol_regime_shift_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    rsi = np.log(_safe_div(v21, v252) + _EPS)
    vel = rsi.diff(5)
    return vel.diff(5)


def rvl_drv3_010_intraday_vol_jerk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = ((high - low) / (close + _EPS)).rolling(21).mean()
    vel = v.diff(5)
    return vel.diff(5)


def rvl_drv3_011_gap_volatility_jerk(close: pd.Series, open: pd.Series) -> pd.Series:
    v = ((open - close.shift(1)) / (close.shift(1) + _EPS)).rolling(63).std()
    vel = v.diff(5)
    return vel.diff(5)


def rvl_drv3_012_vol_energy_density_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    ed = (v**2) * v_rat
    vel = ed.diff(5)
    return vel.diff(5)


def rvl_drv3_013_vol_at_unit_turnover_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    to = _safe_div(volume, sharesbas).rolling(21).mean()
    ratio = _safe_div(v, to)
    vel = ratio.diff(5)
    return vel.diff(5)


def rvl_drv3_014_vol_weighted_dd_climax_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    h = close.rolling(252).max()
    dd = (h - close) / (h + _EPS)
    vel = (v * dd).diff(5)
    return vel.diff(5)


def rvl_drv3_015_vol_drift_stability_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v.rolling(63).apply(_rsq, raw=True)
    vel = rs.diff(5)
    return vel.diff(5)


def rvl_drv3_016_vol_momentum_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    roc = v.diff(21)
    z = (roc - roc.rolling(63).mean()) / (roc.rolling(63).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def rvl_drv3_017_final_fear_index_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = rvl_150_final_fear_index(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def rvl_drv3_018_vol_entropy_jerk(close: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = close.pct_change().rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)


def rvl_drv3_019_mktcap_vol_expansion_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v = np.log(mc / mc.shift(1)).rolling(21).std()
    z = (v - v.rolling(252).mean()) / (v.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def rvl_drv3_020_vol_per_unit_dd_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    dd = (close.rolling(252).max() - close) / (close.rolling(252).max() + _EPS)
    ratio = _safe_div(v, dd + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)


def rvl_drv3_021_consecutive_vol_expansion_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    inc = (v > v.shift(1)).astype(int)
    dur = inc.groupby((inc == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def rvl_drv3_022_vol_pct_rank_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    rank = v.expanding().rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def rvl_drv3_023_atr_to_price_jerk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr_p = _safe_div(tr.rolling(21).mean(), close)
    vel = atr_p.diff(5)
    return vel.diff(5)


def rvl_drv3_024_vol_shock_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    vol = ret.rolling(21).std()
    idx = _safe_div(ret.rolling(21).max(), vol)
    vel = idx.diff(5)
    return vel.diff(5)


def rvl_drv3_025_mktcap_vol_regime_shift_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    v252 = np.log(mc / mc.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    vel = ratio.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V25_A_REGISTRY = {
    "rvl_drv3_001_realized_vol_21d_jerk": {"inputs": ["close"], "func": rvl_drv3_001_realized_vol_21d_jerk},
    "rvl_drv3_002_parkinson_vol_jerk": {"inputs": ["high", "low"], "func": rvl_drv3_002_parkinson_vol_jerk},
    "rvl_drv3_003_vol_zscore_jerk": {"inputs": ["close"], "func": rvl_drv3_003_vol_zscore_jerk},
    "rvl_drv3_004_vol_expansion_jerk": {"inputs": ["close"], "func": rvl_drv3_004_vol_expansion_jerk},
    "rvl_drv3_005_volatility_climax_jerk": {"inputs": ["close", "volume"], "func": rvl_drv3_005_volatility_climax_jerk},
    "rvl_drv3_006_vol_of_vol_jerk": {"inputs": ["close"], "func": rvl_drv3_006_vol_of_vol_jerk},
    "rvl_drv3_007_ud_vol_ratio_jerk": {"inputs": ["close"], "func": rvl_drv3_007_ud_vol_ratio_jerk},
    "rvl_drv3_008_vol_persistence_jerk": {"inputs": ["close"], "func": rvl_drv3_008_vol_persistence_jerk},
    "rvl_drv3_009_vol_regime_shift_jerk": {"inputs": ["close"], "func": rvl_drv3_009_vol_regime_shift_jerk},
    "rvl_drv3_010_intraday_vol_jerk": {"inputs": ["high", "low", "close"], "func": rvl_drv3_010_intraday_vol_jerk},
    "rvl_drv3_011_gap_volatility_jerk": {"inputs": ["close", "open"], "func": rvl_drv3_011_gap_volatility_jerk},
    "rvl_drv3_012_vol_energy_density_jerk": {"inputs": ["close", "volume"], "func": rvl_drv3_012_vol_energy_density_jerk},
    "rvl_drv3_013_vol_at_unit_turnover_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": rvl_drv3_013_vol_at_unit_turnover_jerk},
    "rvl_drv3_014_vol_weighted_dd_climax_jerk": {"inputs": ["close"], "func": rvl_drv3_014_vol_weighted_dd_climax_jerk},
    "rvl_drv3_015_vol_drift_stability_jerk": {"inputs": ["close"], "func": rvl_drv3_015_vol_drift_stability_jerk},
    "rvl_drv3_016_vol_momentum_jerk": {"inputs": ["close"], "func": rvl_drv3_016_vol_momentum_jerk},
    "rvl_drv3_017_final_fear_index_jerk": {"inputs": ["close", "volume"], "func": rvl_drv3_017_final_fear_index_jerk},
    "rvl_drv3_018_vol_entropy_jerk": {"inputs": ["close"], "func": rvl_drv3_018_vol_entropy_jerk},
    "rvl_drv3_019_mktcap_vol_expansion_jerk": {"inputs": ["close", "sharesbas"], "func": rvl_drv3_019_mktcap_vol_expansion_jerk},
    "rvl_drv3_020_vol_per_unit_dd_jerk": {"inputs": ["close"], "func": rvl_drv3_020_vol_per_unit_dd_jerk},
    "rvl_drv3_021_consecutive_vol_expansion_jerk": {"inputs": ["close"], "func": rvl_drv3_021_consecutive_vol_expansion_jerk},
    "rvl_drv3_022_vol_pct_rank_jerk": {"inputs": ["close"], "func": rvl_drv3_022_vol_pct_rank_jerk},
    "rvl_drv3_023_atr_to_price_jerk": {"inputs": ["high", "low", "close"], "func": rvl_drv3_023_atr_to_price_jerk},
    "rvl_drv3_024_vol_shock_jerk": {"inputs": ["close"], "func": rvl_drv3_024_vol_shock_jerk},
    "rvl_drv3_025_mktcap_vol_regime_shift_jerk": {"inputs": ["close", "sharesbas"], "func": rvl_drv3_025_mktcap_vol_regime_shift_jerk},
}
