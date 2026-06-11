"""
32_momentum_divergence — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended-base divergence features (MFI/UO/CMO/TSI/A-D/class/confluence)
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — velocity of extended oscillator divergence signals
All features are backward-looking only; no forward information.

Coverage:
  extdrv2_001-005  Velocity of MFI divergence features (pct-rank spread, gap, magnitude)
  extdrv2_006-010  Velocity of Ultimate Oscillator divergence features
  extdrv2_011-015  Velocity of CMO divergence features
  extdrv2_016-018  Velocity of TSI divergence features
  extdrv2_019-021  Velocity of Class A/B/C divergence grading features
  extdrv2_022-023  Velocity of divergence confirmation/density features
  extdrv2_024-025  Velocity of A/D line and 7-oscillator confluence features
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


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────
# Each = rate of change of an extended-base concept from extended_001_075.

# --- Group 1 (extdrv2_001-005): Velocity of MFI divergence features ---

def mdv_extdrv2_001_mfi_pctrank_spread_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of MFI(14)-price pct-rank spread over 63-day window (velocity of ext_005)."""
    mfi = _mfi(close, high, low, volume, 14)
    spread = _pct_rank(mfi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdv_extdrv2_002_mfi_pctrank_spread_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of MFI(14)-price pct-rank spread over 252-day window (velocity of ext_006)."""
    mfi = _mfi(close, high, low, volume, 14)
    spread = _pct_rank(mfi, _TD_YEAR) - _pct_rank(close, _TD_YEAR)
    return spread.diff(_TD_MON)


def mdv_extdrv2_003_mfi_gap_at_price_low_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of MFI gap above its 63-day min at price-new-low bars (velocity of ext_004)."""
    price_nl = _price_new_low(close, _TD_QTR)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_floor = _rolling_min(mfi, _TD_QTR)
    gap = (mfi - mfi_floor).clip(lower=0.0) * price_nl
    return gap.diff(_TD_WEEK)


def mdv_extdrv2_004_mfi_divg_magnitude_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of MFI drawdown divergence magnitude (63-day) — velocity of ext_008."""
    mfi = _mfi(close, high, low, volume, 14)
    price_hi = _rolling_max(close, _TD_QTR)
    mfi_hi = _rolling_max(mfi, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    mfi_range = (mfi_hi - _rolling_min(mfi, _TD_QTR)).clip(lower=_EPS)
    mfi_dd = _safe_div(mfi_hi - mfi, mfi_range)
    mag = price_dd - mfi_dd
    return mag.diff(_TD_WEEK)


def mdv_extdrv2_005_mfi_divg_gap_zscore_63d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of MFI divergence gap z-score (63d) — velocity of ext_009."""
    price_nl = _price_new_low(close, _TD_QTR)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_floor = _rolling_min(mfi, _TD_QTR)
    gap = (mfi - mfi_floor).clip(lower=0.0) * price_nl
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    z = _safe_div(gap - m, s.clip(lower=_EPS))
    return _linslope(z, _TD_MON)


# --- Group 2 (extdrv2_006-010): Velocity of Ultimate Oscillator divergence features ---

def mdv_extdrv2_006_uo_pctrank_spread_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Ultimate Oscillator-price pct-rank spread over 63 days (velocity of ext_015)."""
    uo = _ultimate_oscillator(close, high, low)
    spread = _pct_rank(uo, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdv_extdrv2_007_uo_pctrank_spread_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of UO-price pct-rank spread over 252-day window (velocity of ext_016)."""
    uo = _ultimate_oscillator(close, high, low)
    spread = _pct_rank(uo, _TD_YEAR) - _pct_rank(close, _TD_YEAR)
    return spread.diff(_TD_MON)


def mdv_extdrv2_008_uo_gap_at_price_low_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of UO gap above its 63-day min at price-new-low bars (velocity of ext_014)."""
    price_nl = _price_new_low(close, _TD_QTR)
    uo = _ultimate_oscillator(close, high, low)
    uo_floor = _rolling_min(uo, _TD_QTR)
    gap = (uo - uo_floor).clip(lower=0.0) * price_nl
    return gap.diff(_TD_WEEK)


def mdv_extdrv2_009_uo_divg_magnitude_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of UO drawdown divergence magnitude (63d) — velocity of ext_018."""
    uo = _ultimate_oscillator(close, high, low)
    price_hi = _rolling_max(close, _TD_QTR)
    uo_hi = _rolling_max(uo, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    uo_range = (uo_hi - _rolling_min(uo, _TD_QTR)).clip(lower=_EPS)
    uo_dd = _safe_div(uo_hi - uo, uo_range)
    mag = price_dd - uo_dd
    return mag.diff(_TD_WEEK)


def mdv_extdrv2_010_uo_divg_gap_zscore_63d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope (21d) of UO divergence gap z-score (63d) — velocity of ext_019."""
    price_nl = _price_new_low(close, _TD_QTR)
    uo = _ultimate_oscillator(close, high, low)
    uo_floor = _rolling_min(uo, _TD_QTR)
    gap = (uo - uo_floor).clip(lower=0.0) * price_nl
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    z = _safe_div(gap - m, s.clip(lower=_EPS))
    return _linslope(z, _TD_MON)


# --- Group 3 (extdrv2_011-015): Velocity of CMO divergence features ---

def mdv_extdrv2_011_cmo_pctrank_spread_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of CMO(14)-price pct-rank spread over 63-day window (velocity of ext_025)."""
    cmo = _cmo(close, 14)
    spread = _pct_rank(cmo, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdv_extdrv2_012_cmo_pctrank_spread_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of CMO(14)-price pct-rank spread over 252-day window (velocity of ext_026)."""
    cmo = _cmo(close, 14)
    spread = _pct_rank(cmo, _TD_YEAR) - _pct_rank(close, _TD_YEAR)
    return spread.diff(_TD_MON)


def mdv_extdrv2_013_cmo_gap_at_price_low_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of CMO gap above its 63-day min at price-new-low bars (velocity of ext_024)."""
    price_nl = _price_new_low(close, _TD_QTR)
    cmo = _cmo(close, 14)
    cmo_floor = _rolling_min(cmo, _TD_QTR)
    gap = (cmo - cmo_floor).clip(lower=0.0) * price_nl
    return gap.diff(_TD_WEEK)


def mdv_extdrv2_014_cmo_divg_magnitude_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of CMO drawdown divergence magnitude (63d) — velocity of ext_028."""
    cmo = _cmo(close, 14)
    price_hi = _rolling_max(close, _TD_QTR)
    cmo_hi = _rolling_max(cmo, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    cmo_range = (cmo_hi - _rolling_min(cmo, _TD_QTR)).clip(lower=_EPS)
    cmo_dd = _safe_div(cmo_hi - cmo, cmo_range)
    mag = price_dd - cmo_dd
    return mag.diff(_TD_MON)


def mdv_extdrv2_015_cmo_triple_swing_divg_count_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of CMO triple-swing divergence day count in trailing 63 days (velocity of ext_041)."""
    price_nl = _price_new_low(close, _TD_MON)
    cmo = _cmo(close, 14)
    cmo_nl = _osc_lower_low(cmo, _TD_MON)
    flag = price_nl * (1.0 - cmo_nl)
    count = _rolling_sum(flag, _TD_QTR)
    return count.diff(_TD_WEEK)


# --- Group 4 (extdrv2_016-018): Velocity of TSI divergence features ---

def mdv_extdrv2_016_tsi_pctrank_spread_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of TSI-price pct-rank spread over 63-day window (velocity of ext_033)."""
    tsi = _tsi(close)
    spread = _pct_rank(tsi, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdv_extdrv2_017_tsi_gap_at_price_low_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of TSI gap above its 63-day min at price-new-low bars (velocity of ext_032)."""
    price_nl = _price_new_low(close, _TD_QTR)
    tsi = _tsi(close)
    tsi_floor = _rolling_min(tsi, _TD_QTR)
    gap = (tsi - tsi_floor).clip(lower=0.0) * price_nl
    return gap.diff(_TD_WEEK)


def mdv_extdrv2_018_tsi_divg_magnitude_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of TSI drawdown divergence magnitude (63d) — velocity of ext_036."""
    tsi = _tsi(close)
    price_hi = _rolling_max(close, _TD_QTR)
    tsi_hi = _rolling_max(tsi, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    tsi_range = (tsi_hi - _rolling_min(tsi, _TD_QTR)).clip(lower=_EPS)
    tsi_dd = _safe_div(tsi_hi - tsi, tsi_range)
    mag = price_dd - tsi_dd
    return mag.diff(_TD_MON)


# --- Group 5 (extdrv2_019-021): Velocity of Class A/B/C divergence grading ---

def mdv_extdrv2_019_class_a_divg_count_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of Class A divergence day count in trailing 252 days (velocity of ext_054)."""
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
    class_a = price_nl * large_gap * (agree >= 2.0).astype(float)
    count = _rolling_sum(class_a, _TD_YEAR)
    return count.diff(_TD_MON)


def mdv_extdrv2_020_class_abc_composite_score_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of Class A*3 + B*2 + C*1 composite score (velocity of ext_056)."""
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
    class_a = price_nl * large_gap * (agree >= 2.0).astype(float)
    mod_gap = ((rsi_gap >= 5.0) & (rsi_gap < 10.0)).astype(float)
    agree2 = ((mfi_no_nl + cmo_no_nl) >= 2.0).astype(float)
    class_b = price_nl * ((mod_gap + agree2) >= 1.0).astype(float)
    weak_gap = ((rsi_gap > 0.0) & (rsi_gap < 5.0)).astype(float)
    class_c = price_nl * weak_gap
    composite = 3.0 * class_a + 2.0 * class_b + 1.0 * class_c
    return composite.diff(_TD_WEEK)


def mdv_extdrv2_021_class_a_vs_c_ratio_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of Class A / (Class C + 1) ratio over 252 days (velocity of ext_055)."""
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
    class_a = price_nl * large_gap * (agree >= 2.0).astype(float)
    weak_gap = ((rsi_gap > 0.0) & (rsi_gap < 5.0)).astype(float)
    class_c = price_nl * weak_gap
    a_cnt = _rolling_sum(class_a, _TD_YEAR)
    c_cnt = _rolling_sum(class_c, _TD_YEAR)
    ratio = _safe_div(a_cnt, (c_cnt + 1.0))
    return ratio.diff(_TD_MON)


# --- Group 6 (extdrv2_022-023): Velocity of divergence confirmation/density features ---

def mdv_extdrv2_022_new_osc_divg_density_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of total MFI+CMO+TSI+UO divergence day density in trailing 63 days (velocity of ext_065)."""
    # MFI flag
    price_nl_mon = _price_new_low(close, _TD_MON)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_flag = price_nl_mon * (1.0 - _osc_lower_low(mfi, _TD_MON))
    # CMO flag
    cmo = _cmo(close, 14)
    cmo_flag = price_nl_mon * (1.0 - _osc_lower_low(cmo, _TD_MON))
    # TSI flag
    tsi = _tsi(close)
    tsi_flag = price_nl_mon * (1.0 - _osc_lower_low(tsi, _TD_MON))
    # UO flag
    uo = _ultimate_oscillator(close, high, low)
    uo_flag = price_nl_mon * (1.0 - _osc_lower_low(uo, _TD_MON))
    combined = mfi_flag + cmo_flag + tsi_flag + uo_flag
    density = _rolling_sum(combined, _TD_QTR)
    return density.diff(_TD_WEEK)


def mdv_extdrv2_023_new_osc_divg_density_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of total MFI+CMO+TSI+UO divergence density in trailing 252 days (velocity of ext_066)."""
    price_nl_mon = _price_new_low(close, _TD_MON)
    mfi = _mfi(close, high, low, volume, 14)
    mfi_flag = price_nl_mon * (1.0 - _osc_lower_low(mfi, _TD_MON))
    cmo = _cmo(close, 14)
    cmo_flag = price_nl_mon * (1.0 - _osc_lower_low(cmo, _TD_MON))
    tsi = _tsi(close)
    tsi_flag = price_nl_mon * (1.0 - _osc_lower_low(tsi, _TD_MON))
    uo = _ultimate_oscillator(close, high, low)
    uo_flag = price_nl_mon * (1.0 - _osc_lower_low(uo, _TD_MON))
    combined = mfi_flag + cmo_flag + tsi_flag + uo_flag
    density = _rolling_sum(combined, _TD_YEAR)
    return density.diff(_TD_MON)


# --- Group 7 (extdrv2_024-025): Velocity of A/D line and 7-oscillator confluence ---

def mdv_extdrv2_024_ad_line_pctrank_spread_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of A/D Line-price pct-rank spread over 63-day window (velocity of ext_070)."""
    ad = _ad_line(close, high, low, volume)
    spread = _pct_rank(ad, _TD_QTR) - _pct_rank(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdv_extdrv2_025_seven_osc_confluence_score_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 7-oscillator confluence score at 63-day price lows (velocity of ext_072)."""
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
    return result.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DIVERGENCE_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "mdv_extdrv2_001_mfi_pctrank_spread_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_001_mfi_pctrank_spread_63d_5d_diff},
    "mdv_extdrv2_002_mfi_pctrank_spread_252d_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_002_mfi_pctrank_spread_252d_21d_diff},
    "mdv_extdrv2_003_mfi_gap_at_price_low_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_003_mfi_gap_at_price_low_63d_5d_diff},
    "mdv_extdrv2_004_mfi_divg_magnitude_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_004_mfi_divg_magnitude_63d_5d_diff},
    "mdv_extdrv2_005_mfi_divg_gap_zscore_63d_slope_21d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_005_mfi_divg_gap_zscore_63d_slope_21d},
    "mdv_extdrv2_006_uo_pctrank_spread_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_extdrv2_006_uo_pctrank_spread_63d_5d_diff},
    "mdv_extdrv2_007_uo_pctrank_spread_252d_21d_diff": {"inputs": ["close", "high", "low"], "func": mdv_extdrv2_007_uo_pctrank_spread_252d_21d_diff},
    "mdv_extdrv2_008_uo_gap_at_price_low_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_extdrv2_008_uo_gap_at_price_low_63d_5d_diff},
    "mdv_extdrv2_009_uo_divg_magnitude_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": mdv_extdrv2_009_uo_divg_magnitude_63d_5d_diff},
    "mdv_extdrv2_010_uo_divg_gap_zscore_63d_slope_21d": {"inputs": ["close", "high", "low"], "func": mdv_extdrv2_010_uo_divg_gap_zscore_63d_slope_21d},
    "mdv_extdrv2_011_cmo_pctrank_spread_63d_5d_diff": {"inputs": ["close"], "func": mdv_extdrv2_011_cmo_pctrank_spread_63d_5d_diff},
    "mdv_extdrv2_012_cmo_pctrank_spread_252d_21d_diff": {"inputs": ["close"], "func": mdv_extdrv2_012_cmo_pctrank_spread_252d_21d_diff},
    "mdv_extdrv2_013_cmo_gap_at_price_low_63d_5d_diff": {"inputs": ["close"], "func": mdv_extdrv2_013_cmo_gap_at_price_low_63d_5d_diff},
    "mdv_extdrv2_014_cmo_divg_magnitude_63d_21d_diff": {"inputs": ["close"], "func": mdv_extdrv2_014_cmo_divg_magnitude_63d_21d_diff},
    "mdv_extdrv2_015_cmo_triple_swing_divg_count_63d_5d_diff": {"inputs": ["close"], "func": mdv_extdrv2_015_cmo_triple_swing_divg_count_63d_5d_diff},
    "mdv_extdrv2_016_tsi_pctrank_spread_63d_5d_diff": {"inputs": ["close"], "func": mdv_extdrv2_016_tsi_pctrank_spread_63d_5d_diff},
    "mdv_extdrv2_017_tsi_gap_at_price_low_63d_5d_diff": {"inputs": ["close"], "func": mdv_extdrv2_017_tsi_gap_at_price_low_63d_5d_diff},
    "mdv_extdrv2_018_tsi_divg_magnitude_63d_21d_diff": {"inputs": ["close"], "func": mdv_extdrv2_018_tsi_divg_magnitude_63d_21d_diff},
    "mdv_extdrv2_019_class_a_divg_count_252d_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_019_class_a_divg_count_252d_21d_diff},
    "mdv_extdrv2_020_class_abc_composite_score_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_020_class_abc_composite_score_63d_5d_diff},
    "mdv_extdrv2_021_class_a_vs_c_ratio_252d_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_021_class_a_vs_c_ratio_252d_21d_diff},
    "mdv_extdrv2_022_new_osc_divg_density_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_022_new_osc_divg_density_63d_5d_diff},
    "mdv_extdrv2_023_new_osc_divg_density_252d_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_023_new_osc_divg_density_252d_21d_diff},
    "mdv_extdrv2_024_ad_line_pctrank_spread_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_024_ad_line_pctrank_spread_63d_5d_diff},
    "mdv_extdrv2_025_seven_osc_confluence_score_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": mdv_extdrv2_025_seven_osc_confluence_score_63d_5d_diff},
}
