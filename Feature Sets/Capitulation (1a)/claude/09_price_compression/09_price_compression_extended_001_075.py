"""
09_price_compression — Extended Features 001-075
Domain: NR7/NR4/NR3/NR21 narrowest-range bars, rolling-range percentile at
multi-year lows, coil tightness, volatility-squeeze depth/duration, Donchian-
channel-width contraction, close-range vs HL-range compression, EWM-range
compression, compression z-scores and pct-ranks at additional windows, and
rate-of-change of compression.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _true_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Standard true range (max of HL, H-Cprev, L-Cprev in abs)."""
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low  - prev_c).abs(),
    ], axis=1).max(axis=1)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (raw=True, no lambda with array result)."""
    def _slope(arr):
        n = len(arr)
        if n < max(2, w // 2):
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom < _EPS:
            return np.nan
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


# ── NR helpers ────────────────────────────────────────────────────────────────

def _hl_range(high: pd.Series, low: pd.Series) -> pd.Series:
    return high - low


def _nr_flag(high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    """1 if today's HL range is the narrowest of the last n bars (NRn), else 0."""
    hl = _hl_range(high, low)
    # rolling min of PREVIOUS n-1 bars + today included in window of n
    rolling_min_n = hl.rolling(n, min_periods=n).min()
    # today is NRn if hl == rolling_min over window of size n
    return (hl <= rolling_min_n).astype(float)


def _tr_nr_flag(close: pd.Series, high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    """1 if today's TR is the narrowest of the last n bars (TR-NRn), else 0."""
    tr = _true_range(close, high, low)
    rolling_min_n = tr.rolling(n, min_periods=n).min()
    return (tr <= rolling_min_n).astype(float)


# ── Feature functions ext_001-075 ─────────────────────────────────────────────

# --- Group A (ext_001-010): NR4 / NR7 / NR3 / NR21 flags and basic counts ---

def pcmp_ext_001_nr4_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's HL range is the narrowest of the last 4 bars (NR4)."""
    return _nr_flag(high, low, 4)


def pcmp_ext_002_nr7_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's HL range is the narrowest of the last 7 bars (NR7)."""
    return _nr_flag(high, low, 7)


def pcmp_ext_003_nr3_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's HL range is the narrowest of the last 3 bars (NR3)."""
    return _nr_flag(high, low, 3)


def pcmp_ext_004_nr21_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's HL range is the narrowest of the last 21 bars (NR21)."""
    return _nr_flag(high, low, 21)


def pcmp_ext_005_tr_nr4_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's TR is the narrowest of the last 4 bars (TR-NR4)."""
    return _tr_nr_flag(close, high, low, 4)


def pcmp_ext_006_tr_nr7_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's TR is the narrowest of the last 7 bars (TR-NR7)."""
    return _tr_nr_flag(close, high, low, 7)


def pcmp_ext_007_nr4_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR4 bars in trailing 21-day window."""
    return _rolling_sum(_nr_flag(high, low, 4), _TD_MON)


def pcmp_ext_008_nr7_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 bars in trailing 21-day window."""
    return _rolling_sum(_nr_flag(high, low, 7), _TD_MON)


def pcmp_ext_009_nr4_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR4 bars in trailing 63-day window."""
    return _rolling_sum(_nr_flag(high, low, 4), _TD_QTR)


def pcmp_ext_010_nr7_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 bars in trailing 63-day window."""
    return _rolling_sum(_nr_flag(high, low, 7), _TD_QTR)


# --- Group B (ext_011-020): NR days-since, consecutive streaks, NR3/NR21 counts ---

def pcmp_ext_011_days_since_nr4(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since the most recent NR4 bar (0 = today is NR4)."""
    flag = _nr_flag(high, low, 4)
    def _days_since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0.5:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return flag.rolling(_TD_QTR, min_periods=1).apply(_days_since, raw=True)


def pcmp_ext_012_days_since_nr7(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since the most recent NR7 bar (0 = today is NR7)."""
    flag = _nr_flag(high, low, 7)
    def _days_since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0.5:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return flag.rolling(_TD_QTR, min_periods=1).apply(_days_since, raw=True)


def pcmp_ext_013_nr3_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR3 bars in trailing 21-day window."""
    return _rolling_sum(_nr_flag(high, low, 3), _TD_MON)


def pcmp_ext_014_nr21_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR21 bars in trailing 63-day window."""
    return _rolling_sum(_nr_flag(high, low, 21), _TD_QTR)


def pcmp_ext_015_nr7_consecutive_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of consecutive NR7 bars ending today (streak resets on non-NR7 day)."""
    flag = _nr_flag(high, low, 7)
    def _streak(arr):
        count = 0.0
        for v in arr:
            if v > 0.5:
                count += 1.0
            else:
                count = 0.0
        return count
    return flag.rolling(_TD_MON, min_periods=1).apply(_streak, raw=True)


def pcmp_ext_016_nr4_consecutive_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of consecutive NR4 bars ending today (streak resets on non-NR4 day)."""
    flag = _nr_flag(high, low, 4)
    def _streak(arr):
        count = 0.0
        for v in arr:
            if v > 0.5:
                count += 1.0
            else:
                count = 0.0
        return count
    return flag.rolling(_TD_MON, min_periods=1).apply(_streak, raw=True)


def pcmp_ext_017_nr7_then_expansion_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in last 21d where a NR7 was followed within 3 days by range expansion >median."""
    hl    = _hl_range(high, low)
    nr7   = _nr_flag(high, low, 7)
    med   = _rolling_median(hl, _TD_MON)
    # expansion = range > 21-day median
    expand = (hl > med).astype(float)
    # NR7 then expansion: expand[t] * (nr7[t-1] | nr7[t-2] | nr7[t-3])
    nr7_lag1 = nr7.shift(1).fillna(0.0)
    nr7_lag2 = nr7.shift(2).fillna(0.0)
    nr7_lag3 = nr7.shift(3).fillna(0.0)
    nr7_pre  = ((nr7_lag1 + nr7_lag2 + nr7_lag3) > 0).astype(float)
    seq      = expand * nr7_pre
    return _rolling_sum(seq, _TD_MON)


def pcmp_ext_018_nr4_then_expansion_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in last 21d where a NR4 was followed within 3 days by range > median."""
    hl    = _hl_range(high, low)
    nr4   = _nr_flag(high, low, 4)
    med   = _rolling_median(hl, _TD_MON)
    expand = (hl > med).astype(float)
    nr4_lag1 = nr4.shift(1).fillna(0.0)
    nr4_lag2 = nr4.shift(2).fillna(0.0)
    nr4_lag3 = nr4.shift(3).fillna(0.0)
    nr4_pre  = ((nr4_lag1 + nr4_lag2 + nr4_lag3) > 0).astype(float)
    seq      = expand * nr4_pre
    return _rolling_sum(seq, _TD_MON)


def pcmp_ext_019_tr_nr7_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TR-NR7 bars in trailing 63-day window."""
    return _rolling_sum(_tr_nr_flag(close, high, low, 7), _TD_QTR)


def pcmp_ext_020_nr7_frac_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of NR7 bars in trailing 252-day window."""
    return _safe_div(_rolling_sum(_nr_flag(high, low, 7), _TD_YEAR),
                     pd.Series(_TD_YEAR, index=high.index, dtype=float))


# --- Group C (ext_021-030): Rolling-range percentile at multi-year lows ---

def pcmp_ext_021_hl_range_pct_rank_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's HL range within trailing 504-day (2yr) window."""
    hl = _hl_range(high, low)
    return hl.rolling(504, min_periods=_TD_QTR).rank(pct=True)


def pcmp_ext_022_hl_range_pct_rank_756d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's HL range within trailing 756-day (3yr) window."""
    hl = _hl_range(high, low)
    return hl.rolling(756, min_periods=_TD_HALF).rank(pct=True)


def pcmp_ext_023_tr_pct_rank_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 504-day (2yr) window."""
    tr = _true_range(close, high, low)
    return tr.rolling(504, min_periods=_TD_QTR).rank(pct=True)


def pcmp_ext_024_tr_pct_rank_756d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 756-day (3yr) window."""
    tr = _true_range(close, high, low)
    return tr.rolling(756, min_periods=_TD_HALF).rank(pct=True)


def pcmp_ext_025_hl_range_vs_504d_min(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of today's HL range to the 504-day rolling minimum HL range."""
    hl     = _hl_range(high, low)
    min504 = hl.rolling(504, min_periods=_TD_QTR).min()
    return _safe_div(hl, min504)


def pcmp_ext_026_tr_vs_504d_min(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of today's TR to the 504-day rolling minimum TR."""
    tr     = _true_range(close, high, low)
    min504 = tr.rolling(504, min_periods=_TD_QTR).min()
    return _safe_div(tr, min504)


def pcmp_ext_027_atr21_pct_rank_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ATR within trailing 504-day window."""
    atr21 = _rolling_mean(_true_range(close, high, low), _TD_MON)
    return atr21.rolling(504, min_periods=_TD_QTR).rank(pct=True)


def pcmp_ext_028_atr21_pct_rank_756d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ATR within trailing 756-day window."""
    atr21 = _rolling_mean(_true_range(close, high, low), _TD_MON)
    return atr21.rolling(756, min_periods=_TD_HALF).rank(pct=True)


def pcmp_ext_029_hl_range_expanding_pct_rank(high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of today's HL range (low = historically tiny range)."""
    hl = _hl_range(high, low)
    return hl.expanding(min_periods=5).rank(pct=True)


def pcmp_ext_030_atr5_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 5-day ATR within trailing 252-day window."""
    atr5 = _rolling_mean(_true_range(close, high, low), _TD_WEEK)
    return _rolling_rank_pct(atr5, _TD_YEAR)


# --- Group D (ext_031-040): Coil/consolidation tightness and contraction streaks ---

def pcmp_ext_031_coil_tightness_5d_vs_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(max-H minus min-L) over 5d / same over 21d — how tight the recent coil is vs broader."""
    band5  = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    band21 = _rolling_max(high, _TD_MON)  - _rolling_min(low, _TD_MON)
    return _safe_div(band5, band21)


def pcmp_ext_032_coil_tightness_3d_vs_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(max-H minus min-L) over 3d / same over 21d — ultra-short coil tightness."""
    band3  = _rolling_max(high, 3) - _rolling_min(low, 3)
    band21 = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    return _safe_div(band3, band21)


def pcmp_ext_033_coil_tightness_10d_vs_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(max-H minus min-L) over 10d / same over 63d."""
    band10 = _rolling_max(high, 10) - _rolling_min(low, 10)
    band63 = _rolling_max(high, _TD_QTR) - _rolling_min(low, _TD_QTR)
    return _safe_div(band10, band63)


def pcmp_ext_034_hl_shrink_streak_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days in last 21 where each bar's HL range < prior bar's HL range (monotone shrink streak)."""
    hl   = _hl_range(high, low)
    shrk = (hl < hl.shift(1)).astype(float)
    return _rolling_sum(shrk, _TD_MON)


def pcmp_ext_035_tr_shrink_streak_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days in last 21 where each bar's TR < prior bar's TR."""
    tr   = _true_range(close, high, low)
    shrk = (tr < tr.shift(1)).astype(float)
    return _rolling_sum(shrk, _TD_MON)


def pcmp_ext_036_hl_shrink_max_run_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum consecutive run of shrinking HL-range bars within the last 21 days."""
    hl   = _hl_range(high, low)
    shrk = (hl < hl.shift(1)).astype(float)
    def _max_run(arr):
        best, cur = 0.0, 0.0
        for v in arr:
            if v > 0.5:
                cur += 1.0
                best = max(best, cur)
            else:
                cur = 0.0
        return best
    return shrk.rolling(_TD_MON, min_periods=1).apply(_max_run, raw=True)


def pcmp_ext_037_tr_shrink_max_run_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum consecutive run of shrinking TR bars within the last 21 days."""
    tr   = _true_range(close, high, low)
    shrk = (tr < tr.shift(1)).astype(float)
    def _max_run(arr):
        best, cur = 0.0, 0.0
        for v in arr:
            if v > 0.5:
                cur += 1.0
                best = max(best, cur)
            else:
                cur = 0.0
        return best
    return shrk.rolling(_TD_MON, min_periods=1).apply(_max_run, raw=True)


def pcmp_ext_038_coil_depth_ratio_5d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5d HL band to 252d HL band — depth of current coil vs long baseline."""
    band5   = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    band252 = _rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR)
    return _safe_div(band5, band252)


def pcmp_ext_039_close_range_vs_hl_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21d close-to-close range (max-min of close) to 21d HL band."""
    close_range = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    hl_band     = _rolling_max(high,  _TD_MON) - _rolling_min(low,   _TD_MON)
    return _safe_div(close_range, hl_band)


def pcmp_ext_040_close_range_vs_hl_range_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 63d close-to-close range to 63d HL band."""
    close_range = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    hl_band     = _rolling_max(high,  _TD_QTR) - _rolling_min(low,   _TD_QTR)
    return _safe_div(close_range, hl_band)


# --- Group E (ext_041-050): Donchian channel width contraction ---

def pcmp_ext_041_donchian_width_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day Donchian channel width (max_high - min_low) / close."""
    dc = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    return _safe_div(dc, close)


def pcmp_ext_042_donchian_width_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day Donchian channel width / close."""
    dc = _rolling_max(high, 10) - _rolling_min(low, 10)
    return _safe_div(dc, close)


def pcmp_ext_043_donchian_width_20d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """20-day Donchian channel width / close."""
    dc = _rolling_max(high, 20) - _rolling_min(low, 20)
    return _safe_div(dc, close)


def pcmp_ext_044_donchian_width_ratio_5d_vs_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day to 63-day Donchian channel width."""
    dc5  = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    dc63 = _rolling_max(high, _TD_QTR)  - _rolling_min(low, _TD_QTR)
    return _safe_div(dc5, dc63)


def pcmp_ext_045_donchian_width_ratio_10d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 10-day to 252-day Donchian channel width."""
    dc10  = _rolling_max(high, 10)       - _rolling_min(low, 10)
    dc252 = _rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR)
    return _safe_div(dc10, dc252)


def pcmp_ext_046_donchian_width_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 5-day Donchian width within trailing 252-day window."""
    dc5 = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    return _rolling_rank_pct(dc5, _TD_YEAR)


def pcmp_ext_047_donchian_width_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 5-day Donchian width within trailing 252-day window."""
    dc5 = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    return _zscore_rolling(dc5, _TD_YEAR)


def pcmp_ext_048_donchian_width_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 5-day Donchian width over trailing 21 days (negative = contracting)."""
    dc5 = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    return _linslope(dc5, _TD_MON)


def pcmp_ext_049_donchian_width_ewm_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of EWM-21 Donchian width to EWM-63 Donchian width (fast vs slow contraction)."""
    dc5 = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    return _safe_div(_ewm_mean(dc5, _TD_MON), _ewm_mean(dc5, _TD_QTR))


def pcmp_ext_050_donchian_width_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5-day Donchian width — speed of channel contraction."""
    dc5 = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    return dc5.diff(_TD_WEEK)


# --- Group F (ext_051-060): Volatility squeeze depth, duration, EWM-range compression ---

def pcmp_ext_051_vol_squeeze_depth_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth of BB-vs-Keltner squeeze: max(0, kc_width - bb_width) / price, 21d."""
    ma    = _rolling_mean(close, _TD_MON)
    bb_w  = 4.0 * _rolling_std(close, _TD_MON)
    tr    = _true_range(close, high, low)
    kc_w  = 4.0 * _rolling_mean(tr, _TD_MON)
    depth = (kc_w - bb_w).clip(lower=0.0)
    return _safe_div(depth, ma)


def pcmp_ext_052_vol_squeeze_depth_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth of BB-vs-Keltner squeeze over 63-day window / price."""
    ma    = _rolling_mean(close, _TD_QTR)
    bb_w  = 4.0 * _rolling_std(close, _TD_QTR)
    tr    = _true_range(close, high, low)
    kc_w  = 4.0 * _rolling_mean(tr, _TD_QTR)
    depth = (kc_w - bb_w).clip(lower=0.0)
    return _safe_div(depth, ma)


def pcmp_ext_053_vol_squeeze_depth_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21d squeeze depth within trailing 252-day window."""
    ma    = _rolling_mean(close, _TD_MON)
    bb_w  = 4.0 * _rolling_std(close, _TD_MON)
    tr    = _true_range(close, high, low)
    kc_w  = 4.0 * _rolling_mean(tr, _TD_MON)
    depth = _safe_div((kc_w - bb_w).clip(lower=0.0), ma)
    return _rolling_rank_pct(depth, _TD_YEAR)


def pcmp_ext_054_vol_squeeze_consecutive_days_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days of active BB-vs-Keltner squeeze (streak ending today, 21d window)."""
    bb_w = 4.0 * _rolling_std(close, _TD_MON)
    tr   = _true_range(close, high, low)
    kc_w = 4.0 * _rolling_mean(tr, _TD_MON)
    in_sq = (bb_w < kc_w).astype(float)
    def _streak(arr):
        count = 0.0
        for v in arr:
            if v > 0.5:
                count += 1.0
            else:
                count = 0.0
        return count
    return in_sq.rolling(_TD_MON, min_periods=1).apply(_streak, raw=True)


def pcmp_ext_055_ewm_tr_ratio_5_vs_63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of EWM-TR (span=5) to EWM-TR (span=63) — shortest vs quarterly compression."""
    tr = _true_range(close, high, low)
    return _safe_div(_ewm_mean(tr, _TD_WEEK), _ewm_mean(tr, _TD_QTR))


def pcmp_ext_056_ewm_tr_ratio_21_vs_126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of EWM-TR (span=21) to EWM-TR (span=126) — monthly vs semi-annual."""
    tr = _true_range(close, high, low)
    return _safe_div(_ewm_mean(tr, _TD_MON), _ewm_mean(tr, _TD_HALF))


def pcmp_ext_057_ewm_hl_ratio_5_vs_126(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of EWM-21 HL/close to EWM-126 HL/close — fast vs slow range compression."""
    hl_frac = _safe_div(high - low, close)
    return _safe_div(_ewm_mean(hl_frac, _TD_WEEK), _ewm_mean(hl_frac, _TD_HALF))


def pcmp_ext_058_ewm_vol_ratio_5_vs_252(close: pd.Series) -> pd.Series:
    """Ratio of EWM-std (span=5) to EWM-std (span=252) — fastest vs annual vol compression."""
    return _safe_div(_ewm_std(close, _TD_WEEK), _ewm_std(close, _TD_YEAR))


def pcmp_ext_059_ewm_tr_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of EWM-TR (span=5) within trailing 252-day window."""
    tr_ewm5 = _ewm_mean(_true_range(close, high, low), _TD_WEEK)
    return _rolling_rank_pct(tr_ewm5, _TD_YEAR)


def pcmp_ext_060_ewm_hl_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of EWM-21 HL/close within trailing 252-day distribution."""
    hl_frac = _safe_div(high - low, close)
    ewm21   = _ewm_mean(hl_frac, _TD_MON)
    return _zscore_rolling(ewm21, _TD_YEAR)


# --- Group G (ext_061-070): Compression z-scores at additional windows, ROC ---

def pcmp_ext_061_hl_range_zscore_126d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's HL range vs trailing 126-day distribution."""
    return _zscore_rolling(_hl_range(high, low), _TD_HALF)


def pcmp_ext_062_tr_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's TR vs trailing 126-day distribution."""
    return _zscore_rolling(_true_range(close, high, low), _TD_HALF)


def pcmp_ext_063_atr21_zscore_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day ATR within trailing 504-day (2yr) window."""
    atr21 = _rolling_mean(_true_range(close, high, low), _TD_MON)
    m     = atr21.rolling(504, min_periods=_TD_QTR).mean()
    sd    = atr21.rolling(504, min_periods=_TD_QTR).std()
    return _safe_div(atr21 - m, sd)


def pcmp_ext_064_bbw_21d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day BB width within trailing 504-day (2yr) window."""
    bbw21 = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    m     = bbw21.rolling(504, min_periods=_TD_QTR).mean()
    sd    = bbw21.rolling(504, min_periods=_TD_QTR).std()
    return _safe_div(bbw21 - m, sd)


def pcmp_ext_065_hl_range_roc_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rate-of-change of HL range: (HL_today - HL_21d_ago) / HL_21d_ago."""
    hl  = _hl_range(high, low)
    return _safe_div(hl - hl.shift(_TD_MON), hl.shift(_TD_MON).replace(0, np.nan))


def pcmp_ext_066_tr_roc_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rate-of-change of TR."""
    tr = _true_range(close, high, low)
    return _safe_div(tr - tr.shift(_TD_MON), tr.shift(_TD_MON).replace(0, np.nan))


def pcmp_ext_067_atr21_roc_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rate-of-change of 21-day ATR."""
    atr21 = _rolling_mean(_true_range(close, high, low), _TD_MON)
    return _safe_div(atr21 - atr21.shift(_TD_MON), atr21.shift(_TD_MON).replace(0, np.nan))


def pcmp_ext_068_bbw_21d_roc_21d(close: pd.Series) -> pd.Series:
    """21-day rate-of-change of 21-day BB width."""
    bbw = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return _safe_div(bbw - bbw.shift(_TD_MON), bbw.shift(_TD_MON).replace(0, np.nan))


def pcmp_ext_069_hl_range_roc_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rate-of-change of HL range."""
    hl = _hl_range(high, low)
    return _safe_div(hl - hl.shift(_TD_WEEK), hl.shift(_TD_WEEK).replace(0, np.nan))


def pcmp_ext_070_tr_roc_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rate-of-change of TR."""
    tr = _true_range(close, high, low)
    return _safe_div(tr - tr.shift(_TD_WEEK), tr.shift(_TD_WEEK).replace(0, np.nan))


# --- Group H (ext_071-075): NR composites and synthesis features ---

def pcmp_ext_071_nr_composite_score_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite NR score: (NR3_count + NR4_count + NR7_count) / 63 — multi-threshold compression density."""
    nr3c = _rolling_sum(_nr_flag(high, low, 3), _TD_MON)
    nr4c = _rolling_sum(_nr_flag(high, low, 4), _TD_MON)
    nr7c = _rolling_sum(_nr_flag(high, low, 7), _TD_MON)
    return _safe_div(nr3c + nr4c + nr7c, pd.Series(63.0, index=high.index))


def pcmp_ext_072_nr7_and_squeeze_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if NR7 day AND BB-vs-Keltner squeeze is active (dual compression confirmation)."""
    nr7   = _nr_flag(high, low, 7)
    bb_w  = 4.0 * _rolling_std(close, _TD_MON)
    tr    = _true_range(close, high, low)
    kc_w  = 4.0 * _rolling_mean(tr, _TD_MON)
    in_sq = (bb_w < kc_w).astype(float)
    return (nr7 * in_sq)


def pcmp_ext_073_nr7_count_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21d NR7 count within 252-day history."""
    nr7c = _rolling_sum(_nr_flag(high, low, 7), _TD_MON)
    return _rolling_rank_pct(nr7c, _TD_YEAR)


def pcmp_ext_074_range_compression_trifecta(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trifecta compression score: avg of NR7-count-rank, Donchian-width-rank, TR-pct-rank (all 252d)."""
    nr7c     = _rolling_sum(_nr_flag(high, low, 7), _TD_MON)
    nr7_r    = _rolling_rank_pct(nr7c, _TD_YEAR)
    dc5      = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    dc_r     = _rolling_rank_pct(dc5, _TD_YEAR)
    tr       = _true_range(close, high, low)
    tr_r     = _rolling_rank_pct(tr, _TD_YEAR)
    return (nr7_r + dc_r + tr_r) / 3.0


def pcmp_ext_075_nr_expansion_asymmetry_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR7-then-expansion count minus expansion-then-NR7 count over 21d: asymmetry of sequence."""
    hl     = _hl_range(high, low)
    nr7    = _nr_flag(high, low, 7)
    med    = _rolling_median(hl, _TD_MON)
    expand = (hl > med).astype(float)
    # NR7 followed by expansion (expansion after NR7)
    nr7_then_exp = expand * ((nr7.shift(1).fillna(0) + nr7.shift(2).fillna(0)) > 0).astype(float)
    # expansion followed by NR7 (NR7 after expansion)
    exp_then_nr7 = nr7 * ((expand.shift(1).fillna(0) + expand.shift(2).fillna(0)) > 0).astype(float)
    return _rolling_sum(nr7_then_exp, _TD_MON) - _rolling_sum(exp_then_nr7, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_COMPRESSION_EXTENDED_REGISTRY_001_075 = {
    "pcmp_ext_001_nr4_flag":                      {"inputs": ["high", "low"],                     "func": pcmp_ext_001_nr4_flag},
    "pcmp_ext_002_nr7_flag":                      {"inputs": ["high", "low"],                     "func": pcmp_ext_002_nr7_flag},
    "pcmp_ext_003_nr3_flag":                      {"inputs": ["high", "low"],                     "func": pcmp_ext_003_nr3_flag},
    "pcmp_ext_004_nr21_flag":                     {"inputs": ["high", "low"],                     "func": pcmp_ext_004_nr21_flag},
    "pcmp_ext_005_tr_nr4_flag":                   {"inputs": ["close", "high", "low"],            "func": pcmp_ext_005_tr_nr4_flag},
    "pcmp_ext_006_tr_nr7_flag":                   {"inputs": ["close", "high", "low"],            "func": pcmp_ext_006_tr_nr7_flag},
    "pcmp_ext_007_nr4_count_21d":                 {"inputs": ["high", "low"],                     "func": pcmp_ext_007_nr4_count_21d},
    "pcmp_ext_008_nr7_count_21d":                 {"inputs": ["high", "low"],                     "func": pcmp_ext_008_nr7_count_21d},
    "pcmp_ext_009_nr4_count_63d":                 {"inputs": ["high", "low"],                     "func": pcmp_ext_009_nr4_count_63d},
    "pcmp_ext_010_nr7_count_63d":                 {"inputs": ["high", "low"],                     "func": pcmp_ext_010_nr7_count_63d},
    "pcmp_ext_011_days_since_nr4":                {"inputs": ["high", "low"],                     "func": pcmp_ext_011_days_since_nr4},
    "pcmp_ext_012_days_since_nr7":                {"inputs": ["high", "low"],                     "func": pcmp_ext_012_days_since_nr7},
    "pcmp_ext_013_nr3_count_21d":                 {"inputs": ["high", "low"],                     "func": pcmp_ext_013_nr3_count_21d},
    "pcmp_ext_014_nr21_count_63d":                {"inputs": ["high", "low"],                     "func": pcmp_ext_014_nr21_count_63d},
    "pcmp_ext_015_nr7_consecutive_streak":        {"inputs": ["high", "low"],                     "func": pcmp_ext_015_nr7_consecutive_streak},
    "pcmp_ext_016_nr4_consecutive_streak":        {"inputs": ["high", "low"],                     "func": pcmp_ext_016_nr4_consecutive_streak},
    "pcmp_ext_017_nr7_then_expansion_21d":        {"inputs": ["high", "low"],                     "func": pcmp_ext_017_nr7_then_expansion_21d},
    "pcmp_ext_018_nr4_then_expansion_21d":        {"inputs": ["high", "low"],                     "func": pcmp_ext_018_nr4_then_expansion_21d},
    "pcmp_ext_019_tr_nr7_count_63d":              {"inputs": ["close", "high", "low"],            "func": pcmp_ext_019_tr_nr7_count_63d},
    "pcmp_ext_020_nr7_frac_252d":                 {"inputs": ["high", "low"],                     "func": pcmp_ext_020_nr7_frac_252d},
    "pcmp_ext_021_hl_range_pct_rank_504d":        {"inputs": ["high", "low"],                     "func": pcmp_ext_021_hl_range_pct_rank_504d},
    "pcmp_ext_022_hl_range_pct_rank_756d":        {"inputs": ["high", "low"],                     "func": pcmp_ext_022_hl_range_pct_rank_756d},
    "pcmp_ext_023_tr_pct_rank_504d":              {"inputs": ["close", "high", "low"],            "func": pcmp_ext_023_tr_pct_rank_504d},
    "pcmp_ext_024_tr_pct_rank_756d":              {"inputs": ["close", "high", "low"],            "func": pcmp_ext_024_tr_pct_rank_756d},
    "pcmp_ext_025_hl_range_vs_504d_min":          {"inputs": ["high", "low"],                     "func": pcmp_ext_025_hl_range_vs_504d_min},
    "pcmp_ext_026_tr_vs_504d_min":                {"inputs": ["close", "high", "low"],            "func": pcmp_ext_026_tr_vs_504d_min},
    "pcmp_ext_027_atr21_pct_rank_504d":           {"inputs": ["close", "high", "low"],            "func": pcmp_ext_027_atr21_pct_rank_504d},
    "pcmp_ext_028_atr21_pct_rank_756d":           {"inputs": ["close", "high", "low"],            "func": pcmp_ext_028_atr21_pct_rank_756d},
    "pcmp_ext_029_hl_range_expanding_pct_rank":   {"inputs": ["high", "low"],                     "func": pcmp_ext_029_hl_range_expanding_pct_rank},
    "pcmp_ext_030_atr5_pct_rank_252d":            {"inputs": ["close", "high", "low"],            "func": pcmp_ext_030_atr5_pct_rank_252d},
    "pcmp_ext_031_coil_tightness_5d_vs_21d":      {"inputs": ["high", "low"],                     "func": pcmp_ext_031_coil_tightness_5d_vs_21d},
    "pcmp_ext_032_coil_tightness_3d_vs_21d":      {"inputs": ["high", "low"],                     "func": pcmp_ext_032_coil_tightness_3d_vs_21d},
    "pcmp_ext_033_coil_tightness_10d_vs_63d":     {"inputs": ["high", "low"],                     "func": pcmp_ext_033_coil_tightness_10d_vs_63d},
    "pcmp_ext_034_hl_shrink_streak_count_21d":    {"inputs": ["high", "low"],                     "func": pcmp_ext_034_hl_shrink_streak_count_21d},
    "pcmp_ext_035_tr_shrink_streak_count_21d":    {"inputs": ["close", "high", "low"],            "func": pcmp_ext_035_tr_shrink_streak_count_21d},
    "pcmp_ext_036_hl_shrink_max_run_21d":         {"inputs": ["high", "low"],                     "func": pcmp_ext_036_hl_shrink_max_run_21d},
    "pcmp_ext_037_tr_shrink_max_run_21d":         {"inputs": ["close", "high", "low"],            "func": pcmp_ext_037_tr_shrink_max_run_21d},
    "pcmp_ext_038_coil_depth_ratio_5d_vs_252d":   {"inputs": ["high", "low"],                     "func": pcmp_ext_038_coil_depth_ratio_5d_vs_252d},
    "pcmp_ext_039_close_range_vs_hl_range_21d":   {"inputs": ["high", "low", "close"],            "func": pcmp_ext_039_close_range_vs_hl_range_21d},
    "pcmp_ext_040_close_range_vs_hl_range_63d":   {"inputs": ["high", "low", "close"],            "func": pcmp_ext_040_close_range_vs_hl_range_63d},
    "pcmp_ext_041_donchian_width_5d":             {"inputs": ["high", "low", "close"],            "func": pcmp_ext_041_donchian_width_5d},
    "pcmp_ext_042_donchian_width_10d":            {"inputs": ["high", "low", "close"],            "func": pcmp_ext_042_donchian_width_10d},
    "pcmp_ext_043_donchian_width_20d":            {"inputs": ["high", "low", "close"],            "func": pcmp_ext_043_donchian_width_20d},
    "pcmp_ext_044_donchian_width_ratio_5d_vs_63d": {"inputs": ["high", "low"],                   "func": pcmp_ext_044_donchian_width_ratio_5d_vs_63d},
    "pcmp_ext_045_donchian_width_ratio_10d_vs_252d": {"inputs": ["high", "low"],                 "func": pcmp_ext_045_donchian_width_ratio_10d_vs_252d},
    "pcmp_ext_046_donchian_width_pct_rank_252d":  {"inputs": ["high", "low"],                     "func": pcmp_ext_046_donchian_width_pct_rank_252d},
    "pcmp_ext_047_donchian_width_zscore_252d":    {"inputs": ["high", "low"],                     "func": pcmp_ext_047_donchian_width_zscore_252d},
    "pcmp_ext_048_donchian_width_slope_21d":      {"inputs": ["high", "low"],                     "func": pcmp_ext_048_donchian_width_slope_21d},
    "pcmp_ext_049_donchian_width_ewm_ratio":      {"inputs": ["high", "low"],                     "func": pcmp_ext_049_donchian_width_ewm_ratio},
    "pcmp_ext_050_donchian_width_5d_diff":        {"inputs": ["high", "low"],                     "func": pcmp_ext_050_donchian_width_5d_diff},
    "pcmp_ext_051_vol_squeeze_depth_21d":         {"inputs": ["close", "high", "low"],            "func": pcmp_ext_051_vol_squeeze_depth_21d},
    "pcmp_ext_052_vol_squeeze_depth_63d":         {"inputs": ["close", "high", "low"],            "func": pcmp_ext_052_vol_squeeze_depth_63d},
    "pcmp_ext_053_vol_squeeze_depth_pct_rank_252d": {"inputs": ["close", "high", "low"],          "func": pcmp_ext_053_vol_squeeze_depth_pct_rank_252d},
    "pcmp_ext_054_vol_squeeze_consecutive_days_21d": {"inputs": ["close", "high", "low"],         "func": pcmp_ext_054_vol_squeeze_consecutive_days_21d},
    "pcmp_ext_055_ewm_tr_ratio_5_vs_63":          {"inputs": ["close", "high", "low"],            "func": pcmp_ext_055_ewm_tr_ratio_5_vs_63},
    "pcmp_ext_056_ewm_tr_ratio_21_vs_126":        {"inputs": ["close", "high", "low"],            "func": pcmp_ext_056_ewm_tr_ratio_21_vs_126},
    "pcmp_ext_057_ewm_hl_ratio_5_vs_126":         {"inputs": ["high", "low", "close"],            "func": pcmp_ext_057_ewm_hl_ratio_5_vs_126},
    "pcmp_ext_058_ewm_vol_ratio_5_vs_252":        {"inputs": ["close"],                           "func": pcmp_ext_058_ewm_vol_ratio_5_vs_252},
    "pcmp_ext_059_ewm_tr_pct_rank_252d":          {"inputs": ["close", "high", "low"],            "func": pcmp_ext_059_ewm_tr_pct_rank_252d},
    "pcmp_ext_060_ewm_hl_zscore_252d":            {"inputs": ["high", "low", "close"],            "func": pcmp_ext_060_ewm_hl_zscore_252d},
    "pcmp_ext_061_hl_range_zscore_126d":          {"inputs": ["high", "low"],                     "func": pcmp_ext_061_hl_range_zscore_126d},
    "pcmp_ext_062_tr_zscore_126d":                {"inputs": ["close", "high", "low"],            "func": pcmp_ext_062_tr_zscore_126d},
    "pcmp_ext_063_atr21_zscore_504d":             {"inputs": ["close", "high", "low"],            "func": pcmp_ext_063_atr21_zscore_504d},
    "pcmp_ext_064_bbw_21d_zscore_504d":           {"inputs": ["close"],                           "func": pcmp_ext_064_bbw_21d_zscore_504d},
    "pcmp_ext_065_hl_range_roc_21d":              {"inputs": ["high", "low"],                     "func": pcmp_ext_065_hl_range_roc_21d},
    "pcmp_ext_066_tr_roc_21d":                    {"inputs": ["close", "high", "low"],            "func": pcmp_ext_066_tr_roc_21d},
    "pcmp_ext_067_atr21_roc_21d":                 {"inputs": ["close", "high", "low"],            "func": pcmp_ext_067_atr21_roc_21d},
    "pcmp_ext_068_bbw_21d_roc_21d":               {"inputs": ["close"],                           "func": pcmp_ext_068_bbw_21d_roc_21d},
    "pcmp_ext_069_hl_range_roc_5d":               {"inputs": ["high", "low"],                     "func": pcmp_ext_069_hl_range_roc_5d},
    "pcmp_ext_070_tr_roc_5d":                     {"inputs": ["close", "high", "low"],            "func": pcmp_ext_070_tr_roc_5d},
    "pcmp_ext_071_nr_composite_score_21d":        {"inputs": ["high", "low"],                     "func": pcmp_ext_071_nr_composite_score_21d},
    "pcmp_ext_072_nr7_and_squeeze_flag":          {"inputs": ["close", "high", "low"],            "func": pcmp_ext_072_nr7_and_squeeze_flag},
    "pcmp_ext_073_nr7_count_pct_rank_252d":       {"inputs": ["high", "low"],                     "func": pcmp_ext_073_nr7_count_pct_rank_252d},
    "pcmp_ext_074_range_compression_trifecta":    {"inputs": ["close", "high", "low"],            "func": pcmp_ext_074_range_compression_trifecta},
    "pcmp_ext_075_nr_expansion_asymmetry_21d":    {"inputs": ["high", "low"],                     "func": pcmp_ext_075_nr_expansion_asymmetry_21d},
}
