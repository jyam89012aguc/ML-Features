"""
10_trough_clustering — Base Features 076-150
Domain: density of local minima, repeated bottoms, double/triple-bottom signatures,
        trough spacing and clustering in price and time — continued.
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


def _local_min_flag(low: pd.Series, w: int) -> pd.Series:
    """Backward-only local-minimum flag: low[t] equals rolling_min(low, w)[t]."""
    rmin = low.rolling(w, min_periods=max(1, w // 2)).min()
    return (low <= rmin + _EPS).astype(float)


def _trough_count_raw(x, threshold_pct):
    if len(x) == 0:
        return np.nan
    mn = np.min(x)
    return float(np.sum(x <= mn * (1.0 + threshold_pct) + _EPS))


def _trough_std_raw(x):
    if len(x) < 2:
        return np.nan
    mn = np.min(x)
    near = x[x <= mn * 1.03 + _EPS]
    if len(near) < 2:
        return np.nan
    return float(np.std(near))


def _trough_spacing_raw(x):
    idxs = np.where(x > 0.5)[0]
    if len(idxs) < 2:
        return np.nan
    return float(np.mean(np.diff(idxs.astype(float))))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        num = ((xi - xi_m) * (x - x.mean())).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-088): Volume-weighted trough metrics ---

def tcl_076_volume_at_troughs_fraction_126d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 126-day volume occurring on local-min days (5-bar definition)."""
    flag = _local_min_flag(low, 5)
    vol_trough = flag * volume
    return _safe_div(_rolling_sum(vol_trough, _TD_HALF), _rolling_sum(volume, _TD_HALF))


def tcl_077_volume_at_troughs_fraction_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day volume occurring on local-min days."""
    flag = _local_min_flag(low, 5)
    vol_trough = flag * volume
    return _safe_div(_rolling_sum(vol_trough, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))


def tcl_078_avg_volume_on_trough_days_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on local-min days within trailing 63 days."""
    flag = _local_min_flag(low, 5)
    flag_vol = flag * volume
    cnt = _rolling_sum(flag, _TD_QTR).replace(0, np.nan)
    return _rolling_sum(flag_vol, _TD_QTR) / cnt


def tcl_079_avg_volume_on_trough_days_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on local-min days within trailing 252 days."""
    flag = _local_min_flag(low, 5)
    flag_vol = flag * volume
    cnt = _rolling_sum(flag, _TD_YEAR).replace(0, np.nan)
    return _rolling_sum(flag_vol, _TD_YEAR) / cnt


def tcl_080_volume_ratio_trough_vs_nontrough_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean volume on trough days vs non-trough days (63d window)."""
    flag = _local_min_flag(low, 5)
    non_flag = 1.0 - flag
    vol_t = flag * volume
    vol_n = non_flag * volume
    cnt_t = _rolling_sum(flag, _TD_QTR).replace(0, np.nan)
    cnt_n = _rolling_sum(non_flag, _TD_QTR).replace(0, np.nan)
    mean_t = _rolling_sum(vol_t, _TD_QTR) / cnt_t
    mean_n = _rolling_sum(vol_n, _TD_QTR) / cnt_n
    return _safe_div(mean_t, mean_n)


def tcl_081_volume_ratio_trough_vs_nontrough_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean volume on trough days vs non-trough days (252d window)."""
    flag = _local_min_flag(low, 5)
    non_flag = 1.0 - flag
    vol_t = flag * volume
    vol_n = non_flag * volume
    cnt_t = _rolling_sum(flag, _TD_YEAR).replace(0, np.nan)
    cnt_n = _rolling_sum(non_flag, _TD_YEAR).replace(0, np.nan)
    mean_t = _rolling_sum(vol_t, _TD_YEAR) / cnt_t
    mean_n = _rolling_sum(vol_n, _TD_YEAR) / cnt_n
    return _safe_div(mean_t, mean_n)


def tcl_082_volume_zscore_on_trough_days_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume when at local min, computed vs 63-day volume distribution."""
    flag = _local_min_flag(low, 5)
    vol_mean = _rolling_mean(volume, _TD_QTR)
    vol_std = _rolling_std(volume, _TD_QTR)
    vol_z = _safe_div(volume - vol_mean, vol_std)
    return vol_z * flag


def tcl_083_high_volume_trough_count_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 63-day days that are both a local min AND have above-median volume."""
    flag = _local_min_flag(low, 5)
    med_vol = _rolling_median(volume, _TD_QTR)
    high_vol = (volume >= med_vol).astype(float)
    return _rolling_sum(flag * high_vol, _TD_QTR)


def tcl_084_high_volume_trough_count_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 252-day days that are local min AND have above-median volume."""
    flag = _local_min_flag(low, 5)
    med_vol = _rolling_median(volume, _TD_YEAR)
    high_vol = (volume >= med_vol).astype(float)
    return _rolling_sum(flag * high_vol, _TD_YEAR)


def tcl_085_trough_volume_trend_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of volume on trough days over 63 days (are retests getting louder?)."""
    flag = _local_min_flag(low, 5)
    trough_vol = flag * volume
    return _linslope(trough_vol, _TD_QTR)


def tcl_086_volume_concentration_near_low_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Fraction of 63-day volume in bars within 2% of 63-day low.
    Measures whether volume concentrates at the support level.
    """
    rmin = _rolling_min(low, _TD_QTR)
    near = (low <= rmin * 1.02 + _EPS).astype(float)
    return _safe_div(_rolling_sum(near * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def tcl_087_volume_concentration_near_low_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day volume in bars within 3% of 252-day low."""
    rmin = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin * 1.03 + _EPS).astype(float)
    return _safe_div(_rolling_sum(near * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))


def tcl_088_volume_weighted_trough_price_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of low prices within 3% of 63-day min."""
    rmin = _rolling_min(low, _TD_QTR)
    near = (low <= rmin * 1.03 + _EPS).astype(float)
    wt = near * volume
    return _safe_div(_rolling_sum(wt * low, _TD_QTR), _rolling_sum(wt, _TD_QTR))


# --- Group H (089-100): Trough level relative measures ---

def tcl_089_rolling_min_slope_21d(low: pd.Series) -> pd.Series:
    """OLS slope of the 21-day rolling minimum (trend of the support floor)."""
    rmin = _rolling_min(low, _TD_MON)
    return _linslope(rmin, _TD_MON)


def tcl_090_rolling_min_slope_63d(low: pd.Series) -> pd.Series:
    """OLS slope of the 63-day rolling minimum."""
    rmin = _rolling_min(low, _TD_QTR)
    return _linslope(rmin, _TD_QTR)


def tcl_091_rolling_min_slope_126d(low: pd.Series) -> pd.Series:
    """OLS slope of the 126-day rolling minimum."""
    rmin = _rolling_min(low, _TD_HALF)
    return _linslope(rmin, _TD_HALF)


def tcl_092_rolling_min_slope_252d(low: pd.Series) -> pd.Series:
    """OLS slope of the 252-day rolling minimum."""
    rmin = _rolling_min(low, _TD_YEAR)
    return _linslope(rmin, _TD_YEAR)


def tcl_093_rolling_min_acceleration_63d(low: pd.Series) -> pd.Series:
    """Change in 63-day rolling-min slope over 21 days (acceleration of floor movement)."""
    rmin = _rolling_min(low, _TD_QTR)
    slope = _linslope(rmin, _TD_QTR)
    return slope.diff(_TD_MON)


def tcl_094_double_bottom_flag_63d(low: pd.Series) -> pd.Series:
    """
    Simple double-bottom score: count of bars within 1% of the 63-day min
    that are at least 5 bars apart (two distinct low touches).
    Uses rolling apply with a scalar helper.
    """
    def _db_score(x):
        if len(x) < 10:
            return np.nan
        mn = np.min(x)
        trough_idxs = np.where(x <= mn * 1.01 + _EPS)[0]
        if len(trough_idxs) < 2:
            return 0.0
        gaps = np.diff(trough_idxs)
        return float(np.sum(gaps >= 5))
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_db_score, raw=True)


def tcl_095_double_bottom_flag_126d(low: pd.Series) -> pd.Series:
    """Double-bottom score over 126-day window (2% band, 5-bar min separation)."""
    def _db_score(x):
        if len(x) < 10:
            return np.nan
        mn = np.min(x)
        trough_idxs = np.where(x <= mn * 1.02 + _EPS)[0]
        if len(trough_idxs) < 2:
            return 0.0
        gaps = np.diff(trough_idxs)
        return float(np.sum(gaps >= 5))
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_db_score, raw=True)


def tcl_096_triple_bottom_flag_252d(low: pd.Series) -> pd.Series:
    """Triple-bottom score: pairs of near-lows with >= 5-bar separation, 252d window."""
    def _tb_score(x):
        if len(x) < 15:
            return np.nan
        mn = np.min(x)
        trough_idxs = np.where(x <= mn * 1.02 + _EPS)[0]
        if len(trough_idxs) < 3:
            return 0.0
        gaps = np.diff(trough_idxs)
        separated = trough_idxs[np.concatenate([[True], gaps >= 5])]
        return float(max(0, len(separated) - 2))
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_tb_score, raw=True)


def tcl_097_trough_low_vs_prior_trough_63d(low: pd.Series) -> pd.Series:
    """
    Ratio of current 63-day min to the prior 63-day min (21 bars ago).
    < 1 = lower low (still declining); > 1 = higher low (possible base).
    """
    rmin_now = _rolling_min(low, _TD_QTR)
    rmin_prior = rmin_now.shift(_TD_MON)
    return _safe_div(rmin_now, rmin_prior)


def tcl_098_trough_low_vs_prior_trough_126d(low: pd.Series) -> pd.Series:
    """Ratio of 126-day min to the 63-bars-ago 126-day min."""
    rmin_now = _rolling_min(low, _TD_HALF)
    rmin_prior = rmin_now.shift(_TD_QTR)
    return _safe_div(rmin_now, rmin_prior)


def tcl_099_trough_low_vs_prior_trough_252d(low: pd.Series) -> pd.Series:
    """Ratio of 252-day min to the 126-bars-ago 252-day min."""
    rmin_now = _rolling_min(low, _TD_YEAR)
    rmin_prior = rmin_now.shift(_TD_HALF)
    return _safe_div(rmin_now, rmin_prior)


def tcl_100_higher_low_flag_63d(low: pd.Series) -> pd.Series:
    """Binary: 1 if 63-day min > prior (21-bar shifted) 63-day min (higher low)."""
    rmin_now = _rolling_min(low, _TD_QTR)
    rmin_prior = rmin_now.shift(_TD_MON)
    return (rmin_now > rmin_prior).astype(float)


# --- Group I (101-112): Trough clustering with open/high ---

def tcl_101_open_at_trough_fraction_63d(low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 63-day bars where open is within 2% of 63-day low."""
    rmin = _rolling_min(low, _TD_QTR)
    near = (open <= rmin * 1.02 + _EPS).astype(float)
    return _rolling_mean(near, _TD_QTR)


def tcl_102_open_at_trough_fraction_252d(low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 252-day bars where open is within 3% of 252-day low."""
    rmin = _rolling_min(low, _TD_YEAR)
    near = (open <= rmin * 1.03 + _EPS).astype(float)
    return _rolling_mean(near, _TD_YEAR)


def tcl_103_intraday_low_touch_fraction_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 63d bars where intraday low is within 1% of 63-day close low."""
    rmin_c = _rolling_min(close, _TD_QTR)
    near = (low <= rmin_c * 1.01 + _EPS).astype(float)
    return _rolling_mean(near, _TD_QTR)


def tcl_104_high_low_range_at_trough_63d(low: pd.Series, high: pd.Series) -> pd.Series:
    """Mean (high - low) / low on local-min days (trough bar range)."""
    flag = _local_min_flag(low, 5)
    bar_range = _safe_div(high - low, low)
    return _rolling_mean(bar_range * flag, _TD_QTR)


def tcl_105_high_low_range_at_trough_252d(low: pd.Series, high: pd.Series) -> pd.Series:
    """Mean (high - low) / low on local-min days (252d)."""
    flag = _local_min_flag(low, 5)
    bar_range = _safe_div(high - low, low)
    return _rolling_mean(bar_range * flag, _TD_YEAR)


def tcl_106_close_above_low_at_trough_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (close - low) / low on local-min days in 63d (trough recovery within bar)."""
    flag = _local_min_flag(low, 5)
    recovery = _safe_div(close - low, low)
    return _rolling_mean(recovery * flag, _TD_QTR)


def tcl_107_close_above_low_at_trough_252d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (close - low) / low on local-min days in 252d."""
    flag = _local_min_flag(low, 5)
    recovery = _safe_div(close - low, low)
    return _rolling_mean(recovery * flag, _TD_YEAR)


def tcl_108_trough_candle_body_frac_63d(low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |close-open|/(high implied range) on trough days in 63d."""
    flag = _local_min_flag(low, 5)
    body = (close - open).abs()
    body_norm = _safe_div(body, low.replace(0, np.nan))
    return _rolling_mean(body_norm * flag, _TD_QTR)


def tcl_109_local_min_count_5bar_21d_close(close: pd.Series) -> pd.Series:
    """Count of close-based 5-bar local mins in trailing 21d (short-term trough density)."""
    flag = _local_min_flag(close, 5)
    return _rolling_sum(flag, _TD_MON)


def tcl_110_local_min_count_10bar_252d(low: pd.Series) -> pd.Series:
    """Count of 10-bar local-min flags in trailing 252d."""
    flag = _local_min_flag(low, 10)
    return _rolling_sum(flag, _TD_YEAR)


def tcl_111_trough_bar_close_vs_open_ratio_252d(low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean close/open on local-min days in 252d (>1 = bullish close on trough bar)."""
    flag = _local_min_flag(low, 5)
    ratio = _safe_div(close, open.replace(0, np.nan))
    return _rolling_mean(ratio * flag, _TD_YEAR)


def tcl_112_trough_bar_close_vs_high_ratio_252d(low: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean close/high on local-min days in 252d (measures recovery from trough bar high)."""
    flag = _local_min_flag(low, 5)
    ratio = _safe_div(close, high.replace(0, np.nan))
    return _rolling_mean(ratio * flag, _TD_YEAR)


# --- Group J (113-125): Basing period duration and consistency ---

def tcl_113_bars_since_last_local_min(low: pd.Series) -> pd.Series:
    """Bars since the most recent local-min flag (5-bar definition)."""
    flag = _local_min_flag(low, 5)
    def _bars_since(x):
        idxs = np.where(x > 0.5)[0]
        if len(idxs) == 0:
            return np.nan
        return float(len(x) - 1 - idxs[-1])
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_bars_since, raw=True)


def tcl_114_bars_since_last_local_min_10bar(low: pd.Series) -> pd.Series:
    """Bars since last 10-bar local-min flag."""
    flag = _local_min_flag(low, 10)
    def _bars_since(x):
        idxs = np.where(x > 0.5)[0]
        if len(idxs) == 0:
            return np.nan
        return float(len(x) - 1 - idxs[-1])
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_bars_since, raw=True)


def tcl_115_trough_recency_score_252d(low: pd.Series) -> pd.Series:
    """
    Recency-weighted trough count: sum of flag * (position/window) over 252d.
    More recent troughs get higher weight.
    """
    flag = _local_min_flag(low, 5)
    def _recency(x):
        w = len(x)
        weights = np.arange(1, w + 1, dtype=float) / w
        return float(np.sum(x * weights))
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_recency, raw=True)


def tcl_116_trough_recency_score_126d(low: pd.Series) -> pd.Series:
    """Recency-weighted trough count over 126d."""
    flag = _local_min_flag(low, 5)
    def _recency(x):
        w = len(x)
        weights = np.arange(1, w + 1, dtype=float) / w
        return float(np.sum(x * weights))
    return flag.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_recency, raw=True)


def tcl_117_trough_count_ratio_recent_vs_old_252d(low: pd.Series) -> pd.Series:
    """
    Ratio of trough count in last 63d vs prior 189d within a 252d window.
    > 0.5 means troughs are clustering in the recent period.
    """
    cnt_63 = tcl_002_local_min_count_63d(low)
    cnt_252 = tcl_004_local_min_count_252d(low)
    cnt_old = (cnt_252 - cnt_63).clip(lower=0)
    return _safe_div(cnt_63, cnt_old.replace(0, np.nan))


def tcl_118_consecutive_trough_days_63d(low: pd.Series) -> pd.Series:
    """Max run of consecutive local-min flags within 63d window."""
    flag = _local_min_flag(low, 5)
    def _max_run(x):
        if len(x) == 0:
            return np.nan
        best, cur = 0, 0
        for v in x:
            if v > 0.5:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def tcl_119_consecutive_trough_days_252d(low: pd.Series) -> pd.Series:
    """Max run of consecutive local-min flags within 252d window."""
    flag = _local_min_flag(low, 5)
    def _max_run(x):
        if len(x) == 0:
            return np.nan
        best, cur = 0, 0
        for v in x:
            if v > 0.5:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return float(best)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def tcl_120_trough_periodicity_score_252d(low: pd.Series) -> pd.Series:
    """
    Regularity of trough spacing: 1 / (1 + std/mean of gaps), 252d.
    Higher = more periodic troughs (regular basing cycle).
    """
    flag = _local_min_flag(low, 5)
    def _periodicity(x):
        idxs = np.where(x > 0.5)[0]
        if len(idxs) < 3:
            return np.nan
        gaps = np.diff(idxs.astype(float))
        m = np.mean(gaps)
        if m < _EPS:
            return np.nan
        return float(1.0 / (1.0 + np.std(gaps) / m))
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_periodicity, raw=True)


def tcl_121_expanding_trough_count(low: pd.Series) -> pd.Series:
    """Expanding (all-history) count of 5-bar local-min flags."""
    flag = _local_min_flag(low, 5)
    return flag.expanding(min_periods=1).sum()


def tcl_122_expanding_trough_fraction(low: pd.Series) -> pd.Series:
    """Expanding fraction of bars that are 5-bar local minima."""
    flag = _local_min_flag(low, 5)
    return flag.expanding(min_periods=1).mean()


def tcl_123_trough_count_low_21bar_63d(low: pd.Series) -> pd.Series:
    """Count of 21-bar local-min flags in 63d (broader definition of troughs)."""
    flag = _local_min_flag(low, 21)
    return _rolling_sum(flag, _TD_QTR)


def tcl_124_trough_count_low_21bar_252d(low: pd.Series) -> pd.Series:
    """Count of 21-bar local-min flags in 252d."""
    flag = _local_min_flag(low, 21)
    return _rolling_sum(flag, _TD_YEAR)


def tcl_125_trough_count_change_63d(low: pd.Series) -> pd.Series:
    """Change in 63-day trough count vs 21 bars ago (momentum of basing activity)."""
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    return cnt.diff(_TD_MON)


# --- Group K (126-138): Cross-series trough comparison and ratios ---

def tcl_126_close_low_trough_agreement_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 63d days that are BOTH low-based and close-based local mins."""
    fl = _local_min_flag(low, 5)
    fc = _local_min_flag(close, 5)
    return _rolling_mean(fl * fc, _TD_QTR)


def tcl_127_close_low_trough_agreement_252d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 252d days that are BOTH low-based and close-based local mins."""
    fl = _local_min_flag(low, 5)
    fc = _local_min_flag(close, 5)
    return _rolling_mean(fl * fc, _TD_YEAR)


def tcl_128_low_trough_but_not_close_trough_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 63d days with low-min flag but close does NOT confirm (shadow only)."""
    fl = _local_min_flag(low, 5)
    fc = _local_min_flag(close, 5)
    shadow_only = fl * (1.0 - fc)
    return _rolling_mean(shadow_only, _TD_QTR)


def tcl_129_low_min_count_vs_close_min_count_63d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of low-based trough count to close-based trough count (63d)."""
    cnt_l = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    cnt_c = _rolling_sum(_local_min_flag(close, 5), _TD_QTR)
    return _safe_div(cnt_l, cnt_c)


def tcl_130_trough_price_vs_open_at_trough_63d(low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean (open - low) / low on local-min days in 63d (gap down through open?)."""
    flag = _local_min_flag(low, 5)
    ratio = _safe_div(open - low, low.replace(0, np.nan))
    return _rolling_mean(ratio * flag, _TD_QTR)


def tcl_131_trough_intraday_recovery_252d(low: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean (close - low) / (high - low) on local-min days in 252d."""
    flag = _local_min_flag(low, 5)
    rng = (high - low).replace(0, np.nan)
    recovery = (close - low) / rng
    return _rolling_mean(recovery * flag, _TD_YEAR)


def tcl_132_trough_count_10pct_band_close_252d(close: pd.Series) -> pd.Series:
    """Count of 252d bars where close is within 10% of 252d close min."""
    rmin = _rolling_min(close, _TD_YEAR)
    near = (close <= rmin * 1.10 + _EPS).astype(float)
    return _rolling_sum(near, _TD_YEAR)


def tcl_133_trough_count_10pct_band_low_252d(low: pd.Series) -> pd.Series:
    """Count of 252d bars where low is within 10% of 252d low min."""
    rmin = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin * 1.10 + _EPS).astype(float)
    return _rolling_sum(near, _TD_YEAR)


def tcl_134_trough_spread_normalized_126d(low: pd.Series) -> pd.Series:
    """(75th pct of trough prices - min) / min within 126d (spread of support zone)."""
    def _spread(x):
        if len(x) < 2:
            return np.nan
        mn = np.min(x)
        near = x[x <= mn * 1.05 + _EPS]
        if len(near) < 2:
            return np.nan
        q75 = float(np.percentile(near, 75))
        if mn < _EPS:
            return np.nan
        return float((q75 - mn) / mn)
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_spread, raw=True)


def tcl_135_trough_spread_normalized_252d(low: pd.Series) -> pd.Series:
    """(75th pct of trough prices - min) / min within 252d."""
    def _spread(x):
        if len(x) < 2:
            return np.nan
        mn = np.min(x)
        near = x[x <= mn * 1.05 + _EPS]
        if len(near) < 2:
            return np.nan
        q75 = float(np.percentile(near, 75))
        if mn < _EPS:
            return np.nan
        return float((q75 - mn) / mn)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_spread, raw=True)


def tcl_136_trough_price_percentile_rank_252d(low: pd.Series) -> pd.Series:
    """Percentile rank of current low within 252-day distribution (how deep is today?)."""
    return _rolling_rank_pct(low, _TD_YEAR)


def tcl_137_trough_price_percentile_rank_126d(low: pd.Series) -> pd.Series:
    """Percentile rank of current low within 126-day distribution."""
    return _rolling_rank_pct(low, _TD_HALF)


def tcl_138_trough_price_percentile_rank_63d(low: pd.Series) -> pd.Series:
    """Percentile rank of current low within 63-day distribution."""
    return _rolling_rank_pct(low, _TD_QTR)


# --- Group L (139-150): Composite, normalized, and derived trough cluster scores ---

def tcl_139_trough_cluster_intensity_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Composite: trough_count_63d * volume_at_troughs_fraction_63d.
    High = many troughs AND volume concentrated at lows.
    """
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    flag = _local_min_flag(low, 5)
    vol_frac = _safe_div(_rolling_sum(flag * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return cnt * vol_frac.fillna(0.0)


def tcl_140_trough_cluster_intensity_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: trough_count_252d * volume_at_troughs_fraction_252d."""
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_YEAR)
    flag = _local_min_flag(low, 5)
    vol_frac = _safe_div(_rolling_sum(flag * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    return cnt * vol_frac.fillna(0.0)


def tcl_141_trough_zscore_63d_in_252d(low: pd.Series) -> pd.Series:
    """Z-score of 63-day trough count relative to its 252-day history."""
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


def tcl_142_support_retest_zscore_63d(low: pd.Series) -> pd.Series:
    """Z-score of 63-day support retest count (3% of 252d low) vs 252d history."""
    rmin_252 = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    cnt = _rolling_sum(near, _TD_QTR)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


def tcl_143_basing_range_21d_vs_252d(low: pd.Series, high: pd.Series) -> pd.Series:
    """Ratio of 21-day basing range to 252-day basing range (tightening of range)."""
    r21 = _safe_div(_rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON),
                    _rolling_min(low, _TD_MON))
    r252 = _safe_div(_rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR),
                     _rolling_min(low, _TD_YEAR))
    return _safe_div(r21, r252)


def tcl_144_basing_range_63d_vs_252d(low: pd.Series, high: pd.Series) -> pd.Series:
    """Ratio of 63-day basing range to 252-day basing range."""
    r63 = _safe_div(_rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR),
                    _rolling_min(low, _TD_QTR))
    r252 = _safe_div(_rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR),
                     _rolling_min(low, _TD_YEAR))
    return _safe_div(r63, r252)


def tcl_145_trough_count_pct_rank_in_252d_history(low: pd.Series) -> pd.Series:
    """Pct-rank of current 63-day trough count within its 252-day rolling distribution."""
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    return _rolling_rank_pct(cnt, _TD_YEAR)


def tcl_146_retest_fraction_trend_21d(low: pd.Series) -> pd.Series:
    """OLS slope of daily near-low indicator (21-day window): acceleration of retests."""
    rmin = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin * 1.03 + _EPS).astype(float)
    return _linslope(near, _TD_MON)


def tcl_147_retest_fraction_trend_63d(low: pd.Series) -> pd.Series:
    """OLS slope of daily near-low indicator (63-day window)."""
    rmin = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin * 1.03 + _EPS).astype(float)
    return _linslope(near, _TD_QTR)


def tcl_148_trough_min_price_stability_252d(low: pd.Series) -> pd.Series:
    """
    Std of the 21-day rolling minimum series over 252 days / mean of that series.
    Low = stable floor; high = declining/volatile floor.
    """
    rmin_21 = _rolling_min(low, _TD_MON)
    return _safe_div(_rolling_std(rmin_21, _TD_YEAR), _rolling_mean(rmin_21, _TD_YEAR))


def tcl_149_trough_count_low_vs_close_diff_252d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Difference: low-based trough count minus close-based trough count (252d)."""
    cnt_l = _rolling_sum(_local_min_flag(low, 5), _TD_YEAR)
    cnt_c = _rolling_sum(_local_min_flag(close, 5), _TD_YEAR)
    return cnt_l - cnt_c


def tcl_150_trough_composite_basing_score(low: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """
    Composite basing score (0-1 range targets):
      - high trough count (normalized)
      - tight basing range
      - support retests
    All normalized by their respective 252-day rolling max; averaged.
    """
    cnt = _rolling_sum(_local_min_flag(low, 5), _TD_QTR)
    cnt_max = cnt.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max().replace(0, np.nan)
    cnt_norm = cnt / cnt_max

    r63 = _safe_div(_rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR),
                    _rolling_min(low, _TD_QTR))
    r_max = r63.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max().replace(0, np.nan)
    tightness_norm = 1.0 - (r63 / r_max).clip(0, 1)

    rmin_252 = _rolling_min(low, _TD_YEAR)
    near = (low <= rmin_252 * 1.03 + _EPS).astype(float)
    retest_cnt = _rolling_sum(near, _TD_QTR)
    retest_max = retest_cnt.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max().replace(0, np.nan)
    retest_norm = retest_cnt / retest_max

    return (cnt_norm.fillna(0) + tightness_norm.fillna(0) + retest_norm.fillna(0)) / 3.0


# ── Helper shims for registry cross-references ────────────────────────────────

def tcl_002_local_min_count_63d(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min (5-bar window) within trailing 63 days."""
    flag = _local_min_flag(low, 5)
    return _rolling_sum(flag, _TD_QTR)


def tcl_004_local_min_count_252d(low: pd.Series) -> pd.Series:
    """Count of bars flagged as local min (5-bar window) within trailing 252 days."""
    flag = _local_min_flag(low, 5)
    return _rolling_sum(flag, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

TROUGH_CLUSTERING_REGISTRY_076_150 = {
    "tcl_076_volume_at_troughs_fraction_126d":        {"inputs": ["low", "volume"],           "func": tcl_076_volume_at_troughs_fraction_126d},
    "tcl_077_volume_at_troughs_fraction_252d":        {"inputs": ["low", "volume"],           "func": tcl_077_volume_at_troughs_fraction_252d},
    "tcl_078_avg_volume_on_trough_days_63d":          {"inputs": ["low", "volume"],           "func": tcl_078_avg_volume_on_trough_days_63d},
    "tcl_079_avg_volume_on_trough_days_252d":         {"inputs": ["low", "volume"],           "func": tcl_079_avg_volume_on_trough_days_252d},
    "tcl_080_volume_ratio_trough_vs_nontrough_63d":   {"inputs": ["low", "volume"],           "func": tcl_080_volume_ratio_trough_vs_nontrough_63d},
    "tcl_081_volume_ratio_trough_vs_nontrough_252d":  {"inputs": ["low", "volume"],           "func": tcl_081_volume_ratio_trough_vs_nontrough_252d},
    "tcl_082_volume_zscore_on_trough_days_63d":       {"inputs": ["low", "volume"],           "func": tcl_082_volume_zscore_on_trough_days_63d},
    "tcl_083_high_volume_trough_count_63d":           {"inputs": ["low", "volume"],           "func": tcl_083_high_volume_trough_count_63d},
    "tcl_084_high_volume_trough_count_252d":          {"inputs": ["low", "volume"],           "func": tcl_084_high_volume_trough_count_252d},
    "tcl_085_trough_volume_trend_63d":                {"inputs": ["low", "volume"],           "func": tcl_085_trough_volume_trend_63d},
    "tcl_086_volume_concentration_near_low_63d":      {"inputs": ["low", "volume"],           "func": tcl_086_volume_concentration_near_low_63d},
    "tcl_087_volume_concentration_near_low_252d":     {"inputs": ["low", "volume"],           "func": tcl_087_volume_concentration_near_low_252d},
    "tcl_088_volume_weighted_trough_price_63d":       {"inputs": ["low", "volume"],           "func": tcl_088_volume_weighted_trough_price_63d},
    "tcl_089_rolling_min_slope_21d":                  {"inputs": ["low"],                     "func": tcl_089_rolling_min_slope_21d},
    "tcl_090_rolling_min_slope_63d":                  {"inputs": ["low"],                     "func": tcl_090_rolling_min_slope_63d},
    "tcl_091_rolling_min_slope_126d":                 {"inputs": ["low"],                     "func": tcl_091_rolling_min_slope_126d},
    "tcl_092_rolling_min_slope_252d":                 {"inputs": ["low"],                     "func": tcl_092_rolling_min_slope_252d},
    "tcl_093_rolling_min_acceleration_63d":           {"inputs": ["low"],                     "func": tcl_093_rolling_min_acceleration_63d},
    "tcl_094_double_bottom_flag_63d":                 {"inputs": ["low"],                     "func": tcl_094_double_bottom_flag_63d},
    "tcl_095_double_bottom_flag_126d":                {"inputs": ["low"],                     "func": tcl_095_double_bottom_flag_126d},
    "tcl_096_triple_bottom_flag_252d":                {"inputs": ["low"],                     "func": tcl_096_triple_bottom_flag_252d},
    "tcl_097_trough_low_vs_prior_trough_63d":         {"inputs": ["low"],                     "func": tcl_097_trough_low_vs_prior_trough_63d},
    "tcl_098_trough_low_vs_prior_trough_126d":        {"inputs": ["low"],                     "func": tcl_098_trough_low_vs_prior_trough_126d},
    "tcl_099_trough_low_vs_prior_trough_252d":        {"inputs": ["low"],                     "func": tcl_099_trough_low_vs_prior_trough_252d},
    "tcl_100_higher_low_flag_63d":                    {"inputs": ["low"],                     "func": tcl_100_higher_low_flag_63d},
    "tcl_101_open_at_trough_fraction_63d":            {"inputs": ["low", "open"],             "func": tcl_101_open_at_trough_fraction_63d},
    "tcl_102_open_at_trough_fraction_252d":           {"inputs": ["low", "open"],             "func": tcl_102_open_at_trough_fraction_252d},
    "tcl_103_intraday_low_touch_fraction_63d":        {"inputs": ["low", "close"],            "func": tcl_103_intraday_low_touch_fraction_63d},
    "tcl_104_high_low_range_at_trough_63d":           {"inputs": ["low", "high"],             "func": tcl_104_high_low_range_at_trough_63d},
    "tcl_105_high_low_range_at_trough_252d":          {"inputs": ["low", "high"],             "func": tcl_105_high_low_range_at_trough_252d},
    "tcl_106_close_above_low_at_trough_63d":          {"inputs": ["low", "close"],            "func": tcl_106_close_above_low_at_trough_63d},
    "tcl_107_close_above_low_at_trough_252d":         {"inputs": ["low", "close"],            "func": tcl_107_close_above_low_at_trough_252d},
    "tcl_108_trough_candle_body_frac_63d":            {"inputs": ["low", "open", "close"],    "func": tcl_108_trough_candle_body_frac_63d},
    "tcl_109_local_min_count_5bar_21d_close":         {"inputs": ["close"],                   "func": tcl_109_local_min_count_5bar_21d_close},
    "tcl_110_local_min_count_10bar_252d":             {"inputs": ["low"],                     "func": tcl_110_local_min_count_10bar_252d},
    "tcl_111_trough_bar_close_vs_open_ratio_252d":    {"inputs": ["low", "open", "close"],    "func": tcl_111_trough_bar_close_vs_open_ratio_252d},
    "tcl_112_trough_bar_close_vs_high_ratio_252d":    {"inputs": ["low", "high", "close"],    "func": tcl_112_trough_bar_close_vs_high_ratio_252d},
    "tcl_113_bars_since_last_local_min":              {"inputs": ["low"],                     "func": tcl_113_bars_since_last_local_min},
    "tcl_114_bars_since_last_local_min_10bar":        {"inputs": ["low"],                     "func": tcl_114_bars_since_last_local_min_10bar},
    "tcl_115_trough_recency_score_252d":              {"inputs": ["low"],                     "func": tcl_115_trough_recency_score_252d},
    "tcl_116_trough_recency_score_126d":              {"inputs": ["low"],                     "func": tcl_116_trough_recency_score_126d},
    "tcl_117_trough_count_ratio_recent_vs_old_252d":  {"inputs": ["low"],                     "func": tcl_117_trough_count_ratio_recent_vs_old_252d},
    "tcl_118_consecutive_trough_days_63d":            {"inputs": ["low"],                     "func": tcl_118_consecutive_trough_days_63d},
    "tcl_119_consecutive_trough_days_252d":           {"inputs": ["low"],                     "func": tcl_119_consecutive_trough_days_252d},
    "tcl_120_trough_periodicity_score_252d":          {"inputs": ["low"],                     "func": tcl_120_trough_periodicity_score_252d},
    "tcl_121_expanding_trough_count":                 {"inputs": ["low"],                     "func": tcl_121_expanding_trough_count},
    "tcl_122_expanding_trough_fraction":              {"inputs": ["low"],                     "func": tcl_122_expanding_trough_fraction},
    "tcl_123_trough_count_low_21bar_63d":             {"inputs": ["low"],                     "func": tcl_123_trough_count_low_21bar_63d},
    "tcl_124_trough_count_low_21bar_252d":            {"inputs": ["low"],                     "func": tcl_124_trough_count_low_21bar_252d},
    "tcl_125_trough_count_change_63d":                {"inputs": ["low"],                     "func": tcl_125_trough_count_change_63d},
    "tcl_126_close_low_trough_agreement_63d":         {"inputs": ["low", "close"],            "func": tcl_126_close_low_trough_agreement_63d},
    "tcl_127_close_low_trough_agreement_252d":        {"inputs": ["low", "close"],            "func": tcl_127_close_low_trough_agreement_252d},
    "tcl_128_low_trough_but_not_close_trough_63d":    {"inputs": ["low", "close"],            "func": tcl_128_low_trough_but_not_close_trough_63d},
    "tcl_129_low_min_count_vs_close_min_count_63d":   {"inputs": ["low", "close"],            "func": tcl_129_low_min_count_vs_close_min_count_63d},
    "tcl_130_trough_price_vs_open_at_trough_63d":     {"inputs": ["low", "open"],             "func": tcl_130_trough_price_vs_open_at_trough_63d},
    "tcl_131_trough_intraday_recovery_252d":          {"inputs": ["low", "close", "high"],    "func": tcl_131_trough_intraday_recovery_252d},
    "tcl_132_trough_count_10pct_band_close_252d":     {"inputs": ["close"],                   "func": tcl_132_trough_count_10pct_band_close_252d},
    "tcl_133_trough_count_10pct_band_low_252d":       {"inputs": ["low"],                     "func": tcl_133_trough_count_10pct_band_low_252d},
    "tcl_134_trough_spread_normalized_126d":          {"inputs": ["low"],                     "func": tcl_134_trough_spread_normalized_126d},
    "tcl_135_trough_spread_normalized_252d":          {"inputs": ["low"],                     "func": tcl_135_trough_spread_normalized_252d},
    "tcl_136_trough_price_percentile_rank_252d":      {"inputs": ["low"],                     "func": tcl_136_trough_price_percentile_rank_252d},
    "tcl_137_trough_price_percentile_rank_126d":      {"inputs": ["low"],                     "func": tcl_137_trough_price_percentile_rank_126d},
    "tcl_138_trough_price_percentile_rank_63d":       {"inputs": ["low"],                     "func": tcl_138_trough_price_percentile_rank_63d},
    "tcl_139_trough_cluster_intensity_63d":           {"inputs": ["low", "volume"],           "func": tcl_139_trough_cluster_intensity_63d},
    "tcl_140_trough_cluster_intensity_252d":          {"inputs": ["low", "volume"],           "func": tcl_140_trough_cluster_intensity_252d},
    "tcl_141_trough_zscore_63d_in_252d":              {"inputs": ["low"],                     "func": tcl_141_trough_zscore_63d_in_252d},
    "tcl_142_support_retest_zscore_63d":              {"inputs": ["low"],                     "func": tcl_142_support_retest_zscore_63d},
    "tcl_143_basing_range_21d_vs_252d":               {"inputs": ["low", "high"],             "func": tcl_143_basing_range_21d_vs_252d},
    "tcl_144_basing_range_63d_vs_252d":               {"inputs": ["low", "high"],             "func": tcl_144_basing_range_63d_vs_252d},
    "tcl_145_trough_count_pct_rank_in_252d_history":  {"inputs": ["low"],                     "func": tcl_145_trough_count_pct_rank_in_252d_history},
    "tcl_146_retest_fraction_trend_21d":              {"inputs": ["low"],                     "func": tcl_146_retest_fraction_trend_21d},
    "tcl_147_retest_fraction_trend_63d":              {"inputs": ["low"],                     "func": tcl_147_retest_fraction_trend_63d},
    "tcl_148_trough_min_price_stability_252d":        {"inputs": ["low"],                     "func": tcl_148_trough_min_price_stability_252d},
    "tcl_149_trough_count_low_vs_close_diff_252d":    {"inputs": ["low", "close"],            "func": tcl_149_trough_count_low_vs_close_diff_252d},
    "tcl_150_trough_composite_basing_score":          {"inputs": ["low", "high", "close"],    "func": tcl_150_trough_composite_basing_score},
}
