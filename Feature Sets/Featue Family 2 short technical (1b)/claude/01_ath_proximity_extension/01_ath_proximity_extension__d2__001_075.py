"""ath_proximity_extension d2 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the ATH-proximity/extension theme:
distance / time / range-position / statistical / Fibonacci / prior-cycle.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _expanding_max_grouped(s: pd.Series, group: pd.Series) -> pd.Series:
    """Within-group expanding max — vectorized via groupby+cummax."""
    return s.groupby(group).cummax()


def _prior_period_max(s: pd.Series, period_id: pd.Series) -> pd.Series:
    """For each bar, the max of s over the prior (closed) calendar period.
    Implementation: compute completed-period max, then shift onto current period bars."""
    # Per-period closed max (only known when the period ends). We approximate
    # by taking the running within-period max at the *last* bar of the prior period.
    period_complete_max = s.groupby(period_id).transform("max")
    # When the period flips, we want to read the previous period's complete max.
    # Build a lookup: for each unique period, the max value of s in that period.
    period_max_map = s.groupby(period_id).max()
    # Determine prior period id at each bar
    unique_periods = period_id.drop_duplicates().tolist()
    prior_map = {p: (unique_periods[i - 1] if i > 0 else np.nan) for i, p in enumerate(unique_periods)}
    prior_period_at_bar = period_id.map(prior_map)
    return prior_period_at_bar.map(period_max_map)


def f01_athx_001_log_dist_above_21d_high_d2(high: pd.Series) -> pd.Series:
    """Log distance of close-high above 21d rolling max — monthly extension."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff()


def f01_athx_002_log_dist_above_126d_high_d2(high: pd.Series) -> pd.Series:
    """Log distance above 126d rolling max — half-year extension (gap horizon)."""
    rmax = high.rolling(126, min_periods=QDAYS).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff()


def f01_athx_003_log_dist_above_504d_high_d2(high: pd.Series) -> pd.Series:
    """Log distance above 504d (2y) rolling max — biennial extension."""
    rmax = high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff()


def f01_athx_004_log_dist_above_756d_high_d2(high: pd.Series) -> pd.Series:
    """Log distance above 756d (3y) rolling max — triennial extension."""
    rmax = high.rolling(DDAYS_3Y, min_periods=YDAYS).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff()


def f01_athx_005_atr_dist_above_21d_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above 21d rolling max."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - rmax, atr)).diff().diff()


def f01_athx_006_atr_dist_above_63d_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above 63d rolling max."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - rmax, atr)).diff().diff()


def f01_athx_007_atr_dist_above_252d_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above 252d rolling max — annual stretch in vol units."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - rmax, atr)).diff().diff()


def f01_athx_008_atr_dist_above_504d_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above 504d rolling max."""
    rmax = high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - rmax, atr)).diff().diff()


def f01_athx_009_sigma_dist_above_252d_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Realized-sigma normalized distance of close above 252d max (annualized 63d sigma)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ret = _safe_log(close).diff()
    sigma = ret.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(_safe_log(close) - _safe_log(rmax), sigma)).diff().diff()


def f01_athx_010_pct_dist_above_252d_high_d2(high: pd.Series) -> pd.Series:
    """Raw percentage distance above 252d high (not log)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(high - rmax, rmax)).diff().diff()


def f01_athx_011_dollar_dist_above_252d_high_norm_close_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Dollar distance above 252d max, normalized by close — scale-free magnitude."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(close - rmax, close)).diff().diff()


def f01_athx_012_atr_dist_above_126d_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above 126d (half-year) rolling max."""
    rmax = high.rolling(126, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - rmax, atr)).diff().diff()


def f01_athx_013_log_dist_above_expanding_alltime_high_d2(high: pd.Series) -> pd.Series:
    """Log distance above expanding-window all-time high (full history to date)."""
    rmax = high.expanding(min_periods=QDAYS).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff()


def f01_athx_014_atr_dist_above_alltime_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance above expanding all-time high."""
    rmax = high.expanding(min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - rmax, atr)).diff().diff()


def f01_athx_015_days_since_alltime_high_d2(high: pd.Series) -> pd.Series:
    """Bars since expanding all-time high was set — staleness of lifetime peak."""
    arr = high.to_numpy(copy=True)
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_max_idx = -1
    for i in range(n):
        v = arr[i]
        if not np.isnan(v):
            if v >= cur_max:
                cur_max = v
                cur_max_idx = i
            if cur_max_idx >= 0:
                out[i] = float(i - cur_max_idx)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_016_fraction_expanding_within_5pct_of_alltime_d2(high: pd.Series) -> pd.Series:
    """Fraction of full expanding history within 5% of running all-time high."""
    rmax = high.expanding(min_periods=QDAYS).max()
    within = (high >= 0.95 * rmax).astype(float)
    # expanding mean of "within" — fraction of all bars so far at/near ATH
    return (within.expanding(min_periods=QDAYS).mean()).diff().diff()


def f01_athx_017_bars_between_distinct_alltime_high_resets_d2(high: pd.Series) -> pd.Series:
    """Bars since the previous distinct all-time-high level was last broken
    (so the current bar's 'time-since-last-reset')."""
    arr = high.to_numpy(copy=True)
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    prev_reset_idx = -1
    cur_max = -np.inf
    for i in range(n):
        v = arr[i]
        if not np.isnan(v):
            if v > cur_max and cur_max > -np.inf:
                # a strict reset just happened
                if prev_reset_idx >= 0:
                    out[i] = float(i - prev_reset_idx)
                prev_reset_idx = i
                cur_max = v
            elif v > cur_max:
                cur_max = v
                prev_reset_idx = i
        # carry-forward last gap
        if np.isnan(out[i]) and prev_reset_idx >= 0 and i > 0 and not np.isnan(out[i - 1]):
            out[i] = out[i - 1]
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_018_alltime_high_recency_years_d2(high: pd.Series) -> pd.Series:
    """Recency of lifetime high expressed in years (252-bar units)."""
    arr = high.to_numpy(copy=True)
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_max_idx = -1
    for i in range(n):
        v = arr[i]
        if not np.isnan(v):
            if v >= cur_max:
                cur_max = v
                cur_max_idx = i
            if cur_max_idx >= 0:
                out[i] = (i - cur_max_idx) / float(YDAYS)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_019_alltime_high_recency_zscore_d2(high: pd.Series) -> pd.Series:
    """Z-score (over 504d) of 'days since alltime high' — anomalously young/old peak."""
    arr = high.to_numpy(copy=True)
    n = len(arr)
    rec = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_max_idx = -1
    for i in range(n):
        v = arr[i]
        if not np.isnan(v):
            if v >= cur_max:
                cur_max = v
                cur_max_idx = i
            if cur_max_idx >= 0:
                rec[i] = float(i - cur_max_idx)
    rec_s = pd.Series(rec, index=high.index)
    return (_rolling_zscore(rec_s, DDAYS_2Y, min_periods=YDAYS)).diff().diff()


def f01_athx_020_lifetime_high_persistence_ratio_d2(high: pd.Series) -> pd.Series:
    """Persistence: cumulative bars-at-alltime-high / total bars-so-far.
    Higher = more of history spent at lifetime peaks."""
    rmax = high.expanding(min_periods=QDAYS).max()
    at_ath = (high >= 0.999 * rmax).astype(float)
    cum_at_ath = at_ath.expanding(min_periods=QDAYS).sum()
    bars_so_far = pd.Series(np.arange(1, len(high) + 1, dtype=float), index=high.index)
    return (_safe_div(cum_at_ath, bars_so_far)).diff().diff()


def f01_athx_021_log_dist_above_prior_calendar_year_high_d2(high: pd.Series) -> pd.Series:
    """Log distance of high above the prior calendar year's high."""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    year_id = pd.Series(high.index.year, index=high.index)
    prior_yr_max = _prior_period_max(high, year_id)
    return (_safe_log(high) - _safe_log(prior_yr_max)).diff().diff()


def f01_athx_022_log_dist_above_prior_calendar_quarter_high_d2(high: pd.Series) -> pd.Series:
    """Log distance above prior calendar quarter's high."""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    q_id = pd.Series(high.index.to_period("Q").astype(str), index=high.index)
    prior_q_max = _prior_period_max(high, q_id)
    return (_safe_log(high) - _safe_log(prior_q_max)).diff().diff()


def f01_athx_023_log_dist_above_prior_calendar_month_high_d2(high: pd.Series) -> pd.Series:
    """Log distance above prior calendar month's high."""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    m_id = pd.Series(high.index.to_period("M").astype(str), index=high.index)
    prior_m_max = _prior_period_max(high, m_id)
    return (_safe_log(high) - _safe_log(prior_m_max)).diff().diff()


def f01_athx_024_log_dist_above_ytd_high_d2(high: pd.Series) -> pd.Series:
    """Log distance above the current year's YTD high (within-year expanding max)."""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    year_id = pd.Series(high.index.year, index=high.index)
    ytd_max = _expanding_max_grouped(high, year_id)
    return (_safe_log(high) - _safe_log(ytd_max)).diff().diff()


def f01_athx_025_log_dist_above_qtd_high_d2(high: pd.Series) -> pd.Series:
    """Log distance above the current quarter's QTD high."""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    q_id = pd.Series(high.index.to_period("Q").astype(str), index=high.index)
    qtd_max = _expanding_max_grouped(high, q_id)
    return (_safe_log(high) - _safe_log(qtd_max)).diff().diff()


def f01_athx_026_days_since_ytd_high_d2(high: pd.Series) -> pd.Series:
    """Bars since the YTD high was set — staleness of within-year peak."""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    year_id = pd.Series(high.index.year, index=high.index)
    arr = high.to_numpy(copy=True)
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    last_year = None
    cur_max = -np.inf
    cur_max_idx = -1
    for i in range(n):
        y = year_id.iat[i]
        if y != last_year:
            cur_max = -np.inf
            cur_max_idx = -1
            last_year = y
        v = arr[i]
        if not np.isnan(v):
            if v >= cur_max:
                cur_max = v
                cur_max_idx = i
            if cur_max_idx >= 0:
                out[i] = float(i - cur_max_idx)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_027_days_since_prior_calendar_year_high_d2(high: pd.Series) -> pd.Series:
    """Bars since the prior calendar year's high — long-base anchor staleness."""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    year_id = pd.Series(high.index.year, index=high.index)
    prior_yr_max = _prior_period_max(high, year_id)
    arr = high.to_numpy(copy=True)
    pyr = prior_yr_max.to_numpy(copy=True)
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    # For each bar, find the most recent index where high == prior-year-max
    # we walk forward, tracking position of last bar with high>=prior_yr_max
    last_meet_idx = -1
    last_target = np.nan
    for i in range(n):
        tgt = pyr[i]
        v = arr[i]
        if not np.isnan(tgt):
            if tgt != last_target:
                # new anchor — reset search by scanning backwards for last bar with v>=tgt
                last_target = tgt
                last_meet_idx = -1
                for j in range(i, -1, -1):
                    if not np.isnan(arr[j]) and arr[j] >= tgt:
                        last_meet_idx = j
                        break
            else:
                if not np.isnan(v) and v >= tgt:
                    last_meet_idx = i
            if last_meet_idx >= 0:
                out[i] = float(i - last_meet_idx)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_028_ratio_ytd_high_to_prior_year_high_d2(high: pd.Series) -> pd.Series:
    """YTD high / prior-year high — how much new ground has this year covered."""
    if not isinstance(high.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=high.index)
    year_id = pd.Series(high.index.year, index=high.index)
    ytd_max = _expanding_max_grouped(high, year_id)
    prior_yr_max = _prior_period_max(high, year_id)
    return (_safe_div(ytd_max, prior_yr_max)).diff().diff()


def f01_athx_029_dwell_within_half_pct_of_252d_max_21d_d2(high: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d within 0.5% of the 252d rolling max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = (high >= 0.995 * rmax).astype(float)
    return (within.rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff()


def f01_athx_030_mean_time_between_21d_high_prints_252d_d2(high: pd.Series) -> pd.Series:
    """Average gap (in bars) between bars that print a new 21d-high, over trailing 252d."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_nh = (high >= rmax).astype(float)
    def _mean_gap(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return (is_nh.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True)).diff().diff()


def f01_athx_031_cum_time_in_top_decile_of_252d_range_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative bars in trailing 63d where close in top decile of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = (pos >= 0.9).astype(float)
    return (in_top.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()


def f01_athx_032_time_since_first_minus_last_252d_high_in_252d_d2(high: pd.Series) -> pd.Series:
    """(bars since FIRST 252d-high in window) minus (bars since LAST 252d-high in window).
    Spread between earliest and latest new-high events within the 1y window."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high >= rmax).astype(float).to_numpy(copy=True)
    n = len(is_nh)
    out = np.full(n, np.nan, dtype=float)
    win = YDAYS
    for i in range(n):
        lo = max(0, i - win + 1)
        w = is_nh[lo:i + 1]
        idx = np.where(w > 0)[0]
        if idx.size >= 2:
            first = idx[0]
            last = idx[-1]
            out[i] = float(last - first)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_033_median_bars_between_252d_high_prints_504d_d2(high: pd.Series) -> pd.Series:
    """Median gap (bars) between 252d new-high prints in trailing 504d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high >= rmax).astype(float)
    def _med_gap(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.median(np.diff(idx)))
    return (is_nh.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_med_gap, raw=True)).diff().diff()


def f01_athx_034_calendar_months_since_alltime_high_d2(high: pd.Series) -> pd.Series:
    """Days-since-alltime-high expressed in calendar months (21-bar units)."""
    arr = high.to_numpy(copy=True)
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    cur_max_idx = -1
    for i in range(n):
        v = arr[i]
        if not np.isnan(v):
            if v >= cur_max:
                cur_max = v
                cur_max_idx = i
            if cur_max_idx >= 0:
                out[i] = (i - cur_max_idx) / float(MDAYS)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_035_bars_since_most_recent_5y_high_d2(high: pd.Series) -> pd.Series:
    """Bars since 1260d (5y) rolling max was set."""
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return float((len(w) - 1) - int(np.nanargmax(w)))
    return (high.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_bsm, raw=True)).diff().diff()


def f01_athx_036_stale_high_indicator_no_new_252d_in_63d_d2(high: pd.Series) -> pd.Series:
    """1 if NO new 252d-high was printed in trailing 63d, else 0 — stale leadership."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high >= rmax).astype(float)
    cnt = is_nh.rolling(QDAYS, min_periods=MDAYS).sum()
    return ((cnt == 0).astype(float).where(cnt.notna(), np.nan)).diff().diff()


def f01_athx_037_half_life_dist_from_252d_high_decay_63d_d2(high: pd.Series) -> pd.Series:
    """Half-life (in bars) of |log distance from 252d high| decaying back toward 0
    over trailing 63d — estimated by linear regression of log|dist+eps| vs time."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dist = _safe_log(rmax) - _safe_log(high)   # >= 0
    y = np.log(dist.replace(0, np.nan) + 1e-6)
    sl = _rolling_slope(y, QDAYS)
    # half-life = ln(2) / |slope| when slope < 0
    out = -np.log(2.0) / sl
    return (out.where(sl < 0, np.nan)).diff().diff()


def f01_athx_038_persistence_within_1pct_of_252d_high_state_d2(high: pd.Series) -> pd.Series:
    """Current streak length: consecutive bars within 1% of 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_state = (high >= 0.99 * rmax).astype(float).to_numpy(copy=True)
    n = len(in_state)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(in_state[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if in_state[i] > 0 else 0
            out[i] = float(streak)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_039_count_new_5d_highs_in_63d_d2(high: pd.Series) -> pd.Series:
    """Count of new 5d-highs in trailing 63d window — short cadence."""
    rmax = high.rolling(WDAYS, min_periods=2).max()
    is_nh = (high >= rmax).astype(float)
    return (is_nh.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()


def f01_athx_040_count_new_21d_highs_in_126d_d2(high: pd.Series) -> pd.Series:
    """Count of new 21d-highs in trailing 126d window — medium cadence."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_nh = (high >= rmax).astype(float)
    return (is_nh.rolling(126, min_periods=QDAYS).sum()).diff().diff()


def f01_athx_041_count_new_63d_highs_in_252d_d2(high: pd.Series) -> pd.Series:
    """Count of new 63d-highs in trailing 252d window — quarterly cadence."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = (high >= rmax).astype(float)
    return (is_nh.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()


def f01_athx_042_count_new_126d_highs_in_504d_d2(high: pd.Series) -> pd.Series:
    """Count of new 126d-highs in trailing 504d window — semi-annual cadence."""
    rmax = high.rolling(126, min_periods=QDAYS).max()
    is_nh = (high >= rmax).astype(float)
    return (is_nh.rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff().diff()


def f01_athx_043_mean_gap_between_21d_high_events_252d_d2(high: pd.Series) -> pd.Series:
    """Mean gap (bars) between 21d-high events, over trailing 252d."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_nh = (high >= rmax).astype(float)
    def _mean_gap(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return (is_nh.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True)).diff().diff()


def f01_athx_044_std_gap_between_21d_high_events_252d_d2(high: pd.Series) -> pd.Series:
    """Std-dev of gaps between 21d-high events over trailing 252d — cadence irregularity."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_nh = (high >= rmax).astype(float)
    def _std_gap(w):
        idx = np.where(w > 0)[0]
        if idx.size < 3:
            return np.nan
        return float(np.std(np.diff(idx), ddof=1))
    return (is_nh.rolling(YDAYS, min_periods=QDAYS).apply(_std_gap, raw=True)).diff().diff()


def f01_athx_045_acceleration_of_new_21d_high_rate_d2(high: pd.Series) -> pd.Series:
    """Change in new-21d-high rate: (count in last 21d) - (count in 21d before that)."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_nh = (high >= rmax).astype(float)
    recent = is_nh.rolling(MDAYS, min_periods=WDAYS).sum()
    prior = is_nh.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).sum()
    return (recent - prior).diff().diff()


def f01_athx_046_consecutive_new_5d_highs_streak_d2(high: pd.Series) -> pd.Series:
    """Current consecutive new-5d-high streak length."""
    rmax = high.rolling(WDAYS, min_periods=2).max()
    is_nh = (high >= rmax).astype(float).to_numpy(copy=True)
    n = len(is_nh)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(is_nh[i]):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if is_nh[i] > 0 else 0
            out[i] = float(streak)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_047_consecutive_higher_highs_streak_d2(high: pd.Series) -> pd.Series:
    """Current consecutive higher-high (bar > prior bar) streak length."""
    is_hh = (high.diff() > 0).astype(float).to_numpy(copy=True)
    is_hh[0] = np.nan
    n = len(is_hh)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        v = is_hh[i]
        if np.isnan(v):
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if v > 0 else 0
            out[i] = float(streak)
    return (pd.Series(out, index=high.index)).diff().diff()


def f01_athx_048_velocity_new_21d_high_events_per_day_63d_d2(high: pd.Series) -> pd.Series:
    """New 21d-high events per day in trailing 63d (count / 63)."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_nh = (high >= rmax).astype(float)
    return (is_nh.rolling(QDAYS, min_periods=MDAYS).sum() / float(QDAYS)).diff().diff()


def f01_athx_049_distinct_252d_max_levels_in_504d_d2(high: pd.Series) -> pd.Series:
    """Number of distinct strict 252d-max reset levels in trailing 504d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    diff_resets = (rmax.diff() > 0).astype(float)
    return (diff_resets.rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff().diff()


def f01_athx_050_first_new_252d_high_in_last_63d_indicator_d2(high: pd.Series) -> pd.Series:
    """1 if today is a new 252d-high AND no new 252d-high in prior 62 days."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high >= rmax).astype(float)
    prior = is_nh.shift(1).rolling(QDAYS - 1, min_periods=MDAYS).sum()
    today = is_nh
    return (((today > 0) & (prior == 0)).astype(float).where(today.notna() & prior.notna(), np.nan)).diff().diff()


def f01_athx_051_new_high_event_entropy_252d_d2(high: pd.Series) -> pd.Series:
    """Shannon entropy (base 2) of inter-arrival gaps between 21d-highs in 252d window.
    Higher = more dispersed timing; lower = clustered."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    is_nh = (high >= rmax).astype(float)
    def _ent(w):
        idx = np.where(w > 0)[0]
        if idx.size < 3:
            return np.nan
        gaps = np.diff(idx).astype(float)
        # discretize into 5 bins of equal count for entropy
        bins = np.quantile(gaps, [0.2, 0.4, 0.6, 0.8]) if gaps.size >= 5 else None
        if bins is None or len(np.unique(bins)) < 2:
            # fall back: count unique gaps directly
            _, counts = np.unique(gaps, return_counts=True)
            p = counts / counts.sum()
            return float(-(p * np.log2(p)).sum())
        digit = np.digitize(gaps, bins)
        _, counts = np.unique(digit, return_counts=True)
        p = counts / counts.sum()
        return float(-(p * np.log2(p)).sum())
    return (is_nh.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)).diff().diff()


def f01_athx_052_hazard_rate_next_new_252d_high_63d_d2(high: pd.Series) -> pd.Series:
    """Empirical hazard rate: P(new 252d-high tomorrow | bars-since-last) over 63d horizon
    — implemented as count_of_new_252d_highs_in_63d / (63 - bars_since_last)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high >= rmax).astype(float)
    cnt = is_nh.rolling(QDAYS, min_periods=MDAYS).sum()
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        idx = np.where(w > 0)[0]
        if idx.size == 0:
            return float(len(w))
        return float((len(w) - 1) - idx[-1])
    bsl = is_nh.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)
    denom = (QDAYS - bsl).replace(0, np.nan)
    return (_safe_div(cnt, denom)).diff().diff()


def f01_athx_053_inter_252d_high_event_irregularity_index_d2(high: pd.Series) -> pd.Series:
    """Coefficient of variation of inter-arrival gaps between 252d-highs in 504d
    — measures cadence irregularity for the long-window anchor."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high >= rmax).astype(float)
    def _cv(w):
        idx = np.where(w > 0)[0]
        if idx.size < 3:
            return np.nan
        g = np.diff(idx).astype(float)
        m = g.mean()
        if m == 0:
            return np.nan
        return float(g.std(ddof=1) / m)
    return (is_nh.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_cv, raw=True)).diff().diff()


def f01_athx_054_close_position_in_1d_range_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close as percentile of today's intraday range (close-to-high asymmetry)."""
    return (_safe_div(close - low, high - low)).diff().diff()


def f01_athx_055_close_position_in_5d_range_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close as percentile of 5d (weekly) range."""
    rmax = high.rolling(WDAYS, min_periods=2).max()
    rmin = low.rolling(WDAYS, min_periods=2).min()
    return (_safe_div(close - rmin, rmax - rmin)).diff().diff()


def f01_athx_056_close_position_in_21d_range_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close as percentile of 21d (monthly) range."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin = low.rolling(MDAYS, min_periods=WDAYS).min()
    return (_safe_div(close - rmin, rmax - rmin)).diff().diff()


def f01_athx_057_close_position_in_63d_range_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close as percentile of 63d (quarterly) range."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    return (_safe_div(close - rmin, rmax - rmin)).diff().diff()


def f01_athx_058_close_in_top_quintile_of_63d_range_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close in top 20% of 63d range."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return ((pos >= 0.8).astype(float).where(pos.notna(), np.nan)).diff().diff()


def f01_athx_059_close_in_top_quintile_of_252d_range_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close in top 20% of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return ((pos >= 0.8).astype(float).where(pos.notna(), np.nan)).diff().diff()


def f01_athx_060_time_in_top_5pct_of_63d_range_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 21d count of bars with close in top 5% of 63d range."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    inn = (pos >= 0.95).astype(float)
    return (inn.rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff()


def f01_athx_061_time_in_top_5pct_of_252d_range_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d count of bars with close in top 5% of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    inn = (pos >= 0.95).astype(float)
    return (inn.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()


def f01_athx_062_asym_close_to_high_vs_low_at_252d_max_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max, ratio of (high-close)/(close-low) — closing weakness at peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    asym = _safe_div(high - close, close - low)
    return (asym.where(at_peak, np.nan)).diff().diff()


def f01_athx_063_range_truncation_zscore_when_at_252d_max_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max, z-score of (high-close) gap vs 63d distribution
    — flags extreme upper-wick rejection right at the peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    gap = high - close
    z = _rolling_zscore(gap, QDAYS)
    at_peak = high >= rmax
    return (z.where(at_peak, np.nan)).diff().diff()


def f01_athx_064_median_close_pos_in_252d_range_over_5d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d median of close-position-in-252d-range — robust 'at-the-top' measure."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return (pos.rolling(WDAYS, min_periods=2).median()).diff().diff()


def f01_athx_065_slope_of_position_in_252d_range_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of position-in-252d-range — climbing toward top vs sliding from it."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return (_rolling_slope(pos, MDAYS)).diff().diff()


def f01_athx_066_dispersion_of_position_in_252d_range_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d std of position-in-252d-range — does the price oscillate or hug the top?"""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return (pos.rolling(MDAYS, min_periods=WDAYS).std()).diff().diff()


def f01_athx_067_multi_horizon_top_decile_breadth_count_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons {21,63,126,252,504} where close is in top decile of range."""
    pieces = []
    for hz, mp in [(MDAYS, WDAYS), (QDAYS, MDAYS), (126, QDAYS), (YDAYS, QDAYS), (DDAYS_2Y, YDAYS)]:
        rmax = high.rolling(hz, min_periods=mp).max()
        rmin = low.rolling(hz, min_periods=mp).min()
        pos = _safe_div(close - rmin, rmax - rmin)
        pieces.append(((pos >= 0.9).astype(float)).rename(f"h{hz}"))
    df = pd.concat(pieces, axis=1)
    return (df.sum(axis=1)).diff().diff()


def f01_athx_068_close_in_top_quintile_of_5d_range_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close in top 20% of weekly (5d) range."""
    rmax = high.rolling(WDAYS, min_periods=2).max()
    rmin = low.rolling(WDAYS, min_periods=2).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return ((pos >= 0.8).astype(float).where(pos.notna(), np.nan)).diff().diff()


def f01_athx_069_zscore_close_in_504d_window_d2(close: pd.Series) -> pd.Series:
    """Z-score of close in 504d (2y) distribution — long-horizon statistical extension."""
    return (_rolling_zscore(close, DDAYS_2Y, min_periods=YDAYS)).diff().diff()


def f01_athx_070_zscore_close_in_756d_window_d2(close: pd.Series) -> pd.Series:
    """Z-score of close in 756d (3y) distribution — extension over the typical macro cycle."""
    return (_rolling_zscore(close, DDAYS_3Y, min_periods=YDAYS)).diff().diff()


def f01_athx_071_robust_zscore_mad_close_in_252d_d2(close: pd.Series) -> pd.Series:
    """Robust z-score using median + MAD (median absolute deviation) in 252d window
    — heavy-tail-resistant alternative to standard z-score."""
    med = close.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (close - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(close - med, 1.4826 * mad)).diff().diff()


def f01_athx_072_percentile_rank_close_in_252d_d2(close: pd.Series) -> pd.Series:
    """Empirical percentile rank of close in trailing 252d distribution."""
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return (close.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)).diff().diff()


def f01_athx_073_percentile_rank_close_in_504d_d2(close: pd.Series) -> pd.Series:
    """Empirical percentile rank of close in trailing 504d distribution."""
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return (close.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)).diff().diff()


def f01_athx_074_percentile_rank_close_in_1260d_d2(close: pd.Series) -> pd.Series:
    """Empirical percentile rank of close in trailing 1260d (5y) distribution."""
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return (close.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_rk, raw=True)).diff().diff()


def f01_athx_075_hampel_outlier_at_high_indicator_252d_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: at bars where high is the 252d max, Hampel filter flags close as outlier
    ( |close - median| > 3 * 1.4826 * MAD in 252d window )."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    med = close.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (close - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    z = _safe_div(close - med, 1.4826 * mad)
    outlier = (z.abs() > 3.0).astype(float)
    return (outlier.where(at_peak & z.notna(), np.nan)).diff().diff()

# ============================================================
#                         REGISTRY 001_075 (d2)
# ============================================================

ATH_PROXIMITY_EXTENSION_D2_REGISTRY_001_075 = {
    "f01_athx_001_log_dist_above_21d_high_d2": {"inputs": ["high"], "func": f01_athx_001_log_dist_above_21d_high_d2},
    "f01_athx_002_log_dist_above_126d_high_d2": {"inputs": ["high"], "func": f01_athx_002_log_dist_above_126d_high_d2},
    "f01_athx_003_log_dist_above_504d_high_d2": {"inputs": ["high"], "func": f01_athx_003_log_dist_above_504d_high_d2},
    "f01_athx_004_log_dist_above_756d_high_d2": {"inputs": ["high"], "func": f01_athx_004_log_dist_above_756d_high_d2},
    "f01_athx_005_atr_dist_above_21d_high_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_005_atr_dist_above_21d_high_d2},
    "f01_athx_006_atr_dist_above_63d_high_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_006_atr_dist_above_63d_high_d2},
    "f01_athx_007_atr_dist_above_252d_high_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_007_atr_dist_above_252d_high_d2},
    "f01_athx_008_atr_dist_above_504d_high_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_008_atr_dist_above_504d_high_d2},
    "f01_athx_009_sigma_dist_above_252d_high_d2": {"inputs": ["high", "close"], "func": f01_athx_009_sigma_dist_above_252d_high_d2},
    "f01_athx_010_pct_dist_above_252d_high_d2": {"inputs": ["high"], "func": f01_athx_010_pct_dist_above_252d_high_d2},
    "f01_athx_011_dollar_dist_above_252d_high_norm_close_d2": {"inputs": ["high", "close"], "func": f01_athx_011_dollar_dist_above_252d_high_norm_close_d2},
    "f01_athx_012_atr_dist_above_126d_high_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_012_atr_dist_above_126d_high_d2},
    "f01_athx_013_log_dist_above_expanding_alltime_high_d2": {"inputs": ["high"], "func": f01_athx_013_log_dist_above_expanding_alltime_high_d2},
    "f01_athx_014_atr_dist_above_alltime_high_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_014_atr_dist_above_alltime_high_d2},
    "f01_athx_015_days_since_alltime_high_d2": {"inputs": ["high"], "func": f01_athx_015_days_since_alltime_high_d2},
    "f01_athx_016_fraction_expanding_within_5pct_of_alltime_d2": {"inputs": ["high"], "func": f01_athx_016_fraction_expanding_within_5pct_of_alltime_d2},
    "f01_athx_017_bars_between_distinct_alltime_high_resets_d2": {"inputs": ["high"], "func": f01_athx_017_bars_between_distinct_alltime_high_resets_d2},
    "f01_athx_018_alltime_high_recency_years_d2": {"inputs": ["high"], "func": f01_athx_018_alltime_high_recency_years_d2},
    "f01_athx_019_alltime_high_recency_zscore_d2": {"inputs": ["high"], "func": f01_athx_019_alltime_high_recency_zscore_d2},
    "f01_athx_020_lifetime_high_persistence_ratio_d2": {"inputs": ["high"], "func": f01_athx_020_lifetime_high_persistence_ratio_d2},
    "f01_athx_021_log_dist_above_prior_calendar_year_high_d2": {"inputs": ["high"], "func": f01_athx_021_log_dist_above_prior_calendar_year_high_d2},
    "f01_athx_022_log_dist_above_prior_calendar_quarter_high_d2": {"inputs": ["high"], "func": f01_athx_022_log_dist_above_prior_calendar_quarter_high_d2},
    "f01_athx_023_log_dist_above_prior_calendar_month_high_d2": {"inputs": ["high"], "func": f01_athx_023_log_dist_above_prior_calendar_month_high_d2},
    "f01_athx_024_log_dist_above_ytd_high_d2": {"inputs": ["high"], "func": f01_athx_024_log_dist_above_ytd_high_d2},
    "f01_athx_025_log_dist_above_qtd_high_d2": {"inputs": ["high"], "func": f01_athx_025_log_dist_above_qtd_high_d2},
    "f01_athx_026_days_since_ytd_high_d2": {"inputs": ["high"], "func": f01_athx_026_days_since_ytd_high_d2},
    "f01_athx_027_days_since_prior_calendar_year_high_d2": {"inputs": ["high"], "func": f01_athx_027_days_since_prior_calendar_year_high_d2},
    "f01_athx_028_ratio_ytd_high_to_prior_year_high_d2": {"inputs": ["high"], "func": f01_athx_028_ratio_ytd_high_to_prior_year_high_d2},
    "f01_athx_029_dwell_within_half_pct_of_252d_max_21d_d2": {"inputs": ["high"], "func": f01_athx_029_dwell_within_half_pct_of_252d_max_21d_d2},
    "f01_athx_030_mean_time_between_21d_high_prints_252d_d2": {"inputs": ["high"], "func": f01_athx_030_mean_time_between_21d_high_prints_252d_d2},
    "f01_athx_031_cum_time_in_top_decile_of_252d_range_63d_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_031_cum_time_in_top_decile_of_252d_range_63d_d2},
    "f01_athx_032_time_since_first_minus_last_252d_high_in_252d_d2": {"inputs": ["high"], "func": f01_athx_032_time_since_first_minus_last_252d_high_in_252d_d2},
    "f01_athx_033_median_bars_between_252d_high_prints_504d_d2": {"inputs": ["high"], "func": f01_athx_033_median_bars_between_252d_high_prints_504d_d2},
    "f01_athx_034_calendar_months_since_alltime_high_d2": {"inputs": ["high"], "func": f01_athx_034_calendar_months_since_alltime_high_d2},
    "f01_athx_035_bars_since_most_recent_5y_high_d2": {"inputs": ["high"], "func": f01_athx_035_bars_since_most_recent_5y_high_d2},
    "f01_athx_036_stale_high_indicator_no_new_252d_in_63d_d2": {"inputs": ["high"], "func": f01_athx_036_stale_high_indicator_no_new_252d_in_63d_d2},
    "f01_athx_037_half_life_dist_from_252d_high_decay_63d_d2": {"inputs": ["high"], "func": f01_athx_037_half_life_dist_from_252d_high_decay_63d_d2},
    "f01_athx_038_persistence_within_1pct_of_252d_high_state_d2": {"inputs": ["high"], "func": f01_athx_038_persistence_within_1pct_of_252d_high_state_d2},
    "f01_athx_039_count_new_5d_highs_in_63d_d2": {"inputs": ["high"], "func": f01_athx_039_count_new_5d_highs_in_63d_d2},
    "f01_athx_040_count_new_21d_highs_in_126d_d2": {"inputs": ["high"], "func": f01_athx_040_count_new_21d_highs_in_126d_d2},
    "f01_athx_041_count_new_63d_highs_in_252d_d2": {"inputs": ["high"], "func": f01_athx_041_count_new_63d_highs_in_252d_d2},
    "f01_athx_042_count_new_126d_highs_in_504d_d2": {"inputs": ["high"], "func": f01_athx_042_count_new_126d_highs_in_504d_d2},
    "f01_athx_043_mean_gap_between_21d_high_events_252d_d2": {"inputs": ["high"], "func": f01_athx_043_mean_gap_between_21d_high_events_252d_d2},
    "f01_athx_044_std_gap_between_21d_high_events_252d_d2": {"inputs": ["high"], "func": f01_athx_044_std_gap_between_21d_high_events_252d_d2},
    "f01_athx_045_acceleration_of_new_21d_high_rate_d2": {"inputs": ["high"], "func": f01_athx_045_acceleration_of_new_21d_high_rate_d2},
    "f01_athx_046_consecutive_new_5d_highs_streak_d2": {"inputs": ["high"], "func": f01_athx_046_consecutive_new_5d_highs_streak_d2},
    "f01_athx_047_consecutive_higher_highs_streak_d2": {"inputs": ["high"], "func": f01_athx_047_consecutive_higher_highs_streak_d2},
    "f01_athx_048_velocity_new_21d_high_events_per_day_63d_d2": {"inputs": ["high"], "func": f01_athx_048_velocity_new_21d_high_events_per_day_63d_d2},
    "f01_athx_049_distinct_252d_max_levels_in_504d_d2": {"inputs": ["high"], "func": f01_athx_049_distinct_252d_max_levels_in_504d_d2},
    "f01_athx_050_first_new_252d_high_in_last_63d_indicator_d2": {"inputs": ["high"], "func": f01_athx_050_first_new_252d_high_in_last_63d_indicator_d2},
    "f01_athx_051_new_high_event_entropy_252d_d2": {"inputs": ["high"], "func": f01_athx_051_new_high_event_entropy_252d_d2},
    "f01_athx_052_hazard_rate_next_new_252d_high_63d_d2": {"inputs": ["high"], "func": f01_athx_052_hazard_rate_next_new_252d_high_63d_d2},
    "f01_athx_053_inter_252d_high_event_irregularity_index_d2": {"inputs": ["high"], "func": f01_athx_053_inter_252d_high_event_irregularity_index_d2},
    "f01_athx_054_close_position_in_1d_range_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_athx_054_close_position_in_1d_range_d2},
    "f01_athx_055_close_position_in_5d_range_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_055_close_position_in_5d_range_d2},
    "f01_athx_056_close_position_in_21d_range_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_056_close_position_in_21d_range_d2},
    "f01_athx_057_close_position_in_63d_range_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_057_close_position_in_63d_range_d2},
    "f01_athx_058_close_in_top_quintile_of_63d_range_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_058_close_in_top_quintile_of_63d_range_d2},
    "f01_athx_059_close_in_top_quintile_of_252d_range_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_059_close_in_top_quintile_of_252d_range_d2},
    "f01_athx_060_time_in_top_5pct_of_63d_range_21d_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_060_time_in_top_5pct_of_63d_range_21d_d2},
    "f01_athx_061_time_in_top_5pct_of_252d_range_63d_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_061_time_in_top_5pct_of_252d_range_63d_d2},
    "f01_athx_062_asym_close_to_high_vs_low_at_252d_max_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_062_asym_close_to_high_vs_low_at_252d_max_d2},
    "f01_athx_063_range_truncation_zscore_when_at_252d_max_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_063_range_truncation_zscore_when_at_252d_max_d2},
    "f01_athx_064_median_close_pos_in_252d_range_over_5d_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_064_median_close_pos_in_252d_range_over_5d_d2},
    "f01_athx_065_slope_of_position_in_252d_range_21d_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_065_slope_of_position_in_252d_range_21d_d2},
    "f01_athx_066_dispersion_of_position_in_252d_range_21d_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_066_dispersion_of_position_in_252d_range_21d_d2},
    "f01_athx_067_multi_horizon_top_decile_breadth_count_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_067_multi_horizon_top_decile_breadth_count_d2},
    "f01_athx_068_close_in_top_quintile_of_5d_range_d2": {"inputs": ["high", "low", "close"], "func": f01_athx_068_close_in_top_quintile_of_5d_range_d2},
    "f01_athx_069_zscore_close_in_504d_window_d2": {"inputs": ["close"], "func": f01_athx_069_zscore_close_in_504d_window_d2},
    "f01_athx_070_zscore_close_in_756d_window_d2": {"inputs": ["close"], "func": f01_athx_070_zscore_close_in_756d_window_d2},
    "f01_athx_071_robust_zscore_mad_close_in_252d_d2": {"inputs": ["close"], "func": f01_athx_071_robust_zscore_mad_close_in_252d_d2},
    "f01_athx_072_percentile_rank_close_in_252d_d2": {"inputs": ["close"], "func": f01_athx_072_percentile_rank_close_in_252d_d2},
    "f01_athx_073_percentile_rank_close_in_504d_d2": {"inputs": ["close"], "func": f01_athx_073_percentile_rank_close_in_504d_d2},
    "f01_athx_074_percentile_rank_close_in_1260d_d2": {"inputs": ["close"], "func": f01_athx_074_percentile_rank_close_in_1260d_d2},
    "f01_athx_075_hampel_outlier_at_high_indicator_252d_d2": {"inputs": ["high", "close"], "func": f01_athx_075_hampel_outlier_at_high_indicator_252d_d2},
}
