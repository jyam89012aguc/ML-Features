"""
92_ownership_concentration — Extended Features 001-075
=======================================================
Domain: SHAPE and CONCENTRATION of the institutional holdings distribution —
additional variants NOT covered by the four base files. Explores new horizons
(3-quarter, 3-year), de-concentration / fragmentation signals, incremental
tranche shares (holders 2-5, 6-10), effective-N dynamics, concentration
streaks and drawdown depth, decay-weighted concentration, and cross-tranche
composite distress scores.

Asset class: US equities | Sharadar SF3 13-F snapshots (quarterly -> daily).

Quarterly -> Daily Alignment Contract
--------------------------------------
All input Series arrive as *daily* pandas Series whose values have been
forward-filled from quarterly SF3 snapshots. Values change ~4 times per year;
rolling windows shorter than 63 trading days will see flat stretches.

Input fields:
    hhi, top1_shares, top5_shares, top10_shares,
    inst_shares, inst_holders, inst_value, avg_position

Trading-day constants: 1q=63, 2q=126, 3q=189, 1y=252, 2y=504, 3y=756.
All features are backward-looking only; no forward information.
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
_TD_3Q   = 189
_EPS     = 1e-9

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


def _align_quarterly_to_daily(s: pd.Series) -> pd.Series:
    """Forward-fill a quarterly Series to a daily index (idempotent if daily)."""
    return s.ffill()


def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    """Element-wise a / b; NaN where b is zero or NaN."""
    return a / b.replace(0, np.nan)


def _safe_div_abs(a: pd.Series, b: pd.Series) -> pd.Series:
    """Element-wise a / |b|; NaN where |b| is zero or NaN."""
    return a / b.abs().replace(0, np.nan)


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
    return s.rolling(w, min_periods=2).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=1).mean()


def _consec_increase_streak(s: pd.Series, lag: int) -> pd.Series:
    """Count of consecutive observations where s rose vs `lag` rows prior."""
    diff = s - s.shift(lag)
    rising = (diff > 0).astype(int)
    result = rising.astype(float).copy()
    count = 0.0
    for i in range(len(result)):
        if rising.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def _top1_ratio(top1_shares: pd.Series, inst_shares: pd.Series) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(inst_shares))


def _top5_ratio(top5_shares: pd.Series, inst_shares: pd.Series) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top5_shares),
                     _align_quarterly_to_daily(inst_shares))


def _top10_ratio(top10_shares: pd.Series, inst_shares: pd.Series) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top10_shares),
                     _align_quarterly_to_daily(inst_shares))


# ===========================================================================
# Features 001-075
# ===========================================================================

# --- Group A (001-014): Additional HHI horizons and de-concentration signals ---

def ocn_ext_001_hhi_3q_chg(hhi: pd.Series) -> pd.Series:
    """3-quarter change in HHI."""
    h = _align_quarterly_to_daily(hhi)
    return h - h.shift(_TD_3Q)


def ocn_ext_002_hhi_3q_pct_chg(hhi: pd.Series) -> pd.Series:
    """3-quarter percentage change in HHI."""
    h = _align_quarterly_to_daily(hhi)
    return _safe_div_abs(h - h.shift(_TD_3Q), h.shift(_TD_3Q))


def ocn_ext_003_hhi_zscore_3y(hhi: pd.Series) -> pd.Series:
    """Z-score of HHI over a 3-year rolling window."""
    return _zscore_rolling(_align_quarterly_to_daily(hhi), _TD_3Y)


def ocn_ext_004_hhi_rank_3y(hhi: pd.Series) -> pd.Series:
    """Percentile rank of HHI over a 3-year rolling window."""
    return _rolling_rank_pct(_align_quarterly_to_daily(hhi), _TD_3Y)


def ocn_ext_005_hhi_3q_mean(hhi: pd.Series) -> pd.Series:
    """3-quarter rolling mean of HHI."""
    return _rolling_mean(_align_quarterly_to_daily(hhi), _TD_3Q)


def ocn_ext_006_hhi_pct_from_2y_max(hhi: pd.Series) -> pd.Series:
    """HHI as % drawdown from its 2-year rolling max (de-concentration depth)."""
    h = _align_quarterly_to_daily(hhi)
    mx = _rolling_max(h, _TD_2Y)
    return _safe_div(h - mx, mx.abs())


def ocn_ext_007_hhi_pct_from_2y_min(hhi: pd.Series) -> pd.Series:
    """HHI as % above its 2-year rolling min (concentration build-up)."""
    h = _align_quarterly_to_daily(hhi)
    mn = _rolling_min(h, _TD_2Y)
    return _safe_div(h - mn, mn.abs())


def ocn_ext_008_hhi_drawdown_from_peak(hhi: pd.Series) -> pd.Series:
    """HHI drawdown from expanding historical maximum (de-concentration)."""
    h = _align_quarterly_to_daily(hhi)
    peak = h.expanding(min_periods=1).max()
    return _safe_div(h - peak, peak.abs())


def ocn_ext_009_hhi_3y_range(hhi: pd.Series) -> pd.Series:
    """3-year range (max minus min) of HHI."""
    h = _align_quarterly_to_daily(hhi)
    return _rolling_max(h, _TD_3Y) - _rolling_min(h, _TD_3Y)


def ocn_ext_010_hhi_expanding_pct_rank(hhi: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of HHI."""
    return _align_quarterly_to_daily(hhi).expanding(min_periods=2).rank(pct=True)


def ocn_ext_011_hhi_2y_cv(hhi: pd.Series) -> pd.Series:
    """Coefficient of variation of HHI over a 2-year rolling window."""
    h = _align_quarterly_to_daily(hhi)
    return _safe_div(_rolling_std(h, _TD_2Y), _rolling_mean(h, _TD_2Y).abs())


def ocn_ext_012_hhi_3y_std(hhi: pd.Series) -> pd.Series:
    """3-year rolling standard deviation of HHI."""
    return _rolling_std(_align_quarterly_to_daily(hhi), _TD_3Y)


def ocn_ext_013_hhi_qoq_diff_zscore_2y(hhi: pd.Series) -> pd.Series:
    """Z-score of the QoQ HHI change within a 2-year window (shift signal-to-noise)."""
    h = _align_quarterly_to_daily(hhi)
    return _zscore_rolling(h - h.shift(_TD_QTR), _TD_2Y)


def ocn_ext_014_hhi_below_1y_mean_flag(hhi: pd.Series) -> pd.Series:
    """Binary: 1 if HHI is below its 1-year rolling mean (loosening grip)."""
    h = _align_quarterly_to_daily(hhi)
    return (h < _rolling_mean(h, _TD_YEAR)).astype(float)


# --- Group B (015-028): Effective-N dynamics and fragmentation metrics ---

def ocn_ext_015_eff_n_3q_change(hhi: pd.Series) -> pd.Series:
    """3-quarter change in effective number of holders (1/HHI)."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return eff - eff.shift(_TD_3Q)


def ocn_ext_016_eff_n_3y_change(hhi: pd.Series) -> pd.Series:
    """3-year change in effective number of holders."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return eff - eff.shift(_TD_3Y)


def ocn_ext_017_eff_n_zscore_2y(hhi: pd.Series) -> pd.Series:
    """Z-score of effective number of holders over a 2-year window."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return _zscore_rolling(eff, _TD_2Y)


def ocn_ext_018_eff_n_rank_2y(hhi: pd.Series) -> pd.Series:
    """Percentile rank of effective number of holders over a 2-year window."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return _rolling_rank_pct(eff, _TD_2Y)


def ocn_ext_019_eff_n_pct_from_2y_max(hhi: pd.Series) -> pd.Series:
    """Effective-N as % drawdown from its 2-year rolling max (fragmentation loss)."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    mx = _rolling_max(eff, _TD_2Y)
    return _safe_div(eff - mx, mx.abs())


def ocn_ext_020_eff_n_2y_mean(hhi: pd.Series) -> pd.Series:
    """2-year rolling mean of effective number of holders."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return _rolling_mean(eff, _TD_2Y)


def ocn_ext_021_eff_n_ewm_1y(hhi: pd.Series) -> pd.Series:
    """EWM (span=252) of effective number of holders."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return _ewm_mean(eff, _TD_YEAR)


def ocn_ext_022_eff_n_qoq_pct_chg(hhi: pd.Series) -> pd.Series:
    """QoQ percentage change in effective number of holders."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return _safe_div_abs(eff - eff.shift(_TD_QTR), eff.shift(_TD_QTR))


def ocn_ext_023_inv_eff_n_concentration(hhi: pd.Series, inst_holders: pd.Series) -> pd.Series:
    """Fragmentation gap: actual holders minus effective-N (uneven distribution gap)."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return _align_quarterly_to_daily(inst_holders) - eff


def ocn_ext_024_eff_n_below_1y_mean_streak(hhi: pd.Series) -> pd.Series:
    """Count of consecutive days effective-N is below its 1-year rolling mean."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    below = (eff < _rolling_mean(eff, _TD_YEAR)).astype(int)
    result = below.astype(float).copy()
    count = 0.0
    for i in range(len(result)):
        if below.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def ocn_ext_025_eff_n_drawdown_from_peak(hhi: pd.Series) -> pd.Series:
    """Effective-N drawdown from expanding historical maximum."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    peak = eff.expanding(min_periods=1).max()
    return _safe_div(eff - peak, peak.abs())


def ocn_ext_026_eff_n_per_holder(hhi: pd.Series, inst_holders: pd.Series) -> pd.Series:
    """Effective-N expressed as a fraction of actual holders, QoQ change."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    frac = _safe_div(eff, _align_quarterly_to_daily(inst_holders))
    return frac - frac.shift(_TD_QTR)


def ocn_ext_027_eff_n_2y_range(hhi: pd.Series) -> pd.Series:
    """2-year range (max minus min) of effective number of holders."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return _rolling_max(eff, _TD_2Y) - _rolling_min(eff, _TD_2Y)


def ocn_ext_028_eff_n_yoy_pct_chg(hhi: pd.Series) -> pd.Series:
    """YoY percentage change in effective number of holders."""
    eff = _safe_div(pd.Series(1.0, index=hhi.index), _align_quarterly_to_daily(hhi))
    return _safe_div_abs(eff - eff.shift(_TD_YEAR), eff.shift(_TD_YEAR))


# --- Group C (029-042): Incremental tranche shares and step-spread variants ---

def ocn_ext_029_holders_2to5_share(top1_shares: pd.Series,
                                   top5_shares: pd.Series,
                                   inst_shares: pd.Series) -> pd.Series:
    """Share of inst_shares held by holders ranked 2-5: (top5-top1)/inst_shares."""
    t1 = _align_quarterly_to_daily(top1_shares)
    t5 = _align_quarterly_to_daily(top5_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div((t5 - t1).clip(lower=0), ins)


def ocn_ext_030_holders_6to10_share(top5_shares: pd.Series,
                                    top10_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """Share of inst_shares held by holders ranked 6-10: (top10-top5)/inst_shares."""
    t5 = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div((t10 - t5).clip(lower=0), ins)


def ocn_ext_031_holders_2to5_share_qoq_chg(top1_shares: pd.Series,
                                           top5_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the holders-2-to-5 share of institutional shares."""
    t1 = _align_quarterly_to_daily(top1_shares)
    t5 = _align_quarterly_to_daily(top5_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    r = _safe_div((t5 - t1).clip(lower=0), ins)
    return r - r.shift(_TD_QTR)


def ocn_ext_032_holders_6to10_share_qoq_chg(top5_shares: pd.Series,
                                            top10_shares: pd.Series,
                                            inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the holders-6-to-10 share of institutional shares."""
    t5 = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    r = _safe_div((t10 - t5).clip(lower=0), ins)
    return r - r.shift(_TD_QTR)


def ocn_ext_033_top1_to_top10_ratio(top1_shares: pd.Series,
                                    top10_shares: pd.Series) -> pd.Series:
    """Top-1 shares divided by top-10 shares (apex dominance within the top tier)."""
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(top10_shares))


def ocn_ext_034_top1_to_top10_ratio_qoq_chg(top1_shares: pd.Series,
                                            top10_shares: pd.Series) -> pd.Series:
    """QoQ change in the top-1 / top-10 shares ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(top10_shares))
    return r - r.shift(_TD_QTR)


def ocn_ext_035_top1_share_of_top5(top1_shares: pd.Series,
                                   top5_shares: pd.Series) -> pd.Series:
    """Top-1 shares as a fraction of top-5 shares (apex share of the top-5 block)."""
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(top5_shares))


def ocn_ext_036_top5_share_of_top10(top5_shares: pd.Series,
                                    top10_shares: pd.Series) -> pd.Series:
    """Top-5 shares as a fraction of top-10 shares (upper-half share of top-10)."""
    return _safe_div(_align_quarterly_to_daily(top5_shares),
                     _align_quarterly_to_daily(top10_shares))


def ocn_ext_037_tranche_step_2to5_vs_6to10(top1_shares: pd.Series,
                                           top5_shares: pd.Series,
                                           top10_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """Difference between the holders-2-5 share and the holders-6-10 share."""
    t1 = _align_quarterly_to_daily(top1_shares)
    t5 = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    s2to5 = _safe_div((t5 - t1).clip(lower=0), ins)
    s6to10 = _safe_div((t10 - t5).clip(lower=0), ins)
    return s2to5 - s6to10


def ocn_ext_038_outside_top10_share_qoq_chg(top10_shares: pd.Series,
                                            inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the fraction of institutional shares held outside the top-10."""
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    outside = _safe_div((ins - t10).clip(lower=0), ins)
    return outside - outside.shift(_TD_QTR)


def ocn_ext_039_outside_top10_share_rank_1y(top10_shares: pd.Series,
                                            inst_shares: pd.Series) -> pd.Series:
    """1-year percentile rank of the fraction held outside the top-10."""
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    outside = _safe_div((ins - t10).clip(lower=0), ins)
    return _rolling_rank_pct(outside, _TD_YEAR)


def ocn_ext_040_top1_to_top10_ratio_zscore_1y(top1_shares: pd.Series,
                                              top10_shares: pd.Series) -> pd.Series:
    """1-year z-score of the top-1 / top-10 shares ratio."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(top10_shares))
    return _zscore_rolling(r, _TD_YEAR)


def ocn_ext_041_top1_share_of_top5_yoy_chg(top1_shares: pd.Series,
                                           top5_shares: pd.Series) -> pd.Series:
    """YoY change in the top-1 share of the top-5 block."""
    r = _safe_div(_align_quarterly_to_daily(top1_shares),
                  _align_quarterly_to_daily(top5_shares))
    return r - r.shift(_TD_YEAR)


def ocn_ext_042_holders_6to10_share_zscore_1y(top5_shares: pd.Series,
                                              top10_shares: pd.Series,
                                              inst_shares: pd.Series) -> pd.Series:
    """1-year z-score of the holders-6-to-10 share of institutional shares."""
    t5 = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    r = _safe_div((t10 - t5).clip(lower=0), ins)
    return _zscore_rolling(r, _TD_YEAR)


# --- Group D (043-056): Concentration-ratio horizons, ranks and drawdowns ---

def ocn_ext_043_top1_conc_ratio_3q_chg(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """3-quarter change in the top-1 concentration ratio."""
    r = _top1_ratio(top1_shares, inst_shares)
    return r - r.shift(_TD_3Q)


def ocn_ext_044_top5_conc_ratio_3q_chg(top5_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """3-quarter change in the top-5 concentration ratio."""
    r = _top5_ratio(top5_shares, inst_shares)
    return r - r.shift(_TD_3Q)


def ocn_ext_045_top10_conc_ratio_3q_chg(top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """3-quarter change in the top-10 concentration ratio."""
    r = _top10_ratio(top10_shares, inst_shares)
    return r - r.shift(_TD_3Q)


def ocn_ext_046_top1_conc_ratio_3y_chg(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """3-year change in the top-1 concentration ratio."""
    r = _top1_ratio(top1_shares, inst_shares)
    return r - r.shift(_TD_3Y)


def ocn_ext_047_top1_conc_ratio_rank_3y(top1_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """3-year percentile rank of the top-1 concentration ratio."""
    return _rolling_rank_pct(_top1_ratio(top1_shares, inst_shares), _TD_3Y)


def ocn_ext_048_top5_conc_ratio_rank_3y(top5_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """3-year percentile rank of the top-5 concentration ratio."""
    return _rolling_rank_pct(_top5_ratio(top5_shares, inst_shares), _TD_3Y)


def ocn_ext_049_top1_conc_ratio_zscore_3y(top1_shares: pd.Series,
                                          inst_shares: pd.Series) -> pd.Series:
    """3-year z-score of the top-1 concentration ratio."""
    return _zscore_rolling(_top1_ratio(top1_shares, inst_shares), _TD_3Y)


def ocn_ext_050_top10_conc_ratio_zscore_3y(top10_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """3-year z-score of the top-10 concentration ratio."""
    return _zscore_rolling(_top10_ratio(top10_shares, inst_shares), _TD_3Y)


def ocn_ext_051_top1_conc_ratio_pct_from_2y_max(top1_shares: pd.Series,
                                                inst_shares: pd.Series) -> pd.Series:
    """Top-1 concentration ratio as % drawdown from its 2-year rolling max."""
    r = _top1_ratio(top1_shares, inst_shares)
    mx = _rolling_max(r, _TD_2Y)
    return _safe_div(r - mx, mx.abs())


def ocn_ext_052_top5_conc_ratio_pct_from_2y_max(top5_shares: pd.Series,
                                                inst_shares: pd.Series) -> pd.Series:
    """Top-5 concentration ratio as % drawdown from its 2-year rolling max."""
    r = _top5_ratio(top5_shares, inst_shares)
    mx = _rolling_max(r, _TD_2Y)
    return _safe_div(r - mx, mx.abs())


def ocn_ext_053_top10_conc_ratio_drawdown_from_peak(top10_shares: pd.Series,
                                                    inst_shares: pd.Series) -> pd.Series:
    """Top-10 concentration ratio drawdown from expanding historical maximum."""
    r = _top10_ratio(top10_shares, inst_shares)
    peak = r.expanding(min_periods=1).max()
    return _safe_div(r - peak, peak.abs())


def ocn_ext_054_top1_conc_ratio_3y_range(top1_shares: pd.Series,
                                         inst_shares: pd.Series) -> pd.Series:
    """3-year range (max minus min) of the top-1 concentration ratio."""
    r = _top1_ratio(top1_shares, inst_shares)
    return _rolling_max(r, _TD_3Y) - _rolling_min(r, _TD_3Y)


def ocn_ext_055_top5_conc_ratio_2y_cv(top5_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """Coefficient of variation of the top-5 concentration ratio over 2 years."""
    r = _top5_ratio(top5_shares, inst_shares)
    return _safe_div(_rolling_std(r, _TD_2Y), _rolling_mean(r, _TD_2Y).abs())


def ocn_ext_056_top1_conc_ratio_expanding_rank(top1_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of the top-1 concentration ratio."""
    return _top1_ratio(top1_shares, inst_shares).expanding(min_periods=2).rank(pct=True)


# --- Group E (057-066): Concentration streaks and decay-weighted signals ---

def ocn_ext_057_consec_hhi_rises_qoq(hhi: pd.Series) -> pd.Series:
    """Count of consecutive QoQ-rising observations in HHI (concentration build)."""
    return _consec_increase_streak(_align_quarterly_to_daily(hhi), _TD_QTR)


def ocn_ext_058_consec_top1_conc_rises_qoq(top1_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """Count of consecutive QoQ-rising observations in the top-1 concentration ratio."""
    return _consec_increase_streak(_top1_ratio(top1_shares, inst_shares), _TD_QTR)


def ocn_ext_059_hhi_above_1y_mean_streak(hhi: pd.Series) -> pd.Series:
    """Count of consecutive days HHI is above its 1-year rolling mean."""
    h = _align_quarterly_to_daily(hhi)
    above = (h > _rolling_mean(h, _TD_YEAR)).astype(int)
    result = above.astype(float).copy()
    count = 0.0
    for i in range(len(result)):
        if above.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def ocn_ext_060_hhi_above_1y_mean_frac_2y(hhi: pd.Series) -> pd.Series:
    """Fraction of last 504 days HHI was above its 1-year rolling mean."""
    h = _align_quarterly_to_daily(hhi)
    above = (h > _rolling_mean(h, _TD_YEAR)).astype(float)
    return _rolling_mean(above, _TD_2Y)


def ocn_ext_061_hhi_ewm_126(hhi: pd.Series) -> pd.Series:
    """26-week EWM (span=126) of HHI."""
    return _ewm_mean(_align_quarterly_to_daily(hhi), _TD_2Q)


def ocn_ext_062_hhi_ewm_ratio_1y(hhi: pd.Series) -> pd.Series:
    """Ratio of HHI to its EWM (span=252); above 1 = above the smoothed trend."""
    h = _align_quarterly_to_daily(hhi)
    return _safe_div(h, _ewm_mean(h, _TD_YEAR))


def ocn_ext_063_top1_conc_ratio_ewm_dev(top1_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """Top-1 concentration ratio minus its EWM (span=252)."""
    r = _top1_ratio(top1_shares, inst_shares)
    return r - _ewm_mean(r, _TD_YEAR)


def ocn_ext_064_top5_conc_ratio_ewm_dev(top5_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """Top-5 concentration ratio minus its EWM (span=252)."""
    r = _top5_ratio(top5_shares, inst_shares)
    return r - _ewm_mean(r, _TD_YEAR)


def ocn_ext_065_hhi_ewm_short_minus_long(hhi: pd.Series) -> pd.Series:
    """Short minus long EWM of HHI (span=63 minus span=252) — concentration momentum."""
    h = _align_quarterly_to_daily(hhi)
    return _ewm_mean(h, _TD_QTR) - _ewm_mean(h, _TD_YEAR)


def ocn_ext_066_hhi_qoq_chg_ewm(hhi: pd.Series) -> pd.Series:
    """EWM (span=126) of the QoQ HHI change — smoothed concentration drift."""
    h = _align_quarterly_to_daily(hhi)
    return _ewm_mean(h - h.shift(_TD_QTR), _TD_2Q)


# --- Group F (067-075): Cross-series and composite concentration distress ---

def ocn_ext_067_avg_position_qoq_pct(avg_position: pd.Series) -> pd.Series:
    """QoQ percentage change in the mean shares-per-holder."""
    a = _align_quarterly_to_daily(avg_position)
    return _safe_div_abs(a - a.shift(_TD_QTR), a.shift(_TD_QTR))


def ocn_ext_068_avg_position_zscore_1y(avg_position: pd.Series) -> pd.Series:
    """1-year z-score of the mean shares-per-holder."""
    return _zscore_rolling(_align_quarterly_to_daily(avg_position), _TD_YEAR)


def ocn_ext_069_avg_position_rank_2y(avg_position: pd.Series) -> pd.Series:
    """2-year percentile rank of the mean shares-per-holder."""
    return _rolling_rank_pct(_align_quarterly_to_daily(avg_position), _TD_2Y)


def ocn_ext_070_hhi_to_eff_n_pct_product(hhi: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """HHI multiplied by holder count, QoQ change (joint concentration-breadth drift)."""
    h = _align_quarterly_to_daily(hhi)
    n = _align_quarterly_to_daily(inst_holders)
    prod = h * n
    return prod - prod.shift(_TD_QTR)


def ocn_ext_071_value_conc_top1_qoq_pct(top1_shares: pd.Series,
                                        inst_shares: pd.Series,
                                        inst_value: pd.Series) -> pd.Series:
    """QoQ % change in the estimated USD value held by the top-1 holder."""
    share_frac = _top1_ratio(top1_shares, inst_shares)
    val = _align_quarterly_to_daily(inst_value)
    top1_val = share_frac * val
    return _safe_div_abs(top1_val - top1_val.shift(_TD_QTR), top1_val.shift(_TD_QTR))


def ocn_ext_072_hhi_minus_top1_ratio_sq(hhi: pd.Series,
                                        top1_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """HHI minus the squared top-1 concentration ratio (tail-concentration residual)."""
    h = _align_quarterly_to_daily(hhi)
    r1 = _top1_ratio(top1_shares, inst_shares)
    return h - r1 ** 2


def ocn_ext_073_concentration_change_composite(hhi: pd.Series,
                                               top1_shares: pd.Series,
                                               top5_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """Average of the QoQ changes in HHI, top-1 ratio and top-5 ratio."""
    h = _align_quarterly_to_daily(hhi)
    r1 = _top1_ratio(top1_shares, inst_shares)
    r5 = _top5_ratio(top5_shares, inst_shares)
    d_h = h - h.shift(_TD_QTR)
    d_1 = r1 - r1.shift(_TD_QTR)
    d_5 = r5 - r5.shift(_TD_QTR)
    return (d_h + d_1 + d_5) / 3.0


def ocn_ext_074_deconcentration_count(hhi: pd.Series,
                                      top1_shares: pd.Series,
                                      top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """Count of HHI, top-1, top-5 and top-10 ratios with a negative QoQ change (0-4)."""
    h = _align_quarterly_to_daily(hhi)
    series = [
        h,
        _top1_ratio(top1_shares, inst_shares),
        _top5_ratio(top5_shares, inst_shares),
        _top10_ratio(top10_shares, inst_shares),
    ]
    flags = [(x - x.shift(_TD_QTR) < 0).astype(float) for x in series]
    result = flags[0]
    for f in flags[1:]:
        result = result + f
    return result


def ocn_ext_075_concentration_distress_score(hhi: pd.Series,
                                             top1_shares: pd.Series,
                                             top5_shares: pd.Series,
                                             inst_shares: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """
    Concentration-distress score combining four normalized signals (each ~0-1):
      - HHI 2-year percentile rank (extreme concentration)
      - top-1 concentration ratio 2-year percentile rank
      - top-5 concentration ratio 2-year percentile rank
      - 1 minus the 2-year percentile rank of holder count (thin breadth)
    Average of the four; higher = a thinly-held, apex-concentrated structure.
    """
    h = _align_quarterly_to_daily(hhi)
    n = _align_quarterly_to_daily(inst_holders)
    hhi_rank = _rolling_rank_pct(h, _TD_2Y)
    t1_rank = _rolling_rank_pct(_top1_ratio(top1_shares, inst_shares), _TD_2Y)
    t5_rank = _rolling_rank_pct(_top5_ratio(top5_shares, inst_shares), _TD_2Y)
    breadth_rank = _rolling_rank_pct(n, _TD_2Y)
    return (hhi_rank.fillna(0.5) + t1_rank.fillna(0.5)
            + t5_rank.fillna(0.5) + (1.0 - breadth_rank.fillna(0.5))) / 4.0


# ===========================================================================
# Registry
# ===========================================================================
OWNERSHIP_CONCENTRATION_EXTENDED_REGISTRY_001_075 = {
    "ocn_ext_001_hhi_3q_chg":                      {"inputs": ["hhi"],                                                       "func": ocn_ext_001_hhi_3q_chg},
    "ocn_ext_002_hhi_3q_pct_chg":                  {"inputs": ["hhi"],                                                       "func": ocn_ext_002_hhi_3q_pct_chg},
    "ocn_ext_003_hhi_zscore_3y":                   {"inputs": ["hhi"],                                                       "func": ocn_ext_003_hhi_zscore_3y},
    "ocn_ext_004_hhi_rank_3y":                     {"inputs": ["hhi"],                                                       "func": ocn_ext_004_hhi_rank_3y},
    "ocn_ext_005_hhi_3q_mean":                     {"inputs": ["hhi"],                                                       "func": ocn_ext_005_hhi_3q_mean},
    "ocn_ext_006_hhi_pct_from_2y_max":             {"inputs": ["hhi"],                                                       "func": ocn_ext_006_hhi_pct_from_2y_max},
    "ocn_ext_007_hhi_pct_from_2y_min":             {"inputs": ["hhi"],                                                       "func": ocn_ext_007_hhi_pct_from_2y_min},
    "ocn_ext_008_hhi_drawdown_from_peak":          {"inputs": ["hhi"],                                                       "func": ocn_ext_008_hhi_drawdown_from_peak},
    "ocn_ext_009_hhi_3y_range":                    {"inputs": ["hhi"],                                                       "func": ocn_ext_009_hhi_3y_range},
    "ocn_ext_010_hhi_expanding_pct_rank":          {"inputs": ["hhi"],                                                       "func": ocn_ext_010_hhi_expanding_pct_rank},
    "ocn_ext_011_hhi_2y_cv":                       {"inputs": ["hhi"],                                                       "func": ocn_ext_011_hhi_2y_cv},
    "ocn_ext_012_hhi_3y_std":                      {"inputs": ["hhi"],                                                       "func": ocn_ext_012_hhi_3y_std},
    "ocn_ext_013_hhi_qoq_diff_zscore_2y":          {"inputs": ["hhi"],                                                       "func": ocn_ext_013_hhi_qoq_diff_zscore_2y},
    "ocn_ext_014_hhi_below_1y_mean_flag":          {"inputs": ["hhi"],                                                       "func": ocn_ext_014_hhi_below_1y_mean_flag},
    "ocn_ext_015_eff_n_3q_change":                 {"inputs": ["hhi"],                                                       "func": ocn_ext_015_eff_n_3q_change},
    "ocn_ext_016_eff_n_3y_change":                 {"inputs": ["hhi"],                                                       "func": ocn_ext_016_eff_n_3y_change},
    "ocn_ext_017_eff_n_zscore_2y":                 {"inputs": ["hhi"],                                                       "func": ocn_ext_017_eff_n_zscore_2y},
    "ocn_ext_018_eff_n_rank_2y":                   {"inputs": ["hhi"],                                                       "func": ocn_ext_018_eff_n_rank_2y},
    "ocn_ext_019_eff_n_pct_from_2y_max":           {"inputs": ["hhi"],                                                       "func": ocn_ext_019_eff_n_pct_from_2y_max},
    "ocn_ext_020_eff_n_2y_mean":                   {"inputs": ["hhi"],                                                       "func": ocn_ext_020_eff_n_2y_mean},
    "ocn_ext_021_eff_n_ewm_1y":                    {"inputs": ["hhi"],                                                       "func": ocn_ext_021_eff_n_ewm_1y},
    "ocn_ext_022_eff_n_qoq_pct_chg":               {"inputs": ["hhi"],                                                       "func": ocn_ext_022_eff_n_qoq_pct_chg},
    "ocn_ext_023_inv_eff_n_concentration":         {"inputs": ["hhi", "inst_holders"],                                       "func": ocn_ext_023_inv_eff_n_concentration},
    "ocn_ext_024_eff_n_below_1y_mean_streak":      {"inputs": ["hhi"],                                                       "func": ocn_ext_024_eff_n_below_1y_mean_streak},
    "ocn_ext_025_eff_n_drawdown_from_peak":        {"inputs": ["hhi"],                                                       "func": ocn_ext_025_eff_n_drawdown_from_peak},
    "ocn_ext_026_eff_n_per_holder":                {"inputs": ["hhi", "inst_holders"],                                       "func": ocn_ext_026_eff_n_per_holder},
    "ocn_ext_027_eff_n_2y_range":                  {"inputs": ["hhi"],                                                       "func": ocn_ext_027_eff_n_2y_range},
    "ocn_ext_028_eff_n_yoy_pct_chg":               {"inputs": ["hhi"],                                                       "func": ocn_ext_028_eff_n_yoy_pct_chg},
    "ocn_ext_029_holders_2to5_share":              {"inputs": ["top1_shares", "top5_shares", "inst_shares"],                 "func": ocn_ext_029_holders_2to5_share},
    "ocn_ext_030_holders_6to10_share":             {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                "func": ocn_ext_030_holders_6to10_share},
    "ocn_ext_031_holders_2to5_share_qoq_chg":      {"inputs": ["top1_shares", "top5_shares", "inst_shares"],                 "func": ocn_ext_031_holders_2to5_share_qoq_chg},
    "ocn_ext_032_holders_6to10_share_qoq_chg":     {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                "func": ocn_ext_032_holders_6to10_share_qoq_chg},
    "ocn_ext_033_top1_to_top10_ratio":             {"inputs": ["top1_shares", "top10_shares"],                               "func": ocn_ext_033_top1_to_top10_ratio},
    "ocn_ext_034_top1_to_top10_ratio_qoq_chg":     {"inputs": ["top1_shares", "top10_shares"],                               "func": ocn_ext_034_top1_to_top10_ratio_qoq_chg},
    "ocn_ext_035_top1_share_of_top5":              {"inputs": ["top1_shares", "top5_shares"],                                "func": ocn_ext_035_top1_share_of_top5},
    "ocn_ext_036_top5_share_of_top10":             {"inputs": ["top5_shares", "top10_shares"],                               "func": ocn_ext_036_top5_share_of_top10},
    "ocn_ext_037_tranche_step_2to5_vs_6to10":      {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"], "func": ocn_ext_037_tranche_step_2to5_vs_6to10},
    "ocn_ext_038_outside_top10_share_qoq_chg":     {"inputs": ["top10_shares", "inst_shares"],                               "func": ocn_ext_038_outside_top10_share_qoq_chg},
    "ocn_ext_039_outside_top10_share_rank_1y":     {"inputs": ["top10_shares", "inst_shares"],                               "func": ocn_ext_039_outside_top10_share_rank_1y},
    "ocn_ext_040_top1_to_top10_ratio_zscore_1y":   {"inputs": ["top1_shares", "top10_shares"],                               "func": ocn_ext_040_top1_to_top10_ratio_zscore_1y},
    "ocn_ext_041_top1_share_of_top5_yoy_chg":      {"inputs": ["top1_shares", "top5_shares"],                                "func": ocn_ext_041_top1_share_of_top5_yoy_chg},
    "ocn_ext_042_holders_6to10_share_zscore_1y":   {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                "func": ocn_ext_042_holders_6to10_share_zscore_1y},
    "ocn_ext_043_top1_conc_ratio_3q_chg":          {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_043_top1_conc_ratio_3q_chg},
    "ocn_ext_044_top5_conc_ratio_3q_chg":          {"inputs": ["top5_shares", "inst_shares"],                                "func": ocn_ext_044_top5_conc_ratio_3q_chg},
    "ocn_ext_045_top10_conc_ratio_3q_chg":         {"inputs": ["top10_shares", "inst_shares"],                               "func": ocn_ext_045_top10_conc_ratio_3q_chg},
    "ocn_ext_046_top1_conc_ratio_3y_chg":          {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_046_top1_conc_ratio_3y_chg},
    "ocn_ext_047_top1_conc_ratio_rank_3y":         {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_047_top1_conc_ratio_rank_3y},
    "ocn_ext_048_top5_conc_ratio_rank_3y":         {"inputs": ["top5_shares", "inst_shares"],                                "func": ocn_ext_048_top5_conc_ratio_rank_3y},
    "ocn_ext_049_top1_conc_ratio_zscore_3y":       {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_049_top1_conc_ratio_zscore_3y},
    "ocn_ext_050_top10_conc_ratio_zscore_3y":      {"inputs": ["top10_shares", "inst_shares"],                               "func": ocn_ext_050_top10_conc_ratio_zscore_3y},
    "ocn_ext_051_top1_conc_ratio_pct_from_2y_max": {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_051_top1_conc_ratio_pct_from_2y_max},
    "ocn_ext_052_top5_conc_ratio_pct_from_2y_max": {"inputs": ["top5_shares", "inst_shares"],                                "func": ocn_ext_052_top5_conc_ratio_pct_from_2y_max},
    "ocn_ext_053_top10_conc_ratio_drawdown_from_peak":{"inputs": ["top10_shares", "inst_shares"],                            "func": ocn_ext_053_top10_conc_ratio_drawdown_from_peak},
    "ocn_ext_054_top1_conc_ratio_3y_range":        {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_054_top1_conc_ratio_3y_range},
    "ocn_ext_055_top5_conc_ratio_2y_cv":           {"inputs": ["top5_shares", "inst_shares"],                                "func": ocn_ext_055_top5_conc_ratio_2y_cv},
    "ocn_ext_056_top1_conc_ratio_expanding_rank":  {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_056_top1_conc_ratio_expanding_rank},
    "ocn_ext_057_consec_hhi_rises_qoq":            {"inputs": ["hhi"],                                                       "func": ocn_ext_057_consec_hhi_rises_qoq},
    "ocn_ext_058_consec_top1_conc_rises_qoq":      {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_058_consec_top1_conc_rises_qoq},
    "ocn_ext_059_hhi_above_1y_mean_streak":        {"inputs": ["hhi"],                                                       "func": ocn_ext_059_hhi_above_1y_mean_streak},
    "ocn_ext_060_hhi_above_1y_mean_frac_2y":       {"inputs": ["hhi"],                                                       "func": ocn_ext_060_hhi_above_1y_mean_frac_2y},
    "ocn_ext_061_hhi_ewm_126":                     {"inputs": ["hhi"],                                                       "func": ocn_ext_061_hhi_ewm_126},
    "ocn_ext_062_hhi_ewm_ratio_1y":                {"inputs": ["hhi"],                                                       "func": ocn_ext_062_hhi_ewm_ratio_1y},
    "ocn_ext_063_top1_conc_ratio_ewm_dev":         {"inputs": ["top1_shares", "inst_shares"],                                "func": ocn_ext_063_top1_conc_ratio_ewm_dev},
    "ocn_ext_064_top5_conc_ratio_ewm_dev":         {"inputs": ["top5_shares", "inst_shares"],                                "func": ocn_ext_064_top5_conc_ratio_ewm_dev},
    "ocn_ext_065_hhi_ewm_short_minus_long":        {"inputs": ["hhi"],                                                       "func": ocn_ext_065_hhi_ewm_short_minus_long},
    "ocn_ext_066_hhi_qoq_chg_ewm":                 {"inputs": ["hhi"],                                                       "func": ocn_ext_066_hhi_qoq_chg_ewm},
    "ocn_ext_067_avg_position_qoq_pct":            {"inputs": ["avg_position"],                                              "func": ocn_ext_067_avg_position_qoq_pct},
    "ocn_ext_068_avg_position_zscore_1y":          {"inputs": ["avg_position"],                                              "func": ocn_ext_068_avg_position_zscore_1y},
    "ocn_ext_069_avg_position_rank_2y":            {"inputs": ["avg_position"],                                              "func": ocn_ext_069_avg_position_rank_2y},
    "ocn_ext_070_hhi_to_eff_n_pct_product":        {"inputs": ["hhi", "inst_holders"],                                       "func": ocn_ext_070_hhi_to_eff_n_pct_product},
    "ocn_ext_071_value_conc_top1_qoq_pct":         {"inputs": ["top1_shares", "inst_shares", "inst_value"],                  "func": ocn_ext_071_value_conc_top1_qoq_pct},
    "ocn_ext_072_hhi_minus_top1_ratio_sq":         {"inputs": ["hhi", "top1_shares", "inst_shares"],                         "func": ocn_ext_072_hhi_minus_top1_ratio_sq},
    "ocn_ext_073_concentration_change_composite":  {"inputs": ["hhi", "top1_shares", "top5_shares", "inst_shares"],          "func": ocn_ext_073_concentration_change_composite},
    "ocn_ext_074_deconcentration_count":           {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"], "func": ocn_ext_074_deconcentration_count},
    "ocn_ext_075_concentration_distress_score":    {"inputs": ["hhi", "top1_shares", "top5_shares", "inst_shares", "inst_holders"], "func": ocn_ext_075_concentration_distress_score},
}
