"""
84_insider_buy_size — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative insider buy-size features
Asset class: US equities | Sharadar SF2 insider transactions (daily aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series,
aggregated from Sharadar SF2 insider transaction filings to one row per
(ticker, date).  These are EVENT-DRIVEN series: most days are ZERO; positive
values appear only on filing days.  Do NOT forward-fill these series.
The 3rd-derivative series are extremely sparse on the daily index — this is
correct and expected given the event-driven nature of insider filing data.
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


# ── 2nd-derivative base helpers (self-contained — no cross-file imports) ──────

def _d2_buy_value_21d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 21-day buy value sum."""
    base = _rolling_sum(insider_buy_value, _W21)
    return base - base.shift(_W21)


def _d2_buy_value_63d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 63-day buy value sum."""
    base = _rolling_sum(insider_buy_value, _W63)
    return base - base.shift(_W63)


def _d2_buy_value_252d_63d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 252-day buy value sum."""
    base = _rolling_sum(insider_buy_value, _W252)
    return base - base.shift(_W63)


def _d2_officer_buy_63d(officer_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 63-day officer buy value."""
    base = _rolling_sum(officer_buy_value, _W63)
    return base - base.shift(_W21)


def _d2_ceo_buy_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 63-day CEO buy value."""
    base = _rolling_sum(ceo_buy_value, _W63)
    return base - base.shift(_W21)


def _d2_avg_buy_size_63d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of average buy transaction size (63-day window)."""
    val = _rolling_sum(insider_buy_value, _W63)
    cnt = _rolling_sum(insider_buy_count, _W63)
    base = _safe_div(val, cnt)
    return base - base.shift(_W21)


def _d2_net_buy_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 63-day net buy value."""
    base = _rolling_sum(insider_buy_value, _W63) - _rolling_sum(insider_sell_value, _W63)
    return base - base.shift(_W21)


def _d2_buy_value_21d_pct_chg(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: percent change in 21-day buy value at 21-day lag."""
    base  = _rolling_sum(insider_buy_value, _W21)
    prior = base.shift(_W21)
    return _safe_div(base - prior, prior)


def _d2_buy_value_63d_pct_chg(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: percent change in 63-day buy value at 63-day lag."""
    base  = _rolling_sum(insider_buy_value, _W63)
    prior = base.shift(_W63)
    return _safe_div(base - prior, prior)


def _d2_peak_buy_63d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of peak daily buy value in 63-day window."""
    base = _rolling_max(insider_buy_value, _W63)
    return base - base.shift(_W21)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def ibs_drv3_001_buy_value_21d_d3_21d(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 21-day diff of the 2nd-derivative (21-day diff of 21-day buy sum).
    Captures the jerk (rate of change of acceleration) in short-term buy momentum.
    """
    d2 = _d2_buy_value_21d(insider_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_002_buy_value_63d_d3_63d(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 63-day buy sum).
    Captures jerk in quarterly buy momentum.
    """
    d2 = _d2_buy_value_63d(insider_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_003_buy_value_252d_63d_d3_63d(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 252-day buy sum).
    Captures jerk in annual buy value trend.
    """
    d2 = _d2_buy_value_252d_63d(insider_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_004_buy_value_21d_d3_pct_chg(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: percent change in the 2nd-derivative (21-day diff of 21-day buy sum).
    Captures proportional jerk in short-term buying acceleration.
    """
    d2    = _d2_buy_value_21d(insider_buy_value)
    prior = d2.shift(_W21)
    return _safe_div(d2 - prior, prior.abs())


def ibs_drv3_005_buy_value_63d_d3_pct_chg(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: percent change in the 2nd-derivative (63-day diff of 63-day buy sum).
    """
    d2    = _d2_buy_value_63d(insider_buy_value)
    prior = d2.shift(_W63)
    return _safe_div(d2 - prior, prior.abs())


def ibs_drv3_006_officer_buy_63d_d3_21d(officer_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 21-day diff of the 2nd-derivative of 63-day officer buy value.
    Captures jerk in officer buying pace.
    """
    d2 = _d2_officer_buy_63d(officer_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_007_ceo_buy_63d_d3_21d(ceo_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 21-day diff of the 2nd-derivative of 63-day CEO buy value.
    """
    d2 = _d2_ceo_buy_63d(ceo_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_008_avg_buy_size_63d_d3_21d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """
    3rd derivative: 21-day diff of the 2nd-derivative of average buy transaction size.
    Captures jerk in transaction-size changes.
    """
    d2 = _d2_avg_buy_size_63d(insider_buy_value, insider_buy_count)
    return d2 - d2.shift(_W21)


def ibs_drv3_009_net_buy_63d_d3_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 21-day diff of the 2nd-derivative of 63-day net buy value.
    Captures jerk in net buying momentum.
    """
    d2 = _d2_net_buy_63d(insider_buy_value, insider_sell_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_010_peak_buy_63d_d3_21d(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 21-day diff of the 2nd-derivative of peak daily buy value (63-day).
    Captures jerk in the pace of peak-transaction-size changes.
    """
    d2 = _d2_peak_buy_63d(insider_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_011_buy_value_21d_pct_d3_21d(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 21-day diff of the percent-change-2nd-derivative of 21-day buy sum.
    """
    d2 = _d2_buy_value_21d_pct_chg(insider_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_012_buy_value_63d_pct_d3_63d(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 63-day diff of the percent-change-2nd-derivative of 63-day buy sum.
    """
    d2 = _d2_buy_value_63d_pct_chg(insider_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_013_buy_value_21d_d3_zscore_252d(insider_buy_value: pd.Series) -> pd.Series:
    """
    Z-score of the 3rd-derivative (21d-diff of the 21d-diff of 21-day buy sum)
    within a trailing 252-day window — how extreme is the current jerk vs history.
    """
    d2   = _d2_buy_value_21d(insider_buy_value)
    d3   = d2 - d2.shift(_W21)
    m    = _rolling_mean(d3, _W252)
    sd   = _rolling_std(d3, _W252)
    return _safe_div(d3 - m, sd)


def ibs_drv3_014_buy_value_63d_d3_zscore_252d(insider_buy_value: pd.Series) -> pd.Series:
    """
    Z-score of the 3rd-derivative (63d-diff of the 63d-diff of 63-day buy sum)
    within a trailing 252-day window.
    """
    d2 = _d2_buy_value_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    m  = _rolling_mean(d3, _W252)
    sd = _rolling_std(d3, _W252)
    return _safe_div(d3 - m, sd)


def ibs_drv3_015_buy_value_21d_d3_ewm_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd-derivative (21-day diff of 2nd-derivative of 21-day buy sum)
    divided by its EWM (span=252) — how far the jerk is from its trend.
    """
    d2  = _d2_buy_value_21d(insider_buy_value)
    d3  = d2 - d2.shift(_W21)
    ewm = d3.ewm(span=_W252, min_periods=max(1, _W252 // 4)).mean()
    return _safe_div(d3, ewm)


def ibs_drv3_016_officer_buy_d3_vs_buy_d3_ratio(officer_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """
    Ratio of officer-buy 3rd-derivative to total-buy 3rd-derivative (21-day, 21-day windows).
    Captures whether officer jerk leads total buy jerk.
    """
    d2_off   = _d2_officer_buy_63d(officer_buy_value)
    d3_off   = d2_off - d2_off.shift(_W21)
    d2_total = _d2_buy_value_21d(insider_buy_value)
    d3_total = d2_total - d2_total.shift(_W21)
    return _safe_div(d3_off, d3_total)


def ibs_drv3_017_buy_value_252d_d3_21d(insider_buy_value: pd.Series) -> pd.Series:
    """
    3rd derivative at 21-day lag of the 63-day-diff of 252-day buy sum.
    Measures jerk in the trend of annual buying.
    """
    d2 = _d2_buy_value_252d_63d(insider_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_018_buy_value_21d_d3_sign(insider_buy_value: pd.Series) -> pd.Series:
    """
    Sign of the 3rd-derivative of 21-day buy sum: +1 (increasing acceleration),
    -1 (decreasing acceleration), 0 (flat). Categorical signal.
    """
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    return np.sign(d3)


def ibs_drv3_019_buy_value_63d_d3_sign(insider_buy_value: pd.Series) -> pd.Series:
    """
    Sign of the 3rd-derivative of 63-day buy sum: +1, -1, or 0.
    """
    d2 = _d2_buy_value_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    return np.sign(d3)


def ibs_drv3_020_buy_value_21d_d3_expanding_rank(insider_buy_value: pd.Series) -> pd.Series:
    """
    Expanding percentile rank of the 3rd-derivative (21d jerk of 21-day buy sum).
    How extreme is the current jerk vs all history?
    """
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    return d3.expanding(min_periods=2).rank(pct=True)


def ibs_drv3_021_buy_value_63d_d3_expanding_rank(insider_buy_value: pd.Series) -> pd.Series:
    """
    Expanding percentile rank of the 3rd-derivative (63d jerk of 63-day buy sum).
    """
    d2 = _d2_buy_value_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    return d3.expanding(min_periods=2).rank(pct=True)


def ibs_drv3_022_net_buy_63d_d3_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """
    3rd derivative: 63-day diff of the 2nd-derivative of 63-day net buy value.
    """
    d2 = _d2_net_buy_63d(insider_buy_value, insider_sell_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_023_avg_buy_size_d3_pct_chg(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """
    Percent change in the 2nd-derivative of average buy size (63d window, 21d lag).
    How fast is the transaction-size acceleration itself changing?
    """
    d2    = _d2_avg_buy_size_63d(insider_buy_value, insider_buy_count)
    prior = d2.shift(_W21)
    return _safe_div(d2 - prior, prior.abs())


def ibs_drv3_024_buy_value_21d_d3_rolling_sum_63d(insider_buy_value: pd.Series) -> pd.Series:
    """
    Rolling 63-day sum of the 3rd-derivative of 21-day buy sum (cumulative jerk).
    Captures whether buy-momentum jerk has been consistently positive or negative.
    """
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    return _rolling_sum(d3, _W63)


def ibs_drv3_025_buy_magnitude_d3_composite(insider_buy_value: pd.Series, officer_buy_value: pd.Series, ceo_buy_value: pd.Series) -> pd.Series:
    """
    Composite 3rd-derivative score: equally weighted average of three 3rd-derivatives
    (total buy, officer buy, CEO buy — all using 21-day diff of 21-day-diff of 63-day sum).
    Broad measure of buy-magnitude jerk across all insider roles.
    """
    def _d3_63d_21d(s):
        base = _rolling_sum(s, _W63)
        d1   = base - base.shift(_W21)
        d2   = d1 - d1.shift(_W21)
        return d2 - d2.shift(_W21)

    d3_total = _d3_63d_21d(insider_buy_value)
    d3_off   = _d3_63d_21d(officer_buy_value)
    d3_ceo   = _d3_63d_21d(ceo_buy_value)
    return (d3_total + d3_off + d3_ceo) / 3.0


# ── Additional 2nd-derivative base helpers for 3rd-derivative features 026-075 ─

def _d2_buy_value_126d_63d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 126-day buy value sum."""
    base = _rolling_sum(insider_buy_value, _W126)
    return base - base.shift(_W63)


def _d2_buy_value_504d_63d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 504-day buy value sum."""
    base = _rolling_sum(insider_buy_value, _W504)
    return base - base.shift(_W63)


def _d2_buy_value_252d_21d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 252-day buy value sum."""
    base = _rolling_sum(insider_buy_value, _W252)
    return base - base.shift(_W21)


def _d2_officer_buy_252d_63d(officer_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 252-day officer buy value."""
    base = _rolling_sum(officer_buy_value, _W252)
    return base - base.shift(_W63)


def _d2_officer_buy_126d_21d(officer_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 126-day officer buy value."""
    base = _rolling_sum(officer_buy_value, _W126)
    return base - base.shift(_W21)


def _d2_ceo_buy_252d_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 252-day CEO buy value."""
    base = _rolling_sum(ceo_buy_value, _W252)
    return base - base.shift(_W63)


def _d2_ceo_buy_126d_21d(ceo_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 126-day CEO buy value."""
    base = _rolling_sum(ceo_buy_value, _W126)
    return base - base.shift(_W21)


def _d2_director_buy_63d_21d(director_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 63-day director buy value."""
    base = _rolling_sum(director_buy_value, _W63)
    return base - base.shift(_W21)


def _d2_director_buy_252d_63d(director_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 252-day director buy value."""
    base = _rolling_sum(director_buy_value, _W252)
    return base - base.shift(_W63)


def _d2_tenpct_buy_63d_21d(tenpct_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 63-day 10%+ holder buy value."""
    base = _rolling_sum(tenpct_buy_value, _W63)
    return base - base.shift(_W21)


def _d2_tenpct_buy_252d_63d(tenpct_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 252-day 10%+ holder buy value."""
    base = _rolling_sum(tenpct_buy_value, _W252)
    return base - base.shift(_W63)


def _d2_cfo_buy_63d_21d(cfo_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 63-day CFO buy value."""
    base = _rolling_sum(cfo_buy_value, _W63)
    return base - base.shift(_W21)


def _d2_buy_shares_63d_21d(insider_buy_shares: pd.Series) -> pd.Series:
    """2nd-derivative: 21-day diff of 63-day buy shares sum."""
    base = _rolling_sum(insider_buy_shares, _W63)
    return base - base.shift(_W21)


def _d2_buy_shares_252d_63d(insider_buy_shares: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 252-day buy shares sum."""
    base = _rolling_sum(insider_buy_shares, _W252)
    return base - base.shift(_W63)


def _d2_net_buy_252d_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of 252-day net buy value."""
    base = _rolling_sum(insider_buy_value, _W252) - _rolling_sum(insider_sell_value, _W252)
    return base - base.shift(_W63)


def _d2_buy_value_63d_126d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 126-day diff of 63-day buy value sum."""
    base = _rolling_sum(insider_buy_value, _W63)
    return base - base.shift(_W126)


def _d2_peak_buy_252d_63d(insider_buy_value: pd.Series) -> pd.Series:
    """2nd-derivative: 63-day diff of rolling-252-day peak daily buy value."""
    base = _rolling_max(insider_buy_value, _W252)
    return base - base.shift(_W63)


# ── 3rd-derivative feature functions 026-075 ─────────────────────────────────

def ibs_drv3_026_buy_value_126d_d3_63d(insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 126-day buy sum)."""
    d2 = _d2_buy_value_126d_63d(insider_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_027_buy_value_504d_d3_63d(insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 504-day buy sum)."""
    d2 = _d2_buy_value_504d_63d(insider_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_028_buy_value_252d_21d_d3_21d(insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (21-day diff of 252-day buy sum)."""
    d2 = _d2_buy_value_252d_21d(insider_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_029_officer_buy_252d_d3_63d(officer_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 252-day officer buy)."""
    d2 = _d2_officer_buy_252d_63d(officer_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_030_officer_buy_126d_d3_21d(officer_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (21-day diff of 126-day officer buy)."""
    d2 = _d2_officer_buy_126d_21d(officer_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_031_ceo_buy_252d_d3_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 252-day CEO buy)."""
    d2 = _d2_ceo_buy_252d_63d(ceo_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_032_ceo_buy_126d_d3_21d(ceo_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (21-day diff of 126-day CEO buy)."""
    d2 = _d2_ceo_buy_126d_21d(ceo_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_033_director_buy_63d_d3_21d(director_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (21-day diff of 63-day director buy)."""
    d2 = _d2_director_buy_63d_21d(director_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_034_director_buy_252d_d3_63d(director_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 252-day director buy)."""
    d2 = _d2_director_buy_252d_63d(director_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_035_tenpct_buy_63d_d3_21d(tenpct_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (21-day diff of 63-day 10%+ buy)."""
    d2 = _d2_tenpct_buy_63d_21d(tenpct_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_036_tenpct_buy_252d_d3_63d(tenpct_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 252-day 10%+ buy)."""
    d2 = _d2_tenpct_buy_252d_63d(tenpct_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_037_cfo_buy_63d_d3_21d(cfo_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (21-day diff of 63-day CFO buy)."""
    d2 = _d2_cfo_buy_63d_21d(cfo_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_038_buy_shares_63d_d3_21d(insider_buy_shares: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (21-day diff of 63-day buy shares)."""
    d2 = _d2_buy_shares_63d_21d(insider_buy_shares)
    return d2 - d2.shift(_W21)


def ibs_drv3_039_buy_shares_252d_d3_63d(insider_buy_shares: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 252-day buy shares)."""
    d2 = _d2_buy_shares_252d_63d(insider_buy_shares)
    return d2 - d2.shift(_W63)


def ibs_drv3_040_net_buy_252d_d3_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 252-day net buy)."""
    d2 = _d2_net_buy_252d_63d(insider_buy_value, insider_sell_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_041_buy_value_63d_d3_126d(insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 126-day diff of the 2nd-derivative (126-day diff of 63-day buy sum)."""
    d2 = _d2_buy_value_63d_126d(insider_buy_value)
    return d2 - d2.shift(_W126)


def ibs_drv3_042_peak_buy_252d_d3_63d(insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (63-day diff of 252-day peak buy)."""
    d2 = _d2_peak_buy_252d_63d(insider_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_043_buy_value_21d_d3_63d(insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (21-day diff of 21-day buy sum)."""
    d2 = _d2_buy_value_21d(insider_buy_value)
    return d2 - d2.shift(_W63)


def ibs_drv3_044_buy_value_63d_d3_21d(insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (63-day diff of 63-day buy sum)."""
    d2 = _d2_buy_value_63d(insider_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_045_buy_value_252d_63d_d3_21d(insider_buy_value: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of the 2nd-derivative (63-day diff of 252-day buy sum)."""
    d2 = _d2_buy_value_252d_63d(insider_buy_value)
    return d2 - d2.shift(_W21)


def ibs_drv3_046_buy_value_21d_d3_zscore_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of the 3rd-derivative (21-day jerk of 21-day buy sum) within 504-day window."""
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    m  = _rolling_mean(d3, _W504)
    sd = _rolling_std(d3, _W504)
    return _safe_div(d3 - m, sd)


def ibs_drv3_047_buy_value_63d_d3_zscore_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of the 3rd-derivative (63-day jerk of 63-day buy sum) within 504-day window."""
    d2 = _d2_buy_value_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    m  = _rolling_mean(d3, _W504)
    sd = _rolling_std(d3, _W504)
    return _safe_div(d3 - m, sd)


def ibs_drv3_048_buy_value_21d_d3_rolling_sum_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 252-day sum of the 3rd-derivative of 21-day buy sum (sustained jerk)."""
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    return _rolling_sum(d3, _W252)


def ibs_drv3_049_buy_value_63d_d3_rolling_sum_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 252-day sum of the 3rd-derivative of 63-day buy sum (sustained quarterly jerk)."""
    d2 = _d2_buy_value_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    return _rolling_sum(d3, _W252)


def ibs_drv3_050_buy_value_21d_d3_expanding_zscore(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of the 3rd-derivative of 21-day buy sum (all-history extremity)."""
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    m  = d3.expanding(min_periods=2).mean()
    sd = d3.expanding(min_periods=2).std()
    return _safe_div(d3 - m, sd)


def ibs_drv3_051_buy_value_63d_d3_expanding_zscore(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of the 3rd-derivative of 63-day buy sum."""
    d2 = _d2_buy_value_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    m  = d3.expanding(min_periods=2).mean()
    sd = d3.expanding(min_periods=2).std()
    return _safe_div(d3 - m, sd)


def ibs_drv3_052_director_buy_63d_d3_sign(director_buy_value: pd.Series) -> pd.Series:
    """Sign of the 3rd-derivative of 63-day director buy sum: +1, -1, or 0."""
    d2 = _d2_director_buy_63d_21d(director_buy_value)
    d3 = d2 - d2.shift(_W21)
    return np.sign(d3)


def ibs_drv3_053_tenpct_buy_63d_d3_sign(tenpct_buy_value: pd.Series) -> pd.Series:
    """Sign of the 3rd-derivative of 63-day 10%+ holder buy sum: +1, -1, or 0."""
    d2 = _d2_tenpct_buy_63d_21d(tenpct_buy_value)
    d3 = d2 - d2.shift(_W21)
    return np.sign(d3)


def ibs_drv3_054_officer_buy_d3_sign(officer_buy_value: pd.Series) -> pd.Series:
    """Sign of the 3rd-derivative of 63-day officer buy sum: +1, -1, or 0."""
    d2 = _d2_officer_buy_63d(officer_buy_value)
    d3 = d2 - d2.shift(_W21)
    return np.sign(d3)


def ibs_drv3_055_buy_value_252d_d3_63d_expanding_rank(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding percentile rank of the 3rd-derivative (63-day diff of 63d-diff of 252d buy sum)."""
    d2 = _d2_buy_value_252d_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    return d3.expanding(min_periods=2).rank(pct=True)


def ibs_drv3_056_buy_value_126d_d3_63d_expanding_rank(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding percentile rank of the 3rd-derivative (63-day diff of 63-day diff of 126-day buy sum)."""
    d2 = _d2_buy_value_126d_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    return d3.expanding(min_periods=2).rank(pct=True)


def ibs_drv3_057_buy_value_21d_d3_ewm_ratio_span63(insider_buy_value: pd.Series) -> pd.Series:
    """3rd-derivative of 21-day buy sum divided by its EWM (span=63) — deviation from short trend."""
    d2  = _d2_buy_value_21d(insider_buy_value)
    d3  = d2 - d2.shift(_W21)
    ewm = d3.ewm(span=_W63, min_periods=max(1, _W63 // 4)).mean()
    return _safe_div(d3, ewm)


def ibs_drv3_058_officer_buy_d3_vs_total_buy_d3_63d(officer_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of officer-buy 3rd-derivative (63d lag) to total-buy 3rd-derivative (63d lag)."""
    d2_off   = _d2_officer_buy_252d_63d(officer_buy_value)
    d3_off   = d2_off - d2_off.shift(_W63)
    d2_total = _d2_buy_value_252d_63d(insider_buy_value)
    d3_total = d2_total - d2_total.shift(_W63)
    return _safe_div(d3_off, d3_total)


def ibs_drv3_059_ceo_buy_d3_vs_total_buy_d3_21d(ceo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of CEO-buy 3rd-derivative to total-buy 3rd-derivative (both at 21-day lag of d2)."""
    d2_ceo   = _d2_ceo_buy_63d(ceo_buy_value)
    d3_ceo   = d2_ceo - d2_ceo.shift(_W21)
    d2_total = _d2_buy_value_21d(insider_buy_value)
    d3_total = d2_total - d2_total.shift(_W21)
    return _safe_div(d3_ceo, d3_total)


def ibs_drv3_060_net_buy_63d_d3_21d_sign(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Sign of the 3rd-derivative of 63-day net buy value (21-day lag of 2nd derivative)."""
    d2 = _d2_net_buy_63d(insider_buy_value, insider_sell_value)
    d3 = d2 - d2.shift(_W21)
    return np.sign(d3)


def ibs_drv3_061_buy_value_21d_d3_rolling_sum_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 63-day sum of the 3rd-derivative of 21-day buy sum (near-term jerk accumulation)."""
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    return _rolling_sum(d3, _W63)


def ibs_drv3_062_buy_value_63d_d3_rolling_sum_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 63-day sum of the 3rd-derivative of 63-day buy sum."""
    d2 = _d2_buy_value_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    return _rolling_sum(d3, _W63)


def ibs_drv3_063_buy_value_21d_d3_pct_chg_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change in the 3rd-derivative of 21-day buy sum at 63-day lag."""
    d2    = _d2_buy_value_21d(insider_buy_value)
    d3    = d2 - d2.shift(_W21)
    prior = d3.shift(_W63)
    return _safe_div(d3 - prior, prior.abs())


def ibs_drv3_064_buy_value_63d_d3_pct_chg_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Percent change in the 3rd-derivative of 63-day buy sum at 21-day lag."""
    d2    = _d2_buy_value_63d(insider_buy_value)
    d3    = d2 - d2.shift(_W63)
    prior = d3.shift(_W21)
    return _safe_div(d3 - prior, prior.abs())


def ibs_drv3_065_buy_value_21d_d3_zscore_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of the 3rd-derivative of 21-day buy sum within a 126-day window."""
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    m  = _rolling_mean(d3, _W126)
    sd = _rolling_std(d3, _W126)
    return _safe_div(d3 - m, sd)


def ibs_drv3_066_buy_value_63d_d3_zscore_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of the 3rd-derivative of 63-day buy sum within a 126-day window."""
    d2 = _d2_buy_value_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    m  = _rolling_mean(d3, _W126)
    sd = _rolling_std(d3, _W126)
    return _safe_div(d3 - m, sd)


def ibs_drv3_067_avg_buy_size_63d_d3_63d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative of average buy size (63-day, 21-day)."""
    d2 = _d2_avg_buy_size_63d(insider_buy_value, insider_buy_count)
    return d2 - d2.shift(_W63)


def ibs_drv3_068_buy_shares_63d_d3_63d(insider_buy_shares: pd.Series) -> pd.Series:
    """3rd derivative: 63-day diff of the 2nd-derivative (21-day diff of 63-day buy shares)."""
    d2 = _d2_buy_shares_63d_21d(insider_buy_shares)
    return d2 - d2.shift(_W63)


def ibs_drv3_069_buy_shares_252d_d3_63d_sign(insider_buy_shares: pd.Series) -> pd.Series:
    """Sign of the 3rd-derivative (63-day diff of 63-day diff of 252-day buy shares)."""
    d2 = _d2_buy_shares_252d_63d(insider_buy_shares)
    d3 = d2 - d2.shift(_W63)
    return np.sign(d3)


def ibs_drv3_070_net_buy_252d_d3_63d_sign(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Sign of the 3rd-derivative (63-day diff of 63-day diff of 252-day net buy value)."""
    d2 = _d2_net_buy_252d_63d(insider_buy_value, insider_sell_value)
    d3 = d2 - d2.shift(_W63)
    return np.sign(d3)


def ibs_drv3_071_buy_value_252d_d3_63d_zscore_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of the 3rd-derivative (63d-diff of 63d-diff of 252-day buy sum) within 252-day window."""
    d2 = _d2_buy_value_252d_63d(insider_buy_value)
    d3 = d2 - d2.shift(_W63)
    m  = _rolling_mean(d3, _W252)
    sd = _rolling_std(d3, _W252)
    return _safe_div(d3 - m, sd)


def ibs_drv3_072_buy_value_21d_d4_21d(insider_buy_value: pd.Series) -> pd.Series:
    """
    4th-order finite difference of 21-day buy sum at 21-day lag
    (third diff of the third diff, i.e., jerk-of-jerk).
    """
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    return d3 - d3.shift(_W21)


def ibs_drv3_073_buy_magnitude_d3_composite_63d(insider_buy_value: pd.Series, officer_buy_value: pd.Series, ceo_buy_value: pd.Series) -> pd.Series:
    """Composite 3rd-derivative (63-day lag): equally weighted avg of three 63-day-jerk signals."""
    def _d3_63d_63d(s):
        base = _rolling_sum(s, _W63)
        d1   = base - base.shift(_W63)
        d2   = d1 - d1.shift(_W63)
        return d2 - d2.shift(_W63)

    return (_d3_63d_63d(insider_buy_value) + _d3_63d_63d(officer_buy_value) + _d3_63d_63d(ceo_buy_value)) / 3.0


def ibs_drv3_074_director_buy_d3_vs_ceo_buy_d3_21d(director_buy_value: pd.Series, ceo_buy_value: pd.Series) -> pd.Series:
    """Ratio of director-buy 3rd-derivative to CEO-buy 3rd-derivative (21-day lag)."""
    d2_dir = _d2_director_buy_63d_21d(director_buy_value)
    d3_dir = d2_dir - d2_dir.shift(_W21)
    d2_ceo = _d2_ceo_buy_63d(ceo_buy_value)
    d3_ceo = d2_ceo - d2_ceo.shift(_W21)
    return _safe_div(d3_dir, d3_ceo)


def ibs_drv3_075_buy_value_21d_d3_rolling_max_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 63-day max of the absolute 3rd-derivative of 21-day buy sum (peak jerk magnitude)."""
    d2 = _d2_buy_value_21d(insider_buy_value)
    d3 = d2 - d2.shift(_W21)
    return _rolling_max(d3.abs(), _W63)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

INSIDER_BUY_SIZE_REGISTRY_3RD_DERIVATIVES = {
    "ibs_drv3_001_buy_value_21d_d3_21d":              {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_001_buy_value_21d_d3_21d},
    "ibs_drv3_002_buy_value_63d_d3_63d":              {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_002_buy_value_63d_d3_63d},
    "ibs_drv3_003_buy_value_252d_63d_d3_63d":         {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_003_buy_value_252d_63d_d3_63d},
    "ibs_drv3_004_buy_value_21d_d3_pct_chg":          {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_004_buy_value_21d_d3_pct_chg},
    "ibs_drv3_005_buy_value_63d_d3_pct_chg":          {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_005_buy_value_63d_d3_pct_chg},
    "ibs_drv3_006_officer_buy_63d_d3_21d":            {"inputs": ["officer_buy_value"],                                       "func": ibs_drv3_006_officer_buy_63d_d3_21d},
    "ibs_drv3_007_ceo_buy_63d_d3_21d":                {"inputs": ["ceo_buy_value"],                                           "func": ibs_drv3_007_ceo_buy_63d_d3_21d},
    "ibs_drv3_008_avg_buy_size_63d_d3_21d":           {"inputs": ["insider_buy_value", "insider_buy_count"],                  "func": ibs_drv3_008_avg_buy_size_63d_d3_21d},
    "ibs_drv3_009_net_buy_63d_d3_21d":                {"inputs": ["insider_buy_value", "insider_sell_value"],                 "func": ibs_drv3_009_net_buy_63d_d3_21d},
    "ibs_drv3_010_peak_buy_63d_d3_21d":               {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_010_peak_buy_63d_d3_21d},
    "ibs_drv3_011_buy_value_21d_pct_d3_21d":          {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_011_buy_value_21d_pct_d3_21d},
    "ibs_drv3_012_buy_value_63d_pct_d3_63d":          {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_012_buy_value_63d_pct_d3_63d},
    "ibs_drv3_013_buy_value_21d_d3_zscore_252d":      {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_013_buy_value_21d_d3_zscore_252d},
    "ibs_drv3_014_buy_value_63d_d3_zscore_252d":      {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_014_buy_value_63d_d3_zscore_252d},
    "ibs_drv3_015_buy_value_21d_d3_ewm_ratio":        {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_015_buy_value_21d_d3_ewm_ratio},
    "ibs_drv3_016_officer_buy_d3_vs_buy_d3_ratio":    {"inputs": ["officer_buy_value", "insider_buy_value"],                  "func": ibs_drv3_016_officer_buy_d3_vs_buy_d3_ratio},
    "ibs_drv3_017_buy_value_252d_d3_21d":             {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_017_buy_value_252d_d3_21d},
    "ibs_drv3_018_buy_value_21d_d3_sign":             {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_018_buy_value_21d_d3_sign},
    "ibs_drv3_019_buy_value_63d_d3_sign":             {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_019_buy_value_63d_d3_sign},
    "ibs_drv3_020_buy_value_21d_d3_expanding_rank":   {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_020_buy_value_21d_d3_expanding_rank},
    "ibs_drv3_021_buy_value_63d_d3_expanding_rank":   {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_021_buy_value_63d_d3_expanding_rank},
    "ibs_drv3_022_net_buy_63d_d3_63d":                {"inputs": ["insider_buy_value", "insider_sell_value"],                 "func": ibs_drv3_022_net_buy_63d_d3_63d},
    "ibs_drv3_023_avg_buy_size_d3_pct_chg":           {"inputs": ["insider_buy_value", "insider_buy_count"],                  "func": ibs_drv3_023_avg_buy_size_d3_pct_chg},
    "ibs_drv3_024_buy_value_21d_d3_rolling_sum_63d":  {"inputs": ["insider_buy_value"],                                       "func": ibs_drv3_024_buy_value_21d_d3_rolling_sum_63d},
    "ibs_drv3_025_buy_magnitude_d3_composite":        {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value"], "func": ibs_drv3_025_buy_magnitude_d3_composite},
    "ibs_drv3_026_buy_value_126d_d3_63d":             {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_026_buy_value_126d_d3_63d},
    "ibs_drv3_027_buy_value_504d_d3_63d":             {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_027_buy_value_504d_d3_63d},
    "ibs_drv3_028_buy_value_252d_21d_d3_21d":         {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_028_buy_value_252d_21d_d3_21d},
    "ibs_drv3_029_officer_buy_252d_d3_63d":           {"inputs": ["officer_buy_value"],                                        "func": ibs_drv3_029_officer_buy_252d_d3_63d},
    "ibs_drv3_030_officer_buy_126d_d3_21d":           {"inputs": ["officer_buy_value"],                                        "func": ibs_drv3_030_officer_buy_126d_d3_21d},
    "ibs_drv3_031_ceo_buy_252d_d3_63d":               {"inputs": ["ceo_buy_value"],                                            "func": ibs_drv3_031_ceo_buy_252d_d3_63d},
    "ibs_drv3_032_ceo_buy_126d_d3_21d":               {"inputs": ["ceo_buy_value"],                                            "func": ibs_drv3_032_ceo_buy_126d_d3_21d},
    "ibs_drv3_033_director_buy_63d_d3_21d":           {"inputs": ["director_buy_value"],                                       "func": ibs_drv3_033_director_buy_63d_d3_21d},
    "ibs_drv3_034_director_buy_252d_d3_63d":          {"inputs": ["director_buy_value"],                                       "func": ibs_drv3_034_director_buy_252d_d3_63d},
    "ibs_drv3_035_tenpct_buy_63d_d3_21d":             {"inputs": ["tenpct_buy_value"],                                         "func": ibs_drv3_035_tenpct_buy_63d_d3_21d},
    "ibs_drv3_036_tenpct_buy_252d_d3_63d":            {"inputs": ["tenpct_buy_value"],                                         "func": ibs_drv3_036_tenpct_buy_252d_d3_63d},
    "ibs_drv3_037_cfo_buy_63d_d3_21d":                {"inputs": ["cfo_buy_value"],                                            "func": ibs_drv3_037_cfo_buy_63d_d3_21d},
    "ibs_drv3_038_buy_shares_63d_d3_21d":             {"inputs": ["insider_buy_shares"],                                       "func": ibs_drv3_038_buy_shares_63d_d3_21d},
    "ibs_drv3_039_buy_shares_252d_d3_63d":            {"inputs": ["insider_buy_shares"],                                       "func": ibs_drv3_039_buy_shares_252d_d3_63d},
    "ibs_drv3_040_net_buy_252d_d3_63d":               {"inputs": ["insider_buy_value", "insider_sell_value"],                  "func": ibs_drv3_040_net_buy_252d_d3_63d},
    "ibs_drv3_041_buy_value_63d_d3_126d":             {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_041_buy_value_63d_d3_126d},
    "ibs_drv3_042_peak_buy_252d_d3_63d":              {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_042_peak_buy_252d_d3_63d},
    "ibs_drv3_043_buy_value_21d_d3_63d":              {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_043_buy_value_21d_d3_63d},
    "ibs_drv3_044_buy_value_63d_d3_21d":              {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_044_buy_value_63d_d3_21d},
    "ibs_drv3_045_buy_value_252d_63d_d3_21d":         {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_045_buy_value_252d_63d_d3_21d},
    "ibs_drv3_046_buy_value_21d_d3_zscore_504d":      {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_046_buy_value_21d_d3_zscore_504d},
    "ibs_drv3_047_buy_value_63d_d3_zscore_504d":      {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_047_buy_value_63d_d3_zscore_504d},
    "ibs_drv3_048_buy_value_21d_d3_rolling_sum_252d": {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_048_buy_value_21d_d3_rolling_sum_252d},
    "ibs_drv3_049_buy_value_63d_d3_rolling_sum_252d": {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_049_buy_value_63d_d3_rolling_sum_252d},
    "ibs_drv3_050_buy_value_21d_d3_expanding_zscore": {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_050_buy_value_21d_d3_expanding_zscore},
    "ibs_drv3_051_buy_value_63d_d3_expanding_zscore": {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_051_buy_value_63d_d3_expanding_zscore},
    "ibs_drv3_052_director_buy_63d_d3_sign":          {"inputs": ["director_buy_value"],                                       "func": ibs_drv3_052_director_buy_63d_d3_sign},
    "ibs_drv3_053_tenpct_buy_63d_d3_sign":            {"inputs": ["tenpct_buy_value"],                                         "func": ibs_drv3_053_tenpct_buy_63d_d3_sign},
    "ibs_drv3_054_officer_buy_d3_sign":               {"inputs": ["officer_buy_value"],                                        "func": ibs_drv3_054_officer_buy_d3_sign},
    "ibs_drv3_055_buy_value_252d_d3_63d_expanding_rank":{"inputs": ["insider_buy_value"],                                      "func": ibs_drv3_055_buy_value_252d_d3_63d_expanding_rank},
    "ibs_drv3_056_buy_value_126d_d3_63d_expanding_rank":{"inputs": ["insider_buy_value"],                                      "func": ibs_drv3_056_buy_value_126d_d3_63d_expanding_rank},
    "ibs_drv3_057_buy_value_21d_d3_ewm_ratio_span63": {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_057_buy_value_21d_d3_ewm_ratio_span63},
    "ibs_drv3_058_officer_buy_d3_vs_total_buy_d3_63d":{"inputs": ["officer_buy_value", "insider_buy_value"],                   "func": ibs_drv3_058_officer_buy_d3_vs_total_buy_d3_63d},
    "ibs_drv3_059_ceo_buy_d3_vs_total_buy_d3_21d":    {"inputs": ["ceo_buy_value", "insider_buy_value"],                       "func": ibs_drv3_059_ceo_buy_d3_vs_total_buy_d3_21d},
    "ibs_drv3_060_net_buy_63d_d3_21d_sign":           {"inputs": ["insider_buy_value", "insider_sell_value"],                  "func": ibs_drv3_060_net_buy_63d_d3_21d_sign},
    "ibs_drv3_061_buy_value_21d_d3_rolling_sum_63d":  {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_061_buy_value_21d_d3_rolling_sum_63d},
    "ibs_drv3_062_buy_value_63d_d3_rolling_sum_63d":  {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_062_buy_value_63d_d3_rolling_sum_63d},
    "ibs_drv3_063_buy_value_21d_d3_pct_chg_63d":      {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_063_buy_value_21d_d3_pct_chg_63d},
    "ibs_drv3_064_buy_value_63d_d3_pct_chg_21d":      {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_064_buy_value_63d_d3_pct_chg_21d},
    "ibs_drv3_065_buy_value_21d_d3_zscore_126d":      {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_065_buy_value_21d_d3_zscore_126d},
    "ibs_drv3_066_buy_value_63d_d3_zscore_126d":      {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_066_buy_value_63d_d3_zscore_126d},
    "ibs_drv3_067_avg_buy_size_63d_d3_63d":           {"inputs": ["insider_buy_value", "insider_buy_count"],                   "func": ibs_drv3_067_avg_buy_size_63d_d3_63d},
    "ibs_drv3_068_buy_shares_63d_d3_63d":             {"inputs": ["insider_buy_shares"],                                       "func": ibs_drv3_068_buy_shares_63d_d3_63d},
    "ibs_drv3_069_buy_shares_252d_d3_63d_sign":       {"inputs": ["insider_buy_shares"],                                       "func": ibs_drv3_069_buy_shares_252d_d3_63d_sign},
    "ibs_drv3_070_net_buy_252d_d3_63d_sign":          {"inputs": ["insider_buy_value", "insider_sell_value"],                  "func": ibs_drv3_070_net_buy_252d_d3_63d_sign},
    "ibs_drv3_071_buy_value_252d_d3_63d_zscore_252d": {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_071_buy_value_252d_d3_63d_zscore_252d},
    "ibs_drv3_072_buy_value_21d_d4_21d":              {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_072_buy_value_21d_d4_21d},
    "ibs_drv3_073_buy_magnitude_d3_composite_63d":    {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value"],  "func": ibs_drv3_073_buy_magnitude_d3_composite_63d},
    "ibs_drv3_074_director_buy_d3_vs_ceo_buy_d3_21d": {"inputs": ["director_buy_value", "ceo_buy_value"],                     "func": ibs_drv3_074_director_buy_d3_vs_ceo_buy_d3_21d},
    "ibs_drv3_075_buy_value_21d_d3_rolling_max_63d":  {"inputs": ["insider_buy_value"],                                        "func": ibs_drv3_075_buy_value_21d_d3_rolling_max_63d},
}
