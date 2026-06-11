"""
97_reverse_split_signal — Extended Features 001-075
Domain: reverse splits as late-stage distress flags — additional angles: split-gap timing,
        post-split sub-threshold relapse, magnitude percentiles, cumulative-factor drawdowns,
        nominal-price streak depths, RS clustering composites
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to one shared daily
trading-day index.  Functions look strictly backward using .shift(positive),
.rolling(), or .expanding().  Trading-day constants: 1 year = 252 td,
1 quarter = 63 td, 1 month = 21 td, 1 week = 5 td.

  split_factor  : per-day split factor; 1.0 on normal days.
                  < 1.0 on reverse-split effective dates (e.g. 1-for-10 -> 0.1).
                  > 1.0 on forward-split effective dates (e.g. 2-for-1 -> 2.0).
  closeunadj    : raw unadjusted daily close price (USD); nominally raised by
                  reverse splits; driven toward sub-$1 by distress.
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


def _is_reverse_split(split_factor: pd.Series) -> pd.Series:
    """Binary indicator: 1 on days where split_factor < 1 (reverse split), else 0."""
    return (split_factor < 1.0).astype(float)


def _is_forward_split(split_factor: pd.Series) -> pd.Series:
    """Binary indicator: 1 on days where split_factor > 1 (forward split), else 0."""
    return (split_factor > 1.0).astype(float)


def _reverse_split_magnitude(split_factor: pd.Series) -> pd.Series:
    """Reverse-split magnitude: 1/split_factor on RS days, NaN otherwise."""
    rs = split_factor.copy().astype(float)
    rs[rs >= 1.0] = np.nan
    return 1.0 / rs.replace(0, np.nan)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum().astype(float)


def _days_since_event(flag: pd.Series) -> pd.Series:
    """Trading days since flag last equalled 1 (NaN before any event)."""
    arr = flag.values
    out = np.full(len(arr), np.nan)
    last = -1
    for i in range(len(arr)):
        if arr[i] == 1.0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=flag.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Split-gap timing and inter-event spacing ---

def rss_ext_001_days_since_any_split(split_factor: pd.Series) -> pd.Series:
    """Trading days since the most recent split of any kind (NaN if none yet)."""
    any_split = (split_factor != 1.0).astype(float)
    return _days_since_event(any_split)


def rss_ext_002_rs_within_31d_flag(split_factor: pd.Series) -> pd.Series:
    """1 if any reverse split occurred in the trailing 31 trading days."""
    return (_rolling_sum(_is_reverse_split(split_factor), 31) > 0).astype(float)


def rss_ext_003_rs_within_756d_flag(split_factor: pd.Series) -> pd.Series:
    """1 if any reverse split occurred in the trailing 756 trading days."""
    return (_rolling_sum(_is_reverse_split(split_factor), _TD_3Y) > 0).astype(float)


def rss_ext_004_rs_within_1260d_flag(split_factor: pd.Series) -> pd.Series:
    """1 if any reverse split occurred in the trailing 1260 trading days (5 years)."""
    return (_rolling_sum(_is_reverse_split(split_factor), _TD_5Y) > 0).astype(float)


def rss_ext_005_days_since_rs_capped_252(split_factor: pd.Series) -> pd.Series:
    """Days since last reverse split, capped at 252 (recency saturated at 1 year)."""
    raw = _days_since_event(_is_reverse_split(split_factor))
    return raw.clip(upper=float(_TD_YEAR))


def rss_ext_006_rs_recency_inverse(split_factor: pd.Series) -> pd.Series:
    """Inverse-recency score 1/(1+days since last reverse split); high right after an RS."""
    raw = _days_since_event(_is_reverse_split(split_factor))
    return 1.0 / (1.0 + raw)


def rss_ext_007_rs_inter_arrival_gap(split_factor: pd.Series) -> pd.Series:
    """Trading-day gap between the two most recent reverse splits (NaN until 2 exist)."""
    rs = _is_reverse_split(split_factor).values
    idxs = [i for i in range(len(rs)) if rs[i] == 1.0]
    out = np.full(len(rs), np.nan)
    if len(idxs) >= 2:
        for k in range(1, len(idxs)):
            gap = float(idxs[k] - idxs[k - 1])
            start = idxs[k]
            end = idxs[k + 1] if k + 1 < len(idxs) else len(rs)
            out[start:end] = gap
    return pd.Series(out, index=split_factor.index)


def rss_ext_008_days_since_rs_log1p_capped(split_factor: pd.Series) -> pd.Series:
    """Log(1 + days since last reverse split), capped at log1p(1260)."""
    raw = _days_since_event(_is_reverse_split(split_factor))
    return np.log1p(raw.clip(upper=float(_TD_5Y)))


def rss_ext_009_rs_recency_decay_fast(split_factor: pd.Series) -> pd.Series:
    """EWM-decayed reverse-split flag with fast decay (span=21)."""
    return _ewm_mean(_is_reverse_split(split_factor), _TD_MO)


def rss_ext_010_rs_recency_decay_medium(split_factor: pd.Series) -> pd.Series:
    """EWM-decayed reverse-split flag with medium decay (span=126)."""
    return _ewm_mean(_is_reverse_split(split_factor), _TD_2Q)


def rss_ext_011_any_split_within_63d_flag(split_factor: pd.Series) -> pd.Series:
    """1 if any split of either direction occurred in the trailing 63 trading days."""
    any_split = (split_factor != 1.0).astype(float)
    return (_rolling_sum(any_split, _TD_QTR) > 0).astype(float)


def rss_ext_012_days_since_rs_over_63d_flag(split_factor: pd.Series) -> pd.Series:
    """1 when the most recent reverse split was more than 63 days ago (post-split window)."""
    raw = _days_since_event(_is_reverse_split(split_factor))
    return (raw > float(_TD_QTR)).fillna(False).astype(float)


# --- Group B (013-024): Reverse-split magnitude distributions ---

def rss_ext_013_rs_magnitude_filled(split_factor: pd.Series) -> pd.Series:
    """Reverse-split magnitude (1/sf) on RS days, forward-filled to carry last magnitude."""
    return _reverse_split_magnitude(split_factor).ffill()


def rss_ext_014_rs_magnitude_last(split_factor: pd.Series) -> pd.Series:
    """Magnitude of the most recent reverse split, held until the next one (0 before any)."""
    return _reverse_split_magnitude(split_factor).ffill().fillna(0.0)


def rss_ext_015_rs_magnitude_mean_252d(split_factor: pd.Series) -> pd.Series:
    """Mean reverse-split magnitude across RS days in trailing 252 days (NaN if none)."""
    mag = _reverse_split_magnitude(split_factor)
    rs = _is_reverse_split(split_factor)
    num = _rolling_sum(mag.fillna(0.0) * rs, _TD_YEAR)
    den = _rolling_sum(rs, _TD_YEAR)
    return _safe_div(num, den)


def rss_ext_016_rs_magnitude_sum_504d(split_factor: pd.Series) -> pd.Series:
    """Sum of reverse-split magnitudes across RS days in trailing 504 days."""
    mag = _reverse_split_magnitude(split_factor).fillna(0.0)
    return _rolling_sum(mag, _TD_2Y)


def rss_ext_017_rs_log_magnitude_sum_756d(split_factor: pd.Series) -> pd.Series:
    """Sum of log reverse-split magnitudes across RS days in trailing 756 days."""
    mag = _reverse_split_magnitude(split_factor)
    logmag = np.log(mag.replace(0, np.nan)).fillna(0.0)
    return _rolling_sum(logmag, _TD_3Y)


def rss_ext_018_rs_magnitude_pct_rank_756d(split_factor: pd.Series) -> pd.Series:
    """Percentile rank of current carried RS magnitude within trailing 756 days."""
    mag = _reverse_split_magnitude(split_factor).ffill().fillna(0.0)
    return _rolling_rank_pct(mag, _TD_3Y)


def rss_ext_019_rs_magnitude_max_756d(split_factor: pd.Series) -> pd.Series:
    """Maximum reverse-split magnitude observed in trailing 756 days."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _rolling_max(mag, _TD_3Y)


def rss_ext_020_rs_magnitude_max_1260d(split_factor: pd.Series) -> pd.Series:
    """Maximum reverse-split magnitude observed in trailing 1260 days."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _rolling_max(mag, _TD_5Y)


def rss_ext_021_rs_severity_gte50_flag(split_factor: pd.Series) -> pd.Series:
    """1 on days with a reverse split magnitude >= 50 (1-for-50 or worse)."""
    mag = _reverse_split_magnitude(split_factor)
    return (mag >= 50.0).fillna(False).astype(float)


def rss_ext_022_rs_severe_count_252d(split_factor: pd.Series) -> pd.Series:
    """Count of RS events with magnitude >= 5 in trailing 252 days."""
    mag = _reverse_split_magnitude(split_factor)
    severe = (mag >= 5.0).fillna(False).astype(float)
    return _rolling_sum(severe, _TD_YEAR)


def rss_ext_023_rs_extreme_count_756d(split_factor: pd.Series) -> pd.Series:
    """Count of RS events with magnitude >= 20 in trailing 756 days."""
    mag = _reverse_split_magnitude(split_factor)
    extreme = (mag >= 20.0).fillna(False).astype(float)
    return _rolling_sum(extreme, _TD_3Y)


def rss_ext_024_rs_magnitude_log_last(split_factor: pd.Series) -> pd.Series:
    """Log magnitude of the most recent reverse split, carried forward (0 before any)."""
    mag = _reverse_split_magnitude(split_factor)
    return np.log(mag.replace(0, np.nan)).ffill().fillna(0.0)


# --- Group C (025-036): Cumulative split-factor drawdowns and trends ---

def rss_ext_025_cumulative_rs_factor_126d(split_factor: pd.Series) -> pd.Series:
    """Cumulative product of split_factor over trailing 126 days."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return np.exp(_rolling_sum(log_sf, _TD_2Q))


def rss_ext_026_cumulative_rs_factor_1260d(split_factor: pd.Series) -> pd.Series:
    """Cumulative product of split_factor over trailing 1260 days (5 years)."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return np.exp(_rolling_sum(log_sf, _TD_5Y))


def rss_ext_027_cumulative_log_sf_252d(split_factor: pd.Series) -> pd.Series:
    """Sum of log split_factor over trailing 252 days (negative = net reverse splits)."""
    return _rolling_sum(np.log(split_factor.clip(lower=_EPS)), _TD_YEAR)


def rss_ext_028_cumulative_log_sf_expanding(split_factor: pd.Series) -> pd.Series:
    """Expanding sum of log split_factor (cumulative net split adjustment, all history)."""
    return np.log(split_factor.clip(lower=_EPS)).expanding(min_periods=1).sum()


def rss_ext_029_cumulative_rs_factor_drawdown_756d(split_factor: pd.Series) -> pd.Series:
    """Expanding cumulative split-factor product minus its trailing 756-day peak."""
    cum = np.exp(np.log(split_factor.clip(lower=_EPS)).expanding(min_periods=1).sum())
    return cum - _rolling_max(cum, _TD_3Y)


def rss_ext_030_net_split_direction_252d(split_factor: pd.Series) -> pd.Series:
    """Sign of net split adjustment over 252 days (-1 net reverse, +1 net forward)."""
    return np.sign(_rolling_sum(np.log(split_factor.clip(lower=_EPS)), _TD_YEAR))


def rss_ext_031_rs_count_minus_fs_count_756d(split_factor: pd.Series) -> pd.Series:
    """Reverse-split count minus forward-split count over trailing 756 days."""
    rs = _rolling_sum(_is_reverse_split(split_factor), _TD_3Y)
    fs = _rolling_sum(_is_forward_split(split_factor), _TD_3Y)
    return rs - fs


def rss_ext_032_rs_density_756d(split_factor: pd.Series) -> pd.Series:
    """Fraction of trailing 756 days that were reverse-split effective dates."""
    return _rolling_mean(_is_reverse_split(split_factor), _TD_3Y)


def rss_ext_033_rs_density_ratio_126d_vs_756d(split_factor: pd.Series) -> pd.Series:
    """Ratio of RS density in 126d vs 756d window — recent RS clustering."""
    d126 = _rolling_mean(_is_reverse_split(split_factor), _TD_2Q)
    d756 = _rolling_mean(_is_reverse_split(split_factor), _TD_3Y)
    return _safe_div(d126, d756 + _EPS)


def rss_ext_034_rs_count_acceleration_252d(split_factor: pd.Series) -> pd.Series:
    """Change in trailing-252d RS count vs one year earlier (RS-frequency acceleration)."""
    cnt = _rolling_sum(_is_reverse_split(split_factor), _TD_YEAR)
    return cnt - cnt.shift(_TD_YEAR)


def rss_ext_035_expanding_rs_count_per_year(split_factor: pd.Series) -> pd.Series:
    """Cumulative RS count divided by years of history (annualized RS rate)."""
    cum = _is_reverse_split(split_factor).expanding(min_periods=1).sum()
    age = pd.Series(np.arange(1, len(split_factor) + 1), index=split_factor.index, dtype=float)
    years = age / float(_TD_YEAR)
    return _safe_div(cum, years)


def rss_ext_036_rs_repeat_offender_3plus_756d_flag(split_factor: pd.Series) -> pd.Series:
    """1 if 3 or more reverse splits occurred in trailing 756 days (serial offender)."""
    return (_rolling_sum(_is_reverse_split(split_factor), _TD_3Y) >= 3).astype(float)


# --- Group D (037-052): Nominal-price sub-threshold relapse and depth ---

def rss_ext_037_closeunadj_below_0_5_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $0.50 (deep sub-penny distress)."""
    return (closeunadj < 0.5).astype(float)


def rss_ext_038_closeunadj_below_3_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $3.00."""
    return (closeunadj < 3.0).astype(float)


def rss_ext_039_closeunadj_below_0_5_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days unadjusted close has been below $0.50."""
    return _consec_streak(closeunadj < 0.5)


def rss_ext_040_closeunadj_below_2_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days unadjusted close has been below $2.00."""
    return _consec_streak(closeunadj < 2.0)


def rss_ext_041_closeunadj_below_10_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days unadjusted close has been below $10.00."""
    return _consec_streak(closeunadj < 10.0)


def rss_ext_042_days_since_closeunadj_above_5(closeunadj: pd.Series) -> pd.Series:
    """Trading days since unadjusted close was last at or above $5.00."""
    above = (closeunadj >= 5.0).astype(int)
    days = np.zeros(len(above), dtype=float)
    arr = above.values
    counter = 0.0
    for i in range(len(arr)):
        counter = 0.0 if arr[i] > 0 else counter + 1.0
        days[i] = counter
    return pd.Series(days, index=closeunadj.index)


def rss_ext_043_closeunadj_log_distance_to_1(closeunadj: pd.Series) -> pd.Series:
    """Log of unadjusted close relative to $1 (negative = sub-$1 listing-risk zone)."""
    return np.log(closeunadj.clip(lower=_EPS))


def rss_ext_044_closeunadj_days_below_1_count_63d(closeunadj: pd.Series) -> pd.Series:
    """Count of days below $1 in the trailing 63 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_QTR)


def rss_ext_045_closeunadj_fraction_below_1_756d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of trailing 756 days the unadjusted close was below $1."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_3Y)


def rss_ext_046_closeunadj_fraction_below_5_756d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of trailing 756 days the unadjusted close was below $5."""
    return _rolling_mean((closeunadj < 5.0).astype(float), _TD_3Y)


def rss_ext_047_post_rs_relapse_below_1_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 when a reverse split occurred in the last 252 days AND close is back below $1."""
    rs_recent = (_rolling_sum(_is_reverse_split(split_factor), _TD_YEAR) > 0).astype(float)
    return rs_recent * (closeunadj < 1.0).astype(float)


def rss_ext_048_post_rs_relapse_below_3_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 when a reverse split occurred in the last 504 days AND close is back below $3."""
    rs_recent = (_rolling_sum(_is_reverse_split(split_factor), _TD_2Y) > 0).astype(float)
    return rs_recent * (closeunadj < 3.0).astype(float)


def rss_ext_049_closeunadj_pct_rank_756d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of unadjusted close within trailing 756 trading days."""
    return _rolling_rank_pct(closeunadj, _TD_3Y)


def rss_ext_050_closeunadj_zscore_756d(closeunadj: pd.Series) -> pd.Series:
    """Z-score of unadjusted close within trailing 756 trading days."""
    return _zscore_rolling(closeunadj, _TD_3Y)


def rss_ext_051_closeunadj_drawdown_from_504d_peak(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close minus its 504-day rolling maximum (nominal drawdown)."""
    return closeunadj - _rolling_max(closeunadj, _TD_2Y)


def rss_ext_052_closeunadj_pct_drawdown_756d(closeunadj: pd.Series) -> pd.Series:
    """Percent drawdown of unadjusted close from its 756-day rolling peak."""
    peak = _rolling_max(closeunadj, _TD_3Y)
    return _safe_div_abs(closeunadj - peak, peak)


# --- Group E (053-064): Adjusted-close interaction with split events ---

def rss_ext_053_close_below_0_5_flag(close: pd.Series) -> pd.Series:
    """Binary: 1 if adjusted close < $0.50."""
    return (close < 0.5).astype(float)


def rss_ext_054_close_below_3_flag(close: pd.Series) -> pd.Series:
    """Binary: 1 if adjusted close < $3.00."""
    return (close < 3.0).astype(float)


def rss_ext_055_close_pct_rank_756d(close: pd.Series) -> pd.Series:
    """Percentile rank of adjusted close within trailing 756 trading days."""
    return _rolling_rank_pct(close, _TD_3Y)


def rss_ext_056_close_drawdown_from_756d_peak(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its 756-day rolling peak."""
    return close - _rolling_max(close, _TD_3Y)


def rss_ext_057_close_pct_drawdown_756d(close: pd.Series) -> pd.Series:
    """Percent drawdown of adjusted close from its 756-day rolling peak."""
    peak = _rolling_max(close, _TD_3Y)
    return _safe_div_abs(close - peak, peak)


def rss_ext_058_rs_within_504d_and_drawdown_lt_neg70_flag(split_factor: pd.Series, close: pd.Series) -> pd.Series:
    """1 when an RS occurred in the last 504 days AND adjusted close is >70% below its 504d peak."""
    rs_recent = (_rolling_sum(_is_reverse_split(split_factor), _TD_2Y) > 0).astype(float)
    peak = _rolling_max(close, _TD_2Y)
    dd = _safe_div_abs(close - peak, peak)
    return rs_recent * (dd < -0.7).astype(float)


def rss_ext_059_rs_magnitude_x_close_drawdown_252d(split_factor: pd.Series, close: pd.Series) -> pd.Series:
    """Carried RS magnitude multiplied by adjusted-close drawdown from 252d peak."""
    mag = _reverse_split_magnitude(split_factor).ffill().fillna(0.0)
    peak = _rolling_max(close, _TD_YEAR)
    dd = _safe_div_abs(close - peak, peak)
    return mag * dd


def rss_ext_060_rs_count_756d_x_close_below2_flag(split_factor: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing-756d RS count multiplied by sub-$2 adjusted-close flag (joint distress)."""
    cnt = _rolling_sum(_is_reverse_split(split_factor), _TD_3Y)
    return cnt * (close < 2.0).astype(float)


def rss_ext_061_close_adj_vs_unadj_ratio_zscore_252d(close: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Z-score of the adjusted/unadjusted close ratio within trailing 252 days."""
    ratio = _safe_div(close, closeunadj)
    return _zscore_rolling(ratio, _TD_YEAR)


def rss_ext_062_close_adj_unadj_ratio_change_252d(close: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """YoY change in the adjusted/unadjusted close ratio (cumulative split-adjustment drift)."""
    ratio = _safe_div(close, closeunadj)
    return ratio - ratio.shift(_TD_YEAR)


def rss_ext_063_rs_recent_and_close_at_3y_low_flag(split_factor: pd.Series, close: pd.Series) -> pd.Series:
    """1 when an RS occurred in the last 252 days AND adjusted close equals its 756d minimum."""
    rs_recent = (_rolling_sum(_is_reverse_split(split_factor), _TD_YEAR) > 0).astype(float)
    at_low = (close <= _rolling_min(close, _TD_3Y) + _EPS).astype(float)
    return rs_recent * at_low


def rss_ext_064_rs_recent_x_closeunadj_pct_drawdown(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Recent-RS flag (252d) multiplied by unadjusted-close percent drawdown from 252d peak."""
    rs_recent = (_rolling_sum(_is_reverse_split(split_factor), _TD_YEAR) > 0).astype(float)
    peak = _rolling_max(closeunadj, _TD_YEAR)
    dd = _safe_div_abs(closeunadj - peak, peak)
    return rs_recent * dd


# --- Group F (065-075): Nominal-price momentum, dispersion and composites ---

def rss_ext_065_closeunadj_return_126d(closeunadj: pd.Series) -> pd.Series:
    """126-day log return of unadjusted close."""
    cur = np.log(closeunadj.clip(lower=_EPS))
    return cur - np.log(closeunadj.shift(_TD_2Q).clip(lower=_EPS))


def rss_ext_066_closeunadj_return_504d(closeunadj: pd.Series) -> pd.Series:
    """504-day log return of unadjusted close."""
    cur = np.log(closeunadj.clip(lower=_EPS))
    return cur - np.log(closeunadj.shift(_TD_2Y).clip(lower=_EPS))


def rss_ext_067_closeunadj_volatility_126d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 126-day std of daily log returns of unadjusted close."""
    lr = np.log(closeunadj.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_2Q)


def rss_ext_068_closeunadj_downside_vol_63d(closeunadj: pd.Series) -> pd.Series:
    """Root-mean-square of negative daily log returns of unadjusted close over 63 days."""
    lr = np.log(closeunadj.clip(lower=_EPS)).diff(1)
    neg = lr.clip(upper=0.0)
    return _rolling_mean(neg ** 2, _TD_QTR) ** 0.5


def rss_ext_069_closeunadj_normalized_position_756d(closeunadj: pd.Series) -> pd.Series:
    """Position of unadjusted close within its 756-day min-max range (0=low, 1=high)."""
    mn = _rolling_min(closeunadj, _TD_3Y)
    mx = _rolling_max(closeunadj, _TD_3Y)
    return _safe_div(closeunadj - mn, mx - mn)


def rss_ext_070_closeunadj_cv_252d(closeunadj: pd.Series) -> pd.Series:
    """Coefficient of variation of unadjusted close over trailing 252 days (std / |mean|)."""
    m  = _rolling_mean(closeunadj, _TD_YEAR)
    sd = _rolling_std(closeunadj, _TD_YEAR)
    return _safe_div_abs(sd, m)


def rss_ext_071_closeunadj_pct_above_756d_min(closeunadj: pd.Series) -> pd.Series:
    """Percent of unadjusted close above its trailing 756-day minimum."""
    mn = _rolling_min(closeunadj, _TD_3Y)
    return _safe_div_abs(closeunadj - mn, mn)


def rss_ext_072_closeunadj_below_756d_min_flag(closeunadj: pd.Series) -> pd.Series:
    """1 when unadjusted close sets a new trailing 756-day low."""
    return (closeunadj <= _rolling_min(closeunadj, _TD_3Y) + _EPS).astype(float)


def rss_ext_073_closeunadj_consecutive_decline_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days the unadjusted close fell vs the prior day."""
    return _consec_streak(closeunadj < closeunadj.shift(1))


def rss_ext_074_rs_distress_intensity_756d(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """RS density (756d) times fraction of days below $1 (756d): chronic RS-distress intensity."""
    rs_density = _rolling_mean(_is_reverse_split(split_factor), _TD_3Y)
    below1 = _rolling_mean((closeunadj < 1.0).astype(float), _TD_3Y)
    return rs_density * below1


def rss_ext_075_reverse_split_distress_composite(split_factor: pd.Series, closeunadj: pd.Series, close: pd.Series) -> pd.Series:
    """Composite distress score: recent-RS recency + sub-$1 nominal flag + adjusted-close
    percent drawdown from 756-day peak (higher = deeper late-stage distress)."""
    rs_recency = 1.0 / (1.0 + _days_since_event(_is_reverse_split(split_factor)))
    below1 = (closeunadj < 1.0).astype(float)
    peak = _rolling_max(close, _TD_3Y)
    dd = _safe_div_abs(peak - close, peak).clip(lower=0.0)
    return rs_recency.fillna(0.0) + below1 + dd


# ── Registry ──────────────────────────────────────────────────────────────────

REVERSE_SPLIT_SIGNAL_EXTENDED_REGISTRY_001_075 = {
    "rss_ext_001_days_since_any_split":          {"inputs": ["split_factor"],                          "func": rss_ext_001_days_since_any_split},
    "rss_ext_002_rs_within_31d_flag":            {"inputs": ["split_factor"],                          "func": rss_ext_002_rs_within_31d_flag},
    "rss_ext_003_rs_within_756d_flag":           {"inputs": ["split_factor"],                          "func": rss_ext_003_rs_within_756d_flag},
    "rss_ext_004_rs_within_1260d_flag":          {"inputs": ["split_factor"],                          "func": rss_ext_004_rs_within_1260d_flag},
    "rss_ext_005_days_since_rs_capped_252":      {"inputs": ["split_factor"],                          "func": rss_ext_005_days_since_rs_capped_252},
    "rss_ext_006_rs_recency_inverse":            {"inputs": ["split_factor"],                          "func": rss_ext_006_rs_recency_inverse},
    "rss_ext_007_rs_inter_arrival_gap":          {"inputs": ["split_factor"],                          "func": rss_ext_007_rs_inter_arrival_gap},
    "rss_ext_008_days_since_rs_log1p_capped":    {"inputs": ["split_factor"],                          "func": rss_ext_008_days_since_rs_log1p_capped},
    "rss_ext_009_rs_recency_decay_fast":         {"inputs": ["split_factor"],                          "func": rss_ext_009_rs_recency_decay_fast},
    "rss_ext_010_rs_recency_decay_medium":       {"inputs": ["split_factor"],                          "func": rss_ext_010_rs_recency_decay_medium},
    "rss_ext_011_any_split_within_63d_flag":     {"inputs": ["split_factor"],                          "func": rss_ext_011_any_split_within_63d_flag},
    "rss_ext_012_days_since_rs_over_63d_flag":   {"inputs": ["split_factor"],                          "func": rss_ext_012_days_since_rs_over_63d_flag},
    "rss_ext_013_rs_magnitude_filled":           {"inputs": ["split_factor"],                          "func": rss_ext_013_rs_magnitude_filled},
    "rss_ext_014_rs_magnitude_last":             {"inputs": ["split_factor"],                          "func": rss_ext_014_rs_magnitude_last},
    "rss_ext_015_rs_magnitude_mean_252d":        {"inputs": ["split_factor"],                          "func": rss_ext_015_rs_magnitude_mean_252d},
    "rss_ext_016_rs_magnitude_sum_504d":         {"inputs": ["split_factor"],                          "func": rss_ext_016_rs_magnitude_sum_504d},
    "rss_ext_017_rs_log_magnitude_sum_756d":     {"inputs": ["split_factor"],                          "func": rss_ext_017_rs_log_magnitude_sum_756d},
    "rss_ext_018_rs_magnitude_pct_rank_756d":    {"inputs": ["split_factor"],                          "func": rss_ext_018_rs_magnitude_pct_rank_756d},
    "rss_ext_019_rs_magnitude_max_756d":         {"inputs": ["split_factor"],                          "func": rss_ext_019_rs_magnitude_max_756d},
    "rss_ext_020_rs_magnitude_max_1260d":        {"inputs": ["split_factor"],                          "func": rss_ext_020_rs_magnitude_max_1260d},
    "rss_ext_021_rs_severity_gte50_flag":        {"inputs": ["split_factor"],                          "func": rss_ext_021_rs_severity_gte50_flag},
    "rss_ext_022_rs_severe_count_252d":          {"inputs": ["split_factor"],                          "func": rss_ext_022_rs_severe_count_252d},
    "rss_ext_023_rs_extreme_count_756d":         {"inputs": ["split_factor"],                          "func": rss_ext_023_rs_extreme_count_756d},
    "rss_ext_024_rs_magnitude_log_last":         {"inputs": ["split_factor"],                          "func": rss_ext_024_rs_magnitude_log_last},
    "rss_ext_025_cumulative_rs_factor_126d":     {"inputs": ["split_factor"],                          "func": rss_ext_025_cumulative_rs_factor_126d},
    "rss_ext_026_cumulative_rs_factor_1260d":    {"inputs": ["split_factor"],                          "func": rss_ext_026_cumulative_rs_factor_1260d},
    "rss_ext_027_cumulative_log_sf_252d":        {"inputs": ["split_factor"],                          "func": rss_ext_027_cumulative_log_sf_252d},
    "rss_ext_028_cumulative_log_sf_expanding":   {"inputs": ["split_factor"],                          "func": rss_ext_028_cumulative_log_sf_expanding},
    "rss_ext_029_cumulative_rs_factor_drawdown_756d":{"inputs": ["split_factor"],                      "func": rss_ext_029_cumulative_rs_factor_drawdown_756d},
    "rss_ext_030_net_split_direction_252d":      {"inputs": ["split_factor"],                          "func": rss_ext_030_net_split_direction_252d},
    "rss_ext_031_rs_count_minus_fs_count_756d":  {"inputs": ["split_factor"],                          "func": rss_ext_031_rs_count_minus_fs_count_756d},
    "rss_ext_032_rs_density_756d":               {"inputs": ["split_factor"],                          "func": rss_ext_032_rs_density_756d},
    "rss_ext_033_rs_density_ratio_126d_vs_756d": {"inputs": ["split_factor"],                          "func": rss_ext_033_rs_density_ratio_126d_vs_756d},
    "rss_ext_034_rs_count_acceleration_252d":    {"inputs": ["split_factor"],                          "func": rss_ext_034_rs_count_acceleration_252d},
    "rss_ext_035_expanding_rs_count_per_year":   {"inputs": ["split_factor"],                          "func": rss_ext_035_expanding_rs_count_per_year},
    "rss_ext_036_rs_repeat_offender_3plus_756d_flag":{"inputs": ["split_factor"],                      "func": rss_ext_036_rs_repeat_offender_3plus_756d_flag},
    "rss_ext_037_closeunadj_below_0_5_flag":     {"inputs": ["closeunadj"],                            "func": rss_ext_037_closeunadj_below_0_5_flag},
    "rss_ext_038_closeunadj_below_3_flag":       {"inputs": ["closeunadj"],                            "func": rss_ext_038_closeunadj_below_3_flag},
    "rss_ext_039_closeunadj_below_0_5_streak":   {"inputs": ["closeunadj"],                            "func": rss_ext_039_closeunadj_below_0_5_streak},
    "rss_ext_040_closeunadj_below_2_streak":     {"inputs": ["closeunadj"],                            "func": rss_ext_040_closeunadj_below_2_streak},
    "rss_ext_041_closeunadj_below_10_streak":    {"inputs": ["closeunadj"],                            "func": rss_ext_041_closeunadj_below_10_streak},
    "rss_ext_042_days_since_closeunadj_above_5": {"inputs": ["closeunadj"],                            "func": rss_ext_042_days_since_closeunadj_above_5},
    "rss_ext_043_closeunadj_log_distance_to_1":  {"inputs": ["closeunadj"],                            "func": rss_ext_043_closeunadj_log_distance_to_1},
    "rss_ext_044_closeunadj_days_below_1_count_63d":{"inputs": ["closeunadj"],                         "func": rss_ext_044_closeunadj_days_below_1_count_63d},
    "rss_ext_045_closeunadj_fraction_below_1_756d":{"inputs": ["closeunadj"],                          "func": rss_ext_045_closeunadj_fraction_below_1_756d},
    "rss_ext_046_closeunadj_fraction_below_5_756d":{"inputs": ["closeunadj"],                          "func": rss_ext_046_closeunadj_fraction_below_5_756d},
    "rss_ext_047_post_rs_relapse_below_1_flag":  {"inputs": ["split_factor", "closeunadj"],            "func": rss_ext_047_post_rs_relapse_below_1_flag},
    "rss_ext_048_post_rs_relapse_below_3_flag":  {"inputs": ["split_factor", "closeunadj"],            "func": rss_ext_048_post_rs_relapse_below_3_flag},
    "rss_ext_049_closeunadj_pct_rank_756d":      {"inputs": ["closeunadj"],                            "func": rss_ext_049_closeunadj_pct_rank_756d},
    "rss_ext_050_closeunadj_zscore_756d":        {"inputs": ["closeunadj"],                            "func": rss_ext_050_closeunadj_zscore_756d},
    "rss_ext_051_closeunadj_drawdown_from_504d_peak":{"inputs": ["closeunadj"],                        "func": rss_ext_051_closeunadj_drawdown_from_504d_peak},
    "rss_ext_052_closeunadj_pct_drawdown_756d":  {"inputs": ["closeunadj"],                            "func": rss_ext_052_closeunadj_pct_drawdown_756d},
    "rss_ext_053_close_below_0_5_flag":          {"inputs": ["close"],                                 "func": rss_ext_053_close_below_0_5_flag},
    "rss_ext_054_close_below_3_flag":            {"inputs": ["close"],                                 "func": rss_ext_054_close_below_3_flag},
    "rss_ext_055_close_pct_rank_756d":           {"inputs": ["close"],                                 "func": rss_ext_055_close_pct_rank_756d},
    "rss_ext_056_close_drawdown_from_756d_peak": {"inputs": ["close"],                                 "func": rss_ext_056_close_drawdown_from_756d_peak},
    "rss_ext_057_close_pct_drawdown_756d":       {"inputs": ["close"],                                 "func": rss_ext_057_close_pct_drawdown_756d},
    "rss_ext_058_rs_within_504d_and_drawdown_lt_neg70_flag":{"inputs": ["split_factor", "close"],      "func": rss_ext_058_rs_within_504d_and_drawdown_lt_neg70_flag},
    "rss_ext_059_rs_magnitude_x_close_drawdown_252d":{"inputs": ["split_factor", "close"],             "func": rss_ext_059_rs_magnitude_x_close_drawdown_252d},
    "rss_ext_060_rs_count_756d_x_close_below2_flag":{"inputs": ["split_factor", "close"],              "func": rss_ext_060_rs_count_756d_x_close_below2_flag},
    "rss_ext_061_close_adj_vs_unadj_ratio_zscore_252d":{"inputs": ["close", "closeunadj"],             "func": rss_ext_061_close_adj_vs_unadj_ratio_zscore_252d},
    "rss_ext_062_close_adj_unadj_ratio_change_252d":{"inputs": ["close", "closeunadj"],                "func": rss_ext_062_close_adj_unadj_ratio_change_252d},
    "rss_ext_063_rs_recent_and_close_at_3y_low_flag":{"inputs": ["split_factor", "close"],             "func": rss_ext_063_rs_recent_and_close_at_3y_low_flag},
    "rss_ext_064_rs_recent_x_closeunadj_pct_drawdown":{"inputs": ["split_factor", "closeunadj"],       "func": rss_ext_064_rs_recent_x_closeunadj_pct_drawdown},
    "rss_ext_065_closeunadj_return_126d":        {"inputs": ["closeunadj"],                            "func": rss_ext_065_closeunadj_return_126d},
    "rss_ext_066_closeunadj_return_504d":        {"inputs": ["closeunadj"],                            "func": rss_ext_066_closeunadj_return_504d},
    "rss_ext_067_closeunadj_volatility_126d":    {"inputs": ["closeunadj"],                            "func": rss_ext_067_closeunadj_volatility_126d},
    "rss_ext_068_closeunadj_downside_vol_63d":   {"inputs": ["closeunadj"],                            "func": rss_ext_068_closeunadj_downside_vol_63d},
    "rss_ext_069_closeunadj_normalized_position_756d":{"inputs": ["closeunadj"],                       "func": rss_ext_069_closeunadj_normalized_position_756d},
    "rss_ext_070_closeunadj_cv_252d":            {"inputs": ["closeunadj"],                            "func": rss_ext_070_closeunadj_cv_252d},
    "rss_ext_071_closeunadj_pct_above_756d_min": {"inputs": ["closeunadj"],                            "func": rss_ext_071_closeunadj_pct_above_756d_min},
    "rss_ext_072_closeunadj_below_756d_min_flag":{"inputs": ["closeunadj"],                            "func": rss_ext_072_closeunadj_below_756d_min_flag},
    "rss_ext_073_closeunadj_consecutive_decline_streak":{"inputs": ["closeunadj"],                     "func": rss_ext_073_closeunadj_consecutive_decline_streak},
    "rss_ext_074_rs_distress_intensity_756d":    {"inputs": ["split_factor", "closeunadj"],            "func": rss_ext_074_rs_distress_intensity_756d},
    "rss_ext_075_reverse_split_distress_composite":{"inputs": ["split_factor", "closeunadj", "close"], "func": rss_ext_075_reverse_split_distress_composite},
}
