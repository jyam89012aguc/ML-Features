"""long_momentum_smoothed_pmo d1 features 001-075 - Pipeline 1b-technical.

150 distinct hypotheses across __base__001_075.py and __base__076_150.py.
Each feature encodes a *different concept*.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers - no cross-family imports.
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
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _sma(s, n, mp=None):
    if mp is None:
        mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _wma(s, n):
    w = np.arange(1, n + 1, dtype=float)
    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _rolling_corr(a, b, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return a.rolling(n, min_periods=min_periods).corr(b)

def _roc(close, n):
    return 100.0 * (close / close.shift(n) - 1.0)


def _pring_pmo(close):
    """DecisionPoint Price Momentum Oscillator (Pring/Swenlin).

    Standard formulation:
      1) 1-bar ROC of close
      2) Custom 35-period smoothing = EMA with alpha=2/(35+1) but applied as smoothed-rate
      3) Second smoothing = 20-period EMA
      4) Signal = 10-period EMA of the result
    """
    roc = 100.0 * close.pct_change()
    sm1 = roc.ewm(span=35, adjust=False, min_periods=10).mean()
    pmo = sm1.ewm(span=20, adjust=False, min_periods=10).mean()
    sig = pmo.ewm(span=10, adjust=False, min_periods=5).mean()
    return pmo, sig


def _pring_special_k(close):
    """Pring's Special K = weighted sum of multiple ROC periods, each smoothed.

    Per Pring's specification (StockCharts), aggregates short-, intermediate-, and
    long-term momentum into one composite.
    """
    # Short-term components
    roc10 = _roc(close, 10).rolling(10, min_periods=3).mean()
    roc15 = _roc(close, 15).rolling(10, min_periods=3).mean()
    roc20 = _roc(close, 20).rolling(10, min_periods=3).mean()
    roc30 = _roc(close, 30).rolling(15, min_periods=5).mean()
    # Intermediate-term
    roc40 = _roc(close, 40).rolling(50, min_periods=15).mean()
    roc65 = _roc(close, 65).rolling(65, min_periods=20).mean()
    roc75 = _roc(close, 75).rolling(75, min_periods=25).mean()
    roc100 = _roc(close, 100).rolling(100, min_periods=33).mean()
    # Long-term
    roc195 = _roc(close, 195).rolling(130, min_periods=43).mean()
    roc265 = _roc(close, 265).rolling(130, min_periods=43).mean()
    roc390 = _roc(close, 390).rolling(130, min_periods=43).mean()
    roc530 = _roc(close, 530).rolling(195, min_periods=65).mean()
    return (roc10 + 2 * roc15 + 3 * roc20 + 4 * roc30
            + roc40 + 2 * roc65 + 2 * roc75 + roc100
            + roc195 + 2 * roc265 + 3 * roc390 + 4 * roc530)


def _kst(close):
    """Pring KST: weighted sum of smoothed ROCs at 10/15/20/30 (daily-time-frame proxy)."""
    rcma1 = _roc(close, 10).rolling(10, min_periods=3).mean()
    rcma2 = _roc(close, 15).rolling(10, min_periods=3).mean()
    rcma3 = _roc(close, 20).rolling(10, min_periods=3).mean()
    rcma4 = _roc(close, 30).rolling(15, min_periods=5).mean()
    return rcma1 + 2 * rcma2 + 3 * rcma3 + 4 * rcma4


def _kst_signal(close):
    return _kst(close).rolling(9, min_periods=3).mean()


def _coppock_annual(close):
    """Coppock = 10-period WMA of (ROC14 + ROC11) - canonical 'annual' form (Coppock 1962)."""
    rc = _roc(close, 14 * 21) + _roc(close, 11 * 21)
    return _wma_simple(rc, 10 * 21)


def _wma_simple(s, n):
    w = np.arange(1, n + 1, dtype=float)
    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < max(n // 3, 5):
            return np.nan
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)
    return s.rolling(n, min_periods=max(n // 3, 5)).apply(_f, raw=True)


def _trix_with_signal(close, n=15, sig_n=9):
    e1 = _ema(close, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    tr = 100.0 * e3.pct_change()
    return tr, tr.ewm(span=sig_n, adjust=False, min_periods=3).mean()


def _ppo_with_signal(close, fast=12, slow=26, sig=9):
    fast_ma = _ema(close, fast); slow_ma = _ema(close, slow)
    ppo = 100.0 * (fast_ma - slow_ma) / slow_ma.replace(0, np.nan)
    return ppo, ppo.ewm(span=sig, adjust=False, min_periods=3).mean()


def _rolling_q(s, n, q, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).quantile(q)


def _rolling_pct_rank(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(n, min_periods=min_periods).apply(_rk, raw=True)


def _zero_cross_events(s):
    """Return (cross_up, cross_down) indicator Series."""
    sgn = np.sign(s.fillna(0.0))
    prev = sgn.shift(1)
    up = ((sgn > 0) & (prev <= 0)).astype(float)
    dn = ((sgn < 0) & (prev >= 0)).astype(float)
    return up, dn


def _bars_since_last_event(ind):
    arr = ind.values
    nb = len(arr)
    out = np.full(nb, np.nan, dtype=float)
    last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=ind.index)


def _days_since_max_in_window(s, n):
    mp = max(n // 3, 5)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < mp:
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _days_since_min_in_window(s, n):
    mp = max(n // 3, 5)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < mp:
            return np.nan
        return float(len(w) - 1 - int(np.nanargmin(w)))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def f55_lmps_001_mayer_multiple_close_sma200_d1(close: pd.Series) -> pd.Series:
    """Mayer multiple = close / SMA200 - canonical price-vs-trend ratio."""
    sma200 = _sma(close, 200)
    return (_safe_div(close, sma200)).diff()

def f55_lmps_002_mayer_multiple_log_d1(close: pd.Series) -> pd.Series:
    """Log-Mayer multiple = log(close) - log(SMA200)."""
    sma200 = _sma(close, 200)
    return (_safe_log(close) - _safe_log(sma200)).diff()

def f55_lmps_003_mayer_multiple_zscore_504d_d1(close: pd.Series) -> pd.Series:
    """504d z-score of Mayer multiple - relative-extension regime."""
    mm = _safe_div(close, _sma(close, 200))
    return (_rolling_zscore(mm, DDAYS_2Y)).diff()

def f55_lmps_004_mayer_multiple_pct_rank_504d_d1(close: pd.Series) -> pd.Series:
    """504d percentile rank of Mayer multiple."""
    mm = _safe_div(close, _sma(close, 200))
    return (_rolling_pct_rank(mm, DDAYS_2Y)).diff()

def f55_lmps_005_mayer_multiple_pct_change_21d_d1(close: pd.Series) -> pd.Series:
    """21-bar change in Mayer multiple - extension velocity."""
    mm = _safe_div(close, _sma(close, 200))
    return (mm.pct_change(MDAYS)).diff()

def f55_lmps_006_mayer_multiple_days_above_1_d1(close: pd.Series) -> pd.Series:
    """Bars since Mayer multiple last fell below 1.0 (capped at YDAYS)."""
    mm = _safe_div(close, _sma(close, 200))
    ind = (mm < 1.0).astype(float).where(mm.notna(), np.nan)
    arr = ind.values; nb = len(arr); out = np.full(nb, np.nan); last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index).clip(upper=float(YDAYS))
    return (res).diff()

def f55_lmps_007_mayer_multiple_days_above_1_5_d1(close: pd.Series) -> pd.Series:
    """Bars since Mayer multiple last fell below 1.5."""
    mm = _safe_div(close, _sma(close, 200))
    ind = (mm < 1.5).astype(float).where(mm.notna(), np.nan)
    arr = ind.values; nb = len(arr); out = np.full(nb, np.nan); last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index).clip(upper=float(YDAYS))
    return (res).diff()

def f55_lmps_008_mayer_multiple_days_above_2_d1(close: pd.Series) -> pd.Series:
    """Bars since Mayer multiple last fell below 2.0 - extreme extension persistence."""
    mm = _safe_div(close, _sma(close, 200))
    ind = (mm < 2.0).astype(float).where(mm.notna(), np.nan)
    arr = ind.values; nb = len(arr); out = np.full(nb, np.nan); last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index).clip(upper=float(YDAYS))
    return (res).diff()

def f55_lmps_009_mayer_multiple_above_p90_252d_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: Mayer multiple > 252d 90th percentile."""
    mm = _safe_div(close, _sma(close, 200))
    p90 = mm.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((mm > p90).astype(float).where(p90.notna(), np.nan)).diff()

def f55_lmps_010_mayer_multiple_at_252d_high_x_above_2_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: Mayer > 2.0 AND close = 252d max."""
    mm = _safe_div(close, _sma(close, 200))
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((mm > 2.0) & (close >= rmax - 1e-12)).astype(float).where(mm.notna(), np.nan)).diff()

def f55_lmps_011_pring_pmo_value_d1(close: pd.Series) -> pd.Series:
    """Pring DecisionPoint Price Momentum Oscillator value."""
    pmo, sig = _pring_pmo(close)
    return (pmo).diff()

def f55_lmps_012_pring_pmo_signal_value_d1(close: pd.Series) -> pd.Series:
    """PMO signal-line (10-EMA of PMO)."""
    pmo, sig = _pring_pmo(close)
    return (sig).diff()

def f55_lmps_013_pring_pmo_minus_signal_d1(close: pd.Series) -> pd.Series:
    """PMO minus signal - momentum-of-momentum divergence."""
    pmo, sig = _pring_pmo(close)
    return (pmo - sig).diff()

def f55_lmps_014_pring_pmo_bearish_signal_cross_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: PMO crosses below signal-line."""
    pmo, sig = _pring_pmo(close)
    spread = pmo - sig
    return (((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)).diff()

def f55_lmps_015_pring_pmo_zero_cross_down_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: PMO crosses below zero."""
    pmo, sig = _pring_pmo(close)
    up, dn = _zero_cross_events(pmo)
    return (dn).diff()

def f55_lmps_016_pring_pmo_days_since_top_504d_d1(close: pd.Series) -> pd.Series:
    """Bars since PMO peak within last 504d."""
    pmo, sig = _pring_pmo(close)
    return (_days_since_max_in_window(pmo, DDAYS_2Y)).diff()

def f55_lmps_017_pring_pmo_overbought_above_2_persistence_63d_d1(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with PMO > 2.0 - overbought regime persistence."""
    pmo, sig = _pring_pmo(close)
    ind = (pmo > 2.0).astype(float).where(pmo.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff()

def f55_lmps_018_pring_pmo_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of PMO - relative regime."""
    pmo, sig = _pring_pmo(close)
    return (_rolling_zscore(pmo, YDAYS)).diff()

def f55_lmps_019_pring_pmo_falling_at_252d_high_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: PMO < signal AND close = 252d max - momentum loss at new high."""
    pmo, sig = _pring_pmo(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((pmo < sig) & (close >= rmax - 1e-12)).astype(float).where(pmo.notna(), np.nan)).diff()

def f55_lmps_020_pring_pmo_bearish_cross_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of PMO/signal bearish crossings in last 252d."""
    pmo, sig = _pring_pmo(close)
    spread = pmo - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff()

def f55_lmps_021_pring_special_k_value_d1(close: pd.Series) -> pd.Series:
    """Pring's Special K composite (multi-horizon weighted ROCs)."""
    sk = _pring_special_k(close)
    return (sk).diff()

def f55_lmps_022_pring_special_k_signal_value_d1(close: pd.Series) -> pd.Series:
    """Special K signal-line (10-period EMA)."""
    sk = _pring_special_k(close)
    return (sk.ewm(span=10, adjust=False, min_periods=3).mean()).diff()

def f55_lmps_023_pring_special_k_minus_signal_d1(close: pd.Series) -> pd.Series:
    """Special K minus its signal line."""
    sk = _pring_special_k(close)
    sig = sk.ewm(span=10, adjust=False, min_periods=3).mean()
    return (sk - sig).diff()

def f55_lmps_024_pring_special_k_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of Special K."""
    sk = _pring_special_k(close)
    return (_rolling_zscore(sk, YDAYS)).diff()

def f55_lmps_025_pring_special_k_signal_bearish_cross_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: Special K crosses below its signal."""
    sk = _pring_special_k(close)
    sig = sk.ewm(span=10, adjust=False, min_periods=3).mean()
    spread = sk - sig
    return (((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)).diff()

def f55_lmps_026_pring_special_k_days_since_top_504d_d1(close: pd.Series) -> pd.Series:
    """Bars since Special K peak within 504d."""
    sk = _pring_special_k(close)
    return (_days_since_max_in_window(sk, DDAYS_2Y)).diff()

def f55_lmps_027_pring_special_k_minus_kst_252d_d1(close: pd.Series) -> pd.Series:
    """Special K minus KST - intermediate-vs-short momentum gap (252d z-scored)."""
    sk = _pring_special_k(close)
    kst = _kst(close)
    return (_rolling_zscore(sk - kst, YDAYS)).diff()

def f55_lmps_028_pring_special_k_above_p90_252d_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: Special K > 252d-p90 - overbought regime."""
    sk = _pring_special_k(close)
    p90 = sk.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((sk > p90).astype(float).where(p90.notna(), np.nan)).diff()

def f55_lmps_029_pring_special_k_falling_at_252d_high_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: Special K < signal AND close = 252d max."""
    sk = _pring_special_k(close)
    sig = sk.ewm(span=10, adjust=False, min_periods=3).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((sk < sig) & (close >= rmax - 1e-12)).astype(float).where(sk.notna(), np.nan)).diff()

def f55_lmps_030_pring_special_k_long_horizon_decay_rate_252d_d1(close: pd.Series) -> pd.Series:
    """21-bar pct decline of Special K from its 252d max - cycle-decay rate."""
    sk = _pring_special_k(close)
    mx = sk.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(sk - mx, mx)).diff()

def f55_lmps_031_dpo_10d_value_d1(close: pd.Series) -> pd.Series:
    """Detrended Price Oscillator value at 10d - close minus trailing SMA10."""
    dpo = close - _sma(close, 10)
    return (dpo).diff()

def f55_lmps_032_dpo_21d_value_d1(close: pd.Series) -> pd.Series:
    """Detrended Price Oscillator value at 21d - close minus trailing SMA21."""
    dpo = close - _sma(close, 21)
    return (dpo).diff()

def f55_lmps_033_dpo_63d_value_d1(close: pd.Series) -> pd.Series:
    """Detrended Price Oscillator value at 63d - close minus trailing SMA63."""
    dpo = close - _sma(close, 63)
    return (dpo).diff()

def f55_lmps_034_dpo_126d_value_d1(close: pd.Series) -> pd.Series:
    """Detrended Price Oscillator value at 126d - close minus trailing SMA126."""
    dpo = close - _sma(close, 126)
    return (dpo).diff()

def f55_lmps_035_dpo_252d_value_d1(close: pd.Series) -> pd.Series:
    """Detrended Price Oscillator value at 252d - close minus trailing SMA252."""
    dpo = close - _sma(close, 252)
    return (dpo).diff()

def f55_lmps_036_dpo_10d_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of DPO(10)."""
    dpo = close - _sma(close, 10)
    return (_rolling_zscore(dpo, YDAYS)).diff()

def f55_lmps_037_dpo_21d_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of DPO(21)."""
    dpo = close - _sma(close, 21)
    return (_rolling_zscore(dpo, YDAYS)).diff()

def f55_lmps_038_dpo_63d_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of DPO(63)."""
    dpo = close - _sma(close, 63)
    return (_rolling_zscore(dpo, YDAYS)).diff()

def f55_lmps_039_dpo_126d_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of DPO(126)."""
    dpo = close - _sma(close, 126)
    return (_rolling_zscore(dpo, YDAYS)).diff()

def f55_lmps_040_dpo_multi_horizon_all_negative_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where DPO at 21,63,126,252 are all negative."""
    d21 = close - _sma(close, 21); d63 = close - _sma(close, 63)
    d126 = close - _sma(close, 126); d252 = close - _sma(close, 252)
    ind = ((d21 < 0) & (d63 < 0) & (d126 < 0) & (d252 < 0)).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum()).diff()

def f55_lmps_041_trix_15d_value_d1(close: pd.Series) -> pd.Series:
    """TRIX(15) value."""
    tr, sig = _trix_with_signal(close, 15, 9)
    return (tr).diff()

def f55_lmps_042_trix_signal_9d_value_d1(close: pd.Series) -> pd.Series:
    """TRIX signal-line (9-EMA of TRIX)."""
    tr, sig = _trix_with_signal(close, 15, 9)
    return (sig).diff()

def f55_lmps_043_trix_minus_signal_15d_d1(close: pd.Series) -> pd.Series:
    """TRIX - signal."""
    tr, sig = _trix_with_signal(close, 15, 9)
    return (tr - sig).diff()

def f55_lmps_044_trix_signal_bearish_cross_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: TRIX crosses below its signal."""
    tr, sig = _trix_with_signal(close, 15, 9)
    spread = tr - sig
    return (((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)).diff()

def f55_lmps_045_trix_signal_bullish_cross_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: TRIX crosses above its signal."""
    tr, sig = _trix_with_signal(close, 15, 9)
    spread = tr - sig
    return (((spread > 0) & (spread.shift(1) <= 0)).astype(float).where(spread.notna(), np.nan)).diff()

def f55_lmps_046_trix_days_since_last_bearish_cross_252d_d1(close: pd.Series) -> pd.Series:
    """Bars since last TRIX bearish signal-line cross (capped 252)."""
    tr, sig = _trix_with_signal(close, 15, 9)
    spread = tr - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff()

def f55_lmps_047_trix_days_since_last_bullish_cross_252d_d1(close: pd.Series) -> pd.Series:
    """Bars since last TRIX bullish cross."""
    tr, sig = _trix_with_signal(close, 15, 9)
    spread = tr - sig
    ev = ((spread > 0) & (spread.shift(1) <= 0)).astype(float).where(spread.notna(), np.nan)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff()

def f55_lmps_048_trix_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of TRIX."""
    tr, sig = _trix_with_signal(close, 15, 9)
    return (_rolling_zscore(tr, YDAYS)).diff()

def f55_lmps_049_trix_bearish_cross_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of TRIX bearish signal-crosses in 252d."""
    tr, sig = _trix_with_signal(close, 15, 9)
    spread = tr - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff()

def f55_lmps_050_trix_negative_at_252d_high_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: TRIX < 0 AND close = 252d max."""
    tr, sig = _trix_with_signal(close, 15, 9)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((tr < 0) & (close >= rmax - 1e-12)).astype(float).where(tr.notna(), np.nan)).diff()

def f55_lmps_051_ppo_12_26_value_d1(close: pd.Series) -> pd.Series:
    """Percentage Price Oscillator(12,26) value."""
    ppo, sig = _ppo_with_signal(close)
    return (ppo).diff()

def f55_lmps_052_ppo_signal_9d_value_d1(close: pd.Series) -> pd.Series:
    """PPO signal-line."""
    ppo, sig = _ppo_with_signal(close)
    return (sig).diff()

def f55_lmps_053_ppo_minus_signal_d1(close: pd.Series) -> pd.Series:
    """PPO - signal."""
    ppo, sig = _ppo_with_signal(close)
    return (ppo - sig).diff()

def f55_lmps_054_ppo_zero_cross_down_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: PPO crosses below zero."""
    ppo, sig = _ppo_with_signal(close)
    up, dn = _zero_cross_events(ppo)
    return (dn).diff()

def f55_lmps_055_ppo_signal_bearish_cross_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: PPO crosses below its signal."""
    ppo, sig = _ppo_with_signal(close)
    spread = ppo - sig
    return (((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)).diff()

def f55_lmps_056_ppo_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of PPO."""
    ppo, sig = _ppo_with_signal(close)
    return (_rolling_zscore(ppo, YDAYS)).diff()

def f55_lmps_057_ppo_falling_at_252d_high_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: PPO < signal AND close = 252d max."""
    ppo, sig = _ppo_with_signal(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ppo < sig) & (close >= rmax - 1e-12)).astype(float).where(ppo.notna(), np.nan)).diff()

def f55_lmps_058_ppo_above_p90_252d_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: PPO above its 252d-p90 - extreme momentum."""
    ppo, sig = _ppo_with_signal(close)
    p90 = ppo.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((ppo > p90).astype(float).where(p90.notna(), np.nan)).diff()

def f55_lmps_059_ppo_overbought_above_5pct_persistence_63d_d1(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with PPO > 5%."""
    ppo, sig = _ppo_with_signal(close)
    return ((ppo > 5.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()).diff()

def f55_lmps_060_ppo_days_since_last_signal_bearish_cross_252d_d1(close: pd.Series) -> pd.Series:
    """Bars since last PPO bearish signal-cross (capped 252)."""
    ppo, sig = _ppo_with_signal(close)
    spread = ppo - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff()

def f55_lmps_061_coppock_annual_zero_cross_up_event_d1(close: pd.Series) -> pd.Series:
    """Coppock annual zero-cross UP event indicator (canonical Coppock 'buy' signal)."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    return (up).diff()

def f55_lmps_062_coppock_annual_zero_cross_down_event_d1(close: pd.Series) -> pd.Series:
    """Coppock zero-cross DOWN event indicator (sell-side reversal)."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    return (dn).diff()

def f55_lmps_063_coppock_zero_cross_at_252d_high_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: Coppock zero-cross-down AND close = 252d max - sell signal at top."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((dn * (close >= rmax - 1e-12).astype(float)).where(cop.notna(), np.nan)).diff()

def f55_lmps_064_coppock_below_zero_persistence_63d_d1(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with Coppock < 0."""
    cop = _coppock_annual(close)
    return ((cop < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()).diff()

def f55_lmps_065_coppock_above_zero_persistence_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of last 252d with Coppock > 0."""
    cop = _coppock_annual(close)
    return ((cop > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f55_lmps_066_coppock_days_since_last_zero_cross_d1(close: pd.Series) -> pd.Series:
    """Bars since last Coppock zero crossing (either direction; capped 504)."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    ev = (up + dn).clip(upper=1.0)
    return (_bars_since_last_event(ev).clip(upper=float(DDAYS_2Y))).diff()

def f55_lmps_067_coppock_zero_cross_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of Coppock zero crossings in 252d."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    return ((up + dn).rolling(YDAYS, min_periods=QDAYS).sum()).diff()

def f55_lmps_068_coppock_zero_cross_count_504d_d1(close: pd.Series) -> pd.Series:
    """Count of Coppock zero crossings in 504d."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    return ((up + dn).rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff()

def f55_lmps_069_coppock_2nd_derivative_at_zero_cross_down_d1(close: pd.Series) -> pd.Series:
    """Coppock d² value at bars where Coppock crosses down through zero."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    c_acc = cop.diff().diff()
    return (c_acc.where(dn > 0.5, np.nan)).diff()

def f55_lmps_070_coppock_falling_after_high_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: Coppock making lower-high after a 504d Coppock peak."""
    cop = _coppock_annual(close)
    mx_504 = cop.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    below_max = (cop < mx_504 - 1e-6).astype(float)
    decline = (cop.diff() < 0).astype(float)
    return ((below_max * decline).where(cop.notna(), np.nan)).diff()

def f55_lmps_071_kst_signal_bearish_cross_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: KST crosses below its signal line."""
    k = _kst(close)
    sig = _kst_signal(close)
    spread = k - sig
    return (((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)).diff()

def f55_lmps_072_kst_signal_bullish_cross_event_indicator_d1(close: pd.Series) -> pd.Series:
    """Indicator: KST crosses above its signal line."""
    k = _kst(close)
    sig = _kst_signal(close)
    spread = k - sig
    return (((spread > 0) & (spread.shift(1) <= 0)).astype(float).where(spread.notna(), np.nan)).diff()

def f55_lmps_073_kst_days_since_last_bearish_cross_252d_d1(close: pd.Series) -> pd.Series:
    """Bars since last KST bearish cross (capped 252)."""
    k = _kst(close)
    sig = _kst_signal(close)
    spread = k - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff()

def f55_lmps_074_kst_days_since_last_bullish_cross_252d_d1(close: pd.Series) -> pd.Series:
    """Bars since last KST bullish cross."""
    k = _kst(close)
    sig = _kst_signal(close)
    spread = k - sig
    ev = ((spread > 0) & (spread.shift(1) <= 0)).astype(float).where(spread.notna(), np.nan)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff()

def f55_lmps_075_kst_bearish_cross_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of KST bearish crosses in 252d."""
    k = _kst(close)
    sig = _kst_signal(close)
    spread = k - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


# ============================================================
#                         REGISTRY 001_075 (d1)
# ============================================================

LONG_MOMENTUM_SMOOTHED_PMO_D1_REGISTRY_001_075 = {
    "f55_lmps_001_mayer_multiple_close_sma200_d1": {"inputs": ["close"], "func": f55_lmps_001_mayer_multiple_close_sma200_d1},
    "f55_lmps_002_mayer_multiple_log_d1": {"inputs": ["close"], "func": f55_lmps_002_mayer_multiple_log_d1},
    "f55_lmps_003_mayer_multiple_zscore_504d_d1": {"inputs": ["close"], "func": f55_lmps_003_mayer_multiple_zscore_504d_d1},
    "f55_lmps_004_mayer_multiple_pct_rank_504d_d1": {"inputs": ["close"], "func": f55_lmps_004_mayer_multiple_pct_rank_504d_d1},
    "f55_lmps_005_mayer_multiple_pct_change_21d_d1": {"inputs": ["close"], "func": f55_lmps_005_mayer_multiple_pct_change_21d_d1},
    "f55_lmps_006_mayer_multiple_days_above_1_d1": {"inputs": ["close"], "func": f55_lmps_006_mayer_multiple_days_above_1_d1},
    "f55_lmps_007_mayer_multiple_days_above_1_5_d1": {"inputs": ["close"], "func": f55_lmps_007_mayer_multiple_days_above_1_5_d1},
    "f55_lmps_008_mayer_multiple_days_above_2_d1": {"inputs": ["close"], "func": f55_lmps_008_mayer_multiple_days_above_2_d1},
    "f55_lmps_009_mayer_multiple_above_p90_252d_indicator_d1": {"inputs": ["close"], "func": f55_lmps_009_mayer_multiple_above_p90_252d_indicator_d1},
    "f55_lmps_010_mayer_multiple_at_252d_high_x_above_2_indicator_d1": {"inputs": ["close"], "func": f55_lmps_010_mayer_multiple_at_252d_high_x_above_2_indicator_d1},
    "f55_lmps_011_pring_pmo_value_d1": {"inputs": ["close"], "func": f55_lmps_011_pring_pmo_value_d1},
    "f55_lmps_012_pring_pmo_signal_value_d1": {"inputs": ["close"], "func": f55_lmps_012_pring_pmo_signal_value_d1},
    "f55_lmps_013_pring_pmo_minus_signal_d1": {"inputs": ["close"], "func": f55_lmps_013_pring_pmo_minus_signal_d1},
    "f55_lmps_014_pring_pmo_bearish_signal_cross_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_014_pring_pmo_bearish_signal_cross_event_indicator_d1},
    "f55_lmps_015_pring_pmo_zero_cross_down_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_015_pring_pmo_zero_cross_down_event_indicator_d1},
    "f55_lmps_016_pring_pmo_days_since_top_504d_d1": {"inputs": ["close"], "func": f55_lmps_016_pring_pmo_days_since_top_504d_d1},
    "f55_lmps_017_pring_pmo_overbought_above_2_persistence_63d_d1": {"inputs": ["close"], "func": f55_lmps_017_pring_pmo_overbought_above_2_persistence_63d_d1},
    "f55_lmps_018_pring_pmo_zscore_252d_d1": {"inputs": ["close"], "func": f55_lmps_018_pring_pmo_zscore_252d_d1},
    "f55_lmps_019_pring_pmo_falling_at_252d_high_indicator_d1": {"inputs": ["close"], "func": f55_lmps_019_pring_pmo_falling_at_252d_high_indicator_d1},
    "f55_lmps_020_pring_pmo_bearish_cross_count_252d_d1": {"inputs": ["close"], "func": f55_lmps_020_pring_pmo_bearish_cross_count_252d_d1},
    "f55_lmps_021_pring_special_k_value_d1": {"inputs": ["close"], "func": f55_lmps_021_pring_special_k_value_d1},
    "f55_lmps_022_pring_special_k_signal_value_d1": {"inputs": ["close"], "func": f55_lmps_022_pring_special_k_signal_value_d1},
    "f55_lmps_023_pring_special_k_minus_signal_d1": {"inputs": ["close"], "func": f55_lmps_023_pring_special_k_minus_signal_d1},
    "f55_lmps_024_pring_special_k_zscore_252d_d1": {"inputs": ["close"], "func": f55_lmps_024_pring_special_k_zscore_252d_d1},
    "f55_lmps_025_pring_special_k_signal_bearish_cross_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_025_pring_special_k_signal_bearish_cross_event_indicator_d1},
    "f55_lmps_026_pring_special_k_days_since_top_504d_d1": {"inputs": ["close"], "func": f55_lmps_026_pring_special_k_days_since_top_504d_d1},
    "f55_lmps_027_pring_special_k_minus_kst_252d_d1": {"inputs": ["close"], "func": f55_lmps_027_pring_special_k_minus_kst_252d_d1},
    "f55_lmps_028_pring_special_k_above_p90_252d_indicator_d1": {"inputs": ["close"], "func": f55_lmps_028_pring_special_k_above_p90_252d_indicator_d1},
    "f55_lmps_029_pring_special_k_falling_at_252d_high_indicator_d1": {"inputs": ["close"], "func": f55_lmps_029_pring_special_k_falling_at_252d_high_indicator_d1},
    "f55_lmps_030_pring_special_k_long_horizon_decay_rate_252d_d1": {"inputs": ["close"], "func": f55_lmps_030_pring_special_k_long_horizon_decay_rate_252d_d1},
    "f55_lmps_031_dpo_10d_value_d1": {"inputs": ["close"], "func": f55_lmps_031_dpo_10d_value_d1},
    "f55_lmps_032_dpo_21d_value_d1": {"inputs": ["close"], "func": f55_lmps_032_dpo_21d_value_d1},
    "f55_lmps_033_dpo_63d_value_d1": {"inputs": ["close"], "func": f55_lmps_033_dpo_63d_value_d1},
    "f55_lmps_034_dpo_126d_value_d1": {"inputs": ["close"], "func": f55_lmps_034_dpo_126d_value_d1},
    "f55_lmps_035_dpo_252d_value_d1": {"inputs": ["close"], "func": f55_lmps_035_dpo_252d_value_d1},
    "f55_lmps_036_dpo_10d_zscore_252d_d1": {"inputs": ["close"], "func": f55_lmps_036_dpo_10d_zscore_252d_d1},
    "f55_lmps_037_dpo_21d_zscore_252d_d1": {"inputs": ["close"], "func": f55_lmps_037_dpo_21d_zscore_252d_d1},
    "f55_lmps_038_dpo_63d_zscore_252d_d1": {"inputs": ["close"], "func": f55_lmps_038_dpo_63d_zscore_252d_d1},
    "f55_lmps_039_dpo_126d_zscore_252d_d1": {"inputs": ["close"], "func": f55_lmps_039_dpo_126d_zscore_252d_d1},
    "f55_lmps_040_dpo_multi_horizon_all_negative_count_252d_d1": {"inputs": ["close"], "func": f55_lmps_040_dpo_multi_horizon_all_negative_count_252d_d1},
    "f55_lmps_041_trix_15d_value_d1": {"inputs": ["close"], "func": f55_lmps_041_trix_15d_value_d1},
    "f55_lmps_042_trix_signal_9d_value_d1": {"inputs": ["close"], "func": f55_lmps_042_trix_signal_9d_value_d1},
    "f55_lmps_043_trix_minus_signal_15d_d1": {"inputs": ["close"], "func": f55_lmps_043_trix_minus_signal_15d_d1},
    "f55_lmps_044_trix_signal_bearish_cross_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_044_trix_signal_bearish_cross_event_indicator_d1},
    "f55_lmps_045_trix_signal_bullish_cross_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_045_trix_signal_bullish_cross_event_indicator_d1},
    "f55_lmps_046_trix_days_since_last_bearish_cross_252d_d1": {"inputs": ["close"], "func": f55_lmps_046_trix_days_since_last_bearish_cross_252d_d1},
    "f55_lmps_047_trix_days_since_last_bullish_cross_252d_d1": {"inputs": ["close"], "func": f55_lmps_047_trix_days_since_last_bullish_cross_252d_d1},
    "f55_lmps_048_trix_zscore_252d_d1": {"inputs": ["close"], "func": f55_lmps_048_trix_zscore_252d_d1},
    "f55_lmps_049_trix_bearish_cross_count_252d_d1": {"inputs": ["close"], "func": f55_lmps_049_trix_bearish_cross_count_252d_d1},
    "f55_lmps_050_trix_negative_at_252d_high_indicator_d1": {"inputs": ["close"], "func": f55_lmps_050_trix_negative_at_252d_high_indicator_d1},
    "f55_lmps_051_ppo_12_26_value_d1": {"inputs": ["close"], "func": f55_lmps_051_ppo_12_26_value_d1},
    "f55_lmps_052_ppo_signal_9d_value_d1": {"inputs": ["close"], "func": f55_lmps_052_ppo_signal_9d_value_d1},
    "f55_lmps_053_ppo_minus_signal_d1": {"inputs": ["close"], "func": f55_lmps_053_ppo_minus_signal_d1},
    "f55_lmps_054_ppo_zero_cross_down_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_054_ppo_zero_cross_down_event_indicator_d1},
    "f55_lmps_055_ppo_signal_bearish_cross_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_055_ppo_signal_bearish_cross_event_indicator_d1},
    "f55_lmps_056_ppo_zscore_252d_d1": {"inputs": ["close"], "func": f55_lmps_056_ppo_zscore_252d_d1},
    "f55_lmps_057_ppo_falling_at_252d_high_indicator_d1": {"inputs": ["close"], "func": f55_lmps_057_ppo_falling_at_252d_high_indicator_d1},
    "f55_lmps_058_ppo_above_p90_252d_indicator_d1": {"inputs": ["close"], "func": f55_lmps_058_ppo_above_p90_252d_indicator_d1},
    "f55_lmps_059_ppo_overbought_above_5pct_persistence_63d_d1": {"inputs": ["close"], "func": f55_lmps_059_ppo_overbought_above_5pct_persistence_63d_d1},
    "f55_lmps_060_ppo_days_since_last_signal_bearish_cross_252d_d1": {"inputs": ["close"], "func": f55_lmps_060_ppo_days_since_last_signal_bearish_cross_252d_d1},
    "f55_lmps_061_coppock_annual_zero_cross_up_event_d1": {"inputs": ["close"], "func": f55_lmps_061_coppock_annual_zero_cross_up_event_d1},
    "f55_lmps_062_coppock_annual_zero_cross_down_event_d1": {"inputs": ["close"], "func": f55_lmps_062_coppock_annual_zero_cross_down_event_d1},
    "f55_lmps_063_coppock_zero_cross_at_252d_high_indicator_d1": {"inputs": ["close"], "func": f55_lmps_063_coppock_zero_cross_at_252d_high_indicator_d1},
    "f55_lmps_064_coppock_below_zero_persistence_63d_d1": {"inputs": ["close"], "func": f55_lmps_064_coppock_below_zero_persistence_63d_d1},
    "f55_lmps_065_coppock_above_zero_persistence_252d_d1": {"inputs": ["close"], "func": f55_lmps_065_coppock_above_zero_persistence_252d_d1},
    "f55_lmps_066_coppock_days_since_last_zero_cross_d1": {"inputs": ["close"], "func": f55_lmps_066_coppock_days_since_last_zero_cross_d1},
    "f55_lmps_067_coppock_zero_cross_count_252d_d1": {"inputs": ["close"], "func": f55_lmps_067_coppock_zero_cross_count_252d_d1},
    "f55_lmps_068_coppock_zero_cross_count_504d_d1": {"inputs": ["close"], "func": f55_lmps_068_coppock_zero_cross_count_504d_d1},
    "f55_lmps_069_coppock_2nd_derivative_at_zero_cross_down_d1": {"inputs": ["close"], "func": f55_lmps_069_coppock_2nd_derivative_at_zero_cross_down_d1},
    "f55_lmps_070_coppock_falling_after_high_indicator_d1": {"inputs": ["close"], "func": f55_lmps_070_coppock_falling_after_high_indicator_d1},
    "f55_lmps_071_kst_signal_bearish_cross_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_071_kst_signal_bearish_cross_event_indicator_d1},
    "f55_lmps_072_kst_signal_bullish_cross_event_indicator_d1": {"inputs": ["close"], "func": f55_lmps_072_kst_signal_bullish_cross_event_indicator_d1},
    "f55_lmps_073_kst_days_since_last_bearish_cross_252d_d1": {"inputs": ["close"], "func": f55_lmps_073_kst_days_since_last_bearish_cross_252d_d1},
    "f55_lmps_074_kst_days_since_last_bullish_cross_252d_d1": {"inputs": ["close"], "func": f55_lmps_074_kst_days_since_last_bullish_cross_252d_d1},
    "f55_lmps_075_kst_bearish_cross_count_252d_d1": {"inputs": ["close"], "func": f55_lmps_075_kst_bearish_cross_count_252d_d1},
}
