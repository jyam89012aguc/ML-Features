"""
25_realized_volatility — 2nd Derivatives
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


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of realized volatility metrics
def rvl_drv2_001_realized_vol_21d_velocity(close: pd.Series) -> pd.Series:
    # Change in 21-day realized volatility
    v = np.log(close / close.shift(1)).rolling(21).std() * np.sqrt(252)
    return v.diff(5)


def rvl_drv2_002_parkinson_vol_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    v = np.sqrt((1 / (4 * np.log(2))) * (np.log(high / low)**2)).rolling(21).mean() * np.sqrt(252)
    return v.diff(5)


def rvl_drv2_003_vol_zscore_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    z = (v - v.rolling(252).mean()) / v.rolling(252).std()
    return z.diff(5)


def rvl_drv2_004_vol_expansion_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    ratio = _safe_div(v21, v21.rolling(252).mean())
    return ratio.diff(5)


def rvl_drv2_005_volatility_climax_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    vs = _safe_div(volume, volume.rolling(252).median())
    return (v * vs).diff(5)


def rvl_drv2_006_vol_of_vol_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    vov = v.rolling(63).std()
    return vov.diff(5)


def rvl_drv2_007_ud_vol_ratio_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    ratio = _safe_div(ret.where(ret < 0).rolling(63).std(), ret.where(ret > 0).rolling(63).std())
    return ratio.diff(5)


def rvl_drv2_008_vol_persistence_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    per = (v21 > v21.rolling(252).mean()).rolling(63).mean()
    return per.diff(5)


def rvl_drv2_009_vol_regime_shift_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    rsi = np.log(_safe_div(v21, v252) + _EPS)
    return rsi.diff(5)


def rvl_drv2_010_intraday_vol_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = ((high - low) / close).rolling(21).mean()
    return v.diff(5)


def rvl_drv2_011_gap_volatility_velocity(close: pd.Series, open: pd.Series) -> pd.Series:
    v = ((open - close.shift(1)) / close.shift(1)).rolling(63).std()
    return v.diff(5)


def rvl_drv2_012_vol_energy_density_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    ed = (v**2) * v_rat
    return ed.diff(5)


def rvl_drv2_013_vol_at_unit_turnover_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    to = _safe_div(volume, sharesbas).rolling(21).mean()
    ratio = _safe_div(v, to)
    return ratio.diff(5)


def rvl_drv2_014_vol_weighted_dd_climax_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    h = close.rolling(252).max()
    dd = (h - close) / h
    return (v * dd).diff(5)


def rvl_drv2_015_vol_drift_stability_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v.rolling(63).apply(_rsq, raw=True)
    return rs.diff(5)


def rvl_drv2_016_vol_momentum_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    roc = v.diff(21)
    z = (roc - roc.rolling(63).mean()) / (roc.rolling(63).std() + _EPS)
    return z.diff(5)


def rvl_drv2_017_final_fear_index_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = rvl_150_final_fear_index(close, volume)
    return score.diff(5)


def rvl_drv2_018_vol_entropy_velocity(close: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = close.pct_change().rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def rvl_drv2_019_mktcap_vol_expansion_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v = np.log(mc / mc.shift(1)).rolling(21).std()
    z = (v - v.rolling(252).mean()) / (v.rolling(252).std() + _EPS)
    return z.diff(5)


def rvl_drv2_020_vol_per_unit_dd_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    dd = (close.rolling(252).max() - close) / close.rolling(252).max()
    ratio = _safe_div(v, dd + _EPS)
    return ratio.diff(5)


def rvl_drv2_021_consecutive_vol_expansion_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    inc = (v > v.shift(1)).astype(int)
    dur = inc.groupby((inc == 0).cumsum()).cumsum()
    return dur.diff(5)


def rvl_drv2_022_vol_pct_rank_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    rank = v.expanding().rank(pct=True)
    return rank.diff(5)


def rvl_drv2_023_atr_to_price_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr_p = _safe_div(tr.rolling(21).mean(), close)
    return atr_p.diff(5)


def rvl_drv2_024_vol_shock_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    vol = ret.rolling(21).std()
    idx = _safe_div(ret.rolling(21).max(), vol)
    return idx.diff(5)


def rvl_drv2_025_mktcap_vol_regime_shift_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    v252 = np.log(mc / mc.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    return ratio.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V25_V_REGISTRY = {
    "rvl_drv2_001_realized_vol_21d_velocity": {"inputs": ["close"], "func": rvl_drv2_001_realized_vol_21d_velocity},
    "rvl_drv2_002_parkinson_vol_velocity": {"inputs": ["high", "low"], "func": rvl_drv2_002_parkinson_vol_velocity},
    "rvl_drv2_003_vol_zscore_velocity": {"inputs": ["close"], "func": rvl_drv2_003_vol_zscore_velocity},
    "rvl_drv2_004_vol_expansion_velocity": {"inputs": ["close"], "func": rvl_drv2_004_vol_expansion_velocity},
    "rvl_drv2_005_volatility_climax_velocity": {"inputs": ["close", "volume"], "func": rvl_drv2_005_volatility_climax_velocity},
    "rvl_drv2_006_vol_of_vol_velocity": {"inputs": ["close"], "func": rvl_drv2_006_vol_of_vol_velocity},
    "rvl_drv2_007_ud_vol_ratio_velocity": {"inputs": ["close"], "func": rvl_drv2_007_ud_vol_ratio_velocity},
    "rvl_drv2_008_vol_persistence_velocity": {"inputs": ["close"], "func": rvl_drv2_008_vol_persistence_velocity},
    "rvl_drv2_009_vol_regime_shift_velocity": {"inputs": ["close"], "func": rvl_drv2_009_vol_regime_shift_velocity},
    "rvl_drv2_010_intraday_vol_velocity": {"inputs": ["high", "low", "close"], "func": rvl_drv2_010_intraday_vol_velocity},
    "rvl_drv2_011_gap_volatility_velocity": {"inputs": ["close", "open"], "func": rvl_drv2_011_gap_volatility_velocity},
    "rvl_drv2_012_vol_energy_density_velocity": {"inputs": ["close", "volume"], "func": rvl_drv2_012_vol_energy_density_velocity},
    "rvl_drv2_013_vol_at_unit_turnover_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": rvl_drv2_013_vol_at_unit_turnover_velocity},
    "rvl_drv2_014_vol_weighted_dd_climax_velocity": {"inputs": ["close"], "func": rvl_drv2_014_vol_weighted_dd_climax_velocity},
    "rvl_drv2_015_vol_drift_stability_velocity": {"inputs": ["close"], "func": rvl_drv2_015_vol_drift_stability_velocity},
    "rvl_drv2_016_vol_momentum_velocity": {"inputs": ["close"], "func": rvl_drv2_016_vol_momentum_velocity},
    "rvl_drv2_017_final_fear_index_velocity": {"inputs": ["close", "volume"], "func": rvl_drv2_017_final_fear_index_velocity},
    "rvl_drv2_018_vol_entropy_velocity": {"inputs": ["close"], "func": rvl_drv2_018_vol_entropy_velocity},
    "rvl_drv2_019_mktcap_vol_expansion_velocity": {"inputs": ["close", "sharesbas"], "func": rvl_drv2_019_mktcap_vol_expansion_velocity},
    "rvl_drv2_020_vol_per_unit_dd_velocity": {"inputs": ["close"], "func": rvl_drv2_020_vol_per_unit_dd_velocity},
    "rvl_drv2_021_consecutive_vol_expansion_velocity": {"inputs": ["close"], "func": rvl_drv2_021_consecutive_vol_expansion_velocity},
    "rvl_drv2_022_vol_pct_rank_velocity": {"inputs": ["close"], "func": rvl_drv2_022_vol_pct_rank_velocity},
    "rvl_drv2_023_atr_to_price_velocity": {"inputs": ["high", "low", "close"], "func": rvl_drv2_023_atr_to_price_velocity},
    "rvl_drv2_024_vol_shock_velocity": {"inputs": ["close"], "func": rvl_drv2_024_vol_shock_velocity},
    "rvl_drv2_025_mktcap_vol_regime_shift_velocity": {"inputs": ["close", "sharesbas"], "func": rvl_drv2_025_mktcap_vol_regime_shift_velocity},
}
