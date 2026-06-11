"""
09_price_compression — Base Features 001-075
Domain: price range narrowing / contraction near the absolute low
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
Measures SHRINKING of price dispersion (range, TR, BB-width, channel width).
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Intraday high-low range as fraction of price ---

def pcmp_001_hl_range_frac_close_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day rolling mean of (high-low)/close — raw daily range compressed by price level."""
    hl = (high - low) / close.replace(0, np.nan)
    return _rolling_mean(hl, _TD_WEEK)


def pcmp_002_hl_range_frac_close_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling mean of (high-low)/close."""
    hl = (high - low) / close.replace(0, np.nan)
    return _rolling_mean(hl, _TD_MON)


def pcmp_003_hl_range_frac_close_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling mean of (high-low)/close."""
    hl = (high - low) / close.replace(0, np.nan)
    return _rolling_mean(hl, _TD_QTR)


def pcmp_004_hl_range_frac_close_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """126-day rolling mean of (high-low)/close."""
    hl = (high - low) / close.replace(0, np.nan)
    return _rolling_mean(hl, _TD_HALF)


def pcmp_005_hl_range_frac_close_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling mean of (high-low)/close."""
    hl = (high - low) / close.replace(0, np.nan)
    return _rolling_mean(hl, _TD_YEAR)


def pcmp_006_hl_range_ratio_5d_vs_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day avg HL/close to 63-day avg HL/close — contraction vs baseline."""
    hl = (high - low) / close.replace(0, np.nan)
    return _safe_div(_rolling_mean(hl, _TD_WEEK), _rolling_mean(hl, _TD_QTR))


def pcmp_007_hl_range_ratio_5d_vs_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day avg HL/close to 252-day avg — short vs annual range."""
    hl = (high - low) / close.replace(0, np.nan)
    return _safe_div(_rolling_mean(hl, _TD_WEEK), _rolling_mean(hl, _TD_YEAR))


def pcmp_008_hl_range_ratio_21d_vs_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day avg HL/close to 252-day avg — monthly vs annual range."""
    hl = (high - low) / close.replace(0, np.nan)
    return _safe_div(_rolling_mean(hl, _TD_MON), _rolling_mean(hl, _TD_YEAR))


def pcmp_009_hl_range_ratio_63d_vs_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 63-day avg HL/close to 252-day avg."""
    hl = (high - low) / close.replace(0, np.nan)
    return _safe_div(_rolling_mean(hl, _TD_QTR), _rolling_mean(hl, _TD_YEAR))


def pcmp_010_hl_range_ratio_21d_vs_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day avg HL/close to 63-day avg."""
    hl = (high - low) / close.replace(0, np.nan)
    return _safe_div(_rolling_mean(hl, _TD_MON), _rolling_mean(hl, _TD_QTR))


# --- Group B (011-020): True range contraction ---

def pcmp_011_tr_frac_close_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day avg true range / close — ATR-normalized TR at short horizon."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_WEEK), close)


def pcmp_012_tr_frac_close_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day avg true range / close."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_MON), close)


def pcmp_013_tr_frac_close_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day avg true range / close."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_QTR), close)


def pcmp_014_tr_frac_close_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """126-day avg true range / close."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_HALF), close)


def pcmp_015_tr_frac_close_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day avg true range / close."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_YEAR), close)


def pcmp_016_tr_ratio_5d_vs_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day ATR to 63-day ATR — short TR vs quarterly baseline."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_QTR))


def pcmp_017_tr_ratio_5d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day ATR to 252-day ATR — short TR vs annual baseline."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_YEAR))


def pcmp_018_tr_ratio_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day ATR to 252-day ATR."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))


def pcmp_019_tr_ratio_63d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 63-day ATR to 252-day ATR."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_QTR), _rolling_mean(tr, _TD_YEAR))


def pcmp_020_tr_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of daily TR within trailing 252-day window (low rank = compression)."""
    tr = _true_range(close, high, low)
    return _rolling_rank_pct(tr, _TD_YEAR)


# --- Group C (021-030): Bollinger Band width contraction ---

def pcmp_021_bbw_21d(close: pd.Series) -> pd.Series:
    """Bollinger Band width (4*std/mean) on 21-day window — monthly squeeze."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    return _safe_div(4.0 * sd, ma)


def pcmp_022_bbw_63d(close: pd.Series) -> pd.Series:
    """Bollinger Band width on 63-day window."""
    ma = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    return _safe_div(4.0 * sd, ma)


def pcmp_023_bbw_126d(close: pd.Series) -> pd.Series:
    """Bollinger Band width on 126-day window."""
    ma = _rolling_mean(close, _TD_HALF)
    sd = _rolling_std(close, _TD_HALF)
    return _safe_div(4.0 * sd, ma)


def pcmp_024_bbw_252d(close: pd.Series) -> pd.Series:
    """Bollinger Band width on 252-day window."""
    ma = _rolling_mean(close, _TD_YEAR)
    sd = _rolling_std(close, _TD_YEAR)
    return _safe_div(4.0 * sd, ma)


def pcmp_025_bbw_ratio_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day BB width to 252-day BB width — squeeze intensity."""
    bbw21  = _safe_div(4.0 * _rolling_std(close, _TD_MON),  _rolling_mean(close, _TD_MON))
    bbw252 = _safe_div(4.0 * _rolling_std(close, _TD_YEAR), _rolling_mean(close, _TD_YEAR))
    return _safe_div(bbw21, bbw252)


def pcmp_026_bbw_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day BB width to 252-day BB width."""
    bbw63  = _safe_div(4.0 * _rolling_std(close, _TD_QTR),  _rolling_mean(close, _TD_QTR))
    bbw252 = _safe_div(4.0 * _rolling_std(close, _TD_YEAR), _rolling_mean(close, _TD_YEAR))
    return _safe_div(bbw63, bbw252)


def pcmp_027_bbw_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day BB width within trailing 252-day window."""
    bbw21 = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return _rolling_rank_pct(bbw21, _TD_YEAR)


def pcmp_028_bbw_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day BB width within trailing 504-day window."""
    bbw21 = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return bbw21.rolling(504, min_periods=_TD_QTR).rank(pct=True)


def pcmp_029_bbw_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day BB width over trailing 252-day window."""
    bbw21 = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return _zscore_rolling(bbw21, _TD_YEAR)


def pcmp_030_bbw_ewm_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day BB width to its 63-day EMA (short squeeze vs smoothed baseline)."""
    bbw21 = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return _safe_div(bbw21, _ewm_mean(bbw21, _TD_QTR))


# --- Group D (031-040): Rolling max-min channel width (price band) ---

def pcmp_031_channel_width_21d(close: pd.Series) -> pd.Series:
    """(max - min) / min of close over 21 days — channel width normalized."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    return _safe_div(h - l, l)


def pcmp_032_channel_width_63d(close: pd.Series) -> pd.Series:
    """(max - min) / min of close over 63 days."""
    h = _rolling_max(close, _TD_QTR)
    l = _rolling_min(close, _TD_QTR)
    return _safe_div(h - l, l)


def pcmp_033_channel_width_126d(close: pd.Series) -> pd.Series:
    """(max - min) / min of close over 126 days."""
    h = _rolling_max(close, _TD_HALF)
    l = _rolling_min(close, _TD_HALF)
    return _safe_div(h - l, l)


def pcmp_034_channel_width_252d(close: pd.Series) -> pd.Series:
    """(max - min) / min of close over 252 days."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    return _safe_div(h - l, l)


def pcmp_035_channel_width_ratio_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day channel width to 252-day channel width — coiling."""
    cw21  = _safe_div(_rolling_max(close, _TD_MON)  - _rolling_min(close, _TD_MON),  _rolling_min(close, _TD_MON))
    cw252 = _safe_div(_rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return _safe_div(cw21, cw252)


def pcmp_036_channel_width_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day channel width to 252-day channel width."""
    cw63  = _safe_div(_rolling_max(close, _TD_QTR)  - _rolling_min(close, _TD_QTR),  _rolling_min(close, _TD_QTR))
    cw252 = _safe_div(_rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return _safe_div(cw63, cw252)


def pcmp_037_channel_width_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(rolling-max-high - rolling-min-low) / rolling-min-low over 21 days."""
    h = _rolling_max(high, _TD_MON)
    l = _rolling_min(low,  _TD_MON)
    return _safe_div(h - l, l)


def pcmp_038_channel_width_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(rolling-max-high - rolling-min-low) / rolling-min-low over 63 days."""
    h = _rolling_max(high, _TD_QTR)
    l = _rolling_min(low,  _TD_QTR)
    return _safe_div(h - l, l)


def pcmp_039_channel_width_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(rolling-max-high - rolling-min-low) / rolling-min-low over 252 days."""
    h = _rolling_max(high, _TD_YEAR)
    l = _rolling_min(low,  _TD_YEAR)
    return _safe_div(h - l, l)


def pcmp_040_channel_width_hl_ratio_21d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day intraday channel width to 252-day intraday channel width."""
    cw21  = _safe_div(_rolling_max(high, _TD_MON)  - _rolling_min(low, _TD_MON),  _rolling_min(low, _TD_MON))
    cw252 = _safe_div(_rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR), _rolling_min(low, _TD_YEAR))
    return _safe_div(cw21, cw252)


# --- Group E (041-050): Close-to-close dispersion / realized volatility compression ---

def pcmp_041_realized_vol_5d(close: pd.Series) -> pd.Series:
    """5-day realized vol of daily log returns."""
    lr = _log_safe(close).diff(1)
    return lr.rolling(_TD_WEEK, min_periods=2).std()


def pcmp_042_realized_vol_21d(close: pd.Series) -> pd.Series:
    """21-day realized vol of daily log returns."""
    lr = _log_safe(close).diff(1)
    return lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()


def pcmp_043_realized_vol_63d(close: pd.Series) -> pd.Series:
    """63-day realized vol of daily log returns."""
    lr = _log_safe(close).diff(1)
    return lr.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()


def pcmp_044_realized_vol_252d(close: pd.Series) -> pd.Series:
    """252-day realized vol of daily log returns."""
    lr = _log_safe(close).diff(1)
    return lr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).std()


def pcmp_045_vol_ratio_5d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day realized vol to 63-day realized vol."""
    lr = _log_safe(close).diff(1)
    v5  = lr.rolling(_TD_WEEK, min_periods=2).std()
    v63 = lr.rolling(_TD_QTR,  min_periods=max(2, _TD_QTR // 2)).std()
    return _safe_div(v5, v63)


def pcmp_046_vol_ratio_5d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day realized vol to 252-day realized vol."""
    lr   = _log_safe(close).diff(1)
    v5   = lr.rolling(_TD_WEEK, min_periods=2).std()
    v252 = lr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).std()
    return _safe_div(v5, v252)


def pcmp_047_vol_ratio_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day realized vol to 252-day realized vol."""
    lr   = _log_safe(close).diff(1)
    v21  = lr.rolling(_TD_MON,  min_periods=max(2, _TD_MON // 2)).std()
    v252 = lr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).std()
    return _safe_div(v21, v252)


def pcmp_048_vol_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day realized vol to 252-day realized vol."""
    lr   = _log_safe(close).diff(1)
    v63  = lr.rolling(_TD_QTR,  min_periods=max(2, _TD_QTR // 2)).std()
    v252 = lr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).std()
    return _safe_div(v63, v252)


def pcmp_049_vol_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day realized vol within trailing 252-day window."""
    lr  = _log_safe(close).diff(1)
    v21 = lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    return _rolling_rank_pct(v21, _TD_YEAR)


def pcmp_050_vol_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day realized vol vs trailing 252-day distribution."""
    lr  = _log_safe(close).diff(1)
    v21 = lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    return _zscore_rolling(v21, _TD_YEAR)


# --- Group F (051-060): Inside-bar frequency and run-length of contracting bars ---

def pcmp_051_inside_bar_frac_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of inside bars (H<prev H AND L>prev L) over 5 days."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return _rolling_mean(inside, _TD_WEEK)


def pcmp_052_inside_bar_frac_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of inside bars over 21 days."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return _rolling_mean(inside, _TD_MON)


def pcmp_053_inside_bar_frac_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of inside bars over 63 days."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    return _rolling_mean(inside, _TD_QTR)


def pcmp_054_contracting_bar_frac_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of bars with smaller HL range than previous bar, 5-day window."""
    hl_range = high - low
    contracting = (hl_range < hl_range.shift(1)).astype(float)
    return _rolling_mean(contracting, _TD_WEEK)


def pcmp_055_contracting_bar_frac_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of contracting-range bars over 21 days."""
    hl_range = high - low
    contracting = (hl_range < hl_range.shift(1)).astype(float)
    return _rolling_mean(contracting, _TD_MON)


def pcmp_056_contracting_bar_frac_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of contracting-range bars over 63 days."""
    hl_range = high - low
    contracting = (hl_range < hl_range.shift(1)).astype(float)
    return _rolling_mean(contracting, _TD_QTR)


def pcmp_057_contracting_tr_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of bars with smaller TR than previous bar, 21-day window."""
    tr = _true_range(close, high, low)
    contracting = (tr < tr.shift(1)).astype(float)
    return _rolling_mean(contracting, _TD_MON)


def pcmp_058_contracting_tr_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of bars with smaller TR than previous bar, 63-day window."""
    tr = _true_range(close, high, low)
    contracting = (tr < tr.shift(1)).astype(float)
    return _rolling_mean(contracting, _TD_QTR)


def pcmp_059_days_since_range_expansion_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since HL range exceeded its 21-day rolling max (range expansion event)."""
    hl_range = high - low
    max_range = _rolling_max(hl_range, _TD_MON)
    expanded = (hl_range >= max_range.shift(1)).astype(float)
    # rolling sum of 1s since last expansion — count backward
    def _days_since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return hl_range.rolling(_TD_QTR, min_periods=1).apply(
        lambda x: _days_since((x == x.rolling(len(x), min_periods=1).max()).astype(float).values),
        raw=False
    )


def pcmp_060_consecutive_contracting_bars(high: pd.Series, low: pd.Series) -> pd.Series:
    """Run-length of consecutive contracting HL-range bars (reset on expansion)."""
    hl = high - low
    def _run(arr):
        count = 0.0
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                count += 1.0
            else:
                count = 0.0
        return count
    return hl.rolling(_TD_MON, min_periods=2).apply(_run, raw=True)


# --- Group G (061-070): Range quantile and expansion/contraction ratio ---

def pcmp_061_hl_range_quantile_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's HL range within trailing 252-day distribution."""
    hl = high - low
    return _rolling_rank_pct(hl, _TD_YEAR)


def pcmp_062_hl_range_quantile_rank_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's HL range within trailing 63-day distribution."""
    hl = high - low
    return _rolling_rank_pct(hl, _TD_QTR)


def pcmp_063_tr_quantile_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 252-day distribution."""
    tr = _true_range(close, high, low)
    return _rolling_rank_pct(tr, _TD_YEAR)


def pcmp_064_tr_quantile_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's TR within trailing 63-day distribution."""
    tr = _true_range(close, high, low)
    return _rolling_rank_pct(tr, _TD_QTR)


def pcmp_065_hl_range_vs_252d_max_range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's HL range as fraction of 252-day max HL range."""
    hl     = high - low
    max_hl = _rolling_max(hl, _TD_YEAR)
    return _safe_div(hl, max_hl)


def pcmp_066_hl_range_vs_252d_mean_range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's HL range vs 252-day mean HL range."""
    hl     = high - low
    avg_hl = _rolling_mean(hl, _TD_YEAR)
    return _safe_div(hl, avg_hl)


def pcmp_067_tr_vs_252d_max_tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR as fraction of 252-day max TR."""
    tr     = _true_range(close, high, low)
    max_tr = _rolling_max(tr, _TD_YEAR)
    return _safe_div(tr, max_tr)


def pcmp_068_tr_vs_63d_mean_tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR vs 63-day mean TR."""
    tr     = _true_range(close, high, low)
    avg_tr = _rolling_mean(tr, _TD_QTR)
    return _safe_div(tr, avg_tr)


def pcmp_069_oc_range_frac_close_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day avg of |open-close|/close — open-close body compression."""
    oc = (open - close).abs() / close.replace(0, np.nan)
    return _rolling_mean(oc, _TD_MON)


def pcmp_070_oc_range_frac_close_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """63-day avg of |open-close|/close — body compression quarterly."""
    oc = (open - close).abs() / close.replace(0, np.nan)
    return _rolling_mean(oc, _TD_QTR)


# --- Group H (071-075): Volume-weighted and EWM range compression ---

def pcmp_071_volume_weighted_range_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean HL range / close over 21 days."""
    hl_frac = (high - low) / close.replace(0, np.nan)
    v_norm  = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _rolling_mean(hl_frac * v_norm, _TD_MON)


def pcmp_072_volume_weighted_range_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean HL range / close over 63 days."""
    hl_frac = (high - low) / close.replace(0, np.nan)
    v_norm  = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return _rolling_mean(hl_frac * v_norm, _TD_QTR)


def pcmp_073_ewm_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=21) of HL/close — exponentially smoothed range."""
    hl_frac = (high - low) / close.replace(0, np.nan)
    return _ewm_mean(hl_frac, _TD_MON)


def pcmp_074_ewm_range_ratio_21d_vs_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of EWM-21 range to EWM-252 range — fast vs slow compression."""
    hl_frac = (high - low) / close.replace(0, np.nan)
    return _safe_div(_ewm_mean(hl_frac, _TD_MON), _ewm_mean(hl_frac, _TD_YEAR))


def pcmp_075_composite_range_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite range contraction: avg of BB-width rank, TR rank, channel-width rank (all 252d)."""
    bbw21   = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    bbw_r   = _rolling_rank_pct(bbw21, _TD_YEAR)
    tr      = _true_range(close, high, low)
    tr_r    = _rolling_rank_pct(tr, _TD_YEAR)
    cw21    = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                        _rolling_min(close, _TD_MON))
    cw_r    = _rolling_rank_pct(cw21, _TD_YEAR)
    return (bbw_r + tr_r + cw_r) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_COMPRESSION_REGISTRY_001_075 = {
    "pcmp_001_hl_range_frac_close_5d":          {"inputs": ["high", "low", "close"], "func": pcmp_001_hl_range_frac_close_5d},
    "pcmp_002_hl_range_frac_close_21d":         {"inputs": ["high", "low", "close"], "func": pcmp_002_hl_range_frac_close_21d},
    "pcmp_003_hl_range_frac_close_63d":         {"inputs": ["high", "low", "close"], "func": pcmp_003_hl_range_frac_close_63d},
    "pcmp_004_hl_range_frac_close_126d":        {"inputs": ["high", "low", "close"], "func": pcmp_004_hl_range_frac_close_126d},
    "pcmp_005_hl_range_frac_close_252d":        {"inputs": ["high", "low", "close"], "func": pcmp_005_hl_range_frac_close_252d},
    "pcmp_006_hl_range_ratio_5d_vs_63d":        {"inputs": ["high", "low", "close"], "func": pcmp_006_hl_range_ratio_5d_vs_63d},
    "pcmp_007_hl_range_ratio_5d_vs_252d":       {"inputs": ["high", "low", "close"], "func": pcmp_007_hl_range_ratio_5d_vs_252d},
    "pcmp_008_hl_range_ratio_21d_vs_252d":      {"inputs": ["high", "low", "close"], "func": pcmp_008_hl_range_ratio_21d_vs_252d},
    "pcmp_009_hl_range_ratio_63d_vs_252d":      {"inputs": ["high", "low", "close"], "func": pcmp_009_hl_range_ratio_63d_vs_252d},
    "pcmp_010_hl_range_ratio_21d_vs_63d":       {"inputs": ["high", "low", "close"], "func": pcmp_010_hl_range_ratio_21d_vs_63d},
    "pcmp_011_tr_frac_close_5d":                {"inputs": ["close", "high", "low"], "func": pcmp_011_tr_frac_close_5d},
    "pcmp_012_tr_frac_close_21d":               {"inputs": ["close", "high", "low"], "func": pcmp_012_tr_frac_close_21d},
    "pcmp_013_tr_frac_close_63d":               {"inputs": ["close", "high", "low"], "func": pcmp_013_tr_frac_close_63d},
    "pcmp_014_tr_frac_close_126d":              {"inputs": ["close", "high", "low"], "func": pcmp_014_tr_frac_close_126d},
    "pcmp_015_tr_frac_close_252d":              {"inputs": ["close", "high", "low"], "func": pcmp_015_tr_frac_close_252d},
    "pcmp_016_tr_ratio_5d_vs_63d":              {"inputs": ["close", "high", "low"], "func": pcmp_016_tr_ratio_5d_vs_63d},
    "pcmp_017_tr_ratio_5d_vs_252d":             {"inputs": ["close", "high", "low"], "func": pcmp_017_tr_ratio_5d_vs_252d},
    "pcmp_018_tr_ratio_21d_vs_252d":            {"inputs": ["close", "high", "low"], "func": pcmp_018_tr_ratio_21d_vs_252d},
    "pcmp_019_tr_ratio_63d_vs_252d":            {"inputs": ["close", "high", "low"], "func": pcmp_019_tr_ratio_63d_vs_252d},
    "pcmp_020_tr_pct_rank_252d":                {"inputs": ["close", "high", "low"], "func": pcmp_020_tr_pct_rank_252d},
    "pcmp_021_bbw_21d":                         {"inputs": ["close"], "func": pcmp_021_bbw_21d},
    "pcmp_022_bbw_63d":                         {"inputs": ["close"], "func": pcmp_022_bbw_63d},
    "pcmp_023_bbw_126d":                        {"inputs": ["close"], "func": pcmp_023_bbw_126d},
    "pcmp_024_bbw_252d":                        {"inputs": ["close"], "func": pcmp_024_bbw_252d},
    "pcmp_025_bbw_ratio_21d_vs_252d":           {"inputs": ["close"], "func": pcmp_025_bbw_ratio_21d_vs_252d},
    "pcmp_026_bbw_ratio_63d_vs_252d":           {"inputs": ["close"], "func": pcmp_026_bbw_ratio_63d_vs_252d},
    "pcmp_027_bbw_pct_rank_252d":               {"inputs": ["close"], "func": pcmp_027_bbw_pct_rank_252d},
    "pcmp_028_bbw_pct_rank_504d":               {"inputs": ["close"], "func": pcmp_028_bbw_pct_rank_504d},
    "pcmp_029_bbw_zscore_252d":                 {"inputs": ["close"], "func": pcmp_029_bbw_zscore_252d},
    "pcmp_030_bbw_ewm_ratio_21d":               {"inputs": ["close"], "func": pcmp_030_bbw_ewm_ratio_21d},
    "pcmp_031_channel_width_21d":               {"inputs": ["close"], "func": pcmp_031_channel_width_21d},
    "pcmp_032_channel_width_63d":               {"inputs": ["close"], "func": pcmp_032_channel_width_63d},
    "pcmp_033_channel_width_126d":              {"inputs": ["close"], "func": pcmp_033_channel_width_126d},
    "pcmp_034_channel_width_252d":              {"inputs": ["close"], "func": pcmp_034_channel_width_252d},
    "pcmp_035_channel_width_ratio_21d_vs_252d": {"inputs": ["close"], "func": pcmp_035_channel_width_ratio_21d_vs_252d},
    "pcmp_036_channel_width_ratio_63d_vs_252d": {"inputs": ["close"], "func": pcmp_036_channel_width_ratio_63d_vs_252d},
    "pcmp_037_channel_width_hl_21d":            {"inputs": ["high", "low"], "func": pcmp_037_channel_width_hl_21d},
    "pcmp_038_channel_width_hl_63d":            {"inputs": ["high", "low"], "func": pcmp_038_channel_width_hl_63d},
    "pcmp_039_channel_width_hl_252d":           {"inputs": ["high", "low"], "func": pcmp_039_channel_width_hl_252d},
    "pcmp_040_channel_width_hl_ratio_21d_vs_252d": {"inputs": ["high", "low"], "func": pcmp_040_channel_width_hl_ratio_21d_vs_252d},
    "pcmp_041_realized_vol_5d":                 {"inputs": ["close"], "func": pcmp_041_realized_vol_5d},
    "pcmp_042_realized_vol_21d":                {"inputs": ["close"], "func": pcmp_042_realized_vol_21d},
    "pcmp_043_realized_vol_63d":                {"inputs": ["close"], "func": pcmp_043_realized_vol_63d},
    "pcmp_044_realized_vol_252d":               {"inputs": ["close"], "func": pcmp_044_realized_vol_252d},
    "pcmp_045_vol_ratio_5d_vs_63d":             {"inputs": ["close"], "func": pcmp_045_vol_ratio_5d_vs_63d},
    "pcmp_046_vol_ratio_5d_vs_252d":            {"inputs": ["close"], "func": pcmp_046_vol_ratio_5d_vs_252d},
    "pcmp_047_vol_ratio_21d_vs_252d":           {"inputs": ["close"], "func": pcmp_047_vol_ratio_21d_vs_252d},
    "pcmp_048_vol_ratio_63d_vs_252d":           {"inputs": ["close"], "func": pcmp_048_vol_ratio_63d_vs_252d},
    "pcmp_049_vol_pct_rank_252d":               {"inputs": ["close"], "func": pcmp_049_vol_pct_rank_252d},
    "pcmp_050_vol_zscore_252d":                 {"inputs": ["close"], "func": pcmp_050_vol_zscore_252d},
    "pcmp_051_inside_bar_frac_5d":              {"inputs": ["high", "low"], "func": pcmp_051_inside_bar_frac_5d},
    "pcmp_052_inside_bar_frac_21d":             {"inputs": ["high", "low"], "func": pcmp_052_inside_bar_frac_21d},
    "pcmp_053_inside_bar_frac_63d":             {"inputs": ["high", "low"], "func": pcmp_053_inside_bar_frac_63d},
    "pcmp_054_contracting_bar_frac_5d":         {"inputs": ["high", "low"], "func": pcmp_054_contracting_bar_frac_5d},
    "pcmp_055_contracting_bar_frac_21d":        {"inputs": ["high", "low"], "func": pcmp_055_contracting_bar_frac_21d},
    "pcmp_056_contracting_bar_frac_63d":        {"inputs": ["high", "low"], "func": pcmp_056_contracting_bar_frac_63d},
    "pcmp_057_contracting_tr_frac_21d":         {"inputs": ["close", "high", "low"], "func": pcmp_057_contracting_tr_frac_21d},
    "pcmp_058_contracting_tr_frac_63d":         {"inputs": ["close", "high", "low"], "func": pcmp_058_contracting_tr_frac_63d},
    "pcmp_059_days_since_range_expansion_21d":  {"inputs": ["high", "low"], "func": pcmp_059_days_since_range_expansion_21d},
    "pcmp_060_consecutive_contracting_bars":    {"inputs": ["high", "low"], "func": pcmp_060_consecutive_contracting_bars},
    "pcmp_061_hl_range_quantile_rank_252d":     {"inputs": ["high", "low"], "func": pcmp_061_hl_range_quantile_rank_252d},
    "pcmp_062_hl_range_quantile_rank_63d":      {"inputs": ["high", "low"], "func": pcmp_062_hl_range_quantile_rank_63d},
    "pcmp_063_tr_quantile_rank_252d":           {"inputs": ["close", "high", "low"], "func": pcmp_063_tr_quantile_rank_252d},
    "pcmp_064_tr_quantile_rank_63d":            {"inputs": ["close", "high", "low"], "func": pcmp_064_tr_quantile_rank_63d},
    "pcmp_065_hl_range_vs_252d_max_range":      {"inputs": ["high", "low"], "func": pcmp_065_hl_range_vs_252d_max_range},
    "pcmp_066_hl_range_vs_252d_mean_range":     {"inputs": ["high", "low"], "func": pcmp_066_hl_range_vs_252d_mean_range},
    "pcmp_067_tr_vs_252d_max_tr":               {"inputs": ["close", "high", "low"], "func": pcmp_067_tr_vs_252d_max_tr},
    "pcmp_068_tr_vs_63d_mean_tr":               {"inputs": ["close", "high", "low"], "func": pcmp_068_tr_vs_63d_mean_tr},
    "pcmp_069_oc_range_frac_close_21d":         {"inputs": ["open", "close"], "func": pcmp_069_oc_range_frac_close_21d},
    "pcmp_070_oc_range_frac_close_63d":         {"inputs": ["open", "close"], "func": pcmp_070_oc_range_frac_close_63d},
    "pcmp_071_volume_weighted_range_21d":       {"inputs": ["high", "low", "close", "volume"], "func": pcmp_071_volume_weighted_range_21d},
    "pcmp_072_volume_weighted_range_63d":       {"inputs": ["high", "low", "close", "volume"], "func": pcmp_072_volume_weighted_range_63d},
    "pcmp_073_ewm_range_21d":                   {"inputs": ["high", "low", "close"], "func": pcmp_073_ewm_range_21d},
    "pcmp_074_ewm_range_ratio_21d_vs_252d":     {"inputs": ["high", "low", "close"], "func": pcmp_074_ewm_range_ratio_21d_vs_252d},
    "pcmp_075_composite_range_score":           {"inputs": ["close", "high", "low"], "func": pcmp_075_composite_range_score},
}
