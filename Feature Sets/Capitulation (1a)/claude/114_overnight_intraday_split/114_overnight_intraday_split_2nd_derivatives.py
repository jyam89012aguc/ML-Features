"""
114_overnight_intraday_split — 2nd Derivatives (Features ois_drv2_001-025)
Domain: rate of change of base overnight/intraday split features — velocity of
        session-return decomposition, gap persistence trends, distress acceleration
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _overnight_ret(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight return: prior close -> today open."""
    return open_ / close.shift(1) - 1.0


def _intraday_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday return: today open -> today close."""
    return close / open_ - 1.0


def _total_ret(close: pd.Series) -> pd.Series:
    """Total daily return: prior close -> today close."""
    return close.pct_change(1)


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

def ois_drv2_001_overnight_ret_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight return (velocity of gap change)."""
    return _overnight_ret(close, open).diff(_TD_WEEK)


def ois_drv2_002_intraday_ret_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of intraday return (velocity of intraday change)."""
    return _intraday_ret(open, close).diff(_TD_WEEK)


def ois_drv2_003_overnight_ret_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of overnight return (monthly velocity of gap movement)."""
    return _overnight_ret(close, open).diff(_TD_MON)


def ois_drv2_004_intraday_ret_21d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of intraday return (monthly velocity of intraday movement)."""
    return _intraday_ret(open, close).diff(_TD_MON)


def ois_drv2_005_cum_overnight_ret_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative overnight return (velocity of overnight pressure)."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    return cum.diff(_TD_WEEK)


def ois_drv2_006_cum_intraday_ret_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative intraday return (velocity of intraday pressure)."""
    cum = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    return cum.diff(_TD_WEEK)


def ois_drv2_007_overnight_vol_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day overnight volatility (velocity of vol change)."""
    vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    return vol.diff(_TD_WEEK)


def ois_drv2_008_intraday_vol_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday volatility."""
    vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    return vol.diff(_TD_WEEK)


def ois_drv2_009_overnight_distress_score_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day overnight distress score (deepening overnight losses)."""
    dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    return dist.diff(_TD_WEEK)


def ois_drv2_010_intraday_distress_score_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday distress score."""
    dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    return dist.diff(_TD_WEEK)


def ois_drv2_011_overnight_negative_days_frac_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day fraction of negative overnight days."""
    frac = _rolling_sum((_overnight_ret(close, open) < 0).astype(float), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def ois_drv2_012_intraday_negative_days_frac_21d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day fraction of negative intraday days."""
    frac = _rolling_sum((_intraday_ret(open, close) < 0).astype(float), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def ois_drv2_013_overnight_vs_intraday_vol_ratio_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight/intraday vol ratio (session vol balance shift)."""
    on_vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    ratio = _safe_div(on_vol, intra_vol.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


def ois_drv2_014_overnight_share_cum_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight share of 21-day cumulative return."""
    on = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    tot = _rolling_sum(_total_ret(close), _TD_MON)
    share = _safe_div(on, tot.replace(0, np.nan))
    return share.diff(_TD_WEEK)


def ois_drv2_015_gap_persistence_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight gap persistence ratio (21d)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    gap_down = on < 0
    persistent = (gap_down & (intra < 0)).astype(float)
    gap_cnt = _rolling_sum(gap_down.astype(float), _TD_MON)
    pers_cnt = _rolling_sum(persistent, _TD_MON)
    pers_ratio = _safe_div(pers_cnt, gap_cnt.replace(0, np.nan))
    return pers_ratio.diff(_TD_WEEK)


def ois_drv2_016_reversal_frac_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of intraday reversal fraction (21d)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    rev = ((np.sign(on) != np.sign(intra)) & (on != 0) & (intra != 0)).astype(float)
    frac = _rolling_sum(rev, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def ois_drv2_017_overnight_down_consec_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of consecutive overnight down streak."""
    streak = _consec_streak(_overnight_ret(close, open) < 0)
    return streak.diff(_TD_WEEK)


def ois_drv2_018_intraday_down_consec_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of consecutive intraday down streak."""
    streak = _consec_streak(_intraday_ret(open, close) < 0)
    return streak.diff(_TD_WEEK)


def ois_drv2_019_overnight_ret_zscore_63d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight return 63d z-score (velocity of extreme gap reading)."""
    on = _overnight_ret(close, open)
    m = _rolling_mean(on, _TD_QTR)
    s = _rolling_std(on, _TD_QTR)
    z = _safe_div(on - m, s)
    return z.diff(_TD_WEEK)


def ois_drv2_020_intraday_ret_zscore_63d_5d_diff(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of intraday return 63d z-score."""
    intra = _intraday_ret(open, close)
    m = _rolling_mean(intra, _TD_QTR)
    s = _rolling_std(intra, _TD_QTR)
    z = _safe_div(intra - m, s)
    return z.diff(_TD_WEEK)


def ois_drv2_021_overnight_vol_fraction_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight vol fraction (overnight/total vol share change)."""
    on_vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    total_vol = on_vol + intra_vol
    frac = _safe_div(on_vol, total_vol.replace(0, np.nan))
    return frac.diff(_TD_WEEK)


def ois_drv2_022_overnight_distress_21d_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of overnight distress score."""
    dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    vel5 = dist.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def ois_drv2_023_intraday_distress_21d_slope_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of intraday distress score."""
    dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    vel5 = dist.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def ois_drv2_024_overnight_cum_ret_21d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 21d cumulative overnight return (monthly change in overnight trend)."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    return cum.diff(_TD_MON)


def ois_drv2_025_overnight_vs_intraday_distress_ratio_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight-to-intraday distress ratio (63d window)."""
    on_dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0).abs(), _TD_QTR)
    intra_dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0).abs(), _TD_QTR)
    ratio = _safe_div(on_dist, intra_dist.replace(0, np.nan))
    return ratio.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

OVERNIGHT_INTRADAY_SPLIT_REGISTRY_2ND_DERIVATIVES = {
    "ois_drv2_001_overnight_ret_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_001_overnight_ret_5d_diff},
    "ois_drv2_002_intraday_ret_5d_diff": {"inputs": ["open", "close"], "func": ois_drv2_002_intraday_ret_5d_diff},
    "ois_drv2_003_overnight_ret_21d_diff": {"inputs": ["close", "open"], "func": ois_drv2_003_overnight_ret_21d_diff},
    "ois_drv2_004_intraday_ret_21d_diff": {"inputs": ["open", "close"], "func": ois_drv2_004_intraday_ret_21d_diff},
    "ois_drv2_005_cum_overnight_ret_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_005_cum_overnight_ret_21d_5d_diff},
    "ois_drv2_006_cum_intraday_ret_21d_5d_diff": {"inputs": ["open", "close"], "func": ois_drv2_006_cum_intraday_ret_21d_5d_diff},
    "ois_drv2_007_overnight_vol_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_007_overnight_vol_21d_5d_diff},
    "ois_drv2_008_intraday_vol_21d_5d_diff": {"inputs": ["open", "close"], "func": ois_drv2_008_intraday_vol_21d_5d_diff},
    "ois_drv2_009_overnight_distress_score_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_009_overnight_distress_score_21d_5d_diff},
    "ois_drv2_010_intraday_distress_score_21d_5d_diff": {"inputs": ["open", "close"], "func": ois_drv2_010_intraday_distress_score_21d_5d_diff},
    "ois_drv2_011_overnight_negative_days_frac_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_011_overnight_negative_days_frac_21d_5d_diff},
    "ois_drv2_012_intraday_negative_days_frac_21d_5d_diff": {"inputs": ["open", "close"], "func": ois_drv2_012_intraday_negative_days_frac_21d_5d_diff},
    "ois_drv2_013_overnight_vs_intraday_vol_ratio_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_013_overnight_vs_intraday_vol_ratio_21d_5d_diff},
    "ois_drv2_014_overnight_share_cum_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_014_overnight_share_cum_21d_5d_diff},
    "ois_drv2_015_gap_persistence_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_015_gap_persistence_21d_5d_diff},
    "ois_drv2_016_reversal_frac_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_016_reversal_frac_21d_5d_diff},
    "ois_drv2_017_overnight_down_consec_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_017_overnight_down_consec_5d_diff},
    "ois_drv2_018_intraday_down_consec_5d_diff": {"inputs": ["open", "close"], "func": ois_drv2_018_intraday_down_consec_5d_diff},
    "ois_drv2_019_overnight_ret_zscore_63d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_019_overnight_ret_zscore_63d_5d_diff},
    "ois_drv2_020_intraday_ret_zscore_63d_5d_diff": {"inputs": ["open", "close"], "func": ois_drv2_020_intraday_ret_zscore_63d_5d_diff},
    "ois_drv2_021_overnight_vol_fraction_21d_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_021_overnight_vol_fraction_21d_5d_diff},
    "ois_drv2_022_overnight_distress_21d_slope_21d": {"inputs": ["close", "open"], "func": ois_drv2_022_overnight_distress_21d_slope_21d},
    "ois_drv2_023_intraday_distress_21d_slope_21d": {"inputs": ["open", "close"], "func": ois_drv2_023_intraday_distress_21d_slope_21d},
    "ois_drv2_024_overnight_cum_ret_21d_21d_diff": {"inputs": ["close", "open"], "func": ois_drv2_024_overnight_cum_ret_21d_21d_diff},
    "ois_drv2_025_overnight_vs_intraday_distress_ratio_5d_diff": {"inputs": ["close", "open"], "func": ois_drv2_025_overnight_vs_intraday_distress_ratio_5d_diff},
}
