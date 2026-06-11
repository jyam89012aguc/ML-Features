"""short_interest_buildup_trajectory base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py. Hypotheses cover: SI vs N-period high, persistence
counts of consecutive rising periods, surge events, SI volatility, SI-vs-price divergence,
SI vs ADV ratios, and vol-normalized SI buildup. PIT-clean throughout.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 3, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()


def _rolling_max(s, w, mp=None):
    if mp is None:
        mp = max(w // 3, 2)
    return s.rolling(w, min_periods=mp).max()


def _rolling_min(s, w, mp=None):
    if mp is None:
        mp = max(w // 3, 2)
    return s.rolling(w, min_periods=mp).min()


def _pct_change(s, n):
    return _safe_div(s - s.shift(n), s.shift(n).abs())


# ============================================================
#                    FEATURES 076-150
# ============================================================

# ---- Block F: SI vs N-period HIGH / max-since-snap (076-090) ----

def f25_sibt_076_shortinterest_to_63d_high(shortinterest):
    return _safe_div(shortinterest, _rolling_max(shortinterest, 63, mp=10))


def f25_sibt_077_shortinterest_to_126d_high(shortinterest):
    return _safe_div(shortinterest, _rolling_max(shortinterest, 126, mp=20))


def f25_sibt_078_shortinterest_to_252d_high(shortinterest):
    return _safe_div(shortinterest, _rolling_max(shortinterest, 252, mp=42))


def f25_sibt_079_shortinterest_distance_to_252d_high(shortinterest):
    return shortinterest - _rolling_max(shortinterest, 252, mp=42)


def f25_sibt_080_shortinterest_distance_to_252d_low(shortinterest):
    return shortinterest - _rolling_min(shortinterest, 252, mp=42)


def f25_sibt_081_shortinterest_range_position_252d(shortinterest):
    hi = _rolling_max(shortinterest, 252, mp=42)
    lo = _rolling_min(shortinterest, 252, mp=42)
    return _safe_div(shortinterest - lo, hi - lo)


def f25_sibt_082_shortinterest_range_position_126d(shortinterest):
    hi = _rolling_max(shortinterest, 126, mp=20)
    lo = _rolling_min(shortinterest, 126, mp=20)
    return _safe_div(shortinterest - lo, hi - lo)


def f25_sibt_083_daystocover_range_position_252d(daystocover):
    hi = _rolling_max(daystocover, 252, mp=42)
    lo = _rolling_min(daystocover, 252, mp=42)
    return _safe_div(daystocover - lo, hi - lo)


def f25_sibt_084_shortpctfloat_range_position_252d(shortpctfloat):
    hi = _rolling_max(shortpctfloat, 252, mp=42)
    lo = _rolling_min(shortpctfloat, 252, mp=42)
    return _safe_div(shortpctfloat - lo, hi - lo)


def f25_sibt_085_shortinterest_at_new_252d_high_indicator(shortinterest):
    hi = _rolling_max(shortinterest, 252, mp=42)
    flag = (shortinterest >= hi).astype(float)
    return flag.where(shortinterest.notna(), np.nan)


def f25_sibt_086_shortpctfloat_at_new_252d_high_indicator(shortpctfloat):
    hi = _rolling_max(shortpctfloat, 252, mp=42)
    flag = (shortpctfloat >= hi).astype(float)
    return flag.where(shortpctfloat.notna(), np.nan)


def f25_sibt_087_daystocover_at_new_252d_high_indicator(daystocover):
    hi = _rolling_max(daystocover, 252, mp=42)
    flag = (daystocover >= hi).astype(float)
    return flag.where(daystocover.notna(), np.nan)


def f25_sibt_088_si_log_drawdown_from_252d_high(shortinterest):
    hi = _rolling_max(shortinterest, 252, mp=42)
    return _safe_log(shortinterest) - _safe_log(hi)


def f25_sibt_089_si_log_rally_from_252d_low(shortinterest):
    lo = _rolling_min(shortinterest, 252, mp=42)
    return _safe_log(shortinterest) - _safe_log(lo)


def f25_sibt_090_si_252d_high_minus_low_log_range(shortinterest):
    return _safe_log(_rolling_max(shortinterest, 252, mp=42)) - _safe_log(_rolling_min(shortinterest, 252, mp=42))


# ---- Block G: SI rate-of-change z-scores & persistence (091-105) ----

def f25_sibt_091_si_pct_chg21_zscore_252d(shortinterest):
    return _rolling_zscore(_pct_change(shortinterest, 21), 252)


def f25_sibt_092_si_pct_chg63_zscore_252d(shortinterest):
    return _rolling_zscore(_pct_change(shortinterest, 63), 252)


def f25_sibt_093_spf_chg63_zscore_252d(shortpctfloat):
    return _rolling_zscore(shortpctfloat - shortpctfloat.shift(63), 252)


def f25_sibt_094_dtc_chg63_zscore_252d(daystocover):
    return _rolling_zscore(daystocover - daystocover.shift(63), 252)


def f25_sibt_095_si_rising_persistence_63d(shortinterest):
    rising = (shortinterest > shortinterest.shift(21)).astype(float)
    return rising.rolling(63, min_periods=10).sum()


def f25_sibt_096_spf_rising_persistence_63d(shortpctfloat):
    rising = (shortpctfloat > shortpctfloat.shift(21)).astype(float)
    return rising.rolling(63, min_periods=10).sum()


def f25_sibt_097_dtc_rising_persistence_63d(daystocover):
    rising = (daystocover > daystocover.shift(21)).astype(float)
    return rising.rolling(63, min_periods=10).sum()


def f25_sibt_098_si_rising_persistence_126d(shortinterest):
    rising = (shortinterest > shortinterest.shift(21)).astype(float)
    return rising.rolling(126, min_periods=20).sum()


def f25_sibt_099_si_strictly_higher_streak_63d(shortinterest):
    rising = (shortinterest.diff(21) > 0).astype(float)
    return rising.rolling(63, min_periods=10).mean()


def f25_sibt_100_spf_strictly_higher_streak_126d(shortpctfloat):
    rising = (shortpctfloat.diff(21) > 0).astype(float)
    return rising.rolling(126, min_periods=20).mean()


def f25_sibt_101_si_above_ema63_persistence(shortinterest):
    e63 = _ema(shortinterest, 63, min_periods=10)
    above = (shortinterest > e63).astype(float)
    return above.rolling(126, min_periods=20).mean()


def f25_sibt_102_spf_above_ema63_persistence(shortpctfloat):
    e63 = _ema(shortpctfloat, 63, min_periods=10)
    above = (shortpctfloat > e63).astype(float)
    return above.rolling(126, min_periods=20).mean()


def f25_sibt_103_dtc_above_ema63_persistence(daystocover):
    e63 = _ema(daystocover, 63, min_periods=10)
    above = (daystocover > e63).astype(float)
    return above.rolling(126, min_periods=20).mean()


def f25_sibt_104_si_log_slope_63d(shortinterest):
    log_si = _safe_log(shortinterest)
    return (log_si - log_si.shift(63)) / 63.0


def f25_sibt_105_si_log_slope_252d(shortinterest):
    log_si = _safe_log(shortinterest)
    return (log_si - log_si.shift(252)) / 252.0


# ---- Block H: SI volatility, surge events, threshold crossings (106-120) ----

def f25_sibt_106_si_log_change_realized_vol_63d(shortinterest):
    return _safe_log(shortinterest).diff().rolling(63, min_periods=10).std()


def f25_sibt_107_si_log_change_realized_vol_126d(shortinterest):
    return _safe_log(shortinterest).diff().rolling(126, min_periods=20).std()


def f25_sibt_108_spf_realized_vol_63d(shortpctfloat):
    return shortpctfloat.diff().rolling(63, min_periods=10).std()


def f25_sibt_109_dtc_realized_vol_63d(daystocover):
    return daystocover.diff().rolling(63, min_periods=10).std()


def f25_sibt_110_si_surge_25pct_in_21d_indicator(shortinterest):
    chg = _pct_change(shortinterest, 21)
    flag = (chg > 0.25).astype(float)
    return flag.where(chg.notna(), np.nan)


def f25_sibt_111_si_surge_50pct_in_63d_indicator(shortinterest):
    chg = _pct_change(shortinterest, 63)
    flag = (chg > 0.50).astype(float)
    return flag.where(chg.notna(), np.nan)


def f25_sibt_112_si_doubled_in_126d_indicator(shortinterest):
    chg = _pct_change(shortinterest, 126)
    flag = (chg > 1.0).astype(float)
    return flag.where(chg.notna(), np.nan)


def f25_sibt_113_spf_jumped_5pp_in_63d_indicator(shortpctfloat):
    chg = shortpctfloat - shortpctfloat.shift(63)
    flag = (chg > 5.0).astype(float)
    return flag.where(chg.notna(), np.nan)


def f25_sibt_114_dtc_jumped_2x_in_63d_indicator(daystocover):
    chg = _pct_change(daystocover, 63)
    flag = (chg > 1.0).astype(float)
    return flag.where(chg.notna(), np.nan)


def f25_sibt_115_si_crossed_above_252d_median_recently(shortinterest):
    med = shortinterest.rolling(252, min_periods=42).median()
    above_now = shortinterest > med
    above_prev = shortinterest.shift(21) > med.shift(21)
    cross = (above_now & ~above_prev).astype(float)
    return cross.where(shortinterest.notna() & med.notna(), np.nan)


def f25_sibt_116_spf_crossed_above_10_recently(shortpctfloat):
    above_now = shortpctfloat > 10.0
    above_prev = shortpctfloat.shift(21) > 10.0
    cross = (above_now & ~above_prev).astype(float)
    return cross.where(shortpctfloat.notna() & shortpctfloat.shift(21).notna(), np.nan)


def f25_sibt_117_si_vol_normalized_chg63(shortinterest):
    chg = _pct_change(shortinterest, 63)
    vol = _safe_log(shortinterest).diff().rolling(63, min_periods=10).std()
    return _safe_div(chg, vol)


def f25_sibt_118_spf_vol_normalized_chg63(shortpctfloat):
    chg = shortpctfloat - shortpctfloat.shift(63)
    vol = shortpctfloat.diff().rolling(63, min_periods=10).std()
    return _safe_div(chg, vol)


def f25_sibt_119_dtc_vol_normalized_chg63(daystocover):
    chg = daystocover - daystocover.shift(63)
    vol = daystocover.diff().rolling(63, min_periods=10).std()
    return _safe_div(chg, vol)


def f25_sibt_120_si_log_chg_skew_126d(shortinterest):
    return _safe_log(shortinterest).diff().rolling(126, min_periods=20).skew()


# ---- Block I: SI vs PRICE divergence (cross-feature) (121-135) ----

def f25_sibt_121_si_pct_chg63_minus_price_pct_chg63(shortinterest, close):
    return _pct_change(shortinterest, 63) - _pct_change(close, 63)


def f25_sibt_122_spf_chg63_times_price_chg63(shortpctfloat, close):
    return (shortpctfloat - shortpctfloat.shift(63)) * _pct_change(close, 63)


def f25_sibt_123_si_rising_while_price_rising_indicator(shortinterest, close):
    si_rising = (_pct_change(shortinterest, 63) > 0)
    px_rising = (_pct_change(close, 63) > 0)
    flag = (si_rising & px_rising).astype(float)
    valid = shortinterest.notna() & close.notna()
    return flag.where(valid, np.nan)


def f25_sibt_124_si_rising_while_price_near_252d_high_indicator(shortinterest, close):
    si_rising = (_pct_change(shortinterest, 63) > 0)
    near_hi = (_safe_div(close, _rolling_max(close, 252, mp=42)) > 0.95)
    flag = (si_rising & near_hi).astype(float)
    valid = shortinterest.notna() & close.notna()
    return flag.where(valid, np.nan)


def f25_sibt_125_si_zscore_minus_price_zscore_63d(shortinterest, close):
    return _rolling_zscore(_safe_log(shortinterest), 63) - _rolling_zscore(_safe_log(close), 63)


def f25_sibt_126_si_zscore_minus_price_zscore_126d(shortinterest, close):
    return _rolling_zscore(_safe_log(shortinterest), 126) - _rolling_zscore(_safe_log(close), 126)


def f25_sibt_127_spf_chg63_div_price_chg63(shortpctfloat, close):
    return _safe_div(shortpctfloat - shortpctfloat.shift(63), _pct_change(close, 63))


def f25_sibt_128_dtc_chg63_div_price_chg63(daystocover, close):
    return _safe_div(daystocover - daystocover.shift(63), _pct_change(close, 63))


def f25_sibt_129_si_log_chg63_times_price_log_chg63(shortinterest, close):
    return (_safe_log(shortinterest) - _safe_log(shortinterest.shift(63))) * (_safe_log(close) - _safe_log(close.shift(63)))


def f25_sibt_130_spf_chg126_with_positive_price_chg126(shortpctfloat, close):
    spf_chg = shortpctfloat - shortpctfloat.shift(126)
    px_chg = _pct_change(close, 126)
    return spf_chg.where(px_chg > 0, np.nan)


def f25_sibt_131_si_buildup_during_price_uptrend_persistence(shortinterest, close):
    si_rising = (shortinterest.diff(21) > 0)
    px_rising = (close > close.rolling(126, min_periods=20).mean())
    both = (si_rising & px_rising).astype(float)
    return both.rolling(63, min_periods=10).mean()


def f25_sibt_132_si_pct_chg63_when_price_above_ema63(shortinterest, close):
    e63 = _ema(close, 63, min_periods=10)
    chg = _pct_change(shortinterest, 63)
    return chg.where(close > e63, np.nan)


def f25_sibt_133_si_to_market_cap_proxy(shortinterest, close, sharesbas):
    mc = close * sharesbas
    return _safe_div(shortinterest * close, mc)


def f25_sibt_134_si_dollar_value_log(shortinterest, close):
    return _safe_log(shortinterest * close)


def f25_sibt_135_si_dollar_value_pct_chg63(shortinterest, close):
    return _pct_change(shortinterest * close, 63)


# ---- Block J: SI vs ADV / volume-based & regime shifts (136-150) ----

def f25_sibt_136_shortinterest_to_adv_21d(shortinterest, volume):
    adv21 = volume.rolling(21, min_periods=5).mean()
    return _safe_div(shortinterest, adv21)


def f25_sibt_137_shortinterest_to_adv_63d(shortinterest, volume):
    adv63 = volume.rolling(63, min_periods=10).mean()
    return _safe_div(shortinterest, adv63)


def f25_sibt_138_shortinterest_to_adv_252d(shortinterest, volume):
    adv252 = volume.rolling(252, min_periods=42).mean()
    return _safe_div(shortinterest, adv252)


def f25_sibt_139_si_to_adv_chg63(shortinterest, volume):
    adv63 = volume.rolling(63, min_periods=10).mean()
    ratio = _safe_div(shortinterest, adv63)
    return ratio - ratio.shift(63)


def f25_sibt_140_dtc_minus_si_to_adv_gap(daystocover, shortinterest, volume):
    adv63 = volume.rolling(63, min_periods=10).mean()
    return daystocover - _safe_div(shortinterest, adv63)


def f25_sibt_141_si_normalized_by_252d_adv_chg126(shortinterest, volume):
    adv252 = volume.rolling(252, min_periods=42).mean()
    ratio = _safe_div(shortinterest, adv252)
    return ratio - ratio.shift(126)


def f25_sibt_142_dtc_regime_shift_short_vs_long(daystocover):
    short = daystocover.rolling(21, min_periods=5).mean()
    long = daystocover.rolling(126, min_periods=20).mean()
    return _safe_div(short - long, long.abs())


def f25_sibt_143_si_regime_shift_short_vs_long(shortinterest):
    short = _safe_log(shortinterest).rolling(21, min_periods=5).mean()
    long = _safe_log(shortinterest).rolling(126, min_periods=20).mean()
    return short - long


def f25_sibt_144_spf_regime_shift_short_vs_long(shortpctfloat):
    short = shortpctfloat.rolling(21, min_periods=5).mean()
    long = shortpctfloat.rolling(126, min_periods=20).mean()
    return short - long


def f25_sibt_145_si_chg63_normalized_by_price_realized_vol(shortinterest, close):
    si_chg = _pct_change(shortinterest, 63)
    px_vol = _safe_log(close).diff().rolling(63, min_periods=10).std()
    return _safe_div(si_chg, px_vol)


def f25_sibt_146_dtc_chg63_normalized_by_price_realized_vol(daystocover, close):
    dtc_chg = daystocover - daystocover.shift(63)
    px_vol = _safe_log(close).diff().rolling(63, min_periods=10).std()
    return _safe_div(dtc_chg, px_vol)


def f25_sibt_147_si_buildup_index_compound_63d(shortinterest, shortpctfloat, daystocover):
    si_chg = _pct_change(shortinterest, 63)
    spf_chg = shortpctfloat - shortpctfloat.shift(63)
    dtc_chg = daystocover - daystocover.shift(63)
    return si_chg + 0.01 * spf_chg + 0.1 * dtc_chg


def f25_sibt_148_si_buildup_breadth_indicator(shortinterest, shortpctfloat, daystocover):
    si_up = (_pct_change(shortinterest, 63) > 0).astype(float)
    spf_up = ((shortpctfloat - shortpctfloat.shift(63)) > 0).astype(float)
    dtc_up = ((daystocover - daystocover.shift(63)) > 0).astype(float)
    breadth = si_up + spf_up + dtc_up
    valid = shortinterest.notna() & shortpctfloat.notna() & daystocover.notna()
    return breadth.where(valid, np.nan)


def f25_sibt_149_si_buildup_trend_strength_signed(shortinterest):
    log_si = _safe_log(shortinterest)
    slope = (log_si - log_si.shift(126)) / 126.0
    vol = log_si.diff().rolling(126, min_periods=20).std()
    return _safe_div(slope, vol)


def f25_sibt_150_compound_buildup_trajectory_score(shortinterest, daystocover, shortpctfloat, close):
    si_z = _rolling_zscore(_safe_log(shortinterest), 126)
    dtc_z = _rolling_zscore(daystocover, 126)
    spf_z = _rolling_zscore(shortpctfloat, 126)
    px_z = _rolling_zscore(_safe_log(close), 126)
    return si_z + dtc_z + spf_z - 0.5 * px_z


# ============================================================
#                        REGISTRY
# ============================================================

SHORT_INTEREST_BUILDUP_TRAJECTORY_BASE_REGISTRY_076_150 = {
    "f25_sibt_076_shortinterest_to_63d_high": {"inputs": ["shortinterest"], "func": f25_sibt_076_shortinterest_to_63d_high},
    "f25_sibt_077_shortinterest_to_126d_high": {"inputs": ["shortinterest"], "func": f25_sibt_077_shortinterest_to_126d_high},
    "f25_sibt_078_shortinterest_to_252d_high": {"inputs": ["shortinterest"], "func": f25_sibt_078_shortinterest_to_252d_high},
    "f25_sibt_079_shortinterest_distance_to_252d_high": {"inputs": ["shortinterest"], "func": f25_sibt_079_shortinterest_distance_to_252d_high},
    "f25_sibt_080_shortinterest_distance_to_252d_low": {"inputs": ["shortinterest"], "func": f25_sibt_080_shortinterest_distance_to_252d_low},
    "f25_sibt_081_shortinterest_range_position_252d": {"inputs": ["shortinterest"], "func": f25_sibt_081_shortinterest_range_position_252d},
    "f25_sibt_082_shortinterest_range_position_126d": {"inputs": ["shortinterest"], "func": f25_sibt_082_shortinterest_range_position_126d},
    "f25_sibt_083_daystocover_range_position_252d": {"inputs": ["daystocover"], "func": f25_sibt_083_daystocover_range_position_252d},
    "f25_sibt_084_shortpctfloat_range_position_252d": {"inputs": ["shortpctfloat"], "func": f25_sibt_084_shortpctfloat_range_position_252d},
    "f25_sibt_085_shortinterest_at_new_252d_high_indicator": {"inputs": ["shortinterest"], "func": f25_sibt_085_shortinterest_at_new_252d_high_indicator},
    "f25_sibt_086_shortpctfloat_at_new_252d_high_indicator": {"inputs": ["shortpctfloat"], "func": f25_sibt_086_shortpctfloat_at_new_252d_high_indicator},
    "f25_sibt_087_daystocover_at_new_252d_high_indicator": {"inputs": ["daystocover"], "func": f25_sibt_087_daystocover_at_new_252d_high_indicator},
    "f25_sibt_088_si_log_drawdown_from_252d_high": {"inputs": ["shortinterest"], "func": f25_sibt_088_si_log_drawdown_from_252d_high},
    "f25_sibt_089_si_log_rally_from_252d_low": {"inputs": ["shortinterest"], "func": f25_sibt_089_si_log_rally_from_252d_low},
    "f25_sibt_090_si_252d_high_minus_low_log_range": {"inputs": ["shortinterest"], "func": f25_sibt_090_si_252d_high_minus_low_log_range},
    "f25_sibt_091_si_pct_chg21_zscore_252d": {"inputs": ["shortinterest"], "func": f25_sibt_091_si_pct_chg21_zscore_252d},
    "f25_sibt_092_si_pct_chg63_zscore_252d": {"inputs": ["shortinterest"], "func": f25_sibt_092_si_pct_chg63_zscore_252d},
    "f25_sibt_093_spf_chg63_zscore_252d": {"inputs": ["shortpctfloat"], "func": f25_sibt_093_spf_chg63_zscore_252d},
    "f25_sibt_094_dtc_chg63_zscore_252d": {"inputs": ["daystocover"], "func": f25_sibt_094_dtc_chg63_zscore_252d},
    "f25_sibt_095_si_rising_persistence_63d": {"inputs": ["shortinterest"], "func": f25_sibt_095_si_rising_persistence_63d},
    "f25_sibt_096_spf_rising_persistence_63d": {"inputs": ["shortpctfloat"], "func": f25_sibt_096_spf_rising_persistence_63d},
    "f25_sibt_097_dtc_rising_persistence_63d": {"inputs": ["daystocover"], "func": f25_sibt_097_dtc_rising_persistence_63d},
    "f25_sibt_098_si_rising_persistence_126d": {"inputs": ["shortinterest"], "func": f25_sibt_098_si_rising_persistence_126d},
    "f25_sibt_099_si_strictly_higher_streak_63d": {"inputs": ["shortinterest"], "func": f25_sibt_099_si_strictly_higher_streak_63d},
    "f25_sibt_100_spf_strictly_higher_streak_126d": {"inputs": ["shortpctfloat"], "func": f25_sibt_100_spf_strictly_higher_streak_126d},
    "f25_sibt_101_si_above_ema63_persistence": {"inputs": ["shortinterest"], "func": f25_sibt_101_si_above_ema63_persistence},
    "f25_sibt_102_spf_above_ema63_persistence": {"inputs": ["shortpctfloat"], "func": f25_sibt_102_spf_above_ema63_persistence},
    "f25_sibt_103_dtc_above_ema63_persistence": {"inputs": ["daystocover"], "func": f25_sibt_103_dtc_above_ema63_persistence},
    "f25_sibt_104_si_log_slope_63d": {"inputs": ["shortinterest"], "func": f25_sibt_104_si_log_slope_63d},
    "f25_sibt_105_si_log_slope_252d": {"inputs": ["shortinterest"], "func": f25_sibt_105_si_log_slope_252d},
    "f25_sibt_106_si_log_change_realized_vol_63d": {"inputs": ["shortinterest"], "func": f25_sibt_106_si_log_change_realized_vol_63d},
    "f25_sibt_107_si_log_change_realized_vol_126d": {"inputs": ["shortinterest"], "func": f25_sibt_107_si_log_change_realized_vol_126d},
    "f25_sibt_108_spf_realized_vol_63d": {"inputs": ["shortpctfloat"], "func": f25_sibt_108_spf_realized_vol_63d},
    "f25_sibt_109_dtc_realized_vol_63d": {"inputs": ["daystocover"], "func": f25_sibt_109_dtc_realized_vol_63d},
    "f25_sibt_110_si_surge_25pct_in_21d_indicator": {"inputs": ["shortinterest"], "func": f25_sibt_110_si_surge_25pct_in_21d_indicator},
    "f25_sibt_111_si_surge_50pct_in_63d_indicator": {"inputs": ["shortinterest"], "func": f25_sibt_111_si_surge_50pct_in_63d_indicator},
    "f25_sibt_112_si_doubled_in_126d_indicator": {"inputs": ["shortinterest"], "func": f25_sibt_112_si_doubled_in_126d_indicator},
    "f25_sibt_113_spf_jumped_5pp_in_63d_indicator": {"inputs": ["shortpctfloat"], "func": f25_sibt_113_spf_jumped_5pp_in_63d_indicator},
    "f25_sibt_114_dtc_jumped_2x_in_63d_indicator": {"inputs": ["daystocover"], "func": f25_sibt_114_dtc_jumped_2x_in_63d_indicator},
    "f25_sibt_115_si_crossed_above_252d_median_recently": {"inputs": ["shortinterest"], "func": f25_sibt_115_si_crossed_above_252d_median_recently},
    "f25_sibt_116_spf_crossed_above_10_recently": {"inputs": ["shortpctfloat"], "func": f25_sibt_116_spf_crossed_above_10_recently},
    "f25_sibt_117_si_vol_normalized_chg63": {"inputs": ["shortinterest"], "func": f25_sibt_117_si_vol_normalized_chg63},
    "f25_sibt_118_spf_vol_normalized_chg63": {"inputs": ["shortpctfloat"], "func": f25_sibt_118_spf_vol_normalized_chg63},
    "f25_sibt_119_dtc_vol_normalized_chg63": {"inputs": ["daystocover"], "func": f25_sibt_119_dtc_vol_normalized_chg63},
    "f25_sibt_120_si_log_chg_skew_126d": {"inputs": ["shortinterest"], "func": f25_sibt_120_si_log_chg_skew_126d},
    "f25_sibt_121_si_pct_chg63_minus_price_pct_chg63": {"inputs": ["shortinterest", "close"], "func": f25_sibt_121_si_pct_chg63_minus_price_pct_chg63},
    "f25_sibt_122_spf_chg63_times_price_chg63": {"inputs": ["shortpctfloat", "close"], "func": f25_sibt_122_spf_chg63_times_price_chg63},
    "f25_sibt_123_si_rising_while_price_rising_indicator": {"inputs": ["shortinterest", "close"], "func": f25_sibt_123_si_rising_while_price_rising_indicator},
    "f25_sibt_124_si_rising_while_price_near_252d_high_indicator": {"inputs": ["shortinterest", "close"], "func": f25_sibt_124_si_rising_while_price_near_252d_high_indicator},
    "f25_sibt_125_si_zscore_minus_price_zscore_63d": {"inputs": ["shortinterest", "close"], "func": f25_sibt_125_si_zscore_minus_price_zscore_63d},
    "f25_sibt_126_si_zscore_minus_price_zscore_126d": {"inputs": ["shortinterest", "close"], "func": f25_sibt_126_si_zscore_minus_price_zscore_126d},
    "f25_sibt_127_spf_chg63_div_price_chg63": {"inputs": ["shortpctfloat", "close"], "func": f25_sibt_127_spf_chg63_div_price_chg63},
    "f25_sibt_128_dtc_chg63_div_price_chg63": {"inputs": ["daystocover", "close"], "func": f25_sibt_128_dtc_chg63_div_price_chg63},
    "f25_sibt_129_si_log_chg63_times_price_log_chg63": {"inputs": ["shortinterest", "close"], "func": f25_sibt_129_si_log_chg63_times_price_log_chg63},
    "f25_sibt_130_spf_chg126_with_positive_price_chg126": {"inputs": ["shortpctfloat", "close"], "func": f25_sibt_130_spf_chg126_with_positive_price_chg126},
    "f25_sibt_131_si_buildup_during_price_uptrend_persistence": {"inputs": ["shortinterest", "close"], "func": f25_sibt_131_si_buildup_during_price_uptrend_persistence},
    "f25_sibt_132_si_pct_chg63_when_price_above_ema63": {"inputs": ["shortinterest", "close"], "func": f25_sibt_132_si_pct_chg63_when_price_above_ema63},
    "f25_sibt_133_si_to_market_cap_proxy": {"inputs": ["shortinterest", "close", "sharesbas"], "func": f25_sibt_133_si_to_market_cap_proxy},
    "f25_sibt_134_si_dollar_value_log": {"inputs": ["shortinterest", "close"], "func": f25_sibt_134_si_dollar_value_log},
    "f25_sibt_135_si_dollar_value_pct_chg63": {"inputs": ["shortinterest", "close"], "func": f25_sibt_135_si_dollar_value_pct_chg63},
    "f25_sibt_136_shortinterest_to_adv_21d": {"inputs": ["shortinterest", "volume"], "func": f25_sibt_136_shortinterest_to_adv_21d},
    "f25_sibt_137_shortinterest_to_adv_63d": {"inputs": ["shortinterest", "volume"], "func": f25_sibt_137_shortinterest_to_adv_63d},
    "f25_sibt_138_shortinterest_to_adv_252d": {"inputs": ["shortinterest", "volume"], "func": f25_sibt_138_shortinterest_to_adv_252d},
    "f25_sibt_139_si_to_adv_chg63": {"inputs": ["shortinterest", "volume"], "func": f25_sibt_139_si_to_adv_chg63},
    "f25_sibt_140_dtc_minus_si_to_adv_gap": {"inputs": ["daystocover", "shortinterest", "volume"], "func": f25_sibt_140_dtc_minus_si_to_adv_gap},
    "f25_sibt_141_si_normalized_by_252d_adv_chg126": {"inputs": ["shortinterest", "volume"], "func": f25_sibt_141_si_normalized_by_252d_adv_chg126},
    "f25_sibt_142_dtc_regime_shift_short_vs_long": {"inputs": ["daystocover"], "func": f25_sibt_142_dtc_regime_shift_short_vs_long},
    "f25_sibt_143_si_regime_shift_short_vs_long": {"inputs": ["shortinterest"], "func": f25_sibt_143_si_regime_shift_short_vs_long},
    "f25_sibt_144_spf_regime_shift_short_vs_long": {"inputs": ["shortpctfloat"], "func": f25_sibt_144_spf_regime_shift_short_vs_long},
    "f25_sibt_145_si_chg63_normalized_by_price_realized_vol": {"inputs": ["shortinterest", "close"], "func": f25_sibt_145_si_chg63_normalized_by_price_realized_vol},
    "f25_sibt_146_dtc_chg63_normalized_by_price_realized_vol": {"inputs": ["daystocover", "close"], "func": f25_sibt_146_dtc_chg63_normalized_by_price_realized_vol},
    "f25_sibt_147_si_buildup_index_compound_63d": {"inputs": ["shortinterest", "shortpctfloat", "daystocover"], "func": f25_sibt_147_si_buildup_index_compound_63d},
    "f25_sibt_148_si_buildup_breadth_indicator": {"inputs": ["shortinterest", "shortpctfloat", "daystocover"], "func": f25_sibt_148_si_buildup_breadth_indicator},
    "f25_sibt_149_si_buildup_trend_strength_signed": {"inputs": ["shortinterest"], "func": f25_sibt_149_si_buildup_trend_strength_signed},
    "f25_sibt_150_compound_buildup_trajectory_score": {"inputs": ["shortinterest", "daystocover", "shortpctfloat", "close"], "func": f25_sibt_150_compound_buildup_trajectory_score},
}
