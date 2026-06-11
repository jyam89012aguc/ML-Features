"""
70_dilution_acceleration — Base Features 076-150
Domain: share-count dilution, secondary issuance, share-count growth acceleration
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Quarterly cadence on the daily index: 1 quarter = 63 trading
days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): Share-count acceleration (2nd difference of levels) ---

def dla_076_sharesbas_qoq_acceleration(sharesbas: pd.Series) -> pd.Series:
    """
    Acceleration of QoQ share growth: 2nd difference over 63-day steps.
    d2/dq2 of sharesbas — rising = share growth is speeding up.
    """
    d1 = sharesbas - sharesbas.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def dla_077_sharesbas_zscore_12q(sharesbas: pd.Series) -> pd.Series:
    """Rolling 12-quarter (3-year, 756-day) z-score of basic shares outstanding (extremity vs 3-year window)."""
    return _zscore_rolling(sharesbas, _TD_3Y)


def dla_078_shareswa_qoq_acceleration(shareswa: pd.Series) -> pd.Series:
    """Acceleration of QoQ weighted-average basic share growth."""
    d1 = shareswa - shareswa.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def dla_079_shareswadil_pct_rank_3y(shareswadil: pd.Series) -> pd.Series:
    """Rolling 3-year (756-day) percentile rank of diluted weighted-average shares (position in 3-year dilution history)."""
    return _rolling_rank_pct(shareswadil, _TD_3Y)


def dla_080_sharesbas_rolling_min_4q(sharesbas: pd.Series) -> pd.Series:
    """Rolling 4-quarter (252-day) minimum of basic shares outstanding (lowest share count in past year)."""
    return _rolling_min(sharesbas, _TD_YEAR)


def dla_081_sharesbas_yoy_pct_acceleration(sharesbas: pd.Series) -> pd.Series:
    """Acceleration of YoY percent share growth (2nd diff of YoY pct)."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_YEAR), sharesbas.shift(_TD_YEAR).replace(0, np.nan))
    return pct - pct.shift(_TD_YEAR)


def dla_082_ncfcommon_qoq_change(ncfcommon: pd.Series) -> pd.Series:
    """QoQ absolute change in equity issuance (ncfcommon)."""
    return ncfcommon - ncfcommon.shift(_TD_QTR)


def dla_083_ncfcommon_qoq_pct(ncfcommon: pd.Series) -> pd.Series:
    """QoQ percent change in equity issuance; denominator is abs(prior)."""
    prior = ncfcommon.shift(_TD_QTR)
    return _safe_div_abs(ncfcommon - prior, prior)


def dla_084_ncfcommon_acceleration(ncfcommon: pd.Series) -> pd.Series:
    """Acceleration of ncfcommon: 2nd QoQ difference of equity issuance."""
    d1 = ncfcommon - ncfcommon.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def dla_085_sbcomp_qoq_change(sbcomp: pd.Series) -> pd.Series:
    """QoQ absolute change in stock-based compensation."""
    return sbcomp - sbcomp.shift(_TD_QTR)


def dla_086_sbcomp_qoq_pct(sbcomp: pd.Series) -> pd.Series:
    """QoQ percent change in stock-based compensation."""
    prior = sbcomp.shift(_TD_QTR)
    return _safe_div_abs(sbcomp - prior, prior)


def dla_087_sbcomp_acceleration(sbcomp: pd.Series) -> pd.Series:
    """Acceleration of SBC: 2nd QoQ difference of stock-based compensation."""
    d1 = sbcomp - sbcomp.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def dla_088_diluted_basic_gap_zscore_12q(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Z-score of the diluted-minus-basic share gap within a trailing 3-year window."""
    gap = shareswadil - shareswa
    return _zscore_rolling(gap, _TD_3Y)


def dla_089_sharesbas_qoq_slope_4q(sharesbas: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ share-count change.
    Captures the trend direction in quarterly issuance momentum.
    """
    base = sharesbas - sharesbas.shift(_TD_QTR)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def dla_090_sharesbas_yoy_slope_4q(sharesbas: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the YoY share-count change series.
    """
    base = sharesbas - sharesbas.shift(_TD_YEAR)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


# --- Group I (091-105): Issuance pace, recency, and frequency signals ---

def dla_091_issuance_quarters_2y(ncfcommon: pd.Series) -> pd.Series:
    """Count of issuance quarters (ncfcommon > 0) in the trailing 2 years."""
    flag = (ncfcommon > 0).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def dla_092_issuance_quarters_3y(ncfcommon: pd.Series) -> pd.Series:
    """Count of issuance quarters (ncfcommon > 0) in the trailing 3 years."""
    flag = (ncfcommon > 0).astype(float)
    return _rolling_sum(flag, _TD_3Y)


def dla_093_issuance_fraction_2y(ncfcommon: pd.Series) -> pd.Series:
    """Fraction of 2-year window where equity was actively issued."""
    flag = (ncfcommon > 0).astype(float)
    return _rolling_mean(flag, _TD_2Y)


def dla_094_issuance_fraction_3y(ncfcommon: pd.Series) -> pd.Series:
    """Fraction of 3-year window where equity was actively issued."""
    flag = (ncfcommon > 0).astype(float)
    return _rolling_mean(flag, _TD_3Y)


def dla_095_consecutive_issuance_streak(ncfcommon: pd.Series) -> pd.Series:
    """
    Current consecutive-issuance streak length (quarters where ncfcommon > 0).
    Resets to 0 when issuance stops.
    """
    flag = (ncfcommon > 0).astype(int)
    streak = np.zeros(len(flag), dtype=float)
    arr = flag.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=ncfcommon.index)


def dla_096_max_single_quarter_issuance_1y(ncfcommon: pd.Series) -> pd.Series:
    """Maximum single-quarter equity raise in trailing 1 year (peak issuance event)."""
    return _rolling_max(ncfcommon, _TD_YEAR)


def dla_097_max_single_quarter_issuance_3y(ncfcommon: pd.Series) -> pd.Series:
    """Maximum single-quarter equity raise in trailing 3 years."""
    return _rolling_max(ncfcommon, _TD_3Y)


def dla_098_ncfcommon_current_vs_4q_avg(ncfcommon: pd.Series) -> pd.Series:
    """Current ncfcommon minus trailing 4-quarter average issuance."""
    return ncfcommon - _rolling_mean(ncfcommon, _TD_YEAR)


def dla_099_ncfcommon_zscore_4q(ncfcommon: pd.Series) -> pd.Series:
    """Z-score of ncfcommon within trailing 4-quarter window."""
    return _zscore_rolling(ncfcommon, _TD_YEAR)


def dla_100_ncfcommon_zscore_8q(ncfcommon: pd.Series) -> pd.Series:
    """Z-score of ncfcommon within trailing 8-quarter window."""
    return _zscore_rolling(ncfcommon, _TD_2Y)


def dla_101_ncfcommon_pct_rank_4q(ncfcommon: pd.Series) -> pd.Series:
    """Percentile rank of ncfcommon within trailing 4-quarter window."""
    return _rolling_rank_pct(ncfcommon, _TD_YEAR)


def dla_102_ncfcommon_expanding_pct_rank(ncfcommon: pd.Series) -> pd.Series:
    """Expanding percentile rank of ncfcommon (all-history issuance rank)."""
    return ncfcommon.expanding(min_periods=2).rank(pct=True)


def dla_103_sharesbas_vs_4q_avg(sharesbas: pd.Series) -> pd.Series:
    """Basic shares minus trailing 4-quarter mean (level deviation from recent average)."""
    return sharesbas - _rolling_mean(sharesbas, _TD_YEAR)


def dla_104_sharesbas_vs_8q_avg(sharesbas: pd.Series) -> pd.Series:
    """Basic shares minus trailing 8-quarter mean."""
    return sharesbas - _rolling_mean(sharesbas, _TD_2Y)


def dla_105_sharesbas_pct_vs_4q_avg(sharesbas: pd.Series) -> pd.Series:
    """Basic shares percent deviation from trailing 4-quarter mean."""
    avg = _rolling_mean(sharesbas, _TD_YEAR)
    return _safe_div_abs(sharesbas - avg, avg)


# --- Group J (106-120): SBC-attributed dilution vs equity and operations ---

def dla_106_sbcomp_to_revenue_ratio(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    """SBC as fraction of revenue (SBC burden relative to top line)."""
    return _safe_div(sbcomp, revenue.abs().replace(0, np.nan))


def dla_107_sbcomp_to_assets_ratio(sbcomp: pd.Series, assets: pd.Series) -> pd.Series:
    """SBC as fraction of total assets."""
    return _safe_div(sbcomp, assets.replace(0, np.nan))


def dla_108_sbcomp_to_ncfo_ratio(sbcomp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """SBC as fraction of operating cash flow (SBC as proportion of cash generation)."""
    return _safe_div(sbcomp, ncfo.abs().replace(0, np.nan))


def dla_109_sbcomp_trailing_4q_to_equity(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """TTM SBC as fraction of current book equity."""
    ttm = _rolling_sum(sbcomp, _TD_YEAR)
    return _safe_div(ttm, equity.abs().replace(0, np.nan))


def dla_110_sbcomp_trailing_4q_to_revenue(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    """TTM SBC as fraction of trailing 4-quarter mean revenue."""
    ttm_sbc = _rolling_sum(sbcomp, _TD_YEAR)
    avg_rev = _rolling_mean(revenue, _TD_YEAR)
    return _safe_div(ttm_sbc, avg_rev.abs().replace(0, np.nan))


def dla_111_sbcomp_pct_rank_4q(sbcomp: pd.Series) -> pd.Series:
    """Percentile rank of SBC within trailing 4-quarter window."""
    return _rolling_rank_pct(sbcomp, _TD_YEAR)


def dla_112_sbcomp_at_3y_high_flag(sbcomp: pd.Series) -> pd.Series:
    """1 if current SBC equals or exceeds its 3-year rolling maximum."""
    mx = _rolling_max(sbcomp, _TD_3Y)
    return (sbcomp >= mx).astype(float)


def dla_113_sbcomp_drawdown_from_3y_peak(sbcomp: pd.Series) -> pd.Series:
    """SBC level vs its 3-year rolling peak (how much below peak)."""
    peak = _rolling_max(sbcomp, _TD_3Y)
    return sbcomp - peak


def dla_114_sbcomp_expanding_pct_rank(sbcomp: pd.Series) -> pd.Series:
    """Expanding percentile rank of SBC (all-history SBC rank)."""
    return sbcomp.expanding(min_periods=2).rank(pct=True)


def dla_115_sbcomp_zscore_8q(sbcomp: pd.Series) -> pd.Series:
    """Z-score of SBC within trailing 8-quarter window."""
    return _zscore_rolling(sbcomp, _TD_2Y)


def dla_116_equity_per_share_qoq_change(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """QoQ change in book equity per basic share (book value dilution per share)."""
    bvps = _safe_div(equity, sharesbas.replace(0, np.nan))
    return bvps - bvps.shift(_TD_QTR)


def dla_117_equity_per_share_yoy_change(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """YoY change in book equity per basic share."""
    bvps = _safe_div(equity, sharesbas.replace(0, np.nan))
    return bvps - bvps.shift(_TD_YEAR)


def dla_118_equity_per_share_yoy_pct(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """YoY percent change in book equity per share (per-share equity dilution rate)."""
    bvps  = _safe_div(equity, sharesbas.replace(0, np.nan))
    prior = bvps.shift(_TD_YEAR)
    return _safe_div_abs(bvps - prior, prior)


def dla_119_equity_declining_while_shares_rising(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Binary: 1 if equity fell YoY AND shares rose YoY simultaneously
    (classic distress dilution — raising equity but it's being consumed by losses).
    """
    eq_fell   = (equity < equity.shift(_TD_YEAR)).astype(float)
    shr_rose  = (sharesbas > sharesbas.shift(_TD_YEAR)).astype(float)
    return eq_fell * shr_rose


def dla_120_equity_per_diluted_share_qoq_change(equity: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """QoQ change in book equity per diluted share."""
    bvps = _safe_div(equity, shareswadil.replace(0, np.nan))
    return bvps - bvps.shift(_TD_QTR)


# --- Group K (121-135): Multi-field dilution burden composites ---

def dla_121_total_dilution_3y_pct(sharesbas: pd.Series, sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Composite 3-year dilution burden:
    sharesbas 3Y pct change + (3Y SBC sum / avg equity), equally weighted.
    """
    shr_3y = _safe_div(sharesbas - sharesbas.shift(_TD_3Y), sharesbas.shift(_TD_3Y).replace(0, np.nan))
    sbc_3y = _rolling_sum(sbcomp, _TD_3Y)
    avg_eq = _rolling_mean(equity.abs(), _TD_3Y)
    sbc_rat = _safe_div(sbc_3y, avg_eq.replace(0, np.nan))
    return (shr_3y + sbc_rat) / 2.0


def dla_122_sharesbas_drawdown_from_3y_low(sharesbas: pd.Series) -> pd.Series:
    """
    Current shares minus their 3-year rolling minimum
    (how much share count has been added above the 3-year trough).
    """
    mn = _rolling_min(sharesbas, _TD_3Y)
    return sharesbas - mn


def dla_123_sharesbas_drawdown_from_expanding_min(sharesbas: pd.Series) -> pd.Series:
    """Current shares minus their all-history expanding minimum."""
    mn = sharesbas.expanding(min_periods=1).min()
    return sharesbas - mn


def dla_124_ncfcommon_to_sharesbas_growth(ncfcommon: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Equity raised (ncfcommon) divided by absolute QoQ change in shares
    — implied price at which shares were issued proxy.
    """
    shr_chg = (sharesbas - sharesbas.shift(_TD_QTR)).abs()
    return _safe_div(ncfcommon, shr_chg.replace(0, np.nan))


def dla_125_sharesbas_qoq_pct_vs_4q_avg(sharesbas: pd.Series) -> pd.Series:
    """
    Current QoQ share growth pct minus trailing 4-quarter mean QoQ share growth.
    Is this quarter's issuance pace above or below recent average?
    """
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    return pct - _rolling_mean(pct, _TD_YEAR)


def dla_126_sharesbas_pct_rank_8q(sharesbas: pd.Series) -> pd.Series:
    """Rolling 8-quarter (2-year, 504-day) percentile rank of basic shares outstanding (2-year share-count position)."""
    return _rolling_rank_pct(sharesbas, _TD_2Y)


def dla_127_diluted_basic_gap_at_5y_high_flag(shareswa: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """State flag: the diluted-minus-basic share gap (option overhang) sits at a trailing 5-year high."""
    gap = shareswadil - shareswa
    return (gap >= _rolling_max(gap, _TD_5Y) - _EPS).astype(float)


def dla_128_sharesbas_level_z_expanding(sharesbas: pd.Series) -> pd.Series:
    """Expanding z-score of basic shares outstanding (all-history share-count extremity)."""
    m  = sharesbas.expanding(min_periods=2).mean()
    sd = sharesbas.expanding(min_periods=2).std()
    return _safe_div(sharesbas - m, sd)


def dla_129_ncfcommon_positive_consecutive_2q(ncfcommon: pd.Series) -> pd.Series:
    """1 if ncfcommon was positive in both the current and prior quarter."""
    curr = (ncfcommon > 0).astype(float)
    prev = (ncfcommon.shift(_TD_QTR) > 0).astype(float)
    return curr * prev


def dla_130_ncfcommon_positive_consecutive_4q(ncfcommon: pd.Series) -> pd.Series:
    """1 if ncfcommon was positive in each of the last 4 quarters."""
    def _all_pos(s):
        return (s > 0).astype(float)
    c0 = _all_pos(ncfcommon)
    c1 = _all_pos(ncfcommon.shift(_TD_QTR))
    c2 = _all_pos(ncfcommon.shift(_TD_2Q))
    c3 = _all_pos(ncfcommon.shift(3 * _TD_QTR))
    return (c0 * c1 * c2 * c3)


def dla_131_shares_issued_3y_sum(sharesbas: pd.Series) -> pd.Series:
    """Cumulative net shares issued over 3 years (absolute, in share units)."""
    return (sharesbas - sharesbas.shift(_TD_QTR)).clip(lower=0).rolling(_TD_3Y, min_periods=max(1, _TD_3Y // 4)).sum()


def dla_132_shares_retired_3y_sum(sharesbas: pd.Series) -> pd.Series:
    """Cumulative net shares retired (buybacks) over 3 years (absolute, in share units)."""
    return (sharesbas.shift(_TD_QTR) - sharesbas).clip(lower=0).rolling(_TD_3Y, min_periods=max(1, _TD_3Y // 4)).sum()


def dla_133_net_shares_issued_vs_retired_3y(sharesbas: pd.Series) -> pd.Series:
    """Net issuance minus buybacks over 3 years (net dilution direction)."""
    issued  = (sharesbas - sharesbas.shift(_TD_QTR)).clip(lower=0).rolling(_TD_3Y, min_periods=max(1, _TD_3Y // 4)).sum()
    retired = (sharesbas.shift(_TD_QTR) - sharesbas).clip(lower=0).rolling(_TD_3Y, min_periods=max(1, _TD_3Y // 4)).sum()
    return issued - retired


def dla_134_dilution_velocity_1y(sharesbas: pd.Series) -> pd.Series:
    """
    1-year OLS slope of sharesbas on its own daily index
    (rate of share-count change per trading day over trailing year).
    """
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return sharesbas.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def dla_135_dilution_velocity_3y(sharesbas: pd.Series) -> pd.Series:
    """
    3-year OLS slope of sharesbas on its own daily index.
    """
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return sharesbas.rolling(_TD_3Y, min_periods=max(2, _TD_3Y // 4)).apply(_slope, raw=True)


# --- Group L (136-150): Advanced distress-dilution and cross-field features ---

def dla_136_distress_dilution_consecutive_streak(sharesbas: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Consecutive-quarter streak length of distress-dilution events
    (shares rising QoQ while equity <= 0). Resets on non-event.
    """
    dd = ((sharesbas > sharesbas.shift(_TD_QTR)) & (equity <= 0)).astype(int)
    streak = np.zeros(len(dd), dtype=float)
    arr = dd.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=sharesbas.index)


def dla_137_sharesbas_3y_pct_change(sharesbas: pd.Series) -> pd.Series:
    """Basic shares 3-year cumulative percent change."""
    prior = sharesbas.shift(_TD_3Y)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def dla_138_shareswadil_zscore_8q(shareswadil: pd.Series) -> pd.Series:
    """Rolling 8-quarter (2-year, 504-day) z-score of diluted weighted-average shares (2-year dilution extremity)."""
    return _zscore_rolling(shareswadil, _TD_2Y)


def dla_139_sbcomp_to_sharesbas_qoq_growth(sbcomp: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    SBC divided by (QoQ share growth * 100) — implied SBC cost per new share.
    Proxy for share-price at which SBC awards vest.
    """
    shr_chg = (sharesbas - sharesbas.shift(_TD_QTR)).abs().replace(0, np.nan)
    return _safe_div(sbcomp, shr_chg)


def dla_140_equity_raised_fraction_of_3y_equity_change(ncfcommon: pd.Series, equity: pd.Series) -> pd.Series:
    """
    3-year cumulative equity raised divided by absolute 3-year equity change.
    How much of the equity change is from external raises vs retained earnings?
    """
    iss_3y = _rolling_sum(ncfcommon.clip(lower=0), _TD_3Y)
    eq_chg = (equity - equity.shift(_TD_3Y)).abs().replace(0, np.nan)
    return _safe_div(iss_3y, eq_chg)


def dla_141_shareswadil_3y_pct_change(shareswadil: pd.Series) -> pd.Series:
    """Diluted WA shares 3-year cumulative percent change."""
    prior = shareswadil.shift(_TD_3Y)
    return _safe_div(shareswadil - prior, prior.replace(0, np.nan))


def dla_142_diluted_basic_gap_3y_change(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """3-year change in diluted-vs-basic share gap (sustained overhang buildup)."""
    gap = shareswadil - shareswa
    return gap - gap.shift(_TD_3Y)


def dla_143_ncfcommon_above_equity_flag(ncfcommon: pd.Series, equity: pd.Series) -> pd.Series:
    """
    1 if TTM equity raised exceeds current book equity
    (company raised more cash than its current equity — extreme dilution).
    """
    ttm_iss = _rolling_sum(ncfcommon.clip(lower=0), _TD_YEAR)
    return (ttm_iss > equity.abs()).astype(float)


def dla_144_sharesbas_rolling_median_vs_current(sharesbas: pd.Series) -> pd.Series:
    """Current basic shares minus their 4-quarter rolling median."""
    return sharesbas - _rolling_median(sharesbas, _TD_YEAR)


def dla_145_sharesbas_rolling_std_4q(sharesbas: pd.Series) -> pd.Series:
    """Rolling 4-quarter standard deviation of basic shares (issuance volatility)."""
    return _rolling_std(sharesbas, _TD_YEAR)


def dla_146_sharesbas_rolling_std_8q(sharesbas: pd.Series) -> pd.Series:
    """Rolling 8-quarter standard deviation of basic shares."""
    return _rolling_std(sharesbas, _TD_2Y)


def dla_147_dilution_and_negative_equity_dual_flag(sharesbas: pd.Series, equity: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    """
    1 if: shares grew QoQ AND equity is negative AND equity was raised (ncfcommon > 0).
    Triple-distress dilution signal.
    """
    shr_grew   = (sharesbas > sharesbas.shift(_TD_QTR)).astype(float)
    eq_neg     = (equity < 0).astype(float)
    ncf_pos    = (ncfcommon > 0).astype(float)
    return shr_grew * eq_neg * ncf_pos


def dla_148_sharesbas_qoq_pct_zscore_expanding(sharesbas: pd.Series) -> pd.Series:
    """Expanding z-score of QoQ share growth rate (extremity vs all history)."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    m   = pct.expanding(min_periods=2).mean()
    sd  = pct.expanding(min_periods=2).std()
    return _safe_div(pct - m, sd)


def dla_149_ncfcommon_expanding_zscore(ncfcommon: pd.Series) -> pd.Series:
    """Expanding z-score of ncfcommon (all-history issuance extremity)."""
    m  = ncfcommon.expanding(min_periods=2).mean()
    sd = ncfcommon.expanding(min_periods=2).std()
    return _safe_div(ncfcommon - m, sd)


def dla_150_dilution_severity_composite(sharesbas: pd.Series, shareswa: pd.Series, shareswadil: pd.Series,
                                        ncfcommon: pd.Series, sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Comprehensive dilution severity composite (equal-weight z-scores):
    (1) QoQ sharesbas growth z-score
    (2) Diluted-vs-basic gap pct z-score
    (3) ncfcommon z-score
    (4) SBC-to-equity z-score
    (5) Distress-dilution flag z-score
    All within 4-quarter trailing window.
    """
    bas_pct   = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    gap_pct   = _safe_div(shareswadil - shareswa, shareswa.replace(0, np.nan))
    sbc_eq    = _safe_div(sbcomp, equity.abs().replace(0, np.nan))
    dd_flag   = ((sharesbas > sharesbas.shift(_TD_QTR)) & (equity <= 0)).astype(float)

    z1 = _zscore_rolling(bas_pct, _TD_YEAR)
    z2 = _zscore_rolling(gap_pct, _TD_YEAR)
    z3 = _zscore_rolling(ncfcommon, _TD_YEAR)
    z4 = _zscore_rolling(sbc_eq, _TD_YEAR)
    z5 = _zscore_rolling(dd_flag, _TD_YEAR)
    return (z1 + z2 + z3 + z4 + z5) / 5.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

DILUTION_ACCELERATION_REGISTRY_076_150 = {
    "dla_076_sharesbas_qoq_acceleration":               {"inputs": ["sharesbas"],                                               "func": dla_076_sharesbas_qoq_acceleration},
    "dla_077_sharesbas_zscore_12q":                      {"inputs": ["sharesbas"],                                               "func": dla_077_sharesbas_zscore_12q},
    "dla_078_shareswa_qoq_acceleration":                {"inputs": ["shareswa"],                                                "func": dla_078_shareswa_qoq_acceleration},
    "dla_079_shareswadil_pct_rank_3y":                   {"inputs": ["shareswadil"],                                             "func": dla_079_shareswadil_pct_rank_3y},
    "dla_080_sharesbas_rolling_min_4q":                  {"inputs": ["sharesbas"],                                               "func": dla_080_sharesbas_rolling_min_4q},
    "dla_081_sharesbas_yoy_pct_acceleration":           {"inputs": ["sharesbas"],                                               "func": dla_081_sharesbas_yoy_pct_acceleration},
    "dla_082_ncfcommon_qoq_change":                     {"inputs": ["ncfcommon"],                                               "func": dla_082_ncfcommon_qoq_change},
    "dla_083_ncfcommon_qoq_pct":                        {"inputs": ["ncfcommon"],                                               "func": dla_083_ncfcommon_qoq_pct},
    "dla_084_ncfcommon_acceleration":                   {"inputs": ["ncfcommon"],                                               "func": dla_084_ncfcommon_acceleration},
    "dla_085_sbcomp_qoq_change":                        {"inputs": ["sbcomp"],                                                  "func": dla_085_sbcomp_qoq_change},
    "dla_086_sbcomp_qoq_pct":                           {"inputs": ["sbcomp"],                                                  "func": dla_086_sbcomp_qoq_pct},
    "dla_087_sbcomp_acceleration":                      {"inputs": ["sbcomp"],                                                  "func": dla_087_sbcomp_acceleration},
    "dla_088_diluted_basic_gap_zscore_12q":             {"inputs": ["shareswadil", "shareswa"],                                 "func": dla_088_diluted_basic_gap_zscore_12q},
    "dla_089_sharesbas_qoq_slope_4q":                   {"inputs": ["sharesbas"],                                               "func": dla_089_sharesbas_qoq_slope_4q},
    "dla_090_sharesbas_yoy_slope_4q":                   {"inputs": ["sharesbas"],                                               "func": dla_090_sharesbas_yoy_slope_4q},
    "dla_091_issuance_quarters_2y":                     {"inputs": ["ncfcommon"],                                               "func": dla_091_issuance_quarters_2y},
    "dla_092_issuance_quarters_3y":                     {"inputs": ["ncfcommon"],                                               "func": dla_092_issuance_quarters_3y},
    "dla_093_issuance_fraction_2y":                     {"inputs": ["ncfcommon"],                                               "func": dla_093_issuance_fraction_2y},
    "dla_094_issuance_fraction_3y":                     {"inputs": ["ncfcommon"],                                               "func": dla_094_issuance_fraction_3y},
    "dla_095_consecutive_issuance_streak":              {"inputs": ["ncfcommon"],                                               "func": dla_095_consecutive_issuance_streak},
    "dla_096_max_single_quarter_issuance_1y":           {"inputs": ["ncfcommon"],                                               "func": dla_096_max_single_quarter_issuance_1y},
    "dla_097_max_single_quarter_issuance_3y":           {"inputs": ["ncfcommon"],                                               "func": dla_097_max_single_quarter_issuance_3y},
    "dla_098_ncfcommon_current_vs_4q_avg":              {"inputs": ["ncfcommon"],                                               "func": dla_098_ncfcommon_current_vs_4q_avg},
    "dla_099_ncfcommon_zscore_4q":                      {"inputs": ["ncfcommon"],                                               "func": dla_099_ncfcommon_zscore_4q},
    "dla_100_ncfcommon_zscore_8q":                      {"inputs": ["ncfcommon"],                                               "func": dla_100_ncfcommon_zscore_8q},
    "dla_101_ncfcommon_pct_rank_4q":                    {"inputs": ["ncfcommon"],                                               "func": dla_101_ncfcommon_pct_rank_4q},
    "dla_102_ncfcommon_expanding_pct_rank":             {"inputs": ["ncfcommon"],                                               "func": dla_102_ncfcommon_expanding_pct_rank},
    "dla_103_sharesbas_vs_4q_avg":                      {"inputs": ["sharesbas"],                                               "func": dla_103_sharesbas_vs_4q_avg},
    "dla_104_sharesbas_vs_8q_avg":                      {"inputs": ["sharesbas"],                                               "func": dla_104_sharesbas_vs_8q_avg},
    "dla_105_sharesbas_pct_vs_4q_avg":                  {"inputs": ["sharesbas"],                                               "func": dla_105_sharesbas_pct_vs_4q_avg},
    "dla_106_sbcomp_to_revenue_ratio":                  {"inputs": ["sbcomp", "revenue"],                                       "func": dla_106_sbcomp_to_revenue_ratio},
    "dla_107_sbcomp_to_assets_ratio":                   {"inputs": ["sbcomp", "assets"],                                        "func": dla_107_sbcomp_to_assets_ratio},
    "dla_108_sbcomp_to_ncfo_ratio":                     {"inputs": ["sbcomp", "ncfo"],                                          "func": dla_108_sbcomp_to_ncfo_ratio},
    "dla_109_sbcomp_trailing_4q_to_equity":             {"inputs": ["sbcomp", "equity"],                                        "func": dla_109_sbcomp_trailing_4q_to_equity},
    "dla_110_sbcomp_trailing_4q_to_revenue":            {"inputs": ["sbcomp", "revenue"],                                       "func": dla_110_sbcomp_trailing_4q_to_revenue},
    "dla_111_sbcomp_pct_rank_4q":                       {"inputs": ["sbcomp"],                                                  "func": dla_111_sbcomp_pct_rank_4q},
    "dla_112_sbcomp_at_3y_high_flag":                   {"inputs": ["sbcomp"],                                                  "func": dla_112_sbcomp_at_3y_high_flag},
    "dla_113_sbcomp_drawdown_from_3y_peak":             {"inputs": ["sbcomp"],                                                  "func": dla_113_sbcomp_drawdown_from_3y_peak},
    "dla_114_sbcomp_expanding_pct_rank":                {"inputs": ["sbcomp"],                                                  "func": dla_114_sbcomp_expanding_pct_rank},
    "dla_115_sbcomp_zscore_8q":                         {"inputs": ["sbcomp"],                                                  "func": dla_115_sbcomp_zscore_8q},
    "dla_116_equity_per_share_qoq_change":              {"inputs": ["equity", "sharesbas"],                                     "func": dla_116_equity_per_share_qoq_change},
    "dla_117_equity_per_share_yoy_change":              {"inputs": ["equity", "sharesbas"],                                     "func": dla_117_equity_per_share_yoy_change},
    "dla_118_equity_per_share_yoy_pct":                 {"inputs": ["equity", "sharesbas"],                                     "func": dla_118_equity_per_share_yoy_pct},
    "dla_119_equity_declining_while_shares_rising":     {"inputs": ["equity", "sharesbas"],                                     "func": dla_119_equity_declining_while_shares_rising},
    "dla_120_equity_per_diluted_share_qoq_change":      {"inputs": ["equity", "shareswadil"],                                   "func": dla_120_equity_per_diluted_share_qoq_change},
    "dla_121_total_dilution_3y_pct":                    {"inputs": ["sharesbas", "sbcomp", "equity"],                           "func": dla_121_total_dilution_3y_pct},
    "dla_122_sharesbas_drawdown_from_3y_low":           {"inputs": ["sharesbas"],                                               "func": dla_122_sharesbas_drawdown_from_3y_low},
    "dla_123_sharesbas_drawdown_from_expanding_min":    {"inputs": ["sharesbas"],                                               "func": dla_123_sharesbas_drawdown_from_expanding_min},
    "dla_124_ncfcommon_to_sharesbas_growth":            {"inputs": ["ncfcommon", "sharesbas"],                                  "func": dla_124_ncfcommon_to_sharesbas_growth},
    "dla_125_sharesbas_qoq_pct_vs_4q_avg":              {"inputs": ["sharesbas"],                                               "func": dla_125_sharesbas_qoq_pct_vs_4q_avg},
    "dla_126_sharesbas_pct_rank_8q":                     {"inputs": ["sharesbas"],                                               "func": dla_126_sharesbas_pct_rank_8q},
    "dla_127_diluted_basic_gap_at_5y_high_flag":        {"inputs": ["shareswa", "shareswadil"],                                 "func": dla_127_diluted_basic_gap_at_5y_high_flag},
    "dla_128_sharesbas_level_z_expanding":              {"inputs": ["sharesbas"],                                               "func": dla_128_sharesbas_level_z_expanding},
    "dla_129_ncfcommon_positive_consecutive_2q":        {"inputs": ["ncfcommon"],                                               "func": dla_129_ncfcommon_positive_consecutive_2q},
    "dla_130_ncfcommon_positive_consecutive_4q":        {"inputs": ["ncfcommon"],                                               "func": dla_130_ncfcommon_positive_consecutive_4q},
    "dla_131_shares_issued_3y_sum":                     {"inputs": ["sharesbas"],                                               "func": dla_131_shares_issued_3y_sum},
    "dla_132_shares_retired_3y_sum":                    {"inputs": ["sharesbas"],                                               "func": dla_132_shares_retired_3y_sum},
    "dla_133_net_shares_issued_vs_retired_3y":          {"inputs": ["sharesbas"],                                               "func": dla_133_net_shares_issued_vs_retired_3y},
    "dla_134_dilution_velocity_1y":                     {"inputs": ["sharesbas"],                                               "func": dla_134_dilution_velocity_1y},
    "dla_135_dilution_velocity_3y":                     {"inputs": ["sharesbas"],                                               "func": dla_135_dilution_velocity_3y},
    "dla_136_distress_dilution_consecutive_streak":     {"inputs": ["sharesbas", "equity"],                                     "func": dla_136_distress_dilution_consecutive_streak},
    "dla_137_sharesbas_3y_pct_change":                  {"inputs": ["sharesbas"],                                               "func": dla_137_sharesbas_3y_pct_change},
    "dla_138_shareswadil_zscore_8q":                     {"inputs": ["shareswadil"],                                             "func": dla_138_shareswadil_zscore_8q},
    "dla_139_sbcomp_to_sharesbas_qoq_growth":           {"inputs": ["sbcomp", "sharesbas"],                                     "func": dla_139_sbcomp_to_sharesbas_qoq_growth},
    "dla_140_equity_raised_fraction_of_3y_equity_change": {"inputs": ["ncfcommon", "equity"],                                  "func": dla_140_equity_raised_fraction_of_3y_equity_change},
    "dla_141_shareswadil_3y_pct_change":                {"inputs": ["shareswadil"],                                             "func": dla_141_shareswadil_3y_pct_change},
    "dla_142_diluted_basic_gap_3y_change":              {"inputs": ["shareswadil", "shareswa"],                                 "func": dla_142_diluted_basic_gap_3y_change},
    "dla_143_ncfcommon_above_equity_flag":              {"inputs": ["ncfcommon", "equity"],                                     "func": dla_143_ncfcommon_above_equity_flag},
    "dla_144_sharesbas_rolling_median_vs_current":      {"inputs": ["sharesbas"],                                               "func": dla_144_sharesbas_rolling_median_vs_current},
    "dla_145_sharesbas_rolling_std_4q":                 {"inputs": ["sharesbas"],                                               "func": dla_145_sharesbas_rolling_std_4q},
    "dla_146_sharesbas_rolling_std_8q":                 {"inputs": ["sharesbas"],                                               "func": dla_146_sharesbas_rolling_std_8q},
    "dla_147_dilution_and_negative_equity_dual_flag":   {"inputs": ["sharesbas", "equity", "ncfcommon"],                        "func": dla_147_dilution_and_negative_equity_dual_flag},
    "dla_148_sharesbas_qoq_pct_zscore_expanding":       {"inputs": ["sharesbas"],                                               "func": dla_148_sharesbas_qoq_pct_zscore_expanding},
    "dla_149_ncfcommon_expanding_zscore":               {"inputs": ["ncfcommon"],                                               "func": dla_149_ncfcommon_expanding_zscore},
    "dla_150_dilution_severity_composite":              {"inputs": ["sharesbas", "shareswa", "shareswadil", "ncfcommon", "sbcomp", "equity"], "func": dla_150_dilution_severity_composite},
}
