"""
54_turnover_ratio — 3rd Derivatives (Features tnv_drv3_001-025)
Domain: rate of change of 2nd-derivative turnover features — acceleration of velocity
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — jerk / convexity of multi-year turnover extremes.
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
_TD_2YR = 504
_TD_3YR = 756
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _dollar_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
    return close * volume


def _turnover_proxy(volume: pd.Series, window: int) -> pd.Series:
    return _safe_div(volume, _rolling_mean(volume, window))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each = diff/slope applied to a 2nd-derivative concept

def tnv_drv3_001_turnover_proxy_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d-normalised turnover (acceleration of annual turnover rate)."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    vel = tnv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_002_turnover_proxy_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 252d turnover (jerk in monthly change)."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    vel21 = tnv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_003_turnover_proxy_504d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 504d-normalised turnover (2yr turnover acceleration)."""
    tnv = _turnover_proxy(volume, _TD_2YR)
    vel = tnv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_004_turnover_proxy_504d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 504d turnover proxy."""
    tnv = _turnover_proxy(volume, _TD_2YR)
    vel21 = tnv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_005_vol_pct_rank_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d volume percentile rank (rank acceleration)."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_006_vol_zscore_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d volume z-score (z-score acceleration)."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_007_dvol_pct_rank_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d dollar-volume pct rank (dvol rank acceleration)."""
    dv = _dollar_volume(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_008_amihud_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d Amihud mean (illiquidity acceleration)."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    m = illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    vel = m.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_009_amihud_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252d Amihud mean."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    m = illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    vel21 = m.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_010_mean_vol_ratio_252d_504d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d/504d mean ratio (regime shift acceleration)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_mean(volume, _TD_2YR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_011_turnover_proxy_252d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252d turnover over 21 days (slope acceleration)."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    slp = _linslope(tnv, _TD_MON)
    return slp.diff(_TD_WEEK)


def tnv_drv3_012_vol_pct_rank_252d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252d pct-rank over 21 days."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    slp = _linslope(rank, _TD_MON)
    return slp.diff(_TD_WEEK)


def tnv_drv3_013_turnover_proxy_504d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 504d turnover over 63 days."""
    tnv = _turnover_proxy(volume, _TD_2YR)
    slp = _linslope(tnv, _TD_QTR)
    return slp.diff(_TD_WEEK)


def tnv_drv3_014_dvol_zscore_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d dollar-volume z-score."""
    dv = _dollar_volume(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_015_turnover_down_fraction_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252d fraction of volume on down days."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, 0.0)
    frac = _safe_div(_rolling_sum(down_vol, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_016_vol_cum_ratio_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of cumulative-252d/504d ratio."""
    ratio = _safe_div(_rolling_sum(volume, _TD_YEAR), _rolling_sum(volume, _TD_2YR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_017_vol_expanding_pct_rank_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in expanding pct-rank."""
    rank = volume.expanding(min_periods=_TD_QTR).rank(pct=True)
    vel21 = rank.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_018_turnover_extremity_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252d extremity score."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ext = (rank - 0.5).abs()
    vel21 = ext.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_019_dvol_vs_cum_dvol_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of daily-dvol/252d-cum-dvol fraction."""
    dv = _dollar_volume(close, volume)
    frac = _safe_div(dv, _rolling_sum(dv, _TD_YEAR))
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_020_vol_pct_rank_504d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 504d volume pct-rank."""
    rank = volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)
    vel21 = rank.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_021_turnover_proxy_252d_21d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 21d-velocity of 252d turnover proxy."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    vel21 = tnv.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def tnv_drv3_022_mean_vol_ratio_252d_756d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252d/756d mean-volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_mean(volume, _TD_3YR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_023_vol_per_price_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of volume-per-price-unit / 252d-norm (acceleration)."""
    vpu = _safe_div(volume, close)
    norm = _safe_div(vpu, _rolling_mean(vpu, _TD_YEAR))
    vel = norm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tnv_drv3_024_vol_zscore_504d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 504d volume z-score."""
    m = _rolling_mean(volume, _TD_2YR)
    s = _rolling_std(volume, _TD_2YR)
    z = _safe_div(volume - m, s)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tnv_drv3_025_turnover_composite_extremity_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in composite extremity score (252d+504d avg)."""
    r252 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r504 = volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)
    ext = ((r252 - 0.5).abs() + (r504 - 0.5).abs()) / 2.0
    vel21 = ext.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

TURNOVER_RATIO_REGISTRY_3RD_DERIVATIVES = {
    "tnv_drv3_001_turnover_proxy_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_001_turnover_proxy_252d_5d_diff_5d_diff},
    "tnv_drv3_002_turnover_proxy_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_002_turnover_proxy_252d_21d_diff_5d_diff},
    "tnv_drv3_003_turnover_proxy_504d_5d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_003_turnover_proxy_504d_5d_diff_5d_diff},
    "tnv_drv3_004_turnover_proxy_504d_21d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_004_turnover_proxy_504d_21d_diff_5d_diff},
    "tnv_drv3_005_vol_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_005_vol_pct_rank_252d_5d_diff_5d_diff},
    "tnv_drv3_006_vol_zscore_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_006_vol_zscore_252d_5d_diff_5d_diff},
    "tnv_drv3_007_dvol_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv3_007_dvol_pct_rank_252d_5d_diff_5d_diff},
    "tnv_drv3_008_amihud_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv3_008_amihud_252d_5d_diff_5d_diff},
    "tnv_drv3_009_amihud_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv3_009_amihud_252d_21d_diff_5d_diff},
    "tnv_drv3_010_mean_vol_ratio_252d_504d_5d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_010_mean_vol_ratio_252d_504d_5d_diff_5d_diff},
    "tnv_drv3_011_turnover_proxy_252d_slope_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_011_turnover_proxy_252d_slope_5d_diff},
    "tnv_drv3_012_vol_pct_rank_252d_slope_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_012_vol_pct_rank_252d_slope_5d_diff},
    "tnv_drv3_013_turnover_proxy_504d_slope_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_013_turnover_proxy_504d_slope_5d_diff},
    "tnv_drv3_014_dvol_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv3_014_dvol_zscore_252d_5d_diff_5d_diff},
    "tnv_drv3_015_turnover_down_fraction_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv3_015_turnover_down_fraction_252d_21d_diff_5d_diff},
    "tnv_drv3_016_vol_cum_ratio_5d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_016_vol_cum_ratio_5d_diff_5d_diff},
    "tnv_drv3_017_vol_expanding_pct_rank_21d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_017_vol_expanding_pct_rank_21d_diff_5d_diff},
    "tnv_drv3_018_turnover_extremity_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_018_turnover_extremity_252d_21d_diff_5d_diff},
    "tnv_drv3_019_dvol_vs_cum_dvol_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv3_019_dvol_vs_cum_dvol_252d_5d_diff_5d_diff},
    "tnv_drv3_020_vol_pct_rank_504d_21d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_020_vol_pct_rank_504d_21d_diff_5d_diff},
    "tnv_drv3_021_turnover_proxy_252d_21d_diff_slope_21d": {"inputs": ["volume"], "func": tnv_drv3_021_turnover_proxy_252d_21d_diff_slope_21d},
    "tnv_drv3_022_mean_vol_ratio_252d_756d_21d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_022_mean_vol_ratio_252d_756d_21d_diff_5d_diff},
    "tnv_drv3_023_vol_per_price_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv3_023_vol_per_price_5d_diff_5d_diff},
    "tnv_drv3_024_vol_zscore_504d_21d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_024_vol_zscore_504d_21d_diff_5d_diff},
    "tnv_drv3_025_turnover_composite_extremity_21d_diff_5d_diff": {"inputs": ["volume"], "func": tnv_drv3_025_turnover_composite_extremity_21d_diff_5d_diff},
}
