"""33_coppock_curve_kst d3 features 376-450 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
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

def _hma(s, n):
    half = max(int(n / 2), 1)
    sqn = max(int(np.sqrt(n)), 1)
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)

def _tema(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3

def _dema(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    return 2.0 * e1 - e2

def _roc_pct(s, n):
    return s.pct_change(n) * 100.0

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
    return 1.0 * _sma(_roc_pct(close, 10), 10) + 2.0 * _sma(_roc_pct(close, 15), 10) + 3.0 * _sma(_roc_pct(close, 20), 10) + 4.0 * _sma(_roc_pct(close, 30), 15)

def _kst_short_term(close):
    return 1.0 * _sma(_roc_pct(close, 5), 5) + 2.0 * _sma(_roc_pct(close, 8), 5) + 3.0 * _sma(_roc_pct(close, 12), 5) + 4.0 * _sma(_roc_pct(close, 18), 8)

def _kst_long_term(close):
    return 1.0 * _sma(_roc_pct(close, 65), 21) + 2.0 * _sma(_roc_pct(close, 130), 21) + 3.0 * _sma(_roc_pct(close, 195), 21) + 4.0 * _sma(_roc_pct(close, 260), 42)

def _special_k(close):
    return 1.0 * _sma(_roc_pct(close, 10), 10) + 2.0 * _sma(_roc_pct(close, 15), 10) + 3.0 * _sma(_roc_pct(close, 20), 10) + 4.0 * _sma(_roc_pct(close, 30), 15) + 1.0 * _sma(_roc_pct(close, 50), 50) + 2.0 * _sma(_roc_pct(close, 65), 65) + 3.0 * _sma(_roc_pct(close, 100), 100) + 4.0 * _sma(_roc_pct(close, 195), 130)

def _vwma(close, volume, n):
    pv = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    v = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(pv, v)

def _vwma_coppock_cycle(close, volume, n_long, n_short, n_wma, n_vwma=QDAYS):
    smoothed = _vwma(close, volume, n_vwma)
    return _coppock(smoothed, n_long, n_short, n_wma)

def _dti(close, r=14, s=10, u=5):
    mom = np.sign(close - close.shift(r)) * _safe_log(close).diff().abs()
    e1 = _ema(mom, r)
    e2 = _ema(e1, s)
    e3 = _ema(e2, u)
    abs_e1 = _ema(mom.abs(), r)
    abs_e2 = _ema(abs_e1, s)
    abs_e3 = _ema(abs_e2, u)
    return 100.0 * _safe_div(e3, abs_e3)

def f33_cpkt_376_kst_long_term_signal_line_sma21_d3(close: pd.Series) -> pd.Series:
    """SMA-21 of long-term KST (signal line for long-term KST)."""
    return _sma(_kst_long_term(close), 21).diff().diff().diff()

def f33_cpkt_377_kst_long_term_minus_signal_diff_d3(close: pd.Series) -> pd.Series:
    """Long-term KST - SMA-21 signal line."""
    return (_kst_long_term(close) - _sma(_kst_long_term(close), 21)).diff().diff().diff()

def f33_cpkt_378_kst_long_term_signal_cross_bearish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where long-term KST crosses below its 21d signal line."""
    diff = _kst_long_term(close) - _sma(_kst_long_term(close), 21)
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan).diff().diff().diff()

def f33_cpkt_379_days_since_kst_long_bearish_cross_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent bearish cross of long-term KST below its 21d signal line."""
    diff = _kst_long_term(close) - _sma(_kst_long_term(close), 21)
    flag = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    return _bars_since_true(flag).diff().diff().diff()

def f33_cpkt_380_kst_short_term_signal_line_sma5_d3(close: pd.Series) -> pd.Series:
    """SMA-5 of short-term KST (signal line)."""
    return _sma(_kst_short_term(close), 5).diff().diff().diff()

def f33_cpkt_381_kst_short_term_minus_signal_diff_d3(close: pd.Series) -> pd.Series:
    """Short-term KST - SMA-5 signal line."""
    return (_kst_short_term(close) - _sma(_kst_short_term(close), 5)).diff().diff().diff()

def f33_cpkt_382_kst_short_term_signal_cross_bearish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where short-term KST crosses below its 5d signal line."""
    diff = _kst_short_term(close) - _sma(_kst_short_term(close), 5)
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan).diff().diff().diff()

def f33_cpkt_383_days_since_kst_short_bearish_cross_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent bearish cross of short-term KST."""
    diff = _kst_short_term(close) - _sma(_kst_short_term(close), 5)
    flag = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    return _bars_since_true(flag).diff().diff().diff()

def f33_cpkt_384_kst_long_term_above_signal_persistence_63d_d3(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where long-term KST > its 21d signal line."""
    diff = _kst_long_term(close) - _sma(_kst_long_term(close), 21)
    return (diff > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f33_cpkt_385_kst_short_term_below_signal_persistence_21d_d3(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where short-term KST < its 5d signal line."""
    diff = _kst_short_term(close) - _sma(_kst_short_term(close), 5)
    return (diff < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f33_cpkt_386_coppock_quarterly_zero_cross_count_252d_d3(close: pd.Series) -> pd.Series:
    """Total zero-crossings (either direction) of quarterly Coppock in trailing 252d."""
    c = _coppock_quarterly(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f33_cpkt_387_coppock_semi_annual_zero_cross_count_252d_d3(close: pd.Series) -> pd.Series:
    """Total zero-crossings of semi-annual Coppock in trailing 252d."""
    c = _coppock_semi_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f33_cpkt_388_coppock_biennial_zero_cross_count_252d_d3(close: pd.Series) -> pd.Series:
    """Total zero-crossings of biennial Coppock in trailing 252d."""
    c = _coppock_biennial(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f33_cpkt_389_coppock_quarterly_zero_cross_count_504d_d3(close: pd.Series) -> pd.Series:
    """Zero-crossings of quarterly Coppock in trailing 504d."""
    c = _coppock_quarterly(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f33_cpkt_390_coppock_semi_annual_zero_cross_count_504d_d3(close: pd.Series) -> pd.Series:
    """Zero-crossings of semi-annual Coppock in trailing 504d."""
    c = _coppock_semi_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f33_cpkt_391_coppock_biennial_zero_cross_count_504d_d3(close: pd.Series) -> pd.Series:
    """Zero-crossings of biennial Coppock in trailing 504d."""
    c = _coppock_biennial(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f33_cpkt_392_coppock_quarterly_consecutive_positive_bars_current_d3(close: pd.Series) -> pd.Series:
    """Current consecutive-positive-bar streak length for quarterly Coppock."""
    c = _coppock_quarterly(close)
    flag = (c > 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f33_cpkt_393_coppock_semi_annual_consecutive_positive_bars_current_d3(close: pd.Series) -> pd.Series:
    """Current consecutive-positive-bar streak length for semi-annual Coppock."""
    c = _coppock_semi_annual(close)
    flag = (c > 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f33_cpkt_394_coppock_biennial_consecutive_positive_bars_current_d3(close: pd.Series) -> pd.Series:
    """Current consecutive-positive-bar streak length for biennial Coppock."""
    c = _coppock_biennial(close)
    flag = (c > 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f33_cpkt_395_coppock_quarterly_consecutive_negative_bars_current_d3(close: pd.Series) -> pd.Series:
    """Current consecutive-negative-bar streak length for quarterly Coppock."""
    c = _coppock_quarterly(close)
    flag = (c < 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f33_cpkt_396_coppock_quarterly_d2_zero_cross_bearish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where d²(quarterly Coppock) crosses + → -."""
    c = _coppock_quarterly(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan).diff().diff().diff()

def f33_cpkt_397_coppock_semi_annual_d2_zero_cross_bearish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where d²(semi-annual Coppock) crosses + → -."""
    c = _coppock_semi_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan).diff().diff().diff()

def f33_cpkt_398_coppock_biennial_d2_zero_cross_bearish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where d²(biennial Coppock) crosses + → -."""
    c = _coppock_biennial(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) > 0) & (d2 <= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan).diff().diff().diff()

def f33_cpkt_399_coppock_quarterly_d2_zero_cross_bullish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where d²(quarterly Coppock) crosses - → + (acceleration bottoming)."""
    c = _coppock_quarterly(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) < 0) & (d2 >= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan).diff().diff().diff()

def f33_cpkt_400_coppock_semi_annual_d2_zero_cross_bullish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where d²(semi-annual Coppock) crosses - → +."""
    c = _coppock_semi_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) < 0) & (d2 >= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan).diff().diff().diff()

def f33_cpkt_401_coppock_biennial_d2_zero_cross_bullish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where d²(biennial Coppock) crosses - → +."""
    c = _coppock_biennial(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    return ((d2.shift(1) < 0) & (d2 >= 0)).astype(float).where(d2.notna() & d2.shift(1).notna(), np.nan).diff().diff().diff()

def f33_cpkt_402_days_since_coppock_quarterly_d2_bearish_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent d²(quarterly Coppock) bearish crossover."""
    c = _coppock_quarterly(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return _bars_since_true(flag).diff().diff().diff()

def f33_cpkt_403_days_since_coppock_semi_annual_d2_bearish_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent d²(semi-annual Coppock) bearish crossover."""
    c = _coppock_semi_annual(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return _bars_since_true(flag).diff().diff().diff()

def f33_cpkt_404_days_since_coppock_biennial_d2_bearish_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent d²(biennial Coppock) bearish crossover."""
    c = _coppock_biennial(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return _bars_since_true(flag).diff().diff().diff()

def f33_cpkt_405_coppock_quarterly_d2_zero_cross_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of d²(quarterly Coppock) bearish crossovers in trailing 252d."""
    c = _coppock_quarterly(close)
    d2 = _rolling_slope(_rolling_slope(c, MDAYS), MDAYS)
    flag = ((d2.shift(1) > 0) & (d2 <= 0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f33_cpkt_406_coppock_quarterly_cycle_amplitude_252d_d3(close: pd.Series) -> pd.Series:
    """Trailing 252d range (max - min) of quarterly Coppock."""
    c = _coppock_quarterly(close)
    return (c.rolling(YDAYS, min_periods=QDAYS).max() - c.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff().diff()

def f33_cpkt_407_coppock_semi_annual_cycle_amplitude_252d_d3(close: pd.Series) -> pd.Series:
    """Trailing 252d range of semi-annual Coppock."""
    c = _coppock_semi_annual(close)
    return (c.rolling(YDAYS, min_periods=QDAYS).max() - c.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff().diff()

def f33_cpkt_408_coppock_biennial_cycle_amplitude_252d_d3(close: pd.Series) -> pd.Series:
    """Trailing 252d range of biennial Coppock."""
    c = _coppock_biennial(close)
    return (c.rolling(YDAYS, min_periods=QDAYS).max() - c.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff().diff()

def f33_cpkt_409_coppock_quarterly_cycle_amplitude_504d_d3(close: pd.Series) -> pd.Series:
    """Trailing 504d range of quarterly Coppock."""
    c = _coppock_quarterly(close)
    return (c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()).diff().diff().diff()

def f33_cpkt_410_coppock_semi_annual_cycle_amplitude_504d_d3(close: pd.Series) -> pd.Series:
    """Trailing 504d range of semi-annual Coppock."""
    c = _coppock_semi_annual(close)
    return (c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()).diff().diff().diff()

def f33_cpkt_411_coppock_biennial_cycle_amplitude_504d_d3(close: pd.Series) -> pd.Series:
    """Trailing 504d range of biennial Coppock."""
    c = _coppock_biennial(close)
    return (c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()).diff().diff().diff()

def f33_cpkt_412_coppock_quarterly_amplitude_decay_ratio_d3(close: pd.Series) -> pd.Series:
    """252d amplitude / 504d amplitude for quarterly Coppock — <1 means cycle compressing."""
    c = _coppock_quarterly(close)
    a252 = c.rolling(YDAYS, min_periods=QDAYS).max() - c.rolling(YDAYS, min_periods=QDAYS).min()
    a504 = c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(a252, a504).diff().diff().diff()

def f33_cpkt_413_coppock_semi_annual_amplitude_decay_ratio_d3(close: pd.Series) -> pd.Series:
    """252d/504d amplitude ratio for semi-annual Coppock."""
    c = _coppock_semi_annual(close)
    a252 = c.rolling(YDAYS, min_periods=QDAYS).max() - c.rolling(YDAYS, min_periods=QDAYS).min()
    a504 = c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(a252, a504).diff().diff().diff()

def f33_cpkt_414_coppock_biennial_amplitude_decay_ratio_d3(close: pd.Series) -> pd.Series:
    """252d/504d amplitude ratio for biennial Coppock."""
    c = _coppock_biennial(close)
    a252 = c.rolling(YDAYS, min_periods=QDAYS).max() - c.rolling(YDAYS, min_periods=QDAYS).min()
    a504 = c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(a252, a504).diff().diff().diff()

def f33_cpkt_415_coppock_quarterly_value_relative_to_amplitude_d3(close: pd.Series) -> pd.Series:
    """Current quarterly Coppock / (504d amplitude / 2) — normalized position within cycle range."""
    c = _coppock_quarterly(close)
    amp = (c.rolling(DDAYS_2Y, min_periods=YDAYS).max() - c.rolling(DDAYS_2Y, min_periods=YDAYS).min()) / 2.0
    return _safe_div(c, amp).diff().diff().diff()

def f33_cpkt_416_tema_long_momentum_21d_value_d3(close: pd.Series) -> pd.Series:
    """TEMA(21) of ROC(21) — monthly TEMA-smoothed momentum."""
    return _tema(_roc_pct(close, MDAYS), MDAYS).diff().diff().diff()

def f33_cpkt_417_tema_long_momentum_126d_value_d3(close: pd.Series) -> pd.Series:
    """TEMA(126) of ROC(126) — semi-annual TEMA-smoothed momentum."""
    return _tema(_roc_pct(close, 126), 126).diff().diff().diff()

def f33_cpkt_418_tema_long_momentum_252d_value_d3(close: pd.Series) -> pd.Series:
    """TEMA(252) of ROC(252) — annual TEMA-smoothed momentum."""
    return _tema(_roc_pct(close, YDAYS), YDAYS).diff().diff().diff()

def f33_cpkt_419_dema_long_momentum_21d_value_d3(close: pd.Series) -> pd.Series:
    """DEMA(21) of ROC(21) — monthly DEMA-smoothed momentum."""
    return _dema(_roc_pct(close, MDAYS), MDAYS).diff().diff().diff()

def f33_cpkt_420_dema_long_momentum_126d_value_d3(close: pd.Series) -> pd.Series:
    """DEMA(126) of ROC(126)."""
    return _dema(_roc_pct(close, 126), 126).diff().diff().diff()

def f33_cpkt_421_dema_long_momentum_252d_value_d3(close: pd.Series) -> pd.Series:
    """DEMA(252) of ROC(252)."""
    return _dema(_roc_pct(close, YDAYS), YDAYS).diff().diff().diff()

def f33_cpkt_422_hma_long_momentum_21d_value_d3(close: pd.Series) -> pd.Series:
    """Hull(21) of ROC(21) — monthly Hull-smoothed momentum."""
    return _hma(_roc_pct(close, MDAYS), MDAYS).diff().diff().diff()

def f33_cpkt_423_hma_long_momentum_126d_value_d3(close: pd.Series) -> pd.Series:
    """Hull(126) of ROC(126)."""
    return _hma(_roc_pct(close, 126), 126).diff().diff().diff()

def f33_cpkt_424_hma_long_momentum_252d_value_d3(close: pd.Series) -> pd.Series:
    """Hull(252) of ROC(252)."""
    return _hma(_roc_pct(close, YDAYS), YDAYS).diff().diff().diff()

def f33_cpkt_425_tema_long_momentum_252d_slope_63d_d3(close: pd.Series) -> pd.Series:
    """63d slope of TEMA-long-momentum(252)."""
    return _rolling_slope(_tema(_roc_pct(close, YDAYS), YDAYS), QDAYS).diff().diff().diff()

def f33_cpkt_426_dema_long_momentum_252d_slope_63d_d3(close: pd.Series) -> pd.Series:
    """63d slope of DEMA-long-momentum(252)."""
    return _rolling_slope(_dema(_roc_pct(close, YDAYS), YDAYS), QDAYS).diff().diff().diff()

def f33_cpkt_427_hma_long_momentum_252d_slope_63d_d3(close: pd.Series) -> pd.Series:
    """63d slope of Hull-long-momentum(252)."""
    return _rolling_slope(_hma(_roc_pct(close, YDAYS), YDAYS), QDAYS).diff().diff().diff()

def f33_cpkt_428_tema_long_momentum_252d_above_zero_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when TEMA-long-momentum(252) > 0."""
    t = _tema(_roc_pct(close, YDAYS), YDAYS)
    return (t > 0).astype(float).where(t.notna(), np.nan).diff().diff().diff()

def f33_cpkt_429_dema_long_momentum_252d_above_zero_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when DEMA-long-momentum(252) > 0."""
    d = _dema(_roc_pct(close, YDAYS), YDAYS)
    return (d > 0).astype(float).where(d.notna(), np.nan).diff().diff().diff()

def f33_cpkt_430_hma_long_momentum_252d_above_zero_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when Hull-long-momentum(252) > 0."""
    h = _hma(_roc_pct(close, YDAYS), YDAYS)
    return (h > 0).astype(float).where(h.notna(), np.nan).diff().diff().diff()

def f33_cpkt_431_vwma_coppock_quarterly_value_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWMA-weighted quarterly Coppock (63/42/21 on VWMA63-smoothed close)."""
    return _vwma_coppock_cycle(close, volume, QDAYS, 42, MDAYS, QDAYS).diff().diff().diff()

def f33_cpkt_432_vwma_coppock_semi_annual_value_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWMA-weighted semi-annual Coppock (126/84/42)."""
    return _vwma_coppock_cycle(close, volume, 126, 84, 42, QDAYS).diff().diff().diff()

def f33_cpkt_433_vwma_coppock_biennial_value_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWMA-weighted biennial Coppock (504/378/210)."""
    return _vwma_coppock_cycle(close, volume, DDAYS_2Y, 378, 210, QDAYS).diff().diff().diff()

def f33_cpkt_434_vwma_coppock_quarterly_slope_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of VWMA-quarterly Coppock."""
    return _rolling_slope(_vwma_coppock_cycle(close, volume, QDAYS, 42, MDAYS, QDAYS), MDAYS).diff().diff().diff()

def f33_cpkt_435_vwma_coppock_semi_annual_slope_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of VWMA-semi-annual Coppock."""
    return _rolling_slope(_vwma_coppock_cycle(close, volume, 126, 84, 42, QDAYS), QDAYS).diff().diff().diff()

def f33_cpkt_436_vwma_coppock_biennial_slope_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of VWMA-biennial Coppock."""
    return _rolling_slope(_vwma_coppock_cycle(close, volume, DDAYS_2Y, 378, 210, QDAYS), QDAYS).diff().diff().diff()

def f33_cpkt_437_vwma_coppock_quarterly_zscore_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of VWMA-quarterly Coppock over 252d."""
    return _rolling_zscore(_vwma_coppock_cycle(close, volume, QDAYS, 42, MDAYS, QDAYS), YDAYS).diff().diff().diff()

def f33_cpkt_438_vwma_coppock_semi_annual_zscore_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of VWMA-semi-annual Coppock over 252d."""
    return _rolling_zscore(_vwma_coppock_cycle(close, volume, 126, 84, 42, QDAYS), YDAYS).diff().diff().diff()

def f33_cpkt_439_vwma_coppock_biennial_zscore_504d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of VWMA-biennial Coppock over 504d."""
    return _rolling_zscore(_vwma_coppock_cycle(close, volume, DDAYS_2Y, 378, 210, QDAYS), DDAYS_2Y).diff().diff().diff()

def f33_cpkt_440_vwma_coppock_vs_std_coppock_quarterly_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWMA-quarterly-Coppock minus standard quarterly Coppock (volume-weighting effect)."""
    return (_vwma_coppock_cycle(close, volume, QDAYS, 42, MDAYS, QDAYS) - _coppock_quarterly(close)).diff().diff().diff()

def f33_cpkt_441_dti_short_value_d3(close: pd.Series) -> pd.Series:
    """DTI short variant (r=7, s=5, u=3)."""
    return _dti(close, 7, 5, 3).diff().diff().diff()

def f33_cpkt_442_dti_long_value_d3(close: pd.Series) -> pd.Series:
    """DTI long variant (r=21, s=14, u=7)."""
    return _dti(close, 21, 14, 7).diff().diff().diff()

def f33_cpkt_443_dti_short_slope_21d_d3(close: pd.Series) -> pd.Series:
    """21d slope of DTI short."""
    return _rolling_slope(_dti(close, 7, 5, 3), MDAYS).diff().diff().diff()

def f33_cpkt_444_dti_long_slope_63d_d3(close: pd.Series) -> pd.Series:
    """63d slope of DTI long."""
    return _rolling_slope(_dti(close, 21, 14, 7), QDAYS).diff().diff().diff()

def f33_cpkt_445_dti_short_above_zero_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when DTI short > 0."""
    d = _dti(close, 7, 5, 3)
    return (d > 0).astype(float).where(d.notna(), np.nan).diff().diff().diff()

def f33_cpkt_446_special_k_signal_line_sma10_d3(close: pd.Series) -> pd.Series:
    """SMA-10 of Special K (signal line)."""
    return _sma(_special_k(close), 10).diff().diff().diff()

def f33_cpkt_447_special_k_above_signal_indicator_d3(close: pd.Series) -> pd.Series:
    """+1 when Special K > SMA-10 signal line."""
    sk = _special_k(close)
    return (sk > _sma(sk, 10)).astype(float).where(sk.notna(), np.nan).diff().diff().diff()

def f33_cpkt_448_special_k_slope_21d_d3(close: pd.Series) -> pd.Series:
    """21d slope of Special K."""
    return _rolling_slope(_special_k(close), MDAYS).diff().diff().diff()

def f33_cpkt_449_special_k_d2_21d_d3(close: pd.Series) -> pd.Series:
    """d²(Special K) at 21d horizon — acceleration."""
    return _rolling_slope(_rolling_slope(_special_k(close), MDAYS), MDAYS).diff().diff().diff()

def f33_cpkt_450_special_k_zero_cross_bearish_event_d3(close: pd.Series) -> pd.Series:
    """+1 on bar where Special K crosses + → 0 (bearish zero-cross)."""
    sk = _special_k(close)
    return ((sk.shift(1) > 0) & (sk <= 0)).astype(float).where(sk.notna() & sk.shift(1).notna(), np.nan).diff().diff().diff()
COPPOCK_CURVE_KST_D3_REGISTRY_376_450 = {'f33_cpkt_376_kst_long_term_signal_line_sma21_d3': {'inputs': ['close'], 'func': f33_cpkt_376_kst_long_term_signal_line_sma21_d3}, 'f33_cpkt_377_kst_long_term_minus_signal_diff_d3': {'inputs': ['close'], 'func': f33_cpkt_377_kst_long_term_minus_signal_diff_d3}, 'f33_cpkt_378_kst_long_term_signal_cross_bearish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_378_kst_long_term_signal_cross_bearish_event_d3}, 'f33_cpkt_379_days_since_kst_long_bearish_cross_d3': {'inputs': ['close'], 'func': f33_cpkt_379_days_since_kst_long_bearish_cross_d3}, 'f33_cpkt_380_kst_short_term_signal_line_sma5_d3': {'inputs': ['close'], 'func': f33_cpkt_380_kst_short_term_signal_line_sma5_d3}, 'f33_cpkt_381_kst_short_term_minus_signal_diff_d3': {'inputs': ['close'], 'func': f33_cpkt_381_kst_short_term_minus_signal_diff_d3}, 'f33_cpkt_382_kst_short_term_signal_cross_bearish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_382_kst_short_term_signal_cross_bearish_event_d3}, 'f33_cpkt_383_days_since_kst_short_bearish_cross_d3': {'inputs': ['close'], 'func': f33_cpkt_383_days_since_kst_short_bearish_cross_d3}, 'f33_cpkt_384_kst_long_term_above_signal_persistence_63d_d3': {'inputs': ['close'], 'func': f33_cpkt_384_kst_long_term_above_signal_persistence_63d_d3}, 'f33_cpkt_385_kst_short_term_below_signal_persistence_21d_d3': {'inputs': ['close'], 'func': f33_cpkt_385_kst_short_term_below_signal_persistence_21d_d3}, 'f33_cpkt_386_coppock_quarterly_zero_cross_count_252d_d3': {'inputs': ['close'], 'func': f33_cpkt_386_coppock_quarterly_zero_cross_count_252d_d3}, 'f33_cpkt_387_coppock_semi_annual_zero_cross_count_252d_d3': {'inputs': ['close'], 'func': f33_cpkt_387_coppock_semi_annual_zero_cross_count_252d_d3}, 'f33_cpkt_388_coppock_biennial_zero_cross_count_252d_d3': {'inputs': ['close'], 'func': f33_cpkt_388_coppock_biennial_zero_cross_count_252d_d3}, 'f33_cpkt_389_coppock_quarterly_zero_cross_count_504d_d3': {'inputs': ['close'], 'func': f33_cpkt_389_coppock_quarterly_zero_cross_count_504d_d3}, 'f33_cpkt_390_coppock_semi_annual_zero_cross_count_504d_d3': {'inputs': ['close'], 'func': f33_cpkt_390_coppock_semi_annual_zero_cross_count_504d_d3}, 'f33_cpkt_391_coppock_biennial_zero_cross_count_504d_d3': {'inputs': ['close'], 'func': f33_cpkt_391_coppock_biennial_zero_cross_count_504d_d3}, 'f33_cpkt_392_coppock_quarterly_consecutive_positive_bars_current_d3': {'inputs': ['close'], 'func': f33_cpkt_392_coppock_quarterly_consecutive_positive_bars_current_d3}, 'f33_cpkt_393_coppock_semi_annual_consecutive_positive_bars_current_d3': {'inputs': ['close'], 'func': f33_cpkt_393_coppock_semi_annual_consecutive_positive_bars_current_d3}, 'f33_cpkt_394_coppock_biennial_consecutive_positive_bars_current_d3': {'inputs': ['close'], 'func': f33_cpkt_394_coppock_biennial_consecutive_positive_bars_current_d3}, 'f33_cpkt_395_coppock_quarterly_consecutive_negative_bars_current_d3': {'inputs': ['close'], 'func': f33_cpkt_395_coppock_quarterly_consecutive_negative_bars_current_d3}, 'f33_cpkt_396_coppock_quarterly_d2_zero_cross_bearish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_396_coppock_quarterly_d2_zero_cross_bearish_event_d3}, 'f33_cpkt_397_coppock_semi_annual_d2_zero_cross_bearish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_397_coppock_semi_annual_d2_zero_cross_bearish_event_d3}, 'f33_cpkt_398_coppock_biennial_d2_zero_cross_bearish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_398_coppock_biennial_d2_zero_cross_bearish_event_d3}, 'f33_cpkt_399_coppock_quarterly_d2_zero_cross_bullish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_399_coppock_quarterly_d2_zero_cross_bullish_event_d3}, 'f33_cpkt_400_coppock_semi_annual_d2_zero_cross_bullish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_400_coppock_semi_annual_d2_zero_cross_bullish_event_d3}, 'f33_cpkt_401_coppock_biennial_d2_zero_cross_bullish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_401_coppock_biennial_d2_zero_cross_bullish_event_d3}, 'f33_cpkt_402_days_since_coppock_quarterly_d2_bearish_d3': {'inputs': ['close'], 'func': f33_cpkt_402_days_since_coppock_quarterly_d2_bearish_d3}, 'f33_cpkt_403_days_since_coppock_semi_annual_d2_bearish_d3': {'inputs': ['close'], 'func': f33_cpkt_403_days_since_coppock_semi_annual_d2_bearish_d3}, 'f33_cpkt_404_days_since_coppock_biennial_d2_bearish_d3': {'inputs': ['close'], 'func': f33_cpkt_404_days_since_coppock_biennial_d2_bearish_d3}, 'f33_cpkt_405_coppock_quarterly_d2_zero_cross_count_252d_d3': {'inputs': ['close'], 'func': f33_cpkt_405_coppock_quarterly_d2_zero_cross_count_252d_d3}, 'f33_cpkt_406_coppock_quarterly_cycle_amplitude_252d_d3': {'inputs': ['close'], 'func': f33_cpkt_406_coppock_quarterly_cycle_amplitude_252d_d3}, 'f33_cpkt_407_coppock_semi_annual_cycle_amplitude_252d_d3': {'inputs': ['close'], 'func': f33_cpkt_407_coppock_semi_annual_cycle_amplitude_252d_d3}, 'f33_cpkt_408_coppock_biennial_cycle_amplitude_252d_d3': {'inputs': ['close'], 'func': f33_cpkt_408_coppock_biennial_cycle_amplitude_252d_d3}, 'f33_cpkt_409_coppock_quarterly_cycle_amplitude_504d_d3': {'inputs': ['close'], 'func': f33_cpkt_409_coppock_quarterly_cycle_amplitude_504d_d3}, 'f33_cpkt_410_coppock_semi_annual_cycle_amplitude_504d_d3': {'inputs': ['close'], 'func': f33_cpkt_410_coppock_semi_annual_cycle_amplitude_504d_d3}, 'f33_cpkt_411_coppock_biennial_cycle_amplitude_504d_d3': {'inputs': ['close'], 'func': f33_cpkt_411_coppock_biennial_cycle_amplitude_504d_d3}, 'f33_cpkt_412_coppock_quarterly_amplitude_decay_ratio_d3': {'inputs': ['close'], 'func': f33_cpkt_412_coppock_quarterly_amplitude_decay_ratio_d3}, 'f33_cpkt_413_coppock_semi_annual_amplitude_decay_ratio_d3': {'inputs': ['close'], 'func': f33_cpkt_413_coppock_semi_annual_amplitude_decay_ratio_d3}, 'f33_cpkt_414_coppock_biennial_amplitude_decay_ratio_d3': {'inputs': ['close'], 'func': f33_cpkt_414_coppock_biennial_amplitude_decay_ratio_d3}, 'f33_cpkt_415_coppock_quarterly_value_relative_to_amplitude_d3': {'inputs': ['close'], 'func': f33_cpkt_415_coppock_quarterly_value_relative_to_amplitude_d3}, 'f33_cpkt_416_tema_long_momentum_21d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_416_tema_long_momentum_21d_value_d3}, 'f33_cpkt_417_tema_long_momentum_126d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_417_tema_long_momentum_126d_value_d3}, 'f33_cpkt_418_tema_long_momentum_252d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_418_tema_long_momentum_252d_value_d3}, 'f33_cpkt_419_dema_long_momentum_21d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_419_dema_long_momentum_21d_value_d3}, 'f33_cpkt_420_dema_long_momentum_126d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_420_dema_long_momentum_126d_value_d3}, 'f33_cpkt_421_dema_long_momentum_252d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_421_dema_long_momentum_252d_value_d3}, 'f33_cpkt_422_hma_long_momentum_21d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_422_hma_long_momentum_21d_value_d3}, 'f33_cpkt_423_hma_long_momentum_126d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_423_hma_long_momentum_126d_value_d3}, 'f33_cpkt_424_hma_long_momentum_252d_value_d3': {'inputs': ['close'], 'func': f33_cpkt_424_hma_long_momentum_252d_value_d3}, 'f33_cpkt_425_tema_long_momentum_252d_slope_63d_d3': {'inputs': ['close'], 'func': f33_cpkt_425_tema_long_momentum_252d_slope_63d_d3}, 'f33_cpkt_426_dema_long_momentum_252d_slope_63d_d3': {'inputs': ['close'], 'func': f33_cpkt_426_dema_long_momentum_252d_slope_63d_d3}, 'f33_cpkt_427_hma_long_momentum_252d_slope_63d_d3': {'inputs': ['close'], 'func': f33_cpkt_427_hma_long_momentum_252d_slope_63d_d3}, 'f33_cpkt_428_tema_long_momentum_252d_above_zero_indicator_d3': {'inputs': ['close'], 'func': f33_cpkt_428_tema_long_momentum_252d_above_zero_indicator_d3}, 'f33_cpkt_429_dema_long_momentum_252d_above_zero_indicator_d3': {'inputs': ['close'], 'func': f33_cpkt_429_dema_long_momentum_252d_above_zero_indicator_d3}, 'f33_cpkt_430_hma_long_momentum_252d_above_zero_indicator_d3': {'inputs': ['close'], 'func': f33_cpkt_430_hma_long_momentum_252d_above_zero_indicator_d3}, 'f33_cpkt_431_vwma_coppock_quarterly_value_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_431_vwma_coppock_quarterly_value_d3}, 'f33_cpkt_432_vwma_coppock_semi_annual_value_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_432_vwma_coppock_semi_annual_value_d3}, 'f33_cpkt_433_vwma_coppock_biennial_value_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_433_vwma_coppock_biennial_value_d3}, 'f33_cpkt_434_vwma_coppock_quarterly_slope_21d_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_434_vwma_coppock_quarterly_slope_21d_d3}, 'f33_cpkt_435_vwma_coppock_semi_annual_slope_63d_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_435_vwma_coppock_semi_annual_slope_63d_d3}, 'f33_cpkt_436_vwma_coppock_biennial_slope_63d_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_436_vwma_coppock_biennial_slope_63d_d3}, 'f33_cpkt_437_vwma_coppock_quarterly_zscore_252d_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_437_vwma_coppock_quarterly_zscore_252d_d3}, 'f33_cpkt_438_vwma_coppock_semi_annual_zscore_252d_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_438_vwma_coppock_semi_annual_zscore_252d_d3}, 'f33_cpkt_439_vwma_coppock_biennial_zscore_504d_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_439_vwma_coppock_biennial_zscore_504d_d3}, 'f33_cpkt_440_vwma_coppock_vs_std_coppock_quarterly_diff_d3': {'inputs': ['close', 'volume'], 'func': f33_cpkt_440_vwma_coppock_vs_std_coppock_quarterly_diff_d3}, 'f33_cpkt_441_dti_short_value_d3': {'inputs': ['close'], 'func': f33_cpkt_441_dti_short_value_d3}, 'f33_cpkt_442_dti_long_value_d3': {'inputs': ['close'], 'func': f33_cpkt_442_dti_long_value_d3}, 'f33_cpkt_443_dti_short_slope_21d_d3': {'inputs': ['close'], 'func': f33_cpkt_443_dti_short_slope_21d_d3}, 'f33_cpkt_444_dti_long_slope_63d_d3': {'inputs': ['close'], 'func': f33_cpkt_444_dti_long_slope_63d_d3}, 'f33_cpkt_445_dti_short_above_zero_indicator_d3': {'inputs': ['close'], 'func': f33_cpkt_445_dti_short_above_zero_indicator_d3}, 'f33_cpkt_446_special_k_signal_line_sma10_d3': {'inputs': ['close'], 'func': f33_cpkt_446_special_k_signal_line_sma10_d3}, 'f33_cpkt_447_special_k_above_signal_indicator_d3': {'inputs': ['close'], 'func': f33_cpkt_447_special_k_above_signal_indicator_d3}, 'f33_cpkt_448_special_k_slope_21d_d3': {'inputs': ['close'], 'func': f33_cpkt_448_special_k_slope_21d_d3}, 'f33_cpkt_449_special_k_d2_21d_d3': {'inputs': ['close'], 'func': f33_cpkt_449_special_k_d2_21d_d3}, 'f33_cpkt_450_special_k_zero_cross_bearish_event_d3': {'inputs': ['close'], 'func': f33_cpkt_450_special_k_zero_cross_bearish_event_d3}}