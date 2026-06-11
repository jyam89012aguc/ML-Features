"""
33_trend_breakdown — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative concepts —
        jerk / acceleration-of-acceleration in slow/fast PSAR distance velocity,
        Supertrend(7,2)/(14,4) distance acceleration, Aroon-50 oscillator jerk,
        Ichimoku cloud-thickness acceleration, Vortex spread jerk,
        linear-regression slope curvature (slope-of-slope), Chande Kroll jerk,
        Donchian position acceleration, ADXR jerk, Trend Intensity Index jerk,
        Mass Index jerk, Choppiness jerk, extended confluence score jerk.
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


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _atr_wilder(close: pd.Series, high: pd.Series, low: pd.Series,
                period: int) -> pd.Series:
    """ATR using Wilder smoothing."""
    tr = _tr(close, high, low)
    return tr.ewm(alpha=1.0 / period, min_periods=period // 2,
                  adjust=False).mean()


def _adx_components(close: pd.Series, high: pd.Series, low: pd.Series,
                    period: int = 14):
    """Return (adx, plus_di, minus_di) using Wilder smoothing."""
    tr  = _tr(close, high, low)
    dm_plus  = (high - high.shift(1)).clip(lower=0.0)
    dm_minus = (low.shift(1) - low).clip(lower=0.0)
    dm_plus  = dm_plus.where(dm_plus > dm_minus, 0.0)
    dm_minus = dm_minus.where(dm_minus > dm_plus, 0.0)
    atr   = tr.ewm(alpha=1.0 / period, min_periods=period // 2,
                   adjust=False).mean()
    sdi_p = dm_plus.ewm(alpha=1.0 / period, min_periods=period // 2,
                        adjust=False).mean()
    sdi_m = dm_minus.ewm(alpha=1.0 / period, min_periods=period // 2,
                         adjust=False).mean()
    di_p  = _safe_div(sdi_p, atr) * 100
    di_m  = _safe_div(sdi_m, atr) * 100
    dx    = _safe_div((di_p - di_m).abs(), (di_p + di_m).abs()) * 100
    adx   = dx.ewm(alpha=1.0 / period, min_periods=period // 2,
                   adjust=False).mean()
    return adx, di_p, di_m


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _psar_distance_slow(close: pd.Series, high: pd.Series,
                        low: pd.Series) -> pd.Series:
    """(close - SAR) / close using slow AF PSAR (step=0.01, max=0.1)."""
    n = len(high)
    hi = high.values
    lo = low.values
    sar = np.full(n, np.nan)
    is_bull = True
    ep = hi[0]
    af = 0.01
    af_step = 0.01
    af_max  = 0.1
    sar[0]  = lo[0]
    for i in range(1, n):
        pv = sar[i - 1]
        if is_bull:
            ns = pv + af * (ep - pv)
            ns = min(ns, lo[i - 1])
            if i >= 2:
                ns = min(ns, lo[i - 2])
            if lo[i] < ns:
                is_bull = False
                ns = ep
                ep = lo[i]
                af = af_step
            else:
                if hi[i] > ep:
                    ep = hi[i]
                    af = min(af + af_step, af_max)
        else:
            ns = pv + af * (ep - pv)
            ns = max(ns, hi[i - 1])
            if i >= 2:
                ns = max(ns, hi[i - 2])
            if hi[i] > ns:
                is_bull = True
                ns = ep
                ep = hi[i]
                af = af_step
            else:
                if lo[i] < ep:
                    ep = lo[i]
                    af = min(af + af_step, af_max)
        sar[i] = ns
    sar_s = pd.Series(sar, index=close.index)
    return _safe_div(close - sar_s, close)


def _psar_distance_fast(close: pd.Series, high: pd.Series,
                        low: pd.Series) -> pd.Series:
    """(close - SAR) / close using fast AF PSAR (step=0.04, max=0.4)."""
    n = len(high)
    hi = high.values
    lo = low.values
    sar = np.full(n, np.nan)
    is_bull = True
    ep = hi[0]
    af = 0.04
    af_step = 0.04
    af_max  = 0.4
    sar[0]  = lo[0]
    for i in range(1, n):
        pv = sar[i - 1]
        if is_bull:
            ns = pv + af * (ep - pv)
            ns = min(ns, lo[i - 1])
            if i >= 2:
                ns = min(ns, lo[i - 2])
            if lo[i] < ns:
                is_bull = False
                ns = ep
                ep = lo[i]
                af = af_step
            else:
                if hi[i] > ep:
                    ep = hi[i]
                    af = min(af + af_step, af_max)
        else:
            ns = pv + af * (ep - pv)
            ns = max(ns, hi[i - 1])
            if i >= 2:
                ns = max(ns, hi[i - 2])
            if hi[i] > ns:
                is_bull = True
                ns = ep
                ep = hi[i]
                af = af_step
            else:
                if lo[i] < ep:
                    ep = lo[i]
                    af = min(af + af_step, af_max)
        sar[i] = ns
    sar_s = pd.Series(sar, index=close.index)
    return _safe_div(close - sar_s, close)


def _supertrend_distance_72(close: pd.Series, high: pd.Series,
                             low: pd.Series) -> pd.Series:
    """(close - Supertrend line) / close for ST(7, 2.0)."""
    n = len(close)
    cl = close.values
    hi = high.values
    lo = low.values
    atr_period = 7
    multiplier = 2.0
    tr_arr = np.full(n, np.nan)
    for i in range(1, n):
        tr_arr[i] = max(hi[i] - lo[i],
                        abs(hi[i] - cl[i - 1]),
                        abs(lo[i] - cl[i - 1]))
    tr_arr[0] = hi[0] - lo[0]
    atr_arr = np.full(n, np.nan)
    if n >= atr_period:
        atr_arr[atr_period - 1] = np.nanmean(tr_arr[:atr_period])
        alpha = 1.0 / atr_period
        for i in range(atr_period, n):
            atr_arr[i] = atr_arr[i - 1] * (1 - alpha) + tr_arr[i] * alpha
    hl2 = (hi + lo) / 2.0
    ub = hl2 + multiplier * atr_arr
    lb = hl2 - multiplier * atr_arr
    ub_b = np.full(n, np.nan)
    lb_b = np.full(n, np.nan)
    trend = np.full(n, np.nan)
    st_l  = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(atr_arr[i]):
            continue
        if i == 0 or np.isnan(ub_b[i - 1]):
            ub_b[i] = ub[i]
            lb_b[i] = lb[i]
            trend[i] = 1.0 if cl[i] > lb[i] else -1.0
            st_l[i] = lb_b[i] if trend[i] == 1.0 else ub_b[i]
            continue
        ub_b[i] = (ub[i] if (ub[i] < ub_b[i - 1] or cl[i - 1] > ub_b[i - 1])
                   else ub_b[i - 1])
        lb_b[i] = (lb[i] if (lb[i] > lb_b[i - 1] or cl[i - 1] < lb_b[i - 1])
                   else lb_b[i - 1])
        pt = trend[i - 1]
        trend[i] = ((-1.0 if cl[i] < lb_b[i] else 1.0) if pt == 1.0
                    else (1.0 if cl[i] > ub_b[i] else -1.0))
        st_l[i] = lb_b[i] if trend[i] == 1.0 else ub_b[i]
    st_s = pd.Series(st_l, index=close.index)
    return _safe_div(close - st_s, close)


def _supertrend_distance_144(close: pd.Series, high: pd.Series,
                              low: pd.Series) -> pd.Series:
    """(close - Supertrend line) / close for ST(14, 4.0)."""
    n = len(close)
    cl = close.values
    hi = high.values
    lo = low.values
    atr_period = 14
    multiplier = 4.0
    tr_arr = np.full(n, np.nan)
    for i in range(1, n):
        tr_arr[i] = max(hi[i] - lo[i],
                        abs(hi[i] - cl[i - 1]),
                        abs(lo[i] - cl[i - 1]))
    tr_arr[0] = hi[0] - lo[0]
    atr_arr = np.full(n, np.nan)
    if n >= atr_period:
        atr_arr[atr_period - 1] = np.nanmean(tr_arr[:atr_period])
        alpha = 1.0 / atr_period
        for i in range(atr_period, n):
            atr_arr[i] = atr_arr[i - 1] * (1 - alpha) + tr_arr[i] * alpha
    hl2 = (hi + lo) / 2.0
    ub = hl2 + multiplier * atr_arr
    lb = hl2 - multiplier * atr_arr
    ub_b = np.full(n, np.nan)
    lb_b = np.full(n, np.nan)
    trend = np.full(n, np.nan)
    st_l  = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(atr_arr[i]):
            continue
        if i == 0 or np.isnan(ub_b[i - 1]):
            ub_b[i] = ub[i]
            lb_b[i] = lb[i]
            trend[i] = 1.0 if cl[i] > lb[i] else -1.0
            st_l[i] = lb_b[i] if trend[i] == 1.0 else ub_b[i]
            continue
        ub_b[i] = (ub[i] if (ub[i] < ub_b[i - 1] or cl[i - 1] > ub_b[i - 1])
                   else ub_b[i - 1])
        lb_b[i] = (lb[i] if (lb[i] > lb_b[i - 1] or cl[i - 1] < lb_b[i - 1])
                   else lb_b[i - 1])
        pt = trend[i - 1]
        trend[i] = ((-1.0 if cl[i] < lb_b[i] else 1.0) if pt == 1.0
                    else (1.0 if cl[i] > ub_b[i] else -1.0))
        st_l[i] = lb_b[i] if trend[i] == 1.0 else ub_b[i]
    st_s = pd.Series(st_l, index=close.index)
    return _safe_div(close - st_s, close)


def _aroon_osc(high: pd.Series, low: pd.Series, period: int) -> pd.Series:
    """Aroon Oscillator = Aroon Up - Aroon Down for given period."""
    w = period + 1
    def _bs_h(arr): return float(len(arr) - 1 - np.argmax(arr))
    def _bs_l(arr): return float(len(arr) - 1 - np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_h, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_l, raw=True)
    up = (period - bsh) / period * 100
    dn = (period - bsl) / period * 100
    return up - dn


def _ichimoku_cloud_thickness_norm(close: pd.Series, high: pd.Series,
                                   low: pd.Series) -> pd.Series:
    """Ichimoku cloud thickness |Span A - Span B| / close."""
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    span_a = (tenkan + kijun) / 2.0
    span_b = (_rolling_max(high, 52) + _rolling_min(low, 52)) / 2.0
    return _safe_div((span_a - span_b).abs(), close)


def _ichimoku_kijun(high: pd.Series, low: pd.Series) -> pd.Series:
    """Kijun-sen (26-period base line)."""
    return (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0


def _vortex_spread(high: pd.Series, low: pd.Series, close: pd.Series,
                   period: int = 14) -> pd.Series:
    """Vortex spread: VI- minus VI+; positive = bearish dominance."""
    vm_plus  = (high - low.shift(1)).abs()
    vm_minus = (low  - high.shift(1)).abs()
    tr = _tr(close, high, low)
    vi_plus  = _safe_div(_rolling_sum(vm_plus,  period), _rolling_sum(tr, period))
    vi_minus = _safe_div(_rolling_sum(vm_minus, period), _rolling_sum(tr, period))
    return vi_minus - vi_plus


def _chande_kroll_distance(close: pd.Series, high: pd.Series,
                           low: pd.Series) -> pd.Series:
    """(close - CKS_Stop_Short) / close; negative = bearish (below stop)."""
    atr    = _atr_wilder(close, high, low, 10)
    fh     = _rolling_max(high, 10) - 3 * atr
    stop_s = _rolling_max(fh, 9)
    return _safe_div(close - stop_s, close)


def _donchian_pct_rank_63d(close: pd.Series, high: pd.Series,
                           low: pd.Series) -> pd.Series:
    """Position of close within 63-day Donchian channel: 0=bottom, 1=top."""
    upper = _rolling_max(high, _TD_QTR)
    lower = _rolling_min(low,  _TD_QTR)
    return _safe_div(close - lower, upper - lower)


def _adxr14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ADXR(14) = (ADX[today] + ADX[today-14]) / 2."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return (adx + adx.shift(14)) / 2.0


def _trend_intensity_21d(close: pd.Series) -> pd.Series:
    """Trend Intensity Index (TII, 21-day)."""
    sma   = _rolling_mean(close, _TD_MON)
    above = (close > sma).astype(float)
    return _rolling_sum(above, _TD_MON) / _TD_MON * 100


def _mass_index(high: pd.Series, low: pd.Series,
                fast: int = 9, slow: int = 25) -> pd.Series:
    """Mass Index(9,25)."""
    hl    = high - low
    ema1  = _ewm_mean(hl, fast)
    ema2  = _ewm_mean(ema1, fast)
    ratio = _safe_div(ema1, ema2)
    return _rolling_sum(ratio, slow)


def _choppiness_index(close: pd.Series, high: pd.Series, low: pd.Series,
                      period: int = 14) -> pd.Series:
    """Choppiness Index over given period."""
    tr1      = _tr(close, high, low)
    atr_sum  = _rolling_sum(tr1, period)
    h_max    = _rolling_max(high, period)
    l_min    = _rolling_min(low,  period)
    hl_range = h_max - l_min
    ratio    = _safe_div(atr_sum, hl_range)
    log_n    = np.log10(float(period))
    return 100.0 * ratio.apply(
        lambda x: np.log10(x) if (not np.isnan(x) and x > 0) else np.nan
    ) / log_n


def _extended_confluence_score(close: pd.Series, high: pd.Series,
                               low: pd.Series) -> pd.Series:
    """Extended breakdown confluence score (0-6)."""
    spread = _vortex_spread(high, low, close, 14)
    s1 = (spread > 0).astype(float)
    st_dist = _supertrend_distance_72(close, high, low)
    s2 = (st_dist < 0).astype(float)
    ck_dist = _chande_kroll_distance(close, high, low)
    s3 = (ck_dist < 0).astype(float)
    slp = _linslope(close, _TD_MON)
    s4 = (slp < 0).astype(float)
    chop = _choppiness_index(close, high, low, 14)
    s5 = (chop > 61.8).astype(float)
    pos = _donchian_pct_rank_63d(close, high, low)
    s6 = (pos < 0.25).astype(float)
    return s1 + s2 + s3 + s4 + s5 + s6


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────
# Each = diff/slope applied to an extended 2nd-derivative concept

def tbd_extdrv3_001_psar_slow_distance_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of slow-AF PSAR distance (jerk in slow-SAR divergence rate)."""
    dist = _psar_distance_slow(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_002_psar_slow_distance_21d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of slow-AF PSAR distance."""
    dist  = _psar_distance_slow(close, high, low)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_extdrv3_003_psar_fast_distance_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of fast-AF PSAR distance (jerk in fast-SAR divergence)."""
    dist = _psar_distance_fast(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_004_psar_fast_distance_21d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of fast-AF PSAR distance."""
    dist  = _psar_distance_fast(close, high, low)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_extdrv3_005_supertrend_72_distance_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Supertrend(7,2) distance (jerk in ST-72 divergence)."""
    dist = _supertrend_distance_72(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_006_supertrend_72_distance_21d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Supertrend(7,2) distance."""
    dist  = _supertrend_distance_72(close, high, low)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_extdrv3_007_supertrend_144_distance_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Supertrend(14,4) distance (jerk in loose-band ST divergence)."""
    dist = _supertrend_distance_144(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_008_supertrend_144_distance_21d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Supertrend(14,4) distance."""
    dist  = _supertrend_distance_144(close, high, low)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_extdrv3_009_aroon_osc50_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Aroon Oscillator(50) (jerk in 50-period Aroon momentum)."""
    osc = _aroon_osc(high, low, 50)
    vel = osc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_010_aroon_osc50_21d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Aroon Oscillator(50)."""
    osc   = _aroon_osc(high, low, 50)
    vel21 = osc.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_extdrv3_011_ichimoku_cloud_thickness_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Ichimoku cloud thickness (jerk in cloud expansion rate)."""
    thickness = _ichimoku_cloud_thickness_norm(close, high, low)
    vel = thickness.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_012_ichimoku_kijun_slope_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Kijun-sen slope (jerk in Kijun decline acceleration)."""
    kijun       = _ichimoku_kijun(high, low)
    kijun_slope = kijun.diff(1)
    vel         = kijun_slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_013_vortex14_spread_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Vortex(14) spread (jerk in vortex divergence rate)."""
    spread = _vortex_spread(high, low, close, 14)
    vel    = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_014_vortex14_spread_21d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Vortex(14) spread."""
    spread = _vortex_spread(high, low, close, 14)
    vel21  = spread.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_extdrv3_015_vortex21_spread_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Vortex(21) spread (jerk in 21-period vortex)."""
    spread = _vortex_spread(high, low, close, 21)
    vel    = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_016_linreg_slope_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day OLS slope (slope-of-slope curvature jerk)."""
    slp = _linslope(close, _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_017_linreg_slope_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day OLS slope (jerk in quarterly slope velocity)."""
    slp = _linslope(close, _TD_QTR)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_018_chande_kroll_distance_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Chande Kroll distance (jerk in CKS velocity)."""
    dist = _chande_kroll_distance(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_019_chande_kroll_distance_21d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Chande Kroll distance."""
    dist  = _chande_kroll_distance(close, high, low)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_extdrv3_020_donchian_63_pct_rank_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day Donchian position (jerk in breakdown depth rate)."""
    pos = _donchian_pct_rank_63d(close, high, low)
    vel = pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_021_adxr14_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ADXR(14) (jerk in averaged trend-strength collapse)."""
    adxr = _adxr14(close, high, low)
    vel  = adxr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_022_trend_intensity_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Trend Intensity Index(21) (jerk in TII bearish deterioration)."""
    tii = _trend_intensity_21d(close)
    vel = tii.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_023_mass_index_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Mass Index(9,25) (jerk in reversal-bulge formation)."""
    mi  = _mass_index(high, low)
    vel = mi.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_024_choppiness_14_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Choppiness Index(14) (jerk in trend-quality change)."""
    chop = _choppiness_index(close, high, low, 14)
    vel  = chop.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_extdrv3_025_extended_confluence_score_5d_diff_5d_diff(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of extended confluence score (jerk in multi-indicator regime change)."""
    score = _extended_confluence_score(close, high, low)
    vel   = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

TREND_BREAKDOWN_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "tbd_extdrv3_001_psar_slow_distance_5d_diff_5d_diff":           {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_001_psar_slow_distance_5d_diff_5d_diff},
    "tbd_extdrv3_002_psar_slow_distance_21d_diff_5d_diff":          {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_002_psar_slow_distance_21d_diff_5d_diff},
    "tbd_extdrv3_003_psar_fast_distance_5d_diff_5d_diff":           {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_003_psar_fast_distance_5d_diff_5d_diff},
    "tbd_extdrv3_004_psar_fast_distance_21d_diff_5d_diff":          {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_004_psar_fast_distance_21d_diff_5d_diff},
    "tbd_extdrv3_005_supertrend_72_distance_5d_diff_5d_diff":       {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_005_supertrend_72_distance_5d_diff_5d_diff},
    "tbd_extdrv3_006_supertrend_72_distance_21d_diff_5d_diff":      {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_006_supertrend_72_distance_21d_diff_5d_diff},
    "tbd_extdrv3_007_supertrend_144_distance_5d_diff_5d_diff":      {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_007_supertrend_144_distance_5d_diff_5d_diff},
    "tbd_extdrv3_008_supertrend_144_distance_21d_diff_5d_diff":     {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_008_supertrend_144_distance_21d_diff_5d_diff},
    "tbd_extdrv3_009_aroon_osc50_5d_diff_5d_diff":                  {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_009_aroon_osc50_5d_diff_5d_diff},
    "tbd_extdrv3_010_aroon_osc50_21d_diff_5d_diff":                 {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_010_aroon_osc50_21d_diff_5d_diff},
    "tbd_extdrv3_011_ichimoku_cloud_thickness_5d_diff_5d_diff":     {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_011_ichimoku_cloud_thickness_5d_diff_5d_diff},
    "tbd_extdrv3_012_ichimoku_kijun_slope_5d_diff_5d_diff":         {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_012_ichimoku_kijun_slope_5d_diff_5d_diff},
    "tbd_extdrv3_013_vortex14_spread_5d_diff_5d_diff":              {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_013_vortex14_spread_5d_diff_5d_diff},
    "tbd_extdrv3_014_vortex14_spread_21d_diff_5d_diff":             {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_014_vortex14_spread_21d_diff_5d_diff},
    "tbd_extdrv3_015_vortex21_spread_5d_diff_5d_diff":              {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_015_vortex21_spread_5d_diff_5d_diff},
    "tbd_extdrv3_016_linreg_slope_21d_5d_diff_5d_diff":             {"inputs": ["close"],                "func": tbd_extdrv3_016_linreg_slope_21d_5d_diff_5d_diff},
    "tbd_extdrv3_017_linreg_slope_63d_5d_diff_5d_diff":             {"inputs": ["close"],                "func": tbd_extdrv3_017_linreg_slope_63d_5d_diff_5d_diff},
    "tbd_extdrv3_018_chande_kroll_distance_5d_diff_5d_diff":        {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_018_chande_kroll_distance_5d_diff_5d_diff},
    "tbd_extdrv3_019_chande_kroll_distance_21d_diff_5d_diff":       {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_019_chande_kroll_distance_21d_diff_5d_diff},
    "tbd_extdrv3_020_donchian_63_pct_rank_5d_diff_5d_diff":         {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_020_donchian_63_pct_rank_5d_diff_5d_diff},
    "tbd_extdrv3_021_adxr14_5d_diff_5d_diff":                       {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_021_adxr14_5d_diff_5d_diff},
    "tbd_extdrv3_022_trend_intensity_21d_5d_diff_5d_diff":          {"inputs": ["close"],                "func": tbd_extdrv3_022_trend_intensity_21d_5d_diff_5d_diff},
    "tbd_extdrv3_023_mass_index_5d_diff_5d_diff":                   {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_023_mass_index_5d_diff_5d_diff},
    "tbd_extdrv3_024_choppiness_14_5d_diff_5d_diff":                {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_024_choppiness_14_5d_diff_5d_diff},
    "tbd_extdrv3_025_extended_confluence_score_5d_diff_5d_diff":    {"inputs": ["close", "high", "low"], "func": tbd_extdrv3_025_extended_confluence_score_5d_diff_5d_diff},
}
