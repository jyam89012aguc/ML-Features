"""coppock_curve_kst d2 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py around long-smoothed
momentum indicators: Coppock Curve (multiple regime-length variants), KST (Know Sure
Thing) at standard/short/long-term horizons, signal-line crossovers, slope/rollover/
sign-change events, and price-divergence variants.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


# ---------------------------- Coppock / KST helpers ----------------------------

def _wma(s, n):
    """Weighted moving average with linearly increasing weights (Coppock convention)."""
    weights = np.arange(1, n + 1, dtype=float)
    wsum = weights.sum()
    def _ww(w):
        if np.isnan(w).any():
            return np.nan
        return float(np.dot(w, weights) / wsum)
    return s.rolling(n, min_periods=n).apply(_ww, raw=True)


def _roc_pct(s, n):
    return s.pct_change(n) * 100.0


def _coppock(close, n_long, n_short, n_wma):
    """Generic Coppock Curve: WMA(n_wma) of (ROC(n_long) + ROC(n_short))."""
    return _wma(_roc_pct(close, n_long) + _roc_pct(close, n_short), n_wma)


# Canonical Coppock variants — distinct regime-length hypotheses
def _coppock_annual(close):
    """Monthly-canonical Coppock adapted to daily: 14m/11m ROCs, 10m WMA (294/231/210)."""
    return _coppock(close, 294, 231, 210)


def _coppock_biennial(close):
    """Biennial-cycle Coppock: 504/378/210 — secular regime change detector."""
    return _coppock(close, DDAYS_2Y, 378, 210)


def _coppock_semi_annual(close):
    """Semi-annual-cycle Coppock: 126/84/42 — intermediate regime."""
    return _coppock(close, 126, 84, 42)


def _coppock_quarterly(close):
    """Quarterly-cycle Coppock: 63/42/21 — short-cycle momentum smoothing."""
    return _coppock(close, QDAYS, 42, MDAYS)


def _kst(close):
    """Pring's standard KST adapted to daily: 4-component weighted SMA of ROCs.
    Weights 1/2/3/4; ROC horizons 10/15/20/30; SMA horizons 10/10/10/15."""
    return (1.0 * _sma(_roc_pct(close, 10), 10)
            + 2.0 * _sma(_roc_pct(close, 15), 10)
            + 3.0 * _sma(_roc_pct(close, 20), 10)
            + 4.0 * _sma(_roc_pct(close, 30), 15))


def _kst_short_term(close):
    """Short-term KST (faster ROCs): horizons 5/8/12/18; SMA 5/5/5/8."""
    return (1.0 * _sma(_roc_pct(close, 5), 5)
            + 2.0 * _sma(_roc_pct(close, 8), 5)
            + 3.0 * _sma(_roc_pct(close, 12), 5)
            + 4.0 * _sma(_roc_pct(close, 18), 8))


def _kst_long_term(close):
    """Long-term KST (slower ROCs): horizons 65/130/195/260; SMA 21/21/21/42 — secular regime tool."""
    return (1.0 * _sma(_roc_pct(close, 65), 21)
            + 2.0 * _sma(_roc_pct(close, 130), 21)
            + 3.0 * _sma(_roc_pct(close, 195), 21)
            + 4.0 * _sma(_roc_pct(close, 260), 42))


def _kst_signal(close, n_sig=9):
    return _sma(_kst(close), n_sig)


def _kst_long_signal(close, n_sig=21):
    return _sma(_kst_long_term(close), n_sig)


# ---------------------------- divergence helpers (reused from family 32 patterns) ----------------------------

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


def _rolling_corr_pearson(a, b, n):
    return a.rolling(n, min_periods=max(n // 3, 2)).corr(b)


def _zscore_gap(price, osc, n):
    return _rolling_zscore(_safe_log(price), n) - _rolling_zscore(osc, n)


# ============================================================
# Bucket A — Coppock (annual default) level & rank (001-010)
# ============================================================

def f33_cpkt_001_coppock_annual_value(close: pd.Series) -> pd.Series:
    """Coppock Curve at annual horizon (294/231/210) — canonical adapted to daily."""
    return _coppock_annual(close)


def f33_cpkt_002_coppock_annual_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of annual Coppock over trailing 252d."""
    return _rolling_zscore(_coppock_annual(close), YDAYS)


def f33_cpkt_003_coppock_annual_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of annual Coppock over trailing 504d (biennial baseline)."""
    return _rolling_zscore(_coppock_annual(close), DDAYS_2Y)


def f33_cpkt_004_coppock_annual_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of annual Coppock within trailing 252d."""
    return _pct_rank(_coppock_annual(close), YDAYS)


def f33_cpkt_005_coppock_annual_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of annual Coppock within trailing 504d."""
    return _pct_rank(_coppock_annual(close), DDAYS_2Y)


def f33_cpkt_006_coppock_annual_pct_rank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of annual Coppock within trailing 1260d (5y secular)."""
    return _pct_rank(_coppock_annual(close), DDAYS_5Y)


def f33_cpkt_007_coppock_annual_in_top_decile_indicator_252d(close: pd.Series) -> pd.Series:
    """+1 when annual Coppock is in trailing-252d top decile (overheated)."""
    return (_pct_rank(_coppock_annual(close), YDAYS) >= 0.9).astype(float).where(_coppock_annual(close).notna(), np.nan)


def f33_cpkt_008_coppock_annual_time_in_top_decile_252d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d that the annual Coppock spent in its trailing-252d top decile."""
    flag = (_pct_rank(_coppock_annual(close), YDAYS) >= 0.9).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_009_coppock_annual_above_zero_indicator(close: pd.Series) -> pd.Series:
    """+1 when annual Coppock > 0 (positive long-momentum regime)."""
    c = _coppock_annual(close)
    return (c > 0).astype(float).where(c.notna(), np.nan)


def f33_cpkt_010_coppock_annual_dist_from_zero_normalized_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual Coppock value normalized by ATR21 — scale-free distance from zero."""
    c = _coppock_annual(close)
    atr = _atr(high, low, close, MDAYS)
    return _safe_div(c, atr)


# ============================================================
# Bucket B — Coppock (annual) slope / rollover (011-020)
# ============================================================

def f33_cpkt_011_coppock_annual_slope_63d(close: pd.Series) -> pd.Series:
    """Slope of annual Coppock over trailing 63d (short-cycle trajectory)."""
    return _rolling_slope(_coppock_annual(close), QDAYS)


def f33_cpkt_012_coppock_annual_slope_252d(close: pd.Series) -> pd.Series:
    """Slope of annual Coppock over trailing 252d (annual trajectory)."""
    return _rolling_slope(_coppock_annual(close), YDAYS)


def f33_cpkt_013_coppock_annual_slope_sign(close: pd.Series) -> pd.Series:
    """Sign of 63d-slope (+1/0/-1)."""
    s = _rolling_slope(_coppock_annual(close), QDAYS)
    return np.sign(s).where(s.notna(), np.nan)


def f33_cpkt_014_coppock_annual_slope_sign_change_bearish_indicator(close: pd.Series) -> pd.Series:
    """+1 when 63d-slope crosses from + to - (rollover event)."""
    s = _rolling_slope(_coppock_annual(close), QDAYS)
    return ((s.shift(1) > 0) & (s <= 0)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)


def f33_cpkt_015_coppock_annual_rollover_event_63d(close: pd.Series) -> pd.Series:
    """+1 if 63d-ago Coppock-slope was positive AND current 21d-slope is negative."""
    s_long = _rolling_slope(_coppock_annual(close), QDAYS).shift(QDAYS)
    s_short = _rolling_slope(_coppock_annual(close), MDAYS)
    return ((s_long > 0) & (s_short < 0)).astype(float).where(s_long.notna() & s_short.notna(), np.nan)


def f33_cpkt_016_coppock_annual_peak_detected_local21d_indicator(close: pd.Series) -> pd.Series:
    """+1 when current Coppock equals its trailing-21d max AND > 3d-prior value — confirmed local peak."""
    c = _coppock_annual(close)
    return ((c == c.rolling(MDAYS, min_periods=WDAYS).max()) & (c > c.shift(3))).astype(float).where(c.notna(), np.nan)


def f33_cpkt_017_coppock_annual_peak_to_current_decay_pct(close: pd.Series) -> pd.Series:
    """Percentage decay of current Coppock from its trailing-252d max (negative = below peak)."""
    c = _coppock_annual(close)
    mx = c.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(c - mx, mx.abs())


def f33_cpkt_018_coppock_annual_days_since_252d_peak(close: pd.Series) -> pd.Series:
    """Bars since Coppock printed its trailing-252d maximum."""
    c = _coppock_annual(close)
    flag = (c == c.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_019_coppock_annual_dist_from_252d_max(close: pd.Series) -> pd.Series:
    """Difference (Coppock - 252d-trailing-max). Always ≤ 0; magnitude = distance below peak."""
    c = _coppock_annual(close)
    return c - c.rolling(YDAYS, min_periods=QDAYS).max()


def f33_cpkt_020_coppock_annual_velocity_at_peak(close: pd.Series) -> pd.Series:
    """5d-slope of Coppock at the bar of trailing-21d-max — speed of approach to local peak."""
    c = _coppock_annual(close)
    slope5 = _rolling_slope(c, WDAYS)
    is_pk = (c == c.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    return slope5.where(is_pk == 1, np.nan).ffill()


# ============================================================
# Bucket C — Coppock (annual) sign-change events (021-030)
# ============================================================

def f33_cpkt_021_coppock_annual_days_since_positive_zero_cross(close: pd.Series) -> pd.Series:
    """Bars since Coppock crossed from negative to positive."""
    c = _coppock_annual(close)
    flag = ((c.shift(1) < 0) & (c >= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_022_coppock_annual_days_since_negative_zero_cross(close: pd.Series) -> pd.Series:
    """Bars since Coppock crossed from positive to negative — age of bearish regime."""
    c = _coppock_annual(close)
    flag = ((c.shift(1) > 0) & (c <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_023_coppock_annual_zero_cross_freq_252d(close: pd.Series) -> pd.Series:
    """Total zero-crossings (either direction) in trailing 252d — regime instability."""
    c = _coppock_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_024_coppock_annual_fraction_positive_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars with positive Coppock — bullish-regime density."""
    c = _coppock_annual(close)
    flag = (c > 0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean()


def f33_cpkt_025_coppock_annual_fraction_positive_504d(close: pd.Series) -> pd.Series:
    """Fraction positive over 504d — biennial-regime density."""
    c = _coppock_annual(close)
    flag = (c > 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f33_cpkt_026_coppock_annual_longest_positive_run_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive-positive run length within trailing 252d."""
    c = _coppock_annual(close)
    flag = (c > 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max()


def f33_cpkt_027_coppock_annual_longest_negative_run_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive-negative run length within trailing 252d."""
    c = _coppock_annual(close)
    flag = (c < 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max()


def f33_cpkt_028_coppock_annual_consecutive_positive_bars_current(close: pd.Series) -> pd.Series:
    """Current consecutive-positive-bar streak length."""
    c = _coppock_annual(close)
    flag = (c > 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f33_cpkt_029_coppock_annual_consecutive_negative_bars_current(close: pd.Series) -> pd.Series:
    """Current consecutive-negative-bar streak length."""
    c = _coppock_annual(close)
    flag = (c < 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f33_cpkt_030_coppock_annual_zero_cross_count_504d(close: pd.Series) -> pd.Series:
    """Zero-crossings in trailing 504d — long-window instability."""
    c = _coppock_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


# ============================================================
# Bucket D — Coppock variants at different cycle horizons (031-040)
# Each variant = a distinct hypothesis about regime length
# ============================================================

def f33_cpkt_031_coppock_quarterly_value(close: pd.Series) -> pd.Series:
    """Quarterly-cycle Coppock (63/42/21) — short-cycle momentum smoothing hypothesis."""
    return _coppock_quarterly(close)


def f33_cpkt_032_coppock_semi_annual_value(close: pd.Series) -> pd.Series:
    """Semi-annual Coppock (126/84/42) — intermediate-cycle hypothesis."""
    return _coppock_semi_annual(close)


def f33_cpkt_033_coppock_biennial_value(close: pd.Series) -> pd.Series:
    """Biennial Coppock (504/378/210) — secular-regime hypothesis."""
    return _coppock_biennial(close)


def f33_cpkt_034_coppock_quarterly_slope_63d(close: pd.Series) -> pd.Series:
    """63d slope of quarterly Coppock — second-derivative of short-cycle momentum."""
    return _rolling_slope(_coppock_quarterly(close), QDAYS)


def f33_cpkt_035_coppock_semi_annual_slope_63d(close: pd.Series) -> pd.Series:
    """63d slope of semi-annual Coppock — intermediate-cycle rollover indicator."""
    return _rolling_slope(_coppock_semi_annual(close), QDAYS)


def f33_cpkt_036_coppock_annual_slope_21d_short(close: pd.Series) -> pd.Series:
    """21d slope of annual Coppock — acute monthly trajectory in long-cycle indicator."""
    return _rolling_slope(_coppock_annual(close), MDAYS)


def f33_cpkt_037_coppock_biennial_slope_252d(close: pd.Series) -> pd.Series:
    """252d slope of biennial Coppock — secular-trajectory hypothesis."""
    return _rolling_slope(_coppock_biennial(close), YDAYS)


def f33_cpkt_038_coppock_quarterly_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of quarterly Coppock over 252d."""
    return _rolling_zscore(_coppock_quarterly(close), YDAYS)


def f33_cpkt_039_coppock_biennial_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of biennial Coppock over 504d."""
    return _rolling_zscore(_coppock_biennial(close), DDAYS_2Y)


def f33_cpkt_040_coppock_short_vs_long_disagreement(close: pd.Series) -> pd.Series:
    """Sign-disagreement: +1 if quarterly Coppock > 0 AND biennial Coppock < 0 (or vice versa) — regime tension."""
    cq = _coppock_quarterly(close); cb = _coppock_biennial(close)
    dis = ((np.sign(cq) != np.sign(cb)) & cq.notna() & cb.notna()).astype(float)
    return dis.where(cq.notna() & cb.notna(), np.nan)


# ============================================================
# Bucket E — KST level / extreme (041-050)
# ============================================================

def f33_cpkt_041_kst_daily_value(close: pd.Series) -> pd.Series:
    """Pring's KST adapted to daily — standard parameterization."""
    return _kst(close)


def f33_cpkt_042_kst_short_term_value(close: pd.Series) -> pd.Series:
    """Short-term KST (faster horizons) — acute-momentum hypothesis."""
    return _kst_short_term(close)


def f33_cpkt_043_kst_long_term_value(close: pd.Series) -> pd.Series:
    """Long-term KST (slow horizons) — secular-regime hypothesis."""
    return _kst_long_term(close)


def f33_cpkt_044_kst_daily_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of standard KST over trailing 252d."""
    return _rolling_zscore(_kst(close), YDAYS)


def f33_cpkt_045_kst_daily_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of standard KST over trailing 504d."""
    return _rolling_zscore(_kst(close), DDAYS_2Y)


def f33_cpkt_046_kst_daily_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of standard KST in trailing 252d."""
    return _pct_rank(_kst(close), YDAYS)


def f33_cpkt_047_kst_daily_pct_rank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of standard KST in trailing 1260d (5y)."""
    return _pct_rank(_kst(close), DDAYS_5Y)


def f33_cpkt_048_kst_daily_above_zero_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST > 0 (positive regime)."""
    k = _kst(close)
    return (k > 0).astype(float).where(k.notna(), np.nan)


def f33_cpkt_049_kst_daily_in_top_decile_indicator_252d(close: pd.Series) -> pd.Series:
    """+1 when KST in top decile of trailing 252d (overheated)."""
    return (_pct_rank(_kst(close), YDAYS) >= 0.9).astype(float).where(_kst(close).notna(), np.nan)


def f33_cpkt_050_kst_daily_dist_from_zero_normalized_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """KST normalized by ATR21 — scale-free distance from zero."""
    return _safe_div(_kst(close), _atr(high, low, close, MDAYS))


# ============================================================
# Bucket F — KST signal-line crossover (051-060)
# ============================================================

def f33_cpkt_051_kst_signal_line_value(close: pd.Series) -> pd.Series:
    """SMA-9 of KST (signal line)."""
    return _kst_signal(close, 9)


def f33_cpkt_052_kst_minus_signal_diff(close: pd.Series) -> pd.Series:
    """KST - signal-line — positive = bullish stance."""
    return _kst(close) - _kst_signal(close, 9)


def f33_cpkt_053_kst_signal_cross_bearish_indicator(close: pd.Series) -> pd.Series:
    """+1 on the bar where KST crossed below its signal line."""
    diff = _kst(close) - _kst_signal(close, 9)
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f33_cpkt_054_days_since_kst_bearish_cross(close: pd.Series) -> pd.Series:
    """Bars since the most recent KST bearish signal-line cross."""
    diff = _kst(close) - _kst_signal(close, 9)
    flag = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_055_kst_below_signal_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST < signal line."""
    diff = _kst(close) - _kst_signal(close, 9)
    return (diff < 0).astype(float).where(diff.notna(), np.nan)


def f33_cpkt_056_kst_persistence_below_signal_consec_bars(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with KST < signal."""
    diff = _kst(close) - _kst_signal(close, 9)
    flag = (diff < 0).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f33_cpkt_057_kst_signal_cross_count_252d(close: pd.Series) -> pd.Series:
    """Count of bearish KST signal crosses in trailing 252d — instability."""
    diff = _kst(close) - _kst_signal(close, 9)
    flag = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_058_kst_signal_gap_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (KST - signal) over 252d — normalized extension/lag."""
    return _rolling_zscore(_kst(close) - _kst_signal(close, 9), YDAYS)


def f33_cpkt_059_kst_signal_cross_magnitude_at_event(close: pd.Series) -> pd.Series:
    """KST level at moment of last bearish cross — held-forward as 'cross altitude' indicator."""
    k = _kst(close)
    diff = k - _kst_signal(close, 9)
    flag = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    return k.where(flag == 1, np.nan).ffill()


def f33_cpkt_060_days_since_kst_bullish_cross(close: pd.Series) -> pd.Series:
    """Bars since most recent bullish KST signal-line cross — age of bullish regime."""
    diff = _kst(close) - _kst_signal(close, 9)
    flag = ((diff.shift(1) < 0) & (diff >= 0)).astype(float)
    return _bars_since_true(flag)


# ============================================================
# Bucket G — KST slope / rollover (061-070)
# ============================================================

def f33_cpkt_061_kst_slope_63d(close: pd.Series) -> pd.Series:
    """63d slope of standard KST."""
    return _rolling_slope(_kst(close), QDAYS)


def f33_cpkt_062_kst_slope_252d(close: pd.Series) -> pd.Series:
    """252d slope of standard KST — long-cycle trajectory."""
    return _rolling_slope(_kst(close), YDAYS)


def f33_cpkt_063_kst_slope_sign(close: pd.Series) -> pd.Series:
    """Sign of 63d-KST slope (+1/0/-1)."""
    s = _rolling_slope(_kst(close), QDAYS)
    return np.sign(s).where(s.notna(), np.nan)


def f33_cpkt_064_kst_slope_sign_change_bearish_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where KST 63d-slope flipped + → -."""
    s = _rolling_slope(_kst(close), QDAYS)
    return ((s.shift(1) > 0) & (s <= 0)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan)


def f33_cpkt_065_kst_rollover_event_63d(close: pd.Series) -> pd.Series:
    """+1 if KST slope 63d ago was positive AND current 21d slope is negative."""
    s_long = _rolling_slope(_kst(close), QDAYS).shift(QDAYS)
    s_short = _rolling_slope(_kst(close), MDAYS)
    return ((s_long > 0) & (s_short < 0)).astype(float).where(s_long.notna() & s_short.notna(), np.nan)


def f33_cpkt_066_kst_peak_detected_local21d_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST equals trailing-21d max AND > 3d-prior — confirmed local peak."""
    k = _kst(close)
    return ((k == k.rolling(MDAYS, min_periods=WDAYS).max()) & (k > k.shift(3))).astype(float).where(k.notna(), np.nan)


def f33_cpkt_067_kst_days_since_252d_peak(close: pd.Series) -> pd.Series:
    """Bars since KST printed its trailing-252d maximum."""
    k = _kst(close)
    flag = (k == k.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_068_kst_peak_to_current_decay_pct(close: pd.Series) -> pd.Series:
    """% decay of KST from its trailing-252d max."""
    k = _kst(close)
    mx = k.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(k - mx, mx.abs())


def f33_cpkt_069_kst_dist_from_252d_max(close: pd.Series) -> pd.Series:
    """KST minus its trailing-252d max — distance below peak."""
    k = _kst(close)
    return k - k.rolling(YDAYS, min_periods=QDAYS).max()


def f33_cpkt_070_kst_slope_acceleration_21d(close: pd.Series) -> pd.Series:
    """Slope-of-slope of KST over 21d — short-term acceleration."""
    s = _rolling_slope(_kst(close), MDAYS)
    return _rolling_slope(s, MDAYS)


# ============================================================
# Bucket H — KST × price divergence (071-075)
# ============================================================

def f33_cpkt_071_kst_slope_div_sign_63d(close: pd.Series) -> pd.Series:
    """Bearish slope-divergence between log-close and KST over 63d."""
    return _slope_div_sign(close, _kst(close), QDAYS)


def f33_cpkt_072_kst_shift_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — price > 63d-ago AND KST < 63d-ago."""
    return _shift_div_bearish_indicator(close, _kst(close), QDAYS)


def f33_cpkt_073_kst_zscore_gap_63d(close: pd.Series) -> pd.Series:
    """z(log close,63) - z(KST,63) — extension gap."""
    return _zscore_gap(close, _kst(close), QDAYS)


def f33_cpkt_074_kst_hidden_bearish_div_63d(close: pd.Series) -> pd.Series:
    """Hidden bearish — price LH + KST HH over 63d."""
    return _shift_div_hidden_bearish_indicator(close, _kst(close), QDAYS)


def f33_cpkt_075_kst_rolling_corr_price_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d Pearson corr of log-close and KST."""
    return _rolling_corr_pearson(_safe_log(close), _kst(close), QDAYS)


# ============================================================
# REGISTRY
# ============================================================



def f33_cpkt_001_coppock_annual_value_d2(close):
    return f33_cpkt_001_coppock_annual_value(close).diff().diff()


def f33_cpkt_002_coppock_annual_zscore_252d_d2(close):
    return f33_cpkt_002_coppock_annual_zscore_252d(close).diff().diff()


def f33_cpkt_003_coppock_annual_zscore_504d_d2(close):
    return f33_cpkt_003_coppock_annual_zscore_504d(close).diff().diff()


def f33_cpkt_004_coppock_annual_pct_rank_252d_d2(close):
    return f33_cpkt_004_coppock_annual_pct_rank_252d(close).diff().diff()


def f33_cpkt_005_coppock_annual_pct_rank_504d_d2(close):
    return f33_cpkt_005_coppock_annual_pct_rank_504d(close).diff().diff()


def f33_cpkt_006_coppock_annual_pct_rank_1260d_d2(close):
    return f33_cpkt_006_coppock_annual_pct_rank_1260d(close).diff().diff()


def f33_cpkt_007_coppock_annual_in_top_decile_indicator_252d_d2(close):
    return f33_cpkt_007_coppock_annual_in_top_decile_indicator_252d(close).diff().diff()


def f33_cpkt_008_coppock_annual_time_in_top_decile_252d_d2(close):
    return f33_cpkt_008_coppock_annual_time_in_top_decile_252d(close).diff().diff()


def f33_cpkt_009_coppock_annual_above_zero_indicator_d2(close):
    return f33_cpkt_009_coppock_annual_above_zero_indicator(close).diff().diff()


def f33_cpkt_010_coppock_annual_dist_from_zero_normalized_atr_d2(high, low, close):
    return f33_cpkt_010_coppock_annual_dist_from_zero_normalized_atr(high, low, close).diff().diff()


def f33_cpkt_011_coppock_annual_slope_63d_d2(close):
    return f33_cpkt_011_coppock_annual_slope_63d(close).diff().diff()


def f33_cpkt_012_coppock_annual_slope_252d_d2(close):
    return f33_cpkt_012_coppock_annual_slope_252d(close).diff().diff()


def f33_cpkt_013_coppock_annual_slope_sign_d2(close):
    return f33_cpkt_013_coppock_annual_slope_sign(close).diff().diff()


def f33_cpkt_014_coppock_annual_slope_sign_change_bearish_indicator_d2(close):
    return f33_cpkt_014_coppock_annual_slope_sign_change_bearish_indicator(close).diff().diff()


def f33_cpkt_015_coppock_annual_rollover_event_63d_d2(close):
    return f33_cpkt_015_coppock_annual_rollover_event_63d(close).diff().diff()


def f33_cpkt_016_coppock_annual_peak_detected_local21d_indicator_d2(close):
    return f33_cpkt_016_coppock_annual_peak_detected_local21d_indicator(close).diff().diff()


def f33_cpkt_017_coppock_annual_peak_to_current_decay_pct_d2(close):
    return f33_cpkt_017_coppock_annual_peak_to_current_decay_pct(close).diff().diff()


def f33_cpkt_018_coppock_annual_days_since_252d_peak_d2(close):
    return f33_cpkt_018_coppock_annual_days_since_252d_peak(close).diff().diff()


def f33_cpkt_019_coppock_annual_dist_from_252d_max_d2(close):
    return f33_cpkt_019_coppock_annual_dist_from_252d_max(close).diff().diff()


def f33_cpkt_020_coppock_annual_velocity_at_peak_d2(close):
    return f33_cpkt_020_coppock_annual_velocity_at_peak(close).diff().diff()


def f33_cpkt_021_coppock_annual_days_since_positive_zero_cross_d2(close):
    return f33_cpkt_021_coppock_annual_days_since_positive_zero_cross(close).diff().diff()


def f33_cpkt_022_coppock_annual_days_since_negative_zero_cross_d2(close):
    return f33_cpkt_022_coppock_annual_days_since_negative_zero_cross(close).diff().diff()


def f33_cpkt_023_coppock_annual_zero_cross_freq_252d_d2(close):
    return f33_cpkt_023_coppock_annual_zero_cross_freq_252d(close).diff().diff()


def f33_cpkt_024_coppock_annual_fraction_positive_252d_d2(close):
    return f33_cpkt_024_coppock_annual_fraction_positive_252d(close).diff().diff()


def f33_cpkt_025_coppock_annual_fraction_positive_504d_d2(close):
    return f33_cpkt_025_coppock_annual_fraction_positive_504d(close).diff().diff()


def f33_cpkt_026_coppock_annual_longest_positive_run_252d_d2(close):
    return f33_cpkt_026_coppock_annual_longest_positive_run_252d(close).diff().diff()


def f33_cpkt_027_coppock_annual_longest_negative_run_252d_d2(close):
    return f33_cpkt_027_coppock_annual_longest_negative_run_252d(close).diff().diff()


def f33_cpkt_028_coppock_annual_consecutive_positive_bars_current_d2(close):
    return f33_cpkt_028_coppock_annual_consecutive_positive_bars_current(close).diff().diff()


def f33_cpkt_029_coppock_annual_consecutive_negative_bars_current_d2(close):
    return f33_cpkt_029_coppock_annual_consecutive_negative_bars_current(close).diff().diff()


def f33_cpkt_030_coppock_annual_zero_cross_count_504d_d2(close):
    return f33_cpkt_030_coppock_annual_zero_cross_count_504d(close).diff().diff()


def f33_cpkt_031_coppock_quarterly_value_d2(close):
    return f33_cpkt_031_coppock_quarterly_value(close).diff().diff()


def f33_cpkt_032_coppock_semi_annual_value_d2(close):
    return f33_cpkt_032_coppock_semi_annual_value(close).diff().diff()


def f33_cpkt_033_coppock_biennial_value_d2(close):
    return f33_cpkt_033_coppock_biennial_value(close).diff().diff()


def f33_cpkt_034_coppock_quarterly_slope_63d_d2(close):
    return f33_cpkt_034_coppock_quarterly_slope_63d(close).diff().diff()


def f33_cpkt_035_coppock_semi_annual_slope_63d_d2(close):
    return f33_cpkt_035_coppock_semi_annual_slope_63d(close).diff().diff()


def f33_cpkt_036_coppock_annual_slope_21d_short_d2(close):
    return f33_cpkt_036_coppock_annual_slope_21d_short(close).diff().diff()


def f33_cpkt_037_coppock_biennial_slope_252d_d2(close):
    return f33_cpkt_037_coppock_biennial_slope_252d(close).diff().diff()


def f33_cpkt_038_coppock_quarterly_zscore_252d_d2(close):
    return f33_cpkt_038_coppock_quarterly_zscore_252d(close).diff().diff()


def f33_cpkt_039_coppock_biennial_zscore_504d_d2(close):
    return f33_cpkt_039_coppock_biennial_zscore_504d(close).diff().diff()


def f33_cpkt_040_coppock_short_vs_long_disagreement_d2(close):
    return f33_cpkt_040_coppock_short_vs_long_disagreement(close).diff().diff()


def f33_cpkt_041_kst_daily_value_d2(close):
    return f33_cpkt_041_kst_daily_value(close).diff().diff()


def f33_cpkt_042_kst_short_term_value_d2(close):
    return f33_cpkt_042_kst_short_term_value(close).diff().diff()


def f33_cpkt_043_kst_long_term_value_d2(close):
    return f33_cpkt_043_kst_long_term_value(close).diff().diff()


def f33_cpkt_044_kst_daily_zscore_252d_d2(close):
    return f33_cpkt_044_kst_daily_zscore_252d(close).diff().diff()


def f33_cpkt_045_kst_daily_zscore_504d_d2(close):
    return f33_cpkt_045_kst_daily_zscore_504d(close).diff().diff()


def f33_cpkt_046_kst_daily_pct_rank_252d_d2(close):
    return f33_cpkt_046_kst_daily_pct_rank_252d(close).diff().diff()


def f33_cpkt_047_kst_daily_pct_rank_1260d_d2(close):
    return f33_cpkt_047_kst_daily_pct_rank_1260d(close).diff().diff()


def f33_cpkt_048_kst_daily_above_zero_indicator_d2(close):
    return f33_cpkt_048_kst_daily_above_zero_indicator(close).diff().diff()


def f33_cpkt_049_kst_daily_in_top_decile_indicator_252d_d2(close):
    return f33_cpkt_049_kst_daily_in_top_decile_indicator_252d(close).diff().diff()


def f33_cpkt_050_kst_daily_dist_from_zero_normalized_atr_d2(high, low, close):
    return f33_cpkt_050_kst_daily_dist_from_zero_normalized_atr(high, low, close).diff().diff()


def f33_cpkt_051_kst_signal_line_value_d2(close):
    return f33_cpkt_051_kst_signal_line_value(close).diff().diff()


def f33_cpkt_052_kst_minus_signal_diff_d2(close):
    return f33_cpkt_052_kst_minus_signal_diff(close).diff().diff()


def f33_cpkt_053_kst_signal_cross_bearish_indicator_d2(close):
    return f33_cpkt_053_kst_signal_cross_bearish_indicator(close).diff().diff()


def f33_cpkt_054_days_since_kst_bearish_cross_d2(close):
    return f33_cpkt_054_days_since_kst_bearish_cross(close).diff().diff()


def f33_cpkt_055_kst_below_signal_indicator_d2(close):
    return f33_cpkt_055_kst_below_signal_indicator(close).diff().diff()


def f33_cpkt_056_kst_persistence_below_signal_consec_bars_d2(close):
    return f33_cpkt_056_kst_persistence_below_signal_consec_bars(close).diff().diff()


def f33_cpkt_057_kst_signal_cross_count_252d_d2(close):
    return f33_cpkt_057_kst_signal_cross_count_252d(close).diff().diff()


def f33_cpkt_058_kst_signal_gap_zscore_252d_d2(close):
    return f33_cpkt_058_kst_signal_gap_zscore_252d(close).diff().diff()


def f33_cpkt_059_kst_signal_cross_magnitude_at_event_d2(close):
    return f33_cpkt_059_kst_signal_cross_magnitude_at_event(close).diff().diff()


def f33_cpkt_060_days_since_kst_bullish_cross_d2(close):
    return f33_cpkt_060_days_since_kst_bullish_cross(close).diff().diff()


def f33_cpkt_061_kst_slope_63d_d2(close):
    return f33_cpkt_061_kst_slope_63d(close).diff().diff()


def f33_cpkt_062_kst_slope_252d_d2(close):
    return f33_cpkt_062_kst_slope_252d(close).diff().diff()


def f33_cpkt_063_kst_slope_sign_d2(close):
    return f33_cpkt_063_kst_slope_sign(close).diff().diff()


def f33_cpkt_064_kst_slope_sign_change_bearish_indicator_d2(close):
    return f33_cpkt_064_kst_slope_sign_change_bearish_indicator(close).diff().diff()


def f33_cpkt_065_kst_rollover_event_63d_d2(close):
    return f33_cpkt_065_kst_rollover_event_63d(close).diff().diff()


def f33_cpkt_066_kst_peak_detected_local21d_indicator_d2(close):
    return f33_cpkt_066_kst_peak_detected_local21d_indicator(close).diff().diff()


def f33_cpkt_067_kst_days_since_252d_peak_d2(close):
    return f33_cpkt_067_kst_days_since_252d_peak(close).diff().diff()


def f33_cpkt_068_kst_peak_to_current_decay_pct_d2(close):
    return f33_cpkt_068_kst_peak_to_current_decay_pct(close).diff().diff()


def f33_cpkt_069_kst_dist_from_252d_max_d2(close):
    return f33_cpkt_069_kst_dist_from_252d_max(close).diff().diff()


def f33_cpkt_070_kst_slope_acceleration_21d_d2(close):
    return f33_cpkt_070_kst_slope_acceleration_21d(close).diff().diff()


def f33_cpkt_071_kst_slope_div_sign_63d_d2(close):
    return f33_cpkt_071_kst_slope_div_sign_63d(close).diff().diff()


def f33_cpkt_072_kst_shift_div_indicator_63d_d2(close):
    return f33_cpkt_072_kst_shift_div_indicator_63d(close).diff().diff()


def f33_cpkt_073_kst_zscore_gap_63d_d2(close):
    return f33_cpkt_073_kst_zscore_gap_63d(close).diff().diff()


def f33_cpkt_074_kst_hidden_bearish_div_63d_d2(close):
    return f33_cpkt_074_kst_hidden_bearish_div_63d(close).diff().diff()


def f33_cpkt_075_kst_rolling_corr_price_63d_d2(close):
    return f33_cpkt_075_kst_rolling_corr_price_63d(close).diff().diff()


COPPOCK_CURVE_KST_D2_REGISTRY_001_075 = {
    "f33_cpkt_001_coppock_annual_value_d2": {"inputs": ["close"], "func": f33_cpkt_001_coppock_annual_value_d2},
    "f33_cpkt_002_coppock_annual_zscore_252d_d2": {"inputs": ["close"], "func": f33_cpkt_002_coppock_annual_zscore_252d_d2},
    "f33_cpkt_003_coppock_annual_zscore_504d_d2": {"inputs": ["close"], "func": f33_cpkt_003_coppock_annual_zscore_504d_d2},
    "f33_cpkt_004_coppock_annual_pct_rank_252d_d2": {"inputs": ["close"], "func": f33_cpkt_004_coppock_annual_pct_rank_252d_d2},
    "f33_cpkt_005_coppock_annual_pct_rank_504d_d2": {"inputs": ["close"], "func": f33_cpkt_005_coppock_annual_pct_rank_504d_d2},
    "f33_cpkt_006_coppock_annual_pct_rank_1260d_d2": {"inputs": ["close"], "func": f33_cpkt_006_coppock_annual_pct_rank_1260d_d2},
    "f33_cpkt_007_coppock_annual_in_top_decile_indicator_252d_d2": {"inputs": ["close"], "func": f33_cpkt_007_coppock_annual_in_top_decile_indicator_252d_d2},
    "f33_cpkt_008_coppock_annual_time_in_top_decile_252d_d2": {"inputs": ["close"], "func": f33_cpkt_008_coppock_annual_time_in_top_decile_252d_d2},
    "f33_cpkt_009_coppock_annual_above_zero_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_009_coppock_annual_above_zero_indicator_d2},
    "f33_cpkt_010_coppock_annual_dist_from_zero_normalized_atr_d2": {"inputs": ["high", "low", "close"], "func": f33_cpkt_010_coppock_annual_dist_from_zero_normalized_atr_d2},
    "f33_cpkt_011_coppock_annual_slope_63d_d2": {"inputs": ["close"], "func": f33_cpkt_011_coppock_annual_slope_63d_d2},
    "f33_cpkt_012_coppock_annual_slope_252d_d2": {"inputs": ["close"], "func": f33_cpkt_012_coppock_annual_slope_252d_d2},
    "f33_cpkt_013_coppock_annual_slope_sign_d2": {"inputs": ["close"], "func": f33_cpkt_013_coppock_annual_slope_sign_d2},
    "f33_cpkt_014_coppock_annual_slope_sign_change_bearish_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_014_coppock_annual_slope_sign_change_bearish_indicator_d2},
    "f33_cpkt_015_coppock_annual_rollover_event_63d_d2": {"inputs": ["close"], "func": f33_cpkt_015_coppock_annual_rollover_event_63d_d2},
    "f33_cpkt_016_coppock_annual_peak_detected_local21d_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_016_coppock_annual_peak_detected_local21d_indicator_d2},
    "f33_cpkt_017_coppock_annual_peak_to_current_decay_pct_d2": {"inputs": ["close"], "func": f33_cpkt_017_coppock_annual_peak_to_current_decay_pct_d2},
    "f33_cpkt_018_coppock_annual_days_since_252d_peak_d2": {"inputs": ["close"], "func": f33_cpkt_018_coppock_annual_days_since_252d_peak_d2},
    "f33_cpkt_019_coppock_annual_dist_from_252d_max_d2": {"inputs": ["close"], "func": f33_cpkt_019_coppock_annual_dist_from_252d_max_d2},
    "f33_cpkt_020_coppock_annual_velocity_at_peak_d2": {"inputs": ["close"], "func": f33_cpkt_020_coppock_annual_velocity_at_peak_d2},
    "f33_cpkt_021_coppock_annual_days_since_positive_zero_cross_d2": {"inputs": ["close"], "func": f33_cpkt_021_coppock_annual_days_since_positive_zero_cross_d2},
    "f33_cpkt_022_coppock_annual_days_since_negative_zero_cross_d2": {"inputs": ["close"], "func": f33_cpkt_022_coppock_annual_days_since_negative_zero_cross_d2},
    "f33_cpkt_023_coppock_annual_zero_cross_freq_252d_d2": {"inputs": ["close"], "func": f33_cpkt_023_coppock_annual_zero_cross_freq_252d_d2},
    "f33_cpkt_024_coppock_annual_fraction_positive_252d_d2": {"inputs": ["close"], "func": f33_cpkt_024_coppock_annual_fraction_positive_252d_d2},
    "f33_cpkt_025_coppock_annual_fraction_positive_504d_d2": {"inputs": ["close"], "func": f33_cpkt_025_coppock_annual_fraction_positive_504d_d2},
    "f33_cpkt_026_coppock_annual_longest_positive_run_252d_d2": {"inputs": ["close"], "func": f33_cpkt_026_coppock_annual_longest_positive_run_252d_d2},
    "f33_cpkt_027_coppock_annual_longest_negative_run_252d_d2": {"inputs": ["close"], "func": f33_cpkt_027_coppock_annual_longest_negative_run_252d_d2},
    "f33_cpkt_028_coppock_annual_consecutive_positive_bars_current_d2": {"inputs": ["close"], "func": f33_cpkt_028_coppock_annual_consecutive_positive_bars_current_d2},
    "f33_cpkt_029_coppock_annual_consecutive_negative_bars_current_d2": {"inputs": ["close"], "func": f33_cpkt_029_coppock_annual_consecutive_negative_bars_current_d2},
    "f33_cpkt_030_coppock_annual_zero_cross_count_504d_d2": {"inputs": ["close"], "func": f33_cpkt_030_coppock_annual_zero_cross_count_504d_d2},
    "f33_cpkt_031_coppock_quarterly_value_d2": {"inputs": ["close"], "func": f33_cpkt_031_coppock_quarterly_value_d2},
    "f33_cpkt_032_coppock_semi_annual_value_d2": {"inputs": ["close"], "func": f33_cpkt_032_coppock_semi_annual_value_d2},
    "f33_cpkt_033_coppock_biennial_value_d2": {"inputs": ["close"], "func": f33_cpkt_033_coppock_biennial_value_d2},
    "f33_cpkt_034_coppock_quarterly_slope_63d_d2": {"inputs": ["close"], "func": f33_cpkt_034_coppock_quarterly_slope_63d_d2},
    "f33_cpkt_035_coppock_semi_annual_slope_63d_d2": {"inputs": ["close"], "func": f33_cpkt_035_coppock_semi_annual_slope_63d_d2},
    "f33_cpkt_036_coppock_annual_slope_21d_short_d2": {"inputs": ["close"], "func": f33_cpkt_036_coppock_annual_slope_21d_short_d2},
    "f33_cpkt_037_coppock_biennial_slope_252d_d2": {"inputs": ["close"], "func": f33_cpkt_037_coppock_biennial_slope_252d_d2},
    "f33_cpkt_038_coppock_quarterly_zscore_252d_d2": {"inputs": ["close"], "func": f33_cpkt_038_coppock_quarterly_zscore_252d_d2},
    "f33_cpkt_039_coppock_biennial_zscore_504d_d2": {"inputs": ["close"], "func": f33_cpkt_039_coppock_biennial_zscore_504d_d2},
    "f33_cpkt_040_coppock_short_vs_long_disagreement_d2": {"inputs": ["close"], "func": f33_cpkt_040_coppock_short_vs_long_disagreement_d2},
    "f33_cpkt_041_kst_daily_value_d2": {"inputs": ["close"], "func": f33_cpkt_041_kst_daily_value_d2},
    "f33_cpkt_042_kst_short_term_value_d2": {"inputs": ["close"], "func": f33_cpkt_042_kst_short_term_value_d2},
    "f33_cpkt_043_kst_long_term_value_d2": {"inputs": ["close"], "func": f33_cpkt_043_kst_long_term_value_d2},
    "f33_cpkt_044_kst_daily_zscore_252d_d2": {"inputs": ["close"], "func": f33_cpkt_044_kst_daily_zscore_252d_d2},
    "f33_cpkt_045_kst_daily_zscore_504d_d2": {"inputs": ["close"], "func": f33_cpkt_045_kst_daily_zscore_504d_d2},
    "f33_cpkt_046_kst_daily_pct_rank_252d_d2": {"inputs": ["close"], "func": f33_cpkt_046_kst_daily_pct_rank_252d_d2},
    "f33_cpkt_047_kst_daily_pct_rank_1260d_d2": {"inputs": ["close"], "func": f33_cpkt_047_kst_daily_pct_rank_1260d_d2},
    "f33_cpkt_048_kst_daily_above_zero_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_048_kst_daily_above_zero_indicator_d2},
    "f33_cpkt_049_kst_daily_in_top_decile_indicator_252d_d2": {"inputs": ["close"], "func": f33_cpkt_049_kst_daily_in_top_decile_indicator_252d_d2},
    "f33_cpkt_050_kst_daily_dist_from_zero_normalized_atr_d2": {"inputs": ["high", "low", "close"], "func": f33_cpkt_050_kst_daily_dist_from_zero_normalized_atr_d2},
    "f33_cpkt_051_kst_signal_line_value_d2": {"inputs": ["close"], "func": f33_cpkt_051_kst_signal_line_value_d2},
    "f33_cpkt_052_kst_minus_signal_diff_d2": {"inputs": ["close"], "func": f33_cpkt_052_kst_minus_signal_diff_d2},
    "f33_cpkt_053_kst_signal_cross_bearish_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_053_kst_signal_cross_bearish_indicator_d2},
    "f33_cpkt_054_days_since_kst_bearish_cross_d2": {"inputs": ["close"], "func": f33_cpkt_054_days_since_kst_bearish_cross_d2},
    "f33_cpkt_055_kst_below_signal_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_055_kst_below_signal_indicator_d2},
    "f33_cpkt_056_kst_persistence_below_signal_consec_bars_d2": {"inputs": ["close"], "func": f33_cpkt_056_kst_persistence_below_signal_consec_bars_d2},
    "f33_cpkt_057_kst_signal_cross_count_252d_d2": {"inputs": ["close"], "func": f33_cpkt_057_kst_signal_cross_count_252d_d2},
    "f33_cpkt_058_kst_signal_gap_zscore_252d_d2": {"inputs": ["close"], "func": f33_cpkt_058_kst_signal_gap_zscore_252d_d2},
    "f33_cpkt_059_kst_signal_cross_magnitude_at_event_d2": {"inputs": ["close"], "func": f33_cpkt_059_kst_signal_cross_magnitude_at_event_d2},
    "f33_cpkt_060_days_since_kst_bullish_cross_d2": {"inputs": ["close"], "func": f33_cpkt_060_days_since_kst_bullish_cross_d2},
    "f33_cpkt_061_kst_slope_63d_d2": {"inputs": ["close"], "func": f33_cpkt_061_kst_slope_63d_d2},
    "f33_cpkt_062_kst_slope_252d_d2": {"inputs": ["close"], "func": f33_cpkt_062_kst_slope_252d_d2},
    "f33_cpkt_063_kst_slope_sign_d2": {"inputs": ["close"], "func": f33_cpkt_063_kst_slope_sign_d2},
    "f33_cpkt_064_kst_slope_sign_change_bearish_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_064_kst_slope_sign_change_bearish_indicator_d2},
    "f33_cpkt_065_kst_rollover_event_63d_d2": {"inputs": ["close"], "func": f33_cpkt_065_kst_rollover_event_63d_d2},
    "f33_cpkt_066_kst_peak_detected_local21d_indicator_d2": {"inputs": ["close"], "func": f33_cpkt_066_kst_peak_detected_local21d_indicator_d2},
    "f33_cpkt_067_kst_days_since_252d_peak_d2": {"inputs": ["close"], "func": f33_cpkt_067_kst_days_since_252d_peak_d2},
    "f33_cpkt_068_kst_peak_to_current_decay_pct_d2": {"inputs": ["close"], "func": f33_cpkt_068_kst_peak_to_current_decay_pct_d2},
    "f33_cpkt_069_kst_dist_from_252d_max_d2": {"inputs": ["close"], "func": f33_cpkt_069_kst_dist_from_252d_max_d2},
    "f33_cpkt_070_kst_slope_acceleration_21d_d2": {"inputs": ["close"], "func": f33_cpkt_070_kst_slope_acceleration_21d_d2},
    "f33_cpkt_071_kst_slope_div_sign_63d_d2": {"inputs": ["close"], "func": f33_cpkt_071_kst_slope_div_sign_63d_d2},
    "f33_cpkt_072_kst_shift_div_indicator_63d_d2": {"inputs": ["close"], "func": f33_cpkt_072_kst_shift_div_indicator_63d_d2},
    "f33_cpkt_073_kst_zscore_gap_63d_d2": {"inputs": ["close"], "func": f33_cpkt_073_kst_zscore_gap_63d_d2},
    "f33_cpkt_074_kst_hidden_bearish_div_63d_d2": {"inputs": ["close"], "func": f33_cpkt_074_kst_hidden_bearish_div_63d_d2},
    "f33_cpkt_075_kst_rolling_corr_price_63d_d2": {"inputs": ["close"], "func": f33_cpkt_075_kst_rolling_corr_price_63d_d2},
}
