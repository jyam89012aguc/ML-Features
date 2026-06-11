"""
87_insider_timing — 3rd Derivative Features (itm_drv3_001 to itm_drv3_075)
Domain: insider activity timing vs price drawdown depth — 2nd-order rate-of-change
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

These 3rd-derivative features compute diffs/slopes of the 2nd-derivative
concepts — i.e. acceleration of the 1st-order rate of change.  On a daily
index with sparse insider data these will be very sparse — that is EXPECTED
and correct.  Every function must return a same-length pandas Series with no
exception even when all insider series inputs are zero.

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


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _slope_ols(s: pd.Series, w: int) -> pd.Series:
    """OLS slope of s over trailing w days."""
    x   = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    cov = s.rolling(w, min_periods=max(2, w // 4)).cov(x)
    var = x.rolling(w, min_periods=max(2, w // 4)).var()
    return _safe_div(cov, var)


def _drawdown_from_expanding_high(close: pd.Series) -> pd.Series:
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _drawdown_from_rolling_high(close: pd.Series, w: int) -> pd.Series:
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


# ── Helper: reconstruct 2nd-derivative base concepts (self-contained) ─────────

def _d2_buy_count_63d_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21d diff of 63d buy count (same as drv2_001)."""
    return _rolling_sum(insider_buy_count, _TD_QTR).diff(_TD_MON)


def _d2_buy_value_63d_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21d diff of 63d buy value (same as drv2_002)."""
    return _rolling_sum(insider_buy_value, _TD_QTR).diff(_TD_MON)


def _d2_buy_value_x_ath_dd_diff21(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (63d buy value log1p * ATH DD mag) (same as drv2_008)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    return base.diff(_TD_MON)


def _d2_buy_count_x_ath_dd_diff21(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21d diff of (63d buy count * ATH DD mag) (same as drv2_007)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    return base.diff(_TD_MON)


def _d2_net_buy_63d_diff21(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21d diff of 63d net buy value (same as drv2_016)."""
    base = _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)
    return base.diff(_TD_MON)


# ── 3rd Derivative Feature Functions ─────────────────────────────────────────

def itm_drv3_001_buy_count_63d_diff21_diff21(
    insider_buy_count: pd.Series
) -> pd.Series:
    """21-day diff of the (21-day diff of 63d buy count).
    Acceleration of the buying rate change."""
    d2 = _d2_buy_count_63d_diff21(insider_buy_count)
    return d2.diff(_TD_MON)


def itm_drv3_002_buy_value_63d_diff21_diff21(
    insider_buy_value: pd.Series
) -> pd.Series:
    """21-day diff of the (21-day diff of 63d buy value).
    Acceleration of the buy value rate of change."""
    d2 = _d2_buy_value_63d_diff21(insider_buy_value)
    return d2.diff(_TD_MON)


def itm_drv3_003_buy_count_63d_diff21_diff63(
    insider_buy_count: pd.Series
) -> pd.Series:
    """63-day diff of the 21d-diff of 63d buy count (quarterly change in weekly momentum)."""
    d2 = _d2_buy_count_63d_diff21(insider_buy_count)
    return d2.diff(_TD_QTR)


def itm_drv3_004_buy_value_63d_diff21_diff63(
    insider_buy_value: pd.Series
) -> pd.Series:
    """63-day diff of the 21d-diff of 63d buy value."""
    d2 = _d2_buy_value_63d_diff21(insider_buy_value)
    return d2.diff(_TD_QTR)


def itm_drv3_005_buy_value_x_ath_dd_diff21_diff21(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of buy-value x ATH-DD product).
    2nd-order acceleration of the buy-into-decline signal."""
    d2 = _d2_buy_value_x_ath_dd_diff21(close, insider_buy_value)
    return d2.diff(_TD_MON)


def itm_drv3_006_buy_count_x_ath_dd_diff21_diff21(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of buy-count x ATH-DD product)."""
    d2 = _d2_buy_count_x_ath_dd_diff21(close, insider_buy_count)
    return d2.diff(_TD_MON)


def itm_drv3_007_buy_value_x_ath_dd_diff21_diff63(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d diff of (21d diff of buy-value x ATH-DD product)."""
    d2 = _d2_buy_value_x_ath_dd_diff21(close, insider_buy_value)
    return d2.diff(_TD_QTR)


def itm_drv3_008_ath_dd_diff21_diff21(close: pd.Series) -> pd.Series:
    """21d diff of (21d diff of ATH drawdown) — 2nd-order drawdown acceleration."""
    d2 = _drawdown_from_expanding_high(close).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_009_ath_dd_diff63_diff21(close: pd.Series) -> pd.Series:
    """21d diff of (63d diff of ATH drawdown)."""
    d2 = _drawdown_from_expanding_high(close).diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_010_buy_count_63d_slope_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21d diff of the 63d OLS slope of 63d rolling buy count."""
    slope = _slope_ols(_rolling_sum(insider_buy_count, _TD_QTR), _TD_QTR)
    return slope.diff(_TD_MON)


def itm_drv3_011_buy_value_63d_slope_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21d diff of the 63d OLS slope of 63d rolling buy value."""
    slope = _slope_ols(_rolling_sum(insider_buy_value, _TD_QTR), _TD_QTR)
    return slope.diff(_TD_MON)


def itm_drv3_012_net_buy_63d_diff21_diff21(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of 63d net buy value) — net sentiment acceleration."""
    d2 = _d2_net_buy_63d_diff21(insider_buy_value, insider_sell_value)
    return d2.diff(_TD_MON)


def itm_drv3_013_net_buy_63d_diff21_diff63(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """63d diff of (21d diff of 63d net buy value)."""
    d2 = _d2_net_buy_63d_diff21(insider_buy_value, insider_sell_value)
    return d2.diff(_TD_QTR)


def itm_drv3_014_officer_buy_63d_diff21_diff21(
    officer_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of 63d officer buy value)."""
    d2 = _rolling_sum(officer_buy_value, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_015_officer_buy_x_ath_dd_diff21_diff21(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of officer 63d buy value x ATH DD mag)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    ov63    = _rolling_sum(officer_buy_value, _TD_QTR)
    base    = np.log1p(ov63.clip(lower=0)) * dd_mag
    d2      = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_016_buyers_63d_diff21_diff21(insider_buyers: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 63d unique buyer count)."""
    d2 = _rolling_sum(insider_buyers, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_017_buy_value_z_diff21_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 252d z-score of daily buy value)."""
    z  = _zscore_rolling(insider_buy_value, _TD_YEAR)
    d2 = z.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_018_buy_count_pct_chg_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21d diff of (21d pct-change of 63d buy count) — acceleration of pct change."""
    base    = _rolling_sum(insider_buy_count, _TD_QTR)
    prev    = base.shift(_TD_MON)
    pct_chg = _safe_div(base - prev, prev.abs().replace(0, np.nan))
    return pct_chg.diff(_TD_MON)


def itm_drv3_019_dd_pct_rank_diff21_diff21(close: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 252d pct-rank of ATH drawdown)."""
    dd   = _drawdown_from_expanding_high(close)
    pct  = dd.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)
    d2   = pct.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_020_buy_value_x_ath_dd_slope_diff21(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21d diff of the 252d OLS slope of (buy value log1p * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    slope  = _slope_ols(base, _TD_YEAR)
    return slope.diff(_TD_MON)


def itm_drv3_021_buy_count_x_ath_dd_slope_diff21(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21d diff of the 63d OLS slope of (buy count * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    slope  = _slope_ols(base, _TD_QTR)
    return slope.diff(_TD_MON)


def itm_drv3_022_buy_consistency_diff21_diff21(
    insider_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of 63d buy-day fraction)."""
    nonzero = (insider_buy_value > 0).astype(float)
    base    = _rolling_mean(nonzero, _TD_QTR)
    d2      = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_023_ceo_buy_x_ath_dd_diff21_diff21(
    close: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of CEO 63d buy value x ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    cv63   = _rolling_sum(ceo_buy_value, _TD_QTR)
    base   = np.log1p(cv63.clip(lower=0)) * dd_mag
    d2     = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_024_1y_dd_diff21_diff21(close: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 1-year rolling drawdown) — 2nd-order 1y-DD acceleration."""
    d2 = _drawdown_from_rolling_high(close, _TD_YEAR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_025_composite_timing_diff21_diff21(
    close: pd.Series, insider_buy_value: pd.Series,
    insider_buy_count: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of composite insider timing score).
    Captures the acceleration of the composite signal's momentum."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    s1 = np.log1p(_rolling_sum(insider_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s2 = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    s3 = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    z1 = _zscore_rolling(s1, _TD_YEAR)
    z2 = _zscore_rolling(s2, _TD_YEAR)
    z3 = _zscore_rolling(s3, _TD_YEAR)
    composite = (z1 + z2 + z3) / 3.0
    d2 = composite.diff(_TD_MON)
    return d2.diff(_TD_MON)


# ── 3rd Derivative Feature Functions 026-075 ──────────────────────────────────

def itm_drv3_026_buy_count_252d_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 252d buy count) — acceleration of annual pace."""
    d2 = _rolling_sum(insider_buy_count, _TD_YEAR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_027_buy_value_252d_diff21_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 252d buy value)."""
    d2 = _rolling_sum(insider_buy_value, _TD_YEAR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_028_buy_count_63d_diff63_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21d diff of (63d diff of 63d buy count)."""
    d2 = _rolling_sum(insider_buy_count, _TD_QTR).diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_029_buy_value_63d_diff63_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21d diff of (63d diff of 63d buy value)."""
    d2 = _rolling_sum(insider_buy_value, _TD_QTR).diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_030_buy_count_21d_diff5_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21d diff of (5d diff of 21d buy count)."""
    d2 = _rolling_sum(insider_buy_count, _TD_MON).diff(_TD_WEEK)
    return d2.diff(_TD_MON)


def itm_drv3_031_buy_value_21d_diff5_diff21(insider_buy_value: pd.Series) -> pd.Series:
    """21d diff of (5d diff of 21d buy value)."""
    d2 = _rolling_sum(insider_buy_value, _TD_MON).diff(_TD_WEEK)
    return d2.diff(_TD_MON)


def itm_drv3_032_ath_dd_slope_63d_diff21(close: pd.Series) -> pd.Series:
    """21d diff of the 63d OLS slope of ATH drawdown."""
    slope = _slope_ols(_drawdown_from_expanding_high(close), _TD_QTR)
    return slope.diff(_TD_MON)


def itm_drv3_033_ath_dd_slope_252d_diff21(close: pd.Series) -> pd.Series:
    """21d diff of the 252d OLS slope of ATH drawdown."""
    slope = _slope_ols(_drawdown_from_expanding_high(close), _TD_YEAR)
    return slope.diff(_TD_MON)


def itm_drv3_034_1y_dd_diff21_diff21(close: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 1-year drawdown) — 2nd-order 1y-DD acceleration."""
    d2 = _drawdown_from_rolling_high(close, _TD_YEAR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_035_1y_dd_diff63_diff21(close: pd.Series) -> pd.Series:
    """21d diff of (63d diff of 1-year drawdown)."""
    d2 = _drawdown_from_rolling_high(close, _TD_YEAR).diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_036_net_buy_value_252d_diff21_diff21(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of 252d net buy value)."""
    d2 = (_rolling_sum(insider_buy_value, _TD_YEAR) - _rolling_sum(insider_sell_value, _TD_YEAR)).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_037_net_buy_value_63d_diff63_diff21(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21d diff of (63d diff of 63d net buy value)."""
    d2 = (_rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)).diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_038_sell_value_63d_diff21_diff21(insider_sell_value: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 63d sell value)."""
    d2 = _rolling_sum(insider_sell_value, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_039_sell_count_63d_diff21_diff21(insider_sell_count: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 63d sell count)."""
    d2 = _rolling_sum(insider_sell_count, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_040_buyers_63d_diff63_diff21(insider_buyers: pd.Series) -> pd.Series:
    """21d diff of (63d diff of 63d unique buyer count)."""
    d2 = _rolling_sum(insider_buyers, _TD_QTR).diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_041_buyers_x_ath_dd_diff63_diff21(
    close: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """21d diff of (63d diff of buyers x ATH DD mag)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    d2     = base.diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_042_officer_buy_63d_diff21_diff63(officer_buy_value: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 63d officer buy value)."""
    d2 = _rolling_sum(officer_buy_value, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_043_officer_buy_x_ath_dd_diff63_diff21(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (63d diff of officer 63d buy x ATH DD mag)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    ov63   = _rolling_sum(officer_buy_value, _TD_QTR)
    base   = np.log1p(ov63.clip(lower=0)) * dd_mag
    d2     = base.diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_044_buy_shares_63d_diff21_diff21(insider_buy_shares: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 63d buy shares)."""
    d2 = _rolling_sum(insider_buy_shares, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_045_buy_shares_x_ath_dd_diff21_diff21(
    close: pd.Series, insider_buy_shares: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of buy shares x ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    sh63   = _rolling_sum(insider_buy_shares, _TD_QTR)
    base   = np.log1p(sh63.clip(lower=0)) * dd_mag
    d2     = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_046_cfo_buy_value_63d_diff21_diff21(cfo_buy_value: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 63d CFO buy value)."""
    d2 = _rolling_sum(cfo_buy_value, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_047_ceo_buy_63d_diff63_diff21(ceo_buy_value: pd.Series) -> pd.Series:
    """21d diff of (63d diff of 63d CEO buy value)."""
    d2 = _rolling_sum(ceo_buy_value, _TD_QTR).diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_048_buy_value_x_1y_dd_diff21_diff21(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of 63d buy value x 1y DD mag)."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    d2     = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_049_buy_count_x_1y_dd_diff21_diff21(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of buy count x 1y DD magnitude)."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    d2     = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_050_buy_count_63d_slope_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63d diff of the 63d OLS slope of 63d rolling buy count."""
    slope = _slope_ols(_rolling_sum(insider_buy_count, _TD_QTR), _TD_QTR)
    return slope.diff(_TD_QTR)


def itm_drv3_051_buy_value_63d_slope_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63d diff of the 63d OLS slope of 63d rolling buy value."""
    slope = _slope_ols(_rolling_sum(insider_buy_value, _TD_QTR), _TD_QTR)
    return slope.diff(_TD_QTR)


def itm_drv3_052_buy_value_z_diff21_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 252d z-score of daily buy value)."""
    z  = _zscore_rolling(insider_buy_value, _TD_YEAR)
    d2 = z.diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_053_buy_count_z_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 252d z-score of daily buy count)."""
    z  = _zscore_rolling(insider_buy_count, _TD_YEAR)
    d2 = z.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_054_dd_pct_rank_1y_diff63_diff21(close: pd.Series) -> pd.Series:
    """21d diff of (63d diff of 252d pct-rank of ATH drawdown)."""
    dd  = _drawdown_from_expanding_high(close)
    pct = dd.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)
    d2  = pct.diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_055_buy_value_x_ath_dd_diff63_diff21(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (63d diff of buy value x ATH DD product)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    d2     = base.diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_056_buy_count_x_ath_dd_diff63_diff21(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21d diff of (63d diff of buy count x ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    d2     = base.diff(_TD_QTR)
    return d2.diff(_TD_MON)


def itm_drv3_057_net_buy_count_63d_diff21_diff21(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of 63d net buy count)."""
    base = _rolling_sum(insider_buy_count, _TD_QTR) - _rolling_sum(insider_sell_count, _TD_QTR)
    d2   = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_058_buy_consistency_diff21_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 63d buy-day fraction)."""
    nonzero = (insider_buy_value > 0).astype(float)
    base    = _rolling_mean(nonzero, _TD_QTR)
    d2      = base.diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_059_buy_count_pct_chg_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63d diff of (21d pct-change of 63d buy count)."""
    base    = _rolling_sum(insider_buy_count, _TD_QTR)
    prev    = base.shift(_TD_MON)
    pct_chg = _safe_div(base - prev, prev.abs().replace(0, np.nan))
    return pct_chg.diff(_TD_QTR)


def itm_drv3_060_buy_value_x_ath_dd_slope_diff63(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d diff of the 252d OLS slope of (buy value log1p * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    slope  = _slope_ols(base, _TD_YEAR)
    return slope.diff(_TD_QTR)


def itm_drv3_061_buy_count_x_ath_dd_slope_diff63(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63d diff of the 63d OLS slope of (buy count * ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    base   = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    slope  = _slope_ols(base, _TD_QTR)
    return slope.diff(_TD_QTR)


def itm_drv3_062_ceo_buy_x_ath_dd_diff21_diff63(
    close: pd.Series, ceo_buy_value: pd.Series
) -> pd.Series:
    """63d diff of (21d diff of CEO 63d buy x ATH DD magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    cv63   = _rolling_sum(ceo_buy_value, _TD_QTR)
    base   = np.log1p(cv63.clip(lower=0)) * dd_mag
    d2     = base.diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_063_1y_dd_diff21_diff63(close: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 1-year rolling drawdown)."""
    d2 = _drawdown_from_rolling_high(close, _TD_YEAR).diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_064_ath_dd_diff21_diff63(close: pd.Series) -> pd.Series:
    """63d diff of (21d diff of ATH drawdown)."""
    d2 = _drawdown_from_expanding_high(close).diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_065_officer_buy_x_ath_dd_diff21_diff63(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """63d diff of (21d diff of officer 63d buy x ATH DD mag)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    ov63   = _rolling_sum(officer_buy_value, _TD_QTR)
    base   = np.log1p(ov63.clip(lower=0)) * dd_mag
    d2     = base.diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_066_buy_count_252d_diff21_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 252d buy count)."""
    d2 = _rolling_sum(insider_buy_count, _TD_YEAR).diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_067_buy_value_252d_diff21_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 252d buy value)."""
    d2 = _rolling_sum(insider_buy_value, _TD_YEAR).diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_068_sell_value_63d_diff21_diff63(insider_sell_value: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 63d sell value)."""
    d2 = _rolling_sum(insider_sell_value, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_069_sell_to_buy_ratio_63d_diff21_diff21(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of sell/buy value ratio)."""
    buy63  = _rolling_sum(insider_buy_value, _TD_QTR)
    sell63 = _rolling_sum(insider_sell_value, _TD_QTR)
    base   = _safe_div(sell63, buy63)
    d2     = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_070_buy_value_zscore_diff21_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 252d z-score of daily buy value)."""
    base = _zscore_rolling(insider_buy_value, _TD_YEAR)
    d2   = base.diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_071_buyers_63d_diff21_diff63(insider_buyers: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 63d unique buyer count)."""
    d2 = _rolling_sum(insider_buyers, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_072_buy_shares_63d_diff21_diff63(insider_buy_shares: pd.Series) -> pd.Series:
    """63d diff of (21d diff of 63d buy shares)."""
    d2 = _rolling_sum(insider_buy_shares, _TD_QTR).diff(_TD_MON)
    return d2.diff(_TD_QTR)


def itm_drv3_073_buy_value_x_2y_dd_diff21_diff21(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of 63d buy value x 2y DD magnitude)."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_2Y).abs()
    val63  = _rolling_sum(insider_buy_value, _TD_QTR)
    base   = np.log1p(val63.clip(lower=0)) * dd_mag
    d2     = base.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_074_dd_pct_rank_3y_diff21_diff21(close: pd.Series) -> pd.Series:
    """21d diff of (21d diff of 756d pct-rank of ATH drawdown)."""
    dd  = _drawdown_from_expanding_high(close)
    pct = dd.rolling(756, min_periods=max(2, 756 // 4)).rank(pct=True)
    d2  = pct.diff(_TD_MON)
    return d2.diff(_TD_MON)


def itm_drv3_075_grand_composite_diff21_diff21(
    close: pd.Series, insider_buy_value: pd.Series,
    insider_buy_count: pd.Series, officer_buy_value: pd.Series,
    insider_buyers: pd.Series
) -> pd.Series:
    """21d diff of (21d diff of grand composite timing score)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    s1 = np.log1p(_rolling_sum(insider_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s2 = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    s3 = np.log1p(_rolling_sum(officer_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s4 = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    composite = sum(_zscore_rolling(s, _TD_YEAR) for s in (s1, s2, s3, s4)) / 4.0
    d2 = composite.diff(_TD_MON)
    return d2.diff(_TD_MON)


# ── Registry 3rd Derivatives ─────────────────────────────────────────────────

INSIDER_TIMING_REGISTRY_3RD_DERIVATIVES = {
    "itm_drv3_001_buy_count_63d_diff21_diff21":         {"inputs": ["insider_buy_count"],                                                    "func": itm_drv3_001_buy_count_63d_diff21_diff21},
    "itm_drv3_002_buy_value_63d_diff21_diff21":         {"inputs": ["insider_buy_value"],                                                    "func": itm_drv3_002_buy_value_63d_diff21_diff21},
    "itm_drv3_003_buy_count_63d_diff21_diff63":         {"inputs": ["insider_buy_count"],                                                    "func": itm_drv3_003_buy_count_63d_diff21_diff63},
    "itm_drv3_004_buy_value_63d_diff21_diff63":         {"inputs": ["insider_buy_value"],                                                    "func": itm_drv3_004_buy_value_63d_diff21_diff63},
    "itm_drv3_005_buy_value_x_ath_dd_diff21_diff21":    {"inputs": ["close", "insider_buy_value"],                                          "func": itm_drv3_005_buy_value_x_ath_dd_diff21_diff21},
    "itm_drv3_006_buy_count_x_ath_dd_diff21_diff21":    {"inputs": ["close", "insider_buy_count"],                                          "func": itm_drv3_006_buy_count_x_ath_dd_diff21_diff21},
    "itm_drv3_007_buy_value_x_ath_dd_diff21_diff63":    {"inputs": ["close", "insider_buy_value"],                                          "func": itm_drv3_007_buy_value_x_ath_dd_diff21_diff63},
    "itm_drv3_008_ath_dd_diff21_diff21":                {"inputs": ["close"],                                                               "func": itm_drv3_008_ath_dd_diff21_diff21},
    "itm_drv3_009_ath_dd_diff63_diff21":                {"inputs": ["close"],                                                               "func": itm_drv3_009_ath_dd_diff63_diff21},
    "itm_drv3_010_buy_count_63d_slope_diff21":          {"inputs": ["insider_buy_count"],                                                   "func": itm_drv3_010_buy_count_63d_slope_diff21},
    "itm_drv3_011_buy_value_63d_slope_diff21":          {"inputs": ["insider_buy_value"],                                                   "func": itm_drv3_011_buy_value_63d_slope_diff21},
    "itm_drv3_012_net_buy_63d_diff21_diff21":           {"inputs": ["insider_buy_value", "insider_sell_value"],                             "func": itm_drv3_012_net_buy_63d_diff21_diff21},
    "itm_drv3_013_net_buy_63d_diff21_diff63":           {"inputs": ["insider_buy_value", "insider_sell_value"],                             "func": itm_drv3_013_net_buy_63d_diff21_diff63},
    "itm_drv3_014_officer_buy_63d_diff21_diff21":       {"inputs": ["officer_buy_value"],                                                   "func": itm_drv3_014_officer_buy_63d_diff21_diff21},
    "itm_drv3_015_officer_buy_x_ath_dd_diff21_diff21":  {"inputs": ["close", "officer_buy_value"],                                         "func": itm_drv3_015_officer_buy_x_ath_dd_diff21_diff21},
    "itm_drv3_016_buyers_63d_diff21_diff21":            {"inputs": ["insider_buyers"],                                                      "func": itm_drv3_016_buyers_63d_diff21_diff21},
    "itm_drv3_017_buy_value_z_diff21_diff21":           {"inputs": ["insider_buy_value"],                                                   "func": itm_drv3_017_buy_value_z_diff21_diff21},
    "itm_drv3_018_buy_count_pct_chg_diff21":            {"inputs": ["insider_buy_count"],                                                   "func": itm_drv3_018_buy_count_pct_chg_diff21},
    "itm_drv3_019_dd_pct_rank_diff21_diff21":           {"inputs": ["close"],                                                               "func": itm_drv3_019_dd_pct_rank_diff21_diff21},
    "itm_drv3_020_buy_value_x_ath_dd_slope_diff21":     {"inputs": ["close", "insider_buy_value"],                                         "func": itm_drv3_020_buy_value_x_ath_dd_slope_diff21},
    "itm_drv3_021_buy_count_x_ath_dd_slope_diff21":     {"inputs": ["close", "insider_buy_count"],                                         "func": itm_drv3_021_buy_count_x_ath_dd_slope_diff21},
    "itm_drv3_022_buy_consistency_diff21_diff21":       {"inputs": ["insider_buy_value"],                                                   "func": itm_drv3_022_buy_consistency_diff21_diff21},
    "itm_drv3_023_ceo_buy_x_ath_dd_diff21_diff21":      {"inputs": ["close", "ceo_buy_value"],                                             "func": itm_drv3_023_ceo_buy_x_ath_dd_diff21_diff21},
    "itm_drv3_024_1y_dd_diff21_diff21":                 {"inputs": ["close"],                                                               "func": itm_drv3_024_1y_dd_diff21_diff21},
    "itm_drv3_025_composite_timing_diff21_diff21":      {"inputs": ["close", "insider_buy_value", "insider_buy_count", "insider_buyers"],    "func": itm_drv3_025_composite_timing_diff21_diff21},
    "itm_drv3_026_buy_count_252d_diff21_diff21":        {"inputs": ["insider_buy_count"],                                                    "func": itm_drv3_026_buy_count_252d_diff21_diff21},
    "itm_drv3_027_buy_value_252d_diff21_diff21":        {"inputs": ["insider_buy_value"],                                                    "func": itm_drv3_027_buy_value_252d_diff21_diff21},
    "itm_drv3_028_buy_count_63d_diff63_diff21":         {"inputs": ["insider_buy_count"],                                                    "func": itm_drv3_028_buy_count_63d_diff63_diff21},
    "itm_drv3_029_buy_value_63d_diff63_diff21":         {"inputs": ["insider_buy_value"],                                                    "func": itm_drv3_029_buy_value_63d_diff63_diff21},
    "itm_drv3_030_buy_count_21d_diff5_diff21":          {"inputs": ["insider_buy_count"],                                                    "func": itm_drv3_030_buy_count_21d_diff5_diff21},
    "itm_drv3_031_buy_value_21d_diff5_diff21":          {"inputs": ["insider_buy_value"],                                                    "func": itm_drv3_031_buy_value_21d_diff5_diff21},
    "itm_drv3_032_ath_dd_slope_63d_diff21":             {"inputs": ["close"],                                                               "func": itm_drv3_032_ath_dd_slope_63d_diff21},
    "itm_drv3_033_ath_dd_slope_252d_diff21":            {"inputs": ["close"],                                                               "func": itm_drv3_033_ath_dd_slope_252d_diff21},
    "itm_drv3_034_1y_dd_diff21_diff21":                 {"inputs": ["close"],                                                               "func": itm_drv3_034_1y_dd_diff21_diff21},
    "itm_drv3_035_1y_dd_diff63_diff21":                 {"inputs": ["close"],                                                               "func": itm_drv3_035_1y_dd_diff63_diff21},
    "itm_drv3_036_net_buy_value_252d_diff21_diff21":    {"inputs": ["insider_buy_value", "insider_sell_value"],                             "func": itm_drv3_036_net_buy_value_252d_diff21_diff21},
    "itm_drv3_037_net_buy_value_63d_diff63_diff21":     {"inputs": ["insider_buy_value", "insider_sell_value"],                             "func": itm_drv3_037_net_buy_value_63d_diff63_diff21},
    "itm_drv3_038_sell_value_63d_diff21_diff21":        {"inputs": ["insider_sell_value"],                                                  "func": itm_drv3_038_sell_value_63d_diff21_diff21},
    "itm_drv3_039_sell_count_63d_diff21_diff21":        {"inputs": ["insider_sell_count"],                                                  "func": itm_drv3_039_sell_count_63d_diff21_diff21},
    "itm_drv3_040_buyers_63d_diff63_diff21":            {"inputs": ["insider_buyers"],                                                      "func": itm_drv3_040_buyers_63d_diff63_diff21},
    "itm_drv3_041_buyers_x_ath_dd_diff63_diff21":       {"inputs": ["close", "insider_buyers"],                                            "func": itm_drv3_041_buyers_x_ath_dd_diff63_diff21},
    "itm_drv3_042_officer_buy_63d_diff21_diff63":       {"inputs": ["officer_buy_value"],                                                   "func": itm_drv3_042_officer_buy_63d_diff21_diff63},
    "itm_drv3_043_officer_buy_x_ath_dd_diff63_diff21":  {"inputs": ["close", "officer_buy_value"],                                         "func": itm_drv3_043_officer_buy_x_ath_dd_diff63_diff21},
    "itm_drv3_044_buy_shares_63d_diff21_diff21":        {"inputs": ["insider_buy_shares"],                                                  "func": itm_drv3_044_buy_shares_63d_diff21_diff21},
    "itm_drv3_045_buy_shares_x_ath_dd_diff21_diff21":   {"inputs": ["close", "insider_buy_shares"],                                        "func": itm_drv3_045_buy_shares_x_ath_dd_diff21_diff21},
    "itm_drv3_046_cfo_buy_value_63d_diff21_diff21":     {"inputs": ["cfo_buy_value"],                                                      "func": itm_drv3_046_cfo_buy_value_63d_diff21_diff21},
    "itm_drv3_047_ceo_buy_63d_diff63_diff21":           {"inputs": ["ceo_buy_value"],                                                      "func": itm_drv3_047_ceo_buy_63d_diff63_diff21},
    "itm_drv3_048_buy_value_x_1y_dd_diff21_diff21":     {"inputs": ["close", "insider_buy_value"],                                         "func": itm_drv3_048_buy_value_x_1y_dd_diff21_diff21},
    "itm_drv3_049_buy_count_x_1y_dd_diff21_diff21":     {"inputs": ["close", "insider_buy_count"],                                         "func": itm_drv3_049_buy_count_x_1y_dd_diff21_diff21},
    "itm_drv3_050_buy_count_63d_slope_diff63":          {"inputs": ["insider_buy_count"],                                                   "func": itm_drv3_050_buy_count_63d_slope_diff63},
    "itm_drv3_051_buy_value_63d_slope_diff63":          {"inputs": ["insider_buy_value"],                                                   "func": itm_drv3_051_buy_value_63d_slope_diff63},
    "itm_drv3_052_buy_value_z_diff21_diff63":           {"inputs": ["insider_buy_value"],                                                   "func": itm_drv3_052_buy_value_z_diff21_diff63},
    "itm_drv3_053_buy_count_z_diff21_diff21":           {"inputs": ["insider_buy_count"],                                                   "func": itm_drv3_053_buy_count_z_diff21_diff21},
    "itm_drv3_054_dd_pct_rank_1y_diff63_diff21":        {"inputs": ["close"],                                                               "func": itm_drv3_054_dd_pct_rank_1y_diff63_diff21},
    "itm_drv3_055_buy_value_x_ath_dd_diff63_diff21":    {"inputs": ["close", "insider_buy_value"],                                         "func": itm_drv3_055_buy_value_x_ath_dd_diff63_diff21},
    "itm_drv3_056_buy_count_x_ath_dd_diff63_diff21":    {"inputs": ["close", "insider_buy_count"],                                         "func": itm_drv3_056_buy_count_x_ath_dd_diff63_diff21},
    "itm_drv3_057_net_buy_count_63d_diff21_diff21":     {"inputs": ["insider_buy_count", "insider_sell_count"],                            "func": itm_drv3_057_net_buy_count_63d_diff21_diff21},
    "itm_drv3_058_buy_consistency_diff21_diff63":       {"inputs": ["insider_buy_value"],                                                   "func": itm_drv3_058_buy_consistency_diff21_diff63},
    "itm_drv3_059_buy_count_pct_chg_diff63":            {"inputs": ["insider_buy_count"],                                                   "func": itm_drv3_059_buy_count_pct_chg_diff63},
    "itm_drv3_060_buy_value_x_ath_dd_slope_diff63":     {"inputs": ["close", "insider_buy_value"],                                         "func": itm_drv3_060_buy_value_x_ath_dd_slope_diff63},
    "itm_drv3_061_buy_count_x_ath_dd_slope_diff63":     {"inputs": ["close", "insider_buy_count"],                                         "func": itm_drv3_061_buy_count_x_ath_dd_slope_diff63},
    "itm_drv3_062_ceo_buy_x_ath_dd_diff21_diff63":      {"inputs": ["close", "ceo_buy_value"],                                             "func": itm_drv3_062_ceo_buy_x_ath_dd_diff21_diff63},
    "itm_drv3_063_1y_dd_diff21_diff63":                 {"inputs": ["close"],                                                               "func": itm_drv3_063_1y_dd_diff21_diff63},
    "itm_drv3_064_ath_dd_diff21_diff63":                {"inputs": ["close"],                                                               "func": itm_drv3_064_ath_dd_diff21_diff63},
    "itm_drv3_065_officer_buy_x_ath_dd_diff21_diff63":  {"inputs": ["close", "officer_buy_value"],                                         "func": itm_drv3_065_officer_buy_x_ath_dd_diff21_diff63},
    "itm_drv3_066_buy_count_252d_diff21_diff63":        {"inputs": ["insider_buy_count"],                                                   "func": itm_drv3_066_buy_count_252d_diff21_diff63},
    "itm_drv3_067_buy_value_252d_diff21_diff63":        {"inputs": ["insider_buy_value"],                                                   "func": itm_drv3_067_buy_value_252d_diff21_diff63},
    "itm_drv3_068_sell_value_63d_diff21_diff63":        {"inputs": ["insider_sell_value"],                                                  "func": itm_drv3_068_sell_value_63d_diff21_diff63},
    "itm_drv3_069_sell_to_buy_ratio_63d_diff21_diff21": {"inputs": ["insider_buy_value", "insider_sell_value"],                            "func": itm_drv3_069_sell_to_buy_ratio_63d_diff21_diff21},
    "itm_drv3_070_buy_value_zscore_diff21_diff63":      {"inputs": ["insider_buy_value"],                                                   "func": itm_drv3_070_buy_value_zscore_diff21_diff63},
    "itm_drv3_071_buyers_63d_diff21_diff63":            {"inputs": ["insider_buyers"],                                                      "func": itm_drv3_071_buyers_63d_diff21_diff63},
    "itm_drv3_072_buy_shares_63d_diff21_diff63":        {"inputs": ["insider_buy_shares"],                                                  "func": itm_drv3_072_buy_shares_63d_diff21_diff63},
    "itm_drv3_073_buy_value_x_2y_dd_diff21_diff21":     {"inputs": ["close", "insider_buy_value"],                                         "func": itm_drv3_073_buy_value_x_2y_dd_diff21_diff21},
    "itm_drv3_074_dd_pct_rank_3y_diff21_diff21":        {"inputs": ["close"],                                                               "func": itm_drv3_074_dd_pct_rank_3y_diff21_diff21},
    "itm_drv3_075_grand_composite_diff21_diff21":       {"inputs": ["close", "insider_buy_value", "insider_buy_count", "officer_buy_value", "insider_buyers"], "func": itm_drv3_075_grand_composite_diff21_diff21},
}
