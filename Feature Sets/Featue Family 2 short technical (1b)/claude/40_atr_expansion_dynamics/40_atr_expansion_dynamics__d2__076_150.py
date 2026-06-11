"""atr_expansion_dynamics d2 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each feature
encodes a *different concept* in the ATR / true-range expansion theme:
gap-vs-intraday TR decomposition (cont), NATR regime durations, single-bar
TR shocks, sequential TR expansion, ATR-volume coupling, ATR-normalized MA
distance, cumulative range exhaustion, quartile-bar ATR splits, NATR shocks,
TR sign-direction descriptors, ATR persistence, ATR spike regimes, plus a
catch-all of misc ATR / TR descriptors.

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


def _longest_run(w: np.ndarray) -> float:
    m = 0; c = 0
    for v in w:
        if v > 0.5:
            c += 1; m = c if c > m else m
        else:
            c = 0
    return float(m)


# ============================================================
# Bucket M — Gap-vs-intraday TR decomposition (continued; 076-080)
# ============================================================

def f40_atxd_076_gap_share_of_tr_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (|open−prev_close| / TR) over 21d — gap share of true range."""
    tr = _true_range(high, low, close)
    g = (open - close.shift(1)).abs()
    return _safe_div(g, tr).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_077_gap_share_of_tr_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean gap share of TR over 252d — annual overnight share."""
    tr = _true_range(high, low, close)
    g = (open - close.shift(1)).abs()
    return _safe_div(g, tr).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_078_tr_component_asymmetry_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR-component asymmetry: mean (high−prev_close) − (prev_close−low), both clipped ≥0, over 63d."""
    pc = close.shift(1)
    up = (high - pc).clip(lower=0.0)
    dn = (pc - low).clip(lower=0.0)
    return (up - dn).rolling(QDAYS, min_periods=MDAYS).mean()


def f40_atxd_079_corr_gap_body_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr(|gap|, intraday range) — joint expansion coupling."""
    g = (open - close.shift(1)).abs()
    body = high - low
    return g.rolling(QDAYS, min_periods=MDAYS).corr(body)


def f40_atxd_080_overnight_variance_share_of_tr_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight variance share of TR: Σ gap² / Σ TR² over 63d."""
    g = (open - close.shift(1)).abs()
    tr = _true_range(high, low, close)
    return _safe_div((g ** 2).rolling(QDAYS, min_periods=MDAYS).sum(),
                     (tr ** 2).rolling(QDAYS, min_periods=MDAYS).sum())


# ============================================================
# Bucket N — NATR regime indicators (081-085)
# ============================================================

def _bars_since_event(ind: pd.Series) -> pd.Series:
    arr = ind.fillna(0).astype(int).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, x in enumerate(arr):
        if x:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=ind.index)


def f40_atxd_081_bars_since_natr21_above_p75(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since NATR(21) last exceeded its trailing-252d 75th percentile."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    p75 = n.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return _bars_since_event((n > p75).astype(float))


def f40_atxd_082_count_natr21_above_p75_transitions_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of NATR(21) crossings of 75th-pct over 63d."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    p75 = n.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    above = (n > p75).astype(float)
    return above.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_083_longest_run_natr21_above_p75_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of NATR(21) > trailing-252d 75th-pct within 252d window."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    p75 = n.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (n > p75).astype(float).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).apply(_longest_run, raw=True)


def f40_atxd_084_time_share_natr21_top_quartile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of time NATR(21) in top quartile of own past 252d distribution."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    p75 = n.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (n > p75).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_085_time_share_natr21_bottom_quartile_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of time NATR(21) in bottom quartile of own past 252d distribution."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    p25 = n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (n < p25).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket O — ATR shock magnitude (086-090)
# ============================================================

def f40_atxd_086_tr_over_mean_tr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR / mean(TR, last 21d) — single-bar TR shock relative to short baseline."""
    tr = _true_range(high, low, close)
    return _safe_div(tr, tr.rolling(MDAYS, min_periods=WDAYS).mean())


def f40_atxd_087_tr_over_mean_tr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR / mean(TR, last 63d) — single-bar TR shock vs intermediate baseline."""
    tr = _true_range(high, low, close)
    return _safe_div(tr, tr.rolling(QDAYS, min_periods=MDAYS).mean())


def f40_atxd_088_tr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR z-score within trailing 252d — single-bar TR shock in σ_TR units."""
    return _rolling_zscore(_true_range(high, low, close), YDAYS)


def f40_atxd_089_zscore_tr_over_mean21_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (TR / mean_TR_21d) within trailing 252d distribution."""
    tr = _true_range(high, low, close)
    return _rolling_zscore(_safe_div(tr, tr.rolling(MDAYS, min_periods=WDAYS).mean()), YDAYS)


def f40_atxd_090_max_tr_over_mean21_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max of (TR / mean_TR_21d) within trailing 63d — peak single-bar TR shock."""
    tr = _true_range(high, low, close)
    return _safe_div(tr, tr.rolling(MDAYS, min_periods=WDAYS).mean()).rolling(QDAYS, min_periods=MDAYS).max()


# ============================================================
# Bucket P — Sequential bar expansion (091-095)
# ============================================================

def f40_atxd_091_longest_tr_increase_run_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of consecutive TR-increases within 63d window."""
    tr = _true_range(high, low, close)
    up = (tr > tr.shift(1)).astype(float).fillna(0.0)
    return up.rolling(QDAYS, min_periods=MDAYS).apply(_longest_run, raw=True)


def f40_atxd_092_longest_tr_decrease_run_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of consecutive TR-decreases within 63d window."""
    tr = _true_range(high, low, close)
    dn = (tr < tr.shift(1)).astype(float).fillna(0.0)
    return dn.rolling(QDAYS, min_periods=MDAYS).apply(_longest_run, raw=True)


def f40_atxd_093_count_tr_increases_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of TR-increase bars (TR > TR.shift(1)) within 21d."""
    tr = _true_range(high, low, close)
    return (tr > tr.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f40_atxd_094_mean_runlength_tr_expansions_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean run-length of consecutive TR-expansion streaks within 252d."""
    tr = _true_range(high, low, close)
    up = (tr > tr.shift(1)).astype(float).fillna(0.0)

    def _mean_run(w):
        runs = []
        cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
            elif cur > 0:
                runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        return float(np.mean(runs)) if runs else np.nan
    return up.rolling(YDAYS, min_periods=QDAYS).apply(_mean_run, raw=True)


def f40_atxd_095_total_abs_tr_change_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ |TR.diff()| over 63d — TR-instability total variation."""
    tr = _true_range(high, low, close)
    return tr.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket Q — ATR-volume coupling (096-100)
# ============================================================

def f40_atxd_096_corr_atr21_logvol_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr(ATR(21), log(volume)) — short-horizon ATR-volume coupling."""
    return _atr(high, low, close, MDAYS).rolling(QDAYS, min_periods=MDAYS).corr(_safe_log(volume))


def f40_atxd_097_corr_atr21_logvol_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr(ATR(21), log(volume)) — annual ATR-volume coupling."""
    return _atr(high, low, close, MDAYS).rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(volume))


def f40_atxd_098_atr21_on_high_vs_low_vol_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio ATR(21) on high-vol (vz>1) vs low-vol (vz<−1) days within 252d."""
    a = _atr(high, low, close, MDAYS)
    vz = _rolling_zscore(volume, QDAYS)
    hi = a.where(vz > 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    lo = a.where(vz < -1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(hi, lo)


def f40_atxd_099_corr_natr21_volz_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr(NATR(21), volume z-score)."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    return n.rolling(YDAYS, min_periods=QDAYS).corr(_rolling_zscore(volume, QDAYS))


def f40_atxd_100_count_atr_p75_and_volz_above_1_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count bars where ATR(21) > 252d p75 AND vol_z > 1, within 63d (joint expansion)."""
    a = _atr(high, low, close, MDAYS)
    p75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    vz = _rolling_zscore(volume, QDAYS)
    return ((a > p75) & (vz > 1.0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket R — ATR-normalized distance from MA (101-105)
# ============================================================

def f40_atxd_101_atr21_norm_dist_sma21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|close − SMA(21)| / ATR(21) — short-horizon ATR-normalized MA-distance."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div((close - sma).abs(), _atr(high, low, close, MDAYS))


def f40_atxd_102_atr21_norm_dist_sma63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|close − SMA(63)| / ATR(21) — intermediate-horizon ATR-normalized MA-distance."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div((close - sma).abs(), _atr(high, low, close, MDAYS))


def f40_atxd_103_atr21_norm_dist_sma252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|close − SMA(252)| / ATR(21) — annual ATR-normalized MA-distance."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div((close - sma).abs(), _atr(high, low, close, MDAYS))


def f40_atxd_104_std_atr21_norm_dist_sma21_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d std of ATR-normalized |close − SMA(21)| — distance-instability."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    d = _safe_div((close - sma).abs(), _atr(high, low, close, MDAYS))
    return d.rolling(QDAYS, min_periods=MDAYS).std()


def f40_atxd_105_max_atr21_norm_dist_sma21_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max ATR-normalized |close − SMA(21)| within 63d — peak ATR-normalized stretch."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    d = _safe_div((close - sma).abs(), _atr(high, low, close, MDAYS))
    return d.rolling(QDAYS, min_periods=MDAYS).max()


# ============================================================
# Bucket S — Cumulative range exhaustion (106-110)
# ============================================================

def f40_atxd_106_sum_tr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ TR over 21d — cumulative range short-horizon."""
    return _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).sum()


def f40_atxd_107_sum_tr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ TR over 63d — cumulative range intermediate."""
    return _true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_108_sum_tr_252d_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ TR over 252d / close — annual cumulative range per dollar of price."""
    return _safe_div(_true_range(high, low, close).rolling(YDAYS, min_periods=QDAYS).sum(), close)


def f40_atxd_109_ratio_sum_tr_21_over_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ TR over 21d / Σ TR over 252d — short-vs-annual cumulative range ratio."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.rolling(MDAYS, min_periods=WDAYS).sum(),
                     tr.rolling(YDAYS, min_periods=QDAYS).sum())


def f40_atxd_110_log_ratio_sum_tr_21_over_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(Σ TR over 21d / Σ TR over 252d)."""
    tr = _true_range(high, low, close)
    return _safe_log(tr.rolling(MDAYS, min_periods=WDAYS).sum()) - _safe_log(tr.rolling(YDAYS, min_periods=QDAYS).sum())


# ============================================================
# Bucket T — Quartile-bar ATR splits (111-114)
# ============================================================

def f40_atxd_111_atr_on_top_quartile_tr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR restricted to top-quartile-TR bars within 63d — large-bar ATR."""
    tr = _true_range(high, low, close)
    p75 = tr.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    return tr.where(tr > p75, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f40_atxd_112_atr_on_bottom_quartile_tr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR restricted to bottom-quartile-TR bars within 63d — small-bar ATR."""
    tr = _true_range(high, low, close)
    p25 = tr.rolling(QDAYS, min_periods=MDAYS).quantile(0.25)
    return tr.where(tr < p25, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f40_atxd_113_ratio_large_small_bar_atr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of large-bar ATR / small-bar ATR within 63d — range concentration."""
    tr = _true_range(high, low, close)
    p25 = tr.rolling(QDAYS, min_periods=MDAYS).quantile(0.25)
    p75 = tr.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    large = tr.where(tr > p75, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    small = tr.where(tr < p25, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(large, small)


def f40_atxd_114_diff_large_small_bar_atr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Difference of large-bar ATR − small-bar ATR within 63d."""
    tr = _true_range(high, low, close)
    p25 = tr.rolling(QDAYS, min_periods=MDAYS).quantile(0.25)
    p75 = tr.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    large = tr.where(tr > p75, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    small = tr.where(tr < p25, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    return large - small


# ============================================================
# Bucket U — NATR shocks / extremes (115-119)
# ============================================================

def f40_atxd_115_natr21_change_lag21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Monthly NATR(21) Δ: NATR(21) − NATR(21).shift(21)."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    return n - n.shift(MDAYS)


def f40_atxd_116_natr21_pct_change_lag63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Quarterly relative NATR(21) change."""
    return _safe_div(_atr(high, low, close, MDAYS), close).pct_change(QDAYS)


def f40_atxd_117_natr21_pct_change_lag252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual relative NATR(21) change."""
    return _safe_div(_atr(high, low, close, MDAYS), close).pct_change(YDAYS)


def f40_atxd_118_natr21_range_max_min_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual NATR(21) range: max − min over 252d."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    return n.rolling(YDAYS, min_periods=QDAYS).max() - n.rolling(YDAYS, min_periods=QDAYS).min()


def f40_atxd_119_natr21_over_rollmean_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(21) / rolling 1260d mean of NATR(21) — multi-year normalization."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    return _safe_div(n, n.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).mean())


# ============================================================
# Bucket V — TR sign-direction descriptors (120-124)
# ============================================================

def f40_atxd_120_skew_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d skew of TR — range distribution asymmetry."""
    return _true_range(high, low, close).rolling(YDAYS, min_periods=QDAYS).skew()


def f40_atxd_121_kurt_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d kurtosis of TR — range tail-heaviness."""
    return _true_range(high, low, close).rolling(YDAYS, min_periods=QDAYS).kurt()


def f40_atxd_122_freq_tr_above_lag_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars where TR > TR.shift(1) within 63d — upward-TR frequency."""
    tr = _true_range(high, low, close)
    return (tr > tr.shift(1)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f40_atxd_123_cumulative_tr_diff_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ TR.diff() over 63d — signed cumulative TR change."""
    return _true_range(high, low, close).diff().rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_124_autocorr_tr_diff_lag1_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr(ΔTR_t, ΔTR_{t-1}) — TR-momentum persistence."""
    d = _true_range(high, low, close).diff()
    return d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(1))


# ============================================================
# Bucket W — ATR persistence (125-129)
# ============================================================

def f40_atxd_125_ar1_atr21_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coef of ATR(21) over 252d via rolling corr(ATR_t, ATR_{t-1})."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(1))


def f40_atxd_126_ar1_natr21_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coef of NATR(21) over 252d."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    return n.rolling(YDAYS, min_periods=QDAYS).corr(n.shift(1))


def f40_atxd_127_halflife_atr_shock_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Half-life of ATR(21) shock implied by AR(1) coef over 252d (clipped 0..200)."""
    a = _atr(high, low, close, MDAYS)
    rho = a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(1))
    ar = rho.abs().clip(upper=0.99, lower=1e-3)
    hl = -np.log(2.0) / np.log(ar)
    return hl.clip(upper=200.0)


def f40_atxd_128_autocorr_atr21_lag5_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr(ATR(21)_t, ATR(21)_{t-5}) — weekly-lag ATR persistence."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(WDAYS))


def f40_atxd_129_autocorr_atr21_lag21_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 504d corr(ATR(21)_t, ATR(21)_{t-21}) — monthly-lag ATR persistence."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(DDAYS_2Y, min_periods=YDAYS).corr(a.shift(MDAYS))


# ============================================================
# Bucket X — ATR spike events / regime triggers (130-134)
# ============================================================

def f40_atxd_130_count_atr21_above_15x_atr63_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(21) > 1.5·ATR(63) within 63d — moderate-spike event count."""
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    return (a21 > 1.5 * a63).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_131_bars_since_atr5_above_2x_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bar where ATR(5) > 2·ATR(63) — vol-spike recency."""
    a5 = _atr(high, low, close, WDAYS)
    a63 = _atr(high, low, close, QDAYS)
    return _bars_since_event((a5 > 2 * a63).astype(float))


def f40_atxd_132_count_natr21_above_2x_natr252_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where NATR(21) > 2·NATR(252) within 252d — extreme NATR-spike events."""
    n21 = _safe_div(_atr(high, low, close, MDAYS), close)
    n252 = _safe_div(_atr(high, low, close, YDAYS), close)
    return (n21 > 2 * n252).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_133_peak_atr5_over_atr252_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max of (ATR(5)/ATR(252)) within 63d — peak fast-vs-annual expansion."""
    return _safe_div(_atr(high, low, close, WDAYS), _atr(high, low, close, YDAYS)).rolling(QDAYS, min_periods=MDAYS).max()


def f40_atxd_134_longest_atr21_above_p75_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of ATR(21) > trailing-252d p75 within 252d window."""
    a = _atr(high, low, close, MDAYS)
    p75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (a > p75).astype(float).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).apply(_longest_run, raw=True)


# ============================================================
# Bucket Y — Misc ATR / TR descriptors (135-150)
# ============================================================

def f40_atxd_135_ratio_mean_tr_high_vs_low_vol_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio mean TR on top-decile-volume vs bottom-decile-volume bars over 252d."""
    tr = _true_range(high, low, close)
    pv90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    pv10 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    hi = tr.where(volume > pv90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    lo = tr.where(volume < pv10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(hi, lo)


def f40_atxd_136_cv_atr21_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CV (std/mean) of ATR(21) over 504d — multi-year coefficient of variation."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a.rolling(DDAYS_2Y, min_periods=YDAYS).std(),
                     a.rolling(DDAYS_2Y, min_periods=YDAYS).mean())


def f40_atxd_137_current_atr21_rising_run_length(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Length of current consecutive ATR(21)-rising run (positive integers; reset on decrease)."""
    a = _atr(high, low, close, MDAYS)
    up = (a > a.shift(1)).astype(int).fillna(0).values
    out = np.zeros(len(up), dtype=float)
    cur = 0
    for i, v in enumerate(up):
        cur = cur + 1 if v == 1 else 0
        out[i] = cur
    return pd.Series(out, index=close.index)


def f40_atxd_138_centered_pctrank_atr21_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Centered ATR(21) percentile rank: (rank − 0.5) over 252d → −0.5..+0.5."""
    a = _atr(high, low, close, MDAYS)
    rk = a.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan,
        raw=True,
    )
    return rk - 0.5


def f40_atxd_139_current_atr21_top_decile_dwell(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Length of current consecutive ATR(21)-in-top-decile-of-252d run."""
    a = _atr(high, low, close, MDAYS)
    p90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    inc = (a > p90).astype(int).fillna(0).values
    out = np.zeros(len(inc), dtype=float)
    cur = 0
    for i, v in enumerate(inc):
        cur = cur + 1 if v == 1 else 0
        out[i] = cur
    return pd.Series(out, index=close.index)


def f40_atxd_140_range_of_natr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range of NATR(21) z-score within 252d: max(z) − min(z)."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    z = _rolling_zscore(n, YDAYS)
    return z.rolling(YDAYS, min_periods=QDAYS).max() - z.rolling(YDAYS, min_periods=QDAYS).min()


def f40_atxd_141_zscore_range_252d_dispersion(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of intraday (high−low) within trailing 252d — single-bar dispersion shock."""
    return _rolling_zscore(high - low, YDAYS)


def f40_atxd_142_slope_atr_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d slope of (ATR(21)/ATR(21).shift(63)) ratio — ATR-momentum trend."""
    a = _atr(high, low, close, MDAYS)
    return _rolling_slope(_safe_div(a, a.shift(QDAYS)), QDAYS)


def f40_atxd_143_atr_acceleration_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21d mean of ATR(21).diff().diff() — short-horizon ATR acceleration."""
    a = _atr(high, low, close, MDAYS)
    return a.diff().diff().rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_144_natr_acceleration_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21d mean of NATR(21).diff().diff() — NATR acceleration."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    return n.diff().diff().rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_145_count_atr21_jump_15x_lag_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of single-bar ATR(21) jumps (ATR > 1.5·ATR.shift(1)) within 63d."""
    a = _atr(high, low, close, MDAYS)
    return (a > 1.5 * a.shift(1)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_146_count_tr_above_3xlag_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of single-bar TR shocks (TR > 3·TR.shift(1)) within 252d."""
    tr = _true_range(high, low, close)
    return (tr > 3 * tr.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_147_autocorr_tr_lag5_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr(TR_t, TR_{t-5}) — weekly-lag TR persistence."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(WDAYS))


def f40_atxd_148_hill_atr21_top10_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hill estimator (top 10%) of ATR(21) distribution over 1260d — heavy-tailed vol regime."""
    a = _atr(high, low, close, MDAYS)

    def _hill(w):
        arr = w[~np.isnan(w)]
        if len(arr) < 60:
            return np.nan
        k = max(int(len(arr) * 0.10), 5)
        top = np.sort(arr)[-k:]
        th = top[0]
        if th <= 0:
            return np.nan
        lg = np.log(top / th)
        val = lg[1:].mean() if len(lg) > 1 else np.nan
        return float(val) if np.isfinite(val) and val > 0 else np.nan
    return a.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).apply(_hill, raw=True)


def f40_atxd_149_skew_atr21_504d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 504d skew of ATR(21) distribution."""
    return _atr(high, low, close, MDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).skew()


def f40_atxd_150_tr_theil_concentration_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR concentration: Σ TR² / (Σ TR)² over 252d — Theil-style range concentration index."""
    tr = _true_range(high, low, close)
    s2 = (tr ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    s = tr.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(s2, s ** 2)


# ============================================================
#                         REGISTRY 076-150
# ============================================================



def f40_atxd_076_gap_share_of_tr_21d_d2(open, high, low, close):
    return f40_atxd_076_gap_share_of_tr_21d(open, high, low, close).diff().diff()


def f40_atxd_077_gap_share_of_tr_252d_d2(open, high, low, close):
    return f40_atxd_077_gap_share_of_tr_252d(open, high, low, close).diff().diff()


def f40_atxd_078_tr_component_asymmetry_63d_d2(high, low, close):
    return f40_atxd_078_tr_component_asymmetry_63d(high, low, close).diff().diff()


def f40_atxd_079_corr_gap_body_63d_d2(open, high, low, close):
    return f40_atxd_079_corr_gap_body_63d(open, high, low, close).diff().diff()


def f40_atxd_080_overnight_variance_share_of_tr_63d_d2(open, high, low, close):
    return f40_atxd_080_overnight_variance_share_of_tr_63d(open, high, low, close).diff().diff()


def f40_atxd_081_bars_since_natr21_above_p75_d2(high, low, close):
    return f40_atxd_081_bars_since_natr21_above_p75(high, low, close).diff().diff()


def f40_atxd_082_count_natr21_above_p75_transitions_63d_d2(high, low, close):
    return f40_atxd_082_count_natr21_above_p75_transitions_63d(high, low, close).diff().diff()


def f40_atxd_083_longest_run_natr21_above_p75_252d_d2(high, low, close):
    return f40_atxd_083_longest_run_natr21_above_p75_252d(high, low, close).diff().diff()


def f40_atxd_084_time_share_natr21_top_quartile_252d_d2(high, low, close):
    return f40_atxd_084_time_share_natr21_top_quartile_252d(high, low, close).diff().diff()


def f40_atxd_085_time_share_natr21_bottom_quartile_252d_d2(high, low, close):
    return f40_atxd_085_time_share_natr21_bottom_quartile_252d(high, low, close).diff().diff()


def f40_atxd_086_tr_over_mean_tr_21d_d2(high, low, close):
    return f40_atxd_086_tr_over_mean_tr_21d(high, low, close).diff().diff()


def f40_atxd_087_tr_over_mean_tr_63d_d2(high, low, close):
    return f40_atxd_087_tr_over_mean_tr_63d(high, low, close).diff().diff()


def f40_atxd_088_tr_zscore_252d_d2(high, low, close):
    return f40_atxd_088_tr_zscore_252d(high, low, close).diff().diff()


def f40_atxd_089_zscore_tr_over_mean21_252d_d2(high, low, close):
    return f40_atxd_089_zscore_tr_over_mean21_252d(high, low, close).diff().diff()


def f40_atxd_090_max_tr_over_mean21_63d_d2(high, low, close):
    return f40_atxd_090_max_tr_over_mean21_63d(high, low, close).diff().diff()


def f40_atxd_091_longest_tr_increase_run_63d_d2(high, low, close):
    return f40_atxd_091_longest_tr_increase_run_63d(high, low, close).diff().diff()


def f40_atxd_092_longest_tr_decrease_run_63d_d2(high, low, close):
    return f40_atxd_092_longest_tr_decrease_run_63d(high, low, close).diff().diff()


def f40_atxd_093_count_tr_increases_21d_d2(high, low, close):
    return f40_atxd_093_count_tr_increases_21d(high, low, close).diff().diff()


def f40_atxd_094_mean_runlength_tr_expansions_252d_d2(high, low, close):
    return f40_atxd_094_mean_runlength_tr_expansions_252d(high, low, close).diff().diff()


def f40_atxd_095_total_abs_tr_change_63d_d2(high, low, close):
    return f40_atxd_095_total_abs_tr_change_63d(high, low, close).diff().diff()


def f40_atxd_096_corr_atr21_logvol_63d_d2(high, low, close, volume):
    return f40_atxd_096_corr_atr21_logvol_63d(high, low, close, volume).diff().diff()


def f40_atxd_097_corr_atr21_logvol_252d_d2(high, low, close, volume):
    return f40_atxd_097_corr_atr21_logvol_252d(high, low, close, volume).diff().diff()


def f40_atxd_098_atr21_on_high_vs_low_vol_252d_d2(high, low, close, volume):
    return f40_atxd_098_atr21_on_high_vs_low_vol_252d(high, low, close, volume).diff().diff()


def f40_atxd_099_corr_natr21_volz_252d_d2(high, low, close, volume):
    return f40_atxd_099_corr_natr21_volz_252d(high, low, close, volume).diff().diff()


def f40_atxd_100_count_atr_p75_and_volz_above_1_63d_d2(high, low, close, volume):
    return f40_atxd_100_count_atr_p75_and_volz_above_1_63d(high, low, close, volume).diff().diff()


def f40_atxd_101_atr21_norm_dist_sma21_d2(high, low, close):
    return f40_atxd_101_atr21_norm_dist_sma21(high, low, close).diff().diff()


def f40_atxd_102_atr21_norm_dist_sma63_d2(high, low, close):
    return f40_atxd_102_atr21_norm_dist_sma63(high, low, close).diff().diff()


def f40_atxd_103_atr21_norm_dist_sma252_d2(high, low, close):
    return f40_atxd_103_atr21_norm_dist_sma252(high, low, close).diff().diff()


def f40_atxd_104_std_atr21_norm_dist_sma21_63d_d2(high, low, close):
    return f40_atxd_104_std_atr21_norm_dist_sma21_63d(high, low, close).diff().diff()


def f40_atxd_105_max_atr21_norm_dist_sma21_63d_d2(high, low, close):
    return f40_atxd_105_max_atr21_norm_dist_sma21_63d(high, low, close).diff().diff()


def f40_atxd_106_sum_tr_21d_d2(high, low, close):
    return f40_atxd_106_sum_tr_21d(high, low, close).diff().diff()


def f40_atxd_107_sum_tr_63d_d2(high, low, close):
    return f40_atxd_107_sum_tr_63d(high, low, close).diff().diff()


def f40_atxd_108_sum_tr_252d_over_close_d2(high, low, close):
    return f40_atxd_108_sum_tr_252d_over_close(high, low, close).diff().diff()


def f40_atxd_109_ratio_sum_tr_21_over_252_d2(high, low, close):
    return f40_atxd_109_ratio_sum_tr_21_over_252(high, low, close).diff().diff()


def f40_atxd_110_log_ratio_sum_tr_21_over_252_d2(high, low, close):
    return f40_atxd_110_log_ratio_sum_tr_21_over_252(high, low, close).diff().diff()


def f40_atxd_111_atr_on_top_quartile_tr_63d_d2(high, low, close):
    return f40_atxd_111_atr_on_top_quartile_tr_63d(high, low, close).diff().diff()


def f40_atxd_112_atr_on_bottom_quartile_tr_63d_d2(high, low, close):
    return f40_atxd_112_atr_on_bottom_quartile_tr_63d(high, low, close).diff().diff()


def f40_atxd_113_ratio_large_small_bar_atr_63d_d2(high, low, close):
    return f40_atxd_113_ratio_large_small_bar_atr_63d(high, low, close).diff().diff()


def f40_atxd_114_diff_large_small_bar_atr_63d_d2(high, low, close):
    return f40_atxd_114_diff_large_small_bar_atr_63d(high, low, close).diff().diff()


def f40_atxd_115_natr21_change_lag21_d2(high, low, close):
    return f40_atxd_115_natr21_change_lag21(high, low, close).diff().diff()


def f40_atxd_116_natr21_pct_change_lag63_d2(high, low, close):
    return f40_atxd_116_natr21_pct_change_lag63(high, low, close).diff().diff()


def f40_atxd_117_natr21_pct_change_lag252_d2(high, low, close):
    return f40_atxd_117_natr21_pct_change_lag252(high, low, close).diff().diff()


def f40_atxd_118_natr21_range_max_min_252d_d2(high, low, close):
    return f40_atxd_118_natr21_range_max_min_252d(high, low, close).diff().diff()


def f40_atxd_119_natr21_over_rollmean_1260d_d2(high, low, close):
    return f40_atxd_119_natr21_over_rollmean_1260d(high, low, close).diff().diff()


def f40_atxd_120_skew_tr_252d_d2(high, low, close):
    return f40_atxd_120_skew_tr_252d(high, low, close).diff().diff()


def f40_atxd_121_kurt_tr_252d_d2(high, low, close):
    return f40_atxd_121_kurt_tr_252d(high, low, close).diff().diff()


def f40_atxd_122_freq_tr_above_lag_63d_d2(high, low, close):
    return f40_atxd_122_freq_tr_above_lag_63d(high, low, close).diff().diff()


def f40_atxd_123_cumulative_tr_diff_63d_d2(high, low, close):
    return f40_atxd_123_cumulative_tr_diff_63d(high, low, close).diff().diff()


def f40_atxd_124_autocorr_tr_diff_lag1_252d_d2(high, low, close):
    return f40_atxd_124_autocorr_tr_diff_lag1_252d(high, low, close).diff().diff()


def f40_atxd_125_ar1_atr21_252d_d2(high, low, close):
    return f40_atxd_125_ar1_atr21_252d(high, low, close).diff().diff()


def f40_atxd_126_ar1_natr21_252d_d2(high, low, close):
    return f40_atxd_126_ar1_natr21_252d(high, low, close).diff().diff()


def f40_atxd_127_halflife_atr_shock_252d_d2(high, low, close):
    return f40_atxd_127_halflife_atr_shock_252d(high, low, close).diff().diff()


def f40_atxd_128_autocorr_atr21_lag5_252d_d2(high, low, close):
    return f40_atxd_128_autocorr_atr21_lag5_252d(high, low, close).diff().diff()


def f40_atxd_129_autocorr_atr21_lag21_504d_d2(high, low, close):
    return f40_atxd_129_autocorr_atr21_lag21_504d(high, low, close).diff().diff()


def f40_atxd_130_count_atr21_above_15x_atr63_63d_d2(high, low, close):
    return f40_atxd_130_count_atr21_above_15x_atr63_63d(high, low, close).diff().diff()


def f40_atxd_131_bars_since_atr5_above_2x_atr63_d2(high, low, close):
    return f40_atxd_131_bars_since_atr5_above_2x_atr63(high, low, close).diff().diff()


def f40_atxd_132_count_natr21_above_2x_natr252_252d_d2(high, low, close):
    return f40_atxd_132_count_natr21_above_2x_natr252_252d(high, low, close).diff().diff()


def f40_atxd_133_peak_atr5_over_atr252_63d_d2(high, low, close):
    return f40_atxd_133_peak_atr5_over_atr252_63d(high, low, close).diff().diff()


def f40_atxd_134_longest_atr21_above_p75_252d_d2(high, low, close):
    return f40_atxd_134_longest_atr21_above_p75_252d(high, low, close).diff().diff()


def f40_atxd_135_ratio_mean_tr_high_vs_low_vol_252d_d2(high, low, close, volume):
    return f40_atxd_135_ratio_mean_tr_high_vs_low_vol_252d(high, low, close, volume).diff().diff()


def f40_atxd_136_cv_atr21_504d_d2(high, low, close):
    return f40_atxd_136_cv_atr21_504d(high, low, close).diff().diff()


def f40_atxd_137_current_atr21_rising_run_length_d2(high, low, close):
    return f40_atxd_137_current_atr21_rising_run_length(high, low, close).diff().diff()


def f40_atxd_138_centered_pctrank_atr21_252d_d2(high, low, close):
    return f40_atxd_138_centered_pctrank_atr21_252d(high, low, close).diff().diff()


def f40_atxd_139_current_atr21_top_decile_dwell_d2(high, low, close):
    return f40_atxd_139_current_atr21_top_decile_dwell(high, low, close).diff().diff()


def f40_atxd_140_range_of_natr_zscore_252d_d2(high, low, close):
    return f40_atxd_140_range_of_natr_zscore_252d(high, low, close).diff().diff()


def f40_atxd_141_zscore_range_252d_dispersion_d2(high, low):
    return f40_atxd_141_zscore_range_252d_dispersion(high, low).diff().diff()


def f40_atxd_142_slope_atr_ratio_63d_d2(high, low, close):
    return f40_atxd_142_slope_atr_ratio_63d(high, low, close).diff().diff()


def f40_atxd_143_atr_acceleration_21d_d2(high, low, close):
    return f40_atxd_143_atr_acceleration_21d(high, low, close).diff().diff()


def f40_atxd_144_natr_acceleration_21d_d2(high, low, close):
    return f40_atxd_144_natr_acceleration_21d(high, low, close).diff().diff()


def f40_atxd_145_count_atr21_jump_15x_lag_63d_d2(high, low, close):
    return f40_atxd_145_count_atr21_jump_15x_lag_63d(high, low, close).diff().diff()


def f40_atxd_146_count_tr_above_3xlag_252d_d2(high, low, close):
    return f40_atxd_146_count_tr_above_3xlag_252d(high, low, close).diff().diff()


def f40_atxd_147_autocorr_tr_lag5_252d_d2(high, low, close):
    return f40_atxd_147_autocorr_tr_lag5_252d(high, low, close).diff().diff()


def f40_atxd_148_hill_atr21_top10_1260d_d2(high, low, close):
    return f40_atxd_148_hill_atr21_top10_1260d(high, low, close).diff().diff()


def f40_atxd_149_skew_atr21_504d_d2(high, low, close):
    return f40_atxd_149_skew_atr21_504d(high, low, close).diff().diff()


def f40_atxd_150_tr_theil_concentration_252d_d2(high, low, close):
    return f40_atxd_150_tr_theil_concentration_252d(high, low, close).diff().diff()


ATR_EXPANSION_DYNAMICS_D2_REGISTRY_076_150 = {
    "f40_atxd_076_gap_share_of_tr_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_076_gap_share_of_tr_21d_d2},
    "f40_atxd_077_gap_share_of_tr_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_077_gap_share_of_tr_252d_d2},
    "f40_atxd_078_tr_component_asymmetry_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_078_tr_component_asymmetry_63d_d2},
    "f40_atxd_079_corr_gap_body_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_079_corr_gap_body_63d_d2},
    "f40_atxd_080_overnight_variance_share_of_tr_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_080_overnight_variance_share_of_tr_63d_d2},
    "f40_atxd_081_bars_since_natr21_above_p75_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_081_bars_since_natr21_above_p75_d2},
    "f40_atxd_082_count_natr21_above_p75_transitions_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_082_count_natr21_above_p75_transitions_63d_d2},
    "f40_atxd_083_longest_run_natr21_above_p75_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_083_longest_run_natr21_above_p75_252d_d2},
    "f40_atxd_084_time_share_natr21_top_quartile_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_084_time_share_natr21_top_quartile_252d_d2},
    "f40_atxd_085_time_share_natr21_bottom_quartile_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_085_time_share_natr21_bottom_quartile_252d_d2},
    "f40_atxd_086_tr_over_mean_tr_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_086_tr_over_mean_tr_21d_d2},
    "f40_atxd_087_tr_over_mean_tr_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_087_tr_over_mean_tr_63d_d2},
    "f40_atxd_088_tr_zscore_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_088_tr_zscore_252d_d2},
    "f40_atxd_089_zscore_tr_over_mean21_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_089_zscore_tr_over_mean21_252d_d2},
    "f40_atxd_090_max_tr_over_mean21_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_090_max_tr_over_mean21_63d_d2},
    "f40_atxd_091_longest_tr_increase_run_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_091_longest_tr_increase_run_63d_d2},
    "f40_atxd_092_longest_tr_decrease_run_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_092_longest_tr_decrease_run_63d_d2},
    "f40_atxd_093_count_tr_increases_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_093_count_tr_increases_21d_d2},
    "f40_atxd_094_mean_runlength_tr_expansions_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_094_mean_runlength_tr_expansions_252d_d2},
    "f40_atxd_095_total_abs_tr_change_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_095_total_abs_tr_change_63d_d2},
    "f40_atxd_096_corr_atr21_logvol_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_096_corr_atr21_logvol_63d_d2},
    "f40_atxd_097_corr_atr21_logvol_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_097_corr_atr21_logvol_252d_d2},
    "f40_atxd_098_atr21_on_high_vs_low_vol_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_098_atr21_on_high_vs_low_vol_252d_d2},
    "f40_atxd_099_corr_natr21_volz_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_099_corr_natr21_volz_252d_d2},
    "f40_atxd_100_count_atr_p75_and_volz_above_1_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_100_count_atr_p75_and_volz_above_1_63d_d2},
    "f40_atxd_101_atr21_norm_dist_sma21_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_101_atr21_norm_dist_sma21_d2},
    "f40_atxd_102_atr21_norm_dist_sma63_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_102_atr21_norm_dist_sma63_d2},
    "f40_atxd_103_atr21_norm_dist_sma252_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_103_atr21_norm_dist_sma252_d2},
    "f40_atxd_104_std_atr21_norm_dist_sma21_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_104_std_atr21_norm_dist_sma21_63d_d2},
    "f40_atxd_105_max_atr21_norm_dist_sma21_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_105_max_atr21_norm_dist_sma21_63d_d2},
    "f40_atxd_106_sum_tr_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_106_sum_tr_21d_d2},
    "f40_atxd_107_sum_tr_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_107_sum_tr_63d_d2},
    "f40_atxd_108_sum_tr_252d_over_close_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_108_sum_tr_252d_over_close_d2},
    "f40_atxd_109_ratio_sum_tr_21_over_252_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_109_ratio_sum_tr_21_over_252_d2},
    "f40_atxd_110_log_ratio_sum_tr_21_over_252_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_110_log_ratio_sum_tr_21_over_252_d2},
    "f40_atxd_111_atr_on_top_quartile_tr_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_111_atr_on_top_quartile_tr_63d_d2},
    "f40_atxd_112_atr_on_bottom_quartile_tr_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_112_atr_on_bottom_quartile_tr_63d_d2},
    "f40_atxd_113_ratio_large_small_bar_atr_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_113_ratio_large_small_bar_atr_63d_d2},
    "f40_atxd_114_diff_large_small_bar_atr_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_114_diff_large_small_bar_atr_63d_d2},
    "f40_atxd_115_natr21_change_lag21_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_115_natr21_change_lag21_d2},
    "f40_atxd_116_natr21_pct_change_lag63_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_116_natr21_pct_change_lag63_d2},
    "f40_atxd_117_natr21_pct_change_lag252_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_117_natr21_pct_change_lag252_d2},
    "f40_atxd_118_natr21_range_max_min_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_118_natr21_range_max_min_252d_d2},
    "f40_atxd_119_natr21_over_rollmean_1260d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_119_natr21_over_rollmean_1260d_d2},
    "f40_atxd_120_skew_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_120_skew_tr_252d_d2},
    "f40_atxd_121_kurt_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_121_kurt_tr_252d_d2},
    "f40_atxd_122_freq_tr_above_lag_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_122_freq_tr_above_lag_63d_d2},
    "f40_atxd_123_cumulative_tr_diff_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_123_cumulative_tr_diff_63d_d2},
    "f40_atxd_124_autocorr_tr_diff_lag1_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_124_autocorr_tr_diff_lag1_252d_d2},
    "f40_atxd_125_ar1_atr21_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_125_ar1_atr21_252d_d2},
    "f40_atxd_126_ar1_natr21_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_126_ar1_natr21_252d_d2},
    "f40_atxd_127_halflife_atr_shock_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_127_halflife_atr_shock_252d_d2},
    "f40_atxd_128_autocorr_atr21_lag5_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_128_autocorr_atr21_lag5_252d_d2},
    "f40_atxd_129_autocorr_atr21_lag21_504d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_129_autocorr_atr21_lag21_504d_d2},
    "f40_atxd_130_count_atr21_above_15x_atr63_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_130_count_atr21_above_15x_atr63_63d_d2},
    "f40_atxd_131_bars_since_atr5_above_2x_atr63_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_131_bars_since_atr5_above_2x_atr63_d2},
    "f40_atxd_132_count_natr21_above_2x_natr252_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_132_count_natr21_above_2x_natr252_252d_d2},
    "f40_atxd_133_peak_atr5_over_atr252_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_133_peak_atr5_over_atr252_63d_d2},
    "f40_atxd_134_longest_atr21_above_p75_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_134_longest_atr21_above_p75_252d_d2},
    "f40_atxd_135_ratio_mean_tr_high_vs_low_vol_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_135_ratio_mean_tr_high_vs_low_vol_252d_d2},
    "f40_atxd_136_cv_atr21_504d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_136_cv_atr21_504d_d2},
    "f40_atxd_137_current_atr21_rising_run_length_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_137_current_atr21_rising_run_length_d2},
    "f40_atxd_138_centered_pctrank_atr21_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_138_centered_pctrank_atr21_252d_d2},
    "f40_atxd_139_current_atr21_top_decile_dwell_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_139_current_atr21_top_decile_dwell_d2},
    "f40_atxd_140_range_of_natr_zscore_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_140_range_of_natr_zscore_252d_d2},
    "f40_atxd_141_zscore_range_252d_dispersion_d2": {"inputs": ["high", "low"], "func": f40_atxd_141_zscore_range_252d_dispersion_d2},
    "f40_atxd_142_slope_atr_ratio_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_142_slope_atr_ratio_63d_d2},
    "f40_atxd_143_atr_acceleration_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_143_atr_acceleration_21d_d2},
    "f40_atxd_144_natr_acceleration_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_144_natr_acceleration_21d_d2},
    "f40_atxd_145_count_atr21_jump_15x_lag_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_145_count_atr21_jump_15x_lag_63d_d2},
    "f40_atxd_146_count_tr_above_3xlag_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_146_count_tr_above_3xlag_252d_d2},
    "f40_atxd_147_autocorr_tr_lag5_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_147_autocorr_tr_lag5_252d_d2},
    "f40_atxd_148_hill_atr21_top10_1260d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_148_hill_atr21_top10_1260d_d2},
    "f40_atxd_149_skew_atr21_504d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_149_skew_atr21_504d_d2},
    "f40_atxd_150_tr_theil_concentration_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_150_tr_theil_concentration_252d_d2},
}
