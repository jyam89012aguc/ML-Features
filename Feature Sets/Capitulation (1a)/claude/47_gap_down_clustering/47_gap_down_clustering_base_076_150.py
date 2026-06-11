"""
47_gap_down_clustering — Base Features 076-150
Domain: clustered down-gaps and gap streaks — gap-sequence acceleration, magnitude z-scores,
volume-weighted gap clustering, gap-down following gap-down patterns, time-between clusters,
multi-scale density ratios, streak severity, gap-close interaction, island-reversal recency
and magnitude, top-island detection, and gap-down-then-gap-up reversal signatures.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _down_gap(close: pd.Series, open: pd.Series) -> pd.Series:
    """Boolean: today's open < prior close (down-gap day)."""
    return open < close.shift(1)


def _down_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Down-gap as fraction of prior close (zero on non-gap days)."""
    raw = (close.shift(1) - open).clip(lower=0.0)
    return _safe_div(raw, close.shift(1).replace(0, np.nan))


def _down_gap_size(close: pd.Series, open: pd.Series) -> pd.Series:
    """Raw down-gap magnitude in price points (zero on non-gap days)."""
    return (close.shift(1) - open).clip(lower=0.0)


def _up_gap(close: pd.Series, open: pd.Series) -> pd.Series:
    """Boolean: today's open > prior close (up-gap day)."""
    return open > close.shift(1)


def _up_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Up-gap as fraction of prior close (zero on non-gap days)."""
    raw = (open - close.shift(1)).clip(lower=0.0)
    return _safe_div(raw, close.shift(1).replace(0, np.nan))


# ── Island reversal helpers ───────────────────────────────────────────────────

def _island_bottom_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Island-bottom flag: gap-down into a cluster (1-5 bars ago) + gap-up today.
    Fires on the confirmation day. Fully backward-looking.
    """
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        result = result + (ug & entry_gap).astype(float)
    return result.clip(upper=1.0)


def _island_top_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Island-top flag: gap-up into a cluster (1-5 bars ago) + gap-down today.
    Fires on the confirmation day. Fully backward-looking.
    """
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = ug.shift(lag, fill_value=False)
        result = result + (dg & entry_gap).astype(float)
    return result.clip(upper=1.0)


def _days_since_island_bottom(close: pd.Series, open: pd.Series) -> pd.Series:
    """Bars elapsed since the last confirmed island-bottom signal."""
    flag = _island_bottom_flag(close, open)
    not_island = 1.0 - flag
    group = flag.cumsum()
    return not_island.groupby(group).cumsum()


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Gap-down magnitude z-scores and extremity ---

def gdc_076_gap_down_pct_zscore_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of today's down-gap pct relative to 21-day mean/std of gap pct."""
    pct = _down_gap_pct(close, open)
    m = _rolling_mean(pct, _TD_MON)
    s = _rolling_std(pct, _TD_MON)
    return _safe_div(pct - m, s)


def gdc_077_gap_down_pct_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of today's down-gap pct relative to 63-day mean/std of gap pct."""
    pct = _down_gap_pct(close, open)
    m = _rolling_mean(pct, _TD_QTR)
    s = _rolling_std(pct, _TD_QTR)
    return _safe_div(pct - m, s)


def gdc_078_gap_down_pct_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of today's down-gap pct relative to 252-day mean/std."""
    pct = _down_gap_pct(close, open)
    m = _rolling_mean(pct, _TD_YEAR)
    s = _rolling_std(pct, _TD_YEAR)
    return _safe_div(pct - m, s)


def gdc_079_sum_gap_pct_21d_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 21-day cumulative gap-down pct vs its 252-day distribution."""
    pct21 = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    m = _rolling_mean(pct21, _TD_YEAR)
    s = _rolling_std(pct21, _TD_YEAR)
    return _safe_div(pct21 - m, s)


def gdc_080_gap_down_pct_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of today's down-gap pct within trailing 252 days."""
    pct = _down_gap_pct(close, open)
    return pct.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def gdc_081_gap_down_pct_pct_rank_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of today's down-gap pct within trailing 63 days."""
    pct = _down_gap_pct(close, open)
    return pct.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def gdc_082_max_gap_pct_252d_expanding_rank(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day max gap pct (all history)."""
    mx = _rolling_max(_down_gap_pct(close, open), _TD_YEAR)
    return mx.expanding(min_periods=5).rank(pct=True)


def gdc_083_gap_down_pct_ewm_21(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=21) of down-gap pct (smooth recency-weighted gap severity)."""
    return _ewm_mean(_down_gap_pct(close, open), _TD_MON)


def gdc_084_gap_down_pct_ewm_63(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=63) of down-gap pct (medium-term recency-weighted severity)."""
    return _ewm_mean(_down_gap_pct(close, open), _TD_QTR)


def gdc_085_gap_down_pct_std_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day standard deviation of daily down-gap pct (gap volatility)."""
    return _rolling_std(_down_gap_pct(close, open), _TD_MON)


# --- Group I (086-095): Volume-weighted gap-down clustering ---

def gdc_086_vol_wtd_gap_pct_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of down-gap pct over trailing 21 days."""
    pct = _down_gap_pct(close, open)
    return _rolling_sum(pct * volume, _TD_MON)


def gdc_087_vol_wtd_gap_pct_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of down-gap pct over trailing 63 days."""
    pct = _down_gap_pct(close, open)
    return _rolling_sum(pct * volume, _TD_QTR)


def gdc_088_vol_on_gap_down_avg_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on gap-down days over the trailing 21 days."""
    cond = _down_gap(close, open)
    return volume.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()


def gdc_089_vol_on_gap_down_avg_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on gap-down days over the trailing 63 days."""
    cond = _down_gap(close, open)
    return volume.where(cond, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def gdc_090_vol_gap_vs_nongap_ratio_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on gap-down days to avg volume on non-gap days, 21d."""
    cond = _down_gap(close, open)
    gap_vol = volume.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()
    nongap_vol = volume.where(~cond, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(gap_vol, nongap_vol)


def gdc_091_vol_gap_vs_nongap_ratio_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on gap-down days to avg volume on non-gap days, 63d."""
    cond = _down_gap(close, open)
    gap_vol = volume.where(cond, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    nongap_vol = volume.where(~cond, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(gap_vol, nongap_vol)


def gdc_092_high_vol_gap_down_count_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of gap-down days with volume > 2x its 21d average, in last 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = (_down_gap(close, open) & (volume > 2.0 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def gdc_093_high_vol_gap_down_count_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of gap-down days with volume > 2x its 21d average, in last 63 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = (_down_gap(close, open) & (volume > 2.0 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def gdc_094_gap_down_vol_pct_of_total_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on gap-down days as fraction of total volume over trailing 21 days."""
    cond = _down_gap(close, open)
    gap_vol = _rolling_sum(volume.where(cond, 0.0), _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(gap_vol, total_vol)


def gdc_095_gap_down_vol_pct_of_total_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on gap-down days as fraction of total volume over trailing 63 days."""
    cond = _down_gap(close, open)
    gap_vol = _rolling_sum(volume.where(cond, 0.0), _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(gap_vol, total_vol)


# --- Group J (096-105): Gap-down sequence acceleration ---

def gdc_096_gap_down_count_5d_diff_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 5-day gap-down count (acceleration of clustering)."""
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    return cnt5.diff(_TD_WEEK)


def gdc_097_gap_down_count_21d_diff_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day gap-down count (recent surge in cluster density)."""
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    return cnt21.diff(_TD_WEEK)


def gdc_098_gap_down_count_63d_diff_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day gap-down count."""
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    return cnt63.diff(_TD_MON)


def gdc_099_consec_gap_down_streak_diff_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of current consecutive gap-down streak (velocity of streak growth)."""
    streak = _consec_streak(_down_gap(close, open))
    return streak.diff(_TD_WEEK)


def gdc_100_cum_gap_pct_streak_diff_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of cumulative gap-pct over the current streak (loss acceleration)."""
    pct = _down_gap_pct(close, open)
    cond = _down_gap(close, open)
    group = (~cond).cumsum()
    cum = pct.groupby(group).cumsum().where(cond, 0.0)
    return cum.diff(_TD_WEEK)


def gdc_101_gap_down_pct_21d_diff_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative down-gap pct sum (recent cluster intensity change)."""
    pct21 = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    return pct21.diff(_TD_WEEK)


def gdc_102_gap_down_pct_63d_diff_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day cumulative down-gap pct sum."""
    pct63 = _rolling_sum(_down_gap_pct(close, open), _TD_QTR)
    return pct63.diff(_TD_MON)


def gdc_103_gap_down_ewm21_diff_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) gap-down count (acceleration of smoothed clustering)."""
    ewm = _ewm_mean(_down_gap(close, open).astype(float), _TD_MON)
    return ewm.diff(_TD_WEEK)


def gdc_104_gap_down_streak_start_freq_diff_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day gap-streak start frequency."""
    cond = _down_gap(close, open)
    prev = cond.shift(1, fill_value=False)
    is_start = (cond & (~prev)).astype(float)
    freq63 = _rolling_sum(is_start, _TD_QTR)
    return freq63.diff(_TD_MON)


def gdc_105_gap_down_count_5d_vs_252d_zscore(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 5-day gap-down count relative to its 252-day mean and std."""
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    m = _rolling_mean(cnt5, _TD_YEAR)
    s = _rolling_std(cnt5, _TD_YEAR)
    return _safe_div(cnt5 - m, s)


# --- Group K (106-115): Gap-close interaction and intraday fill patterns ---

def gdc_106_gap_down_closed_same_day_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-down days where close >= prior close (gap filled same day), 21d."""
    cond = _down_gap(close, open)
    filled = cond & (close >= close.shift(1))
    return _rolling_sum(filled.astype(float), _TD_MON)


def gdc_107_gap_down_worsened_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-down days where close < open (gap extended intraday), 21d."""
    cond = _down_gap(close, open)
    worsened = cond & (close < open)
    return _rolling_sum(worsened.astype(float), _TD_MON)


def gdc_108_gap_down_worsened_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-down days where close < open (gap extended intraday), 63d."""
    cond = _down_gap(close, open)
    worsened = cond & (close < open)
    return _rolling_sum(worsened.astype(float), _TD_QTR)


def gdc_109_gap_down_worsened_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down days in 21d that ended with close < open."""
    cnt_gap = _rolling_count_true(_down_gap(close, open), _TD_MON)
    cnt_worse = gdc_107_gap_down_worsened_count_21d(close, open)
    return _safe_div(cnt_worse, cnt_gap)


def gdc_110_gap_down_worsened_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down days in 63d that ended with close < open."""
    cnt_gap = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    cnt_worse = gdc_108_gap_down_worsened_count_63d(close, open)
    return _safe_div(cnt_worse, cnt_gap)


def gdc_111_consec_gap_worsened(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive gap-down days that each ended with close < open."""
    cond = _down_gap(close, open) & (close < open)
    return _consec_streak(cond)


def gdc_112_gap_down_close_vs_open_avg_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average (close - open) on gap-down days over 21d (intraday follow-through)."""
    cond = _down_gap(close, open)
    diff = (close - open).where(cond, np.nan)
    return diff.rolling(_TD_MON, min_periods=1).mean()


def gdc_113_gap_down_range_avg_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average intraday high-low range on gap-down days over trailing 21 days."""
    cond = _down_gap(close, open)
    rng = (high - low).where(cond, np.nan)
    return rng.rolling(_TD_MON, min_periods=1).mean()


def gdc_114_gap_down_body_pct_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average |close-open|/(prior_close) on gap-down days over 21 days."""
    cond = _down_gap(close, open)
    body = ((close - open).abs() / close.shift(1).replace(0, np.nan)).where(cond, np.nan)
    return body.rolling(_TD_MON, min_periods=1).mean()


def gdc_115_gap_open_vs_prior_low_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Average (prior_low - open) on gap-down days over 21d (gap below prior low)."""
    cond = _down_gap(close, open)
    below_low = (low.shift(1) - open).where(cond, np.nan)
    return below_low.rolling(_TD_MON, min_periods=1).mean()


# --- Group L (116-125): Multi-scale cluster comparison and ratio features ---

def gdc_116_gap_cnt_21d_vs_63d_norm(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day gap count rate vs 63-day gap count rate (normalized ratio)."""
    r21 = _rolling_count_true(_down_gap(close, open), _TD_MON) / _TD_MON
    r63 = _rolling_count_true(_down_gap(close, open), _TD_QTR) / _TD_QTR
    return _safe_div(r21, r63)


def gdc_117_gap_cnt_5d_vs_21d_norm(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day gap count rate vs 21-day gap count rate."""
    r5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK) / _TD_WEEK
    r21 = _rolling_count_true(_down_gap(close, open), _TD_MON) / _TD_MON
    return _safe_div(r5, r21)


def gdc_118_gap_cnt_63d_vs_252d_norm(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day gap count rate vs 252-day gap count rate."""
    r63 = _rolling_count_true(_down_gap(close, open), _TD_QTR) / _TD_QTR
    r252 = _rolling_count_true(_down_gap(close, open), _TD_YEAR) / _TD_YEAR
    return _safe_div(r63, r252)


def gdc_119_gap_pct_sum_21d_vs_63d_norm(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day cumulative gap-pct rate vs 63-day rate (magnitude surge)."""
    pct = _down_gap_pct(close, open)
    s21 = _rolling_sum(pct, _TD_MON) / _TD_MON
    s63 = _rolling_sum(pct, _TD_QTR) / _TD_QTR
    return _safe_div(s21, s63)


def gdc_120_gap_pct_sum_63d_vs_252d_norm(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day cumulative gap-pct rate vs 252-day rate."""
    pct = _down_gap_pct(close, open)
    s63 = _rolling_sum(pct, _TD_QTR) / _TD_QTR
    s252 = _rolling_sum(pct, _TD_YEAR) / _TD_YEAR
    return _safe_div(s63, s252)


def gdc_121_max_gap_pct_21d_vs_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21-day max gap pct to 63-day max gap pct."""
    pct = _down_gap_pct(close, open)
    return _safe_div(_rolling_max(pct, _TD_MON), _rolling_max(pct, _TD_QTR))


def gdc_122_max_gap_pct_63d_vs_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 63-day max gap pct to 252-day max gap pct."""
    pct = _down_gap_pct(close, open)
    return _safe_div(_rolling_max(pct, _TD_QTR), _rolling_max(pct, _TD_YEAR))


def gdc_123_gap_down_streak_len_vs_avg_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current gap streak length vs 252-day average streak length."""
    streak = _consec_streak(_down_gap(close, open))
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def gdc_124_gap_cluster_score_composite(close: pd.Series, open: pd.Series) -> pd.Series:
    """Composite: (fraction_5d + fraction_21d + fraction_63d) / 3 cluster score."""
    cond = _down_gap(close, open).astype(float)
    f5 = _rolling_sum(cond, _TD_WEEK) / _TD_WEEK
    f21 = _rolling_sum(cond, _TD_MON) / _TD_MON
    f63 = _rolling_sum(cond, _TD_QTR) / _TD_QTR
    return (f5 + f21 + f63) / 3.0


def gdc_125_gap_cluster_score_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of composite cluster score within trailing 252 days."""
    score = gdc_124_gap_cluster_score_composite(close, open)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group M (126-135): Gap-down streaks with intraday low context ---

def gdc_126_consec_gap_below_prior_low(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where open gaps below prior day's intraday low."""
    cond = open < low.shift(1)
    return _consec_streak(cond)


def gdc_127_count_gap_below_prior_low_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where open < prior day low in trailing 21 days."""
    cond = open < low.shift(1)
    return _rolling_count_true(cond, _TD_MON)


def gdc_128_count_gap_below_prior_low_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where open < prior day low in trailing 63 days."""
    cond = open < low.shift(1)
    return _rolling_count_true(cond, _TD_QTR)


def gdc_129_gap_below_2d_low_count_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where open < 2-day rolling low in trailing 21 days."""
    two_day_low = low.rolling(2, min_periods=1).min().shift(1)
    cond = open < two_day_low
    return _rolling_count_true(cond, _TD_MON)


def gdc_130_gap_below_5d_low_count_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where open < 5-day rolling low (prior) in trailing 21 days."""
    five_day_low = low.rolling(_TD_WEEK, min_periods=1).min().shift(1)
    cond = open < five_day_low
    return _rolling_count_true(cond, _TD_MON)


def gdc_131_gap_below_21d_low_count_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where open < 21-day rolling low (prior) in trailing 63 days."""
    mon_low = low.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min().shift(1)
    cond = open < mon_low
    return _rolling_count_true(cond, _TD_QTR)


def gdc_132_gap_down_below_low_fraction_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of gap-down days where open was also below prior day low, 21d."""
    gap = _down_gap(close, open)
    below_low = open < low.shift(1)
    both = (gap & below_low).astype(float)
    gap_cnt = _rolling_count_true(gap, _TD_MON)
    both_cnt = _rolling_sum(both, _TD_MON)
    return _safe_div(both_cnt, gap_cnt)


def gdc_133_gap_size_below_prior_low_avg_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Average (prior_low - open) for days where open < prior low, 21d."""
    diff = (low.shift(1) - open).clip(lower=0.0)
    cond = open < low.shift(1)
    return diff.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()


def gdc_134_breakaway_gap_pct_avg_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Average pct gap on breakaway days (open < prior 21d low) over 63d."""
    pct = _down_gap_pct(close, open)
    prior_21_low = low.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    cond = (open < close.shift(1)) & (open < prior_21_low)
    return pct.where(cond, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def gdc_135_breakaway_gap_down_flag_63d_count(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of breakaway down-gap days in trailing 63 days (open < prior 21-day low)."""
    prior_21_low = low.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    flag = ((open < close.shift(1)) & (open < prior_21_low)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


# --- Group N (136-140): Cluster exhaustion signals ---

def gdc_136_gap_cluster_then_no_gap_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: at least 3 gaps in prior 21d but zero gaps in the last 5d (exhaustion)."""
    cond = _down_gap(close, open)
    cnt21 = _rolling_count_true(cond, _TD_MON)
    cnt5 = _rolling_count_true(cond, _TD_WEEK)
    return ((cnt21 >= 3) & (cnt5 == 0)).astype(float)


def gdc_137_gap_cluster_then_no_gap_10d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: at least 5 gaps in prior 63d but zero gaps in the last 10d (exhaustion)."""
    cond = _down_gap(close, open)
    cnt63 = _rolling_count_true(cond, _TD_QTR)
    cnt10 = _rolling_count_true(cond, 10)
    return ((cnt63 >= 5) & (cnt10 == 0)).astype(float)


def gdc_138_gap_density_decay_21_5(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day gap fraction minus 5-day gap fraction (cluster fading signal)."""
    f21 = _rolling_count_true(_down_gap(close, open), _TD_MON) / _TD_MON
    f5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK) / _TD_WEEK
    return f21 - f5


def gdc_139_gap_density_decay_63_21(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day gap fraction minus 21-day gap fraction (cluster fading over medium term)."""
    f63 = _rolling_count_true(_down_gap(close, open), _TD_QTR) / _TD_QTR
    f21 = _rolling_count_true(_down_gap(close, open), _TD_MON) / _TD_MON
    return f63 - f21


def gdc_140_gap_down_streak_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of current gap streak length vs 252-day mean/std of streak length."""
    streak = _consec_streak(_down_gap(close, open))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    return _safe_div(streak - m, s)


# --- Group O (141-150): Island Reversal — recency, magnitude, top-island, signatures ---

def gdc_141_days_since_island_bottom(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Bars elapsed since the last confirmed island-bottom reversal.
    Island-bottom: gap-down into cluster, gap-up out — confirmed at the exit gap.
    Recency of this signal matters for capitulation timing.
    """
    return _days_since_island_bottom(close, open)


def gdc_142_days_since_island_bottom_log(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log1p of bars since last island-bottom (compresses long waits)."""
    return np.log1p(_days_since_island_bottom(close, open))


def gdc_143_island_bottom_entry_plus_exit_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Combined magnitude: entry down-gap pct + exit up-gap pct on island-bottom days.
    Larger bracket gaps = more decisive island isolation. Zero on non-island days.
    """
    ug_pct = _up_gap_pct(close, open)
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    dg_pct = _down_gap_pct(close, open)
    entry_pct = pd.Series(0.0, index=close.index)
    flag = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        mask = ug & entry_gap & (flag == 0.0)
        entry_pct = entry_pct.where(~mask, dg_pct.shift(lag).fillna(0.0))
        flag = flag.where(~mask, 1.0)
    return (entry_pct + ug_pct) * flag


def gdc_144_island_top_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Island-top flag: gap-up into a cluster (1-5 bars ago) followed by gap-down today.
    Opposite of island-bottom; confirms a stranded price cluster at a top.
    Relevant as a context feature — recent tops increase capitulation likelihood.
    """
    return _island_top_flag(close, open)


def gdc_145_island_top_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of confirmed island-top patterns in the trailing 63 days."""
    return _rolling_sum(_island_top_flag(close, open), _TD_QTR)


def gdc_146_island_bottom_gap_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Ratio of exit up-gap pct to entry down-gap pct on island-bottom confirmation days.
    Ratio > 1 means the recovery gap is larger than the panic gap — strong reversal signal.
    Zero on non-island days.
    """
    ug_pct = _up_gap_pct(close, open)
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    dg_pct = _down_gap_pct(close, open)
    entry_pct = pd.Series(0.0, index=close.index)
    flag = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        mask = ug & entry_gap & (flag == 0.0)
        entry_pct = entry_pct.where(~mask, dg_pct.shift(lag).fillna(0.0))
        flag = flag.where(~mask, 1.0)
    return _safe_div(ug_pct * flag, entry_pct.replace(0, np.nan))


def gdc_147_island_bottom_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of island-bottom reversals in the trailing 21 days."""
    return _rolling_sum(_island_bottom_flag(close, open), _TD_MON)


def gdc_148_gap_down_then_gap_up_1bar_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Count of single-bar island bottoms (gap-down yesterday, gap-up today) in 63 days.
    The sharpest capitulation-reversal signature in the gap-clustering domain.
    """
    dg_lag1 = _down_gap(close, open).shift(1, fill_value=False)
    ug = _up_gap(close, open)
    flag = (ug & dg_lag1).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def gdc_149_island_bottom_ewm_decay_21(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    EWM (span=21) of island-bottom flags — recency-weighted island-reversal density.
    Higher values indicate frequent recent island-bottom patterns.
    """
    return _ewm_mean(_island_bottom_flag(close, open), _TD_MON)


def gdc_150_island_bottom_flag_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    21-day island-bottom count ranked as percentile within trailing 252 days.
    Captures whether the current pace of island reversals is historically elevated.
    """
    cnt21 = _rolling_sum(_island_bottom_flag(close, open), _TD_MON)
    return cnt21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_DOWN_CLUSTERING_REGISTRY_076_150 = {
    "gdc_076_gap_down_pct_zscore_21d": {"inputs": ["close", "open"], "func": gdc_076_gap_down_pct_zscore_21d},
    "gdc_077_gap_down_pct_zscore_63d": {"inputs": ["close", "open"], "func": gdc_077_gap_down_pct_zscore_63d},
    "gdc_078_gap_down_pct_zscore_252d": {"inputs": ["close", "open"], "func": gdc_078_gap_down_pct_zscore_252d},
    "gdc_079_sum_gap_pct_21d_zscore_252d": {"inputs": ["close", "open"], "func": gdc_079_sum_gap_pct_21d_zscore_252d},
    "gdc_080_gap_down_pct_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_080_gap_down_pct_pct_rank_252d},
    "gdc_081_gap_down_pct_pct_rank_63d": {"inputs": ["close", "open"], "func": gdc_081_gap_down_pct_pct_rank_63d},
    "gdc_082_max_gap_pct_252d_expanding_rank": {"inputs": ["close", "open"], "func": gdc_082_max_gap_pct_252d_expanding_rank},
    "gdc_083_gap_down_pct_ewm_21": {"inputs": ["close", "open"], "func": gdc_083_gap_down_pct_ewm_21},
    "gdc_084_gap_down_pct_ewm_63": {"inputs": ["close", "open"], "func": gdc_084_gap_down_pct_ewm_63},
    "gdc_085_gap_down_pct_std_21d": {"inputs": ["close", "open"], "func": gdc_085_gap_down_pct_std_21d},
    "gdc_086_vol_wtd_gap_pct_21d": {"inputs": ["close", "open", "volume"], "func": gdc_086_vol_wtd_gap_pct_21d},
    "gdc_087_vol_wtd_gap_pct_63d": {"inputs": ["close", "open", "volume"], "func": gdc_087_vol_wtd_gap_pct_63d},
    "gdc_088_vol_on_gap_down_avg_21d": {"inputs": ["close", "open", "volume"], "func": gdc_088_vol_on_gap_down_avg_21d},
    "gdc_089_vol_on_gap_down_avg_63d": {"inputs": ["close", "open", "volume"], "func": gdc_089_vol_on_gap_down_avg_63d},
    "gdc_090_vol_gap_vs_nongap_ratio_21d": {"inputs": ["close", "open", "volume"], "func": gdc_090_vol_gap_vs_nongap_ratio_21d},
    "gdc_091_vol_gap_vs_nongap_ratio_63d": {"inputs": ["close", "open", "volume"], "func": gdc_091_vol_gap_vs_nongap_ratio_63d},
    "gdc_092_high_vol_gap_down_count_21d": {"inputs": ["close", "open", "volume"], "func": gdc_092_high_vol_gap_down_count_21d},
    "gdc_093_high_vol_gap_down_count_63d": {"inputs": ["close", "open", "volume"], "func": gdc_093_high_vol_gap_down_count_63d},
    "gdc_094_gap_down_vol_pct_of_total_21d": {"inputs": ["close", "open", "volume"], "func": gdc_094_gap_down_vol_pct_of_total_21d},
    "gdc_095_gap_down_vol_pct_of_total_63d": {"inputs": ["close", "open", "volume"], "func": gdc_095_gap_down_vol_pct_of_total_63d},
    "gdc_096_gap_down_count_5d_diff_5d": {"inputs": ["close", "open"], "func": gdc_096_gap_down_count_5d_diff_5d},
    "gdc_097_gap_down_count_21d_diff_5d": {"inputs": ["close", "open"], "func": gdc_097_gap_down_count_21d_diff_5d},
    "gdc_098_gap_down_count_63d_diff_21d": {"inputs": ["close", "open"], "func": gdc_098_gap_down_count_63d_diff_21d},
    "gdc_099_consec_gap_down_streak_diff_5d": {"inputs": ["close", "open"], "func": gdc_099_consec_gap_down_streak_diff_5d},
    "gdc_100_cum_gap_pct_streak_diff_5d": {"inputs": ["close", "open"], "func": gdc_100_cum_gap_pct_streak_diff_5d},
    "gdc_101_gap_down_pct_21d_diff_5d": {"inputs": ["close", "open"], "func": gdc_101_gap_down_pct_21d_diff_5d},
    "gdc_102_gap_down_pct_63d_diff_21d": {"inputs": ["close", "open"], "func": gdc_102_gap_down_pct_63d_diff_21d},
    "gdc_103_gap_down_ewm21_diff_5d": {"inputs": ["close", "open"], "func": gdc_103_gap_down_ewm21_diff_5d},
    "gdc_104_gap_down_streak_start_freq_diff_21d": {"inputs": ["close", "open"], "func": gdc_104_gap_down_streak_start_freq_diff_21d},
    "gdc_105_gap_down_count_5d_vs_252d_zscore": {"inputs": ["close", "open"], "func": gdc_105_gap_down_count_5d_vs_252d_zscore},
    "gdc_106_gap_down_closed_same_day_count_21d": {"inputs": ["close", "open"], "func": gdc_106_gap_down_closed_same_day_count_21d},
    "gdc_107_gap_down_worsened_count_21d": {"inputs": ["close", "open"], "func": gdc_107_gap_down_worsened_count_21d},
    "gdc_108_gap_down_worsened_count_63d": {"inputs": ["close", "open"], "func": gdc_108_gap_down_worsened_count_63d},
    "gdc_109_gap_down_worsened_fraction_21d": {"inputs": ["close", "open"], "func": gdc_109_gap_down_worsened_fraction_21d},
    "gdc_110_gap_down_worsened_fraction_63d": {"inputs": ["close", "open"], "func": gdc_110_gap_down_worsened_fraction_63d},
    "gdc_111_consec_gap_worsened": {"inputs": ["close", "open"], "func": gdc_111_consec_gap_worsened},
    "gdc_112_gap_down_close_vs_open_avg_21d": {"inputs": ["close", "open"], "func": gdc_112_gap_down_close_vs_open_avg_21d},
    "gdc_113_gap_down_range_avg_21d": {"inputs": ["close", "open", "high", "low"], "func": gdc_113_gap_down_range_avg_21d},
    "gdc_114_gap_down_body_pct_21d": {"inputs": ["close", "open"], "func": gdc_114_gap_down_body_pct_21d},
    "gdc_115_gap_open_vs_prior_low_21d": {"inputs": ["close", "open", "low"], "func": gdc_115_gap_open_vs_prior_low_21d},
    "gdc_116_gap_cnt_21d_vs_63d_norm": {"inputs": ["close", "open"], "func": gdc_116_gap_cnt_21d_vs_63d_norm},
    "gdc_117_gap_cnt_5d_vs_21d_norm": {"inputs": ["close", "open"], "func": gdc_117_gap_cnt_5d_vs_21d_norm},
    "gdc_118_gap_cnt_63d_vs_252d_norm": {"inputs": ["close", "open"], "func": gdc_118_gap_cnt_63d_vs_252d_norm},
    "gdc_119_gap_pct_sum_21d_vs_63d_norm": {"inputs": ["close", "open"], "func": gdc_119_gap_pct_sum_21d_vs_63d_norm},
    "gdc_120_gap_pct_sum_63d_vs_252d_norm": {"inputs": ["close", "open"], "func": gdc_120_gap_pct_sum_63d_vs_252d_norm},
    "gdc_121_max_gap_pct_21d_vs_63d": {"inputs": ["close", "open"], "func": gdc_121_max_gap_pct_21d_vs_63d},
    "gdc_122_max_gap_pct_63d_vs_252d": {"inputs": ["close", "open"], "func": gdc_122_max_gap_pct_63d_vs_252d},
    "gdc_123_gap_down_streak_len_vs_avg_252d": {"inputs": ["close", "open"], "func": gdc_123_gap_down_streak_len_vs_avg_252d},
    "gdc_124_gap_cluster_score_composite": {"inputs": ["close", "open"], "func": gdc_124_gap_cluster_score_composite},
    "gdc_125_gap_cluster_score_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_125_gap_cluster_score_pct_rank_252d},
    "gdc_126_consec_gap_below_prior_low": {"inputs": ["close", "open", "low"], "func": gdc_126_consec_gap_below_prior_low},
    "gdc_127_count_gap_below_prior_low_21d": {"inputs": ["close", "open", "low"], "func": gdc_127_count_gap_below_prior_low_21d},
    "gdc_128_count_gap_below_prior_low_63d": {"inputs": ["close", "open", "low"], "func": gdc_128_count_gap_below_prior_low_63d},
    "gdc_129_gap_below_2d_low_count_21d": {"inputs": ["close", "open", "low"], "func": gdc_129_gap_below_2d_low_count_21d},
    "gdc_130_gap_below_5d_low_count_21d": {"inputs": ["close", "open", "low"], "func": gdc_130_gap_below_5d_low_count_21d},
    "gdc_131_gap_below_21d_low_count_63d": {"inputs": ["close", "open", "low"], "func": gdc_131_gap_below_21d_low_count_63d},
    "gdc_132_gap_down_below_low_fraction_21d": {"inputs": ["close", "open", "low"], "func": gdc_132_gap_down_below_low_fraction_21d},
    "gdc_133_gap_size_below_prior_low_avg_21d": {"inputs": ["close", "open", "low"], "func": gdc_133_gap_size_below_prior_low_avg_21d},
    "gdc_134_breakaway_gap_pct_avg_63d": {"inputs": ["close", "open", "low"], "func": gdc_134_breakaway_gap_pct_avg_63d},
    "gdc_135_breakaway_gap_down_flag_63d_count": {"inputs": ["close", "open", "low"], "func": gdc_135_breakaway_gap_down_flag_63d_count},
    "gdc_136_gap_cluster_then_no_gap_5d": {"inputs": ["close", "open"], "func": gdc_136_gap_cluster_then_no_gap_5d},
    "gdc_137_gap_cluster_then_no_gap_10d": {"inputs": ["close", "open"], "func": gdc_137_gap_cluster_then_no_gap_10d},
    "gdc_138_gap_density_decay_21_5": {"inputs": ["close", "open"], "func": gdc_138_gap_density_decay_21_5},
    "gdc_139_gap_density_decay_63_21": {"inputs": ["close", "open"], "func": gdc_139_gap_density_decay_63_21},
    "gdc_140_gap_down_streak_zscore_252d": {"inputs": ["close", "open"], "func": gdc_140_gap_down_streak_zscore_252d},
    "gdc_141_days_since_island_bottom": {"inputs": ["close", "open"], "func": gdc_141_days_since_island_bottom},
    "gdc_142_days_since_island_bottom_log": {"inputs": ["close", "open"], "func": gdc_142_days_since_island_bottom_log},
    "gdc_143_island_bottom_entry_plus_exit_gap_pct": {"inputs": ["close", "open"], "func": gdc_143_island_bottom_entry_plus_exit_gap_pct},
    "gdc_144_island_top_flag": {"inputs": ["close", "open"], "func": gdc_144_island_top_flag},
    "gdc_145_island_top_count_63d": {"inputs": ["close", "open"], "func": gdc_145_island_top_count_63d},
    "gdc_146_island_bottom_gap_ratio": {"inputs": ["close", "open"], "func": gdc_146_island_bottom_gap_ratio},
    "gdc_147_island_bottom_count_21d": {"inputs": ["close", "open"], "func": gdc_147_island_bottom_count_21d},
    "gdc_148_gap_down_then_gap_up_1bar_count_63d": {"inputs": ["close", "open"], "func": gdc_148_gap_down_then_gap_up_1bar_count_63d},
    "gdc_149_island_bottom_ewm_decay_21": {"inputs": ["close", "open"], "func": gdc_149_island_bottom_ewm_decay_21},
    "gdc_150_island_bottom_flag_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_150_island_bottom_flag_pct_rank_252d},
}
