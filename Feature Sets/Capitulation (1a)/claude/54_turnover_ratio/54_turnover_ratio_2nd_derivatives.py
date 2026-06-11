"""
54_turnover_ratio — 2nd Derivatives (Features tnv_drv2_001-025)
Domain: rate of change of base turnover-ratio features — velocity of long-horizon turnover
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — acceleration of multi-year turnover extremes.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def tnv_drv2_001_turnover_proxy_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 252d-normalised turnover (weekly velocity of annual turnover rate)."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    return tnv.diff(_TD_WEEK)


def tnv_drv2_002_turnover_proxy_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252d-normalised turnover (monthly velocity)."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    return tnv.diff(_TD_MON)


def tnv_drv2_003_turnover_proxy_504d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 504d-normalised turnover."""
    tnv = _turnover_proxy(volume, _TD_2YR)
    return tnv.diff(_TD_WEEK)


def tnv_drv2_004_turnover_proxy_504d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 504d-normalised turnover (monthly change in 2yr turnover rate)."""
    tnv = _turnover_proxy(volume, _TD_2YR)
    return tnv.diff(_TD_MON)


def tnv_drv2_005_vol_pct_rank_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 252d volume percentile rank (weekly momentum in turnover rank)."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def tnv_drv2_006_vol_pct_rank_504d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 504d volume percentile rank."""
    rank = volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)
    return rank.diff(_TD_MON)


def tnv_drv2_007_vol_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 252d volume z-score (velocity of z-score change)."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_WEEK)


def tnv_drv2_008_vol_zscore_504d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 504d volume z-score."""
    m = _rolling_mean(volume, _TD_2YR)
    s = _rolling_std(volume, _TD_2YR)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_MON)


def tnv_drv2_009_dvol_pct_rank_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 252d dollar-volume percentile rank."""
    dv = _dollar_volume(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def tnv_drv2_010_dvol_pct_rank_504d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 504d dollar-volume percentile rank."""
    dv = _dollar_volume(close, volume)
    rank = dv.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)
    return rank.diff(_TD_MON)


def tnv_drv2_011_amihud_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 252d Amihud illiquidity mean (velocity of illiquidity change)."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    m = illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return m.diff(_TD_WEEK)


def tnv_drv2_012_amihud_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252d Amihud illiquidity mean."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    m = illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return m.diff(_TD_MON)


def tnv_drv2_013_mean_vol_ratio_252d_504d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 252d/504d mean-volume ratio (regime shift velocity)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_mean(volume, _TD_2YR))
    return ratio.diff(_TD_WEEK)


def tnv_drv2_014_mean_vol_ratio_252d_756d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252d/756d mean-volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_mean(volume, _TD_3YR))
    return ratio.diff(_TD_MON)


def tnv_drv2_015_turnover_proxy_252d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252d-normalised turnover over trailing 21 days."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    return _linslope(tnv, _TD_MON)


def tnv_drv2_016_turnover_proxy_504d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 504d-normalised turnover over trailing 63 days."""
    tnv = _turnover_proxy(volume, _TD_2YR)
    return _linslope(tnv, _TD_QTR)


def tnv_drv2_017_vol_pct_rank_252d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252d volume pct-rank over trailing 21 days."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return _linslope(rank, _TD_MON)


def tnv_drv2_018_dvol_zscore_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 252d dollar-volume z-score."""
    dv = _dollar_volume(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    return z.diff(_TD_WEEK)


def tnv_drv2_019_turnover_down_fraction_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252d fraction of volume on down days."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, 0.0)
    frac = _safe_div(_rolling_sum(down_vol, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    return frac.diff(_TD_MON)


def tnv_drv2_020_vol_cum_252d_vs_504d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of cumulative-252d/cumulative-504d volume ratio."""
    ratio = _safe_div(_rolling_sum(volume, _TD_YEAR), _rolling_sum(volume, _TD_2YR))
    return ratio.diff(_TD_WEEK)


def tnv_drv2_021_vol_per_price_252d_norm_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume-per-price-unit normalised by 252d mean."""
    vpu = _safe_div(volume, close)
    norm = _safe_div(vpu, _rolling_mean(vpu, _TD_YEAR))
    return norm.diff(_TD_WEEK)


def tnv_drv2_022_consecutive_below_252d_mean_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of consecutive-below-252d-mean streak (illiquidity streak velocity)."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    cond = volume < baseline
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum().astype(float)
    return streak.diff(_TD_MON)


def tnv_drv2_023_vol_expanding_pct_rank_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of expanding all-history volume pct rank."""
    rank = volume.expanding(min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_MON)


def tnv_drv2_024_dvol_vs_cum_dvol_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of daily dollar-volume / 252d cumulative dollar-volume ratio."""
    dv = _dollar_volume(close, volume)
    frac = _safe_div(dv, _rolling_sum(dv, _TD_YEAR))
    return frac.diff(_TD_WEEK)


def tnv_drv2_025_turnover_extremity_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252d turnover extremity score (dist from median rank)."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ext = (rank - 0.5).abs()
    return ext.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

TURNOVER_RATIO_REGISTRY_2ND_DERIVATIVES = {
    "tnv_drv2_001_turnover_proxy_252d_5d_diff": {"inputs": ["volume"], "func": tnv_drv2_001_turnover_proxy_252d_5d_diff},
    "tnv_drv2_002_turnover_proxy_252d_21d_diff": {"inputs": ["volume"], "func": tnv_drv2_002_turnover_proxy_252d_21d_diff},
    "tnv_drv2_003_turnover_proxy_504d_5d_diff": {"inputs": ["volume"], "func": tnv_drv2_003_turnover_proxy_504d_5d_diff},
    "tnv_drv2_004_turnover_proxy_504d_21d_diff": {"inputs": ["volume"], "func": tnv_drv2_004_turnover_proxy_504d_21d_diff},
    "tnv_drv2_005_vol_pct_rank_252d_5d_diff": {"inputs": ["volume"], "func": tnv_drv2_005_vol_pct_rank_252d_5d_diff},
    "tnv_drv2_006_vol_pct_rank_504d_21d_diff": {"inputs": ["volume"], "func": tnv_drv2_006_vol_pct_rank_504d_21d_diff},
    "tnv_drv2_007_vol_zscore_252d_5d_diff": {"inputs": ["volume"], "func": tnv_drv2_007_vol_zscore_252d_5d_diff},
    "tnv_drv2_008_vol_zscore_504d_21d_diff": {"inputs": ["volume"], "func": tnv_drv2_008_vol_zscore_504d_21d_diff},
    "tnv_drv2_009_dvol_pct_rank_252d_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv2_009_dvol_pct_rank_252d_5d_diff},
    "tnv_drv2_010_dvol_pct_rank_504d_21d_diff": {"inputs": ["close", "volume"], "func": tnv_drv2_010_dvol_pct_rank_504d_21d_diff},
    "tnv_drv2_011_amihud_252d_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv2_011_amihud_252d_5d_diff},
    "tnv_drv2_012_amihud_252d_21d_diff": {"inputs": ["close", "volume"], "func": tnv_drv2_012_amihud_252d_21d_diff},
    "tnv_drv2_013_mean_vol_ratio_252d_504d_5d_diff": {"inputs": ["volume"], "func": tnv_drv2_013_mean_vol_ratio_252d_504d_5d_diff},
    "tnv_drv2_014_mean_vol_ratio_252d_756d_21d_diff": {"inputs": ["volume"], "func": tnv_drv2_014_mean_vol_ratio_252d_756d_21d_diff},
    "tnv_drv2_015_turnover_proxy_252d_slope_21d": {"inputs": ["volume"], "func": tnv_drv2_015_turnover_proxy_252d_slope_21d},
    "tnv_drv2_016_turnover_proxy_504d_slope_63d": {"inputs": ["volume"], "func": tnv_drv2_016_turnover_proxy_504d_slope_63d},
    "tnv_drv2_017_vol_pct_rank_252d_slope_21d": {"inputs": ["volume"], "func": tnv_drv2_017_vol_pct_rank_252d_slope_21d},
    "tnv_drv2_018_dvol_zscore_252d_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv2_018_dvol_zscore_252d_5d_diff},
    "tnv_drv2_019_turnover_down_fraction_252d_21d_diff": {"inputs": ["close", "volume"], "func": tnv_drv2_019_turnover_down_fraction_252d_21d_diff},
    "tnv_drv2_020_vol_cum_252d_vs_504d_5d_diff": {"inputs": ["volume"], "func": tnv_drv2_020_vol_cum_252d_vs_504d_5d_diff},
    "tnv_drv2_021_vol_per_price_252d_norm_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv2_021_vol_per_price_252d_norm_5d_diff},
    "tnv_drv2_022_consecutive_below_252d_mean_21d_diff": {"inputs": ["volume"], "func": tnv_drv2_022_consecutive_below_252d_mean_21d_diff},
    "tnv_drv2_023_vol_expanding_pct_rank_21d_diff": {"inputs": ["volume"], "func": tnv_drv2_023_vol_expanding_pct_rank_21d_diff},
    "tnv_drv2_024_dvol_vs_cum_dvol_252d_5d_diff": {"inputs": ["close", "volume"], "func": tnv_drv2_024_dvol_vs_cum_dvol_252d_5d_diff},
    "tnv_drv2_025_turnover_extremity_252d_21d_diff": {"inputs": ["volume"], "func": tnv_drv2_025_turnover_extremity_252d_21d_diff},
}
