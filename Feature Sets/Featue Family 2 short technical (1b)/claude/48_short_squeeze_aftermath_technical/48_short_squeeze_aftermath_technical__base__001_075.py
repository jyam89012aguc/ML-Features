"""short_squeeze_aftermath_technical base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Target phenomenon:
Nasdaq names that ran parabolically (often short-squeeze-driven) then collapsed
permanently. Features capture (a) NSIR-based short-interest dynamics, (b) price-
based squeeze-event signatures, (c) post-squeeze price collapse, (d) capitulation
and shake-out events, and (e) post-decline volume dryness.

Bucket A: NSIR short-interest levels & states.
Bucket B: NSIR changes / post-squeeze unwind.
Bucket C: Squeeze-event detection from price + volume (no NSIR).
Bucket D: Post-squeeze price-collapse measures (drawdown family).
Bucket E: Pre-collapse high-vol shake-outs / capitulation.
Bucket F: Volume during decline.

Inputs: SEP OHLCV (always) + NSIR (shortinterest, daystocover, shortpctfloat,
shortpctshares). NSIR-dependent functions return all-NaN series when their NSIR
input is all-NaN (pipeline contract: missing NSIR ticker is fed as NaN-stub).
Self-contained helpers; PIT-clean.
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


def _bars_since_true(mask):
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


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


# ============================================================
# Bucket A — NSIR short-interest levels & states (001-015)
# ============================================================

def f48_ssat_001_shortinterest_level(shortinterest: pd.Series) -> pd.Series:
    """Raw short-interest level (NSIR). NaN-stub when NSIR absent."""
    return shortinterest.astype(float)


def f48_ssat_002_shortinterest_zscore_252(shortinterest: pd.Series) -> pd.Series:
    """Z-score of short interest vs trailing 252d distribution."""
    return _rolling_zscore(shortinterest.astype(float), YDAYS, min_periods=QDAYS)


def f48_ssat_003_shortinterest_pct_change_21(shortinterest: pd.Series) -> pd.Series:
    """21d %-change in short interest — monthly SI trend."""
    return shortinterest.astype(float).pct_change(MDAYS)


def f48_ssat_004_shortinterest_pct_change_63(shortinterest: pd.Series) -> pd.Series:
    """63d %-change in short interest — quarterly SI trend."""
    return shortinterest.astype(float).pct_change(QDAYS)


def f48_ssat_005_shortinterest_pct_rank_252(shortinterest: pd.Series) -> pd.Series:
    """Pct rank of short interest vs trailing 252d."""
    return shortinterest.astype(float).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f48_ssat_006_daystocover_level(daystocover: pd.Series) -> pd.Series:
    """Days-to-cover level (NSIR)."""
    return daystocover.astype(float)


def f48_ssat_007_daystocover_zscore_252(daystocover: pd.Series) -> pd.Series:
    """Z-score of days-to-cover vs 252d distribution."""
    return _rolling_zscore(daystocover.astype(float), YDAYS, min_periods=QDAYS)


def f48_ssat_008_daystocover_above_5_state(daystocover: pd.Series) -> pd.Series:
    """1 if daystocover > 5 — elevated squeeze-risk state."""
    d = daystocover.astype(float)
    return (d > 5.0).astype(float).where(d.notna(), np.nan)


def f48_ssat_009_daystocover_above_10_extreme(daystocover: pd.Series) -> pd.Series:
    """1 if daystocover > 10 — extreme squeeze-risk state."""
    d = daystocover.astype(float)
    return (d > 10.0).astype(float).where(d.notna(), np.nan)


def f48_ssat_010_shortpctfloat_level(shortpctfloat: pd.Series) -> pd.Series:
    """Short % of float — raw level."""
    return shortpctfloat.astype(float)


def f48_ssat_011_shortpctfloat_zscore_252(shortpctfloat: pd.Series) -> pd.Series:
    """Z-score of short % float vs 252d distribution."""
    return _rolling_zscore(shortpctfloat.astype(float), YDAYS, min_periods=QDAYS)


def f48_ssat_012_shortpctfloat_above_20_state(shortpctfloat: pd.Series) -> pd.Series:
    """1 if short % float > 20% — heavy short-float regime."""
    p = shortpctfloat.astype(float)
    return (p > 20.0).astype(float).where(p.notna(), np.nan)


def f48_ssat_013_shortpctfloat_above_30_extreme(shortpctfloat: pd.Series) -> pd.Series:
    """1 if short % float > 30% — extreme short-float regime (squeeze setup)."""
    p = shortpctfloat.astype(float)
    return (p > 30.0).astype(float).where(p.notna(), np.nan)


def f48_ssat_014_shortpctshares_level(shortpctshares: pd.Series) -> pd.Series:
    """Short % shares — raw level."""
    return shortpctshares.astype(float)


def f48_ssat_015_shortpctshares_zscore_252(shortpctshares: pd.Series) -> pd.Series:
    """Z-score of short % shares vs trailing 252d distribution."""
    return _rolling_zscore(shortpctshares.astype(float), YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket B — NSIR changes / post-squeeze unwind (016-025)
# ============================================================

def f48_ssat_016_si_change_21d_abs(shortinterest: pd.Series) -> pd.Series:
    """1-month absolute change in short interest."""
    return shortinterest.astype(float).diff(MDAYS)


def f48_ssat_017_si_change_63d_abs(shortinterest: pd.Series) -> pd.Series:
    """3-month absolute change in short interest."""
    return shortinterest.astype(float).diff(QDAYS)


def f48_ssat_018_si_decline_from_252d_max(shortinterest: pd.Series) -> pd.Series:
    """SI - trailing-252d-max — post-squeeze unwind size (<=0)."""
    s = shortinterest.astype(float)
    return s - s.rolling(YDAYS, min_periods=QDAYS).max()


def f48_ssat_019_bars_since_si_252d_max(shortinterest: pd.Series) -> pd.Series:
    """Bars since short-interest 252d max."""
    s = shortinterest.astype(float)
    return _bars_since_true(s == s.rolling(YDAYS, min_periods=QDAYS).max())


def f48_ssat_020_si_over_252d_max_ratio(shortinterest: pd.Series) -> pd.Series:
    """SI / trailing-252d-max — fraction of peak SI remaining (lower = more unwound)."""
    s = shortinterest.astype(float)
    return _safe_div(s, s.rolling(YDAYS, min_periods=QDAYS).max())


def f48_ssat_021_dtc_decline_from_252d_max(daystocover: pd.Series) -> pd.Series:
    """Days-to-cover decline from trailing 252d max."""
    d = daystocover.astype(float)
    return d - d.rolling(YDAYS, min_periods=QDAYS).max()


def f48_ssat_022_shortpctfloat_decline_from_252d_max(shortpctfloat: pd.Series) -> pd.Series:
    """Short %-float decline from trailing 252d max."""
    p = shortpctfloat.astype(float)
    return p - p.rolling(YDAYS, min_periods=QDAYS).max()


def f48_ssat_023_si_slope_63(shortinterest: pd.Series) -> pd.Series:
    """63d slope of short interest — quarterly SI momentum."""
    return _rolling_slope(shortinterest.astype(float), QDAYS)


def f48_ssat_024_shortpctfloat_slope_63(shortpctfloat: pd.Series) -> pd.Series:
    """63d slope of short %-float."""
    return _rolling_slope(shortpctfloat.astype(float), QDAYS)


def f48_ssat_025_si_net_change_252d(shortinterest: pd.Series) -> pd.Series:
    """Net change in short interest past 252d = current - 252-bars-ago."""
    s = shortinterest.astype(float)
    return s - s.shift(YDAYS)


# ============================================================
# Bucket C — Squeeze-event detection from price + vol (026-040)
# ============================================================

def f48_ssat_026_parabolic_63_ret_over_100pct_atr_expanded_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 63d return > 100% AND ATR21/ATR252 > 2 — parabolic-with-vol-expansion run."""
    r = close.pct_change(QDAYS)
    expansion = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS))
    return ((r > 1.0) & (expansion > 2.0)).astype(float).where(r.notna() & expansion.notna(), np.nan)


def f48_ssat_027_parabolic_252_ret_over_200pct_flag(close: pd.Series) -> pd.Series:
    """1 if 252d return > 200% — annual parabolic-run flag."""
    r = close.pct_change(YDAYS)
    return (r > 2.0).astype(float).where(r.notna(), np.nan)


def f48_ssat_028_bars_since_last_parabolic_run(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last parabolic-run flag fired."""
    r = close.pct_change(QDAYS)
    expansion = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS))
    return _bars_since_true((r > 1.0) & (expansion > 2.0))


def f48_ssat_029_parabolic_run_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of parabolic-run flags past 252 bars."""
    r = close.pct_change(QDAYS)
    expansion = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS))
    ev = ((r > 1.0) & (expansion > 2.0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)


def f48_ssat_030_peak_21d_return_past_252(close: pd.Series) -> pd.Series:
    """Max of 21d return over past 252 bars — peak monthly return amplitude."""
    return close.pct_change(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()


def f48_ssat_031_peak_21d_return_past_504(close: pd.Series) -> pd.Series:
    """Max of 21d return over past 504 bars — multi-year peak monthly return."""
    return close.pct_change(MDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).max()


def f48_ssat_032_explosion_bar_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if |1-bar return| > 4 * 21d ATR (in price units) — explosion bar."""
    a = _atr(high, low, close, MDAYS)
    move = (close - close.shift(1)).abs()
    return (move > 4.0 * a).astype(float).where(a.notna(), np.nan)


def f48_ssat_033_explosion_bar_count_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of explosion bars past 21."""
    a = _atr(high, low, close, MDAYS)
    move = (close - close.shift(1)).abs()
    return (move > 4.0 * a).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(a.notna(), np.nan)


def f48_ssat_034_explosion_bar_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of explosion bars past 63."""
    a = _atr(high, low, close, MDAYS)
    move = (close - close.shift(1)).abs()
    return (move > 4.0 * a).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(a.notna(), np.nan)


def f48_ssat_035_explosion_bar_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of explosion bars."""
    a = _atr(high, low, close, MDAYS)
    move = (close - close.shift(1)).abs()
    return (move > 4.0 * a).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(a.notna(), np.nan)


def f48_ssat_036_vertical_move_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 21d return > 100% AND volume > 5x 252d avg volume — vertical-move signature."""
    r = close.pct_change(MDAYS)
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    return ((r > 1.0) & (v_ratio > 5.0)).astype(float).where(r.notna() & v_ratio.notna(), np.nan)


def f48_ssat_037_vertical_move_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of vertical-move flags."""
    r = close.pct_change(MDAYS)
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    ev = ((r > 1.0) & (v_ratio > 5.0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna() & v_ratio.notna(), np.nan)


def f48_ssat_038_retest_sma200_after_100pct_run_flag(close: pd.Series) -> pd.Series:
    """1 if past-252d max return was >100% AND close currently <= SMA200 — base-retest after run."""
    r = close.pct_change(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    sma = _sma(close, 200)
    return ((r > 1.0) & (close <= sma)).astype(float).where(sma.notna(), np.nan)


def f48_ssat_039_days_at_252d_high_in_252(high: pd.Series) -> pd.Series:
    """Count of bars in past 252 where high equals its trailing 252d max — days-at-high frequency."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (high == rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(rmax.notna(), np.nan)


def f48_ssat_040_capitulation_bar_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 1-bar return < -3 * 21d ATR AND volume > 3x 21d avg — capitulation bar."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float).where(a.notna() & v_ratio.notna(), np.nan)


# ============================================================
# Bucket D — Post-squeeze price-collapse measures (041-055)
# ============================================================

def f48_ssat_041_drawdown_from_21d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """(close / 21d high) - 1 — short-term drawdown from monthly peak (<=0)."""
    return _safe_div(close, high.rolling(MDAYS, min_periods=WDAYS).max()) - 1.0


def f48_ssat_042_drawdown_from_63d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """(close / 63d high) - 1 — quarterly drawdown."""
    return _safe_div(close, high.rolling(QDAYS, min_periods=MDAYS).max()) - 1.0


def f48_ssat_043_drawdown_from_252d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """(close / 252d high) - 1 — annual drawdown (close to label target)."""
    return _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0


def f48_ssat_044_drawdown_from_504d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """(close / 504d high) - 1 — multi-year drawdown."""
    return _safe_div(close, high.rolling(DDAYS_2Y, min_periods=YDAYS).max()) - 1.0


def f48_ssat_045_dd_below_50pct_state(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if drawdown from 252d high <= -50% — moderate post-blowoff collapse."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (dd <= -0.5).astype(float).where(dd.notna(), np.nan)


def f48_ssat_046_dd_below_80pct_state(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if drawdown from 252d high <= -80% — deep collapse (label-adjacent observation)."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (dd <= -0.8).astype(float).where(dd.notna(), np.nan)


def f48_ssat_047_bars_since_21d_high(high: pd.Series) -> pd.Series:
    """Bars since most recent 21d high."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    return _bars_since_true(high == rmax)


def f48_ssat_048_bars_since_63d_high(high: pd.Series) -> pd.Series:
    """Bars since most recent 63d high."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return _bars_since_true(high == rmax)


def f48_ssat_049_bars_since_252d_high(high: pd.Series) -> pd.Series:
    """Bars since most recent 252d high — recency of annual peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(high == rmax)


def f48_ssat_050_dd_slope_21(high: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of drawdown-from-252d-high — short-term decay rate."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return _rolling_slope(dd, MDAYS)


def f48_ssat_051_dd_slope_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """63d slope of drawdown — quarterly decay rate."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return _rolling_slope(dd, QDAYS)


def f48_ssat_052_dd_acceleration(high: pd.Series, close: pd.Series) -> pd.Series:
    """2nd difference of drawdown — drawdown acceleration."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.diff().diff()


def f48_ssat_053_max_drawdown_velocity_21(high: pd.Series, close: pd.Series) -> pd.Series:
    """Most-negative 1-bar drawdown change in past 21 — deepest single-bar deterioration."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return dd.diff().rolling(MDAYS, min_periods=WDAYS).min()


def f48_ssat_054_largest_5d_decline_past_21(close: pd.Series) -> pd.Series:
    """Largest 5-day decline (min 5-bar return) in past 21 bars — peak crash speed."""
    return close.pct_change(WDAYS).rolling(MDAYS, min_periods=WDAYS).min()


def f48_ssat_055_largest_21d_decline_past_63(close: pd.Series) -> pd.Series:
    """Largest 21-day decline in past 63 — quarterly worst-month return."""
    return close.pct_change(MDAYS).rolling(QDAYS, min_periods=MDAYS).min()


# ============================================================
# Bucket E — Pre-collapse high-vol shake-outs / capitulation (056-068)
# ============================================================

def f48_ssat_056_capit_bar_count_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation-bar count past 21."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    ev = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float)
    return ev.rolling(MDAYS, min_periods=WDAYS).sum().where(a.notna() & v_ratio.notna(), np.nan)


def f48_ssat_057_capit_bar_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation-bar count past 63."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    ev = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(a.notna() & v_ratio.notna(), np.nan)


def f48_ssat_058_capit_bar_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of capitulation bars."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    ev = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(a.notna() & v_ratio.notna(), np.nan)


def f48_ssat_059_bars_since_last_capit_bar(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent capitulation bar."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return _bars_since_true((move < -3.0 * a) & (v_ratio > 3.0))


def f48_ssat_060_capit_cluster_3_in_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 3+ capitulation bars in past 21 — cluster warning."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    ev = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float)
    cnt = ev.rolling(MDAYS, min_periods=WDAYS).sum()
    return (cnt >= 3).astype(float).where(a.notna() & v_ratio.notna(), np.nan)


def f48_ssat_061_decline_20pct_flag(close: pd.Series) -> pd.Series:
    """1 if 1-bar return <= -20% — gap-down / panic flag."""
    r = close.pct_change()
    return (r <= -0.20).astype(float).where(r.notna(), np.nan)


def f48_ssat_062_decline_20pct_count_252(close: pd.Series) -> pd.Series:
    """Annual count of >=20% 1-bar declines."""
    r = close.pct_change()
    return (r <= -0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna(), np.nan)


def f48_ssat_063_bars_since_last_20pct_decline(close: pd.Series) -> pd.Series:
    """Bars since most recent >=20% 1-bar decline."""
    r = close.pct_change()
    return _bars_since_true(r <= -0.20)


def f48_ssat_064_cum_decline_past_21(close: pd.Series) -> pd.Series:
    """Sum of negative daily returns past 21 — monthly cumulative decline magnitude."""
    r = close.pct_change()
    return r.where(r < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()


def f48_ssat_065_cum_decline_past_63(close: pd.Series) -> pd.Series:
    """Sum of negative daily returns past 63 — quarterly cumulative decline."""
    r = close.pct_change()
    return r.where(r < 0, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()


def f48_ssat_066_cum_decline_past_252(close: pd.Series) -> pd.Series:
    """Annual sum of negative daily returns."""
    r = close.pct_change()
    return r.where(r < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f48_ssat_067_pos_minus_neg_ret_past_63(close: pd.Series) -> pd.Series:
    """Sum of positive returns minus |sum of negative| past 63 — net up-down magnitude."""
    r = close.pct_change()
    return r.where(r > 0, 0.0).rolling(QDAYS, min_periods=MDAYS).sum() - r.where(r < 0, 0.0).abs().rolling(QDAYS, min_periods=MDAYS).sum()


def f48_ssat_068_decline_day_frac_past_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with close < prev close — decline-day rate (quarterly)."""
    return (close < close.shift(1)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(close.shift(1).notna(), np.nan)


# ============================================================
# Bucket F — Volume during decline (069-075)
# ============================================================

def f48_ssat_069_down_vol_sum_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on down-close days past 21 — monthly down-vol."""
    dn = (close < close.shift(1)).astype(float)
    return (dn * volume).rolling(MDAYS, min_periods=WDAYS).sum().where(close.shift(1).notna(), np.nan)


def f48_ssat_070_down_vol_sum_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of down-close volume past 63 — quarterly down-vol."""
    dn = (close < close.shift(1)).astype(float)
    return (dn * volume).rolling(QDAYS, min_periods=MDAYS).sum().where(close.shift(1).notna(), np.nan)


def f48_ssat_071_down_over_up_vol_ratio_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-vol / up-vol past 21 — monthly down-pressure ratio."""
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    uv = (up * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    dv = (dn * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dv, uv)


def f48_ssat_072_down_over_up_vol_ratio_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-vol / up-vol past 63 — quarterly down-pressure ratio."""
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    uv = (up * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    dv = (dn * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dv, uv)


def f48_ssat_073_max_down_day_vol_over_median_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max down-day volume past 63 / median volume past 63 — peak down-day intensity."""
    dn_vol = volume.where(close < close.shift(1), np.nan)
    return _safe_div(dn_vol.rolling(QDAYS, min_periods=MDAYS).max(), volume.rolling(QDAYS, min_periods=MDAYS).median())


def f48_ssat_074_down_vol_on_dd_deepening(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on bars where drawdown deepened (dd < dd[t-1]) past 63 — deepening-pressure vol."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    cond = (dd < dd.shift(1)).astype(float)
    return (cond * volume).rolling(QDAYS, min_periods=MDAYS).sum().where(dd.notna(), np.nan)


def f48_ssat_075_capit_vol_spike_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if (vol > 3x 21d avg) AND (close < prev close) AND drawdown deepening — capitulation-vol-spike."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    cond = (v_ratio > 3.0) & (close < close.shift(1)) & (dd < dd.shift(1))
    return cond.astype(float).where(dd.notna() & v_ratio.notna(), np.nan)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

_HC = ["high", "close"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_CV = ["close", "volume"]
_HCV = ["high", "close", "volume"]

SHORT_SQUEEZE_AFTERMATH_TECHNICAL_BASE_REGISTRY_001_075 = {
    "f48_ssat_001_shortinterest_level": {"inputs": ["shortinterest"], "func": f48_ssat_001_shortinterest_level},
    "f48_ssat_002_shortinterest_zscore_252": {"inputs": ["shortinterest"], "func": f48_ssat_002_shortinterest_zscore_252},
    "f48_ssat_003_shortinterest_pct_change_21": {"inputs": ["shortinterest"], "func": f48_ssat_003_shortinterest_pct_change_21},
    "f48_ssat_004_shortinterest_pct_change_63": {"inputs": ["shortinterest"], "func": f48_ssat_004_shortinterest_pct_change_63},
    "f48_ssat_005_shortinterest_pct_rank_252": {"inputs": ["shortinterest"], "func": f48_ssat_005_shortinterest_pct_rank_252},
    "f48_ssat_006_daystocover_level": {"inputs": ["daystocover"], "func": f48_ssat_006_daystocover_level},
    "f48_ssat_007_daystocover_zscore_252": {"inputs": ["daystocover"], "func": f48_ssat_007_daystocover_zscore_252},
    "f48_ssat_008_daystocover_above_5_state": {"inputs": ["daystocover"], "func": f48_ssat_008_daystocover_above_5_state},
    "f48_ssat_009_daystocover_above_10_extreme": {"inputs": ["daystocover"], "func": f48_ssat_009_daystocover_above_10_extreme},
    "f48_ssat_010_shortpctfloat_level": {"inputs": ["shortpctfloat"], "func": f48_ssat_010_shortpctfloat_level},
    "f48_ssat_011_shortpctfloat_zscore_252": {"inputs": ["shortpctfloat"], "func": f48_ssat_011_shortpctfloat_zscore_252},
    "f48_ssat_012_shortpctfloat_above_20_state": {"inputs": ["shortpctfloat"], "func": f48_ssat_012_shortpctfloat_above_20_state},
    "f48_ssat_013_shortpctfloat_above_30_extreme": {"inputs": ["shortpctfloat"], "func": f48_ssat_013_shortpctfloat_above_30_extreme},
    "f48_ssat_014_shortpctshares_level": {"inputs": ["shortpctshares"], "func": f48_ssat_014_shortpctshares_level},
    "f48_ssat_015_shortpctshares_zscore_252": {"inputs": ["shortpctshares"], "func": f48_ssat_015_shortpctshares_zscore_252},
    "f48_ssat_016_si_change_21d_abs": {"inputs": ["shortinterest"], "func": f48_ssat_016_si_change_21d_abs},
    "f48_ssat_017_si_change_63d_abs": {"inputs": ["shortinterest"], "func": f48_ssat_017_si_change_63d_abs},
    "f48_ssat_018_si_decline_from_252d_max": {"inputs": ["shortinterest"], "func": f48_ssat_018_si_decline_from_252d_max},
    "f48_ssat_019_bars_since_si_252d_max": {"inputs": ["shortinterest"], "func": f48_ssat_019_bars_since_si_252d_max},
    "f48_ssat_020_si_over_252d_max_ratio": {"inputs": ["shortinterest"], "func": f48_ssat_020_si_over_252d_max_ratio},
    "f48_ssat_021_dtc_decline_from_252d_max": {"inputs": ["daystocover"], "func": f48_ssat_021_dtc_decline_from_252d_max},
    "f48_ssat_022_shortpctfloat_decline_from_252d_max": {"inputs": ["shortpctfloat"], "func": f48_ssat_022_shortpctfloat_decline_from_252d_max},
    "f48_ssat_023_si_slope_63": {"inputs": ["shortinterest"], "func": f48_ssat_023_si_slope_63},
    "f48_ssat_024_shortpctfloat_slope_63": {"inputs": ["shortpctfloat"], "func": f48_ssat_024_shortpctfloat_slope_63},
    "f48_ssat_025_si_net_change_252d": {"inputs": ["shortinterest"], "func": f48_ssat_025_si_net_change_252d},
    "f48_ssat_026_parabolic_63_ret_over_100pct_atr_expanded_flag": {"inputs": _HLC, "func": f48_ssat_026_parabolic_63_ret_over_100pct_atr_expanded_flag},
    "f48_ssat_027_parabolic_252_ret_over_200pct_flag": {"inputs": ["close"], "func": f48_ssat_027_parabolic_252_ret_over_200pct_flag},
    "f48_ssat_028_bars_since_last_parabolic_run": {"inputs": _HLC, "func": f48_ssat_028_bars_since_last_parabolic_run},
    "f48_ssat_029_parabolic_run_count_252": {"inputs": _HLC, "func": f48_ssat_029_parabolic_run_count_252},
    "f48_ssat_030_peak_21d_return_past_252": {"inputs": ["close"], "func": f48_ssat_030_peak_21d_return_past_252},
    "f48_ssat_031_peak_21d_return_past_504": {"inputs": ["close"], "func": f48_ssat_031_peak_21d_return_past_504},
    "f48_ssat_032_explosion_bar_flag": {"inputs": _HLC, "func": f48_ssat_032_explosion_bar_flag},
    "f48_ssat_033_explosion_bar_count_21": {"inputs": _HLC, "func": f48_ssat_033_explosion_bar_count_21},
    "f48_ssat_034_explosion_bar_count_63": {"inputs": _HLC, "func": f48_ssat_034_explosion_bar_count_63},
    "f48_ssat_035_explosion_bar_count_252": {"inputs": _HLC, "func": f48_ssat_035_explosion_bar_count_252},
    "f48_ssat_036_vertical_move_flag": {"inputs": _CV, "func": f48_ssat_036_vertical_move_flag},
    "f48_ssat_037_vertical_move_count_252": {"inputs": _CV, "func": f48_ssat_037_vertical_move_count_252},
    "f48_ssat_038_retest_sma200_after_100pct_run_flag": {"inputs": ["close"], "func": f48_ssat_038_retest_sma200_after_100pct_run_flag},
    "f48_ssat_039_days_at_252d_high_in_252": {"inputs": ["high"], "func": f48_ssat_039_days_at_252d_high_in_252},
    "f48_ssat_040_capitulation_bar_flag": {"inputs": _HLCV, "func": f48_ssat_040_capitulation_bar_flag},
    "f48_ssat_041_drawdown_from_21d_high": {"inputs": _HC, "func": f48_ssat_041_drawdown_from_21d_high},
    "f48_ssat_042_drawdown_from_63d_high": {"inputs": _HC, "func": f48_ssat_042_drawdown_from_63d_high},
    "f48_ssat_043_drawdown_from_252d_high": {"inputs": _HC, "func": f48_ssat_043_drawdown_from_252d_high},
    "f48_ssat_044_drawdown_from_504d_high": {"inputs": _HC, "func": f48_ssat_044_drawdown_from_504d_high},
    "f48_ssat_045_dd_below_50pct_state": {"inputs": _HC, "func": f48_ssat_045_dd_below_50pct_state},
    "f48_ssat_046_dd_below_80pct_state": {"inputs": _HC, "func": f48_ssat_046_dd_below_80pct_state},
    "f48_ssat_047_bars_since_21d_high": {"inputs": ["high"], "func": f48_ssat_047_bars_since_21d_high},
    "f48_ssat_048_bars_since_63d_high": {"inputs": ["high"], "func": f48_ssat_048_bars_since_63d_high},
    "f48_ssat_049_bars_since_252d_high": {"inputs": ["high"], "func": f48_ssat_049_bars_since_252d_high},
    "f48_ssat_050_dd_slope_21": {"inputs": _HC, "func": f48_ssat_050_dd_slope_21},
    "f48_ssat_051_dd_slope_63": {"inputs": _HC, "func": f48_ssat_051_dd_slope_63},
    "f48_ssat_052_dd_acceleration": {"inputs": _HC, "func": f48_ssat_052_dd_acceleration},
    "f48_ssat_053_max_drawdown_velocity_21": {"inputs": _HC, "func": f48_ssat_053_max_drawdown_velocity_21},
    "f48_ssat_054_largest_5d_decline_past_21": {"inputs": ["close"], "func": f48_ssat_054_largest_5d_decline_past_21},
    "f48_ssat_055_largest_21d_decline_past_63": {"inputs": ["close"], "func": f48_ssat_055_largest_21d_decline_past_63},
    "f48_ssat_056_capit_bar_count_21": {"inputs": _HLCV, "func": f48_ssat_056_capit_bar_count_21},
    "f48_ssat_057_capit_bar_count_63": {"inputs": _HLCV, "func": f48_ssat_057_capit_bar_count_63},
    "f48_ssat_058_capit_bar_count_252": {"inputs": _HLCV, "func": f48_ssat_058_capit_bar_count_252},
    "f48_ssat_059_bars_since_last_capit_bar": {"inputs": _HLCV, "func": f48_ssat_059_bars_since_last_capit_bar},
    "f48_ssat_060_capit_cluster_3_in_21": {"inputs": _HLCV, "func": f48_ssat_060_capit_cluster_3_in_21},
    "f48_ssat_061_decline_20pct_flag": {"inputs": ["close"], "func": f48_ssat_061_decline_20pct_flag},
    "f48_ssat_062_decline_20pct_count_252": {"inputs": ["close"], "func": f48_ssat_062_decline_20pct_count_252},
    "f48_ssat_063_bars_since_last_20pct_decline": {"inputs": ["close"], "func": f48_ssat_063_bars_since_last_20pct_decline},
    "f48_ssat_064_cum_decline_past_21": {"inputs": ["close"], "func": f48_ssat_064_cum_decline_past_21},
    "f48_ssat_065_cum_decline_past_63": {"inputs": ["close"], "func": f48_ssat_065_cum_decline_past_63},
    "f48_ssat_066_cum_decline_past_252": {"inputs": ["close"], "func": f48_ssat_066_cum_decline_past_252},
    "f48_ssat_067_pos_minus_neg_ret_past_63": {"inputs": ["close"], "func": f48_ssat_067_pos_minus_neg_ret_past_63},
    "f48_ssat_068_decline_day_frac_past_63": {"inputs": ["close"], "func": f48_ssat_068_decline_day_frac_past_63},
    "f48_ssat_069_down_vol_sum_21": {"inputs": _CV, "func": f48_ssat_069_down_vol_sum_21},
    "f48_ssat_070_down_vol_sum_63": {"inputs": _CV, "func": f48_ssat_070_down_vol_sum_63},
    "f48_ssat_071_down_over_up_vol_ratio_21": {"inputs": _CV, "func": f48_ssat_071_down_over_up_vol_ratio_21},
    "f48_ssat_072_down_over_up_vol_ratio_63": {"inputs": _CV, "func": f48_ssat_072_down_over_up_vol_ratio_63},
    "f48_ssat_073_max_down_day_vol_over_median_63": {"inputs": _CV, "func": f48_ssat_073_max_down_day_vol_over_median_63},
    "f48_ssat_074_down_vol_on_dd_deepening": {"inputs": _HCV, "func": f48_ssat_074_down_vol_on_dd_deepening},
    "f48_ssat_075_capit_vol_spike_flag": {"inputs": _HLCV, "func": f48_ssat_075_capit_vol_spike_flag},
}
