"""trix_tsi_cci_family base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py.
Bucket A: TRIX (triple-smoothed momentum) variants.
Bucket B: TSI (True Strength Index) variants.
Bucket C: CCI (Commodity Channel Index) variants.
Bucket D: DPO (Detrended Price Oscillator) variants.
Bucket E: KST (Pring's Know Sure Thing) variants.
Bucket F: CMO (Chande Momentum Oscillator) variants.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers.
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()


def _trix(close, n=15):
    e1 = _ema(close, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 100.0 * e3.pct_change()


def _tsi(close, n1=25, n2=13):
    m = close.diff()
    e1 = _ema(m, n1)
    e2 = _ema(e1, n2)
    a1 = _ema(m.abs(), n1)
    a2 = _ema(a1, n2)
    return 100.0 * _safe_div(e2, a2)


def _cci(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(tp - sma, 0.015 * mad)


def _dpo(close, n=20):
    sma = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return close - sma.shift(n // 2 + 1)


def _kst(close):
    roc10 = close.pct_change(10)
    roc15 = close.pct_change(15)
    roc20 = close.pct_change(20)
    roc30 = close.pct_change(30)
    r1 = roc10.rolling(10, min_periods=5).mean()
    r2 = roc15.rolling(10, min_periods=5).mean()
    r3 = roc20.rolling(10, min_periods=5).mean()
    r4 = roc30.rolling(15, min_periods=8).mean()
    return r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4


def _cmo(close, n=14):
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    su = up.rolling(n, min_periods=max(n // 3, 2)).sum()
    sd = dn.rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(su - sd, su + sd)


def _bars_since_true(mask: pd.Series) -> pd.Series:
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


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# Bucket A — TRIX variants (001-013)
# ============================================================

def f28_ttcf_001_trix_15(close: pd.Series) -> pd.Series:
    """Classical TRIX(15) — % change of triple-EMA-smoothed close (cycle-period filter)."""
    return _trix(close, 15)


def f28_ttcf_002_trix_signal_9(close: pd.Series) -> pd.Series:
    """TRIX(15) signal line = EMA9 of TRIX."""
    return _ema(_trix(close, 15), 9)


def f28_ttcf_003_trix_histogram(close: pd.Series) -> pd.Series:
    """TRIX(15) - signal — momentum-of-TRIX."""
    t = _trix(close, 15)
    return t - _ema(t, 9)


def f28_ttcf_004_trix_30_long(close: pd.Series) -> pd.Series:
    """Long-cycle TRIX(30) — slower triple-smoothed momentum (distinct cycle hypothesis)."""
    return _trix(close, 30)


def f28_ttcf_005_trix_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if TRIX(15) > 0 — bullish triple-smoothed-trend regime."""
    t = _trix(close, 15)
    return (t > 0).astype(float).where(t.notna(), np.nan)


def f28_ttcf_006_trix_signal_bearish_cross_indicator(close: pd.Series) -> pd.Series:
    """1 if TRIX crossed below its signal — TRIX bearish cross trigger."""
    t = _trix(close, 15)
    s = _ema(t, 9)
    d = t - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f28_ttcf_007_trix_zero_cross_down_indicator(close: pd.Series) -> pd.Series:
    """1 if TRIX crossed below zero this bar — TRIX zero-line trigger."""
    t = _trix(close, 15)
    return ((t.shift(1) >= 0) & (t < 0)).astype(float).where(t.notna(), np.nan)


def f28_ttcf_008_trix_peak_decay_63(close: pd.Series) -> pd.Series:
    """TRIX 63d max - TRIX from 63 bars ago — quarterly TRIX peak decay."""
    t = _trix(close, 15)
    pmax = t.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f28_ttcf_009_trix_bars_since_252_max(close: pd.Series) -> pd.Series:
    """Bars since TRIX hit its 252d max — TRIX peak recency."""
    t = _trix(close, 15)
    at_max = t == t.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f28_ttcf_010_trix_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TRIX divergence vs price (63d horizon): new 63d high but TRIX below prior 63d TRIX max."""
    t = _trix(close, 15)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    t_below = t < t.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & t_below).astype(float).where(t.notna(), np.nan)


def f28_ttcf_011_trix_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of TRIX over 252d — distribution-based TRIX position."""
    return _rolling_zscore(_trix(close, 15), YDAYS, min_periods=QDAYS)


def f28_ttcf_012_trix_persistence_above_zero_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with TRIX > 0 — annual bullish-cycle dwell."""
    t = _trix(close, 15)
    return (t > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(t.notna(), np.nan)


def f28_ttcf_013_trix_slope_neg_at_price_252_high_state(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d slope of TRIX < 0 AND price at 252d max — TRIX cooling at price peak."""
    t = _trix(close, 15)
    sl = _rolling_slope(t, MDAYS)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((sl < 0) & at_max).astype(float).where(sl.notna(), np.nan)


# ============================================================
# Bucket B — TSI variants (014-025)
# ============================================================

def f28_ttcf_014_tsi_25_13(close: pd.Series) -> pd.Series:
    """Classical TSI(25, 13) — double-smoothed signed momentum."""
    return _tsi(close, 25, 13)


def f28_ttcf_015_tsi_signal_7(close: pd.Series) -> pd.Series:
    """TSI signal line = EMA7 of TSI."""
    return _ema(_tsi(close, 25, 13), 7)


def f28_ttcf_016_tsi_histogram(close: pd.Series) -> pd.Series:
    """TSI - signal — momentum-of-TSI."""
    t = _tsi(close, 25, 13)
    return t - _ema(t, 7)


def f28_ttcf_017_tsi_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if TSI > 0 — bullish double-smoothed-momentum regime."""
    t = _tsi(close, 25, 13)
    return (t > 0).astype(float).where(t.notna(), np.nan)


def f28_ttcf_018_tsi_signal_bearish_cross_indicator(close: pd.Series) -> pd.Series:
    """1 if TSI crossed below its signal — TSI bearish cross trigger."""
    t = _tsi(close, 25, 13)
    s = _ema(t, 7)
    d = t - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f28_ttcf_019_tsi_above_25_state(close: pd.Series) -> pd.Series:
    """1 if TSI > 25 — TSI OB threshold (asymmetric since TSI rarely exceeds 50)."""
    t = _tsi(close, 25, 13)
    return (t > 25.0).astype(float).where(t.notna(), np.nan)


def f28_ttcf_020_tsi_just_exited_above_25(close: pd.Series) -> pd.Series:
    """1 if TSI crossed back below 25 this bar — TSI OB exit trigger."""
    t = _tsi(close, 25, 13)
    return ((t.shift(1) > 25.0) & (t <= 25.0)).astype(float).where(t.notna(), np.nan)


def f28_ttcf_021_tsi_dwell_above_25_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with TSI > 25 — quarterly TSI OB dwell."""
    t = _tsi(close, 25, 13)
    return (t > 25.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(t.notna(), np.nan)


def f28_ttcf_022_tsi_bars_since_252_max(close: pd.Series) -> pd.Series:
    """Bars since TSI hit its 252d max — TSI peak recency."""
    t = _tsi(close, 25, 13)
    at_max = t == t.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f28_ttcf_023_tsi_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of TSI over 252d — distribution-based TSI position."""
    return _rolling_zscore(_tsi(close, 25, 13), YDAYS, min_periods=QDAYS)


def f28_ttcf_024_tsi_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish TSI divergence vs price (63d horizon)."""
    t = _tsi(close, 25, 13)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    t_below = t < t.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & t_below).astype(float).where(t.notna(), np.nan)


def f28_ttcf_025_tsi_persistence_above_zero_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with TSI > 0 — annual double-smoothed-bullish dwell."""
    t = _tsi(close, 25, 13)
    return (t > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(t.notna(), np.nan)


# ============================================================
# Bucket C — CCI variants (026-040)
# ============================================================

def f28_ttcf_026_cci_20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical CCI(20) — typical-price deviation from SMA normalized by MAD."""
    return _cci(high, low, close, 20)


def f28_ttcf_027_cci_50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(50) — medium-horizon deviation (distinct concept)."""
    return _cci(high, low, close, 50)


def f28_ttcf_028_cci_above_100_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if CCI(20) > 100 — classical CCI OB."""
    c = _cci(high, low, close, 20)
    return (c > 100.0).astype(float).where(c.notna(), np.nan)


def f28_ttcf_029_cci_above_200_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if CCI(20) > 200 — extreme CCI OB."""
    c = _cci(high, low, close, 20)
    return (c > 200.0).astype(float).where(c.notna(), np.nan)


def f28_ttcf_030_cci_just_exited_above_100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if CCI(20) crossed back below 100 — CCI OB-exit trigger."""
    c = _cci(high, low, close, 20)
    return ((c.shift(1) > 100.0) & (c <= 100.0)).astype(float).where(c.notna(), np.nan)


def f28_ttcf_031_cci_just_exited_above_200(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if CCI(20) crossed back below 200 — extreme-OB exit trigger."""
    c = _cci(high, low, close, 20)
    return ((c.shift(1) > 200.0) & (c <= 200.0)).astype(float).where(c.notna(), np.nan)


def f28_ttcf_032_cci_dwell_above_100_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with CCI > 100 — quarterly CCI OB dwell."""
    c = _cci(high, low, close, 20)
    return (c > 100.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan)


def f28_ttcf_033_cci_dwell_above_100_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with CCI > 100 — annual CCI OB dwell."""
    c = _cci(high, low, close, 20)
    return (c > 100.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(c.notna(), np.nan)


def f28_ttcf_034_cci_bars_since_252_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since CCI hit its 252d max — CCI peak recency."""
    c = _cci(high, low, close, 20)
    at_max = c == c.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f28_ttcf_035_cci_div_vs_price_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CCI divergence vs price (63d horizon)."""
    c = _cci(high, low, close, 20)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    c_below = c < c.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & c_below).astype(float).where(c.notna(), np.nan)


def f28_ttcf_036_cci_div_vs_price_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CCI divergence vs price (annual horizon)."""
    c = _cci(high, low, close, 20)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    c_below = c < c.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & c_below).astype(float).where(c.notna(), np.nan)


def f28_ttcf_037_cci_count_ob100_exits_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of CCI OB-100 exits in past 252 — annual CCI turnover frequency."""
    c = _cci(high, low, close, 20)
    ev = ((c.shift(1) > 100.0) & (c <= 100.0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(c.notna(), np.nan)


def f28_ttcf_038_cci_persistence_above_q90_dist_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with CCI above its 252d 90th percentile — distribution-OB persistence."""
    c = _cci(high, low, close, 20)
    q = c.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (c > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(c.notna() & q.notna(), np.nan)


def f28_ttcf_039_cci_peak_decay_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI 63d max - CCI from 63 bars ago — quarterly CCI peak decay."""
    c = _cci(high, low, close, 20)
    pmax = c.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f28_ttcf_040_cci_above_q99_dist_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if CCI above its 252d 99th percentile — extreme distribution-CCI OB."""
    c = _cci(high, low, close, 20)
    q = c.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return (c > q).astype(float).where(c.notna() & q.notna(), np.nan)


# ============================================================
# Bucket D — DPO variants (041-050)
# ============================================================

def f28_ttcf_041_dpo_21(close: pd.Series) -> pd.Series:
    """DPO(21) — monthly detrended price oscillator (cycle-isolation)."""
    return _dpo(close, MDAYS)


def f28_ttcf_042_dpo_63(close: pd.Series) -> pd.Series:
    """DPO(63) — quarterly detrended price oscillator (distinct cycle)."""
    return _dpo(close, QDAYS)


def f28_ttcf_043_dpo_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if DPO(21) > 0 — price above its displaced past mean (cycle-peak state)."""
    d = _dpo(close, MDAYS)
    return (d > 0).astype(float).where(d.notna(), np.nan)


def f28_ttcf_044_dpo_above_q90_dist_252(close: pd.Series) -> pd.Series:
    """1 if DPO above its 252d 90th percentile — distribution-DPO OB."""
    d = _dpo(close, MDAYS)
    q = d.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (d > q).astype(float).where(d.notna() & q.notna(), np.nan)


def f28_ttcf_045_dpo_just_crossed_below_zero(close: pd.Series) -> pd.Series:
    """1 if DPO crossed below zero this bar — cycle-peak rollover trigger."""
    d = _dpo(close, MDAYS)
    return ((d.shift(1) >= 0) & (d < 0)).astype(float).where(d.notna(), np.nan)


def f28_ttcf_046_dpo_peak_decay_63(close: pd.Series) -> pd.Series:
    """DPO 63d max - DPO from 63 bars ago — quarterly DPO peak decay."""
    d = _dpo(close, MDAYS)
    pmax = d.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f28_ttcf_047_dpo_dwell_above_zero_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with DPO > 0 — annual cycle-peak dwell."""
    d = _dpo(close, MDAYS)
    return (d > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(d.notna(), np.nan)


def f28_ttcf_048_dpo_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of DPO over 252d — distribution-based DPO position."""
    return _rolling_zscore(_dpo(close, MDAYS), YDAYS, min_periods=QDAYS)


def f28_ttcf_049_dpo_bars_since_252_max(close: pd.Series) -> pd.Series:
    """Bars since DPO hit its 252d max — DPO peak recency."""
    d = _dpo(close, MDAYS)
    at_max = d == d.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f28_ttcf_050_dpo_robust_zscore_mad_252(close: pd.Series) -> pd.Series:
    """Robust z-score: (DPO - median) / (1.4826 * MAD) over 252d — outlier-resistant DPO position."""
    d = _dpo(close, MDAYS)
    med = d.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (d - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(d - med, 1.4826 * mad)


# ============================================================
# Bucket E — KST variants (051-060)
# ============================================================

def f28_ttcf_051_kst_classic(close: pd.Series) -> pd.Series:
    """Pring's classic KST = sum of weighted smoothed ROCs (10/15/20/30)."""
    return _kst(close)


def f28_ttcf_052_kst_signal_9(close: pd.Series) -> pd.Series:
    """KST signal = SMA9 of KST."""
    return _kst(close).rolling(9, min_periods=4).mean()


def f28_ttcf_053_kst_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if KST > 0 — bullish long-term momentum-of-ROCs."""
    k = _kst(close)
    return (k > 0).astype(float).where(k.notna(), np.nan)


def f28_ttcf_054_kst_signal_bearish_cross_indicator(close: pd.Series) -> pd.Series:
    """1 if KST crossed below its signal — KST bearish cross trigger."""
    k = _kst(close)
    s = k.rolling(9, min_periods=4).mean()
    d = k - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f28_ttcf_055_kst_zero_cross_down_indicator(close: pd.Series) -> pd.Series:
    """1 if KST crossed below zero — long-term momentum-sign flip down."""
    k = _kst(close)
    return ((k.shift(1) >= 0) & (k < 0)).astype(float).where(k.notna(), np.nan)


def f28_ttcf_056_kst_bars_since_252_max(close: pd.Series) -> pd.Series:
    """Bars since KST hit its 252d max — KST peak recency."""
    k = _kst(close)
    at_max = k == k.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f28_ttcf_057_kst_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish KST divergence vs price (63d horizon)."""
    k = _kst(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    k_below = k < k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & k_below).astype(float).where(k.notna(), np.nan)


def f28_ttcf_058_kst_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of KST over 252d — distribution-based KST position."""
    return _rolling_zscore(_kst(close), YDAYS, min_periods=QDAYS)


def f28_ttcf_059_kst_dwell_above_zero_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with KST > 0 — annual long-momentum-bullish dwell."""
    k = _kst(close)
    return (k > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(k.notna(), np.nan)


def f28_ttcf_060_kst_peak_decay_63(close: pd.Series) -> pd.Series:
    """KST 63d max - KST from 63 bars ago — quarterly KST peak decay."""
    k = _kst(close)
    pmax = k.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


# ============================================================
# Bucket F — CMO variants (061-075)
# ============================================================

def f28_ttcf_061_cmo_14(close: pd.Series) -> pd.Series:
    """Classical CMO(14) — Chande momentum oscillator on [-100, +100]."""
    return _cmo(close, 14)


def f28_ttcf_062_cmo_21(close: pd.Series) -> pd.Series:
    """CMO(21) — monthly horizon (distinct concept)."""
    return _cmo(close, MDAYS)


def f28_ttcf_063_cmo_63(close: pd.Series) -> pd.Series:
    """CMO(63) — quarterly horizon (distinct concept)."""
    return _cmo(close, QDAYS)


def f28_ttcf_064_cmo_above_50_state(close: pd.Series) -> pd.Series:
    """1 if CMO(14) > 50 — CMO OB threshold."""
    c = _cmo(close, 14)
    return (c > 50.0).astype(float).where(c.notna(), np.nan)


def f28_ttcf_065_cmo_above_75_state(close: pd.Series) -> pd.Series:
    """1 if CMO(14) > 75 — extreme CMO OB."""
    c = _cmo(close, 14)
    return (c > 75.0).astype(float).where(c.notna(), np.nan)


def f28_ttcf_066_cmo_just_exited_above_50(close: pd.Series) -> pd.Series:
    """1 if CMO(14) crossed back below 50 — CMO OB-exit trigger."""
    c = _cmo(close, 14)
    return ((c.shift(1) > 50.0) & (c <= 50.0)).astype(float).where(c.notna(), np.nan)


def f28_ttcf_067_cmo_just_exited_above_75(close: pd.Series) -> pd.Series:
    """1 if CMO(14) crossed back below 75 — extreme CMO OB-exit."""
    c = _cmo(close, 14)
    return ((c.shift(1) > 75.0) & (c <= 75.0)).astype(float).where(c.notna(), np.nan)


def f28_ttcf_068_cmo_dwell_above_50_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with CMO > 50 — quarterly CMO OB dwell."""
    c = _cmo(close, 14)
    return (c > 50.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan)


def f28_ttcf_069_cmo_dwell_above_50_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with CMO > 50 — annual CMO OB dwell."""
    c = _cmo(close, 14)
    return (c > 50.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(c.notna(), np.nan)


def f28_ttcf_070_cmo_bars_since_252_max(close: pd.Series) -> pd.Series:
    """Bars since CMO hit its 252d max — CMO peak recency."""
    c = _cmo(close, 14)
    at_max = c == c.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f28_ttcf_071_cmo_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CMO divergence vs price (63d horizon)."""
    c = _cmo(close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    c_below = c < c.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & c_below).astype(float).where(c.notna(), np.nan)


def f28_ttcf_072_cmo_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of CMO over 252d — distribution-based CMO position."""
    return _rolling_zscore(_cmo(close, 14), YDAYS, min_periods=QDAYS)


def f28_ttcf_073_cmo_peak_decay_63(close: pd.Series) -> pd.Series:
    """CMO 63d max - CMO from 63 bars ago — quarterly CMO peak decay."""
    c = _cmo(close, 14)
    pmax = c.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f28_ttcf_074_cmo_persistence_above_q90_dist_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with CMO above its 252d 90th percentile — distribution-CMO persistence."""
    c = _cmo(close, 14)
    q = c.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (c > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(c.notna() & q.notna(), np.nan)


def f28_ttcf_075_cmo_signal_cross_down_ema9(close: pd.Series) -> pd.Series:
    """1 if CMO crossed below its EMA9 signal — CMO bearish cross trigger."""
    c = _cmo(close, 14)
    s = _ema(c, 9)
    d = c - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

TRIX_TSI_CCI_FAMILY_BASE_REGISTRY_001_075 = {
    "f28_ttcf_001_trix_15": {"inputs": ["close"], "func": f28_ttcf_001_trix_15},
    "f28_ttcf_002_trix_signal_9": {"inputs": ["close"], "func": f28_ttcf_002_trix_signal_9},
    "f28_ttcf_003_trix_histogram": {"inputs": ["close"], "func": f28_ttcf_003_trix_histogram},
    "f28_ttcf_004_trix_30_long": {"inputs": ["close"], "func": f28_ttcf_004_trix_30_long},
    "f28_ttcf_005_trix_above_zero_state": {"inputs": ["close"], "func": f28_ttcf_005_trix_above_zero_state},
    "f28_ttcf_006_trix_signal_bearish_cross_indicator": {"inputs": ["close"], "func": f28_ttcf_006_trix_signal_bearish_cross_indicator},
    "f28_ttcf_007_trix_zero_cross_down_indicator": {"inputs": ["close"], "func": f28_ttcf_007_trix_zero_cross_down_indicator},
    "f28_ttcf_008_trix_peak_decay_63": {"inputs": ["close"], "func": f28_ttcf_008_trix_peak_decay_63},
    "f28_ttcf_009_trix_bars_since_252_max": {"inputs": ["close"], "func": f28_ttcf_009_trix_bars_since_252_max},
    "f28_ttcf_010_trix_div_vs_price_63": {"inputs": ["high", "close"], "func": f28_ttcf_010_trix_div_vs_price_63},
    "f28_ttcf_011_trix_zscore_252": {"inputs": ["close"], "func": f28_ttcf_011_trix_zscore_252},
    "f28_ttcf_012_trix_persistence_above_zero_252": {"inputs": ["close"], "func": f28_ttcf_012_trix_persistence_above_zero_252},
    "f28_ttcf_013_trix_slope_neg_at_price_252_high_state": {"inputs": ["high", "close"], "func": f28_ttcf_013_trix_slope_neg_at_price_252_high_state},
    "f28_ttcf_014_tsi_25_13": {"inputs": ["close"], "func": f28_ttcf_014_tsi_25_13},
    "f28_ttcf_015_tsi_signal_7": {"inputs": ["close"], "func": f28_ttcf_015_tsi_signal_7},
    "f28_ttcf_016_tsi_histogram": {"inputs": ["close"], "func": f28_ttcf_016_tsi_histogram},
    "f28_ttcf_017_tsi_above_zero_state": {"inputs": ["close"], "func": f28_ttcf_017_tsi_above_zero_state},
    "f28_ttcf_018_tsi_signal_bearish_cross_indicator": {"inputs": ["close"], "func": f28_ttcf_018_tsi_signal_bearish_cross_indicator},
    "f28_ttcf_019_tsi_above_25_state": {"inputs": ["close"], "func": f28_ttcf_019_tsi_above_25_state},
    "f28_ttcf_020_tsi_just_exited_above_25": {"inputs": ["close"], "func": f28_ttcf_020_tsi_just_exited_above_25},
    "f28_ttcf_021_tsi_dwell_above_25_63": {"inputs": ["close"], "func": f28_ttcf_021_tsi_dwell_above_25_63},
    "f28_ttcf_022_tsi_bars_since_252_max": {"inputs": ["close"], "func": f28_ttcf_022_tsi_bars_since_252_max},
    "f28_ttcf_023_tsi_zscore_252": {"inputs": ["close"], "func": f28_ttcf_023_tsi_zscore_252},
    "f28_ttcf_024_tsi_div_vs_price_63": {"inputs": ["high", "close"], "func": f28_ttcf_024_tsi_div_vs_price_63},
    "f28_ttcf_025_tsi_persistence_above_zero_252": {"inputs": ["close"], "func": f28_ttcf_025_tsi_persistence_above_zero_252},
    "f28_ttcf_026_cci_20": {"inputs": ["high", "low", "close"], "func": f28_ttcf_026_cci_20},
    "f28_ttcf_027_cci_50": {"inputs": ["high", "low", "close"], "func": f28_ttcf_027_cci_50},
    "f28_ttcf_028_cci_above_100_state": {"inputs": ["high", "low", "close"], "func": f28_ttcf_028_cci_above_100_state},
    "f28_ttcf_029_cci_above_200_state": {"inputs": ["high", "low", "close"], "func": f28_ttcf_029_cci_above_200_state},
    "f28_ttcf_030_cci_just_exited_above_100": {"inputs": ["high", "low", "close"], "func": f28_ttcf_030_cci_just_exited_above_100},
    "f28_ttcf_031_cci_just_exited_above_200": {"inputs": ["high", "low", "close"], "func": f28_ttcf_031_cci_just_exited_above_200},
    "f28_ttcf_032_cci_dwell_above_100_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_032_cci_dwell_above_100_63},
    "f28_ttcf_033_cci_dwell_above_100_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_033_cci_dwell_above_100_252},
    "f28_ttcf_034_cci_bars_since_252_max": {"inputs": ["high", "low", "close"], "func": f28_ttcf_034_cci_bars_since_252_max},
    "f28_ttcf_035_cci_div_vs_price_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_035_cci_div_vs_price_63},
    "f28_ttcf_036_cci_div_vs_price_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_036_cci_div_vs_price_252},
    "f28_ttcf_037_cci_count_ob100_exits_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_037_cci_count_ob100_exits_252},
    "f28_ttcf_038_cci_persistence_above_q90_dist_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_038_cci_persistence_above_q90_dist_252},
    "f28_ttcf_039_cci_peak_decay_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_039_cci_peak_decay_63},
    "f28_ttcf_040_cci_above_q99_dist_state": {"inputs": ["high", "low", "close"], "func": f28_ttcf_040_cci_above_q99_dist_state},
    "f28_ttcf_041_dpo_21": {"inputs": ["close"], "func": f28_ttcf_041_dpo_21},
    "f28_ttcf_042_dpo_63": {"inputs": ["close"], "func": f28_ttcf_042_dpo_63},
    "f28_ttcf_043_dpo_above_zero_state": {"inputs": ["close"], "func": f28_ttcf_043_dpo_above_zero_state},
    "f28_ttcf_044_dpo_above_q90_dist_252": {"inputs": ["close"], "func": f28_ttcf_044_dpo_above_q90_dist_252},
    "f28_ttcf_045_dpo_just_crossed_below_zero": {"inputs": ["close"], "func": f28_ttcf_045_dpo_just_crossed_below_zero},
    "f28_ttcf_046_dpo_peak_decay_63": {"inputs": ["close"], "func": f28_ttcf_046_dpo_peak_decay_63},
    "f28_ttcf_047_dpo_dwell_above_zero_252": {"inputs": ["close"], "func": f28_ttcf_047_dpo_dwell_above_zero_252},
    "f28_ttcf_048_dpo_zscore_252": {"inputs": ["close"], "func": f28_ttcf_048_dpo_zscore_252},
    "f28_ttcf_049_dpo_bars_since_252_max": {"inputs": ["close"], "func": f28_ttcf_049_dpo_bars_since_252_max},
    "f28_ttcf_050_dpo_robust_zscore_mad_252": {"inputs": ["close"], "func": f28_ttcf_050_dpo_robust_zscore_mad_252},
    "f28_ttcf_051_kst_classic": {"inputs": ["close"], "func": f28_ttcf_051_kst_classic},
    "f28_ttcf_052_kst_signal_9": {"inputs": ["close"], "func": f28_ttcf_052_kst_signal_9},
    "f28_ttcf_053_kst_above_zero_state": {"inputs": ["close"], "func": f28_ttcf_053_kst_above_zero_state},
    "f28_ttcf_054_kst_signal_bearish_cross_indicator": {"inputs": ["close"], "func": f28_ttcf_054_kst_signal_bearish_cross_indicator},
    "f28_ttcf_055_kst_zero_cross_down_indicator": {"inputs": ["close"], "func": f28_ttcf_055_kst_zero_cross_down_indicator},
    "f28_ttcf_056_kst_bars_since_252_max": {"inputs": ["close"], "func": f28_ttcf_056_kst_bars_since_252_max},
    "f28_ttcf_057_kst_div_vs_price_63": {"inputs": ["high", "close"], "func": f28_ttcf_057_kst_div_vs_price_63},
    "f28_ttcf_058_kst_zscore_252": {"inputs": ["close"], "func": f28_ttcf_058_kst_zscore_252},
    "f28_ttcf_059_kst_dwell_above_zero_252": {"inputs": ["close"], "func": f28_ttcf_059_kst_dwell_above_zero_252},
    "f28_ttcf_060_kst_peak_decay_63": {"inputs": ["close"], "func": f28_ttcf_060_kst_peak_decay_63},
    "f28_ttcf_061_cmo_14": {"inputs": ["close"], "func": f28_ttcf_061_cmo_14},
    "f28_ttcf_062_cmo_21": {"inputs": ["close"], "func": f28_ttcf_062_cmo_21},
    "f28_ttcf_063_cmo_63": {"inputs": ["close"], "func": f28_ttcf_063_cmo_63},
    "f28_ttcf_064_cmo_above_50_state": {"inputs": ["close"], "func": f28_ttcf_064_cmo_above_50_state},
    "f28_ttcf_065_cmo_above_75_state": {"inputs": ["close"], "func": f28_ttcf_065_cmo_above_75_state},
    "f28_ttcf_066_cmo_just_exited_above_50": {"inputs": ["close"], "func": f28_ttcf_066_cmo_just_exited_above_50},
    "f28_ttcf_067_cmo_just_exited_above_75": {"inputs": ["close"], "func": f28_ttcf_067_cmo_just_exited_above_75},
    "f28_ttcf_068_cmo_dwell_above_50_63": {"inputs": ["close"], "func": f28_ttcf_068_cmo_dwell_above_50_63},
    "f28_ttcf_069_cmo_dwell_above_50_252": {"inputs": ["close"], "func": f28_ttcf_069_cmo_dwell_above_50_252},
    "f28_ttcf_070_cmo_bars_since_252_max": {"inputs": ["close"], "func": f28_ttcf_070_cmo_bars_since_252_max},
    "f28_ttcf_071_cmo_div_vs_price_63": {"inputs": ["high", "close"], "func": f28_ttcf_071_cmo_div_vs_price_63},
    "f28_ttcf_072_cmo_zscore_252": {"inputs": ["close"], "func": f28_ttcf_072_cmo_zscore_252},
    "f28_ttcf_073_cmo_peak_decay_63": {"inputs": ["close"], "func": f28_ttcf_073_cmo_peak_decay_63},
    "f28_ttcf_074_cmo_persistence_above_q90_dist_252": {"inputs": ["close"], "func": f28_ttcf_074_cmo_persistence_above_q90_dist_252},
    "f28_ttcf_075_cmo_signal_cross_down_ema9": {"inputs": ["close"], "func": f28_ttcf_075_cmo_signal_cross_down_ema9},
}


# === D3 wrappers + registry (001_075) ===
def f28_ttcf_001_trix_15_d3(close): return f28_ttcf_001_trix_15(close).diff().diff().diff()
def f28_ttcf_002_trix_signal_9_d3(close): return f28_ttcf_002_trix_signal_9(close).diff().diff().diff()
def f28_ttcf_003_trix_histogram_d3(close): return f28_ttcf_003_trix_histogram(close).diff().diff().diff()
def f28_ttcf_004_trix_30_long_d3(close): return f28_ttcf_004_trix_30_long(close).diff().diff().diff()
def f28_ttcf_005_trix_above_zero_state_d3(close): return f28_ttcf_005_trix_above_zero_state(close).diff().diff().diff()
def f28_ttcf_006_trix_signal_bearish_cross_indicator_d3(close): return f28_ttcf_006_trix_signal_bearish_cross_indicator(close).diff().diff().diff()
def f28_ttcf_007_trix_zero_cross_down_indicator_d3(close): return f28_ttcf_007_trix_zero_cross_down_indicator(close).diff().diff().diff()
def f28_ttcf_008_trix_peak_decay_63_d3(close): return f28_ttcf_008_trix_peak_decay_63(close).diff().diff().diff()
def f28_ttcf_009_trix_bars_since_252_max_d3(close): return f28_ttcf_009_trix_bars_since_252_max(close).diff().diff().diff()
def f28_ttcf_010_trix_div_vs_price_63_d3(high, close): return f28_ttcf_010_trix_div_vs_price_63(high, close).diff().diff().diff()
def f28_ttcf_011_trix_zscore_252_d3(close): return f28_ttcf_011_trix_zscore_252(close).diff().diff().diff()
def f28_ttcf_012_trix_persistence_above_zero_252_d3(close): return f28_ttcf_012_trix_persistence_above_zero_252(close).diff().diff().diff()
def f28_ttcf_013_trix_slope_neg_at_price_252_high_state_d3(high, close): return f28_ttcf_013_trix_slope_neg_at_price_252_high_state(high, close).diff().diff().diff()
def f28_ttcf_014_tsi_25_13_d3(close): return f28_ttcf_014_tsi_25_13(close).diff().diff().diff()
def f28_ttcf_015_tsi_signal_7_d3(close): return f28_ttcf_015_tsi_signal_7(close).diff().diff().diff()
def f28_ttcf_016_tsi_histogram_d3(close): return f28_ttcf_016_tsi_histogram(close).diff().diff().diff()
def f28_ttcf_017_tsi_above_zero_state_d3(close): return f28_ttcf_017_tsi_above_zero_state(close).diff().diff().diff()
def f28_ttcf_018_tsi_signal_bearish_cross_indicator_d3(close): return f28_ttcf_018_tsi_signal_bearish_cross_indicator(close).diff().diff().diff()
def f28_ttcf_019_tsi_above_25_state_d3(close): return f28_ttcf_019_tsi_above_25_state(close).diff().diff().diff()
def f28_ttcf_020_tsi_just_exited_above_25_d3(close): return f28_ttcf_020_tsi_just_exited_above_25(close).diff().diff().diff()
def f28_ttcf_021_tsi_dwell_above_25_63_d3(close): return f28_ttcf_021_tsi_dwell_above_25_63(close).diff().diff().diff()
def f28_ttcf_022_tsi_bars_since_252_max_d3(close): return f28_ttcf_022_tsi_bars_since_252_max(close).diff().diff().diff()
def f28_ttcf_023_tsi_zscore_252_d3(close): return f28_ttcf_023_tsi_zscore_252(close).diff().diff().diff()
def f28_ttcf_024_tsi_div_vs_price_63_d3(high, close): return f28_ttcf_024_tsi_div_vs_price_63(high, close).diff().diff().diff()
def f28_ttcf_025_tsi_persistence_above_zero_252_d3(close): return f28_ttcf_025_tsi_persistence_above_zero_252(close).diff().diff().diff()
def f28_ttcf_026_cci_20_d3(high, low, close): return f28_ttcf_026_cci_20(high, low, close).diff().diff().diff()
def f28_ttcf_027_cci_50_d3(high, low, close): return f28_ttcf_027_cci_50(high, low, close).diff().diff().diff()
def f28_ttcf_028_cci_above_100_state_d3(high, low, close): return f28_ttcf_028_cci_above_100_state(high, low, close).diff().diff().diff()
def f28_ttcf_029_cci_above_200_state_d3(high, low, close): return f28_ttcf_029_cci_above_200_state(high, low, close).diff().diff().diff()
def f28_ttcf_030_cci_just_exited_above_100_d3(high, low, close): return f28_ttcf_030_cci_just_exited_above_100(high, low, close).diff().diff().diff()
def f28_ttcf_031_cci_just_exited_above_200_d3(high, low, close): return f28_ttcf_031_cci_just_exited_above_200(high, low, close).diff().diff().diff()
def f28_ttcf_032_cci_dwell_above_100_63_d3(high, low, close): return f28_ttcf_032_cci_dwell_above_100_63(high, low, close).diff().diff().diff()
def f28_ttcf_033_cci_dwell_above_100_252_d3(high, low, close): return f28_ttcf_033_cci_dwell_above_100_252(high, low, close).diff().diff().diff()
def f28_ttcf_034_cci_bars_since_252_max_d3(high, low, close): return f28_ttcf_034_cci_bars_since_252_max(high, low, close).diff().diff().diff()
def f28_ttcf_035_cci_div_vs_price_63_d3(high, low, close): return f28_ttcf_035_cci_div_vs_price_63(high, low, close).diff().diff().diff()
def f28_ttcf_036_cci_div_vs_price_252_d3(high, low, close): return f28_ttcf_036_cci_div_vs_price_252(high, low, close).diff().diff().diff()
def f28_ttcf_037_cci_count_ob100_exits_252_d3(high, low, close): return f28_ttcf_037_cci_count_ob100_exits_252(high, low, close).diff().diff().diff()
def f28_ttcf_038_cci_persistence_above_q90_dist_252_d3(high, low, close): return f28_ttcf_038_cci_persistence_above_q90_dist_252(high, low, close).diff().diff().diff()
def f28_ttcf_039_cci_peak_decay_63_d3(high, low, close): return f28_ttcf_039_cci_peak_decay_63(high, low, close).diff().diff().diff()
def f28_ttcf_040_cci_above_q99_dist_state_d3(high, low, close): return f28_ttcf_040_cci_above_q99_dist_state(high, low, close).diff().diff().diff()
def f28_ttcf_041_dpo_21_d3(close): return f28_ttcf_041_dpo_21(close).diff().diff().diff()
def f28_ttcf_042_dpo_63_d3(close): return f28_ttcf_042_dpo_63(close).diff().diff().diff()
def f28_ttcf_043_dpo_above_zero_state_d3(close): return f28_ttcf_043_dpo_above_zero_state(close).diff().diff().diff()
def f28_ttcf_044_dpo_above_q90_dist_252_d3(close): return f28_ttcf_044_dpo_above_q90_dist_252(close).diff().diff().diff()
def f28_ttcf_045_dpo_just_crossed_below_zero_d3(close): return f28_ttcf_045_dpo_just_crossed_below_zero(close).diff().diff().diff()
def f28_ttcf_046_dpo_peak_decay_63_d3(close): return f28_ttcf_046_dpo_peak_decay_63(close).diff().diff().diff()
def f28_ttcf_047_dpo_dwell_above_zero_252_d3(close): return f28_ttcf_047_dpo_dwell_above_zero_252(close).diff().diff().diff()
def f28_ttcf_048_dpo_zscore_252_d3(close): return f28_ttcf_048_dpo_zscore_252(close).diff().diff().diff()
def f28_ttcf_049_dpo_bars_since_252_max_d3(close): return f28_ttcf_049_dpo_bars_since_252_max(close).diff().diff().diff()
def f28_ttcf_050_dpo_robust_zscore_mad_252_d3(close): return f28_ttcf_050_dpo_robust_zscore_mad_252(close).diff().diff().diff()
def f28_ttcf_051_kst_classic_d3(close): return f28_ttcf_051_kst_classic(close).diff().diff().diff()
def f28_ttcf_052_kst_signal_9_d3(close): return f28_ttcf_052_kst_signal_9(close).diff().diff().diff()
def f28_ttcf_053_kst_above_zero_state_d3(close): return f28_ttcf_053_kst_above_zero_state(close).diff().diff().diff()
def f28_ttcf_054_kst_signal_bearish_cross_indicator_d3(close): return f28_ttcf_054_kst_signal_bearish_cross_indicator(close).diff().diff().diff()
def f28_ttcf_055_kst_zero_cross_down_indicator_d3(close): return f28_ttcf_055_kst_zero_cross_down_indicator(close).diff().diff().diff()
def f28_ttcf_056_kst_bars_since_252_max_d3(close): return f28_ttcf_056_kst_bars_since_252_max(close).diff().diff().diff()
def f28_ttcf_057_kst_div_vs_price_63_d3(high, close): return f28_ttcf_057_kst_div_vs_price_63(high, close).diff().diff().diff()
def f28_ttcf_058_kst_zscore_252_d3(close): return f28_ttcf_058_kst_zscore_252(close).diff().diff().diff()
def f28_ttcf_059_kst_dwell_above_zero_252_d3(close): return f28_ttcf_059_kst_dwell_above_zero_252(close).diff().diff().diff()
def f28_ttcf_060_kst_peak_decay_63_d3(close): return f28_ttcf_060_kst_peak_decay_63(close).diff().diff().diff()
def f28_ttcf_061_cmo_14_d3(close): return f28_ttcf_061_cmo_14(close).diff().diff().diff()
def f28_ttcf_062_cmo_21_d3(close): return f28_ttcf_062_cmo_21(close).diff().diff().diff()
def f28_ttcf_063_cmo_63_d3(close): return f28_ttcf_063_cmo_63(close).diff().diff().diff()
def f28_ttcf_064_cmo_above_50_state_d3(close): return f28_ttcf_064_cmo_above_50_state(close).diff().diff().diff()
def f28_ttcf_065_cmo_above_75_state_d3(close): return f28_ttcf_065_cmo_above_75_state(close).diff().diff().diff()
def f28_ttcf_066_cmo_just_exited_above_50_d3(close): return f28_ttcf_066_cmo_just_exited_above_50(close).diff().diff().diff()
def f28_ttcf_067_cmo_just_exited_above_75_d3(close): return f28_ttcf_067_cmo_just_exited_above_75(close).diff().diff().diff()
def f28_ttcf_068_cmo_dwell_above_50_63_d3(close): return f28_ttcf_068_cmo_dwell_above_50_63(close).diff().diff().diff()
def f28_ttcf_069_cmo_dwell_above_50_252_d3(close): return f28_ttcf_069_cmo_dwell_above_50_252(close).diff().diff().diff()
def f28_ttcf_070_cmo_bars_since_252_max_d3(close): return f28_ttcf_070_cmo_bars_since_252_max(close).diff().diff().diff()
def f28_ttcf_071_cmo_div_vs_price_63_d3(high, close): return f28_ttcf_071_cmo_div_vs_price_63(high, close).diff().diff().diff()
def f28_ttcf_072_cmo_zscore_252_d3(close): return f28_ttcf_072_cmo_zscore_252(close).diff().diff().diff()
def f28_ttcf_073_cmo_peak_decay_63_d3(close): return f28_ttcf_073_cmo_peak_decay_63(close).diff().diff().diff()
def f28_ttcf_074_cmo_persistence_above_q90_dist_252_d3(close): return f28_ttcf_074_cmo_persistence_above_q90_dist_252(close).diff().diff().diff()
def f28_ttcf_075_cmo_signal_cross_down_ema9_d3(close): return f28_ttcf_075_cmo_signal_cross_down_ema9(close).diff().diff().diff()

TRIX_TSI_CCI_FAMILY_D3_REGISTRY_001_075 = {
    "f28_ttcf_001_trix_15_d3": {"inputs": ["close"], "func": f28_ttcf_001_trix_15_d3},
    "f28_ttcf_002_trix_signal_9_d3": {"inputs": ["close"], "func": f28_ttcf_002_trix_signal_9_d3},
    "f28_ttcf_003_trix_histogram_d3": {"inputs": ["close"], "func": f28_ttcf_003_trix_histogram_d3},
    "f28_ttcf_004_trix_30_long_d3": {"inputs": ["close"], "func": f28_ttcf_004_trix_30_long_d3},
    "f28_ttcf_005_trix_above_zero_state_d3": {"inputs": ["close"], "func": f28_ttcf_005_trix_above_zero_state_d3},
    "f28_ttcf_006_trix_signal_bearish_cross_indicator_d3": {"inputs": ["close"], "func": f28_ttcf_006_trix_signal_bearish_cross_indicator_d3},
    "f28_ttcf_007_trix_zero_cross_down_indicator_d3": {"inputs": ["close"], "func": f28_ttcf_007_trix_zero_cross_down_indicator_d3},
    "f28_ttcf_008_trix_peak_decay_63_d3": {"inputs": ["close"], "func": f28_ttcf_008_trix_peak_decay_63_d3},
    "f28_ttcf_009_trix_bars_since_252_max_d3": {"inputs": ["close"], "func": f28_ttcf_009_trix_bars_since_252_max_d3},
    "f28_ttcf_010_trix_div_vs_price_63_d3": {"inputs": ["high", "close"], "func": f28_ttcf_010_trix_div_vs_price_63_d3},
    "f28_ttcf_011_trix_zscore_252_d3": {"inputs": ["close"], "func": f28_ttcf_011_trix_zscore_252_d3},
    "f28_ttcf_012_trix_persistence_above_zero_252_d3": {"inputs": ["close"], "func": f28_ttcf_012_trix_persistence_above_zero_252_d3},
    "f28_ttcf_013_trix_slope_neg_at_price_252_high_state_d3": {"inputs": ["high", "close"], "func": f28_ttcf_013_trix_slope_neg_at_price_252_high_state_d3},
    "f28_ttcf_014_tsi_25_13_d3": {"inputs": ["close"], "func": f28_ttcf_014_tsi_25_13_d3},
    "f28_ttcf_015_tsi_signal_7_d3": {"inputs": ["close"], "func": f28_ttcf_015_tsi_signal_7_d3},
    "f28_ttcf_016_tsi_histogram_d3": {"inputs": ["close"], "func": f28_ttcf_016_tsi_histogram_d3},
    "f28_ttcf_017_tsi_above_zero_state_d3": {"inputs": ["close"], "func": f28_ttcf_017_tsi_above_zero_state_d3},
    "f28_ttcf_018_tsi_signal_bearish_cross_indicator_d3": {"inputs": ["close"], "func": f28_ttcf_018_tsi_signal_bearish_cross_indicator_d3},
    "f28_ttcf_019_tsi_above_25_state_d3": {"inputs": ["close"], "func": f28_ttcf_019_tsi_above_25_state_d3},
    "f28_ttcf_020_tsi_just_exited_above_25_d3": {"inputs": ["close"], "func": f28_ttcf_020_tsi_just_exited_above_25_d3},
    "f28_ttcf_021_tsi_dwell_above_25_63_d3": {"inputs": ["close"], "func": f28_ttcf_021_tsi_dwell_above_25_63_d3},
    "f28_ttcf_022_tsi_bars_since_252_max_d3": {"inputs": ["close"], "func": f28_ttcf_022_tsi_bars_since_252_max_d3},
    "f28_ttcf_023_tsi_zscore_252_d3": {"inputs": ["close"], "func": f28_ttcf_023_tsi_zscore_252_d3},
    "f28_ttcf_024_tsi_div_vs_price_63_d3": {"inputs": ["high", "close"], "func": f28_ttcf_024_tsi_div_vs_price_63_d3},
    "f28_ttcf_025_tsi_persistence_above_zero_252_d3": {"inputs": ["close"], "func": f28_ttcf_025_tsi_persistence_above_zero_252_d3},
    "f28_ttcf_026_cci_20_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_026_cci_20_d3},
    "f28_ttcf_027_cci_50_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_027_cci_50_d3},
    "f28_ttcf_028_cci_above_100_state_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_028_cci_above_100_state_d3},
    "f28_ttcf_029_cci_above_200_state_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_029_cci_above_200_state_d3},
    "f28_ttcf_030_cci_just_exited_above_100_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_030_cci_just_exited_above_100_d3},
    "f28_ttcf_031_cci_just_exited_above_200_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_031_cci_just_exited_above_200_d3},
    "f28_ttcf_032_cci_dwell_above_100_63_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_032_cci_dwell_above_100_63_d3},
    "f28_ttcf_033_cci_dwell_above_100_252_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_033_cci_dwell_above_100_252_d3},
    "f28_ttcf_034_cci_bars_since_252_max_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_034_cci_bars_since_252_max_d3},
    "f28_ttcf_035_cci_div_vs_price_63_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_035_cci_div_vs_price_63_d3},
    "f28_ttcf_036_cci_div_vs_price_252_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_036_cci_div_vs_price_252_d3},
    "f28_ttcf_037_cci_count_ob100_exits_252_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_037_cci_count_ob100_exits_252_d3},
    "f28_ttcf_038_cci_persistence_above_q90_dist_252_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_038_cci_persistence_above_q90_dist_252_d3},
    "f28_ttcf_039_cci_peak_decay_63_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_039_cci_peak_decay_63_d3},
    "f28_ttcf_040_cci_above_q99_dist_state_d3": {"inputs": ["high", "low", "close"], "func": f28_ttcf_040_cci_above_q99_dist_state_d3},
    "f28_ttcf_041_dpo_21_d3": {"inputs": ["close"], "func": f28_ttcf_041_dpo_21_d3},
    "f28_ttcf_042_dpo_63_d3": {"inputs": ["close"], "func": f28_ttcf_042_dpo_63_d3},
    "f28_ttcf_043_dpo_above_zero_state_d3": {"inputs": ["close"], "func": f28_ttcf_043_dpo_above_zero_state_d3},
    "f28_ttcf_044_dpo_above_q90_dist_252_d3": {"inputs": ["close"], "func": f28_ttcf_044_dpo_above_q90_dist_252_d3},
    "f28_ttcf_045_dpo_just_crossed_below_zero_d3": {"inputs": ["close"], "func": f28_ttcf_045_dpo_just_crossed_below_zero_d3},
    "f28_ttcf_046_dpo_peak_decay_63_d3": {"inputs": ["close"], "func": f28_ttcf_046_dpo_peak_decay_63_d3},
    "f28_ttcf_047_dpo_dwell_above_zero_252_d3": {"inputs": ["close"], "func": f28_ttcf_047_dpo_dwell_above_zero_252_d3},
    "f28_ttcf_048_dpo_zscore_252_d3": {"inputs": ["close"], "func": f28_ttcf_048_dpo_zscore_252_d3},
    "f28_ttcf_049_dpo_bars_since_252_max_d3": {"inputs": ["close"], "func": f28_ttcf_049_dpo_bars_since_252_max_d3},
    "f28_ttcf_050_dpo_robust_zscore_mad_252_d3": {"inputs": ["close"], "func": f28_ttcf_050_dpo_robust_zscore_mad_252_d3},
    "f28_ttcf_051_kst_classic_d3": {"inputs": ["close"], "func": f28_ttcf_051_kst_classic_d3},
    "f28_ttcf_052_kst_signal_9_d3": {"inputs": ["close"], "func": f28_ttcf_052_kst_signal_9_d3},
    "f28_ttcf_053_kst_above_zero_state_d3": {"inputs": ["close"], "func": f28_ttcf_053_kst_above_zero_state_d3},
    "f28_ttcf_054_kst_signal_bearish_cross_indicator_d3": {"inputs": ["close"], "func": f28_ttcf_054_kst_signal_bearish_cross_indicator_d3},
    "f28_ttcf_055_kst_zero_cross_down_indicator_d3": {"inputs": ["close"], "func": f28_ttcf_055_kst_zero_cross_down_indicator_d3},
    "f28_ttcf_056_kst_bars_since_252_max_d3": {"inputs": ["close"], "func": f28_ttcf_056_kst_bars_since_252_max_d3},
    "f28_ttcf_057_kst_div_vs_price_63_d3": {"inputs": ["high", "close"], "func": f28_ttcf_057_kst_div_vs_price_63_d3},
    "f28_ttcf_058_kst_zscore_252_d3": {"inputs": ["close"], "func": f28_ttcf_058_kst_zscore_252_d3},
    "f28_ttcf_059_kst_dwell_above_zero_252_d3": {"inputs": ["close"], "func": f28_ttcf_059_kst_dwell_above_zero_252_d3},
    "f28_ttcf_060_kst_peak_decay_63_d3": {"inputs": ["close"], "func": f28_ttcf_060_kst_peak_decay_63_d3},
    "f28_ttcf_061_cmo_14_d3": {"inputs": ["close"], "func": f28_ttcf_061_cmo_14_d3},
    "f28_ttcf_062_cmo_21_d3": {"inputs": ["close"], "func": f28_ttcf_062_cmo_21_d3},
    "f28_ttcf_063_cmo_63_d3": {"inputs": ["close"], "func": f28_ttcf_063_cmo_63_d3},
    "f28_ttcf_064_cmo_above_50_state_d3": {"inputs": ["close"], "func": f28_ttcf_064_cmo_above_50_state_d3},
    "f28_ttcf_065_cmo_above_75_state_d3": {"inputs": ["close"], "func": f28_ttcf_065_cmo_above_75_state_d3},
    "f28_ttcf_066_cmo_just_exited_above_50_d3": {"inputs": ["close"], "func": f28_ttcf_066_cmo_just_exited_above_50_d3},
    "f28_ttcf_067_cmo_just_exited_above_75_d3": {"inputs": ["close"], "func": f28_ttcf_067_cmo_just_exited_above_75_d3},
    "f28_ttcf_068_cmo_dwell_above_50_63_d3": {"inputs": ["close"], "func": f28_ttcf_068_cmo_dwell_above_50_63_d3},
    "f28_ttcf_069_cmo_dwell_above_50_252_d3": {"inputs": ["close"], "func": f28_ttcf_069_cmo_dwell_above_50_252_d3},
    "f28_ttcf_070_cmo_bars_since_252_max_d3": {"inputs": ["close"], "func": f28_ttcf_070_cmo_bars_since_252_max_d3},
    "f28_ttcf_071_cmo_div_vs_price_63_d3": {"inputs": ["high", "close"], "func": f28_ttcf_071_cmo_div_vs_price_63_d3},
    "f28_ttcf_072_cmo_zscore_252_d3": {"inputs": ["close"], "func": f28_ttcf_072_cmo_zscore_252_d3},
    "f28_ttcf_073_cmo_peak_decay_63_d3": {"inputs": ["close"], "func": f28_ttcf_073_cmo_peak_decay_63_d3},
    "f28_ttcf_074_cmo_persistence_above_q90_dist_252_d3": {"inputs": ["close"], "func": f28_ttcf_074_cmo_persistence_above_q90_dist_252_d3},
    "f28_ttcf_075_cmo_signal_cross_down_ema9_d3": {"inputs": ["close"], "func": f28_ttcf_075_cmo_signal_cross_down_ema9_d3},
}
