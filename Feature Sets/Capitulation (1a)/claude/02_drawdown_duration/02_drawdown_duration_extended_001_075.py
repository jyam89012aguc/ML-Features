"""
02_drawdown_duration — Extended Features 001-075
Domain: recovery time, drawdown-spell distribution, time-decay since new high,
        underwater-to-at-high ratios, age vs depth, duration z-scores at new windows
Asset class: US equities | Daily OHLCV only (SEP folder — no fundamental inputs)
Target: capitulation features at/near multi-year absolute low
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MO = 21
_TD_WK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    """Number of bars since the all-time (expanding) maximum occurred."""
    cummax = s.cummax()
    is_new_high = (s >= cummax)
    pos = pd.Series(np.arange(len(s)), index=s.index)
    last_high_pos = pos.where(is_new_high).ffill().fillna(0)
    return pos - last_high_pos


def _underwater_expanding_flag(s: pd.Series) -> pd.Series:
    """1 if below all-time high, 0 otherwise."""
    return (s < s.cummax()).astype(float)


def _consec_streak(flag: pd.Series) -> pd.Series:
    """Current consecutive run length of flag==1."""
    groups = (flag == 0).cumsum()
    return flag.groupby(groups).cumsum()


def _spell_lengths_in_window(flag: pd.Series, w: int) -> pd.Series:
    """
    For each date, scan the trailing w-bar window and return the vector of
    completed drawdown-spell lengths (runs of 1 in flag) as a list stored
    in an object Series.  Used only internally by aggregator helpers — never
    passed to rolling().apply() directly.
    """
    arr = flag.values
    n = len(arr)
    result = [None] * n
    for i in range(n):
        start = max(0, i - w + 1)
        window = arr[start: i + 1]
        spells = []
        cur = 0
        for v in window:
            if v == 1.0:
                cur += 1
            else:
                if cur > 0:
                    spells.append(cur)
                    cur = 0
        # do NOT append current open spell — backward-looking only closed spells
        result[i] = spells
    return pd.Series(result, index=flag.index)


def _spell_agg(flag: pd.Series, w: int, agg: str) -> pd.Series:
    """Aggregate completed spell lengths within trailing w-bar window."""
    spells_s = _spell_lengths_in_window(flag, w)
    out = np.full(len(flag), np.nan)
    for i, spells in enumerate(spells_s):
        if spells and len(spells) > 0:
            a = np.array(spells, dtype=float)
            if agg == "mean":
                out[i] = a.mean()
            elif agg == "median":
                out[i] = np.median(a)
            elif agg == "max":
                out[i] = a.max()
            elif agg == "count":
                out[i] = float(len(a))
            elif agg == "std":
                out[i] = a.std() if len(a) > 1 else 0.0
            elif agg == "sum":
                out[i] = a.sum()
        else:
            if agg == "count":
                out[i] = 0.0
            elif agg == "sum":
                out[i] = 0.0
    return pd.Series(out, index=flag.index)


def _current_spell_pctrank_in_window(flag: pd.Series, w: int) -> pd.Series:
    """
    Percentile rank of current open spell length among all completed spell
    lengths within the trailing w-bar window.
    """
    spells_s = _spell_lengths_in_window(flag, w)
    cur_streak = _consec_streak(flag)
    out = np.full(len(flag), np.nan)
    for i in range(len(flag)):
        spells = spells_s.iloc[i]
        cur = cur_streak.iloc[i]
        if cur == 0:
            out[i] = 0.0
        elif spells and len(spells) > 0:
            a = np.array(spells, dtype=float)
            out[i] = float(np.mean(a <= cur))
        else:
            out[i] = 1.0
    return pd.Series(out, index=flag.index)


def _last_high_pos_series(close: pd.Series) -> pd.Series:
    """Integer position of the most recent all-time high (expanding)."""
    cummax = close.cummax()
    is_new_high = (close >= cummax)
    pos = pd.Series(np.arange(len(close)), index=close.index)
    return pos.where(is_new_high).ffill().fillna(0)


def _last_low_pos_series(close: pd.Series) -> pd.Series:
    """Integer position of the most recent all-time low (expanding)."""
    cummin = close.cummin()
    is_new_low = (close <= cummin)
    pos = pd.Series(np.arange(len(close)), index=close.index)
    return pos.where(is_new_low).ffill().fillna(0)


# ── Feature functions 001–075 ─────────────────────────────────────────────────

# --- Group A: elapsed recovery time (time since price was BELOW current level on way down) ---

def ddur_ext_001_bars_elapsed_since_level_crossed_up(close: pd.Series) -> pd.Series:
    """
    Backward-looking recovery-elapsed time: for each bar, find the most recent
    prior bar where close was strictly below today's close AND the close had
    been declining (close[t-1] < close[t-2]).  Returns bars elapsed since that
    bar.  Proxy for 'time already spent recovering from the trough.'
    """
    n = len(close)
    arr = close.values
    result = np.full(n, np.nan)
    for i in range(2, n):
        c_today = arr[i]
        # scan backward for last bar j where arr[j] < c_today
        for j in range(i - 1, -1, -1):
            if arr[j] < c_today:
                result[i] = float(i - j)
                break
        else:
            result[i] = float(i)
    return pd.Series(result, index=close.index)


def ddur_ext_002_recovery_elapsed_since_trough_ath(close: pd.Series) -> pd.Series:
    """
    Bars elapsed since the trough of the current ATH drawdown spell.
    Trough = bar with the minimum close since the last ATH.
    Backward-looking: 0 if a new ATH was just set.
    """
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_ath_pos = _last_high_pos_series(close).astype(int)
    n = len(close)
    arr = close.values
    result = np.full(n, np.nan)
    for i in range(n):
        ath_p = int(last_ath_pos.iloc[i])
        if ath_p == i:
            result[i] = 0.0
        else:
            segment = arr[ath_p: i + 1]
            trough_idx = int(np.argmin(segment))
            result[i] = float(i - (ath_p + trough_idx))
    return pd.Series(result, index=close.index)


def ddur_ext_003_recovery_fraction_of_drawdown_spell(close: pd.Series) -> pd.Series:
    """
    Recovery fraction: bars_elapsed_since_trough / total_bars_in_current_drawdown_spell.
    0 = just hit trough, 1 = fully recovered (new ATH).  Backward-looking only.
    """
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_ath_pos = _last_high_pos_series(close).astype(int)
    n = len(close)
    arr = close.values
    result = np.full(n, np.nan)
    for i in range(n):
        ath_p = int(last_ath_pos.iloc[i])
        if ath_p == i:
            result[i] = 1.0
        else:
            segment = arr[ath_p: i + 1]
            trough_idx = int(np.argmin(segment))
            spell_len = float(i - ath_p)
            bars_since_trough = float(i - (ath_p + trough_idx))
            if spell_len > 0:
                result[i] = bars_since_trough / spell_len
            else:
                result[i] = np.nan
    return pd.Series(result, index=close.index)


def ddur_ext_004_price_recovery_pct_from_trough(close: pd.Series) -> pd.Series:
    """
    Percentage price recovered from the trough of the current ATH drawdown spell.
    (close - trough_price) / (ath_price - trough_price).  Bounded [0,1] within spell.
    """
    last_ath_pos = _last_high_pos_series(close).astype(int)
    n = len(close)
    arr = close.values
    result = np.full(n, np.nan)
    for i in range(n):
        ath_p = int(last_ath_pos.iloc[i])
        ath_price = arr[ath_p]
        if ath_p == i:
            result[i] = 1.0
        else:
            segment = arr[ath_p: i + 1]
            trough_price = float(np.min(segment))
            denom = ath_price - trough_price
            if denom > _EPS:
                result[i] = (arr[i] - trough_price) / denom
            else:
                result[i] = np.nan
    return pd.Series(result, index=close.index)


def ddur_ext_005_price_vs_midpoint_ath_trough(close: pd.Series) -> pd.Series:
    """
    Whether close is above the midpoint of [trough, ATH] within current drawdown spell.
    1 = above midpoint (upper half of recovery), 0 = below midpoint.
    """
    last_ath_pos = _last_high_pos_series(close).astype(int)
    n = len(close)
    arr = close.values
    result = np.full(n, np.nan)
    for i in range(n):
        ath_p = int(last_ath_pos.iloc[i])
        ath_price = arr[ath_p]
        if ath_p == i:
            result[i] = 1.0
        else:
            segment = arr[ath_p: i + 1]
            trough_price = float(np.min(segment))
            midpoint = (ath_price + trough_price) / 2.0
            result[i] = 1.0 if arr[i] >= midpoint else 0.0
    return pd.Series(result, index=close.index)


def ddur_ext_006_trough_depth_pct_in_current_spell(close: pd.Series) -> pd.Series:
    """
    Depth of the trough in the current ATH drawdown spell:
    (ath_price - trough_price) / ath_price.  Stays constant until new ATH.
    """
    last_ath_pos = _last_high_pos_series(close).astype(int)
    n = len(close)
    arr = close.values
    result = np.full(n, np.nan)
    for i in range(n):
        ath_p = int(last_ath_pos.iloc[i])
        ath_price = arr[ath_p]
        if ath_p == i:
            result[i] = 0.0
        else:
            segment = arr[ath_p: i + 1]
            trough_price = float(np.min(segment))
            if ath_price > _EPS:
                result[i] = (ath_price - trough_price) / ath_price
            else:
                result[i] = np.nan
    return pd.Series(result, index=close.index)


def ddur_ext_007_recovery_time_per_unit_depth(close: pd.Series) -> pd.Series:
    """
    Bars-since-trough / trough-depth-fraction.
    High value = slow recovery per unit of depth (sluggish recovery).
    """
    rec_elapsed = ddur_ext_002_recovery_elapsed_since_trough_ath(close)
    depth = ddur_ext_006_trough_depth_pct_in_current_spell(close)
    return _safe_div(rec_elapsed, depth.replace(0, np.nan))


def ddur_ext_008_expected_recovery_proxy_vol_scaled(close: pd.Series) -> pd.Series:
    """
    Expected recovery time proxy: trough_depth / annualized_vol.
    Larger = deeper drawdown relative to volatility, longer expected recovery.
    Backward-looking (uses realized vol up to today).
    """
    depth = ddur_ext_006_trough_depth_pct_in_current_spell(close)
    vol = close.pct_change().rolling(_TD_QTR, min_periods=10).std() * np.sqrt(_TD_YEAR)
    vol = vol.fillna(vol.expanding().mean())
    return _safe_div(depth, vol)


def ddur_ext_009_drawdown_duration_exceeds_historical_median_recovery(close: pd.Series) -> pd.Series:
    """
    Flag: 1 if the current drawdown spell length (bars since ATH) exceeds the
    median completed drawdown spell length in the trailing 504-bar window.
    Proxy for 'this drawdown has lasted longer than typical.'
    """
    dsh = _days_since_expanding_high(close)
    uw_flag = _underwater_expanding_flag(close)
    median_spell = _spell_agg(uw_flag, 504, "median")
    return (dsh > median_spell).astype(float)


def ddur_ext_010_drawdown_duration_pctrank_vs_historical_spells(close: pd.Series) -> pd.Series:
    """
    Percentile rank of current drawdown spell age (bars since ATH) among
    all completed drawdown spells in the trailing 504-bar window.
    """
    dsh = _days_since_expanding_high(close)
    uw_flag = _underwater_expanding_flag(close)
    spells_s = _spell_lengths_in_window(uw_flag, 504)
    out = np.full(len(close), np.nan)
    for i in range(len(close)):
        spells = spells_s.iloc[i]
        cur = dsh.iloc[i]
        if spells and len(spells) > 0:
            a = np.array(spells, dtype=float)
            out[i] = float(np.mean(a <= cur))
        else:
            out[i] = np.nan
    return pd.Series(out, index=close.index)


# --- Group B: distribution of underwater-spell lengths ---

def ddur_ext_011_mean_spell_len_under_ath_252d(close: pd.Series) -> pd.Series:
    """Mean length of completed drawdown spells below ATH in trailing 252-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, _TD_YEAR, "mean")


def ddur_ext_012_median_spell_len_under_ath_252d(close: pd.Series) -> pd.Series:
    """Median length of completed drawdown spells below ATH in trailing 252-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, _TD_YEAR, "median")


def ddur_ext_013_max_spell_len_under_ath_252d(close: pd.Series) -> pd.Series:
    """Max completed drawdown spell length below ATH in trailing 252-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, _TD_YEAR, "max")


def ddur_ext_014_mean_spell_len_under_ath_504d(close: pd.Series) -> pd.Series:
    """Mean length of completed drawdown spells below ATH in trailing 504-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, 504, "mean")


def ddur_ext_015_max_spell_len_under_ath_504d(close: pd.Series) -> pd.Series:
    """Max completed drawdown spell length below ATH in trailing 504-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, 504, "max")


def ddur_ext_016_std_spell_len_under_ath_252d(close: pd.Series) -> pd.Series:
    """Std dev of completed drawdown spell lengths below ATH in trailing 252-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, _TD_YEAR, "std")


def ddur_ext_017_mean_spell_len_under_252d_high_252d(close: pd.Series) -> pd.Series:
    """Mean length of completed drawdown spells below 252d high in trailing 252-bar window."""
    uw = (close < _rolling_max(close, _TD_YEAR)).astype(float)
    return _spell_agg(uw, _TD_YEAR, "mean")


def ddur_ext_018_max_spell_len_under_252d_high_252d(close: pd.Series) -> pd.Series:
    """Max completed drawdown spell length below 252d high in trailing 252-bar window."""
    uw = (close < _rolling_max(close, _TD_YEAR)).astype(float)
    return _spell_agg(uw, _TD_YEAR, "max")


def ddur_ext_019_count_distinct_spells_under_ath_252d(close: pd.Series) -> pd.Series:
    """Count of distinct completed drawdown spells below ATH in trailing 252-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, _TD_YEAR, "count")


def ddur_ext_020_count_distinct_spells_under_ath_504d(close: pd.Series) -> pd.Series:
    """Count of distinct completed drawdown spells below ATH in trailing 504-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, 504, "count")


def ddur_ext_021_count_distinct_spells_under_252d_high_252d(close: pd.Series) -> pd.Series:
    """Count of distinct completed drawdown spells below 252d high in trailing 252-bar window."""
    uw = (close < _rolling_max(close, _TD_YEAR)).astype(float)
    return _spell_agg(uw, _TD_YEAR, "count")


def ddur_ext_022_current_spell_pctrank_under_ath_252d(close: pd.Series) -> pd.Series:
    """
    Percentile rank of the current open drawdown-spell length (below ATH) among
    all completed spell lengths in the trailing 252-bar window.
    """
    uw = _underwater_expanding_flag(close)
    return _current_spell_pctrank_in_window(uw, _TD_YEAR)


def ddur_ext_023_current_spell_pctrank_under_ath_504d(close: pd.Series) -> pd.Series:
    """
    Percentile rank of the current open drawdown-spell length (below ATH) among
    all completed spell lengths in the trailing 504-bar window.
    """
    uw = _underwater_expanding_flag(close)
    return _current_spell_pctrank_in_window(uw, 504)


def ddur_ext_024_current_spell_pctrank_under_252d_high_252d(close: pd.Series) -> pd.Series:
    """
    Percentile rank of current open spell below 252d high among completed spells
    in trailing 252-bar window.
    """
    uw = (close < _rolling_max(close, _TD_YEAR)).astype(float)
    return _current_spell_pctrank_in_window(uw, _TD_YEAR)


def ddur_ext_025_total_bars_in_spells_under_ath_252d(close: pd.Series) -> pd.Series:
    """Total bars spent inside completed drawdown spells below ATH in trailing 252-bar window."""
    uw = _underwater_expanding_flag(close)
    return _spell_agg(uw, _TD_YEAR, "sum")


# --- Group C: time-decay since last new high (new transforms) ---

def ddur_ext_026_time_decay_since_252d_high_halflife_21d(close: pd.Series) -> pd.Series:
    """
    Exponential time-decay of bars-since-252d-high with half-life = 21 bars.
    Shorter half-life than existing features (existing use 63d, 252d).
    """
    dsh = _days_since_expanding_high(close)
    return np.exp(-dsh * np.log(2.0) / _TD_MO)


def ddur_ext_027_time_decay_since_ath_halflife_126d(close: pd.Series) -> pd.Series:
    """
    Exponential time-decay of days-since-ATH with half-life = 126 bars.
    Fills gap between existing 63d and 252d half-lives.
    """
    dsh = _days_since_expanding_high(close)
    return np.exp(-dsh * np.log(2.0) / _TD_HALF)


def ddur_ext_028_time_decay_since_ath_halflife_504d(close: pd.Series) -> pd.Series:
    """
    Exponential time-decay of days-since-ATH with half-life = 504 bars.
    Long-cycle decay not in existing features.
    """
    dsh = _days_since_expanding_high(close)
    return np.exp(-dsh * np.log(2.0) / 504.0)


def ddur_ext_029_time_decay_since_new_252d_high_halflife_63d(close: pd.Series) -> pd.Series:
    """
    Decay of bars since last new 252d rolling high was set, half-life = 63 bars.
    Uses the 252d-high event (not ATH) unlike existing decay features.
    """
    is_high = (close == _rolling_max(close, _TD_YEAR))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(is_high).ffill().fillna(0)
    dsh = pos - last_pos
    return np.exp(-dsh * np.log(2.0) / _TD_QTR)


def ddur_ext_030_log_time_since_ath(close: pd.Series) -> pd.Series:
    """
    log1p(days_since_ATH): compresses large values for use as a feature.
    Not in existing features (which use raw counts, norms, and exp-decays).
    """
    dsh = _days_since_expanding_high(close)
    return np.log1p(dsh)


def ddur_ext_031_log_time_since_252d_high(close: pd.Series) -> pd.Series:
    """log1p(days_since_252d_high): log-compressed version of rolling-high age."""
    dsh = close.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True
    )
    return np.log1p(dsh)


def ddur_ext_032_sqrt_time_since_ath(close: pd.Series) -> pd.Series:
    """sqrt(days_since_ATH): square-root compressed age."""
    dsh = _days_since_expanding_high(close)
    return np.sqrt(dsh)


# --- Group D: ratio of time-underwater to time-at-highs ---

def ddur_ext_033_underwater_to_at_high_ratio_252d(close: pd.Series) -> pd.Series:
    """
    Ratio: days_underwater_below_ath / days_at_or_above_ath in trailing 252d.
    High = mostly underwater; low = mostly at highs.
    """
    uw = _underwater_expanding_flag(close)
    uw_count = _rolling_sum(uw, _TD_YEAR)
    at_high_count = _rolling_sum(1.0 - uw, _TD_YEAR)
    return _safe_div(uw_count, at_high_count.replace(0, np.nan))


def ddur_ext_034_underwater_to_at_high_ratio_504d(close: pd.Series) -> pd.Series:
    """
    Ratio: days_underwater_below_ath / days_at_or_above_ath in trailing 504d.
    """
    uw = _underwater_expanding_flag(close)
    uw_count = _rolling_sum(uw, 504)
    at_high_count = _rolling_sum(1.0 - uw, 504)
    return _safe_div(uw_count, at_high_count.replace(0, np.nan))


def ddur_ext_035_underwater_to_at_high_ratio_expanding(close: pd.Series) -> pd.Series:
    """
    Expanding ratio: cumulative days below ATH / cumulative days at or above ATH.
    """
    uw = _underwater_expanding_flag(close)
    uw_cum = uw.expanding().sum()
    at_high_cum = (1.0 - uw).expanding().sum()
    return _safe_div(uw_cum, at_high_cum.replace(0, np.nan))


def ddur_ext_036_at_high_fraction_expanding(close: pd.Series) -> pd.Series:
    """
    Expanding fraction of all bars where price was at or above its ATH
    (i.e., was setting a new all-time high or matching it).
    """
    at_high = (1.0 - _underwater_expanding_flag(close))
    return at_high.expanding().mean()


def ddur_ext_037_at_high_fraction_252d(close: pd.Series) -> pd.Series:
    """
    Fraction of last 252 bars where price was at or above its expanding ATH.
    Complement of ddur_027 which uses rolling-window high.
    """
    at_high = (1.0 - _underwater_expanding_flag(close))
    return _rolling_mean(at_high, _TD_YEAR)


def ddur_ext_038_high_touch_interval_mean_252d(close: pd.Series) -> pd.Series:
    """
    Mean interval (in bars) between successive ATH touches in trailing 252-bar window.
    High interval = very rare new highs = deep stagnation.
    """
    is_at_high = (1.0 - _underwater_expanding_flag(close))
    count = _rolling_sum(is_at_high, _TD_YEAR)
    return _safe_div(pd.Series(float(_TD_YEAR), index=close.index), count)


def ddur_ext_039_high_touch_interval_mean_504d(close: pd.Series) -> pd.Series:
    """
    Mean interval (in bars) between successive ATH touches in trailing 504-bar window.
    """
    is_at_high = (1.0 - _underwater_expanding_flag(close))
    count = _rolling_sum(is_at_high, 504)
    return _safe_div(pd.Series(504.0, index=close.index), count)


def ddur_ext_040_uw_to_at_high_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """
    Z-score (over 252d) of the rolling 252d underwater-to-at-high ratio.
    """
    ratio = ddur_ext_033_underwater_to_at_high_ratio_252d(close)
    mu = _rolling_mean(ratio, _TD_YEAR)
    sigma = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - mu, sigma)


# --- Group E: age of current drawdown vs its depth ---

def ddur_ext_041_age_to_depth_ratio_ath(close: pd.Series) -> pd.Series:
    """
    Current drawdown age (bars since ATH) divided by drawdown depth (fraction from ATH).
    High value = old drawdown relative to its depth (stale decline, slow recovery).
    """
    age = _days_since_expanding_high(close)
    ath = close.cummax()
    depth = _safe_div(ath - close, ath)
    return _safe_div(age, depth)


def ddur_ext_042_age_to_depth_ratio_252d_high(close: pd.Series) -> pd.Series:
    """
    Current drawdown age (bars since 252d high) divided by drawdown depth from 252d high.
    """
    h252 = _rolling_max(close, _TD_YEAR)
    age = close.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True
    )
    depth = _safe_div(h252 - close, h252)
    return _safe_div(age, depth)


def ddur_ext_043_depth_per_unit_age_ath(close: pd.Series) -> pd.Series:
    """
    Drawdown depth from ATH per bar of drawdown age.
    High value = drawdown deepening quickly; low = stalling in shallow zone.
    """
    age = _days_since_expanding_high(close)
    ath = close.cummax()
    depth = _safe_div(ath - close, ath)
    return _safe_div(depth, age.replace(0, np.nan))


def ddur_ext_044_trough_age_product(close: pd.Series) -> pd.Series:
    """
    Product of trough depth fraction and drawdown age (bars since ATH).
    Captures severity x duration simultaneously.
    """
    age = _days_since_expanding_high(close)
    depth = ddur_ext_006_trough_depth_pct_in_current_spell(close)
    return age * depth


def ddur_ext_045_age_above_expected_for_depth_flag(close: pd.Series) -> pd.Series:
    """
    Flag: 1 if current drawdown age exceeds the rolling 252d mean age of drawdowns
    at similar depth (depth within ±5% of current depth).  Proxy for 'longer than
    typical for this severity.'  Backward-looking median used as threshold.
    """
    age = _days_since_expanding_high(close)
    ath = close.cummax()
    depth = _safe_div(ath - close, ath).fillna(0)
    # rolling median age as a simple threshold (self-contained, no cross-file)
    median_age = _rolling_median(age, _TD_YEAR)
    return (age > median_age).astype(float)


def ddur_ext_046_normalized_age_vs_trough_depth(close: pd.Series) -> pd.Series:
    """
    (age - mean_age_252d) / (trough_depth + eps).
    Measures age adjusted for depth, z-score-like but depth-denominated.
    """
    age = _days_since_expanding_high(close)
    mu_age = _rolling_mean(age, _TD_YEAR)
    depth = ddur_ext_006_trough_depth_pct_in_current_spell(close).fillna(0) + _EPS
    return (age - mu_age) / depth


def ddur_ext_047_recovery_pct_vs_elapsed_recovery_time(close: pd.Series) -> pd.Series:
    """
    Price recovery fraction / elapsed recovery time (bars since trough).
    High = fast recovery per bar; low = stalled recovery.
    """
    rec_pct = ddur_ext_004_price_recovery_pct_from_trough(close)
    elapsed = ddur_ext_002_recovery_elapsed_since_trough_ath(close)
    return _safe_div(rec_pct, elapsed.replace(0, np.nan))


def ddur_ext_048_recovery_momentum_5d(close: pd.Series) -> pd.Series:
    """
    5-bar change in price-recovery-fraction (acceleration of the recovery).
    Backward-looking only; uses rec_pct from ddur_ext_004.
    """
    rec_pct = ddur_ext_004_price_recovery_pct_from_trough(close)
    return rec_pct.diff(5)


def ddur_ext_049_recovery_momentum_21d(close: pd.Series) -> pd.Series:
    """
    21-bar change in price-recovery-fraction from trough.
    """
    rec_pct = ddur_ext_004_price_recovery_pct_from_trough(close)
    return rec_pct.diff(_TD_MO)


def ddur_ext_050_recovery_stall_flag_5d(close: pd.Series) -> pd.Series:
    """
    Flag: 1 if 5-bar recovery momentum is negative (recovery stalling/reversing).
    """
    mom = ddur_ext_048_recovery_momentum_5d(close)
    return (mom < 0).astype(float)


# --- Group F: duration z-scores and percentile ranks at additional windows ---

def ddur_ext_051_dsh_ath_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-ATH over trailing 252-bar window."""
    dsh = _days_since_expanding_high(close)
    mu = _rolling_mean(dsh, _TD_YEAR)
    sigma = _rolling_std(dsh, _TD_YEAR)
    return _safe_div(dsh - mu, sigma)


def ddur_ext_052_dsh_ath_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-ATH over trailing 126-bar window."""
    dsh = _days_since_expanding_high(close)
    mu = _rolling_mean(dsh, _TD_HALF)
    sigma = _rolling_std(dsh, _TD_HALF)
    return _safe_div(dsh - mu, sigma)


def ddur_ext_053_dsh_ath_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-ATH over trailing 63-bar window."""
    dsh = _days_since_expanding_high(close)
    mu = _rolling_mean(dsh, _TD_QTR)
    sigma = _rolling_std(dsh, _TD_QTR)
    return _safe_div(dsh - mu, sigma)


def ddur_ext_054_dsh_252d_high_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-252d-high over trailing 126-bar window."""
    dsh = close.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True
    )
    mu = _rolling_mean(dsh, _TD_HALF)
    sigma = _rolling_std(dsh, _TD_HALF)
    return _safe_div(dsh - mu, sigma)


def ddur_ext_055_dsh_252d_high_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-252d-high over trailing 63-bar window."""
    dsh = close.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True
    )
    mu = _rolling_mean(dsh, _TD_QTR)
    sigma = _rolling_std(dsh, _TD_QTR)
    return _safe_div(dsh - mu, sigma)


def ddur_ext_056_dsh_ath_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of days-since-ATH in trailing 252-bar window."""
    dsh = _days_since_expanding_high(close)
    return dsh.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).rank(pct=True)


def ddur_ext_057_dsh_ath_pctrank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of days-since-ATH in trailing 126-bar window."""
    dsh = _days_since_expanding_high(close)
    return dsh.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 4)).rank(pct=True)


def ddur_ext_058_dsh_ath_pctrank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of days-since-ATH in trailing 63-bar window."""
    dsh = _days_since_expanding_high(close)
    return dsh.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 4)).rank(pct=True)


def ddur_ext_059_mean_spell_len_zscore_expanding(close: pd.Series) -> pd.Series:
    """
    Z-score of the 252d mean spell length (below ATH) relative to its expanding history.
    """
    uw = _underwater_expanding_flag(close)
    mean_spell = _spell_agg(uw, _TD_YEAR, "mean")
    mu = mean_spell.expanding(min_periods=1).mean()
    sigma = mean_spell.expanding(min_periods=2).std()
    return _safe_div(mean_spell - mu, sigma)


def ddur_ext_060_max_spell_len_pctrank_expanding(close: pd.Series) -> pd.Series:
    """
    Expanding percentile rank of the 252d maximum spell length (below ATH).
    """
    uw = _underwater_expanding_flag(close)
    max_spell = _spell_agg(uw, _TD_YEAR, "max")
    return max_spell.expanding(min_periods=1).rank(pct=True)


# --- Group G: rate-of-change of recovery / spell-distribution features ---

def ddur_ext_061_mean_spell_len_velocity_21d(close: pd.Series) -> pd.Series:
    """21-bar change in mean drawdown spell length (below ATH, 252d window)."""
    uw = _underwater_expanding_flag(close)
    mean_spell = _spell_agg(uw, _TD_YEAR, "mean")
    return mean_spell.diff(_TD_MO)


def ddur_ext_062_mean_spell_len_velocity_63d(close: pd.Series) -> pd.Series:
    """63-bar change in mean drawdown spell length (below ATH, 252d window)."""
    uw = _underwater_expanding_flag(close)
    mean_spell = _spell_agg(uw, _TD_YEAR, "mean")
    return mean_spell.diff(_TD_QTR)


def ddur_ext_063_spell_count_velocity_21d(close: pd.Series) -> pd.Series:
    """21-bar change in count of distinct drawdown spells (below ATH, 252d window)."""
    uw = _underwater_expanding_flag(close)
    cnt = _spell_agg(uw, _TD_YEAR, "count")
    return cnt.diff(_TD_MO)


def ddur_ext_064_uw_to_at_high_ratio_velocity_21d(close: pd.Series) -> pd.Series:
    """21-bar change in 252d underwater-to-at-high ratio."""
    ratio = ddur_ext_033_underwater_to_at_high_ratio_252d(close)
    return ratio.diff(_TD_MO)


def ddur_ext_065_age_depth_product_velocity_21d(close: pd.Series) -> pd.Series:
    """21-bar change in age * trough_depth product (severity score velocity)."""
    prod = ddur_ext_044_trough_age_product(close)
    return prod.diff(_TD_MO)


def ddur_ext_066_age_to_depth_ratio_velocity_21d(close: pd.Series) -> pd.Series:
    """21-bar change in age-to-depth ratio (ATH basis)."""
    ratio = ddur_ext_041_age_to_depth_ratio_ath(close)
    return ratio.diff(_TD_MO)


def ddur_ext_067_recovery_fraction_velocity_5d(close: pd.Series) -> pd.Series:
    """5-bar change in recovery fraction (within current ATH drawdown spell)."""
    rec = ddur_ext_003_recovery_fraction_of_drawdown_spell(close)
    return rec.diff(5)


def ddur_ext_068_recovery_fraction_velocity_21d(close: pd.Series) -> pd.Series:
    """21-bar change in recovery fraction (within current ATH drawdown spell)."""
    rec = ddur_ext_003_recovery_fraction_of_drawdown_spell(close)
    return rec.diff(_TD_MO)


# --- Group H: volume-conditioned recovery / spell features ---

def ddur_ext_069_vol_during_recovery_vs_vol_during_decline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Ratio of average volume during recovery phase (after trough, within current spell)
    to average volume during decline phase (from ATH to trough).
    >1 = recovery accompanied by more volume than decline (bullish divergence).
    """
    last_ath_pos = _last_high_pos_series(close).astype(int)
    n = len(close)
    arr_c = close.values
    arr_v = volume.values
    result = np.full(n, np.nan)
    for i in range(n):
        ath_p = int(last_ath_pos.iloc[i])
        if ath_p == i:
            result[i] = np.nan
            continue
        segment_c = arr_c[ath_p: i + 1]
        segment_v = arr_v[ath_p: i + 1]
        trough_idx = int(np.argmin(segment_c))
        if trough_idx == 0:
            result[i] = np.nan
            continue
        vol_decline = segment_v[:trough_idx + 1]
        vol_recovery = segment_v[trough_idx:]
        if len(vol_decline) > 0 and len(vol_recovery) > 0 and vol_decline.mean() > _EPS:
            result[i] = vol_recovery.mean() / vol_decline.mean()
        else:
            result[i] = np.nan
    return pd.Series(result, index=close.index)


def ddur_ext_070_avg_vol_on_recovery_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Average volume on days where close > close[t-1] AND price is below ATH
    (i.e., recovery attempts while still underwater), over trailing 252d.
    """
    uw = _underwater_expanding_flag(close)
    ret = close.diff(1)
    recovery_day = ((ret > 0) & (uw > 0)).astype(float)
    num = _rolling_sum(volume * recovery_day, _TD_YEAR)
    den = _rolling_sum(recovery_day, _TD_YEAR)
    return _safe_div(num, den)


def ddur_ext_071_pct_recovery_days_with_high_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Fraction of recovery-attempt days (up close, below ATH) that have above-average volume,
    over trailing 252d.  High = volume-backed recoveries; low = weak, low-vol bounces.
    """
    uw = _underwater_expanding_flag(close)
    ret = close.diff(1)
    recovery_day = ((ret > 0) & (uw > 0)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    hi_vol_on_rec = ((volume > avg_vol) & (recovery_day > 0)).astype(float)
    num = _rolling_sum(hi_vol_on_rec, _TD_YEAR)
    den = _rolling_sum(recovery_day, _TD_YEAR)
    return _safe_div(num, den)


def ddur_ext_072_spell_count_vs_high_touch_count_ratio_252d(close: pd.Series) -> pd.Series:
    """
    Ratio of drawdown spell count to ATH-touch count in trailing 252d.
    High = many drawdowns, few new highs (choppy but bearish); low = few drawdowns, many highs.
    """
    uw = _underwater_expanding_flag(close)
    spell_cnt = _spell_agg(uw, _TD_YEAR, "count")
    at_high = (1.0 - uw)
    high_touch_cnt = _rolling_sum(at_high, _TD_YEAR)
    return _safe_div(spell_cnt, high_touch_cnt.replace(0, np.nan))


def ddur_ext_073_recovery_time_exceeds_spell_mean_flag(close: pd.Series) -> pd.Series:
    """
    Flag: 1 if elapsed recovery time (bars since trough) exceeds the mean completed
    spell length in the trailing 252-bar window.  Signals unusually prolonged recovery.
    """
    elapsed = ddur_ext_002_recovery_elapsed_since_trough_ath(close)
    uw = _underwater_expanding_flag(close)
    mean_spell = _spell_agg(uw, _TD_YEAR, "mean")
    return (elapsed > mean_spell).astype(float)


def ddur_ext_074_vol_weighted_recovery_fraction(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Volume-weighted price recovery fraction from trough of current ATH drawdown spell.
    Each bar's distance from trough relative to full depth is weighted by its volume.
    Backward-looking within current spell.
    """
    last_ath_pos = _last_high_pos_series(close).astype(int)
    n = len(close)
    arr_c = close.values
    arr_v = volume.values
    result = np.full(n, np.nan)
    for i in range(n):
        ath_p = int(last_ath_pos.iloc[i])
        if ath_p == i:
            result[i] = 1.0
            continue
        segment_c = arr_c[ath_p: i + 1]
        segment_v = arr_v[ath_p: i + 1]
        ath_price = arr_c[ath_p]
        trough_price = float(np.min(segment_c))
        depth = ath_price - trough_price
        if depth < _EPS:
            result[i] = np.nan
            continue
        rec_fracs = (segment_c - trough_price) / depth
        total_vol = segment_v.sum()
        if total_vol > _EPS:
            result[i] = float(np.dot(rec_fracs, segment_v) / total_vol)
        else:
            result[i] = np.nan
    return pd.Series(result, index=close.index)


def ddur_ext_075_drawdown_age_pctrank_vs_all_historical_spells_expanding(close: pd.Series) -> pd.Series:
    """
    Expanding percentile rank of the current drawdown age (bars since ATH) among
    all completed drawdown spell lengths observed since inception.
    Unlike ddur_ext_010 (504d window) this uses the full expanding history.
    """
    dsh = _days_since_expanding_high(close)
    uw = _underwater_expanding_flag(close)
    # collect all completed spells up to each point using expanding window
    arr_uw = uw.values
    arr_dsh = dsh.values
    n = len(close)
    all_spells = []
    cur = 0
    result = np.full(n, np.nan)
    for i in range(n):
        v = arr_uw[i]
        if v == 1.0:
            cur += 1
        else:
            if cur > 0:
                all_spells.append(cur)
                cur = 0
        age = arr_dsh[i]
        if all_spells:
            a = np.array(all_spells, dtype=float)
            result[i] = float(np.mean(a <= age))
        else:
            result[i] = np.nan
    return pd.Series(result, index=close.index)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DURATION_EXTENDED_REGISTRY_001_075 = {
    "ddur_ext_001_bars_elapsed_since_level_crossed_up": {"inputs": ["close"], "func": ddur_ext_001_bars_elapsed_since_level_crossed_up},
    "ddur_ext_002_recovery_elapsed_since_trough_ath": {"inputs": ["close"], "func": ddur_ext_002_recovery_elapsed_since_trough_ath},
    "ddur_ext_003_recovery_fraction_of_drawdown_spell": {"inputs": ["close"], "func": ddur_ext_003_recovery_fraction_of_drawdown_spell},
    "ddur_ext_004_price_recovery_pct_from_trough": {"inputs": ["close"], "func": ddur_ext_004_price_recovery_pct_from_trough},
    "ddur_ext_005_price_vs_midpoint_ath_trough": {"inputs": ["close"], "func": ddur_ext_005_price_vs_midpoint_ath_trough},
    "ddur_ext_006_trough_depth_pct_in_current_spell": {"inputs": ["close"], "func": ddur_ext_006_trough_depth_pct_in_current_spell},
    "ddur_ext_007_recovery_time_per_unit_depth": {"inputs": ["close"], "func": ddur_ext_007_recovery_time_per_unit_depth},
    "ddur_ext_008_expected_recovery_proxy_vol_scaled": {"inputs": ["close"], "func": ddur_ext_008_expected_recovery_proxy_vol_scaled},
    "ddur_ext_009_drawdown_duration_exceeds_historical_median_recovery": {"inputs": ["close"], "func": ddur_ext_009_drawdown_duration_exceeds_historical_median_recovery},
    "ddur_ext_010_drawdown_duration_pctrank_vs_historical_spells": {"inputs": ["close"], "func": ddur_ext_010_drawdown_duration_pctrank_vs_historical_spells},
    "ddur_ext_011_mean_spell_len_under_ath_252d": {"inputs": ["close"], "func": ddur_ext_011_mean_spell_len_under_ath_252d},
    "ddur_ext_012_median_spell_len_under_ath_252d": {"inputs": ["close"], "func": ddur_ext_012_median_spell_len_under_ath_252d},
    "ddur_ext_013_max_spell_len_under_ath_252d": {"inputs": ["close"], "func": ddur_ext_013_max_spell_len_under_ath_252d},
    "ddur_ext_014_mean_spell_len_under_ath_504d": {"inputs": ["close"], "func": ddur_ext_014_mean_spell_len_under_ath_504d},
    "ddur_ext_015_max_spell_len_under_ath_504d": {"inputs": ["close"], "func": ddur_ext_015_max_spell_len_under_ath_504d},
    "ddur_ext_016_std_spell_len_under_ath_252d": {"inputs": ["close"], "func": ddur_ext_016_std_spell_len_under_ath_252d},
    "ddur_ext_017_mean_spell_len_under_252d_high_252d": {"inputs": ["close"], "func": ddur_ext_017_mean_spell_len_under_252d_high_252d},
    "ddur_ext_018_max_spell_len_under_252d_high_252d": {"inputs": ["close"], "func": ddur_ext_018_max_spell_len_under_252d_high_252d},
    "ddur_ext_019_count_distinct_spells_under_ath_252d": {"inputs": ["close"], "func": ddur_ext_019_count_distinct_spells_under_ath_252d},
    "ddur_ext_020_count_distinct_spells_under_ath_504d": {"inputs": ["close"], "func": ddur_ext_020_count_distinct_spells_under_ath_504d},
    "ddur_ext_021_count_distinct_spells_under_252d_high_252d": {"inputs": ["close"], "func": ddur_ext_021_count_distinct_spells_under_252d_high_252d},
    "ddur_ext_022_current_spell_pctrank_under_ath_252d": {"inputs": ["close"], "func": ddur_ext_022_current_spell_pctrank_under_ath_252d},
    "ddur_ext_023_current_spell_pctrank_under_ath_504d": {"inputs": ["close"], "func": ddur_ext_023_current_spell_pctrank_under_ath_504d},
    "ddur_ext_024_current_spell_pctrank_under_252d_high_252d": {"inputs": ["close"], "func": ddur_ext_024_current_spell_pctrank_under_252d_high_252d},
    "ddur_ext_025_total_bars_in_spells_under_ath_252d": {"inputs": ["close"], "func": ddur_ext_025_total_bars_in_spells_under_ath_252d},
    "ddur_ext_026_time_decay_since_252d_high_halflife_21d": {"inputs": ["close"], "func": ddur_ext_026_time_decay_since_252d_high_halflife_21d},
    "ddur_ext_027_time_decay_since_ath_halflife_126d": {"inputs": ["close"], "func": ddur_ext_027_time_decay_since_ath_halflife_126d},
    "ddur_ext_028_time_decay_since_ath_halflife_504d": {"inputs": ["close"], "func": ddur_ext_028_time_decay_since_ath_halflife_504d},
    "ddur_ext_029_time_decay_since_new_252d_high_halflife_63d": {"inputs": ["close"], "func": ddur_ext_029_time_decay_since_new_252d_high_halflife_63d},
    "ddur_ext_030_log_time_since_ath": {"inputs": ["close"], "func": ddur_ext_030_log_time_since_ath},
    "ddur_ext_031_log_time_since_252d_high": {"inputs": ["close"], "func": ddur_ext_031_log_time_since_252d_high},
    "ddur_ext_032_sqrt_time_since_ath": {"inputs": ["close"], "func": ddur_ext_032_sqrt_time_since_ath},
    "ddur_ext_033_underwater_to_at_high_ratio_252d": {"inputs": ["close"], "func": ddur_ext_033_underwater_to_at_high_ratio_252d},
    "ddur_ext_034_underwater_to_at_high_ratio_504d": {"inputs": ["close"], "func": ddur_ext_034_underwater_to_at_high_ratio_504d},
    "ddur_ext_035_underwater_to_at_high_ratio_expanding": {"inputs": ["close"], "func": ddur_ext_035_underwater_to_at_high_ratio_expanding},
    "ddur_ext_036_at_high_fraction_expanding": {"inputs": ["close"], "func": ddur_ext_036_at_high_fraction_expanding},
    "ddur_ext_037_at_high_fraction_252d": {"inputs": ["close"], "func": ddur_ext_037_at_high_fraction_252d},
    "ddur_ext_038_high_touch_interval_mean_252d": {"inputs": ["close"], "func": ddur_ext_038_high_touch_interval_mean_252d},
    "ddur_ext_039_high_touch_interval_mean_504d": {"inputs": ["close"], "func": ddur_ext_039_high_touch_interval_mean_504d},
    "ddur_ext_040_uw_to_at_high_ratio_zscore_252d": {"inputs": ["close"], "func": ddur_ext_040_uw_to_at_high_ratio_zscore_252d},
    "ddur_ext_041_age_to_depth_ratio_ath": {"inputs": ["close"], "func": ddur_ext_041_age_to_depth_ratio_ath},
    "ddur_ext_042_age_to_depth_ratio_252d_high": {"inputs": ["close"], "func": ddur_ext_042_age_to_depth_ratio_252d_high},
    "ddur_ext_043_depth_per_unit_age_ath": {"inputs": ["close"], "func": ddur_ext_043_depth_per_unit_age_ath},
    "ddur_ext_044_trough_age_product": {"inputs": ["close"], "func": ddur_ext_044_trough_age_product},
    "ddur_ext_045_age_above_expected_for_depth_flag": {"inputs": ["close"], "func": ddur_ext_045_age_above_expected_for_depth_flag},
    "ddur_ext_046_normalized_age_vs_trough_depth": {"inputs": ["close"], "func": ddur_ext_046_normalized_age_vs_trough_depth},
    "ddur_ext_047_recovery_pct_vs_elapsed_recovery_time": {"inputs": ["close"], "func": ddur_ext_047_recovery_pct_vs_elapsed_recovery_time},
    "ddur_ext_048_recovery_momentum_5d": {"inputs": ["close"], "func": ddur_ext_048_recovery_momentum_5d},
    "ddur_ext_049_recovery_momentum_21d": {"inputs": ["close"], "func": ddur_ext_049_recovery_momentum_21d},
    "ddur_ext_050_recovery_stall_flag_5d": {"inputs": ["close"], "func": ddur_ext_050_recovery_stall_flag_5d},
    "ddur_ext_051_dsh_ath_zscore_252d": {"inputs": ["close"], "func": ddur_ext_051_dsh_ath_zscore_252d},
    "ddur_ext_052_dsh_ath_zscore_126d": {"inputs": ["close"], "func": ddur_ext_052_dsh_ath_zscore_126d},
    "ddur_ext_053_dsh_ath_zscore_63d": {"inputs": ["close"], "func": ddur_ext_053_dsh_ath_zscore_63d},
    "ddur_ext_054_dsh_252d_high_zscore_126d": {"inputs": ["close"], "func": ddur_ext_054_dsh_252d_high_zscore_126d},
    "ddur_ext_055_dsh_252d_high_zscore_63d": {"inputs": ["close"], "func": ddur_ext_055_dsh_252d_high_zscore_63d},
    "ddur_ext_056_dsh_ath_pctrank_252d": {"inputs": ["close"], "func": ddur_ext_056_dsh_ath_pctrank_252d},
    "ddur_ext_057_dsh_ath_pctrank_126d": {"inputs": ["close"], "func": ddur_ext_057_dsh_ath_pctrank_126d},
    "ddur_ext_058_dsh_ath_pctrank_63d": {"inputs": ["close"], "func": ddur_ext_058_dsh_ath_pctrank_63d},
    "ddur_ext_059_mean_spell_len_zscore_expanding": {"inputs": ["close"], "func": ddur_ext_059_mean_spell_len_zscore_expanding},
    "ddur_ext_060_max_spell_len_pctrank_expanding": {"inputs": ["close"], "func": ddur_ext_060_max_spell_len_pctrank_expanding},
    "ddur_ext_061_mean_spell_len_velocity_21d": {"inputs": ["close"], "func": ddur_ext_061_mean_spell_len_velocity_21d},
    "ddur_ext_062_mean_spell_len_velocity_63d": {"inputs": ["close"], "func": ddur_ext_062_mean_spell_len_velocity_63d},
    "ddur_ext_063_spell_count_velocity_21d": {"inputs": ["close"], "func": ddur_ext_063_spell_count_velocity_21d},
    "ddur_ext_064_uw_to_at_high_ratio_velocity_21d": {"inputs": ["close"], "func": ddur_ext_064_uw_to_at_high_ratio_velocity_21d},
    "ddur_ext_065_age_depth_product_velocity_21d": {"inputs": ["close"], "func": ddur_ext_065_age_depth_product_velocity_21d},
    "ddur_ext_066_age_to_depth_ratio_velocity_21d": {"inputs": ["close"], "func": ddur_ext_066_age_to_depth_ratio_velocity_21d},
    "ddur_ext_067_recovery_fraction_velocity_5d": {"inputs": ["close"], "func": ddur_ext_067_recovery_fraction_velocity_5d},
    "ddur_ext_068_recovery_fraction_velocity_21d": {"inputs": ["close"], "func": ddur_ext_068_recovery_fraction_velocity_21d},
    "ddur_ext_069_vol_during_recovery_vs_vol_during_decline": {"inputs": ["close", "volume"], "func": ddur_ext_069_vol_during_recovery_vs_vol_during_decline},
    "ddur_ext_070_avg_vol_on_recovery_days_252d": {"inputs": ["close", "volume"], "func": ddur_ext_070_avg_vol_on_recovery_days_252d},
    "ddur_ext_071_pct_recovery_days_with_high_vol_252d": {"inputs": ["close", "volume"], "func": ddur_ext_071_pct_recovery_days_with_high_vol_252d},
    "ddur_ext_072_spell_count_vs_high_touch_count_ratio_252d": {"inputs": ["close"], "func": ddur_ext_072_spell_count_vs_high_touch_count_ratio_252d},
    "ddur_ext_073_recovery_time_exceeds_spell_mean_flag": {"inputs": ["close"], "func": ddur_ext_073_recovery_time_exceeds_spell_mean_flag},
    "ddur_ext_074_vol_weighted_recovery_fraction": {"inputs": ["close", "volume"], "func": ddur_ext_074_vol_weighted_recovery_fraction},
    "ddur_ext_075_drawdown_age_pctrank_vs_all_historical_spells_expanding": {"inputs": ["close"], "func": ddur_ext_075_drawdown_age_pctrank_vs_all_historical_spells_expanding},
}
