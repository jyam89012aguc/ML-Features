"""
07_peak_to_trough — Base Features 076-150
Domain: peak-to-trough ratios, swing legs, amplitude, open/high/low vs peak-trough
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


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _peak_trough_span(s: pd.Series, w: int):
    """Returns (peak, trough) rolling within window w."""
    peak = _rolling_max(s, w)
    trough = _rolling_min(s, w)
    return peak, trough


def _recovery_fraction(close: pd.Series, peak: pd.Series, trough: pd.Series) -> pd.Series:
    """(close - trough) / (peak - trough), guarded for zero span."""
    span = peak - trough
    return _safe_div(close - trough, span)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-090): Open / high / low vs rolling peak and trough ---

def ptt_076_open_recovery_fraction_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Recovery fraction using open price vs 252-day close peak and close trough."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _recovery_fraction(open, pk, tr)


def ptt_077_open_recovery_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Recovery fraction using open price vs 63-day close peak/trough."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    return _recovery_fraction(open, pk, tr)


def ptt_078_high_to_252d_peak_ratio(close: pd.Series, high: pd.Series) -> pd.Series:
    """Intraday high relative to 252-day close peak (near-peak probe)."""
    pk = _rolling_max(close, _TD_YEAR)
    return _safe_div(high, pk)


def ptt_079_low_to_252d_trough_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low relative to 252-day close trough (trough probe)."""
    tr = _rolling_min(close, _TD_YEAR)
    return _safe_div(low, tr)


def ptt_080_high_to_63d_peak_ratio(close: pd.Series, high: pd.Series) -> pd.Series:
    """Intraday high relative to 63-day close peak."""
    pk = _rolling_max(close, _TD_QTR)
    return _safe_div(high, pk)


def ptt_081_low_to_63d_trough_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low relative to 63-day close trough."""
    tr = _rolling_min(close, _TD_QTR)
    return _safe_div(low, tr)


def ptt_082_open_to_252d_peak_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """Open price relative to 252-day close peak."""
    pk = _rolling_max(close, _TD_YEAR)
    return _safe_div(open, pk)


def ptt_083_open_to_252d_trough_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """Open price relative to 252-day close trough."""
    tr = _rolling_min(close, _TD_YEAR)
    return _safe_div(open, tr)


def ptt_084_intraday_span_vs_ptt_span_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current intraday high-low range as fraction of 252-day close peak-trough span."""
    intraday_span = high - low
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    ptt_span = pk - tr
    return _safe_div(intraday_span, ptt_span)


def ptt_085_high_recovery_fraction_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Recovery fraction using intraday high vs 252-day close peak/trough."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _recovery_fraction(high, pk, tr)


def ptt_086_low_recovery_fraction_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Recovery fraction using intraday low vs 252-day close peak/trough."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _recovery_fraction(low, pk, tr)


def ptt_087_high_minus_low_vs_ptt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily range (high-low) as fraction of 63-day close peak-trough span."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    span = pk - tr
    return _safe_div(high - low, span)


def ptt_088_close_minus_open_vs_ptt_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Daily close-open move as fraction of 252-day close peak-trough span."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    span = pk - tr
    return _safe_div(close - open, span)


def ptt_089_open_above_midpoint_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if open is above 252-day peak-trough midpoint."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    mid = (pk + tr) / 2.0
    return (open >= mid).astype(float)


def ptt_090_low_below_trough_threshold_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: 1 if today's low is at or below the 252-day close trough."""
    tr = _rolling_min(close, _TD_YEAR)
    return (low <= tr).astype(float)


# --- Group H (091-105): Swing leg counting and amplitude ---

def ptt_091_up_leg_count_63d(close: pd.Series) -> pd.Series:
    """Count of distinct up-leg days (positive daily close changes) in 63-day window."""
    up = (close.diff(1) > 0).astype(float)
    return _rolling_sum(up, _TD_QTR)


def ptt_092_down_leg_count_63d(close: pd.Series) -> pd.Series:
    """Count of distinct down-leg days (negative daily close changes) in 63-day window."""
    down = (close.diff(1) < 0).astype(float)
    return _rolling_sum(down, _TD_QTR)


def ptt_093_up_down_leg_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of up-leg days to down-leg days in 63-day window."""
    up = (close.diff(1) > 0).astype(float)
    down = (close.diff(1) < 0).astype(float)
    return _safe_div(_rolling_sum(up, _TD_QTR), _rolling_sum(down, _TD_QTR))


def ptt_094_up_leg_count_252d(close: pd.Series) -> pd.Series:
    """Count of up-leg days in 252-day window."""
    up = (close.diff(1) > 0).astype(float)
    return _rolling_sum(up, _TD_YEAR)


def ptt_095_down_leg_count_252d(close: pd.Series) -> pd.Series:
    """Count of down-leg days in 252-day window."""
    down = (close.diff(1) < 0).astype(float)
    return _rolling_sum(down, _TD_YEAR)


def ptt_096_up_down_leg_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of up-leg to down-leg days in 252-day window."""
    up = (close.diff(1) > 0).astype(float)
    down = (close.diff(1) < 0).astype(float)
    return _safe_div(_rolling_sum(up, _TD_YEAR), _rolling_sum(down, _TD_YEAR))


def ptt_097_avg_up_day_size_252d(close: pd.Series) -> pd.Series:
    """Mean daily return on up days over trailing 252 days."""
    ret = close.pct_change(1)
    up_ret = ret.where(ret > 0, other=0.0)
    up_count = (ret > 0).astype(float)
    total_up = _rolling_sum(up_ret, _TD_YEAR)
    count_up = _rolling_sum(up_count, _TD_YEAR)
    return _safe_div(total_up, count_up)


def ptt_098_avg_down_day_size_252d(close: pd.Series) -> pd.Series:
    """Mean absolute daily return on down days over trailing 252 days."""
    ret = close.pct_change(1)
    dn_ret = ret.where(ret < 0, other=0.0).abs()
    dn_count = (ret < 0).astype(float)
    total_dn = _rolling_sum(dn_ret, _TD_YEAR)
    count_dn = _rolling_sum(dn_count, _TD_YEAR)
    return _safe_div(total_dn, count_dn)


def ptt_099_up_vs_down_amplitude_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of average up-day size to average down-day size (252d)."""
    ret = close.pct_change(1)
    up_ret = ret.where(ret > 0, other=0.0)
    dn_ret = ret.where(ret < 0, other=0.0).abs()
    up_cnt = (ret > 0).astype(float)
    dn_cnt = (ret < 0).astype(float)
    avg_up = _safe_div(_rolling_sum(up_ret, _TD_YEAR), _rolling_sum(up_cnt, _TD_YEAR))
    avg_dn = _safe_div(_rolling_sum(dn_ret, _TD_YEAR), _rolling_sum(dn_cnt, _TD_YEAR))
    return _safe_div(avg_up, avg_dn)


def ptt_100_largest_up_day_252d(close: pd.Series) -> pd.Series:
    """Largest single-day gain in trailing 252-day window."""
    ret = close.pct_change(1)
    return ret.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()


def ptt_101_largest_down_day_252d(close: pd.Series) -> pd.Series:
    """Largest single-day loss (most negative return) in trailing 252-day window."""
    ret = close.pct_change(1)
    return ret.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()


def ptt_102_largest_swing_amplitude_252d(close: pd.Series) -> pd.Series:
    """Amplitude of largest completed up-then-down or down-then-up swing in 252d.
    Defined as max(|close[t] - close[t-1]|) / trough over window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    span = pk - tr
    return _safe_div(span, tr)


def ptt_103_consecutive_down_days_max_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-close days within trailing 252-day window."""
    down = (close.diff(1) < 0).astype(int)

    def max_consec(x):
        max_run = 0
        cur_run = 0
        for v in x:
            if v == 1:
                cur_run += 1
                if cur_run > max_run:
                    max_run = cur_run
            else:
                cur_run = 0
        return float(max_run)

    return down.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(max_consec, raw=True)


def ptt_104_consecutive_up_days_max_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive up-close days within trailing 252-day window."""
    up = (close.diff(1) > 0).astype(int)

    def max_consec(x):
        max_run = 0
        cur_run = 0
        for v in x:
            if v == 1:
                cur_run += 1
                if cur_run > max_run:
                    max_run = cur_run
            else:
                cur_run = 0
        return float(max_run)

    return up.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(max_consec, raw=True)


def ptt_105_swing_direction_bias_252d(close: pd.Series) -> pd.Series:
    """Net direction bias: (up days - down days) / total days in 252d window."""
    ret = close.pct_change(1)
    up = (ret > 0).astype(float)
    dn = (ret < 0).astype(float)
    net = _rolling_sum(up - dn, _TD_YEAR)
    total = _rolling_sum((ret != 0).astype(float), _TD_YEAR)
    return _safe_div(net, total)


# --- Group I (106-120): Volume-weighted peak-trough features ---

def ptt_106_vwap_recovery_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recovery fraction of VWAP (volume-weighted avg price) relative to 252-day peak/trough of VWAP."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    pk = _rolling_max(vwap, _TD_YEAR)
    tr = _rolling_min(vwap, _TD_YEAR)
    return _recovery_fraction(vwap, pk, tr)


def ptt_107_vwap_to_252d_trough_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling VWAP divided by 252-day close trough."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    tr = _rolling_min(close, _TD_YEAR)
    return _safe_div(vwap, tr)


def ptt_108_vwap_to_252d_peak_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling VWAP divided by 252-day close peak."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    pk = _rolling_max(close, _TD_YEAR)
    return _safe_div(vwap, pk)


def ptt_109_volume_weighted_span_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day peak-trough span weighted by relative volume (span x vol_ratio)."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    span_pct = _safe_div(pk - tr, tr)
    vol_ratio = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return span_pct * vol_ratio


def ptt_110_high_volume_day_near_trough_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252d high-volume days (top decile) that occurred within 2% of trough."""
    tr = _rolling_min(close, _TD_YEAR)
    near_trough = (close <= tr * 1.02).astype(float)
    vol_threshold = _rolling_mean(volume, _TD_YEAR) * 1.5
    high_vol = (volume >= vol_threshold).astype(float)
    high_vol_trough = _rolling_sum(high_vol * near_trough, _TD_YEAR)
    high_vol_total = _rolling_sum(high_vol, _TD_YEAR)
    return _safe_div(high_vol_trough, high_vol_total)


def ptt_111_volume_surge_on_trough_day_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 252d trough day relative to 252d mean volume (capitulation spike proxy)."""
    tr = _rolling_min(close, _TD_YEAR)
    at_trough = (close == tr).astype(float)
    vol_on_trough = _rolling_sum(volume * at_trough, _TD_YEAR)
    trough_days = _rolling_sum(at_trough, _TD_YEAR).replace(0, np.nan)
    avg_vol_trough = vol_on_trough / trough_days
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(avg_vol_trough, avg_vol)


def ptt_112_volume_surge_on_peak_day_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 252d peak day relative to 252d mean volume."""
    pk = _rolling_max(close, _TD_YEAR)
    at_peak = (close == pk).astype(float)
    vol_on_peak = _rolling_sum(volume * at_peak, _TD_YEAR)
    peak_days = _rolling_sum(at_peak, _TD_YEAR).replace(0, np.nan)
    avg_vol_peak = vol_on_peak / peak_days
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(avg_vol_peak, avg_vol)


def ptt_113_volume_weighted_recovery_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted recovery fraction: sum(rf * vol) / sum(vol) over 252d window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    return _safe_div(_rolling_sum(rf * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))


def ptt_114_volume_ratio_trough_half_vs_peak_half_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of volume in lower half of 252d range to upper half."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    mid = (pk + tr) / 2.0
    low_half_vol = _rolling_sum(volume.where(close < mid, other=0.0), _TD_YEAR)
    high_half_vol = _rolling_sum(volume.where(close >= mid, other=0.0), _TD_YEAR)
    return _safe_div(low_half_vol, high_half_vol)


def ptt_115_on_balance_volume_vs_trough_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (on-balance volume) relative to its 252-day trough."""
    direction = np.sign(close.diff(1))
    obv = (volume * direction).fillna(0).cumsum()
    obv_tr = _rolling_min(obv, _TD_YEAR)
    return _safe_div(obv - obv_tr, obv_tr.abs() + _EPS)


def ptt_116_on_balance_volume_recovery_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recovery fraction of OBV within its 252-day peak-trough range."""
    direction = np.sign(close.diff(1))
    obv = (volume * direction).fillna(0).cumsum()
    pk = _rolling_max(obv, _TD_YEAR)
    tr = _rolling_min(obv, _TD_YEAR)
    span = pk - tr
    return _safe_div(obv - tr, span)


def ptt_117_volume_trend_during_decline_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation of volume with negative returns over trailing 252 days."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, other=np.nan)
    down_vol_mean = _rolling_mean(down_vol.fillna(0), _TD_YEAR)
    all_vol_mean = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(down_vol_mean, all_vol_mean)


def ptt_118_vwap_span_pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Peak-trough span (pct) of 252d rolling VWAP."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    pk = _rolling_max(vwap, _TD_YEAR)
    tr = _rolling_min(vwap, _TD_YEAR)
    return _safe_div(pk - tr, tr)


def ptt_119_volume_below_trough_threshold_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume on days within 5% of 252-day close trough, as pct of 252d total."""
    tr = _rolling_min(close, _TD_YEAR)
    near_trough = (close <= tr * 1.05).astype(float)
    vol_near_tr = _rolling_sum(volume * near_trough, _TD_YEAR)
    vol_total = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(vol_near_tr, vol_total)


def ptt_120_volume_above_peak_threshold_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume on days within 5% of 252-day close peak, as pct of 252d total."""
    pk = _rolling_max(close, _TD_YEAR)
    near_peak = (close >= pk * 0.95).astype(float)
    vol_near_pk = _rolling_sum(volume * near_peak, _TD_YEAR)
    vol_total = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(vol_near_pk, vol_total)


# --- Group J (121-135): ATR, true-range, and volatility-normalized PTT ---

def ptt_121_atr_normalized_ptt_span_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day peak-trough span normalized by 252-day ATR."""
    atr = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _safe_div(pk - tr, atr)


def ptt_122_atr_normalized_ptt_span_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day peak-trough span normalized by 63-day ATR."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    pk, tr = _peak_trough_span(close, _TD_QTR)
    return _safe_div(pk - tr, atr)


def ptt_123_recovery_fraction_atr_adj_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Recovery fraction of 252-day range, adjusted for ATR (volatility-scaled)."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    atr = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    span = pk - tr
    vol_adj_span = _safe_div(span, atr)
    return rf * vol_adj_span


def ptt_124_atr_fraction_of_ptt_span_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day ATR as fraction of 252-day peak-trough span."""
    atr = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    return _safe_div(atr, pk - tr)


def ptt_125_intraday_span_vs_atr_ratio_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of current intraday range (high-low) to 252-day ATR."""
    atr = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    return _safe_div(high - low, atr)


def ptt_126_ptt_span_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 252-day peak-trough percent span over trailing 252-day window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    span_pct = _safe_div(pk - tr, tr)
    return _zscore_rolling(span_pct, _TD_YEAR)


def ptt_127_ptt_span_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252-day peak-trough span within trailing 252-day window."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    span_pct = _safe_div(pk - tr, tr)
    return _rolling_rank_pct(span_pct, _TD_YEAR)


def ptt_128_realized_vol_vs_ptt_span_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252-day realized daily vol (annualized) to 252-day log peak-trough span."""
    vol = _rolling_std(_daily_ret(close), _TD_YEAR) * np.sqrt(_TD_YEAR)
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    log_span = _log_safe(pk) - _log_safe(tr)
    return _safe_div(vol, log_span)


def ptt_129_ewm_peak_to_close_ratio_21d(close: pd.Series) -> pd.Series:
    """EMA-smoothed (21d span) peak-to-close ratio: EMA(close/rolling_max_21d)."""
    pk = _rolling_max(close, _TD_MON)
    ratio = _safe_div(close, pk)
    return _ewm_mean(ratio, _TD_MON)


def ptt_130_ewm_trough_to_close_ratio_21d(close: pd.Series) -> pd.Series:
    """EMA-smoothed (21d span) trough-to-close ratio: EMA(close/rolling_min_21d)."""
    tr = _rolling_min(close, _TD_MON)
    ratio = _safe_div(close, tr)
    return _ewm_mean(ratio, _TD_MON)


def ptt_131_ewm_recovery_fraction_63d(close: pd.Series) -> pd.Series:
    """EMA-smoothed (63d span) recovery fraction of 63-day range."""
    pk, tr = _peak_trough_span(close, _TD_QTR)
    rf = _recovery_fraction(close, pk, tr)
    return _ewm_mean(rf, _TD_QTR)


def ptt_132_ewm_recovery_fraction_252d(close: pd.Series) -> pd.Series:
    """EMA-smoothed (252d span) recovery fraction of 252-day range."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    return _ewm_mean(rf, _TD_YEAR)


def ptt_133_rolling_beta_close_to_peak_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d OLS slope of close changes vs peak changes (beta of recovery)."""
    d_close = close.diff(1)
    d_peak = _rolling_max(close, _TD_YEAR).diff(1)
    cov = _rolling_mean(d_close * d_peak, _TD_YEAR) - _rolling_mean(d_close, _TD_YEAR) * _rolling_mean(d_peak, _TD_YEAR)
    var = _rolling_std(d_peak, _TD_YEAR) ** 2
    return _safe_div(cov, var)


def ptt_134_ptt_span_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252-day peak-trough span (how extreme relative to history)."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    span_pct = _safe_div(pk - tr, tr)
    m = span_pct.expanding(min_periods=5).mean()
    sd = span_pct.expanding(min_periods=5).std()
    return _safe_div(span_pct - m, sd)


def ptt_135_ptt_span_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day peak-trough span."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    span_pct = _safe_div(pk - tr, tr)
    return span_pct.expanding(min_periods=5).rank(pct=True)


# --- Group K (136-150): Advanced multi-window and composite PTT features ---

def ptt_136_ptt_ratio_trend_21d(close: pd.Series) -> pd.Series:
    """21-day simple trend of the 63-day peak-trough ratio (.diff(1) EWM)."""
    r63 = _safe_div(_rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return r63.diff(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def ptt_137_recovery_fraction_acceleration_21d(close: pd.Series) -> pd.Series:
    """21-day mean of the 1-day diff of 252d recovery fraction (pace of retracement)."""
    rf = _recovery_fraction(close, _rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return rf.diff(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def ptt_138_peak_minus_trough_to_close_vol_252d(close: pd.Series) -> pd.Series:
    """252-day (peak - trough) / (close * 252d vol): multi-normalization severity."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    denom = close * vol
    return _safe_div(pk - tr, denom)


def ptt_139_close_below_prior_trough_252d(close: pd.Series) -> pd.Series:
    """Binary: 1 if close < prior period (63d lagged) 252-day close trough."""
    prior_trough = _rolling_min(close, _TD_YEAR).shift(_TD_QTR)
    return (close < prior_trough).astype(float)


def ptt_140_ptt_ratio_mean_reversion_252d(close: pd.Series) -> pd.Series:
    """Deviation of current 252d PTT ratio from its trailing 252-day mean."""
    r252 = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    mean_r = _rolling_mean(r252, _TD_YEAR)
    return r252 - mean_r


def ptt_141_close_position_quintile_252d(close: pd.Series) -> pd.Series:
    """Quintile (0-4) of close within 252-day peak-trough range (0=bottom, 4=top)."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    return (rf * 5.0).clip(0, 4.999).apply(np.floor)


def ptt_142_close_position_decile_252d(close: pd.Series) -> pd.Series:
    """Decile (0-9) of close within 252-day peak-trough range."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    rf = _recovery_fraction(close, pk, tr)
    return (rf * 10.0).clip(0, 9.999).apply(np.floor)


def ptt_143_half_year_vs_annual_ptt_ratio_diff(close: pd.Series) -> pd.Series:
    """126d peak-trough ratio minus 252d peak-trough ratio (short-term amplitude surge)."""
    r126 = _safe_div(_rolling_max(close, _TD_HALF), _rolling_min(close, _TD_HALF))
    r252 = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return r126 - r252


def ptt_144_recovery_fraction_ema_cross_signal(close: pd.Series) -> pd.Series:
    """Difference between EMA-21d and EMA-63d of 252d recovery fraction."""
    rf = _recovery_fraction(close, _rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    ema21 = _ewm_mean(rf, _TD_MON)
    ema63 = _ewm_mean(rf, _TD_QTR)
    return ema21 - ema63


def ptt_145_log_ptt_ratio_zscore_expanding(close: pd.Series) -> pd.Series:
    """Expanding z-score of log(252d peak/trough)."""
    pk, tr = _peak_trough_span(close, _TD_YEAR)
    log_r = _log_safe(pk) - _log_safe(tr)
    m = log_r.expanding(min_periods=5).mean()
    sd = log_r.expanding(min_periods=5).std()
    return _safe_div(log_r - m, sd)


def ptt_146_trough_depth_vs_mean_price_252d(close: pd.Series) -> pd.Series:
    """252-day close trough relative to 252-day mean close (how far below average)."""
    tr = _rolling_min(close, _TD_YEAR)
    mu = _rolling_mean(close, _TD_YEAR)
    return _safe_div(tr - mu, mu)


def ptt_147_peak_height_vs_mean_price_252d(close: pd.Series) -> pd.Series:
    """252-day close peak relative to 252-day mean close."""
    pk = _rolling_max(close, _TD_YEAR)
    mu = _rolling_mean(close, _TD_YEAR)
    return _safe_div(pk - mu, mu)


def ptt_148_trough_to_mean_to_peak_balance_252d(close: pd.Series) -> pd.Series:
    """Asymmetry: (peak - mean) / (mean - trough), 252d (>1 = more upside than downside)."""
    pk = _rolling_max(close, _TD_YEAR)
    tr = _rolling_min(close, _TD_YEAR)
    mu = _rolling_mean(close, _TD_YEAR)
    return _safe_div(pk - mu, mu - tr)


def ptt_149_recovery_fraction_vol_band_252d(close: pd.Series) -> pd.Series:
    """Recovery fraction of close within 252d vol-bands [mean-2sd, mean+2sd]."""
    mu = _rolling_mean(close, _TD_YEAR)
    sd = _rolling_std(close, _TD_YEAR)
    lower = mu - 2.0 * sd
    upper = mu + 2.0 * sd
    return _safe_div(close - lower, upper - lower)


def ptt_150_multi_window_ptt_composite(close: pd.Series) -> pd.Series:
    """Composite PTT ratio: 40% 21d + 35% 63d + 25% 252d (multi-scale swing magnitude)."""
    r21 = _safe_div(_rolling_max(close, _TD_MON), _rolling_min(close, _TD_MON))
    r63 = _safe_div(_rolling_max(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    r252 = _safe_div(_rolling_max(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))
    return 0.40 * r21 + 0.35 * r63 + 0.25 * r252


# ── Registry ──────────────────────────────────────────────────────────────────

PEAK_TO_TROUGH_REGISTRY_076_150 = {
    "ptt_076_open_recovery_fraction_252d": {"inputs": ["close", "open"], "func": ptt_076_open_recovery_fraction_252d},
    "ptt_077_open_recovery_fraction_63d": {"inputs": ["close", "open"], "func": ptt_077_open_recovery_fraction_63d},
    "ptt_078_high_to_252d_peak_ratio": {"inputs": ["close", "high"], "func": ptt_078_high_to_252d_peak_ratio},
    "ptt_079_low_to_252d_trough_ratio": {"inputs": ["close", "low"], "func": ptt_079_low_to_252d_trough_ratio},
    "ptt_080_high_to_63d_peak_ratio": {"inputs": ["close", "high"], "func": ptt_080_high_to_63d_peak_ratio},
    "ptt_081_low_to_63d_trough_ratio": {"inputs": ["close", "low"], "func": ptt_081_low_to_63d_trough_ratio},
    "ptt_082_open_to_252d_peak_ratio": {"inputs": ["close", "open"], "func": ptt_082_open_to_252d_peak_ratio},
    "ptt_083_open_to_252d_trough_ratio": {"inputs": ["close", "open"], "func": ptt_083_open_to_252d_trough_ratio},
    "ptt_084_intraday_span_vs_ptt_span_252d": {"inputs": ["close", "high", "low"], "func": ptt_084_intraday_span_vs_ptt_span_252d},
    "ptt_085_high_recovery_fraction_252d": {"inputs": ["close", "high"], "func": ptt_085_high_recovery_fraction_252d},
    "ptt_086_low_recovery_fraction_252d": {"inputs": ["close", "low"], "func": ptt_086_low_recovery_fraction_252d},
    "ptt_087_high_minus_low_vs_ptt_63d": {"inputs": ["close", "high", "low"], "func": ptt_087_high_minus_low_vs_ptt_63d},
    "ptt_088_close_minus_open_vs_ptt_252d": {"inputs": ["close", "open"], "func": ptt_088_close_minus_open_vs_ptt_252d},
    "ptt_089_open_above_midpoint_252d": {"inputs": ["close", "open"], "func": ptt_089_open_above_midpoint_252d},
    "ptt_090_low_below_trough_threshold_252d": {"inputs": ["close", "low"], "func": ptt_090_low_below_trough_threshold_252d},
    "ptt_091_up_leg_count_63d": {"inputs": ["close"], "func": ptt_091_up_leg_count_63d},
    "ptt_092_down_leg_count_63d": {"inputs": ["close"], "func": ptt_092_down_leg_count_63d},
    "ptt_093_up_down_leg_ratio_63d": {"inputs": ["close"], "func": ptt_093_up_down_leg_ratio_63d},
    "ptt_094_up_leg_count_252d": {"inputs": ["close"], "func": ptt_094_up_leg_count_252d},
    "ptt_095_down_leg_count_252d": {"inputs": ["close"], "func": ptt_095_down_leg_count_252d},
    "ptt_096_up_down_leg_ratio_252d": {"inputs": ["close"], "func": ptt_096_up_down_leg_ratio_252d},
    "ptt_097_avg_up_day_size_252d": {"inputs": ["close"], "func": ptt_097_avg_up_day_size_252d},
    "ptt_098_avg_down_day_size_252d": {"inputs": ["close"], "func": ptt_098_avg_down_day_size_252d},
    "ptt_099_up_vs_down_amplitude_ratio_252d": {"inputs": ["close"], "func": ptt_099_up_vs_down_amplitude_ratio_252d},
    "ptt_100_largest_up_day_252d": {"inputs": ["close"], "func": ptt_100_largest_up_day_252d},
    "ptt_101_largest_down_day_252d": {"inputs": ["close"], "func": ptt_101_largest_down_day_252d},
    "ptt_102_largest_swing_amplitude_252d": {"inputs": ["close"], "func": ptt_102_largest_swing_amplitude_252d},
    "ptt_103_consecutive_down_days_max_252d": {"inputs": ["close"], "func": ptt_103_consecutive_down_days_max_252d},
    "ptt_104_consecutive_up_days_max_252d": {"inputs": ["close"], "func": ptt_104_consecutive_up_days_max_252d},
    "ptt_105_swing_direction_bias_252d": {"inputs": ["close"], "func": ptt_105_swing_direction_bias_252d},
    "ptt_106_vwap_recovery_fraction_252d": {"inputs": ["close", "volume"], "func": ptt_106_vwap_recovery_fraction_252d},
    "ptt_107_vwap_to_252d_trough_ratio": {"inputs": ["close", "volume"], "func": ptt_107_vwap_to_252d_trough_ratio},
    "ptt_108_vwap_to_252d_peak_ratio": {"inputs": ["close", "volume"], "func": ptt_108_vwap_to_252d_peak_ratio},
    "ptt_109_volume_weighted_span_252d": {"inputs": ["close", "volume"], "func": ptt_109_volume_weighted_span_252d},
    "ptt_110_high_volume_day_near_trough_fraction_252d": {"inputs": ["close", "volume"], "func": ptt_110_high_volume_day_near_trough_fraction_252d},
    "ptt_111_volume_surge_on_trough_day_252d": {"inputs": ["close", "volume"], "func": ptt_111_volume_surge_on_trough_day_252d},
    "ptt_112_volume_surge_on_peak_day_252d": {"inputs": ["close", "volume"], "func": ptt_112_volume_surge_on_peak_day_252d},
    "ptt_113_volume_weighted_recovery_fraction_252d": {"inputs": ["close", "volume"], "func": ptt_113_volume_weighted_recovery_fraction_252d},
    "ptt_114_volume_ratio_trough_half_vs_peak_half_252d": {"inputs": ["close", "volume"], "func": ptt_114_volume_ratio_trough_half_vs_peak_half_252d},
    "ptt_115_on_balance_volume_vs_trough_252d": {"inputs": ["close", "volume"], "func": ptt_115_on_balance_volume_vs_trough_252d},
    "ptt_116_on_balance_volume_recovery_fraction_252d": {"inputs": ["close", "volume"], "func": ptt_116_on_balance_volume_recovery_fraction_252d},
    "ptt_117_volume_trend_during_decline_252d": {"inputs": ["close", "volume"], "func": ptt_117_volume_trend_during_decline_252d},
    "ptt_118_vwap_span_pct_252d": {"inputs": ["close", "volume"], "func": ptt_118_vwap_span_pct_252d},
    "ptt_119_volume_below_trough_threshold_252d": {"inputs": ["close", "volume"], "func": ptt_119_volume_below_trough_threshold_252d},
    "ptt_120_volume_above_peak_threshold_252d": {"inputs": ["close", "volume"], "func": ptt_120_volume_above_peak_threshold_252d},
    "ptt_121_atr_normalized_ptt_span_252d": {"inputs": ["close", "high", "low"], "func": ptt_121_atr_normalized_ptt_span_252d},
    "ptt_122_atr_normalized_ptt_span_63d": {"inputs": ["close", "high", "low"], "func": ptt_122_atr_normalized_ptt_span_63d},
    "ptt_123_recovery_fraction_atr_adj_252d": {"inputs": ["close", "high", "low"], "func": ptt_123_recovery_fraction_atr_adj_252d},
    "ptt_124_atr_fraction_of_ptt_span_252d": {"inputs": ["close", "high", "low"], "func": ptt_124_atr_fraction_of_ptt_span_252d},
    "ptt_125_intraday_span_vs_atr_ratio_252d": {"inputs": ["close", "high", "low"], "func": ptt_125_intraday_span_vs_atr_ratio_252d},
    "ptt_126_ptt_span_zscore_252d": {"inputs": ["close"], "func": ptt_126_ptt_span_zscore_252d},
    "ptt_127_ptt_span_pct_rank_252d": {"inputs": ["close"], "func": ptt_127_ptt_span_pct_rank_252d},
    "ptt_128_realized_vol_vs_ptt_span_252d": {"inputs": ["close"], "func": ptt_128_realized_vol_vs_ptt_span_252d},
    "ptt_129_ewm_peak_to_close_ratio_21d": {"inputs": ["close"], "func": ptt_129_ewm_peak_to_close_ratio_21d},
    "ptt_130_ewm_trough_to_close_ratio_21d": {"inputs": ["close"], "func": ptt_130_ewm_trough_to_close_ratio_21d},
    "ptt_131_ewm_recovery_fraction_63d": {"inputs": ["close"], "func": ptt_131_ewm_recovery_fraction_63d},
    "ptt_132_ewm_recovery_fraction_252d": {"inputs": ["close"], "func": ptt_132_ewm_recovery_fraction_252d},
    "ptt_133_rolling_beta_close_to_peak_252d": {"inputs": ["close"], "func": ptt_133_rolling_beta_close_to_peak_252d},
    "ptt_134_ptt_span_expanding_zscore": {"inputs": ["close"], "func": ptt_134_ptt_span_expanding_zscore},
    "ptt_135_ptt_span_expanding_pct_rank": {"inputs": ["close"], "func": ptt_135_ptt_span_expanding_pct_rank},
    "ptt_136_ptt_ratio_trend_21d": {"inputs": ["close"], "func": ptt_136_ptt_ratio_trend_21d},
    "ptt_137_recovery_fraction_acceleration_21d": {"inputs": ["close"], "func": ptt_137_recovery_fraction_acceleration_21d},
    "ptt_138_peak_minus_trough_to_close_vol_252d": {"inputs": ["close"], "func": ptt_138_peak_minus_trough_to_close_vol_252d},
    "ptt_139_close_below_prior_trough_252d": {"inputs": ["close"], "func": ptt_139_close_below_prior_trough_252d},
    "ptt_140_ptt_ratio_mean_reversion_252d": {"inputs": ["close"], "func": ptt_140_ptt_ratio_mean_reversion_252d},
    "ptt_141_close_position_quintile_252d": {"inputs": ["close"], "func": ptt_141_close_position_quintile_252d},
    "ptt_142_close_position_decile_252d": {"inputs": ["close"], "func": ptt_142_close_position_decile_252d},
    "ptt_143_half_year_vs_annual_ptt_ratio_diff": {"inputs": ["close"], "func": ptt_143_half_year_vs_annual_ptt_ratio_diff},
    "ptt_144_recovery_fraction_ema_cross_signal": {"inputs": ["close"], "func": ptt_144_recovery_fraction_ema_cross_signal},
    "ptt_145_log_ptt_ratio_zscore_expanding": {"inputs": ["close"], "func": ptt_145_log_ptt_ratio_zscore_expanding},
    "ptt_146_trough_depth_vs_mean_price_252d": {"inputs": ["close"], "func": ptt_146_trough_depth_vs_mean_price_252d},
    "ptt_147_peak_height_vs_mean_price_252d": {"inputs": ["close"], "func": ptt_147_peak_height_vs_mean_price_252d},
    "ptt_148_trough_to_mean_to_peak_balance_252d": {"inputs": ["close"], "func": ptt_148_trough_to_mean_to_peak_balance_252d},
    "ptt_149_recovery_fraction_vol_band_252d": {"inputs": ["close"], "func": ptt_149_recovery_fraction_vol_band_252d},
    "ptt_150_multi_window_ptt_composite": {"inputs": ["close"], "func": ptt_150_multi_window_ptt_composite},
}
