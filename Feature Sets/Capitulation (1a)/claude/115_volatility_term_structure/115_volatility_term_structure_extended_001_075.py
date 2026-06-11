"""
115_volatility_term_structure — Extended Features 001-075
Domain: term structure of realized volatility — deeper variants including GARCH-like
        vol term structure, Yang-Zhang OHLC estimator horizons, overnight/intraday vol
        term splits, regime-conditional vol curves, vol cone percentile at multiple
        horizons, realized skewness/kurtosis cross-horizon term structure, multi-scale
        volatility momentum, vol-curve anomaly flags for capitulation detection.
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility (std of log-returns) over w days."""
    lr = np.log(close / close.shift(1))
    rv = lr.rolling(w, min_periods=max(2, w // 2)).std()
    return rv * np.sqrt(_TD_YEAR)


def _parkinson_vol(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Parkinson high-low range estimator, annualized."""
    hl2 = np.log(high / low.clip(lower=_EPS)) ** 2
    pk = np.sqrt(hl2.rolling(w, min_periods=max(2, w // 2)).mean() / (4.0 * np.log(2.0)))
    return pk * np.sqrt(_TD_YEAR)


def _yang_zhang_vol(open_: pd.Series, high: pd.Series,
                    low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Yang-Zhang OHLC volatility estimator, annualized."""
    k = 0.34 / (1.34 + (w + 1) / max(w - 1, 1))
    oc = np.log(open_ / close.shift(1).clip(lower=_EPS))
    co = np.log(close / open_.clip(lower=_EPS))
    hl = np.log(high / low.clip(lower=_EPS))
    ho = np.log(high / open_.clip(lower=_EPS))
    lo = np.log(low / open_.clip(lower=_EPS))
    oc_var = oc.rolling(w, min_periods=max(2, w // 2)).var()
    co_var = co.rolling(w, min_periods=max(2, w // 2)).var()
    rs = (ho * (ho - co) + lo * (lo - co)).rolling(w, min_periods=max(2, w // 2)).mean()
    yz = np.sqrt((oc_var + k * co_var + (1 - k) * rs.clip(lower=0)).clip(lower=0))
    return yz * np.sqrt(_TD_YEAR)


def _overnight_vol(open_: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Overnight (close-to-open) log-return volatility, annualized."""
    overnight = np.log(open_ / close.shift(1).clip(lower=_EPS))
    return overnight.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(_TD_YEAR)


def _intraday_vol(open_: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Intraday (open-to-close) log-return volatility, annualized."""
    intraday = np.log(close / open_.clip(lower=_EPS))
    return intraday.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(_TD_YEAR)


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


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-015): Yang-Zhang multi-horizon term structure ---

def vts_ext_001_yz_rv5d(open_: pd.Series, high: pd.Series,
                         low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang 5-day realized vol, annualized."""
    return _yang_zhang_vol(open_, high, low, close, _TD_WEEK)


def vts_ext_002_yz_rv21d(open_: pd.Series, high: pd.Series,
                          low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang 21-day realized vol, annualized."""
    return _yang_zhang_vol(open_, high, low, close, _TD_MON)


def vts_ext_003_yz_rv63d(open_: pd.Series, high: pd.Series,
                          low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang 63-day realized vol, annualized."""
    return _yang_zhang_vol(open_, high, low, close, _TD_QTR)


def vts_ext_004_yz_rv252d(open_: pd.Series, high: pd.Series,
                           low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang 252-day realized vol, annualized."""
    return _yang_zhang_vol(open_, high, low, close, _TD_YEAR)


def vts_ext_005_yz_rv5d_rv21d_ratio(open_: pd.Series, high: pd.Series,
                                     low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of YZ 5d to YZ 21d vol (YZ-based term structure short/mid)."""
    return _safe_div(_yang_zhang_vol(open_, high, low, close, _TD_WEEK),
                     _yang_zhang_vol(open_, high, low, close, _TD_MON))


def vts_ext_006_yz_rv21d_rv63d_ratio(open_: pd.Series, high: pd.Series,
                                      low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of YZ 21d to YZ 63d vol."""
    return _safe_div(_yang_zhang_vol(open_, high, low, close, _TD_MON),
                     _yang_zhang_vol(open_, high, low, close, _TD_QTR))


def vts_ext_007_yz_rv63d_rv252d_ratio(open_: pd.Series, high: pd.Series,
                                       low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of YZ 63d to YZ 252d vol."""
    return _safe_div(_yang_zhang_vol(open_, high, low, close, _TD_QTR),
                     _yang_zhang_vol(open_, high, low, close, _TD_YEAR))


def vts_ext_008_yz_ts_inversion_5d21d_flag(open_: pd.Series, high: pd.Series,
                                            low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: YZ 5d vol > YZ 21d vol (OHLC-based short-end inversion)."""
    return (_yang_zhang_vol(open_, high, low, close, _TD_WEEK)
            > _yang_zhang_vol(open_, high, low, close, _TD_MON)).astype(float)


def vts_ext_009_yz_rv5d_rv252d_ratio(open_: pd.Series, high: pd.Series,
                                      low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of YZ 5d to YZ 252d vol (widest YZ term spread)."""
    return _safe_div(_yang_zhang_vol(open_, high, low, close, _TD_WEEK),
                     _yang_zhang_vol(open_, high, low, close, _TD_YEAR))


def vts_ext_010_yz_rv5d_rv21d_spread(open_: pd.Series, high: pd.Series,
                                      low: pd.Series, close: pd.Series) -> pd.Series:
    """YZ 5d RV minus YZ 21d RV (absolute short-end YZ spread)."""
    return (_yang_zhang_vol(open_, high, low, close, _TD_WEEK)
            - _yang_zhang_vol(open_, high, low, close, _TD_MON))


def vts_ext_011_yz_rv5d_pct_rank_252d(open_: pd.Series, high: pd.Series,
                                       low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of YZ 5d vol within 252-day distribution."""
    rv = _yang_zhang_vol(open_, high, low, close, _TD_WEEK)
    return rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_ext_012_yz_rv21d_zscore_252d(open_: pd.Series, high: pd.Series,
                                      low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of YZ 21d vol vs its 252-day distribution."""
    rv = _yang_zhang_vol(open_, high, low, close, _TD_MON)
    return _safe_div(rv - _rolling_mean(rv, _TD_YEAR), _rolling_std(rv, _TD_YEAR))


def vts_ext_013_yz_full_inversion_flag(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: YZ full term-structure inversion (5d>21d>63d>252d)."""
    y5 = _yang_zhang_vol(open_, high, low, close, _TD_WEEK)
    y21 = _yang_zhang_vol(open_, high, low, close, _TD_MON)
    y63 = _yang_zhang_vol(open_, high, low, close, _TD_QTR)
    y252 = _yang_zhang_vol(open_, high, low, close, _TD_YEAR)
    return ((y5 > y21) & (y21 > y63) & (y63 > y252)).astype(float)


def vts_ext_014_yz_curve_curvature(open_: pd.Series, high: pd.Series,
                                    low: pd.Series, close: pd.Series) -> pd.Series:
    """YZ vol-curve curvature: (yz63/yz21)-(yz252/yz63)."""
    y21 = _yang_zhang_vol(open_, high, low, close, _TD_MON).clip(lower=_EPS)
    y63 = _yang_zhang_vol(open_, high, low, close, _TD_QTR).clip(lower=_EPS)
    y252 = _yang_zhang_vol(open_, high, low, close, _TD_YEAR).clip(lower=_EPS)
    return (y63 / y21) - (y252 / y63)


def vts_ext_015_yz_rv5d_rv21d_ratio_5d_diff(open_: pd.Series, high: pd.Series,
                                              low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of YZ 5d/21d ratio (velocity of YZ short-end tilt)."""
    ratio = _safe_div(_yang_zhang_vol(open_, high, low, close, _TD_WEEK),
                      _yang_zhang_vol(open_, high, low, close, _TD_MON))
    return ratio.diff(_TD_WEEK)


# --- Group B (016-030): Overnight vs intraday vol term structure ---

def vts_ext_016_overnight_rv5d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight 5-day vol, annualized."""
    return _overnight_vol(open_, close, _TD_WEEK)


def vts_ext_017_overnight_rv21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight 21-day vol, annualized."""
    return _overnight_vol(open_, close, _TD_MON)


def vts_ext_018_overnight_rv63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight 63-day vol, annualized."""
    return _overnight_vol(open_, close, _TD_QTR)


def vts_ext_019_intraday_rv5d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday (open-to-close) 5-day vol, annualized."""
    return _intraday_vol(open_, close, _TD_WEEK)


def vts_ext_020_intraday_rv21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday 21-day vol, annualized."""
    return _intraday_vol(open_, close, _TD_MON)


def vts_ext_021_intraday_rv63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday 63-day vol, annualized."""
    return _intraday_vol(open_, close, _TD_QTR)


def vts_ext_022_overnight_intraday_rv5d_ratio(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of overnight 5d vol to intraday 5d vol (overnight stress fraction)."""
    return _safe_div(_overnight_vol(open_, close, _TD_WEEK),
                     _intraday_vol(open_, close, _TD_WEEK))


def vts_ext_023_overnight_intraday_rv21d_ratio(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of overnight 21d vol to intraday 21d vol."""
    return _safe_div(_overnight_vol(open_, close, _TD_MON),
                     _intraday_vol(open_, close, _TD_MON))


def vts_ext_024_overnight_rv5d_rv21d_ratio(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of overnight 5d to overnight 21d vol (overnight-only term structure)."""
    return _safe_div(_overnight_vol(open_, close, _TD_WEEK),
                     _overnight_vol(open_, close, _TD_MON))


def vts_ext_025_intraday_rv5d_rv63d_ratio(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of intraday 5d to intraday 63d vol (intraday-only term structure)."""
    return _safe_div(_intraday_vol(open_, close, _TD_WEEK),
                     _intraday_vol(open_, close, _TD_QTR))


def vts_ext_026_overnight_ts_inversion_flag(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: overnight 5d > overnight 21d vol."""
    return (_overnight_vol(open_, close, _TD_WEEK)
            > _overnight_vol(open_, close, _TD_MON)).astype(float)


def vts_ext_027_intraday_ts_inversion_flag(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: intraday 5d > intraday 21d vol."""
    return (_intraday_vol(open_, close, _TD_WEEK)
            > _intraday_vol(open_, close, _TD_MON)).astype(float)


def vts_ext_028_overnight_rv5d_zscore_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of overnight 5d vol vs 252-day distribution."""
    rv = _overnight_vol(open_, close, _TD_WEEK)
    return _safe_div(rv - _rolling_mean(rv, _TD_YEAR), _rolling_std(rv, _TD_YEAR))


def vts_ext_029_overnight_intraday_spread_5d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight 5d vol minus intraday 5d vol (absolute overnight premium)."""
    return _overnight_vol(open_, close, _TD_WEEK) - _intraday_vol(open_, close, _TD_WEEK)


def vts_ext_030_overnight_intraday_spread_pct_rank_252d(open_: pd.Series,
                                                         close: pd.Series) -> pd.Series:
    """Percentile rank of overnight-minus-intraday 5d spread within 252-day history."""
    spread = (_overnight_vol(open_, close, _TD_WEEK)
              - _intraday_vol(open_, close, _TD_WEEK))
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (031-045): Realized higher-moment term structure ---

def vts_ext_031_realized_skew_5d(close: pd.Series) -> pd.Series:
    """Rolling 5-day realized skewness of log-returns."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(_TD_WEEK, min_periods=max(3, _TD_WEEK // 2)).skew()


def vts_ext_032_realized_skew_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day realized skewness of log-returns."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()


def vts_ext_033_realized_skew_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day realized skewness of log-returns."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def vts_ext_034_realized_kurt_5d(close: pd.Series) -> pd.Series:
    """Rolling 5-day realized kurtosis of log-returns (fat-tail indicator)."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(_TD_WEEK, min_periods=max(4, _TD_WEEK // 2)).kurt()


def vts_ext_035_realized_kurt_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day realized kurtosis of log-returns."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).kurt()


def vts_ext_036_realized_kurt_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day realized kurtosis of log-returns."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def vts_ext_037_skew_term_slope(close: pd.Series) -> pd.Series:
    """Skew term-structure slope: skew_5d minus skew_63d (short minus long horizon)."""
    lr = np.log(close / close.shift(1))
    sk5 = lr.rolling(_TD_WEEK, min_periods=max(3, _TD_WEEK // 2)).skew()
    sk63 = lr.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    return sk5 - sk63


def vts_ext_038_kurt_term_slope(close: pd.Series) -> pd.Series:
    """Kurtosis term-structure slope: kurt_5d minus kurt_63d."""
    lr = np.log(close / close.shift(1))
    k5 = lr.rolling(_TD_WEEK, min_periods=max(4, _TD_WEEK // 2)).kurt()
    k63 = lr.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()
    return k5 - k63


def vts_ext_039_downside_rv5d(close: pd.Series) -> pd.Series:
    """Downside-only 5-day realized vol (std of negative log-returns only)."""
    lr = np.log(close / close.shift(1))
    neg_lr = lr.where(lr < 0, 0.0)
    return neg_lr.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).std() * np.sqrt(_TD_YEAR)


def vts_ext_040_downside_rv21d(close: pd.Series) -> pd.Series:
    """Downside-only 21-day realized vol."""
    lr = np.log(close / close.shift(1))
    neg_lr = lr.where(lr < 0, 0.0)
    return neg_lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std() * np.sqrt(_TD_YEAR)


def vts_ext_041_downside_rv5d_rv21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of downside 5d vol to downside 21d vol."""
    lr = np.log(close / close.shift(1))
    neg_lr = lr.where(lr < 0, 0.0)
    ds5 = neg_lr.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).std()
    ds21 = neg_lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    return _safe_div(ds5, ds21)


def vts_ext_042_downside_rv5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of downside 5d vol vs 252-day distribution."""
    lr = np.log(close / close.shift(1))
    neg_lr = lr.where(lr < 0, 0.0)
    ds5 = neg_lr.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).std() * np.sqrt(_TD_YEAR)
    return _safe_div(ds5 - _rolling_mean(ds5, _TD_YEAR), _rolling_std(ds5, _TD_YEAR))


def vts_ext_043_updown_vol_ratio_5d(close: pd.Series) -> pd.Series:
    """Ratio of upside vol to downside vol over 5 days (vol asymmetry short-term)."""
    lr = np.log(close / close.shift(1))
    pos_lr = lr.where(lr > 0, 0.0)
    neg_lr = lr.where(lr < 0, 0.0)
    up5 = pos_lr.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).std() + _EPS
    dn5 = neg_lr.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).std() + _EPS
    return up5 / dn5


def vts_ext_044_updown_vol_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of upside vol to downside vol over 21 days."""
    lr = np.log(close / close.shift(1))
    pos_lr = lr.where(lr > 0, 0.0)
    neg_lr = lr.where(lr < 0, 0.0)
    up21 = pos_lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std() + _EPS
    dn21 = neg_lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std() + _EPS
    return up21 / dn21


def vts_ext_045_updown_vol_ratio_term_slope(close: pd.Series) -> pd.Series:
    """Change in up/down vol ratio from 21d to 5d horizon (short-run asymmetry shift)."""
    lr = np.log(close / close.shift(1))
    pos_lr = lr.where(lr > 0, 0.0)
    neg_lr = lr.where(lr < 0, 0.0)
    up5 = pos_lr.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).std() + _EPS
    dn5 = neg_lr.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).std() + _EPS
    up21 = pos_lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std() + _EPS
    dn21 = neg_lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std() + _EPS
    return (up5 / dn5) - (up21 / dn21)


# --- Group D (046-060): Vol cone multi-horizon percentile ranks & regime flags ---

def vts_ext_046_rv5d_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d RV within 63-day distribution (short-window cone)."""
    rv = _realized_vol(close, _TD_WEEK)
    return rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vts_ext_047_rv21d_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d RV within 63-day distribution."""
    rv = _realized_vol(close, _TD_MON)
    return rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vts_ext_048_rv63d_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d RV within 126-day distribution."""
    rv = _realized_vol(close, _TD_QTR)
    return rv.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def vts_ext_049_rv126d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 126d RV within 252-day distribution."""
    rv = _realized_vol(close, _TD_HALF)
    return rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_ext_050_rv5d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """All-time expanding percentile rank of 5d RV (absolute cone position)."""
    rv = _realized_vol(close, _TD_WEEK)
    return rv.expanding(min_periods=_TD_WEEK).rank(pct=True)


def vts_ext_051_rv21d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """All-time expanding percentile rank of 21d RV."""
    rv = _realized_vol(close, _TD_MON)
    return rv.expanding(min_periods=_TD_MON).rank(pct=True)


def vts_ext_052_vol_regime_high_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 5d RV > 2x 252d mean of 5d RV (high-vol regime indicator)."""
    rv = _realized_vol(close, _TD_WEEK)
    threshold = 2.0 * _rolling_mean(rv, _TD_YEAR)
    return (rv > threshold).astype(float)


def vts_ext_053_vol_regime_extreme_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 5d RV > 3x 252d mean of 5d RV (extreme vol regime)."""
    rv = _realized_vol(close, _TD_WEEK)
    threshold = 3.0 * _rolling_mean(rv, _TD_YEAR)
    return (rv > threshold).astype(float)


def vts_ext_054_vol_ts_stress_score(close: pd.Series) -> pd.Series:
    """Composite stress score: sum of inversion flags (5d>21d) + (21d>63d) + (63d>252d)."""
    r5 = _realized_vol(close, _TD_WEEK)
    r21 = _realized_vol(close, _TD_MON)
    r63 = _realized_vol(close, _TD_QTR)
    r252 = _realized_vol(close, _TD_YEAR)
    return ((r5 > r21).astype(float)
            + (r21 > r63).astype(float)
            + (r63 > r252).astype(float))


def vts_ext_055_rv5d_cone_expansion_rate(close: pd.Series) -> pd.Series:
    """5-day change in 5d RV pct-rank within 252d distribution (cone expansion speed)."""
    rv = _realized_vol(close, _TD_WEEK)
    pct = rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return pct.diff(_TD_WEEK)


def vts_ext_056_rv5d_rv252d_cone_gap(close: pd.Series) -> pd.Series:
    """Pct-rank gap: 5d RV rank minus 252d RV rank within 252d window."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv252 = _realized_vol(close, _TD_YEAR)
    r5 = rv5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r252 = rv252.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return r5 - r252


def vts_ext_057_rv_cone_steepness(close: pd.Series) -> pd.Series:
    """Cone steepness: max percentile rank minus min rank across 5d/21d/63d/252d."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv252 = _realized_vol(close, _TD_YEAR)
    r5 = rv5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r21 = rv21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r63 = rv63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r252 = rv252.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    df = pd.concat([r5, r21, r63, r252], axis=1)
    return df.max(axis=1) - df.min(axis=1)


def vts_ext_058_consec_high_vol_regime_days(close: pd.Series) -> pd.Series:
    """Consecutive days 5d RV > 252d mean of 5d RV (high-vol streak)."""
    rv = _realized_vol(close, _TD_WEEK)
    mean_rv = _rolling_mean(rv, _TD_YEAR)
    return _consec_streak(rv > mean_rv)


def vts_ext_059_consec_extreme_vol_days(close: pd.Series) -> pd.Series:
    """Consecutive days 5d RV > 2x 252d mean (extreme vol streak)."""
    rv = _realized_vol(close, _TD_WEEK)
    threshold = 2.0 * _rolling_mean(rv, _TD_YEAR)
    return _consec_streak(rv > threshold)


def vts_ext_060_rv5d_rv21d_ratio_regime_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 5d/21d ratio relative to 252-day distribution, clipped at ±5."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    z = _safe_div(ratio - _rolling_mean(ratio, _TD_YEAR), _rolling_std(ratio, _TD_YEAR))
    return z.clip(-5.0, 5.0)


# --- Group E (061-075): Multi-scale vol momentum and cross-horizon divergence ---

def vts_ext_061_rv5d_momentum_21d(close: pd.Series) -> pd.Series:
    """21-day log-ratio of 5d RV to its 21-day lagged value (vol momentum)."""
    rv = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    return np.log(rv / rv.shift(_TD_MON))


def vts_ext_062_rv21d_momentum_63d(close: pd.Series) -> pd.Series:
    """63-day log-ratio of 21d RV to its 63-day lagged value."""
    rv = _realized_vol(close, _TD_MON).clip(lower=_EPS)
    return np.log(rv / rv.shift(_TD_QTR))


def vts_ext_063_rv5d_rv252d_momentum_divergence(close: pd.Series) -> pd.Series:
    """21-day change in 5d RV minus 21-day change in 252d RV (cross-horizon divergence)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv252 = _realized_vol(close, _TD_YEAR)
    return rv5.diff(_TD_MON) - rv252.diff(_TD_MON)


def vts_ext_064_vol_slope_momentum_21d(close: pd.Series) -> pd.Series:
    """21-day change in log-linear vol curve slope (how fast curve is steepening)."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    slope = np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)
    return slope.diff(_TD_MON)


def vts_ext_065_rv5d_rv21d_ratio_momentum(close: pd.Series) -> pd.Series:
    """21-day change in 5d/21d ratio (how fast short-end tilt is changing)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    return ratio.diff(_TD_MON)


def vts_ext_066_cross_horizon_vol_dispersion(close: pd.Series) -> pd.Series:
    """Std across 5 horizons: std(rv5,rv21,rv63,rv126,rv252) row-wise."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv126 = _realized_vol(close, _TD_HALF)
    rv252 = _realized_vol(close, _TD_YEAR)
    df = pd.concat([rv5, rv21, rv63, rv126, rv252], axis=1)
    return df.std(axis=1)


def vts_ext_067_vol_dispersion_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of cross-horizon vol dispersion within 252-day history."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv126 = _realized_vol(close, _TD_HALF)
    rv252 = _realized_vol(close, _TD_YEAR)
    df = pd.concat([rv5, rv21, rv63, rv126, rv252], axis=1)
    disp = df.std(axis=1)
    return disp.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_ext_068_rv5d_vs_rv21d_garch_like_ratio(close: pd.Series) -> pd.Series:
    """EWM-vol(span=5) / EWM-vol(span=21) normalized by 252d mean of that ratio."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s5 = np.sqrt(_ewm_mean(lr2, _TD_WEEK)) + _EPS
    s21 = np.sqrt(_ewm_mean(lr2, _TD_MON)) + _EPS
    ratio = s5 / s21
    mean_ratio = _rolling_mean(ratio, _TD_YEAR).clip(lower=_EPS)
    return ratio / mean_ratio


def vts_ext_069_pk_vs_close_rv_ratio_5d(high: pd.Series, low: pd.Series,
                                         close: pd.Series) -> pd.Series:
    """Ratio of Parkinson 5d vol to close-only 5d RV (range vs close estimator ratio)."""
    return _safe_div(_parkinson_vol(high, low, _TD_WEEK),
                     _realized_vol(close, _TD_WEEK))


def vts_ext_070_pk_vs_close_rv_ratio_21d(high: pd.Series, low: pd.Series,
                                          close: pd.Series) -> pd.Series:
    """Ratio of Parkinson 21d vol to close-only 21d RV."""
    return _safe_div(_parkinson_vol(high, low, _TD_MON),
                     _realized_vol(close, _TD_MON))


def vts_ext_071_pk_vs_close_ratio_term_slope(high: pd.Series, low: pd.Series,
                                              close: pd.Series) -> pd.Series:
    """Slope of PK/close-RV ratio from 5d to 21d (range vs close divergence curve)."""
    r5 = _safe_div(_parkinson_vol(high, low, _TD_WEEK),
                   _realized_vol(close, _TD_WEEK))
    r21 = _safe_div(_parkinson_vol(high, low, _TD_MON),
                    _realized_vol(close, _TD_MON))
    return r5 - r21


def vts_ext_072_vol_ts_inversion_score_pct_rank(close: pd.Series) -> pd.Series:
    """21-day rolling mean of term-structure inversion score percentile-ranked in 252d."""
    r5 = _realized_vol(close, _TD_WEEK)
    r21 = _realized_vol(close, _TD_MON)
    r63 = _realized_vol(close, _TD_QTR)
    r252 = _realized_vol(close, _TD_YEAR)
    score = ((r5 > r21).astype(float)
             + (r21 > r63).astype(float)
             + (r63 > r252).astype(float))
    smoothed = _rolling_mean(score, _TD_MON)
    return smoothed.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_ext_073_vol_curve_flatness(close: pd.Series) -> pd.Series:
    """Flatness metric: 1 minus std of (rv5,rv21,rv63,rv252) / mean of those."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv252 = _realized_vol(close, _TD_YEAR)
    df = pd.concat([rv5, rv21, rv63, rv252], axis=1)
    cv = _safe_div(df.std(axis=1), df.mean(axis=1).clip(lower=_EPS))
    return 1.0 - cv.clip(0.0, 2.0)


def vts_ext_074_rv5d_long_run_ratio(close: pd.Series) -> pd.Series:
    """5d RV divided by 252d expanding mean of 5d RV (deviation from long-run avg)."""
    rv = _realized_vol(close, _TD_WEEK)
    long_mean = rv.expanding(min_periods=_TD_YEAR).mean().clip(lower=_EPS)
    return rv / long_mean


def vts_ext_075_vol_term_structure_capitulation_flag(close: pd.Series) -> pd.Series:
    """Composite binary flag: short vol > 2x long vol AND 5d RV above 90th pct (252d)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv252 = _realized_vol(close, _TD_YEAR)
    pct90 = rv5.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return ((rv5 > 2.0 * rv252) & (rv5 > pct90)).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_TERM_STRUCTURE_EXTENDED_REGISTRY_001_075 = {
    "vts_ext_001_yz_rv5d": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_001_yz_rv5d},
    "vts_ext_002_yz_rv21d": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_002_yz_rv21d},
    "vts_ext_003_yz_rv63d": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_003_yz_rv63d},
    "vts_ext_004_yz_rv252d": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_004_yz_rv252d},
    "vts_ext_005_yz_rv5d_rv21d_ratio": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_005_yz_rv5d_rv21d_ratio},
    "vts_ext_006_yz_rv21d_rv63d_ratio": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_006_yz_rv21d_rv63d_ratio},
    "vts_ext_007_yz_rv63d_rv252d_ratio": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_007_yz_rv63d_rv252d_ratio},
    "vts_ext_008_yz_ts_inversion_5d21d_flag": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_008_yz_ts_inversion_5d21d_flag},
    "vts_ext_009_yz_rv5d_rv252d_ratio": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_009_yz_rv5d_rv252d_ratio},
    "vts_ext_010_yz_rv5d_rv21d_spread": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_010_yz_rv5d_rv21d_spread},
    "vts_ext_011_yz_rv5d_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_011_yz_rv5d_pct_rank_252d},
    "vts_ext_012_yz_rv21d_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_012_yz_rv21d_zscore_252d},
    "vts_ext_013_yz_full_inversion_flag": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_013_yz_full_inversion_flag},
    "vts_ext_014_yz_curve_curvature": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_014_yz_curve_curvature},
    "vts_ext_015_yz_rv5d_rv21d_ratio_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": vts_ext_015_yz_rv5d_rv21d_ratio_5d_diff},
    "vts_ext_016_overnight_rv5d": {"inputs": ["open", "close"], "func": vts_ext_016_overnight_rv5d},
    "vts_ext_017_overnight_rv21d": {"inputs": ["open", "close"], "func": vts_ext_017_overnight_rv21d},
    "vts_ext_018_overnight_rv63d": {"inputs": ["open", "close"], "func": vts_ext_018_overnight_rv63d},
    "vts_ext_019_intraday_rv5d": {"inputs": ["open", "close"], "func": vts_ext_019_intraday_rv5d},
    "vts_ext_020_intraday_rv21d": {"inputs": ["open", "close"], "func": vts_ext_020_intraday_rv21d},
    "vts_ext_021_intraday_rv63d": {"inputs": ["open", "close"], "func": vts_ext_021_intraday_rv63d},
    "vts_ext_022_overnight_intraday_rv5d_ratio": {"inputs": ["open", "close"], "func": vts_ext_022_overnight_intraday_rv5d_ratio},
    "vts_ext_023_overnight_intraday_rv21d_ratio": {"inputs": ["open", "close"], "func": vts_ext_023_overnight_intraday_rv21d_ratio},
    "vts_ext_024_overnight_rv5d_rv21d_ratio": {"inputs": ["open", "close"], "func": vts_ext_024_overnight_rv5d_rv21d_ratio},
    "vts_ext_025_intraday_rv5d_rv63d_ratio": {"inputs": ["open", "close"], "func": vts_ext_025_intraday_rv5d_rv63d_ratio},
    "vts_ext_026_overnight_ts_inversion_flag": {"inputs": ["open", "close"], "func": vts_ext_026_overnight_ts_inversion_flag},
    "vts_ext_027_intraday_ts_inversion_flag": {"inputs": ["open", "close"], "func": vts_ext_027_intraday_ts_inversion_flag},
    "vts_ext_028_overnight_rv5d_zscore_252d": {"inputs": ["open", "close"], "func": vts_ext_028_overnight_rv5d_zscore_252d},
    "vts_ext_029_overnight_intraday_spread_5d": {"inputs": ["open", "close"], "func": vts_ext_029_overnight_intraday_spread_5d},
    "vts_ext_030_overnight_intraday_spread_pct_rank_252d": {"inputs": ["open", "close"], "func": vts_ext_030_overnight_intraday_spread_pct_rank_252d},
    "vts_ext_031_realized_skew_5d": {"inputs": ["close"], "func": vts_ext_031_realized_skew_5d},
    "vts_ext_032_realized_skew_21d": {"inputs": ["close"], "func": vts_ext_032_realized_skew_21d},
    "vts_ext_033_realized_skew_63d": {"inputs": ["close"], "func": vts_ext_033_realized_skew_63d},
    "vts_ext_034_realized_kurt_5d": {"inputs": ["close"], "func": vts_ext_034_realized_kurt_5d},
    "vts_ext_035_realized_kurt_21d": {"inputs": ["close"], "func": vts_ext_035_realized_kurt_21d},
    "vts_ext_036_realized_kurt_63d": {"inputs": ["close"], "func": vts_ext_036_realized_kurt_63d},
    "vts_ext_037_skew_term_slope": {"inputs": ["close"], "func": vts_ext_037_skew_term_slope},
    "vts_ext_038_kurt_term_slope": {"inputs": ["close"], "func": vts_ext_038_kurt_term_slope},
    "vts_ext_039_downside_rv5d": {"inputs": ["close"], "func": vts_ext_039_downside_rv5d},
    "vts_ext_040_downside_rv21d": {"inputs": ["close"], "func": vts_ext_040_downside_rv21d},
    "vts_ext_041_downside_rv5d_rv21d_ratio": {"inputs": ["close"], "func": vts_ext_041_downside_rv5d_rv21d_ratio},
    "vts_ext_042_downside_rv5d_zscore_252d": {"inputs": ["close"], "func": vts_ext_042_downside_rv5d_zscore_252d},
    "vts_ext_043_updown_vol_ratio_5d": {"inputs": ["close"], "func": vts_ext_043_updown_vol_ratio_5d},
    "vts_ext_044_updown_vol_ratio_21d": {"inputs": ["close"], "func": vts_ext_044_updown_vol_ratio_21d},
    "vts_ext_045_updown_vol_ratio_term_slope": {"inputs": ["close"], "func": vts_ext_045_updown_vol_ratio_term_slope},
    "vts_ext_046_rv5d_pct_rank_63d": {"inputs": ["close"], "func": vts_ext_046_rv5d_pct_rank_63d},
    "vts_ext_047_rv21d_pct_rank_63d": {"inputs": ["close"], "func": vts_ext_047_rv21d_pct_rank_63d},
    "vts_ext_048_rv63d_pct_rank_126d": {"inputs": ["close"], "func": vts_ext_048_rv63d_pct_rank_126d},
    "vts_ext_049_rv126d_pct_rank_252d": {"inputs": ["close"], "func": vts_ext_049_rv126d_pct_rank_252d},
    "vts_ext_050_rv5d_expanding_pct_rank": {"inputs": ["close"], "func": vts_ext_050_rv5d_expanding_pct_rank},
    "vts_ext_051_rv21d_expanding_pct_rank": {"inputs": ["close"], "func": vts_ext_051_rv21d_expanding_pct_rank},
    "vts_ext_052_vol_regime_high_flag": {"inputs": ["close"], "func": vts_ext_052_vol_regime_high_flag},
    "vts_ext_053_vol_regime_extreme_flag": {"inputs": ["close"], "func": vts_ext_053_vol_regime_extreme_flag},
    "vts_ext_054_vol_ts_stress_score": {"inputs": ["close"], "func": vts_ext_054_vol_ts_stress_score},
    "vts_ext_055_rv5d_cone_expansion_rate": {"inputs": ["close"], "func": vts_ext_055_rv5d_cone_expansion_rate},
    "vts_ext_056_rv5d_rv252d_cone_gap": {"inputs": ["close"], "func": vts_ext_056_rv5d_rv252d_cone_gap},
    "vts_ext_057_rv_cone_steepness": {"inputs": ["close"], "func": vts_ext_057_rv_cone_steepness},
    "vts_ext_058_consec_high_vol_regime_days": {"inputs": ["close"], "func": vts_ext_058_consec_high_vol_regime_days},
    "vts_ext_059_consec_extreme_vol_days": {"inputs": ["close"], "func": vts_ext_059_consec_extreme_vol_days},
    "vts_ext_060_rv5d_rv21d_ratio_regime_zscore": {"inputs": ["close"], "func": vts_ext_060_rv5d_rv21d_ratio_regime_zscore},
    "vts_ext_061_rv5d_momentum_21d": {"inputs": ["close"], "func": vts_ext_061_rv5d_momentum_21d},
    "vts_ext_062_rv21d_momentum_63d": {"inputs": ["close"], "func": vts_ext_062_rv21d_momentum_63d},
    "vts_ext_063_rv5d_rv252d_momentum_divergence": {"inputs": ["close"], "func": vts_ext_063_rv5d_rv252d_momentum_divergence},
    "vts_ext_064_vol_slope_momentum_21d": {"inputs": ["close"], "func": vts_ext_064_vol_slope_momentum_21d},
    "vts_ext_065_rv5d_rv21d_ratio_momentum": {"inputs": ["close"], "func": vts_ext_065_rv5d_rv21d_ratio_momentum},
    "vts_ext_066_cross_horizon_vol_dispersion": {"inputs": ["close"], "func": vts_ext_066_cross_horizon_vol_dispersion},
    "vts_ext_067_vol_dispersion_pct_rank_252d": {"inputs": ["close"], "func": vts_ext_067_vol_dispersion_pct_rank_252d},
    "vts_ext_068_rv5d_vs_rv21d_garch_like_ratio": {"inputs": ["close"], "func": vts_ext_068_rv5d_vs_rv21d_garch_like_ratio},
    "vts_ext_069_pk_vs_close_rv_ratio_5d": {"inputs": ["high", "low", "close"], "func": vts_ext_069_pk_vs_close_rv_ratio_5d},
    "vts_ext_070_pk_vs_close_rv_ratio_21d": {"inputs": ["high", "low", "close"], "func": vts_ext_070_pk_vs_close_rv_ratio_21d},
    "vts_ext_071_pk_vs_close_ratio_term_slope": {"inputs": ["high", "low", "close"], "func": vts_ext_071_pk_vs_close_ratio_term_slope},
    "vts_ext_072_vol_ts_inversion_score_pct_rank": {"inputs": ["close"], "func": vts_ext_072_vol_ts_inversion_score_pct_rank},
    "vts_ext_073_vol_curve_flatness": {"inputs": ["close"], "func": vts_ext_073_vol_curve_flatness},
    "vts_ext_074_rv5d_long_run_ratio": {"inputs": ["close"], "func": vts_ext_074_rv5d_long_run_ratio},
    "vts_ext_075_vol_term_structure_capitulation_flag": {"inputs": ["close"], "func": vts_ext_075_vol_term_structure_capitulation_flag},
}
