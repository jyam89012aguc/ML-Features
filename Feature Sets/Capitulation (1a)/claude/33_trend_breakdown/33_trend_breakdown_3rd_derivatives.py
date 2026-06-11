"""
33_trend_breakdown — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative trend-breakdown concepts —
        acceleration of crossover velocity, slope-change acceleration,
        ADX collapse jerk, Parabolic SAR jerk, Supertrend jerk,
        Aroon oscillator acceleration, Ichimoku distance acceleration.
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


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _adx_components(close: pd.Series, high: pd.Series, low: pd.Series, period: int = 14):
    """Return (adx, plus_di, minus_di) using Wilder smoothing."""
    tr  = _tr(close, high, low)
    dm_plus  = (high - high.shift(1)).clip(lower=0.0)
    dm_minus = (low.shift(1) - low).clip(lower=0.0)
    dm_plus  = dm_plus.where(dm_plus > dm_minus, 0.0)
    dm_minus = dm_minus.where(dm_minus > dm_plus, 0.0)
    atr   = tr.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    sdi_p = dm_plus.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    sdi_m = dm_minus.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    di_p  = _safe_div(sdi_p, atr) * 100
    di_m  = _safe_div(sdi_m, atr) * 100
    dx    = _safe_div((di_p - di_m).abs(), (di_p + di_m).abs()) * 100
    adx   = dx.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    return adx, di_p, di_m


def _macd_components(close: pd.Series):
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    macd  = ema12 - ema26
    sig   = _ewm_mean(macd, 9)
    hist  = macd - sig
    return macd, sig, hist


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _psar_distance(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - SAR) / close — Parabolic SAR distance ratio."""
    n = len(high); hi = high.values; lo = low.values; cl = close.values
    sar = np.full(n, np.nan); is_bull = True; ep = hi[0]; af = 0.02; sar[0] = lo[0]
    for i in range(1, n):
        pv = sar[i-1]
        if is_bull:
            ns = pv + af*(ep-pv); ns = min(ns, lo[i-1])
            if i >= 2: ns = min(ns, lo[i-2])
            if lo[i] < ns: is_bull=False; ns=ep; ep=lo[i]; af=0.02
            else:
                if hi[i] > ep: ep=hi[i]; af=min(af+0.02, 0.2)
        else:
            ns = pv + af*(ep-pv); ns = max(ns, hi[i-1])
            if i >= 2: ns = max(ns, hi[i-2])
            if hi[i] > ns: is_bull=True; ns=ep; ep=hi[i]; af=0.02
            else:
                if lo[i] < ep: ep=lo[i]; af=min(af+0.02, 0.2)
        sar[i] = ns
    sar_s = pd.Series(sar, index=close.index)
    return _safe_div(close - sar_s, close)


def _supertrend_distance(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - Supertrend line) / close."""
    n = len(close); cl = close.values; hi = high.values; lo = low.values
    tr_arr = np.full(n, np.nan)
    for i in range(1, n):
        tr_arr[i] = max(hi[i]-lo[i], abs(hi[i]-cl[i-1]), abs(lo[i]-cl[i-1]))
    tr_arr[0] = hi[0]-lo[0]
    atr_arr = np.full(n, np.nan); ap = 10
    if n >= ap:
        atr_arr[ap-1] = np.nanmean(tr_arr[:ap]); alpha = 1.0/ap
        for i in range(ap, n): atr_arr[i] = atr_arr[i-1]*(1-alpha)+tr_arr[i]*alpha
    hl2 = (hi+lo)/2.0; ub = hl2+3.0*atr_arr; lb = hl2-3.0*atr_arr
    ub_b = np.full(n,np.nan); lb_b = np.full(n,np.nan)
    trend = np.full(n,np.nan); st_l = np.full(n,np.nan)
    for i in range(n):
        if np.isnan(atr_arr[i]): continue
        if i==0 or np.isnan(ub_b[i-1]):
            ub_b[i]=ub[i]; lb_b[i]=lb[i]
            trend[i]=1.0 if cl[i]>lb[i] else -1.0
            st_l[i]=lb_b[i] if trend[i]==1.0 else ub_b[i]; continue
        ub_b[i]=ub[i] if (ub[i]<ub_b[i-1] or cl[i-1]>ub_b[i-1]) else ub_b[i-1]
        lb_b[i]=lb[i] if (lb[i]>lb_b[i-1] or cl[i-1]<lb_b[i-1]) else lb_b[i-1]
        pt=trend[i-1]
        trend[i]=(-1.0 if cl[i]<lb_b[i] else 1.0) if pt==1.0 else (1.0 if cl[i]>ub_b[i] else -1.0)
        st_l[i]=lb_b[i] if trend[i]==1.0 else ub_b[i]
    st_s = pd.Series(st_l, index=close.index)
    return _safe_div(close - st_s, close)


def _aroon_osc(high: pd.Series, low: pd.Series, period: int) -> pd.Series:
    w = period+1
    def _bs_h(arr): return float(len(arr)-1-np.argmax(arr))
    def _bs_l(arr): return float(len(arr)-1-np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_h, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_l, raw=True)
    return ((period-bsh)/period*100) - ((period-bsl)/period*100)


def _ichimoku_distance(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    tenkan = (_rolling_max(high, 9)+_rolling_min(low, 9))/2.0
    kijun  = (_rolling_max(high,26)+_rolling_min(low,26))/2.0
    span_a = (tenkan+kijun)/2.0
    span_b = (_rolling_max(high,52)+_rolling_min(low,52))/2.0
    cloud_bottom = pd.concat([span_a, span_b], axis=1).min(axis=1)
    return _safe_div((cloud_bottom-close).clip(lower=0.0), close)


# ── 3rd-Derivative Feature Functions ──────────────────────────────────────────
# Each = diff/slope applied to a 2nd-derivative concept

def tbd_drv3_001_death_cross_state_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of death-cross state (acceleration of cross-state velocity)."""
    state = (_rolling_mean(close, 50) < _rolling_mean(close, 200)).astype(float)
    vel   = state.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_002_macd_histogram_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of MACD histogram (jerk in histogram change)."""
    _, _, hist = _macd_components(close)
    vel = hist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_003_macd_histogram_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of MACD histogram."""
    _, _, hist = _macd_components(close)
    vel21 = hist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_drv3_004_sma20_slope_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of SMA20 slope (acceleration of slope acceleration)."""
    slope = _rolling_mean(close, _TD_MON).diff(1)
    vel   = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_005_sma200_slope_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in SMA200 slope."""
    slope  = _rolling_mean(close, 200).diff(1)
    vel21  = slope.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_drv3_006_adx14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ADX(14) (jerk in trend-strength collapse)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    vel = adx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_007_adx14_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in ADX(14)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    vel21 = adx.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_drv3_008_dmi_spread_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of DI- minus DI+ spread (jerk in DMI divergence)."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    spread = di_m - di_p
    vel    = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_009_psar_distance_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of PSAR distance (jerk in SAR divergence rate)."""
    dist = _psar_distance(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_010_psar_distance_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of PSAR distance."""
    dist  = _psar_distance(close, high, low)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_drv3_011_supertrend_distance_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Supertrend distance (jerk in ST divergence rate)."""
    dist = _supertrend_distance(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_012_supertrend_distance_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Supertrend distance."""
    dist  = _supertrend_distance(close, high, low)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_drv3_013_aroon_osc14_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Aroon Oscillator(14) (jerk in Aroon momentum)."""
    osc = _aroon_osc(high, low, 14)
    vel = osc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_014_aroon_osc14_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Aroon Oscillator(14)."""
    osc   = _aroon_osc(high, low, 14)
    vel21 = osc.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_drv3_015_ichimoku_distance_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Ichimoku distance-below-cloud (jerk in cloud breakdown)."""
    dist = _ichimoku_distance(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_016_ichimoku_distance_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of Ichimoku below-cloud distance."""
    dist  = _ichimoku_distance(close, high, low)
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_drv3_017_macd_line_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of MACD line (jerk in MACD decline)."""
    macd, _, _ = _macd_components(close)
    vel = macd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_018_sma_fan_spread_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of SMA20-SMA200 spread ratio."""
    sma20  = _rolling_mean(close, _TD_MON)
    sma200 = _rolling_mean(close, 200)
    spread = _safe_div(sma20 - sma200, sma200)
    vel    = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_019_breakdown_state_count_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of breakdown state count (jerk in regime deterioration)."""
    dc   = (_rolling_mean(close, 50) < _rolling_mean(close, 200)).astype(float)
    edc  = (_ewm_mean(close, 50) < _ewm_mean(close, 200)).astype(float)
    mb   = ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) < 0).astype(float)
    _, di_p, di_m = _adx_components(close, high, low, 14)
    dmi  = (di_m > di_p).astype(float)
    s20  = _rolling_mean(close, _TD_MON); s50 = _rolling_mean(close, 50)
    s200 = _rolling_mean(close, 200)
    slp  = ((s20 < s20.shift(1)) & (s50 < s50.shift(1)) & (s200 < s200.shift(1))).astype(float)
    score = dc + edc + mb + dmi + slp
    vel   = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_020_dmi_spread_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in DI- minus DI+ spread."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    vel21 = (di_m - di_p).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tbd_drv3_021_aroon_osc25_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Aroon Oscillator(25) (jerk in 25-period Aroon)."""
    osc = _aroon_osc(high, low, 25)
    vel = osc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_022_ichimoku_tenkan_kijun_spread_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of (Tenkan - Kijun) / close spread."""
    tenkan = (_rolling_max(high, 9)+_rolling_min(low, 9))/2.0
    kijun  = (_rolling_max(high,26)+_rolling_min(low,26))/2.0
    spread = _safe_div(tenkan - kijun, close)
    vel    = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tbd_drv3_023_psar_distance_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of PSAR distance."""
    dist = _psar_distance(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def tbd_drv3_024_supertrend_distance_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of Supertrend distance."""
    dist = _supertrend_distance(close, high, low)
    vel  = dist.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def tbd_drv3_025_macd_histogram_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of MACD histogram."""
    _, _, hist = _macd_components(close)
    vel = hist.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

TREND_BREAKDOWN_REGISTRY_3RD_DERIVATIVES = {
    "tbd_drv3_001_death_cross_state_5d_diff_5d_diff": {"inputs": ["close"], "func": tbd_drv3_001_death_cross_state_5d_diff_5d_diff},
    "tbd_drv3_002_macd_histogram_5d_diff_5d_diff": {"inputs": ["close"], "func": tbd_drv3_002_macd_histogram_5d_diff_5d_diff},
    "tbd_drv3_003_macd_histogram_21d_diff_5d_diff": {"inputs": ["close"], "func": tbd_drv3_003_macd_histogram_21d_diff_5d_diff},
    "tbd_drv3_004_sma20_slope_5d_diff_5d_diff": {"inputs": ["close"], "func": tbd_drv3_004_sma20_slope_5d_diff_5d_diff},
    "tbd_drv3_005_sma200_slope_21d_diff_5d_diff": {"inputs": ["close"], "func": tbd_drv3_005_sma200_slope_21d_diff_5d_diff},
    "tbd_drv3_006_adx14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_006_adx14_5d_diff_5d_diff},
    "tbd_drv3_007_adx14_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_007_adx14_21d_diff_5d_diff},
    "tbd_drv3_008_dmi_spread_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_008_dmi_spread_5d_diff_5d_diff},
    "tbd_drv3_009_psar_distance_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_009_psar_distance_5d_diff_5d_diff},
    "tbd_drv3_010_psar_distance_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_010_psar_distance_21d_diff_5d_diff},
    "tbd_drv3_011_supertrend_distance_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_011_supertrend_distance_5d_diff_5d_diff},
    "tbd_drv3_012_supertrend_distance_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_012_supertrend_distance_21d_diff_5d_diff},
    "tbd_drv3_013_aroon_osc14_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_013_aroon_osc14_5d_diff_5d_diff},
    "tbd_drv3_014_aroon_osc14_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_014_aroon_osc14_21d_diff_5d_diff},
    "tbd_drv3_015_ichimoku_distance_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_015_ichimoku_distance_5d_diff_5d_diff},
    "tbd_drv3_016_ichimoku_distance_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_016_ichimoku_distance_21d_diff_5d_diff},
    "tbd_drv3_017_macd_line_5d_diff_5d_diff": {"inputs": ["close"], "func": tbd_drv3_017_macd_line_5d_diff_5d_diff},
    "tbd_drv3_018_sma_fan_spread_5d_diff_5d_diff": {"inputs": ["close"], "func": tbd_drv3_018_sma_fan_spread_5d_diff_5d_diff},
    "tbd_drv3_019_breakdown_state_count_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_019_breakdown_state_count_5d_diff_5d_diff},
    "tbd_drv3_020_dmi_spread_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_020_dmi_spread_21d_diff_5d_diff},
    "tbd_drv3_021_aroon_osc25_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_021_aroon_osc25_5d_diff_5d_diff},
    "tbd_drv3_022_ichimoku_tenkan_kijun_spread_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv3_022_ichimoku_tenkan_kijun_spread_5d_diff_5d_diff},
    "tbd_drv3_023_psar_distance_slope_21d": {"inputs": ["close", "high", "low"], "func": tbd_drv3_023_psar_distance_slope_21d},
    "tbd_drv3_024_supertrend_distance_slope_21d": {"inputs": ["close", "high", "low"], "func": tbd_drv3_024_supertrend_distance_slope_21d},
    "tbd_drv3_025_macd_histogram_5d_diff_slope_21d": {"inputs": ["close"], "func": tbd_drv3_025_macd_histogram_5d_diff_slope_21d},
}
