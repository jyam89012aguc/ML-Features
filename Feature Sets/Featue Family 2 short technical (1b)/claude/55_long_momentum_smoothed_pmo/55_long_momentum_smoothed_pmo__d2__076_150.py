"""long_momentum_smoothed_pmo d2 features 076-150 - Pipeline 1b-technical.

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


def f55_lmps_076_kst_at_252d_max_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: KST = 252d max."""
    k = _kst(close)
    mx = k.rolling(YDAYS, min_periods=QDAYS).max()
    return ((k >= mx - 1e-9).astype(float).where(k.notna(), np.nan)).diff().diff()

def f55_lmps_077_kst_signal_cross_at_overbought_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: KST bearish cross AND KST > 252d-p75."""
    k = _kst(close)
    sig = _kst_signal(close)
    spread = k - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    p75 = k.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return ((ev * (k > p75).astype(float)).where(p75.notna(), np.nan)).diff().diff()

def f55_lmps_078_kst_signal_cross_at_252d_high_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: KST bearish cross AND close = 252d max."""
    k = _kst(close)
    sig = _kst_signal(close)
    spread = k - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float))).diff().diff()

def f55_lmps_079_kst_negative_at_252d_high_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: KST < 0 AND close = 252d max."""
    k = _kst(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((k < 0) & (close >= rmax - 1e-12)).astype(float).where(k.notna(), np.nan)).diff().diff()

def f55_lmps_080_kst_cross_velocity_252d_d2(close: pd.Series) -> pd.Series:
    """KST bearish cross count / 252 - frequency."""
    k = _kst(close)
    sig = _kst_signal(close)
    spread = k - sig
    ev = ((spread < 0) & (spread.shift(1) >= 0)).astype(float).where(spread.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)).diff().diff()

def f55_lmps_081_momentum_stack_alignment_bullish_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: KST > 0 AND PMO > 0 AND Coppock > 0 - aligned bullish long-term momentum."""
    k = _kst(close)
    pmo, sig = _pring_pmo(close)
    cop = _coppock_annual(close)
    return (((k > 0) & (pmo > 0) & (cop > 0)).astype(float).where(k.notna() & pmo.notna() & cop.notna(), np.nan)).diff().diff()

def f55_lmps_082_momentum_stack_alignment_bearish_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: KST < 0 AND PMO < 0 AND Coppock < 0 - aligned bearish long-term momentum."""
    k = _kst(close)
    pmo, sig = _pring_pmo(close)
    cop = _coppock_annual(close)
    return (((k < 0) & (pmo < 0) & (cop < 0)).astype(float).where(k.notna() & pmo.notna() & cop.notna(), np.nan)).diff().diff()

def f55_lmps_083_momentum_stack_breadth_above_zero_count_d2(close: pd.Series) -> pd.Series:
    """Count of {KST, PMO, Coppock, TRIX, PPO} above zero at current bar (0-5)."""
    k = _kst(close)
    pmo, sig1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, sig2 = _trix_with_signal(close, 15, 9)
    ppo, sig3 = _ppo_with_signal(close)
    cnt = (k > 0).astype(float) + (pmo > 0).astype(float) + (cop > 0).astype(float) + (tr > 0).astype(float) + (ppo > 0).astype(float)
    return (cnt.where(k.notna() & pmo.notna() & cop.notna() & tr.notna() & ppo.notna(), np.nan)).diff().diff()

def f55_lmps_084_momentum_stack_breadth_below_zero_count_d2(close: pd.Series) -> pd.Series:
    """Count of 5 oscillators below zero at current bar."""
    k = _kst(close)
    pmo, sig1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, sig2 = _trix_with_signal(close, 15, 9)
    ppo, sig3 = _ppo_with_signal(close)
    cnt = (k < 0).astype(float) + (pmo < 0).astype(float) + (cop < 0).astype(float) + (tr < 0).astype(float) + (ppo < 0).astype(float)
    return (cnt.where(k.notna() & pmo.notna() & cop.notna() & tr.notna() & ppo.notna(), np.nan)).diff().diff()

def f55_lmps_085_momentum_stack_consensus_zscore_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of 252d z-scores of 5 oscillators."""
    k = _kst(close)
    pmo, sig1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, sig2 = _trix_with_signal(close, 15, 9)
    ppo, sig3 = _ppo_with_signal(close)
    zs = (_rolling_zscore(k, YDAYS) + _rolling_zscore(pmo, YDAYS) + _rolling_zscore(cop, YDAYS)
          + _rolling_zscore(tr, YDAYS) + _rolling_zscore(ppo, YDAYS)) / 5.0
    return (zs).diff().diff()

def f55_lmps_086_momentum_stack_disagreement_max_minus_min_252d_d2(close: pd.Series) -> pd.Series:
    """Max - Min of z-scores across 5 oscillators - disagreement."""
    k = _kst(close)
    pmo, sig1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, sig2 = _trix_with_signal(close, 15, 9)
    ppo, sig3 = _ppo_with_signal(close)
    df = pd.concat([_rolling_zscore(k, YDAYS).rename('a'),
                    _rolling_zscore(pmo, YDAYS).rename('b'),
                    _rolling_zscore(cop, YDAYS).rename('c'),
                    _rolling_zscore(tr, YDAYS).rename('d'),
                    _rolling_zscore(ppo, YDAYS).rename('e')], axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff()

def f55_lmps_087_momentum_stack_alignment_bull_persistence_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 252d with bullish stack alignment."""
    k = _kst(close)
    pmo, sig1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    ind = ((k > 0) & (pmo > 0) & (cop > 0)).astype(float).where(
        k.notna() & pmo.notna() & cop.notna(), np.nan)
    return (ind.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f55_lmps_088_momentum_stack_alignment_bear_persistence_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 252d with bearish stack alignment."""
    k = _kst(close)
    pmo, sig1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    ind = ((k < 0) & (pmo < 0) & (cop < 0)).astype(float).where(
        k.notna() & pmo.notna() & cop.notna(), np.nan)
    return (ind.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f55_lmps_089_momentum_stack_acceleration_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of 1st differences of 5 z-scored oscillators - aggregate acceleration."""
    k = _kst(close)
    pmo, sig1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, sig2 = _trix_with_signal(close, 15, 9)
    ppo, sig3 = _ppo_with_signal(close)
    zs = (_rolling_zscore(k, YDAYS) + _rolling_zscore(pmo, YDAYS) + _rolling_zscore(cop, YDAYS)
          + _rolling_zscore(tr, YDAYS) + _rolling_zscore(ppo, YDAYS)) / 5.0
    return (zs.diff()).diff().diff()

def f55_lmps_090_momentum_stack_regime_change_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: stack-alignment flips from bull to bear within 21 bars."""
    k = _kst(close)
    pmo, sig1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    bull = ((k > 0) & (pmo > 0) & (cop > 0)).astype(float)
    bear = ((k < 0) & (pmo < 0) & (cop < 0)).astype(float)
    had_bull = bull.shift(MDAYS).rolling(MDAYS, min_periods=5).max()
    return (((had_bull > 0.5) & (bear > 0.5)).astype(float).where(k.notna(), np.nan)).diff().diff()

def f55_lmps_091_coppock_peak_value_504d_d2(close: pd.Series) -> pd.Series:
    """Max Coppock value in last 504d."""
    cop = _coppock_annual(close)
    return (cop.rolling(DDAYS_2Y, min_periods=YDAYS).max()).diff().diff()

def f55_lmps_092_coppock_trough_value_504d_d2(close: pd.Series) -> pd.Series:
    """Min Coppock value in last 504d."""
    cop = _coppock_annual(close)
    return (cop.rolling(DDAYS_2Y, min_periods=YDAYS).min()).diff().diff()

def f55_lmps_093_coppock_days_since_504d_peak_d2(close: pd.Series) -> pd.Series:
    """Bars since Coppock 504d peak."""
    cop = _coppock_annual(close)
    return (_days_since_max_in_window(cop, DDAYS_2Y)).diff().diff()

def f55_lmps_094_coppock_days_since_504d_trough_d2(close: pd.Series) -> pd.Series:
    """Bars since Coppock 504d trough."""
    cop = _coppock_annual(close)
    return (_days_since_min_in_window(cop, DDAYS_2Y)).diff().diff()

def f55_lmps_095_coppock_peak_to_current_decay_pct_d2(close: pd.Series) -> pd.Series:
    """(Coppock current - 504d-max) / 504d-max - current % below peak."""
    cop = _coppock_annual(close)
    mx = cop.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return (_safe_div(cop - mx, mx.abs() + 1e-9)).diff().diff()

def f55_lmps_096_coppock_cycle_amplitude_504d_d2(close: pd.Series) -> pd.Series:
    """504d max - 504d min of Coppock - cycle amplitude."""
    cop = _coppock_annual(close)
    return (cop.rolling(DDAYS_2Y, min_periods=YDAYS).max() - cop.rolling(DDAYS_2Y, min_periods=YDAYS).min()).diff().diff()

def f55_lmps_097_coppock_cycle_position_pct_504d_d2(close: pd.Series) -> pd.Series:
    """(Coppock - min) / (max - min) over 504d - position within cycle range (0..1)."""
    cop = _coppock_annual(close)
    mx = cop.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    mn = cop.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return (_safe_div(cop - mn, mx - mn)).diff().diff()

def f55_lmps_098_coppock_peaks_count_504d_d2(close: pd.Series) -> pd.Series:
    """Count of Coppock zero-cross-up events in last 504d (cycle starts)."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    return (up.rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff().diff()

def f55_lmps_099_coppock_current_minus_peak_zscore_504d_d2(close: pd.Series) -> pd.Series:
    """Z-score over 504d of (Coppock - 504d peak)."""
    cop = _coppock_annual(close)
    mx = cop.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return (_rolling_zscore(cop - mx, DDAYS_2Y)).diff().diff()

def f55_lmps_100_coppock_post_peak_decline_persistence_63d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 63d where Coppock is declining from peak (cop < cop.shift(21))."""
    cop = _coppock_annual(close)
    ind = (cop < cop.shift(MDAYS)).astype(float).where(cop.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f55_lmps_101_coppock_pct_rank_504d_d2(close: pd.Series) -> pd.Series:
    """504d percentile rank of Coppock."""
    cop = _coppock_annual(close)
    return (_rolling_pct_rank(cop, DDAYS_2Y)).diff().diff()

def f55_lmps_102_coppock_pct_rank_1260d_d2(close: pd.Series) -> pd.Series:
    """1260d percentile rank of Coppock."""
    cop = _coppock_annual(close)
    return (_rolling_pct_rank(cop, DDAYS_5Y)).diff().diff()

def f55_lmps_103_kst_pct_rank_504d_d2(close: pd.Series) -> pd.Series:
    """504d pct-rank of KST."""
    k = _kst(close)
    return (_rolling_pct_rank(k, DDAYS_2Y)).diff().diff()

def f55_lmps_104_pmo_pct_rank_504d_d2(close: pd.Series) -> pd.Series:
    """504d pct-rank of PMO."""
    pmo, sig = _pring_pmo(close)
    return (_rolling_pct_rank(pmo, DDAYS_2Y)).diff().diff()

def f55_lmps_105_pmo_pct_rank_1260d_d2(close: pd.Series) -> pd.Series:
    """1260d pct-rank of PMO."""
    pmo, sig = _pring_pmo(close)
    return (_rolling_pct_rank(pmo, DDAYS_5Y)).diff().diff()

def f55_lmps_106_special_k_pct_rank_504d_d2(close: pd.Series) -> pd.Series:
    """504d pct-rank of Special K."""
    sk = _pring_special_k(close)
    return (_rolling_pct_rank(sk, DDAYS_2Y)).diff().diff()

def f55_lmps_107_trix_pct_rank_504d_d2(close: pd.Series) -> pd.Series:
    """504d pct-rank of TRIX."""
    tr, sig = _trix_with_signal(close, 15, 9)
    return (_rolling_pct_rank(tr, DDAYS_2Y)).diff().diff()

def f55_lmps_108_ppo_pct_rank_504d_d2(close: pd.Series) -> pd.Series:
    """504d pct-rank of PPO."""
    ppo, sig = _ppo_with_signal(close)
    return (_rolling_pct_rank(ppo, DDAYS_2Y)).diff().diff()

def f55_lmps_109_dpo_63d_pct_rank_504d_d2(close: pd.Series) -> pd.Series:
    """504d pct-rank of DPO(63)."""
    dpo = close - _sma(close, 63)
    return (_rolling_pct_rank(dpo, DDAYS_2Y)).diff().diff()

def f55_lmps_110_multi_momentum_avg_rank_504d_d2(close: pd.Series) -> pd.Series:
    """Mean of 504d pct-ranks across {Coppock, KST, PMO, TRIX, PPO}."""
    cop = _coppock_annual(close); k = _kst(close); pmo, _s1 = _pring_pmo(close)
    tr, _s2 = _trix_with_signal(close, 15, 9); ppo, _s3 = _ppo_with_signal(close)
    r = (_rolling_pct_rank(cop, DDAYS_2Y) + _rolling_pct_rank(k, DDAYS_2Y)
         + _rolling_pct_rank(pmo, DDAYS_2Y) + _rolling_pct_rank(tr, DDAYS_2Y)
         + _rolling_pct_rank(ppo, DDAYS_2Y)) / 5.0
    return (r).diff().diff()

def f55_lmps_111_roc_composite_pring_weighted_value_d2(close: pd.Series) -> pd.Series:
    """Pring KST raw composite (no smoothing) - sum of weighted ROCs at 10/15/20/30."""
    r1 = _roc(close, 10); r2 = _roc(close, 15); r3 = _roc(close, 20); r4 = _roc(close, 30)
    return (r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4).diff().diff()

def f55_lmps_112_roc_composite_pring_smoothed_9d_d2(close: pd.Series) -> pd.Series:
    """Pring composite ROC smoothed with 9-EMA."""
    r1 = _roc(close, 10); r2 = _roc(close, 15); r3 = _roc(close, 20); r4 = _roc(close, 30)
    comp = r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4
    return (comp.ewm(span=9, adjust=False, min_periods=3).mean()).diff().diff()

def f55_lmps_113_roc_short_med_long_composite_z_252d_d2(close: pd.Series) -> pd.Series:
    """Mean z-score across ROC(10)/ROC(63)/ROC(252) - aggregate momentum z."""
    r1 = _roc(close, 10); r2 = _roc(close, 63); r3 = _roc(close, 252)
    z = (_rolling_zscore(r1, YDAYS) + _rolling_zscore(r2, YDAYS) + _rolling_zscore(r3, YDAYS)) / 3.0
    return (z).diff().diff()

def f55_lmps_114_roc_short_med_long_all_positive_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: ROC(10)>0 AND ROC(63)>0 AND ROC(252)>0."""
    r1 = _roc(close, 10); r2 = _roc(close, 63); r3 = _roc(close, 252)
    return (((r1 > 0) & (r2 > 0) & (r3 > 0)).astype(float).where(r1.notna() & r2.notna() & r3.notna(), np.nan)).diff().diff()

def f55_lmps_115_roc_short_med_long_all_negative_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: ROC(10)<0 AND ROC(63)<0 AND ROC(252)<0."""
    r1 = _roc(close, 10); r2 = _roc(close, 63); r3 = _roc(close, 252)
    return (((r1 < 0) & (r2 < 0) & (r3 < 0)).astype(float).where(r1.notna() & r2.notna() & r3.notna(), np.nan)).diff().diff()

def f55_lmps_116_roc_consensus_z_252d_composite_d2(close: pd.Series) -> pd.Series:
    """Mean of 252d z-scores across ROC at 5 horizons."""
    r5 = _roc(close, 5); r21 = _roc(close, 21); r63 = _roc(close, 63); r126 = _roc(close, 126); r252 = _roc(close, 252)
    z = (_rolling_zscore(r5, YDAYS) + _rolling_zscore(r21, YDAYS) + _rolling_zscore(r63, YDAYS)
         + _rolling_zscore(r126, YDAYS) + _rolling_zscore(r252, YDAYS)) / 5.0
    return (z).diff().diff()

def f55_lmps_117_roc_cross_horizon_disagreement_max_minus_min_252d_d2(close: pd.Series) -> pd.Series:
    """Max - Min of 252d z-scores of ROCs at 5 horizons."""
    r5 = _roc(close, 5); r21 = _roc(close, 21); r63 = _roc(close, 63); r126 = _roc(close, 126); r252 = _roc(close, 252)
    df = pd.concat([_rolling_zscore(r5, YDAYS).rename('a'),
                    _rolling_zscore(r21, YDAYS).rename('b'),
                    _rolling_zscore(r63, YDAYS).rename('c'),
                    _rolling_zscore(r126, YDAYS).rename('d'),
                    _rolling_zscore(r252, YDAYS).rename('e')], axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff()

def f55_lmps_118_roc_acceleration_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Mean(d²ROC at 5 horizons) over 252d."""
    r5 = _roc(close, 5); r21 = _roc(close, 21); r63 = _roc(close, 63); r126 = _roc(close, 126); r252 = _roc(close, 252)
    acc = (r5.diff().diff() + r21.diff().diff() + r63.diff().diff() + r126.diff().diff() + r252.diff().diff()) / 5.0
    return (acc).diff().diff()

def f55_lmps_119_roc_velocity_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of slopes of ROC at multiple horizons over 252d."""
    r5 = _roc(close, 5); r21 = _roc(close, 21); r63 = _roc(close, 63); r126 = _roc(close, 126); r252 = _roc(close, 252)
    vs = (_rolling_slope(r5, MDAYS) + _rolling_slope(r21, MDAYS) + _rolling_slope(r63, MDAYS)
          + _rolling_slope(r126, MDAYS) + _rolling_slope(r252, MDAYS)) / 5.0
    return (vs).diff().diff()

def f55_lmps_120_roc_long_horizon_decay_rate_252d_d2(close: pd.Series) -> pd.Series:
    """21-bar diff of ROC(252) / current ROC(252) - long-horizon decay rate."""
    r252 = _roc(close, 252)
    return (_safe_div(r252 - r252.shift(MDAYS), r252.abs() + 1e-9)).diff().diff()

def f55_lmps_121_smoothed_252d_momentum_sign_changes_count_d2(close: pd.Series) -> pd.Series:
    """Count of sign changes of SMA63-smoothed log_ret over 252d."""
    r = _safe_log(close).diff()
    sm = r.rolling(QDAYS, min_periods=MDAYS).mean()
    sgn = np.sign(sm.fillna(0.0))
    flip = ((sgn != sgn.shift(1)) & (sgn != 0)).astype(float)
    return (flip.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f55_lmps_122_smoothed_504d_momentum_sign_changes_count_d2(close: pd.Series) -> pd.Series:
    """Count of sign changes of SMA126-smoothed log_ret over 504d."""
    r = _safe_log(close).diff()
    sm = r.rolling(126, min_periods=QDAYS).mean()
    sgn = np.sign(sm.fillna(0.0))
    flip = ((sgn != sgn.shift(1)) & (sgn != 0)).astype(float)
    return (flip.rolling(DDAYS_2Y, min_periods=YDAYS).sum()).diff().diff()

def f55_lmps_123_coppock_sign_change_at_252d_high_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: Coppock sign-change (either dir) AND close = 252d max."""
    cop = _coppock_annual(close)
    up, dn = _zero_cross_events(cop)
    ev = (up + dn).clip(upper=1.0)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float))).diff().diff()

def f55_lmps_124_kst_sign_change_at_252d_high_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: KST sign-change AND close = 252d max."""
    k = _kst(close)
    up, dn = _zero_cross_events(k)
    ev = (up + dn).clip(upper=1.0)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float))).diff().diff()

def f55_lmps_125_pmo_sign_change_at_252d_high_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: PMO sign-change AND close = 252d max."""
    pmo, sig = _pring_pmo(close)
    up, dn = _zero_cross_events(pmo)
    ev = (up + dn).clip(upper=1.0)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((ev * (close >= rmax - 1e-12).astype(float))).diff().diff()

def f55_lmps_126_all_three_oscillators_sign_change_simultaneous_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where Coppock, KST, PMO all change sign within 5 bars of each other."""
    cop = _coppock_annual(close); k = _kst(close); pmo, _s = _pring_pmo(close)
    u1, d1 = _zero_cross_events(cop); u2, d2 = _zero_cross_events(k); u3, d3 = _zero_cross_events(pmo)
    e1 = (u1 + d1).clip(upper=1.0); e2 = (u2 + d2).clip(upper=1.0); e3 = (u3 + d3).clip(upper=1.0)
    joint = (e1.rolling(WDAYS, min_periods=1).max() * e2.rolling(WDAYS, min_periods=1).max() * e3.rolling(WDAYS, min_periods=1).max())
    return (joint.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f55_lmps_127_major_momentum_regime_shift_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: avg 5-osc z drops more than 1.5 std over 21d - regime-shift."""
    k = _kst(close)
    pmo, _s1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, _s2 = _trix_with_signal(close, 15, 9)
    ppo, _s3 = _ppo_with_signal(close)
    zs = (_rolling_zscore(k, YDAYS) + _rolling_zscore(pmo, YDAYS) + _rolling_zscore(cop, YDAYS)
          + _rolling_zscore(tr, YDAYS) + _rolling_zscore(ppo, YDAYS)) / 5.0
    drop = zs.shift(MDAYS) - zs
    return ((drop > 1.5).astype(float).where(zs.notna(), np.nan)).diff().diff()

def f55_lmps_128_long_term_momentum_failure_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: avg 5-osc z below -1 AND close = 252d max - momentum failure at high."""
    k = _kst(close)
    pmo, _s1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, _s2 = _trix_with_signal(close, 15, 9)
    ppo, _s3 = _ppo_with_signal(close)
    zs = (_rolling_zscore(k, YDAYS) + _rolling_zscore(pmo, YDAYS) + _rolling_zscore(cop, YDAYS)
          + _rolling_zscore(tr, YDAYS) + _rolling_zscore(ppo, YDAYS)) / 5.0
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((zs < -1.0) & (close >= rmax - 1e-12)).astype(float).where(zs.notna(), np.nan)).diff().diff()

def f55_lmps_129_cycle_completion_indicator_double_top_coppock_504d_d2(close: pd.Series) -> pd.Series:
    """Indicator: Coppock prints two peaks within 504d AND second peak <= first."""
    cop = _coppock_annual(close)
    p_ph = cop.where(cop == cop.rolling(63, center=False).max(), np.nan).shift(0)
    p_arr = p_ph.values; nb = len(p_arr); out = np.full(nb, np.nan); history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]):
            recent = [h for h in history if (t - h[0]) <= DDAYS_2Y]
            if recent:
                prev = recent[-1]
                out[t] = 1.0 if p_arr[t] <= prev[1] + 1e-9 else 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f55_lmps_130_cycle_completion_indicator_double_bottom_coppock_504d_d2(close: pd.Series) -> pd.Series:
    """Indicator: Coppock prints two troughs within 504d AND second trough >= first."""
    cop = _coppock_annual(close)
    p_pl = cop.where(cop == cop.rolling(63, center=False).min(), np.nan).shift(0)
    p_arr = p_pl.values; nb = len(p_arr); out = np.full(nb, np.nan); history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]):
            recent = [h for h in history if (t - h[0]) <= DDAYS_2Y]
            if recent:
                prev = recent[-1]
                out[t] = 1.0 if p_arr[t] >= prev[1] - 1e-9 else 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f55_lmps_131_coppock_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """21-bar diff of 1-bar diff of Coppock - acceleration."""
    cop = _coppock_annual(close)
    return (cop.diff().diff()).diff().diff()

def f55_lmps_132_coppock_jerk_252d_d2(close: pd.Series) -> pd.Series:
    """21-bar diff of acceleration of Coppock."""
    cop = _coppock_annual(close)
    return (cop.diff().diff().diff()).diff().diff()

def f55_lmps_133_pmo_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """PMO 2nd derivative."""
    pmo, sig = _pring_pmo(close)
    return (pmo.diff().diff()).diff().diff()

def f55_lmps_134_kst_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """KST 2nd derivative."""
    k = _kst(close)
    return (k.diff().diff()).diff().diff()

def f55_lmps_135_trix_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """TRIX 2nd derivative."""
    tr, sig = _trix_with_signal(close, 15, 9)
    return (tr.diff().diff()).diff().diff()

def f55_lmps_136_special_k_acceleration_252d_d2(close: pd.Series) -> pd.Series:
    """Special K 2nd derivative."""
    sk = _pring_special_k(close)
    return (sk.diff().diff()).diff().diff()

def f55_lmps_137_momentum_acceleration_decline_at_high_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: avg 2nd-derivative of 5 oscillators < 0 AND close = 252d max."""
    k = _kst(close)
    pmo, _s1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, _s2 = _trix_with_signal(close, 15, 9)
    ppo, _s3 = _ppo_with_signal(close)
    acc = (k.diff().diff() + pmo.diff().diff() + cop.diff().diff() + tr.diff().diff() + ppo.diff().diff()) / 5.0
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((acc < 0) & (close >= rmax - 1e-12)).astype(float).where(acc.notna(), np.nan)).diff().diff()

def f55_lmps_138_momentum_deceleration_persistence_63d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 63d where avg 2nd-derivative of 5 oscillators < 0."""
    k = _kst(close)
    pmo, _s1 = _pring_pmo(close)
    cop = _coppock_annual(close)
    tr, _s2 = _trix_with_signal(close, 15, 9)
    ppo, _s3 = _ppo_with_signal(close)
    acc = (k.diff().diff() + pmo.diff().diff() + cop.diff().diff() + tr.diff().diff() + ppo.diff().diff()) / 5.0
    return ((acc < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f55_lmps_139_momentum_d2_negative_with_d1_positive_count_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where 2nd-derivative of KST < 0 AND 1st-derivative > 0."""
    k = _kst(close)
    k1 = k.diff(); k2 = k.diff().diff()
    return (((k2 < 0) & (k1 > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f55_lmps_140_momentum_curvature_change_event_252d_d2(close: pd.Series) -> pd.Series:
    """Indicator: sign change of 2nd-derivative of KST."""
    k = _kst(close)
    k2 = k.diff().diff()
    sgn = np.sign(k2.fillna(0.0))
    return (((sgn != sgn.shift(1)) & (sgn != 0)).astype(float).where(k.notna(), np.nan)).diff().diff()

def f55_lmps_141_master_long_term_momentum_score_252d_d2(close: pd.Series) -> pd.Series:
    """Aggregate z-sum of: Mayer, PMO, KST, Coppock, Special K, TRIX, PPO over 252d."""
    mm = _safe_div(close, _sma(close, 200))
    pmo, _ = _pring_pmo(close)
    k = _kst(close)
    cop = _coppock_annual(close)
    sk = _pring_special_k(close)
    tr, _ = _trix_with_signal(close, 15, 9)
    ppo, _ = _ppo_with_signal(close)
    z = (_rolling_zscore(mm, YDAYS) + _rolling_zscore(pmo, YDAYS) + _rolling_zscore(k, YDAYS)
         + _rolling_zscore(cop, YDAYS) + _rolling_zscore(sk, YDAYS)
         + _rolling_zscore(tr, YDAYS) + _rolling_zscore(ppo, YDAYS))
    return (z).diff().diff()

def f55_lmps_142_blowoff_smoothed_momentum_signature_252d_d2(close: pd.Series) -> pd.Series:
    """Mayer * (PMO z) * close-z over 252d - blowoff distribution profile."""
    mm = _safe_div(close, _sma(close, 200))
    pmo, _ = _pring_pmo(close)
    z_pmo = _rolling_zscore(pmo, YDAYS)
    z_c = _rolling_zscore(_safe_log(close), YDAYS)
    return (mm * z_pmo * z_c).diff().diff()

def f55_lmps_143_coppock_kst_pmo_alignment_composite_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of indicator (Coppock>0) + (KST>0) + (PMO>0) - alignment 0..3."""
    k = _kst(close); pmo, _ = _pring_pmo(close); cop = _coppock_annual(close)
    return (((k > 0).astype(float) + (pmo > 0).astype(float) + (cop > 0).astype(float))).diff().diff()

def f55_lmps_144_multi_oscillator_overbought_breadth_count_252d_d2(close: pd.Series) -> pd.Series:
    """Count of {KST, PMO, Coppock, TRIX, PPO} above their 252d-p75 - overbought breadth."""
    k = _kst(close); pmo, _ = _pring_pmo(close); cop = _coppock_annual(close)
    tr, _ = _trix_with_signal(close, 15, 9); ppo, _ = _ppo_with_signal(close)
    pk = k.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    pp = pmo.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    pc = cop.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    pt = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    px = ppo.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (((k > pk).astype(float) + (pmo > pp).astype(float) + (cop > pc).astype(float)
         + (tr > pt).astype(float) + (ppo > px).astype(float))).diff().diff()

def f55_lmps_145_composite_smoothed_momentum_peak_persistence_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 252d where momentum-stack-bullish-alignment is true."""
    k = _kst(close); pmo, _ = _pring_pmo(close); cop = _coppock_annual(close)
    ind = ((k > 0) & (pmo > 0) & (cop > 0)).astype(float).where(
        k.notna() & pmo.notna() & cop.notna(), np.nan)
    return (ind.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f55_lmps_146_composite_rolling_topping_signal_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with (PMO < signal) AND (KST < signal) AND (TRIX < signal)."""
    pmo, sig1 = _pring_pmo(close)
    k = _kst(close); sig2 = _kst_signal(close)
    tr, sig3 = _trix_with_signal(close, 15, 9)
    ind = ((pmo < sig1) & (k < sig2) & (tr < sig3)).astype(float).where(
        pmo.notna() & k.notna() & tr.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f55_lmps_147_coppock_negative_with_special_k_negative_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: Coppock < 0 AND Special K < 0 - cycle deeply bearish."""
    cop = _coppock_annual(close)
    sk = _pring_special_k(close)
    return (((cop < 0) & (sk < 0)).astype(float).where(cop.notna() & sk.notna(), np.nan)).diff().diff()

def f55_lmps_148_all_4_smoothed_oscillators_falling_at_high_indicator_d2(close: pd.Series) -> pd.Series:
    """Indicator: KST,PMO,Coppock,TRIX all decreasing AND close = 252d max."""
    k = _kst(close); pmo, _ = _pring_pmo(close); cop = _coppock_annual(close)
    tr, _ = _trix_with_signal(close, 15, 9)
    fall = ((k < k.shift(MDAYS)) & (pmo < pmo.shift(MDAYS)) & (cop < cop.shift(MDAYS)) & (tr < tr.shift(MDAYS))).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((fall * (close >= rmax - 1e-12).astype(float)).where(
    k.notna() & pmo.notna() & cop.notna() & tr.notna(), np.nan)).diff().diff()

def f55_lmps_149_long_term_momentum_divergence_intensity_score_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of z-scored: (z(close) - z(KST)), (z(close) - z(Coppock)), (z(close) - z(PMO)) over 252d."""
    k = _kst(close); pmo, _ = _pring_pmo(close); cop = _coppock_annual(close)
    zc = _rolling_zscore(_safe_log(close), YDAYS)
    g1 = zc - _rolling_zscore(k, YDAYS); g2 = zc - _rolling_zscore(cop, YDAYS); g3 = zc - _rolling_zscore(pmo, YDAYS)
    return (g1.fillna(0.0) + g2.fillna(0.0) + g3.fillna(0.0)).diff().diff()

def f55_lmps_150_blowoff_momentum_imminence_composite_score_252d_d2(close: pd.Series) -> pd.Series:
    """Composite: high Mayer + falling avg-osc + close-z>1 + Coppock-cycle-position high."""
    mm = _safe_div(close, _sma(close, 200))
    k = _kst(close); pmo, _ = _pring_pmo(close); cop = _coppock_annual(close)
    tr, _ = _trix_with_signal(close, 15, 9); ppo, _ = _ppo_with_signal(close)
    zs = (_rolling_zscore(k, YDAYS) + _rolling_zscore(pmo, YDAYS) + _rolling_zscore(cop, YDAYS)
          + _rolling_zscore(tr, YDAYS) + _rolling_zscore(ppo, YDAYS)) / 5.0
    falling = (zs < zs.shift(MDAYS)).astype(float)
    zc = _rolling_zscore(_safe_log(close), YDAYS)
    mx = cop.rolling(DDAYS_2Y, min_periods=YDAYS).max(); mn = cop.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    pos = _safe_div(cop - mn, mx - mn)
    return (mm * falling * (zc > 1.0).astype(float) * pos).diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d2)
# ============================================================

LONG_MOMENTUM_SMOOTHED_PMO_D2_REGISTRY_076_150 = {
    "f55_lmps_076_kst_at_252d_max_indicator_d2": {"inputs": ["close"], "func": f55_lmps_076_kst_at_252d_max_indicator_d2},
    "f55_lmps_077_kst_signal_cross_at_overbought_indicator_d2": {"inputs": ["close"], "func": f55_lmps_077_kst_signal_cross_at_overbought_indicator_d2},
    "f55_lmps_078_kst_signal_cross_at_252d_high_indicator_d2": {"inputs": ["close"], "func": f55_lmps_078_kst_signal_cross_at_252d_high_indicator_d2},
    "f55_lmps_079_kst_negative_at_252d_high_indicator_d2": {"inputs": ["close"], "func": f55_lmps_079_kst_negative_at_252d_high_indicator_d2},
    "f55_lmps_080_kst_cross_velocity_252d_d2": {"inputs": ["close"], "func": f55_lmps_080_kst_cross_velocity_252d_d2},
    "f55_lmps_081_momentum_stack_alignment_bullish_indicator_d2": {"inputs": ["close"], "func": f55_lmps_081_momentum_stack_alignment_bullish_indicator_d2},
    "f55_lmps_082_momentum_stack_alignment_bearish_indicator_d2": {"inputs": ["close"], "func": f55_lmps_082_momentum_stack_alignment_bearish_indicator_d2},
    "f55_lmps_083_momentum_stack_breadth_above_zero_count_d2": {"inputs": ["close"], "func": f55_lmps_083_momentum_stack_breadth_above_zero_count_d2},
    "f55_lmps_084_momentum_stack_breadth_below_zero_count_d2": {"inputs": ["close"], "func": f55_lmps_084_momentum_stack_breadth_below_zero_count_d2},
    "f55_lmps_085_momentum_stack_consensus_zscore_252d_d2": {"inputs": ["close"], "func": f55_lmps_085_momentum_stack_consensus_zscore_252d_d2},
    "f55_lmps_086_momentum_stack_disagreement_max_minus_min_252d_d2": {"inputs": ["close"], "func": f55_lmps_086_momentum_stack_disagreement_max_minus_min_252d_d2},
    "f55_lmps_087_momentum_stack_alignment_bull_persistence_252d_d2": {"inputs": ["close"], "func": f55_lmps_087_momentum_stack_alignment_bull_persistence_252d_d2},
    "f55_lmps_088_momentum_stack_alignment_bear_persistence_252d_d2": {"inputs": ["close"], "func": f55_lmps_088_momentum_stack_alignment_bear_persistence_252d_d2},
    "f55_lmps_089_momentum_stack_acceleration_composite_252d_d2": {"inputs": ["close"], "func": f55_lmps_089_momentum_stack_acceleration_composite_252d_d2},
    "f55_lmps_090_momentum_stack_regime_change_indicator_252d_d2": {"inputs": ["close"], "func": f55_lmps_090_momentum_stack_regime_change_indicator_252d_d2},
    "f55_lmps_091_coppock_peak_value_504d_d2": {"inputs": ["close"], "func": f55_lmps_091_coppock_peak_value_504d_d2},
    "f55_lmps_092_coppock_trough_value_504d_d2": {"inputs": ["close"], "func": f55_lmps_092_coppock_trough_value_504d_d2},
    "f55_lmps_093_coppock_days_since_504d_peak_d2": {"inputs": ["close"], "func": f55_lmps_093_coppock_days_since_504d_peak_d2},
    "f55_lmps_094_coppock_days_since_504d_trough_d2": {"inputs": ["close"], "func": f55_lmps_094_coppock_days_since_504d_trough_d2},
    "f55_lmps_095_coppock_peak_to_current_decay_pct_d2": {"inputs": ["close"], "func": f55_lmps_095_coppock_peak_to_current_decay_pct_d2},
    "f55_lmps_096_coppock_cycle_amplitude_504d_d2": {"inputs": ["close"], "func": f55_lmps_096_coppock_cycle_amplitude_504d_d2},
    "f55_lmps_097_coppock_cycle_position_pct_504d_d2": {"inputs": ["close"], "func": f55_lmps_097_coppock_cycle_position_pct_504d_d2},
    "f55_lmps_098_coppock_peaks_count_504d_d2": {"inputs": ["close"], "func": f55_lmps_098_coppock_peaks_count_504d_d2},
    "f55_lmps_099_coppock_current_minus_peak_zscore_504d_d2": {"inputs": ["close"], "func": f55_lmps_099_coppock_current_minus_peak_zscore_504d_d2},
    "f55_lmps_100_coppock_post_peak_decline_persistence_63d_d2": {"inputs": ["close"], "func": f55_lmps_100_coppock_post_peak_decline_persistence_63d_d2},
    "f55_lmps_101_coppock_pct_rank_504d_d2": {"inputs": ["close"], "func": f55_lmps_101_coppock_pct_rank_504d_d2},
    "f55_lmps_102_coppock_pct_rank_1260d_d2": {"inputs": ["close"], "func": f55_lmps_102_coppock_pct_rank_1260d_d2},
    "f55_lmps_103_kst_pct_rank_504d_d2": {"inputs": ["close"], "func": f55_lmps_103_kst_pct_rank_504d_d2},
    "f55_lmps_104_pmo_pct_rank_504d_d2": {"inputs": ["close"], "func": f55_lmps_104_pmo_pct_rank_504d_d2},
    "f55_lmps_105_pmo_pct_rank_1260d_d2": {"inputs": ["close"], "func": f55_lmps_105_pmo_pct_rank_1260d_d2},
    "f55_lmps_106_special_k_pct_rank_504d_d2": {"inputs": ["close"], "func": f55_lmps_106_special_k_pct_rank_504d_d2},
    "f55_lmps_107_trix_pct_rank_504d_d2": {"inputs": ["close"], "func": f55_lmps_107_trix_pct_rank_504d_d2},
    "f55_lmps_108_ppo_pct_rank_504d_d2": {"inputs": ["close"], "func": f55_lmps_108_ppo_pct_rank_504d_d2},
    "f55_lmps_109_dpo_63d_pct_rank_504d_d2": {"inputs": ["close"], "func": f55_lmps_109_dpo_63d_pct_rank_504d_d2},
    "f55_lmps_110_multi_momentum_avg_rank_504d_d2": {"inputs": ["close"], "func": f55_lmps_110_multi_momentum_avg_rank_504d_d2},
    "f55_lmps_111_roc_composite_pring_weighted_value_d2": {"inputs": ["close"], "func": f55_lmps_111_roc_composite_pring_weighted_value_d2},
    "f55_lmps_112_roc_composite_pring_smoothed_9d_d2": {"inputs": ["close"], "func": f55_lmps_112_roc_composite_pring_smoothed_9d_d2},
    "f55_lmps_113_roc_short_med_long_composite_z_252d_d2": {"inputs": ["close"], "func": f55_lmps_113_roc_short_med_long_composite_z_252d_d2},
    "f55_lmps_114_roc_short_med_long_all_positive_indicator_d2": {"inputs": ["close"], "func": f55_lmps_114_roc_short_med_long_all_positive_indicator_d2},
    "f55_lmps_115_roc_short_med_long_all_negative_indicator_d2": {"inputs": ["close"], "func": f55_lmps_115_roc_short_med_long_all_negative_indicator_d2},
    "f55_lmps_116_roc_consensus_z_252d_composite_d2": {"inputs": ["close"], "func": f55_lmps_116_roc_consensus_z_252d_composite_d2},
    "f55_lmps_117_roc_cross_horizon_disagreement_max_minus_min_252d_d2": {"inputs": ["close"], "func": f55_lmps_117_roc_cross_horizon_disagreement_max_minus_min_252d_d2},
    "f55_lmps_118_roc_acceleration_composite_252d_d2": {"inputs": ["close"], "func": f55_lmps_118_roc_acceleration_composite_252d_d2},
    "f55_lmps_119_roc_velocity_composite_252d_d2": {"inputs": ["close"], "func": f55_lmps_119_roc_velocity_composite_252d_d2},
    "f55_lmps_120_roc_long_horizon_decay_rate_252d_d2": {"inputs": ["close"], "func": f55_lmps_120_roc_long_horizon_decay_rate_252d_d2},
    "f55_lmps_121_smoothed_252d_momentum_sign_changes_count_d2": {"inputs": ["close"], "func": f55_lmps_121_smoothed_252d_momentum_sign_changes_count_d2},
    "f55_lmps_122_smoothed_504d_momentum_sign_changes_count_d2": {"inputs": ["close"], "func": f55_lmps_122_smoothed_504d_momentum_sign_changes_count_d2},
    "f55_lmps_123_coppock_sign_change_at_252d_high_indicator_d2": {"inputs": ["close"], "func": f55_lmps_123_coppock_sign_change_at_252d_high_indicator_d2},
    "f55_lmps_124_kst_sign_change_at_252d_high_indicator_d2": {"inputs": ["close"], "func": f55_lmps_124_kst_sign_change_at_252d_high_indicator_d2},
    "f55_lmps_125_pmo_sign_change_at_252d_high_indicator_d2": {"inputs": ["close"], "func": f55_lmps_125_pmo_sign_change_at_252d_high_indicator_d2},
    "f55_lmps_126_all_three_oscillators_sign_change_simultaneous_252d_d2": {"inputs": ["close"], "func": f55_lmps_126_all_three_oscillators_sign_change_simultaneous_252d_d2},
    "f55_lmps_127_major_momentum_regime_shift_indicator_252d_d2": {"inputs": ["close"], "func": f55_lmps_127_major_momentum_regime_shift_indicator_252d_d2},
    "f55_lmps_128_long_term_momentum_failure_indicator_252d_d2": {"inputs": ["close"], "func": f55_lmps_128_long_term_momentum_failure_indicator_252d_d2},
    "f55_lmps_129_cycle_completion_indicator_double_top_coppock_504d_d2": {"inputs": ["close"], "func": f55_lmps_129_cycle_completion_indicator_double_top_coppock_504d_d2},
    "f55_lmps_130_cycle_completion_indicator_double_bottom_coppock_504d_d2": {"inputs": ["close"], "func": f55_lmps_130_cycle_completion_indicator_double_bottom_coppock_504d_d2},
    "f55_lmps_131_coppock_acceleration_252d_d2": {"inputs": ["close"], "func": f55_lmps_131_coppock_acceleration_252d_d2},
    "f55_lmps_132_coppock_jerk_252d_d2": {"inputs": ["close"], "func": f55_lmps_132_coppock_jerk_252d_d2},
    "f55_lmps_133_pmo_acceleration_252d_d2": {"inputs": ["close"], "func": f55_lmps_133_pmo_acceleration_252d_d2},
    "f55_lmps_134_kst_acceleration_252d_d2": {"inputs": ["close"], "func": f55_lmps_134_kst_acceleration_252d_d2},
    "f55_lmps_135_trix_acceleration_252d_d2": {"inputs": ["close"], "func": f55_lmps_135_trix_acceleration_252d_d2},
    "f55_lmps_136_special_k_acceleration_252d_d2": {"inputs": ["close"], "func": f55_lmps_136_special_k_acceleration_252d_d2},
    "f55_lmps_137_momentum_acceleration_decline_at_high_indicator_d2": {"inputs": ["close"], "func": f55_lmps_137_momentum_acceleration_decline_at_high_indicator_d2},
    "f55_lmps_138_momentum_deceleration_persistence_63d_d2": {"inputs": ["close"], "func": f55_lmps_138_momentum_deceleration_persistence_63d_d2},
    "f55_lmps_139_momentum_d2_negative_with_d1_positive_count_252d_d2": {"inputs": ["close"], "func": f55_lmps_139_momentum_d2_negative_with_d1_positive_count_252d_d2},
    "f55_lmps_140_momentum_curvature_change_event_252d_d2": {"inputs": ["close"], "func": f55_lmps_140_momentum_curvature_change_event_252d_d2},
    "f55_lmps_141_master_long_term_momentum_score_252d_d2": {"inputs": ["close"], "func": f55_lmps_141_master_long_term_momentum_score_252d_d2},
    "f55_lmps_142_blowoff_smoothed_momentum_signature_252d_d2": {"inputs": ["close"], "func": f55_lmps_142_blowoff_smoothed_momentum_signature_252d_d2},
    "f55_lmps_143_coppock_kst_pmo_alignment_composite_252d_d2": {"inputs": ["close"], "func": f55_lmps_143_coppock_kst_pmo_alignment_composite_252d_d2},
    "f55_lmps_144_multi_oscillator_overbought_breadth_count_252d_d2": {"inputs": ["close"], "func": f55_lmps_144_multi_oscillator_overbought_breadth_count_252d_d2},
    "f55_lmps_145_composite_smoothed_momentum_peak_persistence_252d_d2": {"inputs": ["close"], "func": f55_lmps_145_composite_smoothed_momentum_peak_persistence_252d_d2},
    "f55_lmps_146_composite_rolling_topping_signal_252d_d2": {"inputs": ["close"], "func": f55_lmps_146_composite_rolling_topping_signal_252d_d2},
    "f55_lmps_147_coppock_negative_with_special_k_negative_indicator_d2": {"inputs": ["close"], "func": f55_lmps_147_coppock_negative_with_special_k_negative_indicator_d2},
    "f55_lmps_148_all_4_smoothed_oscillators_falling_at_high_indicator_d2": {"inputs": ["close"], "func": f55_lmps_148_all_4_smoothed_oscillators_falling_at_high_indicator_d2},
    "f55_lmps_149_long_term_momentum_divergence_intensity_score_252d_d2": {"inputs": ["close"], "func": f55_lmps_149_long_term_momentum_divergence_intensity_score_252d_d2},
    "f55_lmps_150_blowoff_momentum_imminence_composite_score_252d_d2": {"inputs": ["close"], "func": f55_lmps_150_blowoff_momentum_imminence_composite_score_252d_d2},
}
