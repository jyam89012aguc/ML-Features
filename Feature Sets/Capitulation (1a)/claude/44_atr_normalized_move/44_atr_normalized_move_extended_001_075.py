"""
44_atr_normalized_move — Extended Features 001-075
Domain: ATR-normalized price moves — deeper variants using ATR7/10/30/42/126 periods,
        multi-day log moves on longer/shorter horizons not yet covered, ATR-unit
        drawdown from all-time and expanding references, open/close wick asymmetries,
        volume-conditioned ATR aggregates, percentile-rank and z-score hybrids,
        and capitulation-specific composite distress signals.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range: max of H-L, |H-prev_C|, |L-prev_C|."""
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low - prev_c).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Rolling mean ATR over w periods."""
    return _rolling_mean(_tr(close, high, low), w)


def _atr_ewm(close: pd.Series, high: pd.Series, low: pd.Series, span: int) -> pd.Series:
    """EWM-smoothed ATR (Wilder-style via ewm)."""
    return _ewm_mean(_tr(close, high, low), span)


def _daily_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    ret = _log_safe(close) - _log_safe(close.shift(1))
    return _safe_div(ret, _atr(close, high, low, 14))


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): New ATR periods not in base files (ATR7, ATR10, ATR30, ATR42, ATR126) ---

def atr_ext_001_daily_move_atr7(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-return divided by 7-day ATR (ultra-short-range normalization)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    return _safe_div(ret, _atr(close, high, low, 7))


def atr_ext_002_daily_move_atr10(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-return divided by 10-day ATR."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    return _safe_div(ret, _atr(close, high, low, 10))


def atr_ext_003_daily_move_atr30(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-return divided by 30-day ATR."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    return _safe_div(ret, _atr(close, high, low, 30))


def atr_ext_004_daily_move_atr42(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-return divided by 42-day ATR (two-month horizon)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    return _safe_div(ret, _atr(close, high, low, 42))


def atr_ext_005_daily_move_atr126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-return divided by 126-day ATR (half-year volatility baseline)."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    return _safe_div(ret, _atr(close, high, low, _TD_HALF))


def atr_ext_006_5d_move_atr7(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day log-return divided by 7-day ATR."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    return _safe_div(ret, _atr(close, high, low, 7))


def atr_ext_007_5d_move_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day log-return divided by 21-day ATR (weekly move in monthly-ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    return _safe_div(ret, _atr(close, high, low, _TD_MON))


def atr_ext_008_21d_move_atr7(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day log-return divided by 7-day ATR (monthly move in ultra-short ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return _safe_div(ret, _atr(close, high, low, 7))


def atr_ext_009_63d_move_atr42(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day log-return divided by 42-day ATR."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    return _safe_div(ret, _atr(close, high, low, 42))


def atr_ext_010_126d_move_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """126-day log-return divided by 63-day ATR (half-year self-normalized move)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_HALF))
    return _safe_div(ret, _atr(close, high, low, _TD_QTR))


# --- Group B (011-020): ATR-unit moves at new horizons (3d, 15d, 30d, 42d) ---

def atr_ext_011_3d_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """3-day log-return divided by ATR14 (3-day move in ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(3))
    return _safe_div(ret, _atr(close, high, low, 14))


def atr_ext_012_15d_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """15-day log-return divided by ATR14."""
    ret = _log_safe(close) - _log_safe(close.shift(15))
    return _safe_div(ret, _atr(close, high, low, 14))


def atr_ext_013_30d_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """30-day log-return divided by ATR14."""
    ret = _log_safe(close) - _log_safe(close.shift(30))
    return _safe_div(ret, _atr(close, high, low, 14))


def atr_ext_014_42d_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """42-day log-return divided by ATR14 (two-month move)."""
    ret = _log_safe(close) - _log_safe(close.shift(42))
    return _safe_div(ret, _atr(close, high, low, 14))


def atr_ext_015_42d_move_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """42-day log-return divided by ATR21."""
    ret = _log_safe(close) - _log_safe(close.shift(42))
    return _safe_div(ret, _atr(close, high, low, _TD_MON))


def atr_ext_016_63d_move_atr7(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day log-return divided by ATR7 (quarterly displacement in ultra-short ATR)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    return _safe_div(ret, _atr(close, high, low, 7))


def atr_ext_017_126d_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """126-day log-return divided by ATR14 (half-year move in ATR14 units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_HALF))
    return _safe_div(ret, _atr(close, high, low, 14))


def atr_ext_018_252d_move_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day log-return divided by ATR63 (annual move in quarterly-ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_YEAR))
    return _safe_div(ret, _atr(close, high, low, _TD_QTR))


def atr_ext_019_252d_move_atr126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day log-return divided by ATR126 (annual move in half-year ATR units)."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_YEAR))
    return _safe_div(ret, _atr(close, high, low, _TD_HALF))


def atr_ext_020_3d_abs_move_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute 3-day move divided by ATR14 (short burst magnitude)."""
    return atr_ext_011_3d_move_atr14(close, high, low).abs()


# --- Group C (021-030): Expanding-window ATR reference and all-time drawdown ---

def atr_ext_021_dist_from_alltime_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below all-time (expanding) high in ATR14 units."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, 14)
    return _safe_div(close - exp_high, atr)


def atr_ext_022_dist_from_alltime_high_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below all-time high in ATR21 units."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - exp_high, atr)


def atr_ext_023_dist_from_alltime_high_expanding_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of all-time-high ATR14-distance."""
    exp_high = close.expanding(min_periods=1).max()
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - exp_high, atr)
    return dist.expanding(min_periods=5).rank(pct=True)


def atr_ext_024_dist_from_3yr_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 3-year (756-day) high in ATR14 units."""
    high_756 = _rolling_max(close, 756)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_756, atr)


def atr_ext_025_dist_from_2yr_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 2-year (504-day) high in ATR14 units."""
    high_504 = _rolling_max(close, 504)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_504, atr)


def atr_ext_026_dist_from_5d_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 5-day high in ATR14 units (intraweek dislocation)."""
    high_5 = _rolling_max(close, _TD_WEEK)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_5, atr)


def atr_ext_027_dist_from_10d_high_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close below 10-day high in ATR14 units."""
    high_10 = _rolling_max(close, 10)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - high_10, atr)


def atr_ext_028_dist_from_10d_low_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close above 10-day low in ATR14 units."""
    low_10 = _rolling_min(close, 10)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - low_10, atr)


def atr_ext_029_dist_from_126d_low_atr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close above 126-day low in ATR14 units."""
    low_126 = _rolling_min(close, _TD_HALF)
    atr = _atr(close, high, low, 14)
    return _safe_div(close - low_126, atr)


def atr_ext_030_dist_from_252d_low_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance of close above 252-day low in ATR21 units."""
    low_252 = _rolling_min(close, _TD_YEAR)
    atr = _atr(close, high, low, _TD_MON)
    return _safe_div(close - low_252, atr)


# --- Group D (031-040): ATR-unit z-scores at new window combinations ---

def atr_ext_031_daily_move_atr14_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of daily ATR14-normalized move vs trailing 63-day distribution."""
    m = _daily_move_atr14(close, high, low)
    mu = _rolling_mean(m, _TD_QTR)
    sd = _rolling_std(m, _TD_QTR)
    return _safe_div(m - mu, sd)


def atr_ext_032_daily_move_atr14_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of daily ATR14-normalized move vs trailing 21-day distribution."""
    m = _daily_move_atr14(close, high, low)
    mu = _rolling_mean(m, _TD_MON)
    sd = _rolling_std(m, _TD_MON)
    return _safe_div(m - mu, sd)


def atr_ext_033_daily_move_atr7_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of daily ATR7-normalized move vs trailing 252-day distribution."""
    m = atr_ext_001_daily_move_atr7(close, high, low)
    mu = _rolling_mean(m, _TD_YEAR)
    sd = _rolling_std(m, _TD_YEAR)
    return _safe_div(m - mu, sd)


def atr_ext_034_5d_move_atr14_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 5-day ATR14-move vs trailing 63-day distribution."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    m = _safe_div(ret, _atr(close, high, low, 14))
    mu = _rolling_mean(m, _TD_QTR)
    sd = _rolling_std(m, _TD_QTR)
    return _safe_div(m - mu, sd)


def atr_ext_035_21d_move_atr21_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day ATR21-move vs trailing 252-day distribution."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    m = _safe_div(ret, _atr(close, high, low, _TD_MON))
    mu = _rolling_mean(m, _TD_YEAR)
    sd = _rolling_std(m, _TD_YEAR)
    return _safe_div(m - mu, sd)


def atr_ext_036_drawdown_252d_atr7_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score (expanding) of 252-day drawdown expressed in ATR7 units."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 7)
    dd = _safe_div(close - high_252, atr)
    mu = dd.expanding(min_periods=5).mean()
    sd = dd.expanding(min_periods=5).std()
    return _safe_div(dd - mu, sd)


def atr_ext_037_dist_below_sma200_atr7_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of SMA200 ATR7-distance vs trailing 252-day distribution."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 7)
    dist = _safe_div(close - ma, atr)
    mu = _rolling_mean(dist, _TD_YEAR)
    sd = _rolling_std(dist, _TD_YEAR)
    return _safe_div(dist - mu, sd)


def atr_ext_038_daily_move_atr14_expanding_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding (all-history) z-score of daily ATR14-normalized move."""
    m = _daily_move_atr14(close, high, low)
    mu = m.expanding(min_periods=5).mean()
    sd = m.expanding(min_periods=5).std()
    return _safe_div(m - mu, sd)


def atr_ext_039_daily_move_atr21_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of daily ATR21-normalized move vs trailing 252-day distribution."""
    ret = _log_safe(close) - _log_safe(close.shift(1))
    m = _safe_div(ret, _atr(close, high, low, _TD_MON))
    mu = _rolling_mean(m, _TD_YEAR)
    sd = _rolling_std(m, _TD_YEAR)
    return _safe_div(m - mu, sd)


def atr_ext_040_63d_move_atr63_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 63-day ATR63-move vs trailing 252-day distribution."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    m = _safe_div(ret, _atr(close, high, low, _TD_QTR))
    mu = _rolling_mean(m, _TD_YEAR)
    sd = _rolling_std(m, _TD_YEAR)
    return _safe_div(m - mu, sd)


# --- Group E (041-050): Percentile ranks at new window/period combos ---

def atr_ext_041_daily_move_atr14_pct_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of daily ATR14-move in trailing 63-day window."""
    m = _daily_move_atr14(close, high, low)
    return m.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def atr_ext_042_daily_move_atr14_pct_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of daily ATR14-move in trailing 21-day window."""
    m = _daily_move_atr14(close, high, low)
    return m.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def atr_ext_043_daily_move_atr14_expanding_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of daily ATR14-normalized move."""
    m = _daily_move_atr14(close, high, low)
    return m.expanding(min_periods=5).rank(pct=True)


def atr_ext_044_5d_move_atr14_pct_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 5-day ATR14-move in trailing 63-day window."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    m = _safe_div(ret, _atr(close, high, low, 14))
    return m.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def atr_ext_045_21d_move_atr14_pct_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ATR14-move in trailing 126-day window."""
    ret = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    m = _safe_div(ret, _atr(close, high, low, 14))
    return m.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def atr_ext_046_dist_below_sma200_atr14_pct_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of SMA200 ATR14-distance in trailing 126-day window."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return dist.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def atr_ext_047_drawdown_252d_atr14_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 252-day-high drawdown (ATR14) in trailing 252-day window."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dd = _safe_div(close - high_252, atr)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def atr_ext_048_cum_down_atr_63d_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63-day cumulative down-ATR14 in trailing 252-day window."""
    m = _daily_move_atr14(close, high, low)
    cum_dn = m.where(m < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    return cum_dn.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def atr_ext_049_dist_below_sma21_atr14_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of SMA21 ATR14-distance in trailing 252-day window."""
    ma = _rolling_mean(close, _TD_MON)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def atr_ext_050_intraday_range_atr14_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of intraday H-L range in ATR14 units vs 252-day history."""
    rng = _safe_div(high - low, _atr(close, high, low, 14))
    return rng.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group F (051-060): Open/gap/wick variants not in base files ---

def atr_ext_051_gap_up_atr14(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Upward gap move (open vs prior close) in ATR14 units; zero on gap-down days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    raw = _safe_div(gap, atr)
    return raw.where(raw > 0, 0.0)


def atr_ext_052_cum_gap_up_atr_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative gap-up ATR14-units over 21 days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    raw = _safe_div(gap, atr)
    up = raw.where(raw > 0, 0.0)
    return _rolling_sum(up, _TD_MON)


def atr_ext_053_abs_gap_atr14(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute gap (open vs prior close) in ATR14 units."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    return _safe_div(gap, atr).abs()


def atr_ext_054_cum_abs_gap_atr_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative absolute gap in ATR14 units over 21 days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    atr = _atr(close, high, low, 14)
    abs_gap = _safe_div(gap, atr).abs()
    return _rolling_sum(abs_gap, _TD_MON)


def atr_ext_055_open_to_close_down_atr14(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday down move (close < open) in ATR14 units; zero on up days."""
    move = _log_safe(close) - _log_safe(open)
    atr = _atr(close, high, low, 14)
    raw = _safe_div(move, atr)
    return raw.where(raw < 0, 0.0)


def atr_ext_056_open_to_close_abs_atr14_63d_mean(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """63-day mean of |open-to-close| in ATR14 units."""
    move = (_log_safe(close) - _log_safe(open)).abs()
    atr = _atr(close, high, low, 14)
    return _rolling_mean(_safe_div(move, atr), _TD_QTR)


def atr_ext_057_cum_open_to_close_down_atr14_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative intraday down moves in ATR14 units over 63 days."""
    move = _log_safe(close) - _log_safe(open)
    atr = _atr(close, high, low, 14)
    raw = _safe_div(move, atr)
    dn = raw.where(raw < 0, 0.0)
    return _rolling_sum(dn, _TD_QTR)


def atr_ext_058_lower_wick_atr14_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of lower wick (close - low) in ATR14 units."""
    atr = _atr(close, high, low, 14)
    lw = _safe_div(close - low, atr)
    return _rolling_mean(lw, _TD_MON)


def atr_ext_059_upper_wick_atr14_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of upper wick (high - close) in ATR14 units."""
    atr = _atr(close, high, low, 14)
    uw = _safe_div(high - close, atr)
    return _rolling_mean(uw, _TD_MON)


def atr_ext_060_wick_imbalance_atr14_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of (lower_wick - upper_wick) in ATR14 units."""
    atr = _atr(close, high, low, 14)
    lw = _safe_div(close - low, atr)
    uw = _safe_div(high - close, atr)
    return _rolling_mean(lw - uw, _TD_MON)


# --- Group G (061-070): Volume-conditioned and ATR-scaled composites ---

def atr_ext_061_vol_weighted_down_atr14_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted cumulative downward ATR14-move over 63 days."""
    m = _daily_move_atr14(close, high, low)
    dn = m.where(m < 0, 0.0)
    wt = dn * volume
    return _safe_div(_rolling_sum(wt, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def atr_ext_062_extreme_down_vol_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with move < -2 ATR14 AND volume > avg_vol over trailing 63 days."""
    m = _daily_move_atr14(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    flag = ((m < -2) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def atr_ext_063_vol_surge_down_atr14_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (|ATR14 down-move| * vol_ratio) on days where vol > 2x avg, over 21 days."""
    m = _daily_move_atr14(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    surge_dn = m.where(m < 0, 0.0).abs() * vol_ratio.where(volume > 2 * avg_vol, 0.0)
    return _rolling_sum(surge_dn, _TD_MON)


def atr_ext_064_high_vol_down_day_mean_atr14_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean ATR14-move on high-volume DOWN days (below-average days excluded), over 63d."""
    m = _daily_move_atr14(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    m_cond = m.where((volume > avg_vol) & (m < 0), np.nan)
    return m_cond.rolling(_TD_QTR, min_periods=1).mean()


def atr_ext_065_atr14_move_vol_corr_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rolling correlation between ATR14-move and volume."""
    m = _daily_move_atr14(close, high, low)
    return m.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).corr(volume)


def atr_ext_066_count_gt1atr_down_moves_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with move < -1 ATR14 unit in trailing 21 days."""
    m = _daily_move_atr14(close, high, low)
    return _rolling_sum((m < -1).astype(float), _TD_MON)


def atr_ext_067_count_gt1atr_down_moves_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with move < -1 ATR14 unit in trailing 63 days."""
    m = _daily_move_atr14(close, high, low)
    return _rolling_sum((m < -1).astype(float), _TD_QTR)


def atr_ext_068_count_gt4atr_down_moves_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with move < -4 ATR14 units in trailing 252 days (crash events)."""
    m = _daily_move_atr14(close, high, low)
    return _rolling_sum((m < -4).astype(float), _TD_YEAR)


def atr_ext_069_extreme_down_move_flag_gt3atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today's down-move exceeds -3 ATR14 units."""
    m = _daily_move_atr14(close, high, low)
    return (m < -3).astype(float)


def atr_ext_070_consec_down_atr14_days(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with negative ATR14-normalized daily move (down streak length)."""
    m = _daily_move_atr14(close, high, low)
    cond = m < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# --- Group H (071-075): ATR-unit OLS slopes, EWM velocities, composites ---

def atr_ext_071_dist_below_sma200_atr14_slope_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 5 days of SMA200 ATR14-distance (very short-term breakdown pace)."""
    ma = _rolling_mean(close, 200)
    atr = _atr(close, high, low, 14)
    dist = _safe_div(close - ma, atr)
    return _linslope(dist, _TD_WEEK)


def atr_ext_072_drawdown_252d_atr14_slope_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 5 days of 252-day high ATR14-drawdown."""
    high_252 = _rolling_max(close, _TD_YEAR)
    atr = _atr(close, high, low, 14)
    dd = _safe_div(close - high_252, atr)
    return _linslope(dd, _TD_WEEK)


def atr_ext_073_atr_velocity_63d_ewm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM (span=63) of daily ATR14-normalized moves (smooth long-term velocity)."""
    m = _daily_move_atr14(close, high, low)
    return _ewm_mean(m, _TD_QTR)


def atr_ext_074_composite_distress_atr14_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distress composite: sum of (normalized) 5d/21d/63d ATR14 drawdowns from respective highs."""
    atr = _atr(close, high, low, 14)
    d5 = _safe_div(close - _rolling_max(close, _TD_WEEK), atr).clip(upper=0)
    d21 = _safe_div(close - _rolling_max(close, _TD_MON), atr).clip(upper=0)
    d63 = _safe_div(close - _rolling_max(close, _TD_QTR), atr).clip(upper=0)
    return d5 + d21 + d63


def atr_ext_075_atr14_capitulation_composite(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Capitulation composite: SMA200-dist + 252d-drawdown + 21d-velocity, all in ATR14 units.
    Score is more negative at deeper capitulation."""
    atr = _atr(close, high, low, 14)
    ma_dist = _safe_div(close - _rolling_mean(close, 200), atr)
    dd_252 = _safe_div(close - _rolling_max(close, _TD_YEAR), atr)
    m = _daily_move_atr14(close, high, low)
    vel_21 = _rolling_mean(m, _TD_MON)
    return ma_dist + dd_252 + vel_21


# ── Registry ──────────────────────────────────────────────────────────────────

ATR_NORMALIZED_MOVE_EXTENDED_REGISTRY_001_075 = {
    "atr_ext_001_daily_move_atr7": {"inputs": ["close", "high", "low"], "func": atr_ext_001_daily_move_atr7},
    "atr_ext_002_daily_move_atr10": {"inputs": ["close", "high", "low"], "func": atr_ext_002_daily_move_atr10},
    "atr_ext_003_daily_move_atr30": {"inputs": ["close", "high", "low"], "func": atr_ext_003_daily_move_atr30},
    "atr_ext_004_daily_move_atr42": {"inputs": ["close", "high", "low"], "func": atr_ext_004_daily_move_atr42},
    "atr_ext_005_daily_move_atr126": {"inputs": ["close", "high", "low"], "func": atr_ext_005_daily_move_atr126},
    "atr_ext_006_5d_move_atr7": {"inputs": ["close", "high", "low"], "func": atr_ext_006_5d_move_atr7},
    "atr_ext_007_5d_move_atr21": {"inputs": ["close", "high", "low"], "func": atr_ext_007_5d_move_atr21},
    "atr_ext_008_21d_move_atr7": {"inputs": ["close", "high", "low"], "func": atr_ext_008_21d_move_atr7},
    "atr_ext_009_63d_move_atr42": {"inputs": ["close", "high", "low"], "func": atr_ext_009_63d_move_atr42},
    "atr_ext_010_126d_move_atr63": {"inputs": ["close", "high", "low"], "func": atr_ext_010_126d_move_atr63},
    "atr_ext_011_3d_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_011_3d_move_atr14},
    "atr_ext_012_15d_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_012_15d_move_atr14},
    "atr_ext_013_30d_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_013_30d_move_atr14},
    "atr_ext_014_42d_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_014_42d_move_atr14},
    "atr_ext_015_42d_move_atr21": {"inputs": ["close", "high", "low"], "func": atr_ext_015_42d_move_atr21},
    "atr_ext_016_63d_move_atr7": {"inputs": ["close", "high", "low"], "func": atr_ext_016_63d_move_atr7},
    "atr_ext_017_126d_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_017_126d_move_atr14},
    "atr_ext_018_252d_move_atr63": {"inputs": ["close", "high", "low"], "func": atr_ext_018_252d_move_atr63},
    "atr_ext_019_252d_move_atr126": {"inputs": ["close", "high", "low"], "func": atr_ext_019_252d_move_atr126},
    "atr_ext_020_3d_abs_move_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_020_3d_abs_move_atr14},
    "atr_ext_021_dist_from_alltime_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_021_dist_from_alltime_high_atr14},
    "atr_ext_022_dist_from_alltime_high_atr21": {"inputs": ["close", "high", "low"], "func": atr_ext_022_dist_from_alltime_high_atr21},
    "atr_ext_023_dist_from_alltime_high_expanding_rank": {"inputs": ["close", "high", "low"], "func": atr_ext_023_dist_from_alltime_high_expanding_rank},
    "atr_ext_024_dist_from_3yr_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_024_dist_from_3yr_high_atr14},
    "atr_ext_025_dist_from_2yr_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_025_dist_from_2yr_high_atr14},
    "atr_ext_026_dist_from_5d_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_026_dist_from_5d_high_atr14},
    "atr_ext_027_dist_from_10d_high_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_027_dist_from_10d_high_atr14},
    "atr_ext_028_dist_from_10d_low_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_028_dist_from_10d_low_atr14},
    "atr_ext_029_dist_from_126d_low_atr14": {"inputs": ["close", "high", "low"], "func": atr_ext_029_dist_from_126d_low_atr14},
    "atr_ext_030_dist_from_252d_low_atr21": {"inputs": ["close", "high", "low"], "func": atr_ext_030_dist_from_252d_low_atr21},
    "atr_ext_031_daily_move_atr14_zscore_63d": {"inputs": ["close", "high", "low"], "func": atr_ext_031_daily_move_atr14_zscore_63d},
    "atr_ext_032_daily_move_atr14_zscore_21d": {"inputs": ["close", "high", "low"], "func": atr_ext_032_daily_move_atr14_zscore_21d},
    "atr_ext_033_daily_move_atr7_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_033_daily_move_atr7_zscore_252d},
    "atr_ext_034_5d_move_atr14_zscore_63d": {"inputs": ["close", "high", "low"], "func": atr_ext_034_5d_move_atr14_zscore_63d},
    "atr_ext_035_21d_move_atr21_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_035_21d_move_atr21_zscore_252d},
    "atr_ext_036_drawdown_252d_atr7_zscore": {"inputs": ["close", "high", "low"], "func": atr_ext_036_drawdown_252d_atr7_zscore},
    "atr_ext_037_dist_below_sma200_atr7_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_037_dist_below_sma200_atr7_zscore_252d},
    "atr_ext_038_daily_move_atr14_expanding_zscore": {"inputs": ["close", "high", "low"], "func": atr_ext_038_daily_move_atr14_expanding_zscore},
    "atr_ext_039_daily_move_atr21_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_039_daily_move_atr21_zscore_252d},
    "atr_ext_040_63d_move_atr63_zscore_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_040_63d_move_atr63_zscore_252d},
    "atr_ext_041_daily_move_atr14_pct_rank_63d": {"inputs": ["close", "high", "low"], "func": atr_ext_041_daily_move_atr14_pct_rank_63d},
    "atr_ext_042_daily_move_atr14_pct_rank_21d": {"inputs": ["close", "high", "low"], "func": atr_ext_042_daily_move_atr14_pct_rank_21d},
    "atr_ext_043_daily_move_atr14_expanding_pct_rank": {"inputs": ["close", "high", "low"], "func": atr_ext_043_daily_move_atr14_expanding_pct_rank},
    "atr_ext_044_5d_move_atr14_pct_rank_63d": {"inputs": ["close", "high", "low"], "func": atr_ext_044_5d_move_atr14_pct_rank_63d},
    "atr_ext_045_21d_move_atr14_pct_rank_126d": {"inputs": ["close", "high", "low"], "func": atr_ext_045_21d_move_atr14_pct_rank_126d},
    "atr_ext_046_dist_below_sma200_atr14_pct_rank_126d": {"inputs": ["close", "high", "low"], "func": atr_ext_046_dist_below_sma200_atr14_pct_rank_126d},
    "atr_ext_047_drawdown_252d_atr14_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_047_drawdown_252d_atr14_pct_rank_252d},
    "atr_ext_048_cum_down_atr_63d_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_048_cum_down_atr_63d_pct_rank_252d},
    "atr_ext_049_dist_below_sma21_atr14_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_049_dist_below_sma21_atr14_pct_rank_252d},
    "atr_ext_050_intraday_range_atr14_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_050_intraday_range_atr14_pct_rank_252d},
    "atr_ext_051_gap_up_atr14": {"inputs": ["close", "high", "low", "open"], "func": atr_ext_051_gap_up_atr14},
    "atr_ext_052_cum_gap_up_atr_21d": {"inputs": ["close", "high", "low", "open"], "func": atr_ext_052_cum_gap_up_atr_21d},
    "atr_ext_053_abs_gap_atr14": {"inputs": ["close", "high", "low", "open"], "func": atr_ext_053_abs_gap_atr14},
    "atr_ext_054_cum_abs_gap_atr_21d": {"inputs": ["close", "high", "low", "open"], "func": atr_ext_054_cum_abs_gap_atr_21d},
    "atr_ext_055_open_to_close_down_atr14": {"inputs": ["close", "high", "low", "open"], "func": atr_ext_055_open_to_close_down_atr14},
    "atr_ext_056_open_to_close_abs_atr14_63d_mean": {"inputs": ["close", "high", "low", "open"], "func": atr_ext_056_open_to_close_abs_atr14_63d_mean},
    "atr_ext_057_cum_open_to_close_down_atr14_63d": {"inputs": ["close", "high", "low", "open"], "func": atr_ext_057_cum_open_to_close_down_atr14_63d},
    "atr_ext_058_lower_wick_atr14_21d_mean": {"inputs": ["close", "high", "low"], "func": atr_ext_058_lower_wick_atr14_21d_mean},
    "atr_ext_059_upper_wick_atr14_21d_mean": {"inputs": ["close", "high", "low"], "func": atr_ext_059_upper_wick_atr14_21d_mean},
    "atr_ext_060_wick_imbalance_atr14_21d_mean": {"inputs": ["close", "high", "low"], "func": atr_ext_060_wick_imbalance_atr14_21d_mean},
    "atr_ext_061_vol_weighted_down_atr14_63d": {"inputs": ["close", "high", "low", "volume"], "func": atr_ext_061_vol_weighted_down_atr14_63d},
    "atr_ext_062_extreme_down_vol_flag_63d": {"inputs": ["close", "high", "low", "volume"], "func": atr_ext_062_extreme_down_vol_flag_63d},
    "atr_ext_063_vol_surge_down_atr14_21d": {"inputs": ["close", "high", "low", "volume"], "func": atr_ext_063_vol_surge_down_atr14_21d},
    "atr_ext_064_high_vol_down_day_mean_atr14_63d": {"inputs": ["close", "high", "low", "volume"], "func": atr_ext_064_high_vol_down_day_mean_atr14_63d},
    "atr_ext_065_atr14_move_vol_corr_5d": {"inputs": ["close", "high", "low", "volume"], "func": atr_ext_065_atr14_move_vol_corr_5d},
    "atr_ext_066_count_gt1atr_down_moves_21d": {"inputs": ["close", "high", "low"], "func": atr_ext_066_count_gt1atr_down_moves_21d},
    "atr_ext_067_count_gt1atr_down_moves_63d": {"inputs": ["close", "high", "low"], "func": atr_ext_067_count_gt1atr_down_moves_63d},
    "atr_ext_068_count_gt4atr_down_moves_252d": {"inputs": ["close", "high", "low"], "func": atr_ext_068_count_gt4atr_down_moves_252d},
    "atr_ext_069_extreme_down_move_flag_gt3atr": {"inputs": ["close", "high", "low"], "func": atr_ext_069_extreme_down_move_flag_gt3atr},
    "atr_ext_070_consec_down_atr14_days": {"inputs": ["close", "high", "low"], "func": atr_ext_070_consec_down_atr14_days},
    "atr_ext_071_dist_below_sma200_atr14_slope_5d": {"inputs": ["close", "high", "low"], "func": atr_ext_071_dist_below_sma200_atr14_slope_5d},
    "atr_ext_072_drawdown_252d_atr14_slope_5d": {"inputs": ["close", "high", "low"], "func": atr_ext_072_drawdown_252d_atr14_slope_5d},
    "atr_ext_073_atr_velocity_63d_ewm": {"inputs": ["close", "high", "low"], "func": atr_ext_073_atr_velocity_63d_ewm},
    "atr_ext_074_composite_distress_atr14_score": {"inputs": ["close", "high", "low"], "func": atr_ext_074_composite_distress_atr14_score},
    "atr_ext_075_atr14_capitulation_composite": {"inputs": ["close", "high", "low"], "func": atr_ext_075_atr14_capitulation_composite},
}
