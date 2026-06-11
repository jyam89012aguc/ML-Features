"""
92_ownership_concentration — Base Features 076-150, extended to 200
===================================================
Domain: SHAPE and CONCENTRATION of institutional holdings distribution.
Covers HHI levels, top-N holder share ratios, effective-number-of-holders,
gini-like proxies from top-N tranches, concentration z-scores / ranks,
and QoQ / YoY shifts of all of the above.

Quarterly -> Daily Alignment Contract
--------------------------------------
All input Series arrive as *daily* pandas Series whose values have been
forward-filled from quarterly Sharadar SF3 13-F snapshots.  Because the
underlying data is quarterly, values change only ~4 times per year;
rolling windows shorter than 63 trading days will often see flat stretches.

Input fields used across this file:
    hhi          — Herfindahl-Hirschman index of institutional holdings (0..1)
    top1_shares  — shares held by the single largest institutional holder
    top5_shares  — shares held by top-5 institutional holders combined
    top10_shares — shares held by top-10 institutional holders combined
    inst_shares  — aggregate shares held by ALL institutions
    inst_holders — count of institutional holders
    inst_value   — aggregate USD value held by all institutions
    avg_position — mean shares per institutional holder

Trading-day constants:
    1 quarter  = 63 td   (_TD_QTR)
    2 quarters = 126 td  (_TD_2Q)
    1 year     = 252 td  (_TD_YEAR)
    2 years    = 504 td  (_TD_2Y)
    3 years    = 756 td  (_TD_3Y)
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_TD_YEAR = 252
_TD_2Y   = 504
_TD_3Y   = 756
_TD_QTR  = 63
_TD_2Q   = 126
_EPS     = 1e-9

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _align_quarterly_to_daily(s: pd.Series) -> pd.Series:
    """Return s as-is (already forward-filled to daily by the pipeline)."""
    return s


def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    """Element-wise a / b; returns NaN where b is zero or NaN."""
    b_safe = b.replace(0, np.nan)
    return a / b_safe


def _safe_div_abs(a: pd.Series, b: pd.Series) -> pd.Series:
    """Element-wise a / |b|; returns NaN where |b| is zero or NaN."""
    b_safe = b.abs().replace(0, np.nan)
    return a / b_safe


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=2).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=1).mean()

# ===========================================================================
# Features 076-150
# ===========================================================================

# --- Concentration Persistence / Regime (076-085) ---------------------------

def ocn_076_hhi_above_median_1y(hhi: pd.Series) -> pd.Series:
    """Binary: 1 if current HHI > 1y rolling median, else 0."""
    h = _align_quarterly_to_daily(hhi)
    med = _rolling_median(h, _TD_YEAR)
    return (h > med).astype(float)


def ocn_077_hhi_consecutive_rises(hhi: pd.Series) -> pd.Series:
    """Count of consecutive QoQ quarters where HHI increased."""
    h = _align_quarterly_to_daily(hhi)
    diff = h - h.shift(_TD_QTR)

    def _consec(arr):
        if np.isnan(arr[-1]):
            return np.nan
        count = 0
        for v in reversed(arr):
            if v > 0:
                count += 1
            else:
                break
        return float(count)

    return diff.rolling(_TD_YEAR, min_periods=1).apply(_consec, raw=True)


def ocn_078_hhi_pct_time_above_2y_mean(hhi: pd.Series) -> pd.Series:
    """Fraction of the last 2 years HHI was above its 2y mean."""
    h = _align_quarterly_to_daily(hhi)
    mean2y = _rolling_mean(h, _TD_2Y)
    above = (h > mean2y).astype(float)
    return _rolling_mean(above, _TD_2Y)


def ocn_079_hhi_range_1y(hhi: pd.Series) -> pd.Series:
    """1-year HHI range: max - min."""
    h = _align_quarterly_to_daily(hhi)
    return _rolling_max(h, _TD_YEAR) - _rolling_min(h, _TD_YEAR)


def ocn_080_hhi_range_2y(hhi: pd.Series) -> pd.Series:
    """2-year HHI range: max - min."""
    h = _align_quarterly_to_daily(hhi)
    return _rolling_max(h, _TD_2Y) - _rolling_min(h, _TD_2Y)


def ocn_081_hhi_vs_3y_mean(hhi: pd.Series) -> pd.Series:
    """HHI minus its 3-year rolling mean."""
    h = _align_quarterly_to_daily(hhi)
    return h - _rolling_mean(h, _TD_3Y)


def ocn_082_hhi_zscore_3y(hhi: pd.Series) -> pd.Series:
    """Z-score of HHI over a 3-year rolling window."""
    return _zscore_rolling(_align_quarterly_to_daily(hhi), _TD_3Y)


def ocn_083_hhi_rank_3y(hhi: pd.Series) -> pd.Series:
    """Percentile rank of HHI over a 3-year rolling window."""
    return _rolling_rank_pct(_align_quarterly_to_daily(hhi), _TD_3Y)


def ocn_084_hhi_expanding_rank(hhi: pd.Series) -> pd.Series:
    """Expanding percentile rank of HHI from start of series."""
    h = _align_quarterly_to_daily(hhi)
    return h.expanding(min_periods=1).rank(pct=True)


def ocn_085_hhi_expanding_zscore(hhi: pd.Series) -> pd.Series:
    """Expanding z-score of HHI from start of series."""
    h = _align_quarterly_to_daily(hhi)
    mu  = h.expanding(min_periods=1).mean()
    sig = h.expanding(min_periods=2).std()
    return _safe_div(h - mu, sig)


# --- Top-1 Advanced Features (086-095) --------------------------------------

def ocn_086_top1_share_raw(top1_shares: pd.Series) -> pd.Series:
    """Raw top-1 institutional holder share count."""
    return _align_quarterly_to_daily(top1_shares).copy()


def ocn_087_top1_share_pct_of_avg(top1_shares: pd.Series,
                                    avg_position: pd.Series) -> pd.Series:
    """Top-1 shares as multiple of average holder position."""
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(avg_position))


def ocn_088_top1_share_pct_of_avg_zscore_1y(top1_shares: pd.Series,
                                              avg_position: pd.Series) -> pd.Series:
    """Z-score (1y) of top-1-to-avg-position multiple."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(avg_position))
    return _zscore_rolling(r, _TD_YEAR)


def ocn_089_top1_conc_ratio_rank_2y(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of top-1 concentration ratio over 2 years."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_rank_pct(r, _TD_2Y)


def ocn_090_top1_conc_accel(top1_shares: pd.Series,
                              inst_shares: pd.Series) -> pd.Series:
    """QoQ acceleration of top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    d1 = r - r.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_091_top1_conc_ewm_4q(top1_shares: pd.Series,
                               inst_shares: pd.Series) -> pd.Series:
    """4-quarter EWM (span=252) of top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _ewm_mean(r, _TD_YEAR)


def ocn_092_top1_conc_slope_4q(top1_shares: pd.Series,
                                 inst_shares: pd.Series) -> pd.Series:
    """Linear slope of top-1 concentration over 4 quarters."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))

    def _slope(arr):
        if len(arr) < 4:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan

    return r.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def ocn_093_top1_conc_ratio_3y_chg(top1_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """3-year change in top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_3Y)


def ocn_094_top1_conc_vs_3y_mean(top1_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Top-1 concentration ratio minus its 3-year rolling mean."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_mean(r, _TD_3Y)


def ocn_095_top1_conc_ratio_zscore_3y(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Z-score of top-1 concentration ratio over 3 years."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(r, _TD_3Y)


# --- Top-5 Advanced Features (096-105) --------------------------------------

def ocn_096_top5_conc_ratio_rank_2y(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of top-5 concentration ratio over 2 years."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_rank_pct(r, _TD_2Y)


def ocn_097_top5_conc_accel(top5_shares: pd.Series,
                              inst_shares: pd.Series) -> pd.Series:
    """QoQ acceleration of top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    d1 = r - r.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_098_top5_conc_slope_4q(top5_shares: pd.Series,
                                 inst_shares: pd.Series) -> pd.Series:
    """Linear slope of top-5 concentration ratio over 4 quarters."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))

    def _slope(arr):
        if len(arr) < 4:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan

    return r.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def ocn_099_top5_conc_3y_chg(top5_shares: pd.Series,
                               inst_shares: pd.Series) -> pd.Series:
    """3-year change in top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_3Y)


def ocn_100_top5_conc_vs_3y_mean(top5_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Top-5 concentration ratio minus its 3-year rolling mean."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_mean(r, _TD_3Y)


def ocn_101_top5_conc_ratio_zscore_3y(top5_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Z-score of top-5 concentration ratio over 3 years."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(r, _TD_3Y)


def ocn_102_top5_conc_rank_3y(top5_shares: pd.Series,
                                inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of top-5 concentration ratio over 3 years."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_rank_pct(r, _TD_3Y)


def ocn_103_top5_ewm_vs_raw(top5_shares: pd.Series,
                              inst_shares: pd.Series) -> pd.Series:
    """Top-5 ratio minus its EWM (span=252)."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _ewm_mean(r, _TD_YEAR)


def ocn_104_top5_conc_ratio_2q_chg(top5_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """2-quarter change in top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_2Q)


def ocn_105_top5_to_top1_concentration_index(top1_shares: pd.Series,
                                               top5_shares: pd.Series) -> pd.Series:
    """Ratio of top-1 to top-5 shares; near 1 = single-holder dominance."""
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(top5_shares))


# --- Top-10 Advanced Features (106-115) -------------------------------------

def ocn_106_top10_conc_ratio_rank_2y(top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of top-10 concentration ratio over 2 years."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_rank_pct(r, _TD_2Y)


def ocn_107_top10_conc_accel(top10_shares: pd.Series,
                               inst_shares: pd.Series) -> pd.Series:
    """QoQ acceleration of top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    d1 = r - r.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_108_top10_conc_slope_4q(top10_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """Linear slope of top-10 concentration ratio over 4 quarters."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))

    def _slope(arr):
        if len(arr) < 4:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan

    return r.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def ocn_109_top10_conc_3y_chg(top10_shares: pd.Series,
                                inst_shares: pd.Series) -> pd.Series:
    """3-year change in top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_3Y)


def ocn_110_top10_conc_vs_3y_mean(top10_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Top-10 concentration ratio minus its 3-year rolling mean."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_mean(r, _TD_3Y)


def ocn_111_top10_conc_zscore_3y(top10_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Z-score of top-10 concentration ratio over 3 years."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(r, _TD_3Y)


def ocn_112_top10_conc_rank_3y(top10_shares: pd.Series,
                                 inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of top-10 concentration ratio over 3 years."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_rank_pct(r, _TD_3Y)


def ocn_113_top10_ewm_vs_raw(top10_shares: pd.Series,
                               inst_shares: pd.Series) -> pd.Series:
    """Top-10 ratio minus its EWM (span=252)."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _ewm_mean(r, _TD_YEAR)


def ocn_114_top10_conc_2q_chg(top10_shares: pd.Series,
                                inst_shares: pd.Series) -> pd.Series:
    """2-quarter change in top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_2Q)


def ocn_115_top10_to_top5_ratio(top5_shares: pd.Series,
                                  top10_shares: pd.Series) -> pd.Series:
    """Top-5 as fraction of top-10; near 1 = top-5 dominate top-10."""
    return _safe_div(_align_quarterly_to_daily(top5_shares),
                     _align_quarterly_to_daily(top10_shares))


# --- Concentration vs Holder Count (116-125) --------------------------------

def ocn_116_hhi_per_holder(hhi: pd.Series,
                             inst_holders: pd.Series) -> pd.Series:
    """HHI divided by holder count: measures per-holder contribution to concentration."""
    h = _align_quarterly_to_daily(hhi)
    n = _align_quarterly_to_daily(inst_holders)
    return _safe_div(h, n)


def ocn_117_conc_adjusted_holder_count(hhi: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    """Effective-N as fraction of actual holders (concentration-adjusted breadth)."""
    h = _align_quarterly_to_daily(hhi)
    n = _align_quarterly_to_daily(inst_holders)
    eff = _safe_div(pd.Series(np.ones(len(h)), index=h.index), h)
    return _safe_div(eff, n)


def ocn_118_conc_adj_breadth_zscore_1y(hhi: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    """Z-score (1y) of concentration-adjusted breadth."""
    h = _align_quarterly_to_daily(hhi)
    n = _align_quarterly_to_daily(inst_holders)
    eff = _safe_div(pd.Series(np.ones(len(h)), index=h.index), h)
    breadth = _safe_div(eff, n)
    return _zscore_rolling(breadth, _TD_YEAR)


def ocn_119_top1_conc_per_holder(top1_shares: pd.Series,
                                   inst_shares: pd.Series,
                                   inst_holders: pd.Series) -> pd.Series:
    """Top-1 concentration ratio divided by holder count."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    n = _align_quarterly_to_daily(inst_holders)
    return _safe_div(r, n)


def ocn_120_top5_conc_per_holder(top5_shares: pd.Series,
                                   inst_shares: pd.Series,
                                   inst_holders: pd.Series) -> pd.Series:
    """Top-5 concentration ratio divided by holder count."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    n = _align_quarterly_to_daily(inst_holders)
    return _safe_div(r, n)


def ocn_121_hhi_x_top1_ratio(hhi: pd.Series,
                               top1_shares: pd.Series,
                               inst_shares: pd.Series) -> pd.Series:
    """Product of HHI and top-1 ratio: joint concentration signal."""
    h = _align_quarterly_to_daily(hhi)
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return h * r


def ocn_122_hhi_x_top1_ratio_zscore_1y(hhi: pd.Series,
                                         top1_shares: pd.Series,
                                         inst_shares: pd.Series) -> pd.Series:
    """Z-score (1y) of HHI * top-1 ratio product."""
    h = _align_quarterly_to_daily(hhi)
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    prod = h * r
    return _zscore_rolling(prod, _TD_YEAR)


def ocn_123_conc_breadth_divergence(hhi: pd.Series,
                                     inst_holders: pd.Series) -> pd.Series:
    """HHI minus its 1y mean, minus (holder count - 1y mean) normalized."""
    h  = _align_quarterly_to_daily(hhi)
    n  = _align_quarterly_to_daily(inst_holders)
    dh = h - _rolling_mean(h, _TD_YEAR)
    dn = _safe_div_abs(n - _rolling_mean(n, _TD_YEAR),
                       _rolling_std(n, _TD_YEAR))
    return dh - dn


def ocn_124_eff_n_vs_holders_diff(hhi: pd.Series,
                                   inst_holders: pd.Series) -> pd.Series:
    """Effective-N minus actual holder count (absolute gap)."""
    h = _align_quarterly_to_daily(hhi)
    n = _align_quarterly_to_daily(inst_holders)
    eff = _safe_div(pd.Series(np.ones(len(h)), index=h.index), h)
    return eff - n


def ocn_125_eff_n_holder_gap_yoy(hhi: pd.Series,
                                   inst_holders: pd.Series) -> pd.Series:
    """YoY change in the effective-N to holder-count gap."""
    h = _align_quarterly_to_daily(hhi)
    n = _align_quarterly_to_daily(inst_holders)
    eff = _safe_div(pd.Series(np.ones(len(h)), index=h.index), h)
    gap = eff - n
    return gap - gap.shift(_TD_YEAR)


# --- Average Position & Value Features (126-135) ----------------------------

def ocn_126_avg_position_zscore_1y(avg_position: pd.Series) -> pd.Series:
    """Z-score of average institutional position over 1 year."""
    return _zscore_rolling(_align_quarterly_to_daily(avg_position), _TD_YEAR)


def ocn_127_avg_position_rank_1y(avg_position: pd.Series) -> pd.Series:
    """Percentile rank of average institutional position over 1 year."""
    return _rolling_rank_pct(_align_quarterly_to_daily(avg_position), _TD_YEAR)


def ocn_128_avg_position_yoy_pct_chg(avg_position: pd.Series) -> pd.Series:
    """YoY percentage change in average institutional position."""
    a = _align_quarterly_to_daily(avg_position)
    prev = a.shift(_TD_YEAR)
    return _safe_div_abs(a - prev, prev)


def ocn_129_avg_position_qoq_chg(avg_position: pd.Series) -> pd.Series:
    """QoQ change in average institutional position."""
    a = _align_quarterly_to_daily(avg_position)
    return a - a.shift(_TD_QTR)


def ocn_130_avg_pos_vs_1y_mean(avg_position: pd.Series) -> pd.Series:
    """Average position minus its 1-year rolling mean."""
    a = _align_quarterly_to_daily(avg_position)
    return a - _rolling_mean(a, _TD_YEAR)


def ocn_131_inst_value_per_holder_zscore_1y(inst_value: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """Z-score (1y) of USD value per institutional holder."""
    v = _align_quarterly_to_daily(inst_value)
    n = _align_quarterly_to_daily(inst_holders)
    vph = _safe_div(v, n)
    return _zscore_rolling(vph, _TD_YEAR)


def ocn_132_inst_value_per_holder_rank_1y(inst_value: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """Percentile rank (1y) of USD value per institutional holder."""
    v = _align_quarterly_to_daily(inst_value)
    n = _align_quarterly_to_daily(inst_holders)
    vph = _safe_div(v, n)
    return _rolling_rank_pct(vph, _TD_YEAR)


def ocn_133_inst_value_per_holder_yoy_chg(inst_value: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """YoY change in USD value per institutional holder."""
    v = _align_quarterly_to_daily(inst_value)
    n = _align_quarterly_to_daily(inst_holders)
    vph = _safe_div(v, n)
    return vph - vph.shift(_TD_YEAR)


def ocn_134_top1_value_estimate_zscore_1y(top1_shares: pd.Series,
                                           inst_shares: pd.Series,
                                           inst_value: pd.Series) -> pd.Series:
    """Z-score (1y) of estimated top-1 holder USD value."""
    frac = _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(inst_shares))
    val  = frac * _align_quarterly_to_daily(inst_value)
    return _zscore_rolling(val, _TD_YEAR)


def ocn_135_avg_pos_slope_4q(avg_position: pd.Series) -> pd.Series:
    """Linear slope of average institutional position over 4 quarters."""
    a = _align_quarterly_to_daily(avg_position)

    def _slope(arr):
        if len(arr) < 4:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan

    return a.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


# --- Multi-Variable Concentration Composites (136-145) ----------------------

def ocn_136_conc_rising_regime(hhi: pd.Series,
                                top5_shares: pd.Series,
                                inst_shares: pd.Series) -> pd.Series:
    """1 if both HHI and top-5 ratio are above their 1y means simultaneously."""
    h  = _align_quarterly_to_daily(hhi)
    r5 = _safe_div(_align_quarterly_to_daily(top5_shares),
                   _align_quarterly_to_daily(inst_shares))
    hhi_above  = (h  > _rolling_mean(h,  _TD_YEAR)).astype(float)
    top5_above = (r5 > _rolling_mean(r5, _TD_YEAR)).astype(float)
    return hhi_above * top5_above


def ocn_137_conc_composite_zscore_1y(hhi: pd.Series,
                                      top1_shares: pd.Series,
                                      top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """Z-score of equal-weighted composite of HHI + top-1 + top-5 + top-10 ratios."""
    ins = _align_quarterly_to_daily(inst_shares)
    h   = _align_quarterly_to_daily(hhi)
    r1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    comp = (h + r1 + r5 + r10) / 4.0
    return _zscore_rolling(comp, _TD_YEAR)


def ocn_138_conc_composite_rank_1y(hhi: pd.Series,
                                    top1_shares: pd.Series,
                                    top5_shares: pd.Series,
                                    top10_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """Percentile rank (1y) of equal-weighted concentration composite."""
    ins = _align_quarterly_to_daily(inst_shares)
    h   = _align_quarterly_to_daily(hhi)
    r1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    comp = (h + r1 + r5 + r10) / 4.0
    return _rolling_rank_pct(comp, _TD_YEAR)


def ocn_139_conc_composite_yoy_chg(hhi: pd.Series,
                                    top1_shares: pd.Series,
                                    top5_shares: pd.Series,
                                    top10_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """YoY change in equal-weighted concentration composite."""
    ins = _align_quarterly_to_daily(inst_shares)
    h   = _align_quarterly_to_daily(hhi)
    r1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    comp = (h + r1 + r5 + r10) / 4.0
    return comp - comp.shift(_TD_YEAR)


def ocn_140_conc_composite_2y_chg(hhi: pd.Series,
                                   top1_shares: pd.Series,
                                   top5_shares: pd.Series,
                                   top10_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """2-year change in equal-weighted concentration composite."""
    ins = _align_quarterly_to_daily(inst_shares)
    h   = _align_quarterly_to_daily(hhi)
    r1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    comp = (h + r1 + r5 + r10) / 4.0
    return comp - comp.shift(_TD_2Y)


def ocn_141_conc_composite_slope_4q(hhi: pd.Series,
                                     top1_shares: pd.Series,
                                     top5_shares: pd.Series,
                                     top10_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Linear slope of the composite concentration over 4 quarters."""
    ins = _align_quarterly_to_daily(inst_shares)
    h   = _align_quarterly_to_daily(hhi)
    r1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    comp = (h + r1 + r5 + r10) / 4.0

    def _slope(arr):
        if len(arr) < 4:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan

    return comp.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def ocn_142_hhi_top1_divergence(hhi: pd.Series,
                                  top1_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """Z-score(HHI) minus z-score(top1 ratio) over 1y: divergence signal."""
    h  = _align_quarterly_to_daily(hhi)
    r1 = _safe_div(_align_quarterly_to_daily(top1_shares),
                   _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(h, _TD_YEAR) - _zscore_rolling(r1, _TD_YEAR)


def ocn_143_top5_top10_divergence(top5_shares: pd.Series,
                                   top10_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Z-score(top5 ratio) minus z-score(top10 ratio) over 1y."""
    ins = _align_quarterly_to_daily(inst_shares)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    return _zscore_rolling(r5, _TD_YEAR) - _zscore_rolling(r10, _TD_YEAR)


def ocn_144_conc_momentum_score(hhi: pd.Series,
                                  top1_shares: pd.Series,
                                  top5_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """Sum of QoQ sign indicators: +1 if HHI, top-1, top-5 each rose QoQ."""
    h  = _align_quarterly_to_daily(hhi)
    r1 = _safe_div(_align_quarterly_to_daily(top1_shares),
                   _align_quarterly_to_daily(inst_shares))
    r5 = _safe_div(_align_quarterly_to_daily(top5_shares),
                   _align_quarterly_to_daily(inst_shares))
    s_h  = ((h  - h.shift(_TD_QTR))  > 0).astype(float)
    s_r1 = ((r1 - r1.shift(_TD_QTR)) > 0).astype(float)
    s_r5 = ((r5 - r5.shift(_TD_QTR)) > 0).astype(float)
    return s_h + s_r1 + s_r5


def ocn_145_conc_momentum_sum_4q(hhi: pd.Series,
                                   top1_shares: pd.Series,
                                   top5_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Rolling 4-quarter sum of the concentration momentum score."""
    h  = _align_quarterly_to_daily(hhi)
    r1 = _safe_div(_align_quarterly_to_daily(top1_shares),
                   _align_quarterly_to_daily(inst_shares))
    r5 = _safe_div(_align_quarterly_to_daily(top5_shares),
                   _align_quarterly_to_daily(inst_shares))
    s_h  = ((h  - h.shift(_TD_QTR))  > 0).astype(float)
    s_r1 = ((r1 - r1.shift(_TD_QTR)) > 0).astype(float)
    s_r5 = ((r5 - r5.shift(_TD_QTR)) > 0).astype(float)
    score = s_h + s_r1 + s_r5
    return _rolling_sum(score, _TD_YEAR)


# --- Residual / Tail Concentration Features (146-150) -----------------------

def ocn_146_tail_conc_ratio(top5_shares: pd.Series,
                              top10_shares: pd.Series,
                              inst_shares: pd.Series) -> pd.Series:
    """Shares outside top-5 but inside top-10 as fraction of inst_shares."""
    t5  = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div((t10 - t5).clip(lower=0), ins)


def ocn_147_tail_conc_ratio_zscore_1y(top5_shares: pd.Series,
                                       top10_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Z-score (1y) of the 6-10 holder tranche concentration ratio."""
    t5  = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    r = _safe_div((t10 - t5).clip(lower=0), ins)
    return _zscore_rolling(r, _TD_YEAR)


def ocn_148_tail_conc_ratio_yoy_chg(top5_shares: pd.Series,
                                     top10_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """YoY change in the 6-10 holder tranche concentration ratio."""
    t5  = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    r = _safe_div((t10 - t5).clip(lower=0), ins)
    return r - r.shift(_TD_YEAR)


def ocn_149_outside_top5_conc_ratio(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Fraction of inst_shares held outside the top-5."""
    t5  = _align_quarterly_to_daily(top5_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div((ins - t5).clip(lower=0), ins)


def ocn_150_outside_top5_conc_zscore_2y(top5_shares: pd.Series,
                                         inst_shares: pd.Series) -> pd.Series:
    """Z-score (2y) of fraction of inst_shares held outside the top-5."""
    t5  = _align_quarterly_to_daily(top5_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    r = _safe_div((ins - t5).clip(lower=0), ins)
    return _zscore_rolling(r, _TD_2Y)


# --- New Features 176-200 ---------------------------------------------------

def ocn_176_avg_position_2y_mean(avg_position: pd.Series) -> pd.Series:
    """2-year rolling mean of average institutional position."""
    return _rolling_mean(_align_quarterly_to_daily(avg_position), _TD_2Y)


def ocn_177_avg_position_2y_zscore(avg_position: pd.Series) -> pd.Series:
    """Z-score of average institutional position over 2 years."""
    return _zscore_rolling(_align_quarterly_to_daily(avg_position), _TD_2Y)


def ocn_178_avg_position_vs_2y_mean(avg_position: pd.Series) -> pd.Series:
    """Average position minus its 2-year rolling mean."""
    a = _align_quarterly_to_daily(avg_position)
    return a - _rolling_mean(a, _TD_2Y)


def ocn_179_avg_position_qoq_pct_chg(avg_position: pd.Series) -> pd.Series:
    """QoQ percentage change in average institutional position."""
    a = _align_quarterly_to_daily(avg_position)
    prev = a.shift(_TD_QTR)
    b_safe = prev.abs().replace(0, np.nan)
    return (a - prev) / b_safe


def ocn_180_avg_position_ewm_4q(avg_position: pd.Series) -> pd.Series:
    """EWM (span=252) of average institutional position."""
    return _ewm_mean(_align_quarterly_to_daily(avg_position), _TD_YEAR)


def ocn_181_inst_value_zscore_1y(inst_value: pd.Series) -> pd.Series:
    """Z-score of total institutional USD value over 1 year."""
    return _zscore_rolling(_align_quarterly_to_daily(inst_value), _TD_YEAR)


def ocn_182_inst_value_rank_1y(inst_value: pd.Series) -> pd.Series:
    """Percentile rank of total institutional USD value over 1 year."""
    return _rolling_rank_pct(_align_quarterly_to_daily(inst_value), _TD_YEAR)


def ocn_183_inst_value_yoy_chg(inst_value: pd.Series) -> pd.Series:
    """YoY change in total institutional USD value."""
    v = _align_quarterly_to_daily(inst_value)
    return v - v.shift(_TD_YEAR)


def ocn_184_inst_value_qoq_chg(inst_value: pd.Series) -> pd.Series:
    """QoQ change in total institutional USD value."""
    v = _align_quarterly_to_daily(inst_value)
    return v - v.shift(_TD_QTR)


def ocn_185_inst_value_vs_1y_mean(inst_value: pd.Series) -> pd.Series:
    """Total institutional value minus its 1-year rolling mean."""
    v = _align_quarterly_to_daily(inst_value)
    return v - _rolling_mean(v, _TD_YEAR)


def ocn_186_hhi_abs_dev_from_2y_mean(hhi: pd.Series) -> pd.Series:
    """Absolute deviation of HHI from its 2-year rolling mean."""
    h = _align_quarterly_to_daily(hhi)
    return (h - _rolling_mean(h, _TD_2Y)).abs()


def ocn_187_top1_conc_ratio_ewm_2q(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Short EWM (span=126) of top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _ewm_mean(r, _TD_2Q)


def ocn_188_top5_conc_ratio_ewm_2q(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Short EWM (span=126) of top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _ewm_mean(r, _TD_2Q)


def ocn_189_top10_conc_ratio_ewm_2q(top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """Short EWM (span=126) of top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _ewm_mean(r, _TD_2Q)


def ocn_190_conc_composite_median_1y(hhi: pd.Series,
                                      top1_shares: pd.Series,
                                      top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """1-year rolling median of the equal-weighted concentration composite."""
    ins = _align_quarterly_to_daily(inst_shares)
    h   = _align_quarterly_to_daily(hhi)
    r1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    comp = (h + r1 + r5 + r10) / 4.0
    return _rolling_median(comp, _TD_YEAR)


def ocn_191_top1_conc_expanding_rank(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Expanding percentile rank of top-1 concentration ratio from series start."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r.expanding(min_periods=1).rank(pct=True)


def ocn_192_top5_conc_expanding_rank(top5_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Expanding percentile rank of top-5 concentration ratio from series start."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r.expanding(min_periods=1).rank(pct=True)


def ocn_193_outside_top5_conc_yoy_chg(top5_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """YoY change in fraction of inst_shares held outside top-5."""
    t5  = _align_quarterly_to_daily(top5_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    r = _safe_div((ins - t5).clip(lower=0), ins)
    return r - r.shift(_TD_YEAR)


def ocn_194_tail_conc_ratio_qoq_chg(top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 6-10 holder tranche concentration ratio."""
    t5  = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    r = _safe_div((t10 - t5).clip(lower=0), ins)
    return r - r.shift(_TD_QTR)


def ocn_195_gini_proxy_yoy_chg(top1_shares: pd.Series,
                                 top5_shares: pd.Series,
                                 top10_shares: pd.Series,
                                 inst_shares: pd.Series) -> pd.Series:
    """YoY change in the Gini-like proxy value."""
    ins = _align_quarterly_to_daily(inst_shares)
    s1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    s5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    s10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    g = 0.5 * (0.1 * s1 + 0.4 * (s1 + s5) + 0.5 * (s5 + s10))
    return g - g.shift(_TD_YEAR)


def ocn_196_hhi_vs_top10_ratio_spread(hhi: pd.Series,
                                       top10_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """HHI minus top-10 concentration ratio squared (structure residual)."""
    h   = _align_quarterly_to_daily(hhi)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares),
                    _align_quarterly_to_daily(inst_shares))
    return h - r10 ** 2


def ocn_197_top10_conc_expanding_zscore(top10_shares: pd.Series,
                                          inst_shares: pd.Series) -> pd.Series:
    """Expanding z-score of top-10 concentration ratio from series start."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    mu  = r.expanding(min_periods=1).mean()
    sig = r.expanding(min_periods=2).std()
    return _safe_div(r - mu, sig)


def ocn_198_conc_composite_3y_chg(hhi: pd.Series,
                                    top1_shares: pd.Series,
                                    top5_shares: pd.Series,
                                    top10_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """3-year change in equal-weighted concentration composite."""
    ins = _align_quarterly_to_daily(inst_shares)
    h   = _align_quarterly_to_daily(hhi)
    r1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    comp = (h + r1 + r5 + r10) / 4.0
    return comp - comp.shift(_TD_3Y)


def ocn_199_hhi_std_4q(hhi: pd.Series) -> pd.Series:
    """Rolling std of HHI over the past 4 quarters (252 td)."""
    return _rolling_std(_align_quarterly_to_daily(hhi), _TD_YEAR)


def ocn_200_inst_holders_vs_1y_mean(inst_holders: pd.Series) -> pd.Series:
    """Institutional holder count minus its 1-year rolling mean."""
    n = _align_quarterly_to_daily(inst_holders)
    return n - _rolling_mean(n, _TD_YEAR)


# ===========================================================================
# Registry
# ===========================================================================
OWNERSHIP_CONCENTRATION_REGISTRY_076_150 = {
    "ocn_076_hhi_above_median_1y":               {"inputs": ["hhi"],                                                                             "func": ocn_076_hhi_above_median_1y},
    "ocn_077_hhi_consecutive_rises":             {"inputs": ["hhi"],                                                                             "func": ocn_077_hhi_consecutive_rises},
    "ocn_078_hhi_pct_time_above_2y_mean":        {"inputs": ["hhi"],                                                                             "func": ocn_078_hhi_pct_time_above_2y_mean},
    "ocn_079_hhi_range_1y":                      {"inputs": ["hhi"],                                                                             "func": ocn_079_hhi_range_1y},
    "ocn_080_hhi_range_2y":                      {"inputs": ["hhi"],                                                                             "func": ocn_080_hhi_range_2y},
    "ocn_081_hhi_vs_3y_mean":                    {"inputs": ["hhi"],                                                                             "func": ocn_081_hhi_vs_3y_mean},
    "ocn_082_hhi_zscore_3y":                     {"inputs": ["hhi"],                                                                             "func": ocn_082_hhi_zscore_3y},
    "ocn_083_hhi_rank_3y":                       {"inputs": ["hhi"],                                                                             "func": ocn_083_hhi_rank_3y},
    "ocn_084_hhi_expanding_rank":                {"inputs": ["hhi"],                                                                             "func": ocn_084_hhi_expanding_rank},
    "ocn_085_hhi_expanding_zscore":              {"inputs": ["hhi"],                                                                             "func": ocn_085_hhi_expanding_zscore},
    "ocn_086_top1_share_raw":                    {"inputs": ["top1_shares"],                                                                     "func": ocn_086_top1_share_raw},
    "ocn_087_top1_share_pct_of_avg":             {"inputs": ["top1_shares", "avg_position"],                                                     "func": ocn_087_top1_share_pct_of_avg},
    "ocn_088_top1_share_pct_of_avg_zscore_1y":   {"inputs": ["top1_shares", "avg_position"],                                                     "func": ocn_088_top1_share_pct_of_avg_zscore_1y},
    "ocn_089_top1_conc_ratio_rank_2y":           {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_089_top1_conc_ratio_rank_2y},
    "ocn_090_top1_conc_accel":                   {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_090_top1_conc_accel},
    "ocn_091_top1_conc_ewm_4q":                  {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_091_top1_conc_ewm_4q},
    "ocn_092_top1_conc_slope_4q":                {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_092_top1_conc_slope_4q},
    "ocn_093_top1_conc_ratio_3y_chg":            {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_093_top1_conc_ratio_3y_chg},
    "ocn_094_top1_conc_vs_3y_mean":              {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_094_top1_conc_vs_3y_mean},
    "ocn_095_top1_conc_ratio_zscore_3y":         {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_095_top1_conc_ratio_zscore_3y},
    "ocn_096_top5_conc_ratio_rank_2y":           {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_096_top5_conc_ratio_rank_2y},
    "ocn_097_top5_conc_accel":                   {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_097_top5_conc_accel},
    "ocn_098_top5_conc_slope_4q":                {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_098_top5_conc_slope_4q},
    "ocn_099_top5_conc_3y_chg":                  {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_099_top5_conc_3y_chg},
    "ocn_100_top5_conc_vs_3y_mean":              {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_100_top5_conc_vs_3y_mean},
    "ocn_101_top5_conc_ratio_zscore_3y":         {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_101_top5_conc_ratio_zscore_3y},
    "ocn_102_top5_conc_rank_3y":                 {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_102_top5_conc_rank_3y},
    "ocn_103_top5_ewm_vs_raw":                   {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_103_top5_ewm_vs_raw},
    "ocn_104_top5_conc_ratio_2q_chg":            {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_104_top5_conc_ratio_2q_chg},
    "ocn_105_top5_to_top1_concentration_index":  {"inputs": ["top1_shares", "top5_shares"],                                                      "func": ocn_105_top5_to_top1_concentration_index},
    "ocn_106_top10_conc_ratio_rank_2y":          {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_106_top10_conc_ratio_rank_2y},
    "ocn_107_top10_conc_accel":                  {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_107_top10_conc_accel},
    "ocn_108_top10_conc_slope_4q":               {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_108_top10_conc_slope_4q},
    "ocn_109_top10_conc_3y_chg":                 {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_109_top10_conc_3y_chg},
    "ocn_110_top10_conc_vs_3y_mean":             {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_110_top10_conc_vs_3y_mean},
    "ocn_111_top10_conc_zscore_3y":              {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_111_top10_conc_zscore_3y},
    "ocn_112_top10_conc_rank_3y":                {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_112_top10_conc_rank_3y},
    "ocn_113_top10_ewm_vs_raw":                  {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_113_top10_ewm_vs_raw},
    "ocn_114_top10_conc_2q_chg":                 {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_114_top10_conc_2q_chg},
    "ocn_115_top10_to_top5_ratio":               {"inputs": ["top5_shares", "top10_shares"],                                                     "func": ocn_115_top10_to_top5_ratio},
    "ocn_116_hhi_per_holder":                    {"inputs": ["hhi", "inst_holders"],                                                             "func": ocn_116_hhi_per_holder},
    "ocn_117_conc_adjusted_holder_count":        {"inputs": ["hhi", "inst_holders"],                                                             "func": ocn_117_conc_adjusted_holder_count},
    "ocn_118_conc_adj_breadth_zscore_1y":        {"inputs": ["hhi", "inst_holders"],                                                             "func": ocn_118_conc_adj_breadth_zscore_1y},
    "ocn_119_top1_conc_per_holder":              {"inputs": ["top1_shares", "inst_shares", "inst_holders"],                                      "func": ocn_119_top1_conc_per_holder},
    "ocn_120_top5_conc_per_holder":              {"inputs": ["top5_shares", "inst_shares", "inst_holders"],                                      "func": ocn_120_top5_conc_per_holder},
    "ocn_121_hhi_x_top1_ratio":                  {"inputs": ["hhi", "top1_shares", "inst_shares"],                                               "func": ocn_121_hhi_x_top1_ratio},
    "ocn_122_hhi_x_top1_ratio_zscore_1y":        {"inputs": ["hhi", "top1_shares", "inst_shares"],                                               "func": ocn_122_hhi_x_top1_ratio_zscore_1y},
    "ocn_123_conc_breadth_divergence":           {"inputs": ["hhi", "inst_holders"],                                                             "func": ocn_123_conc_breadth_divergence},
    "ocn_124_eff_n_vs_holders_diff":             {"inputs": ["hhi", "inst_holders"],                                                             "func": ocn_124_eff_n_vs_holders_diff},
    "ocn_125_eff_n_holder_gap_yoy":              {"inputs": ["hhi", "inst_holders"],                                                             "func": ocn_125_eff_n_holder_gap_yoy},
    "ocn_126_avg_position_zscore_1y":            {"inputs": ["avg_position"],                                                                    "func": ocn_126_avg_position_zscore_1y},
    "ocn_127_avg_position_rank_1y":              {"inputs": ["avg_position"],                                                                    "func": ocn_127_avg_position_rank_1y},
    "ocn_128_avg_position_yoy_pct_chg":          {"inputs": ["avg_position"],                                                                    "func": ocn_128_avg_position_yoy_pct_chg},
    "ocn_129_avg_position_qoq_chg":              {"inputs": ["avg_position"],                                                                    "func": ocn_129_avg_position_qoq_chg},
    "ocn_130_avg_pos_vs_1y_mean":                {"inputs": ["avg_position"],                                                                    "func": ocn_130_avg_pos_vs_1y_mean},
    "ocn_131_inst_value_per_holder_zscore_1y":   {"inputs": ["inst_value", "inst_holders"],                                                      "func": ocn_131_inst_value_per_holder_zscore_1y},
    "ocn_132_inst_value_per_holder_rank_1y":     {"inputs": ["inst_value", "inst_holders"],                                                      "func": ocn_132_inst_value_per_holder_rank_1y},
    "ocn_133_inst_value_per_holder_yoy_chg":     {"inputs": ["inst_value", "inst_holders"],                                                      "func": ocn_133_inst_value_per_holder_yoy_chg},
    "ocn_134_top1_value_estimate_zscore_1y":     {"inputs": ["top1_shares", "inst_shares", "inst_value"],                                        "func": ocn_134_top1_value_estimate_zscore_1y},
    "ocn_135_avg_pos_slope_4q":                  {"inputs": ["avg_position"],                                                                    "func": ocn_135_avg_pos_slope_4q},
    "ocn_136_conc_rising_regime":                {"inputs": ["hhi", "top5_shares", "inst_shares"],                                               "func": ocn_136_conc_rising_regime},
    "ocn_137_conc_composite_zscore_1y":          {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_137_conc_composite_zscore_1y},
    "ocn_138_conc_composite_rank_1y":            {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_138_conc_composite_rank_1y},
    "ocn_139_conc_composite_yoy_chg":            {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_139_conc_composite_yoy_chg},
    "ocn_140_conc_composite_2y_chg":             {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_140_conc_composite_2y_chg},
    "ocn_141_conc_composite_slope_4q":           {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_141_conc_composite_slope_4q},
    "ocn_142_hhi_top1_divergence":               {"inputs": ["hhi", "top1_shares", "inst_shares"],                                               "func": ocn_142_hhi_top1_divergence},
    "ocn_143_top5_top10_divergence":             {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                      "func": ocn_143_top5_top10_divergence},
    "ocn_144_conc_momentum_score":               {"inputs": ["hhi", "top1_shares", "top5_shares", "inst_shares"],                                "func": ocn_144_conc_momentum_score},
    "ocn_145_conc_momentum_sum_4q":              {"inputs": ["hhi", "top1_shares", "top5_shares", "inst_shares"],                                "func": ocn_145_conc_momentum_sum_4q},
    "ocn_146_tail_conc_ratio":                   {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                      "func": ocn_146_tail_conc_ratio},
    "ocn_147_tail_conc_ratio_zscore_1y":         {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                      "func": ocn_147_tail_conc_ratio_zscore_1y},
    "ocn_148_tail_conc_ratio_yoy_chg":           {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                      "func": ocn_148_tail_conc_ratio_yoy_chg},
    "ocn_149_outside_top5_conc_ratio":           {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_149_outside_top5_conc_ratio},
    "ocn_150_outside_top5_conc_zscore_2y":       {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_150_outside_top5_conc_zscore_2y},
    "ocn_176_avg_position_2y_mean":              {"inputs": ["avg_position"],                                                                    "func": ocn_176_avg_position_2y_mean},
    "ocn_177_avg_position_2y_zscore":            {"inputs": ["avg_position"],                                                                    "func": ocn_177_avg_position_2y_zscore},
    "ocn_178_avg_position_vs_2y_mean":           {"inputs": ["avg_position"],                                                                    "func": ocn_178_avg_position_vs_2y_mean},
    "ocn_179_avg_position_qoq_pct_chg":          {"inputs": ["avg_position"],                                                                    "func": ocn_179_avg_position_qoq_pct_chg},
    "ocn_180_avg_position_ewm_4q":               {"inputs": ["avg_position"],                                                                    "func": ocn_180_avg_position_ewm_4q},
    "ocn_181_inst_value_zscore_1y":              {"inputs": ["inst_value"],                                                                      "func": ocn_181_inst_value_zscore_1y},
    "ocn_182_inst_value_rank_1y":                {"inputs": ["inst_value"],                                                                      "func": ocn_182_inst_value_rank_1y},
    "ocn_183_inst_value_yoy_chg":                {"inputs": ["inst_value"],                                                                      "func": ocn_183_inst_value_yoy_chg},
    "ocn_184_inst_value_qoq_chg":                {"inputs": ["inst_value"],                                                                      "func": ocn_184_inst_value_qoq_chg},
    "ocn_185_inst_value_vs_1y_mean":             {"inputs": ["inst_value"],                                                                      "func": ocn_185_inst_value_vs_1y_mean},
    "ocn_186_hhi_abs_dev_from_2y_mean":          {"inputs": ["hhi"],                                                                             "func": ocn_186_hhi_abs_dev_from_2y_mean},
    "ocn_187_top1_conc_ratio_ewm_2q":            {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_187_top1_conc_ratio_ewm_2q},
    "ocn_188_top5_conc_ratio_ewm_2q":            {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_188_top5_conc_ratio_ewm_2q},
    "ocn_189_top10_conc_ratio_ewm_2q":           {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_189_top10_conc_ratio_ewm_2q},
    "ocn_190_conc_composite_median_1y":          {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_190_conc_composite_median_1y},
    "ocn_191_top1_conc_expanding_rank":          {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_191_top1_conc_expanding_rank},
    "ocn_192_top5_conc_expanding_rank":          {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_192_top5_conc_expanding_rank},
    "ocn_193_outside_top5_conc_yoy_chg":         {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_193_outside_top5_conc_yoy_chg},
    "ocn_194_tail_conc_ratio_qoq_chg":           {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                      "func": ocn_194_tail_conc_ratio_qoq_chg},
    "ocn_195_gini_proxy_yoy_chg":                {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],                       "func": ocn_195_gini_proxy_yoy_chg},
    "ocn_196_hhi_vs_top10_ratio_spread":         {"inputs": ["hhi", "top10_shares", "inst_shares"],                                              "func": ocn_196_hhi_vs_top10_ratio_spread},
    "ocn_197_top10_conc_expanding_zscore":       {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_197_top10_conc_expanding_zscore},
    "ocn_198_conc_composite_3y_chg":             {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_198_conc_composite_3y_chg},
    "ocn_199_hhi_std_4q":                        {"inputs": ["hhi"],                                                                             "func": ocn_199_hhi_std_4q},
    "ocn_200_inst_holders_vs_1y_mean":           {"inputs": ["inst_holders"],                                                                    "func": ocn_200_inst_holders_vs_1y_mean},
}
