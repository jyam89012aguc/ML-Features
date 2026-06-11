"""atr_extension_signature d3 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Theme:
ATR-normalized "extension" — distance of price from a reference (MA / VWAP /
anchor / rolling high/low) expressed in units of ATR. Distinct from family 40
(atr_expansion_dynamics, raw ATR ratios) by always denominating a price-distance
in ATR units. Distinct from family 11 (sma_ema_extension) by being purely
ATR-normalized rather than log-normalized.

Bucket A: Extension from SMA references (close/high vs SMA_n) / ATR.
Bucket B: Extension from EMA / DEMA references / ATR.
Bucket C: Extension from rolling VWAP-anchored references / ATR.
Bucket D: Extension from rolling highs / ATR.
Bucket E: Extension from rolling lows / ATR (extension *above* a low).
Bucket F: Extension z-scores.
Bucket G: Extension percentile ranks.
Bucket H: Extension-extreme / above-threshold states & recency.
Bucket I: ATR-normalized return / momentum extensions.

Inputs: SEP OHLCV. Self-contained helpers; PIT-clean (right-anchored rolling,
explicit min_periods, no centered windows, no .shift(N)).
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


def _bars_since_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _dema(s, n):
    e = _ema(s, n)
    return 2.0 * e - _ema(e, n)


def _rolling_vwap(close, volume, n):
    """Rolling VWAP over past n bars = sum(close*vol) / sum(vol)."""
    num = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    den = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _anchored_vwap_from_rolling_low(close, volume, n):
    """Anchored VWAP from the lowest-low bar within trailing n bars.
    For each bar t: find the bar k* in [t-n+1, t] where price was lowest,
    then VWAP = sum_{i=k*..t}(close_i*vol_i) / sum_{i=k*..t}(vol_i).
    PIT-clean.
    """
    pv = close * volume
    out = pd.Series(np.nan, index=close.index)
    close_arr = close.to_numpy()
    vol_arr = volume.to_numpy()
    pv_arr = pv.to_numpy()
    for t in range(close_arr.size):
        lo = max(0, t - n + 1)
        # find lowest-low index in window
        w = close_arr[lo : t + 1]
        if np.all(np.isnan(w)) or w.size == 0:
            continue
        # ignore NaN in argmin
        if np.isnan(w).all():
            continue
        # use nanargmin
        rel = int(np.nanargmin(w))
        k = lo + rel
        sum_pv = np.nansum(pv_arr[k : t + 1])
        sum_v = np.nansum(vol_arr[k : t + 1])
        if sum_v == 0:
            continue
        out.iloc[t] = sum_pv / sum_v
    return out


# ============================================================
# Bucket A — Extension from SMA references (001-010)
# ============================================================


def f47_atxs_001_close_minus_sma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - SMA21) / ATR21 — short-horizon ATR-normalized extension."""
    return (_safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_002_close_minus_sma50_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - SMA50) / ATR21 — extension from 50-day MA in ATR units."""
    return (_safe_div(close - _sma(close, 50), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_003_close_minus_sma63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - SMA63) / ATR21 — quarterly MA extension."""
    return (_safe_div(close - _sma(close, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_004_close_minus_sma100_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - SMA100) / ATR21."""
    return (_safe_div(close - _sma(close, 100), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_005_close_minus_sma200_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - SMA200) / ATR21 — classic 200-day MA extension in ATR units."""
    return (_safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_006_close_minus_sma252_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - SMA252) / ATR21 — annual MA extension."""
    return (_safe_div(close - _sma(close, YDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_007_close_minus_sma504_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - SMA504) / ATR21 — multi-year MA extension."""
    return (_safe_div(close - _sma(close, DDAYS_2Y), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_008_high_minus_sma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - SMA21) / ATR21 — intra-bar extension above monthly MA."""
    return (_safe_div(high - _sma(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_009_high_minus_sma63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - SMA63) / ATR21 — intra-bar extension above quarterly MA."""
    return (_safe_div(high - _sma(close, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_010_high_minus_sma252_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - SMA252) / ATR21 — intra-bar extension above annual MA."""
    return (_safe_div(high - _sma(close, YDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_011_close_minus_ema21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - EMA21) / ATR21 — extension from monthly EMA."""
    return (_safe_div(close - _ema(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_012_close_minus_ema50_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - EMA50) / ATR21."""
    return (_safe_div(close - _ema(close, 50), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_013_close_minus_ema63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - EMA63) / ATR21 — extension from quarterly EMA."""
    return (_safe_div(close - _ema(close, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_014_close_minus_ema200_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - EMA200) / ATR21 — extension from 200-day EMA in ATR units."""
    return (_safe_div(close - _ema(close, 200), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_015_close_minus_ema21_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - EMA21) / ATR63 — cross-horizon: short EMA, quarterly ATR."""
    return (_safe_div(close - _ema(close, MDAYS), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_016_close_minus_ema63_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - EMA63) / ATR63 — same-horizon EMA & ATR."""
    return (_safe_div(close - _ema(close, QDAYS), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_017_close_minus_ema200_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - EMA200) / ATR252 — long-horizon extension."""
    return (_safe_div(close - _ema(close, 200), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_018_close_minus_dema63_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - DEMA63) / ATR63 — extension from double-EMA reference."""
    return (_safe_div(close - _dema(close, QDAYS), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_019_close_minus_vwap21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - rolling-VWAP21) / ATR21 — monthly VWAP extension."""
    return (_safe_div(close - _rolling_vwap(close, volume, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_020_close_minus_vwap63_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - rolling-VWAP63) / ATR63 — quarterly VWAP extension."""
    return (_safe_div(close - _rolling_vwap(close, volume, QDAYS), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_021_close_minus_vwap252_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - rolling-VWAP252) / ATR252 — annual VWAP extension."""
    return (_safe_div(close - _rolling_vwap(close, volume, YDAYS), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_022_close_minus_aVWAP_from_252d_low_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - anchored-VWAP-from-252d-low) / ATR21 — extension above swing-low anchored VWAP."""
    return (_safe_div(close - _anchored_vwap_from_rolling_low(close, volume, YDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_023_close_minus_aVWAP_from_252d_low_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - aVWAP-from-252d-low) / ATR252 — long-horizon swing-anchored extension."""
    return (_safe_div(close - _anchored_vwap_from_rolling_low(close, volume, YDAYS), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_024_close_minus_vwap21_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWAP21) / ATR63 — short VWAP vs quarterly ATR (cross-horizon)."""
    return (_safe_div(close - _rolling_vwap(close, volume, MDAYS), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_025_close_minus_vwap63_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWAP63) / ATR252 — quarterly VWAP vs annual ATR."""
    return (_safe_div(close - _rolling_vwap(close, volume, QDAYS), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_026_high_minus_vwap21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(high - VWAP21) / ATR21 — intra-bar extension above monthly VWAP."""
    return (_safe_div(high - _rolling_vwap(close, volume, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_027_close_minus_21d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 21d high) / ATR21 — gap below recent high in ATR units (zero or negative)."""
    return (_safe_div(close - high.rolling(MDAYS, min_periods=WDAYS).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_028_close_minus_63d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 63d high) / ATR21 — quarterly-high gap in ATR21."""
    return (_safe_div(close - high.rolling(QDAYS, min_periods=MDAYS).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_029_close_minus_63d_high_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 63d high) / ATR63 — same-horizon gap in quarterly ATR."""
    return (_safe_div(close - high.rolling(QDAYS, min_periods=MDAYS).max(), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_030_close_minus_252d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d high) / ATR21 — annual-high gap, monthly ATR."""
    return (_safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_031_close_minus_252d_high_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d high) / ATR63 — annual-high gap, quarterly ATR."""
    return (_safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_032_close_minus_252d_high_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d high) / ATR252 — annual-high gap, annual ATR."""
    return (_safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_033_close_minus_504d_high_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 504d high) / ATR252 — multi-year-high gap in annual ATR."""
    return (_safe_div(close - high.rolling(DDAYS_2Y, min_periods=YDAYS).max(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_034_high_minus_252d_high_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - 252d high) / ATR252 — intra-bar overshoot of annual high in ATR units (0 if not at high)."""
    return (_safe_div(high - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_035_close_minus_21d_low_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 21d low) / ATR21 — extension above monthly low."""
    return (_safe_div(close - low.rolling(MDAYS, min_periods=WDAYS).min(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_036_close_minus_63d_low_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 63d low) / ATR21 — extension above quarterly low."""
    return (_safe_div(close - low.rolling(QDAYS, min_periods=MDAYS).min(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_037_close_minus_252d_low_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d low) / ATR21 — extension above annual low."""
    return (_safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_038_close_minus_252d_low_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d low) / ATR252 — annual-low extension in annual ATR."""
    return (_safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_039_close_minus_504d_low_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 504d low) / ATR252 — multi-year-low extension."""
    return (_safe_div(close - low.rolling(DDAYS_2Y, min_periods=YDAYS).min(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_040_close_minus_252d_low_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d low) / ATR63 — cross-horizon extension above annual low."""
    return (_safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_041_high_minus_252d_low_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - 252d low) / ATR252 — total extension from annual low to today's high."""
    return (_safe_div(high - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_042_low_minus_252d_low_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(low - 252d low) / ATR252 — today's low vs annual low in ATR units."""
    return (_safe_div(low - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_043_zscore_252_close_minus_sma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of (close - SMA21) / ATR21 — relative monthly extension percentile."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (_rolling_zscore(e, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f47_atxs_044_zscore_252_close_minus_sma63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of (close - SMA63) / ATR21."""
    e = _safe_div(close - _sma(close, QDAYS), _atr(high, low, close, MDAYS))
    return (_rolling_zscore(e, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f47_atxs_045_zscore_252_close_minus_sma252_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of (close - SMA252) / ATR21."""
    e = _safe_div(close - _sma(close, YDAYS), _atr(high, low, close, MDAYS))
    return (_rolling_zscore(e, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f47_atxs_046_zscore_252_close_minus_vwap63_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (252d) of (close - VWAP63) / ATR63."""
    e = _safe_div(close - _rolling_vwap(close, volume, QDAYS), _atr(high, low, close, QDAYS))
    return (_rolling_zscore(e, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f47_atxs_047_zscore_252_close_minus_21d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of (close - 21d high) / ATR21."""
    e = _safe_div(close - high.rolling(MDAYS, min_periods=WDAYS).max(), _atr(high, low, close, MDAYS))
    return (_rolling_zscore(e, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f47_atxs_048_zscore_252_close_minus_252d_high_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of (close - 252d high) / ATR63."""
    e = _safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, QDAYS))
    return (_rolling_zscore(e, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f47_atxs_049_zscore_504_close_minus_sma200_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (504d) of (close - SMA200) / ATR21."""
    e = _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))
    return (_rolling_zscore(e, DDAYS_2Y, min_periods=YDAYS)).diff().diff().diff()


def f47_atxs_050_zscore_504_close_minus_252d_high_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (504d) of (close - 252d high) / ATR63."""
    e = _safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, QDAYS))
    return (_rolling_zscore(e, DDAYS_2Y, min_periods=YDAYS)).diff().diff().diff()


def f47_atxs_051_pctrank_252_close_minus_sma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank (252d) of (close - SMA21) / ATR21."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f47_atxs_052_pctrank_252_close_minus_sma252_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank (252d) of (close - SMA252) / ATR21."""
    e = _safe_div(close - _sma(close, YDAYS), _atr(high, low, close, MDAYS))
    return (e.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f47_atxs_053_pctrank_252_close_minus_21d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank (252d) of (close - 21d high) / ATR21."""
    e = _safe_div(close - high.rolling(MDAYS, min_periods=WDAYS).max(), _atr(high, low, close, MDAYS))
    return (e.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f47_atxs_054_pctrank_252_close_minus_252d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank (252d) of (close - 252d high) / ATR21."""
    e = _safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, MDAYS))
    return (e.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f47_atxs_055_pctrank_504_close_minus_252d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank (504d) of (close - 252d high) / ATR21."""
    e = _safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, MDAYS))
    return (e.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)).diff().diff().diff()


def f47_atxs_056_pctrank_504_close_minus_sma200_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank (504d) of (close - SMA200) / ATR21."""
    e = _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))
    return (e.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)).diff().diff().diff()


def f47_atxs_057_pctrank_252_high_minus_sma200_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank (252d) of (high - SMA200) / ATR21 — intra-bar extension percentile."""
    e = _safe_div(high - _sma(close, 200), _atr(high, low, close, MDAYS))
    return (e.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f47_atxs_058_pctrank_252_close_minus_vwap63_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct-rank (252d) of (close - VWAP63) / ATR63."""
    e = _safe_div(close - _rolling_vwap(close, volume, QDAYS), _atr(high, low, close, QDAYS))
    return (e.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()


def f47_atxs_059_close_sma21_atr21_above_2_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close - SMA21)/ATR21 > 2 — overextension state."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return ((e > 2.0).astype(float).where(e.notna(), np.nan)).diff().diff().diff()


def f47_atxs_060_close_sma21_atr21_above_3_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close - SMA21)/ATR21 > 3 — strong overextension state."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return ((e > 3.0).astype(float).where(e.notna(), np.nan)).diff().diff().diff()


def f47_atxs_061_close_sma63_atr21_above_3_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close - SMA63)/ATR21 > 3 — quarterly overextension."""
    e = _safe_div(close - _sma(close, QDAYS), _atr(high, low, close, MDAYS))
    return ((e > 3.0).astype(float).where(e.notna(), np.nan)).diff().diff().diff()


def f47_atxs_062_close_sma252_atr21_above_5_extreme_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close - SMA252)/ATR21 > 5 — extreme annual overextension."""
    e = _safe_div(close - _sma(close, YDAYS), _atr(high, low, close, MDAYS))
    return ((e > 5.0).astype(float).where(e.notna(), np.nan)).diff().diff().diff()


def f47_atxs_063_close_252d_high_atr21_above_0_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close - 252d high)/ATR21 > 0 — current at new high above prior 252d high."""
    e = _safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, MDAYS))
    return ((e > 0.0).astype(float).where(e.notna(), np.nan)).diff().diff().diff()


def f47_atxs_064_close_sma200_atr21_above_4_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close - SMA200)/ATR21 > 4 — far above 200-day MA."""
    e = _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))
    return ((e > 4.0).astype(float).where(e.notna(), np.nan)).diff().diff().diff()


def f47_atxs_065_bars_since_close_sma21_atr21_above_2_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent (close-SMA21)/ATR21 > 2 event — recency of overextension."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (_bars_since_true(e > 2.0)).diff().diff().diff()


def f47_atxs_066_count_close_sma21_atr21_above_2_in_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (close-SMA21)/ATR21 > 2 events past 63 bars."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return ((e > 2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)).diff().diff().diff()


def f47_atxs_067_ret21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - close[t-21]) / ATR21 — 21-bar move in ATR units."""
    return (_safe_div(close - close.shift(MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_068_ret63_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - close[t-63]) / ATR63 — 63-bar move in ATR units."""
    return (_safe_div(close - close.shift(QDAYS), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_069_ret252_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - close[t-252]) / ATR252 — 252-bar move in ATR units."""
    return (_safe_div(close - close.shift(YDAYS), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_070_ret504_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - close[t-504]) / ATR252 — multi-year move in annual ATR."""
    return (_safe_div(close - close.shift(DDAYS_2Y), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_071_ret21_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - close[t-21]) / ATR63 — short move in quarterly ATR (cross-horizon)."""
    return (_safe_div(close - close.shift(MDAYS), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_072_ret63_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - close[t-63]) / ATR252 — quarterly move in annual ATR."""
    return (_safe_div(close - close.shift(QDAYS), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_073_log_ret21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(close/close[t-21]) / ATR21 — log-return normalized by ATR (price-scale-free)."""
    return (_safe_div(_safe_log(close) - _safe_log(close.shift(MDAYS)), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_074_log_ret63_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(close/close[t-63]) / ATR63 — quarterly log-return in ATR units."""
    return (_safe_div(_safe_log(close) - _safe_log(close.shift(QDAYS)), _atr(high, low, close, QDAYS))).diff().diff().diff()


def f47_atxs_075_log_ret252_over_atr63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(close/close[t-252]) / ATR63 — annual log-return in quarterly ATR."""
    return (_safe_div(_safe_log(close) - _safe_log(close.shift(YDAYS)), _atr(high, low, close, QDAYS))).diff().diff().diff()


# ============================================================
#                         REGISTRY 001-075 (d3)
# ============================================================

_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]

ATR_EXTENSION_SIGNATURE_D3_REGISTRY_001_075 = {
    "f47_atxs_001_close_minus_sma21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_001_close_minus_sma21_over_atr21_d3},
    "f47_atxs_002_close_minus_sma50_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_002_close_minus_sma50_over_atr21_d3},
    "f47_atxs_003_close_minus_sma63_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_003_close_minus_sma63_over_atr21_d3},
    "f47_atxs_004_close_minus_sma100_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_004_close_minus_sma100_over_atr21_d3},
    "f47_atxs_005_close_minus_sma200_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_005_close_minus_sma200_over_atr21_d3},
    "f47_atxs_006_close_minus_sma252_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_006_close_minus_sma252_over_atr21_d3},
    "f47_atxs_007_close_minus_sma504_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_007_close_minus_sma504_over_atr21_d3},
    "f47_atxs_008_high_minus_sma21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_008_high_minus_sma21_over_atr21_d3},
    "f47_atxs_009_high_minus_sma63_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_009_high_minus_sma63_over_atr21_d3},
    "f47_atxs_010_high_minus_sma252_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_010_high_minus_sma252_over_atr21_d3},
    "f47_atxs_011_close_minus_ema21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_011_close_minus_ema21_over_atr21_d3},
    "f47_atxs_012_close_minus_ema50_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_012_close_minus_ema50_over_atr21_d3},
    "f47_atxs_013_close_minus_ema63_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_013_close_minus_ema63_over_atr21_d3},
    "f47_atxs_014_close_minus_ema200_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_014_close_minus_ema200_over_atr21_d3},
    "f47_atxs_015_close_minus_ema21_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_015_close_minus_ema21_over_atr63_d3},
    "f47_atxs_016_close_minus_ema63_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_016_close_minus_ema63_over_atr63_d3},
    "f47_atxs_017_close_minus_ema200_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_017_close_minus_ema200_over_atr252_d3},
    "f47_atxs_018_close_minus_dema63_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_018_close_minus_dema63_over_atr63_d3},
    "f47_atxs_019_close_minus_vwap21_over_atr21_d3": {"inputs": _HLCV, "func": f47_atxs_019_close_minus_vwap21_over_atr21_d3},
    "f47_atxs_020_close_minus_vwap63_over_atr63_d3": {"inputs": _HLCV, "func": f47_atxs_020_close_minus_vwap63_over_atr63_d3},
    "f47_atxs_021_close_minus_vwap252_over_atr252_d3": {"inputs": _HLCV, "func": f47_atxs_021_close_minus_vwap252_over_atr252_d3},
    "f47_atxs_022_close_minus_aVWAP_from_252d_low_over_atr21_d3": {"inputs": _HLCV, "func": f47_atxs_022_close_minus_aVWAP_from_252d_low_over_atr21_d3},
    "f47_atxs_023_close_minus_aVWAP_from_252d_low_over_atr252_d3": {"inputs": _HLCV, "func": f47_atxs_023_close_minus_aVWAP_from_252d_low_over_atr252_d3},
    "f47_atxs_024_close_minus_vwap21_over_atr63_d3": {"inputs": _HLCV, "func": f47_atxs_024_close_minus_vwap21_over_atr63_d3},
    "f47_atxs_025_close_minus_vwap63_over_atr252_d3": {"inputs": _HLCV, "func": f47_atxs_025_close_minus_vwap63_over_atr252_d3},
    "f47_atxs_026_high_minus_vwap21_over_atr21_d3": {"inputs": _HLCV, "func": f47_atxs_026_high_minus_vwap21_over_atr21_d3},
    "f47_atxs_027_close_minus_21d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_027_close_minus_21d_high_over_atr21_d3},
    "f47_atxs_028_close_minus_63d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_028_close_minus_63d_high_over_atr21_d3},
    "f47_atxs_029_close_minus_63d_high_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_029_close_minus_63d_high_over_atr63_d3},
    "f47_atxs_030_close_minus_252d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_030_close_minus_252d_high_over_atr21_d3},
    "f47_atxs_031_close_minus_252d_high_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_031_close_minus_252d_high_over_atr63_d3},
    "f47_atxs_032_close_minus_252d_high_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_032_close_minus_252d_high_over_atr252_d3},
    "f47_atxs_033_close_minus_504d_high_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_033_close_minus_504d_high_over_atr252_d3},
    "f47_atxs_034_high_minus_252d_high_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_034_high_minus_252d_high_over_atr252_d3},
    "f47_atxs_035_close_minus_21d_low_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_035_close_minus_21d_low_over_atr21_d3},
    "f47_atxs_036_close_minus_63d_low_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_036_close_minus_63d_low_over_atr21_d3},
    "f47_atxs_037_close_minus_252d_low_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_037_close_minus_252d_low_over_atr21_d3},
    "f47_atxs_038_close_minus_252d_low_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_038_close_minus_252d_low_over_atr252_d3},
    "f47_atxs_039_close_minus_504d_low_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_039_close_minus_504d_low_over_atr252_d3},
    "f47_atxs_040_close_minus_252d_low_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_040_close_minus_252d_low_over_atr63_d3},
    "f47_atxs_041_high_minus_252d_low_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_041_high_minus_252d_low_over_atr252_d3},
    "f47_atxs_042_low_minus_252d_low_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_042_low_minus_252d_low_over_atr252_d3},
    "f47_atxs_043_zscore_252_close_minus_sma21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_043_zscore_252_close_minus_sma21_over_atr21_d3},
    "f47_atxs_044_zscore_252_close_minus_sma63_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_044_zscore_252_close_minus_sma63_over_atr21_d3},
    "f47_atxs_045_zscore_252_close_minus_sma252_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_045_zscore_252_close_minus_sma252_over_atr21_d3},
    "f47_atxs_046_zscore_252_close_minus_vwap63_over_atr63_d3": {"inputs": _HLCV, "func": f47_atxs_046_zscore_252_close_minus_vwap63_over_atr63_d3},
    "f47_atxs_047_zscore_252_close_minus_21d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_047_zscore_252_close_minus_21d_high_over_atr21_d3},
    "f47_atxs_048_zscore_252_close_minus_252d_high_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_048_zscore_252_close_minus_252d_high_over_atr63_d3},
    "f47_atxs_049_zscore_504_close_minus_sma200_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_049_zscore_504_close_minus_sma200_over_atr21_d3},
    "f47_atxs_050_zscore_504_close_minus_252d_high_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_050_zscore_504_close_minus_252d_high_over_atr63_d3},
    "f47_atxs_051_pctrank_252_close_minus_sma21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_051_pctrank_252_close_minus_sma21_over_atr21_d3},
    "f47_atxs_052_pctrank_252_close_minus_sma252_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_052_pctrank_252_close_minus_sma252_over_atr21_d3},
    "f47_atxs_053_pctrank_252_close_minus_21d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_053_pctrank_252_close_minus_21d_high_over_atr21_d3},
    "f47_atxs_054_pctrank_252_close_minus_252d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_054_pctrank_252_close_minus_252d_high_over_atr21_d3},
    "f47_atxs_055_pctrank_504_close_minus_252d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_055_pctrank_504_close_minus_252d_high_over_atr21_d3},
    "f47_atxs_056_pctrank_504_close_minus_sma200_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_056_pctrank_504_close_minus_sma200_over_atr21_d3},
    "f47_atxs_057_pctrank_252_high_minus_sma200_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_057_pctrank_252_high_minus_sma200_over_atr21_d3},
    "f47_atxs_058_pctrank_252_close_minus_vwap63_over_atr63_d3": {"inputs": _HLCV, "func": f47_atxs_058_pctrank_252_close_minus_vwap63_over_atr63_d3},
    "f47_atxs_059_close_sma21_atr21_above_2_state_d3": {"inputs": _HLC, "func": f47_atxs_059_close_sma21_atr21_above_2_state_d3},
    "f47_atxs_060_close_sma21_atr21_above_3_state_d3": {"inputs": _HLC, "func": f47_atxs_060_close_sma21_atr21_above_3_state_d3},
    "f47_atxs_061_close_sma63_atr21_above_3_state_d3": {"inputs": _HLC, "func": f47_atxs_061_close_sma63_atr21_above_3_state_d3},
    "f47_atxs_062_close_sma252_atr21_above_5_extreme_d3": {"inputs": _HLC, "func": f47_atxs_062_close_sma252_atr21_above_5_extreme_d3},
    "f47_atxs_063_close_252d_high_atr21_above_0_state_d3": {"inputs": _HLC, "func": f47_atxs_063_close_252d_high_atr21_above_0_state_d3},
    "f47_atxs_064_close_sma200_atr21_above_4_state_d3": {"inputs": _HLC, "func": f47_atxs_064_close_sma200_atr21_above_4_state_d3},
    "f47_atxs_065_bars_since_close_sma21_atr21_above_2_d3": {"inputs": _HLC, "func": f47_atxs_065_bars_since_close_sma21_atr21_above_2_d3},
    "f47_atxs_066_count_close_sma21_atr21_above_2_in_63_d3": {"inputs": _HLC, "func": f47_atxs_066_count_close_sma21_atr21_above_2_in_63_d3},
    "f47_atxs_067_ret21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_067_ret21_over_atr21_d3},
    "f47_atxs_068_ret63_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_068_ret63_over_atr63_d3},
    "f47_atxs_069_ret252_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_069_ret252_over_atr252_d3},
    "f47_atxs_070_ret504_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_070_ret504_over_atr252_d3},
    "f47_atxs_071_ret21_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_071_ret21_over_atr63_d3},
    "f47_atxs_072_ret63_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_072_ret63_over_atr252_d3},
    "f47_atxs_073_log_ret21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_073_log_ret21_over_atr21_d3},
    "f47_atxs_074_log_ret63_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_074_log_ret63_over_atr63_d3},
    "f47_atxs_075_log_ret252_over_atr63_d3": {"inputs": _HLC, "func": f47_atxs_075_log_ret252_over_atr63_d3},
}
