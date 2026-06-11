"""
12_high_water_distance — 2nd Derivatives
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


def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(s == cummax).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of high water distance metrics
def hwd_drv2_001_pct_below_ath_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    p = _safe_div(close - h, h)
    return p.diff(5)


def hwd_drv2_002_days_since_ath_velocity(close: pd.Series) -> pd.Series:
    d = _days_since_expanding_high(close)
    return d.diff(5)


def hwd_drv2_003_ath_to_close_velocity(close: pd.Series) -> pd.Series:
    r = _safe_div(close.cummax(), close)
    return r.diff(5)


def hwd_drv2_004_ath_drawdown_velocity_accel(close: pd.Series) -> pd.Series:
    dist = (close.cummax() - close) / close.cummax()
    dur = _days_since_expanding_high(close)
    v = _safe_div(dist, dur)
    return v.diff(5)


def hwd_drv2_005_mktcap_pct_below_ath_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    p = _safe_div(mc - mc.cummax(), mc.cummax())
    return p.diff(5)


def hwd_drv2_006_secular_decay_velocity(close: pd.Series) -> pd.Series:
    dist = (close.cummax() - close) / close.cummax()
    dur = np.log(_days_since_expanding_high(close) + 2.0)
    idx = dist * dur
    return idx.diff(5)


def hwd_drv2_007_ath_drawdown_area_velocity(close: pd.Series) -> pd.Series:
    dist = (close.cummax() - close) / close.cummax()
    area = dist.expanding().sum()
    return area.diff(5)


def hwd_drv2_008_ath_renewal_gap_velocity(close: pd.Series) -> pd.Series:
    is_high = (close == close.cummax())
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_high).ffill()
    gap = indices.diff().rolling(252).mean()
    return gap.diff(5)


def hwd_drv2_009_ath_recovery_fraction_velocity(close: pd.Series) -> pd.Series:
    l = close.cummin()
    h = close.cummax()
    rf = _safe_div(close - l, h - l)
    return rf.diff(5)


def hwd_drv2_010_days_under_ath_norm_velocity(close: pd.Series) -> pd.Series:
    under = (close < close.cummax()).astype(int)
    dur = under.groupby((under == 0).cumsum()).cumsum()
    vol = close.pct_change().rolling(252).std() * np.sqrt(252)
    idx = _safe_div(dur, vol)
    return idx.diff(5)


def hwd_drv2_011_ath_to_200ma_velocity(close: pd.Series) -> pd.Series:
    r = _safe_div(close.cummax(), close.rolling(200).mean())
    return r.diff(5)


def hwd_drv2_012_ath_drawdown_persistence_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    per = (dd > 0.20).rolling(252).mean()
    return per.diff(5)


def hwd_drv2_013_days_since_ebitda_ath_velocity(ebitda: pd.Series) -> pd.Series:
    return _days_since_expanding_high(ebitda).diff(5)


def hwd_drv2_014_ath_drawdown_convexity_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    area = dd.expanding().sum()
    dur = _days_since_expanding_high(close)
    score = _safe_div(area, dur)
    return score.diff(5)


def hwd_drv2_015_ath_drawdown_energy_velocity(close: pd.Series) -> pd.Series:
    dist = (close.cummax() - close) / close.cummax()
    dur = _days_since_expanding_high(close)
    energy = (dist**2) * dur
    return energy.diff(5)


def hwd_drv2_016_ath_stale_years_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    is_big = (h > h.shift(1) * 1.05)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_big).ffill()
    stale = (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0
    return stale.diff(5)


def hwd_drv2_017_ath_proximity_oscillator_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    p = close / h
    osc = (p - p.rolling(252).min()) / (p.rolling(252).max() - p.rolling(252).min() + _EPS)
    return osc.diff(5)


def hwd_drv2_018_cumulative_ath_pain_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    pain = np.sqrt((dd**2).expanding().mean())
    return pain.diff(5)


def hwd_drv2_019_ath_exhaustion_composite_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dist = (h - close) / h
    dur = _days_since_expanding_high(close) / (252 * 10)
    v_dist = dist.rolling(63).std()
    score = 0.4 * dist + 0.4 * dur.clip(0,1) + 0.2 * v_dist
    return score.diff(5)


def hwd_drv2_020_ath_log_dist_velocity(close: pd.Series) -> pd.Series:
    return np.log(close / close.cummax()).diff(5)


def hwd_drv2_021_price_vs_rev_ath_div_velocity(close: pd.Series, revenue: pd.Series) -> pd.Series:
    p_rat = close / close.cummax()
    r_rat = revenue / revenue.cummax()
    div = p_rat - r_rat
    return div.diff(5)


def hwd_drv2_022_dist_to_ath_zscore_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dist = (h - close) / h
    z = (dist - dist.rolling(252).mean()) / dist.rolling(252).std()
    return z.diff(5)


def hwd_drv2_023_ath_renewal_freq_velocity(close: pd.Series) -> pd.Series:
    is_high = (close == close.cummax()).astype(int)
    freq = is_high.rolling(252).sum()
    return freq.diff(5)


def hwd_drv2_024_equity_ps_below_ath_velocity(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    bvps = _safe_div(equity, sharesbas)
    p = _safe_div(bvps - bvps.cummax(), bvps.cummax())
    return p.diff(1)


def hwd_drv2_025_ath_drawdown_log_decay_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h + 0.01
    def _decay(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), np.log(y)).slope
    dec = dd.rolling(63).apply(_decay, raw=True)
    return dec.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V12_V_REGISTRY = {
    "hwd_drv2_001_pct_below_ath_velocity": {"inputs": ["close"], "func": hwd_drv2_001_pct_below_ath_velocity},
    "hwd_drv2_002_days_since_ath_velocity": {"inputs": ["close"], "func": hwd_drv2_002_days_since_ath_velocity},
    "hwd_drv2_003_ath_to_close_velocity": {"inputs": ["close"], "func": hwd_drv2_003_ath_to_close_velocity},
    "hwd_drv2_004_ath_drawdown_velocity_accel": {"inputs": ["close"], "func": hwd_drv2_004_ath_drawdown_velocity_accel},
    "hwd_drv2_005_mktcap_pct_below_ath_velocity": {"inputs": ["close", "sharesbas"], "func": hwd_drv2_005_mktcap_pct_below_ath_velocity},
    "hwd_drv2_006_secular_decay_velocity": {"inputs": ["close"], "func": hwd_drv2_006_secular_decay_velocity},
    "hwd_drv2_007_ath_drawdown_area_velocity": {"inputs": ["close"], "func": hwd_drv2_007_ath_drawdown_area_velocity},
    "hwd_drv2_008_ath_renewal_gap_velocity": {"inputs": ["close"], "func": hwd_drv2_008_ath_renewal_gap_velocity},
    "hwd_drv2_009_ath_recovery_fraction_velocity": {"inputs": ["close"], "func": hwd_drv2_009_ath_recovery_fraction_velocity},
    "hwd_drv2_010_days_under_ath_norm_velocity": {"inputs": ["close"], "func": hwd_drv2_010_days_under_ath_norm_velocity},
    "hwd_drv2_011_ath_to_200ma_velocity": {"inputs": ["close"], "func": hwd_drv2_011_ath_to_200ma_velocity},
    "hwd_drv2_012_ath_drawdown_persistence_velocity": {"inputs": ["close"], "func": hwd_drv2_012_ath_drawdown_persistence_velocity},
    "hwd_drv2_013_days_since_ebitda_ath_velocity": {"inputs": ["ebitda"], "func": hwd_drv2_013_days_since_ebitda_ath_velocity},
    "hwd_drv2_014_ath_drawdown_convexity_velocity": {"inputs": ["close"], "func": hwd_drv2_014_ath_drawdown_convexity_velocity},
    "hwd_drv2_015_ath_drawdown_energy_velocity": {"inputs": ["close"], "func": hwd_drv2_015_ath_drawdown_energy_velocity},
    "hwd_drv2_016_ath_stale_years_velocity": {"inputs": ["close"], "func": hwd_drv2_016_ath_stale_years_velocity},
    "hwd_drv2_017_ath_proximity_oscillator_velocity": {"inputs": ["close"], "func": hwd_drv2_017_ath_proximity_oscillator_velocity},
    "hwd_drv2_018_cumulative_ath_pain_velocity": {"inputs": ["close"], "func": hwd_drv2_018_cumulative_ath_pain_velocity},
    "hwd_drv2_019_ath_exhaustion_composite_velocity": {"inputs": ["close"], "func": hwd_drv2_019_ath_exhaustion_composite_velocity},
    "hwd_drv2_020_ath_log_dist_velocity": {"inputs": ["close"], "func": hwd_drv2_020_ath_log_dist_velocity},
    "hwd_drv2_021_price_vs_rev_ath_div_velocity": {"inputs": ["close", "revenue"], "func": hwd_drv2_021_price_vs_rev_ath_div_velocity},
    "hwd_drv2_022_dist_to_ath_zscore_velocity": {"inputs": ["close"], "func": hwd_drv2_022_dist_to_ath_zscore_velocity},
    "hwd_drv2_023_ath_renewal_freq_velocity": {"inputs": ["close"], "func": hwd_drv2_023_ath_renewal_freq_velocity},
    "hwd_drv2_024_equity_ps_below_ath_velocity": {"inputs": ["equity", "sharesbas"], "func": hwd_drv2_024_equity_ps_below_ath_velocity},
    "hwd_drv2_025_ath_drawdown_log_decay_velocity": {"inputs": ["close"], "func": hwd_drv2_025_ath_drawdown_log_decay_velocity},
}
