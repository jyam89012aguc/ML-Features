"""
07_peak_to_trough — Extended Features 001-075
Domain: peak-to-trough ratios, swing-leg anatomy, recovery fractions —
        deeper variants: log-space ratios, ATR-normalised swings, volume-weighted
        trough levels, percentile-rank of swing depth, EWM smoothing, open/high/low
        anchored versions, cross-window comparisons, momentum of swing depth.
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
    return num / den.replace(0, np.nan)


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


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


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(_tr(close, high, low), w)


def _peak_trough_span(s: pd.Series, w: int):
    """Returns (peak, trough) rolling within window w."""
    peak   = _rolling_max(s, w)
    trough = _rolling_min(s, w)
    return peak, trough


def _recovery_fraction(close: pd.Series, peak: pd.Series, trough: pd.Series) -> pd.Series:
    span = peak - trough
    return _safe_div(close - trough, span)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Log-ratio peak-to-trough (log swing depth) ---

def ptt_ext_001_log_swing_21d(close: pd.Series) -> pd.Series:
    """Log-ratio of 21-day rolling max to 21-day rolling min (log swing depth)."""
    pk, tr = _peak_trough_span(close, _TD_MON)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_002_log_swing_63d(close: pd.Series) -> pd.Series:
    """Log-ratio of 63-day rolling max to 63-day rolling min."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_003_log_swing_126d(close: pd.Series) -> pd.Series:
    """Log-ratio of 126-day rolling max to 126-day rolling min."""
    pk, tr = _peak_trough_span(close, _TD_HALF)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_004_log_swing_252d(close: pd.Series) -> pd.Series:
    """Log-ratio of 252-day rolling max to 252-day rolling min."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_005_log_swing_504d(close: pd.Series) -> pd.Series:
    """Log-ratio of 504-day rolling max to 504-day rolling min (2yr swing)."""
    pk, tr = _peak_trough_span(close, 504)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_006_log_swing_42d(close: pd.Series) -> pd.Series:
    """Log-ratio 42-day peak to trough (2-month swing)."""
    pk, tr = _peak_trough_span(close, 42)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_007_log_swing_189d(close: pd.Series) -> pd.Series:
    """Log-ratio 189-day peak to trough (9-month swing)."""
    pk, tr = _peak_trough_span(close, 189)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_008_log_swing_378d(close: pd.Series) -> pd.Series:
    """Log-ratio 378-day peak to trough (18-month swing)."""
    pk, tr = _peak_trough_span(close, 378)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_009_log_swing_756d(close: pd.Series) -> pd.Series:
    """Log-ratio 756-day peak to trough (3-year swing)."""
    pk, tr = _peak_trough_span(close, 756)
    return _log_safe(pk) - _log_safe(tr)


def ptt_ext_010_log_swing_10d(close: pd.Series) -> pd.Series:
    """Log-ratio 10-day peak to trough (2-week micro-swing)."""
    pk, tr = _peak_trough_span(close, 10)
    return _log_safe(pk) - _log_safe(tr)


# --- Group B (011-018): ATR-normalised swing depth ---

def ptt_ext_011_atr_norm_swing_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day swing depth (max-min) normalised by 21-day ATR."""
    pk, tr = _peak_trough_span(close, _TD_MON)
    atr    = _atr(close, high, low, _TD_MON)
    return _safe_div(pk - tr, atr)


def ptt_ext_012_atr_norm_swing_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day swing depth normalised by 63-day ATR."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    atr    = _atr(close, high, low, _TD_QTR)
    return _safe_div(pk - tr, atr)


def ptt_ext_013_atr_norm_swing_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """126-day swing depth normalised by 63-day ATR."""
    pk, tr = _peak_trough_span(close, _TD_HALF)
    atr    = _atr(close, high, low, _TD_QTR)
    return _safe_div(pk - tr, atr)


def ptt_ext_014_atr_norm_swing_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day swing depth normalised by 63-day ATR."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    atr    = _atr(close, high, low, _TD_QTR)
    return _safe_div(pk - tr, atr)


def ptt_ext_015_atr_norm_swing_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """504-day swing depth normalised by 63-day ATR."""
    pk, tr = _peak_trough_span(close, 504)
    atr    = _atr(close, high, low, _TD_QTR)
    return _safe_div(pk - tr, atr)


# --- Group C (016-025): Recovery fraction variants ---

def ptt_ext_016_recovery_frac_21d(close: pd.Series) -> pd.Series:
    """Recovery fraction within 21-day swing: (close-trough)/(peak-trough)."""
    pk, tr = _peak_trough_span(close, _TD_MON)
    return _recovery_fraction(close, pk, tr)


def ptt_ext_017_recovery_frac_63d(close: pd.Series) -> pd.Series:
    """Recovery fraction within 63-day swing."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    return _recovery_fraction(close, pk, tr)


def ptt_ext_018_recovery_frac_126d(close: pd.Series) -> pd.Series:
    """Recovery fraction within 126-day swing."""
    pk, tr = _peak_trough_span(close, _TD_HALF)
    return _recovery_fraction(close, pk, tr)


def ptt_ext_019_recovery_frac_504d(close: pd.Series) -> pd.Series:
    """Recovery fraction within 504-day swing."""
    pk, tr = _peak_trough_span(close, 504)
    return _recovery_fraction(close, pk, tr)


def ptt_ext_020_recovery_frac_756d(close: pd.Series) -> pd.Series:
    """Recovery fraction within 756-day swing."""
    pk, tr = _peak_trough_span(close, 756)
    return _recovery_fraction(close, pk, tr)


def ptt_ext_021_log_recovery_frac_252d(close: pd.Series) -> pd.Series:
    """Log of recovery fraction within 252-day swing (log compress near-zero)."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr).clip(lower=_EPS, upper=1 - _EPS)
    return np.log(rf)


def ptt_ext_022_recovery_deficit_252d(close: pd.Series) -> pd.Series:
    """1 minus recovery fraction: distance remaining to peak within 252-day swing."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return 1.0 - _recovery_fraction(close, pk, tr)


def ptt_ext_023_recovery_frac_high_252d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Recovery fraction using daily HIGH instead of close (intraday recovery)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    return _recovery_fraction(high, pk, tr)


def ptt_ext_024_recovery_frac_low_252d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Recovery fraction using daily LOW (worst intraday position in swing)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    return _recovery_fraction(low, pk, tr)


def ptt_ext_025_recovery_frac_open_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Recovery fraction using daily OPEN within 252-day swing."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    return _recovery_fraction(open, pk, tr)


# --- Group D (026-034): Swing depth z-score and percentile rank ---

def ptt_ext_026_swing_depth_pctrank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d swing depth (max-min)/min over trailing 252 days."""
    pk, tr  = _peak_trough_span(close, _TD_QTR)
    depth   = _safe_div(pk - tr, tr)
    return _rolling_rank_pct(depth, _TD_YEAR)


def ptt_ext_027_swing_depth_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d swing depth over trailing 504 days."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    depth  = _safe_div(pk - tr, tr)
    return _rolling_rank_pct(depth, 504)


def ptt_ext_028_swing_depth_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 63d swing depth (max-min)/min, over 252d window."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    depth  = _safe_div(pk - tr, tr)
    return _zscore_rolling(depth, _TD_YEAR)


def ptt_ext_029_swing_depth_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 252d swing depth over 504d window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    depth  = _safe_div(pk - tr, tr)
    return _zscore_rolling(depth, 504)


def ptt_ext_030_log_swing_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of log 63d swing depth, over 252d window."""
    pk, tr    = _peak_trough_span(close, _TD_QTR)
    log_depth = _log_safe(pk) - _log_safe(tr)
    return _zscore_rolling(log_depth, _TD_YEAR)


def ptt_ext_031_log_swing_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of log 252d swing depth, over 504d window."""
    pk, tr    = _peak_trough_span(close, _TD_YEAR)
    log_depth = _log_safe(pk) - _log_safe(tr)
    return _zscore_rolling(log_depth, 504)


def ptt_ext_032_recovery_frac_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 252d recovery fraction over 252d window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf     = _recovery_fraction(close, pk, tr)
    return _zscore_rolling(rf, _TD_YEAR)


def ptt_ext_033_recovery_frac_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d recovery fraction over 252d window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf     = _recovery_fraction(close, pk, tr)
    return _rolling_rank_pct(rf, _TD_YEAR)


def ptt_ext_034_swing_to_range_ratio_21_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21d swing depth to 252d swing depth (recent vs historical range)."""
    pk21,  tr21  = _peak_trough_span(close, _TD_MON)
    pk252, tr252 = _peak_trough_span(close, _TD_YEAR)
    d21  = pk21  - tr21
    d252 = pk252 - tr252
    return _safe_div(d21, d252 + _EPS)


# --- Group E (035-044): EWM smoothed swing & recovery metrics ---

def ptt_ext_035_ewm_swing_depth_21d(close: pd.Series) -> pd.Series:
    """EWM(21)-smoothed 63d swing depth ratio."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    depth  = _safe_div(pk - tr, tr)
    return _ewm_mean(depth, _TD_MON)


def ptt_ext_036_ewm_swing_depth_63d(close: pd.Series) -> pd.Series:
    """EWM(63)-smoothed 252d swing depth ratio."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    depth  = _safe_div(pk - tr, tr)
    return _ewm_mean(depth, _TD_QTR)


def ptt_ext_037_ewm_recovery_frac_21d(close: pd.Series) -> pd.Series:
    """EWM(21)-smoothed 252d recovery fraction."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf     = _recovery_fraction(close, pk, tr)
    return _ewm_mean(rf, _TD_MON)


def ptt_ext_038_ewm_recovery_frac_63d(close: pd.Series) -> pd.Series:
    """EWM(63)-smoothed 252d recovery fraction."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf     = _recovery_fraction(close, pk, tr)
    return _ewm_mean(rf, _TD_QTR)


def ptt_ext_039_ewm_log_swing_21d(close: pd.Series) -> pd.Series:
    """EWM(21)-smoothed log 63d swing depth."""
    pk, tr    = _peak_trough_span(close, _TD_QTR)
    log_depth = _log_safe(pk) - _log_safe(tr)
    return _ewm_mean(log_depth, _TD_MON)


def ptt_ext_040_ewm_log_swing_63d(close: pd.Series) -> pd.Series:
    """EWM(63)-smoothed log 252d swing depth."""
    pk, tr    = _peak_trough_span(close, _TD_YEAR)
    log_depth = _log_safe(pk) - _log_safe(tr)
    return _ewm_mean(log_depth, _TD_QTR)


# --- Group F (041-050): Cross-window swing comparisons & ratios ---

def ptt_ext_041_swing_ratio_21_to_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21d to 63d swing depth (normalised by trough)."""
    pk21, tr21 = _peak_trough_span(close, _TD_MON)
    pk63, tr63 = _peak_trough_span(close, _TD_QTR)
    d21 = _safe_div(pk21 - tr21, tr21 + _EPS)
    d63 = _safe_div(pk63 - tr63, tr63 + _EPS)
    return _safe_div(d21, d63 + _EPS)


def ptt_ext_042_swing_ratio_63_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63d to 252d swing depth."""
    pk63,  tr63  = _peak_trough_span(close, _TD_QTR)
    pk252, tr252 = _peak_trough_span(close, _TD_YEAR)
    d63  = _safe_div(pk63  - tr63,  tr63  + _EPS)
    d252 = _safe_div(pk252 - tr252, tr252 + _EPS)
    return _safe_div(d63, d252 + _EPS)


def ptt_ext_043_swing_ratio_126_to_504d(close: pd.Series) -> pd.Series:
    """Ratio of 126d to 504d swing depth."""
    pk126, tr126 = _peak_trough_span(close, _TD_HALF)
    pk504, tr504 = _peak_trough_span(close, 504)
    d126 = _safe_div(pk126 - tr126, tr126 + _EPS)
    d504 = _safe_div(pk504 - tr504, tr504 + _EPS)
    return _safe_div(d126, d504 + _EPS)


def ptt_ext_044_recovery_frac_diff_21_252d(close: pd.Series) -> pd.Series:
    """Difference in recovery fraction: 21d minus 252d (near vs far recovery)."""
    pk21,  tr21  = _peak_trough_span(close, _TD_MON)
    pk252, tr252 = _peak_trough_span(close, _TD_YEAR)
    rf21  = _recovery_fraction(close, pk21,  tr21)
    rf252 = _recovery_fraction(close, pk252, tr252)
    return rf21 - rf252


def ptt_ext_045_recovery_frac_diff_63_252d(close: pd.Series) -> pd.Series:
    """Difference in recovery fraction: 63d minus 252d."""
    pk63,  tr63  = _peak_trough_span(close, _TD_QTR)
    pk252, tr252 = _peak_trough_span(close, _TD_YEAR)
    rf63  = _recovery_fraction(close, pk63,  tr63)
    rf252 = _recovery_fraction(close, pk252, tr252)
    return rf63 - rf252


def ptt_ext_046_swing_depth_momentum_21d(close: pd.Series) -> pd.Series:
    """21-day change in 63d swing depth (worsening/improving)."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    depth  = _safe_div(pk - tr, tr)
    return depth - depth.shift(_TD_MON)


def ptt_ext_047_swing_depth_momentum_63d(close: pd.Series) -> pd.Series:
    """63-day change in 252d swing depth."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    depth  = _safe_div(pk - tr, tr)
    return depth - depth.shift(_TD_QTR)


def ptt_ext_048_recovery_frac_momentum_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d recovery fraction (improving = recovery in progress)."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf     = _recovery_fraction(close, pk, tr)
    return rf - rf.shift(_TD_MON)


def ptt_ext_049_log_swing_ratio_short_long(close: pd.Series) -> pd.Series:
    """Log ratio of 63d swing to 252d swing (relative compression measure)."""
    pk63,  tr63  = _peak_trough_span(close, _TD_QTR)
    pk252, tr252 = _peak_trough_span(close, _TD_YEAR)
    log_s63  = _log_safe(pk63)  - _log_safe(tr63)
    log_s252 = _log_safe(pk252) - _log_safe(tr252)
    return _safe_div(log_s63, log_s252 + _EPS)


def ptt_ext_050_trough_vs_mean_252d(close: pd.Series) -> pd.Series:
    """252-day rolling trough expressed relative to 252d rolling mean."""
    tr   = _rolling_min(close, _TD_YEAR)
    mean = _rolling_mean(close, _TD_YEAR)
    return _safe_div(tr - mean, mean)


# --- Group G (051-060): Volume-weighted swing measures ---

def ptt_ext_051_vol_at_trough_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on days where close equals rolling 21d min (trough volume signature)."""
    mn     = _rolling_min(close, _TD_MON)
    at_tr  = (close <= mn + _EPS).astype(float)
    vol_tr = volume * at_tr
    return _safe_div(
        vol_tr.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum(),
        at_tr.rolling(_TD_MON,  min_periods=max(1, _TD_MON // 2)).sum()
    )


def ptt_ext_052_vol_at_trough_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on days at or near 63d rolling close min."""
    mn     = _rolling_min(close, _TD_QTR)
    at_tr  = (close <= mn * 1.01 + _EPS).astype(float)
    vol_tr = volume * at_tr
    return _safe_div(
        vol_tr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum(),
        at_tr.rolling(_TD_QTR,  min_periods=max(1, _TD_QTR // 2)).sum()
    )


def ptt_ext_053_vol_at_peak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on days at or near 252d rolling close max."""
    mx     = _rolling_max(close, _TD_YEAR)
    at_pk  = (close >= mx * 0.99).astype(float)
    vol_pk = volume * at_pk
    return _safe_div(
        vol_pk.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum(),
        at_pk.rolling(_TD_YEAR,  min_periods=max(1, _TD_YEAR // 2)).sum()
    )


def ptt_ext_054_vol_trough_vs_peak_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of trough-day volume to peak-day volume (252d): capitulation signature."""
    vt = ptt_ext_052_vol_at_trough_63d(close, volume)
    vp = ptt_ext_053_vol_at_peak_252d(close, volume)
    return _safe_div(vt, vp + _EPS)


def ptt_ext_055_vwap_swing_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 252d VWAP to 252d rolling max (VWAP position in peak-to-trough)."""
    vwap = _safe_div(
        _rolling_sum(close * volume, _TD_YEAR),
        _rolling_sum(volume, _TD_YEAR)
    )
    mx   = _rolling_max(close, _TD_YEAR)
    return _safe_div(vwap, mx + _EPS)


def ptt_ext_056_swing_depth_high_low_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252d swing depth using intraday high/low extremes: (max_high - min_low)/min_low."""
    mx = _rolling_max(high, _TD_YEAR)
    mn = _rolling_min(low,  _TD_YEAR)
    return _safe_div(mx - mn, mn)


def ptt_ext_057_swing_depth_open_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """252d swing using open as peak anchor: (max_open - min_close)/min_close."""
    mx = _rolling_max(open,  _TD_YEAR)
    mn = _rolling_min(close, _TD_YEAR)
    return _safe_div(mx - mn, mn)


def ptt_ext_058_swing_depth_log_high_low_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log-space 252d swing using intraday extremes."""
    mx = _rolling_max(high, _TD_YEAR)
    mn = _rolling_min(low,  _TD_YEAR)
    return _log_safe(mx) - _log_safe(mn)


def ptt_ext_059_recovery_frac_intraday_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recovery fraction using max_high as peak and min_low as trough (252d window)."""
    pk = _rolling_max(high, _TD_YEAR)
    tr = _rolling_min(low,  _TD_YEAR)
    return _recovery_fraction(close, pk, tr)


def ptt_ext_060_swing_depth_close_vs_intraday_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of close-based 252d swing depth to intraday-based depth (close vs range anchor)."""
    pk_c, tr_c = _peak_trough_span(close, _TD_YEAR)
    pk_h = _rolling_max(high, _TD_YEAR)
    tr_l = _rolling_min(low,  _TD_YEAR)
    d_c  = _safe_div(pk_c - tr_c, tr_c + _EPS)
    d_i  = _safe_div(pk_h - tr_l, tr_l + _EPS)
    return _safe_div(d_c, d_i + _EPS)


# --- Group H (061-075): Composite and multi-horizon features ---

def ptt_ext_061_avg_log_swing_all_windows(close: pd.Series) -> pd.Series:
    """Average log swing across 21, 63, 126, 252d windows."""
    s1 = _log_safe(_rolling_max(close, _TD_MON))  - _log_safe(_rolling_min(close, _TD_MON))
    s2 = _log_safe(_rolling_max(close, _TD_QTR))  - _log_safe(_rolling_min(close, _TD_QTR))
    s3 = _log_safe(_rolling_max(close, _TD_HALF)) - _log_safe(_rolling_min(close, _TD_HALF))
    s4 = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(_rolling_min(close, _TD_YEAR))
    return (s1 + s2 + s3 + s4) / 4.0


def ptt_ext_062_avg_recovery_frac_all_windows(close: pd.Series) -> pd.Series:
    """Average recovery fraction across 21, 63, 126, 252d swing windows."""
    rf1 = _recovery_fraction(close, *_peak_trough_span(close, _TD_MON))
    rf2 = _recovery_fraction(close, *_peak_trough_span(close, _TD_QTR))
    rf3 = _recovery_fraction(close, *_peak_trough_span(close, _TD_HALF))
    rf4 = _recovery_fraction(close, *_peak_trough_span(close, _TD_YEAR))
    return (rf1 + rf2 + rf3 + rf4) / 4.0


def ptt_ext_063_min_recovery_frac_all_windows(close: pd.Series) -> pd.Series:
    """Minimum (worst) recovery fraction across 21, 63, 126, 252d windows."""
    rf1 = _recovery_fraction(close, *_peak_trough_span(close, _TD_MON))
    rf2 = _recovery_fraction(close, *_peak_trough_span(close, _TD_QTR))
    rf3 = _recovery_fraction(close, *_peak_trough_span(close, _TD_HALF))
    rf4 = _recovery_fraction(close, *_peak_trough_span(close, _TD_YEAR))
    return pd.concat([rf1, rf2, rf3, rf4], axis=1).min(axis=1)


def ptt_ext_064_swing_depth_rolling_std_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of 21d swing depth (volatility of swing size)."""
    pk, tr = _peak_trough_span(close, _TD_MON)
    depth  = _safe_div(pk - tr, tr)
    return _rolling_std(depth, _TD_QTR)


def ptt_ext_065_swing_depth_rolling_std_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d std of 63d swing depth."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    depth  = _safe_div(pk - tr, tr)
    return _rolling_std(depth, _TD_YEAR)


def ptt_ext_066_trough_below_252d_trough_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current close equals 252-day rolling minimum (at multi-year trough)."""
    tr252 = _rolling_min(close, _TD_YEAR)
    return (close <= tr252 + _EPS).astype(float)


def ptt_ext_067_trough_below_504d_trough_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close equals 504-day rolling minimum (2-year depth)."""
    tr504 = _rolling_min(close, 504)
    return (close <= tr504 + _EPS).astype(float)


def ptt_ext_068_swing_depth_ewm_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EWM(21)-smoothed 252d swing depth over 252d window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    depth  = _safe_div(pk - tr, tr)
    sm     = _ewm_mean(depth, _TD_MON)
    return _zscore_rolling(sm, _TD_YEAR)


def ptt_ext_069_trough_pct_above_252d_open_min(open: pd.Series, close: pd.Series) -> pd.Series:
    """252d rolling close min expressed as pct above 252d rolling open min."""
    mn_c = _rolling_min(close, _TD_YEAR)
    mn_o = _rolling_min(open,  _TD_YEAR)
    return _safe_div(mn_c - mn_o, mn_o)


def ptt_ext_070_log_swing_rolling_mean_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of daily log-return magnitude (average |log-ret|)."""
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    return _rolling_mean(log_ret.abs(), _TD_QTR)


def ptt_ext_071_swing_cum_loss_to_trough_252d(close: pd.Series) -> pd.Series:
    """Cumulative log-return from 252d rolling peak to current (total decline)."""
    pk = _rolling_max(close, _TD_YEAR)
    return _log_safe(close) - _log_safe(pk)


def ptt_ext_072_swing_cum_gain_from_trough_252d(close: pd.Series) -> pd.Series:
    """Cumulative log-return from 252d rolling trough to current (total bounce)."""
    tr = _rolling_min(close, _TD_YEAR)
    return _log_safe(close) - _log_safe(tr)


def ptt_ext_073_swing_ratio_252d_vs_std(close: pd.Series) -> pd.Series:
    """252d swing depth (log) normalised by 252d std of log-returns."""
    pk, tr    = _peak_trough_span(close, _TD_YEAR)
    log_depth = _log_safe(pk) - _log_safe(tr)
    log_ret   = _log_safe(close) - _log_safe(close.shift(1))
    sd        = _rolling_std(log_ret, _TD_YEAR)
    return _safe_div(log_depth, sd + _EPS)


def ptt_ext_074_recovery_frac_change_63d(close: pd.Series) -> pd.Series:
    """63-day change in 252d recovery fraction (trend of recovery)."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf     = _recovery_fraction(close, pk, tr)
    return rf - rf.shift(_TD_QTR)


def ptt_ext_075_peak_decay_rate_252d(close: pd.Series) -> pd.Series:
    """Rate at which the 252d rolling peak is declining: (peak - peak.shift(21))/peak."""
    pk = _rolling_max(close, _TD_YEAR)
    return _safe_div(pk - pk.shift(_TD_MON), pk.shift(_TD_MON))


# ── Registry ──────────────────────────────────────────────────────────────────

PEAK_TO_TROUGH_EXTENDED_REGISTRY_001_075 = {
    "ptt_ext_001_log_swing_21d":                  {"inputs": ["close"],                      "func": ptt_ext_001_log_swing_21d},
    "ptt_ext_002_log_swing_63d":                  {"inputs": ["close"],                      "func": ptt_ext_002_log_swing_63d},
    "ptt_ext_003_log_swing_126d":                 {"inputs": ["close"],                      "func": ptt_ext_003_log_swing_126d},
    "ptt_ext_004_log_swing_252d":                 {"inputs": ["close"],                      "func": ptt_ext_004_log_swing_252d},
    "ptt_ext_005_log_swing_504d":                 {"inputs": ["close"],                      "func": ptt_ext_005_log_swing_504d},
    "ptt_ext_006_log_swing_42d":                  {"inputs": ["close"],                      "func": ptt_ext_006_log_swing_42d},
    "ptt_ext_007_log_swing_189d":                 {"inputs": ["close"],                      "func": ptt_ext_007_log_swing_189d},
    "ptt_ext_008_log_swing_378d":                 {"inputs": ["close"],                      "func": ptt_ext_008_log_swing_378d},
    "ptt_ext_009_log_swing_756d":                 {"inputs": ["close"],                      "func": ptt_ext_009_log_swing_756d},
    "ptt_ext_010_log_swing_10d":                  {"inputs": ["close"],                      "func": ptt_ext_010_log_swing_10d},
    "ptt_ext_011_atr_norm_swing_21d":             {"inputs": ["close", "high", "low"],       "func": ptt_ext_011_atr_norm_swing_21d},
    "ptt_ext_012_atr_norm_swing_63d":             {"inputs": ["close", "high", "low"],       "func": ptt_ext_012_atr_norm_swing_63d},
    "ptt_ext_013_atr_norm_swing_126d":            {"inputs": ["close", "high", "low"],       "func": ptt_ext_013_atr_norm_swing_126d},
    "ptt_ext_014_atr_norm_swing_252d":            {"inputs": ["close", "high", "low"],       "func": ptt_ext_014_atr_norm_swing_252d},
    "ptt_ext_015_atr_norm_swing_504d":            {"inputs": ["close", "high", "low"],       "func": ptt_ext_015_atr_norm_swing_504d},
    "ptt_ext_016_recovery_frac_21d":              {"inputs": ["close"],                      "func": ptt_ext_016_recovery_frac_21d},
    "ptt_ext_017_recovery_frac_63d":              {"inputs": ["close"],                      "func": ptt_ext_017_recovery_frac_63d},
    "ptt_ext_018_recovery_frac_126d":             {"inputs": ["close"],                      "func": ptt_ext_018_recovery_frac_126d},
    "ptt_ext_019_recovery_frac_504d":             {"inputs": ["close"],                      "func": ptt_ext_019_recovery_frac_504d},
    "ptt_ext_020_recovery_frac_756d":             {"inputs": ["close"],                      "func": ptt_ext_020_recovery_frac_756d},
    "ptt_ext_021_log_recovery_frac_252d":         {"inputs": ["close"],                      "func": ptt_ext_021_log_recovery_frac_252d},
    "ptt_ext_022_recovery_deficit_252d":          {"inputs": ["close"],                      "func": ptt_ext_022_recovery_deficit_252d},
    "ptt_ext_023_recovery_frac_high_252d":        {"inputs": ["high", "close"],              "func": ptt_ext_023_recovery_frac_high_252d},
    "ptt_ext_024_recovery_frac_low_252d":         {"inputs": ["low", "close"],               "func": ptt_ext_024_recovery_frac_low_252d},
    "ptt_ext_025_recovery_frac_open_252d":        {"inputs": ["open", "close"],              "func": ptt_ext_025_recovery_frac_open_252d},
    "ptt_ext_026_swing_depth_pctrank_63d":        {"inputs": ["close"],                      "func": ptt_ext_026_swing_depth_pctrank_63d},
    "ptt_ext_027_swing_depth_pctrank_252d":       {"inputs": ["close"],                      "func": ptt_ext_027_swing_depth_pctrank_252d},
    "ptt_ext_028_swing_depth_zscore_63d":         {"inputs": ["close"],                      "func": ptt_ext_028_swing_depth_zscore_63d},
    "ptt_ext_029_swing_depth_zscore_252d":        {"inputs": ["close"],                      "func": ptt_ext_029_swing_depth_zscore_252d},
    "ptt_ext_030_log_swing_zscore_63d":           {"inputs": ["close"],                      "func": ptt_ext_030_log_swing_zscore_63d},
    "ptt_ext_031_log_swing_zscore_252d":          {"inputs": ["close"],                      "func": ptt_ext_031_log_swing_zscore_252d},
    "ptt_ext_032_recovery_frac_zscore_252d":      {"inputs": ["close"],                      "func": ptt_ext_032_recovery_frac_zscore_252d},
    "ptt_ext_033_recovery_frac_pctrank_252d":     {"inputs": ["close"],                      "func": ptt_ext_033_recovery_frac_pctrank_252d},
    "ptt_ext_034_swing_to_range_ratio_21_252d":   {"inputs": ["close"],                      "func": ptt_ext_034_swing_to_range_ratio_21_252d},
    "ptt_ext_035_ewm_swing_depth_21d":            {"inputs": ["close"],                      "func": ptt_ext_035_ewm_swing_depth_21d},
    "ptt_ext_036_ewm_swing_depth_63d":            {"inputs": ["close"],                      "func": ptt_ext_036_ewm_swing_depth_63d},
    "ptt_ext_037_ewm_recovery_frac_21d":          {"inputs": ["close"],                      "func": ptt_ext_037_ewm_recovery_frac_21d},
    "ptt_ext_038_ewm_recovery_frac_63d":          {"inputs": ["close"],                      "func": ptt_ext_038_ewm_recovery_frac_63d},
    "ptt_ext_039_ewm_log_swing_21d":              {"inputs": ["close"],                      "func": ptt_ext_039_ewm_log_swing_21d},
    "ptt_ext_040_ewm_log_swing_63d":              {"inputs": ["close"],                      "func": ptt_ext_040_ewm_log_swing_63d},
    "ptt_ext_041_swing_ratio_21_to_63d":          {"inputs": ["close"],                      "func": ptt_ext_041_swing_ratio_21_to_63d},
    "ptt_ext_042_swing_ratio_63_to_252d":         {"inputs": ["close"],                      "func": ptt_ext_042_swing_ratio_63_to_252d},
    "ptt_ext_043_swing_ratio_126_to_504d":        {"inputs": ["close"],                      "func": ptt_ext_043_swing_ratio_126_to_504d},
    "ptt_ext_044_recovery_frac_diff_21_252d":     {"inputs": ["close"],                      "func": ptt_ext_044_recovery_frac_diff_21_252d},
    "ptt_ext_045_recovery_frac_diff_63_252d":     {"inputs": ["close"],                      "func": ptt_ext_045_recovery_frac_diff_63_252d},
    "ptt_ext_046_swing_depth_momentum_21d":       {"inputs": ["close"],                      "func": ptt_ext_046_swing_depth_momentum_21d},
    "ptt_ext_047_swing_depth_momentum_63d":       {"inputs": ["close"],                      "func": ptt_ext_047_swing_depth_momentum_63d},
    "ptt_ext_048_recovery_frac_momentum_21d":     {"inputs": ["close"],                      "func": ptt_ext_048_recovery_frac_momentum_21d},
    "ptt_ext_049_log_swing_ratio_short_long":     {"inputs": ["close"],                      "func": ptt_ext_049_log_swing_ratio_short_long},
    "ptt_ext_050_trough_vs_mean_252d":            {"inputs": ["close"],                      "func": ptt_ext_050_trough_vs_mean_252d},
    "ptt_ext_051_vol_at_trough_21d":              {"inputs": ["close", "volume"],            "func": ptt_ext_051_vol_at_trough_21d},
    "ptt_ext_052_vol_at_trough_63d":              {"inputs": ["close", "volume"],            "func": ptt_ext_052_vol_at_trough_63d},
    "ptt_ext_053_vol_at_peak_252d":               {"inputs": ["close", "volume"],            "func": ptt_ext_053_vol_at_peak_252d},
    "ptt_ext_054_vol_trough_vs_peak_ratio_252d":  {"inputs": ["close", "volume"],            "func": ptt_ext_054_vol_trough_vs_peak_ratio_252d},
    "ptt_ext_055_vwap_swing_ratio_252d":          {"inputs": ["close", "volume"],            "func": ptt_ext_055_vwap_swing_ratio_252d},
    "ptt_ext_056_swing_depth_high_low_252d":      {"inputs": ["high", "low"],                "func": ptt_ext_056_swing_depth_high_low_252d},
    "ptt_ext_057_swing_depth_open_252d":          {"inputs": ["open", "close"],              "func": ptt_ext_057_swing_depth_open_252d},
    "ptt_ext_058_swing_depth_log_high_low_252d":  {"inputs": ["high", "low"],                "func": ptt_ext_058_swing_depth_log_high_low_252d},
    "ptt_ext_059_recovery_frac_intraday_252d":    {"inputs": ["high", "low", "close"],       "func": ptt_ext_059_recovery_frac_intraday_252d},
    "ptt_ext_060_swing_depth_close_vs_intraday_252d": {"inputs": ["close", "high", "low"],  "func": ptt_ext_060_swing_depth_close_vs_intraday_252d},
    "ptt_ext_061_avg_log_swing_all_windows":      {"inputs": ["close"],                      "func": ptt_ext_061_avg_log_swing_all_windows},
    "ptt_ext_062_avg_recovery_frac_all_windows":  {"inputs": ["close"],                      "func": ptt_ext_062_avg_recovery_frac_all_windows},
    "ptt_ext_063_min_recovery_frac_all_windows":  {"inputs": ["close"],                      "func": ptt_ext_063_min_recovery_frac_all_windows},
    "ptt_ext_064_swing_depth_rolling_std_63d":    {"inputs": ["close"],                      "func": ptt_ext_064_swing_depth_rolling_std_63d},
    "ptt_ext_065_swing_depth_rolling_std_252d":   {"inputs": ["close"],                      "func": ptt_ext_065_swing_depth_rolling_std_252d},
    "ptt_ext_066_trough_below_252d_trough_flag":  {"inputs": ["close"],                      "func": ptt_ext_066_trough_below_252d_trough_flag},
    "ptt_ext_067_trough_below_504d_trough_flag":  {"inputs": ["close"],                      "func": ptt_ext_067_trough_below_504d_trough_flag},
    "ptt_ext_068_swing_depth_ewm_zscore_252d":    {"inputs": ["close"],                      "func": ptt_ext_068_swing_depth_ewm_zscore_252d},
    "ptt_ext_069_trough_pct_above_252d_open_min": {"inputs": ["open", "close"],              "func": ptt_ext_069_trough_pct_above_252d_open_min},
    "ptt_ext_070_log_swing_rolling_mean_63d":     {"inputs": ["close"],                      "func": ptt_ext_070_log_swing_rolling_mean_63d},
    "ptt_ext_071_swing_cum_loss_to_trough_252d":  {"inputs": ["close"],                      "func": ptt_ext_071_swing_cum_loss_to_trough_252d},
    "ptt_ext_072_swing_cum_gain_from_trough_252d":{"inputs": ["close"],                      "func": ptt_ext_072_swing_cum_gain_from_trough_252d},
    "ptt_ext_073_swing_ratio_252d_vs_std":        {"inputs": ["close"],                      "func": ptt_ext_073_swing_ratio_252d_vs_std},
    "ptt_ext_074_recovery_frac_change_63d":       {"inputs": ["close"],                      "func": ptt_ext_074_recovery_frac_change_63d},
    "ptt_ext_075_peak_decay_rate_252d":           {"inputs": ["close"],                      "func": ptt_ext_075_peak_decay_rate_252d},
}
