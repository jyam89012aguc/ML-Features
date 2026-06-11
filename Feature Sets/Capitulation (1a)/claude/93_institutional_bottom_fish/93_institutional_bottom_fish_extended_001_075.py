"""
93_institutional_bottom_fish — Extended Features 001-075
Domain: Institutional accumulation at price lows ("bottom fishing") — additional
        variants: longer/shorter lookbacks, new thresholds, percentile ranks,
        streaks, EWM smoothing, holder-level intensity, composite distress scores.
Asset class: US equities | Sharadar SF3 13F institutional ownership (quarterly,
        forward-filled to a daily index).
All features are backward-looking only; no forward information.

These extended features do NOT duplicate base_001_075, base_076_150,
2nd_derivatives or 3rd_derivatives — they explore different windows, thresholds,
smoothing and composite angles within the same accumulation-at-lows domain.

QUARTERLY -> DAILY ALIGNMENT CONTRACT
-------------------------------------
SF3 13F ownership fields (new_positions, increased_positions, closed_positions,
decreased_positions, inst_holders, inst_shares, inst_value, inst_pct) are
reported quarterly and forward-filled to a daily index upstream. `_align_quarterly_to_daily`
documents this contract; alignment is performed by the pipeline before call.
`close` is a genuine daily price series used only to characterise drawdown.
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

def _align_quarterly_to_daily(series: pd.Series) -> pd.Series:
    """Forward-fill a quarterly snapshot series to a daily index (no-op if
    already ffilled by caller). Documents the alignment contract."""
    return series


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; zero denominator replaced with NaN."""
    return num / (den.replace(0, np.nan) + _EPS * (den == 0).astype(float))


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
    sd = _rolling_std(s, w).replace(0, np.nan)
    return (s - mu) / (sd + _EPS)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=1).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    grp = (~cond).cumsum()
    return c.groupby(grp).cumsum().astype(float)


def _proximity_to_trailing_low(close: pd.Series, window: int) -> pd.Series:
    """(close - trailing_low) / trailing_low >= 0; 0 = at the low."""
    trail_low = _rolling_min(close, window)
    return _safe_div(close - trail_low, trail_low)


def _drawdown_from_trailing_high(close: pd.Series, window: int) -> pd.Series:
    """(trailing_high - close) / trailing_high >= 0; 0 = at the high."""
    trail_high = _rolling_max(close, window)
    return _safe_div(trail_high - close, trail_high)


def _gross(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    return new_positions.fillna(0) + increased_positions.fillna(0)


def _net(new_positions, increased_positions, closed_positions, decreased_positions):
    adds = new_positions.fillna(0) + increased_positions.fillna(0)
    drops = closed_positions.fillna(0) + decreased_positions.fillna(0)
    return adds - drops


# ===========================================================================
# Extended Features 001 - 075
# ===========================================================================

# --- Group A (001-010): Half-year / 3-year drawdown-depth weighted accumulation ---

def ibf_ext_001_new_pos_at_6m_low(new_positions: pd.Series, close: pd.Series) -> pd.Series:
    """New positions weighted by 6-month (126td) drawdown depth."""
    prox = _proximity_to_trailing_low(close, _TD_2Q)
    return new_positions.fillna(0) * (1 - prox).clip(0, 1)


def ibf_ext_002_increased_pos_at_6m_low(increased_positions: pd.Series, close: pd.Series) -> pd.Series:
    """Increased positions weighted by 6-month drawdown depth."""
    prox = _proximity_to_trailing_low(close, _TD_2Q)
    return increased_positions.fillna(0) * (1 - prox).clip(0, 1)


def ibf_ext_003_gross_add_at_6m_low(new_positions: pd.Series, increased_positions: pd.Series,
                                     close: pd.Series) -> pd.Series:
    """Gross additions weighted by 6-month drawdown depth."""
    prox = _proximity_to_trailing_low(close, _TD_2Q)
    return _gross(new_positions, increased_positions) * (1 - prox).clip(0, 1)


def ibf_ext_004_increased_pos_at_3y_low(increased_positions: pd.Series, close: pd.Series) -> pd.Series:
    """Increased positions weighted by 3-year drawdown depth."""
    prox = _proximity_to_trailing_low(close, _TD_3Y)
    return increased_positions.fillna(0) * (1 - prox).clip(0, 1)


def ibf_ext_005_new_pos_times_dd_2y(new_positions: pd.Series, close: pd.Series) -> pd.Series:
    """New positions * 2-year drawdown-from-high."""
    return new_positions.fillna(0) * _drawdown_from_trailing_high(close, _TD_2Y)


def ibf_ext_006_new_pos_times_dd_3y(new_positions: pd.Series, close: pd.Series) -> pd.Series:
    """New positions * 3-year drawdown-from-high."""
    return new_positions.fillna(0) * _drawdown_from_trailing_high(close, _TD_3Y)


def ibf_ext_007_increased_pos_times_dd_1y(increased_positions: pd.Series, close: pd.Series) -> pd.Series:
    """Increased positions * 1-year drawdown-from-high."""
    return increased_positions.fillna(0) * _drawdown_from_trailing_high(close, _TD_YEAR)


def ibf_ext_008_gross_add_times_dd_3y(new_positions: pd.Series, increased_positions: pd.Series,
                                       close: pd.Series) -> pd.Series:
    """Gross additions * 3-year drawdown-from-high."""
    return _gross(new_positions, increased_positions) * _drawdown_from_trailing_high(close, _TD_3Y)


def ibf_ext_009_net_add_times_dd_1y(new_positions: pd.Series, increased_positions: pd.Series,
                                     closed_positions: pd.Series, decreased_positions: pd.Series,
                                     close: pd.Series) -> pd.Series:
    """Net additions (positive only) * 1-year drawdown-from-high."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    return net.clip(lower=0) * _drawdown_from_trailing_high(close, _TD_YEAR)


def ibf_ext_010_net_add_times_dd_2y(new_positions: pd.Series, increased_positions: pd.Series,
                                     closed_positions: pd.Series, decreased_positions: pd.Series,
                                     close: pd.Series) -> pd.Series:
    """Net additions (positive only) * 2-year drawdown-from-high."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    return net.clip(lower=0) * _drawdown_from_trailing_high(close, _TD_2Y)


# --- Group B (011-020): Additional proximity thresholds / flags ---

def ibf_ext_011_flag_within3pct_1y_low(close: pd.Series) -> pd.Series:
    """1 if close is within 3% above 1-yr trailing low."""
    return (_proximity_to_trailing_low(close, _TD_YEAR) <= 0.03).astype(float)


def ibf_ext_012_flag_within15pct_1y_low(close: pd.Series) -> pd.Series:
    """1 if close is within 15% above 1-yr trailing low."""
    return (_proximity_to_trailing_low(close, _TD_YEAR) <= 0.15).astype(float)


def ibf_ext_013_flag_within5pct_2y_low(close: pd.Series) -> pd.Series:
    """1 if close is within 5% above 2-yr trailing low."""
    return (_proximity_to_trailing_low(close, _TD_2Y) <= 0.05).astype(float)


def ibf_ext_014_flag_within10pct_3y_low(close: pd.Series) -> pd.Series:
    """1 if close is within 10% above 3-yr trailing low."""
    return (_proximity_to_trailing_low(close, _TD_3Y) <= 0.10).astype(float)


def ibf_ext_015_new_pos_within15pct_1y_low(new_positions: pd.Series, close: pd.Series) -> pd.Series:
    """New positions when stock is within 15% of 1-yr low."""
    flag = (_proximity_to_trailing_low(close, _TD_YEAR) <= 0.15).astype(float)
    return new_positions.fillna(0) * flag


def ibf_ext_016_gross_add_within5pct_2y_low(new_positions: pd.Series, increased_positions: pd.Series,
                                             close: pd.Series) -> pd.Series:
    """Gross additions when within 5% of 2-yr low."""
    flag = (_proximity_to_trailing_low(close, _TD_2Y) <= 0.05).astype(float)
    return _gross(new_positions, increased_positions) * flag


def ibf_ext_017_gross_add_within10pct_3y_low(new_positions: pd.Series, increased_positions: pd.Series,
                                              close: pd.Series) -> pd.Series:
    """Gross additions when within 10% of 3-yr low."""
    flag = (_proximity_to_trailing_low(close, _TD_3Y) <= 0.10).astype(float)
    return _gross(new_positions, increased_positions) * flag


def ibf_ext_018_increased_pos_within3pct_1y_low(increased_positions: pd.Series, close: pd.Series) -> pd.Series:
    """Increased positions when within 3% of 1-yr low."""
    flag = (_proximity_to_trailing_low(close, _TD_YEAR) <= 0.03).astype(float)
    return increased_positions.fillna(0) * flag


def ibf_ext_019_flag_dd_over_50pct_2y(close: pd.Series) -> pd.Series:
    """1 if 2-yr drawdown-from-high exceeds 50% (deep distress regime)."""
    return (_drawdown_from_trailing_high(close, _TD_2Y) >= 0.50).astype(float)


def ibf_ext_020_flag_dd_over_60pct_3y(close: pd.Series) -> pd.Series:
    """1 if 3-yr drawdown-from-high exceeds 60% (severe capitulation regime)."""
    return (_drawdown_from_trailing_high(close, _TD_3Y) >= 0.60).astype(float)


# --- Group C (021-030): Percentile-rank variants of accumulation series ---

def ibf_ext_021_new_pos_pctile_1y(new_positions: pd.Series) -> pd.Series:
    """1-year rolling percentile rank of new-position count."""
    return _rolling_rank_pct(new_positions.fillna(0), _TD_YEAR)


def ibf_ext_022_new_pos_pctile_3y(new_positions: pd.Series) -> pd.Series:
    """3-year rolling percentile rank of new-position count."""
    return _rolling_rank_pct(new_positions.fillna(0), _TD_3Y)


def ibf_ext_023_increased_pos_pctile_2y(increased_positions: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of increased-position count."""
    return _rolling_rank_pct(increased_positions.fillna(0), _TD_2Y)


def ibf_ext_024_gross_add_pctile_1y(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    """1-year rolling percentile rank of gross additions."""
    return _rolling_rank_pct(_gross(new_positions, increased_positions), _TD_YEAR)


def ibf_ext_025_gross_add_pctile_3y(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    """3-year rolling percentile rank of gross additions."""
    return _rolling_rank_pct(_gross(new_positions, increased_positions), _TD_3Y)


def ibf_ext_026_net_add_pctile_2y(new_positions: pd.Series, increased_positions: pd.Series,
                                   closed_positions: pd.Series, decreased_positions: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of net additions."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    return _rolling_rank_pct(net, _TD_2Y)


def ibf_ext_027_inst_shares_pctile_2y(inst_shares: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of institutional share count."""
    return _rolling_rank_pct(inst_shares.ffill().fillna(0), _TD_2Y)


def ibf_ext_028_inst_value_pctile_2y(inst_value: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of institutional value."""
    return _rolling_rank_pct(inst_value.ffill().fillna(0), _TD_2Y)


def ibf_ext_029_inst_pct_pctile_3y(inst_pct: pd.Series) -> pd.Series:
    """3-year rolling percentile rank of institutional ownership pct."""
    return _rolling_rank_pct(inst_pct.ffill().fillna(0), _TD_3Y)


def ibf_ext_030_new_pos_expanding_pctile(new_positions: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of new-position count."""
    np_ = new_positions.fillna(0)
    def _r(x):
        if len(x) < 2:
            return np.nan
        return (x[:-1] < x[-1]).sum() / (len(x) - 1)
    return np_.expanding(min_periods=2).apply(_r, raw=True)


# --- Group D (031-040): Z-score variants with new windows ---

def ibf_ext_031_new_pos_zscore_2q(new_positions: pd.Series) -> pd.Series:
    """2-quarter rolling z-score of new-position count."""
    return _zscore_rolling(new_positions.fillna(0), _TD_2Q)


def ibf_ext_032_new_pos_zscore_3y(new_positions: pd.Series) -> pd.Series:
    """3-year rolling z-score of new-position count."""
    return _zscore_rolling(new_positions.fillna(0), _TD_3Y)


def ibf_ext_033_increased_pos_zscore_2y(increased_positions: pd.Series) -> pd.Series:
    """2-year rolling z-score of increased-position count."""
    return _zscore_rolling(increased_positions.fillna(0), _TD_2Y)


def ibf_ext_034_gross_add_zscore_3y(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    """3-year rolling z-score of gross additions."""
    return _zscore_rolling(_gross(new_positions, increased_positions), _TD_3Y)


def ibf_ext_035_net_add_zscore_2y(new_positions: pd.Series, increased_positions: pd.Series,
                                   closed_positions: pd.Series, decreased_positions: pd.Series) -> pd.Series:
    """2-year rolling z-score of net additions."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    return _zscore_rolling(net, _TD_2Y)


def ibf_ext_036_inst_shares_qoq_change_zscore_2y(inst_shares: pd.Series) -> pd.Series:
    """2-year z-score of QoQ change in institutional shares."""
    chg = inst_shares.ffill().diff(_TD_QTR)
    return _zscore_rolling(chg, _TD_2Y)


def ibf_ext_037_inst_value_qoq_change_zscore_2y(inst_value: pd.Series) -> pd.Series:
    """2-year z-score of QoQ change in institutional value."""
    chg = inst_value.ffill().diff(_TD_QTR)
    return _zscore_rolling(chg, _TD_2Y)


def ibf_ext_038_inst_pct_qoq_change_zscore_2y(inst_pct: pd.Series) -> pd.Series:
    """2-year z-score of QoQ change in institutional ownership pct."""
    chg = inst_pct.ffill().diff(_TD_QTR)
    return _zscore_rolling(chg, _TD_2Y)


def ibf_ext_039_new_pos_expanding_zscore(new_positions: pd.Series) -> pd.Series:
    """Expanding all-history z-score of new-position count."""
    s = new_positions.fillna(0)
    mu = s.expanding(min_periods=2).mean()
    sd = s.expanding(min_periods=2).std()
    return _safe_div(s - mu, sd)


def ibf_ext_040_gross_add_expanding_zscore(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    """Expanding all-history z-score of gross additions."""
    s = _gross(new_positions, increased_positions)
    mu = s.expanding(min_periods=2).mean()
    sd = s.expanding(min_periods=2).std()
    return _safe_div(s - mu, sd)


# --- Group E (041-050): Accumulation streaks and persistence ---

def ibf_ext_041_consec_days_new_pos_positive(new_positions: pd.Series) -> pd.Series:
    """Consecutive days new_positions has been > 0."""
    return _consec_streak(new_positions.fillna(0) > 0)


def ibf_ext_042_consec_days_gross_add_above_median(new_positions: pd.Series,
                                                    increased_positions: pd.Series) -> pd.Series:
    """Consecutive days gross additions exceed their trailing 1-yr median."""
    gross = _gross(new_positions, increased_positions)
    return _consec_streak(gross > _rolling_median(gross, _TD_YEAR))


def ibf_ext_043_consec_days_net_add_positive(new_positions: pd.Series, increased_positions: pd.Series,
                                              closed_positions: pd.Series,
                                              decreased_positions: pd.Series) -> pd.Series:
    """Consecutive days net additions have been positive."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    return _consec_streak(net > 0)


def ibf_ext_044_consec_days_inst_shares_rising(inst_shares: pd.Series) -> pd.Series:
    """Consecutive days institutional shares above their QoQ-prior value."""
    s = inst_shares.ffill()
    return _consec_streak(s > s.shift(_TD_QTR))


def ibf_ext_045_consec_days_inst_pct_rising(inst_pct: pd.Series) -> pd.Series:
    """Consecutive days institutional ownership pct above its QoQ-prior value."""
    s = inst_pct.ffill()
    return _consec_streak(s > s.shift(_TD_QTR))


def ibf_ext_046_new_pos_positive_days_2y(new_positions: pd.Series) -> pd.Series:
    """Count of days in trailing 2 years where new_positions > 0."""
    return _rolling_sum((new_positions.fillna(0) > 0).astype(float), _TD_2Y)


def ibf_ext_047_gross_add_above_mean_days_1y(new_positions: pd.Series,
                                              increased_positions: pd.Series) -> pd.Series:
    """Count of days in trailing year gross additions exceeded trailing-year mean."""
    gross = _gross(new_positions, increased_positions)
    return _rolling_sum((gross > _rolling_mean(gross, _TD_YEAR)).astype(float), _TD_YEAR)


def ibf_ext_048_inst_shares_up_days_2y(inst_shares: pd.Series) -> pd.Series:
    """Count of days in trailing 2 years institutional shares rose QoQ."""
    s = inst_shares.ffill()
    return _rolling_sum((s.diff(_TD_QTR) > 0).astype(float), _TD_2Y)


def ibf_ext_049_max_new_pos_streak_2y(new_positions: pd.Series) -> pd.Series:
    """Longest run of consecutive new_positions>0 days within trailing 2 years."""
    streak = _consec_streak(new_positions.fillna(0) > 0)
    return _rolling_max(streak, _TD_2Y)


def ibf_ext_050_max_net_add_streak_2y(new_positions: pd.Series, increased_positions: pd.Series,
                                       closed_positions: pd.Series,
                                       decreased_positions: pd.Series) -> pd.Series:
    """Longest run of consecutive net-additions-positive days within trailing 2 years."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    return _rolling_max(_consec_streak(net > 0), _TD_2Y)


# --- Group F (051-058): EWM-smoothed accumulation, new spans ---

def ibf_ext_051_new_pos_ewm_2q(new_positions: pd.Series) -> pd.Series:
    """EWM-smoothed new-position count (span=2 quarters)."""
    return _ewm_mean(new_positions.fillna(0), _TD_2Q)


def ibf_ext_052_new_pos_ewm_1y(new_positions: pd.Series) -> pd.Series:
    """EWM-smoothed new-position count (span=1 year)."""
    return _ewm_mean(new_positions.fillna(0), _TD_YEAR)


def ibf_ext_053_increased_pos_ewm_1q(increased_positions: pd.Series) -> pd.Series:
    """EWM-smoothed increased-position count (span=1 quarter)."""
    return _ewm_mean(increased_positions.fillna(0), _TD_QTR)


def ibf_ext_054_gross_add_ewm_1y(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    """EWM-smoothed gross additions (span=1 year)."""
    return _ewm_mean(_gross(new_positions, increased_positions), _TD_YEAR)


def ibf_ext_055_net_add_ewm_2q(new_positions: pd.Series, increased_positions: pd.Series,
                                closed_positions: pd.Series, decreased_positions: pd.Series) -> pd.Series:
    """EWM-smoothed net additions (span=2 quarters)."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    return _ewm_mean(net, _TD_2Q)


def ibf_ext_056_gross_add_ewm_short_minus_long(new_positions: pd.Series,
                                                increased_positions: pd.Series) -> pd.Series:
    """Gross-additions EWM(1q) minus EWM(1y) — accumulation momentum spread."""
    gross = _gross(new_positions, increased_positions)
    return _ewm_mean(gross, _TD_QTR) - _ewm_mean(gross, _TD_YEAR)


def ibf_ext_057_inst_value_ewm_2q(inst_value: pd.Series) -> pd.Series:
    """EWM-smoothed institutional value (span=2 quarters)."""
    return _ewm_mean(inst_value.ffill().fillna(0), _TD_2Q)


def ibf_ext_058_new_pos_vs_ewm_deviation(new_positions: pd.Series) -> pd.Series:
    """New-position count minus its EWM(1q) — deviation from smoothed trend."""
    np_ = new_positions.fillna(0)
    return np_ - _ewm_mean(np_, _TD_QTR)


# --- Group G (059-066): Holder-level intensity and ratios ---

def ibf_ext_059_value_per_gross_add(inst_value: pd.Series, new_positions: pd.Series,
                                     increased_positions: pd.Series) -> pd.Series:
    """Institutional value / gross additions — implied USD ticket per buying institution."""
    gross = _gross(new_positions, increased_positions)
    return _safe_div(inst_value.fillna(0), gross.replace(0, np.nan))


def ibf_ext_060_value_per_holder(inst_value: pd.Series, inst_holders: pd.Series) -> pd.Series:
    """Average institutional value held per holder."""
    return _safe_div(inst_value.fillna(0), inst_holders.replace(0, np.nan))


def ibf_ext_061_shares_per_holder(inst_shares: pd.Series, inst_holders: pd.Series) -> pd.Series:
    """Average institutional shares held per holder."""
    return _safe_div(inst_shares.fillna(0), inst_holders.replace(0, np.nan))


def ibf_ext_062_new_to_increased_ratio(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    """New positions / increased positions — fresh-money vs add-on mix."""
    return _safe_div(new_positions.fillna(0), increased_positions.replace(0, np.nan))


def ibf_ext_063_new_share_of_gross_add(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    """New positions as fraction of gross additions."""
    gross = _gross(new_positions, increased_positions)
    return _safe_div(new_positions.fillna(0), gross.replace(0, np.nan))


def ibf_ext_064_value_per_holder_qoq_change(inst_value: pd.Series, inst_holders: pd.Series) -> pd.Series:
    """QoQ change in value-per-holder (rising = each holder committing more)."""
    vph = _safe_div(inst_value.fillna(0), inst_holders.replace(0, np.nan))
    return vph - vph.shift(_TD_QTR)


def ibf_ext_065_net_add_pct_of_prior_holders(new_positions: pd.Series, increased_positions: pd.Series,
                                              closed_positions: pd.Series, decreased_positions: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """Net additions / inst_holders one quarter prior — net head-count growth rate."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    prior = inst_holders.ffill().shift(_TD_QTR)
    return _safe_div(net, prior.replace(0, np.nan))


def ibf_ext_066_inst_holders_qoq_growth(inst_holders: pd.Series) -> pd.Series:
    """QoQ percentage growth in institutional holder count."""
    s = inst_holders.ffill()
    prev = s.shift(_TD_QTR)
    return _safe_div(s - prev, prev.abs() + _EPS)


# --- Group H (067-075): Composite accumulation-at-low distress scores ---

def ibf_ext_067_new_pos_high_water_2y(new_positions: pd.Series) -> pd.Series:
    """New positions / trailing-2y max — 1 = at 2-year accumulation record."""
    np_ = new_positions.fillna(0)
    return _safe_div(np_, _rolling_max(np_, _TD_2Y) + _EPS)


def ibf_ext_068_gross_add_high_water_3y(new_positions: pd.Series, increased_positions: pd.Series) -> pd.Series:
    """Gross additions / trailing-3y max — 1 = at 3-year accumulation record."""
    gross = _gross(new_positions, increased_positions)
    return _safe_div(gross, _rolling_max(gross, _TD_3Y) + _EPS)


def ibf_ext_069_gross_add_zscore_times_dd_1y(new_positions: pd.Series, increased_positions: pd.Series,
                                              close: pd.Series) -> pd.Series:
    """1-yr z-score of gross additions * 1-yr drawdown-from-high (z-weighted distress add)."""
    z = _zscore_rolling(_gross(new_positions, increased_positions), _TD_YEAR)
    return z * _drawdown_from_trailing_high(close, _TD_YEAR)


def ibf_ext_070_net_add_pctile_times_dd_2y(new_positions: pd.Series, increased_positions: pd.Series,
                                            closed_positions: pd.Series, decreased_positions: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """2-yr percentile rank of net additions * 2-yr drawdown-from-high."""
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    return _rolling_rank_pct(net, _TD_2Y) * _drawdown_from_trailing_high(close, _TD_2Y)


def ibf_ext_071_composite_add_2y_low(new_positions: pd.Series, increased_positions: pd.Series,
                                      inst_pct: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: (gross-add 2y z-score + inst_pct QoQ rise) * 2-yr drawdown depth."""
    gross_z = _zscore_rolling(_gross(new_positions, increased_positions), _TD_2Y)
    pct_chg = inst_pct.ffill().diff(_TD_QTR).clip(lower=0)
    return (gross_z + pct_chg) * _drawdown_from_trailing_high(close, _TD_2Y)


def ibf_ext_072_bottom_fish_intensity_index(new_positions: pd.Series, increased_positions: pd.Series,
                                             close: pd.Series) -> pd.Series:
    """Gross-add percentile * deep-low flag (within 10% of 3y low) — discrete intensity index."""
    pct = _rolling_rank_pct(_gross(new_positions, increased_positions), _TD_2Y)
    flag = (_proximity_to_trailing_low(close, _TD_3Y) <= 0.10).astype(float)
    return pct * flag


def ibf_ext_073_inst_pct_recovery_from_min_3y(inst_pct: pd.Series) -> pd.Series:
    """Inst ownership pct minus its 3-yr rolling minimum — rebound off the ownership trough."""
    s = inst_pct.ffill()
    return s - _rolling_min(s, _TD_3Y)


def ibf_ext_074_inst_shares_recovery_from_min_2y(inst_shares: pd.Series) -> pd.Series:
    """Inst shares / 2-yr rolling minimum minus 1 — fractional rebound off share trough."""
    s = inst_shares.ffill()
    return _safe_div(s, _rolling_min(s, _TD_2Y).replace(0, np.nan)) - 1.0


def ibf_ext_075_capitulation_accumulation_composite(new_positions: pd.Series,
                                                     increased_positions: pd.Series,
                                                     closed_positions: pd.Series,
                                                     decreased_positions: pd.Series,
                                                     inst_pct: pd.Series,
                                                     close: pd.Series) -> pd.Series:
    """Capitulation composite: normalized gross-add pctile + net-add positivity flag + inst_pct
    QoQ rise, all amplified by 3-yr drawdown depth. Higher = stronger buy-the-bottom signal."""
    gross_pct = _rolling_rank_pct(_gross(new_positions, increased_positions), _TD_2Y).fillna(0.5)
    net = _net(new_positions, increased_positions, closed_positions, decreased_positions)
    net_flag = (net > 0).astype(float)
    pct_rise = inst_pct.ffill().diff(_TD_QTR).clip(lower=0)
    dd = _drawdown_from_trailing_high(close, _TD_3Y)
    return (gross_pct + net_flag + pct_rise.clip(upper=1.0)) * dd


# ===========================================================================
# Registry
# ===========================================================================
INSTITUTIONAL_BOTTOM_FISH_EXTENDED_REGISTRY_001_075 = {
    "ibf_ext_001_new_pos_at_6m_low": {"inputs": ["new_positions", "close"], "func": ibf_ext_001_new_pos_at_6m_low},
    "ibf_ext_002_increased_pos_at_6m_low": {"inputs": ["increased_positions", "close"], "func": ibf_ext_002_increased_pos_at_6m_low},
    "ibf_ext_003_gross_add_at_6m_low": {"inputs": ["new_positions", "increased_positions", "close"], "func": ibf_ext_003_gross_add_at_6m_low},
    "ibf_ext_004_increased_pos_at_3y_low": {"inputs": ["increased_positions", "close"], "func": ibf_ext_004_increased_pos_at_3y_low},
    "ibf_ext_005_new_pos_times_dd_2y": {"inputs": ["new_positions", "close"], "func": ibf_ext_005_new_pos_times_dd_2y},
    "ibf_ext_006_new_pos_times_dd_3y": {"inputs": ["new_positions", "close"], "func": ibf_ext_006_new_pos_times_dd_3y},
    "ibf_ext_007_increased_pos_times_dd_1y": {"inputs": ["increased_positions", "close"], "func": ibf_ext_007_increased_pos_times_dd_1y},
    "ibf_ext_008_gross_add_times_dd_3y": {"inputs": ["new_positions", "increased_positions", "close"], "func": ibf_ext_008_gross_add_times_dd_3y},
    "ibf_ext_009_net_add_times_dd_1y": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "close"], "func": ibf_ext_009_net_add_times_dd_1y},
    "ibf_ext_010_net_add_times_dd_2y": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "close"], "func": ibf_ext_010_net_add_times_dd_2y},
    "ibf_ext_011_flag_within3pct_1y_low": {"inputs": ["close"], "func": ibf_ext_011_flag_within3pct_1y_low},
    "ibf_ext_012_flag_within15pct_1y_low": {"inputs": ["close"], "func": ibf_ext_012_flag_within15pct_1y_low},
    "ibf_ext_013_flag_within5pct_2y_low": {"inputs": ["close"], "func": ibf_ext_013_flag_within5pct_2y_low},
    "ibf_ext_014_flag_within10pct_3y_low": {"inputs": ["close"], "func": ibf_ext_014_flag_within10pct_3y_low},
    "ibf_ext_015_new_pos_within15pct_1y_low": {"inputs": ["new_positions", "close"], "func": ibf_ext_015_new_pos_within15pct_1y_low},
    "ibf_ext_016_gross_add_within5pct_2y_low": {"inputs": ["new_positions", "increased_positions", "close"], "func": ibf_ext_016_gross_add_within5pct_2y_low},
    "ibf_ext_017_gross_add_within10pct_3y_low": {"inputs": ["new_positions", "increased_positions", "close"], "func": ibf_ext_017_gross_add_within10pct_3y_low},
    "ibf_ext_018_increased_pos_within3pct_1y_low": {"inputs": ["increased_positions", "close"], "func": ibf_ext_018_increased_pos_within3pct_1y_low},
    "ibf_ext_019_flag_dd_over_50pct_2y": {"inputs": ["close"], "func": ibf_ext_019_flag_dd_over_50pct_2y},
    "ibf_ext_020_flag_dd_over_60pct_3y": {"inputs": ["close"], "func": ibf_ext_020_flag_dd_over_60pct_3y},
    "ibf_ext_021_new_pos_pctile_1y": {"inputs": ["new_positions"], "func": ibf_ext_021_new_pos_pctile_1y},
    "ibf_ext_022_new_pos_pctile_3y": {"inputs": ["new_positions"], "func": ibf_ext_022_new_pos_pctile_3y},
    "ibf_ext_023_increased_pos_pctile_2y": {"inputs": ["increased_positions"], "func": ibf_ext_023_increased_pos_pctile_2y},
    "ibf_ext_024_gross_add_pctile_1y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_024_gross_add_pctile_1y},
    "ibf_ext_025_gross_add_pctile_3y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_025_gross_add_pctile_3y},
    "ibf_ext_026_net_add_pctile_2y": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_ext_026_net_add_pctile_2y},
    "ibf_ext_027_inst_shares_pctile_2y": {"inputs": ["inst_shares"], "func": ibf_ext_027_inst_shares_pctile_2y},
    "ibf_ext_028_inst_value_pctile_2y": {"inputs": ["inst_value"], "func": ibf_ext_028_inst_value_pctile_2y},
    "ibf_ext_029_inst_pct_pctile_3y": {"inputs": ["inst_pct"], "func": ibf_ext_029_inst_pct_pctile_3y},
    "ibf_ext_030_new_pos_expanding_pctile": {"inputs": ["new_positions"], "func": ibf_ext_030_new_pos_expanding_pctile},
    "ibf_ext_031_new_pos_zscore_2q": {"inputs": ["new_positions"], "func": ibf_ext_031_new_pos_zscore_2q},
    "ibf_ext_032_new_pos_zscore_3y": {"inputs": ["new_positions"], "func": ibf_ext_032_new_pos_zscore_3y},
    "ibf_ext_033_increased_pos_zscore_2y": {"inputs": ["increased_positions"], "func": ibf_ext_033_increased_pos_zscore_2y},
    "ibf_ext_034_gross_add_zscore_3y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_034_gross_add_zscore_3y},
    "ibf_ext_035_net_add_zscore_2y": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_ext_035_net_add_zscore_2y},
    "ibf_ext_036_inst_shares_qoq_change_zscore_2y": {"inputs": ["inst_shares"], "func": ibf_ext_036_inst_shares_qoq_change_zscore_2y},
    "ibf_ext_037_inst_value_qoq_change_zscore_2y": {"inputs": ["inst_value"], "func": ibf_ext_037_inst_value_qoq_change_zscore_2y},
    "ibf_ext_038_inst_pct_qoq_change_zscore_2y": {"inputs": ["inst_pct"], "func": ibf_ext_038_inst_pct_qoq_change_zscore_2y},
    "ibf_ext_039_new_pos_expanding_zscore": {"inputs": ["new_positions"], "func": ibf_ext_039_new_pos_expanding_zscore},
    "ibf_ext_040_gross_add_expanding_zscore": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_040_gross_add_expanding_zscore},
    "ibf_ext_041_consec_days_new_pos_positive": {"inputs": ["new_positions"], "func": ibf_ext_041_consec_days_new_pos_positive},
    "ibf_ext_042_consec_days_gross_add_above_median": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_042_consec_days_gross_add_above_median},
    "ibf_ext_043_consec_days_net_add_positive": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_ext_043_consec_days_net_add_positive},
    "ibf_ext_044_consec_days_inst_shares_rising": {"inputs": ["inst_shares"], "func": ibf_ext_044_consec_days_inst_shares_rising},
    "ibf_ext_045_consec_days_inst_pct_rising": {"inputs": ["inst_pct"], "func": ibf_ext_045_consec_days_inst_pct_rising},
    "ibf_ext_046_new_pos_positive_days_2y": {"inputs": ["new_positions"], "func": ibf_ext_046_new_pos_positive_days_2y},
    "ibf_ext_047_gross_add_above_mean_days_1y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_047_gross_add_above_mean_days_1y},
    "ibf_ext_048_inst_shares_up_days_2y": {"inputs": ["inst_shares"], "func": ibf_ext_048_inst_shares_up_days_2y},
    "ibf_ext_049_max_new_pos_streak_2y": {"inputs": ["new_positions"], "func": ibf_ext_049_max_new_pos_streak_2y},
    "ibf_ext_050_max_net_add_streak_2y": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_ext_050_max_net_add_streak_2y},
    "ibf_ext_051_new_pos_ewm_2q": {"inputs": ["new_positions"], "func": ibf_ext_051_new_pos_ewm_2q},
    "ibf_ext_052_new_pos_ewm_1y": {"inputs": ["new_positions"], "func": ibf_ext_052_new_pos_ewm_1y},
    "ibf_ext_053_increased_pos_ewm_1q": {"inputs": ["increased_positions"], "func": ibf_ext_053_increased_pos_ewm_1q},
    "ibf_ext_054_gross_add_ewm_1y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_054_gross_add_ewm_1y},
    "ibf_ext_055_net_add_ewm_2q": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_ext_055_net_add_ewm_2q},
    "ibf_ext_056_gross_add_ewm_short_minus_long": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_056_gross_add_ewm_short_minus_long},
    "ibf_ext_057_inst_value_ewm_2q": {"inputs": ["inst_value"], "func": ibf_ext_057_inst_value_ewm_2q},
    "ibf_ext_058_new_pos_vs_ewm_deviation": {"inputs": ["new_positions"], "func": ibf_ext_058_new_pos_vs_ewm_deviation},
    "ibf_ext_059_value_per_gross_add": {"inputs": ["inst_value", "new_positions", "increased_positions"], "func": ibf_ext_059_value_per_gross_add},
    "ibf_ext_060_value_per_holder": {"inputs": ["inst_value", "inst_holders"], "func": ibf_ext_060_value_per_holder},
    "ibf_ext_061_shares_per_holder": {"inputs": ["inst_shares", "inst_holders"], "func": ibf_ext_061_shares_per_holder},
    "ibf_ext_062_new_to_increased_ratio": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_062_new_to_increased_ratio},
    "ibf_ext_063_new_share_of_gross_add": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_063_new_share_of_gross_add},
    "ibf_ext_064_value_per_holder_qoq_change": {"inputs": ["inst_value", "inst_holders"], "func": ibf_ext_064_value_per_holder_qoq_change},
    "ibf_ext_065_net_add_pct_of_prior_holders": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "inst_holders"], "func": ibf_ext_065_net_add_pct_of_prior_holders},
    "ibf_ext_066_inst_holders_qoq_growth": {"inputs": ["inst_holders"], "func": ibf_ext_066_inst_holders_qoq_growth},
    "ibf_ext_067_new_pos_high_water_2y": {"inputs": ["new_positions"], "func": ibf_ext_067_new_pos_high_water_2y},
    "ibf_ext_068_gross_add_high_water_3y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_ext_068_gross_add_high_water_3y},
    "ibf_ext_069_gross_add_zscore_times_dd_1y": {"inputs": ["new_positions", "increased_positions", "close"], "func": ibf_ext_069_gross_add_zscore_times_dd_1y},
    "ibf_ext_070_net_add_pctile_times_dd_2y": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "close"], "func": ibf_ext_070_net_add_pctile_times_dd_2y},
    "ibf_ext_071_composite_add_2y_low": {"inputs": ["new_positions", "increased_positions", "inst_pct", "close"], "func": ibf_ext_071_composite_add_2y_low},
    "ibf_ext_072_bottom_fish_intensity_index": {"inputs": ["new_positions", "increased_positions", "close"], "func": ibf_ext_072_bottom_fish_intensity_index},
    "ibf_ext_073_inst_pct_recovery_from_min_3y": {"inputs": ["inst_pct"], "func": ibf_ext_073_inst_pct_recovery_from_min_3y},
    "ibf_ext_074_inst_shares_recovery_from_min_2y": {"inputs": ["inst_shares"], "func": ibf_ext_074_inst_shares_recovery_from_min_2y},
    "ibf_ext_075_capitulation_accumulation_composite": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "inst_pct", "close"], "func": ibf_ext_075_capitulation_accumulation_composite},
}
