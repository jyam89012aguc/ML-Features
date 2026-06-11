"""
12_high_water_distance — Base Features 076–150
Domain: distance/time from prior all-time high
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(s == cummax).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Secular Momentum relative to High Water Marks
def hwd_076_ath_to_200ma_ratio(close: pd.Series) -> pd.Series:
    ath = close.cummax()
    ma = close.rolling(200).mean()
    return _safe_div(ath, ma)


def hwd_077_ath_drawdown_persistence_252d(close: pd.Series) -> pd.Series:
    # Fraction of last year spent in > 20% ATH drawdown
    h = close.cummax()
    dd = (h - close) / h
    return (dd > 0.20).rolling(252).mean()


def hwd_078_days_since_ath_zscore_ath(close: pd.Series) -> pd.Series:
    d = _days_since_expanding_high(close)
    return (d - d.expanding().mean()) / d.expanding().std()


# 091-105: Climax Signatures near ATH lows
def hwd_091_ath_recovery_velocity_21d(close: pd.Series) -> pd.Series:
    # Change in ATH-normalized price over last month
    h = close.cummax()
    p_norm = close / h
    return p_norm.diff(21)


def hwd_092_volume_at_ath_drawdown_peak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Volume on the day of the deepest ATH drawdown in the last 63 days
    h = close.cummax()
    dd = (h - close) / h
    max_dd_idx = dd.rolling(63).apply(np.argmax, raw=True)
    return volume.iloc[max_dd_idx.astype(int)]


# 106-125: Multiple Horizon High Water Comparisons
def hwd_106_dist_to_ath_vs_dist_to_5y_high(close: pd.Series) -> pd.Series:
    d_ath = close / close.cummax()
    d_5y = close / _rolling_max(close, 252 * 5)
    return d_ath - d_5y


def hwd_107_ath_renewal_gap_avg_252d(close: pd.Series) -> pd.Series:
    # Average days between new all-time highs in the last year
    is_high = (close == close.cummax())
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_high).ffill()
    return indices.diff().rolling(252).mean()


# 126-140: Metric Specific ATH Durations
def hwd_126_days_since_ebitda_ath(ebitda: pd.Series) -> pd.Series:
    return _days_since_expanding_high(ebitda)


def hwd_127_days_since_netinc_ath(netinc: pd.Series) -> pd.Series:
    return _days_since_expanding_high(netinc)


def hwd_128_days_since_assets_ath(assets: pd.Series) -> pd.Series:
    return _days_since_expanding_high(assets)


# 141-150: Final High Water Composites
def hwd_141_ath_drawdown_convexity_score_ath(close: pd.Series) -> pd.Series:
    # Integral of ATH drawdown normalized by duration
    h = close.cummax()
    dd = (h - close) / h
    area = dd.expanding().sum()
    dur = hwd_016_days_since_ath(close)
    return _safe_div(area, dur)


def hwd_142_mktcap_to_revenue_ath_ratio(close: pd.Series, sharesbas: pd.Series, revenue: pd.Series) -> pd.Series:
    # Current Mkt Cap / ATH Revenue
    mc = close * sharesbas
    r_ath = revenue.cummax()
    return _safe_div(mc, r_ath)


def hwd_143_ath_drawdown_log_decay_constant(close: pd.Series) -> pd.Series:
    # Fitting exponential decay to the ATH drawdown path
    h = close.cummax()
    dd = (h - close) / h + 0.01
    def _decay(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), np.log(y)).slope
    return dd.rolling(63).apply(_decay, raw=True)


def hwd_144_days_since_ath_to_cycle_high_ratio(close: pd.Series) -> pd.Series:
    d_ath = _days_since_expanding_high(close)
    d_252 = pd.Series(np.arange(len(close)), index=close.index) - pd.Series(np.arange(len(close)), index=close.index).where(close == _rolling_max(close, 252)).ffill()
    return _safe_div(d_ath, d_252)


def hwd_145_ath_drawdown_energy_index(close: pd.Series) -> pd.Series:
    # (Pct below ATH)^2 * Days since ATH
    dist = (close.cummax() - close) / close.cummax()
    dur = hwd_016_days_since_ath(close)
    return (dist**2) * dur


def hwd_146_years_since_equity_ath(equity: pd.Series) -> pd.Series:
    return _days_since_expanding_high(equity) / 252.0


def hwd_147_ath_stale_years_count(close: pd.Series) -> pd.Series:
    # Days since last *significant* ATH update
    h = close.cummax()
    is_big = (h > h.shift(1) * 1.05)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_big).ffill()
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def hwd_148_ath_proximity_oscillator_252d(close: pd.Series) -> pd.Series:
    h = close.cummax()
    p = close / h
    return (p - p.rolling(252).min()) / (p.rolling(252).max() - p.rolling(252).min())


def hwd_149_cumulative_ath_pain_index_ath(close: pd.Series) -> pd.Series:
    # Square root of the integral of squared ATH drawdowns
    h = close.cummax()
    dd = (h - close) / h
    return np.sqrt((dd**2).expanding().mean())


def hwd_150_ath_exhaustion_composite(close: pd.Series) -> pd.Series:
    # Weighted: (Time since ATH) + (Depth from ATH) + (Volatility of ATH distance)
    h = close.cummax()
    dist = (h - close) / h
    dur = hwd_016_days_since_ath(close) / (252 * 10) # 10y norm
    v_dist = dist.rolling(63).std()
    return 0.4 * dist + 0.4 * dur.clip(0,1) + 0.2 * v_dist


# ── Registry ──────────────────────────────────────────────────────────────────

V12_REGISTRY = {
    "hwd_076_ath_to_200ma_ratio": {"inputs": ["close"], "func": hwd_076_ath_to_200ma_ratio},
    "hwd_077_ath_drawdown_persistence_252d": {"inputs": ["close"], "func": hwd_077_ath_drawdown_persistence_252d},
    "hwd_078_days_since_ath_zscore_ath": {"inputs": ["close"], "func": hwd_078_days_since_ath_zscore_ath},
    "hwd_091_ath_recovery_velocity_21d": {"inputs": ["close"], "func": hwd_091_ath_recovery_velocity_21d},
    "hwd_092_volume_at_ath_drawdown_peak_63d": {"inputs": ["close", "volume"], "func": hwd_092_volume_at_ath_drawdown_peak_63d},
    "hwd_106_dist_to_ath_vs_dist_to_5y_high": {"inputs": ["close"], "func": hwd_106_dist_to_ath_vs_dist_to_5y_high},
    "hwd_107_ath_renewal_gap_avg_252d": {"inputs": ["close"], "func": hwd_107_ath_renewal_gap_avg_252d},
    "hwd_126_days_since_ebitda_ath": {"inputs": ["ebitda"], "func": hwd_126_days_since_ebitda_ath},
    "hwd_127_days_since_netinc_ath": {"inputs": ["netinc"], "func": hwd_127_days_since_netinc_ath},
    "hwd_128_days_since_assets_ath": {"inputs": ["assets"], "func": hwd_128_days_since_assets_ath},
    "hwd_141_ath_drawdown_convexity_score_ath": {"inputs": ["close"], "func": hwd_141_ath_drawdown_convexity_score_ath},
    "hwd_142_mktcap_to_revenue_ath_ratio": {"inputs": ["close", "sharesbas", "revenue"], "func": hwd_142_mktcap_to_revenue_ath_ratio},
    "hwd_143_ath_drawdown_log_decay_constant": {"inputs": ["close"], "func": hwd_143_ath_drawdown_log_decay_constant},
    "hwd_144_days_since_ath_to_cycle_high_ratio": {"inputs": ["close"], "func": hwd_144_days_since_ath_to_cycle_high_ratio},
    "hwd_145_ath_drawdown_energy_index": {"inputs": ["close"], "func": hwd_145_ath_drawdown_energy_index},
    "hwd_146_years_since_equity_ath": {"inputs": ["equity"], "func": hwd_146_years_since_equity_ath},
    "hwd_147_ath_stale_years_count": {"inputs": ["close"], "func": hwd_147_ath_stale_years_count},
    "hwd_148_ath_proximity_oscillator_252d": {"inputs": ["close"], "func": hwd_148_ath_proximity_oscillator_252d},
    "hwd_149_cumulative_ath_pain_index_ath": {"inputs": ["close"], "func": hwd_149_cumulative_ath_pain_index_ath},
    "hwd_150_ath_exhaustion_composite": {"inputs": ["close"], "func": hwd_150_ath_exhaustion_composite},
}
