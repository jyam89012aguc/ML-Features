"""
86_insider_buy_sell_ratio — 2nd-Derivative Features 001-075
Domain: rate of change of base buy/sell balance features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
Inputs to all feature functions are daily-frequency pandas Series aggregated
from Sharadar SF2 insider transaction filings.  Each row represents one
(ticker, date); most days have ZERO activity — positive values appear only on
filing days.  Do NOT forward-fill these series.

The 2nd-derivative series are very sparse on the daily index because the
underlying event-driven data is mostly zero — this is correct and expected.
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


# ── Base concept helpers (self-contained — no cross-file imports) ─────────────

def _value_ratio_63d(buy_val: pd.Series, sell_val: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(buy_val, _W63), _rolling_sum(sell_val, _W63))


def _value_ratio_252d(buy_val: pd.Series, sell_val: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(buy_val, _W252), _rolling_sum(sell_val, _W252))


def _count_ratio_63d(buy_cnt: pd.Series, sell_cnt: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(buy_cnt, _W63), _rolling_sum(sell_cnt, _W63))


def _buy_fraction(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    sb = _rolling_sum(buy, w)
    ss = _rolling_sum(sell, w)
    return _safe_div(sb, sb + ss)


def _net_flow_value(buy_val: pd.Series, sell_val: pd.Series, w: int) -> pd.Series:
    return _rolling_sum(buy_val, w) - _rolling_sum(sell_val, w)


def _net_flow_count(buy_cnt: pd.Series, sell_cnt: pd.Series, w: int) -> pd.Series:
    return _rolling_sum(buy_cnt, w) - _rolling_sum(sell_cnt, w)


def _net_flow_norm(buy: pd.Series, sell: pd.Series, w: int) -> pd.Series:
    sb = _rolling_sum(buy, w)
    ss = _rolling_sum(sell, w)
    return _safe_div(sb - ss, sb + ss)


def _value_net_flow_zscore(buy_val: pd.Series, sell_val: pd.Series, w: int) -> pd.Series:
    net_daily = buy_val - sell_val
    m  = _rolling_mean(net_daily, w)
    sd = _rolling_std(net_daily, w)
    return _safe_div(net_daily - m, sd)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def ibr_drv2_001_value_ratio_63d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day value ratio — rate of change in quarterly buy/sell balance."""
    base = _value_ratio_63d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W21)


def ibr_drv2_002_value_ratio_63d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day value ratio — quarter-over-quarter change in sentiment ratio."""
    base = _value_ratio_63d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W63)


def ibr_drv2_003_value_ratio_252d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of rolling 252-day value ratio."""
    base = _value_ratio_252d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W63)


def ibr_drv2_004_count_ratio_63d_21d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day count ratio — rate of change in count-based sentiment."""
    base = _count_ratio_63d(insider_buy_count, insider_sell_count)
    return base - base.shift(_W21)


def ibr_drv2_005_count_ratio_63d_63d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day count ratio."""
    base = _count_ratio_63d(insider_buy_count, insider_sell_count)
    return base - base.shift(_W63)


def ibr_drv2_006_buy_fraction_63d_21d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day buy fraction — acceleration of buy-share shift."""
    base = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    return base - base.shift(_W21)


def ibr_drv2_007_buy_fraction_63d_63d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day buy fraction."""
    base = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    return base - base.shift(_W63)


def ibr_drv2_008_value_net_flow_63d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day net dollar flow — acceleration of flow balance."""
    base = _net_flow_value(insider_buy_value, insider_sell_value, _W63)
    return base - base.shift(_W21)


def ibr_drv2_009_value_net_flow_63d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day net dollar flow."""
    base = _net_flow_value(insider_buy_value, insider_sell_value, _W63)
    return base - base.shift(_W63)


def ibr_drv2_010_value_net_flow_252d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of rolling 252-day net dollar flow — quarterly change in annual flow balance."""
    base = _net_flow_value(insider_buy_value, insider_sell_value, _W252)
    return base - base.shift(_W63)


def ibr_drv2_011_count_net_flow_63d_21d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day net count flow."""
    base = _net_flow_count(insider_buy_count, insider_sell_count, _W63)
    return base - base.shift(_W21)


def ibr_drv2_012_value_net_flow_norm_63d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of the 63-day normalized net dollar flow."""
    base = _net_flow_norm(insider_buy_value, insider_sell_value, _W63)
    return base - base.shift(_W21)


def ibr_drv2_013_value_net_flow_norm_63d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of the 63-day normalized net dollar flow."""
    base = _net_flow_norm(insider_buy_value, insider_sell_value, _W63)
    return base - base.shift(_W63)


def ibr_drv2_014_buyer_fraction_63d_21d_diff(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day buyer fraction (distinct persons)."""
    base = _buy_fraction(insider_buyers, insider_sellers, _W63)
    return base - base.shift(_W21)


def ibr_drv2_015_buyer_fraction_63d_63d_diff(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day buyer fraction (distinct persons)."""
    base = _buy_fraction(insider_buyers, insider_sellers, _W63)
    return base - base.shift(_W63)


def ibr_drv2_016_officer_net_flow_63d_21d_diff(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day officer net dollar flow."""
    base = _net_flow_value(officer_buy_value, officer_sell_value, _W63)
    return base - base.shift(_W21)


def ibr_drv2_017_director_net_flow_63d_21d_diff(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day director net dollar flow."""
    base = _net_flow_value(director_buy_value, director_sell_value, _W63)
    return base - base.shift(_W21)


def ibr_drv2_018_value_ratio_63d_slope_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """
    OLS slope of the rolling 63-day value ratio over a trailing 252-day window.
    Captures the trend in quarterly buy/sell balance.
    """
    base = _value_ratio_63d(insider_buy_value, insider_sell_value)

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

    return base.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_drv2_019_buy_fraction_252d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of rolling 252-day buy-fraction by value."""
    base = _buy_fraction(insider_buy_value, insider_sell_value, _W252)
    return base - base.shift(_W63)


def ibr_drv2_020_value_net_flow_zscore_252d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of the rolling 252-day z-score of daily net dollar flow."""
    base = _value_net_flow_zscore(insider_buy_value, insider_sell_value, _W252)
    return base - base.shift(_W21)


def ibr_drv2_021_share_buy_fraction_63d_21d_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day buy-fraction by shares."""
    base = _buy_fraction(insider_buy_shares, insider_sell_shares, _W63)
    return base - base.shift(_W21)


def ibr_drv2_022_share_net_flow_norm_63d_21d_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """21-day diff of the 63-day normalized net share flow."""
    base = _net_flow_norm(insider_buy_shares, insider_sell_shares, _W63)
    return base - base.shift(_W21)


def ibr_drv2_023_value_ratio_21d_pct_change_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day percent change of rolling 21-day value ratio — relative acceleration."""
    ratio21 = _safe_div(_rolling_sum(insider_buy_value, _W21), _rolling_sum(insider_sell_value, _W21))
    prior   = ratio21.shift(_W63)
    return _safe_div(ratio21 - prior, prior.abs().replace(0, np.nan))


def ibr_drv2_024_buyer_seller_net_63d_21d_diff(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day net buyer surplus (buyers minus sellers count)."""
    base = _rolling_sum(insider_buyers, _W63) - _rolling_sum(insider_sellers, _W63)
    return base - base.shift(_W21)


def ibr_drv2_025_sell_pressure_intensity_63d_21d_diff(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of 63-day sell-pressure intensity — acceleration of sell dominance."""
    ss = _rolling_sum(insider_sell_value, _W63)
    sb = _rolling_sum(insider_buy_value, _W63)
    base = _safe_div(ss, sb + ss)
    return base - base.shift(_W21)


# --- 2nd derivatives 026-050: longer lags and new base concepts ---

def ibr_drv2_026_value_ratio_63d_126d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """126-day diff of rolling 63-day value ratio — half-year change in quarterly balance."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    return base - base.shift(_W126)


def ibr_drv2_027_count_ratio_63d_63d_diff_alt(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day diff of rolling 21-day count ratio — change in short-window count sentiment."""
    base = _safe_div(_rolling_sum(insider_buy_count, _W21), _rolling_sum(insider_sell_count, _W21))
    return base - base.shift(_W63)


def ibr_drv2_028_value_net_flow_252d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 252-day net dollar flow."""
    base = _net_flow_value(insider_buy_value, insider_sell_value, _W252)
    return base - base.shift(_W21)


def ibr_drv2_029_count_net_flow_252d_63d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day diff of rolling 252-day net count flow."""
    base = _net_flow_count(insider_buy_count, insider_sell_count, _W252)
    return base - base.shift(_W63)


def ibr_drv2_030_buy_fraction_252d_21d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day diff of rolling 252-day buy fraction by count."""
    base = _buy_fraction(insider_buy_count, insider_sell_count, _W252)
    return base - base.shift(_W21)


def ibr_drv2_031_value_net_flow_norm_252d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of the 252-day normalized net dollar flow."""
    base = _net_flow_norm(insider_buy_value, insider_sell_value, _W252)
    return base - base.shift(_W63)


def ibr_drv2_032_share_buy_fraction_63d_63d_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day buy-fraction by shares."""
    base = _buy_fraction(insider_buy_shares, insider_sell_shares, _W63)
    return base - base.shift(_W63)


def ibr_drv2_033_share_net_flow_norm_252d_63d_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """63-day diff of the 252-day normalized net share flow."""
    base = _net_flow_norm(insider_buy_shares, insider_sell_shares, _W252)
    return base - base.shift(_W63)


def ibr_drv2_034_buyer_fraction_252d_63d_diff(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """63-day diff of rolling 252-day buyer fraction (distinct persons)."""
    base = _buy_fraction(insider_buyers, insider_sellers, _W252)
    return base - base.shift(_W63)


def ibr_drv2_035_officer_net_flow_63d_63d_diff(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day officer net dollar flow."""
    base = _net_flow_value(officer_buy_value, officer_sell_value, _W63)
    return base - base.shift(_W63)


def ibr_drv2_036_director_net_flow_63d_63d_diff(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day director net dollar flow."""
    base = _net_flow_value(director_buy_value, director_sell_value, _W63)
    return base - base.shift(_W63)


def ibr_drv2_037_sell_pressure_63d_63d_diff(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of 63-day sell-pressure intensity."""
    ss = _rolling_sum(insider_sell_value, _W63)
    sb = _rolling_sum(insider_buy_value, _W63)
    base = _safe_div(ss, sb + ss)
    return base - base.shift(_W63)


def ibr_drv2_038_value_ratio_126d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 126-day value ratio."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W126), _rolling_sum(insider_sell_value, _W126))
    return base - base.shift(_W21)


def ibr_drv2_039_count_ratio_126d_21d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day diff of rolling 126-day count ratio."""
    base = _safe_div(_rolling_sum(insider_buy_count, _W126), _rolling_sum(insider_sell_count, _W126))
    return base - base.shift(_W21)


def ibr_drv2_040_buy_fraction_126d_21d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day diff of rolling 126-day buy fraction by count."""
    base = _buy_fraction(insider_buy_count, insider_sell_count, _W126)
    return base - base.shift(_W21)


def ibr_drv2_041_value_net_flow_norm_21d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of the 21-day normalized net dollar flow — very short-term acceleration."""
    base = _net_flow_norm(insider_buy_value, insider_sell_value, _W21)
    return base - base.shift(_W21)


def ibr_drv2_042_count_net_flow_norm_21d_21d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day diff of the 21-day normalized net count flow."""
    base = _net_flow_norm(insider_buy_count, insider_sell_count, _W21)
    return base - base.shift(_W21)


def ibr_drv2_043_buyer_seller_net_252d_63d_diff(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """63-day diff of rolling 252-day net buyer surplus (buyers minus sellers)."""
    base = _rolling_sum(insider_buyers, _W252) - _rolling_sum(insider_sellers, _W252)
    return base - base.shift(_W63)


def ibr_drv2_044_officer_value_ratio_63d_21d_diff(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day officer value ratio."""
    base = _safe_div(_rolling_sum(officer_buy_value, _W63), _rolling_sum(officer_sell_value, _W63))
    return base - base.shift(_W21)


def ibr_drv2_045_director_value_ratio_63d_21d_diff(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day director value ratio."""
    base = _safe_div(_rolling_sum(director_buy_value, _W63), _rolling_sum(director_sell_value, _W63))
    return base - base.shift(_W21)


def ibr_drv2_046_value_ratio_63d_slope_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day value ratio over a trailing 63-day window — short-trend acceleration."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return base.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_drv2_047_buy_fraction_63d_slope_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day buy fraction over a trailing 63-day window."""
    base = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return base.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)


def ibr_drv2_048_value_net_flow_norm_63d_126d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """126-day diff of 63-day normalized net dollar flow — medium-term change in flow balance."""
    base = _net_flow_norm(insider_buy_value, insider_sell_value, _W63)
    return base - base.shift(_W126)


def ibr_drv2_049_share_ratio_63d_21d_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day share ratio."""
    base = _safe_div(_rolling_sum(insider_buy_shares, _W63), _rolling_sum(insider_sell_shares, _W63))
    return base - base.shift(_W21)


def ibr_drv2_050_value_ratio_252d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 252-day value ratio — short-term change in long-window sentiment."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_sell_value, _W252))
    return base - base.shift(_W21)


# --- 2nd derivatives 051-075: cross-series rates, pct-change, and EWM deviations ---

def ibr_drv2_051_value_ratio_63d_pct_change_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day percent change of rolling 63-day value ratio."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    prior = base.shift(_W21)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def ibr_drv2_052_count_ratio_63d_pct_change_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day percent change of rolling 63-day count ratio."""
    base = _safe_div(_rolling_sum(insider_buy_count, _W63), _rolling_sum(insider_sell_count, _W63))
    prior = base.shift(_W21)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def ibr_drv2_053_buy_fraction_252d_pct_change_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day percent change of rolling 252-day buy fraction by count."""
    base = _buy_fraction(insider_buy_count, insider_sell_count, _W252)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def ibr_drv2_054_value_net_flow_63d_pct_change_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day percent change of rolling 63-day net dollar flow."""
    base = _net_flow_value(insider_buy_value, insider_sell_value, _W63)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def ibr_drv2_055_buyer_fraction_252d_21d_diff(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """21-day diff of rolling 252-day buyer fraction by distinct persons."""
    base = _buy_fraction(insider_buyers, insider_sellers, _W252)
    return base - base.shift(_W21)


def ibr_drv2_056_value_ratio_21d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 21-day value ratio — very short-term acceleration."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W21), _rolling_sum(insider_sell_value, _W21))
    return base - base.shift(_W21)


def ibr_drv2_057_count_ratio_21d_21d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day diff of rolling 21-day count ratio — very short-term count sentiment acceleration."""
    base = _safe_div(_rolling_sum(insider_buy_count, _W21), _rolling_sum(insider_sell_count, _W21))
    return base - base.shift(_W21)


def ibr_drv2_058_sell_pressure_252d_63d_diff(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of 252-day sell-pressure intensity."""
    ss = _rolling_sum(insider_sell_value, _W252)
    sb = _rolling_sum(insider_buy_value, _W252)
    base = _safe_div(ss, sb + ss)
    return base - base.shift(_W63)


def ibr_drv2_059_sell_pressure_126d_21d_diff(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of 126-day sell-pressure intensity."""
    ss = _rolling_sum(insider_sell_value, _W126)
    sb = _rolling_sum(insider_buy_value, _W126)
    base = _safe_div(ss, sb + ss)
    return base - base.shift(_W21)


def ibr_drv2_060_value_net_flow_63d_ewm_deviation(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day net dollar flow minus its EWM (span=63) — deviation from trend as 2nd-order signal."""
    base = _net_flow_value(insider_buy_value, insider_sell_value, _W63)
    ewm = base.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return base - ewm


def ibr_drv2_061_count_net_flow_63d_ewm_deviation(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day net count flow minus its EWM (span=63) — deviation from trend."""
    base = _net_flow_count(insider_buy_count, insider_sell_count, _W63)
    ewm = base.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return base - ewm


def ibr_drv2_062_buy_fraction_63d_ewm_deviation(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day buy fraction minus its EWM (span=63) — deviation of buy-fraction from its own trend."""
    base = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    ewm = base.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return base - ewm


def ibr_drv2_063_value_ratio_63d_ewm_deviation(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day value ratio minus its EWM (span=63) — cyclical component of quarterly ratio."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    ewm = base.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return base - ewm


def ibr_drv2_064_buyer_fraction_63d_ewm_deviation(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """63-day buyer fraction minus its EWM (span=63)."""
    base = _buy_fraction(insider_buyers, insider_sellers, _W63)
    ewm = base.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return base - ewm


def ibr_drv2_065_sell_pressure_63d_ewm_deviation(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63-day sell-pressure intensity minus its EWM (span=63)."""
    ss = _rolling_sum(insider_sell_value, _W63)
    sb = _rolling_sum(insider_buy_value, _W63)
    base = _safe_div(ss, sb + ss)
    ewm = base.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return base - ewm


def ibr_drv2_066_value_net_flow_252d_ewm_deviation(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """252-day net dollar flow minus its EWM (span=252) — long-horizon deviation."""
    base = _net_flow_value(insider_buy_value, insider_sell_value, _W252)
    ewm = base.ewm(span=_W252, min_periods=max(1, _W252 // 4)).mean()
    return base - ewm


def ibr_drv2_067_count_ratio_252d_63d_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day diff of rolling 252-day count ratio."""
    base = _safe_div(_rolling_sum(insider_buy_count, _W252), _rolling_sum(insider_sell_count, _W252))
    return base - base.shift(_W63)


def ibr_drv2_068_officer_buy_fraction_63d_21d_diff(officer_buy_value: pd.Series, officer_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day officer buy fraction."""
    sb = _rolling_sum(officer_buy_value, _W63)
    ss = _rolling_sum(officer_sell_value, _W63)
    base = _safe_div(sb, sb + ss)
    return base - base.shift(_W21)


def ibr_drv2_069_director_buy_fraction_63d_21d_diff(director_buy_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    """21-day diff of rolling 63-day director buy fraction."""
    sb = _rolling_sum(director_buy_value, _W63)
    ss = _rolling_sum(director_sell_value, _W63)
    base = _safe_div(sb, sb + ss)
    return base - base.shift(_W21)


def ibr_drv2_070_share_net_flow_63d_63d_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """63-day diff of rolling 63-day net share flow."""
    base = _net_flow_value(insider_buy_shares, insider_sell_shares, _W63)
    return base - base.shift(_W63)


def ibr_drv2_071_value_ratio_63d_slope_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day value ratio over a trailing 126-day window."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_sell_value, _W63))
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return base.rolling(_W126, min_periods=max(2, _W126 // 4)).apply(_slope, raw=True)


def ibr_drv2_072_buy_fraction_63d_slope_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of rolling 63-day buy fraction over a trailing 126-day window."""
    base = _buy_fraction(insider_buy_count, insider_sell_count, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return base.rolling(_W126, min_periods=max(2, _W126 // 4)).apply(_slope, raw=True)


def ibr_drv2_073_value_net_flow_norm_63d_slope_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """OLS slope of 63-day normalized net dollar flow over a trailing 252-day window."""
    base = _net_flow_norm(insider_buy_value, insider_sell_value, _W63)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = np.nanmean(arr)
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else float(np.nansum((x - xm) * (arr - ym)) / d)
    return base.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)


def ibr_drv2_074_buyer_seller_net_126d_21d_diff(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """21-day diff of rolling 126-day net buyer surplus (buyers minus sellers)."""
    base = _rolling_sum(insider_buyers, _W126) - _rolling_sum(insider_sellers, _W126)
    return base - base.shift(_W21)


def ibr_drv2_075_value_ratio_504d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of rolling 504-day value ratio — change in 2-year buy/sell balance."""
    base = _safe_div(_rolling_sum(insider_buy_value, _W504), _rolling_sum(insider_sell_value, _W504))
    return base - base.shift(_W63)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

INSIDER_BUY_SELL_RATIO_REGISTRY_2ND_DERIVATIVES = {
    "ibr_drv2_001_value_ratio_63d_21d_diff":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_001_value_ratio_63d_21d_diff},
    "ibr_drv2_002_value_ratio_63d_63d_diff":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_002_value_ratio_63d_63d_diff},
    "ibr_drv2_003_value_ratio_252d_63d_diff":          {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_003_value_ratio_252d_63d_diff},
    "ibr_drv2_004_count_ratio_63d_21d_diff":           {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_004_count_ratio_63d_21d_diff},
    "ibr_drv2_005_count_ratio_63d_63d_diff":           {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_005_count_ratio_63d_63d_diff},
    "ibr_drv2_006_buy_fraction_63d_21d_diff":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_006_buy_fraction_63d_21d_diff},
    "ibr_drv2_007_buy_fraction_63d_63d_diff":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_007_buy_fraction_63d_63d_diff},
    "ibr_drv2_008_value_net_flow_63d_21d_diff":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_008_value_net_flow_63d_21d_diff},
    "ibr_drv2_009_value_net_flow_63d_63d_diff":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_009_value_net_flow_63d_63d_diff},
    "ibr_drv2_010_value_net_flow_252d_63d_diff":       {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_010_value_net_flow_252d_63d_diff},
    "ibr_drv2_011_count_net_flow_63d_21d_diff":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_011_count_net_flow_63d_21d_diff},
    "ibr_drv2_012_value_net_flow_norm_63d_21d_diff":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_012_value_net_flow_norm_63d_21d_diff},
    "ibr_drv2_013_value_net_flow_norm_63d_63d_diff":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_013_value_net_flow_norm_63d_63d_diff},
    "ibr_drv2_014_buyer_fraction_63d_21d_diff":        {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv2_014_buyer_fraction_63d_21d_diff},
    "ibr_drv2_015_buyer_fraction_63d_63d_diff":        {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv2_015_buyer_fraction_63d_63d_diff},
    "ibr_drv2_016_officer_net_flow_63d_21d_diff":      {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_drv2_016_officer_net_flow_63d_21d_diff},
    "ibr_drv2_017_director_net_flow_63d_21d_diff":     {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_drv2_017_director_net_flow_63d_21d_diff},
    "ibr_drv2_018_value_ratio_63d_slope_252d":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_018_value_ratio_63d_slope_252d},
    "ibr_drv2_019_buy_fraction_252d_63d_diff":         {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_019_buy_fraction_252d_63d_diff},
    "ibr_drv2_020_value_net_flow_zscore_252d_21d_diff":{"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_020_value_net_flow_zscore_252d_21d_diff},
    "ibr_drv2_021_share_buy_fraction_63d_21d_diff":    {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_drv2_021_share_buy_fraction_63d_21d_diff},
    "ibr_drv2_022_share_net_flow_norm_63d_21d_diff":   {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_drv2_022_share_net_flow_norm_63d_21d_diff},
    "ibr_drv2_023_value_ratio_21d_pct_change_63d":     {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_023_value_ratio_21d_pct_change_63d},
    "ibr_drv2_024_buyer_seller_net_63d_21d_diff":      {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv2_024_buyer_seller_net_63d_21d_diff},
    "ibr_drv2_025_sell_pressure_intensity_63d_21d_diff":{"inputs": ["insider_sell_value", "insider_buy_value"],  "func": ibr_drv2_025_sell_pressure_intensity_63d_21d_diff},
    "ibr_drv2_026_value_ratio_63d_126d_diff":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_026_value_ratio_63d_126d_diff},
    "ibr_drv2_027_count_ratio_63d_63d_diff_alt":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_027_count_ratio_63d_63d_diff_alt},
    "ibr_drv2_028_value_net_flow_252d_21d_diff":        {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_028_value_net_flow_252d_21d_diff},
    "ibr_drv2_029_count_net_flow_252d_63d_diff":        {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_029_count_net_flow_252d_63d_diff},
    "ibr_drv2_030_buy_fraction_252d_21d_diff":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_030_buy_fraction_252d_21d_diff},
    "ibr_drv2_031_value_net_flow_norm_252d_63d_diff":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_031_value_net_flow_norm_252d_63d_diff},
    "ibr_drv2_032_share_buy_fraction_63d_63d_diff":     {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_drv2_032_share_buy_fraction_63d_63d_diff},
    "ibr_drv2_033_share_net_flow_norm_252d_63d_diff":   {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_drv2_033_share_net_flow_norm_252d_63d_diff},
    "ibr_drv2_034_buyer_fraction_252d_63d_diff":        {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv2_034_buyer_fraction_252d_63d_diff},
    "ibr_drv2_035_officer_net_flow_63d_63d_diff":       {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_drv2_035_officer_net_flow_63d_63d_diff},
    "ibr_drv2_036_director_net_flow_63d_63d_diff":      {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_drv2_036_director_net_flow_63d_63d_diff},
    "ibr_drv2_037_sell_pressure_63d_63d_diff":          {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv2_037_sell_pressure_63d_63d_diff},
    "ibr_drv2_038_value_ratio_126d_21d_diff":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_038_value_ratio_126d_21d_diff},
    "ibr_drv2_039_count_ratio_126d_21d_diff":           {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_039_count_ratio_126d_21d_diff},
    "ibr_drv2_040_buy_fraction_126d_21d_diff":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_040_buy_fraction_126d_21d_diff},
    "ibr_drv2_041_value_net_flow_norm_21d_21d_diff":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_041_value_net_flow_norm_21d_21d_diff},
    "ibr_drv2_042_count_net_flow_norm_21d_21d_diff":    {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_042_count_net_flow_norm_21d_21d_diff},
    "ibr_drv2_043_buyer_seller_net_252d_63d_diff":      {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv2_043_buyer_seller_net_252d_63d_diff},
    "ibr_drv2_044_officer_value_ratio_63d_21d_diff":    {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_drv2_044_officer_value_ratio_63d_21d_diff},
    "ibr_drv2_045_director_value_ratio_63d_21d_diff":   {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_drv2_045_director_value_ratio_63d_21d_diff},
    "ibr_drv2_046_value_ratio_63d_slope_63d":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_046_value_ratio_63d_slope_63d},
    "ibr_drv2_047_buy_fraction_63d_slope_63d":          {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_047_buy_fraction_63d_slope_63d},
    "ibr_drv2_048_value_net_flow_norm_63d_126d_diff":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_048_value_net_flow_norm_63d_126d_diff},
    "ibr_drv2_049_share_ratio_63d_21d_diff":            {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_drv2_049_share_ratio_63d_21d_diff},
    "ibr_drv2_050_value_ratio_252d_21d_diff":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_050_value_ratio_252d_21d_diff},
    "ibr_drv2_051_value_ratio_63d_pct_change_21d":      {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_051_value_ratio_63d_pct_change_21d},
    "ibr_drv2_052_count_ratio_63d_pct_change_21d":      {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_052_count_ratio_63d_pct_change_21d},
    "ibr_drv2_053_buy_fraction_252d_pct_change_63d":    {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_053_buy_fraction_252d_pct_change_63d},
    "ibr_drv2_054_value_net_flow_63d_pct_change_63d":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_054_value_net_flow_63d_pct_change_63d},
    "ibr_drv2_055_buyer_fraction_252d_21d_diff":        {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv2_055_buyer_fraction_252d_21d_diff},
    "ibr_drv2_056_value_ratio_21d_21d_diff":            {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_056_value_ratio_21d_21d_diff},
    "ibr_drv2_057_count_ratio_21d_21d_diff":            {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_057_count_ratio_21d_21d_diff},
    "ibr_drv2_058_sell_pressure_252d_63d_diff":         {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv2_058_sell_pressure_252d_63d_diff},
    "ibr_drv2_059_sell_pressure_126d_21d_diff":         {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv2_059_sell_pressure_126d_21d_diff},
    "ibr_drv2_060_value_net_flow_63d_ewm_deviation":    {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_060_value_net_flow_63d_ewm_deviation},
    "ibr_drv2_061_count_net_flow_63d_ewm_deviation":    {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_061_count_net_flow_63d_ewm_deviation},
    "ibr_drv2_062_buy_fraction_63d_ewm_deviation":      {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_062_buy_fraction_63d_ewm_deviation},
    "ibr_drv2_063_value_ratio_63d_ewm_deviation":       {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_063_value_ratio_63d_ewm_deviation},
    "ibr_drv2_064_buyer_fraction_63d_ewm_deviation":    {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv2_064_buyer_fraction_63d_ewm_deviation},
    "ibr_drv2_065_sell_pressure_63d_ewm_deviation":     {"inputs": ["insider_sell_value", "insider_buy_value"],   "func": ibr_drv2_065_sell_pressure_63d_ewm_deviation},
    "ibr_drv2_066_value_net_flow_252d_ewm_deviation":   {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_066_value_net_flow_252d_ewm_deviation},
    "ibr_drv2_067_count_ratio_252d_63d_diff":           {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_067_count_ratio_252d_63d_diff},
    "ibr_drv2_068_officer_buy_fraction_63d_21d_diff":   {"inputs": ["officer_buy_value", "officer_sell_value"],   "func": ibr_drv2_068_officer_buy_fraction_63d_21d_diff},
    "ibr_drv2_069_director_buy_fraction_63d_21d_diff":  {"inputs": ["director_buy_value", "director_sell_value"], "func": ibr_drv2_069_director_buy_fraction_63d_21d_diff},
    "ibr_drv2_070_share_net_flow_63d_63d_diff":         {"inputs": ["insider_buy_shares", "insider_sell_shares"], "func": ibr_drv2_070_share_net_flow_63d_63d_diff},
    "ibr_drv2_071_value_ratio_63d_slope_126d":          {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_071_value_ratio_63d_slope_126d},
    "ibr_drv2_072_buy_fraction_63d_slope_126d":         {"inputs": ["insider_buy_count", "insider_sell_count"],   "func": ibr_drv2_072_buy_fraction_63d_slope_126d},
    "ibr_drv2_073_value_net_flow_norm_63d_slope_252d":  {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_073_value_net_flow_norm_63d_slope_252d},
    "ibr_drv2_074_buyer_seller_net_126d_21d_diff":      {"inputs": ["insider_buyers", "insider_sellers"],         "func": ibr_drv2_074_buyer_seller_net_126d_21d_diff},
    "ibr_drv2_075_value_ratio_504d_63d_diff":           {"inputs": ["insider_buy_value", "insider_sell_value"],   "func": ibr_drv2_075_value_ratio_504d_63d_diff},
}
