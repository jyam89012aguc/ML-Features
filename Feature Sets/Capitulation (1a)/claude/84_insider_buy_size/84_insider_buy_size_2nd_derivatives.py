"""
84_insider_buy_size — 2nd-Derivative Features 001-075
Domain: rate of change of base insider buy-size features
Asset class: US equities | Sharadar SF2 insider transactions (daily aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series,
aggregated from Sharadar SF2 insider transaction filings to one row per
(ticker, date).  These are EVENT-DRIVEN series: most days are ZERO; positive
values appear only on filing days.  Do NOT forward-fill these series.
The 2nd-derivative series are very sparse on the daily index because the
underlying insider data is event-driven — this is correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  All diffs use positive shift values only.
Trading-day cadence: 1 week = 5, 1 month = 21, 1 quarter = 63, 1 year = 252.

Canonical input fields (lowercase):
    insider_buy_value, insider_buy_shares, insider_buy_count,
    officer_buy_value, ceo_buy_value, cfo_buy_value, tenpct_buy_value,
    director_buy_value, insider_sell_value, insider_shares_held
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


# ── Base feature helpers (self-contained recomputes — no cross-file imports) ──

def _buy_value_21d(insider_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_value, _W21)


def _buy_value_63d(insider_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_value, _W63)


def _buy_value_252d(insider_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_value, _W252)


def _officer_buy_value_63d(officer_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_value, _W63)


def _officer_buy_value_252d(officer_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_value, _W252)


def _ceo_buy_value_63d(ceo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(ceo_buy_value, _W63)


def _ceo_buy_value_252d(ceo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(ceo_buy_value, _W252)


def _avg_buy_size_63d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    val = _rolling_sum(insider_buy_value, _W63)
    cnt = _rolling_sum(insider_buy_count, _W63)
    return _safe_div(val, cnt)


def _buy_value_zscore_252d(insider_buy_value: pd.Series) -> pd.Series:
    m  = _rolling_mean(insider_buy_value, _W252)
    sd = _rolling_std(insider_buy_value, _W252)
    return _safe_div(insider_buy_value - m, sd)


def _net_buy_value_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)


def _peak_daily_buy_value_63d(insider_buy_value: pd.Series) -> pd.Series:
    return _rolling_max(insider_buy_value, _W63)


def _buy_value_21d_vs_252d_avg(insider_buy_value: pd.Series) -> pd.Series:
    short = _rolling_sum(insider_buy_value, _W21)
    base  = _rolling_mean(insider_buy_value, _W252)
    return _safe_div(short, base)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def ibs_drv2_001_buy_value_21d_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 21-day buy value sum (change in short-term buy volume)."""
    base = _buy_value_21d(insider_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_002_buy_value_63d_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 63-day buy value sum (change in quarterly buy volume)."""
    base = _buy_value_63d(insider_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_003_buy_value_252d_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 252-day buy value sum (quarterly change in annual buy total)."""
    base = _buy_value_252d(insider_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_004_buy_value_252d_252d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """252-day diff of trailing 252-day buy value sum (YoY change in annual buy total)."""
    base = _buy_value_252d(insider_buy_value)
    return base - base.shift(_W252)


def ibs_drv2_005_buy_value_21d_pct_chg_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change in 21-day buy value between current and 21-day-ago value."""
    base  = _buy_value_21d(insider_buy_value)
    prior = base.shift(_W21)
    return _safe_div(base - prior, prior)


def ibs_drv2_006_buy_value_63d_pct_chg_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change in 63-day buy value between current and 63-day-ago value."""
    base  = _buy_value_63d(insider_buy_value)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def ibs_drv2_007_officer_buy_63d_21d_diff(officer_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 63-day officer buy value."""
    base = _officer_buy_value_63d(officer_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_008_officer_buy_252d_63d_diff(officer_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 252-day officer buy value sum."""
    base = _officer_buy_value_252d(officer_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_009_ceo_buy_63d_21d_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 63-day CEO buy value."""
    base = _ceo_buy_value_63d(ceo_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_010_ceo_buy_252d_63d_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 252-day CEO buy value."""
    base = _ceo_buy_value_252d(ceo_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_011_avg_buy_size_63d_21d_diff(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """21-day diff of average buy transaction size (63-day window)."""
    base = _avg_buy_size_63d(insider_buy_value, insider_buy_count)
    return base - base.shift(_W21)


def ibs_drv2_012_avg_buy_size_63d_63d_diff(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """63-day diff of average buy transaction size (63-day window)."""
    base = _avg_buy_size_63d(insider_buy_value, insider_buy_count)
    return base - base.shift(_W63)


def ibs_drv2_013_buy_value_zscore_252d_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of daily buy-value z-score within 252-day window."""
    base = _buy_value_zscore_252d(insider_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_014_buy_value_zscore_252d_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of daily buy-value z-score within 252-day window."""
    base = _buy_value_zscore_252d(insider_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_015_net_buy_value_63d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of net buy value (buys minus sells) over 63-day window."""
    base = _net_buy_value_63d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W21)


def ibs_drv2_016_net_buy_value_63d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of net buy value over 63-day window."""
    base = _net_buy_value_63d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W63)


def ibs_drv2_017_peak_daily_buy_63d_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of rolling-63-day peak daily buy value (largest single transaction trend)."""
    base = _peak_daily_buy_value_63d(insider_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_018_peak_daily_buy_63d_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of rolling-63-day peak daily buy value."""
    base = _peak_daily_buy_value_63d(insider_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_019_buy_value_21d_vs_252d_avg_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of the ratio (21-day buy sum / 252-day mean daily buy value)."""
    base = _buy_value_21d_vs_252d_avg(insider_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_020_buy_value_21d_acceleration(insider_buy_value: pd.Series) -> pd.Series:
    """
    Second-difference of 21-day buy value at 21-day lag (acceleration of buy momentum):
    [sum_21(t) - sum_21(t-21)] - [sum_21(t-21) - sum_21(t-42)]
    """
    base = _buy_value_21d(insider_buy_value)
    d1   = base - base.shift(_W21)
    return d1 - d1.shift(_W21)


def ibs_drv2_021_buy_value_63d_acceleration(insider_buy_value: pd.Series) -> pd.Series:
    """
    Second-difference of 63-day buy value at 63-day lag (acceleration of quarterly buying):
    [sum_63(t) - sum_63(t-63)] - [sum_63(t-63) - sum_63(t-126)]
    """
    base = _buy_value_63d(insider_buy_value)
    d1   = base - base.shift(_W63)
    return d1 - d1.shift(_W63)


def ibs_drv2_022_buy_value_252d_slope_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """
    OLS slope of 63-day buy value over 252-day window, then 21-day diff of that slope.
    Captures change in the trend of quarterly buying.
    """
    val = _buy_value_63d(insider_buy_value)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    slope = val.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_W21)


def ibs_drv2_023_buy_value_63d_ewm_diff_21d(insider_buy_value: pd.Series) -> pd.Series:
    """
    21-day diff of (63-day buy sum minus its EWM span=252) — change in buy intensity vs trend.
    """
    val  = _buy_value_63d(insider_buy_value)
    ewm  = val.ewm(span=_W252, min_periods=max(1, _W252 // 4)).mean()
    base = val - ewm
    return base - base.shift(_W21)


def ibs_drv2_024_officer_buy_63d_pct_chg_63d(officer_buy_value: pd.Series) -> pd.Series:
    """Percent change in 63-day officer buy value between current and 63-day-ago value."""
    base  = _officer_buy_value_63d(officer_buy_value)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def ibs_drv2_025_buy_size_composite_63d_diff(insider_buy_value: pd.Series, officer_buy_value: pd.Series, ceo_buy_value: pd.Series) -> pd.Series:
    """
    63-day diff of the composite buy-size z-score
    (equally weighted average of 252-day z-scores for total, officer, CEO buy sums).
    Measures whether the broad buy-magnitude signal is accelerating or decelerating.
    """
    def _zs252(s):
        m  = _rolling_mean(s, _W252)
        sd = _rolling_std(s, _W252)
        return _safe_div(s - m, sd)

    composite = (
        _zs252(_rolling_sum(insider_buy_value, _W252))
        + _zs252(_rolling_sum(officer_buy_value, _W252))
        + _zs252(_rolling_sum(ceo_buy_value, _W252))
    ) / 3.0
    return composite - composite.shift(_W63)


# ── Additional base helpers for 2nd-derivative features 026-075 ───────────────

def _buy_value_126d(insider_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_value, _W126)


def _buy_value_504d(insider_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_value, _W504)


def _net_buy_value_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_value, _W252) - _rolling_sum(insider_sell_value, _W252)


def _officer_buy_value_126d(officer_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_value, _W126)


def _officer_buy_value_504d(officer_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_value, _W504)


def _ceo_buy_value_126d(ceo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(ceo_buy_value, _W126)


def _ceo_buy_value_504d(ceo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(ceo_buy_value, _W504)


def _director_buy_value_63d(director_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(director_buy_value, _W63)


def _director_buy_value_252d(director_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(director_buy_value, _W252)


def _tenpct_buy_value_63d(tenpct_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(tenpct_buy_value, _W63)


def _tenpct_buy_value_252d(tenpct_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(tenpct_buy_value, _W252)


def _cfo_buy_value_63d(cfo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(cfo_buy_value, _W63)


def _cfo_buy_value_252d(cfo_buy_value: pd.Series) -> pd.Series:
    return _rolling_sum(cfo_buy_value, _W252)


def _buy_shares_63d(insider_buy_shares: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_shares, _W63)


def _buy_shares_252d(insider_buy_shares: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_shares, _W252)


def _buy_to_sell_ratio_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_value, _W63),
                     _rolling_sum(insider_sell_value, _W63))


def _buy_to_sell_ratio_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_value, _W252),
                     _rolling_sum(insider_sell_value, _W252))


def _avg_buy_size_252d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_value, _W252),
                     _rolling_sum(insider_buy_count, _W252))


def _peak_buy_value_252d(insider_buy_value: pd.Series) -> pd.Series:
    return _rolling_max(insider_buy_value, _W252)


# ── 2nd-derivative feature functions 026-075 ─────────────────────────────────

def ibs_drv2_026_buy_value_126d_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 126-day buy value sum."""
    base = _buy_value_126d(insider_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_027_buy_value_126d_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 126-day buy value sum."""
    base = _buy_value_126d(insider_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_028_buy_value_504d_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 504-day buy value sum."""
    base = _buy_value_504d(insider_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_029_buy_value_504d_252d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """252-day diff of trailing 504-day buy value sum."""
    base = _buy_value_504d(insider_buy_value)
    return base - base.shift(_W252)


def ibs_drv2_030_buy_value_126d_pct_chg_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change in 126-day buy value at 63-day lag."""
    base  = _buy_value_126d(insider_buy_value)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def ibs_drv2_031_net_buy_value_252d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of net buy value (buys minus sells) over 252-day window."""
    base = _net_buy_value_252d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W63)


def ibs_drv2_032_net_buy_value_252d_252d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """252-day diff of net buy value over 252-day window."""
    base = _net_buy_value_252d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W252)


def ibs_drv2_033_officer_buy_126d_21d_diff(officer_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 126-day officer buy value."""
    base = _officer_buy_value_126d(officer_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_034_officer_buy_504d_63d_diff(officer_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 504-day officer buy value."""
    base = _officer_buy_value_504d(officer_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_035_ceo_buy_126d_21d_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 126-day CEO buy value."""
    base = _ceo_buy_value_126d(ceo_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_036_ceo_buy_504d_63d_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 504-day CEO buy value."""
    base = _ceo_buy_value_504d(ceo_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_037_director_buy_63d_21d_diff(director_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 63-day director buy value."""
    base = _director_buy_value_63d(director_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_038_director_buy_252d_63d_diff(director_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 252-day director buy value."""
    base = _director_buy_value_252d(director_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_039_tenpct_buy_63d_21d_diff(tenpct_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 63-day 10%+ holder buy value."""
    base = _tenpct_buy_value_63d(tenpct_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_040_tenpct_buy_252d_63d_diff(tenpct_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 252-day 10%+ holder buy value."""
    base = _tenpct_buy_value_252d(tenpct_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_041_cfo_buy_63d_21d_diff(cfo_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 63-day CFO buy value."""
    base = _cfo_buy_value_63d(cfo_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_042_cfo_buy_252d_63d_diff(cfo_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 252-day CFO buy value."""
    base = _cfo_buy_value_252d(cfo_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_043_buy_shares_63d_21d_diff(insider_buy_shares: pd.Series) -> pd.Series:
    """21-day diff of trailing 63-day buy shares sum."""
    base = _buy_shares_63d(insider_buy_shares)
    return base - base.shift(_W21)


def ibs_drv2_044_buy_shares_252d_63d_diff(insider_buy_shares: pd.Series) -> pd.Series:
    """63-day diff of trailing 252-day buy shares sum."""
    base = _buy_shares_252d(insider_buy_shares)
    return base - base.shift(_W63)


def ibs_drv2_045_buy_shares_252d_pct_chg_63d(insider_buy_shares: pd.Series) -> pd.Series:
    """Percent change in 252-day buy shares sum at 63-day lag."""
    base  = _buy_shares_252d(insider_buy_shares)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def ibs_drv2_046_buy_to_sell_ratio_63d_21d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """21-day diff of buy-to-sell value ratio (63-day window)."""
    base = _buy_to_sell_ratio_63d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W21)


def ibs_drv2_047_buy_to_sell_ratio_252d_63d_diff(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """63-day diff of buy-to-sell value ratio (252-day window)."""
    base = _buy_to_sell_ratio_252d(insider_buy_value, insider_sell_value)
    return base - base.shift(_W63)


def ibs_drv2_048_avg_buy_size_252d_21d_diff(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """21-day diff of average buy transaction size (252-day window)."""
    base = _avg_buy_size_252d(insider_buy_value, insider_buy_count)
    return base - base.shift(_W21)


def ibs_drv2_049_avg_buy_size_252d_63d_diff(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """63-day diff of average buy transaction size (252-day window)."""
    base = _avg_buy_size_252d(insider_buy_value, insider_buy_count)
    return base - base.shift(_W63)


def ibs_drv2_050_peak_buy_value_252d_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of rolling-252-day peak daily buy value."""
    base = _peak_buy_value_252d(insider_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_051_buy_value_252d_pct_chg_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change in 252-day buy value sum at 63-day lag."""
    base  = _buy_value_252d(insider_buy_value)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def ibs_drv2_052_buy_value_21d_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 21-day buy value sum (slower view of short-term change)."""
    base = _buy_value_21d(insider_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_053_buy_value_63d_126d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """126-day diff of trailing 63-day buy value sum."""
    base = _buy_value_63d(insider_buy_value)
    return base - base.shift(_W126)


def ibs_drv2_054_buy_value_126d_126d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """126-day diff of trailing 126-day buy value sum (half-year change in half-year total)."""
    base = _buy_value_126d(insider_buy_value)
    return base - base.shift(_W126)


def ibs_drv2_055_officer_buy_252d_21d_diff(officer_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 252-day officer buy value."""
    base = _officer_buy_value_252d(officer_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_056_officer_buy_63d_pct_chg_21d(officer_buy_value: pd.Series) -> pd.Series:
    """Percent change in 63-day officer buy value at 21-day lag."""
    base  = _officer_buy_value_63d(officer_buy_value)
    prior = base.shift(_W21)
    return _safe_div(base - prior, prior)


def ibs_drv2_057_ceo_buy_252d_21d_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 252-day CEO buy value."""
    base = _ceo_buy_value_252d(ceo_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_058_ceo_buy_252d_pct_chg_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """Percent change in 252-day CEO buy value at 63-day lag."""
    base  = _ceo_buy_value_252d(ceo_buy_value)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def ibs_drv2_059_director_buy_63d_pct_chg_21d(director_buy_value: pd.Series) -> pd.Series:
    """Percent change in 63-day director buy value at 21-day lag."""
    base  = _director_buy_value_63d(director_buy_value)
    prior = base.shift(_W21)
    return _safe_div(base - prior, prior)


def ibs_drv2_060_tenpct_buy_252d_pct_chg_63d(tenpct_buy_value: pd.Series) -> pd.Series:
    """Percent change in 252-day 10%+ holder buy value at 63-day lag."""
    base  = _tenpct_buy_value_252d(tenpct_buy_value)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def ibs_drv2_061_buy_value_63d_zscore_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of z-score of the 63-day buy sum within its 252-day window."""
    val  = _buy_value_63d(insider_buy_value)
    base = _safe_div(val - _rolling_mean(val, _W252), _rolling_std(val, _W252))
    return base - base.shift(_W21)


def ibs_drv2_062_buy_value_252d_zscore_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of z-score of the 252-day buy sum within its 504-day window."""
    val  = _buy_value_252d(insider_buy_value)
    base = _safe_div(val - _rolling_mean(val, _W504), _rolling_std(val, _W504))
    return base - base.shift(_W63)


def ibs_drv2_063_buy_value_126d_acceleration(insider_buy_value: pd.Series) -> pd.Series:
    """Second-difference of 126-day buy sum at 63-day lag (acceleration of half-year buying)."""
    base = _buy_value_126d(insider_buy_value)
    d1   = base - base.shift(_W63)
    return d1 - d1.shift(_W63)


def ibs_drv2_064_buy_value_21d_slope_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """
    63-day diff of OLS slope of 21-day buy sum series over 63-day window.
    Rate of change of the short-term buy trend.
    """
    val = _buy_value_21d(insider_buy_value)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    slope = val.rolling(_W63, min_periods=max(2, _W63 // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_W63)


def ibs_drv2_065_buy_value_63d_ewm_diff_63d(insider_buy_value: pd.Series) -> pd.Series:
    """63-day diff of (63-day buy sum minus its EWM span=252)."""
    val  = _buy_value_63d(insider_buy_value)
    ewm  = val.ewm(span=_W252, min_periods=max(1, _W252 // 4)).mean()
    base = val - ewm
    return base - base.shift(_W63)


def ibs_drv2_066_net_buy_63d_pct_chg_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Percent change in 63-day net buy value at 21-day lag."""
    base  = _net_buy_value_63d(insider_buy_value, insider_sell_value)
    prior = base.shift(_W21)
    return _safe_div(base - prior, prior.abs())


def ibs_drv2_067_buy_value_21d_252d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """252-day diff of trailing 21-day buy sum (long-term momentum of short-window measure)."""
    base = _buy_value_21d(insider_buy_value)
    return base - base.shift(_W252)


def ibs_drv2_068_officer_buy_126d_63d_diff(officer_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 126-day officer buy value."""
    base = _officer_buy_value_126d(officer_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_069_ceo_buy_126d_63d_diff(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day diff of trailing 126-day CEO buy value."""
    base = _ceo_buy_value_126d(ceo_buy_value)
    return base - base.shift(_W63)


def ibs_drv2_070_cfo_buy_252d_pct_chg_63d(cfo_buy_value: pd.Series) -> pd.Series:
    """Percent change in 252-day CFO buy value at 63-day lag."""
    base  = _cfo_buy_value_252d(cfo_buy_value)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def ibs_drv2_071_buy_value_63d_252d_slope_63d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """
    63-day diff of OLS slope of 63-day buy value over 252-day window.
    Changes in the quarterly-buy trend at a quarterly cadence.
    """
    val = _buy_value_63d(insider_buy_value)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    slope = val.rolling(_W252, min_periods=max(2, _W252 // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_W63)


def ibs_drv2_072_buy_shares_126d_21d_diff(insider_buy_shares: pd.Series) -> pd.Series:
    """21-day diff of trailing 126-day buy shares sum."""
    base = _rolling_sum(insider_buy_shares, _W126)
    return base - base.shift(_W21)


def ibs_drv2_073_director_buy_252d_21d_diff(director_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 252-day director buy value."""
    base = _director_buy_value_252d(director_buy_value)
    return base - base.shift(_W21)


def ibs_drv2_074_tenpct_buy_63d_pct_chg_21d(tenpct_buy_value: pd.Series) -> pd.Series:
    """Percent change in 63-day 10%+ holder buy value at 21-day lag."""
    base  = _tenpct_buy_value_63d(tenpct_buy_value)
    prior = base.shift(_W21)
    return _safe_div(base - prior, prior)


def ibs_drv2_075_buy_value_5d_21d_diff(insider_buy_value: pd.Series) -> pd.Series:
    """21-day diff of trailing 5-day buy value sum (change in very near-term spike activity)."""
    base = _rolling_sum(insider_buy_value, _W5)
    return base - base.shift(_W21)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

INSIDER_BUY_SIZE_REGISTRY_2ND_DERIVATIVES = {
    "ibs_drv2_001_buy_value_21d_21d_diff":              {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_001_buy_value_21d_21d_diff},
    "ibs_drv2_002_buy_value_63d_63d_diff":              {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_002_buy_value_63d_63d_diff},
    "ibs_drv2_003_buy_value_252d_63d_diff":             {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_003_buy_value_252d_63d_diff},
    "ibs_drv2_004_buy_value_252d_252d_diff":            {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_004_buy_value_252d_252d_diff},
    "ibs_drv2_005_buy_value_21d_pct_chg_21d":           {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_005_buy_value_21d_pct_chg_21d},
    "ibs_drv2_006_buy_value_63d_pct_chg_63d":           {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_006_buy_value_63d_pct_chg_63d},
    "ibs_drv2_007_officer_buy_63d_21d_diff":            {"inputs": ["officer_buy_value"],                                        "func": ibs_drv2_007_officer_buy_63d_21d_diff},
    "ibs_drv2_008_officer_buy_252d_63d_diff":           {"inputs": ["officer_buy_value"],                                        "func": ibs_drv2_008_officer_buy_252d_63d_diff},
    "ibs_drv2_009_ceo_buy_63d_21d_diff":                {"inputs": ["ceo_buy_value"],                                            "func": ibs_drv2_009_ceo_buy_63d_21d_diff},
    "ibs_drv2_010_ceo_buy_252d_63d_diff":               {"inputs": ["ceo_buy_value"],                                            "func": ibs_drv2_010_ceo_buy_252d_63d_diff},
    "ibs_drv2_011_avg_buy_size_63d_21d_diff":           {"inputs": ["insider_buy_value", "insider_buy_count"],                   "func": ibs_drv2_011_avg_buy_size_63d_21d_diff},
    "ibs_drv2_012_avg_buy_size_63d_63d_diff":           {"inputs": ["insider_buy_value", "insider_buy_count"],                   "func": ibs_drv2_012_avg_buy_size_63d_63d_diff},
    "ibs_drv2_013_buy_value_zscore_252d_21d_diff":      {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_013_buy_value_zscore_252d_21d_diff},
    "ibs_drv2_014_buy_value_zscore_252d_63d_diff":      {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_014_buy_value_zscore_252d_63d_diff},
    "ibs_drv2_015_net_buy_value_63d_21d_diff":          {"inputs": ["insider_buy_value", "insider_sell_value"],                  "func": ibs_drv2_015_net_buy_value_63d_21d_diff},
    "ibs_drv2_016_net_buy_value_63d_63d_diff":          {"inputs": ["insider_buy_value", "insider_sell_value"],                  "func": ibs_drv2_016_net_buy_value_63d_63d_diff},
    "ibs_drv2_017_peak_daily_buy_63d_21d_diff":         {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_017_peak_daily_buy_63d_21d_diff},
    "ibs_drv2_018_peak_daily_buy_63d_63d_diff":         {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_018_peak_daily_buy_63d_63d_diff},
    "ibs_drv2_019_buy_value_21d_vs_252d_avg_21d_diff":  {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_019_buy_value_21d_vs_252d_avg_21d_diff},
    "ibs_drv2_020_buy_value_21d_acceleration":          {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_020_buy_value_21d_acceleration},
    "ibs_drv2_021_buy_value_63d_acceleration":          {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_021_buy_value_63d_acceleration},
    "ibs_drv2_022_buy_value_252d_slope_21d_diff":       {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_022_buy_value_252d_slope_21d_diff},
    "ibs_drv2_023_buy_value_63d_ewm_diff_21d":          {"inputs": ["insider_buy_value"],                                        "func": ibs_drv2_023_buy_value_63d_ewm_diff_21d},
    "ibs_drv2_024_officer_buy_63d_pct_chg_63d":         {"inputs": ["officer_buy_value"],                                        "func": ibs_drv2_024_officer_buy_63d_pct_chg_63d},
    "ibs_drv2_025_buy_size_composite_63d_diff":         {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value"],  "func": ibs_drv2_025_buy_size_composite_63d_diff},
    "ibs_drv2_026_buy_value_126d_21d_diff":             {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_026_buy_value_126d_21d_diff},
    "ibs_drv2_027_buy_value_126d_63d_diff":             {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_027_buy_value_126d_63d_diff},
    "ibs_drv2_028_buy_value_504d_63d_diff":             {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_028_buy_value_504d_63d_diff},
    "ibs_drv2_029_buy_value_504d_252d_diff":            {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_029_buy_value_504d_252d_diff},
    "ibs_drv2_030_buy_value_126d_pct_chg_63d":          {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_030_buy_value_126d_pct_chg_63d},
    "ibs_drv2_031_net_buy_value_252d_63d_diff":         {"inputs": ["insider_buy_value", "insider_sell_value"],                   "func": ibs_drv2_031_net_buy_value_252d_63d_diff},
    "ibs_drv2_032_net_buy_value_252d_252d_diff":        {"inputs": ["insider_buy_value", "insider_sell_value"],                   "func": ibs_drv2_032_net_buy_value_252d_252d_diff},
    "ibs_drv2_033_officer_buy_126d_21d_diff":           {"inputs": ["officer_buy_value"],                                         "func": ibs_drv2_033_officer_buy_126d_21d_diff},
    "ibs_drv2_034_officer_buy_504d_63d_diff":           {"inputs": ["officer_buy_value"],                                         "func": ibs_drv2_034_officer_buy_504d_63d_diff},
    "ibs_drv2_035_ceo_buy_126d_21d_diff":               {"inputs": ["ceo_buy_value"],                                             "func": ibs_drv2_035_ceo_buy_126d_21d_diff},
    "ibs_drv2_036_ceo_buy_504d_63d_diff":               {"inputs": ["ceo_buy_value"],                                             "func": ibs_drv2_036_ceo_buy_504d_63d_diff},
    "ibs_drv2_037_director_buy_63d_21d_diff":           {"inputs": ["director_buy_value"],                                        "func": ibs_drv2_037_director_buy_63d_21d_diff},
    "ibs_drv2_038_director_buy_252d_63d_diff":          {"inputs": ["director_buy_value"],                                        "func": ibs_drv2_038_director_buy_252d_63d_diff},
    "ibs_drv2_039_tenpct_buy_63d_21d_diff":             {"inputs": ["tenpct_buy_value"],                                          "func": ibs_drv2_039_tenpct_buy_63d_21d_diff},
    "ibs_drv2_040_tenpct_buy_252d_63d_diff":            {"inputs": ["tenpct_buy_value"],                                          "func": ibs_drv2_040_tenpct_buy_252d_63d_diff},
    "ibs_drv2_041_cfo_buy_63d_21d_diff":                {"inputs": ["cfo_buy_value"],                                             "func": ibs_drv2_041_cfo_buy_63d_21d_diff},
    "ibs_drv2_042_cfo_buy_252d_63d_diff":               {"inputs": ["cfo_buy_value"],                                             "func": ibs_drv2_042_cfo_buy_252d_63d_diff},
    "ibs_drv2_043_buy_shares_63d_21d_diff":             {"inputs": ["insider_buy_shares"],                                        "func": ibs_drv2_043_buy_shares_63d_21d_diff},
    "ibs_drv2_044_buy_shares_252d_63d_diff":            {"inputs": ["insider_buy_shares"],                                        "func": ibs_drv2_044_buy_shares_252d_63d_diff},
    "ibs_drv2_045_buy_shares_252d_pct_chg_63d":         {"inputs": ["insider_buy_shares"],                                        "func": ibs_drv2_045_buy_shares_252d_pct_chg_63d},
    "ibs_drv2_046_buy_to_sell_ratio_63d_21d_diff":      {"inputs": ["insider_buy_value", "insider_sell_value"],                   "func": ibs_drv2_046_buy_to_sell_ratio_63d_21d_diff},
    "ibs_drv2_047_buy_to_sell_ratio_252d_63d_diff":     {"inputs": ["insider_buy_value", "insider_sell_value"],                   "func": ibs_drv2_047_buy_to_sell_ratio_252d_63d_diff},
    "ibs_drv2_048_avg_buy_size_252d_21d_diff":          {"inputs": ["insider_buy_value", "insider_buy_count"],                    "func": ibs_drv2_048_avg_buy_size_252d_21d_diff},
    "ibs_drv2_049_avg_buy_size_252d_63d_diff":          {"inputs": ["insider_buy_value", "insider_buy_count"],                    "func": ibs_drv2_049_avg_buy_size_252d_63d_diff},
    "ibs_drv2_050_peak_buy_value_252d_21d_diff":        {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_050_peak_buy_value_252d_21d_diff},
    "ibs_drv2_051_buy_value_252d_pct_chg_63d":          {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_051_buy_value_252d_pct_chg_63d},
    "ibs_drv2_052_buy_value_21d_63d_diff":              {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_052_buy_value_21d_63d_diff},
    "ibs_drv2_053_buy_value_63d_126d_diff":             {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_053_buy_value_63d_126d_diff},
    "ibs_drv2_054_buy_value_126d_126d_diff":            {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_054_buy_value_126d_126d_diff},
    "ibs_drv2_055_officer_buy_252d_21d_diff":           {"inputs": ["officer_buy_value"],                                         "func": ibs_drv2_055_officer_buy_252d_21d_diff},
    "ibs_drv2_056_officer_buy_63d_pct_chg_21d":         {"inputs": ["officer_buy_value"],                                         "func": ibs_drv2_056_officer_buy_63d_pct_chg_21d},
    "ibs_drv2_057_ceo_buy_252d_21d_diff":               {"inputs": ["ceo_buy_value"],                                             "func": ibs_drv2_057_ceo_buy_252d_21d_diff},
    "ibs_drv2_058_ceo_buy_252d_pct_chg_63d":            {"inputs": ["ceo_buy_value"],                                             "func": ibs_drv2_058_ceo_buy_252d_pct_chg_63d},
    "ibs_drv2_059_director_buy_63d_pct_chg_21d":        {"inputs": ["director_buy_value"],                                        "func": ibs_drv2_059_director_buy_63d_pct_chg_21d},
    "ibs_drv2_060_tenpct_buy_252d_pct_chg_63d":         {"inputs": ["tenpct_buy_value"],                                          "func": ibs_drv2_060_tenpct_buy_252d_pct_chg_63d},
    "ibs_drv2_061_buy_value_63d_zscore_21d_diff":       {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_061_buy_value_63d_zscore_21d_diff},
    "ibs_drv2_062_buy_value_252d_zscore_63d_diff":      {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_062_buy_value_252d_zscore_63d_diff},
    "ibs_drv2_063_buy_value_126d_acceleration":         {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_063_buy_value_126d_acceleration},
    "ibs_drv2_064_buy_value_21d_slope_63d_diff":        {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_064_buy_value_21d_slope_63d_diff},
    "ibs_drv2_065_buy_value_63d_ewm_diff_63d":          {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_065_buy_value_63d_ewm_diff_63d},
    "ibs_drv2_066_net_buy_63d_pct_chg_21d":             {"inputs": ["insider_buy_value", "insider_sell_value"],                   "func": ibs_drv2_066_net_buy_63d_pct_chg_21d},
    "ibs_drv2_067_buy_value_21d_252d_diff":             {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_067_buy_value_21d_252d_diff},
    "ibs_drv2_068_officer_buy_126d_63d_diff":           {"inputs": ["officer_buy_value"],                                         "func": ibs_drv2_068_officer_buy_126d_63d_diff},
    "ibs_drv2_069_ceo_buy_126d_63d_diff":               {"inputs": ["ceo_buy_value"],                                             "func": ibs_drv2_069_ceo_buy_126d_63d_diff},
    "ibs_drv2_070_cfo_buy_252d_pct_chg_63d":            {"inputs": ["cfo_buy_value"],                                             "func": ibs_drv2_070_cfo_buy_252d_pct_chg_63d},
    "ibs_drv2_071_buy_value_63d_252d_slope_63d_diff":   {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_071_buy_value_63d_252d_slope_63d_diff},
    "ibs_drv2_072_buy_shares_126d_21d_diff":            {"inputs": ["insider_buy_shares"],                                        "func": ibs_drv2_072_buy_shares_126d_21d_diff},
    "ibs_drv2_073_director_buy_252d_21d_diff":          {"inputs": ["director_buy_value"],                                        "func": ibs_drv2_073_director_buy_252d_21d_diff},
    "ibs_drv2_074_tenpct_buy_63d_pct_chg_21d":          {"inputs": ["tenpct_buy_value"],                                          "func": ibs_drv2_074_tenpct_buy_63d_pct_chg_21d},
    "ibs_drv2_075_buy_value_5d_21d_diff":               {"inputs": ["insider_buy_value"],                                         "func": ibs_drv2_075_buy_value_5d_21d_diff},
}
