"""
32_momentum_divergence — Extended Features 001-075
Domain: price makes a new low while a momentum indicator does NOT — extended oscillator coverage
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — extended oscillator divergence, triple-swing, class grading,
                confirmation combos, time/density, volume-price divergence, A/D divergence,
                multi-oscillator confluence depth, ROC/acceleration variants
All features are backward-looking only; no forward information.

NET-NEW vs existing 200:
  ext_001-010  MFI divergence (Money Flow Index — volume-weighted RSI)
  ext_011-020  Ultimate Oscillator divergence
  ext_021-028  CMO (Chande Momentum Oscillator) divergence
  ext_029-036  TSI (True Strength Index) divergence
  ext_037-044  Triple/multi-swing divergence: divergence persisting across 3+ successive lows
  ext_045-050  Divergence-magnitude slope: rate the divergence gap is widening
  ext_051-056  Class A/B/C divergence grading (strength tiers)
  ext_057-062  Divergence confirmation: divergence + oversold + high volume
  ext_063-067  Time-since-last-divergence and divergence density measures (new metrics)
  ext_068-071  Volume-vs-price divergence and A/D line divergence
  ext_072-075  Multi-oscillator confluence depth and ROC acceleration variants
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _price_new_low(close: pd.Series, w: int) -> pd.Series:
    """Boolean: close makes a new w-period low vs prior bar (trailing only)."""
    prior_min = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (close < prior_min).astype(float)


def _osc_lower_low(osc: pd.Series, w: int) -> pd.Series:
    """Boolean: oscillator IS at a new w-period low."""
    prior_min = osc.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (osc < prior_min).astype(float)


def _pct_rank(s: pd.Series, w: int) -> pd.Series:
    """Rolling percentile rank within window w."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder RSI, returns 0-100 series."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period // 2, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period // 2, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - _safe_div(pd.Series(100.0, index=close.index), 1.0 + rs)


def _mfi(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series, period: int = 14) -> pd.Series:
    """Money Flow Index: volume-weighted RSI on typical price."""
    tp = (high + low + close) / 3.0
    mf = tp * volume
    delta_tp = tp.diff(1)
    pos_mf = mf.where(delta_tp > 0, 0.0)
    neg_mf = mf.where(delta_tp < 0, 0.0)
    pos_sum = pos_mf.rolling(period, min_periods=max(1, period // 2)).sum()
    neg_sum = (-neg_mf).rolling(period, min_periods=max(1, period // 2)).sum()
    mfr = _safe_div(pos_sum, neg_sum.clip(lower=_EPS))
    return 100.0 - _safe_div(pd.Series(100.0, index=close.index), 1.0 + mfr)


def _ultimate_oscillator(close: pd.Series, high: pd.Series, low: pd.Series,
                          p1: int = 7, p2: int = 14, p3: int = 28) -> pd.Series:
    """Ultimate Oscillator using three periods (trailing-only, no lookahead)."""
    prev_close = close.shift(1)
    true_low = pd.concat([low, prev_close], axis=1).min(axis=1)
    true_high = pd.concat([high, prev_close], axis=1).max(axis=1)
    true_range = true_high - true_low
    buying_pressure = close - true_low

    def _avg(bp, tr, p):
        bp_sum = bp.rolling(p, min_periods=max(1, p // 2)).sum()
        tr_sum = tr.rolling(p, min_periods=max(1, p // 2)).sum()
        return _safe_div(bp_sum, tr_sum.clip(lower=_EPS))

    avg1 = _avg(buying_pressure, true_range, p1)
    avg2 = _avg(buying_pressure, true_range, p2)
    avg3 = _avg(buying_pressure, true_range, p3)
    return 100.0 * (4.0 * avg1 + 2.0 * avg2 + avg3) / 7.0


def _cmo(close: pd.Series, period: int = 14) -> pd.Series:
    """Chande Momentum Oscillator: ranges -100 to +100."""
    delta = close.diff(1)
    up = delta.clip(lower=0.0)
    dn = (-delta).clip(lower=0.0)
    up_sum = up.rolling(period, min_periods=max(1, period // 2)).sum()
    dn_sum = dn.rolling(period, min_periods=max(1, period // 2)).sum()
    return _safe_div(up_sum - dn_sum, (up_sum + dn_sum).clip(lower=_EPS)) * 100.0


def _tsi(close: pd.Series, fast: int = 13, slow: int = 25) -> pd.Series:
    """True Strength Index: double-smoothed momentum, ranges roughly -100 to +100."""
    delta = close.diff(1)
    abs_delta = delta.abs()
    smooth1 = _ewm_mean(delta, slow)
    smooth2 = _ewm_mean(smooth1, fast)
    abs_smooth1 = _ewm_mean(abs_delta, slow)
    abs_smooth2 = _ewm_mean(abs_smooth1, fast)
    return _safe_div(smooth2, abs_smooth2.clip(lower=_EPS)) * 100.0


def _ad_line(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Accumulation/Distribution Line (Chaikin A/D)."""
    clv_num = (close - low) - (high - close)
    clv_den = (high - low).replace(0, np.nan)
    clv = clv_num / clv_den
    return (clv * volume).cumsum()


def _days_since_flag(flag: pd.Series) -> pd.Series:
    """Bars since the most recent 1 in a binary series; NaN before first occurrence."""
    arr = flag.values.astype(float)
    out = np.full(len(arr), np.nan)
    running = np.nan
    for i in range(len(arr)):
        if arr[i] == 1.0:
            running = float(i)
        if not np.isnan(running):
            out[i] = float(i) - running
    return pd.Series(out, index=flag.index)


# ── Feature functions ext_001-010: MFI Divergence ────────────────────────────

def mdv_ext_001_mfi_divg_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but MFI(14) does NOT make a new low (regular bullish div)."""
    price_nl = _price_new_low(close, _TD_MON)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_nl = _osc_lower_low(mfi, _TD_MON)
    return price_nl * (1.0 - mfi_nl)


def mdv_ext_002_mfi_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but MFI(14) does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_nl = _osc_lower_low(mfi, _TD_QTR)
    return price_nl * (1.0 - mfi_nl)


def mdv_ext_003_mfi_divg_flag_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: price 252-day new low but MFI(14) does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_YEAR)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_nl = _osc_lower_low(mfi, _TD_YEAR)
    return price_nl * (1.0 - mfi_nl)


def mdv_ext_004_mfi_gap_at_price_low_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """MFI(14) above its 63-day min when price makes a 63-day new low (gap magnitude)."""
    price_nl = _price_new_low(close, _TD_QTR)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_floor = _rolling_min(mfi, _TD_QTR)
    return (mfi - mfi_floor).clip(lower=0.0) * price_nl


def mdv_ext_005_mfi_pctrank_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """MFI(14) pct-rank minus price pct-rank over 63-day window."""
    mfi = _mfi(close, high, low, volume, 14)
    return _pct_rank(mfi, _TD_QTR) - _pct_rank(close, _TD_QTR)


def mdv_ext_006_mfi_pctrank_spread_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """MFI(14) pct-rank minus price pct-rank over 252-day window."""
    mfi = _mfi(close, high, low, volume, 14)
    return _pct_rank(mfi, _TD_YEAR) - _pct_rank(close, _TD_YEAR)


def mdv_ext_007_mfi_divg_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of MFI bullish divergence flags in trailing 252 days."""
    flag = mdv_ext_002_mfi_divg_flag_63d(close, high, low, volume)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_ext_008_mfi_divg_magnitude_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Price drawdown fraction minus MFI drawdown fraction from 63-day high."""
    mfi = _mfi(close, high, low, volume, 14)
    price_hi = _rolling_max(close, _TD_QTR)
    mfi_hi = _rolling_max(mfi, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    mfi_range = (mfi_hi - _rolling_min(mfi, _TD_QTR)).clip(lower=_EPS)
    mfi_dd = _safe_div(mfi_hi - mfi, mfi_range)
    return price_dd - mfi_dd


def mdv_ext_009_mfi_divg_gap_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of MFI gap at price-new-low vs 63-day rolling mean/std."""
    price_nl = _price_new_low(close, _TD_QTR)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_floor = _rolling_min(mfi, _TD_QTR)
    gap = (mfi - mfi_floor).clip(lower=0.0) * price_nl
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    return _safe_div(gap - m, s.clip(lower=_EPS))


def mdv_ext_010_mfi_divg_recency_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since last MFI bullish divergence flag (63-day detection window)."""
    flag = mdv_ext_002_mfi_divg_flag_63d(close, high, low, volume)
    return _days_since_flag(flag)


# ── Feature functions ext_011-020: Ultimate Oscillator Divergence ─────────────

def mdv_ext_011_uo_divg_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but Ultimate Oscillator does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_MON)
    uo = _ultimate_oscillator(close, high, low)
    uo_nl = _osc_lower_low(uo, _TD_MON)
    return price_nl * (1.0 - uo_nl)


def mdv_ext_012_uo_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but Ultimate Oscillator does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    uo = _ultimate_oscillator(close, high, low)
    uo_nl = _osc_lower_low(uo, _TD_QTR)
    return price_nl * (1.0 - uo_nl)


def mdv_ext_013_uo_divg_flag_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 252-day new low but Ultimate Oscillator does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_YEAR)
    uo = _ultimate_oscillator(close, high, low)
    uo_nl = _osc_lower_low(uo, _TD_YEAR)
    return price_nl * (1.0 - uo_nl)


def mdv_ext_014_uo_gap_at_price_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ultimate Oscillator above its 63-day min when price makes 63-day new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    uo = _ultimate_oscillator(close, high, low)
    uo_floor = _rolling_min(uo, _TD_QTR)
    return (uo - uo_floor).clip(lower=0.0) * price_nl


def mdv_ext_015_uo_pctrank_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ultimate Oscillator pct-rank minus price pct-rank over 63-day window."""
    uo = _ultimate_oscillator(close, high, low)
    return _pct_rank(uo, _TD_QTR) - _pct_rank(close, _TD_QTR)


def mdv_ext_016_uo_pctrank_spread_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ultimate Oscillator pct-rank minus price pct-rank over 252-day window."""
    uo = _ultimate_oscillator(close, high, low)
    return _pct_rank(uo, _TD_YEAR) - _pct_rank(close, _TD_YEAR)


def mdv_ext_017_uo_divg_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Ultimate Oscillator bullish divergence flags in trailing 252 days."""
    flag = mdv_ext_012_uo_divg_flag_63d(close, high, low)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_ext_018_uo_divg_magnitude_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Price drawdown fraction minus UO drawdown fraction from 63-day peak."""
    uo = _ultimate_oscillator(close, high, low)
    price_hi = _rolling_max(close, _TD_QTR)
    uo_hi = _rolling_max(uo, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    uo_range = (uo_hi - _rolling_min(uo, _TD_QTR)).clip(lower=_EPS)
    uo_dd = _safe_div(uo_hi - uo, uo_range)
    return price_dd - uo_dd


def mdv_ext_019_uo_divg_gap_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Ultimate Oscillator gap at price-new-low vs 63-day mean/std."""
    price_nl = _price_new_low(close, _TD_QTR)
    uo = _ultimate_oscillator(close, high, low)
    uo_floor = _rolling_min(uo, _TD_QTR)
    gap = (uo - uo_floor).clip(lower=0.0) * price_nl
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    return _safe_div(gap - m, s.clip(lower=_EPS))


def mdv_ext_020_uo_divg_recency_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last Ultimate Oscillator bullish divergence flag (63-day detection)."""
    flag = mdv_ext_012_uo_divg_flag_63d(close, high, low)
    return _days_since_flag(flag)


# ── Feature functions ext_021-028: CMO Divergence ────────────────────────────

def mdv_ext_021_cmo_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but CMO(14) does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_MON)
    cmo = _cmo(close, 14)
    cmo_nl = _osc_lower_low(cmo, _TD_MON)
    return price_nl * (1.0 - cmo_nl)


def mdv_ext_022_cmo_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but CMO(14) does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    cmo = _cmo(close, 14)
    cmo_nl = _osc_lower_low(cmo, _TD_QTR)
    return price_nl * (1.0 - cmo_nl)


def mdv_ext_023_cmo_divg_flag_252d(close: pd.Series) -> pd.Series:
    """Binary: price 252-day new low but CMO(14) does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_YEAR)
    cmo = _cmo(close, 14)
    cmo_nl = _osc_lower_low(cmo, _TD_YEAR)
    return price_nl * (1.0 - cmo_nl)


def mdv_ext_024_cmo_gap_at_price_low_63d(close: pd.Series) -> pd.Series:
    """CMO(14) above its 63-day min when price makes a 63-day new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    cmo = _cmo(close, 14)
    cmo_floor = _rolling_min(cmo, _TD_QTR)
    return (cmo - cmo_floor).clip(lower=0.0) * price_nl


def mdv_ext_025_cmo_pctrank_spread_63d(close: pd.Series) -> pd.Series:
    """CMO(14) pct-rank minus price pct-rank over 63-day window."""
    cmo = _cmo(close, 14)
    return _pct_rank(cmo, _TD_QTR) - _pct_rank(close, _TD_QTR)


def mdv_ext_026_cmo_pctrank_spread_252d(close: pd.Series) -> pd.Series:
    """CMO(14) pct-rank minus price pct-rank over 252-day window."""
    cmo = _cmo(close, 14)
    return _pct_rank(cmo, _TD_YEAR) - _pct_rank(close, _TD_YEAR)


def mdv_ext_027_cmo_divg_count_252d(close: pd.Series) -> pd.Series:
    """Count of CMO bullish divergence flags in trailing 252 days."""
    flag = mdv_ext_022_cmo_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_ext_028_cmo_divg_magnitude_63d(close: pd.Series) -> pd.Series:
    """Price drawdown fraction minus CMO drawdown fraction from 63-day high."""
    cmo = _cmo(close, 14)
    price_hi = _rolling_max(close, _TD_QTR)
    cmo_hi = _rolling_max(cmo, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    cmo_range = (cmo_hi - _rolling_min(cmo, _TD_QTR)).clip(lower=_EPS)
    cmo_dd = _safe_div(cmo_hi - cmo, cmo_range)
    return price_dd - cmo_dd


# ── Feature functions ext_029-036: TSI Divergence ────────────────────────────

def mdv_ext_029_tsi_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but TSI does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_MON)
    tsi = _tsi(close)
    tsi_nl = _osc_lower_low(tsi, _TD_MON)
    return price_nl * (1.0 - tsi_nl)


def mdv_ext_030_tsi_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but TSI does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    tsi = _tsi(close)
    tsi_nl = _osc_lower_low(tsi, _TD_QTR)
    return price_nl * (1.0 - tsi_nl)


def mdv_ext_031_tsi_divg_flag_252d(close: pd.Series) -> pd.Series:
    """Binary: price 252-day new low but TSI does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_YEAR)
    tsi = _tsi(close)
    tsi_nl = _osc_lower_low(tsi, _TD_YEAR)
    return price_nl * (1.0 - tsi_nl)


def mdv_ext_032_tsi_gap_at_price_low_63d(close: pd.Series) -> pd.Series:
    """TSI above its 63-day min when price makes a 63-day new low (gap magnitude)."""
    price_nl = _price_new_low(close, _TD_QTR)
    tsi = _tsi(close)
    tsi_floor = _rolling_min(tsi, _TD_QTR)
    return (tsi - tsi_floor).clip(lower=0.0) * price_nl


def mdv_ext_033_tsi_pctrank_spread_63d(close: pd.Series) -> pd.Series:
    """TSI pct-rank minus price pct-rank over 63-day window."""
    tsi = _tsi(close)
    return _pct_rank(tsi, _TD_QTR) - _pct_rank(close, _TD_QTR)


def mdv_ext_034_tsi_pctrank_spread_252d(close: pd.Series) -> pd.Series:
    """TSI pct-rank minus price pct-rank over 252-day window."""
    tsi = _tsi(close)
    return _pct_rank(tsi, _TD_YEAR) - _pct_rank(close, _TD_YEAR)


def mdv_ext_035_tsi_divg_count_252d(close: pd.Series) -> pd.Series:
    """Count of TSI bullish divergence flags in trailing 252 days."""
    flag = mdv_ext_030_tsi_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_ext_036_tsi_divg_magnitude_63d(close: pd.Series) -> pd.Series:
    """Price drawdown fraction minus TSI drawdown fraction from 63-day high."""
    tsi = _tsi(close)
    price_hi = _rolling_max(close, _TD_QTR)
    tsi_hi = _rolling_max(tsi, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    tsi_range = (tsi_hi - _rolling_min(tsi, _TD_QTR)).clip(lower=_EPS)
    tsi_dd = _safe_div(tsi_hi - tsi, tsi_range)
    return price_dd - tsi_dd


# ── Feature functions ext_037-044: Triple/Multi-Swing Divergence ──────────────
# Divergence persisting across 3+ successive price lows using rolling windows.

def mdv_ext_037_rsi_triple_swing_divg_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 63 days that are on a 21-day price new low with RSI NOT new low;
    3+ consecutive such bars = persistent multi-swing bullish divergence."""
    price_nl = _price_new_low(close, _TD_MON)
    rsi = _rsi(close, 14)
    rsi_nl = _osc_lower_low(rsi, _TD_MON)
    flag = price_nl * (1.0 - rsi_nl)
    return _rolling_sum(flag, _TD_QTR)


def mdv_ext_038_rsi_triple_swing_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: 3 or more RSI bullish divergence events in trailing 63 days (triple-swing)."""
    cnt = mdv_ext_037_rsi_triple_swing_divg_count_63d(close)
    return (cnt >= 3.0).astype(float)


def mdv_ext_039_macd_triple_swing_divg_count_63d(close: pd.Series) -> pd.Series:
    """Count of MACD bullish divergence days within trailing 63 days."""
    price_nl = _price_new_low(close, _TD_MON)
    macd_line = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    macd_nl = _osc_lower_low(macd_line, _TD_MON)
    flag = price_nl * (1.0 - macd_nl)
    return _rolling_sum(flag, _TD_QTR)


def mdv_ext_040_macd_triple_swing_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: 3 or more MACD bullish divergence days in trailing 63 days."""
    cnt = mdv_ext_039_macd_triple_swing_divg_count_63d(close)
    return (cnt >= 3.0).astype(float)


def mdv_ext_041_cmo_triple_swing_divg_count_63d(close: pd.Series) -> pd.Series:
    """Count of CMO bullish divergence days within trailing 63 days."""
    price_nl = _price_new_low(close, _TD_MON)
    cmo = _cmo(close, 14)
    cmo_nl = _osc_lower_low(cmo, _TD_MON)
    flag = price_nl * (1.0 - cmo_nl)
    return _rolling_sum(flag, _TD_QTR)


def mdv_ext_042_mfi_triple_swing_divg_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of MFI bullish divergence days within trailing 63 days."""
    price_nl = _price_new_low(close, _TD_MON)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_nl = _osc_lower_low(mfi, _TD_MON)
    flag = price_nl * (1.0 - mfi_nl)
    return _rolling_sum(flag, _TD_QTR)


def mdv_ext_043_multi_osc_triple_swing_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: 3+ oscillators each show 3+ multi-swing divergence days in 63 days; all at once."""
    rsi_cnt = mdv_ext_037_rsi_triple_swing_divg_count_63d(close)
    macd_cnt = mdv_ext_039_macd_triple_swing_divg_count_63d(close)
    mfi_cnt = mdv_ext_042_mfi_triple_swing_divg_count_63d(close, high, low, volume)
    a = (rsi_cnt >= 3.0).astype(float)
    b = (macd_cnt >= 3.0).astype(float)
    c = (mfi_cnt >= 3.0).astype(float)
    return ((a + b + c) >= 2.0).astype(float)


def mdv_ext_044_rsi_triple_swing_divg_count_252d(close: pd.Series) -> pd.Series:
    """Count of RSI bullish divergence days in trailing 252 days (long-horizon multi-swing)."""
    price_nl = _price_new_low(close, _TD_MON)
    rsi = _rsi(close, 14)
    rsi_nl = _osc_lower_low(rsi, _TD_MON)
    flag = price_nl * (1.0 - rsi_nl)
    return _rolling_sum(flag, _TD_YEAR)


# ── Feature functions ext_045-050: Divergence-Magnitude Slope ────────────────
# Rate at which the divergence gap between price and oscillator is widening.

def mdv_ext_045_rsi_divg_gap_widening_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (RSI pct-rank minus price pct-rank); positive = widening divergence."""
    rsi = _rsi(close, 14)
    spread = _pct_rank(rsi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    xi = np.arange(len(spread), dtype=float)
    out = np.full(len(spread), np.nan)
    n = _TD_MON
    min_p = max(2, n // 2)
    vals = spread.values
    for i in range(n - 1, len(vals)):
        start = i - n + 1
        y = vals[start: i + 1]
        valid = ~np.isnan(y)
        if valid.sum() < min_p:
            continue
        x_ = xi[start: i + 1][valid]
        y_ = y[valid]
        if len(x_) < 2:
            continue
        xm, ym = x_.mean(), y_.mean()
        denom = ((x_ - xm) ** 2).sum()
        if denom == 0:
            continue
        out[i] = ((x_ - xm) * (y_ - ym)).sum() / denom
    return pd.Series(out, index=spread.index)


def mdv_ext_046_macd_divg_gap_widening_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (MACD pct-rank minus price pct-rank); positive = widening."""
    macd_line = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    spread = _pct_rank(macd_line, _TD_QTR) - _pct_rank(close, _TD_QTR)
    xi = np.arange(len(spread), dtype=float)
    out = np.full(len(spread), np.nan)
    n = _TD_MON
    min_p = max(2, n // 2)
    vals = spread.values
    for i in range(n - 1, len(vals)):
        start = i - n + 1
        y = vals[start: i + 1]
        valid = ~np.isnan(y)
        if valid.sum() < min_p:
            continue
        x_ = xi[start: i + 1][valid]
        y_ = y[valid]
        if len(x_) < 2:
            continue
        xm, ym = x_.mean(), y_.mean()
        denom = ((x_ - xm) ** 2).sum()
        if denom == 0:
            continue
        out[i] = ((x_ - xm) * (y_ - ym)).sum() / denom
    return pd.Series(out, index=spread.index)


def mdv_ext_047_cmo_divg_gap_widening_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (CMO pct-rank minus price pct-rank); positive = widening."""
    cmo = _cmo(close, 14)
    spread = _pct_rank(cmo, _TD_QTR) - _pct_rank(close, _TD_QTR)
    xi = np.arange(len(spread), dtype=float)
    out = np.full(len(spread), np.nan)
    n = _TD_MON
    min_p = max(2, n // 2)
    vals = spread.values
    for i in range(n - 1, len(vals)):
        start = i - n + 1
        y = vals[start: i + 1]
        valid = ~np.isnan(y)
        if valid.sum() < min_p:
            continue
        x_ = xi[start: i + 1][valid]
        y_ = y[valid]
        if len(x_) < 2:
            continue
        xm, ym = x_.mean(), y_.mean()
        denom = ((x_ - xm) ** 2).sum()
        if denom == 0:
            continue
        out[i] = ((x_ - xm) * (y_ - ym)).sum() / denom
    return pd.Series(out, index=spread.index)


def mdv_ext_048_tsi_divg_gap_widening_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (TSI pct-rank minus price pct-rank); positive = widening."""
    tsi = _tsi(close)
    spread = _pct_rank(tsi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    xi = np.arange(len(spread), dtype=float)
    out = np.full(len(spread), np.nan)
    n = _TD_MON
    min_p = max(2, n // 2)
    vals = spread.values
    for i in range(n - 1, len(vals)):
        start = i - n + 1
        y = vals[start: i + 1]
        valid = ~np.isnan(y)
        if valid.sum() < min_p:
            continue
        x_ = xi[start: i + 1][valid]
        y_ = y[valid]
        if len(x_) < 2:
            continue
        xm, ym = x_.mean(), y_.mean()
        denom = ((x_ - xm) ** 2).sum()
        if denom == 0:
            continue
        out[i] = ((x_ - xm) * (y_ - ym)).sum() / denom
    return pd.Series(out, index=spread.index)


def mdv_ext_049_mfi_divg_gap_widening_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (MFI pct-rank minus price pct-rank); positive = widening."""
    mfi = _mfi(close, high, low, volume, 14)
    spread = _pct_rank(mfi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    xi = np.arange(len(spread), dtype=float)
    out = np.full(len(spread), np.nan)
    n = _TD_MON
    min_p = max(2, n // 2)
    vals = spread.values
    for i in range(n - 1, len(vals)):
        start = i - n + 1
        y = vals[start: i + 1]
        valid = ~np.isnan(y)
        if valid.sum() < min_p:
            continue
        x_ = xi[start: i + 1][valid]
        y_ = y[valid]
        if len(x_) < 2:
            continue
        xm, ym = x_.mean(), y_.mean()
        denom = ((x_ - xm) ** 2).sum()
        if denom == 0:
            continue
        out[i] = ((x_ - xm) * (y_ - ym)).sum() / denom
    return pd.Series(out, index=spread.index)


def mdv_ext_050_composite_divg_widening_slope_avg_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of RSI, MACD, CMO, TSI, MFI gap-widening slopes over 21 days."""
    a = mdv_ext_045_rsi_divg_gap_widening_slope_21d(close)
    b = mdv_ext_046_macd_divg_gap_widening_slope_21d(close)
    c = mdv_ext_047_cmo_divg_gap_widening_slope_21d(close)
    d = mdv_ext_048_tsi_divg_gap_widening_slope_21d(close)
    e = mdv_ext_049_mfi_divg_gap_widening_slope_21d(close, high, low, volume)
    return (a + b + c + d + e) / 5.0


# ── Feature functions ext_051-056: Class A/B/C Divergence Grading ─────────────
# Class A = strongest (large gap + multi-osc + oversold); B = moderate; C = weak.

def mdv_ext_051_class_a_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Class A divergence: RSI gap > 10 pts AND 3+ new oscillators confirm AND price new 63-day low."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    mfi = _mfi(close, high, low, volume, 14)
    cmo = _cmo(close, 14)
    tsi = _tsi(close)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    rsi_gap = (rsi - rsi_floor).clip(lower=0.0)
    large_gap = (rsi_gap > 10.0).astype(float)
    mfi_no_nl = (1.0 - _osc_lower_low(mfi, _TD_QTR))
    cmo_no_nl = (1.0 - _osc_lower_low(cmo, _TD_QTR))
    tsi_no_nl = (1.0 - _osc_lower_low(tsi, _TD_QTR))
    agree = mfi_no_nl + cmo_no_nl + tsi_no_nl
    return price_nl * large_gap * (agree >= 2.0).astype(float)


def mdv_ext_052_class_b_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Class B divergence: RSI gap 5-10 pts OR 2 oscillators confirm at 63-day price low."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    mfi = _mfi(close, high, low, volume, 14)
    cmo = _cmo(close, 14)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    rsi_gap = (rsi - rsi_floor).clip(lower=0.0)
    mod_gap = ((rsi_gap >= 5.0) & (rsi_gap < 10.0)).astype(float)
    mfi_no_nl = (1.0 - _osc_lower_low(mfi, _TD_QTR))
    cmo_no_nl = (1.0 - _osc_lower_low(cmo, _TD_QTR))
    agree2 = (mfi_no_nl + cmo_no_nl >= 2.0).astype(float)
    return price_nl * ((mod_gap + agree2) >= 1.0).astype(float)


def mdv_ext_053_class_c_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Class C divergence: RSI gap >0 but <5 pts at 63-day price low (weakest confirming signal)."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    rsi_gap = (rsi - rsi_floor).clip(lower=0.0)
    weak_gap = ((rsi_gap > 0.0) & (rsi_gap < 5.0)).astype(float)
    return price_nl * weak_gap


def mdv_ext_054_class_a_divg_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Class A divergence days in trailing 252 days."""
    flag = mdv_ext_051_class_a_divg_flag_63d(close, high, low, volume)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_ext_055_class_a_vs_c_ratio_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio: Class A count / (Class C count + 1) over trailing 252 days (signal quality)."""
    a_cnt = _rolling_sum(mdv_ext_051_class_a_divg_flag_63d(close, high, low, volume), _TD_YEAR)
    c_cnt = _rolling_sum(mdv_ext_053_class_c_divg_flag_63d(close), _TD_YEAR)
    return _safe_div(a_cnt, (c_cnt + 1.0))


def mdv_ext_056_class_abc_composite_score_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted composite: Class A * 3 + Class B * 2 + Class C * 1 (strength tiers, 63d lookback)."""
    a = mdv_ext_051_class_a_divg_flag_63d(close, high, low, volume)
    b = mdv_ext_052_class_b_divg_flag_63d(close, high, low, volume)
    c = mdv_ext_053_class_c_divg_flag_63d(close)
    return 3.0 * a + 2.0 * b + 1.0 * c


# ── Feature functions ext_057-062: Divergence Confirmation ────────────────────
# Divergence + oversold + high volume simultaneously.

def mdv_ext_057_rsi_divg_plus_oversold_63d(close: pd.Series) -> pd.Series:
    """Binary: RSI bullish divergence at 63-day low AND RSI < 30 (oversold confirmation)."""
    divg = mdv_ext_022_cmo_divg_flag_63d(close)  # using CMO no — use RSI:
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_nl = _osc_lower_low(rsi, _TD_QTR)
    rsi_divg = price_nl * (1.0 - rsi_nl)
    oversold = (rsi < 30.0).astype(float)
    return rsi_divg * oversold


def mdv_ext_058_mfi_divg_plus_oversold_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: MFI bullish divergence at 63-day low AND MFI < 20 (oversold MFI)."""
    divg = mdv_ext_002_mfi_divg_flag_63d(close, high, low, volume)
    mfi = _mfi(close, high, low, volume, 14)
    oversold = (mfi < 20.0).astype(float)
    return divg * oversold


def mdv_ext_059_rsi_divg_plus_high_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: RSI bullish divergence at 63-day low AND volume > 1.5x its 21-day average."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_nl = _osc_lower_low(rsi, _TD_QTR)
    rsi_divg = price_nl * (1.0 - rsi_nl)
    vol_avg = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > 1.5 * vol_avg.clip(lower=_EPS)).astype(float)
    return rsi_divg * high_vol


def mdv_ext_060_tsi_divg_plus_oversold_63d(close: pd.Series) -> pd.Series:
    """Binary: TSI bullish divergence at 63-day low AND TSI < -25 (extreme negative)."""
    divg = mdv_ext_030_tsi_divg_flag_63d(close)
    tsi = _tsi(close)
    oversold = (tsi < -25.0).astype(float)
    return divg * oversold


def mdv_ext_061_cmo_divg_plus_oversold_63d(close: pd.Series) -> pd.Series:
    """Binary: CMO bullish divergence at 63-day low AND CMO < -50 (oversold CMO)."""
    divg = mdv_ext_022_cmo_divg_flag_63d(close)
    cmo = _cmo(close, 14)
    oversold = (cmo < -50.0).astype(float)
    return divg * oversold


def mdv_ext_062_triple_confirm_divg_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: RSI divergence + MFI divergence + volume spike all simultaneously at 63-day low."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    mfi = _mfi(close, high, low, volume, 14)
    rsi_divg = price_nl * (1.0 - _osc_lower_low(rsi, _TD_QTR))
    mfi_divg = price_nl * (1.0 - _osc_lower_low(mfi, _TD_QTR))
    vol_avg = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > 1.5 * vol_avg.clip(lower=_EPS)).astype(float)
    return rsi_divg * mfi_divg * high_vol


# ── Feature functions ext_063-067: Time-Since-Last-Divergence & Density ───────

def mdv_ext_063_cmo_divg_recency_63d(close: pd.Series) -> pd.Series:
    """Days since last CMO bullish divergence flag (63-day detection window)."""
    flag = mdv_ext_022_cmo_divg_flag_63d(close)
    return _days_since_flag(flag)


def mdv_ext_064_tsi_divg_recency_63d(close: pd.Series) -> pd.Series:
    """Days since last TSI bullish divergence flag (63-day detection window)."""
    flag = mdv_ext_030_tsi_divg_flag_63d(close)
    return _days_since_flag(flag)


def mdv_ext_065_new_osc_divg_density_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Total divergence days across MFI+CMO+TSI+UO in trailing 63 days (density score, 0-63*4)."""
    mfi_flag = mdv_ext_002_mfi_divg_flag_63d(close, high, low, volume)
    cmo_flag = mdv_ext_022_cmo_divg_flag_63d(close)
    tsi_flag = mdv_ext_030_tsi_divg_flag_63d(close)
    uo_flag = mdv_ext_012_uo_divg_flag_63d(close, high, low)
    combined = mfi_flag + cmo_flag + tsi_flag + uo_flag
    return _rolling_sum(combined, _TD_QTR)


def mdv_ext_066_new_osc_divg_density_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Total divergence days across MFI+CMO+TSI+UO in trailing 252 days (long-horizon density)."""
    mfi_flag = mdv_ext_002_mfi_divg_flag_63d(close, high, low, volume)
    cmo_flag = mdv_ext_022_cmo_divg_flag_63d(close)
    tsi_flag = mdv_ext_030_tsi_divg_flag_63d(close)
    uo_flag = mdv_ext_012_uo_divg_flag_63d(close, high, low)
    combined = mfi_flag + cmo_flag + tsi_flag + uo_flag
    return _rolling_sum(combined, _TD_YEAR)


def mdv_ext_067_class_a_recency_inverse_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Inverse days since last Class A divergence event (capped at 252); higher = more recent."""
    flag = mdv_ext_051_class_a_divg_flag_63d(close, high, low, volume)
    recency = _days_since_flag(flag).clip(upper=_TD_YEAR)
    return _safe_div(pd.Series(1.0, index=close.index), recency.clip(lower=_EPS))


# ── Feature functions ext_068-071: Volume-vs-Price & A/D Line Divergence ──────

def mdv_ext_068_ad_line_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but Chaikin A/D Line does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    ad = _ad_line(close, high, low, volume)
    ad_nl = _osc_lower_low(ad, _TD_QTR)
    return price_nl * (1.0 - ad_nl)


def mdv_ext_069_ad_line_divg_flag_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: price 252-day new low but Chaikin A/D Line does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_YEAR)
    ad = _ad_line(close, high, low, volume)
    ad_nl = _osc_lower_low(ad, _TD_YEAR)
    return price_nl * (1.0 - ad_nl)


def mdv_ext_070_ad_line_pctrank_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """A/D Line pct-rank minus price pct-rank over 63-day window."""
    ad = _ad_line(close, high, low, volume)
    return _pct_rank(ad, _TD_QTR) - _pct_rank(close, _TD_QTR)


def mdv_ext_071_ad_line_divg_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of A/D Line bullish divergence flags in trailing 252 days."""
    flag = mdv_ext_068_ad_line_divg_flag_63d(close, high, low, volume)
    return _rolling_sum(flag, _TD_YEAR)


# ── Feature functions ext_072-075: Multi-Osc Confluence Depth & ROC Acceleration ─

def mdv_ext_072_seven_osc_confluence_score_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of oscillators (MFI/UO/CMO/TSI/A-D + RSI/MACD from new angle) diverging at 63-day low; 0-7."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    macd_line = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    mfi = _mfi(close, high, low, volume, 14)
    uo = _ultimate_oscillator(close, high, low)
    cmo = _cmo(close, 14)
    tsi = _tsi(close)
    ad = _ad_line(close, high, low, volume)
    oscs = [rsi, macd_line, mfi, uo, cmo, tsi, ad]
    result = pd.Series(0.0, index=close.index)
    for osc in oscs:
        result = result + price_nl * (1.0 - _osc_lower_low(osc, _TD_QTR))
    return result


def mdv_ext_073_seven_osc_confluence_pctrank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct-rank of 7-oscillator confluence score within trailing 252 days."""
    score = mdv_ext_072_seven_osc_confluence_score_63d(close, high, low, volume)
    return _pct_rank(score, _TD_YEAR)


def mdv_ext_074_rsi_divg_accel_5d_diff(close: pd.Series) -> pd.Series:
    """Acceleration: 5-day diff of the RSI divergence gap widening slope (rate of gap-widen change)."""
    slope = mdv_ext_045_rsi_divg_gap_widening_slope_21d(close)
    return slope.diff(_TD_WEEK)


def mdv_ext_075_composite_new_osc_divg_strength(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Grand composite: 7-osc confluence score * class-A flag * avg gap-widening slope (overall signal strength)."""
    confluence = mdv_ext_072_seven_osc_confluence_score_63d(close, high, low, volume)
    class_a = mdv_ext_051_class_a_divg_flag_63d(close, high, low, volume)
    widening = mdv_ext_050_composite_divg_widening_slope_avg_21d(close, high, low, volume).clip(lower=0.0)
    return confluence * (1.0 + class_a) * (1.0 + widening)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DIVERGENCE_EXTENDED_REGISTRY_001_075 = {
    "mdv_ext_001_mfi_divg_flag_21d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_001_mfi_divg_flag_21d},
    "mdv_ext_002_mfi_divg_flag_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_002_mfi_divg_flag_63d},
    "mdv_ext_003_mfi_divg_flag_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_003_mfi_divg_flag_252d},
    "mdv_ext_004_mfi_gap_at_price_low_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_004_mfi_gap_at_price_low_63d},
    "mdv_ext_005_mfi_pctrank_spread_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_005_mfi_pctrank_spread_63d},
    "mdv_ext_006_mfi_pctrank_spread_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_006_mfi_pctrank_spread_252d},
    "mdv_ext_007_mfi_divg_count_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_007_mfi_divg_count_252d},
    "mdv_ext_008_mfi_divg_magnitude_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_008_mfi_divg_magnitude_63d},
    "mdv_ext_009_mfi_divg_gap_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_009_mfi_divg_gap_zscore_63d},
    "mdv_ext_010_mfi_divg_recency_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_010_mfi_divg_recency_63d},
    "mdv_ext_011_uo_divg_flag_21d": {"inputs": ["close", "high", "low"], "func": mdv_ext_011_uo_divg_flag_21d},
    "mdv_ext_012_uo_divg_flag_63d": {"inputs": ["close", "high", "low"], "func": mdv_ext_012_uo_divg_flag_63d},
    "mdv_ext_013_uo_divg_flag_252d": {"inputs": ["close", "high", "low"], "func": mdv_ext_013_uo_divg_flag_252d},
    "mdv_ext_014_uo_gap_at_price_low_63d": {"inputs": ["close", "high", "low"], "func": mdv_ext_014_uo_gap_at_price_low_63d},
    "mdv_ext_015_uo_pctrank_spread_63d": {"inputs": ["close", "high", "low"], "func": mdv_ext_015_uo_pctrank_spread_63d},
    "mdv_ext_016_uo_pctrank_spread_252d": {"inputs": ["close", "high", "low"], "func": mdv_ext_016_uo_pctrank_spread_252d},
    "mdv_ext_017_uo_divg_count_252d": {"inputs": ["close", "high", "low"], "func": mdv_ext_017_uo_divg_count_252d},
    "mdv_ext_018_uo_divg_magnitude_63d": {"inputs": ["close", "high", "low"], "func": mdv_ext_018_uo_divg_magnitude_63d},
    "mdv_ext_019_uo_divg_gap_zscore_63d": {"inputs": ["close", "high", "low"], "func": mdv_ext_019_uo_divg_gap_zscore_63d},
    "mdv_ext_020_uo_divg_recency_63d": {"inputs": ["close", "high", "low"], "func": mdv_ext_020_uo_divg_recency_63d},
    "mdv_ext_021_cmo_divg_flag_21d": {"inputs": ["close"], "func": mdv_ext_021_cmo_divg_flag_21d},
    "mdv_ext_022_cmo_divg_flag_63d": {"inputs": ["close"], "func": mdv_ext_022_cmo_divg_flag_63d},
    "mdv_ext_023_cmo_divg_flag_252d": {"inputs": ["close"], "func": mdv_ext_023_cmo_divg_flag_252d},
    "mdv_ext_024_cmo_gap_at_price_low_63d": {"inputs": ["close"], "func": mdv_ext_024_cmo_gap_at_price_low_63d},
    "mdv_ext_025_cmo_pctrank_spread_63d": {"inputs": ["close"], "func": mdv_ext_025_cmo_pctrank_spread_63d},
    "mdv_ext_026_cmo_pctrank_spread_252d": {"inputs": ["close"], "func": mdv_ext_026_cmo_pctrank_spread_252d},
    "mdv_ext_027_cmo_divg_count_252d": {"inputs": ["close"], "func": mdv_ext_027_cmo_divg_count_252d},
    "mdv_ext_028_cmo_divg_magnitude_63d": {"inputs": ["close"], "func": mdv_ext_028_cmo_divg_magnitude_63d},
    "mdv_ext_029_tsi_divg_flag_21d": {"inputs": ["close"], "func": mdv_ext_029_tsi_divg_flag_21d},
    "mdv_ext_030_tsi_divg_flag_63d": {"inputs": ["close"], "func": mdv_ext_030_tsi_divg_flag_63d},
    "mdv_ext_031_tsi_divg_flag_252d": {"inputs": ["close"], "func": mdv_ext_031_tsi_divg_flag_252d},
    "mdv_ext_032_tsi_gap_at_price_low_63d": {"inputs": ["close"], "func": mdv_ext_032_tsi_gap_at_price_low_63d},
    "mdv_ext_033_tsi_pctrank_spread_63d": {"inputs": ["close"], "func": mdv_ext_033_tsi_pctrank_spread_63d},
    "mdv_ext_034_tsi_pctrank_spread_252d": {"inputs": ["close"], "func": mdv_ext_034_tsi_pctrank_spread_252d},
    "mdv_ext_035_tsi_divg_count_252d": {"inputs": ["close"], "func": mdv_ext_035_tsi_divg_count_252d},
    "mdv_ext_036_tsi_divg_magnitude_63d": {"inputs": ["close"], "func": mdv_ext_036_tsi_divg_magnitude_63d},
    "mdv_ext_037_rsi_triple_swing_divg_count_63d": {"inputs": ["close"], "func": mdv_ext_037_rsi_triple_swing_divg_count_63d},
    "mdv_ext_038_rsi_triple_swing_divg_flag_63d": {"inputs": ["close"], "func": mdv_ext_038_rsi_triple_swing_divg_flag_63d},
    "mdv_ext_039_macd_triple_swing_divg_count_63d": {"inputs": ["close"], "func": mdv_ext_039_macd_triple_swing_divg_count_63d},
    "mdv_ext_040_macd_triple_swing_divg_flag_63d": {"inputs": ["close"], "func": mdv_ext_040_macd_triple_swing_divg_flag_63d},
    "mdv_ext_041_cmo_triple_swing_divg_count_63d": {"inputs": ["close"], "func": mdv_ext_041_cmo_triple_swing_divg_count_63d},
    "mdv_ext_042_mfi_triple_swing_divg_count_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_042_mfi_triple_swing_divg_count_63d},
    "mdv_ext_043_multi_osc_triple_swing_flag_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_043_multi_osc_triple_swing_flag_63d},
    "mdv_ext_044_rsi_triple_swing_divg_count_252d": {"inputs": ["close"], "func": mdv_ext_044_rsi_triple_swing_divg_count_252d},
    "mdv_ext_045_rsi_divg_gap_widening_slope_21d": {"inputs": ["close"], "func": mdv_ext_045_rsi_divg_gap_widening_slope_21d},
    "mdv_ext_046_macd_divg_gap_widening_slope_21d": {"inputs": ["close"], "func": mdv_ext_046_macd_divg_gap_widening_slope_21d},
    "mdv_ext_047_cmo_divg_gap_widening_slope_21d": {"inputs": ["close"], "func": mdv_ext_047_cmo_divg_gap_widening_slope_21d},
    "mdv_ext_048_tsi_divg_gap_widening_slope_21d": {"inputs": ["close"], "func": mdv_ext_048_tsi_divg_gap_widening_slope_21d},
    "mdv_ext_049_mfi_divg_gap_widening_slope_21d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_049_mfi_divg_gap_widening_slope_21d},
    "mdv_ext_050_composite_divg_widening_slope_avg_21d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_050_composite_divg_widening_slope_avg_21d},
    "mdv_ext_051_class_a_divg_flag_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_051_class_a_divg_flag_63d},
    "mdv_ext_052_class_b_divg_flag_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_052_class_b_divg_flag_63d},
    "mdv_ext_053_class_c_divg_flag_63d": {"inputs": ["close"], "func": mdv_ext_053_class_c_divg_flag_63d},
    "mdv_ext_054_class_a_divg_count_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_054_class_a_divg_count_252d},
    "mdv_ext_055_class_a_vs_c_ratio_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_055_class_a_vs_c_ratio_252d},
    "mdv_ext_056_class_abc_composite_score_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_056_class_abc_composite_score_63d},
    "mdv_ext_057_rsi_divg_plus_oversold_63d": {"inputs": ["close"], "func": mdv_ext_057_rsi_divg_plus_oversold_63d},
    "mdv_ext_058_mfi_divg_plus_oversold_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_058_mfi_divg_plus_oversold_63d},
    "mdv_ext_059_rsi_divg_plus_high_volume_63d": {"inputs": ["close", "volume"], "func": mdv_ext_059_rsi_divg_plus_high_volume_63d},
    "mdv_ext_060_tsi_divg_plus_oversold_63d": {"inputs": ["close"], "func": mdv_ext_060_tsi_divg_plus_oversold_63d},
    "mdv_ext_061_cmo_divg_plus_oversold_63d": {"inputs": ["close"], "func": mdv_ext_061_cmo_divg_plus_oversold_63d},
    "mdv_ext_062_triple_confirm_divg_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_062_triple_confirm_divg_63d},
    "mdv_ext_063_cmo_divg_recency_63d": {"inputs": ["close"], "func": mdv_ext_063_cmo_divg_recency_63d},
    "mdv_ext_064_tsi_divg_recency_63d": {"inputs": ["close"], "func": mdv_ext_064_tsi_divg_recency_63d},
    "mdv_ext_065_new_osc_divg_density_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_065_new_osc_divg_density_63d},
    "mdv_ext_066_new_osc_divg_density_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_066_new_osc_divg_density_252d},
    "mdv_ext_067_class_a_recency_inverse_score": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_067_class_a_recency_inverse_score},
    "mdv_ext_068_ad_line_divg_flag_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_068_ad_line_divg_flag_63d},
    "mdv_ext_069_ad_line_divg_flag_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_069_ad_line_divg_flag_252d},
    "mdv_ext_070_ad_line_pctrank_spread_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_070_ad_line_pctrank_spread_63d},
    "mdv_ext_071_ad_line_divg_count_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_071_ad_line_divg_count_252d},
    "mdv_ext_072_seven_osc_confluence_score_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_072_seven_osc_confluence_score_63d},
    "mdv_ext_073_seven_osc_confluence_pctrank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_073_seven_osc_confluence_pctrank_252d},
    "mdv_ext_074_rsi_divg_accel_5d_diff": {"inputs": ["close"], "func": mdv_ext_074_rsi_divg_accel_5d_diff},
    "mdv_ext_075_composite_new_osc_divg_strength": {"inputs": ["close", "high", "low", "volume"], "func": mdv_ext_075_composite_new_osc_divg_strength},
}
