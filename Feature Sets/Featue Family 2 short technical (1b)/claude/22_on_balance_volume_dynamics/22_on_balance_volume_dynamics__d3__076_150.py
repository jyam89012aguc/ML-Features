"""on_balance_volume_dynamics d3 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across base__001_075 and base__076_150. Each feature
encodes a *different concept* in the OBV-and-related cumulative-signed-volume
theme: slope / divergence / regime / decay / momentum / structural events.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ---------------------------- OBV primitives ----------------------------

def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()


def _obv_oo(close: pd.Series, open_: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close - open_).fillna(0.0)
    return (sgn * volume).cumsum()


def _nvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = close.pct_change().fillna(0.0)
    dv = volume.diff()
    contrib = np.where(dv < 0, r, 0.0)
    return pd.Series(contrib, index=close.index).cumsum()


def _pvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = close.pct_change().fillna(0.0)
    dv = volume.diff()
    contrib = np.where(dv > 0, r, 0.0)
    return pd.Series(contrib, index=close.index).cumsum()


# ---------------------------- family helpers ----------------------------

def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _rolling_argmax_age(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _a(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmax(w))
        return float(len(w) - 1 - idx)
    return s.rolling(window, min_periods=min_periods).apply(_a, raw=True)


def _np_autocorr_lag(w, lag):
    v = w[~np.isnan(w)]
    if v.size < lag + 3:
        return np.nan
    a = v[:-lag] - v[:-lag].mean()
    b = v[lag:] - v[lag:].mean()
    den = np.sqrt((a * a).sum() * (b * b).sum())
    if den <= 0:
        return np.nan
    return float((a * b).sum() / den)


# ============================================================
# Bucket N — Up-vol / down-vol decomposition (076-082)
# ============================================================

def f22_obvd_076_up_volume_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on up-close bars over trailing 21d — short-term up-flow magnitude."""
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0)
    return up_v.rolling(MDAYS, min_periods=WDAYS).sum()


def f22_obvd_077_down_volume_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on down-close bars over trailing 21d — short-term down-flow magnitude."""
    sgn = np.sign(close.diff())
    dn_v = volume.where(sgn < 0, 0.0)
    return dn_v.rolling(MDAYS, min_periods=WDAYS).sum()


def f22_obvd_078_up_to_down_volume_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum up_vol 21d) / (sum down_vol 21d)."""
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(up_v, dn_v + 1.0)


def f22_obvd_079_up_to_down_volume_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum up_vol 63d) / (sum down_vol 63d)."""
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(up_v, dn_v + 1.0)


def f22_obvd_080_net_volume_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score over 252d of net_volume = up_vol - down_vol (computed daily as signed_volume)."""
    sgn = np.sign(close.diff())
    net = sgn.fillna(0.0) * volume
    return _rolling_zscore(net, YDAYS)


def f22_obvd_081_cum_up_volume_to_total_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d total volume that occurred on up-close bars."""
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(up_v, tot)


def f22_obvd_082_cum_down_volume_to_total_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d total volume that occurred on down-close bars."""
    sgn = np.sign(close.diff())
    dn_v = volume.where(sgn < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(dn_v, tot)


# ============================================================
# Bucket O — OBV-vs-HHV(price) divergence (083-088)
# ============================================================

def f22_obvd_083_obv_at_252hh_minus_obv_max_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV at most recent 252d-high bar minus 252d-trailing max OBV. Negative = OBV peak preceded price peak."""
    obv = _obv(close, volume)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_hh = high >= pmax
    obv_at_hh = obv.where(is_hh, np.nan).ffill()
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    return obv_at_hh - omax


def f22_obvd_084_obv_at_252hh_zscore_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV (vs 252d distribution) at the most recent 252d-high bar."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv, YDAYS)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_hh = high >= pmax
    return z.where(is_hh, np.nan).ffill()


def f22_obvd_085_bars_since_obv_at_252hh(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent 252d-high bar (uses high series to find the high)."""
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_hh = (high >= pmax).astype(int)
    grp = is_hh.cumsum()
    return (~is_hh.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)


def f22_obvd_086_obv_delta_between_consecutive_252_highs(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV at current 252d-high minus OBV at previous 252d-high — flow change between consecutive price peaks."""
    obv = _obv(close, volume)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_hh = high >= pmax
    obv_at_hh = obv.where(is_hh, np.nan)
    return obv_at_hh - obv_at_hh.shift(1).ffill()


def f22_obvd_087_obv_lower_at_higher_price_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when current 252d-price-high bar has OBV lower than the prior 252d-high's OBV — classical bearish divergence."""
    obv = _obv(close, volume)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_hh = high >= pmax
    obv_at_hh = obv.where(is_hh, np.nan)
    return ((obv_at_hh < obv_at_hh.shift(1).ffill()) & is_hh).astype(float)


def f22_obvd_088_obv_at_hh_running_max_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 252d-high bars in trailing 252d where OBV did NOT make a new high either."""
    obv = _obv(close, volume)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    is_pp = high >= pmax
    no_op = obv < omax
    return (is_pp & no_op).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket P — CSV-OO variant (089-093)
# ============================================================

def f22_obvd_089_obv_oo_slope_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope(63d) of CSV-OO = cumulative volume signed by (close - open)."""
    obv_oo = _obv_oo(close, open, volume)
    return _rolling_slope(obv_oo, QDAYS)


def f22_obvd_090_obv_oo_zscore_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of CSV-OO cumulative-signed-volume."""
    obv_oo = _obv_oo(close, open, volume)
    return _rolling_zscore(obv_oo, YDAYS)


def f22_obvd_091_obv_minus_obv_oo_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus CSV-OO — disagreement between the two sign conventions (sign-of-close-vs-prev vs close-vs-open)."""
    obv = _obv(close, volume)
    obv_oo = _obv_oo(close, open, volume)
    return obv - obv_oo


def f22_obvd_092_obv_oo_decay_ratio_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CSV-OO / 252d-trailing-max CSV-OO."""
    obv_oo = _obv_oo(close, open, volume)
    rmax = obv_oo.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(obv_oo, rmax)


def f22_obvd_093_obv_oo_minus_price_slope_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CSV-OO slope(252d) minus log-price slope(252d) — CSV-OO divergence with price."""
    obv_oo = _obv_oo(close, open, volume)
    return _rolling_slope(obv_oo, YDAYS) - _rolling_slope(_safe_log(close), YDAYS)


# ============================================================
# Bucket Q — NVI / PVI primitives (094-098)
# ============================================================

def f22_obvd_094_nvi_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of Negative Volume Index over 63d — flow on quiet days."""
    return _rolling_slope(_nvi(close, volume), QDAYS)


def f22_obvd_095_nvi_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of NVI — quiet-day flow extreme."""
    return _rolling_zscore(_nvi(close, volume), YDAYS)


def f22_obvd_096_pvi_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of Positive Volume Index over 63d — flow on busy days."""
    return _rolling_slope(_pvi(close, volume), QDAYS)


def f22_obvd_097_pvi_minus_nvi_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVI slope(252d) minus NVI slope(252d) — busy-day vs quiet-day flow divergence."""
    return _rolling_slope(_pvi(close, volume), YDAYS) - _rolling_slope(_nvi(close, volume), YDAYS)


def f22_obvd_098_pvi_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of PVI."""
    return _rolling_zscore(_pvi(close, volume), YDAYS)


# ============================================================
# Bucket R — Up-day weight ratios (099-105)
# ============================================================

def f22_obvd_099_avg_vol_up_days_minus_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on up-close days minus mean volume on down-close days, trailing 63d."""
    sgn = np.sign(close.diff())
    up = volume.where(sgn > 0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    dn = volume.where(sgn < 0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    return up - dn


def f22_obvd_100_avg_vol_up_days_minus_down_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on up-close days minus mean volume on down-close days, trailing 252d."""
    sgn = np.sign(close.diff())
    up = volume.where(sgn > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = volume.where(sgn < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return up - dn


def f22_obvd_101_signed_vol_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of signed-volume (= obv diff) over 252d — asymmetry of flow distribution."""
    sgn = np.sign(close.diff())
    sv = sgn.fillna(0.0) * volume
    return sv.rolling(YDAYS, min_periods=QDAYS).skew()


def f22_obvd_102_signed_vol_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling excess kurtosis of signed-volume over 252d — tail-heaviness of flow."""
    sgn = np.sign(close.diff())
    sv = sgn.fillna(0.0) * volume
    return sv.rolling(YDAYS, min_periods=QDAYS).kurt()


def f22_obvd_103_count_up_days_in_63d(close: pd.Series) -> pd.Series:
    """Trailing 63d count of up-close days."""
    sgn = np.sign(close.diff())
    return (sgn > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_104_frac_up_days_in_252d(close: pd.Series) -> pd.Series:
    """Trailing 252d fraction of up-close days."""
    sgn = np.sign(close.diff())
    return (sgn > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_105_up_days_with_vol_above_med_minus_down_days_with_vol_above_med_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count(up bars w/ vol > 252d-med) minus count(down bars w/ vol > 252d-med), trailing 252d."""
    sgn = np.sign(close.diff())
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    hi_v = volume > med
    up_hi = ((sgn > 0) & hi_v).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dn_hi = ((sgn < 0) & hi_v).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return up_hi - dn_hi


# ============================================================
# Bucket S — OBV-EMA structural events (106-111)
# ============================================================

def f22_obvd_106_obv_ema21_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope(63d) of EMA21(OBV) — smoothed flow trend."""
    obv = _obv(close, volume)
    ema = obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return _rolling_slope(ema, QDAYS)


def f22_obvd_107_obv_ema21_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope(252d) of EMA21(OBV)."""
    obv = _obv(close, volume)
    ema = obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return _rolling_slope(ema, YDAYS)


def f22_obvd_108_obv_ema_cross_down_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when EMA9(OBV) crosses below EMA21(OBV) — bearish OBV crossover."""
    obv = _obv(close, volume)
    fast = obv.ewm(span=9, min_periods=3, adjust=False).mean()
    slow = obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    cur_above = fast > slow
    prev_above = cur_above.shift(1, fill_value=False)
    return (prev_above & ~cur_above).astype(float)


def f22_obvd_109_obv_ema_cross_up_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when EMA9(OBV) crosses above EMA21(OBV) — bullish OBV crossover."""
    obv = _obv(close, volume)
    fast = obv.ewm(span=9, min_periods=3, adjust=False).mean()
    slow = obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    cur_above = fast > slow
    prev_above = cur_above.shift(1, fill_value=False)
    return (~prev_above & cur_above).astype(float)


def f22_obvd_110_obv_macd_hist_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV MACD-histogram: (EMA9(OBV) - EMA21(OBV)) - signal-line(EMA9 of that diff). 252d window normalization."""
    obv = _obv(close, volume)
    macd = obv.ewm(span=9, min_periods=3, adjust=False).mean() - obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    signal = macd.ewm(span=9, min_periods=3, adjust=False).mean()
    return macd - signal


def f22_obvd_111_obv_ema_distance_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (OBV - EMA21(OBV)) — how unusual is current distance from MA."""
    obv = _obv(close, volume)
    ema = obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return _rolling_zscore(obv - ema, YDAYS)


# ============================================================
# Bucket T — Multi-horizon ratio constructions (112-118)
# ============================================================

def f22_obvd_112_obv_pct_change_21d_to_pct_change_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV(t)/OBV(t-21) divided by OBV(t)/OBV(t-252) — short/long growth ratio."""
    obv = _obv(close, volume)
    r21 = _safe_div(obv, obv.shift(MDAYS))
    r252 = _safe_div(obv, obv.shift(YDAYS))
    return _safe_div(r21, r252)


def f22_obvd_113_obv_slope_21d_minus_slope_63d_minus_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope(21d) - slope(63d) - slope(252d) — multi-scale acceleration index."""
    obv = _obv(close, volume)
    return _rolling_slope(obv, MDAYS) - _rolling_slope(obv, QDAYS) - _rolling_slope(obv, YDAYS)


def f22_obvd_114_obv_short_minus_long_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV z-score(63d) minus z-score(504d) — short-vs-long extreme."""
    obv = _obv(close, volume)
    return _rolling_zscore(obv, QDAYS) - _rolling_zscore(obv, DDAYS_2Y)


def f22_obvd_115_ratio_obv_to_obv_ema63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current OBV / EMA63(OBV) — > 1 when above quarterly trend baseline."""
    obv = _obv(close, volume)
    ema = obv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    return _safe_div(obv, ema)


def f22_obvd_116_obv_position_in_252d_range(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - 252d-min-OBV) / (252d-max-OBV - 252d-min-OBV) — normalized 0-1 position."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(obv - rmin, rmax - rmin)


def f22_obvd_117_obv_position_in_504d_range(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - 504d-min) / (504d-max - 504d-min) — biennial normalized position."""
    obv = _obv(close, volume)
    rmax = obv.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    rmin = obv.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(obv - rmin, rmax - rmin)


def f22_obvd_118_obv_position_diff_short_minus_long(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV position-in-63d-range minus OBV position-in-252d-range — short-vs-long position contrast."""
    obv = _obv(close, volume)
    rmax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    rmin63 = obv.rolling(QDAYS, min_periods=MDAYS).min()
    p63 = _safe_div(obv - rmin63, rmax63 - rmin63)
    rmax252 = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rmin252 = obv.rolling(YDAYS, min_periods=QDAYS).min()
    p252 = _safe_div(obv - rmin252, rmax252 - rmin252)
    return p63 - p252


# ============================================================
# Bucket U — Divergence over multiple horizons + structural (119-128)
# ============================================================

def f22_obvd_119_obv_minus_close_zscore_diff_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV z(252d) minus close z(252d) — z-space divergence."""
    obv = _obv(close, volume)
    return _rolling_zscore(obv, YDAYS) - _rolling_zscore(close, YDAYS)


def f22_obvd_120_obv_pct_rank_minus_close_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank(252d) minus close pct rank(252d) — rank-space divergence."""
    obv = _obv(close, volume)
    return _rolling_pct_rank(obv, YDAYS) - _rolling_pct_rank(close, YDAYS)


def f22_obvd_121_obv_below_zero_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV < 0 (cumulative-flow net negative since the OBV series start)."""
    obv = _obv(close, volume)
    return (obv < 0).astype(float)


def f22_obvd_122_obv_zero_cross_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of OBV crossings of zero in trailing 252d (either direction)."""
    obv = _obv(close, volume)
    cross = (np.sign(obv).diff().abs() > 0).astype(float)
    return cross.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_123_obv_bear_streak_below_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive-bar streak with OBV < its own 21d-trailing max — local distribution persistence."""
    obv = _obv(close, volume)
    rmax21 = obv.rolling(MDAYS, min_periods=WDAYS).max()
    return _consecutive_true_streak(obv < rmax21).astype(float)


def f22_obvd_124_obv_recent_local_max_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count over trailing 63d of bars where OBV equals 21d trailing max — local flow tops."""
    obv = _obv(close, volume)
    rmax21 = obv.rolling(MDAYS, min_periods=WDAYS).max()
    return (obv >= rmax21).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_125_obv_velocity_acceleration_norm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV.diff() z-scored over 252d — per-bar flow velocity vs trailing distribution."""
    obv = _obv(close, volume)
    return _rolling_zscore(obv.diff(), YDAYS)


def f22_obvd_126_obv_diff_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of OBV-diff (i.e. signed volume) over 252d."""
    obv = _obv(close, volume)
    return obv.diff().rolling(YDAYS, min_periods=QDAYS).skew()


def f22_obvd_127_obv_diff_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling excess kurtosis of OBV-diff over 252d."""
    obv = _obv(close, volume)
    return obv.diff().rolling(YDAYS, min_periods=QDAYS).kurt()


def f22_obvd_128_obv_sign_imbalance_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(count up-sign days - count down-sign days) / (count up + count down), trailing 252d."""
    sgn = np.sign(close.diff())
    up = (sgn > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = (sgn < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(up - dn, up + dn)


# ============================================================
# Bucket V — Combined / composite (129-138)
# ============================================================

def f22_obvd_129_obv_underperformance_indicator_combined(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if all of: price 252d new-high AND OBV z(252d)<0 AND OBV slope(63d)<0."""
    obv = _obv(close, volume)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    z = _rolling_zscore(obv, YDAYS)
    so = _rolling_slope(obv, QDAYS)
    return ((high >= pmax) & (z < 0) & (so < 0)).astype(float)


def f22_obvd_130_obv_distribution_score_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of binary distribution signals over trailing 252d: (OBV slope<0)+(OBV<MA63)+(div w/ price)+(below max)."""
    obv = _obv(close, volume)
    so = _rolling_slope(obv, QDAYS)
    sma63 = obv.rolling(QDAYS, min_periods=MDAYS).mean()
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    div = (high >= pmax) & (obv < omax)
    return ((so < 0).astype(float)
            + (obv < sma63).astype(float)
            + div.astype(float)
            + (obv < rmax).astype(float))


def f22_obvd_131_obv_pct_change_5d_minus_close_pct_change_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct change(5d) minus close pct change(5d) — short divergence frame."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff(WDAYS), obv.shift(WDAYS).abs() + 1.0) - close.pct_change(WDAYS)


def f22_obvd_132_obv_pct_change_21d_minus_close_pct_change_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct change(21d) minus close pct change(21d) — monthly divergence."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff(MDAYS), obv.shift(MDAYS).abs() + 1.0) - close.pct_change(MDAYS)


def f22_obvd_133_obv_higher_low_no_price_higher_low_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 63d-trailing OBV-min > 252d-trailing OBV-min AND 63d-trailing low <= 252d-trailing low — bullish divergence kept here as inverse of bearish."""
    obv = _obv(close, volume)
    omin63 = obv.rolling(QDAYS, min_periods=MDAYS).min()
    omin252 = obv.rolling(YDAYS, min_periods=QDAYS).min()
    lmin63 = low.rolling(QDAYS, min_periods=MDAYS).min()
    lmin252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    return ((omin63 > omin252) & (lmin63 <= lmin252)).astype(float)


def f22_obvd_134_obv_lower_high_no_price_lower_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 63d-OBV-max < 252d-OBV-max AND 63d-price-max >= 252d-price-max — classical bearish divergence (rolling)."""
    obv = _obv(close, volume)
    omax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    omax252 = obv.rolling(YDAYS, min_periods=QDAYS).max()
    hmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    hmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((omax63 < omax252) & (hmax63 >= hmax252)).astype(float)


def f22_obvd_135_obv_divergence_persistence_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars satisfying the lower-OBV-high-while-price-high divergence condition."""
    obv = _obv(close, volume)
    omax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    omax252 = obv.rolling(YDAYS, min_periods=QDAYS).max()
    hmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    hmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((omax63 < omax252) & (hmax63 >= hmax252)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_136_obv_distance_from_252d_high_normalized_by_atr(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - 252d-max-OBV) / (ATR21 * volume.rolling(21).mean()) — ATR-normalized OBV drawdown."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    vbase = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(obv - rmax, atr * vbase + 1.0)


def f22_obvd_137_obv_zscore_at_high_price_decile_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV z(252d) on bars where high is in top decile of 252d highs — flow strength at peaks."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv, YDAYS)
    pr_h = _rolling_pct_rank(high, YDAYS)
    return z.where(pr_h >= 0.90, np.nan)


def f22_obvd_138_obv_ratio_to_signed_vol_baseline_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV divided by sum-of-volume(252d) — normalized cumulative flow as fraction of total volume."""
    obv = _obv(close, volume)
    tot = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(obv, tot)


# ============================================================
# Bucket W — Additional structural primitives (139-150)
# ============================================================

def f22_obvd_139_obv_drawdown_streak_consec(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive bars OBV has been below its 252d trailing max — uninterrupted-deficit streak."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    return _consecutive_true_streak(obv < rmax).astype(float)


def f22_obvd_140_obv_count_new_252d_lows(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV bars equal to 252d trailing min — flow capitulation events."""
    obv = _obv(close, volume)
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    return (obv <= rmin).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_141_obv_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling excess kurtosis of OBV (level) over 252d."""
    obv = _obv(close, volume)
    return obv.rolling(YDAYS, min_periods=QDAYS).kurt()


def f22_obvd_142_obv_slope_r2_combined_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope(252d) multiplied by R² of OBV over 252d — slope weighted by trend cleanliness."""
    obv = _obv(close, volume)
    slope = _rolling_slope(obv, YDAYS)
    def _r2(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        x = np.arange(v.size, dtype=float)
        xm = x.mean(); ym = v.mean()
        sxx = ((x - xm) ** 2).sum()
        syy = ((v - ym) ** 2).sum()
        sxy = ((x - xm) * (v - ym)).sum()
        if sxx <= 0 or syy <= 0:
            return np.nan
        r = sxy / np.sqrt(sxx * syy)
        return float(r * r)
    r2 = obv.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)
    return slope * r2


def f22_obvd_143_obv_first_diff_zero_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with zero OBV-diff (= unchanged close → zero signed volume)."""
    obv = _obv(close, volume)
    return (obv.diff() == 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_144_obv_in_top_quartile_of_252d_range_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV is in top 25% of (252d-max-OBV - 252d-min-OBV) range."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(obv - rmin, rmax - rmin)
    return (pos >= 0.75).astype(float)


def f22_obvd_145_obv_in_bottom_quartile_of_252d_range_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV is in bottom 25% of 252d range."""
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(obv - rmin, rmax - rmin)
    return (pos <= 0.25).astype(float)


def f22_obvd_146_obv_max_age_minus_obv_min_age_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV peak age(252d) minus OBV trough age(252d) — positive = trough more recent than peak (post-peak phase)."""
    obv = _obv(close, volume)
    max_age = _rolling_argmax_age(obv, YDAYS)
    def _amn(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmin(w))
        return float(len(w) - 1 - idx)
    min_age = obv.rolling(YDAYS, min_periods=QDAYS).apply(_amn, raw=True)
    return max_age - min_age


def f22_obvd_147_obv_persistence_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 252d of |OBV-diff sign| consistency = fraction of bars sharing same sign as 5-bar majority."""
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    rolling_majority = sgn.rolling(WDAYS, min_periods=2).apply(lambda w: float(np.sign(w.mean()) if w.size > 0 else np.nan), raw=True)
    match = (sgn == rolling_majority).astype(float)
    return match.rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_148_obv_at_close_in_top_decile_252d_mean(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV z(252d) on bars where close is in top decile of 252d range."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return z.where(pos >= 0.90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_149_obv_runs_test_proxy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Runs-test proxy: number of OBV-sign runs in 252d divided by expected (n/2)."""
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    def _r(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        s = np.sign(v)
        runs = 1 + np.sum(s[1:] != s[:-1])
        return float(runs / (v.size / 2.0))
    return sgn.rolling(YDAYS, min_periods=QDAYS).apply(_r, raw=True)


def f22_obvd_150_composite_obv_health_score_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: sum of (OBV>0, OBV>EMA63(OBV), OBV slope(252d)>0, OBV pct_rank(252d)>0.5) — high = healthy flow."""
    obv = _obv(close, volume)
    ema63 = obv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    slope = _rolling_slope(obv, YDAYS)
    pr = _rolling_pct_rank(obv, YDAYS)
    return ((obv > 0).astype(float)
            + (obv > ema63).astype(float)
            + (slope > 0).astype(float)
            + (pr > 0.5).astype(float))


# ============================================================
#                         REGISTRY 076-150
# ============================================================



def f22_obvd_076_up_volume_sum_21d_d3(close, volume):
    return f22_obvd_076_up_volume_sum_21d(close, volume).diff().diff().diff()


def f22_obvd_077_down_volume_sum_21d_d3(close, volume):
    return f22_obvd_077_down_volume_sum_21d(close, volume).diff().diff().diff()


def f22_obvd_078_up_to_down_volume_ratio_21d_d3(close, volume):
    return f22_obvd_078_up_to_down_volume_ratio_21d(close, volume).diff().diff().diff()


def f22_obvd_079_up_to_down_volume_ratio_63d_d3(close, volume):
    return f22_obvd_079_up_to_down_volume_ratio_63d(close, volume).diff().diff().diff()


def f22_obvd_080_net_volume_zscore_252d_d3(close, volume):
    return f22_obvd_080_net_volume_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_081_cum_up_volume_to_total_volume_252d_d3(close, volume):
    return f22_obvd_081_cum_up_volume_to_total_volume_252d(close, volume).diff().diff().diff()


def f22_obvd_082_cum_down_volume_to_total_volume_252d_d3(close, volume):
    return f22_obvd_082_cum_down_volume_to_total_volume_252d(close, volume).diff().diff().diff()


def f22_obvd_083_obv_at_252hh_minus_obv_max_252d_d3(high, close, volume):
    return f22_obvd_083_obv_at_252hh_minus_obv_max_252d(high, close, volume).diff().diff().diff()


def f22_obvd_084_obv_at_252hh_zscore_252d_d3(high, close, volume):
    return f22_obvd_084_obv_at_252hh_zscore_252d(high, close, volume).diff().diff().diff()


def f22_obvd_085_bars_since_obv_at_252hh_d3(high, close, volume):
    return f22_obvd_085_bars_since_obv_at_252hh(high, close, volume).diff().diff().diff()


def f22_obvd_086_obv_delta_between_consecutive_252_highs_d3(high, close, volume):
    return f22_obvd_086_obv_delta_between_consecutive_252_highs(high, close, volume).diff().diff().diff()


def f22_obvd_087_obv_lower_at_higher_price_high_indicator_d3(high, close, volume):
    return f22_obvd_087_obv_lower_at_higher_price_high_indicator(high, close, volume).diff().diff().diff()


def f22_obvd_088_obv_at_hh_running_max_count_252d_d3(high, close, volume):
    return f22_obvd_088_obv_at_hh_running_max_count_252d(high, close, volume).diff().diff().diff()


def f22_obvd_089_obv_oo_slope_63d_d3(open, close, volume):
    return f22_obvd_089_obv_oo_slope_63d(open, close, volume).diff().diff().diff()


def f22_obvd_090_obv_oo_zscore_252d_d3(open, close, volume):
    return f22_obvd_090_obv_oo_zscore_252d(open, close, volume).diff().diff().diff()


def f22_obvd_091_obv_minus_obv_oo_252d_d3(open, close, volume):
    return f22_obvd_091_obv_minus_obv_oo_252d(open, close, volume).diff().diff().diff()


def f22_obvd_092_obv_oo_decay_ratio_252d_d3(open, close, volume):
    return f22_obvd_092_obv_oo_decay_ratio_252d(open, close, volume).diff().diff().diff()


def f22_obvd_093_obv_oo_minus_price_slope_252d_d3(open, close, volume):
    return f22_obvd_093_obv_oo_minus_price_slope_252d(open, close, volume).diff().diff().diff()


def f22_obvd_094_nvi_slope_63d_d3(close, volume):
    return f22_obvd_094_nvi_slope_63d(close, volume).diff().diff().diff()


def f22_obvd_095_nvi_zscore_252d_d3(close, volume):
    return f22_obvd_095_nvi_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_096_pvi_slope_63d_d3(close, volume):
    return f22_obvd_096_pvi_slope_63d(close, volume).diff().diff().diff()


def f22_obvd_097_pvi_minus_nvi_slope_252d_d3(close, volume):
    return f22_obvd_097_pvi_minus_nvi_slope_252d(close, volume).diff().diff().diff()


def f22_obvd_098_pvi_zscore_252d_d3(close, volume):
    return f22_obvd_098_pvi_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_099_avg_vol_up_days_minus_down_days_63d_d3(close, volume):
    return f22_obvd_099_avg_vol_up_days_minus_down_days_63d(close, volume).diff().diff().diff()


def f22_obvd_100_avg_vol_up_days_minus_down_days_252d_d3(close, volume):
    return f22_obvd_100_avg_vol_up_days_minus_down_days_252d(close, volume).diff().diff().diff()


def f22_obvd_101_signed_vol_skew_252d_d3(close, volume):
    return f22_obvd_101_signed_vol_skew_252d(close, volume).diff().diff().diff()


def f22_obvd_102_signed_vol_kurt_252d_d3(close, volume):
    return f22_obvd_102_signed_vol_kurt_252d(close, volume).diff().diff().diff()


def f22_obvd_103_count_up_days_in_63d_d3(close):
    return f22_obvd_103_count_up_days_in_63d(close).diff().diff().diff()


def f22_obvd_104_frac_up_days_in_252d_d3(close):
    return f22_obvd_104_frac_up_days_in_252d(close).diff().diff().diff()


def f22_obvd_105_up_days_with_vol_above_med_minus_down_days_with_vol_above_med_252d_d3(close, volume):
    return f22_obvd_105_up_days_with_vol_above_med_minus_down_days_with_vol_above_med_252d(close, volume).diff().diff().diff()


def f22_obvd_106_obv_ema21_slope_63d_d3(close, volume):
    return f22_obvd_106_obv_ema21_slope_63d(close, volume).diff().diff().diff()


def f22_obvd_107_obv_ema21_slope_252d_d3(close, volume):
    return f22_obvd_107_obv_ema21_slope_252d(close, volume).diff().diff().diff()


def f22_obvd_108_obv_ema_cross_down_indicator_d3(close, volume):
    return f22_obvd_108_obv_ema_cross_down_indicator(close, volume).diff().diff().diff()


def f22_obvd_109_obv_ema_cross_up_indicator_d3(close, volume):
    return f22_obvd_109_obv_ema_cross_up_indicator(close, volume).diff().diff().diff()


def f22_obvd_110_obv_macd_hist_252d_d3(close, volume):
    return f22_obvd_110_obv_macd_hist_252d(close, volume).diff().diff().diff()


def f22_obvd_111_obv_ema_distance_zscore_252d_d3(close, volume):
    return f22_obvd_111_obv_ema_distance_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_112_obv_pct_change_21d_to_pct_change_252d_d3(close, volume):
    return f22_obvd_112_obv_pct_change_21d_to_pct_change_252d(close, volume).diff().diff().diff()


def f22_obvd_113_obv_slope_21d_minus_slope_63d_minus_slope_252d_d3(close, volume):
    return f22_obvd_113_obv_slope_21d_minus_slope_63d_minus_slope_252d(close, volume).diff().diff().diff()


def f22_obvd_114_obv_short_minus_long_zscore_252d_d3(close, volume):
    return f22_obvd_114_obv_short_minus_long_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_115_ratio_obv_to_obv_ema63_d3(close, volume):
    return f22_obvd_115_ratio_obv_to_obv_ema63(close, volume).diff().diff().diff()


def f22_obvd_116_obv_position_in_252d_range_d3(close, volume):
    return f22_obvd_116_obv_position_in_252d_range(close, volume).diff().diff().diff()


def f22_obvd_117_obv_position_in_504d_range_d3(close, volume):
    return f22_obvd_117_obv_position_in_504d_range(close, volume).diff().diff().diff()


def f22_obvd_118_obv_position_diff_short_minus_long_d3(close, volume):
    return f22_obvd_118_obv_position_diff_short_minus_long(close, volume).diff().diff().diff()


def f22_obvd_119_obv_minus_close_zscore_diff_252d_d3(close, volume):
    return f22_obvd_119_obv_minus_close_zscore_diff_252d(close, volume).diff().diff().diff()


def f22_obvd_120_obv_pct_rank_minus_close_pct_rank_252d_d3(close, volume):
    return f22_obvd_120_obv_pct_rank_minus_close_pct_rank_252d(close, volume).diff().diff().diff()


def f22_obvd_121_obv_below_zero_indicator_d3(close, volume):
    return f22_obvd_121_obv_below_zero_indicator(close, volume).diff().diff().diff()


def f22_obvd_122_obv_zero_cross_count_252d_d3(close, volume):
    return f22_obvd_122_obv_zero_cross_count_252d(close, volume).diff().diff().diff()


def f22_obvd_123_obv_bear_streak_below_max_d3(close, volume):
    return f22_obvd_123_obv_bear_streak_below_max(close, volume).diff().diff().diff()


def f22_obvd_124_obv_recent_local_max_count_63d_d3(close, volume):
    return f22_obvd_124_obv_recent_local_max_count_63d(close, volume).diff().diff().diff()


def f22_obvd_125_obv_velocity_acceleration_norm_252d_d3(close, volume):
    return f22_obvd_125_obv_velocity_acceleration_norm_252d(close, volume).diff().diff().diff()


def f22_obvd_126_obv_diff_skew_252d_d3(close, volume):
    return f22_obvd_126_obv_diff_skew_252d(close, volume).diff().diff().diff()


def f22_obvd_127_obv_diff_kurt_252d_d3(close, volume):
    return f22_obvd_127_obv_diff_kurt_252d(close, volume).diff().diff().diff()


def f22_obvd_128_obv_sign_imbalance_index_252d_d3(close, volume):
    return f22_obvd_128_obv_sign_imbalance_index_252d(close, volume).diff().diff().diff()


def f22_obvd_129_obv_underperformance_indicator_combined_d3(high, close, volume):
    return f22_obvd_129_obv_underperformance_indicator_combined(high, close, volume).diff().diff().diff()


def f22_obvd_130_obv_distribution_score_252d_d3(high, close, volume):
    return f22_obvd_130_obv_distribution_score_252d(high, close, volume).diff().diff().diff()


def f22_obvd_131_obv_pct_change_5d_minus_close_pct_change_5d_d3(close, volume):
    return f22_obvd_131_obv_pct_change_5d_minus_close_pct_change_5d(close, volume).diff().diff().diff()


def f22_obvd_132_obv_pct_change_21d_minus_close_pct_change_21d_d3(close, volume):
    return f22_obvd_132_obv_pct_change_21d_minus_close_pct_change_21d(close, volume).diff().diff().diff()


def f22_obvd_133_obv_higher_low_no_price_higher_low_indicator_d3(high, low, close, volume):
    return f22_obvd_133_obv_higher_low_no_price_higher_low_indicator(high, low, close, volume).diff().diff().diff()


def f22_obvd_134_obv_lower_high_no_price_lower_high_indicator_d3(high, close, volume):
    return f22_obvd_134_obv_lower_high_no_price_lower_high_indicator(high, close, volume).diff().diff().diff()


def f22_obvd_135_obv_divergence_persistence_252d_d3(high, close, volume):
    return f22_obvd_135_obv_divergence_persistence_252d(high, close, volume).diff().diff().diff()


def f22_obvd_136_obv_distance_from_252d_high_normalized_by_atr_d3(high, low, close, volume):
    return f22_obvd_136_obv_distance_from_252d_high_normalized_by_atr(high, low, close, volume).diff().diff().diff()


def f22_obvd_137_obv_zscore_at_high_price_decile_252d_d3(high, close, volume):
    return f22_obvd_137_obv_zscore_at_high_price_decile_252d(high, close, volume).diff().diff().diff()


def f22_obvd_138_obv_ratio_to_signed_vol_baseline_252d_d3(close, volume):
    return f22_obvd_138_obv_ratio_to_signed_vol_baseline_252d(close, volume).diff().diff().diff()


def f22_obvd_139_obv_drawdown_streak_consec_d3(close, volume):
    return f22_obvd_139_obv_drawdown_streak_consec(close, volume).diff().diff().diff()


def f22_obvd_140_obv_count_new_252d_lows_d3(close, volume):
    return f22_obvd_140_obv_count_new_252d_lows(close, volume).diff().diff().diff()


def f22_obvd_141_obv_kurt_252d_d3(close, volume):
    return f22_obvd_141_obv_kurt_252d(close, volume).diff().diff().diff()


def f22_obvd_142_obv_slope_r2_combined_252d_d3(close, volume):
    return f22_obvd_142_obv_slope_r2_combined_252d(close, volume).diff().diff().diff()


def f22_obvd_143_obv_first_diff_zero_count_252d_d3(close, volume):
    return f22_obvd_143_obv_first_diff_zero_count_252d(close, volume).diff().diff().diff()


def f22_obvd_144_obv_in_top_quartile_of_252d_range_indicator_d3(close, volume):
    return f22_obvd_144_obv_in_top_quartile_of_252d_range_indicator(close, volume).diff().diff().diff()


def f22_obvd_145_obv_in_bottom_quartile_of_252d_range_indicator_d3(close, volume):
    return f22_obvd_145_obv_in_bottom_quartile_of_252d_range_indicator(close, volume).diff().diff().diff()


def f22_obvd_146_obv_max_age_minus_obv_min_age_252d_d3(close, volume):
    return f22_obvd_146_obv_max_age_minus_obv_min_age_252d(close, volume).diff().diff().diff()


def f22_obvd_147_obv_persistence_index_252d_d3(close, volume):
    return f22_obvd_147_obv_persistence_index_252d(close, volume).diff().diff().diff()


def f22_obvd_148_obv_at_close_in_top_decile_252d_mean_d3(high, low, close, volume):
    return f22_obvd_148_obv_at_close_in_top_decile_252d_mean(high, low, close, volume).diff().diff().diff()


def f22_obvd_149_obv_runs_test_proxy_252d_d3(close, volume):
    return f22_obvd_149_obv_runs_test_proxy_252d(close, volume).diff().diff().diff()


def f22_obvd_150_composite_obv_health_score_252d_d3(high, close, volume):
    return f22_obvd_150_composite_obv_health_score_252d(high, close, volume).diff().diff().diff()


ON_BALANCE_VOLUME_DYNAMICS_D3_REGISTRY_076_150 = {
    "f22_obvd_076_up_volume_sum_21d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_076_up_volume_sum_21d_d3},
    "f22_obvd_077_down_volume_sum_21d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_077_down_volume_sum_21d_d3},
    "f22_obvd_078_up_to_down_volume_ratio_21d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_078_up_to_down_volume_ratio_21d_d3},
    "f22_obvd_079_up_to_down_volume_ratio_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_079_up_to_down_volume_ratio_63d_d3},
    "f22_obvd_080_net_volume_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_080_net_volume_zscore_252d_d3},
    "f22_obvd_081_cum_up_volume_to_total_volume_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_081_cum_up_volume_to_total_volume_252d_d3},
    "f22_obvd_082_cum_down_volume_to_total_volume_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_082_cum_down_volume_to_total_volume_252d_d3},
    "f22_obvd_083_obv_at_252hh_minus_obv_max_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_083_obv_at_252hh_minus_obv_max_252d_d3},
    "f22_obvd_084_obv_at_252hh_zscore_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_084_obv_at_252hh_zscore_252d_d3},
    "f22_obvd_085_bars_since_obv_at_252hh_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_085_bars_since_obv_at_252hh_d3},
    "f22_obvd_086_obv_delta_between_consecutive_252_highs_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_086_obv_delta_between_consecutive_252_highs_d3},
    "f22_obvd_087_obv_lower_at_higher_price_high_indicator_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_087_obv_lower_at_higher_price_high_indicator_d3},
    "f22_obvd_088_obv_at_hh_running_max_count_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_088_obv_at_hh_running_max_count_252d_d3},
    "f22_obvd_089_obv_oo_slope_63d_d3": {"inputs": ["open", "close", "volume"], "func": f22_obvd_089_obv_oo_slope_63d_d3},
    "f22_obvd_090_obv_oo_zscore_252d_d3": {"inputs": ["open", "close", "volume"], "func": f22_obvd_090_obv_oo_zscore_252d_d3},
    "f22_obvd_091_obv_minus_obv_oo_252d_d3": {"inputs": ["open", "close", "volume"], "func": f22_obvd_091_obv_minus_obv_oo_252d_d3},
    "f22_obvd_092_obv_oo_decay_ratio_252d_d3": {"inputs": ["open", "close", "volume"], "func": f22_obvd_092_obv_oo_decay_ratio_252d_d3},
    "f22_obvd_093_obv_oo_minus_price_slope_252d_d3": {"inputs": ["open", "close", "volume"], "func": f22_obvd_093_obv_oo_minus_price_slope_252d_d3},
    "f22_obvd_094_nvi_slope_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_094_nvi_slope_63d_d3},
    "f22_obvd_095_nvi_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_095_nvi_zscore_252d_d3},
    "f22_obvd_096_pvi_slope_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_096_pvi_slope_63d_d3},
    "f22_obvd_097_pvi_minus_nvi_slope_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_097_pvi_minus_nvi_slope_252d_d3},
    "f22_obvd_098_pvi_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_098_pvi_zscore_252d_d3},
    "f22_obvd_099_avg_vol_up_days_minus_down_days_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_099_avg_vol_up_days_minus_down_days_63d_d3},
    "f22_obvd_100_avg_vol_up_days_minus_down_days_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_100_avg_vol_up_days_minus_down_days_252d_d3},
    "f22_obvd_101_signed_vol_skew_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_101_signed_vol_skew_252d_d3},
    "f22_obvd_102_signed_vol_kurt_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_102_signed_vol_kurt_252d_d3},
    "f22_obvd_103_count_up_days_in_63d_d3": {"inputs": ["close"], "func": f22_obvd_103_count_up_days_in_63d_d3},
    "f22_obvd_104_frac_up_days_in_252d_d3": {"inputs": ["close"], "func": f22_obvd_104_frac_up_days_in_252d_d3},
    "f22_obvd_105_up_days_with_vol_above_med_minus_down_days_with_vol_above_med_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_105_up_days_with_vol_above_med_minus_down_days_with_vol_above_med_252d_d3},
    "f22_obvd_106_obv_ema21_slope_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_106_obv_ema21_slope_63d_d3},
    "f22_obvd_107_obv_ema21_slope_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_107_obv_ema21_slope_252d_d3},
    "f22_obvd_108_obv_ema_cross_down_indicator_d3": {"inputs": ["close", "volume"], "func": f22_obvd_108_obv_ema_cross_down_indicator_d3},
    "f22_obvd_109_obv_ema_cross_up_indicator_d3": {"inputs": ["close", "volume"], "func": f22_obvd_109_obv_ema_cross_up_indicator_d3},
    "f22_obvd_110_obv_macd_hist_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_110_obv_macd_hist_252d_d3},
    "f22_obvd_111_obv_ema_distance_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_111_obv_ema_distance_zscore_252d_d3},
    "f22_obvd_112_obv_pct_change_21d_to_pct_change_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_112_obv_pct_change_21d_to_pct_change_252d_d3},
    "f22_obvd_113_obv_slope_21d_minus_slope_63d_minus_slope_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_113_obv_slope_21d_minus_slope_63d_minus_slope_252d_d3},
    "f22_obvd_114_obv_short_minus_long_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_114_obv_short_minus_long_zscore_252d_d3},
    "f22_obvd_115_ratio_obv_to_obv_ema63_d3": {"inputs": ["close", "volume"], "func": f22_obvd_115_ratio_obv_to_obv_ema63_d3},
    "f22_obvd_116_obv_position_in_252d_range_d3": {"inputs": ["close", "volume"], "func": f22_obvd_116_obv_position_in_252d_range_d3},
    "f22_obvd_117_obv_position_in_504d_range_d3": {"inputs": ["close", "volume"], "func": f22_obvd_117_obv_position_in_504d_range_d3},
    "f22_obvd_118_obv_position_diff_short_minus_long_d3": {"inputs": ["close", "volume"], "func": f22_obvd_118_obv_position_diff_short_minus_long_d3},
    "f22_obvd_119_obv_minus_close_zscore_diff_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_119_obv_minus_close_zscore_diff_252d_d3},
    "f22_obvd_120_obv_pct_rank_minus_close_pct_rank_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_120_obv_pct_rank_minus_close_pct_rank_252d_d3},
    "f22_obvd_121_obv_below_zero_indicator_d3": {"inputs": ["close", "volume"], "func": f22_obvd_121_obv_below_zero_indicator_d3},
    "f22_obvd_122_obv_zero_cross_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_122_obv_zero_cross_count_252d_d3},
    "f22_obvd_123_obv_bear_streak_below_max_d3": {"inputs": ["close", "volume"], "func": f22_obvd_123_obv_bear_streak_below_max_d3},
    "f22_obvd_124_obv_recent_local_max_count_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_124_obv_recent_local_max_count_63d_d3},
    "f22_obvd_125_obv_velocity_acceleration_norm_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_125_obv_velocity_acceleration_norm_252d_d3},
    "f22_obvd_126_obv_diff_skew_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_126_obv_diff_skew_252d_d3},
    "f22_obvd_127_obv_diff_kurt_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_127_obv_diff_kurt_252d_d3},
    "f22_obvd_128_obv_sign_imbalance_index_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_128_obv_sign_imbalance_index_252d_d3},
    "f22_obvd_129_obv_underperformance_indicator_combined_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_129_obv_underperformance_indicator_combined_d3},
    "f22_obvd_130_obv_distribution_score_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_130_obv_distribution_score_252d_d3},
    "f22_obvd_131_obv_pct_change_5d_minus_close_pct_change_5d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_131_obv_pct_change_5d_minus_close_pct_change_5d_d3},
    "f22_obvd_132_obv_pct_change_21d_minus_close_pct_change_21d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_132_obv_pct_change_21d_minus_close_pct_change_21d_d3},
    "f22_obvd_133_obv_higher_low_no_price_higher_low_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_133_obv_higher_low_no_price_higher_low_indicator_d3},
    "f22_obvd_134_obv_lower_high_no_price_lower_high_indicator_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_134_obv_lower_high_no_price_lower_high_indicator_d3},
    "f22_obvd_135_obv_divergence_persistence_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_135_obv_divergence_persistence_252d_d3},
    "f22_obvd_136_obv_distance_from_252d_high_normalized_by_atr_d3": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_136_obv_distance_from_252d_high_normalized_by_atr_d3},
    "f22_obvd_137_obv_zscore_at_high_price_decile_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_137_obv_zscore_at_high_price_decile_252d_d3},
    "f22_obvd_138_obv_ratio_to_signed_vol_baseline_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_138_obv_ratio_to_signed_vol_baseline_252d_d3},
    "f22_obvd_139_obv_drawdown_streak_consec_d3": {"inputs": ["close", "volume"], "func": f22_obvd_139_obv_drawdown_streak_consec_d3},
    "f22_obvd_140_obv_count_new_252d_lows_d3": {"inputs": ["close", "volume"], "func": f22_obvd_140_obv_count_new_252d_lows_d3},
    "f22_obvd_141_obv_kurt_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_141_obv_kurt_252d_d3},
    "f22_obvd_142_obv_slope_r2_combined_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_142_obv_slope_r2_combined_252d_d3},
    "f22_obvd_143_obv_first_diff_zero_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_143_obv_first_diff_zero_count_252d_d3},
    "f22_obvd_144_obv_in_top_quartile_of_252d_range_indicator_d3": {"inputs": ["close", "volume"], "func": f22_obvd_144_obv_in_top_quartile_of_252d_range_indicator_d3},
    "f22_obvd_145_obv_in_bottom_quartile_of_252d_range_indicator_d3": {"inputs": ["close", "volume"], "func": f22_obvd_145_obv_in_bottom_quartile_of_252d_range_indicator_d3},
    "f22_obvd_146_obv_max_age_minus_obv_min_age_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_146_obv_max_age_minus_obv_min_age_252d_d3},
    "f22_obvd_147_obv_persistence_index_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_147_obv_persistence_index_252d_d3},
    "f22_obvd_148_obv_at_close_in_top_decile_252d_mean_d3": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_148_obv_at_close_in_top_decile_252d_mean_d3},
    "f22_obvd_149_obv_runs_test_proxy_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_149_obv_runs_test_proxy_252d_d3},
    "f22_obvd_150_composite_obv_health_score_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_150_composite_obv_health_score_252d_d3},
}
