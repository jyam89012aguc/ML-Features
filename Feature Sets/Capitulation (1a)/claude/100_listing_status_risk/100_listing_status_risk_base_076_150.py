"""
100_listing_status_risk — Base Features 076-200
Domain: exchange-tier risk and delisting proximity for distressed US equities
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to a shared trading-day
index.  Status fields (exchange_tier, delist_notice) are forward-filled.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Trading-day constants: 1 year = 252 td, 1 quarter = 63 td,
1 month = 21 td, 1 week = 5 td.

Inputs
------
exchange_tier : daily ordinal — 1=NYSE/NASDAQ Global Select, 2=NASDAQ Global/
                Capital Market, 3=NYSE American/regional, 4=OTCQX/OTCQB,
                5=Pink/Expert Market.  Higher = lower-tier / more distressed.
delist_notice : binary (1.0/0.0) — 1 when a delisting or listing-deficiency
                notice is in effect.
closeunadj    : raw unadjusted daily close price (USD); sub-$1 is delisting-
                relevant under exchange minimum-bid rules.
close         : split/dividend-adjusted daily close price (USD).
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
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator."""
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


def _streak_length(binary: pd.Series) -> pd.Series:
    """Current consecutive run length of 1s; resets to 0 on any 0."""
    arr    = binary.fillna(0).values.astype(int)
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=binary.index)


def _days_since_last_one(binary: pd.Series) -> pd.Series:
    """Days elapsed since the most recent 1; NaN if never seen."""
    arr    = binary.fillna(0).values.astype(float)
    result = np.full(len(arr), np.nan)
    last   = np.nan
    for i in range(len(arr)):
        if arr[i] == 1.0:
            last = 0.0
        elif not np.isnan(last):
            last += 1.0
        result[i] = last
    return pd.Series(result, index=binary.index)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Tier velocity, z-scores, percentile ranks ---

def lsr_076_tier_change_21d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over 21 trading days (positive = downgrade trend)."""
    return exchange_tier.astype(float) - exchange_tier.shift(_TD_MO).astype(float)


def lsr_077_tier_change_63d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over 63 trading days."""
    return exchange_tier.astype(float) - exchange_tier.shift(_TD_QTR).astype(float)


def lsr_078_tier_change_252d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over 252 trading days."""
    return exchange_tier.astype(float) - exchange_tier.shift(_TD_YEAR).astype(float)


def lsr_079_tier_zscore_252d(exchange_tier: pd.Series) -> pd.Series:
    """Z-score of exchange tier within trailing 252-day window."""
    return _zscore_rolling(exchange_tier.astype(float), _TD_YEAR)


def lsr_080_tier_zscore_504d(exchange_tier: pd.Series) -> pd.Series:
    """Z-score of exchange tier within trailing 504-day window."""
    return _zscore_rolling(exchange_tier.astype(float), _TD_2Y)


def lsr_081_tier_pct_rank_252d(exchange_tier: pd.Series) -> pd.Series:
    """Percentile rank of exchange tier within trailing 252-day window."""
    return _rolling_rank_pct(exchange_tier.astype(float), _TD_YEAR)


def lsr_082_tier_pct_rank_504d(exchange_tier: pd.Series) -> pd.Series:
    """Percentile rank of exchange tier within trailing 504-day window."""
    return _rolling_rank_pct(exchange_tier.astype(float), _TD_2Y)


def lsr_083_tier_expanding_zscore(exchange_tier: pd.Series) -> pd.Series:
    """All-history expanding z-score of exchange tier."""
    s  = exchange_tier.astype(float)
    m  = s.expanding(min_periods=2).mean()
    sd = s.expanding(min_periods=2).std()
    return _safe_div(s - m, sd)


def lsr_084_tier_expanding_pct_rank(exchange_tier: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of exchange tier."""
    return exchange_tier.astype(float).expanding(min_periods=2).rank(pct=True)


def lsr_085_tier_above_expanding_mean(exchange_tier: pd.Series) -> pd.Series:
    """Current tier minus all-history expanding mean tier."""
    s = exchange_tier.astype(float)
    return s - s.expanding(min_periods=1).mean()


def lsr_086_tier_rolling_std_63d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 63-day standard deviation of exchange tier (tier volatility)."""
    return _rolling_std(exchange_tier.astype(float), _TD_QTR)


def lsr_087_tier_rolling_std_252d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 252-day standard deviation of exchange tier."""
    return _rolling_std(exchange_tier.astype(float), _TD_YEAR)


def lsr_088_tier_median_252d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 252-day median exchange tier."""
    return _rolling_median(exchange_tier.astype(float), _TD_YEAR)


def lsr_089_tier_vs_median_252d(exchange_tier: pd.Series) -> pd.Series:
    """Current tier minus its 252-day rolling median."""
    s = exchange_tier.astype(float)
    return s - _rolling_median(s, _TD_YEAR)


def lsr_090_tier_min_252d(exchange_tier: pd.Series) -> pd.Series:
    """Lowest (best) tier visited in trailing 252 days."""
    return _rolling_min(exchange_tier.astype(float), _TD_YEAR)


# --- Group G (091-105): Notice recency, acceleration, ewm deviations ---

def lsr_091_notice_change_21d(delist_notice: pd.Series) -> pd.Series:
    """Change in delist-notice status over 21 days (onset=1, removal=-1, else 0)."""
    return delist_notice.astype(float) - delist_notice.shift(_TD_MO).astype(float)


def lsr_092_notice_change_63d(delist_notice: pd.Series) -> pd.Series:
    """Change in delist-notice status over 63 days."""
    return delist_notice.astype(float) - delist_notice.shift(_TD_QTR).astype(float)


def lsr_093_notice_fraction_21d(delist_notice: pd.Series) -> pd.Series:
    """Fraction of days under delist notice in trailing 21 days."""
    return _rolling_mean(delist_notice.astype(float), _TD_MO)


def lsr_094_notice_vs_ewm63(delist_notice: pd.Series) -> pd.Series:
    """Delist-notice flag minus its EWM (span=63) — deviation from recent trend."""
    n = delist_notice.astype(float)
    return n - _ewm_mean(n, _TD_QTR)


def lsr_095_notice_vs_ewm252(delist_notice: pd.Series) -> pd.Series:
    """Delist-notice flag minus its EWM (span=252)."""
    n = delist_notice.astype(float)
    return n - _ewm_mean(n, _TD_YEAR)


def lsr_096_notice_count_5y(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 1260 trading days (5 years)."""
    return _rolling_sum(delist_notice.astype(float), _TD_5Y)


def lsr_097_notice_spell_count_756d(delist_notice: pd.Series) -> pd.Series:
    """Number of distinct delist-notice spells in trailing 756 days."""
    onset = ((delist_notice == 1) & (delist_notice.shift(1).fillna(0) == 0)).astype(float)
    return _rolling_sum(onset, _TD_3Y)


def lsr_098_notice_days_126d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in the trailing 126-day window."""
    return _rolling_sum(delist_notice.astype(float), _TD_2Q)


def lsr_099_notice_fraction_126d(delist_notice: pd.Series) -> pd.Series:
    """Fraction of days under delist notice in trailing 126 days."""
    return _rolling_mean(delist_notice.astype(float), _TD_2Q)


def lsr_100_notice_fraction_756d(delist_notice: pd.Series) -> pd.Series:
    """Fraction of days under delist notice in trailing 756 days."""
    return _rolling_mean(delist_notice.astype(float), _TD_3Y)


def lsr_101_notice_max_streak_252d(delist_notice: pd.Series) -> pd.Series:
    """Longest active-notice streak (days) within trailing 252-day window."""
    streak = _streak_length(delist_notice.astype(float))
    return _rolling_max(streak, _TD_YEAR)


def lsr_102_notice_max_streak_504d(delist_notice: pd.Series) -> pd.Series:
    """Longest active-notice streak within trailing 504-day window."""
    streak = _streak_length(delist_notice.astype(float))
    return _rolling_max(streak, _TD_2Y)


def lsr_103_days_since_notice_end(delist_notice: pd.Series) -> pd.Series:
    """Days since the most recent delist-notice removal (0->1 transition); NaN if never."""
    removal = ((delist_notice == 0) & (delist_notice.shift(1).fillna(0) == 1)).astype(float)
    return _days_since_last_one(removal)


def lsr_104_notice_onset_flag(delist_notice: pd.Series) -> pd.Series:
    """Binary: 1 on the first day a new delist-notice spell begins."""
    return ((delist_notice == 1) & (delist_notice.shift(1).fillna(0) == 0)).astype(float)


def lsr_105_notice_removal_flag(delist_notice: pd.Series) -> pd.Series:
    """Binary: 1 on the day a delist-notice spell ends (removal)."""
    return ((delist_notice == 0) & (delist_notice.shift(1).fillna(0) == 1)).astype(float)


# --- Group H (106-120): Additional sub-$1/$2/$5 and closeunadj features ---

def lsr_106_sub1_days_126d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$1 days in trailing 126 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_2Q)


def lsr_107_sub1_days_504d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$1 days in trailing 504 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_2Y)


def lsr_108_sub1_fraction_126d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of sub-$1 days in trailing 126 days."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_2Q)


def lsr_109_sub1_fraction_504d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of sub-$1 days in trailing 504 days."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_2Y)


def lsr_110_sub2_days_63d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$2 days in trailing 63 trading days."""
    return _rolling_sum((closeunadj < 2.0).astype(float), _TD_QTR)


def lsr_111_sub2_days_252d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$2 days in trailing 252 trading days."""
    return _rolling_sum((closeunadj < 2.0).astype(float), _TD_YEAR)


def lsr_112_sub2_fraction_63d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of sub-$2 days in trailing 63 days."""
    return _rolling_mean((closeunadj < 2.0).astype(float), _TD_QTR)


def lsr_113_sub2_fraction_504d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of sub-$2 days in trailing 504 days."""
    return _rolling_mean((closeunadj < 2.0).astype(float), _TD_2Y)


def lsr_114_sub5_days_252d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$5 days in trailing 252 trading days."""
    return _rolling_sum((closeunadj < 5.0).astype(float), _TD_YEAR)


def lsr_115_sub5_fraction_504d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of sub-$5 days in trailing 504 days."""
    return _rolling_mean((closeunadj < 5.0).astype(float), _TD_2Y)


def lsr_116_closeunadj_min_252d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 252-day minimum of unadjusted close (trough price level)."""
    return _rolling_min(closeunadj, _TD_YEAR)


def lsr_117_closeunadj_min_504d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 504-day minimum of unadjusted close."""
    return _rolling_min(closeunadj, _TD_2Y)


def lsr_118_closeunadj_mean_252d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 252-day mean of unadjusted close."""
    return _rolling_mean(closeunadj, _TD_YEAR)


def lsr_119_closeunadj_vs_min_252d(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close minus its 252-day rolling minimum (distance from trough)."""
    return closeunadj - _rolling_min(closeunadj, _TD_YEAR)


def lsr_120_closeunadj_expanding_min(closeunadj: pd.Series) -> pd.Series:
    """All-time expanding minimum of unadjusted close."""
    return closeunadj.expanding(min_periods=1).min()


# --- Group I (121-135): Tier/notice interaction with price distress ---

def lsr_121_tier_x_notice_x_sub1(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """Triple interaction: tier * notice * sub-$1 flag (maximum stress indicator)."""
    return (
        exchange_tier.astype(float)
        * delist_notice.astype(float)
        * (closeunadj < 1.0).astype(float)
    )


def lsr_122_combined_distress_days_63d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """Days with notice active AND tier >= 3 in trailing 63 days."""
    joint = ((delist_notice == 1) & (exchange_tier >= 3)).astype(float)
    return _rolling_sum(joint, _TD_QTR)


def lsr_123_combined_distress_days_252d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """Days with notice active AND tier >= 3 in trailing 252 days."""
    joint = ((delist_notice == 1) & (exchange_tier >= 3)).astype(float)
    return _rolling_sum(joint, _TD_YEAR)


def lsr_124_notice_sub1_days_252d(
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """Days with notice AND sub-$1 in trailing 252 days."""
    joint = ((delist_notice == 1) & (closeunadj < 1.0)).astype(float)
    return _rolling_sum(joint, _TD_YEAR)


def lsr_125_tier4plus_sub1_days_252d(
    exchange_tier: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """Days at tier >= 4 AND sub-$1 in trailing 252 days."""
    joint = ((exchange_tier >= 4) & (closeunadj < 1.0)).astype(float)
    return _rolling_sum(joint, _TD_YEAR)


def lsr_126_distress_score_ewm63(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """EWM(63) of combined distress: tier + 2*notice + 3*sub1_flag."""
    score = (
        exchange_tier.astype(float)
        + 2.0 * delist_notice.astype(float)
        + 3.0 * (closeunadj < 1.0).astype(float)
    )
    return _ewm_mean(score, _TD_QTR)


def lsr_127_distress_score_ewm252(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """EWM(252) of combined distress score: tier + 2*notice + 3*sub1_flag."""
    score = (
        exchange_tier.astype(float)
        + 2.0 * delist_notice.astype(float)
        + 3.0 * (closeunadj < 1.0).astype(float)
    )
    return _ewm_mean(score, _TD_YEAR)


def lsr_128_notice_fraction_vs_ewm(delist_notice: pd.Series) -> pd.Series:
    """63-day notice fraction minus its own 252-day EWM (acceleration of notice exposure)."""
    frac = _rolling_mean(delist_notice.astype(float), _TD_QTR)
    return frac - _ewm_mean(frac, _TD_YEAR)


def lsr_129_tier_above_max_prior_year(exchange_tier: pd.Series) -> pd.Series:
    """Binary: 1 if current tier exceeds the highest tier of the prior year."""
    prior_max = _rolling_max(exchange_tier.shift(1).astype(float), _TD_YEAR)
    return (exchange_tier.astype(float) > prior_max).astype(float)


def lsr_130_closeunadj_below_expanding_min_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close is at a new all-time closing low."""
    prior_min = closeunadj.shift(1).expanding(min_periods=1).min()
    return (closeunadj < prior_min).astype(float)


def lsr_131_close_at_1y_low_flag(close: pd.Series) -> pd.Series:
    """Binary: 1 if adjusted close equals its 252-day rolling minimum."""
    low_1y = _rolling_min(close, _TD_YEAR)
    return (close <= low_1y + _EPS).astype(float)


def lsr_132_close_at_2y_low_flag(close: pd.Series) -> pd.Series:
    """Binary: 1 if adjusted close equals its 504-day rolling minimum."""
    low_2y = _rolling_min(close, _TD_2Y)
    return (close <= low_2y + _EPS).astype(float)


def lsr_133_close_at_3y_low_flag(close: pd.Series) -> pd.Series:
    """Binary: 1 if adjusted close equals its 756-day rolling minimum."""
    low_3y = _rolling_min(close, _TD_3Y)
    return (close <= low_3y + _EPS).astype(float)


def lsr_134_close_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of adjusted close within trailing 252-day window."""
    return _rolling_rank_pct(close, _TD_YEAR)


def lsr_135_close_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of adjusted close within trailing 504-day window."""
    return _rolling_rank_pct(close, _TD_2Y)


# --- Group J (136-150): Multi-window tier/notice cumulative, EWM combos ---

def lsr_136_tier_cumday_score_756d(exchange_tier: pd.Series) -> pd.Series:
    """Cumulative tier-day product over trailing 756 days."""
    return _rolling_sum(exchange_tier.astype(float), _TD_3Y)


def lsr_137_tier_ewm_deviation_63(exchange_tier: pd.Series) -> pd.Series:
    """Tier minus its EWM(63) — short-term tier momentum deviation."""
    s = exchange_tier.astype(float)
    return s - _ewm_mean(s, _TD_QTR)


def lsr_138_tier_ewm_deviation_252(exchange_tier: pd.Series) -> pd.Series:
    """Tier minus its EWM(252) — long-term tier momentum deviation."""
    s = exchange_tier.astype(float)
    return s - _ewm_mean(s, _TD_YEAR)


def lsr_139_notice_days_756d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 756 trading days."""
    return _rolling_sum(delist_notice.astype(float), _TD_3Y)


def lsr_140_tier_upgrade_count_252d(exchange_tier: pd.Series) -> pd.Series:
    """Count of tier upgrade events (tier decrease) in trailing 252 days."""
    flag = (exchange_tier < exchange_tier.shift(1)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def lsr_141_tier_net_change_252d(exchange_tier: pd.Series) -> pd.Series:
    """Net tier change (downgrades minus upgrades) over trailing 252 days."""
    down = (exchange_tier > exchange_tier.shift(1)).astype(float)
    up   = (exchange_tier < exchange_tier.shift(1)).astype(float)
    return _rolling_sum(down - up, _TD_YEAR)


def lsr_142_tier_change_velocity_63d(exchange_tier: pd.Series) -> pd.Series:
    """Mean daily tier change in the trailing 63-day window."""
    daily_chg = exchange_tier.astype(float).diff(1)
    return _rolling_mean(daily_chg, _TD_QTR)


def lsr_143_tier_change_velocity_252d(exchange_tier: pd.Series) -> pd.Series:
    """Mean daily tier change in the trailing 252-day window."""
    daily_chg = exchange_tier.astype(float).diff(1)
    return _rolling_mean(daily_chg, _TD_YEAR)


def lsr_144_sub1_spell_count_504d(closeunadj: pd.Series) -> pd.Series:
    """Number of distinct sub-$1 spells (onset events) in trailing 504 days."""
    onset = ((closeunadj < 1.0) & (closeunadj.shift(1).fillna(1.0) >= 1.0)).astype(float)
    return _rolling_sum(onset, _TD_2Y)


def lsr_145_sub2_spell_count_504d(closeunadj: pd.Series) -> pd.Series:
    """Number of distinct sub-$2 spells in trailing 504 days."""
    onset = ((closeunadj < 2.0) & (closeunadj.shift(1).fillna(2.0) >= 2.0)).astype(float)
    return _rolling_sum(onset, _TD_2Y)


def lsr_146_closeunadj_zscore_504d(closeunadj: pd.Series) -> pd.Series:
    """Z-score of unadjusted close within trailing 504-day window."""
    return _zscore_rolling(closeunadj, _TD_2Y)


def lsr_147_close_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of adjusted close within trailing 252-day window."""
    return _zscore_rolling(close, _TD_YEAR)


def lsr_148_close_drawdown_3y(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its 756-day rolling peak."""
    peak = _rolling_max(close, _TD_3Y)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def lsr_149_tier_notice_score_mean_252d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """Rolling 252-day mean of (tier + 2*notice) additive distress score."""
    score = exchange_tier.astype(float) + 2.0 * delist_notice.astype(float)
    return _rolling_mean(score, _TD_YEAR)


def lsr_150_full_distress_composite(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """
    Full listing-distress composite: z-scored tier (252d) + 2*notice_fraction_252d
    + sub-$1 fraction (252d) + price drawdown z-score (252d, sign-inverted).
    """
    z_tier    = _zscore_rolling(exchange_tier.astype(float), _TD_YEAR)
    nf        = _rolling_mean(delist_notice.astype(float), _TD_YEAR)
    sub1_frac = _rolling_mean((closeunadj < 1.0).astype(float), _TD_YEAR)
    dd        = _safe_div(close - _rolling_max(close, _TD_YEAR),
                          _rolling_max(close, _TD_YEAR).replace(0, np.nan))
    z_dd      = _zscore_rolling(dd.fillna(0), _TD_YEAR)
    return z_tier + 2.0 * nf + sub1_frac - z_dd


# --- Group K (176-200): Tier/notice/price extended constructions ---

def lsr_176_tier_change_126d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over 126 trading days (half-year tier drift)."""
    return exchange_tier.astype(float) - exchange_tier.shift(_TD_2Q).astype(float)


def lsr_177_tier_change_504d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over 504 trading days (2-year tier drift)."""
    return exchange_tier.astype(float) - exchange_tier.shift(_TD_2Y).astype(float)


def lsr_178_tier_ewm_span21(exchange_tier: pd.Series) -> pd.Series:
    """EWM-smoothed exchange tier (span=21); captures very short-run tier trend."""
    return _ewm_mean(exchange_tier.astype(float), _TD_MO)


def lsr_179_tier_ewm21_deviation(exchange_tier: pd.Series) -> pd.Series:
    """Tier minus its EWM(21) — very short-term tier deviation."""
    s = exchange_tier.astype(float)
    return s - _ewm_mean(s, _TD_MO)


def lsr_180_tier_rolling_std_126d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 126-day standard deviation of exchange tier."""
    return _rolling_std(exchange_tier.astype(float), _TD_2Q)


def lsr_181_tier_median_63d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 63-day median exchange tier."""
    return _rolling_median(exchange_tier.astype(float), _TD_QTR)


def lsr_182_tier_vs_median_63d(exchange_tier: pd.Series) -> pd.Series:
    """Current tier minus its 63-day rolling median."""
    s = exchange_tier.astype(float)
    return s - _rolling_median(s, _TD_QTR)


def lsr_183_tier_cumday_score_126d(exchange_tier: pd.Series) -> pd.Series:
    """Cumulative tier-day product over trailing 126 days."""
    return _rolling_sum(exchange_tier.astype(float), _TD_2Q)


def lsr_184_tier_net_change_63d(exchange_tier: pd.Series) -> pd.Series:
    """Net tier change (downgrades minus upgrades) over trailing 63 days."""
    down = (exchange_tier > exchange_tier.shift(1)).astype(float)
    up   = (exchange_tier < exchange_tier.shift(1)).astype(float)
    return _rolling_sum(down - up, _TD_QTR)


def lsr_185_tier_upgrade_count_63d(exchange_tier: pd.Series) -> pd.Series:
    """Count of tier upgrade events (tier decrease) in trailing 63 days."""
    flag = (exchange_tier < exchange_tier.shift(1)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def lsr_186_notice_days_21d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 21 trading days (alias for clarity)."""
    return _rolling_sum(delist_notice.astype(float), _TD_MO)


def lsr_187_notice_expanding_max_streak(delist_notice: pd.Series) -> pd.Series:
    """All-history expanding maximum consecutive delist-notice spell length."""
    streak = _streak_length(delist_notice)
    return streak.expanding(min_periods=1).max()


def lsr_188_notice_onset_count_63d(delist_notice: pd.Series) -> pd.Series:
    """Count of distinct delist-notice spell onsets in trailing 63 days."""
    onset = ((delist_notice == 1) & (delist_notice.shift(1).fillna(0) == 0)).astype(float)
    return _rolling_sum(onset, _TD_QTR)


def lsr_189_notice_onset_count_126d(delist_notice: pd.Series) -> pd.Series:
    """Count of distinct delist-notice spell onsets in trailing 126 days."""
    onset = ((delist_notice == 1) & (delist_notice.shift(1).fillna(0) == 0)).astype(float)
    return _rolling_sum(onset, _TD_2Q)


def lsr_190_sub1_longest_spell_126d(closeunadj: pd.Series) -> pd.Series:
    """Longest consecutive sub-$1 spell within trailing 126-day window."""
    streak = _streak_length((closeunadj < 1.0).astype(float))
    return _rolling_max(streak, _TD_2Q)


def lsr_191_sub2_longest_spell_252d(closeunadj: pd.Series) -> pd.Series:
    """Longest consecutive sub-$2 spell within trailing 252-day window."""
    streak = _streak_length((closeunadj < 2.0).astype(float))
    return _rolling_max(streak, _TD_YEAR)


def lsr_192_sub5_fraction_63d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $5.00 in trailing 63 days."""
    return _rolling_mean((closeunadj < 5.0).astype(float), _TD_QTR)


def lsr_193_closeunadj_mean_63d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 63-day mean of unadjusted close."""
    return _rolling_mean(closeunadj, _TD_QTR)


def lsr_194_closeunadj_vs_mean_252d(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close minus its 252-day rolling mean (mean-reversion signal)."""
    return closeunadj - _rolling_mean(closeunadj, _TD_YEAR)


def lsr_195_close_min_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day minimum of adjusted close."""
    return _rolling_min(close, _TD_YEAR)


def lsr_196_close_drawdown_126d(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its 126-day rolling peak."""
    peak = _rolling_max(close, _TD_2Q)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def lsr_197_tier_notice_score_mean_63d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """Rolling 63-day mean of (tier + 2*notice) additive distress score."""
    score = exchange_tier.astype(float) + 2.0 * delist_notice.astype(float)
    return _rolling_mean(score, _TD_QTR)


def lsr_198_combined_distress_fraction_252d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """Fraction of days with notice active AND tier >= 3 in trailing 252 days."""
    joint = ((delist_notice == 1) & (exchange_tier >= 3)).astype(float)
    return _rolling_mean(joint, _TD_YEAR)


def lsr_199_tier5_notice_joint_252d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """Days at tier == 5 AND notice active in trailing 252 days (maximum distress count)."""
    joint = ((exchange_tier == 5) & (delist_notice == 1)).astype(float)
    return _rolling_sum(joint, _TD_YEAR)


def lsr_200_extreme_distress_composite(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """
    Extreme distress composite: EWM(21) of (tier==5)*3 + notice*2 + sub-$1 flag
    + abs(drawdown_2y).  Sensitive to Pink-tier and sub-$1 co-occurrence.
    """
    tier5   = (exchange_tier == 5).astype(float)
    sub1    = (closeunadj < 1.0).astype(float)
    peak    = _rolling_max(close, _TD_2Y)
    dd      = _safe_div(close - peak, peak.replace(0, np.nan)).abs()
    raw     = 3.0 * tier5 + 2.0 * delist_notice.astype(float) + sub1 + dd
    return _ewm_mean(raw, _TD_MO)


# ── Registry 076-150 ──────────────────────────────────────────────────────────

LISTING_STATUS_RISK_REGISTRY_076_150 = {
    "lsr_076_tier_change_21d":              {"inputs": ["exchange_tier"],                                       "func": lsr_076_tier_change_21d},
    "lsr_077_tier_change_63d":              {"inputs": ["exchange_tier"],                                       "func": lsr_077_tier_change_63d},
    "lsr_078_tier_change_252d":             {"inputs": ["exchange_tier"],                                       "func": lsr_078_tier_change_252d},
    "lsr_079_tier_zscore_252d":             {"inputs": ["exchange_tier"],                                       "func": lsr_079_tier_zscore_252d},
    "lsr_080_tier_zscore_504d":             {"inputs": ["exchange_tier"],                                       "func": lsr_080_tier_zscore_504d},
    "lsr_081_tier_pct_rank_252d":           {"inputs": ["exchange_tier"],                                       "func": lsr_081_tier_pct_rank_252d},
    "lsr_082_tier_pct_rank_504d":           {"inputs": ["exchange_tier"],                                       "func": lsr_082_tier_pct_rank_504d},
    "lsr_083_tier_expanding_zscore":        {"inputs": ["exchange_tier"],                                       "func": lsr_083_tier_expanding_zscore},
    "lsr_084_tier_expanding_pct_rank":      {"inputs": ["exchange_tier"],                                       "func": lsr_084_tier_expanding_pct_rank},
    "lsr_085_tier_above_expanding_mean":    {"inputs": ["exchange_tier"],                                       "func": lsr_085_tier_above_expanding_mean},
    "lsr_086_tier_rolling_std_63d":         {"inputs": ["exchange_tier"],                                       "func": lsr_086_tier_rolling_std_63d},
    "lsr_087_tier_rolling_std_252d":        {"inputs": ["exchange_tier"],                                       "func": lsr_087_tier_rolling_std_252d},
    "lsr_088_tier_median_252d":             {"inputs": ["exchange_tier"],                                       "func": lsr_088_tier_median_252d},
    "lsr_089_tier_vs_median_252d":          {"inputs": ["exchange_tier"],                                       "func": lsr_089_tier_vs_median_252d},
    "lsr_090_tier_min_252d":                {"inputs": ["exchange_tier"],                                       "func": lsr_090_tier_min_252d},
    "lsr_091_notice_change_21d":            {"inputs": ["delist_notice"],                                       "func": lsr_091_notice_change_21d},
    "lsr_092_notice_change_63d":            {"inputs": ["delist_notice"],                                       "func": lsr_092_notice_change_63d},
    "lsr_093_notice_fraction_21d":          {"inputs": ["delist_notice"],                                       "func": lsr_093_notice_fraction_21d},
    "lsr_094_notice_vs_ewm63":              {"inputs": ["delist_notice"],                                       "func": lsr_094_notice_vs_ewm63},
    "lsr_095_notice_vs_ewm252":             {"inputs": ["delist_notice"],                                       "func": lsr_095_notice_vs_ewm252},
    "lsr_096_notice_count_5y":              {"inputs": ["delist_notice"],                                       "func": lsr_096_notice_count_5y},
    "lsr_097_notice_spell_count_756d":      {"inputs": ["delist_notice"],                                       "func": lsr_097_notice_spell_count_756d},
    "lsr_098_notice_days_126d":             {"inputs": ["delist_notice"],                                       "func": lsr_098_notice_days_126d},
    "lsr_099_notice_fraction_126d":         {"inputs": ["delist_notice"],                                       "func": lsr_099_notice_fraction_126d},
    "lsr_100_notice_fraction_756d":         {"inputs": ["delist_notice"],                                       "func": lsr_100_notice_fraction_756d},
    "lsr_101_notice_max_streak_252d":       {"inputs": ["delist_notice"],                                       "func": lsr_101_notice_max_streak_252d},
    "lsr_102_notice_max_streak_504d":       {"inputs": ["delist_notice"],                                       "func": lsr_102_notice_max_streak_504d},
    "lsr_103_days_since_notice_end":        {"inputs": ["delist_notice"],                                       "func": lsr_103_days_since_notice_end},
    "lsr_104_notice_onset_flag":            {"inputs": ["delist_notice"],                                       "func": lsr_104_notice_onset_flag},
    "lsr_105_notice_removal_flag":          {"inputs": ["delist_notice"],                                       "func": lsr_105_notice_removal_flag},
    "lsr_106_sub1_days_126d":               {"inputs": ["closeunadj"],                                          "func": lsr_106_sub1_days_126d},
    "lsr_107_sub1_days_504d":               {"inputs": ["closeunadj"],                                          "func": lsr_107_sub1_days_504d},
    "lsr_108_sub1_fraction_126d":           {"inputs": ["closeunadj"],                                          "func": lsr_108_sub1_fraction_126d},
    "lsr_109_sub1_fraction_504d":           {"inputs": ["closeunadj"],                                          "func": lsr_109_sub1_fraction_504d},
    "lsr_110_sub2_days_63d":                {"inputs": ["closeunadj"],                                          "func": lsr_110_sub2_days_63d},
    "lsr_111_sub2_days_252d":               {"inputs": ["closeunadj"],                                          "func": lsr_111_sub2_days_252d},
    "lsr_112_sub2_fraction_63d":            {"inputs": ["closeunadj"],                                          "func": lsr_112_sub2_fraction_63d},
    "lsr_113_sub2_fraction_504d":           {"inputs": ["closeunadj"],                                          "func": lsr_113_sub2_fraction_504d},
    "lsr_114_sub5_days_252d":               {"inputs": ["closeunadj"],                                          "func": lsr_114_sub5_days_252d},
    "lsr_115_sub5_fraction_504d":           {"inputs": ["closeunadj"],                                          "func": lsr_115_sub5_fraction_504d},
    "lsr_116_closeunadj_min_252d":          {"inputs": ["closeunadj"],                                          "func": lsr_116_closeunadj_min_252d},
    "lsr_117_closeunadj_min_504d":          {"inputs": ["closeunadj"],                                          "func": lsr_117_closeunadj_min_504d},
    "lsr_118_closeunadj_mean_252d":         {"inputs": ["closeunadj"],                                          "func": lsr_118_closeunadj_mean_252d},
    "lsr_119_closeunadj_vs_min_252d":       {"inputs": ["closeunadj"],                                          "func": lsr_119_closeunadj_vs_min_252d},
    "lsr_120_closeunadj_expanding_min":     {"inputs": ["closeunadj"],                                          "func": lsr_120_closeunadj_expanding_min},
    "lsr_121_tier_x_notice_x_sub1":        {"inputs": ["exchange_tier", "delist_notice", "closeunadj"],        "func": lsr_121_tier_x_notice_x_sub1},
    "lsr_122_combined_distress_days_63d":   {"inputs": ["exchange_tier", "delist_notice"],                      "func": lsr_122_combined_distress_days_63d},
    "lsr_123_combined_distress_days_252d":  {"inputs": ["exchange_tier", "delist_notice"],                      "func": lsr_123_combined_distress_days_252d},
    "lsr_124_notice_sub1_days_252d":        {"inputs": ["delist_notice", "closeunadj"],                         "func": lsr_124_notice_sub1_days_252d},
    "lsr_125_tier4plus_sub1_days_252d":     {"inputs": ["exchange_tier", "closeunadj"],                         "func": lsr_125_tier4plus_sub1_days_252d},
    "lsr_126_distress_score_ewm63":         {"inputs": ["exchange_tier", "delist_notice", "closeunadj"],        "func": lsr_126_distress_score_ewm63},
    "lsr_127_distress_score_ewm252":        {"inputs": ["exchange_tier", "delist_notice", "closeunadj"],        "func": lsr_127_distress_score_ewm252},
    "lsr_128_notice_fraction_vs_ewm":       {"inputs": ["delist_notice"],                                       "func": lsr_128_notice_fraction_vs_ewm},
    "lsr_129_tier_above_max_prior_year":    {"inputs": ["exchange_tier"],                                       "func": lsr_129_tier_above_max_prior_year},
    "lsr_130_closeunadj_below_expanding_min_flag": {"inputs": ["closeunadj"],                                   "func": lsr_130_closeunadj_below_expanding_min_flag},
    "lsr_131_close_at_1y_low_flag":         {"inputs": ["close"],                                               "func": lsr_131_close_at_1y_low_flag},
    "lsr_132_close_at_2y_low_flag":         {"inputs": ["close"],                                               "func": lsr_132_close_at_2y_low_flag},
    "lsr_133_close_at_3y_low_flag":         {"inputs": ["close"],                                               "func": lsr_133_close_at_3y_low_flag},
    "lsr_134_close_pct_rank_252d":          {"inputs": ["close"],                                               "func": lsr_134_close_pct_rank_252d},
    "lsr_135_close_pct_rank_504d":          {"inputs": ["close"],                                               "func": lsr_135_close_pct_rank_504d},
    "lsr_136_tier_cumday_score_756d":       {"inputs": ["exchange_tier"],                                       "func": lsr_136_tier_cumday_score_756d},
    "lsr_137_tier_ewm_deviation_63":        {"inputs": ["exchange_tier"],                                       "func": lsr_137_tier_ewm_deviation_63},
    "lsr_138_tier_ewm_deviation_252":       {"inputs": ["exchange_tier"],                                       "func": lsr_138_tier_ewm_deviation_252},
    "lsr_139_notice_days_756d":             {"inputs": ["delist_notice"],                                       "func": lsr_139_notice_days_756d},
    "lsr_140_tier_upgrade_count_252d":      {"inputs": ["exchange_tier"],                                       "func": lsr_140_tier_upgrade_count_252d},
    "lsr_141_tier_net_change_252d":         {"inputs": ["exchange_tier"],                                       "func": lsr_141_tier_net_change_252d},
    "lsr_142_tier_change_velocity_63d":     {"inputs": ["exchange_tier"],                                       "func": lsr_142_tier_change_velocity_63d},
    "lsr_143_tier_change_velocity_252d":    {"inputs": ["exchange_tier"],                                       "func": lsr_143_tier_change_velocity_252d},
    "lsr_144_sub1_spell_count_504d":        {"inputs": ["closeunadj"],                                          "func": lsr_144_sub1_spell_count_504d},
    "lsr_145_sub2_spell_count_504d":        {"inputs": ["closeunadj"],                                          "func": lsr_145_sub2_spell_count_504d},
    "lsr_146_closeunadj_zscore_504d":       {"inputs": ["closeunadj"],                                          "func": lsr_146_closeunadj_zscore_504d},
    "lsr_147_close_zscore_252d":            {"inputs": ["close"],                                               "func": lsr_147_close_zscore_252d},
    "lsr_148_close_drawdown_3y":            {"inputs": ["close"],                                               "func": lsr_148_close_drawdown_3y},
    "lsr_149_tier_notice_score_mean_252d":  {"inputs": ["exchange_tier", "delist_notice"],                      "func": lsr_149_tier_notice_score_mean_252d},
    "lsr_150_full_distress_composite":      {"inputs": ["exchange_tier", "delist_notice", "closeunadj", "close"], "func": lsr_150_full_distress_composite},
    "lsr_176_tier_change_126d":             {"inputs": ["exchange_tier"],                                         "func": lsr_176_tier_change_126d},
    "lsr_177_tier_change_504d":             {"inputs": ["exchange_tier"],                                         "func": lsr_177_tier_change_504d},
    "lsr_178_tier_ewm_span21":              {"inputs": ["exchange_tier"],                                         "func": lsr_178_tier_ewm_span21},
    "lsr_179_tier_ewm21_deviation":         {"inputs": ["exchange_tier"],                                         "func": lsr_179_tier_ewm21_deviation},
    "lsr_180_tier_rolling_std_126d":        {"inputs": ["exchange_tier"],                                         "func": lsr_180_tier_rolling_std_126d},
    "lsr_181_tier_median_63d":              {"inputs": ["exchange_tier"],                                         "func": lsr_181_tier_median_63d},
    "lsr_182_tier_vs_median_63d":           {"inputs": ["exchange_tier"],                                         "func": lsr_182_tier_vs_median_63d},
    "lsr_183_tier_cumday_score_126d":       {"inputs": ["exchange_tier"],                                         "func": lsr_183_tier_cumday_score_126d},
    "lsr_184_tier_net_change_63d":          {"inputs": ["exchange_tier"],                                         "func": lsr_184_tier_net_change_63d},
    "lsr_185_tier_upgrade_count_63d":       {"inputs": ["exchange_tier"],                                         "func": lsr_185_tier_upgrade_count_63d},
    "lsr_186_notice_days_21d":              {"inputs": ["delist_notice"],                                         "func": lsr_186_notice_days_21d},
    "lsr_187_notice_expanding_max_streak":  {"inputs": ["delist_notice"],                                         "func": lsr_187_notice_expanding_max_streak},
    "lsr_188_notice_onset_count_63d":       {"inputs": ["delist_notice"],                                         "func": lsr_188_notice_onset_count_63d},
    "lsr_189_notice_onset_count_126d":      {"inputs": ["delist_notice"],                                         "func": lsr_189_notice_onset_count_126d},
    "lsr_190_sub1_longest_spell_126d":      {"inputs": ["closeunadj"],                                            "func": lsr_190_sub1_longest_spell_126d},
    "lsr_191_sub2_longest_spell_252d":      {"inputs": ["closeunadj"],                                            "func": lsr_191_sub2_longest_spell_252d},
    "lsr_192_sub5_fraction_63d":            {"inputs": ["closeunadj"],                                            "func": lsr_192_sub5_fraction_63d},
    "lsr_193_closeunadj_mean_63d":          {"inputs": ["closeunadj"],                                            "func": lsr_193_closeunadj_mean_63d},
    "lsr_194_closeunadj_vs_mean_252d":      {"inputs": ["closeunadj"],                                            "func": lsr_194_closeunadj_vs_mean_252d},
    "lsr_195_close_min_252d":               {"inputs": ["close"],                                                 "func": lsr_195_close_min_252d},
    "lsr_196_close_drawdown_126d":          {"inputs": ["close"],                                                 "func": lsr_196_close_drawdown_126d},
    "lsr_197_tier_notice_score_mean_63d":   {"inputs": ["exchange_tier", "delist_notice"],                        "func": lsr_197_tier_notice_score_mean_63d},
    "lsr_198_combined_distress_fraction_252d": {"inputs": ["exchange_tier", "delist_notice"],                     "func": lsr_198_combined_distress_fraction_252d},
    "lsr_199_tier5_notice_joint_252d":      {"inputs": ["exchange_tier", "delist_notice"],                        "func": lsr_199_tier5_notice_joint_252d},
    "lsr_200_extreme_distress_composite":   {"inputs": ["exchange_tier", "delist_notice", "closeunadj", "close"], "func": lsr_200_extreme_distress_composite},
}
