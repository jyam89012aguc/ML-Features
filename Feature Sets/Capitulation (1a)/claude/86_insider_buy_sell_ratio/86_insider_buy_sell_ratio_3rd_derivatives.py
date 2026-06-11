"""
86_insider_buy_sell_ratio — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative buy/sell balance features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
Inputs to all feature functions are daily-frequency pandas Series aggregated
from Sharadar SF2 insider transaction filings.  Each row represents one
(ticker, date); most days have ZERO activity — positive values appear only on
filing days.  Do NOT forward-fill these series.

The 3rd-derivative series are extremely sparse on the daily index because
the underlying event-driven data is mostly zero — this is correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().

Primary fields used in this file (all lowercase canonical names):
  insider_buy_count, insider_sell_count,
  insider_buy_shares, insider_sell_shares,
  insider_buy_value, insider_sell_value,
  insider_buyers, insider_sellers,
  officer_buy_value, officer_sell_value,
  director_buy_value, director_sell_value
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_W5   = 5
_W21  = 21
_W63  = 63
_W126 = 126
_W252 = 252
_W504 = 504
_EPS  = 1e-9

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


# ── Base and 2nd-derivative concept helpers (self-contained) ─────────────────

def _buy_fraction(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    sb = _rolling_sum(buy, w)
    ss = _rolling_sum(sell, w)
    return _safe_div(sb, sb + ss)


def _net_flow_value(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    return _rolling_sum(buy, w) - _rolling_sum(sell, w)


def _net_flow_count(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    return _rolling_sum(buy, w) - _rolling_sum(sell, w)


def _net_flow_norm(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    sb = _rolling_sum(buy, w)
    ss = _rolling_sum(sell, w)
    return _safe_div(sb - ss, sb + ss)


def _value_ratio(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    return _safe_div(_rolling_sum(buy, w), _rolling_sum(sell, w))


def _count_ratio(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    return _safe_div(_rolling_sum(buy, w), _rolling_sum(sell, w))


def _sell_pressure(sell: pd.Series, buy: pd.Series, w: int) -> pd.Series:
    ss = _rolling_sum(sell, w)
    sb = _rolling_sum(buy, w)
    return _safe_div(ss, sb + ss)


# 2nd-derivative helpers (diff of base concept, then we diff again for 3rd)

def _drv2_value_ratio_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _value_ratio(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_count_ratio_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _count_ratio(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_buy_fraction_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _buy_fraction(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_value_net_flow_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _net_flow_value(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_count_net_flow_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _net_flow_count(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_net_flow_norm_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _net_flow_norm(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_buyer_fraction_63d_21d_diff(buyers: pd.Series, sellers: pd.Series) -> pd.Series:
    base = _buy_fraction(buyers, sellers, _W63)
    return base - base.shift(_W21)


def _drv2_sell_pressure_63d_21d_diff(sell: pd.Series, buy: pd.Series) -> pd.Series:
    base = _sell_pressure(sell, buy, _W63)
    return base - base.shift(_W21)


def _drv2_value_ratio_252d_63d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _value_ratio(buy, sell, _W252)
    return base - base.shift(_W63)


def _drv2_buy_fraction_252d_63d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _buy_fraction(buy, sell, _W252)
    return base - base.shift(_W63)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def ibr_drv3_001_value_ratio_63d_diff_21d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative value-ratio-63d-21d-diff.
    Captures jerk (acceleration of acceleration) in quarterly buy/sell balance."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_002_value_ratio_63d_diff_63d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative value-ratio-63d-21d-diff."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_003_count_ratio_63d_diff_21d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative count-ratio-63d-21d-diff."""
    drv2 = _drv2_count_ratio_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_004_buy_fraction_63d_diff_21d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative buy-fraction-63d-21d-diff."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_005_value_net_flow_63d_diff_21d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative value-net-flow-63d-21d-diff."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_006_count_net_flow_63d_diff_21d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative count-net-flow-63d-21d-diff."""
    drv2 = _drv2_count_net_flow_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_007_net_flow_norm_63d_diff_21d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative net-flow-norm-63d-21d-diff."""
    drv2 = _drv2_net_flow_norm_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_008_buyer_fraction_63d_diff_21d_again(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative buyer-fraction-63d-21d-diff."""
    drv2 = _drv2_buyer_fraction_63d_21d_diff(insider_buyers, insider_sellers)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_009_sell_pressure_63d_diff_21d_again(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative sell-pressure-63d-21d-diff."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_010_value_ratio_252d_diff_63d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative value-ratio-252d-63d-diff."""
    drv2 = _drv2_value_ratio_252d_63d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_011_value_ratio_63d_diff_slope_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """
    OLS slope of the 2nd-derivative value-ratio-63d-21d-diff series over
    a trailing 252-day window — trend in the acceleration of buy/sell balance.
    """
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = np.nanmean(arr)
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.nansum((x - xm) * (arr - ym)) / denom)

    return drv2.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_drv3_012_buy_fraction_63d_diff_63d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative buy-fraction-63d-21d-diff."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_013_value_net_flow_63d_diff_63d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative value-net-flow-63d-21d-diff."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_014_count_ratio_63d_diff_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    OLS slope of the 2nd-derivative count-ratio-63d-21d-diff series over
    a trailing 252-day window.
    """
    drv2 = _drv2_count_ratio_63d_21d_diff(insider_buy_count, insider_sell_count)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = np.nanmean(arr)
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.nansum((x - xm) * (arr - ym)) / denom)

    return drv2.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_drv3_015_net_flow_norm_63d_diff_63d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative net-flow-norm-63d-21d-diff."""
    drv2 = _drv2_net_flow_norm_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_016_buy_fraction_252d_diff_63d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative buy-fraction-252d-63d-diff."""
    drv2 = _drv2_buy_fraction_252d_63d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_017_buyer_fraction_63d_diff_63d_again(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative buyer-fraction-63d-21d-diff."""
    drv2 = _drv2_buyer_fraction_63d_21d_diff(insider_buyers, insider_sellers)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_018_value_net_flow_norm_diff_21d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative net-flow-norm-63d-21d-diff (short-lag jerk)."""
    drv2 = _drv2_net_flow_norm_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W5)


def ibr_drv3_019_count_net_flow_63d_diff_63d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative count-net-flow-63d-21d-diff."""
    drv2 = _drv2_count_net_flow_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_020_sell_pressure_63d_diff_63d_again(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative sell-pressure-63d-21d-diff."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_021_value_ratio_diff_ewm_deviation(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """
    3rd-order signal: 2nd-derivative value-ratio-63d-21d-diff minus its own
    EWM (span=63). Measures whether the current acceleration is above its recent trend.
    """
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    ewm  = drv2.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_022_buy_fraction_diff_ewm_deviation(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    3rd-order signal: 2nd-derivative buy-fraction-63d-21d-diff minus its own
    EWM (span=63).
    """
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    ewm  = drv2.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_023_net_flow_diff_ewm_deviation(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """
    3rd-order signal: 2nd-derivative value-net-flow-63d-21d-diff minus its own
    EWM (span=63).
    """
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    ewm  = drv2.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_024_count_ratio_diff_ewm_deviation(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    3rd-order signal: 2nd-derivative count-ratio-63d-21d-diff minus its own
    EWM (span=63).
    """
    drv2 = _drv2_count_ratio_63d_21d_diff(insider_buy_count, insider_sell_count)
    ewm  = drv2.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_025_sell_pressure_diff_ewm_deviation(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd-order signal: 2nd-derivative sell-pressure-63d-21d-diff minus its own
    EWM (span=63). Captures whether sell-pressure acceleration is above its trend.
    """
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    ewm  = drv2.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return drv2 - ewm


# --- Additional 2nd-derivative helpers for 3rd-derivative features 026-075 ---

def _drv2_value_ratio_252d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _value_ratio(buy, sell, _W252)
    return base - base.shift(_W21)


def _drv2_count_net_flow_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _net_flow_count(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_share_buy_fraction_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _buy_fraction(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_officer_net_flow_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _net_flow_value(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_director_net_flow_63d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _net_flow_value(buy, sell, _W63)
    return base - base.shift(_W21)


def _drv2_value_net_flow_63d_63d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _net_flow_value(buy, sell, _W63)
    return base - base.shift(_W63)


def _drv2_count_ratio_63d_63d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _count_ratio(buy, sell, _W63)
    return base - base.shift(_W63)


def _drv2_buy_fraction_252d_21d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _buy_fraction(buy, sell, _W252)
    return base - base.shift(_W21)


def _drv2_sell_pressure_252d_63d_diff(sell: pd.Series, buy: pd.Series) -> pd.Series:
    base = _sell_pressure(sell, buy, _W252)
    return base - base.shift(_W63)


def _drv2_net_flow_norm_252d_63d_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    base = _net_flow_norm(buy, sell, _W252)
    return base - base.shift(_W63)


# --- 3rd derivatives 026-075 ---

def ibr_drv3_026_value_ratio_252d_diff_21d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative value-ratio-252d-21d-diff."""
    drv2 = _drv2_value_ratio_252d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_027_count_net_flow_63d_diff_21d_again_b(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative count-net-flow-63d-21d-diff (independent copy)."""
    drv2 = _drv2_count_net_flow_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_028_share_buy_fraction_63d_diff_21d_again(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative share-buy-fraction-63d-21d-diff."""
    drv2 = _drv2_share_buy_fraction_63d_21d_diff(insider_buy_shares, insider_sell_shares)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_029_officer_net_flow_diff_21d_again(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative officer-net-flow-63d-21d-diff."""
    drv2 = _drv2_officer_net_flow_63d_21d_diff(officer_buy_value, officer_sell_value)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_030_director_net_flow_diff_21d_again(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative director-net-flow-63d-21d-diff."""
    drv2 = _drv2_director_net_flow_63d_21d_diff(director_buy_value, director_sell_value)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_031_value_net_flow_63d_diff_21d_again_b(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative value-net-flow-63d-63d-diff."""
    drv2 = _drv2_value_net_flow_63d_63d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_032_count_ratio_63d_diff_63d_again_b(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative count-ratio-63d-63d-diff."""
    drv2 = _drv2_count_ratio_63d_63d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_033_buy_fraction_252d_diff_21d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of 2nd-derivative buy-fraction-252d-21d-diff."""
    drv2 = _drv2_buy_fraction_252d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W21)


def ibr_drv3_034_sell_pressure_252d_diff_63d_again(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative sell-pressure-252d-63d-diff."""
    drv2 = _drv2_sell_pressure_252d_63d_diff(insider_sell_value, insider_buy_value)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_035_net_flow_norm_252d_diff_63d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of 2nd-derivative net-flow-norm-252d-63d-diff."""
    drv2 = _drv2_net_flow_norm_252d_63d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W63)


def ibr_drv3_036_value_ratio_diff_ewm_deviation_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative value-ratio-63d-21d-diff minus its EWM (span=126)."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    ewm  = drv2.ewm(span=_W126, min_periods=max(1, _W126 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_037_buy_fraction_diff_ewm_deviation_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative buy-fraction-63d-21d-diff minus its EWM (span=126)."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    ewm  = drv2.ewm(span=_W126, min_periods=max(1, _W126 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_038_net_flow_diff_ewm_deviation_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative value-net-flow-63d-21d-diff minus its EWM (span=126)."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    ewm  = drv2.ewm(span=_W126, min_periods=max(1, _W126 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_039_count_ratio_diff_ewm_deviation_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative count-ratio-63d-21d-diff minus its EWM (span=126)."""
    drv2 = _drv2_count_ratio_63d_21d_diff(insider_buy_count, insider_sell_count)
    ewm  = drv2.ewm(span=_W126, min_periods=max(1, _W126 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_040_sell_pressure_diff_ewm_deviation_126d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative sell-pressure-63d-21d-diff minus its EWM (span=126)."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    ewm  = drv2.ewm(span=_W126, min_periods=max(1, _W126 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_041_value_ratio_diff_slope_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of 2nd-derivative value-ratio-63d-21d-diff over trailing 63-day window."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return drv2.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_drv3_042_buy_fraction_diff_slope_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of 2nd-derivative buy-fraction-63d-21d-diff over trailing 63-day window."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return drv2.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_drv3_043_net_flow_diff_slope_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of 2nd-derivative value-net-flow-63d-21d-diff over trailing 63-day window."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return drv2.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_drv3_044_sell_pressure_diff_slope_63d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """OLS slope of 2nd-derivative sell-pressure-63d-21d-diff over trailing 63-day window."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return drv2.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_drv3_045_buyer_fraction_diff_slope_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """OLS slope of 2nd-derivative buyer-fraction-63d-21d-diff over trailing 63-day window."""
    drv2 = _drv2_buyer_fraction_63d_21d_diff(insider_buyers, insider_sellers)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return drv2.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_drv3_046_value_ratio_63d_diff_5d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of the 2nd-derivative value-ratio-63d-21d-diff (ultra-short jerk)."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W5)


def ibr_drv3_047_count_ratio_63d_diff_5d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of the 2nd-derivative count-ratio-63d-21d-diff."""
    drv2 = _drv2_count_ratio_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W5)


def ibr_drv3_048_buy_fraction_63d_diff_5d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of the 2nd-derivative buy-fraction-63d-21d-diff."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W5)


def ibr_drv3_049_net_flow_63d_diff_5d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of the 2nd-derivative value-net-flow-63d-21d-diff."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W5)


def ibr_drv3_050_sell_pressure_63d_diff_5d_again(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of the 2nd-derivative sell-pressure-63d-21d-diff."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    return drv2 - drv2.shift(_W5)


def ibr_drv3_051_value_ratio_diff_zscore_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative value-ratio-63d-21d-diff within a 252-day window."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    m  = _rolling_mean(drv2, _W252)
    sd = _rolling_std(drv2, _W252)
    return _safe_div(drv2 - m, sd)


def ibr_drv3_052_count_ratio_diff_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative count-ratio-63d-21d-diff within a 252-day window."""
    drv2 = _drv2_count_ratio_63d_21d_diff(insider_buy_count, insider_sell_count)
    m  = _rolling_mean(drv2, _W252)
    sd = _rolling_std(drv2, _W252)
    return _safe_div(drv2 - m, sd)


def ibr_drv3_053_buy_fraction_diff_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative buy-fraction-63d-21d-diff within a 252-day window."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    m  = _rolling_mean(drv2, _W252)
    sd = _rolling_std(drv2, _W252)
    return _safe_div(drv2 - m, sd)


def ibr_drv3_054_net_flow_diff_zscore_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative value-net-flow-63d-21d-diff within a 252-day window."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    m  = _rolling_mean(drv2, _W252)
    sd = _rolling_std(drv2, _W252)
    return _safe_div(drv2 - m, sd)


def ibr_drv3_055_sell_pressure_diff_zscore_252d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative sell-pressure-63d-21d-diff within a 252-day window."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    m  = _rolling_mean(drv2, _W252)
    sd = _rolling_std(drv2, _W252)
    return _safe_div(drv2 - m, sd)


def ibr_drv3_056_buyer_fraction_diff_zscore_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative buyer-fraction-63d-21d-diff within a 252-day window."""
    drv2 = _drv2_buyer_fraction_63d_21d_diff(insider_buyers, insider_sellers)
    m  = _rolling_mean(drv2, _W252)
    sd = _rolling_std(drv2, _W252)
    return _safe_div(drv2 - m, sd)


def ibr_drv3_057_value_ratio_diff_pct_rank_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-derivative value-ratio-63d-21d-diff within 252-day history."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2.rolling(_W252, min_periods=max(2, _W252 // 4)).rank(pct=True)


def ibr_drv3_058_buy_fraction_diff_pct_rank_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-derivative buy-fraction-63d-21d-diff within 252-day history."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2.rolling(_W252, min_periods=max(2, _W252 // 4)).rank(pct=True)


def ibr_drv3_059_net_flow_diff_pct_rank_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-derivative value-net-flow-63d-21d-diff within 252-day history."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2.rolling(_W252, min_periods=max(2, _W252 // 4)).rank(pct=True)


def ibr_drv3_060_sell_pressure_diff_pct_rank_252d(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-derivative sell-pressure-63d-21d-diff within 252-day history."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    return drv2.rolling(_W252, min_periods=max(2, _W252 // 4)).rank(pct=True)


def ibr_drv3_061_value_ratio_63d_diff_126d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 126-day diff of the 2nd-derivative value-ratio-63d-21d-diff."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W126)


def ibr_drv3_062_count_ratio_63d_diff_126d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 126-day diff of the 2nd-derivative count-ratio-63d-21d-diff."""
    drv2 = _drv2_count_ratio_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W126)


def ibr_drv3_063_buy_fraction_63d_diff_126d_again(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd derivative: 126-day diff of the 2nd-derivative buy-fraction-63d-21d-diff."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    return drv2 - drv2.shift(_W126)


def ibr_drv3_064_net_flow_63d_diff_126d_again(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 126-day diff of the 2nd-derivative value-net-flow-63d-21d-diff."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    return drv2 - drv2.shift(_W126)


def ibr_drv3_065_sell_pressure_diff_126d_again(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 126-day diff of the 2nd-derivative sell-pressure-63d-21d-diff."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    return drv2 - drv2.shift(_W126)


def ibr_drv3_066_value_ratio_diff_ewm21_deviation(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative value-ratio-63d-21d-diff minus its EWM (span=21)."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    ewm  = drv2.ewm(span=_W21, min_periods=max(1, _W21 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_067_buy_fraction_diff_ewm21_deviation(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative buy-fraction-63d-21d-diff minus its EWM (span=21)."""
    drv2 = _drv2_buy_fraction_63d_21d_diff(insider_buy_count, insider_sell_count)
    ewm  = drv2.ewm(span=_W21, min_periods=max(1, _W21 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_068_net_flow_diff_ewm21_deviation(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative value-net-flow-63d-21d-diff minus its EWM (span=21)."""
    drv2 = _drv2_value_net_flow_63d_21d_diff(insider_buy_value, insider_sell_value)
    ewm  = drv2.ewm(span=_W21, min_periods=max(1, _W21 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_069_sell_pressure_diff_ewm21_deviation(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative sell-pressure-63d-21d-diff minus its EWM (span=21)."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    ewm  = drv2.ewm(span=_W21, min_periods=max(1, _W21 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_070_buyer_fraction_diff_ewm21_deviation(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """3rd-order: 2nd-derivative buyer-fraction-63d-21d-diff minus its EWM (span=21)."""
    drv2 = _drv2_buyer_fraction_63d_21d_diff(insider_buyers, insider_sellers)
    ewm  = drv2.ewm(span=_W21, min_periods=max(1, _W21 // 4)).mean()
    return drv2 - ewm


def ibr_drv3_071_value_ratio_252d_diff_63d_slope(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of 2nd-derivative value-ratio-252d-63d-diff over trailing 252-day window."""
    drv2 = _drv2_value_ratio_252d_63d_diff(insider_buy_value, insider_sell_value)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return drv2.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_drv3_072_buy_fraction_252d_diff_63d_slope(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of 2nd-derivative buy-fraction-252d-63d-diff over trailing 252-day window."""
    drv2 = _drv2_buy_fraction_252d_63d_diff(insider_buy_value, insider_sell_value)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return drv2.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_drv3_073_net_flow_norm_63d_diff_slope_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of 2nd-derivative net-flow-norm-63d-21d-diff over trailing 63-day window."""
    drv2 = _drv2_net_flow_norm_63d_21d_diff(insider_buy_value, insider_sell_value)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return drv2.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_drv3_074_value_ratio_63d_diff_expanding_zscore(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Expanding z-score of 2nd-derivative value-ratio-63d-21d-diff — all-history jerk signal."""
    drv2 = _drv2_value_ratio_63d_21d_diff(insider_buy_value, insider_sell_value)
    m  = drv2.expanding(min_periods=2).mean()
    sd = drv2.expanding(min_periods=2).std()
    return _safe_div(drv2 - m, sd)


def ibr_drv3_075_sell_pressure_diff_expanding_zscore(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of 2nd-derivative sell-pressure-63d-21d-diff — all-history jerk signal."""
    drv2 = _drv2_sell_pressure_63d_21d_diff(insider_sell_value, insider_buy_value)
    m  = drv2.expanding(min_periods=2).mean()
    sd = drv2.expanding(min_periods=2).std()
    return _safe_div(drv2 - m, sd)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

INSIDER_BUY_SELL_RATIO_REGISTRY_3RD_DERIVATIVES = {
    "ibr_drv3_001_value_ratio_63d_diff_21d_again":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_001_value_ratio_63d_diff_21d_again},
    "ibr_drv3_002_value_ratio_63d_diff_63d_again":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_002_value_ratio_63d_diff_63d_again},
    "ibr_drv3_003_count_ratio_63d_diff_21d_again":      {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_003_count_ratio_63d_diff_21d_again},
    "ibr_drv3_004_buy_fraction_63d_diff_21d_again":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_004_buy_fraction_63d_diff_21d_again},
    "ibr_drv3_005_value_net_flow_63d_diff_21d_again":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_005_value_net_flow_63d_diff_21d_again},
    "ibr_drv3_006_count_net_flow_63d_diff_21d_again":   {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_006_count_net_flow_63d_diff_21d_again},
    "ibr_drv3_007_net_flow_norm_63d_diff_21d_again":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_007_net_flow_norm_63d_diff_21d_again},
    "ibr_drv3_008_buyer_fraction_63d_diff_21d_again":   {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv3_008_buyer_fraction_63d_diff_21d_again},
    "ibr_drv3_009_sell_pressure_63d_diff_21d_again":    {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_009_sell_pressure_63d_diff_21d_again},
    "ibr_drv3_010_value_ratio_252d_diff_63d_again":     {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_010_value_ratio_252d_diff_63d_again},
    "ibr_drv3_011_value_ratio_63d_diff_slope_252d":     {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_011_value_ratio_63d_diff_slope_252d},
    "ibr_drv3_012_buy_fraction_63d_diff_63d_again":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_012_buy_fraction_63d_diff_63d_again},
    "ibr_drv3_013_value_net_flow_63d_diff_63d_again":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_013_value_net_flow_63d_diff_63d_again},
    "ibr_drv3_014_count_ratio_63d_diff_slope_252d":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_014_count_ratio_63d_diff_slope_252d},
    "ibr_drv3_015_net_flow_norm_63d_diff_63d_again":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_015_net_flow_norm_63d_diff_63d_again},
    "ibr_drv3_016_buy_fraction_252d_diff_63d_again":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_016_buy_fraction_252d_diff_63d_again},
    "ibr_drv3_017_buyer_fraction_63d_diff_63d_again":   {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv3_017_buyer_fraction_63d_diff_63d_again},
    "ibr_drv3_018_value_net_flow_norm_diff_21d_again":  {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_018_value_net_flow_norm_diff_21d_again},
    "ibr_drv3_019_count_net_flow_63d_diff_63d_again":   {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_019_count_net_flow_63d_diff_63d_again},
    "ibr_drv3_020_sell_pressure_63d_diff_63d_again":    {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_020_sell_pressure_63d_diff_63d_again},
    "ibr_drv3_021_value_ratio_diff_ewm_deviation":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_021_value_ratio_diff_ewm_deviation},
    "ibr_drv3_022_buy_fraction_diff_ewm_deviation":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_022_buy_fraction_diff_ewm_deviation},
    "ibr_drv3_023_net_flow_diff_ewm_deviation":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_023_net_flow_diff_ewm_deviation},
    "ibr_drv3_024_count_ratio_diff_ewm_deviation":      {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_024_count_ratio_diff_ewm_deviation},
    "ibr_drv3_025_sell_pressure_diff_ewm_deviation":    {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_025_sell_pressure_diff_ewm_deviation},
    "ibr_drv3_026_value_ratio_252d_diff_21d_again":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_026_value_ratio_252d_diff_21d_again},
    "ibr_drv3_027_count_net_flow_63d_diff_21d_again_b":  {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_027_count_net_flow_63d_diff_21d_again_b},
    "ibr_drv3_028_share_buy_fraction_63d_diff_21d_again":{"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_drv3_028_share_buy_fraction_63d_diff_21d_again},
    "ibr_drv3_029_officer_net_flow_diff_21d_again":      {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_drv3_029_officer_net_flow_diff_21d_again},
    "ibr_drv3_030_director_net_flow_diff_21d_again":     {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_drv3_030_director_net_flow_diff_21d_again},
    "ibr_drv3_031_value_net_flow_63d_diff_21d_again_b":  {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_031_value_net_flow_63d_diff_21d_again_b},
    "ibr_drv3_032_count_ratio_63d_diff_63d_again_b":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_032_count_ratio_63d_diff_63d_again_b},
    "ibr_drv3_033_buy_fraction_252d_diff_21d_again":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_033_buy_fraction_252d_diff_21d_again},
    "ibr_drv3_034_sell_pressure_252d_diff_63d_again":    {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_034_sell_pressure_252d_diff_63d_again},
    "ibr_drv3_035_net_flow_norm_252d_diff_63d_again":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_035_net_flow_norm_252d_diff_63d_again},
    "ibr_drv3_036_value_ratio_diff_ewm_deviation_126d":  {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_036_value_ratio_diff_ewm_deviation_126d},
    "ibr_drv3_037_buy_fraction_diff_ewm_deviation_126d": {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_037_buy_fraction_diff_ewm_deviation_126d},
    "ibr_drv3_038_net_flow_diff_ewm_deviation_126d":     {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_038_net_flow_diff_ewm_deviation_126d},
    "ibr_drv3_039_count_ratio_diff_ewm_deviation_126d":  {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_039_count_ratio_diff_ewm_deviation_126d},
    "ibr_drv3_040_sell_pressure_diff_ewm_deviation_126d":{"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_040_sell_pressure_diff_ewm_deviation_126d},
    "ibr_drv3_041_value_ratio_diff_slope_63d":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_041_value_ratio_diff_slope_63d},
    "ibr_drv3_042_buy_fraction_diff_slope_63d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_042_buy_fraction_diff_slope_63d},
    "ibr_drv3_043_net_flow_diff_slope_63d":              {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_043_net_flow_diff_slope_63d},
    "ibr_drv3_044_sell_pressure_diff_slope_63d":         {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_044_sell_pressure_diff_slope_63d},
    "ibr_drv3_045_buyer_fraction_diff_slope_63d":        {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv3_045_buyer_fraction_diff_slope_63d},
    "ibr_drv3_046_value_ratio_63d_diff_5d_again":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_046_value_ratio_63d_diff_5d_again},
    "ibr_drv3_047_count_ratio_63d_diff_5d_again":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_047_count_ratio_63d_diff_5d_again},
    "ibr_drv3_048_buy_fraction_63d_diff_5d_again":       {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_048_buy_fraction_63d_diff_5d_again},
    "ibr_drv3_049_net_flow_63d_diff_5d_again":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_049_net_flow_63d_diff_5d_again},
    "ibr_drv3_050_sell_pressure_63d_diff_5d_again":      {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_050_sell_pressure_63d_diff_5d_again},
    "ibr_drv3_051_value_ratio_diff_zscore_252d":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_051_value_ratio_diff_zscore_252d},
    "ibr_drv3_052_count_ratio_diff_zscore_252d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_052_count_ratio_diff_zscore_252d},
    "ibr_drv3_053_buy_fraction_diff_zscore_252d":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_053_buy_fraction_diff_zscore_252d},
    "ibr_drv3_054_net_flow_diff_zscore_252d":            {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_054_net_flow_diff_zscore_252d},
    "ibr_drv3_055_sell_pressure_diff_zscore_252d":       {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_055_sell_pressure_diff_zscore_252d},
    "ibr_drv3_056_buyer_fraction_diff_zscore_252d":      {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv3_056_buyer_fraction_diff_zscore_252d},
    "ibr_drv3_057_value_ratio_diff_pct_rank_252d":       {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_057_value_ratio_diff_pct_rank_252d},
    "ibr_drv3_058_buy_fraction_diff_pct_rank_252d":      {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_058_buy_fraction_diff_pct_rank_252d},
    "ibr_drv3_059_net_flow_diff_pct_rank_252d":          {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_059_net_flow_diff_pct_rank_252d},
    "ibr_drv3_060_sell_pressure_diff_pct_rank_252d":     {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_060_sell_pressure_diff_pct_rank_252d},
    "ibr_drv3_061_value_ratio_63d_diff_126d_again":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_061_value_ratio_63d_diff_126d_again},
    "ibr_drv3_062_count_ratio_63d_diff_126d_again":      {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_062_count_ratio_63d_diff_126d_again},
    "ibr_drv3_063_buy_fraction_63d_diff_126d_again":     {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_063_buy_fraction_63d_diff_126d_again},
    "ibr_drv3_064_net_flow_63d_diff_126d_again":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_064_net_flow_63d_diff_126d_again},
    "ibr_drv3_065_sell_pressure_diff_126d_again":        {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_065_sell_pressure_diff_126d_again},
    "ibr_drv3_066_value_ratio_diff_ewm21_deviation":     {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_066_value_ratio_diff_ewm21_deviation},
    "ibr_drv3_067_buy_fraction_diff_ewm21_deviation":    {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv3_067_buy_fraction_diff_ewm21_deviation},
    "ibr_drv3_068_net_flow_diff_ewm21_deviation":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_068_net_flow_diff_ewm21_deviation},
    "ibr_drv3_069_sell_pressure_diff_ewm21_deviation":   {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_069_sell_pressure_diff_ewm21_deviation},
    "ibr_drv3_070_buyer_fraction_diff_ewm21_deviation":  {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv3_070_buyer_fraction_diff_ewm21_deviation},
    "ibr_drv3_071_value_ratio_252d_diff_63d_slope":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_071_value_ratio_252d_diff_63d_slope},
    "ibr_drv3_072_buy_fraction_252d_diff_63d_slope":     {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_072_buy_fraction_252d_diff_63d_slope},
    "ibr_drv3_073_net_flow_norm_63d_diff_slope_63d":     {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_073_net_flow_norm_63d_diff_slope_63d},
    "ibr_drv3_074_value_ratio_63d_diff_expanding_zscore":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv3_074_value_ratio_63d_diff_expanding_zscore},
    "ibr_drv3_075_sell_pressure_diff_expanding_zscore":  {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv3_075_sell_pressure_diff_expanding_zscore},
}
