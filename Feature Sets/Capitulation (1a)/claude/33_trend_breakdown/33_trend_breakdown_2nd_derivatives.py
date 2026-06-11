"""
33_trend_breakdown — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base trend-breakdown concepts — velocity of crossover
        events, slope sign-changes, ADX collapse, Parabolic SAR distance velocity,
        Supertrend distance velocity, Aroon oscillator velocity, Ichimoku distance
        velocity, and structure-loss measures.
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
    """(close - SAR) / close using Parabolic SAR (af_step=0.02, af_max=0.2)."""
    n = len(high)
    hi = high.values; lo = low.values; cl = close.values
    sar = np.full(n, np.nan)
    is_bull = True; ep = hi[0]; af = 0.02; sar[0] = lo[0]
    for i in range(1, n):
        pv = sar[i - 1]
        if is_bull:
            ns = pv + af * (ep - pv)
            ns = min(ns, lo[i - 1])
            if i >= 2: ns = min(ns, lo[i - 2])
            if lo[i] < ns:
                is_bull = False; ns = ep; ep = lo[i]; af = 0.02
            else:
                if hi[i] > ep: ep = hi[i]; af = min(af + 0.02, 0.2)
        else:
            ns = pv + af * (ep - pv)
            ns = max(ns, hi[i - 1])
            if i >= 2: ns = max(ns, hi[i - 2])
            if hi[i] > ns:
                is_bull = True; ns = ep; ep = hi[i]; af = 0.02
            else:
                if lo[i] < ep: ep = lo[i]; af = min(af + 0.02, 0.2)
        sar[i] = ns
    sar_s = pd.Series(sar, index=close.index)
    return _safe_div(close - sar_s, close)


def _supertrend_distance(close: pd.Series, high: pd.Series, low: pd.Series,
                         atr_period: int = 10, multiplier: float = 3.0) -> pd.Series:
    """(close - Supertrend line) / close. Negative = bearish."""
    n = len(close)
    cl = close.values; hi = high.values; lo = low.values
    tr_arr = np.full(n, np.nan)
    for i in range(1, n):
        tr_arr[i] = max(hi[i] - lo[i], abs(hi[i] - cl[i-1]), abs(lo[i] - cl[i-1]))
    tr_arr[0] = hi[0] - lo[0]
    atr_arr = np.full(n, np.nan)
    if n >= atr_period:
        atr_arr[atr_period - 1] = np.nanmean(tr_arr[:atr_period])
        alpha = 1.0 / atr_period
        for i in range(atr_period, n):
            atr_arr[i] = atr_arr[i-1] * (1 - alpha) + tr_arr[i] * alpha
    hl2 = (hi + lo) / 2.0
    upper_basic = hl2 + multiplier * atr_arr
    lower_basic = hl2 - multiplier * atr_arr
    upper_band = np.full(n, np.nan); lower_band = np.full(n, np.nan)
    st_line = np.full(n, np.nan); trend = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(atr_arr[i]): continue
        if i == 0 or np.isnan(upper_band[i-1]):
            upper_band[i] = upper_basic[i]; lower_band[i] = lower_basic[i]
            trend[i] = 1.0 if cl[i] > lower_basic[i] else -1.0
            st_line[i] = lower_band[i] if trend[i] == 1.0 else upper_band[i]
            continue
        upper_band[i] = (upper_basic[i] if upper_basic[i] < upper_band[i-1] or cl[i-1] > upper_band[i-1] else upper_band[i-1])
        lower_band[i] = (lower_basic[i] if lower_basic[i] > lower_band[i-1] or cl[i-1] < lower_band[i-1] else lower_band[i-1])
        prev_t = trend[i-1]
        if prev_t == 1.0:
            trend[i] = -1.0 if cl[i] < lower_band[i] else 1.0
        else:
            trend[i] = 1.0 if cl[i] > upper_band[i] else -1.0
        st_line[i] = lower_band[i] if trend[i] == 1.0 else upper_band[i]
    st_s = pd.Series(st_line, index=close.index)
    return _safe_div(close - st_s, close)


def _aroon_osc(high: pd.Series, low: pd.Series, period: int) -> pd.Series:
    """Aroon Oscillator = Aroon Up - Aroon Down for given period."""
    w = period + 1
    def _bs_high(arr): return float(len(arr) - 1 - np.argmax(arr))
    def _bs_low(arr):  return float(len(arr) - 1 - np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_high, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_low,  raw=True)
    up  = (period - bsh) / period * 100
    dn  = (period - bsl) / period * 100
    return up - dn


def _ichimoku_distance_below_cloud(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below Ichimoku cloud bottom / close (0 if above cloud)."""
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    span_a = (tenkan + kijun) / 2.0
    span_b = (_rolling_max(high, 52) + _rolling_min(low, 52)) / 2.0
    cloud_bottom = pd.concat([span_a, span_b], axis=1).min(axis=1)
    gap = cloud_bottom - close
    return _safe_div(gap.clip(lower=0.0), close)


# ── 2nd-Derivative Feature Functions ──────────────────────────────────────────

def tbd_drv2_001_death_cross_state_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of SMA50-below-SMA200 binary state (velocity of cross state)."""
    state = (_rolling_mean(close, 50) < _rolling_mean(close, 200)).astype(float)
    return state.diff(_TD_WEEK)


def tbd_drv2_002_macd_histogram_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of MACD histogram (velocity of histogram change)."""
    _, _, hist = _macd_components(close)
    return hist.diff(_TD_WEEK)


def tbd_drv2_003_macd_histogram_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of MACD histogram (monthly velocity)."""
    _, _, hist = _macd_components(close)
    return hist.diff(_TD_MON)


def tbd_drv2_004_sma20_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of SMA20 daily slope (acceleration of SMA20 trend change)."""
    slope = _rolling_mean(close, _TD_MON).diff(1)
    return slope.diff(_TD_WEEK)


def tbd_drv2_005_sma200_slope_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of SMA200 daily slope (monthly velocity of long-term slope)."""
    slope = _rolling_mean(close, 200).diff(1)
    return slope.diff(_TD_MON)


def tbd_drv2_006_adx14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ADX(14) (velocity of trend-strength collapse)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return adx.diff(_TD_WEEK)


def tbd_drv2_007_adx14_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of ADX(14) (monthly change in trend strength)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return adx.diff(_TD_MON)


def tbd_drv2_008_dmi_spread_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of DI-minus-DI+ spread (velocity of bearish DMI widening)."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    spread = di_m - di_p
    return spread.diff(_TD_WEEK)


def tbd_drv2_009_psar_distance_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (close - SAR)/close distance (velocity of SAR divergence)."""
    dist = _psar_distance(close, high, low)
    return dist.diff(_TD_WEEK)


def tbd_drv2_010_psar_distance_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of (close - SAR)/close distance (monthly SAR velocity)."""
    dist = _psar_distance(close, high, low)
    return dist.diff(_TD_MON)


def tbd_drv2_011_supertrend_distance_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Supertrend(10,3) distance from price."""
    dist = _supertrend_distance(close, high, low)
    return dist.diff(_TD_WEEK)


def tbd_drv2_012_supertrend_distance_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of Supertrend(10,3) distance from price (monthly velocity)."""
    dist = _supertrend_distance(close, high, low)
    return dist.diff(_TD_MON)


def tbd_drv2_013_aroon_osc14_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Aroon Oscillator(14) (velocity of aroon momentum change)."""
    osc = _aroon_osc(high, low, 14)
    return osc.diff(_TD_WEEK)


def tbd_drv2_014_aroon_osc14_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of Aroon Oscillator(14)."""
    osc = _aroon_osc(high, low, 14)
    return osc.diff(_TD_MON)


def tbd_drv2_015_ichimoku_distance_below_cloud_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Ichimoku distance-below-cloud (velocity of cloud breakdown depth)."""
    dist = _ichimoku_distance_below_cloud(close, high, low)
    return dist.diff(_TD_WEEK)


def tbd_drv2_016_ichimoku_distance_below_cloud_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of Ichimoku distance-below-cloud (monthly velocity)."""
    dist = _ichimoku_distance_below_cloud(close, high, low)
    return dist.diff(_TD_MON)


def tbd_drv2_017_macd_line_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of MACD line level (velocity of MACD decline)."""
    macd, _, _ = _macd_components(close)
    return macd.diff(_TD_WEEK)


def tbd_drv2_018_sma_fan_spread_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of SMA20-SMA200 spread (velocity of fan breakdown)."""
    sma20  = _rolling_mean(close, _TD_MON)
    sma200 = _rolling_mean(close, 200)
    spread = _safe_div(sma20 - sma200, sma200)
    return spread.diff(_TD_WEEK)


def tbd_drv2_019_breakdown_state_count_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of total breakdown state count."""
    dc   = (_rolling_mean(close, 50) < _rolling_mean(close, 200)).astype(float)
    edc  = (_ewm_mean(close, 50) < _ewm_mean(close, 200)).astype(float)
    mb   = ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) < 0).astype(float)
    _, di_p, di_m = _adx_components(close, high, low, 14)
    dmi  = (di_m > di_p).astype(float)
    s20  = _rolling_mean(close, _TD_MON); s50 = _rolling_mean(close, 50)
    s200 = _rolling_mean(close, 200)
    slp  = ((s20 < s20.shift(1)) & (s50 < s50.shift(1)) & (s200 < s200.shift(1))).astype(float)
    score = dc + edc + mb + dmi + slp
    return score.diff(_TD_WEEK)


def tbd_drv2_020_macd_histogram_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of MACD histogram over 21-day window."""
    _, _, hist = _macd_components(close)
    return _linslope(hist, _TD_MON)


def tbd_drv2_021_psar_bearish_streak_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Parabolic SAR bearish streak length (velocity of streak change)."""
    n = len(high); hi = high.values; lo = low.values
    ps_trend = np.full(n, np.nan)
    is_bull = True; ep = hi[0]; af = 0.02; sv = lo[0]; ps_trend[0] = 1.0
    for i in range(1, n):
        pv = sv
        if is_bull:
            ns = pv + af * (ep - pv); ns = min(ns, lo[i-1])
            if i >= 2: ns = min(ns, lo[i-2])
            if lo[i] < ns:
                is_bull = False; ns = ep; ep = lo[i]; af = 0.02; ps_trend[i] = -1.0
            else:
                ps_trend[i] = 1.0
                if hi[i] > ep: ep = hi[i]; af = min(af + 0.02, 0.2)
        else:
            ns = pv + af * (ep - pv); ns = max(ns, hi[i-1])
            if i >= 2: ns = max(ns, hi[i-2])
            if hi[i] > ns:
                is_bull = True; ns = ep; ep = hi[i]; af = 0.02; ps_trend[i] = 1.0
            else:
                ps_trend[i] = -1.0
                if lo[i] < ep: ep = lo[i]; af = min(af + 0.02, 0.2)
        sv = ns
    trend_s = pd.Series(ps_trend, index=close.index)
    streak = _consec_streak(trend_s < 0)
    return streak.diff(_TD_WEEK)


def tbd_drv2_022_supertrend_streak_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Supertrend bearish streak (velocity of downtrend persistence)."""
    n = len(close); cl = close.values; hi = high.values; lo = low.values
    tr_arr = np.full(n, np.nan)
    for i in range(1, n):
        tr_arr[i] = max(hi[i]-lo[i], abs(hi[i]-cl[i-1]), abs(lo[i]-cl[i-1]))
    tr_arr[0] = hi[0] - lo[0]
    atr_arr = np.full(n, np.nan)
    ap = 10
    if n >= ap:
        atr_arr[ap-1] = np.nanmean(tr_arr[:ap]); alpha = 1.0/ap
        for i in range(ap, n): atr_arr[i] = atr_arr[i-1]*(1-alpha) + tr_arr[i]*alpha
    hl2 = (hi+lo)/2.0; ub = hl2+3.0*atr_arr; lb = hl2-3.0*atr_arr
    ub_b = np.full(n,np.nan); lb_b = np.full(n,np.nan); trend = np.full(n,np.nan)
    for i in range(n):
        if np.isnan(atr_arr[i]): continue
        if i==0 or np.isnan(ub_b[i-1]):
            ub_b[i]=ub[i]; lb_b[i]=lb[i]
            trend[i] = 1.0 if cl[i]>lb[i] else -1.0; continue
        ub_b[i] = ub[i] if (ub[i]<ub_b[i-1] or cl[i-1]>ub_b[i-1]) else ub_b[i-1]
        lb_b[i] = lb[i] if (lb[i]>lb_b[i-1] or cl[i-1]<lb_b[i-1]) else lb_b[i-1]
        pt = trend[i-1]
        trend[i] = (-1.0 if cl[i]<lb_b[i] else 1.0) if pt==1.0 else (1.0 if cl[i]>ub_b[i] else -1.0)
    trend_s = pd.Series(trend, index=close.index)
    streak = _consec_streak(trend_s < 0)
    return streak.diff(_TD_WEEK)


def tbd_drv2_023_aroon_osc25_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Aroon Oscillator(25)."""
    osc = _aroon_osc(high, low, 25)
    return osc.diff(_TD_WEEK)


def tbd_drv2_024_ichimoku_tenkan_kijun_spread_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (Tenkan - Kijun) / close spread (velocity of Ichimoku cross)."""
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    spread = _safe_div(tenkan - kijun, close)
    return spread.diff(_TD_WEEK)


def tbd_drv2_025_death_cross_state_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of death-cross binary state over trailing 21 days."""
    state = (_rolling_mean(close, 50) < _rolling_mean(close, 200)).astype(float)
    return _linslope(state, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

TREND_BREAKDOWN_REGISTRY_2ND_DERIVATIVES = {
    "tbd_drv2_001_death_cross_state_5d_diff": {"inputs": ["close"], "func": tbd_drv2_001_death_cross_state_5d_diff},
    "tbd_drv2_002_macd_histogram_5d_diff": {"inputs": ["close"], "func": tbd_drv2_002_macd_histogram_5d_diff},
    "tbd_drv2_003_macd_histogram_21d_diff": {"inputs": ["close"], "func": tbd_drv2_003_macd_histogram_21d_diff},
    "tbd_drv2_004_sma20_slope_5d_diff": {"inputs": ["close"], "func": tbd_drv2_004_sma20_slope_5d_diff},
    "tbd_drv2_005_sma200_slope_21d_diff": {"inputs": ["close"], "func": tbd_drv2_005_sma200_slope_21d_diff},
    "tbd_drv2_006_adx14_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_006_adx14_5d_diff},
    "tbd_drv2_007_adx14_21d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_007_adx14_21d_diff},
    "tbd_drv2_008_dmi_spread_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_008_dmi_spread_5d_diff},
    "tbd_drv2_009_psar_distance_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_009_psar_distance_5d_diff},
    "tbd_drv2_010_psar_distance_21d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_010_psar_distance_21d_diff},
    "tbd_drv2_011_supertrend_distance_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_011_supertrend_distance_5d_diff},
    "tbd_drv2_012_supertrend_distance_21d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_012_supertrend_distance_21d_diff},
    "tbd_drv2_013_aroon_osc14_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_013_aroon_osc14_5d_diff},
    "tbd_drv2_014_aroon_osc14_21d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_014_aroon_osc14_21d_diff},
    "tbd_drv2_015_ichimoku_distance_below_cloud_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_015_ichimoku_distance_below_cloud_5d_diff},
    "tbd_drv2_016_ichimoku_distance_below_cloud_21d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_016_ichimoku_distance_below_cloud_21d_diff},
    "tbd_drv2_017_macd_line_5d_diff": {"inputs": ["close"], "func": tbd_drv2_017_macd_line_5d_diff},
    "tbd_drv2_018_sma_fan_spread_5d_diff": {"inputs": ["close"], "func": tbd_drv2_018_sma_fan_spread_5d_diff},
    "tbd_drv2_019_breakdown_state_count_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_019_breakdown_state_count_5d_diff},
    "tbd_drv2_020_macd_histogram_slope_21d": {"inputs": ["close"], "func": tbd_drv2_020_macd_histogram_slope_21d},
    "tbd_drv2_021_psar_bearish_streak_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_021_psar_bearish_streak_5d_diff},
    "tbd_drv2_022_supertrend_streak_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_022_supertrend_streak_5d_diff},
    "tbd_drv2_023_aroon_osc25_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_023_aroon_osc25_5d_diff},
    "tbd_drv2_024_ichimoku_tenkan_kijun_spread_5d_diff": {"inputs": ["close", "high", "low"], "func": tbd_drv2_024_ichimoku_tenkan_kijun_spread_5d_diff},
    "tbd_drv2_025_death_cross_state_slope_21d": {"inputs": ["close"], "func": tbd_drv2_025_death_cross_state_slope_21d},
}
