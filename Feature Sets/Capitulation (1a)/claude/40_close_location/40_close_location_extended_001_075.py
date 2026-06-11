"""
40_close_location — Extended Features 001-075
Domain: close-location value (CLV) — deeper variants, volume-interacted CLV,
        multi-price CLV forms, CLV on open/typical price, CLV quantile flags,
        intraday range asymmetry, CLV regime indicators, and capitulation composites.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


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


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _clv_raw(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Core CLV = ((close-low)-(high-close))/(high-low), NaN when range=0."""
    hl = high - low
    return _safe_div((close - low) - (high - close), hl)


def _close_frac(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close as fraction of range: (close-low)/(high-low), in [0,1]."""
    return _safe_div(close - low, high - low)


def _typical_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return (high + low + close) / 3.0


def _weighted_close(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return (high + low + 2.0 * close) / 4.0


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): CLV on alternative price constructs ---

def clv_ext_001_clv_typical_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV where 'close' is replaced by typical price (H+L+C)/3."""
    tp = _typical_price(close, high, low)
    hl = high - low
    return _safe_div((tp - low) - (high - tp), hl)


def clv_ext_002_clv_weighted_close(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV where 'close' is replaced by weighted close (H+L+2C)/4."""
    wc = _weighted_close(close, high, low)
    hl = high - low
    return _safe_div((wc - low) - (high - wc), hl)


def clv_ext_003_clv_open(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV computed on the open price instead of close."""
    hl = high - low
    return _safe_div((open - low) - (high - open), hl)


def clv_ext_004_open_frac_of_range(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Open as fraction of range: (open-low)/(high-low), in [0,1]."""
    return _safe_div(open - low, high - low)


def clv_ext_005_clv_hl_midpoint(high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV for HL midpoint: midpoint is always exactly the bar center, returns 0 always.
    Useful as reference; practical variant: midpoint deviation from prior close."""
    mid = (high + low) / 2.0
    hl = high - low
    return _safe_div((mid - low) - (high - mid), hl)


def clv_ext_006_close_vs_open_frac(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Difference: close-fraction minus open-fraction of range (intraday direction)."""
    cf = _close_frac(close, high, low)
    of = _safe_div(open - low, high - low)
    return cf - of


def clv_ext_007_clv_typical_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of CLV(typical price)."""
    tp = _typical_price(close, high, low)
    hl = high - low
    clv_tp = _safe_div((tp - low) - (high - tp), hl)
    return _rolling_mean(clv_tp, _TD_MON)


def clv_ext_008_clv_typical_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of CLV(typical price) over trailing 63 days."""
    tp = _typical_price(close, high, low)
    hl = high - low
    clv_tp = _safe_div((tp - low) - (high - tp), hl)
    m = _rolling_mean(clv_tp, _TD_QTR)
    s = _rolling_std(clv_tp, _TD_QTR)
    return _safe_div(clv_tp - m, s)


def clv_ext_009_clv_open_sma21(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of CLV(open price)."""
    hl = high - low
    clv_open = _safe_div((open - low) - (high - open), hl)
    return _rolling_mean(clv_open, _TD_MON)


def clv_ext_010_open_to_close_range_frac(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Abs(close - open) / (high - low): body size as fraction of total range."""
    return _safe_div((close - open).abs(), high - low)


# --- Group B (011-020): Volume-weighted CLV extended variants ---

def clv_ext_011_vwclv_avg_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day volume-weighted average CLV."""
    clv = _clv_raw(close, high, low)
    w = 126
    return _safe_div(_rolling_sum(clv * volume, w), _rolling_sum(volume, w))


def clv_ext_012_vwclv_avg_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day volume-weighted average CLV."""
    clv = _clv_raw(close, high, low)
    return _safe_div(_rolling_sum(clv * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))


def clv_ext_013_vwclv_avg_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day volume-weighted average CLV."""
    clv = _clv_raw(close, high, low)
    return _safe_div(_rolling_sum(clv * volume, _TD_WEEK), _rolling_sum(volume, _TD_WEEK))


def clv_ext_014_vwclv_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily volume*CLV relative to 63-day distribution."""
    vc = _clv_raw(close, high, low) * volume
    m = _rolling_mean(vc, _TD_QTR)
    s = _rolling_std(vc, _TD_QTR)
    return _safe_div(vc - m, s)


def clv_ext_015_vwclv_neg_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day sum of volume*CLV on days when CLV < 0 (distribution pressure, quarterly)."""
    clv = _clv_raw(close, high, low)
    neg_contrib = (clv * volume).where(clv < 0, 0.0)
    return _rolling_sum(neg_contrib, _TD_QTR)


def clv_ext_016_vwclv_pos_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day sum of volume*CLV on days when CLV > 0 (accumulation pressure, quarterly)."""
    clv = _clv_raw(close, high, low)
    pos_contrib = (clv * volume).where(clv > 0, 0.0)
    return _rolling_sum(pos_contrib, _TD_QTR)


def clv_ext_017_vwclv_bull_bear_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day ratio of positive vol*CLV sum to abs(negative vol*CLV) sum."""
    clv = _clv_raw(close, high, low)
    pos = _rolling_sum((clv * volume).where(clv > 0, 0.0), _TD_QTR)
    neg = _rolling_sum((clv * volume).where(clv < 0, 0.0).abs(), _TD_QTR)
    return _safe_div(pos, neg)


def clv_ext_018_vwclv_vs_clv_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day VWCLV minus 63-day plain CLV SMA (volume weighting effect, quarterly)."""
    clv = _clv_raw(close, high, low)
    vwavg = _safe_div(_rolling_sum(clv * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return vwavg - _rolling_mean(clv, _TD_QTR)


def clv_ext_019_vwclv_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of daily vol*CLV within trailing 252-day distribution."""
    vc = _clv_raw(close, high, low) * volume
    return vc.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def clv_ext_020_vwclv_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of 5-day VWCLV (trend of volume-weighted close location)."""
    clv = _clv_raw(close, high, low)
    vw5 = _safe_div(_rolling_sum(clv * volume, _TD_WEEK), _rolling_sum(volume, _TD_WEEK))
    return _linslope(vw5, _TD_MON)


# --- Group C (021-030): CLV quantile/threshold flags — extended thresholds ---

def clv_ext_021_close_frac_lt_010_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close in bottom 10% of range (extreme bearish close)."""
    return (_close_frac(close, high, low) <= 0.10).astype(float)


def clv_ext_022_close_frac_lt_015_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close in bottom 15% of range."""
    return (_close_frac(close, high, low) <= 0.15).astype(float)


def clv_ext_023_close_frac_lt_033_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close in bottom third of range (frac <= 0.33)."""
    return (_close_frac(close, high, low) <= 0.333).astype(float)


def clv_ext_024_close_frac_gt_090_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close in top 10% of range (extreme bullish close)."""
    return (_close_frac(close, high, low) >= 0.90).astype(float)


def clv_ext_025_clv_lt_minus09_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV < -0.9 (close extremely near the low)."""
    return (_clv_raw(close, high, low) < -0.9).astype(float)


def clv_ext_026_clv_lt_minus07_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV < -0.7."""
    return (_clv_raw(close, high, low) < -0.7).astype(float)


def clv_ext_027_count_clv_lt_minus09_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with CLV < -0.9 in trailing 21 days (extreme capitulation days)."""
    return _rolling_count_true(_clv_raw(close, high, low) < -0.9, _TD_MON)


def clv_ext_028_count_clv_lt_minus09_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with CLV < -0.9 in trailing 63 days."""
    return _rolling_count_true(_clv_raw(close, high, low) < -0.9, _TD_QTR)


def clv_ext_029_count_clv_lt_minus07_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with CLV < -0.7 in trailing 21 days."""
    return _rolling_count_true(_clv_raw(close, high, low) < -0.7, _TD_MON)


def clv_ext_030_count_close_frac_lt_010_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with close in bottom 10% of range over trailing 63 days."""
    return _rolling_count_true(_close_frac(close, high, low) <= 0.10, _TD_QTR)


# --- Group D (031-040): CLV z-score extended windows and forms ---

def clv_ext_031_clv_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of CLV relative to trailing 5-day mean and std."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, _TD_WEEK)
    s = _rolling_std(clv, _TD_WEEK)
    return _safe_div(clv - m, s)


def clv_ext_032_clv_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of CLV relative to trailing 126-day mean and std."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, 126)
    s = _rolling_std(clv, 126)
    return _safe_div(clv - m, s)


def clv_ext_033_close_frac_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of close-fraction relative to trailing 21-day distribution."""
    cf = _close_frac(close, high, low)
    m = _rolling_mean(cf, _TD_MON)
    s = _rolling_std(cf, _TD_MON)
    return _safe_div(cf - m, s)


def clv_ext_034_close_frac_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of close-fraction relative to trailing 63-day distribution."""
    cf = _close_frac(close, high, low)
    m = _rolling_mean(cf, _TD_QTR)
    s = _rolling_std(cf, _TD_QTR)
    return _safe_div(cf - m, s)


def clv_ext_035_clv_abs_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of |CLV| (magnitude of close displacement) vs 21-day distribution."""
    clv_abs = _clv_raw(close, high, low).abs()
    m = _rolling_mean(clv_abs, _TD_MON)
    s = _rolling_std(clv_abs, _TD_MON)
    return _safe_div(clv_abs - m, s)


def clv_ext_036_clv_abs_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of |CLV| vs 63-day distribution."""
    clv_abs = _clv_raw(close, high, low).abs()
    m = _rolling_mean(clv_abs, _TD_QTR)
    s = _rolling_std(clv_abs, _TD_QTR)
    return _safe_div(clv_abs - m, s)


def clv_ext_037_clv_zscore_252d_clipped(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day CLV z-score clipped at [-3, 0] — distress magnitude only."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, _TD_YEAR)
    s = _rolling_std(clv, _TD_YEAR)
    z = _safe_div(clv - m, s)
    return z.clip(upper=0.0).clip(lower=-3.0)


def clv_ext_038_close_frac_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of close-fraction relative to trailing 252-day distribution."""
    cf = _close_frac(close, high, low)
    m = _rolling_mean(cf, _TD_YEAR)
    s = _rolling_std(cf, _TD_YEAR)
    return _safe_div(cf - m, s)


def clv_ext_039_clv_iqr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day interquartile range of CLV (75th pct - 25th pct)."""
    clv = _clv_raw(close, high, low)
    q75 = clv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = clv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def clv_ext_040_clv_iqr_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day interquartile range of CLV."""
    clv = _clv_raw(close, high, low)
    q75 = clv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = clv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return q75 - q25


# --- Group E (041-050): CLV percentile ranks — extended ---

def clv_ext_041_clv_pct_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's CLV within trailing 5 days."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(_TD_WEEK, min_periods=1).rank(pct=True)


def clv_ext_042_clv_pct_rank_10d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's CLV within trailing 10 days."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(10, min_periods=5).rank(pct=True)


def clv_ext_043_close_frac_pct_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of close-fraction within trailing 21 days."""
    cf = _close_frac(close, high, low)
    return cf.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def clv_ext_044_close_frac_pct_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of close-fraction within trailing 5 days."""
    cf = _close_frac(close, high, low)
    return cf.rolling(_TD_WEEK, min_periods=1).rank(pct=True)


def clv_ext_045_clv_pct_rank_10d_expanding(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of CLV (full history), min 10 periods."""
    clv = _clv_raw(close, high, low)
    return clv.expanding(min_periods=10).rank(pct=True)


def clv_ext_046_close_frac_pct_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of close-fraction within trailing 126 days."""
    cf = _close_frac(close, high, low)
    return cf.rolling(126, min_periods=63).rank(pct=True)


def clv_ext_047_clv_abs_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of |CLV| within trailing 252 days (extremity rank)."""
    clv_abs = _clv_raw(close, high, low).abs()
    return clv_abs.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def clv_ext_048_clv_q10_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10th percentile of CLV over trailing 21 days (near-worst close location)."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.10)


def clv_ext_049_clv_q10_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10th percentile of CLV over trailing 63 days."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)


def clv_ext_050_clv_q25_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """25th percentile of CLV over trailing 252 days (structural bear threshold)."""
    clv = _clv_raw(close, high, low)
    return clv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)


# --- Group F (051-060): CLV regime flags and smoothed variants ---

def clv_ext_051_clv_bear_regime_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bear regime flag: CLV SMA21 < 0 AND close-frac SMA21 < 0.4."""
    clv = _clv_raw(close, high, low)
    cf = _close_frac(close, high, low)
    return ((_rolling_mean(clv, _TD_MON) < 0) & (_rolling_mean(cf, _TD_MON) < 0.4)).astype(float)


def clv_ext_052_clv_severe_bear_regime_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Severe bear regime flag: CLV SMA63 < -0.3 AND close-frac SMA63 < 0.35."""
    clv = _clv_raw(close, high, low)
    cf = _close_frac(close, high, low)
    return ((_rolling_mean(clv, _TD_QTR) < -0.3) & (_rolling_mean(cf, _TD_QTR) < 0.35)).astype(float)


def clv_ext_053_clv_multi_streak_regime_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: consecutive neg-CLV >= 3 AND CLV SMA5 < -0.3 (multi-day bear momentum)."""
    clv = _clv_raw(close, high, low)
    streak = _consec_streak(clv < 0)
    sma5 = _rolling_mean(clv, _TD_WEEK)
    return ((streak >= 3) & (sma5 < -0.3)).astype(float)


def clv_ext_054_clv_triple_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Triple-bearish flag: CLV < 0 AND close-frac < 0.25 AND CLV 21d SMA < -0.2."""
    clv = _clv_raw(close, high, low)
    cf = _close_frac(close, high, low)
    return ((clv < 0) & (cf < 0.25) & (_rolling_mean(clv, _TD_MON) < -0.2)).astype(float)


def clv_ext_055_clv_ema10(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10-day EMA of CLV."""
    return _ewm_mean(_clv_raw(close, high, low), 10)


def clv_ext_056_clv_ema126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """126-day EMA of CLV."""
    return _ewm_mean(_clv_raw(close, high, low), 126)


def clv_ext_057_clv_sma10(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10-day SMA of CLV (between weekly and monthly)."""
    return _rolling_mean(_clv_raw(close, high, low), 10)


def clv_ext_058_clv_sma10_vs_sma63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10-day SMA of CLV minus 63-day SMA (short vs quarterly trend)."""
    clv = _clv_raw(close, high, low)
    return _rolling_mean(clv, 10) - _rolling_mean(clv, _TD_QTR)


def clv_ext_059_close_frac_sma5(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day SMA of close-fraction (weekly average position in range)."""
    return _rolling_mean(_close_frac(close, high, low), _TD_WEEK)


def clv_ext_060_close_frac_sma126(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """126-day SMA of close-fraction (semi-annual average position)."""
    return _rolling_mean(_close_frac(close, high, low), 126)


# --- Group G (061-070): Range asymmetry and intraday structure ---

def clv_ext_061_upper_shadow_frac(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Upper shadow as fraction of total range: (high - max(open_proxy, close))/(high-low).
    Proxy: close for open. Upper shadow = (high - close) / (high - low)."""
    return _safe_div(high - close, high - low)


def clv_ext_062_lower_shadow_frac(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lower shadow fraction: (close - low) / (high - low) = close_frac."""
    return _close_frac(close, high, low)


def clv_ext_063_upper_shadow_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of upper shadow fraction."""
    upper_sh = _safe_div(high - close, high - low)
    return _rolling_mean(upper_sh, _TD_MON)


def clv_ext_064_lower_shadow_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of lower shadow fraction (= 21d SMA of close-frac)."""
    return _rolling_mean(_close_frac(close, high, low), _TD_MON)


def clv_ext_065_shadow_ratio_upper_vs_lower(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio: upper shadow frac / lower shadow frac (dominance of upper vs lower wick)."""
    upper = _safe_div(high - close, high - low)
    lower = _close_frac(close, high, low)
    return _safe_div(upper, lower)


def clv_ext_066_shadow_ratio_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of upper/lower shadow ratio (persistent wick direction)."""
    upper = _safe_div(high - close, high - low)
    lower = _close_frac(close, high, low)
    ratio = _safe_div(upper, lower)
    return _rolling_mean(ratio, _TD_MON)


def clv_ext_067_range_asymmetry_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day avg of (upper_shadow - lower_shadow): persistent bias toward lows."""
    upper = _safe_div(high - close, high - low)
    lower = _close_frac(close, high, low)
    return _rolling_mean(upper - lower, _TD_MON)


def clv_ext_068_close_to_high_pct_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day avg of (close/high - 1): pct gap between close and day's high."""
    return _rolling_mean(_safe_div(close, high) - 1.0, _TD_MON)


def clv_ext_069_close_to_low_pct_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day avg of (close/low - 1): pct gap between close and day's low."""
    return _rolling_mean(_safe_div(close, low) - 1.0, _TD_MON)


def clv_ext_070_hl_range_norm_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of (high-low)/close: range normalized by close (relative volatility)."""
    rng_norm = _safe_div(high - low, close)
    return _rolling_mean(rng_norm, _TD_MON)


# --- Group H (071-075): Capitulation composites and cross-window ---

def clv_ext_071_clv_cap_score_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Capitulation score (63d): 0.5*(1 - CLV SMA63 scaled) + 0.5*frac_near_low_63d."""
    clv = _clv_raw(close, high, low)
    cf = _close_frac(close, high, low)
    avg_clv = _rolling_mean(clv, _TD_QTR)
    frac_low = _rolling_count_true(cf <= 0.25, _TD_QTR) / _TD_QTR
    return 0.5 * (1.0 - avg_clv) / 2.0 + 0.5 * frac_low


def clv_ext_072_clv_depth_below_minus05_sum21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day cumulative depth of CLV below -0.5 (intensity of weak closes)."""
    clv = _clv_raw(close, high, low)
    depth = (-0.5 - clv).clip(lower=0.0)
    return _rolling_sum(depth, _TD_MON)


def clv_ext_073_clv_depth_below_minus08_sum21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day cumulative depth of CLV below -0.8 (extreme capitulation intensity)."""
    clv = _clv_raw(close, high, low)
    depth = (-0.8 - clv).clip(lower=0.0)
    return _rolling_sum(depth, _TD_MON)


def clv_ext_074_clv_vol_interaction_bearish_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day sum of volume * |CLV| on days CLV < 0 (volume-weighted bearish intensity)."""
    clv = _clv_raw(close, high, low)
    neg_intensity = (volume * clv.abs()).where(clv < 0, 0.0)
    return _rolling_sum(neg_intensity, _TD_MON)


def clv_ext_075_clv_composite_distress_3d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """3-component CLV distress composite: z-score(252d) + pct_rank(252d inverted) + VWCLV_21d_normalized.
    Higher value = deeper distress."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, _TD_YEAR)
    s = _rolling_std(clv, _TD_YEAR)
    z = _safe_div(clv - m, s).clip(lower=-3.0, upper=0.0) / (-3.0 + _EPS)
    rank = clv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    inv_rank = (1.0 - rank.fillna(0.5))
    vw21 = _safe_div(_rolling_sum(clv * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    vw_norm = _safe_div(vw21 - _rolling_mean(vw21, _TD_YEAR), _rolling_std(vw21, _TD_YEAR) + _EPS)
    vw_distress = (-vw_norm).clip(lower=0.0) / (3.0 + _EPS)
    return (z + inv_rank + vw_distress) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

CLOSE_LOCATION_EXTENDED_REGISTRY_001_075 = {
    "clv_ext_001_clv_typical_price": {"inputs": ["close", "high", "low"], "func": clv_ext_001_clv_typical_price},
    "clv_ext_002_clv_weighted_close": {"inputs": ["close", "high", "low"], "func": clv_ext_002_clv_weighted_close},
    "clv_ext_003_clv_open": {"inputs": ["open", "high", "low"], "func": clv_ext_003_clv_open},
    "clv_ext_004_open_frac_of_range": {"inputs": ["open", "high", "low"], "func": clv_ext_004_open_frac_of_range},
    "clv_ext_005_clv_hl_midpoint": {"inputs": ["high", "low"], "func": clv_ext_005_clv_hl_midpoint},
    "clv_ext_006_close_vs_open_frac": {"inputs": ["close", "open", "high", "low"], "func": clv_ext_006_close_vs_open_frac},
    "clv_ext_007_clv_typical_sma21": {"inputs": ["close", "high", "low"], "func": clv_ext_007_clv_typical_sma21},
    "clv_ext_008_clv_typical_zscore_63d": {"inputs": ["close", "high", "low"], "func": clv_ext_008_clv_typical_zscore_63d},
    "clv_ext_009_clv_open_sma21": {"inputs": ["open", "high", "low"], "func": clv_ext_009_clv_open_sma21},
    "clv_ext_010_open_to_close_range_frac": {"inputs": ["close", "open", "high", "low"], "func": clv_ext_010_open_to_close_range_frac},
    "clv_ext_011_vwclv_avg_126d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_011_vwclv_avg_126d},
    "clv_ext_012_vwclv_avg_252d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_012_vwclv_avg_252d},
    "clv_ext_013_vwclv_avg_5d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_013_vwclv_avg_5d},
    "clv_ext_014_vwclv_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_014_vwclv_zscore_63d},
    "clv_ext_015_vwclv_neg_sum_63d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_015_vwclv_neg_sum_63d},
    "clv_ext_016_vwclv_pos_sum_63d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_016_vwclv_pos_sum_63d},
    "clv_ext_017_vwclv_bull_bear_ratio_63d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_017_vwclv_bull_bear_ratio_63d},
    "clv_ext_018_vwclv_vs_clv_63d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_018_vwclv_vs_clv_63d},
    "clv_ext_019_vwclv_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_019_vwclv_pct_rank_252d},
    "clv_ext_020_vwclv_slope_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_020_vwclv_slope_21d},
    "clv_ext_021_close_frac_lt_010_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_021_close_frac_lt_010_flag},
    "clv_ext_022_close_frac_lt_015_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_022_close_frac_lt_015_flag},
    "clv_ext_023_close_frac_lt_033_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_023_close_frac_lt_033_flag},
    "clv_ext_024_close_frac_gt_090_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_024_close_frac_gt_090_flag},
    "clv_ext_025_clv_lt_minus09_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_025_clv_lt_minus09_flag},
    "clv_ext_026_clv_lt_minus07_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_026_clv_lt_minus07_flag},
    "clv_ext_027_count_clv_lt_minus09_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_027_count_clv_lt_minus09_21d},
    "clv_ext_028_count_clv_lt_minus09_63d": {"inputs": ["close", "high", "low"], "func": clv_ext_028_count_clv_lt_minus09_63d},
    "clv_ext_029_count_clv_lt_minus07_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_029_count_clv_lt_minus07_21d},
    "clv_ext_030_count_close_frac_lt_010_63d": {"inputs": ["close", "high", "low"], "func": clv_ext_030_count_close_frac_lt_010_63d},
    "clv_ext_031_clv_zscore_5d": {"inputs": ["close", "high", "low"], "func": clv_ext_031_clv_zscore_5d},
    "clv_ext_032_clv_zscore_126d": {"inputs": ["close", "high", "low"], "func": clv_ext_032_clv_zscore_126d},
    "clv_ext_033_close_frac_zscore_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_033_close_frac_zscore_21d},
    "clv_ext_034_close_frac_zscore_63d": {"inputs": ["close", "high", "low"], "func": clv_ext_034_close_frac_zscore_63d},
    "clv_ext_035_clv_abs_zscore_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_035_clv_abs_zscore_21d},
    "clv_ext_036_clv_abs_zscore_63d": {"inputs": ["close", "high", "low"], "func": clv_ext_036_clv_abs_zscore_63d},
    "clv_ext_037_clv_zscore_252d_clipped": {"inputs": ["close", "high", "low"], "func": clv_ext_037_clv_zscore_252d_clipped},
    "clv_ext_038_close_frac_zscore_252d": {"inputs": ["close", "high", "low"], "func": clv_ext_038_close_frac_zscore_252d},
    "clv_ext_039_clv_iqr_63d": {"inputs": ["close", "high", "low"], "func": clv_ext_039_clv_iqr_63d},
    "clv_ext_040_clv_iqr_252d": {"inputs": ["close", "high", "low"], "func": clv_ext_040_clv_iqr_252d},
    "clv_ext_041_clv_pct_rank_5d": {"inputs": ["close", "high", "low"], "func": clv_ext_041_clv_pct_rank_5d},
    "clv_ext_042_clv_pct_rank_10d": {"inputs": ["close", "high", "low"], "func": clv_ext_042_clv_pct_rank_10d},
    "clv_ext_043_close_frac_pct_rank_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_043_close_frac_pct_rank_21d},
    "clv_ext_044_close_frac_pct_rank_5d": {"inputs": ["close", "high", "low"], "func": clv_ext_044_close_frac_pct_rank_5d},
    "clv_ext_045_clv_pct_rank_10d_expanding": {"inputs": ["close", "high", "low"], "func": clv_ext_045_clv_pct_rank_10d_expanding},
    "clv_ext_046_close_frac_pct_rank_126d": {"inputs": ["close", "high", "low"], "func": clv_ext_046_close_frac_pct_rank_126d},
    "clv_ext_047_clv_abs_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": clv_ext_047_clv_abs_pct_rank_252d},
    "clv_ext_048_clv_q10_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_048_clv_q10_21d},
    "clv_ext_049_clv_q10_63d": {"inputs": ["close", "high", "low"], "func": clv_ext_049_clv_q10_63d},
    "clv_ext_050_clv_q25_252d": {"inputs": ["close", "high", "low"], "func": clv_ext_050_clv_q25_252d},
    "clv_ext_051_clv_bear_regime_21d_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_051_clv_bear_regime_21d_flag},
    "clv_ext_052_clv_severe_bear_regime_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_052_clv_severe_bear_regime_flag},
    "clv_ext_053_clv_multi_streak_regime_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_053_clv_multi_streak_regime_flag},
    "clv_ext_054_clv_triple_bearish_flag": {"inputs": ["close", "high", "low"], "func": clv_ext_054_clv_triple_bearish_flag},
    "clv_ext_055_clv_ema10": {"inputs": ["close", "high", "low"], "func": clv_ext_055_clv_ema10},
    "clv_ext_056_clv_ema126": {"inputs": ["close", "high", "low"], "func": clv_ext_056_clv_ema126},
    "clv_ext_057_clv_sma10": {"inputs": ["close", "high", "low"], "func": clv_ext_057_clv_sma10},
    "clv_ext_058_clv_sma10_vs_sma63": {"inputs": ["close", "high", "low"], "func": clv_ext_058_clv_sma10_vs_sma63},
    "clv_ext_059_close_frac_sma5": {"inputs": ["close", "high", "low"], "func": clv_ext_059_close_frac_sma5},
    "clv_ext_060_close_frac_sma126": {"inputs": ["close", "high", "low"], "func": clv_ext_060_close_frac_sma126},
    "clv_ext_061_upper_shadow_frac": {"inputs": ["close", "high", "low"], "func": clv_ext_061_upper_shadow_frac},
    "clv_ext_062_lower_shadow_frac": {"inputs": ["close", "high", "low"], "func": clv_ext_062_lower_shadow_frac},
    "clv_ext_063_upper_shadow_sma21": {"inputs": ["close", "high", "low"], "func": clv_ext_063_upper_shadow_sma21},
    "clv_ext_064_lower_shadow_sma21": {"inputs": ["close", "high", "low"], "func": clv_ext_064_lower_shadow_sma21},
    "clv_ext_065_shadow_ratio_upper_vs_lower": {"inputs": ["close", "high", "low"], "func": clv_ext_065_shadow_ratio_upper_vs_lower},
    "clv_ext_066_shadow_ratio_sma21": {"inputs": ["close", "high", "low"], "func": clv_ext_066_shadow_ratio_sma21},
    "clv_ext_067_range_asymmetry_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_067_range_asymmetry_21d},
    "clv_ext_068_close_to_high_pct_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_068_close_to_high_pct_21d},
    "clv_ext_069_close_to_low_pct_21d": {"inputs": ["close", "high", "low"], "func": clv_ext_069_close_to_low_pct_21d},
    "clv_ext_070_hl_range_norm_sma21": {"inputs": ["close", "high", "low"], "func": clv_ext_070_hl_range_norm_sma21},
    "clv_ext_071_clv_cap_score_63d": {"inputs": ["close", "high", "low"], "func": clv_ext_071_clv_cap_score_63d},
    "clv_ext_072_clv_depth_below_minus05_sum21d": {"inputs": ["close", "high", "low"], "func": clv_ext_072_clv_depth_below_minus05_sum21d},
    "clv_ext_073_clv_depth_below_minus08_sum21d": {"inputs": ["close", "high", "low"], "func": clv_ext_073_clv_depth_below_minus08_sum21d},
    "clv_ext_074_clv_vol_interaction_bearish_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_074_clv_vol_interaction_bearish_21d},
    "clv_ext_075_clv_composite_distress_3d": {"inputs": ["close", "high", "low", "volume"], "func": clv_ext_075_clv_composite_distress_3d},
}
