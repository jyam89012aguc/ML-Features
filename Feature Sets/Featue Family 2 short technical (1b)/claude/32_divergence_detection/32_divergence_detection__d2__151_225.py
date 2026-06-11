"""divergence_detection d2 features 151-225 — Pipeline 1b-technical (gap-fill extension).

Extends the original 001-150 by adding bearish-divergence hypotheses against
oscillators not previously covered: Chaikin Oscillator, Klinger Volume Oscillator,
Force Index (Elder), Ease of Movement, Price Volume Trend, Negative/Positive Volume
Index, Volume Flow Indicator (Katsanos), Bollinger %B, Donchian-channel position,
Disparity Index, Percent Volume Oscillator, and ATR-extension divergence.

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


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


# ---------------------------- volume oscillator helpers ----------------------------

def _ad_line(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    return (mfm * volume).fillna(0).cumsum()


def _chaikin_osc(high, low, close, volume, fast=3, slow=10):
    """Chaikin Oscillator: EMA(fast) of A/D minus EMA(slow) of A/D."""
    ad = _ad_line(high, low, close, volume)
    return _ema(ad, fast) - _ema(ad, slow)


def _klinger_vol_osc(high, low, close, volume, fast=34, slow=55):
    """Klinger Volume Oscillator: EMA(fast) of volume-force minus EMA(slow) of volume-force.
    Volume force = volume × trend × |2 × (dm/cm - 1)| × 100 (simplified canonical form)."""
    hlc = (high + low + close) / 3.0
    trend = np.sign(hlc.diff()).fillna(0)
    dm = high - low
    cm = dm.rolling(2, min_periods=1).sum()  # rough approximation
    vf = volume * trend * (2.0 * _safe_div(dm, cm) - 1.0).abs() * 100.0
    return _ema(vf, fast) - _ema(vf, slow)


def _force_index(close, volume, n=13):
    """Elder's Force Index: EMA(n) of (close.diff() × volume)."""
    raw = close.diff() * volume
    return _ema(raw, n)


def _ease_of_movement(high, low, volume, n=14):
    """Ease of Movement: distance moved / box-ratio, then smoothed."""
    midpoint = (high + low) / 2.0
    distance = midpoint.diff()
    box_ratio = _safe_div(volume / 1e6, high - low)
    raw_emv = _safe_div(distance, box_ratio)
    return _sma(raw_emv, n)


def _pvt(close, volume):
    """Price Volume Trend: cumulative ((close-prevclose)/prevclose × volume)."""
    pc = close.shift(1)
    pct_chg = _safe_div(close - pc, pc)
    return (pct_chg * volume).fillna(0).cumsum()


def _nvi(close, volume):
    """Negative Volume Index: cumulative pct-change on bars where volume DECREASED."""
    pc = close.shift(1); pv = volume.shift(1)
    pct = _safe_div(close - pc, pc)
    decrease = (volume < pv)
    contrib = pct.where(decrease, 0).fillna(0)
    return 1000.0 * (1.0 + contrib).cumprod()


def _pvi(close, volume):
    """Positive Volume Index: cumulative pct-change on bars where volume INCREASED."""
    pc = close.shift(1); pv = volume.shift(1)
    pct = _safe_div(close - pc, pc)
    increase = (volume > pv)
    contrib = pct.where(increase, 0).fillna(0)
    return 1000.0 * (1.0 + contrib).cumprod()


def _vfi(high, low, close, volume, n=130):
    """Katsanos Volume Flow Indicator (simplified): typical-price log-return weighted by volume,
    filtered by a cutoff = 0.2 × std of log-returns over n. Smoothed by EMA(n)."""
    tp = (high + low + close) / 3.0
    inter = _safe_log(tp).diff()
    sd = inter.rolling(n, min_periods=max(n // 3, 2)).std()
    cutoff = 0.2 * sd
    signal = np.where(inter > cutoff, volume, np.where(inter < -cutoff, -volume, 0))
    sig = pd.Series(signal, index=close.index)
    vol_avg = volume.rolling(n, min_periods=max(n // 3, 2)).mean()
    return _ema(_safe_div(sig.rolling(n, min_periods=max(n // 3, 2)).sum(), vol_avg * n), 30)


def _bbands(close, n=20, k=2.0):
    """Bollinger Bands: SMA(n), upper = SMA + k*std, lower = SMA - k*std."""
    m = _sma(close, n)
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return m, m + k * sd, m - k * sd


def _bb_pct_b(close, n=20, k=2.0):
    """Bollinger %B: (close - lower) / (upper - lower)."""
    m, u, l = _bbands(close, n, k)
    return _safe_div(close - l, u - l)


def _donchian_pos(high, low, close, n=20):
    """Donchian channel position: (close - lower) / (upper - lower), upper=highest-high(n), lower=lowest-low(n)."""
    u = high.rolling(n, min_periods=max(n // 3, 2)).max()
    l = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return _safe_div(close - l, u - l)


def _disparity_index(close, n=14):
    """Disparity Index: 100 × (close / SMA(n) - 1) — distance above moving average in %."""
    return 100.0 * (_safe_div(close, _sma(close, n)) - 1.0)


def _pvo(volume, fast=12, slow=26):
    """Percent Volume Oscillator: 100 × (EMA(fast)-EMA(slow)) / EMA(slow) on volume."""
    e_fast = _ema(volume, fast); e_slow = _ema(volume, slow)
    return 100.0 * _safe_div(e_fast - e_slow, e_slow)


# ---------------------------- divergence-detection helpers ----------------------------

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    bear = ((ps > 0) & (osl < 0)).astype(float)
    bull = ((ps < 0) & (osl > 0)).astype(float)
    return (bear - bull).where(ps.notna() & osl.notna(), np.nan)


def _slope_div_magnitude(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    return _rolling_zscore(ps, n) - _rolling_zscore(osl, n)


def _shift_div_bearish_indicator(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    return ((price > pp) & (osc < op)).astype(float).where(pp.notna() & op.notna(), np.nan)


def _shift_div_bearish_magnitude(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    pxch = _safe_div(price - pp, pp.abs())
    oscz = _rolling_zscore(osc, max(k, 21))
    flag = (price > pp) & (osc < op)
    mag = (pxch - (oscz - oscz.shift(k))).where(flag, 0.0)
    return mag.where(pp.notna() & op.notna(), np.nan)


def _shift_div_hidden_bearish_indicator(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    return ((price < pp) & (osc > op)).astype(float).where(pp.notna() & op.notna(), np.nan)


def _rolling_corr_pearson(a, b, n):
    return a.rolling(n, min_periods=max(n // 3, 2)).corr(b)


def _zscore_gap(price, osc, n):
    return _rolling_zscore(_safe_log(price), n) - _rolling_zscore(osc, n)


def _div_persistence(price, osc, k):
    return _bars_since_true(_shift_div_bearish_indicator(price, osc, k))


def _div_count_in_window(price, osc, k, win):
    return _shift_div_bearish_indicator(price, osc, k).fillna(0).rolling(win, min_periods=max(win // 3, 2)).sum()


# ============================================================
# Bucket V — Chaikin Oscillator divergences (151-158)
# ============================================================

def f32_divd_151_chaikin_osc_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Chaikin Oscillator (3/10), 63d."""
    return _slope_div_sign(close, _chaikin_osc(high, low, close, volume, 3, 10), QDAYS)


def f32_divd_152_chaikin_osc_slope_div_sign_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Chaikin Oscillator, 252d (secular)."""
    return _slope_div_sign(close, _chaikin_osc(high, low, close, volume, 3, 10), YDAYS)


def f32_divd_153_chaikin_osc_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs Chaikin Oscillator, 63d lookback."""
    return _shift_div_bearish_indicator(close, _chaikin_osc(high, low, close, volume, 3, 10), QDAYS)


def f32_divd_154_chaikin_osc_shift_div_magnitude_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Magnitude of 63d bearish shift-divergence on Chaikin Oscillator."""
    return _shift_div_bearish_magnitude(close, _chaikin_osc(high, low, close, volume, 3, 10), QDAYS)


def f32_divd_155_chaikin_osc_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(Chaikin Osc,63)."""
    return _zscore_gap(close, _chaikin_osc(high, low, close, volume, 3, 10), QDAYS)


def f32_divd_156_chaikin_osc_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and Chaikin Oscillator."""
    return _rolling_corr_pearson(_safe_log(close), _chaikin_osc(high, low, close, volume, 3, 10), QDAYS)


def f32_divd_157_chaikin_osc_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Chaikin Osc HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _chaikin_osc(high, low, close, volume, 3, 10), QDAYS)


def f32_divd_158_chaikin_osc_div_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when Chaikin-Osc bearish slope-div AND close within 1% of 252d max."""
    div = (_slope_div_sign(close, _chaikin_osc(high, low, close, volume, 3, 10), QDAYS) > 0).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (div * near).where(div.notna() & near.notna(), np.nan)


# ============================================================
# Bucket W — Klinger Volume Oscillator divergences (159-166)
# ============================================================

def f32_divd_159_klinger_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Klinger Volume Oscillator (34/55), 63d."""
    return _slope_div_sign(close, _klinger_vol_osc(high, low, close, volume), QDAYS)


def f32_divd_160_klinger_slope_div_sign_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Klinger bearish slope-divergence over 252d (long-cycle volume failure)."""
    return _slope_div_sign(close, _klinger_vol_osc(high, low, close, volume), YDAYS)


def f32_divd_161_klinger_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on Klinger, 63d."""
    return _shift_div_bearish_indicator(close, _klinger_vol_osc(high, low, close, volume), QDAYS)


def f32_divd_162_klinger_shift_div_magnitude_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Magnitude of 63d bearish shift-divergence on Klinger."""
    return _shift_div_bearish_magnitude(close, _klinger_vol_osc(high, low, close, volume), QDAYS)


def f32_divd_163_klinger_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(Klinger,63)."""
    return _zscore_gap(close, _klinger_vol_osc(high, low, close, volume), QDAYS)


def f32_divd_164_klinger_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and Klinger."""
    return _rolling_corr_pearson(_safe_log(close), _klinger_vol_osc(high, low, close, volume), QDAYS)


def f32_divd_165_klinger_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Klinger HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _klinger_vol_osc(high, low, close, volume), QDAYS)


def f32_divd_166_klinger_div_count_in_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Klinger 21d bearish-shift divergences in trailing 252d."""
    return _div_count_in_window(close, _klinger_vol_osc(high, low, close, volume), MDAYS, YDAYS)


# ============================================================
# Bucket X — Force Index (Elder) divergences (167-174)
# ============================================================

def f32_divd_167_force_index_slope_div_sign_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Elder Force Index (13), 63d."""
    return _slope_div_sign(close, _force_index(close, volume, 13), QDAYS)


def f32_divd_168_force_index_slope_div_sign_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Force Index slope-divergence over 252d (long-cycle thrust failure)."""
    return _slope_div_sign(close, _force_index(close, volume, 13), YDAYS)


def f32_divd_169_force_index_shift_div_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on Force Index, 63d."""
    return _shift_div_bearish_indicator(close, _force_index(close, volume, 13), QDAYS)


def f32_divd_170_force_index_shift_div_magnitude_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Magnitude of 63d bearish shift-divergence on Force Index."""
    return _shift_div_bearish_magnitude(close, _force_index(close, volume, 13), QDAYS)


def f32_divd_171_force_index_zscore_gap_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(Force Index,63)."""
    return _zscore_gap(close, _force_index(close, volume, 13), QDAYS)


def f32_divd_172_force_index_rolling_corr_price_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and Force Index."""
    return _rolling_corr_pearson(_safe_log(close), _force_index(close, volume, 13), QDAYS)


def f32_divd_173_force_index_hidden_bearish_div_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Force Index HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _force_index(close, volume, 13), QDAYS)


def f32_divd_174_force_index_div_at_252d_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when Force Index bearish slope-div AND close near 252d max."""
    div = (_slope_div_sign(close, _force_index(close, volume, 13), QDAYS) > 0).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (div * near).where(div.notna() & near.notna(), np.nan)


# ============================================================
# Bucket Y — Ease of Movement divergences (175-181)
# ============================================================

def f32_divd_175_emv_slope_div_sign_63d(high: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Ease of Movement(14), 63d."""
    return _slope_div_sign(close, _ease_of_movement(high, low, volume, 14), QDAYS)


def f32_divd_176_emv_shift_div_indicator_63d(high: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on EMV, 63d."""
    return _shift_div_bearish_indicator(close, _ease_of_movement(high, low, volume, 14), QDAYS)


def f32_divd_177_emv_shift_div_magnitude_63d(high: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """Magnitude of 63d bearish shift-divergence on EMV."""
    return _shift_div_bearish_magnitude(close, _ease_of_movement(high, low, volume, 14), QDAYS)


def f32_divd_178_emv_zscore_gap_63d(high: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """z(log close,63) - z(EMV,63)."""
    return _zscore_gap(close, _ease_of_movement(high, low, volume, 14), QDAYS)


def f32_divd_179_emv_rolling_corr_price_63d(high: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and EMV."""
    return _rolling_corr_pearson(_safe_log(close), _ease_of_movement(high, low, volume, 14), QDAYS)


def f32_divd_180_emv_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + EMV HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _ease_of_movement(high, low, volume, 14), QDAYS)


def f32_divd_181_emv_div_count_in_252d(high: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    """Count of EMV 21d bearish-shift divergences in trailing 252d."""
    return _div_count_in_window(close, _ease_of_movement(high, low, volume, 14), MDAYS, YDAYS)


# ============================================================
# Bucket Z — PVT (Price Volume Trend) divergences (182-188)
# ============================================================

def f32_divd_182_pvt_slope_div_sign_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on PVT, 63d (distinct from OBV in weighting)."""
    return _slope_div_sign(close, _pvt(close, volume), QDAYS)


def f32_divd_183_pvt_slope_div_sign_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVT slope-divergence over 252d — secular weighted-accumulation failure."""
    return _slope_div_sign(close, _pvt(close, volume), YDAYS)


def f32_divd_184_pvt_shift_div_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on PVT, 63d."""
    return _shift_div_bearish_indicator(close, _pvt(close, volume), QDAYS)


def f32_divd_185_pvt_zscore_gap_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(PVT,63)."""
    return _zscore_gap(close, _pvt(close, volume), QDAYS)


def f32_divd_186_pvt_rolling_corr_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr of log-close and PVT — secular accumulation agreement."""
    return _rolling_corr_pearson(_safe_log(close), _pvt(close, volume), YDAYS)


def f32_divd_187_pvt_hidden_bearish_div_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + PVT HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _pvt(close, volume), QDAYS)


def f32_divd_188_pvt_div_persistence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last 63d PVT bearish divergence event."""
    return _div_persistence(close, _pvt(close, volume), QDAYS)


# ============================================================
# Bucket AA — NVI / PVI divergences (189-194)
# ============================================================

def f32_divd_189_nvi_slope_div_sign_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Negative Volume Index (smart money), 252d window."""
    return _slope_div_sign(close, _nvi(close, volume), YDAYS)


def f32_divd_190_nvi_shift_div_indicator_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on NVI, 252d (smart-money failure to confirm)."""
    return _shift_div_bearish_indicator(close, _nvi(close, volume), YDAYS)


def f32_divd_191_nvi_zscore_gap_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,252) - z(NVI,252)."""
    return _zscore_gap(close, _nvi(close, volume), YDAYS)


def f32_divd_192_pvi_slope_div_sign_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Positive Volume Index (uninformed money), 252d."""
    return _slope_div_sign(close, _pvi(close, volume), YDAYS)


def f32_divd_193_pvi_shift_div_indicator_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on PVI, 252d."""
    return _shift_div_bearish_indicator(close, _pvi(close, volume), YDAYS)


def f32_divd_194_nvi_pvi_disagreement_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign-disagreement: 1 if NVI 252d-slope ≠ PVI 252d-slope (smart-vs-uninformed divergence)."""
    sn = _rolling_slope(_nvi(close, volume), YDAYS)
    sp = _rolling_slope(_pvi(close, volume), YDAYS)
    return ((np.sign(sn) != np.sign(sp)) & sn.notna() & sp.notna()).astype(float).where(sn.notna() & sp.notna(), np.nan)


# ============================================================
# Bucket BB — VFI (Katsanos Volume Flow Indicator) divergences (195-200)
# ============================================================

def f32_divd_195_vfi_value(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume Flow Indicator value (Katsanos, n=130)."""
    return _vfi(high, low, close, volume, 130)


def f32_divd_196_vfi_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on VFI, 63d."""
    return _slope_div_sign(close, _vfi(high, low, close, volume, 130), QDAYS)


def f32_divd_197_vfi_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on VFI, 63d."""
    return _shift_div_bearish_indicator(close, _vfi(high, low, close, volume, 130), QDAYS)


def f32_divd_198_vfi_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(VFI,63)."""
    return _zscore_gap(close, _vfi(high, low, close, volume, 130), QDAYS)


def f32_divd_199_vfi_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and VFI."""
    return _rolling_corr_pearson(_safe_log(close), _vfi(high, low, close, volume, 130), QDAYS)


def f32_divd_200_vfi_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + VFI HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _vfi(high, low, close, volume, 130), QDAYS)


# ============================================================
# Bucket CC — Bollinger %B divergences (201-206)
# ============================================================

def f32_divd_201_pctB_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Bollinger %B(20,2), 63d."""
    return _slope_div_sign(close, _bb_pct_b(close, 20, 2.0), QDAYS)


def f32_divd_202_pctB_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on %B, 63d."""
    return _shift_div_bearish_indicator(close, _bb_pct_b(close, 20, 2.0), QDAYS)


def f32_divd_203_pctB_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(%B,63)."""
    return _zscore_gap(close, _bb_pct_b(close, 20, 2.0), QDAYS)


def f32_divd_204_pctB_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + %B HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _bb_pct_b(close, 20, 2.0), QDAYS)


def f32_divd_205_pctB_above_one_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing-252d bars with %B > 1 (close above upper Bollinger band — overextension density)."""
    return (_bb_pct_b(close, 20, 2.0) > 1.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f32_divd_206_pctB_div_at_band_break_indicator_63d(close: pd.Series) -> pd.Series:
    """+1 when %B > 1 (close above upper band) AND bearish slope-div on %B (band-touch + divergence)."""
    pb = _bb_pct_b(close, 20, 2.0)
    above = (pb > 1.0).astype(float)
    div = (_slope_div_sign(close, pb, QDAYS) > 0).astype(float)
    return (above * div).where(pb.notna() & div.notna(), np.nan)


# ============================================================
# Bucket DD — Donchian-position divergences (207-211)
# ============================================================

def f32_divd_207_donchian_pos_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Donchian-channel position (n=20), 63d."""
    return _slope_div_sign(close, _donchian_pos(high, low, close, 20), QDAYS)


def f32_divd_208_donchian_pos_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on Donchian-position, 63d."""
    return _shift_div_bearish_indicator(close, _donchian_pos(high, low, close, 20), QDAYS)


def f32_divd_209_donchian_pos_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Donchian-pos,63)."""
    return _zscore_gap(close, _donchian_pos(high, low, close, 20), QDAYS)


def f32_divd_210_donchian_pos_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Donchian-pos HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _donchian_pos(high, low, close, 20), QDAYS)


def f32_divd_211_donchian_pos_at_top_div_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when Donchian-pos >= 0.95 AND bearish slope-div on Donchian-pos (top-of-channel + divergence)."""
    dp = _donchian_pos(high, low, close, 20)
    at_top = (dp >= 0.95).astype(float)
    div = (_slope_div_sign(close, dp, QDAYS) > 0).astype(float)
    return (at_top * div).where(dp.notna() & div.notna(), np.nan)


# ============================================================
# Bucket EE — Disparity Index divergences (212-215)
# ============================================================

def f32_divd_212_disparity14_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Disparity Index(14), 63d."""
    return _slope_div_sign(close, _disparity_index(close, 14), QDAYS)


def f32_divd_213_disparity14_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on Disparity Index, 63d."""
    return _shift_div_bearish_indicator(close, _disparity_index(close, 14), QDAYS)


def f32_divd_214_disparity14_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Disparity Index,63)."""
    return _zscore_gap(close, _disparity_index(close, 14), QDAYS)


def f32_divd_215_disparity14_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Disparity Index HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _disparity_index(close, 14), QDAYS)


# ============================================================
# Bucket FF — PVO (Percent Volume Oscillator) divergences (216-219)
# ============================================================

def f32_divd_216_pvo_slope_div_sign_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Percent Volume Oscillator(12/26), 63d."""
    return _slope_div_sign(close, _pvo(volume, 12, 26), QDAYS)


def f32_divd_217_pvo_shift_div_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on PVO, 63d (price up + vol-momentum down)."""
    return _shift_div_bearish_indicator(close, _pvo(volume, 12, 26), QDAYS)


def f32_divd_218_pvo_zscore_gap_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(PVO,63) — price extension vs volume-momentum."""
    return _zscore_gap(close, _pvo(volume, 12, 26), QDAYS)


def f32_divd_219_pvo_rolling_corr_price_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and PVO — falling = volume not confirming."""
    return _rolling_corr_pearson(_safe_log(close), _pvo(volume, 12, 26), QDAYS)


# ============================================================
# Bucket GG — ATR-extension divergences (220-222)
# ============================================================

def f32_divd_220_atr_extension_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on ATR(21) — when price-rising + ATR-falling = vol-dryup at top."""
    return _slope_div_sign(close, _atr(high, low, close, MDAYS), QDAYS)


def f32_divd_221_atr_extension_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on ATR(21), 63d."""
    return _shift_div_bearish_indicator(close, _atr(high, low, close, MDAYS), QDAYS)


def f32_divd_222_atr_extension_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and ATR(21) — negative = vol-dryup-at-rising-price."""
    return _rolling_corr_pearson(_safe_log(close), _atr(high, low, close, MDAYS), QDAYS)


# ============================================================
# Bucket HH — Volume-divergence cross-confirmation breadth (223-225)
# ============================================================

def f32_divd_223_volume_divergence_breadth_5osc_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction (0..1) of 5 NEW volume oscillators (Chaikin-Osc/Klinger/Force/EMV/PVT) showing bearish slope-div over 63d."""
    panel = [
        _chaikin_osc(high, low, close, volume, 3, 10),
        _klinger_vol_osc(high, low, close, volume),
        _force_index(close, volume, 13),
        _ease_of_movement(high, low, volume, 14),
        _pvt(close, volume),
    ]
    flags = [(_slope_div_sign(close, o, QDAYS) > 0).astype(float).rename(f"o{i}") for i, o in enumerate(panel)]
    return pd.concat(flags, axis=1).mean(axis=1)


def f32_divd_224_volume_divergence_stack_count_5osc_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count (0..5) of 5 NEW volume oscillators showing bearish slope-div over 252d (secular consensus)."""
    panel = [
        _chaikin_osc(high, low, close, volume, 3, 10),
        _klinger_vol_osc(high, low, close, volume),
        _force_index(close, volume, 13),
        _ease_of_movement(high, low, volume, 14),
        _pvt(close, volume),
    ]
    flags = [(_slope_div_sign(close, o, YDAYS) > 0).astype(float).rename(f"o{i}") for i, o in enumerate(panel)]
    return pd.concat(flags, axis=1).sum(axis=1)


def f32_divd_225_volume_div_breadth_x_at_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when volume-div-breadth-5osc-63d > 0.6 AND close within 1% of 252d max."""
    breadth = f32_divd_223_volume_divergence_breadth_5osc_63d(high, low, close, volume)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((breadth > 0.6) & (near == 1)).astype(float).where(breadth.notna() & near.notna(), np.nan)


# ============================================================
# REGISTRY
# ============================================================



def f32_divd_151_chaikin_osc_slope_div_sign_63d_d2(high, low, close, volume):
    return f32_divd_151_chaikin_osc_slope_div_sign_63d(high, low, close, volume).diff().diff()


def f32_divd_152_chaikin_osc_slope_div_sign_252d_d2(high, low, close, volume):
    return f32_divd_152_chaikin_osc_slope_div_sign_252d(high, low, close, volume).diff().diff()


def f32_divd_153_chaikin_osc_shift_div_indicator_63d_d2(high, low, close, volume):
    return f32_divd_153_chaikin_osc_shift_div_indicator_63d(high, low, close, volume).diff().diff()


def f32_divd_154_chaikin_osc_shift_div_magnitude_63d_d2(high, low, close, volume):
    return f32_divd_154_chaikin_osc_shift_div_magnitude_63d(high, low, close, volume).diff().diff()


def f32_divd_155_chaikin_osc_zscore_gap_63d_d2(high, low, close, volume):
    return f32_divd_155_chaikin_osc_zscore_gap_63d(high, low, close, volume).diff().diff()


def f32_divd_156_chaikin_osc_rolling_corr_price_63d_d2(high, low, close, volume):
    return f32_divd_156_chaikin_osc_rolling_corr_price_63d(high, low, close, volume).diff().diff()


def f32_divd_157_chaikin_osc_hidden_bearish_div_63d_d2(high, low, close, volume):
    return f32_divd_157_chaikin_osc_hidden_bearish_div_63d(high, low, close, volume).diff().diff()


def f32_divd_158_chaikin_osc_div_at_252d_high_indicator_d2(high, low, close, volume):
    return f32_divd_158_chaikin_osc_div_at_252d_high_indicator(high, low, close, volume).diff().diff()


def f32_divd_159_klinger_slope_div_sign_63d_d2(high, low, close, volume):
    return f32_divd_159_klinger_slope_div_sign_63d(high, low, close, volume).diff().diff()


def f32_divd_160_klinger_slope_div_sign_252d_d2(high, low, close, volume):
    return f32_divd_160_klinger_slope_div_sign_252d(high, low, close, volume).diff().diff()


def f32_divd_161_klinger_shift_div_indicator_63d_d2(high, low, close, volume):
    return f32_divd_161_klinger_shift_div_indicator_63d(high, low, close, volume).diff().diff()


def f32_divd_162_klinger_shift_div_magnitude_63d_d2(high, low, close, volume):
    return f32_divd_162_klinger_shift_div_magnitude_63d(high, low, close, volume).diff().diff()


def f32_divd_163_klinger_zscore_gap_63d_d2(high, low, close, volume):
    return f32_divd_163_klinger_zscore_gap_63d(high, low, close, volume).diff().diff()


def f32_divd_164_klinger_rolling_corr_price_63d_d2(high, low, close, volume):
    return f32_divd_164_klinger_rolling_corr_price_63d(high, low, close, volume).diff().diff()


def f32_divd_165_klinger_hidden_bearish_div_63d_d2(high, low, close, volume):
    return f32_divd_165_klinger_hidden_bearish_div_63d(high, low, close, volume).diff().diff()


def f32_divd_166_klinger_div_count_in_252d_d2(high, low, close, volume):
    return f32_divd_166_klinger_div_count_in_252d(high, low, close, volume).diff().diff()


def f32_divd_167_force_index_slope_div_sign_63d_d2(close, volume):
    return f32_divd_167_force_index_slope_div_sign_63d(close, volume).diff().diff()


def f32_divd_168_force_index_slope_div_sign_252d_d2(close, volume):
    return f32_divd_168_force_index_slope_div_sign_252d(close, volume).diff().diff()


def f32_divd_169_force_index_shift_div_indicator_63d_d2(close, volume):
    return f32_divd_169_force_index_shift_div_indicator_63d(close, volume).diff().diff()


def f32_divd_170_force_index_shift_div_magnitude_63d_d2(close, volume):
    return f32_divd_170_force_index_shift_div_magnitude_63d(close, volume).diff().diff()


def f32_divd_171_force_index_zscore_gap_63d_d2(close, volume):
    return f32_divd_171_force_index_zscore_gap_63d(close, volume).diff().diff()


def f32_divd_172_force_index_rolling_corr_price_63d_d2(close, volume):
    return f32_divd_172_force_index_rolling_corr_price_63d(close, volume).diff().diff()


def f32_divd_173_force_index_hidden_bearish_div_63d_d2(close, volume):
    return f32_divd_173_force_index_hidden_bearish_div_63d(close, volume).diff().diff()


def f32_divd_174_force_index_div_at_252d_high_indicator_d2(close, volume):
    return f32_divd_174_force_index_div_at_252d_high_indicator(close, volume).diff().diff()


def f32_divd_175_emv_slope_div_sign_63d_d2(high, low, volume, close):
    return f32_divd_175_emv_slope_div_sign_63d(high, low, volume, close).diff().diff()


def f32_divd_176_emv_shift_div_indicator_63d_d2(high, low, volume, close):
    return f32_divd_176_emv_shift_div_indicator_63d(high, low, volume, close).diff().diff()


def f32_divd_177_emv_shift_div_magnitude_63d_d2(high, low, volume, close):
    return f32_divd_177_emv_shift_div_magnitude_63d(high, low, volume, close).diff().diff()


def f32_divd_178_emv_zscore_gap_63d_d2(high, low, volume, close):
    return f32_divd_178_emv_zscore_gap_63d(high, low, volume, close).diff().diff()


def f32_divd_179_emv_rolling_corr_price_63d_d2(high, low, volume, close):
    return f32_divd_179_emv_rolling_corr_price_63d(high, low, volume, close).diff().diff()


def f32_divd_180_emv_hidden_bearish_div_63d_d2(high, low, volume, close):
    return f32_divd_180_emv_hidden_bearish_div_63d(high, low, volume, close).diff().diff()


def f32_divd_181_emv_div_count_in_252d_d2(high, low, volume, close):
    return f32_divd_181_emv_div_count_in_252d(high, low, volume, close).diff().diff()


def f32_divd_182_pvt_slope_div_sign_63d_d2(close, volume):
    return f32_divd_182_pvt_slope_div_sign_63d(close, volume).diff().diff()


def f32_divd_183_pvt_slope_div_sign_252d_d2(close, volume):
    return f32_divd_183_pvt_slope_div_sign_252d(close, volume).diff().diff()


def f32_divd_184_pvt_shift_div_indicator_63d_d2(close, volume):
    return f32_divd_184_pvt_shift_div_indicator_63d(close, volume).diff().diff()


def f32_divd_185_pvt_zscore_gap_63d_d2(close, volume):
    return f32_divd_185_pvt_zscore_gap_63d(close, volume).diff().diff()


def f32_divd_186_pvt_rolling_corr_price_252d_d2(close, volume):
    return f32_divd_186_pvt_rolling_corr_price_252d(close, volume).diff().diff()


def f32_divd_187_pvt_hidden_bearish_div_63d_d2(close, volume):
    return f32_divd_187_pvt_hidden_bearish_div_63d(close, volume).diff().diff()


def f32_divd_188_pvt_div_persistence_63d_d2(close, volume):
    return f32_divd_188_pvt_div_persistence_63d(close, volume).diff().diff()


def f32_divd_189_nvi_slope_div_sign_252d_d2(close, volume):
    return f32_divd_189_nvi_slope_div_sign_252d(close, volume).diff().diff()


def f32_divd_190_nvi_shift_div_indicator_252d_d2(close, volume):
    return f32_divd_190_nvi_shift_div_indicator_252d(close, volume).diff().diff()


def f32_divd_191_nvi_zscore_gap_252d_d2(close, volume):
    return f32_divd_191_nvi_zscore_gap_252d(close, volume).diff().diff()


def f32_divd_192_pvi_slope_div_sign_252d_d2(close, volume):
    return f32_divd_192_pvi_slope_div_sign_252d(close, volume).diff().diff()


def f32_divd_193_pvi_shift_div_indicator_252d_d2(close, volume):
    return f32_divd_193_pvi_shift_div_indicator_252d(close, volume).diff().diff()


def f32_divd_194_nvi_pvi_disagreement_252d_d2(close, volume):
    return f32_divd_194_nvi_pvi_disagreement_252d(close, volume).diff().diff()


def f32_divd_195_vfi_value_d2(high, low, close, volume):
    return f32_divd_195_vfi_value(high, low, close, volume).diff().diff()


def f32_divd_196_vfi_slope_div_sign_63d_d2(high, low, close, volume):
    return f32_divd_196_vfi_slope_div_sign_63d(high, low, close, volume).diff().diff()


def f32_divd_197_vfi_shift_div_indicator_63d_d2(high, low, close, volume):
    return f32_divd_197_vfi_shift_div_indicator_63d(high, low, close, volume).diff().diff()


def f32_divd_198_vfi_zscore_gap_63d_d2(high, low, close, volume):
    return f32_divd_198_vfi_zscore_gap_63d(high, low, close, volume).diff().diff()


def f32_divd_199_vfi_rolling_corr_price_63d_d2(high, low, close, volume):
    return f32_divd_199_vfi_rolling_corr_price_63d(high, low, close, volume).diff().diff()


def f32_divd_200_vfi_hidden_bearish_div_63d_d2(high, low, close, volume):
    return f32_divd_200_vfi_hidden_bearish_div_63d(high, low, close, volume).diff().diff()


def f32_divd_201_pctB_slope_div_sign_63d_d2(close):
    return f32_divd_201_pctB_slope_div_sign_63d(close).diff().diff()


def f32_divd_202_pctB_shift_div_indicator_63d_d2(close):
    return f32_divd_202_pctB_shift_div_indicator_63d(close).diff().diff()


def f32_divd_203_pctB_zscore_gap_63d_d2(close):
    return f32_divd_203_pctB_zscore_gap_63d(close).diff().diff()


def f32_divd_204_pctB_hidden_bearish_div_63d_d2(close):
    return f32_divd_204_pctB_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_205_pctB_above_one_count_252d_d2(close):
    return f32_divd_205_pctB_above_one_count_252d(close).diff().diff()


def f32_divd_206_pctB_div_at_band_break_indicator_63d_d2(close):
    return f32_divd_206_pctB_div_at_band_break_indicator_63d(close).diff().diff()


def f32_divd_207_donchian_pos_slope_div_sign_63d_d2(high, low, close):
    return f32_divd_207_donchian_pos_slope_div_sign_63d(high, low, close).diff().diff()


def f32_divd_208_donchian_pos_shift_div_indicator_63d_d2(high, low, close):
    return f32_divd_208_donchian_pos_shift_div_indicator_63d(high, low, close).diff().diff()


def f32_divd_209_donchian_pos_zscore_gap_63d_d2(high, low, close):
    return f32_divd_209_donchian_pos_zscore_gap_63d(high, low, close).diff().diff()


def f32_divd_210_donchian_pos_hidden_bearish_div_63d_d2(high, low, close):
    return f32_divd_210_donchian_pos_hidden_bearish_div_63d(high, low, close).diff().diff()


def f32_divd_211_donchian_pos_at_top_div_indicator_d2(high, low, close):
    return f32_divd_211_donchian_pos_at_top_div_indicator(high, low, close).diff().diff()


def f32_divd_212_disparity14_slope_div_sign_63d_d2(close):
    return f32_divd_212_disparity14_slope_div_sign_63d(close).diff().diff()


def f32_divd_213_disparity14_shift_div_indicator_63d_d2(close):
    return f32_divd_213_disparity14_shift_div_indicator_63d(close).diff().diff()


def f32_divd_214_disparity14_zscore_gap_63d_d2(close):
    return f32_divd_214_disparity14_zscore_gap_63d(close).diff().diff()


def f32_divd_215_disparity14_hidden_bearish_div_63d_d2(close):
    return f32_divd_215_disparity14_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_216_pvo_slope_div_sign_63d_d2(close, volume):
    return f32_divd_216_pvo_slope_div_sign_63d(close, volume).diff().diff()


def f32_divd_217_pvo_shift_div_indicator_63d_d2(close, volume):
    return f32_divd_217_pvo_shift_div_indicator_63d(close, volume).diff().diff()


def f32_divd_218_pvo_zscore_gap_63d_d2(close, volume):
    return f32_divd_218_pvo_zscore_gap_63d(close, volume).diff().diff()


def f32_divd_219_pvo_rolling_corr_price_63d_d2(close, volume):
    return f32_divd_219_pvo_rolling_corr_price_63d(close, volume).diff().diff()


def f32_divd_220_atr_extension_slope_div_sign_63d_d2(high, low, close):
    return f32_divd_220_atr_extension_slope_div_sign_63d(high, low, close).diff().diff()


def f32_divd_221_atr_extension_shift_div_indicator_63d_d2(high, low, close):
    return f32_divd_221_atr_extension_shift_div_indicator_63d(high, low, close).diff().diff()


def f32_divd_222_atr_extension_corr_price_63d_d2(high, low, close):
    return f32_divd_222_atr_extension_corr_price_63d(high, low, close).diff().diff()


def f32_divd_223_volume_divergence_breadth_5osc_63d_d2(high, low, close, volume):
    return f32_divd_223_volume_divergence_breadth_5osc_63d(high, low, close, volume).diff().diff()


def f32_divd_224_volume_divergence_stack_count_5osc_252d_d2(high, low, close, volume):
    return f32_divd_224_volume_divergence_stack_count_5osc_252d(high, low, close, volume).diff().diff()


def f32_divd_225_volume_div_breadth_x_at_high_indicator_d2(high, low, close, volume):
    return f32_divd_225_volume_div_breadth_x_at_high_indicator(high, low, close, volume).diff().diff()


DIVERGENCE_DETECTION_D2_REGISTRY_151_225 = {
    "f32_divd_151_chaikin_osc_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_151_chaikin_osc_slope_div_sign_63d_d2},
    "f32_divd_152_chaikin_osc_slope_div_sign_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_152_chaikin_osc_slope_div_sign_252d_d2},
    "f32_divd_153_chaikin_osc_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_153_chaikin_osc_shift_div_indicator_63d_d2},
    "f32_divd_154_chaikin_osc_shift_div_magnitude_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_154_chaikin_osc_shift_div_magnitude_63d_d2},
    "f32_divd_155_chaikin_osc_zscore_gap_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_155_chaikin_osc_zscore_gap_63d_d2},
    "f32_divd_156_chaikin_osc_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_156_chaikin_osc_rolling_corr_price_63d_d2},
    "f32_divd_157_chaikin_osc_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_157_chaikin_osc_hidden_bearish_div_63d_d2},
    "f32_divd_158_chaikin_osc_div_at_252d_high_indicator_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_158_chaikin_osc_div_at_252d_high_indicator_d2},
    "f32_divd_159_klinger_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_159_klinger_slope_div_sign_63d_d2},
    "f32_divd_160_klinger_slope_div_sign_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_160_klinger_slope_div_sign_252d_d2},
    "f32_divd_161_klinger_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_161_klinger_shift_div_indicator_63d_d2},
    "f32_divd_162_klinger_shift_div_magnitude_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_162_klinger_shift_div_magnitude_63d_d2},
    "f32_divd_163_klinger_zscore_gap_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_163_klinger_zscore_gap_63d_d2},
    "f32_divd_164_klinger_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_164_klinger_rolling_corr_price_63d_d2},
    "f32_divd_165_klinger_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_165_klinger_hidden_bearish_div_63d_d2},
    "f32_divd_166_klinger_div_count_in_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_166_klinger_div_count_in_252d_d2},
    "f32_divd_167_force_index_slope_div_sign_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_167_force_index_slope_div_sign_63d_d2},
    "f32_divd_168_force_index_slope_div_sign_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_168_force_index_slope_div_sign_252d_d2},
    "f32_divd_169_force_index_shift_div_indicator_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_169_force_index_shift_div_indicator_63d_d2},
    "f32_divd_170_force_index_shift_div_magnitude_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_170_force_index_shift_div_magnitude_63d_d2},
    "f32_divd_171_force_index_zscore_gap_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_171_force_index_zscore_gap_63d_d2},
    "f32_divd_172_force_index_rolling_corr_price_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_172_force_index_rolling_corr_price_63d_d2},
    "f32_divd_173_force_index_hidden_bearish_div_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_173_force_index_hidden_bearish_div_63d_d2},
    "f32_divd_174_force_index_div_at_252d_high_indicator_d2": {"inputs": ["close", "volume"], "func": f32_divd_174_force_index_div_at_252d_high_indicator_d2},
    "f32_divd_175_emv_slope_div_sign_63d_d2": {"inputs": ["high", "low", "volume", "close"], "func": f32_divd_175_emv_slope_div_sign_63d_d2},
    "f32_divd_176_emv_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "volume", "close"], "func": f32_divd_176_emv_shift_div_indicator_63d_d2},
    "f32_divd_177_emv_shift_div_magnitude_63d_d2": {"inputs": ["high", "low", "volume", "close"], "func": f32_divd_177_emv_shift_div_magnitude_63d_d2},
    "f32_divd_178_emv_zscore_gap_63d_d2": {"inputs": ["high", "low", "volume", "close"], "func": f32_divd_178_emv_zscore_gap_63d_d2},
    "f32_divd_179_emv_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "volume", "close"], "func": f32_divd_179_emv_rolling_corr_price_63d_d2},
    "f32_divd_180_emv_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "volume", "close"], "func": f32_divd_180_emv_hidden_bearish_div_63d_d2},
    "f32_divd_181_emv_div_count_in_252d_d2": {"inputs": ["high", "low", "volume", "close"], "func": f32_divd_181_emv_div_count_in_252d_d2},
    "f32_divd_182_pvt_slope_div_sign_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_182_pvt_slope_div_sign_63d_d2},
    "f32_divd_183_pvt_slope_div_sign_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_183_pvt_slope_div_sign_252d_d2},
    "f32_divd_184_pvt_shift_div_indicator_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_184_pvt_shift_div_indicator_63d_d2},
    "f32_divd_185_pvt_zscore_gap_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_185_pvt_zscore_gap_63d_d2},
    "f32_divd_186_pvt_rolling_corr_price_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_186_pvt_rolling_corr_price_252d_d2},
    "f32_divd_187_pvt_hidden_bearish_div_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_187_pvt_hidden_bearish_div_63d_d2},
    "f32_divd_188_pvt_div_persistence_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_188_pvt_div_persistence_63d_d2},
    "f32_divd_189_nvi_slope_div_sign_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_189_nvi_slope_div_sign_252d_d2},
    "f32_divd_190_nvi_shift_div_indicator_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_190_nvi_shift_div_indicator_252d_d2},
    "f32_divd_191_nvi_zscore_gap_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_191_nvi_zscore_gap_252d_d2},
    "f32_divd_192_pvi_slope_div_sign_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_192_pvi_slope_div_sign_252d_d2},
    "f32_divd_193_pvi_shift_div_indicator_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_193_pvi_shift_div_indicator_252d_d2},
    "f32_divd_194_nvi_pvi_disagreement_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_194_nvi_pvi_disagreement_252d_d2},
    "f32_divd_195_vfi_value_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_195_vfi_value_d2},
    "f32_divd_196_vfi_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_196_vfi_slope_div_sign_63d_d2},
    "f32_divd_197_vfi_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_197_vfi_shift_div_indicator_63d_d2},
    "f32_divd_198_vfi_zscore_gap_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_198_vfi_zscore_gap_63d_d2},
    "f32_divd_199_vfi_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_199_vfi_rolling_corr_price_63d_d2},
    "f32_divd_200_vfi_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_200_vfi_hidden_bearish_div_63d_d2},
    "f32_divd_201_pctB_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_201_pctB_slope_div_sign_63d_d2},
    "f32_divd_202_pctB_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_202_pctB_shift_div_indicator_63d_d2},
    "f32_divd_203_pctB_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_203_pctB_zscore_gap_63d_d2},
    "f32_divd_204_pctB_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_204_pctB_hidden_bearish_div_63d_d2},
    "f32_divd_205_pctB_above_one_count_252d_d2": {"inputs": ["close"], "func": f32_divd_205_pctB_above_one_count_252d_d2},
    "f32_divd_206_pctB_div_at_band_break_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_206_pctB_div_at_band_break_indicator_63d_d2},
    "f32_divd_207_donchian_pos_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_207_donchian_pos_slope_div_sign_63d_d2},
    "f32_divd_208_donchian_pos_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_208_donchian_pos_shift_div_indicator_63d_d2},
    "f32_divd_209_donchian_pos_zscore_gap_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_209_donchian_pos_zscore_gap_63d_d2},
    "f32_divd_210_donchian_pos_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_210_donchian_pos_hidden_bearish_div_63d_d2},
    "f32_divd_211_donchian_pos_at_top_div_indicator_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_211_donchian_pos_at_top_div_indicator_d2},
    "f32_divd_212_disparity14_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_212_disparity14_slope_div_sign_63d_d2},
    "f32_divd_213_disparity14_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_213_disparity14_shift_div_indicator_63d_d2},
    "f32_divd_214_disparity14_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_214_disparity14_zscore_gap_63d_d2},
    "f32_divd_215_disparity14_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_215_disparity14_hidden_bearish_div_63d_d2},
    "f32_divd_216_pvo_slope_div_sign_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_216_pvo_slope_div_sign_63d_d2},
    "f32_divd_217_pvo_shift_div_indicator_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_217_pvo_shift_div_indicator_63d_d2},
    "f32_divd_218_pvo_zscore_gap_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_218_pvo_zscore_gap_63d_d2},
    "f32_divd_219_pvo_rolling_corr_price_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_219_pvo_rolling_corr_price_63d_d2},
    "f32_divd_220_atr_extension_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_220_atr_extension_slope_div_sign_63d_d2},
    "f32_divd_221_atr_extension_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_221_atr_extension_shift_div_indicator_63d_d2},
    "f32_divd_222_atr_extension_corr_price_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_222_atr_extension_corr_price_63d_d2},
    "f32_divd_223_volume_divergence_breadth_5osc_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_223_volume_divergence_breadth_5osc_63d_d2},
    "f32_divd_224_volume_divergence_stack_count_5osc_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_224_volume_divergence_stack_count_5osc_252d_d2},
    "f32_divd_225_volume_div_breadth_x_at_high_indicator_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_225_volume_div_breadth_x_at_high_indicator_d2},
}
