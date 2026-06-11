"""divergence_detection d2 features 001-075 — Pipeline 1b-technical.

150 distinct bearish-divergence hypotheses across this file and __base__076_150.py.
Each base feature pairs a momentum/volume/volatility oscillator with a distinct
divergence-detection methodology: slope-based, two-point shift, rolling-Pearson,
z-score gap, percentile-rank gap, hidden-bearish, persistence/age, count-in-window,
divergence-x-overbought conjunction.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
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


def _ad_line(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    return (mfm * volume).fillna(0).cumsum()


def _stoch_k(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)


def _stoch_rsi(close, n=14):
    rsi = _rsi_wilder(close, n)
    mn = rsi.rolling(n, min_periods=max(n // 3, 2)).min()
    mx = rsi.rolling(n, min_periods=max(n // 3, 2)).max()
    return _safe_div(rsi - mn, mx - mn)


def _williams_r(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return -100.0 * _safe_div(hh - close, hh - ll)


def _cmf(high, low, close, volume, n=20):
    rng = (high - low).replace(0, np.nan)
    mfm = ((close - low) - (high - close)) / rng
    mfv = (mfm * volume).fillna(0)
    return _safe_div(mfv.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     volume.rolling(n, min_periods=max(n // 3, 2)).sum())


# ---------------------------- divergence-detection helpers ----------------------------

def _slope_div_sign(price, osc, n):
    """+1 = bearish (price slope > 0 & osc slope < 0); -1 = bullish; 0 otherwise."""
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    bear = ((ps > 0) & (osl < 0)).astype(float)
    bull = ((ps < 0) & (osl > 0)).astype(float)
    out = bear - bull
    return out.where(ps.notna() & osl.notna(), np.nan)


def _slope_div_magnitude(price, osc, n):
    """Z-scored slope gap: positive when price rising faster than osc (bearish-leaning)."""
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    psz = _rolling_zscore(ps, n)
    osz = _rolling_zscore(osl, n)
    return psz - osz


def _shift_div_bearish_indicator(price, osc, k):
    """+1 if price[t] > price[t-k] AND osc[t] < osc[t-k] (classic bearish)."""
    pp = price.shift(k); op = osc.shift(k)
    flag = ((price > pp) & (osc < op))
    return flag.astype(float).where(pp.notna() & op.notna(), np.nan)


def _shift_div_bearish_magnitude(price, osc, k):
    """Signed magnitude (px-pct-change minus osc-zscore-change); 0 outside bearish-divergence regime."""
    pp = price.shift(k); op = osc.shift(k)
    pxch = _safe_div(price - pp, pp.abs())
    oscz = _rolling_zscore(osc, max(k, 21))
    oscz_pp = oscz.shift(k)
    flag = (price > pp) & (osc < op)
    mag = (pxch - (oscz - oscz_pp)).where(flag, 0.0)
    return mag.where(pp.notna() & op.notna(), np.nan)


def _shift_div_hidden_bearish_indicator(price, osc, k):
    """+1 if price[t] < price[t-k] AND osc[t] > osc[t-k] (hidden bearish)."""
    pp = price.shift(k); op = osc.shift(k)
    flag = ((price < pp) & (osc > op))
    return flag.astype(float).where(pp.notna() & op.notna(), np.nan)


def _rolling_corr_pearson(a, b, n):
    return a.rolling(n, min_periods=max(n // 3, 2)).corr(b)


def _zscore_gap(price, osc, n):
    """z(log price, n) - z(osc, n). Positive = price extended relative to osc."""
    return _rolling_zscore(_safe_log(price), n) - _rolling_zscore(osc, n)


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _pct_rank_gap(price, osc, n):
    return _pct_rank(price, n) - _pct_rank(osc, n)


def _bars_since_true(flag):
    """For boolean/0-1 series, returns bars-since-last-True (NaN before any True event)."""
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


def _div_persistence(price, osc, k):
    """Bars since last bearish shift-divergence event (k-bar lookback)."""
    flag = _shift_div_bearish_indicator(price, osc, k)
    return _bars_since_true(flag)


def _div_count_in_window(price, osc, k, win):
    """Count of bearish shift-divergence events within trailing `win` bars (k-bar lookback)."""
    flag = _shift_div_bearish_indicator(price, osc, k).fillna(0)
    return flag.rolling(win, min_periods=max(win // 3, 2)).sum()


# ============================================================
# Bucket A — RSI(14) divergences (001-015)
# Distinct methods: slope-sign, slope-mag, shift-indicator, shift-magnitude,
# correlation, z-score gap, pct-rank gap, hidden-bearish, persistence, count,
# divergence-x-overbought conjunction.
# ============================================================

def f32_divd_001_rsi14_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Sign-of-slope-mismatch bearish divergence on RSI(14), 63d window."""
    return _slope_div_sign(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_002_rsi14_slope_div_sign_252d(close: pd.Series) -> pd.Series:
    """Sign-of-slope-mismatch bearish divergence on RSI(14), 252d window (secular)."""
    return _slope_div_sign(close, _rsi_wilder(close, 14), YDAYS)


def f32_divd_003_rsi14_slope_div_magnitude_63d(close: pd.Series) -> pd.Series:
    """Z-scored slope gap (price vs RSI14) over 63d — continuous bearish strength."""
    return _slope_div_magnitude(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_004_rsi14_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence: price up over 63d AND RSI14 down."""
    return _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_005_rsi14_shift_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence over 252d (secular regime change indicator)."""
    return _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), YDAYS)


def f32_divd_006_rsi14_shift_div_magnitude_63d(close: pd.Series) -> pd.Series:
    """Magnitude of 63d two-point bearish divergence (signed continuous)."""
    return _shift_div_bearish_magnitude(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_007_rsi14_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d Pearson corr of log-close and RSI14. Falling/negative = divergent."""
    return _rolling_corr_pearson(_safe_log(close), _rsi_wilder(close, 14), QDAYS)


def f32_divd_008_rsi14_rolling_corr_price_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d Pearson corr — secular price-RSI agreement."""
    return _rolling_corr_pearson(_safe_log(close), _rsi_wilder(close, 14), YDAYS)


def f32_divd_009_rsi14_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(RSI14,63). Positive = price extended vs momentum."""
    return _zscore_gap(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_010_rsi14_zscore_gap_252d(close: pd.Series) -> pd.Series:
    """z(log close,252) - z(RSI14,252) — annual regime divergence."""
    return _zscore_gap(close, _rsi_wilder(close, 14), YDAYS)


def f32_divd_011_rsi14_pct_rank_gap_63d(close: pd.Series) -> pd.Series:
    """Percentile-rank gap (close vs RSI14) over 63d — non-parametric divergence."""
    return _pct_rank_gap(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_012_rsi14_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish divergence: price LH + RSI14 HH over 63d — trend-continuation top tell."""
    return _shift_div_hidden_bearish_indicator(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_013_rsi14_div_persistence_63d(close: pd.Series) -> pd.Series:
    """Bars since last 63d-RSI14 bearish divergence event — age of the divergence."""
    return _div_persistence(close, _rsi_wilder(close, 14), QDAYS)


def f32_divd_014_rsi14_div_count_in_252d(close: pd.Series) -> pd.Series:
    """Count of RSI14 21d bearish-shift divergence events within trailing 252d."""
    return _div_count_in_window(close, _rsi_wilder(close, 14), MDAYS, YDAYS)


def f32_divd_015_rsi14_div_x_overbought_indicator_63d(close: pd.Series) -> pd.Series:
    """RSI14 bearish divergence AND RSI > 70 — conjunction (overbought + divergent)."""
    rsi = _rsi_wilder(close, 14)
    div = _shift_div_bearish_indicator(close, rsi, QDAYS)
    return (div * (rsi > 70).astype(float)).where(rsi.notna() & div.notna(), np.nan)


# ============================================================
# Bucket B — MACD line divergences (016-025)
# ============================================================

def f32_divd_016_macdline_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence: log-close vs MACD line (12/26) over 63d."""
    return _slope_div_sign(close, _macd_line(close, 12, 26), QDAYS)


def f32_divd_017_macdline_slope_div_sign_252d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence: log-close vs MACD line over 252d — secular."""
    return _slope_div_sign(close, _macd_line(close, 12, 26), YDAYS)


def f32_divd_018_macdline_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs MACD line, 63d lookback."""
    return _shift_div_bearish_indicator(close, _macd_line(close, 12, 26), QDAYS)


def f32_divd_019_macdline_shift_div_magnitude_63d(close: pd.Series) -> pd.Series:
    """Magnitude of 63d two-point bearish divergence on MACD line."""
    return _shift_div_bearish_magnitude(close, _macd_line(close, 12, 26), QDAYS)


def f32_divd_020_macdline_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(MACD line,63) — extension gap."""
    return _zscore_gap(close, _macd_line(close, 12, 26), QDAYS)


def f32_divd_021_macdline_pct_rank_gap_63d(close: pd.Series) -> pd.Series:
    """Percentile-rank gap of close vs MACD line — non-parametric divergence."""
    return _pct_rank_gap(close, _macd_line(close, 12, 26), QDAYS)


def f32_divd_022_macdline_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d Pearson corr of log-close and MACD line."""
    return _rolling_corr_pearson(_safe_log(close), _macd_line(close, 12, 26), QDAYS)


def f32_divd_023_macdline_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish: price LH + MACD line HH over 63d."""
    return _shift_div_hidden_bearish_indicator(close, _macd_line(close, 12, 26), QDAYS)


def f32_divd_024_macdline_div_persistence_63d(close: pd.Series) -> pd.Series:
    """Bars since last 63d MACD-line bearish divergence event."""
    return _div_persistence(close, _macd_line(close, 12, 26), QDAYS)


def f32_divd_025_macdline_div_count_in_252d(close: pd.Series) -> pd.Series:
    """Count of MACD-line 21d bearish-shift divergences within trailing 252d."""
    return _div_count_in_window(close, _macd_line(close, 12, 26), MDAYS, YDAYS)


# ============================================================
# Bucket C — MACD histogram divergences (026-033)
# ============================================================

def f32_divd_026_macdhist_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on MACD histogram (12/26/9), 63d."""
    return _slope_div_sign(close, _macd_hist(close, 12, 26, 9), QDAYS)


def f32_divd_027_macdhist_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on MACD histogram, 63d lookback."""
    return _shift_div_bearish_indicator(close, _macd_hist(close, 12, 26, 9), QDAYS)


def f32_divd_028_macdhist_shift_div_magnitude_63d(close: pd.Series) -> pd.Series:
    """Magnitude of 63d two-point bearish divergence on MACD histogram."""
    return _shift_div_bearish_magnitude(close, _macd_hist(close, 12, 26, 9), QDAYS)


def f32_divd_029_macdhist_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(MACD hist,63)."""
    return _zscore_gap(close, _macd_hist(close, 12, 26, 9), QDAYS)


def f32_divd_030_macdhist_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish divergence — price LH + MACD-H HH over 63d."""
    return _shift_div_hidden_bearish_indicator(close, _macd_hist(close, 12, 26, 9), QDAYS)


def f32_divd_031_macdhist_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and MACD histogram."""
    return _rolling_corr_pearson(_safe_log(close), _macd_hist(close, 12, 26, 9), QDAYS)


def f32_divd_032_macdhist_pos_to_neg_flip_at_high_indicator(close: pd.Series) -> pd.Series:
    """MACD-H went from positive to negative within last 5 bars AND close at 252d-max — rollover-at-top."""
    h = _macd_hist(close, 12, 26, 9)
    flip = ((h.shift(1) > 0) & (h <= 0)).astype(float).rolling(WDAYS, min_periods=1).max()
    at_max = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.995).astype(float)
    return (flip * at_max).where(h.notna(), np.nan)


def f32_divd_033_macdhist_consec_lower_peaks_count_252d(close: pd.Series) -> pd.Series:
    """Count of confirmed lower MACD-H peaks observed in trailing 252d. PIT-safe: peak
    confirmation uses only the prior 3-bar trailing max (no forward bar)."""
    h = _macd_hist(close, 12, 26, 9)
    pk = ((h == h.rolling(3, min_periods=3).max()) & (h > h.shift(1))).astype(float)
    pk_val = h.where(pk == 1, np.nan).ffill()
    lower_pk = (pk_val < pk_val.shift(1)).astype(float)
    return lower_pk.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket D — OBV divergences (034-043)
# ============================================================

def f32_divd_034_obv_slope_div_sign_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on OBV vs log-close over 63d."""
    return _slope_div_sign(close, _obv(close, volume), QDAYS)


def f32_divd_035_obv_slope_div_sign_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on OBV vs log-close over 252d (secular)."""
    return _slope_div_sign(close, _obv(close, volume), YDAYS)


def f32_divd_036_obv_shift_div_indicator_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs OBV, 63d lookback."""
    return _shift_div_bearish_indicator(close, _obv(close, volume), QDAYS)


def f32_divd_037_obv_shift_div_magnitude_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Magnitude of 63d bearish shift-divergence on OBV."""
    return _shift_div_bearish_magnitude(close, _obv(close, volume), QDAYS)


def f32_divd_038_obv_zscore_gap_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(OBV,63) — price extended vs accumulation."""
    return _zscore_gap(close, _obv(close, volume), QDAYS)


def f32_divd_039_obv_zscore_gap_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,252) - z(OBV,252) — secular distribution flag."""
    return _zscore_gap(close, _obv(close, volume), YDAYS)


def f32_divd_040_obv_rolling_corr_price_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and OBV — falling toward zero = distribution risk."""
    return _rolling_corr_pearson(_safe_log(close), _obv(close, volume), QDAYS)


def f32_divd_041_obv_hidden_bearish_div_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish: price LH + OBV HH (volume continuing while price weakening)."""
    return _shift_div_hidden_bearish_indicator(close, _obv(close, volume), QDAYS)


def f32_divd_042_obv_div_persistence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last 63d OBV bearish divergence event."""
    return _div_persistence(close, _obv(close, volume), QDAYS)


def f32_divd_043_obv_div_count_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of OBV 21d bearish-shift divergences within trailing 252d."""
    return _div_count_in_window(close, _obv(close, volume), MDAYS, YDAYS)


# ============================================================
# Bucket E — A/D line (Chaikin) divergences (044-051)
# ============================================================

def f32_divd_044_adline_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence: close vs Chaikin A/D line, 63d."""
    return _slope_div_sign(close, _ad_line(high, low, close, volume), QDAYS)


def f32_divd_045_adline_slope_div_sign_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence: close vs A/D line, 252d (secular)."""
    return _slope_div_sign(close, _ad_line(high, low, close, volume), YDAYS)


def f32_divd_046_adline_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs A/D line, 63d lookback."""
    return _shift_div_bearish_indicator(close, _ad_line(high, low, close, volume), QDAYS)


def f32_divd_047_adline_shift_div_magnitude_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Magnitude of 63d bearish shift-divergence on A/D line."""
    return _shift_div_bearish_magnitude(close, _ad_line(high, low, close, volume), QDAYS)


def f32_divd_048_adline_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(close,63) - z(A/D,63)."""
    return _zscore_gap(close, _ad_line(high, low, close, volume), QDAYS)


def f32_divd_049_adline_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and A/D line."""
    return _rolling_corr_pearson(_safe_log(close), _ad_line(high, low, close, volume), QDAYS)


def f32_divd_050_adline_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish: price LH + A/D HH over 63d (latent supply at lower price)."""
    return _shift_div_hidden_bearish_indicator(close, _ad_line(high, low, close, volume), QDAYS)


def f32_divd_051_adline_div_count_in_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of A/D-line 21d bearish-shift divergences in trailing 252d."""
    return _div_count_in_window(close, _ad_line(high, low, close, volume), MDAYS, YDAYS)


# ============================================================
# Bucket F — Stoch %K divergences (052-059)
# ============================================================

def f32_divd_052_stochk_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence: close vs Stoch %K(14), 63d."""
    return _slope_div_sign(close, _stoch_k(high, low, close, 14), QDAYS)


def f32_divd_053_stochk_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs Stoch %K, 63d."""
    return _shift_div_bearish_indicator(close, _stoch_k(high, low, close, 14), QDAYS)


def f32_divd_054_stochk_shift_div_magnitude_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Magnitude of 63d two-point bearish divergence on Stoch %K."""
    return _shift_div_bearish_magnitude(close, _stoch_k(high, low, close, 14), QDAYS)


def f32_divd_055_stochk_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Stoch %K,63)."""
    return _zscore_gap(close, _stoch_k(high, low, close, 14), QDAYS)


def f32_divd_056_stochk_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and Stoch %K."""
    return _rolling_corr_pearson(_safe_log(close), _stoch_k(high, low, close, 14), QDAYS)


def f32_divd_057_stochk_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Stoch %K HH over 63d."""
    return _shift_div_hidden_bearish_indicator(close, _stoch_k(high, low, close, 14), QDAYS)


def f32_divd_058_stochk_div_x_overbought_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish Stoch %K divergence AND Stoch %K > 80 — conjunction."""
    k = _stoch_k(high, low, close, 14)
    div = _shift_div_bearish_indicator(close, k, QDAYS)
    return (div * (k > 80).astype(float)).where(k.notna() & div.notna(), np.nan)


def f32_divd_059_stochk_div_count_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of Stoch %K 21d bearish-shift divergences in trailing 252d."""
    return _div_count_in_window(close, _stoch_k(high, low, close, 14), MDAYS, YDAYS)


# ============================================================
# Bucket G — Stoch RSI divergences (060-065)
# ============================================================

def f32_divd_060_stochrsi_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Stoch RSI(14), 63d."""
    return _slope_div_sign(close, _stoch_rsi(close, 14), QDAYS)


def f32_divd_061_stochrsi_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on Stoch RSI, 63d."""
    return _shift_div_bearish_indicator(close, _stoch_rsi(close, 14), QDAYS)


def f32_divd_062_stochrsi_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Stoch RSI,63)."""
    return _zscore_gap(close, _stoch_rsi(close, 14), QDAYS)


def f32_divd_063_stochrsi_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and Stoch RSI."""
    return _rolling_corr_pearson(_safe_log(close), _stoch_rsi(close, 14), QDAYS)


def f32_divd_064_stochrsi_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Stoch RSI HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _stoch_rsi(close, 14), QDAYS)


def f32_divd_065_stochrsi_div_x_overbought_indicator_63d(close: pd.Series) -> pd.Series:
    """Bearish Stoch RSI divergence AND Stoch RSI > 0.8 — conjunction."""
    sr = _stoch_rsi(close, 14)
    div = _shift_div_bearish_indicator(close, sr, QDAYS)
    return (div * (sr > 0.8).astype(float)).where(sr.notna() & div.notna(), np.nan)


# ============================================================
# Bucket H — Williams %R divergences (066-071)
# ============================================================

def f32_divd_066_williamsr_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on Williams %R(14), 63d."""
    return _slope_div_sign(close, _williams_r(high, low, close, 14), QDAYS)


def f32_divd_067_williamsr_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on Williams %R, 63d."""
    return _shift_div_bearish_indicator(close, _williams_r(high, low, close, 14), QDAYS)


def f32_divd_068_williamsr_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Williams %R,63)."""
    return _zscore_gap(close, _williams_r(high, low, close, 14), QDAYS)


def f32_divd_069_williamsr_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and Williams %R."""
    return _rolling_corr_pearson(_safe_log(close), _williams_r(high, low, close, 14), QDAYS)


def f32_divd_070_williamsr_hidden_bearish_div_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Williams %R HH, 63d."""
    return _shift_div_hidden_bearish_indicator(close, _williams_r(high, low, close, 14), QDAYS)


def f32_divd_071_williamsr_div_x_overbought_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish Williams %R divergence AND %R > -20 — conjunction."""
    wr = _williams_r(high, low, close, 14)
    div = _shift_div_bearish_indicator(close, wr, QDAYS)
    return (div * (wr > -20).astype(float)).where(wr.notna() & div.notna(), np.nan)


# ============================================================
# Bucket I — CMF divergences (072-075)
# ============================================================

def f32_divd_072_cmf_slope_div_sign_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence on CMF(20), 63d."""
    return _slope_div_sign(close, _cmf(high, low, close, volume, 20), QDAYS)


def f32_divd_073_cmf_shift_div_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence on CMF, 63d."""
    return _shift_div_bearish_indicator(close, _cmf(high, low, close, volume, 20), QDAYS)


def f32_divd_074_cmf_zscore_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(log close,63) - z(CMF,63) — price extended vs money-flow."""
    return _zscore_gap(close, _cmf(high, low, close, volume, 20), QDAYS)


def f32_divd_075_cmf_rolling_corr_price_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr of log-close and CMF."""
    return _rolling_corr_pearson(_safe_log(close), _cmf(high, low, close, volume, 20), QDAYS)


# ============================================================
# REGISTRY
# ============================================================



def f32_divd_001_rsi14_slope_div_sign_63d_d2(close):
    return f32_divd_001_rsi14_slope_div_sign_63d(close).diff().diff()


def f32_divd_002_rsi14_slope_div_sign_252d_d2(close):
    return f32_divd_002_rsi14_slope_div_sign_252d(close).diff().diff()


def f32_divd_003_rsi14_slope_div_magnitude_63d_d2(close):
    return f32_divd_003_rsi14_slope_div_magnitude_63d(close).diff().diff()


def f32_divd_004_rsi14_shift_div_indicator_63d_d2(close):
    return f32_divd_004_rsi14_shift_div_indicator_63d(close).diff().diff()


def f32_divd_005_rsi14_shift_div_indicator_252d_d2(close):
    return f32_divd_005_rsi14_shift_div_indicator_252d(close).diff().diff()


def f32_divd_006_rsi14_shift_div_magnitude_63d_d2(close):
    return f32_divd_006_rsi14_shift_div_magnitude_63d(close).diff().diff()


def f32_divd_007_rsi14_rolling_corr_price_63d_d2(close):
    return f32_divd_007_rsi14_rolling_corr_price_63d(close).diff().diff()


def f32_divd_008_rsi14_rolling_corr_price_252d_d2(close):
    return f32_divd_008_rsi14_rolling_corr_price_252d(close).diff().diff()


def f32_divd_009_rsi14_zscore_gap_63d_d2(close):
    return f32_divd_009_rsi14_zscore_gap_63d(close).diff().diff()


def f32_divd_010_rsi14_zscore_gap_252d_d2(close):
    return f32_divd_010_rsi14_zscore_gap_252d(close).diff().diff()


def f32_divd_011_rsi14_pct_rank_gap_63d_d2(close):
    return f32_divd_011_rsi14_pct_rank_gap_63d(close).diff().diff()


def f32_divd_012_rsi14_hidden_bearish_div_63d_d2(close):
    return f32_divd_012_rsi14_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_013_rsi14_div_persistence_63d_d2(close):
    return f32_divd_013_rsi14_div_persistence_63d(close).diff().diff()


def f32_divd_014_rsi14_div_count_in_252d_d2(close):
    return f32_divd_014_rsi14_div_count_in_252d(close).diff().diff()


def f32_divd_015_rsi14_div_x_overbought_indicator_63d_d2(close):
    return f32_divd_015_rsi14_div_x_overbought_indicator_63d(close).diff().diff()


def f32_divd_016_macdline_slope_div_sign_63d_d2(close):
    return f32_divd_016_macdline_slope_div_sign_63d(close).diff().diff()


def f32_divd_017_macdline_slope_div_sign_252d_d2(close):
    return f32_divd_017_macdline_slope_div_sign_252d(close).diff().diff()


def f32_divd_018_macdline_shift_div_indicator_63d_d2(close):
    return f32_divd_018_macdline_shift_div_indicator_63d(close).diff().diff()


def f32_divd_019_macdline_shift_div_magnitude_63d_d2(close):
    return f32_divd_019_macdline_shift_div_magnitude_63d(close).diff().diff()


def f32_divd_020_macdline_zscore_gap_63d_d2(close):
    return f32_divd_020_macdline_zscore_gap_63d(close).diff().diff()


def f32_divd_021_macdline_pct_rank_gap_63d_d2(close):
    return f32_divd_021_macdline_pct_rank_gap_63d(close).diff().diff()


def f32_divd_022_macdline_rolling_corr_price_63d_d2(close):
    return f32_divd_022_macdline_rolling_corr_price_63d(close).diff().diff()


def f32_divd_023_macdline_hidden_bearish_div_63d_d2(close):
    return f32_divd_023_macdline_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_024_macdline_div_persistence_63d_d2(close):
    return f32_divd_024_macdline_div_persistence_63d(close).diff().diff()


def f32_divd_025_macdline_div_count_in_252d_d2(close):
    return f32_divd_025_macdline_div_count_in_252d(close).diff().diff()


def f32_divd_026_macdhist_slope_div_sign_63d_d2(close):
    return f32_divd_026_macdhist_slope_div_sign_63d(close).diff().diff()


def f32_divd_027_macdhist_shift_div_indicator_63d_d2(close):
    return f32_divd_027_macdhist_shift_div_indicator_63d(close).diff().diff()


def f32_divd_028_macdhist_shift_div_magnitude_63d_d2(close):
    return f32_divd_028_macdhist_shift_div_magnitude_63d(close).diff().diff()


def f32_divd_029_macdhist_zscore_gap_63d_d2(close):
    return f32_divd_029_macdhist_zscore_gap_63d(close).diff().diff()


def f32_divd_030_macdhist_hidden_bearish_div_63d_d2(close):
    return f32_divd_030_macdhist_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_031_macdhist_rolling_corr_price_63d_d2(close):
    return f32_divd_031_macdhist_rolling_corr_price_63d(close).diff().diff()


def f32_divd_032_macdhist_pos_to_neg_flip_at_high_indicator_d2(close):
    return f32_divd_032_macdhist_pos_to_neg_flip_at_high_indicator(close).diff().diff()


def f32_divd_033_macdhist_consec_lower_peaks_count_252d_d2(close):
    return f32_divd_033_macdhist_consec_lower_peaks_count_252d(close).diff().diff()


def f32_divd_034_obv_slope_div_sign_63d_d2(close, volume):
    return f32_divd_034_obv_slope_div_sign_63d(close, volume).diff().diff()


def f32_divd_035_obv_slope_div_sign_252d_d2(close, volume):
    return f32_divd_035_obv_slope_div_sign_252d(close, volume).diff().diff()


def f32_divd_036_obv_shift_div_indicator_63d_d2(close, volume):
    return f32_divd_036_obv_shift_div_indicator_63d(close, volume).diff().diff()


def f32_divd_037_obv_shift_div_magnitude_63d_d2(close, volume):
    return f32_divd_037_obv_shift_div_magnitude_63d(close, volume).diff().diff()


def f32_divd_038_obv_zscore_gap_63d_d2(close, volume):
    return f32_divd_038_obv_zscore_gap_63d(close, volume).diff().diff()


def f32_divd_039_obv_zscore_gap_252d_d2(close, volume):
    return f32_divd_039_obv_zscore_gap_252d(close, volume).diff().diff()


def f32_divd_040_obv_rolling_corr_price_63d_d2(close, volume):
    return f32_divd_040_obv_rolling_corr_price_63d(close, volume).diff().diff()


def f32_divd_041_obv_hidden_bearish_div_63d_d2(close, volume):
    return f32_divd_041_obv_hidden_bearish_div_63d(close, volume).diff().diff()


def f32_divd_042_obv_div_persistence_63d_d2(close, volume):
    return f32_divd_042_obv_div_persistence_63d(close, volume).diff().diff()


def f32_divd_043_obv_div_count_in_252d_d2(close, volume):
    return f32_divd_043_obv_div_count_in_252d(close, volume).diff().diff()


def f32_divd_044_adline_slope_div_sign_63d_d2(high, low, close, volume):
    return f32_divd_044_adline_slope_div_sign_63d(high, low, close, volume).diff().diff()


def f32_divd_045_adline_slope_div_sign_252d_d2(high, low, close, volume):
    return f32_divd_045_adline_slope_div_sign_252d(high, low, close, volume).diff().diff()


def f32_divd_046_adline_shift_div_indicator_63d_d2(high, low, close, volume):
    return f32_divd_046_adline_shift_div_indicator_63d(high, low, close, volume).diff().diff()


def f32_divd_047_adline_shift_div_magnitude_63d_d2(high, low, close, volume):
    return f32_divd_047_adline_shift_div_magnitude_63d(high, low, close, volume).diff().diff()


def f32_divd_048_adline_zscore_gap_63d_d2(high, low, close, volume):
    return f32_divd_048_adline_zscore_gap_63d(high, low, close, volume).diff().diff()


def f32_divd_049_adline_rolling_corr_price_63d_d2(high, low, close, volume):
    return f32_divd_049_adline_rolling_corr_price_63d(high, low, close, volume).diff().diff()


def f32_divd_050_adline_hidden_bearish_div_63d_d2(high, low, close, volume):
    return f32_divd_050_adline_hidden_bearish_div_63d(high, low, close, volume).diff().diff()


def f32_divd_051_adline_div_count_in_252d_d2(high, low, close, volume):
    return f32_divd_051_adline_div_count_in_252d(high, low, close, volume).diff().diff()


def f32_divd_052_stochk_slope_div_sign_63d_d2(high, low, close):
    return f32_divd_052_stochk_slope_div_sign_63d(high, low, close).diff().diff()


def f32_divd_053_stochk_shift_div_indicator_63d_d2(high, low, close):
    return f32_divd_053_stochk_shift_div_indicator_63d(high, low, close).diff().diff()


def f32_divd_054_stochk_shift_div_magnitude_63d_d2(high, low, close):
    return f32_divd_054_stochk_shift_div_magnitude_63d(high, low, close).diff().diff()


def f32_divd_055_stochk_zscore_gap_63d_d2(high, low, close):
    return f32_divd_055_stochk_zscore_gap_63d(high, low, close).diff().diff()


def f32_divd_056_stochk_rolling_corr_price_63d_d2(high, low, close):
    return f32_divd_056_stochk_rolling_corr_price_63d(high, low, close).diff().diff()


def f32_divd_057_stochk_hidden_bearish_div_63d_d2(high, low, close):
    return f32_divd_057_stochk_hidden_bearish_div_63d(high, low, close).diff().diff()


def f32_divd_058_stochk_div_x_overbought_indicator_63d_d2(high, low, close):
    return f32_divd_058_stochk_div_x_overbought_indicator_63d(high, low, close).diff().diff()


def f32_divd_059_stochk_div_count_in_252d_d2(high, low, close):
    return f32_divd_059_stochk_div_count_in_252d(high, low, close).diff().diff()


def f32_divd_060_stochrsi_slope_div_sign_63d_d2(close):
    return f32_divd_060_stochrsi_slope_div_sign_63d(close).diff().diff()


def f32_divd_061_stochrsi_shift_div_indicator_63d_d2(close):
    return f32_divd_061_stochrsi_shift_div_indicator_63d(close).diff().diff()


def f32_divd_062_stochrsi_zscore_gap_63d_d2(close):
    return f32_divd_062_stochrsi_zscore_gap_63d(close).diff().diff()


def f32_divd_063_stochrsi_rolling_corr_price_63d_d2(close):
    return f32_divd_063_stochrsi_rolling_corr_price_63d(close).diff().diff()


def f32_divd_064_stochrsi_hidden_bearish_div_63d_d2(close):
    return f32_divd_064_stochrsi_hidden_bearish_div_63d(close).diff().diff()


def f32_divd_065_stochrsi_div_x_overbought_indicator_63d_d2(close):
    return f32_divd_065_stochrsi_div_x_overbought_indicator_63d(close).diff().diff()


def f32_divd_066_williamsr_slope_div_sign_63d_d2(high, low, close):
    return f32_divd_066_williamsr_slope_div_sign_63d(high, low, close).diff().diff()


def f32_divd_067_williamsr_shift_div_indicator_63d_d2(high, low, close):
    return f32_divd_067_williamsr_shift_div_indicator_63d(high, low, close).diff().diff()


def f32_divd_068_williamsr_zscore_gap_63d_d2(high, low, close):
    return f32_divd_068_williamsr_zscore_gap_63d(high, low, close).diff().diff()


def f32_divd_069_williamsr_rolling_corr_price_63d_d2(high, low, close):
    return f32_divd_069_williamsr_rolling_corr_price_63d(high, low, close).diff().diff()


def f32_divd_070_williamsr_hidden_bearish_div_63d_d2(high, low, close):
    return f32_divd_070_williamsr_hidden_bearish_div_63d(high, low, close).diff().diff()


def f32_divd_071_williamsr_div_x_overbought_indicator_63d_d2(high, low, close):
    return f32_divd_071_williamsr_div_x_overbought_indicator_63d(high, low, close).diff().diff()


def f32_divd_072_cmf_slope_div_sign_63d_d2(high, low, close, volume):
    return f32_divd_072_cmf_slope_div_sign_63d(high, low, close, volume).diff().diff()


def f32_divd_073_cmf_shift_div_indicator_63d_d2(high, low, close, volume):
    return f32_divd_073_cmf_shift_div_indicator_63d(high, low, close, volume).diff().diff()


def f32_divd_074_cmf_zscore_gap_63d_d2(high, low, close, volume):
    return f32_divd_074_cmf_zscore_gap_63d(high, low, close, volume).diff().diff()


def f32_divd_075_cmf_rolling_corr_price_63d_d2(high, low, close, volume):
    return f32_divd_075_cmf_rolling_corr_price_63d(high, low, close, volume).diff().diff()


DIVERGENCE_DETECTION_D2_REGISTRY_001_075 = {
    "f32_divd_001_rsi14_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_001_rsi14_slope_div_sign_63d_d2},
    "f32_divd_002_rsi14_slope_div_sign_252d_d2": {"inputs": ["close"], "func": f32_divd_002_rsi14_slope_div_sign_252d_d2},
    "f32_divd_003_rsi14_slope_div_magnitude_63d_d2": {"inputs": ["close"], "func": f32_divd_003_rsi14_slope_div_magnitude_63d_d2},
    "f32_divd_004_rsi14_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_004_rsi14_shift_div_indicator_63d_d2},
    "f32_divd_005_rsi14_shift_div_indicator_252d_d2": {"inputs": ["close"], "func": f32_divd_005_rsi14_shift_div_indicator_252d_d2},
    "f32_divd_006_rsi14_shift_div_magnitude_63d_d2": {"inputs": ["close"], "func": f32_divd_006_rsi14_shift_div_magnitude_63d_d2},
    "f32_divd_007_rsi14_rolling_corr_price_63d_d2": {"inputs": ["close"], "func": f32_divd_007_rsi14_rolling_corr_price_63d_d2},
    "f32_divd_008_rsi14_rolling_corr_price_252d_d2": {"inputs": ["close"], "func": f32_divd_008_rsi14_rolling_corr_price_252d_d2},
    "f32_divd_009_rsi14_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_009_rsi14_zscore_gap_63d_d2},
    "f32_divd_010_rsi14_zscore_gap_252d_d2": {"inputs": ["close"], "func": f32_divd_010_rsi14_zscore_gap_252d_d2},
    "f32_divd_011_rsi14_pct_rank_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_011_rsi14_pct_rank_gap_63d_d2},
    "f32_divd_012_rsi14_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_012_rsi14_hidden_bearish_div_63d_d2},
    "f32_divd_013_rsi14_div_persistence_63d_d2": {"inputs": ["close"], "func": f32_divd_013_rsi14_div_persistence_63d_d2},
    "f32_divd_014_rsi14_div_count_in_252d_d2": {"inputs": ["close"], "func": f32_divd_014_rsi14_div_count_in_252d_d2},
    "f32_divd_015_rsi14_div_x_overbought_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_015_rsi14_div_x_overbought_indicator_63d_d2},
    "f32_divd_016_macdline_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_016_macdline_slope_div_sign_63d_d2},
    "f32_divd_017_macdline_slope_div_sign_252d_d2": {"inputs": ["close"], "func": f32_divd_017_macdline_slope_div_sign_252d_d2},
    "f32_divd_018_macdline_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_018_macdline_shift_div_indicator_63d_d2},
    "f32_divd_019_macdline_shift_div_magnitude_63d_d2": {"inputs": ["close"], "func": f32_divd_019_macdline_shift_div_magnitude_63d_d2},
    "f32_divd_020_macdline_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_020_macdline_zscore_gap_63d_d2},
    "f32_divd_021_macdline_pct_rank_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_021_macdline_pct_rank_gap_63d_d2},
    "f32_divd_022_macdline_rolling_corr_price_63d_d2": {"inputs": ["close"], "func": f32_divd_022_macdline_rolling_corr_price_63d_d2},
    "f32_divd_023_macdline_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_023_macdline_hidden_bearish_div_63d_d2},
    "f32_divd_024_macdline_div_persistence_63d_d2": {"inputs": ["close"], "func": f32_divd_024_macdline_div_persistence_63d_d2},
    "f32_divd_025_macdline_div_count_in_252d_d2": {"inputs": ["close"], "func": f32_divd_025_macdline_div_count_in_252d_d2},
    "f32_divd_026_macdhist_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_026_macdhist_slope_div_sign_63d_d2},
    "f32_divd_027_macdhist_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_027_macdhist_shift_div_indicator_63d_d2},
    "f32_divd_028_macdhist_shift_div_magnitude_63d_d2": {"inputs": ["close"], "func": f32_divd_028_macdhist_shift_div_magnitude_63d_d2},
    "f32_divd_029_macdhist_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_029_macdhist_zscore_gap_63d_d2},
    "f32_divd_030_macdhist_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_030_macdhist_hidden_bearish_div_63d_d2},
    "f32_divd_031_macdhist_rolling_corr_price_63d_d2": {"inputs": ["close"], "func": f32_divd_031_macdhist_rolling_corr_price_63d_d2},
    "f32_divd_032_macdhist_pos_to_neg_flip_at_high_indicator_d2": {"inputs": ["close"], "func": f32_divd_032_macdhist_pos_to_neg_flip_at_high_indicator_d2},
    "f32_divd_033_macdhist_consec_lower_peaks_count_252d_d2": {"inputs": ["close"], "func": f32_divd_033_macdhist_consec_lower_peaks_count_252d_d2},
    "f32_divd_034_obv_slope_div_sign_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_034_obv_slope_div_sign_63d_d2},
    "f32_divd_035_obv_slope_div_sign_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_035_obv_slope_div_sign_252d_d2},
    "f32_divd_036_obv_shift_div_indicator_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_036_obv_shift_div_indicator_63d_d2},
    "f32_divd_037_obv_shift_div_magnitude_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_037_obv_shift_div_magnitude_63d_d2},
    "f32_divd_038_obv_zscore_gap_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_038_obv_zscore_gap_63d_d2},
    "f32_divd_039_obv_zscore_gap_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_039_obv_zscore_gap_252d_d2},
    "f32_divd_040_obv_rolling_corr_price_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_040_obv_rolling_corr_price_63d_d2},
    "f32_divd_041_obv_hidden_bearish_div_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_041_obv_hidden_bearish_div_63d_d2},
    "f32_divd_042_obv_div_persistence_63d_d2": {"inputs": ["close", "volume"], "func": f32_divd_042_obv_div_persistence_63d_d2},
    "f32_divd_043_obv_div_count_in_252d_d2": {"inputs": ["close", "volume"], "func": f32_divd_043_obv_div_count_in_252d_d2},
    "f32_divd_044_adline_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_044_adline_slope_div_sign_63d_d2},
    "f32_divd_045_adline_slope_div_sign_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_045_adline_slope_div_sign_252d_d2},
    "f32_divd_046_adline_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_046_adline_shift_div_indicator_63d_d2},
    "f32_divd_047_adline_shift_div_magnitude_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_047_adline_shift_div_magnitude_63d_d2},
    "f32_divd_048_adline_zscore_gap_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_048_adline_zscore_gap_63d_d2},
    "f32_divd_049_adline_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_049_adline_rolling_corr_price_63d_d2},
    "f32_divd_050_adline_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_050_adline_hidden_bearish_div_63d_d2},
    "f32_divd_051_adline_div_count_in_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_051_adline_div_count_in_252d_d2},
    "f32_divd_052_stochk_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_052_stochk_slope_div_sign_63d_d2},
    "f32_divd_053_stochk_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_053_stochk_shift_div_indicator_63d_d2},
    "f32_divd_054_stochk_shift_div_magnitude_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_054_stochk_shift_div_magnitude_63d_d2},
    "f32_divd_055_stochk_zscore_gap_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_055_stochk_zscore_gap_63d_d2},
    "f32_divd_056_stochk_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_056_stochk_rolling_corr_price_63d_d2},
    "f32_divd_057_stochk_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_057_stochk_hidden_bearish_div_63d_d2},
    "f32_divd_058_stochk_div_x_overbought_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_058_stochk_div_x_overbought_indicator_63d_d2},
    "f32_divd_059_stochk_div_count_in_252d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_059_stochk_div_count_in_252d_d2},
    "f32_divd_060_stochrsi_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f32_divd_060_stochrsi_slope_div_sign_63d_d2},
    "f32_divd_061_stochrsi_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_061_stochrsi_shift_div_indicator_63d_d2},
    "f32_divd_062_stochrsi_zscore_gap_63d_d2": {"inputs": ["close"], "func": f32_divd_062_stochrsi_zscore_gap_63d_d2},
    "f32_divd_063_stochrsi_rolling_corr_price_63d_d2": {"inputs": ["close"], "func": f32_divd_063_stochrsi_rolling_corr_price_63d_d2},
    "f32_divd_064_stochrsi_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f32_divd_064_stochrsi_hidden_bearish_div_63d_d2},
    "f32_divd_065_stochrsi_div_x_overbought_indicator_63d_d2": {"inputs": ["close"], "func": f32_divd_065_stochrsi_div_x_overbought_indicator_63d_d2},
    "f32_divd_066_williamsr_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_066_williamsr_slope_div_sign_63d_d2},
    "f32_divd_067_williamsr_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_067_williamsr_shift_div_indicator_63d_d2},
    "f32_divd_068_williamsr_zscore_gap_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_068_williamsr_zscore_gap_63d_d2},
    "f32_divd_069_williamsr_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_069_williamsr_rolling_corr_price_63d_d2},
    "f32_divd_070_williamsr_hidden_bearish_div_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_070_williamsr_hidden_bearish_div_63d_d2},
    "f32_divd_071_williamsr_div_x_overbought_indicator_63d_d2": {"inputs": ["high", "low", "close"], "func": f32_divd_071_williamsr_div_x_overbought_indicator_63d_d2},
    "f32_divd_072_cmf_slope_div_sign_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_072_cmf_slope_div_sign_63d_d2},
    "f32_divd_073_cmf_shift_div_indicator_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_073_cmf_shift_div_indicator_63d_d2},
    "f32_divd_074_cmf_zscore_gap_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_074_cmf_zscore_gap_63d_d2},
    "f32_divd_075_cmf_rolling_corr_price_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f32_divd_075_cmf_rolling_corr_price_63d_d2},
}
