"""divergence_detection d2 features 076-150 — Pipeline 1b-technical.

150 distinct bearish-divergence hypotheses across __base__001_075.py and this file.
This file extends coverage to MFI / CCI / TRIX / TSI / ROC / UO oscillators, then
adds multi-oscillator stacking, breadth, persistence/age, count-in-window,
magnitude composites, divergence-of-divergence, and cross-oscillator-at-extreme
composites.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers — no cross-family
imports.
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


# ---------------------------- oscillator helpers ----------------------------

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
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


def _stoch_k(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)


def _mfi(high, low, close, volume, n=14):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    delta = tp.diff()
    pos = rmf.where(delta > 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    neg = rmf.where(delta < 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = _safe_div(pos, neg)
    return 100.0 - 100.0 / (1.0 + mr)


def _cci(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(tp - sma, 0.015 * mad)


def _trix(close, n=15):
    e1 = _ema(close, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    return e3.pct_change() * 100.0


def _tsi(close, r=25, s=13):
    m = close.diff()
    am = m.abs()
    return 100.0 * _safe_div(_ema(_ema(m, r), s), _ema(_ema(am, r), s))


def _roc(close, n=12):
    return close.pct_change(n) * 100.0


def _uo(high, low, close, n1=7, n2=14, n3=28):
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = _true_range(high, low, close)
    def _avg(n):
        return _safe_div(bp.rolling(n, min_periods=max(n // 3, 2)).sum(),
                         tr.rolling(n, min_periods=max(n // 3, 2)).sum())
    return 100.0 * (4.0 * _avg(n1) + 2.0 * _avg(n2) + _avg(n3)) / 7.0


# ---------------------------- divergence-detection helpers ----------------------------

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    bear = ((ps > 0) & (osl < 0)).astype(float)
    bull = ((ps < 0) & (osl > 0)).astype(float)
    out = bear - bull
    return out.where(ps.notna() & osl.notna(), np.nan)


def _slope_div_magnitude(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    psz = _rolling_zscore(ps, n)
    osz = _rolling_zscore(osl, n)
    return psz - osz


def _shift_div_bearish_indicator(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    flag = ((price > pp) & (osc < op))
    return flag.astype(float).where(pp.notna() & op.notna(), np.nan)


def _shift_div_bearish_magnitude(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    pxch = _safe_div(price - pp, pp.abs())
    oscz = _rolling_zscore(osc, max(k, 21))
    oscz_pp = oscz.shift(k)
    flag = (price > pp) & (osc < op)
    mag = (pxch - (oscz - oscz_pp)).where(flag, 0.0)
    return mag.where(pp.notna() & op.notna(), np.nan)


def _shift_div_hidden_bearish_indicator(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    flag = ((price < pp) & (osc > op))
    return flag.astype(float).where(pp.notna() & op.notna(), np.nan)


def _rolling_corr_pearson(a, b, n):
    return a.rolling(n, min_periods=max(n // 3, 2)).corr(b)


def _zscore_gap(price, osc, n):
    return _rolling_zscore(_safe_log(price), n) - _rolling_zscore(osc, n)


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _pct_rank_gap(price, osc, n):
    return _pct_rank(price, n) - _pct_rank(osc, n)


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


def _div_persistence(price, osc, k):
    flag = _shift_div_bearish_indicator(price, osc, k)
    return _bars_since_true(flag)


def _div_count_in_window(price, osc, k, win):
    flag = _shift_div_bearish_indicator(price, osc, k).fillna(0)
    return flag.rolling(win, min_periods=max(win // 3, 2)).sum()


def _oscillator_panel_for_breadth(open_, high, low, close, volume):
    """Compute the canonical 5-oscillator panel used for breadth/stacking features.
    Order is fixed: RSI14, MACD-H, OBV, Stoch%K, MFI."""
    return [
        _rsi_wilder(close, 14),
        _macd_hist(close, 12, 26, 9),
        _obv(close, volume),
        _stoch_k(high, low, close, 14),
        _mfi(high, low, close, volume, 14),
    ]


def _oscillator_panel_short_3(open_, high, low, close, volume):
    """Compact 3-oscillator panel: RSI14, OBV, Stoch%K (used for short-horizon breadth)."""
    return [
        _rsi_wilder(close, 14),
        _obv(close, volume),
        _stoch_k(high, low, close, 14),
    ]


def _bearish_div_flags_panel(price, osc_list, n, method="slope"):
    """Return DataFrame: columns o0,o1,...; each = 0/1 bearish divergence flag at horizon n."""
    cols = []
    for i, o in enumerate(osc_list):
        if method == "slope":
            f = (_slope_div_sign(price, o, n) > 0).astype(float)
        elif method == "shift":
            f = (_shift_div_bearish_indicator(price, o, n).fillna(0) > 0).astype(float)
        elif method == "hidden":
            f = (_shift_div_hidden_bearish_indicator(price, o, n).fillna(0) > 0).astype(float)
        else:
            raise ValueError(method)
        cols.append(f.rename(f"o{i}"))
    return pd.concat(cols, axis=1)


def _bearish_div_mag_panel(price, osc_list, n):
    cols = []
    for i, o in enumerate(osc_list):
        m = _slope_div_magnitude(price, o, n).rename(f"o{i}")
        cols.append(m)
    return pd.concat(cols, axis=1)


# ============================================================
# Bucket J — MFI divergences (076-083)
# ============================================================

def f32_divd_076_mfi_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on MFI(14), 63d."""
    return _slope_div_sign(close, _mfi(high, low, close, volume, 14), QDAYS)


def f32_divd_077_mfi_slope_div_sign_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on MFI(14), 252d (secular)."""
    return _slope_div_sign(close, _mfi(high, low, close, volume, 14), YDAYS)


def f32_divd_078_mfi_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on MFI, 63d."""
    return _shift_div_bearish_indicator(close, _mfi(high, low, close, volume, 14), QDAYS)


def f32_divd_079_mfi_shift_div_magnitude_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Magnitude of 63d bearish shift-divergence on MFI."""
    return _shift_div_bearish_magnitude(close, _mfi(high, low, close, volume, 14), QDAYS)


def f32_divd_080_mfi_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(MFI,63)."""
    return _zscore_gap(close, _mfi(high, low, close, volume, 14), QDAYS)


def f32_divd_081_mfi_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and MFI."""
    return _rolling_corr_pearson(_safe_log(close), _mfi(high, low, close, volume, 14), QDAYS)


def f32_divd_082_mfi_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + MFI HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _mfi(high, low, close, volume, 14), QDAYS)


def f32_divd_083_mfi_div_x_overbought_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish MFI divergence AND MFI > 80 — conjunction."""
    m = _mfi(high, low, close, volume, 14)
    div = _shift_div_bearish_indicator(close, m, QDAYS)
    return (div * (m > 80).astype(float)).where(m.notna() & div.notna(), np.nan)


# ============================================================
# Bucket K — CCI divergences (084-089)
# ============================================================

def f32_divd_084_cci_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on CCI(20), 63d."""
    return _slope_div_sign(close, _cci(high, low, close, 20), QDAYS)


def f32_divd_085_cci_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on CCI, 63d."""
    return _shift_div_bearish_indicator(close, _cci(high, low, close, 20), QDAYS)


def f32_divd_086_cci_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """z(log close,63) - z(CCI,63)."""
    return _zscore_gap(close, _cci(high, low, close, 20), QDAYS)


def f32_divd_087_cci_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and CCI."""
    return _rolling_corr_pearson(_safe_log(close), _cci(high, low, close, 20), QDAYS)


def f32_divd_088_cci_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + CCI HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _cci(high, low, close, 20), QDAYS)


def f32_divd_089_cci_div_x_extreme_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CCI divergence AND CCI > +100 (extreme overbought) — conjunction."""
    c = _cci(high, low, close, 20)
    div = _shift_div_bearish_indicator(close, c, QDAYS)
    return (div * (c > 100).astype(float)).where(c.notna() & div.notna(), np.nan)


# ============================================================
# Bucket L — TRIX divergences (090-095)
# ============================================================

def f32_divd_090_trix_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on TRIX(15), 63d."""
    return _slope_div_sign(close, _trix(close, 15), QDAYS)


def f32_divd_091_trix_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on TRIX, 63d."""
    return _shift_div_bearish_indicator(close, _trix(close, 15), QDAYS)


def f32_divd_092_trix_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(TRIX,63)."""
    return _zscore_gap(close, _trix(close, 15), QDAYS)


def f32_divd_093_trix_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and TRIX."""
    return _rolling_corr_pearson(_safe_log(close), _trix(close, 15), QDAYS)


def f32_divd_094_trix_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + TRIX HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _trix(close, 15), QDAYS)


def f32_divd_095_trix_pos_to_neg_flip_at_high_indicator(close: pd.Series) -> pd.Series:
    """TRIX flipped from positive to negative within last 5d AND price within 1% of 252d-max."""
    t = _trix(close, 15)
    flip = ((t.shift(1) > 0) & (t <= 0)).astype(float).rolling(WDAYS, min_periods=1).max()
    at_max = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (flip * at_max).where(t.notna(), np.nan)


# ============================================================
# Bucket M — TSI divergences (096-101)
# ============================================================

def f32_divd_096_tsi_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on TSI(25,13), 63d."""
    return _slope_div_sign(close, _tsi(close, 25, 13), QDAYS)


def f32_divd_097_tsi_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on TSI, 63d."""
    return _shift_div_bearish_indicator(close, _tsi(close, 25, 13), QDAYS)


def f32_divd_098_tsi_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(TSI,63)."""
    return _zscore_gap(close, _tsi(close, 25, 13), QDAYS)


def f32_divd_099_tsi_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and TSI."""
    return _rolling_corr_pearson(_safe_log(close), _tsi(close, 25, 13), QDAYS)


def f32_divd_100_tsi_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + TSI HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _tsi(close, 25, 13), QDAYS)


def f32_divd_101_tsi_div_count_in_252d(close: pd.Series) -> pd.Series:
    """Count of TSI 21d bearish-shift divergences within trailing 252d."""
    return _div_count_in_window(close, _tsi(close, 25, 13), MDAYS, YDAYS)


# ============================================================
# Bucket N — ROC divergences (102-109)
# (Short-ROC = monthly-momentum hypothesis; Long-ROC = quarterly-momentum hypothesis —
#  distinct concepts, not a parameter sweep.)
# ============================================================

def f32_divd_102_roc12_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on short-horizon ROC(12), 63d — monthly momentum."""
    return _slope_div_sign(close, _roc(close, 12), QDAYS)


def f32_divd_103_roc12_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on ROC(12), 63d."""
    return _shift_div_bearish_indicator(close, _roc(close, 12), QDAYS)


def f32_divd_104_roc12_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(ROC12,63)."""
    return _zscore_gap(close, _roc(close, 12), QDAYS)


def f32_divd_105_roc12_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and ROC(12)."""
    return _rolling_corr_pearson(_safe_log(close), _roc(close, 12), QDAYS)


def f32_divd_106_roc63_slope_div_sign_252d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on long-horizon ROC(63), 252d — quarterly momentum vs secular price."""
    return _slope_div_sign(close, _roc(close, QDAYS), YDAYS)


def f32_divd_107_roc63_shift_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on ROC(63), 252d — long-cycle momentum failure."""
    return _shift_div_bearish_indicator(close, _roc(close, QDAYS), YDAYS)


def f32_divd_108_roc12_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + ROC12 HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _roc(close, 12), QDAYS)


def f32_divd_109_roc12_div_count_in_252d(close: pd.Series) -> pd.Series:
    """Count of ROC12 21d bearish-shift divergences in trailing 252d."""
    return _div_count_in_window(close, _roc(close, 12), MDAYS, YDAYS)


# ============================================================
# Bucket O — Ultimate Oscillator divergences (110-115)
# ============================================================

def f32_divd_110_uo_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Ultimate Oscillator (7/14/28), 63d."""
    return _slope_div_sign(close, _uo(high, low, close), QDAYS)


def f32_divd_111_uo_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on UO, 63d."""
    return _shift_div_bearish_indicator(close, _uo(high, low, close), QDAYS)


def f32_divd_112_uo_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """z(log close,63) - z(UO,63)."""
    return _zscore_gap(close, _uo(high, low, close), QDAYS)


def f32_divd_113_uo_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and UO."""
    return _rolling_corr_pearson(_safe_log(close), _uo(high, low, close), QDAYS)


def f32_divd_114_uo_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + UO HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _uo(high, low, close), QDAYS)


def f32_divd_115_uo_div_x_overbought_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish UO divergence AND UO > 70 — conjunction."""
    u = _uo(high, low, close)
    div = _shift_div_bearish_indicator(close, u, QDAYS)
    return (div * (u > 70).astype(float)).where(u.notna() & div.notna(), np.nan)


# ============================================================
# Bucket P — Multi-oscillator stacking & breadth (116-125)
# ============================================================

def f32_divd_116_bearish_div_breadth_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 5 oscillators (RSI/MACD-H/OBV/StochK/MFI) with bearish slope-div over 63d."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    return _bearish_div_flags_panel(close, panel, QDAYS, "slope").mean(axis=1)


def f32_divd_117_bearish_div_breadth_5osc_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same 5-osc breadth but over 252d window — secular bearish-divergence consensus."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    return _bearish_div_flags_panel(close, panel, YDAYS, "slope").mean(axis=1)


def f32_divd_118_bearish_div_stack_count_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count (not fraction) of 5 osc with bearish slope-div, 63d — integer 0..5."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    return _bearish_div_flags_panel(close, panel, QDAYS, "slope").sum(axis=1)


def f32_divd_119_hidden_bearish_breadth_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 5 osc showing HIDDEN bearish over 63d."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    return _bearish_div_flags_panel(close, panel, QDAYS, "hidden").mean(axis=1)


def f32_divd_120_bearish_div_breadth_3osc_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Short-horizon breadth: 3-osc panel (RSI/OBV/StochK) bearish slope-div over 21d — acute breadth."""
    panel = _oscillator_panel_short_3(open, high, low, close, volume)
    return _bearish_div_flags_panel(close, panel, MDAYS, "slope").mean(axis=1)


def f32_divd_121_bearish_div_at_overbought_breadth_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 5 osc where bearish div fires AND osc is in upper percentile (>=80th in 252d)."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    flags = _bearish_div_flags_panel(close, panel, QDAYS, "slope")
    cols = []
    for i, o in enumerate(panel):
        rk = _pct_rank(o, YDAYS)
        cols.append(((flags[f"o{i}"] == 1) & (rk >= 0.8)).astype(float).rename(f"c{i}"))
    return pd.concat(cols, axis=1).sum(axis=1)


def f32_divd_122_bearish_div_consensus_63d_AND_252d_intersect_5osc(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 5 osc where 63d AND 252d slope-div both flag bearish — short+long consensus."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    short_f = _bearish_div_flags_panel(close, panel, QDAYS, "slope")
    long_f = _bearish_div_flags_panel(close, panel, YDAYS, "slope")
    inter = (short_f.values * long_f.values)
    return pd.DataFrame(inter, index=close.index).sum(axis=1)


def f32_divd_123_composite_bearish_div_zscore_sum_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of z-scored slope-divergence magnitudes across 5-osc panel over 63d."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    return _bearish_div_mag_panel(close, panel, QDAYS).sum(axis=1)


def f32_divd_124_composite_bearish_div_zscore_sum_3osc_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of z-scored slope-divergence magnitudes for short-3-osc panel over 252d (secular)."""
    panel = _oscillator_panel_short_3(open, high, low, close, volume)
    return _bearish_div_mag_panel(close, panel, YDAYS).sum(axis=1)


def f32_divd_125_breadth_acceleration_change_over_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in 63d-breadth (Bucket P 116 series) — is breadth accelerating?"""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    breadth = _bearish_div_flags_panel(close, panel, QDAYS, "slope").mean(axis=1)
    return breadth - breadth.shift(MDAYS)


# ============================================================
# Bucket Q — Divergence persistence/age (126-130)
# ============================================================

def f32_divd_126_max_div_age_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum across 5 osc of bars-since-last-63d bearish shift-divergence."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    ages = [_div_persistence(close, o, QDAYS).rename(f"a{i}") for i, o in enumerate(panel)]
    return pd.concat(ages, axis=1).max(axis=1)


def f32_divd_127_median_div_age_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median across 5 osc of bars-since-last-63d bearish shift-divergence."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    ages = [_div_persistence(close, o, QDAYS).rename(f"a{i}") for i, o in enumerate(panel)]
    return pd.concat(ages, axis=1).median(axis=1)


def f32_divd_128_bars_since_first_bearish_div_in_252d_rsi(close: pd.Series) -> pd.Series:
    """Bars since the first RSI14 21d-bearish-shift divergence inside the trailing 252d (oldest active alert)."""
    rsi = _rsi_wilder(close, 14)
    flag = (_shift_div_bearish_indicator(close, rsi, MDAYS).fillna(0) > 0).astype(int)
    # for each bar, find the offset to the first 1 in the trailing 252 bars
    def _first(w):
        if np.all(w == 0):
            return np.nan
        return float(len(w) - 1 - int(np.argmax(w)))  # offset from end to first 1 (np.argmax returns first max)
    return flag.rolling(YDAYS, min_periods=MDAYS).apply(_first, raw=True)


def f32_divd_129_bars_since_last_rsi_div_count_increase(close: pd.Series) -> pd.Series:
    """Bars since the trailing 252d RSI div count last *increased* (i.e. since the last new event)."""
    rsi = _rsi_wilder(close, 14)
    cnt = _div_count_in_window(close, rsi, MDAYS, YDAYS)
    inc = (cnt.diff() > 0).astype(float)
    return _bars_since_true(inc)


def f32_divd_130_bearish_div_streak_length_consec_bars_rsi(close: pd.Series) -> pd.Series:
    """Length of the current consecutive-bar run where RSI14 63d slope-div sign is bearish (+1)."""
    rsi = _rsi_wilder(close, 14)
    flag = (_slope_div_sign(close, rsi, QDAYS) > 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


# ============================================================
# Bucket R — Divergence count metrics in window (131-135)
# ============================================================

def f32_divd_131_total_bearish_div_events_5osc_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total count of 21d-bearish-shift divergence events across 5 osc within trailing 252d."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    parts = []
    for i, o in enumerate(panel):
        parts.append(_div_count_in_window(close, o, MDAYS, YDAYS).rename(f"c{i}"))
    return pd.concat(parts, axis=1).sum(axis=1)


def f32_divd_132_rsi_macd_obv_joint_div_events_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where RSI, MACD-H, AND OBV ALL show 21d bearish shift-div simultaneously."""
    rsi_f = (_shift_div_bearish_indicator(close, _rsi_wilder(close, 14), MDAYS).fillna(0) > 0).astype(int)
    mh_f = (_shift_div_bearish_indicator(close, _macd_hist(close, 12, 26, 9), MDAYS).fillna(0) > 0).astype(int)
    obv_f = (_shift_div_bearish_indicator(close, _obv(close, volume), MDAYS).fillna(0) > 0).astype(int)
    triple = (rsi_f & mh_f & obv_f).astype(float)
    return triple.rolling(YDAYS, min_periods=QDAYS).sum()


def f32_divd_133_div_event_acceleration_21d_vs_63d_rsi(close: pd.Series) -> pd.Series:
    """RSI div count in last 21d vs last 63d (normalized) — short-term acceleration of div events."""
    rsi = _rsi_wilder(close, 14)
    flag = (_shift_div_bearish_indicator(close, rsi, MDAYS).fillna(0) > 0).astype(float)
    c21 = flag.rolling(MDAYS, min_periods=WDAYS).sum() / MDAYS
    c63 = flag.rolling(QDAYS, min_periods=MDAYS).sum() / QDAYS
    return c21 - c63


def f32_divd_134_div_event_dispersion_252d_5osc(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std-deviation across 5 osc of per-osc event-count over 252d (dispersion of divergence load)."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    parts = []
    for i, o in enumerate(panel):
        parts.append(_div_count_in_window(close, o, MDAYS, YDAYS).rename(f"c{i}"))
    return pd.concat(parts, axis=1).std(axis=1)


def f32_divd_135_percentile_rank_div_count_in_504d_rsi(close: pd.Series) -> pd.Series:
    """Percentile rank of trailing-252d-RSI-div-count within trailing 504d — relative regime."""
    rsi = _rsi_wilder(close, 14)
    cnt = _div_count_in_window(close, rsi, MDAYS, YDAYS)
    return _pct_rank(cnt, DDAYS_2Y)


# ============================================================
# Bucket S — Divergence magnitude composites (136-140)
# ============================================================

def f32_divd_136_max_div_magnitude_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum across 5 osc of 63d slope-divergence magnitude (z-scored)."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    return _bearish_div_mag_panel(close, panel, QDAYS).max(axis=1)


def f32_divd_137_mean_div_magnitude_breadth_weighted_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of slope-div magnitudes restricted to oscillators currently flagging bearish (breadth-weighted)."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    flags = _bearish_div_flags_panel(close, panel, QDAYS, "slope")
    mags = _bearish_div_mag_panel(close, panel, QDAYS)
    masked = mags.where(flags == 1, np.nan)
    return masked.mean(axis=1)


def f32_divd_138_min_div_magnitude_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Minimum across 5 osc of 63d slope-divergence magnitude — most-conservative."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    return _bearish_div_mag_panel(close, panel, QDAYS).min(axis=1)


def f32_divd_139_div_magnitude_dispersion_5osc_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std across 5 osc of 63d slope-divergence magnitude — dispersion of signal strength."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    return _bearish_div_mag_panel(close, panel, QDAYS).std(axis=1)


def f32_divd_140_cumulative_div_magnitude_252d_rsi(close: pd.Series) -> pd.Series:
    """Sum of 21d RSI shift-divergence magnitudes over trailing 252d — accumulated divergence load."""
    mag = _shift_div_bearish_magnitude(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    return mag.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket T — Divergence-of-divergence (141-145)
# Rate-of-change of divergence signals themselves
# ============================================================

def f32_divd_141_rsi_div_strength_slope_63d(close: pd.Series) -> pd.Series:
    """Slope (over 63d) of the absolute RSI slope-div-magnitude — is divergence intensifying?"""
    rsi = _rsi_wilder(close, 14)
    mag = _slope_div_magnitude(close, rsi, QDAYS).abs()
    return _rolling_slope(mag, QDAYS)


def f32_divd_142_rsi_div_strength_acceleration_21d(close: pd.Series) -> pd.Series:
    """Slope-of-slope of |RSI div magnitude| over 21d — short-term acceleration of strength."""
    rsi = _rsi_wilder(close, 14)
    mag = _slope_div_magnitude(close, rsi, QDAYS).abs()
    slope1 = _rolling_slope(mag, MDAYS)
    return _rolling_slope(slope1, MDAYS)


def f32_divd_143_breadth_slope_63d_5osc(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of 63d-breadth-of-bearish-divergence across 5 osc over a trailing 63d window."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    breadth = _bearish_div_flags_panel(close, panel, QDAYS, "slope").mean(axis=1)
    return _rolling_slope(breadth, QDAYS)


def f32_divd_144_magnitude_zscore_change_21d_rsi(close: pd.Series) -> pd.Series:
    """21d change in z-scored RSI slope-div magnitude — pulse of bearish-divergence z."""
    rsi = _rsi_wilder(close, 14)
    z = _rolling_zscore(_slope_div_magnitude(close, rsi, QDAYS), YDAYS)
    return z - z.shift(MDAYS)


def f32_divd_145_composite_div_score_slope_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope (63d) of the composite 5-osc z-sum-magnitude — composite-strength trend."""
    panel = _oscillator_panel_for_breadth(open, high, low, close, volume)
    comp = _bearish_div_mag_panel(close, panel, QDAYS).sum(axis=1)
    return _rolling_slope(comp, QDAYS)


# ============================================================
# Bucket U — Cross-oscillator + at-extreme composites (146-150)
# ============================================================

def f32_divd_146_rsi_macd_joint_bearish_div_indicator_63d(close: pd.Series) -> pd.Series:
    """+1 if BOTH RSI and MACD-line flag 63d-bearish slope-divergence at this bar."""
    a = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)
    b = (_slope_div_sign(close, _macd_line(close, 12, 26), QDAYS) > 0).astype(float)
    return (a * b).where(a.notna() & b.notna(), np.nan)


def f32_divd_147_triple_bearish_rsi_macd_obv_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 if RSI AND MACD-line AND OBV all flag 63d-bearish slope-divergence at this bar."""
    a = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)
    b = (_slope_div_sign(close, _macd_line(close, 12, 26), QDAYS) > 0).astype(float)
    c = (_slope_div_sign(close, _obv(close, volume), QDAYS) > 0).astype(float)
    return (a * b * c).where(a.notna() & b.notna() & c.notna(), np.nan)


def f32_divd_148_bearish_div_x_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 if RSI 63d-bearish slope-divergence AND close within 1% of trailing 252d high."""
    div = (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_max = (close >= rmax * 0.99).astype(float)
    return (div * near_max).where(div.notna() & rmax.notna(), np.nan)


def f32_divd_149_bearish_div_x_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 if RSI 252d-bearish slope-divergence AND close within 2% of trailing 1260d (5y) high."""
    div = (_slope_div_sign(close, _rsi_wilder(close, 14), YDAYS) > 0).astype(float)
    rmax = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    near_max = (close >= rmax * 0.98).astype(float)
    return (div * near_max).where(div.notna() & rmax.notna(), np.nan)


def f32_divd_150_weighted_topping_score_composite(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted topping score: 0.3*z(RSI-div-mag) + 0.3*z(MACD-line-div-mag) + 0.2*z(OBV-div-mag) + 0.2*close-pct-rank-1260d."""
    rsi_m = _rolling_zscore(_slope_div_magnitude(close, _rsi_wilder(close, 14), QDAYS), YDAYS)
    ml_m = _rolling_zscore(_slope_div_magnitude(close, _macd_line(close, 12, 26), QDAYS), YDAYS)
    obv_m = _rolling_zscore(_slope_div_magnitude(close, _obv(close, volume), QDAYS), YDAYS)
    px_rank = _pct_rank(close, DDAYS_5Y)
    return 0.3 * rsi_m + 0.3 * ml_m + 0.2 * obv_m + 0.2 * px_rank


# ============================================================
# REGISTRY
# ============================================================



def f32_divd_076_mfi_slope_div_sign_63d_d2(high, low, close, volume):
    return f32_divd_076_mfi_slope_div_sign_63d(high, low, close, volume).diff().diff()


def f32_divd_077_mfi_slope_div_sign_252d_d2(high, low, close, volume):
    return f32_divd_077_mfi_slope_div_sign_252d(high, low, close, volume).diff().diff()


def f32_divd_078_mfi_shift_div_indicator_63d_d2(high, low, close, volume):
    return f32_divd_078_mfi_shift_div_indicator_63d(high, low, close, volume).diff().diff()


def f32_divd_079_mfi_shift_div_magnitude_63d_d2(high, low, close, volume):
    return f32_divd_079_mfi_shift_div_magnitude_63d(high, low, close, volume).diff().diff()


def f32_divd_080_mfi_zscore_gap_63d_d2(high, low, close, volume):
    return f32_divd_080_mfi_zscore_gap_63d(high, low, close, volume).diff().diff()


def f32_divd_081_mfi_rolling_corr_price_63d_d2(high, low, close, volume):
    return f32_divd_081_mfi_rolling_corr_price_63d(high, low, close, volume).diff().diff()


def f32_divd_082_mfi_hidden_bearish_div_63d_d2(high, low, close, volume):
    return f32_divd_082_mfi_hidden_bearish_div_63d(high, low, close, volume).diff().diff()


def f32_divd_083_mfi_div_x_overbought_indicator_63d_d2(high, low, close, volume):
    return f32_divd_083_mfi_div_x_overbought_indicator_63d(high, low, close, volume).diff().diff()


def f32_divd_084_cci_slope_div_sign_63d_d2(high, low, close):
    return f32_divd_084_cci_slope_div_sign_63d(high, low, close).diff().diff()


def f32_divd_085_cci_shift_div_indicator_63d_d2(high, low, close):
    return f32_divd_085_cci_shift_div_indicator_63d(high, low, close).diff().diff()


def f32_divd_086_cci_zscore_gap_63d_d2(high, low, close):
    return f32_divd_086_cci_zscore_gap_63d(high, low, close).diff().diff()


def f32_divd_087_cci_rolling_corr_price_63d_d2(high, low, close):
    return f32_divd_087_cci_rolling_corr_price_63d(high, low, close).diff().diff()


def f32_divd_088_cci_hidden_bearish_div_63d_d2(high, low, close):
    return f32_divd_088_cci_hidden_bearish_div_63d(high, low, close).diff().diff()


def f32_divd_089_cci_div_x_extreme_indicator_63d_d2(high, low, close):
    return f32_divd_089_cci_div_x_extreme_indicator_63d(high, low, close).diff().diff()


def f32_divd_090_trix_slope_div_sign_63d_d2(close):
    return f32_divd_090_trix_slope_div_sign_63d(close).diff().diff()


def f32_divd_091_trix_shift_div_indicator_63d_d2(close):
    return f32_divd_091_trix_shift_div_indicator_63d(close).diff().diff()


def f32_divd_092_trix_zscore_gap_63d_d2(close):
    return f32_divd_092_trix_zscore_gap_63d(close).diff().diff()


def f32_divd_093_trix_rolling_corr_price_63d_d2(close):
    return f32_divd_093_trix_rolling_corr_price_63d(close).diff().diff()


def f32_divd_094_trix_hidden_bearish_div_63d_d2(close):
    return f32_divd_094_trix_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_095_trix_pos_to_neg_flip_at_high_indicator_d2(close):
    return f32_divd_095_trix_pos_to_neg_flip_at_high_indicator(close).diff().diff()


def f32_divd_096_tsi_slope_div_sign_63d_d2(close):
    return f32_divd_096_tsi_slope_div_sign_63d(close).diff().diff()


def f32_divd_097_tsi_shift_div_indicator_63d_d2(close):
    return f32_divd_097_tsi_shift_div_indicator_63d(close).diff().diff()


def f32_divd_098_tsi_zscore_gap_63d_d2(close):
    return f32_divd_098_tsi_zscore_gap_63d(close).diff().diff()


def f32_divd_099_tsi_rolling_corr_price_63d_d2(close):
    return f32_divd_099_tsi_rolling_corr_price_63d(close).diff().diff()


def f32_divd_100_tsi_hidden_bearish_div_63d_d2(close):
    return f32_divd_100_tsi_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_101_tsi_div_count_in_252d_d2(close):
    return f32_divd_101_tsi_div_count_in_252d(close).diff().diff()


def f32_divd_102_roc12_slope_div_sign_63d_d2(close):
    return f32_divd_102_roc12_slope_div_sign_63d(close).diff().diff()


def f32_divd_103_roc12_shift_div_indicator_63d_d2(close):
    return f32_divd_103_roc12_shift_div_indicator_63d(close).diff().diff()


def f32_divd_104_roc12_zscore_gap_63d_d2(close):
    return f32_divd_104_roc12_zscore_gap_63d(close).diff().diff()


def f32_divd_105_roc12_rolling_corr_price_63d_d2(close):
    return f32_divd_105_roc12_rolling_corr_price_63d(close).diff().diff()


def f32_divd_106_roc63_slope_div_sign_252d_d2(close):
    return f32_divd_106_roc63_slope_div_sign_252d(close).diff().diff()


def f32_divd_107_roc63_shift_div_indicator_252d_d2(close):
    return f32_divd_107_roc63_shift_div_indicator_252d(close).diff().diff()


def f32_divd_108_roc12_hidden_bearish_div_63d_d2(close):
    return f32_divd_108_roc12_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_109_roc12_div_count_in_252d_d2(close):
    return f32_divd_109_roc12_div_count_in_252d(close).diff().diff()


def f32_divd_110_uo_slope_div_sign_63d_d2(high, low, close):
    return f32_divd_110_uo_slope_div_sign_63d(high, low, close).diff().diff()


def f32_divd_111_uo_shift_div_indicator_63d_d2(high, low, close):
    return f32_divd_111_uo_shift_div_indicator_63d(high, low, close).diff().diff()


def f32_divd_112_uo_zscore_gap_63d_d2(high, low, close):
    return f32_divd_112_uo_zscore_gap_63d(high, low, close).diff().diff()


def f32_divd_113_uo_rolling_corr_price_63d_d2(high, low, close):
    return f32_divd_113_uo_rolling_corr_price_63d(high, low, close).diff().diff()


def f32_divd_114_uo_hidden_bearish_div_63d_d2(high, low, close):
    return f32_divd_114_uo_hidden_bearish_div_63d(high, low, close).diff().diff()


def f32_divd_115_uo_div_x_overbought_indicator_63d_d2(high, low, close):
    return f32_divd_115_uo_div_x_overbought_indicator_63d(high, low, close).diff().diff()


def f32_divd_116_bearish_div_breadth_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_116_bearish_div_breadth_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_117_bearish_div_breadth_5osc_252d_d2(open, high, low, close, volume):
    return f32_divd_117_bearish_div_breadth_5osc_252d(open, high, low, close, volume).diff().diff()


def f32_divd_118_bearish_div_stack_count_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_118_bearish_div_stack_count_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_119_hidden_bearish_breadth_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_119_hidden_bearish_breadth_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_120_bearish_div_breadth_3osc_21d_d2(open, high, low, close, volume):
    return f32_divd_120_bearish_div_breadth_3osc_21d(open, high, low, close, volume).diff().diff()


def f32_divd_121_bearish_div_at_overbought_breadth_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_121_bearish_div_at_overbought_breadth_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_122_bearish_div_consensus_63d_AND_252d_intersect_5osc_d2(open, high, low, close, volume):
    return f32_divd_122_bearish_div_consensus_63d_AND_252d_intersect_5osc(open, high, low, close, volume).diff().diff()


def f32_divd_123_composite_bearish_div_zscore_sum_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_123_composite_bearish_div_zscore_sum_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_124_composite_bearish_div_zscore_sum_3osc_252d_d2(open, high, low, close, volume):
    return f32_divd_124_composite_bearish_div_zscore_sum_3osc_252d(open, high, low, close, volume).diff().diff()


def f32_divd_125_breadth_acceleration_change_over_21d_d2(open, high, low, close, volume):
    return f32_divd_125_breadth_acceleration_change_over_21d(open, high, low, close, volume).diff().diff()


def f32_divd_126_max_div_age_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_126_max_div_age_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_127_median_div_age_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_127_median_div_age_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_128_bars_since_first_bearish_div_in_252d_rsi_d2(close):
    return f32_divd_128_bars_since_first_bearish_div_in_252d_rsi(close).diff().diff()


def f32_divd_129_bars_since_last_rsi_div_count_increase_d2(close):
    return f32_divd_129_bars_since_last_rsi_div_count_increase(close).diff().diff()


def f32_divd_130_bearish_div_streak_length_consec_bars_rsi_d2(close):
    return f32_divd_130_bearish_div_streak_length_consec_bars_rsi(close).diff().diff()


def f32_divd_131_total_bearish_div_events_5osc_252d_d2(open, high, low, close, volume):
    return f32_divd_131_total_bearish_div_events_5osc_252d(open, high, low, close, volume).diff().diff()


def f32_divd_132_rsi_macd_obv_joint_div_events_252d_d2(close, volume):
    return f32_divd_132_rsi_macd_obv_joint_div_events_252d(close, volume).diff().diff()


def f32_divd_133_div_event_acceleration_21d_vs_63d_rsi_d2(close):
    return f32_divd_133_div_event_acceleration_21d_vs_63d_rsi(close).diff().diff()


def f32_divd_134_div_event_dispersion_252d_5osc_d2(open, high, low, close, volume):
    return f32_divd_134_div_event_dispersion_252d_5osc(open, high, low, close, volume).diff().diff()


def f32_divd_135_percentile_rank_div_count_in_504d_rsi_d2(close):
    return f32_divd_135_percentile_rank_div_count_in_504d_rsi(close).diff().diff()


def f32_divd_136_max_div_magnitude_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_136_max_div_magnitude_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_137_mean_div_magnitude_breadth_weighted_63d_d2(open, high, low, close, volume):
    return f32_divd_137_mean_div_magnitude_breadth_weighted_63d(open, high, low, close, volume).diff().diff()


def f32_divd_138_min_div_magnitude_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_138_min_div_magnitude_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_139_div_magnitude_dispersion_5osc_63d_d2(open, high, low, close, volume):
    return f32_divd_139_div_magnitude_dispersion_5osc_63d(open, high, low, close, volume).diff().diff()


def f32_divd_140_cumulative_div_magnitude_252d_rsi_d2(close):
    return f32_divd_140_cumulative_div_magnitude_252d_rsi(close).diff().diff()


def f32_divd_141_rsi_div_strength_slope_63d_d2(close):
    return f32_divd_141_rsi_div_strength_slope_63d(close).diff().diff()


def f32_divd_142_rsi_div_strength_acceleration_21d_d2(close):
    return f32_divd_142_rsi_div_strength_acceleration_21d(close).diff().diff()


def f32_divd_143_breadth_slope_63d_5osc_d2(open, high, low, close, volume):
    return f32_divd_143_breadth_slope_63d_5osc(open, high, low, close, volume).diff().diff()


def f32_divd_144_magnitude_zscore_change_21d_rsi_d2(close):
    return f32_divd_144_magnitude_zscore_change_21d_rsi(close).diff().diff()


def f32_divd_145_composite_div_score_slope_63d_d2(open, high, low, close, volume):
    return f32_divd_145_composite_div_score_slope_63d(open, high, low, close, volume).diff().diff()


def f32_divd_146_rsi_macd_joint_bearish_div_indicator_63d_d2(close):
    return f32_divd_146_rsi_macd_joint_bearish_div_indicator_63d(close).diff().diff()


def f32_divd_147_triple_bearish_rsi_macd_obv_indicator_63d_d2(close, volume):
    return f32_divd_147_triple_bearish_rsi_macd_obv_indicator_63d(close, volume).diff().diff()


def f32_divd_148_bearish_div_x_252d_high_indicator_d2(close):
    return f32_divd_148_bearish_div_x_252d_high_indicator(close).diff().diff()


def f32_divd_149_bearish_div_x_1260d_high_indicator_d2(close):
    return f32_divd_149_bearish_div_x_1260d_high_indicator(close).diff().diff()


def f32_divd_150_weighted_topping_score_composite_d2(open, high, low, close, volume):
    return f32_divd_150_weighted_topping_score_composite(open, high, low, close, volume).diff().diff()


DIVERGENCE_DETECTION_D2_REGISTRY_076_150 = {
    "f32_divd_076_mfi_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_076_mfi_slope_div_sign_63d_d2},
    "f32_divd_077_mfi_slope_div_sign_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_077_mfi_slope_div_sign_252d_d2},
    "f32_divd_078_mfi_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_078_mfi_shift_div_indicator_63d_d2},
    "f32_divd_079_mfi_shift_div_magnitude_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_079_mfi_shift_div_magnitude_63d_d2},
    "f32_divd_080_mfi_zscore_gap_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_080_mfi_zscore_gap_63d_d2},
    "f32_divd_081_mfi_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_081_mfi_rolling_corr_price_63d_d2},
    "f32_divd_082_mfi_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_082_mfi_hidden_bearish_div_63d_d2},
    "f32_divd_083_mfi_div_x_overbought_indicator_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_083_mfi_div_x_overbought_indicator_63d_d2},
    "f32_divd_084_cci_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_084_cci_slope_div_sign_63d_d2},
    "f32_divd_085_cci_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_085_cci_shift_div_indicator_63d_d2},
    "f32_divd_086_cci_zscore_gap_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_086_cci_zscore_gap_63d_d2},
    "f32_divd_087_cci_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_087_cci_rolling_corr_price_63d_d2},
    "f32_divd_088_cci_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_088_cci_hidden_bearish_div_63d_d2},
    "f32_divd_089_cci_div_x_extreme_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_089_cci_div_x_extreme_indicator_63d_d2},
    "f32_divd_090_trix_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_090_trix_slope_div_sign_63d_d2},
    "f32_divd_091_trix_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_091_trix_shift_div_indicator_63d_d2},
    "f32_divd_092_trix_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_092_trix_zscore_gap_63d_d2},
    "f32_divd_093_trix_rolling_corr_price_63d_d2": {"inputs": ["close"], "func": f32_divd_093_trix_rolling_corr_price_63d_d2},
    "f32_divd_094_trix_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_094_trix_hidden_bearish_div_63d_d2},
    "f32_divd_095_trix_pos_to_neg_flip_at_high_indicator_d2": {"inputs": ["close"], "func": f32_divd_095_trix_pos_to_neg_flip_at_high_indicator_d2},
    "f32_divd_096_tsi_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_096_tsi_slope_div_sign_63d_d2},
    "f32_divd_097_tsi_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_097_tsi_shift_div_indicator_63d_d2},
    "f32_divd_098_tsi_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_098_tsi_zscore_gap_63d_d2},
    "f32_divd_099_tsi_rolling_corr_price_63d_d2": {"inputs": ["close"], "func": f32_divd_099_tsi_rolling_corr_price_63d_d2},
    "f32_divd_100_tsi_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_100_tsi_hidden_bearish_div_63d_d2},
    "f32_divd_101_tsi_div_count_in_252d_d2": {"inputs": ["close"], "func": f32_divd_101_tsi_div_count_in_252d_d2},
    "f32_divd_102_roc12_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_102_roc12_slope_div_sign_63d_d2},
    "f32_divd_103_roc12_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_103_roc12_shift_div_indicator_63d_d2},
    "f32_divd_104_roc12_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_104_roc12_zscore_gap_63d_d2},
    "f32_divd_105_roc12_rolling_corr_price_63d_d2": {"inputs": ["close"], "func": f32_divd_105_roc12_rolling_corr_price_63d_d2},
    "f32_divd_106_roc63_slope_div_sign_252d_d2": {"inputs": ["close"], "func": f32_divd_106_roc63_slope_div_sign_252d_d2},
    "f32_divd_107_roc63_shift_div_indicator_252d_d2": {"inputs": ["close"], "func": f32_divd_107_roc63_shift_div_indicator_252d_d2},
    "f32_divd_108_roc12_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_108_roc12_hidden_bearish_div_63d_d2},
    "f32_divd_109_roc12_div_count_in_252d_d2": {"inputs": ["close"], "func": f32_divd_109_roc12_div_count_in_252d_d2},
    "f32_divd_110_uo_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_110_uo_slope_div_sign_63d_d2},
    "f32_divd_111_uo_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_111_uo_shift_div_indicator_63d_d2},
    "f32_divd_112_uo_zscore_gap_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_112_uo_zscore_gap_63d_d2},
    "f32_divd_113_uo_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_113_uo_rolling_corr_price_63d_d2},
    "f32_divd_114_uo_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_114_uo_hidden_bearish_div_63d_d2},
    "f32_divd_115_uo_div_x_overbought_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_115_uo_div_x_overbought_indicator_63d_d2},
    "f32_divd_116_bearish_div_breadth_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_116_bearish_div_breadth_5osc_63d_d2},
    "f32_divd_117_bearish_div_breadth_5osc_252d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_117_bearish_div_breadth_5osc_252d_d2},
    "f32_divd_118_bearish_div_stack_count_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_118_bearish_div_stack_count_5osc_63d_d2},
    "f32_divd_119_hidden_bearish_breadth_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_119_hidden_bearish_breadth_5osc_63d_d2},
    "f32_divd_120_bearish_div_breadth_3osc_21d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_120_bearish_div_breadth_3osc_21d_d2},
    "f32_divd_121_bearish_div_at_overbought_breadth_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_121_bearish_div_at_overbought_breadth_5osc_63d_d2},
    "f32_divd_122_bearish_div_consensus_63d_AND_252d_intersect_5osc_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_122_bearish_div_consensus_63d_AND_252d_intersect_5osc_d2},
    "f32_divd_123_composite_bearish_div_zscore_sum_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_123_composite_bearish_div_zscore_sum_5osc_63d_d2},
    "f32_divd_124_composite_bearish_div_zscore_sum_3osc_252d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_124_composite_bearish_div_zscore_sum_3osc_252d_d2},
    "f32_divd_125_breadth_acceleration_change_over_21d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_125_breadth_acceleration_change_over_21d_d2},
    "f32_divd_126_max_div_age_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_126_max_div_age_5osc_63d_d2},
    "f32_divd_127_median_div_age_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_127_median_div_age_5osc_63d_d2},
    "f32_divd_128_bars_since_first_bearish_div_in_252d_rsi_d2": {"inputs": ["close"], "func": f32_divd_128_bars_since_first_bearish_div_in_252d_rsi_d2},
    "f32_divd_129_bars_since_last_rsi_div_count_increase_d2": {"inputs": ["close"], "func": f32_divd_129_bars_since_last_rsi_div_count_increase_d2},
    "f32_divd_130_bearish_div_streak_length_consec_bars_rsi_d2": {"inputs": ["close"], "func": f32_divd_130_bearish_div_streak_length_consec_bars_rsi_d2},
    "f32_divd_131_total_bearish_div_events_5osc_252d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_131_total_bearish_div_events_5osc_252d_d2},
    "f32_divd_132_rsi_macd_obv_joint_div_events_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_132_rsi_macd_obv_joint_div_events_252d_d2},
    "f32_divd_133_div_event_acceleration_21d_vs_63d_rsi_d2": {"inputs": ["close"], "func": f32_divd_133_div_event_acceleration_21d_vs_63d_rsi_d2},
    "f32_divd_134_div_event_dispersion_252d_5osc_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_134_div_event_dispersion_252d_5osc_d2},
    "f32_divd_135_percentile_rank_div_count_in_504d_rsi_d2": {"inputs": ["close"], "func": f32_divd_135_percentile_rank_div_count_in_504d_rsi_d2},
    "f32_divd_136_max_div_magnitude_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_136_max_div_magnitude_5osc_63d_d2},
    "f32_divd_137_mean_div_magnitude_breadth_weighted_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_137_mean_div_magnitude_breadth_weighted_63d_d2},
    "f32_divd_138_min_div_magnitude_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_138_min_div_magnitude_5osc_63d_d2},
    "f32_divd_139_div_magnitude_dispersion_5osc_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_139_div_magnitude_dispersion_5osc_63d_d2},
    "f32_divd_140_cumulative_div_magnitude_252d_rsi_d2": {"inputs": ["close"], "func": f32_divd_140_cumulative_div_magnitude_252d_rsi_d2},
    "f32_divd_141_rsi_div_strength_slope_63d_d2": {"inputs": ["close"], "func": f32_divd_141_rsi_div_strength_slope_63d_d2},
    "f32_divd_142_rsi_div_strength_acceleration_21d_d2": {"inputs": ["close"], "func": f32_divd_142_rsi_div_strength_acceleration_21d_d2},
    "f32_divd_143_breadth_slope_63d_5osc_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_143_breadth_slope_63d_5osc_d2},
    "f32_divd_144_magnitude_zscore_change_21d_rsi_d2": {"inputs": ["close"], "func": f32_divd_144_magnitude_zscore_change_21d_rsi_d2},
    "f32_divd_145_composite_div_score_slope_63d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_145_composite_div_score_slope_63d_d2},
    "f32_divd_146_rsi_macd_joint_bearish_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_146_rsi_macd_joint_bearish_div_indicator_63d_d2},
    "f32_divd_147_triple_bearish_rsi_macd_obv_indicator_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_147_triple_bearish_rsi_macd_obv_indicator_63d_d2},
    "f32_divd_148_bearish_div_x_252d_high_indicator_d2": {"inputs": ["close"], "func": f32_divd_148_bearish_div_x_252d_high_indicator_d2},
    "f32_divd_149_bearish_div_x_1260d_high_indicator_d2": {"inputs": ["close"], "func": f32_divd_149_bearish_div_x_1260d_high_indicator_d2},
    "f32_divd_150_weighted_topping_score_composite_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f32_divd_150_weighted_topping_score_composite_d2},
}
