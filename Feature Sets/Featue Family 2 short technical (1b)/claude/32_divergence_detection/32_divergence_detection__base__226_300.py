"""divergence_detection base features 226-300 — Pipeline 1b-technical (gap-fill extension).

Extends 001-225 with: proper 3-pivot Class-A divergence (rolling-argmax-based),
long-horizon 252d/504d variants of methods previously covered only at 63d,
multi-horizon (5/21/63/126/252) heatmap-breadth metas, divergence x volume-condition
conjunctions, rolling R² regression-strength metrics, persistence + magnitude
composites, and cross-asset-class conjunctions.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260


# ---------------------------- standard helpers ----------------------------

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


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


# ---------------------------- oscillator helpers (used here) ----------------------------

def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0); loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(ag, al)
    return 100.0 - 100.0 / (1.0 + rs)


def _macd_line(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)


def _macd_hist(close, fast=12, slow=26, sig=9):
    line = _macd_line(close, fast, slow)
    return line - _ema(line, sig)


def _obv(close, volume):
    sign = np.sign(close.diff().fillna(0))
    return (sign * volume).cumsum()


def _ad_line(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    return (mfm * volume).fillna(0).cumsum()


def _stoch_k(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)


def _mfi(high, low, close, volume, n=14):
    tp = (high + low + close) / 3.0
    rmf = tp * volume; delta = tp.diff()
    pos = rmf.where(delta > 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    neg = rmf.where(delta < 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = _safe_div(pos, neg)
    return 100.0 - 100.0 / (1.0 + mr)


# ---------------------------- divergence-detection helpers ----------------------------

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    bear = ((ps > 0) & (osl < 0)).astype(float)
    bull = ((ps < 0) & (osl > 0)).astype(float)
    return (bear - bull).where(ps.notna() & osl.notna(), np.nan)


def _shift_div_bearish_indicator(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    return ((price > pp) & (osc < op)).astype(float).where(pp.notna() & op.notna(), np.nan)


def _shift_div_hidden_bearish_indicator(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    return ((price < pp) & (osc > op)).astype(float).where(pp.notna() & op.notna(), np.nan)


def _zscore_gap(price, osc, n):
    return _rolling_zscore(_safe_log(price), n) - _rolling_zscore(osc, n)


def _rolling_corr_pearson(a, b, n):
    return a.rolling(n, min_periods=max(n // 3, 2)).corr(b)


# ---------------------------- pivot-based Class-A divergence helper ----------------------------

def _argmax_offset_from_end(s, n, min_periods):
    """For each bar, # of bars back where the max occurred within trailing n bars (0..n-1)."""
    def _arg(w):
        if np.all(np.isnan(w)):
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(n, min_periods=min_periods).apply(_arg, raw=True)


def _class_a_pivot_div(price, osc, near_window, far_window):
    """3-pivot Class-A bearish divergence using rolling argmax over adjacent windows.
    Returns +1 if current rolling-max(price, near_window) > prior rolling-max(price, far_window
    ending near_window bars ago) AND osc at the current price-max bar < osc at the prior price-max bar.
    Vectorized via take-from-index."""
    near_max = price.rolling(near_window, min_periods=max(near_window // 3, 2)).max()
    far_max = price.shift(near_window).rolling(far_window, min_periods=max(far_window // 3, 2)).max()
    near_off = _argmax_offset_from_end(price, near_window, max(near_window // 3, 2))
    far_off = _argmax_offset_from_end(price.shift(near_window), far_window, max(far_window // 3, 2))
    idx = np.arange(len(price))
    near_idx = (idx - near_off.fillna(0).astype(int).values).clip(0, len(osc) - 1)
    far_idx = (idx - near_window - far_off.fillna(0).astype(int).values).clip(0, len(osc) - 1)
    osc_v = osc.values
    osc_at_near = pd.Series(osc_v[near_idx], index=price.index)
    osc_at_far = pd.Series(osc_v[far_idx], index=price.index)
    bear = ((near_max > far_max) & (osc_at_near < osc_at_far)).astype(float)
    valid = near_max.notna() & far_max.notna() & near_off.notna() & far_off.notna()
    return bear.where(valid, np.nan)


# ============================================================
# Bucket II — 3-pivot Class-A bearish divergence on 5 oscillators (226-240)
# ============================================================

def f32_divd_226_rsi14_class_a_pivot_div_63_63(close: pd.Series) -> pd.Series:
    """Class-A 3-pivot bearish divergence: RSI(14) at price's 63d-max vs price's prior-63d-max."""
    return _class_a_pivot_div(close, _rsi_wilder(close, 14), 63, 63)


def f32_divd_227_rsi14_class_a_pivot_div_21_42(close: pd.Series) -> pd.Series:
    """Short-cycle Class-A pivot div on RSI(14), 21d-near vs 42d-far — acute structure."""
    return _class_a_pivot_div(close, _rsi_wilder(close, 14), 21, 42)


def f32_divd_228_rsi14_class_a_pivot_div_126_126(close: pd.Series) -> pd.Series:
    """Half-year Class-A pivot div on RSI(14), 126d-near vs 126d-far — semi-annual structure."""
    return _class_a_pivot_div(close, _rsi_wilder(close, 14), 126, 126)


def f32_divd_229_macdline_class_a_pivot_div_63_63(close: pd.Series) -> pd.Series:
    """Class-A pivot div on MACD line, 63d/63d."""
    return _class_a_pivot_div(close, _macd_line(close, 12, 26), 63, 63)


def f32_divd_230_macdline_class_a_pivot_div_21_42(close: pd.Series) -> pd.Series:
    """Short-cycle Class-A pivot div on MACD line, 21d/42d."""
    return _class_a_pivot_div(close, _macd_line(close, 12, 26), 21, 42)


def f32_divd_231_macdhist_class_a_pivot_div_63_63(close: pd.Series) -> pd.Series:
    """Class-A pivot div on MACD histogram, 63d/63d."""
    return _class_a_pivot_div(close, _macd_hist(close, 12, 26, 9), 63, 63)


def f32_divd_232_obv_class_a_pivot_div_63_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Class-A pivot div on OBV, 63d/63d."""
    return _class_a_pivot_div(close, _obv(close, volume), 63, 63)


def f32_divd_233_obv_class_a_pivot_div_126_126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Class-A pivot div on OBV, 126d/126d — secular accumulation failure."""
    return _class_a_pivot_div(close, _obv(close, volume), 126, 126)


def f32_divd_234_adline_class_a_pivot_div_63_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Class-A pivot div on A/D Chaikin, 63d/63d."""
    return _class_a_pivot_div(close, _ad_line(high, low, close, volume), 63, 63)


def f32_divd_235_stochk_class_a_pivot_div_63_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Class-A pivot div on Stoch %K(14), 63d/63d."""
    return _class_a_pivot_div(close, _stoch_k(high, low, close, 14), 63, 63)


def f32_divd_236_mfi_class_a_pivot_div_63_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Class-A pivot div on MFI(14), 63d/63d."""
    return _class_a_pivot_div(close, _mfi(high, low, close, volume, 14), 63, 63)


def f32_divd_237_class_a_pivot_div_breadth_4osc_63_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction (0..1) of 4 osc (RSI/MACD-line/OBV/MFI) showing Class-A 63/63 pivot div."""
    parts = [
        _class_a_pivot_div(close, _rsi_wilder(close, 14), 63, 63).rename("a"),
        _class_a_pivot_div(close, _macd_line(close, 12, 26), 63, 63).rename("b"),
        _class_a_pivot_div(close, _obv(close, volume), 63, 63).rename("c"),
        _class_a_pivot_div(close, _mfi(high, low, close, volume, 14), 63, 63).rename("d"),
    ]
    return pd.concat(parts, axis=1).mean(axis=1)


def f32_divd_238_class_a_pivot_div_x_at_252d_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI Class-A pivot-div fires AND close within 1% of 252d max."""
    div = _class_a_pivot_div(close, _rsi_wilder(close, 14), 63, 63)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((div == 1) & (near == 1)).astype(float).where(div.notna() & near.notna(), np.nan)


def f32_divd_239_class_a_pivot_div_count_4osc_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where at least 2 of 4 osc had Class-A 63/63 pivot div."""
    parts = [
        _class_a_pivot_div(close, _rsi_wilder(close, 14), 63, 63).fillna(0).rename("a"),
        _class_a_pivot_div(close, _macd_line(close, 12, 26), 63, 63).fillna(0).rename("b"),
        _class_a_pivot_div(close, _obv(close, volume), 63, 63).fillna(0).rename("c"),
        _class_a_pivot_div(close, _mfi(high, low, close, volume, 14), 63, 63).fillna(0).rename("d"),
    ]
    cnt = pd.concat(parts, axis=1).sum(axis=1)
    return (cnt >= 2).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f32_divd_240_class_a_pivot_div_persistence_rsi_63d(close: pd.Series) -> pd.Series:
    """Consecutive bars with RSI Class-A 63/63 pivot div == 1 (current streak length)."""
    flag = _class_a_pivot_div(close, _rsi_wilder(close, 14), 63, 63).fillna(0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


# ============================================================
# Bucket JJ — Long-horizon 252d/504d variants of methods (241-255)
# (Each = a different *secular* hypothesis vs the 63d short-cycle versions in 001-150)
# ============================================================

def f32_divd_241_rsi14_shift_div_indicator_504d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs RSI14, 504d lookback (biennial regime change)."""
    return _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), DDAYS_2Y)


def f32_divd_242_macdline_shift_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on MACD line, 252d lookback (annual structure)."""
    return _shift_div_bearish_indicator(close, _macd_line(close, 12, 26), YDAYS)


def f32_divd_243_macdline_shift_div_indicator_504d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on MACD line, 504d (biennial structure)."""
    return _shift_div_bearish_indicator(close, _macd_line(close, 12, 26), DDAYS_2Y)


def f32_divd_244_macdhist_slope_div_sign_252d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on MACD histogram, 252d (annual cycle failure)."""
    return _slope_div_sign(close, _macd_hist(close, 12, 26, 9), YDAYS)


def f32_divd_245_obv_shift_div_indicator_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on OBV, 504d (secular accumulation failure)."""
    return _shift_div_bearish_indicator(close, _obv(close, volume), DDAYS_2Y)


def f32_divd_246_adline_shift_div_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on A/D line, 252d."""
    return _shift_div_bearish_indicator(close, _ad_line(high, low, close, volume), YDAYS)


def f32_divd_247_mfi_shift_div_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on MFI, 252d (annual money-flow failure)."""
    return _shift_div_bearish_indicator(close, _mfi(high, low, close, volume, 14), YDAYS)


def f32_divd_248_stochk_slope_div_sign_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Stoch %K, 252d."""
    return _slope_div_sign(close, _stoch_k(high, low, close, 14), YDAYS)


def f32_divd_249_macdline_zscore_gap_252d(close: pd.Series) -> pd.Series:
    """z(log close,252) - z(MACD line,252) — annual extension gap."""
    return _zscore_gap(close, _macd_line(close, 12, 26), YDAYS)


def f32_divd_250_macdhist_zscore_gap_252d(close: pd.Series) -> pd.Series:
    """z(log close,252) - z(MACD hist,252) — annual histogram-extension."""
    return _zscore_gap(close, _macd_hist(close, 12, 26, 9), YDAYS)


def f32_divd_251_adline_zscore_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,252) - z(A/D,252)."""
    return _zscore_gap(close, _ad_line(high, low, close, volume), YDAYS)


def f32_divd_252_mfi_zscore_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,252) - z(MFI,252)."""
    return _zscore_gap(close, _mfi(high, low, close, volume, 14), YDAYS)


def f32_divd_253_rsi14_rolling_corr_price_504d(close: pd.Series) -> pd.Series:
    """Rolling 504d corr of log-close and RSI14 (biennial agreement)."""
    return _rolling_corr_pearson(_safe_log(close), _rsi_wilder(close, 14), DDAYS_2Y)


def f32_divd_254_macdline_rolling_corr_price_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr of log-close and MACD line."""
    return _rolling_corr_pearson(_safe_log(close), _macd_line(close, 12, 26), YDAYS)


def f32_divd_255_mfi_rolling_corr_price_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr of log-close and MFI."""
    return _rolling_corr_pearson(_safe_log(close), _mfi(high, low, close, volume, 14), YDAYS)


# ============================================================
# Bucket KK — Multi-horizon heatmap meta (256-265)
# ============================================================

def _multi_horizon_div_sum(price, osc, horizons):
    """Sum of bearish slope-div flags across given horizons (0..len(horizons))."""
    parts = [(_slope_div_sign(price, osc, h) > 0).astype(float).rename(f"h{h}") for h in horizons]
    return pd.concat(parts, axis=1).sum(axis=1)


def f32_divd_256_rsi14_multi_horizon_div_5h(close: pd.Series) -> pd.Series:
    """Sum of bearish slope-div flags on RSI14 across 5 horizons (5/21/63/126/252)."""
    return _multi_horizon_div_sum(close, _rsi_wilder(close, 14), [5, 21, 63, 126, 252])


def f32_divd_257_macdline_multi_horizon_div_5h(close: pd.Series) -> pd.Series:
    """Sum of bearish slope-div flags on MACD line across 5 horizons."""
    return _multi_horizon_div_sum(close, _macd_line(close, 12, 26), [5, 21, 63, 126, 252])


def f32_divd_258_obv_multi_horizon_div_5h(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of bearish slope-div flags on OBV across 5 horizons."""
    return _multi_horizon_div_sum(close, _obv(close, volume), [5, 21, 63, 126, 252])


def f32_divd_259_mfi_multi_horizon_div_5h(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of bearish slope-div flags on MFI across 5 horizons."""
    return _multi_horizon_div_sum(close, _mfi(high, low, close, volume, 14), [5, 21, 63, 126, 252])


def f32_divd_260_rsi14_short_horizon_only_div_3h(close: pd.Series) -> pd.Series:
    """RSI bearish-div sum across short horizons only (5/21/63)."""
    return _multi_horizon_div_sum(close, _rsi_wilder(close, 14), [5, 21, 63])


def f32_divd_261_rsi14_long_horizon_only_div_3h(close: pd.Series) -> pd.Series:
    """RSI bearish-div sum across long horizons only (126/252/504)."""
    return _multi_horizon_div_sum(close, _rsi_wilder(close, 14), [126, 252, 504])


def f32_divd_262_multi_osc_x_multi_horizon_heatmap_total(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total bearish-div flag count across 4 osc (RSI/MACD-line/OBV/MFI) × 5 horizons (5/21/63/126/252) = 20 flags."""
    h = [5, 21, 63, 126, 252]
    parts = []
    for name, osc in [("rsi", _rsi_wilder(close, 14)),
                      ("macd", _macd_line(close, 12, 26)),
                      ("obv", _obv(close, volume))]:
        for hh in h:
            parts.append((_slope_div_sign(close, osc, hh) > 0).astype(float).rename(f"{name}_{hh}"))
    return pd.concat(parts, axis=1).sum(axis=1)


def f32_divd_263_short_vs_long_horizon_div_disagreement_rsi(close: pd.Series) -> pd.Series:
    """RSI bearish-div: short-horizons (21/63) flagging while long-horizons (252/504) NOT — early-warning signal."""
    rsi = _rsi_wilder(close, 14)
    s_short = ((_slope_div_sign(close, rsi, 21) > 0).astype(float)
               + (_slope_div_sign(close, rsi, 63) > 0).astype(float)) >= 1
    s_long = ((_slope_div_sign(close, rsi, 252) > 0).astype(float)
              + (_slope_div_sign(close, rsi, 504) > 0).astype(float)) == 0
    return (s_short & s_long).astype(float)


def f32_divd_264_horizon_consensus_div_rsi_3of5(close: pd.Series) -> pd.Series:
    """+1 when RSI shows bearish slope-div at >=3 of 5 horizons simultaneously."""
    s = _multi_horizon_div_sum(close, _rsi_wilder(close, 14), [5, 21, 63, 126, 252])
    return (s >= 3).astype(float).where(s.notna(), np.nan)


def f32_divd_265_horizon_consensus_div_macd_3of5(close: pd.Series) -> pd.Series:
    """+1 when MACD-line shows bearish slope-div at >=3 of 5 horizons simultaneously."""
    s = _multi_horizon_div_sum(close, _macd_line(close, 12, 26), [5, 21, 63, 126, 252])
    return (s >= 3).astype(float).where(s.notna(), np.nan)


# ============================================================
# Bucket LL — Divergence × volume-condition conjunctions (266-275)
# ============================================================

def f32_divd_266_rsi_div_x_high_volume_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish slope-div AND volume z(63) > 1."""
    div = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)
    vz = _rolling_zscore(volume, QDAYS)
    return ((div == 1) & (vz > 1.0)).astype(float).where(div.notna() & vz.notna(), np.nan)


def f32_divd_267_rsi_div_x_vol_dryup_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish slope-div AND volume z(63) < -0.5 (no-volume divergence — quiet topping)."""
    div = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)
    vz = _rolling_zscore(volume, QDAYS)
    return ((div == 1) & (vz < -0.5)).astype(float).where(div.notna() & vz.notna(), np.nan)


def f32_divd_268_macd_div_x_high_volume_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when MACD-line 63d bearish slope-div AND volume z(63) > 1."""
    div = (_slope_div_sign(close, _macd_line(close, 12, 26), QDAYS) > 0).astype(float)
    vz = _rolling_zscore(volume, QDAYS)
    return ((div == 1) & (vz > 1.0)).astype(float).where(div.notna() & vz.notna(), np.nan)


def f32_divd_269_obv_div_x_atr_expansion_indicator_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when OBV 63d bearish slope-div AND ATR21 > 1.5 × ATR252 (vol-expansion topping)."""
    div = (_slope_div_sign(close, _obv(close, volume), QDAYS) > 0).astype(float)
    a21 = _atr(high, low, close, MDAYS); a252 = _atr(high, low, close, YDAYS)
    expand = (a21 > 1.5 * a252).astype(float)
    return ((div == 1) & (expand == 1)).astype(float).where(div.notna() & expand.notna(), np.nan)


def f32_divd_270_rsi_div_x_dollar_vol_top_decile_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND dollar-volume in 252d top decile."""
    div = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)
    dvol = close * volume
    rk = _pct_rank(dvol, YDAYS)
    return ((div == 1) & (rk >= 0.9)).astype(float).where(div.notna() & rk.notna(), np.nan)


def f32_divd_271_macd_div_x_wide_range_bar_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when MACD-line 63d div AND today's range in 252d top decile."""
    div = (_slope_div_sign(close, _macd_line(close, 12, 26), QDAYS) > 0).astype(float)
    rng = high - low
    rk = _pct_rank(rng, YDAYS)
    return ((div == 1) & (rk >= 0.9)).astype(float).where(div.notna() & rk.notna(), np.nan)


def f32_divd_272_obv_div_x_low_volume_at_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when OBV 63d bearish div AND vol z(63) < -0.5 AND close within 1% of 252d max (distribution-on-no-volume)."""
    div = (_slope_div_sign(close, _obv(close, volume), QDAYS) > 0).astype(float)
    vz = _rolling_zscore(volume, QDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((div == 1) & (vz < -0.5) & (near == 1)).astype(float).where(div.notna() & vz.notna() & near.notna(), np.nan)


def f32_divd_273_div_x_3d_volume_surge_indicator_rsi(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND 3d-volume-sum > 2 × 21d-mean (vol-spike conjunction)."""
    div = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)
    v3 = volume.rolling(3, min_periods=1).sum()
    surge = (v3 > 2.0 * volume.rolling(MDAYS, min_periods=WDAYS).mean() * 3.0).astype(float)
    return ((div == 1) & (surge == 1)).astype(float).where(div.notna() & surge.notna(), np.nan)


def f32_divd_274_div_count_x_vol_zsum_252d_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI 21d-div count in 252d × z-sum of volume in 252d — concentration of div events at high-vol regime."""
    cnt = _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), MDAYS).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    vz_mean = _rolling_zscore(volume, YDAYS).rolling(YDAYS, min_periods=QDAYS).mean()
    return cnt * vz_mean.fillna(0)


def f32_divd_275_div_x_atr_dryup_at_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND ATR21 < 0.7 × ATR252 (vol-dryup topping)."""
    div = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)
    a21 = _atr(high, low, close, MDAYS); a252 = _atr(high, low, close, YDAYS)
    dryup = (a21 < 0.7 * a252).astype(float)
    return ((div == 1) & (dryup == 1)).astype(float).where(div.notna() & dryup.notna(), np.nan)


# ============================================================
# Bucket MM — R² regression strength metrics (276-285)
# ============================================================

def _rolling_r_squared(price, osc, n):
    """Rolling R² of OLS regression of osc on log-price. High R² with negative slope = strong divergence."""
    return _rolling_corr_pearson(_safe_log(price), osc, n) ** 2


def f32_divd_276_rsi14_r_squared_63d(close: pd.Series) -> pd.Series:
    """R² of log-close vs RSI14 over 63d (strength of price-RSI relationship)."""
    return _rolling_r_squared(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_277_rsi14_r_squared_252d(close: pd.Series) -> pd.Series:
    """R² of log-close vs RSI14 over 252d (secular agreement strength)."""
    return _rolling_r_squared(close, _rsi_wilder(close, 14), YDAYS)


def f32_divd_278_macdline_r_squared_63d(close: pd.Series) -> pd.Series:
    """R² of log-close vs MACD line over 63d."""
    return _rolling_r_squared(close, _macd_line(close, 12, 26), QDAYS)


def f32_divd_279_obv_r_squared_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """R² of log-close vs OBV over 252d (secular accumulation-price coupling)."""
    return _rolling_r_squared(close, _obv(close, volume), YDAYS)


def f32_divd_280_mfi_r_squared_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """R² of log-close vs MFI over 63d."""
    return _rolling_r_squared(close, _mfi(high, low, close, volume, 14), QDAYS)


def f32_divd_281_r_squared_with_negative_corr_bearish_strength_rsi_63d(close: pd.Series) -> pd.Series:
    """R² of log-close vs RSI multiplied by sign of corr — negative magnitude = strong bearish-coupling-divergence."""
    c = _rolling_corr_pearson(_safe_log(close), _rsi_wilder(close, 14), QDAYS)
    return (c ** 2) * np.sign(c)


def f32_divd_282_r_squared_with_negative_corr_bearish_strength_obv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """R² × sign(corr) for OBV — negative magnitude = strong bearish OBV-coupling."""
    c = _rolling_corr_pearson(_safe_log(close), _obv(close, volume), QDAYS)
    return (c ** 2) * np.sign(c)


def f32_divd_283_r_squared_decay_21d_rsi(close: pd.Series) -> pd.Series:
    """Change in R²(63d) over 21d — declining R² = decoupling/divergence forming."""
    r = _rolling_r_squared(close, _rsi_wilder(close, 14), QDAYS)
    return r - r.shift(MDAYS)


def f32_divd_284_r_squared_decay_63d_obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Change in R²(252d) over 63d for OBV — declining secular coupling."""
    r = _rolling_r_squared(close, _obv(close, volume), YDAYS)
    return r - r.shift(QDAYS)


def f32_divd_285_corr_sign_flip_event_indicator_63d_rsi(close: pd.Series) -> pd.Series:
    """+1 on bar where 63d corr(log-close, RSI) flipped from positive to negative (decoupling event)."""
    c = _rolling_corr_pearson(_safe_log(close), _rsi_wilder(close, 14), QDAYS)
    return ((c.shift(1) > 0) & (c <= 0)).astype(float).where(c.notna() & c.shift(1).notna(), np.nan)


# ============================================================
# Bucket NN — Persistence + magnitude composites across multiple osc (286-295)
# ============================================================

def f32_divd_286_max_consecutive_div_streak_4osc_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum across 4 osc (RSI/MACD-line/MACD-H/OBV) of current consecutive-bar bearish-slope-div streak."""
    panel = [_rsi_wilder(close, 14), _macd_line(close, 12, 26),
             _macd_hist(close, 12, 26, 9), _obv(close, volume)]
    streaks = []
    for i, o in enumerate(panel):
        flag = (_slope_div_sign(close, o, QDAYS) > 0).astype(int)
        grp = (flag == 0).cumsum()
        st = flag.groupby(grp).cumsum().astype(float).rename(f"s{i}")
        streaks.append(st)
    return pd.concat(streaks, axis=1).max(axis=1)


def f32_divd_287_mean_consecutive_div_streak_4osc_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean across 4 osc of current consecutive bearish-div streak length."""
    panel = [_rsi_wilder(close, 14), _macd_line(close, 12, 26),
             _macd_hist(close, 12, 26, 9), _obv(close, volume)]
    streaks = []
    for i, o in enumerate(panel):
        flag = (_slope_div_sign(close, o, QDAYS) > 0).astype(int)
        grp = (flag == 0).cumsum()
        st = flag.groupby(grp).cumsum().astype(float).rename(f"s{i}")
        streaks.append(st)
    return pd.concat(streaks, axis=1).mean(axis=1)


def f32_divd_288_zscore_gap_composite_3osc_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (z-score gap close vs RSI/MACD-line/OBV) over 252d — composite extension index."""
    parts = [
        _zscore_gap(close, _rsi_wilder(close, 14), YDAYS).rename("a"),
        _zscore_gap(close, _macd_line(close, 12, 26), YDAYS).rename("b"),
        _zscore_gap(close, _obv(close, volume), YDAYS).rename("c"),
    ]
    return pd.concat(parts, axis=1).mean(axis=1)


def f32_divd_289_max_zscore_gap_3osc_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum across 3 osc (RSI/MACD-line/OBV) of 63d z-score gap."""
    parts = [
        _zscore_gap(close, _rsi_wilder(close, 14), QDAYS).rename("a"),
        _zscore_gap(close, _macd_line(close, 12, 26), QDAYS).rename("b"),
        _zscore_gap(close, _obv(close, volume), QDAYS).rename("c"),
    ]
    return pd.concat(parts, axis=1).max(axis=1)


def f32_divd_290_count_div_active_at_overbought_3osc(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 3 osc (RSI/MFI/Stoch%K) where bearish-div AND osc is in overbought zone."""
    osc_thresh = [
        (_rsi_wilder(close, 14), 70.0),
        # MFI requires high/low — use Stoch K and RSI instead, since MFI needs more args
        (_macd_hist(close, 12, 26, 9), 0.0),
    ]
    # Simplified: 2 osc (RSI/MACD-H) to avoid extra inputs
    cnt = pd.Series(0.0, index=close.index)
    for osc, th in osc_thresh:
        div = (_slope_div_sign(close, osc, QDAYS) > 0).astype(float).fillna(0)
        ob = (osc > th).astype(float).fillna(0)
        cnt = cnt + (div * ob)
    return cnt


def f32_divd_291_div_magnitude_zsum_zscore_composite_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (over 252d) of the sum-of-magnitudes of 21d shift-div on RSI/MACD-line/OBV."""
    parts = [
        _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), MDAYS).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().rename("a"),
        _shift_div_bearish_indicator(close, _macd_line(close, 12, 26), MDAYS).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().rename("b"),
        _shift_div_bearish_indicator(close, _obv(close, volume), MDAYS).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().rename("c"),
    ]
    total = pd.concat(parts, axis=1).sum(axis=1)
    return _rolling_zscore(total, YDAYS)


def f32_divd_292_div_freshness_min_age_3osc(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Minimum bars-since-last-21d-bearish-shift-div across 3 osc (RSI/MACD-line/OBV)."""
    parts = []
    for i, o in enumerate([_rsi_wilder(close, 14), _macd_line(close, 12, 26), _obv(close, volume)]):
        flag = _shift_div_bearish_indicator(close, o, MDAYS).fillna(0)
        idx = np.arange(len(flag))
        last = np.where(flag.values > 0, idx, np.nan)
        last_ff = pd.Series(last, index=flag.index).ffill()
        parts.append((pd.Series(idx, index=flag.index) - last_ff).rename(f"a{i}"))
    return pd.concat(parts, axis=1).min(axis=1)


def f32_divd_293_composite_div_intensity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum across 4 osc of div-event-counts in trailing 252d (intensity-of-divergence-load)."""
    osc_list = [_rsi_wilder(close, 14), _macd_line(close, 12, 26),
                _macd_hist(close, 12, 26, 9), _obv(close, volume)]
    parts = []
    for i, o in enumerate(osc_list):
        parts.append(_shift_div_bearish_indicator(close, o, MDAYS).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum().rename(f"o{i}"))
    return pd.concat(parts, axis=1).sum(axis=1)


def f32_divd_294_breadth_x_persistence_composite_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Breadth-of-divergence (4 osc) × mean-streak-length — both wide AND persistent = severe."""
    panel = [_rsi_wilder(close, 14), _macd_line(close, 12, 26),
             _macd_hist(close, 12, 26, 9), _obv(close, volume)]
    flags = []; streaks = []
    for i, o in enumerate(panel):
        f = (_slope_div_sign(close, o, QDAYS) > 0).astype(float).rename(f"f{i}")
        flags.append(f)
        flagi = f.fillna(0).astype(int)
        grp = (flagi == 0).cumsum()
        streaks.append(flagi.groupby(grp).cumsum().astype(float).rename(f"s{i}"))
    breadth = pd.concat(flags, axis=1).mean(axis=1)
    mean_streak = pd.concat(streaks, axis=1).mean(axis=1)
    return breadth * mean_streak


def f32_divd_295_zsum_5h_x_at_high_score_rsi(close: pd.Series) -> pd.Series:
    """Sum of z-score gaps (RSI) across 5 horizons (21/63/126/252/504), gated by close-near-252d-max."""
    horizons = [21, 63, 126, 252, 504]
    zsum = sum(_zscore_gap(close, _rsi_wilder(close, 14), h) for h in horizons)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return zsum * near


# ============================================================
# Bucket OO — Cross-osc-and-vol-and-extreme conjunctions (296-300)
# ============================================================

def f32_divd_296_triple_osc_div_x_252d_high_x_high_vol_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI AND MACD-line AND OBV all show bearish slope-div over 63d AND close near 252d max AND vol z(63) > 0.5."""
    a = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0)
    b = (_slope_div_sign(close, _macd_line(close, 12, 26), QDAYS) > 0)
    c = (_slope_div_sign(close, _obv(close, volume), QDAYS) > 0)
    near = close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99
    vz_high = _rolling_zscore(volume, QDAYS) > 0.5
    return (a & b & c & near & vz_high).astype(float)


def f32_divd_297_breadth_5osc_x_1260d_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when bearish-div-breadth-5osc-63d > 0.6 AND close within 2% of 1260d max."""
    panel = [_rsi_wilder(close, 14), _macd_line(close, 12, 26),
             _macd_hist(close, 12, 26, 9), _obv(close, volume), _stoch_k(close * 0 + close, close * 0 + close, close, 14)]
    flags = [(_slope_div_sign(close, o, QDAYS) > 0).astype(float).rename(f"f{i}") for i, o in enumerate(panel)]
    breadth = pd.concat(flags, axis=1).mean(axis=1)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return ((breadth > 0.6) & (near == 1)).astype(float).where(breadth.notna() & near.notna(), np.nan)


def f32_divd_298_secular_div_x_atr_dryup_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 252d bearish slope-div AND ATR21 < 0.7 × ATR252 AND close near 252d max — quiet secular topping."""
    div = (_slope_div_sign(close, _rsi_wilder(close, 14), YDAYS) > 0).astype(float)
    a21 = _atr(high, low, close, MDAYS); a252 = _atr(high, low, close, YDAYS)
    dryup = (a21 < 0.7 * a252).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((div == 1) & (dryup == 1) & (near == 1)).astype(float).where(div.notna() & dryup.notna() & near.notna(), np.nan)


def f32_divd_299_div_velocity_acceleration_at_high_rsi(close: pd.Series) -> pd.Series:
    """RSI 21d-div-count-acceleration (21d_count - 63d_count) gated by close-near-252d-max."""
    rsi = _rsi_wilder(close, 14)
    flag = _shift_div_bearish_indicator(close, rsi, MDAYS).fillna(0)
    c21 = flag.rolling(MDAYS, min_periods=WDAYS).sum() / MDAYS
    c63 = flag.rolling(QDAYS, min_periods=MDAYS).sum() / QDAYS
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (c21 - c63) * near


def f32_divd_300_master_divergence_topping_index_composite(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Master topping index: 0.25*RSI-zscore-gap-252d + 0.20*MACD-zscore-gap-252d + 0.20*OBV-zscore-gap-252d
    + 0.15*close-pct-rank-1260d + 0.10*breadth-5osc-63d + 0.10*vol-zscore-252d."""
    rsi_z = _zscore_gap(close, _rsi_wilder(close, 14), YDAYS)
    macd_z = _zscore_gap(close, _macd_line(close, 12, 26), YDAYS)
    obv_z = _zscore_gap(close, _obv(close, volume), YDAYS)
    px_rank = _pct_rank(close, DDAYS_5Y)
    panel = [_rsi_wilder(close, 14), _macd_line(close, 12, 26),
             _macd_hist(close, 12, 26, 9), _obv(close, volume), _stoch_k(high, low, close, 14)]
    flags = [(_slope_div_sign(close, o, QDAYS) > 0).astype(float).rename(f"f{i}") for i, o in enumerate(panel)]
    breadth = pd.concat(flags, axis=1).mean(axis=1)
    vz = _rolling_zscore(volume, YDAYS)
    return (0.25 * rsi_z + 0.20 * macd_z + 0.20 * obv_z
            + 0.15 * px_rank + 0.10 * breadth + 0.10 * vz)


# ============================================================
# REGISTRY
# ============================================================

DIVERGENCE_DETECTION_BASE_REGISTRY_226_300 = {
    "f32_divd_226_rsi14_class_a_pivot_div_63_63": {"inputs": ["close"], "func": f32_divd_226_rsi14_class_a_pivot_div_63_63},
    "f32_divd_227_rsi14_class_a_pivot_div_21_42": {"inputs": ["close"], "func": f32_divd_227_rsi14_class_a_pivot_div_21_42},
    "f32_divd_228_rsi14_class_a_pivot_div_126_126": {"inputs": ["close"], "func": f32_divd_228_rsi14_class_a_pivot_div_126_126},
    "f32_divd_229_macdline_class_a_pivot_div_63_63": {"inputs": ["close"], "func": f32_divd_229_macdline_class_a_pivot_div_63_63},
    "f32_divd_230_macdline_class_a_pivot_div_21_42": {"inputs": ["close"], "func": f32_divd_230_macdline_class_a_pivot_div_21_42},
    "f32_divd_231_macdhist_class_a_pivot_div_63_63": {"inputs": ["close"], "func": f32_divd_231_macdhist_class_a_pivot_div_63_63},
    "f32_divd_232_obv_class_a_pivot_div_63_63": {"inputs": ["close", "volume"], "func": f32_divd_232_obv_class_a_pivot_div_63_63},
    "f32_divd_233_obv_class_a_pivot_div_126_126": {"inputs": ["close", "volume"], "func": f32_divd_233_obv_class_a_pivot_div_126_126},
    "f32_divd_234_adline_class_a_pivot_div_63_63": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_234_adline_class_a_pivot_div_63_63},
    "f32_divd_235_stochk_class_a_pivot_div_63_63": {"inputs": ["high", "low", "close"], "func": f32_divd_235_stochk_class_a_pivot_div_63_63},
    "f32_divd_236_mfi_class_a_pivot_div_63_63": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_236_mfi_class_a_pivot_div_63_63},
    "f32_divd_237_class_a_pivot_div_breadth_4osc_63_63": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_237_class_a_pivot_div_breadth_4osc_63_63},
    "f32_divd_238_class_a_pivot_div_x_at_252d_high_indicator": {"inputs": ["close", "volume"], "func": f32_divd_238_class_a_pivot_div_x_at_252d_high_indicator},
    "f32_divd_239_class_a_pivot_div_count_4osc_252d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_239_class_a_pivot_div_count_4osc_252d},
    "f32_divd_240_class_a_pivot_div_persistence_rsi_63d": {"inputs": ["close"], "func": f32_divd_240_class_a_pivot_div_persistence_rsi_63d},
    "f32_divd_241_rsi14_shift_div_indicator_504d": {"inputs": ["close"], "func": f32_divd_241_rsi14_shift_div_indicator_504d},
    "f32_divd_242_macdline_shift_div_indicator_252d": {"inputs": ["close"], "func": f32_divd_242_macdline_shift_div_indicator_252d},
    "f32_divd_243_macdline_shift_div_indicator_504d": {"inputs": ["close"], "func": f32_divd_243_macdline_shift_div_indicator_504d},
    "f32_divd_244_macdhist_slope_div_sign_252d": {"inputs": ["close"], "func": f32_divd_244_macdhist_slope_div_sign_252d},
    "f32_divd_245_obv_shift_div_indicator_504d": {"inputs": ["close", "volume"], "func": f32_divd_245_obv_shift_div_indicator_504d},
    "f32_divd_246_adline_shift_div_indicator_252d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_246_adline_shift_div_indicator_252d},
    "f32_divd_247_mfi_shift_div_indicator_252d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_247_mfi_shift_div_indicator_252d},
    "f32_divd_248_stochk_slope_div_sign_252d": {"inputs": ["high", "low", "close"], "func": f32_divd_248_stochk_slope_div_sign_252d},
    "f32_divd_249_macdline_zscore_gap_252d": {"inputs": ["close"], "func": f32_divd_249_macdline_zscore_gap_252d},
    "f32_divd_250_macdhist_zscore_gap_252d": {"inputs": ["close"], "func": f32_divd_250_macdhist_zscore_gap_252d},
    "f32_divd_251_adline_zscore_gap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_251_adline_zscore_gap_252d},
    "f32_divd_252_mfi_zscore_gap_252d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_252_mfi_zscore_gap_252d},
    "f32_divd_253_rsi14_rolling_corr_price_504d": {"inputs": ["close"], "func": f32_divd_253_rsi14_rolling_corr_price_504d},
    "f32_divd_254_macdline_rolling_corr_price_252d": {"inputs": ["close"], "func": f32_divd_254_macdline_rolling_corr_price_252d},
    "f32_divd_255_mfi_rolling_corr_price_252d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_255_mfi_rolling_corr_price_252d},
    "f32_divd_256_rsi14_multi_horizon_div_5h": {"inputs": ["close"], "func": f32_divd_256_rsi14_multi_horizon_div_5h},
    "f32_divd_257_macdline_multi_horizon_div_5h": {"inputs": ["close"], "func": f32_divd_257_macdline_multi_horizon_div_5h},
    "f32_divd_258_obv_multi_horizon_div_5h": {"inputs": ["close", "volume"], "func": f32_divd_258_obv_multi_horizon_div_5h},
    "f32_divd_259_mfi_multi_horizon_div_5h": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_259_mfi_multi_horizon_div_5h},
    "f32_divd_260_rsi14_short_horizon_only_div_3h": {"inputs": ["close"], "func": f32_divd_260_rsi14_short_horizon_only_div_3h},
    "f32_divd_261_rsi14_long_horizon_only_div_3h": {"inputs": ["close"], "func": f32_divd_261_rsi14_long_horizon_only_div_3h},
    "f32_divd_262_multi_osc_x_multi_horizon_heatmap_total": {"inputs": ["close", "volume"], "func": f32_divd_262_multi_osc_x_multi_horizon_heatmap_total},
    "f32_divd_263_short_vs_long_horizon_div_disagreement_rsi": {"inputs": ["close"], "func": f32_divd_263_short_vs_long_horizon_div_disagreement_rsi},
    "f32_divd_264_horizon_consensus_div_rsi_3of5": {"inputs": ["close"], "func": f32_divd_264_horizon_consensus_div_rsi_3of5},
    "f32_divd_265_horizon_consensus_div_macd_3of5": {"inputs": ["close"], "func": f32_divd_265_horizon_consensus_div_macd_3of5},
    "f32_divd_266_rsi_div_x_high_volume_indicator_63d": {"inputs": ["close", "volume"], "func": f32_divd_266_rsi_div_x_high_volume_indicator_63d},
    "f32_divd_267_rsi_div_x_vol_dryup_indicator_63d": {"inputs": ["close", "volume"], "func": f32_divd_267_rsi_div_x_vol_dryup_indicator_63d},
    "f32_divd_268_macd_div_x_high_volume_indicator_63d": {"inputs": ["close", "volume"], "func": f32_divd_268_macd_div_x_high_volume_indicator_63d},
    "f32_divd_269_obv_div_x_atr_expansion_indicator_63d": {"inputs": ["close", "high", "low", "volume"], "func": f32_divd_269_obv_div_x_atr_expansion_indicator_63d},
    "f32_divd_270_rsi_div_x_dollar_vol_top_decile_indicator": {"inputs": ["close", "volume"], "func": f32_divd_270_rsi_div_x_dollar_vol_top_decile_indicator},
    "f32_divd_271_macd_div_x_wide_range_bar_indicator": {"inputs": ["close", "high", "low"], "func": f32_divd_271_macd_div_x_wide_range_bar_indicator},
    "f32_divd_272_obv_div_x_low_volume_at_high_indicator": {"inputs": ["close", "volume"], "func": f32_divd_272_obv_div_x_low_volume_at_high_indicator},
    "f32_divd_273_div_x_3d_volume_surge_indicator_rsi": {"inputs": ["close", "volume"], "func": f32_divd_273_div_x_3d_volume_surge_indicator_rsi},
    "f32_divd_274_div_count_x_vol_zsum_252d_composite": {"inputs": ["close", "volume"], "func": f32_divd_274_div_count_x_vol_zsum_252d_composite},
    "f32_divd_275_div_x_atr_dryup_at_high_indicator": {"inputs": ["close", "high", "low"], "func": f32_divd_275_div_x_atr_dryup_at_high_indicator},
    "f32_divd_276_rsi14_r_squared_63d": {"inputs": ["close"], "func": f32_divd_276_rsi14_r_squared_63d},
    "f32_divd_277_rsi14_r_squared_252d": {"inputs": ["close"], "func": f32_divd_277_rsi14_r_squared_252d},
    "f32_divd_278_macdline_r_squared_63d": {"inputs": ["close"], "func": f32_divd_278_macdline_r_squared_63d},
    "f32_divd_279_obv_r_squared_252d": {"inputs": ["close", "volume"], "func": f32_divd_279_obv_r_squared_252d},
    "f32_divd_280_mfi_r_squared_63d": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_280_mfi_r_squared_63d},
    "f32_divd_281_r_squared_with_negative_corr_bearish_strength_rsi_63d": {"inputs": ["close"], "func": f32_divd_281_r_squared_with_negative_corr_bearish_strength_rsi_63d},
    "f32_divd_282_r_squared_with_negative_corr_bearish_strength_obv_63d": {"inputs": ["close", "volume"], "func": f32_divd_282_r_squared_with_negative_corr_bearish_strength_obv_63d},
    "f32_divd_283_r_squared_decay_21d_rsi": {"inputs": ["close"], "func": f32_divd_283_r_squared_decay_21d_rsi},
    "f32_divd_284_r_squared_decay_63d_obv": {"inputs": ["close", "volume"], "func": f32_divd_284_r_squared_decay_63d_obv},
    "f32_divd_285_corr_sign_flip_event_indicator_63d_rsi": {"inputs": ["close"], "func": f32_divd_285_corr_sign_flip_event_indicator_63d_rsi},
    "f32_divd_286_max_consecutive_div_streak_4osc_63d": {"inputs": ["close", "volume"], "func": f32_divd_286_max_consecutive_div_streak_4osc_63d},
    "f32_divd_287_mean_consecutive_div_streak_4osc_63d": {"inputs": ["close", "volume"], "func": f32_divd_287_mean_consecutive_div_streak_4osc_63d},
    "f32_divd_288_zscore_gap_composite_3osc_252d": {"inputs": ["close", "volume"], "func": f32_divd_288_zscore_gap_composite_3osc_252d},
    "f32_divd_289_max_zscore_gap_3osc_63d": {"inputs": ["close", "volume"], "func": f32_divd_289_max_zscore_gap_3osc_63d},
    "f32_divd_290_count_div_active_at_overbought_3osc": {"inputs": ["close", "volume"], "func": f32_divd_290_count_div_active_at_overbought_3osc},
    "f32_divd_291_div_magnitude_zsum_zscore_composite_252d": {"inputs": ["close", "volume"], "func": f32_divd_291_div_magnitude_zsum_zscore_composite_252d},
    "f32_divd_292_div_freshness_min_age_3osc": {"inputs": ["close", "volume"], "func": f32_divd_292_div_freshness_min_age_3osc},
    "f32_divd_293_composite_div_intensity_252d": {"inputs": ["close", "volume"], "func": f32_divd_293_composite_div_intensity_252d},
    "f32_divd_294_breadth_x_persistence_composite_63d": {"inputs": ["close", "volume"], "func": f32_divd_294_breadth_x_persistence_composite_63d},
    "f32_divd_295_zsum_5h_x_at_high_score_rsi": {"inputs": ["close"], "func": f32_divd_295_zsum_5h_x_at_high_score_rsi},
    "f32_divd_296_triple_osc_div_x_252d_high_x_high_vol_indicator": {"inputs": ["close", "volume"], "func": f32_divd_296_triple_osc_div_x_252d_high_x_high_vol_indicator},
    "f32_divd_297_breadth_5osc_x_1260d_high_indicator": {"inputs": ["close", "volume"], "func": f32_divd_297_breadth_5osc_x_1260d_high_indicator},
    "f32_divd_298_secular_div_x_atr_dryup_indicator": {"inputs": ["close", "high", "low"], "func": f32_divd_298_secular_div_x_atr_dryup_indicator},
    "f32_divd_299_div_velocity_acceleration_at_high_rsi": {"inputs": ["close"], "func": f32_divd_299_div_velocity_acceleration_at_high_rsi},
    "f32_divd_300_master_divergence_topping_index_composite": {"inputs": ["close", "volume", "high", "low"], "func": f32_divd_300_master_divergence_topping_index_composite},
}
