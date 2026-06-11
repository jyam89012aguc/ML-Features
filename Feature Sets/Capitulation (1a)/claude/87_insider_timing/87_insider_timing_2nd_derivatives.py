"""
87_insider_timing — 2nd Derivative Features (itm_drv2_001 to itm_drv2_075)
Domain: insider activity timing vs price drawdown depth — rate-of-change layer
Asset class: US equities | SF2 insider series + daily close price
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
Inputs are:
  (1) daily close price (standard daily closing price)
  (2) daily event-aggregated Sharadar SF2 insider transaction series, one row
      per (ticker, date).  These series are EVENT-DRIVEN: they are mostly ZERO
      on non-filing dates and must NOT be forward-filled.  They are aggregated
      with trailing rolling SUMS over various windows.

These 2nd-derivative features compute .diff(n), slope, or pct-change of the
base concepts defined in the base files.  Because the daily insider series are
sparse, these derivatives will also be sparse — that is EXPECTED and correct.
Every function must return a same-length pandas Series with no exception even
when all insider series inputs are zero.

Available field names (lowercase):
  close, insider_buy_count, insider_sell_count, insider_buy_shares,
  insider_sell_shares, insider_buy_value, insider_sell_value,
  insider_buyers, insider_sellers, officer_buy_value, ceo_buy_value,
  cfo_buy_value, insider_shares_held

Trading-day constants: 252/yr, 63/qtr, 21/mo, 5/wk.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_QTR   = 63
_TD_HALF  = 126
_TD_MON   = 21
_TD_WEEK  = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominators with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _drawdown_from_expanding_high(close: pd.Series) -> pd.Series:
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _drawdown_from_rolling_high(close: pd.Series, w: int) -> pd.Series:
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


def _slope_ols(s: pd.Series, w: int) -> pd.Series:
    """OLS slope of s over trailing w days (via rolling cov/var on integer index)."""
    x = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    cov = s.rolling(w, min_periods=max(2, w // 4)).cov(x)
    var = x.rolling(w, min_periods=max(2, w // 4)).var()
    return _safe_div(cov, var)


# ── 2nd Derivative Feature Functions ─────────────────────────────────────────

def itm_drv2_001_buy_count_63d_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 63-day rolling insider buy count.
    Measures recent acceleration in insider buying pace."""
    base = _rolling_sum(insider_buy_count, _TD_QTR)
    return base.diff(_TD_MON)


def itm_drv2_002_buy_value_63d_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21-day difference of the 63-day rolling insider buy value."""
    base = _rolling_sum(insider_buy_value, _TD_QTR)
    return base.diff(_TD_MON)


def itm_drv2_003_buy_count_63d_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 63-day rolling buy count (quarter-over-quarter change)."""
    base = _rolling_sum(insider_buy_count, _TD_QTR)
    return base.diff(_TD_QTR)


def itm_drv2_004_buy_value_63d_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63-day difference of the 63-day rolling buy value."""
    base = _rolling_sum(insider_buy_value, _TD_QTR)
    return base.diff(_TD_QTR)


def itm_drv2_005_ath_dd_diff21(close: pd.Series) -> pd.Series:
    """21-day difference of ATH drawdown (how fast the drawdown is changing)."""
    dd = _drawdown_from_expanding_high(close)
    return dd.diff(_TD_MON)


def itm_drv2_006_ath_dd_diff63(close: pd.Series) -> pd.Series:
    """63-day difference of ATH drawdown."""
    dd = _drawdown_from_expanding_high(close)
    return dd.diff(_TD_QTR)


def itm_drv2_007_buy_count_x_ath_dd_diff21(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21-day diff of (63d buy count * ATH DD magnitude).
    Captures change in 'buying into decline' intensity."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_008_buy_value_x_ath_dd_diff21(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21-day diff of (63d buy value log1p * ATH DD magnitude)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    val63   = _rolling_sum(insider_buy_value, _TD_QTR)
    base    = np.log1p(val63.clip(lower=0)) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_009_buy_value_x_ath_dd_diff63(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day diff of (63d buy value log1p * ATH DD magnitude)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    val63   = _rolling_sum(insider_buy_value, _TD_QTR)
    base    = np.log1p(val63.clip(lower=0)) * dd_mag
    return base.diff(_TD_QTR)


def itm_drv2_010_buy_count_63d_slope_63d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 63d rolling buy count over trailing 63 days."""
    base = _rolling_sum(insider_buy_count, _TD_QTR)
    return _slope_ols(base, _TD_QTR)


def itm_drv2_011_buy_value_63d_slope_63d(insider_buy_value: pd.Series) -> pd.Series:
    """OLS slope of 63d rolling buy value over trailing 63 days."""
    base = _rolling_sum(insider_buy_value, _TD_QTR)
    return _slope_ols(base, _TD_QTR)


def itm_drv2_012_buy_count_63d_pct_change_21d(
    insider_buy_count: pd.Series
) -> pd.Series:
    """Percent change of 63d rolling buy count over 21 days."""
    base = _rolling_sum(insider_buy_count, _TD_QTR)
    prev = base.shift(_TD_MON)
    return _safe_div(base - prev, prev.abs().replace(0, np.nan))


def itm_drv2_013_buy_value_63d_pct_change_63d(
    insider_buy_value: pd.Series
) -> pd.Series:
    """Percent change of 63d rolling buy value over 63 days."""
    base = _rolling_sum(insider_buy_value, _TD_QTR)
    prev = base.shift(_TD_QTR)
    return _safe_div(base - prev, prev.abs().replace(0, np.nan))


def itm_drv2_014_officer_buy_value_63d_diff21(
    officer_buy_value: pd.Series
) -> pd.Series:
    """21-day diff of 63d rolling officer buy value."""
    base = _rolling_sum(officer_buy_value, _TD_QTR)
    return base.diff(_TD_MON)


def itm_drv2_015_officer_buy_x_ath_dd_diff21(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """21-day diff of (officer 63d buy value log1p * ATH DD magnitude)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    ov63    = _rolling_sum(officer_buy_value, _TD_QTR)
    base    = np.log1p(ov63.clip(lower=0)) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_016_net_buy_value_63d_diff21(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21-day diff of 63d net insider buy value."""
    base = _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)
    return base.diff(_TD_MON)


def itm_drv2_017_net_buy_value_63d_diff63(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """63-day diff of 63d net insider buy value."""
    base = _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)
    return base.diff(_TD_QTR)


def itm_drv2_018_buy_value_consistency_diff21(
    insider_buy_value: pd.Series
) -> pd.Series:
    """21-day diff of 63d buy-day fraction (fraction of days with nonzero buy)."""
    nonzero = (insider_buy_value > 0).astype(float)
    base    = _rolling_mean(nonzero, _TD_QTR)
    return base.diff(_TD_MON)


def itm_drv2_019_dd_depth_pct_rank_1y_diff21(close: pd.Series) -> pd.Series:
    """21-day diff of the 252d percentile rank of ATH drawdown."""
    dd   = _drawdown_from_expanding_high(close)
    base = dd.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)
    return base.diff(_TD_MON)


def itm_drv2_020_buyers_63d_diff21(insider_buyers: pd.Series) -> pd.Series:
    """21-day diff of 63d unique buyer count."""
    base = _rolling_sum(insider_buyers, _TD_QTR)
    return base.diff(_TD_MON)


def itm_drv2_021_buyers_x_ath_dd_diff21(
    close: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """21-day diff of (63d buyer count * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_022_buy_value_zscore_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of the 252d z-score of daily insider buy value."""
    base = _zscore_rolling(insider_buy_value, _TD_YEAR)
    return base.diff(_TD_MON)


def itm_drv2_023_buy_value_x_ath_dd_slope_252d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """252-day OLS slope of (63d buy value log1p * ATH DD magnitude)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    val63   = _rolling_sum(insider_buy_value, _TD_QTR)
    base    = np.log1p(val63.clip(lower=0)) * dd_mag
    return _slope_ols(base, _TD_YEAR)


def itm_drv2_024_ceo_buy_value_63d_diff63(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day diff of 63d rolling CEO buy value."""
    base = _rolling_sum(ceo_buy_value, _TD_QTR)
    return base.diff(_TD_QTR)


def itm_drv2_025_composite_timing_diff21(
    close: pd.Series, insider_buy_value: pd.Series,
    insider_buy_count: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """21-day diff of the composite insider timing score
    (equal-weight z-scores of buy value x ATH-dd, count x ATH-dd, buyers x ATH-dd)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    s1 = np.log1p(_rolling_sum(insider_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s2 = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    s3 = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    z1 = _zscore_rolling(s1, _TD_YEAR)
    z2 = _zscore_rolling(s2, _TD_YEAR)
    z3 = _zscore_rolling(s3, _TD_YEAR)
    base = (z1 + z2 + z3) / 3.0
    return base.diff(_TD_MON)


# ── 2nd Derivative Feature Functions 026-075 ──────────────────────────────────

def itm_drv2_026_buy_count_252d_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 252-day rolling insider buy count."""
    return _rolling_sum(insider_buy_count, _TD_YEAR).diff(_TD_MON)


def itm_drv2_027_buy_value_252d_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21-day difference of the 252-day rolling insider buy value."""
    return _rolling_sum(insider_buy_value, _TD_YEAR).diff(_TD_MON)


def itm_drv2_028_buy_count_252d_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 252-day rolling buy count."""
    return _rolling_sum(insider_buy_count, _TD_YEAR).diff(_TD_QTR)


def itm_drv2_029_buy_value_252d_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63-day difference of the 252-day rolling buy value."""
    return _rolling_sum(insider_buy_value, _TD_YEAR).diff(_TD_QTR)


def itm_drv2_030_buy_count_21d_diff5(insider_buy_count: pd.Series) -> pd.Series:
    """5-day difference of the 21-day rolling buy count (weekly acceleration)."""
    return _rolling_sum(insider_buy_count, _TD_MON).diff(_TD_WEEK)


def itm_drv2_031_buy_value_21d_diff5(insider_buy_value: pd.Series) -> pd.Series:
    """5-day difference of the 21-day rolling buy value."""
    return _rolling_sum(insider_buy_value, _TD_MON).diff(_TD_WEEK)


def itm_drv2_032_buy_count_63d_slope_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 63d rolling buy count over trailing 252 days."""
    return _slope_ols(_rolling_sum(insider_buy_count, _TD_QTR), _TD_YEAR)


def itm_drv2_033_buy_value_63d_slope_252d(insider_buy_value: pd.Series) -> pd.Series:
    """OLS slope of 63d rolling buy value over trailing 252 days."""
    return _slope_ols(_rolling_sum(insider_buy_value, _TD_QTR), _TD_YEAR)


def itm_drv2_034_sell_value_63d_diff21(insider_sell_value: pd.Series) -> pd.Series:
    """21-day difference of the 63-day rolling sell value."""
    return _rolling_sum(insider_sell_value, _TD_QTR).diff(_TD_MON)


def itm_drv2_035_sell_count_63d_diff21(insider_sell_count: pd.Series) -> pd.Series:
    """21-day difference of the 63-day rolling sell count."""
    return _rolling_sum(insider_sell_count, _TD_QTR).diff(_TD_MON)


def itm_drv2_036_net_buy_value_252d_diff21(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21-day diff of 252d net insider buy value."""
    base = _rolling_sum(insider_buy_value, _TD_YEAR) - _rolling_sum(insider_sell_value, _TD_YEAR)
    return base.diff(_TD_MON)


def itm_drv2_037_net_buy_value_252d_diff63(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """63-day diff of 252d net insider buy value."""
    base = _rolling_sum(insider_buy_value, _TD_YEAR) - _rolling_sum(insider_sell_value, _TD_YEAR)
    return base.diff(_TD_QTR)


def itm_drv2_038_ath_dd_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of ATH drawdown over trailing 63 days."""
    return _slope_ols(_drawdown_from_expanding_high(close), _TD_QTR)


def itm_drv2_039_ath_dd_slope_252d(close: pd.Series) -> pd.Series:
    """OLS slope of ATH drawdown over trailing 252 days."""
    return _slope_ols(_drawdown_from_expanding_high(close), _TD_YEAR)


def itm_drv2_040_1y_dd_diff21(close: pd.Series) -> pd.Series:
    """21-day difference of 1-year rolling drawdown."""
    return _drawdown_from_rolling_high(close, _TD_YEAR).diff(_TD_MON)


def itm_drv2_041_1y_dd_diff63(close: pd.Series) -> pd.Series:
    """63-day difference of 1-year rolling drawdown."""
    return _drawdown_from_rolling_high(close, _TD_YEAR).diff(_TD_QTR)


def itm_drv2_042_buyers_63d_diff63(insider_buyers: pd.Series) -> pd.Series:
    """63-day diff of 63d unique buyer count (quarter-over-quarter change)."""
    return _rolling_sum(insider_buyers, _TD_QTR).diff(_TD_QTR)


def itm_drv2_043_buyers_252d_diff21(insider_buyers: pd.Series) -> pd.Series:
    """21-day diff of 252d unique buyer count."""
    return _rolling_sum(insider_buyers, _TD_YEAR).diff(_TD_MON)


def itm_drv2_044_officer_buy_value_63d_diff63(officer_buy_value: pd.Series) -> pd.Series:
    """63-day diff of 63d rolling officer buy value."""
    return _rolling_sum(officer_buy_value, _TD_QTR).diff(_TD_QTR)


def itm_drv2_045_officer_buy_x_ath_dd_diff63(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """63-day diff of (officer 63d buy value log1p * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    ov63   = _rolling_sum(officer_buy_value, _TD_QTR)
    base   = np.log1p(ov63.clip(lower=0)) * dd_mag
    return base.diff(_TD_QTR)


def itm_drv2_046_buy_value_pct_change_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change of 252d rolling buy value over 252 days."""
    base = _rolling_sum(insider_buy_value, _TD_YEAR)
    prev = base.shift(_TD_YEAR)
    return _safe_div(base - prev, prev.abs().replace(0, np.nan))


def itm_drv2_047_buy_count_pct_change_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Percent change of 63d rolling buy count over 63 days."""
    base = _rolling_sum(insider_buy_count, _TD_QTR)
    prev = base.shift(_TD_QTR)
    return _safe_div(base - prev, prev.abs().replace(0, np.nan))


def itm_drv2_048_buy_shares_63d_diff21(insider_buy_shares: pd.Series) -> pd.Series:
    """21-day difference of the 63-day rolling insider buy shares."""
    return _rolling_sum(insider_buy_shares, _TD_QTR).diff(_TD_MON)


def itm_drv2_049_buy_shares_x_ath_dd_diff21(
    close: pd.Series, insider_buy_shares: pd.Series
) -> pd.Series:
    """21-day diff of (63d buy shares log1p * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    sh63   = _rolling_sum(insider_buy_shares, _TD_QTR)
    base   = np.log1p(sh63.clip(lower=0)) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_050_ceo_buy_x_ath_dd_diff21(
    close: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """21-day diff of (CEO 63d buy value log1p * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    cv63   = _rolling_sum(ceo_buy_value, _TD_QTR)
    base   = np.log1p(cv63.clip(lower=0)) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_051_cfo_buy_value_63d_diff21(cfo_buy_value: pd.Series) -> pd.Series:
    """21-day diff of 63d rolling CFO buy value."""
    return _rolling_sum(cfo_buy_value, _TD_QTR).diff(_TD_MON)


def itm_drv2_052_buy_count_x_1y_dd_diff21(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21-day diff of (63d buy count * 1-year drawdown magnitude)."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_053_buy_value_x_1y_dd_diff63(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day diff of (63d buy value log1p * 1-year drawdown magnitude)."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    return base.diff(_TD_QTR)


def itm_drv2_054_buy_event_density_63d_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day diff of the 63d average daily buy event count."""
    return _rolling_mean(insider_buy_count, _TD_QTR).diff(_TD_MON)


def itm_drv2_055_buy_consistency_63d_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of 63d buy-day fraction."""
    nonzero = (insider_buy_value > 0).astype(float)
    return _rolling_mean(nonzero, _TD_QTR).diff(_TD_QTR)


def itm_drv2_056_sell_to_buy_ratio_63d_diff21(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21-day diff of the 63d sell/buy value ratio."""
    buy63  = _rolling_sum(insider_buy_value, _TD_QTR)
    sell63 = _rolling_sum(insider_sell_value, _TD_QTR)
    base   = _safe_div(sell63, buy63)
    return base.diff(_TD_MON)


def itm_drv2_057_dd_depth_pct_rank_1y_diff63(close: pd.Series) -> pd.Series:
    """63-day diff of the 252d percentile rank of ATH drawdown."""
    dd   = _drawdown_from_expanding_high(close)
    base = dd.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)
    return base.diff(_TD_QTR)


def itm_drv2_058_buy_count_x_ath_dd_diff63(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63-day diff of (63d buy count * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    return base.diff(_TD_QTR)


def itm_drv2_059_buy_value_x_ath_dd_slope_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day OLS slope of (63d buy value log1p * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    return _slope_ols(base, _TD_QTR)


def itm_drv2_060_buyers_x_ath_dd_diff63(
    close: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """63-day diff of (63d buyer count * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    return base.diff(_TD_QTR)


def itm_drv2_061_buy_count_zscore_252d_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day diff of the 252d z-score of daily insider buy count."""
    return _zscore_rolling(insider_buy_count, _TD_YEAR).diff(_TD_MON)


def itm_drv2_062_net_buy_count_63d_diff21(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series
) -> pd.Series:
    """21-day diff of 63d net buy count (buys minus sells)."""
    base = _rolling_sum(insider_buy_count, _TD_QTR) - _rolling_sum(insider_sell_count, _TD_QTR)
    return base.diff(_TD_MON)


def itm_drv2_063_buy_count_21d_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 21-day rolling buy count."""
    return _rolling_sum(insider_buy_count, _TD_MON).diff(_TD_MON)


def itm_drv2_064_buy_value_21d_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21-day difference of the 21-day rolling buy value."""
    return _rolling_sum(insider_buy_value, _TD_MON).diff(_TD_MON)


def itm_drv2_065_sell_value_63d_diff63(insider_sell_value: pd.Series) -> pd.Series:
    """63-day difference of the 63-day rolling sell value."""
    return _rolling_sum(insider_sell_value, _TD_QTR).diff(_TD_QTR)


def itm_drv2_066_officer_buy_63d_slope_252d(officer_buy_value: pd.Series) -> pd.Series:
    """OLS slope of 63d rolling officer buy value over trailing 252 days."""
    return _slope_ols(_rolling_sum(officer_buy_value, _TD_QTR), _TD_YEAR)


def itm_drv2_067_buy_value_x_2y_dd_diff21(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21-day diff of (63d buy value log1p * 2-year drawdown magnitude)."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_2Y).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_068_dd_pct_rank_3y_diff21(close: pd.Series) -> pd.Series:
    """21-day diff of the 756d percentile rank of ATH drawdown."""
    dd   = _drawdown_from_expanding_high(close)
    pct  = dd.rolling(756, min_periods=max(2, 756 // 4)).rank(pct=True)
    return pct.diff(_TD_MON)


def itm_drv2_069_buy_count_ratio_21_to_252_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day diff of the (annualized 21d/252d buy count ratio)."""
    buy21  = _rolling_sum(insider_buy_count, _TD_MON)
    buy252 = _rolling_sum(insider_buy_count, _TD_YEAR)
    base   = _safe_div(buy21 * (_TD_YEAR / _TD_MON), buy252)
    return base.diff(_TD_MON)


def itm_drv2_070_buy_value_consistency_252d_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of 252d buy-day fraction."""
    nonzero = (insider_buy_value > 0).astype(float)
    return _rolling_mean(nonzero, _TD_YEAR).diff(_TD_MON)


def itm_drv2_071_ceo_buy_63d_slope_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """OLS slope of 63d rolling CEO buy value over trailing 63 days."""
    return _slope_ols(_rolling_sum(ceo_buy_value, _TD_QTR), _TD_QTR)


def itm_drv2_072_buy_shares_252d_diff63(insider_buy_shares: pd.Series) -> pd.Series:
    """63-day difference of the 252-day rolling insider buy shares."""
    return _rolling_sum(insider_buy_shares, _TD_YEAR).diff(_TD_QTR)


def itm_drv2_073_buy_count_x_ath_dd_slope_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """252-day OLS slope of (63d buy count * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    return _slope_ols(base, _TD_YEAR)


def itm_drv2_074_sell_value_x_ath_dd_diff21(
    close: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21-day diff of (63d sell value log1p * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    sv63   = _rolling_sum(insider_sell_value, _TD_QTR)
    base   = np.log1p(sv63.clip(lower=0)) * dd_mag
    return base.diff(_TD_MON)


def itm_drv2_075_grand_composite_diff21(
    close: pd.Series, insider_buy_value: pd.Series,
    insider_buy_count: pd.Series, officer_buy_value: pd.Series,
    insider_buyers: pd.Series
) -> pd.Series:
    """21-day diff of grand composite (equal-weight z-scores of four deep-dd signals)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    s1 = np.log1p(_rolling_sum(insider_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s2 = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    s3 = np.log1p(_rolling_sum(officer_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s4 = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    base = sum(_zscore_rolling(s, _TD_YEAR) for s in (s1, s2, s3, s4)) / 4.0
    return base.diff(_TD_MON)


# ── Registry 2nd Derivatives ─────────────────────────────────────────────────

INSIDER_TIMING_REGISTRY_2ND_DERIVATIVES = {
    "itm_drv2_001_buy_count_63d_diff21":            {"inputs": ["insider_buy_count"],                                                   "func": itm_drv2_001_buy_count_63d_diff21},
    "itm_drv2_002_buy_value_63d_diff21":            {"inputs": ["insider_buy_value"],                                                   "func": itm_drv2_002_buy_value_63d_diff21},
    "itm_drv2_003_buy_count_63d_diff63":            {"inputs": ["insider_buy_count"],                                                   "func": itm_drv2_003_buy_count_63d_diff63},
    "itm_drv2_004_buy_value_63d_diff63":            {"inputs": ["insider_buy_value"],                                                   "func": itm_drv2_004_buy_value_63d_diff63},
    "itm_drv2_005_ath_dd_diff21":                   {"inputs": ["close"],                                                              "func": itm_drv2_005_ath_dd_diff21},
    "itm_drv2_006_ath_dd_diff63":                   {"inputs": ["close"],                                                              "func": itm_drv2_006_ath_dd_diff63},
    "itm_drv2_007_buy_count_x_ath_dd_diff21":       {"inputs": ["close", "insider_buy_count"],                                        "func": itm_drv2_007_buy_count_x_ath_dd_diff21},
    "itm_drv2_008_buy_value_x_ath_dd_diff21":       {"inputs": ["close", "insider_buy_value"],                                        "func": itm_drv2_008_buy_value_x_ath_dd_diff21},
    "itm_drv2_009_buy_value_x_ath_dd_diff63":       {"inputs": ["close", "insider_buy_value"],                                        "func": itm_drv2_009_buy_value_x_ath_dd_diff63},
    "itm_drv2_010_buy_count_63d_slope_63d":         {"inputs": ["insider_buy_count"],                                                 "func": itm_drv2_010_buy_count_63d_slope_63d},
    "itm_drv2_011_buy_value_63d_slope_63d":         {"inputs": ["insider_buy_value"],                                                 "func": itm_drv2_011_buy_value_63d_slope_63d},
    "itm_drv2_012_buy_count_63d_pct_change_21d":    {"inputs": ["insider_buy_count"],                                                 "func": itm_drv2_012_buy_count_63d_pct_change_21d},
    "itm_drv2_013_buy_value_63d_pct_change_63d":    {"inputs": ["insider_buy_value"],                                                 "func": itm_drv2_013_buy_value_63d_pct_change_63d},
    "itm_drv2_014_officer_buy_value_63d_diff21":    {"inputs": ["officer_buy_value"],                                                 "func": itm_drv2_014_officer_buy_value_63d_diff21},
    "itm_drv2_015_officer_buy_x_ath_dd_diff21":     {"inputs": ["close", "officer_buy_value"],                                       "func": itm_drv2_015_officer_buy_x_ath_dd_diff21},
    "itm_drv2_016_net_buy_value_63d_diff21":        {"inputs": ["insider_buy_value", "insider_sell_value"],                          "func": itm_drv2_016_net_buy_value_63d_diff21},
    "itm_drv2_017_net_buy_value_63d_diff63":        {"inputs": ["insider_buy_value", "insider_sell_value"],                          "func": itm_drv2_017_net_buy_value_63d_diff63},
    "itm_drv2_018_buy_value_consistency_diff21":    {"inputs": ["insider_buy_value"],                                                 "func": itm_drv2_018_buy_value_consistency_diff21},
    "itm_drv2_019_dd_depth_pct_rank_1y_diff21":     {"inputs": ["close"],                                                            "func": itm_drv2_019_dd_depth_pct_rank_1y_diff21},
    "itm_drv2_020_buyers_63d_diff21":               {"inputs": ["insider_buyers"],                                                   "func": itm_drv2_020_buyers_63d_diff21},
    "itm_drv2_021_buyers_x_ath_dd_diff21":          {"inputs": ["close", "insider_buyers"],                                          "func": itm_drv2_021_buyers_x_ath_dd_diff21},
    "itm_drv2_022_buy_value_zscore_diff21":         {"inputs": ["insider_buy_value"],                                                 "func": itm_drv2_022_buy_value_zscore_diff21},
    "itm_drv2_023_buy_value_x_ath_dd_slope_252d":   {"inputs": ["close", "insider_buy_value"],                                       "func": itm_drv2_023_buy_value_x_ath_dd_slope_252d},
    "itm_drv2_024_ceo_buy_value_63d_diff63":        {"inputs": ["ceo_buy_value"],                                                    "func": itm_drv2_024_ceo_buy_value_63d_diff63},
    "itm_drv2_025_composite_timing_diff21":         {"inputs": ["close", "insider_buy_value", "insider_buy_count", "insider_buyers"], "func": itm_drv2_025_composite_timing_diff21},
    "itm_drv2_026_buy_count_252d_diff21":           {"inputs": ["insider_buy_count"],                                                  "func": itm_drv2_026_buy_count_252d_diff21},
    "itm_drv2_027_buy_value_252d_diff21":           {"inputs": ["insider_buy_value"],                                                  "func": itm_drv2_027_buy_value_252d_diff21},
    "itm_drv2_028_buy_count_252d_diff63":           {"inputs": ["insider_buy_count"],                                                  "func": itm_drv2_028_buy_count_252d_diff63},
    "itm_drv2_029_buy_value_252d_diff63":           {"inputs": ["insider_buy_value"],                                                  "func": itm_drv2_029_buy_value_252d_diff63},
    "itm_drv2_030_buy_count_21d_diff5":             {"inputs": ["insider_buy_count"],                                                  "func": itm_drv2_030_buy_count_21d_diff5},
    "itm_drv2_031_buy_value_21d_diff5":             {"inputs": ["insider_buy_value"],                                                  "func": itm_drv2_031_buy_value_21d_diff5},
    "itm_drv2_032_buy_count_63d_slope_252d":        {"inputs": ["insider_buy_count"],                                                  "func": itm_drv2_032_buy_count_63d_slope_252d},
    "itm_drv2_033_buy_value_63d_slope_252d":        {"inputs": ["insider_buy_value"],                                                  "func": itm_drv2_033_buy_value_63d_slope_252d},
    "itm_drv2_034_sell_value_63d_diff21":           {"inputs": ["insider_sell_value"],                                                 "func": itm_drv2_034_sell_value_63d_diff21},
    "itm_drv2_035_sell_count_63d_diff21":           {"inputs": ["insider_sell_count"],                                                 "func": itm_drv2_035_sell_count_63d_diff21},
    "itm_drv2_036_net_buy_value_252d_diff21":       {"inputs": ["insider_buy_value", "insider_sell_value"],                           "func": itm_drv2_036_net_buy_value_252d_diff21},
    "itm_drv2_037_net_buy_value_252d_diff63":       {"inputs": ["insider_buy_value", "insider_sell_value"],                           "func": itm_drv2_037_net_buy_value_252d_diff63},
    "itm_drv2_038_ath_dd_slope_63d":               {"inputs": ["close"],                                                              "func": itm_drv2_038_ath_dd_slope_63d},
    "itm_drv2_039_ath_dd_slope_252d":              {"inputs": ["close"],                                                              "func": itm_drv2_039_ath_dd_slope_252d},
    "itm_drv2_040_1y_dd_diff21":                   {"inputs": ["close"],                                                              "func": itm_drv2_040_1y_dd_diff21},
    "itm_drv2_041_1y_dd_diff63":                   {"inputs": ["close"],                                                              "func": itm_drv2_041_1y_dd_diff63},
    "itm_drv2_042_buyers_63d_diff63":              {"inputs": ["insider_buyers"],                                                     "func": itm_drv2_042_buyers_63d_diff63},
    "itm_drv2_043_buyers_252d_diff21":             {"inputs": ["insider_buyers"],                                                     "func": itm_drv2_043_buyers_252d_diff21},
    "itm_drv2_044_officer_buy_value_63d_diff63":   {"inputs": ["officer_buy_value"],                                                  "func": itm_drv2_044_officer_buy_value_63d_diff63},
    "itm_drv2_045_officer_buy_x_ath_dd_diff63":    {"inputs": ["close", "officer_buy_value"],                                        "func": itm_drv2_045_officer_buy_x_ath_dd_diff63},
    "itm_drv2_046_buy_value_pct_change_252d":      {"inputs": ["insider_buy_value"],                                                  "func": itm_drv2_046_buy_value_pct_change_252d},
    "itm_drv2_047_buy_count_pct_change_63d":       {"inputs": ["insider_buy_count"],                                                  "func": itm_drv2_047_buy_count_pct_change_63d},
    "itm_drv2_048_buy_shares_63d_diff21":          {"inputs": ["insider_buy_shares"],                                                 "func": itm_drv2_048_buy_shares_63d_diff21},
    "itm_drv2_049_buy_shares_x_ath_dd_diff21":     {"inputs": ["close", "insider_buy_shares"],                                       "func": itm_drv2_049_buy_shares_x_ath_dd_diff21},
    "itm_drv2_050_ceo_buy_x_ath_dd_diff21":        {"inputs": ["close", "ceo_buy_value"],                                            "func": itm_drv2_050_ceo_buy_x_ath_dd_diff21},
    "itm_drv2_051_cfo_buy_value_63d_diff21":       {"inputs": ["cfo_buy_value"],                                                     "func": itm_drv2_051_cfo_buy_value_63d_diff21},
    "itm_drv2_052_buy_count_x_1y_dd_diff21":       {"inputs": ["close", "insider_buy_count"],                                        "func": itm_drv2_052_buy_count_x_1y_dd_diff21},
    "itm_drv2_053_buy_value_x_1y_dd_diff63":       {"inputs": ["close", "insider_buy_value"],                                        "func": itm_drv2_053_buy_value_x_1y_dd_diff63},
    "itm_drv2_054_buy_event_density_63d_diff21":   {"inputs": ["insider_buy_count"],                                                  "func": itm_drv2_054_buy_event_density_63d_diff21},
    "itm_drv2_055_buy_consistency_63d_diff63":     {"inputs": ["insider_buy_value"],                                                  "func": itm_drv2_055_buy_consistency_63d_diff63},
    "itm_drv2_056_sell_to_buy_ratio_63d_diff21":   {"inputs": ["insider_buy_value", "insider_sell_value"],                           "func": itm_drv2_056_sell_to_buy_ratio_63d_diff21},
    "itm_drv2_057_dd_depth_pct_rank_1y_diff63":    {"inputs": ["close"],                                                             "func": itm_drv2_057_dd_depth_pct_rank_1y_diff63},
    "itm_drv2_058_buy_count_x_ath_dd_diff63":      {"inputs": ["close", "insider_buy_count"],                                        "func": itm_drv2_058_buy_count_x_ath_dd_diff63},
    "itm_drv2_059_buy_value_x_ath_dd_slope_63d":   {"inputs": ["close", "insider_buy_value"],                                        "func": itm_drv2_059_buy_value_x_ath_dd_slope_63d},
    "itm_drv2_060_buyers_x_ath_dd_diff63":         {"inputs": ["close", "insider_buyers"],                                           "func": itm_drv2_060_buyers_x_ath_dd_diff63},
    "itm_drv2_061_buy_count_zscore_252d_diff21":   {"inputs": ["insider_buy_count"],                                                  "func": itm_drv2_061_buy_count_zscore_252d_diff21},
    "itm_drv2_062_net_buy_count_63d_diff21":       {"inputs": ["insider_buy_count", "insider_sell_count"],                           "func": itm_drv2_062_net_buy_count_63d_diff21},
    "itm_drv2_063_buy_count_21d_diff21":           {"inputs": ["insider_buy_count"],                                                  "func": itm_drv2_063_buy_count_21d_diff21},
    "itm_drv2_064_buy_value_21d_diff21":           {"inputs": ["insider_buy_value"],                                                  "func": itm_drv2_064_buy_value_21d_diff21},
    "itm_drv2_065_sell_value_63d_diff63":          {"inputs": ["insider_sell_value"],                                                 "func": itm_drv2_065_sell_value_63d_diff63},
    "itm_drv2_066_officer_buy_63d_slope_252d":     {"inputs": ["officer_buy_value"],                                                  "func": itm_drv2_066_officer_buy_63d_slope_252d},
    "itm_drv2_067_buy_value_x_2y_dd_diff21":       {"inputs": ["close", "insider_buy_value"],                                        "func": itm_drv2_067_buy_value_x_2y_dd_diff21},
    "itm_drv2_068_dd_pct_rank_3y_diff21":          {"inputs": ["close"],                                                             "func": itm_drv2_068_dd_pct_rank_3y_diff21},
    "itm_drv2_069_buy_count_ratio_21_to_252_diff21": {"inputs": ["insider_buy_count"],                                               "func": itm_drv2_069_buy_count_ratio_21_to_252_diff21},
    "itm_drv2_070_buy_value_consistency_252d_diff21": {"inputs": ["insider_buy_value"],                                              "func": itm_drv2_070_buy_value_consistency_252d_diff21},
    "itm_drv2_071_ceo_buy_63d_slope_63d":          {"inputs": ["ceo_buy_value"],                                                     "func": itm_drv2_071_ceo_buy_63d_slope_63d},
    "itm_drv2_072_buy_shares_252d_diff63":         {"inputs": ["insider_buy_shares"],                                                 "func": itm_drv2_072_buy_shares_252d_diff63},
    "itm_drv2_073_buy_count_x_ath_dd_slope_252d":  {"inputs": ["close", "insider_buy_count"],                                        "func": itm_drv2_073_buy_count_x_ath_dd_slope_252d},
    "itm_drv2_074_sell_value_x_ath_dd_diff21":     {"inputs": ["close", "insider_sell_value"],                                       "func": itm_drv2_074_sell_value_x_ath_dd_diff21},
    "itm_drv2_075_grand_composite_diff21":          {"inputs": ["close", "insider_buy_value", "insider_buy_count", "officer_buy_value", "insider_buyers"], "func": itm_drv2_075_grand_composite_diff21},
}
