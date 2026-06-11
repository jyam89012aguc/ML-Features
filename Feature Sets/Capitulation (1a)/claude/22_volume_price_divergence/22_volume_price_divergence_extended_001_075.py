"""
22_volume_price_divergence — Extended Features 001-075
Domain: canonical money-flow / volume-price indicators missing from base files —
Chaikin Money Flow (CMF), Chaikin Oscillator, On-Balance Volume (OBV) divergence,
Volume Price Trend (VPT), Force Index, Money Flow Index (MFI), Twiggs Money Flow,
plus multi-period variants, sign/extreme/z-score/streak transforms, A/D Line
divergence vs price, money-flow composites, and rate-of-change of all above.
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _wilder_smooth(s: pd.Series, n: int) -> pd.Series:
    """Wilder smoothing: recursive EMA with alpha = 1/n."""
    return s.ewm(alpha=1.0 / n, min_periods=max(1, n // 2), adjust=False).mean()


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope_vec(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope using vectorised (no .apply) approach via rolling cov/var."""
    idx = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    cov = s.rolling(w, min_periods=max(2, w // 2)).cov(idx)
    var = idx.rolling(w, min_periods=max(2, w // 2)).var()
    return _safe_div(cov, var)


# ── Internal building blocks ──────────────────────────────────────────────────

def _ad_line(close: pd.Series, high: pd.Series, low: pd.Series,
             volume: pd.Series) -> pd.Series:
    """Accumulation/Distribution Line: cumsum of Money Flow Volume."""
    hl_range = (high - low).replace(0, np.nan)
    clv = _safe_div((close - low) - (high - close), hl_range)
    mfv = clv * volume
    return mfv.cumsum()


def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """On-Balance Volume: cumsum of signed volume."""
    sign = np.sign(close.diff(1).fillna(0))
    return (sign * volume).cumsum()


def _typical_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return (high + low + close) / 3.0


def _money_flow_volume(close: pd.Series, high: pd.Series, low: pd.Series,
                       volume: pd.Series) -> pd.Series:
    """Money Flow Volume = CLV * volume, CLV = ((C-L)-(H-C))/(H-L)."""
    hl_range = (high - low).replace(0, np.nan)
    clv = _safe_div((close - low) - (high - close), hl_range)
    return clv * volume


def _cmf(close: pd.Series, high: pd.Series, low: pd.Series,
         volume: pd.Series, n: int) -> pd.Series:
    """Chaikin Money Flow over n periods."""
    mfv = _money_flow_volume(close, high, low, volume)
    return _safe_div(_rolling_sum(mfv, n), _rolling_sum(volume, n))


def _vpt(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume Price Trend: cumsum of volume * pct_change(close)."""
    return (volume * close.pct_change(1).fillna(0)).cumsum()


def _force_index_raw(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Raw Force Index: close.diff(1) * volume."""
    return close.diff(1) * volume


def _mfi_raw(close: pd.Series, high: pd.Series, low: pd.Series,
             volume: pd.Series, n: int) -> pd.Series:
    """Money Flow Index over n periods."""
    tp = _typical_price(close, high, low)
    mf = tp * volume
    up = mf.where(tp > tp.shift(1), 0.0)
    dn = mf.where(tp < tp.shift(1), 0.0)
    pos_mf = _rolling_sum(up, n)
    neg_mf = _rolling_sum(dn, n)
    mfr = _safe_div(pos_mf, neg_mf)
    return 100.0 - _safe_div(pd.Series(100.0, index=close.index), 1.0 + mfr)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# ══ Group A (001-010): Chaikin Money Flow (CMF) ════════════════════════════════

def vpd_ext_001_cmf_21d(close: pd.Series, high: pd.Series, low: pd.Series,
                         volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 21 periods."""
    return _cmf(close, high, low, volume, _TD_MON)


def vpd_ext_002_cmf_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                         volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 63 periods."""
    return _cmf(close, high, low, volume, _TD_QTR)


def vpd_ext_003_cmf_21d_sign(close: pd.Series, high: pd.Series, low: pd.Series,
                               volume: pd.Series) -> pd.Series:
    """Sign of 21-period CMF (-1 / 0 / +1)."""
    return np.sign(_cmf(close, high, low, volume, _TD_MON))


def vpd_ext_004_cmf_21d_negative_flag(close: pd.Series, high: pd.Series,
                                       low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: CMF_21 < 0 (net selling pressure)."""
    return (_cmf(close, high, low, volume, _TD_MON) < 0).astype(float)


def vpd_ext_005_cmf_21d_zscore_252d(close: pd.Series, high: pd.Series,
                                     low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of CMF_21 vs trailing 252-day distribution."""
    cmf = _cmf(close, high, low, volume, _TD_MON)
    m = _rolling_mean(cmf, _TD_YEAR)
    s = _rolling_std(cmf, _TD_YEAR)
    return _safe_div(cmf - m, s)


def vpd_ext_006_cmf_63d_zscore_252d(close: pd.Series, high: pd.Series,
                                     low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of CMF_63 vs trailing 252-day distribution."""
    cmf = _cmf(close, high, low, volume, _TD_QTR)
    m = _rolling_mean(cmf, _TD_YEAR)
    s = _rolling_std(cmf, _TD_YEAR)
    return _safe_div(cmf - m, s)


def vpd_ext_007_cmf_21d_below_neg025_flag(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: CMF_21 < -0.25 (extreme selling pressure threshold)."""
    return (_cmf(close, high, low, volume, _TD_MON) < -0.25).astype(float)


def vpd_ext_008_cmf_21d_streak_negative(close: pd.Series, high: pd.Series,
                                         low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of consecutive trailing days where CMF_21 < 0."""
    cmf = _cmf(close, high, low, volume, _TD_MON)
    neg = (cmf < 0).astype(int)
    # vectorised streak count
    streak = neg * (neg.groupby((neg != neg.shift(1)).cumsum()).cumcount() + 1)
    return streak.astype(float)


def vpd_ext_009_cmf_21d_roc_5d(close: pd.Series, high: pd.Series,
                                 low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate of change of CMF_21."""
    return _cmf(close, high, low, volume, _TD_MON).diff(_TD_WEEK)


def vpd_ext_010_cmf_21d_minus_cmf_63d(close: pd.Series, high: pd.Series,
                                       low: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread: CMF_21 minus CMF_63 (short vs medium money-flow divergence)."""
    return _cmf(close, high, low, volume, _TD_MON) - _cmf(close, high, low, volume, _TD_QTR)


# ══ Group B (011-018): Chaikin Oscillator ══════════════════════════════════════

def vpd_ext_011_chaikin_oscillator(close: pd.Series, high: pd.Series,
                                    low: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Oscillator: EMA(3) of A/D Line minus EMA(10) of A/D Line."""
    ad = _ad_line(close, high, low, volume)
    return _ewm_mean(ad, 3) - _ewm_mean(ad, 10)


def vpd_ext_012_chaikin_osc_sign(close: pd.Series, high: pd.Series,
                                  low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign of the Chaikin Oscillator."""
    osc = vpd_ext_011_chaikin_oscillator(close, high, low, volume)
    return np.sign(osc)


def vpd_ext_013_chaikin_osc_negative_flag(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: Chaikin Oscillator < 0 (A/D momentum turning bearish)."""
    return (vpd_ext_011_chaikin_oscillator(close, high, low, volume) < 0).astype(float)


def vpd_ext_014_chaikin_osc_zscore_252d(close: pd.Series, high: pd.Series,
                                         low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of Chaikin Oscillator vs 252-day distribution."""
    osc = vpd_ext_011_chaikin_oscillator(close, high, low, volume)
    m = _rolling_mean(osc, _TD_YEAR)
    s = _rolling_std(osc, _TD_YEAR)
    return _safe_div(osc - m, s)


def vpd_ext_015_chaikin_osc_roc_5d(close: pd.Series, high: pd.Series,
                                    low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate of change of Chaikin Oscillator."""
    return vpd_ext_011_chaikin_oscillator(close, high, low, volume).diff(_TD_WEEK)


def vpd_ext_016_ad_line_slope_21d(close: pd.Series, high: pd.Series,
                                   low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of A/D Line over 21 days (direction of accumulation)."""
    ad = _ad_line(close, high, low, volume)
    return _linslope_vec(ad, _TD_MON)


def vpd_ext_017_ad_line_slope_63d(close: pd.Series, high: pd.Series,
                                   low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of A/D Line over 63 days."""
    ad = _ad_line(close, high, low, volume)
    return _linslope_vec(ad, _TD_QTR)


def vpd_ext_018_ad_price_divergence_21d(close: pd.Series, high: pd.Series,
                                         low: pd.Series, volume: pd.Series) -> pd.Series:
    """A/D Line slope (21d) minus normalised price slope (21d): A/D vs price divergence."""
    ad = _ad_line(close, high, low, volume)
    ad_slope = _linslope_vec(ad, _TD_MON)
    price_slope = _linslope_vec(close, _TD_MON)
    price_std = _rolling_std(close, _TD_MON).clip(lower=_EPS)
    ad_std = _rolling_std(ad, _TD_MON).clip(lower=_EPS)
    return _safe_div(ad_slope, ad_std) - _safe_div(price_slope, price_std)


# ══ Group C (019-028): OBV Divergence ══════════════════════════════════════════

def vpd_ext_019_obv_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of OBV over 21 days."""
    return _linslope_vec(_obv(close, volume), _TD_MON)


def vpd_ext_020_obv_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of OBV over 63 days."""
    return _linslope_vec(_obv(close, volume), _TD_QTR)


def vpd_ext_021_obv_slope_minus_price_slope_21d(close: pd.Series,
                                                  volume: pd.Series) -> pd.Series:
    """OBV slope (21d) minus normalised price slope (21d): OBV vs price divergence."""
    obv = _obv(close, volume)
    obv_slope = _linslope_vec(obv, _TD_MON)
    price_slope = _linslope_vec(close, _TD_MON)
    obv_std = _rolling_std(obv, _TD_MON).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_MON).clip(lower=_EPS)
    return _safe_div(obv_slope, obv_std) - _safe_div(price_slope, price_std)


def vpd_ext_022_obv_slope_minus_price_slope_63d(close: pd.Series,
                                                  volume: pd.Series) -> pd.Series:
    """OBV slope (63d) minus normalised price slope (63d)."""
    obv = _obv(close, volume)
    obv_slope = _linslope_vec(obv, _TD_QTR)
    price_slope = _linslope_vec(close, _TD_QTR)
    obv_std = _rolling_std(obv, _TD_QTR).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_QTR).clip(lower=_EPS)
    return _safe_div(obv_slope, obv_std) - _safe_div(price_slope, price_std)


def vpd_ext_023_obv_price_lower_low_divergence_21d(close: pd.Series,
                                                    volume: pd.Series) -> pd.Series:
    """Flag: price makes 21-day low but OBV does NOT make 21-day low (bullish divergence)."""
    obv = _obv(close, volume)
    price_21lo = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    obv_21lo = obv.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    price_newlow = (close < price_21lo)
    obv_not_newlow = (obv >= obv_21lo)
    return (price_newlow & obv_not_newlow).astype(float)


def vpd_ext_024_obv_price_lower_low_divergence_63d(close: pd.Series,
                                                    volume: pd.Series) -> pd.Series:
    """Flag: price makes 63-day low but OBV does NOT (bullish divergence on 63d horizon)."""
    obv = _obv(close, volume)
    price_lo = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    obv_lo = obv.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return ((close < price_lo) & (obv >= obv_lo)).astype(float)


def vpd_ext_025_obv_hidden_divergence_21d(close: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """Hidden bearish divergence: price higher high but OBV lower high over 21d."""
    obv = _obv(close, volume)
    price_hi = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    obv_hi = obv.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
    return ((close > price_hi) & (obv < obv_hi)).astype(float)


def vpd_ext_026_obv_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV level vs trailing 252-day distribution."""
    obv = _obv(close, volume)
    m = _rolling_mean(obv, _TD_YEAR)
    s = _rolling_std(obv, _TD_YEAR)
    return _safe_div(obv - m, s)


def vpd_ext_027_obv_roc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rate of change of OBV."""
    return _obv(close, volume).diff(_TD_MON)


def vpd_ext_028_obv_divergence_count_63d(close: pd.Series,
                                          volume: pd.Series) -> pd.Series:
    """Count of 21-day OBV-price lower-low divergence days in trailing 63 days."""
    flag = vpd_ext_023_obv_price_lower_low_divergence_21d(close, volume)
    return _rolling_sum(flag, _TD_QTR)


# ══ Group D (029-038): Volume Price Trend (VPT) ════════════════════════════════

def vpd_ext_029_vpt_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of VPT over 21 days."""
    return _linslope_vec(_vpt(close, volume), _TD_MON)


def vpd_ext_030_vpt_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of VPT over 63 days."""
    return _linslope_vec(_vpt(close, volume), _TD_QTR)


def vpd_ext_031_vpt_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of VPT level vs trailing 252-day distribution."""
    vpt = _vpt(close, volume)
    m = _rolling_mean(vpt, _TD_YEAR)
    s = _rolling_std(vpt, _TD_YEAR)
    return _safe_div(vpt - m, s)


def vpd_ext_032_vpt_roc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rate of change of VPT."""
    return _vpt(close, volume).diff(_TD_MON)


def vpd_ext_033_vpt_slope_minus_price_slope_21d(close: pd.Series,
                                                  volume: pd.Series) -> pd.Series:
    """VPT slope (21d) minus normalised price slope (21d): VPT vs price divergence."""
    vpt = _vpt(close, volume)
    vpt_slope = _linslope_vec(vpt, _TD_MON)
    price_slope = _linslope_vec(close, _TD_MON)
    vpt_std = _rolling_std(vpt, _TD_MON).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_MON).clip(lower=_EPS)
    return _safe_div(vpt_slope, vpt_std) - _safe_div(price_slope, price_std)


def vpd_ext_034_vpt_slope_minus_price_slope_63d(close: pd.Series,
                                                  volume: pd.Series) -> pd.Series:
    """VPT slope (63d) minus normalised price slope (63d)."""
    vpt = _vpt(close, volume)
    vpt_slope = _linslope_vec(vpt, _TD_QTR)
    price_slope = _linslope_vec(close, _TD_QTR)
    vpt_std = _rolling_std(vpt, _TD_QTR).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_QTR).clip(lower=_EPS)
    return _safe_div(vpt_slope, vpt_std) - _safe_div(price_slope, price_std)


def vpd_ext_035_vpt_negative_slope_flag_21d(close: pd.Series,
                                             volume: pd.Series) -> pd.Series:
    """Flag: VPT slope (21d) < 0 (selling pressure accumulating)."""
    return (vpd_ext_029_vpt_slope_21d(close, volume) < 0).astype(float)


def vpd_ext_036_vpt_roc_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate of change of VPT."""
    return _vpt(close, volume).diff(_TD_WEEK)


def vpd_ext_037_vpt_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA(21) of VPT (smoothed accumulation/distribution trend)."""
    return _ewm_mean(_vpt(close, volume), _TD_MON)


def vpd_ext_038_vpt_price_divergence_newlow_63d(close: pd.Series,
                                                  volume: pd.Series) -> pd.Series:
    """Flag: price makes 63-day low but VPT slope (21d) is non-negative."""
    price_lo = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    vpt_slope = vpd_ext_029_vpt_slope_21d(close, volume)
    return ((close < price_lo) & (vpt_slope >= 0)).astype(float)


# ══ Group E (039-048): Force Index ═════════════════════════════════════════════

def vpd_ext_039_force_index_raw(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Raw Force Index: close.diff(1) * volume (daily)."""
    return _force_index_raw(close, volume)


def vpd_ext_040_force_index_ema13(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Force Index smoothed with EMA(13) — standard Elder formulation."""
    return _ewm_mean(_force_index_raw(close, volume), 13)


def vpd_ext_041_force_index_ema2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Force Index smoothed with EMA(2) — short-term entry signal."""
    return _ewm_mean(_force_index_raw(close, volume), 2)


def vpd_ext_042_force_index_ema13_sign(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign of EMA(13) Force Index."""
    return np.sign(vpd_ext_040_force_index_ema13(close, volume))


def vpd_ext_043_force_index_ema13_negative_flag(close: pd.Series,
                                                 volume: pd.Series) -> pd.Series:
    """Flag: EMA(13) Force Index < 0 (bears in control)."""
    return (vpd_ext_040_force_index_ema13(close, volume) < 0).astype(float)


def vpd_ext_044_force_index_ema13_zscore_252d(close: pd.Series,
                                               volume: pd.Series) -> pd.Series:
    """Z-score of EMA(13) Force Index vs 252-day distribution."""
    fi = vpd_ext_040_force_index_ema13(close, volume)
    m = _rolling_mean(fi, _TD_YEAR)
    s = _rolling_std(fi, _TD_YEAR)
    return _safe_div(fi - m, s)


def vpd_ext_045_force_index_neg_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where EMA(13) Force Index < 0 (sustained bear pressure)."""
    fi = vpd_ext_040_force_index_ema13(close, volume)
    neg = (fi < 0).astype(int)
    streak = neg * (neg.groupby((neg != neg.shift(1)).cumsum()).cumcount() + 1)
    return streak.astype(float)


def vpd_ext_046_force_index_ema13_roc_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate of change of EMA(13) Force Index."""
    return vpd_ext_040_force_index_ema13(close, volume).diff(_TD_WEEK)


def vpd_ext_047_force_index_ema13_neg_count_21d(close: pd.Series,
                                                 volume: pd.Series) -> pd.Series:
    """Count of days with EMA(13) Force Index < 0 in trailing 21 days."""
    flag = vpd_ext_043_force_index_ema13_negative_flag(close, volume)
    return _rolling_sum(flag, _TD_MON)


def vpd_ext_048_force_index_ema13_neg_count_63d(close: pd.Series,
                                                 volume: pd.Series) -> pd.Series:
    """Count of days with EMA(13) Force Index < 0 in trailing 63 days."""
    flag = vpd_ext_043_force_index_ema13_negative_flag(close, volume)
    return _rolling_sum(flag, _TD_QTR)


# ══ Group F (049-058): Money Flow Index (MFI) ══════════════════════════════════

def vpd_ext_049_mfi_14d(close: pd.Series, high: pd.Series, low: pd.Series,
                         volume: pd.Series) -> pd.Series:
    """Money Flow Index over 14 periods."""
    return _mfi_raw(close, high, low, volume, 14)


def vpd_ext_050_mfi_21d(close: pd.Series, high: pd.Series, low: pd.Series,
                         volume: pd.Series) -> pd.Series:
    """Money Flow Index over 21 periods."""
    return _mfi_raw(close, high, low, volume, _TD_MON)


def vpd_ext_051_mfi_14d_oversold_flag(close: pd.Series, high: pd.Series,
                                       low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: MFI_14 < 20 (oversold — heavy selling with volume)."""
    return (_mfi_raw(close, high, low, volume, 14) < 20).astype(float)


def vpd_ext_052_mfi_21d_oversold_flag(close: pd.Series, high: pd.Series,
                                       low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: MFI_21 < 20 (oversold on monthly horizon)."""
    return (_mfi_raw(close, high, low, volume, _TD_MON) < 20).astype(float)


def vpd_ext_053_mfi_14d_zscore_252d(close: pd.Series, high: pd.Series,
                                     low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of MFI_14 vs 252-day distribution."""
    mfi = _mfi_raw(close, high, low, volume, 14)
    m = _rolling_mean(mfi, _TD_YEAR)
    s = _rolling_std(mfi, _TD_YEAR)
    return _safe_div(mfi - m, s)


def vpd_ext_054_mfi_14d_roc_5d(close: pd.Series, high: pd.Series,
                                 low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate of change of MFI_14."""
    return _mfi_raw(close, high, low, volume, 14).diff(_TD_WEEK)


def vpd_ext_055_mfi_14d_below_30_count_63d(close: pd.Series, high: pd.Series,
                                            low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days MFI_14 < 30 in trailing 63 days."""
    flag = (_mfi_raw(close, high, low, volume, 14) < 30).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def vpd_ext_056_mfi_price_divergence_21d(close: pd.Series, high: pd.Series,
                                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: price makes 21-day low but MFI_14 does NOT make 21-day low (bullish div)."""
    mfi = _mfi_raw(close, high, low, volume, 14)
    price_lo = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    mfi_lo = mfi.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    return ((close < price_lo) & (mfi >= mfi_lo)).astype(float)


def vpd_ext_057_mfi_21d_slope_21d(close: pd.Series, high: pd.Series,
                                   low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of MFI_21 over trailing 21 days."""
    return _linslope_vec(_mfi_raw(close, high, low, volume, _TD_MON), _TD_MON)


def vpd_ext_058_mfi_14d_neg_streak(close: pd.Series, high: pd.Series,
                                    low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with MFI_14 < 50 (money flow dominated by selling)."""
    flag = (_mfi_raw(close, high, low, volume, 14) < 50).astype(int)
    streak = flag * (flag.groupby((flag != flag.shift(1)).cumsum()).cumcount() + 1)
    return streak.astype(float)


# ══ Group G (059-065): Twiggs Money Flow ══════════════════════════════════════

def vpd_ext_059_twiggs_mf_21d(close: pd.Series, high: pd.Series,
                                low: pd.Series, volume: pd.Series) -> pd.Series:
    """Twiggs Money Flow (21d): Wilder-smoothed CMF refinement.
    Uses true range adjusted CLV: CLV_t = ((C - min(L, C_prev)) - (max(H, C_prev) - C))
                                         / (max(H, C_prev) - min(L, C_prev))
    then Wilder-smooth(MFV, 21) / Wilder-smooth(volume, 21).
    """
    prev_close = close.shift(1)
    adj_high = pd.concat([high, prev_close], axis=1).max(axis=1)
    adj_low = pd.concat([low, prev_close], axis=1).min(axis=1)
    adj_range = (adj_high - adj_low).replace(0, np.nan)
    clv_t = _safe_div((close - adj_low) - (adj_high - close), adj_range)
    mfv_t = clv_t * volume
    smooth_mfv = _wilder_smooth(mfv_t, _TD_MON)
    smooth_vol = _wilder_smooth(volume, _TD_MON)
    return _safe_div(smooth_mfv, smooth_vol)


def vpd_ext_060_twiggs_mf_21d_sign(close: pd.Series, high: pd.Series,
                                    low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign of Twiggs Money Flow (21d)."""
    return np.sign(vpd_ext_059_twiggs_mf_21d(close, high, low, volume))


def vpd_ext_061_twiggs_mf_21d_negative_flag(close: pd.Series, high: pd.Series,
                                             low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: Twiggs MF_21 < 0 (net distribution)."""
    return (vpd_ext_059_twiggs_mf_21d(close, high, low, volume) < 0).astype(float)


def vpd_ext_062_twiggs_mf_21d_zscore_252d(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of Twiggs MF_21 vs 252-day distribution."""
    tmf = vpd_ext_059_twiggs_mf_21d(close, high, low, volume)
    m = _rolling_mean(tmf, _TD_YEAR)
    s = _rolling_std(tmf, _TD_YEAR)
    return _safe_div(tmf - m, s)


def vpd_ext_063_twiggs_mf_21d_roc_5d(close: pd.Series, high: pd.Series,
                                      low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate of change of Twiggs MF_21."""
    return vpd_ext_059_twiggs_mf_21d(close, high, low, volume).diff(_TD_WEEK)


def vpd_ext_064_twiggs_mf_21d_neg_streak(close: pd.Series, high: pd.Series,
                                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where Twiggs MF_21 < 0."""
    neg = (vpd_ext_059_twiggs_mf_21d(close, high, low, volume) < 0).astype(int)
    streak = neg * (neg.groupby((neg != neg.shift(1)).cumsum()).cumcount() + 1)
    return streak.astype(float)


def vpd_ext_065_twiggs_vs_cmf_divergence_21d(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """Twiggs MF_21 minus CMF_21: divergence between Wilder-smoothed and raw CMF."""
    return vpd_ext_059_twiggs_mf_21d(close, high, low, volume) - _cmf(close, high, low, volume, _TD_MON)


# ══ Group H (066-075): Money-Flow Composites & Multi-Indicator Confluence ══════

def vpd_ext_066_moneyflow_composite_bearish_21d(close: pd.Series, high: pd.Series,
                                                 low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite bearish money-flow score (0-1): avg of CMF<0, Twiggs<0, Force<0 flags."""
    cmf_neg = (_cmf(close, high, low, volume, _TD_MON) < 0).astype(float)
    tmf_neg = (vpd_ext_059_twiggs_mf_21d(close, high, low, volume) < 0).astype(float)
    fi_neg = (_ewm_mean(_force_index_raw(close, volume), 13) < 0).astype(float)
    return (cmf_neg + tmf_neg + fi_neg) / 3.0


def vpd_ext_067_moneyflow_composite_zscore_21d(close: pd.Series, high: pd.Series,
                                                low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of CMF z-score, MFI z-score, and Twiggs z-score (21d): composite extremity."""
    cmf_z = vpd_ext_005_cmf_21d_zscore_252d(close, high, low, volume)
    mfi_z = vpd_ext_053_mfi_14d_zscore_252d(close, high, low, volume)
    tmf_z = vpd_ext_062_twiggs_mf_21d_zscore_252d(close, high, low, volume)
    return (cmf_z + mfi_z + tmf_z) / 3.0


def vpd_ext_068_five_indicator_confluence(close: pd.Series, high: pd.Series,
                                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count (0-5) of indicators in bearish zone: CMF<0, Chaikin Osc<0, OBV slope<0,
    Force Index<0, MFI<50."""
    cmf_b = (_cmf(close, high, low, volume, _TD_MON) < 0).astype(float)
    cho_b = (vpd_ext_011_chaikin_oscillator(close, high, low, volume) < 0).astype(float)
    obv_b = (_linslope_vec(_obv(close, volume), _TD_MON) < 0).astype(float)
    fi_b = (_ewm_mean(_force_index_raw(close, volume), 13) < 0).astype(float)
    mfi_b = (_mfi_raw(close, high, low, volume, 14) < 50).astype(float)
    return cmf_b + cho_b + obv_b + fi_b + mfi_b


def vpd_ext_069_volup_pricedown_intensity_21d(close: pd.Series, high: pd.Series,
                                               low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of CMF values on days where price falls and volume rises (21d window).
    Captures magnitude of money-flow on capitulation days."""
    cmf_daily = _money_flow_volume(close, high, low, volume)
    ret = close.pct_change(1)
    vol_up = volume > volume.shift(1)
    price_dn = ret < 0
    flagged = cmf_daily.where(price_dn & vol_up, 0.0)
    return _rolling_sum(flagged, _TD_MON)


def vpd_ext_070_mfi_cmf_divergence_21d(close: pd.Series, high: pd.Series,
                                        low: pd.Series, volume: pd.Series) -> pd.Series:
    """MFI_14 (normalised 0-1) minus CMF_21 (typically -1 to 1): inter-indicator divergence."""
    mfi_norm = _mfi_raw(close, high, low, volume, 14) / 100.0
    cmf21 = _cmf(close, high, low, volume, _TD_MON)
    return mfi_norm - cmf21


def vpd_ext_071_ad_line_price_divergence_63d(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: price 63d slope < 0 but A/D Line 63d slope >= 0 (classic A/D vs price div)."""
    ad = _ad_line(close, high, low, volume)
    ad_slope = _linslope_vec(ad, _TD_QTR)
    price_slope = _linslope_vec(close, _TD_QTR)
    return ((price_slope < 0) & (ad_slope >= 0)).astype(float)


def vpd_ext_072_cmf_obv_vpt_bear_count(close: pd.Series, high: pd.Series,
                                        low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count (0-3): CMF_21<0, OBV slope(21d)<0, VPT slope(21d)<0 — triple bear signal."""
    cmf_b = (_cmf(close, high, low, volume, _TD_MON) < 0).astype(float)
    obv_b = (vpd_ext_019_obv_slope_21d(close, volume) < 0).astype(float)
    vpt_b = (vpd_ext_029_vpt_slope_21d(close, volume) < 0).astype(float)
    return cmf_b + obv_b + vpt_b


def vpd_ext_073_moneyflow_roc_composite_5d(close: pd.Series, high: pd.Series,
                                            low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average 5d ROC across CMF_21, OBV, and VPT (normalised): composite money-flow momentum."""
    cmf_roc = _cmf(close, high, low, volume, _TD_MON).diff(_TD_WEEK)
    obv = _obv(close, volume)
    obv_roc = _safe_div(obv.diff(_TD_WEEK), _rolling_std(obv, _TD_YEAR).clip(lower=_EPS))
    vpt = _vpt(close, volume)
    vpt_roc = _safe_div(vpt.diff(_TD_WEEK), _rolling_std(vpt, _TD_YEAR).clip(lower=_EPS))
    return (cmf_roc + obv_roc + vpt_roc) / 3.0


def vpd_ext_074_extreme_distress_moneyflow_flag(close: pd.Series, high: pd.Series,
                                                 low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: all 4 indicators in extreme bear zone simultaneously.
    CMF_21 < -0.2, MFI_14 < 30, Force Index EMA(13) < 0, Twiggs MF < 0."""
    cmf_ex = (_cmf(close, high, low, volume, _TD_MON) < -0.2).astype(float)
    mfi_ex = (_mfi_raw(close, high, low, volume, 14) < 30).astype(float)
    fi_ex = (_ewm_mean(_force_index_raw(close, volume), 13) < 0).astype(float)
    tmf_ex = (vpd_ext_059_twiggs_mf_21d(close, high, low, volume) < 0).astype(float)
    return (cmf_ex * mfi_ex * fi_ex * tmf_ex)


def vpd_ext_075_moneyflow_composite_pct_rank_252d(close: pd.Series, high: pd.Series,
                                                   low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank (252d) of 5-indicator bearish confluence count (vpd_ext_068)."""
    score = vpd_ext_068_five_indicator_confluence(close, high, low, volume)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PRICE_DIVERGENCE_EXTENDED_REGISTRY_001_075 = {
    "vpd_ext_001_cmf_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_001_cmf_21d},
    "vpd_ext_002_cmf_63d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_002_cmf_63d},
    "vpd_ext_003_cmf_21d_sign": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_003_cmf_21d_sign},
    "vpd_ext_004_cmf_21d_negative_flag": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_004_cmf_21d_negative_flag},
    "vpd_ext_005_cmf_21d_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_005_cmf_21d_zscore_252d},
    "vpd_ext_006_cmf_63d_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_006_cmf_63d_zscore_252d},
    "vpd_ext_007_cmf_21d_below_neg025_flag": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_007_cmf_21d_below_neg025_flag},
    "vpd_ext_008_cmf_21d_streak_negative": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_008_cmf_21d_streak_negative},
    "vpd_ext_009_cmf_21d_roc_5d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_009_cmf_21d_roc_5d},
    "vpd_ext_010_cmf_21d_minus_cmf_63d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_010_cmf_21d_minus_cmf_63d},
    "vpd_ext_011_chaikin_oscillator": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_011_chaikin_oscillator},
    "vpd_ext_012_chaikin_osc_sign": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_012_chaikin_osc_sign},
    "vpd_ext_013_chaikin_osc_negative_flag": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_013_chaikin_osc_negative_flag},
    "vpd_ext_014_chaikin_osc_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_014_chaikin_osc_zscore_252d},
    "vpd_ext_015_chaikin_osc_roc_5d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_015_chaikin_osc_roc_5d},
    "vpd_ext_016_ad_line_slope_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_016_ad_line_slope_21d},
    "vpd_ext_017_ad_line_slope_63d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_017_ad_line_slope_63d},
    "vpd_ext_018_ad_price_divergence_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_018_ad_price_divergence_21d},
    "vpd_ext_019_obv_slope_21d": {"inputs": ["close", "volume"], "func": vpd_ext_019_obv_slope_21d},
    "vpd_ext_020_obv_slope_63d": {"inputs": ["close", "volume"], "func": vpd_ext_020_obv_slope_63d},
    "vpd_ext_021_obv_slope_minus_price_slope_21d": {"inputs": ["close", "volume"], "func": vpd_ext_021_obv_slope_minus_price_slope_21d},
    "vpd_ext_022_obv_slope_minus_price_slope_63d": {"inputs": ["close", "volume"], "func": vpd_ext_022_obv_slope_minus_price_slope_63d},
    "vpd_ext_023_obv_price_lower_low_divergence_21d": {"inputs": ["close", "volume"], "func": vpd_ext_023_obv_price_lower_low_divergence_21d},
    "vpd_ext_024_obv_price_lower_low_divergence_63d": {"inputs": ["close", "volume"], "func": vpd_ext_024_obv_price_lower_low_divergence_63d},
    "vpd_ext_025_obv_hidden_divergence_21d": {"inputs": ["close", "volume"], "func": vpd_ext_025_obv_hidden_divergence_21d},
    "vpd_ext_026_obv_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_ext_026_obv_zscore_252d},
    "vpd_ext_027_obv_roc_21d": {"inputs": ["close", "volume"], "func": vpd_ext_027_obv_roc_21d},
    "vpd_ext_028_obv_divergence_count_63d": {"inputs": ["close", "volume"], "func": vpd_ext_028_obv_divergence_count_63d},
    "vpd_ext_029_vpt_slope_21d": {"inputs": ["close", "volume"], "func": vpd_ext_029_vpt_slope_21d},
    "vpd_ext_030_vpt_slope_63d": {"inputs": ["close", "volume"], "func": vpd_ext_030_vpt_slope_63d},
    "vpd_ext_031_vpt_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_ext_031_vpt_zscore_252d},
    "vpd_ext_032_vpt_roc_21d": {"inputs": ["close", "volume"], "func": vpd_ext_032_vpt_roc_21d},
    "vpd_ext_033_vpt_slope_minus_price_slope_21d": {"inputs": ["close", "volume"], "func": vpd_ext_033_vpt_slope_minus_price_slope_21d},
    "vpd_ext_034_vpt_slope_minus_price_slope_63d": {"inputs": ["close", "volume"], "func": vpd_ext_034_vpt_slope_minus_price_slope_63d},
    "vpd_ext_035_vpt_negative_slope_flag_21d": {"inputs": ["close", "volume"], "func": vpd_ext_035_vpt_negative_slope_flag_21d},
    "vpd_ext_036_vpt_roc_5d": {"inputs": ["close", "volume"], "func": vpd_ext_036_vpt_roc_5d},
    "vpd_ext_037_vpt_ewm21": {"inputs": ["close", "volume"], "func": vpd_ext_037_vpt_ewm21},
    "vpd_ext_038_vpt_price_divergence_newlow_63d": {"inputs": ["close", "volume"], "func": vpd_ext_038_vpt_price_divergence_newlow_63d},
    "vpd_ext_039_force_index_raw": {"inputs": ["close", "volume"], "func": vpd_ext_039_force_index_raw},
    "vpd_ext_040_force_index_ema13": {"inputs": ["close", "volume"], "func": vpd_ext_040_force_index_ema13},
    "vpd_ext_041_force_index_ema2": {"inputs": ["close", "volume"], "func": vpd_ext_041_force_index_ema2},
    "vpd_ext_042_force_index_ema13_sign": {"inputs": ["close", "volume"], "func": vpd_ext_042_force_index_ema13_sign},
    "vpd_ext_043_force_index_ema13_negative_flag": {"inputs": ["close", "volume"], "func": vpd_ext_043_force_index_ema13_negative_flag},
    "vpd_ext_044_force_index_ema13_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_ext_044_force_index_ema13_zscore_252d},
    "vpd_ext_045_force_index_neg_streak": {"inputs": ["close", "volume"], "func": vpd_ext_045_force_index_neg_streak},
    "vpd_ext_046_force_index_ema13_roc_5d": {"inputs": ["close", "volume"], "func": vpd_ext_046_force_index_ema13_roc_5d},
    "vpd_ext_047_force_index_ema13_neg_count_21d": {"inputs": ["close", "volume"], "func": vpd_ext_047_force_index_ema13_neg_count_21d},
    "vpd_ext_048_force_index_ema13_neg_count_63d": {"inputs": ["close", "volume"], "func": vpd_ext_048_force_index_ema13_neg_count_63d},
    "vpd_ext_049_mfi_14d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_049_mfi_14d},
    "vpd_ext_050_mfi_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_050_mfi_21d},
    "vpd_ext_051_mfi_14d_oversold_flag": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_051_mfi_14d_oversold_flag},
    "vpd_ext_052_mfi_21d_oversold_flag": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_052_mfi_21d_oversold_flag},
    "vpd_ext_053_mfi_14d_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_053_mfi_14d_zscore_252d},
    "vpd_ext_054_mfi_14d_roc_5d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_054_mfi_14d_roc_5d},
    "vpd_ext_055_mfi_14d_below_30_count_63d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_055_mfi_14d_below_30_count_63d},
    "vpd_ext_056_mfi_price_divergence_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_056_mfi_price_divergence_21d},
    "vpd_ext_057_mfi_21d_slope_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_057_mfi_21d_slope_21d},
    "vpd_ext_058_mfi_14d_neg_streak": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_058_mfi_14d_neg_streak},
    "vpd_ext_059_twiggs_mf_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_059_twiggs_mf_21d},
    "vpd_ext_060_twiggs_mf_21d_sign": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_060_twiggs_mf_21d_sign},
    "vpd_ext_061_twiggs_mf_21d_negative_flag": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_061_twiggs_mf_21d_negative_flag},
    "vpd_ext_062_twiggs_mf_21d_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_062_twiggs_mf_21d_zscore_252d},
    "vpd_ext_063_twiggs_mf_21d_roc_5d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_063_twiggs_mf_21d_roc_5d},
    "vpd_ext_064_twiggs_mf_21d_neg_streak": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_064_twiggs_mf_21d_neg_streak},
    "vpd_ext_065_twiggs_vs_cmf_divergence_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_065_twiggs_vs_cmf_divergence_21d},
    "vpd_ext_066_moneyflow_composite_bearish_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_066_moneyflow_composite_bearish_21d},
    "vpd_ext_067_moneyflow_composite_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_067_moneyflow_composite_zscore_21d},
    "vpd_ext_068_five_indicator_confluence": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_068_five_indicator_confluence},
    "vpd_ext_069_volup_pricedown_intensity_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_069_volup_pricedown_intensity_21d},
    "vpd_ext_070_mfi_cmf_divergence_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_070_mfi_cmf_divergence_21d},
    "vpd_ext_071_ad_line_price_divergence_63d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_071_ad_line_price_divergence_63d},
    "vpd_ext_072_cmf_obv_vpt_bear_count": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_072_cmf_obv_vpt_bear_count},
    "vpd_ext_073_moneyflow_roc_composite_5d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_073_moneyflow_roc_composite_5d},
    "vpd_ext_074_extreme_distress_moneyflow_flag": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_074_extreme_distress_moneyflow_flag},
    "vpd_ext_075_moneyflow_composite_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_ext_075_moneyflow_composite_pct_rank_252d},
}
