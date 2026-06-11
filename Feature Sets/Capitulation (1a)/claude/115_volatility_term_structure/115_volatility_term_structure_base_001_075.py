"""
115_volatility_term_structure — Base Features 001-075
Domain: term structure of realized volatility — ratios and slopes of short-horizon vs
        long-horizon realized vol (5d/21d, 21d/63d, 63d/252d), vol-curve shape and
        curvature, term-structure inversion (short vol exceeding long vol — stress
        signature), vol cone position, multi-horizon vol spreads.
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
    """Element-wise division; replaces zero denominator with NaN."""
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility (std of log-returns) over w days."""
    lr = np.log(close / close.shift(1))
    rv = lr.rolling(w, min_periods=max(2, w // 2)).std()
    return rv * np.sqrt(_TD_YEAR)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (NaN-safe)."""
    def _slope(x):
        v = x[~np.isnan(x)]
        if len(v) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(v), dtype=float)
        xi_m = xi.mean()
        x_m = v.mean()
        num = ((xi - xi_m) * (v - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Raw realized vol at key horizons ---

def vts_001_rv5d(close: pd.Series) -> pd.Series:
    """5-day (weekly) realized volatility, annualized."""
    return _realized_vol(close, _TD_WEEK)


def vts_002_rv21d(close: pd.Series) -> pd.Series:
    """21-day (monthly) realized volatility, annualized."""
    return _realized_vol(close, _TD_MON)


def vts_003_rv63d(close: pd.Series) -> pd.Series:
    """63-day (quarterly) realized volatility, annualized."""
    return _realized_vol(close, _TD_QTR)


def vts_004_rv126d(close: pd.Series) -> pd.Series:
    """126-day (semi-annual) realized volatility, annualized."""
    return _realized_vol(close, _TD_HALF)


def vts_005_rv252d(close: pd.Series) -> pd.Series:
    """252-day (annual) realized volatility, annualized."""
    return _realized_vol(close, _TD_YEAR)


def vts_006_rv10d(close: pd.Series) -> pd.Series:
    """10-day realized volatility, annualized (2-week horizon)."""
    return _realized_vol(close, 10)


def vts_007_rv15d(close: pd.Series) -> pd.Series:
    """15-day realized volatility, annualized."""
    return _realized_vol(close, 15)


def vts_008_rv30d(close: pd.Series) -> pd.Series:
    """30-day realized volatility, annualized."""
    return _realized_vol(close, 30)


def vts_009_rv42d(close: pd.Series) -> pd.Series:
    """42-day (2-month) realized volatility, annualized."""
    return _realized_vol(close, 42)


def vts_010_rv2d(close: pd.Series) -> pd.Series:
    """2-day realized volatility, annualized (ultra-short horizon)."""
    return _realized_vol(close, 2)


def vts_011_rv3d(close: pd.Series) -> pd.Series:
    """3-day realized volatility, annualized."""
    return _realized_vol(close, 3)


def vts_012_rv7d(close: pd.Series) -> pd.Series:
    """7-day realized volatility, annualized."""
    return _realized_vol(close, 7)


def vts_013_rv189d(close: pd.Series) -> pd.Series:
    """189-day (9-month) realized volatility, annualized."""
    return _realized_vol(close, 189)


def vts_014_rv84d(close: pd.Series) -> pd.Series:
    """84-day (4-month) realized volatility, annualized."""
    return _realized_vol(close, 84)


def vts_015_rv105d(close: pd.Series) -> pd.Series:
    """105-day (5-month) realized volatility, annualized."""
    return _realized_vol(close, 105)


# --- Group B (016-030): Vol term-structure ratios (short/long) ---

def vts_016_rv5d_rv21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5d realized vol to 21d realized vol (weekly/monthly term spread)."""
    return _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))


def vts_017_rv21d_rv63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21d realized vol to 63d realized vol (monthly/quarterly term spread)."""
    return _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_QTR))


def vts_018_rv63d_rv252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63d realized vol to 252d realized vol (quarterly/annual term spread)."""
    return _safe_div(_realized_vol(close, _TD_QTR), _realized_vol(close, _TD_YEAR))


def vts_019_rv5d_rv63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5d to 63d realized vol (weekly/quarterly spread)."""
    return _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_QTR))


def vts_020_rv5d_rv252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5d to 252d realized vol (widest short/long term spread)."""
    return _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_YEAR))


def vts_021_rv21d_rv252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21d to 252d realized vol (monthly/annual term spread)."""
    return _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_YEAR))


def vts_022_rv10d_rv21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 10d to 21d realized vol."""
    return _safe_div(_realized_vol(close, 10), _realized_vol(close, _TD_MON))


def vts_023_rv10d_rv63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 10d to 63d realized vol."""
    return _safe_div(_realized_vol(close, 10), _realized_vol(close, _TD_QTR))


def vts_024_rv21d_rv126d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21d to 126d realized vol (monthly/semi-annual)."""
    return _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_HALF))


def vts_025_rv63d_rv126d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63d to 126d realized vol (quarterly/semi-annual)."""
    return _safe_div(_realized_vol(close, _TD_QTR), _realized_vol(close, _TD_HALF))


def vts_026_rv126d_rv252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 126d to 252d realized vol (semi-annual/annual)."""
    return _safe_div(_realized_vol(close, _TD_HALF), _realized_vol(close, _TD_YEAR))


def vts_027_rv5d_rv126d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5d to 126d realized vol (weekly/semi-annual)."""
    return _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_HALF))


def vts_028_rv3d_rv21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 3d to 21d realized vol (ultra-short/monthly)."""
    return _safe_div(_realized_vol(close, 3), _realized_vol(close, _TD_MON))


def vts_029_rv7d_rv63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 7d to 63d realized vol."""
    return _safe_div(_realized_vol(close, 7), _realized_vol(close, _TD_QTR))


def vts_030_rv30d_rv252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 30d to 252d realized vol."""
    return _safe_div(_realized_vol(close, 30), _realized_vol(close, _TD_YEAR))


# --- Group C (031-045): Vol term-structure spreads (absolute differences) ---

def vts_031_rv5d_rv21d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 5d RV minus 21d RV (positive = inverted/stressed)."""
    return _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)


def vts_032_rv21d_rv63d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 21d RV minus 63d RV."""
    return _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_QTR)


def vts_033_rv63d_rv252d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 63d RV minus 252d RV."""
    return _realized_vol(close, _TD_QTR) - _realized_vol(close, _TD_YEAR)


def vts_034_rv5d_rv63d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 5d RV minus 63d RV."""
    return _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_QTR)


def vts_035_rv5d_rv252d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 5d RV minus 252d RV (widest spread, stress signal)."""
    return _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_YEAR)


def vts_036_rv10d_rv63d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 10d RV minus 63d RV."""
    return _realized_vol(close, 10) - _realized_vol(close, _TD_QTR)


def vts_037_rv21d_rv252d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 21d RV minus 252d RV."""
    return _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_YEAR)


def vts_038_rv21d_rv126d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 21d RV minus 126d RV."""
    return _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_HALF)


def vts_039_rv63d_rv126d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 63d RV minus 126d RV."""
    return _realized_vol(close, _TD_QTR) - _realized_vol(close, _TD_HALF)


def vts_040_rv126d_rv252d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 126d RV minus 252d RV."""
    return _realized_vol(close, _TD_HALF) - _realized_vol(close, _TD_YEAR)


def vts_041_rv3d_rv63d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 3d RV minus 63d RV."""
    return _realized_vol(close, 3) - _realized_vol(close, _TD_QTR)


def vts_042_rv7d_rv21d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 7d RV minus 21d RV."""
    return _realized_vol(close, 7) - _realized_vol(close, _TD_MON)


def vts_043_rv30d_rv126d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 30d RV minus 126d RV."""
    return _realized_vol(close, 30) - _realized_vol(close, _TD_HALF)


def vts_044_rv42d_rv252d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 42d RV minus 252d RV."""
    return _realized_vol(close, 42) - _realized_vol(close, _TD_YEAR)


def vts_045_rv5d_rv126d_spread(close: pd.Series) -> pd.Series:
    """Absolute spread: 5d RV minus 126d RV."""
    return _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_HALF)


# --- Group D (046-055): Inversion flags and inversion duration ---

def vts_046_ts_inversion_5d21d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 5d RV > 21d RV (term structure inverted at short end)."""
    return (_realized_vol(close, _TD_WEEK) > _realized_vol(close, _TD_MON)).astype(float)


def vts_047_ts_inversion_21d63d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 21d RV > 63d RV (monthly exceeds quarterly — mid-curve inversion)."""
    return (_realized_vol(close, _TD_MON) > _realized_vol(close, _TD_QTR)).astype(float)


def vts_048_ts_inversion_63d252d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63d RV > 252d RV (quarterly exceeds annual — back-end inversion)."""
    return (_realized_vol(close, _TD_QTR) > _realized_vol(close, _TD_YEAR)).astype(float)


def vts_049_ts_full_inversion_flag(close: pd.Series) -> pd.Series:
    """Binary flag: full term-structure inversion (5d>21d AND 21d>63d AND 63d>252d)."""
    r5 = _realized_vol(close, _TD_WEEK)
    r21 = _realized_vol(close, _TD_MON)
    r63 = _realized_vol(close, _TD_QTR)
    r252 = _realized_vol(close, _TD_YEAR)
    return ((r5 > r21) & (r21 > r63) & (r63 > r252)).astype(float)


def vts_050_consec_days_5d21d_inverted(close: pd.Series) -> pd.Series:
    """Consecutive days 5d RV has been above 21d RV."""
    return _consec_streak(_realized_vol(close, _TD_WEEK) > _realized_vol(close, _TD_MON))


def vts_051_consec_days_21d63d_inverted(close: pd.Series) -> pd.Series:
    """Consecutive days 21d RV has been above 63d RV."""
    return _consec_streak(_realized_vol(close, _TD_MON) > _realized_vol(close, _TD_QTR))


def vts_052_consec_days_63d252d_inverted(close: pd.Series) -> pd.Series:
    """Consecutive days 63d RV has been above 252d RV."""
    return _consec_streak(_realized_vol(close, _TD_QTR) > _realized_vol(close, _TD_YEAR))


def vts_053_consec_days_full_inversion(close: pd.Series) -> pd.Series:
    """Consecutive days of full term-structure inversion."""
    r5 = _realized_vol(close, _TD_WEEK)
    r21 = _realized_vol(close, _TD_MON)
    r63 = _realized_vol(close, _TD_QTR)
    r252 = _realized_vol(close, _TD_YEAR)
    return _consec_streak((r5 > r21) & (r21 > r63) & (r63 > r252))


def vts_054_ts_inversion_5d63d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 5d RV > 63d RV (weekly exceeds quarterly)."""
    return (_realized_vol(close, _TD_WEEK) > _realized_vol(close, _TD_QTR)).astype(float)


def vts_055_ts_inversion_5d252d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 5d RV > 252d RV (short end stress vs long-run baseline)."""
    return (_realized_vol(close, _TD_WEEK) > _realized_vol(close, _TD_YEAR)).astype(float)


# --- Group E (056-065): Vol cone position (where current RV sits vs history) ---

def vts_056_rv5d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d RV within trailing 252-day distribution of 5d RV."""
    rv = _realized_vol(close, _TD_WEEK)
    return rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_057_rv21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d RV within trailing 252-day distribution of 21d RV."""
    rv = _realized_vol(close, _TD_MON)
    return rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_058_rv63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d RV within trailing 252-day distribution of 63d RV."""
    rv = _realized_vol(close, _TD_QTR)
    return rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_059_rv252d_pct_rank_expanding(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of 252d RV (vol cone upper boundary check)."""
    rv = _realized_vol(close, _TD_YEAR)
    return rv.expanding(min_periods=_TD_YEAR).rank(pct=True)


def vts_060_rv5d_ratio_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d/21d vol ratio within 252-day distribution of that ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_061_rv21d_ratio_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d/63d vol ratio within 252-day distribution."""
    ratio = _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_QTR))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_062_rv5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5d RV vs its trailing 252-day mean and std."""
    rv = _realized_vol(close, _TD_WEEK)
    return _safe_div(rv - _rolling_mean(rv, _TD_YEAR), _rolling_std(rv, _TD_YEAR))


def vts_063_rv21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d RV vs its trailing 252-day mean and std."""
    rv = _realized_vol(close, _TD_MON)
    return _safe_div(rv - _rolling_mean(rv, _TD_YEAR), _rolling_std(rv, _TD_YEAR))


def vts_064_rv63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d RV vs its trailing 252-day mean and std."""
    rv = _realized_vol(close, _TD_QTR)
    return _safe_div(rv - _rolling_mean(rv, _TD_YEAR), _rolling_std(rv, _TD_YEAR))


def vts_065_rv252d_zscore_expanding(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252d RV (all-time cone position)."""
    rv = _realized_vol(close, _TD_YEAR)
    m = rv.expanding(min_periods=_TD_YEAR).mean()
    s = rv.expanding(min_periods=_TD_YEAR).std()
    return _safe_div(rv - m, s)


# --- Group F (066-075): Curve shape, slope, and curvature ---

def vts_066_vol_curve_slope_5d_252d(close: pd.Series) -> pd.Series:
    """Log-linear slope of vol curve from 5d to 252d (log(rv252/rv5)/log(252/5))."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    return np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)


def vts_067_vol_curve_slope_21d_252d(close: pd.Series) -> pd.Series:
    """Log-linear slope of vol curve from 21d to 252d."""
    rv21 = _realized_vol(close, _TD_MON).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    return np.log(rv252 / rv21) / np.log(_TD_YEAR / _TD_MON)


def vts_068_vol_curve_curvature(close: pd.Series) -> pd.Series:
    """Vol-curve curvature: (rv63/rv21) - (rv252/rv63), second-difference shape."""
    rv21 = _realized_vol(close, _TD_MON).clip(lower=_EPS)
    rv63 = _realized_vol(close, _TD_QTR).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    return (rv63 / rv21) - (rv252 / rv63)


def vts_069_vol_curve_butterfly(close: pd.Series) -> pd.Series:
    """Vol-curve butterfly: 2*rv63 - rv21 - rv252 (midpoint deviation)."""
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv252 = _realized_vol(close, _TD_YEAR)
    return 2.0 * rv63 - rv21 - rv252


def vts_070_vol_4pt_slope(close: pd.Series) -> pd.Series:
    """OLS slope across 4 log-horizon points: log(rv5), log(rv21), log(rv63), log(rv252)."""
    rv5 = np.log(_realized_vol(close, _TD_WEEK).clip(lower=_EPS))
    rv21 = np.log(_realized_vol(close, _TD_MON).clip(lower=_EPS))
    rv63 = np.log(_realized_vol(close, _TD_QTR).clip(lower=_EPS))
    rv252 = np.log(_realized_vol(close, _TD_YEAR).clip(lower=_EPS))
    x = np.array([np.log(_TD_WEEK), np.log(_TD_MON), np.log(_TD_QTR), np.log(_TD_YEAR)])
    x_m = x.mean()
    den = ((x - x_m) ** 2).sum()
    df = pd.concat([rv5, rv21, rv63, rv252], axis=1)
    def _row_slope(row):
        y = row.values.astype(float)
        if np.any(np.isnan(y)):
            return np.nan
        return ((x - x_m) * (y - y.mean())).sum() / den
    return df.apply(_row_slope, axis=1)


def vts_071_rv5d_relative_to_rv252d_cone(close: pd.Series) -> pd.Series:
    """5d RV as fraction of 252d max of 5d RV (position in 252d vol cone)."""
    rv = _realized_vol(close, _TD_WEEK)
    cone_top = _rolling_max(rv, _TD_YEAR)
    return _safe_div(rv, cone_top.clip(lower=_EPS))


def vts_072_rv21d_relative_to_rv252d_cone(close: pd.Series) -> pd.Series:
    """21d RV as fraction of 252d max of 21d RV (monthly cone position)."""
    rv = _realized_vol(close, _TD_MON)
    cone_top = _rolling_max(rv, _TD_YEAR)
    return _safe_div(rv, cone_top.clip(lower=_EPS))


def vts_073_rv5d_vs_rv21d_min_ratio(close: pd.Series) -> pd.Series:
    """5d RV / 252d minimum of 5d RV (how far above the bottom of the vol cone)."""
    rv = _realized_vol(close, _TD_WEEK)
    cone_bot = _rolling_min(rv, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(rv, cone_bot)


def vts_074_rv_term_spread_sum(close: pd.Series) -> pd.Series:
    """Sum of all three tier spreads: (rv5-rv21)+(rv21-rv63)+(rv63-rv252) = rv5-rv252."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv252 = _realized_vol(close, _TD_YEAR)
    return rv5 - rv252


def vts_075_vol_term_structure_skewness(close: pd.Series) -> pd.Series:
    """Skewness proxy: (rv5-rv21)/rv21 minus (rv63-rv252)/rv252 — curvature sign."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv21 = _realized_vol(close, _TD_MON).clip(lower=_EPS)
    rv63 = _realized_vol(close, _TD_QTR).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    short_slope = (rv5 - rv21) / rv21
    long_slope = (rv63 - rv252) / rv252
    return short_slope - long_slope


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_TERM_STRUCTURE_REGISTRY_001_075 = {
    "vts_001_rv5d": {"inputs": ["close"], "func": vts_001_rv5d},
    "vts_002_rv21d": {"inputs": ["close"], "func": vts_002_rv21d},
    "vts_003_rv63d": {"inputs": ["close"], "func": vts_003_rv63d},
    "vts_004_rv126d": {"inputs": ["close"], "func": vts_004_rv126d},
    "vts_005_rv252d": {"inputs": ["close"], "func": vts_005_rv252d},
    "vts_006_rv10d": {"inputs": ["close"], "func": vts_006_rv10d},
    "vts_007_rv15d": {"inputs": ["close"], "func": vts_007_rv15d},
    "vts_008_rv30d": {"inputs": ["close"], "func": vts_008_rv30d},
    "vts_009_rv42d": {"inputs": ["close"], "func": vts_009_rv42d},
    "vts_010_rv2d": {"inputs": ["close"], "func": vts_010_rv2d},
    "vts_011_rv3d": {"inputs": ["close"], "func": vts_011_rv3d},
    "vts_012_rv7d": {"inputs": ["close"], "func": vts_012_rv7d},
    "vts_013_rv189d": {"inputs": ["close"], "func": vts_013_rv189d},
    "vts_014_rv84d": {"inputs": ["close"], "func": vts_014_rv84d},
    "vts_015_rv105d": {"inputs": ["close"], "func": vts_015_rv105d},
    "vts_016_rv5d_rv21d_ratio": {"inputs": ["close"], "func": vts_016_rv5d_rv21d_ratio},
    "vts_017_rv21d_rv63d_ratio": {"inputs": ["close"], "func": vts_017_rv21d_rv63d_ratio},
    "vts_018_rv63d_rv252d_ratio": {"inputs": ["close"], "func": vts_018_rv63d_rv252d_ratio},
    "vts_019_rv5d_rv63d_ratio": {"inputs": ["close"], "func": vts_019_rv5d_rv63d_ratio},
    "vts_020_rv5d_rv252d_ratio": {"inputs": ["close"], "func": vts_020_rv5d_rv252d_ratio},
    "vts_021_rv21d_rv252d_ratio": {"inputs": ["close"], "func": vts_021_rv21d_rv252d_ratio},
    "vts_022_rv10d_rv21d_ratio": {"inputs": ["close"], "func": vts_022_rv10d_rv21d_ratio},
    "vts_023_rv10d_rv63d_ratio": {"inputs": ["close"], "func": vts_023_rv10d_rv63d_ratio},
    "vts_024_rv21d_rv126d_ratio": {"inputs": ["close"], "func": vts_024_rv21d_rv126d_ratio},
    "vts_025_rv63d_rv126d_ratio": {"inputs": ["close"], "func": vts_025_rv63d_rv126d_ratio},
    "vts_026_rv126d_rv252d_ratio": {"inputs": ["close"], "func": vts_026_rv126d_rv252d_ratio},
    "vts_027_rv5d_rv126d_ratio": {"inputs": ["close"], "func": vts_027_rv5d_rv126d_ratio},
    "vts_028_rv3d_rv21d_ratio": {"inputs": ["close"], "func": vts_028_rv3d_rv21d_ratio},
    "vts_029_rv7d_rv63d_ratio": {"inputs": ["close"], "func": vts_029_rv7d_rv63d_ratio},
    "vts_030_rv30d_rv252d_ratio": {"inputs": ["close"], "func": vts_030_rv30d_rv252d_ratio},
    "vts_031_rv5d_rv21d_spread": {"inputs": ["close"], "func": vts_031_rv5d_rv21d_spread},
    "vts_032_rv21d_rv63d_spread": {"inputs": ["close"], "func": vts_032_rv21d_rv63d_spread},
    "vts_033_rv63d_rv252d_spread": {"inputs": ["close"], "func": vts_033_rv63d_rv252d_spread},
    "vts_034_rv5d_rv63d_spread": {"inputs": ["close"], "func": vts_034_rv5d_rv63d_spread},
    "vts_035_rv5d_rv252d_spread": {"inputs": ["close"], "func": vts_035_rv5d_rv252d_spread},
    "vts_036_rv10d_rv63d_spread": {"inputs": ["close"], "func": vts_036_rv10d_rv63d_spread},
    "vts_037_rv21d_rv252d_spread": {"inputs": ["close"], "func": vts_037_rv21d_rv252d_spread},
    "vts_038_rv21d_rv126d_spread": {"inputs": ["close"], "func": vts_038_rv21d_rv126d_spread},
    "vts_039_rv63d_rv126d_spread": {"inputs": ["close"], "func": vts_039_rv63d_rv126d_spread},
    "vts_040_rv126d_rv252d_spread": {"inputs": ["close"], "func": vts_040_rv126d_rv252d_spread},
    "vts_041_rv3d_rv63d_spread": {"inputs": ["close"], "func": vts_041_rv3d_rv63d_spread},
    "vts_042_rv7d_rv21d_spread": {"inputs": ["close"], "func": vts_042_rv7d_rv21d_spread},
    "vts_043_rv30d_rv126d_spread": {"inputs": ["close"], "func": vts_043_rv30d_rv126d_spread},
    "vts_044_rv42d_rv252d_spread": {"inputs": ["close"], "func": vts_044_rv42d_rv252d_spread},
    "vts_045_rv5d_rv126d_spread": {"inputs": ["close"], "func": vts_045_rv5d_rv126d_spread},
    "vts_046_ts_inversion_5d21d_flag": {"inputs": ["close"], "func": vts_046_ts_inversion_5d21d_flag},
    "vts_047_ts_inversion_21d63d_flag": {"inputs": ["close"], "func": vts_047_ts_inversion_21d63d_flag},
    "vts_048_ts_inversion_63d252d_flag": {"inputs": ["close"], "func": vts_048_ts_inversion_63d252d_flag},
    "vts_049_ts_full_inversion_flag": {"inputs": ["close"], "func": vts_049_ts_full_inversion_flag},
    "vts_050_consec_days_5d21d_inverted": {"inputs": ["close"], "func": vts_050_consec_days_5d21d_inverted},
    "vts_051_consec_days_21d63d_inverted": {"inputs": ["close"], "func": vts_051_consec_days_21d63d_inverted},
    "vts_052_consec_days_63d252d_inverted": {"inputs": ["close"], "func": vts_052_consec_days_63d252d_inverted},
    "vts_053_consec_days_full_inversion": {"inputs": ["close"], "func": vts_053_consec_days_full_inversion},
    "vts_054_ts_inversion_5d63d_flag": {"inputs": ["close"], "func": vts_054_ts_inversion_5d63d_flag},
    "vts_055_ts_inversion_5d252d_flag": {"inputs": ["close"], "func": vts_055_ts_inversion_5d252d_flag},
    "vts_056_rv5d_pct_rank_252d": {"inputs": ["close"], "func": vts_056_rv5d_pct_rank_252d},
    "vts_057_rv21d_pct_rank_252d": {"inputs": ["close"], "func": vts_057_rv21d_pct_rank_252d},
    "vts_058_rv63d_pct_rank_252d": {"inputs": ["close"], "func": vts_058_rv63d_pct_rank_252d},
    "vts_059_rv252d_pct_rank_expanding": {"inputs": ["close"], "func": vts_059_rv252d_pct_rank_expanding},
    "vts_060_rv5d_ratio_pct_rank_252d": {"inputs": ["close"], "func": vts_060_rv5d_ratio_pct_rank_252d},
    "vts_061_rv21d_ratio_pct_rank_252d": {"inputs": ["close"], "func": vts_061_rv21d_ratio_pct_rank_252d},
    "vts_062_rv5d_zscore_252d": {"inputs": ["close"], "func": vts_062_rv5d_zscore_252d},
    "vts_063_rv21d_zscore_252d": {"inputs": ["close"], "func": vts_063_rv21d_zscore_252d},
    "vts_064_rv63d_zscore_252d": {"inputs": ["close"], "func": vts_064_rv63d_zscore_252d},
    "vts_065_rv252d_zscore_expanding": {"inputs": ["close"], "func": vts_065_rv252d_zscore_expanding},
    "vts_066_vol_curve_slope_5d_252d": {"inputs": ["close"], "func": vts_066_vol_curve_slope_5d_252d},
    "vts_067_vol_curve_slope_21d_252d": {"inputs": ["close"], "func": vts_067_vol_curve_slope_21d_252d},
    "vts_068_vol_curve_curvature": {"inputs": ["close"], "func": vts_068_vol_curve_curvature},
    "vts_069_vol_curve_butterfly": {"inputs": ["close"], "func": vts_069_vol_curve_butterfly},
    "vts_070_vol_4pt_slope": {"inputs": ["close"], "func": vts_070_vol_4pt_slope},
    "vts_071_rv5d_relative_to_rv252d_cone": {"inputs": ["close"], "func": vts_071_rv5d_relative_to_rv252d_cone},
    "vts_072_rv21d_relative_to_rv252d_cone": {"inputs": ["close"], "func": vts_072_rv21d_relative_to_rv252d_cone},
    "vts_073_rv5d_vs_rv21d_min_ratio": {"inputs": ["close"], "func": vts_073_rv5d_vs_rv21d_min_ratio},
    "vts_074_rv_term_spread_sum": {"inputs": ["close"], "func": vts_074_rv_term_spread_sum},
    "vts_075_vol_term_structure_skewness": {"inputs": ["close"], "func": vts_075_vol_term_structure_skewness},
}
