"""coppock_curve_kst d3 features 151-225 — Pipeline 1b-technical (gap-fill extension).

Closes the MAJOR gap left by 001-150: Coppock × price divergence (only KST had
divergence features in the original 150). Also adds Pring's Special K, DPO at long
horizons, DTI (DeMark Trend Indicator), VWMA-weighted Coppock, TEMA/DEMA/Hull
smoothed long-momentum, and Coppock-on-RSI meta.

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


def _wma(s, n):
    weights = np.arange(1, n + 1, dtype=float)
    wsum = weights.sum()
    def _ww(w):
        if np.isnan(w).any():
            return np.nan
        return float(np.dot(w, weights) / wsum)
    return s.rolling(n, min_periods=n).apply(_ww, raw=True)


def _roc_pct(s, n):
    return s.pct_change(n) * 100.0


def _hma(s, n):
    """Hull Moving Average: WMA(sqrt(n)) of (2*WMA(n/2) - WMA(n))."""
    half = max(int(n / 2), 1); sqn = max(int(np.sqrt(n)), 1)
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)


def _tema(s, n):
    """Triple-EMA: 3*EMA(n) - 3*EMA(EMA(n)) + EMA(EMA(EMA(n)))."""
    e1 = _ema(s, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _dema(s, n):
    """Double-EMA: 2*EMA(n) - EMA(EMA(n))."""
    e1 = _ema(s, n); e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0); loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(ag, al)
    return 100.0 - 100.0 / (1.0 + rs)


def _vwma(close, volume, n):
    """Volume-weighted moving average over n bars."""
    pv = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    v = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(pv, v)


# ---------------------------- Coppock / KST helpers ----------------------------

def _coppock(close, n_long, n_short, n_wma):
    return _wma(_roc_pct(close, n_long) + _roc_pct(close, n_short), n_wma)


def _coppock_annual(close):
    return _coppock(close, 294, 231, 210)


def _coppock_biennial(close):
    return _coppock(close, DDAYS_2Y, 378, 210)


def _coppock_semi_annual(close):
    return _coppock(close, 126, 84, 42)


def _coppock_quarterly(close):
    return _coppock(close, QDAYS, 42, MDAYS)


def _kst(close):
    return (1.0 * _sma(_roc_pct(close, 10), 10)
            + 2.0 * _sma(_roc_pct(close, 15), 10)
            + 3.0 * _sma(_roc_pct(close, 20), 10)
            + 4.0 * _sma(_roc_pct(close, 30), 15))


def _kst_long_term(close):
    return (1.0 * _sma(_roc_pct(close, 65), 21)
            + 2.0 * _sma(_roc_pct(close, 130), 21)
            + 3.0 * _sma(_roc_pct(close, 195), 21)
            + 4.0 * _sma(_roc_pct(close, 260), 42))


# ---------------------------- new long-momentum indicators ----------------------------

def _special_k(close):
    """Pring's Special K: weighted sum of 10 smoothed ROCs spanning short to long.
    Adapted to daily by multiplying canonical monthly horizons by ~21.
    Components (weight × ROC(n) smoothed by SMA(m)):
      1 * SMA(10) of ROC(10)
      2 * SMA(10) of ROC(15)
      3 * SMA(10) of ROC(20)
      4 * SMA(15) of ROC(30)
      1 * SMA(50) of ROC(50)
      2 * SMA(65) of ROC(65)
      3 * SMA(75) of ROC(75)
      4 * SMA(100) of ROC(100)
      1 * SMA(130) of ROC(195)
      2 * SMA(195) of ROC(265)
      3 * SMA(265) of ROC(390)
      4 * SMA(390) of ROC(530)
    Total reduced to 8 components for daily-adapted compactness."""
    return (1.0 * _sma(_roc_pct(close, 10), 10)
            + 2.0 * _sma(_roc_pct(close, 15), 10)
            + 3.0 * _sma(_roc_pct(close, 20), 10)
            + 4.0 * _sma(_roc_pct(close, 30), 15)
            + 1.0 * _sma(_roc_pct(close, 50), 50)
            + 2.0 * _sma(_roc_pct(close, 65), 65)
            + 3.0 * _sma(_roc_pct(close, 100), 100)
            + 4.0 * _sma(_roc_pct(close, 195), 130))


def _dpo(close, n):
    """Detrended Price Oscillator: close - SMA(n) shifted forward by (n/2+1) (PIT-safe variant).
    Original DPO uses centered SMA which is not PIT-safe; PIT version uses trailing SMA only."""
    return close - _sma(close, n)


def _dti(close, r=14, s=10, u=5):
    """DeMark's DTI (DeMark Trend Indicator): smoothed high-low momentum sign trend.
    Simplified formulation: EMA(u) of EMA(s) of EMA(r) of momentum where momentum
    is sign of (close - close.shift(r)) weighted by absolute log-return."""
    mom = np.sign(close - close.shift(r)) * (_safe_log(close).diff().abs())
    e1 = _ema(mom, r); e2 = _ema(e1, s); e3 = _ema(e2, u)
    abs_e1 = _ema(mom.abs(), r); abs_e2 = _ema(abs_e1, s); abs_e3 = _ema(abs_e2, u)
    return 100.0 * _safe_div(e3, abs_e3)


def _vwma_coppock(close, volume):
    """VWMA-weighted Coppock variant: WMA-of-ROC computed on VWMA(63)-smoothed close."""
    smoothed = _vwma(close, volume, QDAYS)
    return _coppock(smoothed, 294, 231, 210)


def _tema_long_momentum(close, n=63):
    """TEMA(63) of ROC(63) — long-cycle TEMA-smoothed momentum."""
    return _tema(_roc_pct(close, n), n)


def _dema_long_momentum(close, n=63):
    """DEMA(63) of ROC(63)."""
    return _dema(_roc_pct(close, n), n)


def _hma_long_momentum(close, n=63):
    """Hull-MA(63) of ROC(63) — adaptive smoother."""
    return _hma(_roc_pct(close, n), n)


def _coppock_on_rsi(close):
    """Coppock applied to RSI(14) directly — momentum-of-momentum."""
    rsi = _rsi_wilder(close, 14)
    return _wma(_roc_pct(rsi, 63) + _roc_pct(rsi, 42), 21)


# ---------------------------- divergence helpers ----------------------------

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


def _shift_div_hidden_bearish_indicator(price, osc, k):
    pp = price.shift(k); op = osc.shift(k)
    return ((price < pp) & (osc > op)).astype(float).where(pp.notna() & op.notna(), np.nan)


def _zscore_gap(price, osc, n):
    return _rolling_zscore(_safe_log(price), n) - _rolling_zscore(osc, n)


def _rolling_corr_pearson(a, b, n):
    return a.rolling(n, min_periods=max(n // 3, 2)).corr(b)


# ============================================================
# Bucket PP — Coppock-annual × price divergence (MAJOR gap) (151-162)
# ============================================================

def f33_cpkt_151_coppock_annual_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence between log-close and annual Coppock over 63d (short-window)."""
    return _slope_div_sign(close, _coppock_annual(close), QDAYS)


def f33_cpkt_152_coppock_annual_slope_div_sign_252d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence between log-close and annual Coppock over 252d (annual-cycle failure)."""
    return _slope_div_sign(close, _coppock_annual(close), YDAYS)


def f33_cpkt_153_coppock_annual_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs annual Coppock, 63d."""
    return _shift_div_bearish_indicator(close, _coppock_annual(close), QDAYS)


def f33_cpkt_154_coppock_annual_shift_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs annual Coppock, 252d."""
    return _shift_div_bearish_indicator(close, _coppock_annual(close), YDAYS)


def f33_cpkt_155_coppock_annual_slope_div_magnitude_63d(close: pd.Series) -> pd.Series:
    """Z-scored slope-gap (close vs annual Coppock), 63d — continuous bearish strength."""
    return _slope_div_magnitude(close, _coppock_annual(close), QDAYS)


def f33_cpkt_156_coppock_annual_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(Coppock annual,63) — extension gap."""
    return _zscore_gap(close, _coppock_annual(close), QDAYS)


def f33_cpkt_157_coppock_annual_zscore_gap_252d(close: pd.Series) -> pd.Series:
    """z(log close,252) - z(Coppock annual,252) — annual extension gap."""
    return _zscore_gap(close, _coppock_annual(close), YDAYS)


def f33_cpkt_158_coppock_annual_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d Pearson corr of log-close and annual Coppock."""
    return _rolling_corr_pearson(_safe_log(close), _coppock_annual(close), QDAYS)


def f33_cpkt_159_coppock_annual_rolling_corr_price_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr of log-close and annual Coppock — secular agreement."""
    return _rolling_corr_pearson(_safe_log(close), _coppock_annual(close), YDAYS)


def f33_cpkt_160_coppock_annual_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Coppock-annual HH over 63d."""
    return _shift_div_hidden_bearish_indicator(close, _coppock_annual(close), QDAYS)


def f33_cpkt_161_coppock_annual_div_persistence_63d(close: pd.Series) -> pd.Series:
    """Bars since last 63d Coppock-annual bearish divergence event."""
    return _bars_since_true(_shift_div_bearish_indicator(close, _coppock_annual(close), QDAYS))


def f33_cpkt_162_coppock_annual_div_count_in_252d(close: pd.Series) -> pd.Series:
    """Count of Coppock-annual 21d bearish-shift divergences within trailing 252d."""
    return _shift_div_bearish_indicator(close, _coppock_annual(close), MDAYS).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket QQ — Coppock-cycle × price divergence (other horizons) (163-174)
# ============================================================

def f33_cpkt_163_coppock_quarterly_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence between log-close and quarterly Coppock, 63d."""
    return _slope_div_sign(close, _coppock_quarterly(close), QDAYS)


def f33_cpkt_164_coppock_quarterly_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on quarterly Coppock, 63d."""
    return _shift_div_bearish_indicator(close, _coppock_quarterly(close), QDAYS)


def f33_cpkt_165_coppock_quarterly_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(close,63) - z(Coppock quarterly,63)."""
    return _zscore_gap(close, _coppock_quarterly(close), QDAYS)


def f33_cpkt_166_coppock_quarterly_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + Coppock-quarterly HH over 63d."""
    return _shift_div_hidden_bearish_indicator(close, _coppock_quarterly(close), QDAYS)


def f33_cpkt_167_coppock_semi_annual_slope_div_sign_126d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on semi-annual Coppock over 126d (matches its half-year horizon)."""
    return _slope_div_sign(close, _coppock_semi_annual(close), 126)


def f33_cpkt_168_coppock_semi_annual_shift_div_indicator_126d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs semi-annual Coppock, 126d."""
    return _shift_div_bearish_indicator(close, _coppock_semi_annual(close), 126)


def f33_cpkt_169_coppock_semi_annual_zscore_gap_126d(close: pd.Series) -> pd.Series:
    """z(log close,126) - z(Coppock semi-annual,126)."""
    return _zscore_gap(close, _coppock_semi_annual(close), 126)


def f33_cpkt_170_coppock_biennial_slope_div_sign_252d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence on biennial Coppock over 252d (secular regime failure)."""
    return _slope_div_sign(close, _coppock_biennial(close), YDAYS)


def f33_cpkt_171_coppock_biennial_shift_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on biennial Coppock, 252d."""
    return _shift_div_bearish_indicator(close, _coppock_biennial(close), YDAYS)


def f33_cpkt_172_coppock_biennial_zscore_gap_252d(close: pd.Series) -> pd.Series:
    """z(log close,252) - z(Coppock biennial,252)."""
    return _zscore_gap(close, _coppock_biennial(close), YDAYS)


def f33_cpkt_173_coppock_biennial_rolling_corr_price_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr of log-close and biennial Coppock — secular agreement."""
    return _rolling_corr_pearson(_safe_log(close), _coppock_biennial(close), YDAYS)


def f33_cpkt_174_coppock_div_breadth_4cycles_63d(close: pd.Series) -> pd.Series:
    """Fraction of 4 Coppock variants (quarterly/semi/annual/biennial) showing bearish slope-div over 63d."""
    parts = [
        (_slope_div_sign(close, _coppock_quarterly(close), QDAYS) > 0).astype(float).rename("a"),
        (_slope_div_sign(close, _coppock_semi_annual(close), QDAYS) > 0).astype(float).rename("b"),
        (_slope_div_sign(close, _coppock_annual(close), QDAYS) > 0).astype(float).rename("c"),
        (_slope_div_sign(close, _coppock_biennial(close), QDAYS) > 0).astype(float).rename("d"),
    ]
    return pd.concat(parts, axis=1).mean(axis=1)


# ============================================================
# Bucket RR — KST × price divergence extended methods (175-180)
# ============================================================

def f33_cpkt_175_kst_long_term_slope_div_sign_252d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs long-term KST, 252d (secular)."""
    return _slope_div_sign(close, _kst_long_term(close), YDAYS)


def f33_cpkt_176_kst_long_term_shift_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on long-term KST, 252d."""
    return _shift_div_bearish_indicator(close, _kst_long_term(close), YDAYS)


def f33_cpkt_177_kst_long_term_zscore_gap_252d(close: pd.Series) -> pd.Series:
    """z(log close,252) - z(KST long-term,252)."""
    return _zscore_gap(close, _kst_long_term(close), YDAYS)


def f33_cpkt_178_kst_slope_div_sign_252d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs standard KST, 252d (long-window vs the original 63d)."""
    return _slope_div_sign(close, _kst(close), YDAYS)


def f33_cpkt_179_kst_div_persistence_63d(close: pd.Series) -> pd.Series:
    """Bars since last 63d KST bearish divergence event."""
    return _bars_since_true(_shift_div_bearish_indicator(close, _kst(close), QDAYS))


def f33_cpkt_180_kst_div_count_in_252d(close: pd.Series) -> pd.Series:
    """Count of standard-KST 21d bearish-shift divergences in trailing 252d."""
    return _shift_div_bearish_indicator(close, _kst(close), MDAYS).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket SS — Pring's Special K (181-186)
# ============================================================

def f33_cpkt_181_special_k_value(close: pd.Series) -> pd.Series:
    """Pring's Special K (8-component daily-adapted): summed weighted ROCs across multiple horizons."""
    return _special_k(close)


def f33_cpkt_182_special_k_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Special K over 252d."""
    return _rolling_zscore(_special_k(close), YDAYS)


def f33_cpkt_183_special_k_slope_sign_change_bearish_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where Special K 63d-slope crosses + → -."""
    s = _rolling_slope(_special_k(close), QDAYS)
    return ((s.shift(1) > 0) & (s <= 0)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)


def f33_cpkt_184_special_k_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs Special K, 63d."""
    return _slope_div_sign(close, _special_k(close), QDAYS)


def f33_cpkt_185_special_k_above_signal_indicator(close: pd.Series) -> pd.Series:
    """+1 when Special K > SMA(10) of itself (above signal line)."""
    sk = _special_k(close)
    return (sk > _sma(sk, 10)).astype(float).where(sk.notna(), np.nan)


def f33_cpkt_186_special_k_peaking_at_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when Special K 21d-slope just flipped negative AND close within 1% of 252d max."""
    sk = _special_k(close)
    s = _rolling_slope(sk, MDAYS)
    flip = ((s.shift(1) > 0) & (s <= 0)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (flip * near).where(s.notna() & near.notna(), np.nan)


# ============================================================
# Bucket TT — DPO at long horizons (187-194)
# ============================================================

def f33_cpkt_187_dpo63_value(close: pd.Series) -> pd.Series:
    """Detrended Price Oscillator at 63d horizon (trailing-SMA-detrended, PIT-safe)."""
    return _dpo(close, QDAYS)


def f33_cpkt_188_dpo126_value(close: pd.Series) -> pd.Series:
    """DPO at 126d horizon — semi-annual cycle."""
    return _dpo(close, 126)


def f33_cpkt_189_dpo252_value(close: pd.Series) -> pd.Series:
    """DPO at 252d horizon — annual cycle."""
    return _dpo(close, YDAYS)


def f33_cpkt_190_dpo63_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of DPO(63) over 252d."""
    return _rolling_zscore(_dpo(close, QDAYS), YDAYS)


def f33_cpkt_191_dpo252_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of DPO(252) over 504d — secular cycle z."""
    return _rolling_zscore(_dpo(close, YDAYS), DDAYS_2Y)


def f33_cpkt_192_dpo63_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs DPO(63), 63d."""
    return _slope_div_sign(close, _dpo(close, QDAYS), QDAYS)


def f33_cpkt_193_dpo252_shift_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence on DPO(252), 252d."""
    return _shift_div_bearish_indicator(close, _dpo(close, YDAYS), YDAYS)


def f33_cpkt_194_dpo63_above_zero_persistence_63d(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where DPO(63) > 0 (positive-cycle density)."""
    return (_dpo(close, QDAYS) > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket UU — DTI (DeMark Trend Indicator) (195-200)
# ============================================================

def f33_cpkt_195_dti_value(close: pd.Series) -> pd.Series:
    """DTI (DeMark Trend Indicator) value."""
    return _dti(close)


def f33_cpkt_196_dti_above_zero_indicator(close: pd.Series) -> pd.Series:
    """+1 when DTI > 0 (positive trend regime)."""
    d = _dti(close)
    return (d > 0).astype(float).where(d.notna(), np.nan)


def f33_cpkt_197_dti_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of DTI over 252d."""
    return _rolling_zscore(_dti(close), YDAYS)


def f33_cpkt_198_dti_slope_63d(close: pd.Series) -> pd.Series:
    """63d slope of DTI."""
    return _rolling_slope(_dti(close), QDAYS)


def f33_cpkt_199_dti_slope_sign_change_bearish_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where DTI 63d-slope crossed + → -."""
    s = _rolling_slope(_dti(close), QDAYS)
    return ((s.shift(1) > 0) & (s <= 0)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)


def f33_cpkt_200_dti_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs DTI, 63d."""
    return _slope_div_sign(close, _dti(close), QDAYS)


# ============================================================
# Bucket VV — VWMA-weighted Coppock (201-206)
# ============================================================

def f33_cpkt_201_vwma_coppock_value(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWMA-weighted Coppock variant (Coppock computed on VWMA63-smoothed close)."""
    return _vwma_coppock(close, volume)


def f33_cpkt_202_vwma_coppock_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of VWMA-Coppock over 252d."""
    return _rolling_zscore(_vwma_coppock(close, volume), YDAYS)


def f33_cpkt_203_vwma_coppock_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of VWMA-Coppock."""
    return _rolling_slope(_vwma_coppock(close, volume), QDAYS)


def f33_cpkt_204_vwma_coppock_vs_std_coppock_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWMA-Coppock minus standard annual Coppock — volume-weighting-effect gauge."""
    return _vwma_coppock(close, volume) - _coppock_annual(close)


def f33_cpkt_205_vwma_coppock_slope_div_sign_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs VWMA-Coppock, 63d."""
    return _slope_div_sign(close, _vwma_coppock(close, volume), QDAYS)


def f33_cpkt_206_vwma_coppock_peak_detected_local21d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when VWMA-Coppock equals trailing 21d-max AND > 3-bar-ago value (local-peak confirmation)."""
    c = _vwma_coppock(close, volume)
    return ((c == c.rolling(MDAYS, min_periods=WDAYS).max()) & (c > c.shift(3))).astype(float).where(c.notna(), np.nan)


# ============================================================
# Bucket WW — TEMA/DEMA/Hull smoothed long-momentum (207-216)
# ============================================================

def f33_cpkt_207_tema_long_momentum_63d_value(close: pd.Series) -> pd.Series:
    """TEMA(63) of ROC(63) — long-cycle triple-EMA-smoothed momentum."""
    return _tema_long_momentum(close, QDAYS)


def f33_cpkt_208_tema_long_momentum_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of TEMA-long-momentum(63) over 252d."""
    return _rolling_zscore(_tema_long_momentum(close, QDAYS), YDAYS)


def f33_cpkt_209_tema_long_momentum_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs TEMA-long-momentum(63), 63d."""
    return _slope_div_sign(close, _tema_long_momentum(close, QDAYS), QDAYS)


def f33_cpkt_210_dema_long_momentum_63d_value(close: pd.Series) -> pd.Series:
    """DEMA(63) of ROC(63)."""
    return _dema_long_momentum(close, QDAYS)


def f33_cpkt_211_dema_long_momentum_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of DEMA-long-momentum(63) over 252d."""
    return _rolling_zscore(_dema_long_momentum(close, QDAYS), YDAYS)


def f33_cpkt_212_dema_long_momentum_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs DEMA-long-momentum(63), 63d."""
    return _slope_div_sign(close, _dema_long_momentum(close, QDAYS), QDAYS)


def f33_cpkt_213_hma_long_momentum_63d_value(close: pd.Series) -> pd.Series:
    """Hull MA(63) of ROC(63) — adaptive smoother."""
    return _hma_long_momentum(close, QDAYS)


def f33_cpkt_214_hma_long_momentum_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Hull-long-momentum(63) over 252d."""
    return _rolling_zscore(_hma_long_momentum(close, QDAYS), YDAYS)


def f33_cpkt_215_hma_long_momentum_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence — close vs Hull-long-momentum(63), 63d."""
    return _slope_div_sign(close, _hma_long_momentum(close, QDAYS), QDAYS)


def f33_cpkt_216_smoothers_agreement_breadth_3types(close: pd.Series) -> pd.Series:
    """Fraction of 3 smoothers (TEMA/DEMA/Hull on ROC63) currently > 0 — smoothed-momentum bullish breadth."""
    parts = [
        (_tema_long_momentum(close, QDAYS) > 0).astype(float).rename("a"),
        (_dema_long_momentum(close, QDAYS) > 0).astype(float).rename("b"),
        (_hma_long_momentum(close, QDAYS) > 0).astype(float).rename("c"),
    ]
    return pd.concat(parts, axis=1).mean(axis=1)


# ============================================================
# Bucket XX — Coppock-on-RSI meta (217-220)
# ============================================================

def f33_cpkt_217_coppock_on_rsi_value(close: pd.Series) -> pd.Series:
    """Coppock applied to RSI(14) directly — second-order momentum."""
    return _coppock_on_rsi(close)


def f33_cpkt_218_coppock_on_rsi_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Coppock-on-RSI over 252d."""
    return _rolling_zscore(_coppock_on_rsi(close), YDAYS)


def f33_cpkt_219_coppock_on_rsi_slope_63d(close: pd.Series) -> pd.Series:
    """63d slope of Coppock-on-RSI."""
    return _rolling_slope(_coppock_on_rsi(close), QDAYS)


def f33_cpkt_220_coppock_on_rsi_above_zero_indicator(close: pd.Series) -> pd.Series:
    """+1 when Coppock-on-RSI > 0."""
    c = _coppock_on_rsi(close)
    return (c > 0).astype(float).where(c.notna(), np.nan)


# ============================================================
# Bucket YY — Cross-indicator composites (221-225)
# ============================================================

def f33_cpkt_221_special_k_x_coppock_annual_agreement_indicator(close: pd.Series) -> pd.Series:
    """+1 when Special K AND annual Coppock are BOTH > 0 (agreement bullish regime — at-high should be exhausted)."""
    sk = _special_k(close); ca = _coppock_annual(close)
    return ((sk > 0) & (ca > 0)).astype(float).where(sk.notna() & ca.notna(), np.nan)


def f33_cpkt_222_dti_x_kst_disagreement_indicator(close: pd.Series) -> pd.Series:
    """+1 when DTI sign != KST sign — regime-disagreement signal."""
    d = _dti(close); k = _kst(close)
    return ((np.sign(d) != np.sign(k)) & d.notna() & k.notna()).astype(float).where(d.notna() & k.notna(), np.nan)


def f33_cpkt_223_dpo_x_coppock_joint_topping_indicator(close: pd.Series) -> pd.Series:
    """+1 when DPO(252) > 0 AND annual Coppock 21d-slope < 0 — cycle peak + Coppock rollover."""
    dpo_pos = (_dpo(close, YDAYS) > 0).astype(float)
    cop_falling = (_rolling_slope(_coppock_annual(close), MDAYS) < 0).astype(float)
    return (dpo_pos * cop_falling).where(dpo_pos.notna() & cop_falling.notna(), np.nan)


def f33_cpkt_224_long_smoothed_momentum_topping_score_extended(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite topping: 0.3*z(Coppock-annual,252) + 0.2*z(KST,252) + 0.2*z(Special K,252)
    + 0.15*z(DTI,252) + 0.15*z(VWMA-Coppock,252)."""
    z_cop = _rolling_zscore(_coppock_annual(close), YDAYS)
    z_kst = _rolling_zscore(_kst(close), YDAYS)
    z_sk = _rolling_zscore(_special_k(close), YDAYS)
    z_dti = _rolling_zscore(_dti(close), YDAYS)
    z_vwc = _rolling_zscore(_vwma_coppock(close, volume), YDAYS)
    return 0.3 * z_cop + 0.2 * z_kst + 0.2 * z_sk + 0.15 * z_dti + 0.15 * z_vwc


def f33_cpkt_225_5indicator_long_momentum_bearish_div_breadth_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 5 long-momentum indicators (Coppock-annual / KST / Special K / DTI / VWMA-Coppock)
    showing bearish slope-divergence vs log-close over 63d."""
    parts = [
        (_slope_div_sign(close, _coppock_annual(close), QDAYS) > 0).astype(float).rename("a"),
        (_slope_div_sign(close, _kst(close), QDAYS) > 0).astype(float).rename("b"),
        (_slope_div_sign(close, _special_k(close), QDAYS) > 0).astype(float).rename("c"),
        (_slope_div_sign(close, _dti(close), QDAYS) > 0).astype(float).rename("d"),
        (_slope_div_sign(close, _vwma_coppock(close, volume), QDAYS) > 0).astype(float).rename("e"),
    ]
    return pd.concat(parts, axis=1).mean(axis=1)


# ============================================================
# REGISTRY
# ============================================================



def f33_cpkt_151_coppock_annual_slope_div_sign_63d_d3(close):
    return f33_cpkt_151_coppock_annual_slope_div_sign_63d(close).diff().diff().diff()


def f33_cpkt_152_coppock_annual_slope_div_sign_252d_d3(close):
    return f33_cpkt_152_coppock_annual_slope_div_sign_252d(close).diff().diff().diff()


def f33_cpkt_153_coppock_annual_shift_div_indicator_63d_d3(close):
    return f33_cpkt_153_coppock_annual_shift_div_indicator_63d(close).diff().diff().diff()


def f33_cpkt_154_coppock_annual_shift_div_indicator_252d_d3(close):
    return f33_cpkt_154_coppock_annual_shift_div_indicator_252d(close).diff().diff().diff()


def f33_cpkt_155_coppock_annual_slope_div_magnitude_63d_d3(close):
    return f33_cpkt_155_coppock_annual_slope_div_magnitude_63d(close).diff().diff().diff()


def f33_cpkt_156_coppock_annual_zscore_gap_63d_d3(close):
    return f33_cpkt_156_coppock_annual_zscore_gap_63d(close).diff().diff().diff()


def f33_cpkt_157_coppock_annual_zscore_gap_252d_d3(close):
    return f33_cpkt_157_coppock_annual_zscore_gap_252d(close).diff().diff().diff()


def f33_cpkt_158_coppock_annual_rolling_corr_price_63d_d3(close):
    return f33_cpkt_158_coppock_annual_rolling_corr_price_63d(close).diff().diff().diff()


def f33_cpkt_159_coppock_annual_rolling_corr_price_252d_d3(close):
    return f33_cpkt_159_coppock_annual_rolling_corr_price_252d(close).diff().diff().diff()


def f33_cpkt_160_coppock_annual_hidden_bearish_div_63d_d3(close):
    return f33_cpkt_160_coppock_annual_hidden_bearish_div_63d(close).diff().diff().diff()


def f33_cpkt_161_coppock_annual_div_persistence_63d_d3(close):
    return f33_cpkt_161_coppock_annual_div_persistence_63d(close).diff().diff().diff()


def f33_cpkt_162_coppock_annual_div_count_in_252d_d3(close):
    return f33_cpkt_162_coppock_annual_div_count_in_252d(close).diff().diff().diff()


def f33_cpkt_163_coppock_quarterly_slope_div_sign_63d_d3(close):
    return f33_cpkt_163_coppock_quarterly_slope_div_sign_63d(close).diff().diff().diff()


def f33_cpkt_164_coppock_quarterly_shift_div_indicator_63d_d3(close):
    return f33_cpkt_164_coppock_quarterly_shift_div_indicator_63d(close).diff().diff().diff()


def f33_cpkt_165_coppock_quarterly_zscore_gap_63d_d3(close):
    return f33_cpkt_165_coppock_quarterly_zscore_gap_63d(close).diff().diff().diff()


def f33_cpkt_166_coppock_quarterly_hidden_bearish_div_63d_d3(close):
    return f33_cpkt_166_coppock_quarterly_hidden_bearish_div_63d(close).diff().diff().diff()


def f33_cpkt_167_coppock_semi_annual_slope_div_sign_126d_d3(close):
    return f33_cpkt_167_coppock_semi_annual_slope_div_sign_126d(close).diff().diff().diff()


def f33_cpkt_168_coppock_semi_annual_shift_div_indicator_126d_d3(close):
    return f33_cpkt_168_coppock_semi_annual_shift_div_indicator_126d(close).diff().diff().diff()


def f33_cpkt_169_coppock_semi_annual_zscore_gap_126d_d3(close):
    return f33_cpkt_169_coppock_semi_annual_zscore_gap_126d(close).diff().diff().diff()


def f33_cpkt_170_coppock_biennial_slope_div_sign_252d_d3(close):
    return f33_cpkt_170_coppock_biennial_slope_div_sign_252d(close).diff().diff().diff()


def f33_cpkt_171_coppock_biennial_shift_div_indicator_252d_d3(close):
    return f33_cpkt_171_coppock_biennial_shift_div_indicator_252d(close).diff().diff().diff()


def f33_cpkt_172_coppock_biennial_zscore_gap_252d_d3(close):
    return f33_cpkt_172_coppock_biennial_zscore_gap_252d(close).diff().diff().diff()


def f33_cpkt_173_coppock_biennial_rolling_corr_price_252d_d3(close):
    return f33_cpkt_173_coppock_biennial_rolling_corr_price_252d(close).diff().diff().diff()


def f33_cpkt_174_coppock_div_breadth_4cycles_63d_d3(close):
    return f33_cpkt_174_coppock_div_breadth_4cycles_63d(close).diff().diff().diff()


def f33_cpkt_175_kst_long_term_slope_div_sign_252d_d3(close):
    return f33_cpkt_175_kst_long_term_slope_div_sign_252d(close).diff().diff().diff()


def f33_cpkt_176_kst_long_term_shift_div_indicator_252d_d3(close):
    return f33_cpkt_176_kst_long_term_shift_div_indicator_252d(close).diff().diff().diff()


def f33_cpkt_177_kst_long_term_zscore_gap_252d_d3(close):
    return f33_cpkt_177_kst_long_term_zscore_gap_252d(close).diff().diff().diff()


def f33_cpkt_178_kst_slope_div_sign_252d_d3(close):
    return f33_cpkt_178_kst_slope_div_sign_252d(close).diff().diff().diff()


def f33_cpkt_179_kst_div_persistence_63d_d3(close):
    return f33_cpkt_179_kst_div_persistence_63d(close).diff().diff().diff()


def f33_cpkt_180_kst_div_count_in_252d_d3(close):
    return f33_cpkt_180_kst_div_count_in_252d(close).diff().diff().diff()


def f33_cpkt_181_special_k_value_d3(close):
    return f33_cpkt_181_special_k_value(close).diff().diff().diff()


def f33_cpkt_182_special_k_zscore_252d_d3(close):
    return f33_cpkt_182_special_k_zscore_252d(close).diff().diff().diff()


def f33_cpkt_183_special_k_slope_sign_change_bearish_indicator_d3(close):
    return f33_cpkt_183_special_k_slope_sign_change_bearish_indicator(close).diff().diff().diff()


def f33_cpkt_184_special_k_slope_div_sign_63d_d3(close):
    return f33_cpkt_184_special_k_slope_div_sign_63d(close).diff().diff().diff()


def f33_cpkt_185_special_k_above_signal_indicator_d3(close):
    return f33_cpkt_185_special_k_above_signal_indicator(close).diff().diff().diff()


def f33_cpkt_186_special_k_peaking_at_252d_high_indicator_d3(close):
    return f33_cpkt_186_special_k_peaking_at_252d_high_indicator(close).diff().diff().diff()


def f33_cpkt_187_dpo63_value_d3(close):
    return f33_cpkt_187_dpo63_value(close).diff().diff().diff()


def f33_cpkt_188_dpo126_value_d3(close):
    return f33_cpkt_188_dpo126_value(close).diff().diff().diff()


def f33_cpkt_189_dpo252_value_d3(close):
    return f33_cpkt_189_dpo252_value(close).diff().diff().diff()


def f33_cpkt_190_dpo63_zscore_252d_d3(close):
    return f33_cpkt_190_dpo63_zscore_252d(close).diff().diff().diff()


def f33_cpkt_191_dpo252_zscore_504d_d3(close):
    return f33_cpkt_191_dpo252_zscore_504d(close).diff().diff().diff()


def f33_cpkt_192_dpo63_slope_div_sign_63d_d3(close):
    return f33_cpkt_192_dpo63_slope_div_sign_63d(close).diff().diff().diff()


def f33_cpkt_193_dpo252_shift_div_indicator_252d_d3(close):
    return f33_cpkt_193_dpo252_shift_div_indicator_252d(close).diff().diff().diff()


def f33_cpkt_194_dpo63_above_zero_persistence_63d_d3(close):
    return f33_cpkt_194_dpo63_above_zero_persistence_63d(close).diff().diff().diff()


def f33_cpkt_195_dti_value_d3(close):
    return f33_cpkt_195_dti_value(close).diff().diff().diff()


def f33_cpkt_196_dti_above_zero_indicator_d3(close):
    return f33_cpkt_196_dti_above_zero_indicator(close).diff().diff().diff()


def f33_cpkt_197_dti_zscore_252d_d3(close):
    return f33_cpkt_197_dti_zscore_252d(close).diff().diff().diff()


def f33_cpkt_198_dti_slope_63d_d3(close):
    return f33_cpkt_198_dti_slope_63d(close).diff().diff().diff()


def f33_cpkt_199_dti_slope_sign_change_bearish_indicator_d3(close):
    return f33_cpkt_199_dti_slope_sign_change_bearish_indicator(close).diff().diff().diff()


def f33_cpkt_200_dti_slope_div_sign_63d_d3(close):
    return f33_cpkt_200_dti_slope_div_sign_63d(close).diff().diff().diff()


def f33_cpkt_201_vwma_coppock_value_d3(close, volume):
    return f33_cpkt_201_vwma_coppock_value(close, volume).diff().diff().diff()


def f33_cpkt_202_vwma_coppock_zscore_252d_d3(close, volume):
    return f33_cpkt_202_vwma_coppock_zscore_252d(close, volume).diff().diff().diff()


def f33_cpkt_203_vwma_coppock_slope_63d_d3(close, volume):
    return f33_cpkt_203_vwma_coppock_slope_63d(close, volume).diff().diff().diff()


def f33_cpkt_204_vwma_coppock_vs_std_coppock_diff_d3(close, volume):
    return f33_cpkt_204_vwma_coppock_vs_std_coppock_diff(close, volume).diff().diff().diff()


def f33_cpkt_205_vwma_coppock_slope_div_sign_63d_d3(close, volume):
    return f33_cpkt_205_vwma_coppock_slope_div_sign_63d(close, volume).diff().diff().diff()


def f33_cpkt_206_vwma_coppock_peak_detected_local21d_indicator_d3(close, volume):
    return f33_cpkt_206_vwma_coppock_peak_detected_local21d_indicator(close, volume).diff().diff().diff()


def f33_cpkt_207_tema_long_momentum_63d_value_d3(close):
    return f33_cpkt_207_tema_long_momentum_63d_value(close).diff().diff().diff()


def f33_cpkt_208_tema_long_momentum_zscore_252d_d3(close):
    return f33_cpkt_208_tema_long_momentum_zscore_252d(close).diff().diff().diff()


def f33_cpkt_209_tema_long_momentum_slope_div_sign_63d_d3(close):
    return f33_cpkt_209_tema_long_momentum_slope_div_sign_63d(close).diff().diff().diff()


def f33_cpkt_210_dema_long_momentum_63d_value_d3(close):
    return f33_cpkt_210_dema_long_momentum_63d_value(close).diff().diff().diff()


def f33_cpkt_211_dema_long_momentum_zscore_252d_d3(close):
    return f33_cpkt_211_dema_long_momentum_zscore_252d(close).diff().diff().diff()


def f33_cpkt_212_dema_long_momentum_slope_div_sign_63d_d3(close):
    return f33_cpkt_212_dema_long_momentum_slope_div_sign_63d(close).diff().diff().diff()


def f33_cpkt_213_hma_long_momentum_63d_value_d3(close):
    return f33_cpkt_213_hma_long_momentum_63d_value(close).diff().diff().diff()


def f33_cpkt_214_hma_long_momentum_zscore_252d_d3(close):
    return f33_cpkt_214_hma_long_momentum_zscore_252d(close).diff().diff().diff()


def f33_cpkt_215_hma_long_momentum_slope_div_sign_63d_d3(close):
    return f33_cpkt_215_hma_long_momentum_slope_div_sign_63d(close).diff().diff().diff()


def f33_cpkt_216_smoothers_agreement_breadth_3types_d3(close):
    return f33_cpkt_216_smoothers_agreement_breadth_3types(close).diff().diff().diff()


def f33_cpkt_217_coppock_on_rsi_value_d3(close):
    return f33_cpkt_217_coppock_on_rsi_value(close).diff().diff().diff()


def f33_cpkt_218_coppock_on_rsi_zscore_252d_d3(close):
    return f33_cpkt_218_coppock_on_rsi_zscore_252d(close).diff().diff().diff()


def f33_cpkt_219_coppock_on_rsi_slope_63d_d3(close):
    return f33_cpkt_219_coppock_on_rsi_slope_63d(close).diff().diff().diff()


def f33_cpkt_220_coppock_on_rsi_above_zero_indicator_d3(close):
    return f33_cpkt_220_coppock_on_rsi_above_zero_indicator(close).diff().diff().diff()


def f33_cpkt_221_special_k_x_coppock_annual_agreement_indicator_d3(close):
    return f33_cpkt_221_special_k_x_coppock_annual_agreement_indicator(close).diff().diff().diff()


def f33_cpkt_222_dti_x_kst_disagreement_indicator_d3(close):
    return f33_cpkt_222_dti_x_kst_disagreement_indicator(close).diff().diff().diff()


def f33_cpkt_223_dpo_x_coppock_joint_topping_indicator_d3(close):
    return f33_cpkt_223_dpo_x_coppock_joint_topping_indicator(close).diff().diff().diff()


def f33_cpkt_224_long_smoothed_momentum_topping_score_extended_d3(close, volume):
    return f33_cpkt_224_long_smoothed_momentum_topping_score_extended(close, volume).diff().diff().diff()


def f33_cpkt_225_5indicator_long_momentum_bearish_div_breadth_63d_d3(close, volume):
    return f33_cpkt_225_5indicator_long_momentum_bearish_div_breadth_63d(close, volume).diff().diff().diff()


COPPOCK_CURVE_KST_D3_REGISTRY_151_225 = {
    "f33_cpkt_151_coppock_annual_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f33_cpkt_151_coppock_annual_slope_div_sign_63d_d3},
    "f33_cpkt_152_coppock_annual_slope_div_sign_252d_d3": {"inputs": ["close"], "func": f33_cpkt_152_coppock_annual_slope_div_sign_252d_d3},
    "f33_cpkt_153_coppock_annual_shift_div_indicator_63d_d3": {"inputs": ["close"], "func": f33_cpkt_153_coppock_annual_shift_div_indicator_63d_d3},
    "f33_cpkt_154_coppock_annual_shift_div_indicator_252d_d3": {"inputs": ["close"], "func": f33_cpkt_154_coppock_annual_shift_div_indicator_252d_d3},
    "f33_cpkt_155_coppock_annual_slope_div_magnitude_63d_d3": {"inputs": ["close"], "func": f33_cpkt_155_coppock_annual_slope_div_magnitude_63d_d3},
    "f33_cpkt_156_coppock_annual_zscore_gap_63d_d3": {"inputs": ["close"], "func": f33_cpkt_156_coppock_annual_zscore_gap_63d_d3},
    "f33_cpkt_157_coppock_annual_zscore_gap_252d_d3": {"inputs": ["close"], "func": f33_cpkt_157_coppock_annual_zscore_gap_252d_d3},
    "f33_cpkt_158_coppock_annual_rolling_corr_price_63d_d3": {"inputs": ["close"], "func": f33_cpkt_158_coppock_annual_rolling_corr_price_63d_d3},
    "f33_cpkt_159_coppock_annual_rolling_corr_price_252d_d3": {"inputs": ["close"], "func": f33_cpkt_159_coppock_annual_rolling_corr_price_252d_d3},
    "f33_cpkt_160_coppock_annual_hidden_bearish_div_63d_d3": {"inputs": ["close"], "func": f33_cpkt_160_coppock_annual_hidden_bearish_div_63d_d3},
    "f33_cpkt_161_coppock_annual_div_persistence_63d_d3": {"inputs": ["close"], "func": f33_cpkt_161_coppock_annual_div_persistence_63d_d3},
    "f33_cpkt_162_coppock_annual_div_count_in_252d_d3": {"inputs": ["close"], "func": f33_cpkt_162_coppock_annual_div_count_in_252d_d3},
    "f33_cpkt_163_coppock_quarterly_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f33_cpkt_163_coppock_quarterly_slope_div_sign_63d_d3},
    "f33_cpkt_164_coppock_quarterly_shift_div_indicator_63d_d3": {"inputs": ["close"], "func": f33_cpkt_164_coppock_quarterly_shift_div_indicator_63d_d3},
    "f33_cpkt_165_coppock_quarterly_zscore_gap_63d_d3": {"inputs": ["close"], "func": f33_cpkt_165_coppock_quarterly_zscore_gap_63d_d3},
    "f33_cpkt_166_coppock_quarterly_hidden_bearish_div_63d_d3": {"inputs": ["close"], "func": f33_cpkt_166_coppock_quarterly_hidden_bearish_div_63d_d3},
    "f33_cpkt_167_coppock_semi_annual_slope_div_sign_126d_d3": {"inputs": ["close"], "func": f33_cpkt_167_coppock_semi_annual_slope_div_sign_126d_d3},
    "f33_cpkt_168_coppock_semi_annual_shift_div_indicator_126d_d3": {"inputs": ["close"], "func": f33_cpkt_168_coppock_semi_annual_shift_div_indicator_126d_d3},
    "f33_cpkt_169_coppock_semi_annual_zscore_gap_126d_d3": {"inputs": ["close"], "func": f33_cpkt_169_coppock_semi_annual_zscore_gap_126d_d3},
    "f33_cpkt_170_coppock_biennial_slope_div_sign_252d_d3": {"inputs": ["close"], "func": f33_cpkt_170_coppock_biennial_slope_div_sign_252d_d3},
    "f33_cpkt_171_coppock_biennial_shift_div_indicator_252d_d3": {"inputs": ["close"], "func": f33_cpkt_171_coppock_biennial_shift_div_indicator_252d_d3},
    "f33_cpkt_172_coppock_biennial_zscore_gap_252d_d3": {"inputs": ["close"], "func": f33_cpkt_172_coppock_biennial_zscore_gap_252d_d3},
    "f33_cpkt_173_coppock_biennial_rolling_corr_price_252d_d3": {"inputs": ["close"], "func": f33_cpkt_173_coppock_biennial_rolling_corr_price_252d_d3},
    "f33_cpkt_174_coppock_div_breadth_4cycles_63d_d3": {"inputs": ["close"], "func": f33_cpkt_174_coppock_div_breadth_4cycles_63d_d3},
    "f33_cpkt_175_kst_long_term_slope_div_sign_252d_d3": {"inputs": ["close"], "func": f33_cpkt_175_kst_long_term_slope_div_sign_252d_d3},
    "f33_cpkt_176_kst_long_term_shift_div_indicator_252d_d3": {"inputs": ["close"], "func": f33_cpkt_176_kst_long_term_shift_div_indicator_252d_d3},
    "f33_cpkt_177_kst_long_term_zscore_gap_252d_d3": {"inputs": ["close"], "func": f33_cpkt_177_kst_long_term_zscore_gap_252d_d3},
    "f33_cpkt_178_kst_slope_div_sign_252d_d3": {"inputs": ["close"], "func": f33_cpkt_178_kst_slope_div_sign_252d_d3},
    "f33_cpkt_179_kst_div_persistence_63d_d3": {"inputs": ["close"], "func": f33_cpkt_179_kst_div_persistence_63d_d3},
    "f33_cpkt_180_kst_div_count_in_252d_d3": {"inputs": ["close"], "func": f33_cpkt_180_kst_div_count_in_252d_d3},
    "f33_cpkt_181_special_k_value_d3": {"inputs": ["close"], "func": f33_cpkt_181_special_k_value_d3},
    "f33_cpkt_182_special_k_zscore_252d_d3": {"inputs": ["close"], "func": f33_cpkt_182_special_k_zscore_252d_d3},
    "f33_cpkt_183_special_k_slope_sign_change_bearish_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_183_special_k_slope_sign_change_bearish_indicator_d3},
    "f33_cpkt_184_special_k_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f33_cpkt_184_special_k_slope_div_sign_63d_d3},
    "f33_cpkt_185_special_k_above_signal_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_185_special_k_above_signal_indicator_d3},
    "f33_cpkt_186_special_k_peaking_at_252d_high_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_186_special_k_peaking_at_252d_high_indicator_d3},
    "f33_cpkt_187_dpo63_value_d3": {"inputs": ["close"], "func": f33_cpkt_187_dpo63_value_d3},
    "f33_cpkt_188_dpo126_value_d3": {"inputs": ["close"], "func": f33_cpkt_188_dpo126_value_d3},
    "f33_cpkt_189_dpo252_value_d3": {"inputs": ["close"], "func": f33_cpkt_189_dpo252_value_d3},
    "f33_cpkt_190_dpo63_zscore_252d_d3": {"inputs": ["close"], "func": f33_cpkt_190_dpo63_zscore_252d_d3},
    "f33_cpkt_191_dpo252_zscore_504d_d3": {"inputs": ["close"], "func": f33_cpkt_191_dpo252_zscore_504d_d3},
    "f33_cpkt_192_dpo63_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f33_cpkt_192_dpo63_slope_div_sign_63d_d3},
    "f33_cpkt_193_dpo252_shift_div_indicator_252d_d3": {"inputs": ["close"], "func": f33_cpkt_193_dpo252_shift_div_indicator_252d_d3},
    "f33_cpkt_194_dpo63_above_zero_persistence_63d_d3": {"inputs": ["close"], "func": f33_cpkt_194_dpo63_above_zero_persistence_63d_d3},
    "f33_cpkt_195_dti_value_d3": {"inputs": ["close"], "func": f33_cpkt_195_dti_value_d3},
    "f33_cpkt_196_dti_above_zero_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_196_dti_above_zero_indicator_d3},
    "f33_cpkt_197_dti_zscore_252d_d3": {"inputs": ["close"], "func": f33_cpkt_197_dti_zscore_252d_d3},
    "f33_cpkt_198_dti_slope_63d_d3": {"inputs": ["close"], "func": f33_cpkt_198_dti_slope_63d_d3},
    "f33_cpkt_199_dti_slope_sign_change_bearish_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_199_dti_slope_sign_change_bearish_indicator_d3},
    "f33_cpkt_200_dti_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f33_cpkt_200_dti_slope_div_sign_63d_d3},
    "f33_cpkt_201_vwma_coppock_value_d3": {"inputs": ["close", "volume"], "func": f33_cpkt_201_vwma_coppock_value_d3},
    "f33_cpkt_202_vwma_coppock_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f33_cpkt_202_vwma_coppock_zscore_252d_d3},
    "f33_cpkt_203_vwma_coppock_slope_63d_d3": {"inputs": ["close", "volume"], "func": f33_cpkt_203_vwma_coppock_slope_63d_d3},
    "f33_cpkt_204_vwma_coppock_vs_std_coppock_diff_d3": {"inputs": ["close", "volume"], "func": f33_cpkt_204_vwma_coppock_vs_std_coppock_diff_d3},
    "f33_cpkt_205_vwma_coppock_slope_div_sign_63d_d3": {"inputs": ["close", "volume"], "func": f33_cpkt_205_vwma_coppock_slope_div_sign_63d_d3},
    "f33_cpkt_206_vwma_coppock_peak_detected_local21d_indicator_d3": {"inputs": ["close", "volume"], "func": f33_cpkt_206_vwma_coppock_peak_detected_local21d_indicator_d3},
    "f33_cpkt_207_tema_long_momentum_63d_value_d3": {"inputs": ["close"], "func": f33_cpkt_207_tema_long_momentum_63d_value_d3},
    "f33_cpkt_208_tema_long_momentum_zscore_252d_d3": {"inputs": ["close"], "func": f33_cpkt_208_tema_long_momentum_zscore_252d_d3},
    "f33_cpkt_209_tema_long_momentum_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f33_cpkt_209_tema_long_momentum_slope_div_sign_63d_d3},
    "f33_cpkt_210_dema_long_momentum_63d_value_d3": {"inputs": ["close"], "func": f33_cpkt_210_dema_long_momentum_63d_value_d3},
    "f33_cpkt_211_dema_long_momentum_zscore_252d_d3": {"inputs": ["close"], "func": f33_cpkt_211_dema_long_momentum_zscore_252d_d3},
    "f33_cpkt_212_dema_long_momentum_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f33_cpkt_212_dema_long_momentum_slope_div_sign_63d_d3},
    "f33_cpkt_213_hma_long_momentum_63d_value_d3": {"inputs": ["close"], "func": f33_cpkt_213_hma_long_momentum_63d_value_d3},
    "f33_cpkt_214_hma_long_momentum_zscore_252d_d3": {"inputs": ["close"], "func": f33_cpkt_214_hma_long_momentum_zscore_252d_d3},
    "f33_cpkt_215_hma_long_momentum_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f33_cpkt_215_hma_long_momentum_slope_div_sign_63d_d3},
    "f33_cpkt_216_smoothers_agreement_breadth_3types_d3": {"inputs": ["close"], "func": f33_cpkt_216_smoothers_agreement_breadth_3types_d3},
    "f33_cpkt_217_coppock_on_rsi_value_d3": {"inputs": ["close"], "func": f33_cpkt_217_coppock_on_rsi_value_d3},
    "f33_cpkt_218_coppock_on_rsi_zscore_252d_d3": {"inputs": ["close"], "func": f33_cpkt_218_coppock_on_rsi_zscore_252d_d3},
    "f33_cpkt_219_coppock_on_rsi_slope_63d_d3": {"inputs": ["close"], "func": f33_cpkt_219_coppock_on_rsi_slope_63d_d3},
    "f33_cpkt_220_coppock_on_rsi_above_zero_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_220_coppock_on_rsi_above_zero_indicator_d3},
    "f33_cpkt_221_special_k_x_coppock_annual_agreement_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_221_special_k_x_coppock_annual_agreement_indicator_d3},
    "f33_cpkt_222_dti_x_kst_disagreement_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_222_dti_x_kst_disagreement_indicator_d3},
    "f33_cpkt_223_dpo_x_coppock_joint_topping_indicator_d3": {"inputs": ["close"], "func": f33_cpkt_223_dpo_x_coppock_joint_topping_indicator_d3},
    "f33_cpkt_224_long_smoothed_momentum_topping_score_extended_d3": {"inputs": ["close", "volume"], "func": f33_cpkt_224_long_smoothed_momentum_topping_score_extended_d3},
    "f33_cpkt_225_5indicator_long_momentum_bearish_div_breadth_63d_d3": {"inputs": ["close", "volume"], "func": f33_cpkt_225_5indicator_long_momentum_bearish_div_breadth_63d_d3},
}
