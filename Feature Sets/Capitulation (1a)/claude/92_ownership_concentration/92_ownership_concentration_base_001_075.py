"""
92_ownership_concentration — Base Features 001-075, extended to 100
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
    """Element-wise a / b; returns 0 where b is zero or NaN."""
    b_safe = b.replace(0, np.nan)
    return a / b_safe


def _safe_div_abs(a: pd.Series, b: pd.Series) -> pd.Series:
    """Element-wise a / |b|; returns 0 where |b| is zero or NaN."""
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
# Features 001-075
# ===========================================================================

# --- HHI Level features (001-010) ------------------------------------------

def ocn_001_hhi_raw(hhi: pd.Series) -> pd.Series:
    """Raw HHI value (0..1); higher = more concentrated."""
    return _align_quarterly_to_daily(hhi).copy()


def ocn_002_hhi_1y_mean(hhi: pd.Series) -> pd.Series:
    """1-year rolling mean of HHI."""
    return _rolling_mean(_align_quarterly_to_daily(hhi), _TD_YEAR)


def ocn_003_hhi_2y_mean(hhi: pd.Series) -> pd.Series:
    """2-year rolling mean of HHI."""
    return _rolling_mean(_align_quarterly_to_daily(hhi), _TD_2Y)


def ocn_004_hhi_1y_max(hhi: pd.Series) -> pd.Series:
    """1-year rolling maximum HHI."""
    return _rolling_max(_align_quarterly_to_daily(hhi), _TD_YEAR)


def ocn_005_hhi_1y_min(hhi: pd.Series) -> pd.Series:
    """1-year rolling minimum HHI."""
    return _rolling_min(_align_quarterly_to_daily(hhi), _TD_YEAR)


def ocn_006_hhi_vs_1y_mean(hhi: pd.Series) -> pd.Series:
    """HHI minus its 1-year rolling mean (deviation from trend)."""
    h = _align_quarterly_to_daily(hhi)
    return h - _rolling_mean(h, _TD_YEAR)


def ocn_007_hhi_zscore_1y(hhi: pd.Series) -> pd.Series:
    """Z-score of HHI over a 1-year rolling window."""
    return _zscore_rolling(_align_quarterly_to_daily(hhi), _TD_YEAR)


def ocn_008_hhi_zscore_2y(hhi: pd.Series) -> pd.Series:
    """Z-score of HHI over a 2-year rolling window."""
    return _zscore_rolling(_align_quarterly_to_daily(hhi), _TD_2Y)


def ocn_009_hhi_rank_1y(hhi: pd.Series) -> pd.Series:
    """Percentile rank of HHI over a 1-year rolling window."""
    return _rolling_rank_pct(_align_quarterly_to_daily(hhi), _TD_YEAR)


def ocn_010_hhi_rank_2y(hhi: pd.Series) -> pd.Series:
    """Percentile rank of HHI over a 2-year rolling window."""
    return _rolling_rank_pct(_align_quarterly_to_daily(hhi), _TD_2Y)


# --- Effective Number of Holders (011-020) ----------------------------------

def ocn_011_eff_n_holders(hhi: pd.Series) -> pd.Series:
    """Effective number of holders = 1 / HHI."""
    h = _align_quarterly_to_daily(hhi)
    return _safe_div(pd.Series(np.ones(len(h)), index=h.index), h)


def ocn_012_eff_n_holders_1y_mean(hhi: pd.Series) -> pd.Series:
    """1-year rolling mean of effective number of holders."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return _rolling_mean(eff, _TD_YEAR)


def ocn_013_eff_n_holders_vs_1y_mean(hhi: pd.Series) -> pd.Series:
    """Effective-N minus its 1-year rolling mean."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return eff - _rolling_mean(eff, _TD_YEAR)


def ocn_014_eff_n_holders_zscore_1y(hhi: pd.Series) -> pd.Series:
    """Z-score of effective number of holders over 1 year."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return _zscore_rolling(eff, _TD_YEAR)


def ocn_015_eff_n_holders_rank_1y(hhi: pd.Series) -> pd.Series:
    """Percentile rank of effective-N over 1 year."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return _rolling_rank_pct(eff, _TD_YEAR)


def ocn_016_eff_n_pct_of_actual(hhi: pd.Series,
                                  inst_holders: pd.Series) -> pd.Series:
    """Ratio of effective-N to actual holder count; near 1 = uniform."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return _safe_div(eff, _align_quarterly_to_daily(inst_holders))


def ocn_017_eff_n_qoq_change(hhi: pd.Series) -> pd.Series:
    """QoQ change in effective number of holders."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return eff - eff.shift(_TD_QTR)


def ocn_018_eff_n_yoy_change(hhi: pd.Series) -> pd.Series:
    """YoY change in effective number of holders."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return eff - eff.shift(_TD_YEAR)


def ocn_019_eff_n_2y_change(hhi: pd.Series) -> pd.Series:
    """2-year change in effective number of holders."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return eff - eff.shift(_TD_2Y)


def ocn_020_eff_n_ewm_26w(hhi: pd.Series) -> pd.Series:
    """26-week EWM of effective number of holders (span=130 td)."""
    eff = _safe_div(pd.Series(np.ones(len(hhi)), index=hhi.index),
                    _align_quarterly_to_daily(hhi))
    return _ewm_mean(eff, 130)


# --- Top-1 Concentration Ratio (021-030) ------------------------------------

def ocn_021_top1_conc_ratio(top1_shares: pd.Series,
                              inst_shares: pd.Series) -> pd.Series:
    """Top-1 holder share as fraction of all institutional shares."""
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(inst_shares))


def ocn_022_top1_conc_ratio_1y_mean(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """1-year rolling mean of top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_mean(r, _TD_YEAR)


def ocn_023_top1_conc_ratio_zscore_1y(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Z-score of top-1 concentration ratio over 1 year."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(r, _TD_YEAR)


def ocn_024_top1_conc_ratio_rank_1y(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of top-1 concentration ratio over 1 year."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_rank_pct(r, _TD_YEAR)


def ocn_025_top1_conc_ratio_qoq_chg(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """QoQ change in top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_QTR)


def ocn_026_top1_conc_ratio_yoy_chg(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """YoY change in top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_YEAR)


def ocn_027_top1_conc_ratio_2y_chg(top1_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """2-year change in top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_2Y)


def ocn_028_top1_conc_ratio_vs_1y_max(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Top-1 ratio minus its 1-year rolling max (distance from peak)."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_max(r, _TD_YEAR)


def ocn_029_top1_conc_ratio_vs_1y_min(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Top-1 ratio minus its 1-year rolling min (distance from trough)."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_min(r, _TD_YEAR)


def ocn_030_top1_conc_ratio_ewm_1y(top1_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """EWM (span=252) of top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _ewm_mean(r, _TD_YEAR)


# --- Top-5 Concentration Ratio (031-040) ------------------------------------

def ocn_031_top5_conc_ratio(top5_shares: pd.Series,
                              inst_shares: pd.Series) -> pd.Series:
    """Top-5 holder share as fraction of all institutional shares."""
    return _safe_div(_align_quarterly_to_daily(top5_shares),
                     _align_quarterly_to_daily(inst_shares))


def ocn_032_top5_conc_ratio_1y_mean(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """1-year rolling mean of top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_mean(r, _TD_YEAR)


def ocn_033_top5_conc_ratio_zscore_1y(top5_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Z-score of top-5 concentration ratio over 1 year."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(r, _TD_YEAR)


def ocn_034_top5_conc_ratio_rank_1y(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of top-5 concentration ratio over 1 year."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_rank_pct(r, _TD_YEAR)


def ocn_035_top5_conc_ratio_qoq_chg(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """QoQ change in top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_QTR)


def ocn_036_top5_conc_ratio_yoy_chg(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """YoY change in top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_YEAR)


def ocn_037_top5_conc_ratio_2y_chg(top5_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """2-year change in top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_2Y)


def ocn_038_top5_conc_ratio_vs_2y_mean(top5_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """Top-5 ratio minus its 2-year rolling mean."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_mean(r, _TD_2Y)


def ocn_039_top5_conc_ratio_zscore_2y(top5_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """Z-score of top-5 concentration ratio over 2 years."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(r, _TD_2Y)


def ocn_040_top5_conc_ratio_ewm_1y(top5_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """EWM (span=252) of top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _ewm_mean(r, _TD_YEAR)


# --- Top-10 Concentration Ratio (041-050) -----------------------------------

def ocn_041_top10_conc_ratio(top10_shares: pd.Series,
                               inst_shares: pd.Series) -> pd.Series:
    """Top-10 holder share as fraction of all institutional shares."""
    return _safe_div(_align_quarterly_to_daily(top10_shares),
                     _align_quarterly_to_daily(inst_shares))


def ocn_042_top10_conc_ratio_1y_mean(top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """1-year rolling mean of top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_mean(r, _TD_YEAR)


def ocn_043_top10_conc_ratio_zscore_1y(top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """Z-score of top-10 concentration ratio over 1 year."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(r, _TD_YEAR)


def ocn_044_top10_conc_ratio_rank_1y(top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of top-10 concentration ratio over 1 year."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_rank_pct(r, _TD_YEAR)


def ocn_045_top10_conc_ratio_qoq_chg(top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change in top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_QTR)


def ocn_046_top10_conc_ratio_yoy_chg(top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """YoY change in top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_YEAR)


def ocn_047_top10_conc_ratio_2y_chg(top10_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """2-year change in top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - r.shift(_TD_2Y)


def ocn_048_top10_conc_ratio_vs_2y_mean(top10_shares: pd.Series,
                                         inst_shares: pd.Series) -> pd.Series:
    """Top-10 ratio minus its 2-year rolling mean."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_mean(r, _TD_2Y)


def ocn_049_top10_conc_ratio_zscore_2y(top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """Z-score of top-10 concentration ratio over 2 years."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _zscore_rolling(r, _TD_2Y)


def ocn_050_top10_conc_ratio_ewm_1y(top10_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """EWM (span=252) of top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _ewm_mean(r, _TD_YEAR)


# --- Tranche Spread / Gini-Like Proxies (051-060) ---------------------------

def ocn_051_top1_to_top5_spread(top1_shares: pd.Series,
                                  top5_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """Fraction of inst_shares in top-1 vs top-5: top1/inst - top5/inst."""
    t1 = _safe_div(_align_quarterly_to_daily(top1_shares),
                   _align_quarterly_to_daily(inst_shares))
    t5 = _safe_div(_align_quarterly_to_daily(top5_shares),
                   _align_quarterly_to_daily(inst_shares))
    return t1 - t5


def ocn_052_top5_to_top10_spread(top5_shares: pd.Series,
                                   top10_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Incremental share from holders 6-10: (top10-top5)/inst_shares."""
    t5  = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div(t10 - t5, ins)


def ocn_053_top1_to_rest_ratio(top1_shares: pd.Series,
                                 top5_shares: pd.Series) -> pd.Series:
    """Top-1 shares divided by shares held by holders 2-5."""
    t1 = _align_quarterly_to_daily(top1_shares)
    t5 = _align_quarterly_to_daily(top5_shares)
    rest = (t5 - t1).clip(lower=0)
    return _safe_div(t1, rest)


def ocn_054_top5_to_rest_ratio(top5_shares: pd.Series,
                                 top10_shares: pd.Series) -> pd.Series:
    """Top-5 shares divided by shares held by holders 6-10."""
    t5  = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    rest = (t10 - t5).clip(lower=0)
    return _safe_div(t5, rest)


def ocn_055_outside_top10_share(top10_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """Fraction of institutional shares held outside the top-10."""
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    outside = (ins - t10).clip(lower=0)
    return _safe_div(outside, ins)


def ocn_056_outside_top10_share_zscore_1y(top10_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """Z-score (1y) of fraction outside top-10."""
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    outside = _safe_div((ins - t10).clip(lower=0), ins)
    return _zscore_rolling(outside, _TD_YEAR)


def ocn_057_gini_proxy_top_tranche(top1_shares: pd.Series,
                                    top5_shares: pd.Series,
                                    top10_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """Gini-like proxy from three quantile points of the top-N distribution."""
    ins = _align_quarterly_to_daily(inst_shares)
    s1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    s5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    s10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    # Lorenz area approximation: area under (0,0),(0.1,s1),(0.5,s5),(1,s10)
    # vs equal area = 0.5; higher = more concentrated
    lorenz_area = 0.5 * (0.1 * s1 + (0.5 - 0.1) * (s1 + s5) +
                         (1.0 - 0.5) * (s5 + s10))
    return lorenz_area


def ocn_058_gini_proxy_zscore_1y(top1_shares: pd.Series,
                                  top5_shares: pd.Series,
                                  top10_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """Z-score (1y) of the Gini-like proxy."""
    ins = _align_quarterly_to_daily(inst_shares)
    s1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    s5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    s10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    lorenz_area = 0.5 * (0.1 * s1 + (0.5 - 0.1) * (s1 + s5) +
                         (1.0 - 0.5) * (s5 + s10))
    return _zscore_rolling(lorenz_area, _TD_YEAR)


def ocn_059_tranche_dispersion(top1_shares: pd.Series,
                                 top5_shares: pd.Series,
                                 top10_shares: pd.Series,
                                 inst_shares: pd.Series) -> pd.Series:
    """Std of the three tranche ratios — higher = uneven step sizes."""
    ins = _align_quarterly_to_daily(inst_shares)
    s1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    s5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    s10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    mean_r = (s1 + s5 + s10) / 3.0
    var_r  = ((s1 - mean_r)**2 + (s5 - mean_r)**2 + (s10 - mean_r)**2) / 3.0
    return var_r.apply(np.sqrt)


def ocn_060_tranche_dispersion_yoy_chg(top1_shares: pd.Series,
                                        top5_shares: pd.Series,
                                        top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """YoY change in tranche dispersion."""
    ins = _align_quarterly_to_daily(inst_shares)
    s1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    s5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    s10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    mean_r = (s1 + s5 + s10) / 3.0
    var_r  = ((s1 - mean_r)**2 + (s5 - mean_r)**2 + (s10 - mean_r)**2) / 3.0
    disp = var_r.apply(np.sqrt)
    return disp - disp.shift(_TD_YEAR)


# --- HHI Shifts & Acceleration (061-070) ------------------------------------

def ocn_061_hhi_qoq_chg(hhi: pd.Series) -> pd.Series:
    """QoQ change in HHI (63-day shift)."""
    h = _align_quarterly_to_daily(hhi)
    return h - h.shift(_TD_QTR)


def ocn_062_hhi_yoy_chg(hhi: pd.Series) -> pd.Series:
    """YoY change in HHI."""
    h = _align_quarterly_to_daily(hhi)
    return h - h.shift(_TD_YEAR)


def ocn_063_hhi_2y_chg(hhi: pd.Series) -> pd.Series:
    """2-year change in HHI."""
    h = _align_quarterly_to_daily(hhi)
    return h - h.shift(_TD_2Y)


def ocn_064_hhi_3y_chg(hhi: pd.Series) -> pd.Series:
    """3-year change in HHI."""
    h = _align_quarterly_to_daily(hhi)
    return h - h.shift(_TD_3Y)


def ocn_065_hhi_qoq_pct_chg(hhi: pd.Series) -> pd.Series:
    """QoQ percentage change in HHI."""
    h = _align_quarterly_to_daily(hhi)
    prev = h.shift(_TD_QTR)
    return _safe_div_abs(h - prev, prev)


def ocn_066_hhi_yoy_pct_chg(hhi: pd.Series) -> pd.Series:
    """YoY percentage change in HHI."""
    h = _align_quarterly_to_daily(hhi)
    prev = h.shift(_TD_YEAR)
    return _safe_div_abs(h - prev, prev)


def ocn_067_hhi_accel_qoq(hhi: pd.Series) -> pd.Series:
    """Acceleration: QoQ change in the QoQ HHI change."""
    h = _align_quarterly_to_daily(hhi)
    d1 = h - h.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_068_hhi_slope_4q(hhi: pd.Series) -> pd.Series:
    """Linear slope of HHI over the past 4 quarters (252 td)."""
    h = _align_quarterly_to_daily(hhi)
    x = np.arange(_TD_YEAR)

    def _slope(arr):
        if len(arr) < 4:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan

    return h.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def ocn_069_hhi_slope_8q(hhi: pd.Series) -> pd.Series:
    """Linear slope of HHI over the past 8 quarters (504 td)."""
    h = _align_quarterly_to_daily(hhi)

    def _slope(arr):
        if len(arr) < 4:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan

    return h.rolling(_TD_2Y, min_periods=4).apply(_slope, raw=True)


def ocn_070_hhi_ewm_vs_raw(hhi: pd.Series) -> pd.Series:
    """HHI minus its EWM (span=252); positive = above trend."""
    h = _align_quarterly_to_daily(hhi)
    return h - _ewm_mean(h, _TD_YEAR)


# --- Cross-Series Concentration Signals (071-075) ---------------------------

def ocn_071_avg_pos_vs_mean_ratio(avg_position: pd.Series,
                                   inst_shares: pd.Series,
                                   inst_holders: pd.Series) -> pd.Series:
    """Avg position vs the equal-share mean: avg_position / (inst_shares/inst_holders)."""
    avg  = _align_quarterly_to_daily(avg_position)
    ins  = _align_quarterly_to_daily(inst_shares)
    n    = _align_quarterly_to_daily(inst_holders)
    eq   = _safe_div(ins, n)
    return _safe_div(avg, eq)


def ocn_072_value_conc_top1(top1_shares: pd.Series,
                              inst_shares: pd.Series,
                              inst_value: pd.Series) -> pd.Series:
    """Estimated USD value of top-1 holder as fraction of total inst value."""
    t1  = _align_quarterly_to_daily(top1_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    val = _align_quarterly_to_daily(inst_value)
    share_frac = _safe_div(t1, ins)
    return share_frac * val


def ocn_073_value_conc_top1_ratio(top1_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Top-1 share fraction squared (HHI lower bound proxy)."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r ** 2


def ocn_074_hhi_vs_top5_ratio_spread(hhi: pd.Series,
                                      top5_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """HHI minus top-5 concentration ratio squared (structure residual)."""
    h  = _align_quarterly_to_daily(hhi)
    r5 = _safe_div(_align_quarterly_to_daily(top5_shares),
                   _align_quarterly_to_daily(inst_shares))
    return h - r5 ** 2


def ocn_075_concentration_composite(hhi: pd.Series,
                                     top1_shares: pd.Series,
                                     top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Equal-weighted composite of HHI, top-1 ratio, and top-5 ratio."""
    h  = _align_quarterly_to_daily(hhi)
    r1 = _safe_div(_align_quarterly_to_daily(top1_shares),
                   _align_quarterly_to_daily(inst_shares))
    r5 = _safe_div(_align_quarterly_to_daily(top5_shares),
                   _align_quarterly_to_daily(inst_shares))
    return (h + r1 + r5) / 3.0


# --- New Features 151-175 ---------------------------------------------------

def ocn_151_hhi_3y_mean(hhi: pd.Series) -> pd.Series:
    """3-year rolling mean of HHI."""
    return _rolling_mean(_align_quarterly_to_daily(hhi), _TD_3Y)


def ocn_152_hhi_median_1y(hhi: pd.Series) -> pd.Series:
    """1-year rolling median of HHI."""
    return _rolling_median(_align_quarterly_to_daily(hhi), _TD_YEAR)


def ocn_153_hhi_median_2y(hhi: pd.Series) -> pd.Series:
    """2-year rolling median of HHI."""
    return _rolling_median(_align_quarterly_to_daily(hhi), _TD_2Y)


def ocn_154_hhi_vs_median_1y(hhi: pd.Series) -> pd.Series:
    """HHI minus its 1-year rolling median."""
    h = _align_quarterly_to_daily(hhi)
    return h - _rolling_median(h, _TD_YEAR)


def ocn_155_hhi_ewm_vs_3y_mean(hhi: pd.Series) -> pd.Series:
    """EWM(252) of HHI minus its 3-year rolling mean."""
    h = _align_quarterly_to_daily(hhi)
    return _ewm_mean(h, _TD_YEAR) - _rolling_mean(h, _TD_3Y)


def ocn_156_hhi_2q_chg(hhi: pd.Series) -> pd.Series:
    """2-quarter change in HHI (126-day shift)."""
    h = _align_quarterly_to_daily(hhi)
    return h - h.shift(_TD_2Q)


def ocn_157_hhi_2q_pct_chg(hhi: pd.Series) -> pd.Series:
    """2-quarter percentage change in HHI."""
    h = _align_quarterly_to_daily(hhi)
    prev = h.shift(_TD_2Q)
    return _safe_div_abs(h - prev, prev)


def ocn_158_hhi_3q_chg(hhi: pd.Series) -> pd.Series:
    """3-quarter change in HHI (189-day shift)."""
    h = _align_quarterly_to_daily(hhi)
    return h - h.shift(3 * _TD_QTR)


def ocn_159_hhi_ewm_52w(hhi: pd.Series) -> pd.Series:
    """52-week EWM (span=260) of HHI."""
    return _ewm_mean(_align_quarterly_to_daily(hhi), 260)


def ocn_160_hhi_max_vs_min_ratio_1y(hhi: pd.Series) -> pd.Series:
    """Ratio of 1-year rolling max to 1-year rolling min of HHI."""
    h = _align_quarterly_to_daily(hhi)
    return _safe_div(_rolling_max(h, _TD_YEAR), _rolling_min(h, _TD_YEAR))


def ocn_161_top1_conc_median_1y(top1_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """1-year rolling median of top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_median(r, _TD_YEAR)


def ocn_162_top1_conc_vs_median_1y(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Top-1 concentration ratio minus its 1-year rolling median."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_median(r, _TD_YEAR)


def ocn_163_top5_conc_median_1y(top5_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """1-year rolling median of top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_median(r, _TD_YEAR)


def ocn_164_top5_conc_vs_median_1y(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """Top-5 concentration ratio minus its 1-year rolling median."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return r - _rolling_median(r, _TD_YEAR)


def ocn_165_top10_conc_median_1y(top10_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """1-year rolling median of top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_median(r, _TD_YEAR)


def ocn_166_top5_to_inst_ewm_vs_raw(top5_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """Top-5 ratio EWM(126) minus raw ratio: short-term mean-reversion signal."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _ewm_mean(r, _TD_2Q) - r


def ocn_167_hhi_slope_2q(hhi: pd.Series) -> pd.Series:
    """Linear slope of HHI over the past 2 quarters (126 td)."""
    h = _align_quarterly_to_daily(hhi)

    def _slope(arr):
        if len(arr) < 2:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan

    return h.rolling(_TD_2Q, min_periods=2).apply(_slope, raw=True)


def ocn_168_top1_conc_range_1y(top1_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """1-year range (max-min) of top-1 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_max(r, _TD_YEAR) - _rolling_min(r, _TD_YEAR)


def ocn_169_top5_conc_range_1y(top5_shares: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """1-year range (max-min) of top-5 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top5_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_max(r, _TD_YEAR) - _rolling_min(r, _TD_YEAR)


def ocn_170_top10_conc_range_1y(top10_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """1-year range (max-min) of top-10 concentration ratio."""
    r = _safe_div(_align_quarterly_to_daily(top10_shares),
                  _align_quarterly_to_daily(inst_shares))
    return _rolling_max(r, _TD_YEAR) - _rolling_min(r, _TD_YEAR)


def ocn_171_inst_holders_zscore_1y(inst_holders: pd.Series) -> pd.Series:
    """Z-score of institutional holder count over 1 year."""
    return _zscore_rolling(_align_quarterly_to_daily(inst_holders), _TD_YEAR)


def ocn_172_inst_holders_rank_1y(inst_holders: pd.Series) -> pd.Series:
    """Percentile rank of institutional holder count over 1 year."""
    return _rolling_rank_pct(_align_quarterly_to_daily(inst_holders), _TD_YEAR)


def ocn_173_inst_holders_yoy_chg(inst_holders: pd.Series) -> pd.Series:
    """YoY change in institutional holder count."""
    n = _align_quarterly_to_daily(inst_holders)
    return n - n.shift(_TD_YEAR)


def ocn_174_inst_holders_qoq_chg(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in institutional holder count."""
    n = _align_quarterly_to_daily(inst_holders)
    return n - n.shift(_TD_QTR)


def ocn_175_hhi_x_holder_count(hhi: pd.Series,
                                 inst_holders: pd.Series) -> pd.Series:
    """Product of HHI and holder count: joint signal of concentration and breadth."""
    h = _align_quarterly_to_daily(hhi)
    n = _align_quarterly_to_daily(inst_holders)
    return h * n


# ===========================================================================
# Registry
# ===========================================================================
OWNERSHIP_CONCENTRATION_REGISTRY_001_075 = {
    "ocn_001_hhi_raw":                       {"inputs": ["hhi"],                                                              "func": ocn_001_hhi_raw},
    "ocn_002_hhi_1y_mean":                   {"inputs": ["hhi"],                                                              "func": ocn_002_hhi_1y_mean},
    "ocn_003_hhi_2y_mean":                   {"inputs": ["hhi"],                                                              "func": ocn_003_hhi_2y_mean},
    "ocn_004_hhi_1y_max":                    {"inputs": ["hhi"],                                                              "func": ocn_004_hhi_1y_max},
    "ocn_005_hhi_1y_min":                    {"inputs": ["hhi"],                                                              "func": ocn_005_hhi_1y_min},
    "ocn_006_hhi_vs_1y_mean":                {"inputs": ["hhi"],                                                              "func": ocn_006_hhi_vs_1y_mean},
    "ocn_007_hhi_zscore_1y":                 {"inputs": ["hhi"],                                                              "func": ocn_007_hhi_zscore_1y},
    "ocn_008_hhi_zscore_2y":                 {"inputs": ["hhi"],                                                              "func": ocn_008_hhi_zscore_2y},
    "ocn_009_hhi_rank_1y":                   {"inputs": ["hhi"],                                                              "func": ocn_009_hhi_rank_1y},
    "ocn_010_hhi_rank_2y":                   {"inputs": ["hhi"],                                                              "func": ocn_010_hhi_rank_2y},
    "ocn_011_eff_n_holders":                 {"inputs": ["hhi"],                                                              "func": ocn_011_eff_n_holders},
    "ocn_012_eff_n_holders_1y_mean":         {"inputs": ["hhi"],                                                              "func": ocn_012_eff_n_holders_1y_mean},
    "ocn_013_eff_n_holders_vs_1y_mean":      {"inputs": ["hhi"],                                                              "func": ocn_013_eff_n_holders_vs_1y_mean},
    "ocn_014_eff_n_holders_zscore_1y":       {"inputs": ["hhi"],                                                              "func": ocn_014_eff_n_holders_zscore_1y},
    "ocn_015_eff_n_holders_rank_1y":         {"inputs": ["hhi"],                                                              "func": ocn_015_eff_n_holders_rank_1y},
    "ocn_016_eff_n_pct_of_actual":           {"inputs": ["hhi", "inst_holders"],                                              "func": ocn_016_eff_n_pct_of_actual},
    "ocn_017_eff_n_qoq_change":              {"inputs": ["hhi"],                                                              "func": ocn_017_eff_n_qoq_change},
    "ocn_018_eff_n_yoy_change":              {"inputs": ["hhi"],                                                              "func": ocn_018_eff_n_yoy_change},
    "ocn_019_eff_n_2y_change":               {"inputs": ["hhi"],                                                              "func": ocn_019_eff_n_2y_change},
    "ocn_020_eff_n_ewm_26w":                 {"inputs": ["hhi"],                                                              "func": ocn_020_eff_n_ewm_26w},
    "ocn_021_top1_conc_ratio":               {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_021_top1_conc_ratio},
    "ocn_022_top1_conc_ratio_1y_mean":       {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_022_top1_conc_ratio_1y_mean},
    "ocn_023_top1_conc_ratio_zscore_1y":     {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_023_top1_conc_ratio_zscore_1y},
    "ocn_024_top1_conc_ratio_rank_1y":       {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_024_top1_conc_ratio_rank_1y},
    "ocn_025_top1_conc_ratio_qoq_chg":       {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_025_top1_conc_ratio_qoq_chg},
    "ocn_026_top1_conc_ratio_yoy_chg":       {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_026_top1_conc_ratio_yoy_chg},
    "ocn_027_top1_conc_ratio_2y_chg":        {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_027_top1_conc_ratio_2y_chg},
    "ocn_028_top1_conc_ratio_vs_1y_max":     {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_028_top1_conc_ratio_vs_1y_max},
    "ocn_029_top1_conc_ratio_vs_1y_min":     {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_029_top1_conc_ratio_vs_1y_min},
    "ocn_030_top1_conc_ratio_ewm_1y":        {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_030_top1_conc_ratio_ewm_1y},
    "ocn_031_top5_conc_ratio":               {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_031_top5_conc_ratio},
    "ocn_032_top5_conc_ratio_1y_mean":       {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_032_top5_conc_ratio_1y_mean},
    "ocn_033_top5_conc_ratio_zscore_1y":     {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_033_top5_conc_ratio_zscore_1y},
    "ocn_034_top5_conc_ratio_rank_1y":       {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_034_top5_conc_ratio_rank_1y},
    "ocn_035_top5_conc_ratio_qoq_chg":       {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_035_top5_conc_ratio_qoq_chg},
    "ocn_036_top5_conc_ratio_yoy_chg":       {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_036_top5_conc_ratio_yoy_chg},
    "ocn_037_top5_conc_ratio_2y_chg":        {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_037_top5_conc_ratio_2y_chg},
    "ocn_038_top5_conc_ratio_vs_2y_mean":    {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_038_top5_conc_ratio_vs_2y_mean},
    "ocn_039_top5_conc_ratio_zscore_2y":     {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_039_top5_conc_ratio_zscore_2y},
    "ocn_040_top5_conc_ratio_ewm_1y":        {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_040_top5_conc_ratio_ewm_1y},
    "ocn_041_top10_conc_ratio":              {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_041_top10_conc_ratio},
    "ocn_042_top10_conc_ratio_1y_mean":      {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_042_top10_conc_ratio_1y_mean},
    "ocn_043_top10_conc_ratio_zscore_1y":    {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_043_top10_conc_ratio_zscore_1y},
    "ocn_044_top10_conc_ratio_rank_1y":      {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_044_top10_conc_ratio_rank_1y},
    "ocn_045_top10_conc_ratio_qoq_chg":      {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_045_top10_conc_ratio_qoq_chg},
    "ocn_046_top10_conc_ratio_yoy_chg":      {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_046_top10_conc_ratio_yoy_chg},
    "ocn_047_top10_conc_ratio_2y_chg":       {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_047_top10_conc_ratio_2y_chg},
    "ocn_048_top10_conc_ratio_vs_2y_mean":   {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_048_top10_conc_ratio_vs_2y_mean},
    "ocn_049_top10_conc_ratio_zscore_2y":    {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_049_top10_conc_ratio_zscore_2y},
    "ocn_050_top10_conc_ratio_ewm_1y":       {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_050_top10_conc_ratio_ewm_1y},
    "ocn_051_top1_to_top5_spread":           {"inputs": ["top1_shares", "top5_shares", "inst_shares"],                        "func": ocn_051_top1_to_top5_spread},
    "ocn_052_top5_to_top10_spread":          {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                       "func": ocn_052_top5_to_top10_spread},
    "ocn_053_top1_to_rest_ratio":            {"inputs": ["top1_shares", "top5_shares"],                                       "func": ocn_053_top1_to_rest_ratio},
    "ocn_054_top5_to_rest_ratio":            {"inputs": ["top5_shares", "top10_shares"],                                      "func": ocn_054_top5_to_rest_ratio},
    "ocn_055_outside_top10_share":           {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_055_outside_top10_share},
    "ocn_056_outside_top10_share_zscore_1y": {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_056_outside_top10_share_zscore_1y},
    "ocn_057_gini_proxy_top_tranche":        {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],        "func": ocn_057_gini_proxy_top_tranche},
    "ocn_058_gini_proxy_zscore_1y":          {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],        "func": ocn_058_gini_proxy_zscore_1y},
    "ocn_059_tranche_dispersion":            {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],        "func": ocn_059_tranche_dispersion},
    "ocn_060_tranche_dispersion_yoy_chg":    {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],        "func": ocn_060_tranche_dispersion_yoy_chg},
    "ocn_061_hhi_qoq_chg":                  {"inputs": ["hhi"],                                                              "func": ocn_061_hhi_qoq_chg},
    "ocn_062_hhi_yoy_chg":                  {"inputs": ["hhi"],                                                              "func": ocn_062_hhi_yoy_chg},
    "ocn_063_hhi_2y_chg":                   {"inputs": ["hhi"],                                                              "func": ocn_063_hhi_2y_chg},
    "ocn_064_hhi_3y_chg":                   {"inputs": ["hhi"],                                                              "func": ocn_064_hhi_3y_chg},
    "ocn_065_hhi_qoq_pct_chg":              {"inputs": ["hhi"],                                                              "func": ocn_065_hhi_qoq_pct_chg},
    "ocn_066_hhi_yoy_pct_chg":              {"inputs": ["hhi"],                                                              "func": ocn_066_hhi_yoy_pct_chg},
    "ocn_067_hhi_accel_qoq":                {"inputs": ["hhi"],                                                              "func": ocn_067_hhi_accel_qoq},
    "ocn_068_hhi_slope_4q":                 {"inputs": ["hhi"],                                                              "func": ocn_068_hhi_slope_4q},
    "ocn_069_hhi_slope_8q":                 {"inputs": ["hhi"],                                                              "func": ocn_069_hhi_slope_8q},
    "ocn_070_hhi_ewm_vs_raw":               {"inputs": ["hhi"],                                                              "func": ocn_070_hhi_ewm_vs_raw},
    "ocn_071_avg_pos_vs_mean_ratio":         {"inputs": ["avg_position", "inst_shares", "inst_holders"],                      "func": ocn_071_avg_pos_vs_mean_ratio},
    "ocn_072_value_conc_top1":              {"inputs": ["top1_shares", "inst_shares", "inst_value"],                         "func": ocn_072_value_conc_top1},
    "ocn_073_value_conc_top1_ratio":        {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_073_value_conc_top1_ratio},
    "ocn_074_hhi_vs_top5_ratio_spread":     {"inputs": ["hhi", "top5_shares", "inst_shares"],                                "func": ocn_074_hhi_vs_top5_ratio_spread},
    "ocn_075_concentration_composite":      {"inputs": ["hhi", "top1_shares", "top5_shares", "inst_shares"],                 "func": ocn_075_concentration_composite},
    "ocn_151_hhi_3y_mean":                 {"inputs": ["hhi"],                                                              "func": ocn_151_hhi_3y_mean},
    "ocn_152_hhi_median_1y":               {"inputs": ["hhi"],                                                              "func": ocn_152_hhi_median_1y},
    "ocn_153_hhi_median_2y":               {"inputs": ["hhi"],                                                              "func": ocn_153_hhi_median_2y},
    "ocn_154_hhi_vs_median_1y":            {"inputs": ["hhi"],                                                              "func": ocn_154_hhi_vs_median_1y},
    "ocn_155_hhi_ewm_vs_3y_mean":          {"inputs": ["hhi"],                                                              "func": ocn_155_hhi_ewm_vs_3y_mean},
    "ocn_156_hhi_2q_chg":                  {"inputs": ["hhi"],                                                              "func": ocn_156_hhi_2q_chg},
    "ocn_157_hhi_2q_pct_chg":              {"inputs": ["hhi"],                                                              "func": ocn_157_hhi_2q_pct_chg},
    "ocn_158_hhi_3q_chg":                  {"inputs": ["hhi"],                                                              "func": ocn_158_hhi_3q_chg},
    "ocn_159_hhi_ewm_52w":                 {"inputs": ["hhi"],                                                              "func": ocn_159_hhi_ewm_52w},
    "ocn_160_hhi_max_vs_min_ratio_1y":     {"inputs": ["hhi"],                                                              "func": ocn_160_hhi_max_vs_min_ratio_1y},
    "ocn_161_top1_conc_median_1y":         {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_161_top1_conc_median_1y},
    "ocn_162_top1_conc_vs_median_1y":      {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_162_top1_conc_vs_median_1y},
    "ocn_163_top5_conc_median_1y":         {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_163_top5_conc_median_1y},
    "ocn_164_top5_conc_vs_median_1y":      {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_164_top5_conc_vs_median_1y},
    "ocn_165_top10_conc_median_1y":        {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_165_top10_conc_median_1y},
    "ocn_166_top5_to_inst_ewm_vs_raw":     {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_166_top5_to_inst_ewm_vs_raw},
    "ocn_167_hhi_slope_2q":                {"inputs": ["hhi"],                                                              "func": ocn_167_hhi_slope_2q},
    "ocn_168_top1_conc_range_1y":          {"inputs": ["top1_shares", "inst_shares"],                                       "func": ocn_168_top1_conc_range_1y},
    "ocn_169_top5_conc_range_1y":          {"inputs": ["top5_shares", "inst_shares"],                                       "func": ocn_169_top5_conc_range_1y},
    "ocn_170_top10_conc_range_1y":         {"inputs": ["top10_shares", "inst_shares"],                                      "func": ocn_170_top10_conc_range_1y},
    "ocn_171_inst_holders_zscore_1y":      {"inputs": ["inst_holders"],                                                     "func": ocn_171_inst_holders_zscore_1y},
    "ocn_172_inst_holders_rank_1y":        {"inputs": ["inst_holders"],                                                     "func": ocn_172_inst_holders_rank_1y},
    "ocn_173_inst_holders_yoy_chg":        {"inputs": ["inst_holders"],                                                     "func": ocn_173_inst_holders_yoy_chg},
    "ocn_174_inst_holders_qoq_chg":        {"inputs": ["inst_holders"],                                                     "func": ocn_174_inst_holders_qoq_chg},
    "ocn_175_hhi_x_holder_count":          {"inputs": ["hhi", "inst_holders"],                                              "func": ocn_175_hhi_x_holder_count},
}
