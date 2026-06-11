"""
118_drawdown_recovery_asymmetry — Base Features 076-150
Domain: asymmetry between down-legs and up-legs within the price path —
        intraday high/low range asymmetry, volume-weighted asymmetry, EWM-based
        asymmetry, recovery-from-low geometry, speed ratios, multi-window
        ratchet composites, path tortuosity.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _up_ret(close: pd.Series) -> pd.Series:
    return close.pct_change(1).clip(lower=0.0)


def _dn_ret(close: pd.Series) -> pd.Series:
    return (-close.pct_change(1)).clip(lower=0.0)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Intraday range asymmetry (high/low bar geometry) ---

def dra_076_up_body_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean positive body size (close > open) over 21 days as fraction of open."""
    body = _safe_div(close - open_, open_.replace(0, np.nan))
    up_body = body.where(body > 0)
    return up_body.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_077_dn_body_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean negative body size magnitude (close < open) over 21 days."""
    body = _safe_div(open_ - close, open_.replace(0, np.nan))
    dn_body = body.where(body > 0)
    return dn_body.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_078_body_asymmetry_ratio_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Ratio of mean dn-body to mean up-body over 21 days. > 1 = bigger falling bars."""
    return _safe_div(dra_077_dn_body_21d(close, open_), dra_076_up_body_21d(close, open_))


def dra_079_upper_wick_21d(high: pd.Series, close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean upper wick size as fraction of range over 21 days (upward rejection)."""
    rng = (high - close.combine(open_, min)).replace(0, np.nan)
    upper = _safe_div(high - close.combine(open_, max), rng)
    return upper.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_080_lower_wick_21d(low: pd.Series, close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean lower wick size as fraction of range over 21 days (downward rejection)."""
    rng = (close.combine(open_, max) - low).replace(0, np.nan)
    lower = _safe_div(close.combine(open_, min) - low, rng)
    return lower.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_081_wick_asymmetry_21d(high: pd.Series, low: pd.Series,
                                close: pd.Series, open_: pd.Series) -> pd.Series:
    """Lower wick minus upper wick (mean) over 21 days. Positive = more downward tails."""
    bar_range = (high - low).replace(0, np.nan)
    upper_wick = _safe_div(high - close.combine(open_, max), bar_range)
    lower_wick = _safe_div(close.combine(open_, min) - low, bar_range)
    diff = lower_wick - upper_wick
    return diff.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_082_close_location_value_21d(high: pd.Series, low: pd.Series,
                                      close: pd.Series) -> pd.Series:
    """Mean close-location value over 21 days: (close-low)/(high-low). < 0.5 = bearish close."""
    clv = _safe_div(close - low, (high - low).replace(0, np.nan))
    return clv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_083_low_vs_high_move_21d(high: pd.Series, low: pd.Series,
                                   close: pd.Series) -> pd.Series:
    """Mean daily: (prev_close - low)/(high - prev_close) — dn range vs up range from prev close."""
    prev = close.shift(1)
    dn_range = (prev - low).clip(lower=0.0)
    up_range = (high - prev).clip(lower=0.0)
    ratio = _safe_div(dn_range, up_range.replace(0, np.nan))
    return ratio.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_084_dn_gap_count_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Count of down-gap days (open < prev_close) in trailing 21 days."""
    gap = open_ - close.shift(1)
    return _rolling_sum((gap < 0).astype(float), _TD_MON)


def dra_085_up_gap_count_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Count of up-gap days (open > prev_close) in trailing 21 days."""
    gap = open_ - close.shift(1)
    return _rolling_sum((gap > 0).astype(float), _TD_MON)


# --- Group I (086-095): Volume-weighted down vs up asymmetry ---

def dra_086_vol_weighted_dn_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average down-day return magnitude over 21 days."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    vw_dn = dn * volume
    sum_vw = _rolling_sum(vw_dn, _TD_MON)
    sum_vol_dn = _rolling_sum(volume.where(dn > 0, 0.0), _TD_MON)
    return _safe_div(sum_vw, sum_vol_dn.replace(0, np.nan))


def dra_087_vol_weighted_up_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average up-day return over 21 days."""
    up = close.pct_change(1).clip(lower=0.0)
    vw_up = up * volume
    sum_vw = _rolling_sum(vw_up, _TD_MON)
    sum_vol_up = _rolling_sum(volume.where(up > 0, 0.0), _TD_MON)
    return _safe_div(sum_vw, sum_vol_up.replace(0, np.nan))


def dra_088_vol_asymmetry_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of vol-weighted dn return to vol-weighted up return (21 days). > 1 = heavy down-vol."""
    return _safe_div(dra_086_vol_weighted_dn_ret_21d(close, volume),
                     dra_087_vol_weighted_up_ret_21d(close, volume))


def dra_089_dn_day_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on down days over 21 days."""
    is_dn = (close.pct_change(1) < 0)
    dn_vol = volume.where(is_dn, 0.0)
    cnt_dn = _rolling_sum(is_dn.astype(float), _TD_MON)
    return _safe_div(_rolling_sum(dn_vol, _TD_MON), cnt_dn.replace(0, np.nan))


def dra_090_up_day_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on up days over 21 days."""
    is_up = (close.pct_change(1) > 0)
    up_vol = volume.where(is_up, 0.0)
    cnt_up = _rolling_sum(is_up.astype(float), _TD_MON)
    return _safe_div(_rolling_sum(up_vol, _TD_MON), cnt_up.replace(0, np.nan))


def dra_091_dn_up_volume_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean dn-day volume to mean up-day volume (21 days). > 1 = heavier dn volume."""
    return _safe_div(dra_089_dn_day_volume_21d(close, volume),
                     dra_090_up_day_volume_21d(close, volume))


def dra_092_dn_day_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on down days over 63 days."""
    is_dn = (close.pct_change(1) < 0)
    cnt_dn = _rolling_sum(is_dn.astype(float), _TD_QTR)
    return _safe_div(_rolling_sum(volume.where(is_dn, 0.0), _TD_QTR),
                     cnt_dn.replace(0, np.nan))


def dra_093_up_day_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on up days over 63 days."""
    is_up = (close.pct_change(1) > 0)
    cnt_up = _rolling_sum(is_up.astype(float), _TD_QTR)
    return _safe_div(_rolling_sum(volume.where(is_up, 0.0), _TD_QTR),
                     cnt_up.replace(0, np.nan))


def dra_094_dn_up_volume_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean dn-day volume to mean up-day volume (63 days)."""
    return _safe_div(dra_092_dn_day_volume_63d(close, volume),
                     dra_093_up_day_volume_63d(close, volume))


def dra_095_dn_volume_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total volume on down days over 21 days."""
    is_dn = (close.pct_change(1) < 0)
    sum_dn_vol = _rolling_sum(volume.where(is_dn, 0.0), _TD_MON)
    sum_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(sum_dn_vol, sum_vol.replace(0, np.nan))


# --- Group J (096-105): EWM-based asymmetry (exponential weighting) ---

def dra_096_ewm_avg_up_ret_21d(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily up-returns (exponentially-weighted mean up-move)."""
    up = close.pct_change(1).clip(lower=0.0)
    return _ewm_mean(up, _TD_MON)


def dra_097_ewm_avg_dn_ret_21d(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily down-return magnitudes."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    return _ewm_mean(dn, _TD_MON)


def dra_098_ewm_up_dn_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of EWM up-ret to EWM dn-ret (span=21). < 1 = heavier down-move emphasis."""
    return _safe_div(dra_096_ewm_avg_up_ret_21d(close), dra_097_ewm_avg_dn_ret_21d(close))


def dra_099_ewm_avg_up_ret_63d(close: pd.Series) -> pd.Series:
    """EWM (span=63) of daily up-returns."""
    up = close.pct_change(1).clip(lower=0.0)
    return _ewm_mean(up, _TD_QTR)


def dra_100_ewm_avg_dn_ret_63d(close: pd.Series) -> pd.Series:
    """EWM (span=63) of daily down-return magnitudes."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    return _ewm_mean(dn, _TD_QTR)


def dra_101_ewm_up_dn_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of EWM up-ret to EWM dn-ret (span=63)."""
    return _safe_div(dra_099_ewm_avg_up_ret_63d(close), dra_100_ewm_avg_dn_ret_63d(close))


def dra_102_ewm_dn_excess_21d(close: pd.Series) -> pd.Series:
    """EWM dn-ret minus EWM up-ret (span=21). Positive = heavier recent dn-move."""
    return dra_097_ewm_avg_dn_ret_21d(close) - dra_096_ewm_avg_up_ret_21d(close)


def dra_103_ewm_dn_excess_63d(close: pd.Series) -> pd.Series:
    """EWM dn-ret minus EWM up-ret (span=63)."""
    return dra_100_ewm_avg_dn_ret_63d(close) - dra_099_ewm_avg_up_ret_63d(close)


def dra_104_ewm_up_ret_5d(close: pd.Series) -> pd.Series:
    """EWM (span=5) of daily up-returns (very short-term up pressure)."""
    up = close.pct_change(1).clip(lower=0.0)
    return _ewm_mean(up, _TD_WEEK)


def dra_105_ewm_dn_ret_5d(close: pd.Series) -> pd.Series:
    """EWM (span=5) of daily down-return magnitudes (very short-term dn pressure)."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    return _ewm_mean(dn, _TD_WEEK)


# --- Group K (106-115): Recovery-from-low geometry ---

def dra_106_dist_from_rolling_low_21d(close: pd.Series) -> pd.Series:
    """Close distance from 21-day low as fraction of the 21-day low."""
    lo = _rolling_min(close, _TD_MON)
    return _safe_div(close - lo, lo.replace(0, np.nan))


def dra_107_dist_from_rolling_low_63d(close: pd.Series) -> pd.Series:
    """Close distance from 63-day low as fraction of the 63-day low."""
    lo = _rolling_min(close, _TD_QTR)
    return _safe_div(close - lo, lo.replace(0, np.nan))


def dra_108_dist_from_rolling_low_252d(close: pd.Series) -> pd.Series:
    """Close distance from 252-day low as fraction of the 252-day low."""
    lo = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - lo, lo.replace(0, np.nan))


def dra_109_recovery_ratio_21d(close: pd.Series) -> pd.Series:
    """Recovery fraction: (close - 21d_low) / (21d_high - 21d_low).
    Near 0 = near the bottom of the range; near 1 = full recovery."""
    lo = _rolling_min(close, _TD_MON)
    hi = _rolling_max(close, _TD_MON)
    return _safe_div(close - lo, (hi - lo).replace(0, np.nan))


def dra_110_recovery_ratio_63d(close: pd.Series) -> pd.Series:
    """Recovery fraction: (close - 63d_low) / (63d_high - 63d_low)."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    return _safe_div(close - lo, (hi - lo).replace(0, np.nan))


def dra_111_dist_from_high_vs_low_ratio_21d(close: pd.Series) -> pd.Series:
    """(close - 21d_low) / (21d_high - close): low proximity vs high proximity ratio."""
    lo = _rolling_min(close, _TD_MON)
    hi = _rolling_max(close, _TD_MON)
    dist_from_lo = (close - lo).clip(lower=0.0)
    dist_from_hi = (hi - close).clip(lower=0.0)
    return _safe_div(dist_from_lo, dist_from_hi.replace(0, np.nan))


def dra_112_dist_from_high_vs_low_ratio_63d(close: pd.Series) -> pd.Series:
    """(close - 63d_low) / (63d_high - close)."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    dist_from_lo = (close - lo).clip(lower=0.0)
    dist_from_hi = (hi - close).clip(lower=0.0)
    return _safe_div(dist_from_lo, dist_from_hi.replace(0, np.nan))


def dra_113_new_low_frequency_21d(close: pd.Series) -> pd.Series:
    """Fraction of days in trailing 21 days that closed at a new n-day low (21d window)."""
    prev_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    new_lo = (close < prev_min).astype(float)
    return _rolling_sum(new_lo, _TD_MON) / _TD_MON


def dra_114_new_high_frequency_21d(close: pd.Series) -> pd.Series:
    """Fraction of days in trailing 21 days that closed at a new n-day high."""
    prev_max = close.shift(1).rolling(_TD_MON, min_periods=1).max()
    new_hi = (close > prev_max).astype(float)
    return _rolling_sum(new_hi, _TD_MON) / _TD_MON


def dra_115_new_lo_vs_hi_freq_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of new-low frequency to new-high frequency over 21 days. > 1 = more new lows."""
    return _safe_div(dra_113_new_low_frequency_21d(close),
                     dra_114_new_high_frequency_21d(close))


# --- Group L (116-125): Speed ratio and acceleration asymmetry ---

def dra_116_dn_speed_ratio_21d(close: pd.Series) -> pd.Series:
    """Speed of decline: gross_dn_return / dn_day_count over 21 days (avg dn per dn-day)."""
    dn_sum = _rolling_sum((-close.pct_change(1)).clip(lower=0.0), _TD_MON)
    dn_cnt = _rolling_sum((close.pct_change(1) < 0).astype(float), _TD_MON)
    return _safe_div(dn_sum, dn_cnt.replace(0, np.nan))


def dra_117_up_speed_ratio_21d(close: pd.Series) -> pd.Series:
    """Speed of advance: gross_up_return / up_day_count over 21 days."""
    up_sum = _rolling_sum(close.pct_change(1).clip(lower=0.0), _TD_MON)
    up_cnt = _rolling_sum((close.pct_change(1) > 0).astype(float), _TD_MON)
    return _safe_div(up_sum, up_cnt.replace(0, np.nan))


def dra_118_speed_asymmetry_21d(close: pd.Series) -> pd.Series:
    """Ratio dn_speed / up_speed over 21 days. > 1 = falls faster than it rises."""
    return _safe_div(dra_116_dn_speed_ratio_21d(close), dra_117_up_speed_ratio_21d(close))


def dra_119_dn_speed_ratio_63d(close: pd.Series) -> pd.Series:
    """Speed of decline per dn-day over 63 days."""
    dn_sum = _rolling_sum((-close.pct_change(1)).clip(lower=0.0), _TD_QTR)
    dn_cnt = _rolling_sum((close.pct_change(1) < 0).astype(float), _TD_QTR)
    return _safe_div(dn_sum, dn_cnt.replace(0, np.nan))


def dra_120_up_speed_ratio_63d(close: pd.Series) -> pd.Series:
    """Speed of advance per up-day over 63 days."""
    up_sum = _rolling_sum(close.pct_change(1).clip(lower=0.0), _TD_QTR)
    up_cnt = _rolling_sum((close.pct_change(1) > 0).astype(float), _TD_QTR)
    return _safe_div(up_sum, up_cnt.replace(0, np.nan))


def dra_121_speed_asymmetry_63d(close: pd.Series) -> pd.Series:
    """Ratio dn_speed / up_speed over 63 days."""
    return _safe_div(dra_119_dn_speed_ratio_63d(close), dra_120_up_speed_ratio_63d(close))


def dra_122_dn_speed_ratio_252d(close: pd.Series) -> pd.Series:
    """Speed of decline per dn-day over 252 days."""
    dn_sum = _rolling_sum((-close.pct_change(1)).clip(lower=0.0), _TD_YEAR)
    dn_cnt = _rolling_sum((close.pct_change(1) < 0).astype(float), _TD_YEAR)
    return _safe_div(dn_sum, dn_cnt.replace(0, np.nan))


def dra_123_up_speed_ratio_252d(close: pd.Series) -> pd.Series:
    """Speed of advance per up-day over 252 days."""
    up_sum = _rolling_sum(close.pct_change(1).clip(lower=0.0), _TD_YEAR)
    up_cnt = _rolling_sum((close.pct_change(1) > 0).astype(float), _TD_YEAR)
    return _safe_div(up_sum, up_cnt.replace(0, np.nan))


def dra_124_speed_asymmetry_252d(close: pd.Series) -> pd.Series:
    """Ratio dn_speed / up_speed over 252 days."""
    return _safe_div(dra_122_dn_speed_ratio_252d(close), dra_123_up_speed_ratio_252d(close))


def dra_125_speed_asymmetry_change_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Short-run speed asymmetry (21d) minus long-run (63d). Positive = worsening recently."""
    return dra_118_speed_asymmetry_21d(close) - dra_121_speed_asymmetry_63d(close)


# --- Group M (126-135): Multi-window ratchet composites ---

def dra_126_ratchet_score_21d(close: pd.Series) -> pd.Series:
    """Ratchet score (21d): sum of (dn_day_ret - prior_recovery_ret) normalized.
    Measures whether each decline exceeded the most recent single-day recovery."""
    ret = close.pct_change(1)
    prev_up = ret.clip(lower=0.0).shift(1)
    dn = (-ret).clip(lower=0.0)
    ratchet = (dn - prev_up).clip(lower=0.0)
    return _rolling_sum(ratchet, _TD_MON)


def dra_127_ratchet_score_63d(close: pd.Series) -> pd.Series:
    """Ratchet score (63d): cumulative excess of dn-moves over preceding up-moves."""
    ret = close.pct_change(1)
    prev_up = ret.clip(lower=0.0).shift(1)
    dn = (-ret).clip(lower=0.0)
    ratchet = (dn - prev_up).clip(lower=0.0)
    return _rolling_sum(ratchet, _TD_QTR)


def dra_128_ratchet_score_252d(close: pd.Series) -> pd.Series:
    """Ratchet score (252d): cumulative excess of dn-moves over preceding up-moves."""
    ret = close.pct_change(1)
    prev_up = ret.clip(lower=0.0).shift(1)
    dn = (-ret).clip(lower=0.0)
    ratchet = (dn - prev_up).clip(lower=0.0)
    return _rolling_sum(ratchet, _TD_YEAR)


def dra_129_dn_amplitude_ratio_21d(close: pd.Series) -> pd.Series:
    """Mean dn-day magnitude divided by preceding up-day magnitude (21d rolling average).
    > 1 = drops tend to be bigger than the recoveries preceding them."""
    ret = close.pct_change(1)
    dn = (-ret).clip(lower=0.0)
    prev_up = ret.clip(lower=0.0).shift(1).replace(0, np.nan)
    ratio = _safe_div(dn, prev_up)
    return ratio.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_130_dn_amplitude_ratio_63d(close: pd.Series) -> pd.Series:
    """Mean dn-day magnitude divided by preceding up-day magnitude (63d average)."""
    ret = close.pct_change(1)
    dn = (-ret).clip(lower=0.0)
    prev_up = ret.clip(lower=0.0).shift(1).replace(0, np.nan)
    ratio = _safe_div(dn, prev_up)
    return ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dra_131_path_tortuosity_21d(close: pd.Series) -> pd.Series:
    """Path tortuosity (21d): gross path length / abs(net 21d change).
    High = winding path (many back-and-forth); low = efficient trend."""
    gross = _rolling_sum(close.pct_change(1).abs(), _TD_MON)
    net = close.pct_change(_TD_MON).abs()
    return _safe_div(gross, net.replace(0, np.nan))


def dra_132_path_tortuosity_63d(close: pd.Series) -> pd.Series:
    """Path tortuosity (63d): gross path length / abs(net 63d change)."""
    gross = _rolling_sum(close.pct_change(1).abs(), _TD_QTR)
    net = close.pct_change(_TD_QTR).abs()
    return _safe_div(gross, net.replace(0, np.nan))


def dra_133_dn_tortuosity_21d(close: pd.Series) -> pd.Series:
    """Down-path tortuosity: gross_dn / net_dn_move over 21 days.
    High = the decline was interrupted by many counter-moves."""
    gross_dn = _rolling_sum((-close.pct_change(1)).clip(lower=0.0), _TD_MON)
    net_dn = (-close.pct_change(_TD_MON)).clip(lower=0.0)
    return _safe_div(gross_dn, net_dn.replace(0, np.nan))


def dra_134_up_tortuosity_21d(close: pd.Series) -> pd.Series:
    """Up-path tortuosity: gross_up / net_up_move over 21 days."""
    gross_up = _rolling_sum(close.pct_change(1).clip(lower=0.0), _TD_MON)
    net_up = close.pct_change(_TD_MON).clip(lower=0.0)
    return _safe_div(gross_up, net_up.replace(0, np.nan))


def dra_135_dn_vs_up_tortuosity_21d(close: pd.Series) -> pd.Series:
    """Dn tortuosity minus up tortuosity over 21 days. Positive = declines more interrupted."""
    return dra_133_dn_tortuosity_21d(close) - dra_134_up_tortuosity_21d(close)


# --- Group N (136-145): Asymmetry z-scores and percentile ranks ---

def dra_136_gain_loss_ratio_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 21d gain/loss ratio relative to its 63-day distribution."""
    ratio = _rolling_sum(close.pct_change(1).clip(lower=0.0), _TD_MON) / (
        _rolling_sum((-close.pct_change(1)).clip(lower=0.0), _TD_MON) + _EPS)
    m = _rolling_mean(ratio, _TD_QTR)
    s = _rolling_std(ratio, _TD_QTR)
    return _safe_div(ratio - m, s)


def dra_137_vol_asym_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 21d vol-asymmetry ratio relative to its 63-day distribution."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    ratio = _safe_div(dn_vol, up_vol)
    m = _rolling_mean(ratio, _TD_QTR)
    s = _rolling_std(ratio, _TD_QTR)
    return _safe_div(ratio - m, s)


def dra_138_speed_asym_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 21d speed-asymmetry ratio relative to its 63-day distribution."""
    ret = close.pct_change(1)
    dn_sum = _rolling_sum((-ret).clip(lower=0.0), _TD_MON)
    dn_cnt = _rolling_sum((ret < 0).astype(float), _TD_MON).replace(0, np.nan)
    up_sum = _rolling_sum(ret.clip(lower=0.0), _TD_MON)
    up_cnt = _rolling_sum((ret > 0).astype(float), _TD_MON).replace(0, np.nan)
    dn_spd = _safe_div(dn_sum, dn_cnt)
    up_spd = _safe_div(up_sum, up_cnt)
    ratio = _safe_div(dn_spd, up_spd)
    m = _rolling_mean(ratio, _TD_QTR)
    s = _rolling_std(ratio, _TD_QTR)
    return _safe_div(ratio - m, s)


def dra_139_gain_loss_ratio_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d gain/loss ratio within trailing 252-day distribution."""
    ret = close.pct_change(1)
    ratio = _rolling_sum(ret.clip(lower=0.0), _TD_MON) / (
        _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dra_140_vol_asym_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d vol-asymmetry ratio within trailing 252-day distribution."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    ratio = _safe_div(dn_vol, up_vol)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dra_141_dn_participation_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d dn-participation rate within trailing 252-day distribution."""
    ret = close.pct_change(1)
    up_sq = (ret.clip(lower=0.0) ** 2)
    dn_sq = ((-ret).clip(lower=0.0) ** 2)
    rate = _safe_div(_rolling_sum(dn_sq, _TD_MON),
                     (_rolling_sum(up_sq, _TD_MON) + _rolling_sum(dn_sq, _TD_MON)))
    return rate.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dra_142_gain_loss_ratio_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of 21d gain/loss ratio."""
    ret = close.pct_change(1)
    ratio = _rolling_sum(ret.clip(lower=0.0), _TD_MON) / (
        _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS)
    return ratio.expanding(min_periods=_TD_MON).rank(pct=True)


def dra_143_speed_asym_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of 21d speed-asymmetry ratio."""
    ret = close.pct_change(1)
    dn_sum = _rolling_sum((-ret).clip(lower=0.0), _TD_MON)
    dn_cnt = _rolling_sum((ret < 0).astype(float), _TD_MON).replace(0, np.nan)
    up_sum = _rolling_sum(ret.clip(lower=0.0), _TD_MON)
    up_cnt = _rolling_sum((ret > 0).astype(float), _TD_MON).replace(0, np.nan)
    ratio = _safe_div(_safe_div(dn_sum, dn_cnt), _safe_div(up_sum, up_cnt))
    return ratio.expanding(min_periods=_TD_MON).rank(pct=True)


def dra_144_streak_ratio_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d dn/up streak ratio within trailing 252-day distribution."""
    ret = close.pct_change(1)
    dn_st = _consec_streak(ret < 0)
    up_st = _consec_streak(ret > 0)
    max_dn = dn_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    max_up = up_st.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    ratio = _safe_div(max_dn, max_up)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dra_145_dn_count_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d down-day count relative to its 252-day distribution."""
    dn_cnt = _rolling_sum((close.pct_change(1) < 0).astype(float), _TD_MON)
    m = _rolling_mean(dn_cnt, _TD_YEAR)
    s = _rolling_std(dn_cnt, _TD_YEAR)
    return _safe_div(dn_cnt - m, s)


# --- Group O (146-150): Composite asymmetry indices ---

def dra_146_asymmetry_composite_21d(close: pd.Series) -> pd.Series:
    """Composite asymmetry index (21d): normalized average of vol-asym, speed-asym,
    gain-loss inverse, dn-participation. Higher = more bearish asymmetry."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    vol_asym = _safe_div(dn_vol, up_vol + _EPS)

    dn_sum = _rolling_sum((-ret).clip(lower=0.0), _TD_MON)
    up_sum = _rolling_sum(ret.clip(lower=0.0), _TD_MON)
    gl_inv = _safe_div(dn_sum, up_sum + _EPS)

    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_MON)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_MON)
    dn_part = _safe_div(dn_sq, dn_sq + up_sq + _EPS)

    dn_cnt = _rolling_sum((ret < 0).astype(float), _TD_MON)
    up_cnt = _rolling_sum((ret > 0).astype(float), _TD_MON)
    dn_spd = _safe_div(dn_sum, dn_cnt.replace(0, np.nan))
    up_spd = _safe_div(up_sum, up_cnt.replace(0, np.nan))
    spd_asym = _safe_div(dn_spd, up_spd + _EPS)

    return (vol_asym.fillna(1.0) + gl_inv.fillna(1.0) + dn_part.fillna(0.5) * 2 +
            spd_asym.fillna(1.0)) / 4.0


def dra_147_asymmetry_composite_63d(close: pd.Series) -> pd.Series:
    """Composite asymmetry index (63d): same components as 146 but 63d window."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).std()
    vol_asym = _safe_div(dn_vol, up_vol + _EPS)

    dn_sum = _rolling_sum((-ret).clip(lower=0.0), _TD_QTR)
    up_sum = _rolling_sum(ret.clip(lower=0.0), _TD_QTR)
    gl_inv = _safe_div(dn_sum, up_sum + _EPS)

    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_QTR)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_QTR)
    dn_part = _safe_div(dn_sq, dn_sq + up_sq + _EPS)

    dn_cnt = _rolling_sum((ret < 0).astype(float), _TD_QTR)
    up_cnt = _rolling_sum((ret > 0).astype(float), _TD_QTR)
    dn_spd = _safe_div(dn_sum, dn_cnt.replace(0, np.nan))
    up_spd = _safe_div(up_sum, up_cnt.replace(0, np.nan))
    spd_asym = _safe_div(dn_spd, up_spd + _EPS)

    return (vol_asym.fillna(1.0) + gl_inv.fillna(1.0) + dn_part.fillna(0.5) * 2 +
            spd_asym.fillna(1.0)) / 4.0


def dra_148_asymmetry_short_vs_long_21_vs_252(close: pd.Series) -> pd.Series:
    """Short-term (21d) gain/loss inverse minus long-term (252d) gain/loss inverse.
    Positive = current asymmetry worse than long-run norm."""
    ret = close.pct_change(1)
    gl_21 = _safe_div(_rolling_sum((-ret).clip(lower=0.0), _TD_MON),
                      _rolling_sum(ret.clip(lower=0.0), _TD_MON) + _EPS)
    gl_252 = _safe_div(_rolling_sum((-ret).clip(lower=0.0), _TD_YEAR),
                       _rolling_sum(ret.clip(lower=0.0), _TD_YEAR) + _EPS)
    return gl_21 - gl_252


def dra_149_asymmetry_regime_flag_21d(close: pd.Series) -> pd.Series:
    """Binary flag: 21d gain/loss ratio < 0.8 AND dn-participation > 0.6 (severe asymmetry)."""
    ret = close.pct_change(1)
    gl = _safe_div(_rolling_sum(ret.clip(lower=0.0), _TD_MON),
                   _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS)
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_MON)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_MON)
    dn_part = _safe_div(dn_sq, dn_sq + up_sq + _EPS)
    flag = ((gl < 0.8) & (dn_part > 0.6)).astype(float)
    return flag


def dra_150_dn_day_ret_vs_up_day_vol_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of mean dn-day return to std of up-day returns over 21 days.
    High = large falls relative to the variability of recoveries."""
    ret = close.pct_change(1)
    dn = (-ret).clip(lower=0.0)
    up = ret.clip(lower=0.0)
    avg_dn = dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    std_up = up.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    return _safe_div(avg_dn, std_up.replace(0, np.nan))


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_RECOVERY_ASYMMETRY_REGISTRY_076_150 = {
    "dra_076_up_body_21d": {"inputs": ["close", "open"], "func": dra_076_up_body_21d},
    "dra_077_dn_body_21d": {"inputs": ["close", "open"], "func": dra_077_dn_body_21d},
    "dra_078_body_asymmetry_ratio_21d": {"inputs": ["close", "open"], "func": dra_078_body_asymmetry_ratio_21d},
    "dra_079_upper_wick_21d": {"inputs": ["high", "close", "open"], "func": dra_079_upper_wick_21d},
    "dra_080_lower_wick_21d": {"inputs": ["low", "close", "open"], "func": dra_080_lower_wick_21d},
    "dra_081_wick_asymmetry_21d": {"inputs": ["high", "low", "close", "open"], "func": dra_081_wick_asymmetry_21d},
    "dra_082_close_location_value_21d": {"inputs": ["high", "low", "close"], "func": dra_082_close_location_value_21d},
    "dra_083_low_vs_high_move_21d": {"inputs": ["high", "low", "close"], "func": dra_083_low_vs_high_move_21d},
    "dra_084_dn_gap_count_21d": {"inputs": ["close", "open"], "func": dra_084_dn_gap_count_21d},
    "dra_085_up_gap_count_21d": {"inputs": ["close", "open"], "func": dra_085_up_gap_count_21d},
    "dra_086_vol_weighted_dn_ret_21d": {"inputs": ["close", "volume"], "func": dra_086_vol_weighted_dn_ret_21d},
    "dra_087_vol_weighted_up_ret_21d": {"inputs": ["close", "volume"], "func": dra_087_vol_weighted_up_ret_21d},
    "dra_088_vol_asymmetry_ratio_21d": {"inputs": ["close", "volume"], "func": dra_088_vol_asymmetry_ratio_21d},
    "dra_089_dn_day_volume_21d": {"inputs": ["close", "volume"], "func": dra_089_dn_day_volume_21d},
    "dra_090_up_day_volume_21d": {"inputs": ["close", "volume"], "func": dra_090_up_day_volume_21d},
    "dra_091_dn_up_volume_ratio_21d": {"inputs": ["close", "volume"], "func": dra_091_dn_up_volume_ratio_21d},
    "dra_092_dn_day_volume_63d": {"inputs": ["close", "volume"], "func": dra_092_dn_day_volume_63d},
    "dra_093_up_day_volume_63d": {"inputs": ["close", "volume"], "func": dra_093_up_day_volume_63d},
    "dra_094_dn_up_volume_ratio_63d": {"inputs": ["close", "volume"], "func": dra_094_dn_up_volume_ratio_63d},
    "dra_095_dn_volume_fraction_21d": {"inputs": ["close", "volume"], "func": dra_095_dn_volume_fraction_21d},
    "dra_096_ewm_avg_up_ret_21d": {"inputs": ["close"], "func": dra_096_ewm_avg_up_ret_21d},
    "dra_097_ewm_avg_dn_ret_21d": {"inputs": ["close"], "func": dra_097_ewm_avg_dn_ret_21d},
    "dra_098_ewm_up_dn_ratio_21d": {"inputs": ["close"], "func": dra_098_ewm_up_dn_ratio_21d},
    "dra_099_ewm_avg_up_ret_63d": {"inputs": ["close"], "func": dra_099_ewm_avg_up_ret_63d},
    "dra_100_ewm_avg_dn_ret_63d": {"inputs": ["close"], "func": dra_100_ewm_avg_dn_ret_63d},
    "dra_101_ewm_up_dn_ratio_63d": {"inputs": ["close"], "func": dra_101_ewm_up_dn_ratio_63d},
    "dra_102_ewm_dn_excess_21d": {"inputs": ["close"], "func": dra_102_ewm_dn_excess_21d},
    "dra_103_ewm_dn_excess_63d": {"inputs": ["close"], "func": dra_103_ewm_dn_excess_63d},
    "dra_104_ewm_up_ret_5d": {"inputs": ["close"], "func": dra_104_ewm_up_ret_5d},
    "dra_105_ewm_dn_ret_5d": {"inputs": ["close"], "func": dra_105_ewm_dn_ret_5d},
    "dra_106_dist_from_rolling_low_21d": {"inputs": ["close"], "func": dra_106_dist_from_rolling_low_21d},
    "dra_107_dist_from_rolling_low_63d": {"inputs": ["close"], "func": dra_107_dist_from_rolling_low_63d},
    "dra_108_dist_from_rolling_low_252d": {"inputs": ["close"], "func": dra_108_dist_from_rolling_low_252d},
    "dra_109_recovery_ratio_21d": {"inputs": ["close"], "func": dra_109_recovery_ratio_21d},
    "dra_110_recovery_ratio_63d": {"inputs": ["close"], "func": dra_110_recovery_ratio_63d},
    "dra_111_dist_from_high_vs_low_ratio_21d": {"inputs": ["close"], "func": dra_111_dist_from_high_vs_low_ratio_21d},
    "dra_112_dist_from_high_vs_low_ratio_63d": {"inputs": ["close"], "func": dra_112_dist_from_high_vs_low_ratio_63d},
    "dra_113_new_low_frequency_21d": {"inputs": ["close"], "func": dra_113_new_low_frequency_21d},
    "dra_114_new_high_frequency_21d": {"inputs": ["close"], "func": dra_114_new_high_frequency_21d},
    "dra_115_new_lo_vs_hi_freq_ratio_21d": {"inputs": ["close"], "func": dra_115_new_lo_vs_hi_freq_ratio_21d},
    "dra_116_dn_speed_ratio_21d": {"inputs": ["close"], "func": dra_116_dn_speed_ratio_21d},
    "dra_117_up_speed_ratio_21d": {"inputs": ["close"], "func": dra_117_up_speed_ratio_21d},
    "dra_118_speed_asymmetry_21d": {"inputs": ["close"], "func": dra_118_speed_asymmetry_21d},
    "dra_119_dn_speed_ratio_63d": {"inputs": ["close"], "func": dra_119_dn_speed_ratio_63d},
    "dra_120_up_speed_ratio_63d": {"inputs": ["close"], "func": dra_120_up_speed_ratio_63d},
    "dra_121_speed_asymmetry_63d": {"inputs": ["close"], "func": dra_121_speed_asymmetry_63d},
    "dra_122_dn_speed_ratio_252d": {"inputs": ["close"], "func": dra_122_dn_speed_ratio_252d},
    "dra_123_up_speed_ratio_252d": {"inputs": ["close"], "func": dra_123_up_speed_ratio_252d},
    "dra_124_speed_asymmetry_252d": {"inputs": ["close"], "func": dra_124_speed_asymmetry_252d},
    "dra_125_speed_asymmetry_change_21d_vs_63d": {"inputs": ["close"], "func": dra_125_speed_asymmetry_change_21d_vs_63d},
    "dra_126_ratchet_score_21d": {"inputs": ["close"], "func": dra_126_ratchet_score_21d},
    "dra_127_ratchet_score_63d": {"inputs": ["close"], "func": dra_127_ratchet_score_63d},
    "dra_128_ratchet_score_252d": {"inputs": ["close"], "func": dra_128_ratchet_score_252d},
    "dra_129_dn_amplitude_ratio_21d": {"inputs": ["close"], "func": dra_129_dn_amplitude_ratio_21d},
    "dra_130_dn_amplitude_ratio_63d": {"inputs": ["close"], "func": dra_130_dn_amplitude_ratio_63d},
    "dra_131_path_tortuosity_21d": {"inputs": ["close"], "func": dra_131_path_tortuosity_21d},
    "dra_132_path_tortuosity_63d": {"inputs": ["close"], "func": dra_132_path_tortuosity_63d},
    "dra_133_dn_tortuosity_21d": {"inputs": ["close"], "func": dra_133_dn_tortuosity_21d},
    "dra_134_up_tortuosity_21d": {"inputs": ["close"], "func": dra_134_up_tortuosity_21d},
    "dra_135_dn_vs_up_tortuosity_21d": {"inputs": ["close"], "func": dra_135_dn_vs_up_tortuosity_21d},
    "dra_136_gain_loss_ratio_zscore_63d": {"inputs": ["close"], "func": dra_136_gain_loss_ratio_zscore_63d},
    "dra_137_vol_asym_zscore_63d": {"inputs": ["close"], "func": dra_137_vol_asym_zscore_63d},
    "dra_138_speed_asym_zscore_63d": {"inputs": ["close"], "func": dra_138_speed_asym_zscore_63d},
    "dra_139_gain_loss_ratio_pct_rank_252d": {"inputs": ["close"], "func": dra_139_gain_loss_ratio_pct_rank_252d},
    "dra_140_vol_asym_pct_rank_252d": {"inputs": ["close"], "func": dra_140_vol_asym_pct_rank_252d},
    "dra_141_dn_participation_pct_rank_252d": {"inputs": ["close"], "func": dra_141_dn_participation_pct_rank_252d},
    "dra_142_gain_loss_ratio_expanding_pct_rank": {"inputs": ["close"], "func": dra_142_gain_loss_ratio_expanding_pct_rank},
    "dra_143_speed_asym_expanding_pct_rank": {"inputs": ["close"], "func": dra_143_speed_asym_expanding_pct_rank},
    "dra_144_streak_ratio_pct_rank_252d": {"inputs": ["close"], "func": dra_144_streak_ratio_pct_rank_252d},
    "dra_145_dn_count_zscore_252d": {"inputs": ["close"], "func": dra_145_dn_count_zscore_252d},
    "dra_146_asymmetry_composite_21d": {"inputs": ["close"], "func": dra_146_asymmetry_composite_21d},
    "dra_147_asymmetry_composite_63d": {"inputs": ["close"], "func": dra_147_asymmetry_composite_63d},
    "dra_148_asymmetry_short_vs_long_21_vs_252": {"inputs": ["close"], "func": dra_148_asymmetry_short_vs_long_21_vs_252},
    "dra_149_asymmetry_regime_flag_21d": {"inputs": ["close"], "func": dra_149_asymmetry_regime_flag_21d},
    "dra_150_dn_day_ret_vs_up_day_vol_ratio_21d": {"inputs": ["close"], "func": dra_150_dn_day_ret_vs_up_day_vol_ratio_21d},
}
