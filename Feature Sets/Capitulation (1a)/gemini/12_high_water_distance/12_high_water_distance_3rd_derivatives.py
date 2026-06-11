"""
12_high_water_distance — 3rd Derivatives
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


def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(s == cummax).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing exhaustion/inflection of high water distance acceleration (jerk)
def hwd_drv3_001_pct_below_ath_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    p = _safe_div(close - h, h)
    vel = p.diff(5)
    return vel.diff(5)


def hwd_drv3_002_days_since_ath_jerk(close: pd.Series) -> pd.Series:
    d = _days_since_expanding_high(close)
    vel = d.diff(5)
    return vel.diff(5)


def hwd_drv3_003_ath_to_close_jerk(close: pd.Series) -> pd.Series:
    r = _safe_div(close.cummax(), close)
    vel = r.diff(5)
    return vel.diff(5)


def hwd_drv3_004_ath_drawdown_velocity_jerk(close: pd.Series) -> pd.Series:
    dist = (close.cummax() - close) / close.cummax()
    dur = _days_since_expanding_high(close)
    v = _safe_div(dist, dur)
    vel = v.diff(5)
    return vel.diff(5)


def hwd_drv3_005_mktcap_pct_below_ath_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    p = _safe_div(mc - mc.cummax(), mc.cummax())
    vel = p.diff(5)
    return vel.diff(5)


def hwd_drv3_006_secular_decay_jerk(close: pd.Series) -> pd.Series:
    dist = (close.cummax() - close) / close.cummax()
    dur = np.log(_days_since_expanding_high(close) + 2.0)
    idx = dist * dur
    vel = idx.diff(5)
    return vel.diff(5)


def hwd_drv3_007_ath_drawdown_area_jerk(close: pd.Series) -> pd.Series:
    dist = (close.cummax() - close) / close.cummax()
    area = dist.expanding().sum()
    vel = area.diff(5)
    return vel.diff(5)


def hwd_drv3_008_ath_renewal_gap_jerk(close: pd.Series) -> pd.Series:
    is_high = (close == close.cummax())
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_high).ffill()
    gap = indices.diff().rolling(252).mean()
    vel = gap.diff(5)
    return vel.diff(5)


def hwd_drv3_009_ath_recovery_fraction_jerk(close: pd.Series) -> pd.Series:
    l = close.cummin()
    h = close.cummax()
    rf = _safe_div(close - l, h - l)
    vel = rf.diff(5)
    return vel.diff(5)


def hwd_drv3_010_days_under_ath_norm_jerk(close: pd.Series) -> pd.Series:
    under = (close < close.cummax()).astype(int)
    dur = under.groupby((under == 0).cumsum()).cumsum()
    vol = close.pct_change().rolling(252).std() * np.sqrt(252)
    idx = _safe_div(dur, vol)
    vel = idx.diff(5)
    return vel.diff(5)


def hwd_drv3_011_ath_to_200ma_jerk(close: pd.Series) -> pd.Series:
    r = _safe_div(close.cummax(), close.rolling(200).mean())
    vel = r.diff(5)
    return vel.diff(5)


def hwd_drv3_012_ath_drawdown_persistence_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    per = (dd > 0.20).rolling(252).mean()
    vel = per.diff(5)
    return vel.diff(5)


def hwd_drv3_013_days_since_ebitda_ath_jerk(ebitda: pd.Series) -> pd.Series:
    vel = _days_since_expanding_high(ebitda).diff(5)
    return vel.diff(5)


def hwd_drv3_014_ath_drawdown_convexity_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    area = dd.expanding().sum()
    dur = _days_since_expanding_high(close)
    score = _safe_div(area, dur)
    vel = score.diff(5)
    return vel.diff(5)


def hwd_drv3_015_ath_drawdown_energy_jerk(close: pd.Series) -> pd.Series:
    dist = (close.cummax() - close) / close.cummax()
    dur = _days_since_expanding_high(close)
    energy = (dist**2) * dur
    vel = energy.diff(5)
    return vel.diff(5)


def hwd_drv3_016_ath_stale_years_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    is_big = (h > h.shift(1) * 1.05)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_big).ffill()
    stale = (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0
    vel = stale.diff(5)
    return vel.diff(5)


def hwd_drv3_017_ath_proximity_oscillator_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    p = close / h
    osc = (p - p.rolling(252).min()) / (p.rolling(252).max() - p.rolling(252).min() + _EPS)
    vel = osc.diff(5)
    return vel.diff(5)


def hwd_drv3_018_cumulative_ath_pain_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    pain = np.sqrt((dd**2).expanding().mean())
    vel = pain.diff(5)
    return vel.diff(5)


def hwd_drv3_019_ath_exhaustion_composite_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dist = (h - close) / h
    dur = _days_since_expanding_high(close) / (252 * 10)
    v_dist = dist.rolling(63).std()
    score = 0.4 * dist + 0.4 * dur.clip(0,1) + 0.2 * v_dist
    vel = score.diff(5)
    return vel.diff(5)


def hwd_drv3_020_ath_log_dist_jerk(close: pd.Series) -> pd.Series:
    vel = np.log(close / close.cummax()).diff(5)
    return vel.diff(5)


def hwd_drv3_021_price_vs_rev_ath_div_jerk(close: pd.Series, revenue: pd.Series) -> pd.Series:
    p_rat = close / close.cummax()
    r_rat = revenue / revenue.cummax()
    div = p_rat - r_rat
    vel = div.diff(5)
    return vel.diff(5)


def hwd_drv3_022_dist_to_ath_zscore_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dist = (h - close) / h
    z = (dist - dist.rolling(252).mean()) / dist.rolling(252).std()
    vel = z.diff(5)
    return vel.diff(5)


def hwd_drv3_023_ath_renewal_freq_jerk(close: pd.Series) -> pd.Series:
    is_high = (close == close.cummax()).astype(int)
    freq = is_high.rolling(252).sum()
    vel = freq.diff(5)
    return vel.diff(5)


def hwd_drv3_024_equity_ps_below_ath_jerk(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    bvps = _safe_div(equity, sharesbas)
    p = _safe_div(bvps - bvps.cummax(), bvps.cummax())
    vel = p.diff(1)
    return vel.diff(1)


def hwd_drv3_025_ath_drawdown_log_decay_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h + 0.01
    def _decay(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), np.log(y)).slope
    dec = dd.rolling(63).apply(_decay, raw=True)
    vel = dec.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V12_A_REGISTRY = {
    "hwd_drv3_001_pct_below_ath_jerk": {"inputs": ["close"], "func": hwd_drv3_001_pct_below_ath_jerk},
    "hwd_drv3_002_days_since_ath_jerk": {"inputs": ["close"], "func": hwd_drv3_002_days_since_ath_jerk},
    "hwd_drv3_003_ath_to_close_jerk": {"inputs": ["close"], "func": hwd_drv3_003_ath_to_close_jerk},
    "hwd_drv3_004_ath_drawdown_velocity_jerk": {"inputs": ["close"], "func": hwd_drv3_004_ath_drawdown_velocity_jerk},
    "hwd_drv3_005_mktcap_pct_below_ath_jerk": {"inputs": ["close", "sharesbas"], "func": hwd_drv3_005_mktcap_pct_below_ath_jerk},
    "hwd_drv3_006_secular_decay_jerk": {"inputs": ["close"], "func": hwd_drv3_006_secular_decay_jerk},
    "hwd_drv3_007_ath_drawdown_area_jerk": {"inputs": ["close"], "func": hwd_drv3_007_ath_drawdown_area_jerk},
    "hwd_drv3_008_ath_renewal_gap_jerk": {"inputs": ["close"], "func": hwd_drv3_008_ath_renewal_gap_jerk},
    "hwd_drv3_009_ath_recovery_fraction_jerk": {"inputs": ["close"], "func": hwd_drv3_009_ath_recovery_fraction_jerk},
    "hwd_drv3_010_days_under_ath_norm_jerk": {"inputs": ["close"], "func": hwd_drv3_010_days_under_ath_norm_jerk},
    "hwd_drv3_011_ath_to_200ma_jerk": {"inputs": ["close"], "func": hwd_drv3_011_ath_to_200ma_jerk},
    "hwd_drv3_012_ath_drawdown_persistence_jerk": {"inputs": ["close"], "func": hwd_drv3_012_ath_drawdown_persistence_jerk},
    "hwd_drv3_013_days_since_ebitda_ath_jerk": {"inputs": ["ebitda"], "func": hwd_drv3_013_days_since_ebitda_ath_jerk},
    "hwd_drv3_014_ath_drawdown_convexity_jerk": {"inputs": ["close"], "func": hwd_drv3_014_ath_drawdown_convexity_jerk},
    "hwd_drv3_015_ath_drawdown_energy_jerk": {"inputs": ["close"], "func": hwd_drv3_015_ath_drawdown_energy_jerk},
    "hwd_drv3_016_ath_stale_years_jerk": {"inputs": ["close"], "func": hwd_drv3_016_ath_stale_years_jerk},
    "hwd_drv3_017_ath_proximity_oscillator_jerk": {"inputs": ["close"], "func": hwd_drv3_017_ath_proximity_oscillator_jerk},
    "hwd_drv3_018_cumulative_ath_pain_jerk": {"inputs": ["close"], "func": hwd_drv3_018_cumulative_ath_pain_jerk},
    "hwd_drv3_019_ath_exhaustion_composite_jerk": {"inputs": ["close"], "func": hwd_drv3_019_ath_exhaustion_composite_jerk},
    "hwd_drv3_020_ath_log_dist_jerk": {"inputs": ["close"], "func": hwd_drv3_020_ath_log_dist_jerk},
    "hwd_drv3_021_price_vs_rev_ath_div_jerk": {"inputs": ["close", "revenue"], "func": hwd_drv3_021_price_vs_rev_ath_div_jerk},
    "hwd_drv3_022_dist_to_ath_zscore_jerk": {"inputs": ["close"], "func": hwd_drv3_022_dist_to_ath_zscore_jerk},
    "hwd_drv3_023_ath_renewal_freq_jerk": {"inputs": ["close"], "func": hwd_drv3_023_ath_renewal_freq_jerk},
    "hwd_drv3_024_equity_ps_below_ath_jerk": {"inputs": ["equity", "sharesbas"], "func": hwd_drv3_024_equity_ps_below_ath_jerk},
    "hwd_drv3_025_ath_drawdown_log_decay_jerk": {"inputs": ["close"], "func": hwd_drv3_025_ath_drawdown_log_decay_jerk},
}
