"""f29_relative_strength_vs_benchmark base features 076-150.

Domain: relative strength vs a benchmark series. Disjoint structural classes
from base_001_075: downside beta, semi-beta, beta term-shift, Kendall tau,
rolling Pearson at very different windows, ATR-normalized active risk,
calmar/pain-index diffs, RS pivot dynamics, RS new highs/lows count, RS
DEMA/TEMA/Wilder/T3 deviations, RS jaccard sign overlap, joint-volatility
regime states, RS gini index, RS-line drawdown duration, days-since RS peak,
log-spread oscillator, percentile of beta within stock_ret distribution,
relative-VWAP-like measure using volume weighting, etc. NaN policy:
fillna(<value>) is forbidden inside helpers; only replace([inf,-inf], nan)
at the function's final return. Windows > 21d use closeadj.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _dema(s: pd.Series, n: int) -> pd.Series:
    e1 = _ema(s, n); e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _tema(s: pd.Series, n: int) -> pd.Series:
    e1 = _ema(s, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _rolling_drawdown(s: pd.Series, n: int) -> pd.Series:
    rmax = s.rolling(n, min_periods=n).max()
    return (s / rmax) - 1.0


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === Downside / semi-beta family ===

def f29rs_f29_relative_strength_vs_benchmark_downside_beta_60d_base_v076_signal(closeadj, benchmark):
    """Beta computed only on benchmark-down days over a 60d window. Differs from
    full-sample beta when stock asymmetrically participates in selloffs."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    mask = (rb < 0).astype(float)
    n = 60
    sum_rb = (rb * mask).rolling(n, min_periods=n).sum()
    sum_rs = (rs * mask).rolling(n, min_periods=n).sum()
    cnt = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu_rb = sum_rb / cnt
    mu_rs = sum_rs / cnt
    cov = ((rs - mu_rs) * (rb - mu_rb) * mask).rolling(n, min_periods=n).sum() / cnt
    var = (((rb - mu_rb) ** 2) * mask).rolling(n, min_periods=n).sum() / cnt
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_upside_beta_60d_base_v077_signal(closeadj, benchmark):
    """Beta computed only on benchmark-up days over 60d. Asymmetry counterpart to v076."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    mask = (rb > 0).astype(float)
    n = 60
    sum_rb = (rb * mask).rolling(n, min_periods=n).sum()
    sum_rs = (rs * mask).rolling(n, min_periods=n).sum()
    cnt = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu_rb = sum_rb / cnt
    mu_rs = sum_rs / cnt
    cov = ((rs - mu_rs) * (rb - mu_rb) * mask).rolling(n, min_periods=n).sum() / cnt
    var = (((rb - mu_rb) ** 2) * mask).rolling(n, min_periods=n).sum() / cnt
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_beta_asymm_diff_60d_base_v078_signal(closeadj, benchmark):
    """Upside beta minus downside beta over 60d. Asymmetry indicator."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    n = 60
    out_pieces = []
    for sgn in (1.0, -1.0):
        mask = ((rb > 0) if sgn > 0 else (rb < 0)).astype(float)
        cnt = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        mu_rs = (rs * mask).rolling(n, min_periods=n).sum() / cnt
        mu_rb = (rb * mask).rolling(n, min_periods=n).sum() / cnt
        cov = ((rs - mu_rs) * (rb - mu_rb) * mask).rolling(n, min_periods=n).sum() / cnt
        var = (((rb - mu_rb) ** 2) * mask).rolling(n, min_periods=n).sum() / cnt
        out_pieces.append(cov / var.replace(0.0, np.nan))
    return (out_pieces[0] - out_pieces[1]).replace([np.inf, -np.inf], np.nan)


# === Correlation classes: Kendall, exotic windows ===

def f29rs_f29_relative_strength_vs_benchmark_kendall_tau_returns_60d_base_v079_signal(closeadj, benchmark):
    """Kendall tau of stock and benchmark returns over 60d (concordant minus discordant pairs)."""
    rs = closeadj.pct_change().values
    rb = benchmark.pct_change().values
    out = np.full(len(rs), np.nan, dtype=float)
    n = 60
    for i in range(n - 1, len(rs)):
        wa = rs[i - n + 1: i + 1]
        wb = rb[i - n + 1: i + 1]
        if not (np.all(np.isfinite(wa)) and np.all(np.isfinite(wb))):
            continue
        c = 0; d = 0
        for j in range(n - 1):
            for k in range(j + 1, n):
                sa = wa[j] - wa[k]
                sb = wb[j] - wb[k]
                if sa * sb > 0:
                    c += 1
                elif sa * sb < 0:
                    d += 1
        denom = n * (n - 1) / 2.0
        if denom <= 0:
            continue
        out[i] = (c - d) / denom
    return pd.Series(out, index=closeadj.index, dtype=float).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_corr_squared_returns_60d_base_v080_signal(closeadj, benchmark):
    """Corr of squared returns over 60d. Cojump-style volatility comovement (not levels)."""
    rs2 = closeadj.pct_change() ** 2
    rb2 = benchmark.pct_change() ** 2
    return rs2.rolling(60, min_periods=60).corr(rb2).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_corr_diff_lag1_60d_base_v081_signal(closeadj, benchmark):
    """Corr(stock_t, bench_{t-1}) minus Corr(stock_t, bench_t) over 60d.
    Captures one-sided lead-lag asymmetry."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    c0 = rs.rolling(60, min_periods=60).corr(rb)
    c1 = rs.rolling(60, min_periods=60).corr(rb.shift(1))
    return (c1 - c0).replace([np.inf, -np.inf], np.nan)


# === DEMA/TEMA/Wilder of RS line - new kernel families ===

def f29rs_f29_relative_strength_vs_benchmark_dema_logrs_30d_base_v082_signal(closeadj, benchmark):
    """log(RS) - DEMA(log RS, 30). Double-EMA-smoothed RS deviation."""
    rs = np.log(closeadj / benchmark)
    return (rs - _dema(rs, 30)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_tema_slope_logrs_40d_base_v083_signal(closeadj, benchmark):
    """Slope of TEMA(log RS, 40): TEMA - TEMA.shift(10). Distinct from level deviation."""
    rs = np.log(closeadj / benchmark)
    t = _tema(rs, 40)
    return (t - t.shift(10)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_wilder_logrs_25d_base_v084_signal(closeadj, benchmark):
    """log(RS) - Wilder(log RS, 25). Wilder alpha=1/25 smoothing."""
    rs = np.log(closeadj / benchmark)
    return (rs - _wilder(rs, 25)).replace([np.inf, -np.inf], np.nan)


# === Tracking error sub-features and pain index ===

def f29rs_f29_relative_strength_vs_benchmark_te_zscore_120d_base_v085_signal(closeadj, benchmark):
    """Z-score of 30d tracking err relative to its 120d distribution. Risk regime."""
    te = (closeadj.pct_change() - benchmark.pct_change()).rolling(30, min_periods=30).std(ddof=0)
    mu = te.rolling(120, min_periods=120).mean()
    sd = te.rolling(120, min_periods=120).std(ddof=0)
    return ((te - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_pain_index_80d_base_v086_signal(closeadj, benchmark):
    """Pain-index difference: mean(stock_dd, 80d) - mean(bench_dd, 80d), where dd is computed
    over the same 80d rolling window. More negative = stock has worse pain."""
    s_dd = _rolling_drawdown(closeadj, 80)
    b_dd = _rolling_drawdown(benchmark, 80)
    return (s_dd.rolling(80, min_periods=80).mean() - b_dd.rolling(80, min_periods=80).mean()).replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_active_ulcer_60d_base_v087_signal(closeadj, benchmark):
    """Ulcer index difference: sqrt(mean(stock_dd^2)) - sqrt(mean(bench_dd^2)) over 60d."""
    s_dd = _rolling_drawdown(closeadj, 60)
    b_dd = _rolling_drawdown(benchmark, 60)
    s_ulc = np.sqrt((s_dd ** 2).rolling(60, min_periods=60).mean())
    b_ulc = np.sqrt((b_dd ** 2).rolling(60, min_periods=60).mean())
    return (s_ulc - b_ulc).replace([np.inf, -np.inf], np.nan)


# === RS line dynamics: new high/low counts, days-since peak ===

def f29rs_f29_relative_strength_vs_benchmark_days_since_rs_peak_120d_base_v088_signal(closeadj, benchmark):
    """Days since the maximum log RS observed in trailing 120 days."""
    rs = np.log(closeadj / benchmark).values
    out = np.full(len(rs), np.nan, dtype=float)
    n = 120
    for i in range(n - 1, len(rs)):
        w = rs[i - n + 1: i + 1]
        if not np.all(np.isfinite(w)):
            continue
        am = int(np.argmax(w))
        out[i] = float((n - 1) - am)
    return pd.Series(out, index=closeadj.index, dtype=float).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_days_since_rs_trough_120d_base_v089_signal(closeadj, benchmark):
    """Days since the minimum log RS observed in trailing 120 days."""
    rs = np.log(closeadj / benchmark).values
    out = np.full(len(rs), np.nan, dtype=float)
    n = 120
    for i in range(n - 1, len(rs)):
        w = rs[i - n + 1: i + 1]
        if not np.all(np.isfinite(w)):
            continue
        am = int(np.argmin(w))
        out[i] = float((n - 1) - am)
    return pd.Series(out, index=closeadj.index, dtype=float).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_new_low_count_60d_base_v090_signal(closeadj, benchmark):
    """Count of trailing 60d where log RS hit a new 60-day rolling MIN."""
    rs = np.log(closeadj / benchmark)
    rmin = rs.rolling(60, min_periods=60).min()
    flag = (rs <= rmin + 1e-12).astype(float).where(rmin.notna())
    return flag.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# === Risk-adjusted differentials: Calmar, return per dd, Omega-like ===

def f29rs_f29_relative_strength_vs_benchmark_calmar_diff_120d_base_v091_signal(closeadj, benchmark):
    """Calmar ratio diff: (stock_120d_return / |stock_max_dd|) - same for benchmark."""
    s_ret = closeadj / closeadj.shift(120) - 1.0
    b_ret = benchmark / benchmark.shift(120) - 1.0
    s_dd = _rolling_drawdown(closeadj, 120).rolling(120, min_periods=120).min().abs().replace(0.0, np.nan)
    b_dd = _rolling_drawdown(benchmark, 120).rolling(120, min_periods=120).min().abs().replace(0.0, np.nan)
    return (s_ret / s_dd - b_ret / b_dd).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_omega_diff_60d_base_v092_signal(closeadj, benchmark):
    """Omega-ratio difference: sum(pos active ret) / sum(|neg active ret|) over 60d."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    pos = diff.where(diff > 0, 0.0).rolling(60, min_periods=60).sum()
    neg = (-diff.where(diff < 0, 0.0)).rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (pos / neg - 1.0).replace([np.inf, -np.inf], np.nan)


# === Joint volatility regime states ===

def f29rs_f29_relative_strength_vs_benchmark_joint_vol_regime_45d_base_v093_signal(closeadj, benchmark):
    """4-state joint-vol regime: stock_vol_high(>median) AND bench_vol_high — encoded {0,1,2,3}.
    Uses 45d rolling std and trailing 200d median."""
    sv = closeadj.pct_change().rolling(45, min_periods=45).std(ddof=0)
    bv = benchmark.pct_change().rolling(45, min_periods=45).std(ddof=0)
    sm = sv.rolling(200, min_periods=200).median()
    bm = bv.rolling(200, min_periods=200).median()
    s_hi = (sv > sm).astype(int)
    b_hi = (bv > bm).astype(int)
    state = s_hi * 2 + b_hi
    return state.astype(float).where(sm.notna() & bm.notna()).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_vol_gap_zscore_60d_base_v094_signal(closeadj, benchmark):
    """Z-score (over 60d) of the (stock_vol - bench_vol) gap. Captures abnormal vol divergence."""
    sv = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    bv = benchmark.pct_change().rolling(20, min_periods=20).std(ddof=0)
    gap = sv - bv
    mu = gap.rolling(60, min_periods=60).mean()
    sd = gap.rolling(60, min_periods=60).std(ddof=0)
    return ((gap - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Active-return distribution properties ===

def f29rs_f29_relative_strength_vs_benchmark_active_iqr_zscore_120d_base_v095_signal(closeadj, benchmark):
    """Z-score (120d) of 50d active-return IQR. Active-risk regime."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    iqr = diff.rolling(50, min_periods=50).quantile(0.75) - diff.rolling(50, min_periods=50).quantile(0.25)
    mu = iqr.rolling(120, min_periods=120).mean()
    sd = iqr.rolling(120, min_periods=120).std(ddof=0)
    return ((iqr - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_return_min_45d_base_v096_signal(closeadj, benchmark):
    """Minimum (most negative) active return in trailing 45d. Worst single day vs benchmark."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return diff.rolling(45, min_periods=45).min().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_return_max_45d_base_v097_signal(closeadj, benchmark):
    """Maximum (most positive) active return in trailing 45d. Best single day vs benchmark."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return diff.rolling(45, min_periods=45).max().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_return_median_60d_base_v098_signal(closeadj, benchmark):
    """Median active return over 60d. Robust central tendency vs benchmark."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return diff.rolling(60, min_periods=60).median().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_return_p90_minus_p10_60d_base_v099_signal(closeadj, benchmark):
    """p90 - p10 of active return over 60d. Wide tail dispersion."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return (diff.rolling(60, min_periods=60).quantile(0.9) - diff.rolling(60, min_periods=60).quantile(0.1)).replace(
        [np.inf, -np.inf], np.nan
    )


# === Sign-overlap / agreement measures ===

def f29rs_f29_relative_strength_vs_benchmark_sign_agreement_60d_base_v100_signal(closeadj, benchmark):
    """Fraction of trailing 60d where sign(stock_ret) == sign(bench_ret). Directional agreement."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    match = (np.sign(rs) == np.sign(rb)).astype(float)
    return match.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_jaccard_up_45d_base_v101_signal(closeadj, benchmark):
    """Jaccard on bench-up vs stock-up: intersection / union over 45d. Tail-event agreement on ups."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    s_up = (rs > 0).astype(int)
    b_up = (rb > 0).astype(int)
    inter = (s_up * b_up).rolling(45, min_periods=45).sum()
    union = ((s_up + b_up) > 0).astype(int).rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    return (inter / union).replace([np.inf, -np.inf], np.nan)


# === Volume-weighted relative strength ===

def f29rs_f29_relative_strength_vs_benchmark_volwt_active_ret_60d_base_v102_signal(closeadj, benchmark, volume):
    """Volume-weighted mean active return over 60d. Up-weights conviction days."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    num = (diff * volume).rolling(60, min_periods=60).sum()
    den = volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_volwt_corr_45d_base_v103_signal(closeadj, benchmark, volume):
    """Volume-weighted return correlation: weighted Pearson over 45d using volume weights."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    n = 45
    wsum = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu_rs = (rs * volume).rolling(n, min_periods=n).sum() / wsum
    mu_rb = (rb * volume).rolling(n, min_periods=n).sum() / wsum
    cov = ((rs - mu_rs) * (rb - mu_rb) * volume).rolling(n, min_periods=n).sum() / wsum
    var_rs = (((rs - mu_rs) ** 2) * volume).rolling(n, min_periods=n).sum() / wsum
    var_rb = (((rb - mu_rb) ** 2) * volume).rolling(n, min_periods=n).sum() / wsum
    return (cov / np.sqrt(var_rs * var_rb).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === RS line drawdown / duration ===

def f29rs_f29_relative_strength_vs_benchmark_rs_drawdown_90d_base_v104_signal(closeadj, benchmark):
    """Drawdown of log(closeadj/benchmark) line over 90d. RS-line specific underwater measure."""
    rs = np.log(closeadj / benchmark)
    rmax = rs.rolling(90, min_periods=90).max()
    return (rs - rmax).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_recovery_progress_120d_base_v105_signal(closeadj, benchmark):
    """Fraction by which current RS has recovered from its 120d min toward its 120d max:
    (rs - min)/(max - min). Bounded [0,1]. Distinct from days-since-peak."""
    rs = np.log(closeadj / benchmark)
    hi = rs.rolling(120, min_periods=120).max()
    lo = rs.rolling(120, min_periods=120).min()
    return ((rs - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Cumulative outperformance / momentum across alternative windows ===

def f29rs_f29_relative_strength_vs_benchmark_rs_momentum_short_minus_long_base_v106_signal(closeadj, benchmark):
    """log(RS_now / RS_15d_ago) - log(RS_now / RS_90d_ago). Short vs long RS momentum."""
    rs = closeadj / benchmark
    s = np.log(rs / rs.shift(15))
    l = np.log(rs / rs.shift(90))
    return (s - l).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_log_distance_sma_100d_base_v107_signal(closeadj, benchmark):
    """log(closeadj/benchmark) minus its SMA(100). 100d MA-deviation of RS line."""
    rs = np.log(closeadj / benchmark)
    return (rs - _sma(rs, 100)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_ema_logrs_30_180_diff_base_v108_signal(closeadj, benchmark):
    """EMA(log RS, 30) - EMA(log RS, 180). Very-long-spread RS MACD-style signal,
    differential of two EMAs distinct from rs - SMA(100)."""
    rs = np.log(closeadj / benchmark)
    return (_ema(rs, 30) - _ema(rs, 180)).replace([np.inf, -np.inf], np.nan)


# === Active drawdown count / depth dynamics ===

def f29rs_f29_relative_strength_vs_benchmark_active_dd_depth_45d_base_v109_signal(closeadj, benchmark):
    """Cumulative active log-return drawdown from its 45d max."""
    cum = np.log(closeadj / benchmark)
    rmax = cum.rolling(45, min_periods=45).max()
    return (cum - rmax).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_dd_avg_depth_60d_base_v110_signal(closeadj, benchmark):
    """Mean drawdown depth of the log RS line within a 60d window: avg of (rs - rolling max)
    over those 60d. Negative-valued; deeper troughs → more negative."""
    rs = np.log(closeadj / benchmark)
    rmax = rs.rolling(60, min_periods=60).max()
    return (rs - rmax).rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Cross-sectional-style RS quantile and Gini ===

def f29rs_f29_relative_strength_vs_benchmark_rs_gini_60d_base_v111_signal(closeadj, benchmark):
    """Gini coefficient of |daily active returns| over 60d. Concentration of outperf magnitude."""
    diff = (closeadj.pct_change() - benchmark.pct_change()).abs()

    def _gini(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        y = np.sort(x)
        n = len(y)
        if y.sum() == 0:
            return np.nan
        cum = np.cumsum(y)
        return float((n + 1 - 2 * cum.sum() / cum[-1]) / n)

    return diff.rolling(60, min_periods=60).apply(_gini, raw=True).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_entropy_60d_base_v112_signal(closeadj, benchmark):
    """Shannon entropy of sign(active_return) over 60d. 1 bit at 50/50, 0 at pure trend."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    pos = (diff > 0).astype(float)
    n = 60
    p = pos.rolling(n, min_periods=n).mean()

    def _ent(x):
        eps = 1e-12
        return -x * np.log2(x + eps) - (1 - x) * np.log2(1 - x + eps)

    return _ent(p).replace([np.inf, -np.inf], np.nan)


# === Sign-based outperformance with magnitude weighting ===

def f29rs_f29_relative_strength_vs_benchmark_signed_outperf_intensity_30d_base_v113_signal(close, benchmark):
    """sign(stock-bench return) * |stock-bench return|^0.5 averaged over 30d. Magnitude-weighted sign."""
    diff = close.pct_change() - benchmark.pct_change()
    sig = np.sign(diff) * np.sqrt(diff.abs())
    return sig.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_winsor_active_mean_60d_base_v114_signal(closeadj, benchmark):
    """Winsorized mean (10/90 pctile clip) of active return over 60d. Robust outperformance."""
    diff = closeadj.pct_change() - benchmark.pct_change()

    def _wm(x):
        if not np.all(np.isfinite(x)) or len(x) < 5:
            return np.nan
        lo = np.quantile(x, 0.1); hi = np.quantile(x, 0.9)
        return float(np.mean(np.clip(x, lo, hi)))

    return diff.rolling(60, min_periods=60).apply(_wm, raw=True).replace([np.inf, -np.inf], np.nan)


# === Beta term structure / convexity ===

def f29rs_f29_relative_strength_vs_benchmark_beta_curvature_base_v115_signal(closeadj, benchmark):
    """Quadratic curvature in beta term structure: beta(30) - 2*beta(60) + beta(120)."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    def _beta(n):
        cov = rs.rolling(n, min_periods=n).cov(rb)
        var = rb.rolling(n, min_periods=n).var()
        return cov / var.replace(0.0, np.nan)
    return (_beta(30) - 2.0 * _beta(60) + _beta(120)).replace([np.inf, -np.inf], np.nan)


# === RS spread oscillator / pivot ===

def f29rs_f29_relative_strength_vs_benchmark_rs_pivot_break_30d_base_v116_signal(closeadj, benchmark):
    """(log RS - median(log RS, 30d)) / IQR(log RS, 30d). Pivot-break-style signal in IQR units."""
    rs = np.log(closeadj / benchmark)
    med = rs.rolling(30, min_periods=30).median()
    iqr = rs.rolling(30, min_periods=30).quantile(0.75) - rs.rolling(30, min_periods=30).quantile(0.25)
    return ((rs - med) / iqr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_chop_index_45d_base_v117_signal(closeadj, benchmark):
    """Choppiness-of-RS index: 100 * log10(sum |dRS|) / log10(N) within 45d window scaled by
    log-range. Bounded [0,100]-ish. Detects sideways vs trending RS."""
    rs = np.log(closeadj / benchmark)
    n = 45
    tr = rs.diff().abs()
    s_tr = tr.rolling(n, min_periods=n).sum()
    hi = rs.rolling(n, min_periods=n).max()
    lo = rs.rolling(n, min_periods=n).min()
    rng = (hi - lo).replace(0.0, np.nan)
    return (100.0 * np.log10(s_tr / rng) / np.log10(n)).replace([np.inf, -np.inf], np.nan)


# === Days underperforming / outperforming counts and dynamics ===

def f29rs_f29_relative_strength_vs_benchmark_outperf_count_diff_short_long_base_v118_signal(closeadj, benchmark):
    """(outperf_count_30d / 30) - (outperf_count_120d / 120). Short vs long winning rate."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    c30 = (diff > 0).astype(float).rolling(30, min_periods=30).mean()
    c120 = (diff > 0).astype(float).rolling(120, min_periods=120).mean()
    return (c30 - c120).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_consecutive_outperf_freq_80d_base_v119_signal(closeadj, benchmark):
    """Fraction of days within 80d that are part of an outperf streak >= 2. Persistence indicator."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    dv = diff.values
    streak2 = np.full(len(dv), np.nan, dtype=float)
    for i in range(1, len(dv)):
        if not (np.isfinite(dv[i]) and np.isfinite(dv[i - 1])):
            continue
        streak2[i] = 1.0 if (dv[i] > 0 and dv[i - 1] > 0) else 0.0
    return pd.Series(streak2, index=closeadj.index, dtype=float).rolling(80, min_periods=80).mean().replace(
        [np.inf, -np.inf], np.nan
    )


# === Bench-relative momentum at extra cadences ===

def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_5d_base_v120_signal(close, benchmark):
    """5-day outperformance: close.pct_change(5) - benchmark.pct_change(5)."""
    return (close.pct_change(5) - benchmark.pct_change(5)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_120d_base_v121_signal(closeadj, benchmark):
    """120-day outperformance."""
    return (closeadj.pct_change(120) - benchmark.pct_change(120)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_diff_5_60_base_v122_signal(close, closeadj, benchmark):
    """5d outperformance minus 60d outperformance. Short impulse vs medium baseline."""
    short = close.pct_change(5) - benchmark.pct_change(5)
    long = closeadj.pct_change(60) - benchmark.pct_change(60)
    return (short - long).replace([np.inf, -np.inf], np.nan)


# === Bench-conditional moments ===

def f29rs_f29_relative_strength_vs_benchmark_bench_extreme_outperf_60d_base_v123_signal(closeadj, benchmark):
    """Mean stock-ret on top-decile bench-ret days within 60d. Captures extreme up-days behavior."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    n = 60

    def _f(idx):
        r_b = rb.iloc[idx - n + 1: idx + 1].values
        r_s = rs.iloc[idx - n + 1: idx + 1].values
        if not (np.all(np.isfinite(r_b)) and np.all(np.isfinite(r_s))):
            return np.nan
        thr = np.quantile(r_b, 0.9)
        sel = r_s[r_b >= thr]
        if len(sel) == 0:
            return np.nan
        return float(np.mean(sel))

    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    for i in range(n - 1, len(closeadj)):
        out.iat[i] = _f(i)
    return out.replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_bench_extreme_underperf_60d_base_v124_signal(closeadj, benchmark):
    """Mean stock-ret on bottom-decile bench-ret days within 60d. Captures crash-day behavior."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    n = 60

    def _f(idx):
        r_b = rb.iloc[idx - n + 1: idx + 1].values
        r_s = rs.iloc[idx - n + 1: idx + 1].values
        if not (np.all(np.isfinite(r_b)) and np.all(np.isfinite(r_s))):
            return np.nan
        thr = np.quantile(r_b, 0.1)
        sel = r_s[r_b <= thr]
        if len(sel) == 0:
            return np.nan
        return float(np.mean(sel))

    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    for i in range(n - 1, len(closeadj)):
        out.iat[i] = _f(i)
    return out.replace([np.inf, -np.inf], np.nan)


# === Long-horizon log RS rank distribution ===

def f29rs_f29_relative_strength_vs_benchmark_logrs_rank_250d_base_v125_signal(closeadj, benchmark):
    """Percentile rank of log RS over 250d. Annual-horizon RS positioning."""
    rs = np.log(closeadj / benchmark)
    return rs.rolling(250, min_periods=250).apply(
        lambda x: (np.sum(x <= x[-1]) - 1) / (len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_ret_rank_30d_base_v126_signal(close, benchmark):
    """Percentile rank of today's active return within trailing 30d active-return distribution."""
    diff = close.pct_change() - benchmark.pct_change()
    return diff.rolling(30, min_periods=30).apply(
        lambda x: (np.sum(x <= x[-1]) - 1) / (len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


# === Forward-shifted asymmetric correlation ===

def f29rs_f29_relative_strength_vs_benchmark_corr_recent_vs_past_120d_base_v127_signal(closeadj, benchmark):
    """Recent (last 30d) return corr minus older (60d ago, 30d window) corr. Corr regime shift."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    c_now = rs.rolling(30, min_periods=30).corr(rb)
    c_old = c_now.shift(60)
    return (c_now - c_old).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_ret_bench_vol_interaction_60d_base_v128_signal(closeadj, benchmark):
    """Corr(active_return, bench_vol) over 60d. Captures whether outperformance correlates
    with regime of benchmark volatility."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    bvol = benchmark.pct_change().abs()
    return diff.rolling(60, min_periods=60).corr(bvol).replace([np.inf, -np.inf], np.nan)


# === Volatility-normalized active return ===

def f29rs_f29_relative_strength_vs_benchmark_active_ret_volnorm_30d_base_v129_signal(close, benchmark):
    """Sum of active returns / bench std over 30d. Active return per unit bench volatility."""
    diff = close.pct_change() - benchmark.pct_change()
    num = diff.rolling(30, min_periods=30).sum()
    den = benchmark.pct_change().rolling(30, min_periods=30).std(ddof=0).replace(0.0, np.nan)
    return (num / (den * 30.0)).replace([np.inf, -np.inf], np.nan)


# === Conditional regime mapping ===

def f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_uptrend_base_v130_signal(closeadj, benchmark):
    """Active return mean conditioned on benchmark uptrend (bench > SMA60). Otherwise nan."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    bench_up = (benchmark > _sma(benchmark, 60))
    cond = diff.where(bench_up)
    return cond.rolling(60, min_periods=10).mean().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_downtrend_base_v131_signal(closeadj, benchmark):
    """Active return mean conditioned on benchmark downtrend (bench < SMA60)."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    bench_dn = (benchmark < _sma(benchmark, 60))
    cond = diff.where(bench_dn)
    return cond.rolling(60, min_periods=10).mean().replace([np.inf, -np.inf], np.nan)


# === Rolling slope of correlation / beta ===

def f29rs_f29_relative_strength_vs_benchmark_corr_slope_60d_base_v132_signal(closeadj, benchmark):
    """diff(corr_20d, 30) over a 60d horizon. Rate of change of return correlation."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    c = rs.rolling(20, min_periods=20).corr(rb)
    return c.diff(30).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_beta_slope_45d_base_v133_signal(closeadj, benchmark):
    """diff(beta_30d, 45). Rate of change of beta over 45-day horizon."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(30, min_periods=30).cov(rb)
    var = rb.rolling(30, min_periods=30).var()
    beta = cov / var.replace(0.0, np.nan)
    return beta.diff(45).replace([np.inf, -np.inf], np.nan)


# === Active-return autocorrelation ===

def f29rs_f29_relative_strength_vs_benchmark_active_ret_autocorr_50d_base_v134_signal(closeadj, benchmark):
    """Lag-1 autocorrelation of active return over 50d. Persistence of outperformance."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    diff_lag = diff.shift(1)
    return diff.rolling(50, min_periods=50).corr(diff_lag).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_autocorr_lag5_80d_base_v135_signal(closeadj, benchmark):
    """Lag-5 autocorr of log RS diff over 80d. Weekly momentum/reversion in RS line."""
    drs = np.log(closeadj / benchmark).diff()
    return drs.rolling(80, min_periods=80).corr(drs.shift(5)).replace([np.inf, -np.inf], np.nan)


# === RS amplitude / range features ===

def f29rs_f29_relative_strength_vs_benchmark_rs_range_30d_base_v136_signal(closeadj, benchmark):
    """max(log RS, 30) - min(log RS, 30). RS-line oscillation range."""
    rs = np.log(closeadj / benchmark)
    return (rs.rolling(30, min_periods=30).max() - rs.rolling(30, min_periods=30).min()).replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_rs_range_zscore_120d_base_v137_signal(closeadj, benchmark):
    """Z-score (120d) of 30d RS range. Compression vs expansion of RS oscillation."""
    rs = np.log(closeadj / benchmark)
    rng = rs.rolling(30, min_periods=30).max() - rs.rolling(30, min_periods=30).min()
    mu = rng.rolling(120, min_periods=120).mean()
    sd = rng.rolling(120, min_periods=120).std(ddof=0)
    return ((rng - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Joint trend regime states ===

def f29rs_f29_relative_strength_vs_benchmark_state_trend_alignment_base_v138_signal(closeadj, benchmark):
    """+1 if both stock and benchmark are above their 100d SMAs; -1 if both below; 0 otherwise.
    Captures alignment of stock and benchmark trend regime."""
    s_up = (closeadj > _sma(closeadj, 100))
    b_up = (benchmark > _sma(benchmark, 100))
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    out = out.mask(s_up & b_up, 1.0)
    out = out.mask((~s_up) & (~b_up), -1.0)
    sma_valid = _sma(closeadj, 100).notna() & _sma(benchmark, 100).notna()
    return out.where(sma_valid).replace([np.inf, -np.inf], np.nan)


# === Bench-conditional return ratio ===

def f29rs_f29_relative_strength_vs_benchmark_ret_ratio_med_30d_base_v139_signal(close, benchmark):
    """Median(stock_ret / bench_ret) on days where bench_ret != 0, in 30d window."""
    rs = close.pct_change()
    rb = benchmark.pct_change().replace(0.0, np.nan)
    ratio = rs / rb
    return ratio.rolling(30, min_periods=10).median().replace([np.inf, -np.inf], np.nan)


# === Sequence-based: longest run of underperformance in long window ===

def f29rs_f29_relative_strength_vs_benchmark_max_underperf_run_120d_base_v140_signal(closeadj, benchmark):
    """Longest consecutive underperformance run within trailing 120d window."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    sig = (diff < 0).astype(float).where(diff.notna())

    def _max_run(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        m = 0; cur = 0
        for v in x:
            if v > 0.5:
                cur += 1
                if cur > m:
                    m = cur
            else:
                cur = 0
        return float(m)

    arr = sig.rolling(120, min_periods=120).apply(_max_run, raw=True)
    return arr.replace([np.inf, -np.inf], np.nan)


# === Spread between log-RS and its quantile envelope ===

def f29rs_f29_relative_strength_vs_benchmark_rs_q75_dist_60d_base_v141_signal(closeadj, benchmark):
    """log RS minus its 60d 75th percentile. Distance from upper RS band."""
    rs = np.log(closeadj / benchmark)
    return (rs - rs.rolling(60, min_periods=60).quantile(0.75)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_iqr_zscore_60d_base_v142_signal(closeadj, benchmark):
    """Z-position of log RS within its (p25,p75) interquartile range over 60d:
    (rs - median) / IQR. Robust scale; distinct from quantile distance."""
    rs = np.log(closeadj / benchmark)
    q1 = rs.rolling(60, min_periods=60).quantile(0.25)
    q3 = rs.rolling(60, min_periods=60).quantile(0.75)
    med = rs.rolling(60, min_periods=60).median()
    return ((rs - med) / (q3 - q1).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === RS line %B (BB-style position) ===

def f29rs_f29_relative_strength_vs_benchmark_rs_pctB_30d_base_v143_signal(closeadj, benchmark):
    """%B of log RS using SMA(30) and 2*std(30) bands."""
    rs = np.log(closeadj / benchmark)
    mu = _sma(rs, 30)
    sd = rs.rolling(30, min_periods=30).std(ddof=0)
    lo = mu - 2.0 * sd
    hi = mu + 2.0 * sd
    return ((rs - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_bandwidth_45d_base_v144_signal(closeadj, benchmark):
    """Bollinger bandwidth of log RS: (4 * std_45) / |sma_45|. Vol regime of RS line."""
    rs = np.log(closeadj / benchmark)
    mu = _sma(rs, 45)
    sd = rs.rolling(45, min_periods=45).std(ddof=0)
    return (4.0 * sd / mu.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Beta dispersion ===

def f29rs_f29_relative_strength_vs_benchmark_beta_dispersion_120d_base_v145_signal(closeadj, benchmark):
    """std of rolling 20d beta values over 120d. Beta instability."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(20, min_periods=20).cov(rb)
    var = rb.rolling(20, min_periods=20).var()
    beta = cov / var.replace(0.0, np.nan)
    return beta.rolling(120, min_periods=120).std(ddof=0).replace([np.inf, -np.inf], np.nan)


# === High/low position vs benchmark high/low ===

def f29rs_f29_relative_strength_vs_benchmark_high_to_benchhigh_30d_base_v146_signal(high, benchmark):
    """high(stock,30) / high(bench,30) - 1. Relative high reach intraday-based."""
    sh = high.rolling(30, min_periods=30).max()
    bh = benchmark.rolling(30, min_periods=30).max()
    return (sh / bh.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_low_to_benchlow_30d_base_v147_signal(low, benchmark):
    """low(stock,30) / low(bench,30) - 1. Relative trough depth."""
    sl = low.rolling(30, min_periods=30).min()
    bl = benchmark.rolling(30, min_periods=30).min()
    return (sl / bl.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Tail correlation ===

def f29rs_f29_relative_strength_vs_benchmark_tail_coexceed_60d_base_v148_signal(closeadj, benchmark):
    """Fraction of trailing 60d where both rets in bottom decile (joint left tail)."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    qs = rs.rolling(60, min_periods=60).quantile(0.1)
    qb = rb.rolling(60, min_periods=60).quantile(0.1)
    flag = ((rs <= qs) & (rb <= qb)).astype(float).where(qs.notna() & qb.notna())
    return flag.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Slope of cum log RS regression ===

def f29rs_f29_relative_strength_vs_benchmark_rs_regslope_90d_base_v149_signal(closeadj, benchmark):
    """Linear-regression slope of log RS vs time over 90d, divided by 90 (per-day RS trend)."""
    rs = np.log(closeadj / benchmark)

    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx)); vt = np.sum((t - mt) ** 2)
        if vt == 0.0:
            return np.nan
        return float(cov / vt)

    return rs.rolling(90, min_periods=90).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_regrsq_90d_base_v150_signal(closeadj, benchmark):
    """R-squared of log RS vs time regression over 90d. RS trend straightness."""
    rs = np.log(closeadj / benchmark)

    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        r = cov / np.sqrt(vt * vx)
        return float(r * r)

    return rs.rolling(90, min_periods=90).apply(_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f29_relative_strength_vs_benchmark_base_076_150_REGISTRY = {
    "f29rs_f29_relative_strength_vs_benchmark_downside_beta_60d_base_v076_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_downside_beta_60d_base_v076_signal},
    "f29rs_f29_relative_strength_vs_benchmark_upside_beta_60d_base_v077_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_upside_beta_60d_base_v077_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_asymm_diff_60d_base_v078_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_asymm_diff_60d_base_v078_signal},
    "f29rs_f29_relative_strength_vs_benchmark_kendall_tau_returns_60d_base_v079_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_kendall_tau_returns_60d_base_v079_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_squared_returns_60d_base_v080_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_squared_returns_60d_base_v080_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_diff_lag1_60d_base_v081_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_diff_lag1_60d_base_v081_signal},
    "f29rs_f29_relative_strength_vs_benchmark_dema_logrs_30d_base_v082_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_dema_logrs_30d_base_v082_signal},
    "f29rs_f29_relative_strength_vs_benchmark_tema_slope_logrs_40d_base_v083_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_tema_slope_logrs_40d_base_v083_signal},
    "f29rs_f29_relative_strength_vs_benchmark_wilder_logrs_25d_base_v084_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_wilder_logrs_25d_base_v084_signal},
    "f29rs_f29_relative_strength_vs_benchmark_te_zscore_120d_base_v085_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_te_zscore_120d_base_v085_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_pain_index_80d_base_v086_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_pain_index_80d_base_v086_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_ulcer_60d_base_v087_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_ulcer_60d_base_v087_signal},
    "f29rs_f29_relative_strength_vs_benchmark_days_since_rs_peak_120d_base_v088_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_days_since_rs_peak_120d_base_v088_signal},
    "f29rs_f29_relative_strength_vs_benchmark_days_since_rs_trough_120d_base_v089_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_days_since_rs_trough_120d_base_v089_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_new_low_count_60d_base_v090_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_new_low_count_60d_base_v090_signal},
    "f29rs_f29_relative_strength_vs_benchmark_calmar_diff_120d_base_v091_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_calmar_diff_120d_base_v091_signal},
    "f29rs_f29_relative_strength_vs_benchmark_omega_diff_60d_base_v092_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_omega_diff_60d_base_v092_signal},
    "f29rs_f29_relative_strength_vs_benchmark_joint_vol_regime_45d_base_v093_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_joint_vol_regime_45d_base_v093_signal},
    "f29rs_f29_relative_strength_vs_benchmark_vol_gap_zscore_60d_base_v094_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_vol_gap_zscore_60d_base_v094_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_iqr_zscore_120d_base_v095_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_iqr_zscore_120d_base_v095_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_return_min_45d_base_v096_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_return_min_45d_base_v096_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_return_max_45d_base_v097_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_return_max_45d_base_v097_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_return_median_60d_base_v098_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_return_median_60d_base_v098_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_return_p90_minus_p10_60d_base_v099_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_return_p90_minus_p10_60d_base_v099_signal},
    "f29rs_f29_relative_strength_vs_benchmark_sign_agreement_60d_base_v100_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_sign_agreement_60d_base_v100_signal},
    "f29rs_f29_relative_strength_vs_benchmark_jaccard_up_45d_base_v101_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_jaccard_up_45d_base_v101_signal},
    "f29rs_f29_relative_strength_vs_benchmark_volwt_active_ret_60d_base_v102_signal": {"inputs": ["closeadj", "benchmark", "volume"], "func": f29rs_f29_relative_strength_vs_benchmark_volwt_active_ret_60d_base_v102_signal},
    "f29rs_f29_relative_strength_vs_benchmark_volwt_corr_45d_base_v103_signal": {"inputs": ["closeadj", "benchmark", "volume"], "func": f29rs_f29_relative_strength_vs_benchmark_volwt_corr_45d_base_v103_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_drawdown_90d_base_v104_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_drawdown_90d_base_v104_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_recovery_progress_120d_base_v105_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_recovery_progress_120d_base_v105_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_momentum_short_minus_long_base_v106_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_momentum_short_minus_long_base_v106_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_log_distance_sma_100d_base_v107_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_log_distance_sma_100d_base_v107_signal},
    "f29rs_f29_relative_strength_vs_benchmark_ema_logrs_30_180_diff_base_v108_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_ema_logrs_30_180_diff_base_v108_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_dd_depth_45d_base_v109_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_dd_depth_45d_base_v109_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_dd_avg_depth_60d_base_v110_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_dd_avg_depth_60d_base_v110_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_gini_60d_base_v111_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_gini_60d_base_v111_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_entropy_60d_base_v112_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_entropy_60d_base_v112_signal},
    "f29rs_f29_relative_strength_vs_benchmark_signed_outperf_intensity_30d_base_v113_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_signed_outperf_intensity_30d_base_v113_signal},
    "f29rs_f29_relative_strength_vs_benchmark_winsor_active_mean_60d_base_v114_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_winsor_active_mean_60d_base_v114_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_curvature_base_v115_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_curvature_base_v115_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_pivot_break_30d_base_v116_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_pivot_break_30d_base_v116_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_chop_index_45d_base_v117_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_chop_index_45d_base_v117_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_count_diff_short_long_base_v118_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_count_diff_short_long_base_v118_signal},
    "f29rs_f29_relative_strength_vs_benchmark_consecutive_outperf_freq_80d_base_v119_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_consecutive_outperf_freq_80d_base_v119_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_5d_base_v120_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_5d_base_v120_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_120d_base_v121_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_120d_base_v121_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_diff_5_60_base_v122_signal": {"inputs": ["close", "closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_diff_5_60_base_v122_signal},
    "f29rs_f29_relative_strength_vs_benchmark_bench_extreme_outperf_60d_base_v123_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_bench_extreme_outperf_60d_base_v123_signal},
    "f29rs_f29_relative_strength_vs_benchmark_bench_extreme_underperf_60d_base_v124_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_bench_extreme_underperf_60d_base_v124_signal},
    "f29rs_f29_relative_strength_vs_benchmark_logrs_rank_250d_base_v125_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_logrs_rank_250d_base_v125_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_ret_rank_30d_base_v126_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_ret_rank_30d_base_v126_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_recent_vs_past_120d_base_v127_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_recent_vs_past_120d_base_v127_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_ret_bench_vol_interaction_60d_base_v128_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_ret_bench_vol_interaction_60d_base_v128_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_ret_volnorm_30d_base_v129_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_ret_volnorm_30d_base_v129_signal},
    "f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_uptrend_base_v130_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_uptrend_base_v130_signal},
    "f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_downtrend_base_v131_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_downtrend_base_v131_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_slope_60d_base_v132_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_slope_60d_base_v132_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_slope_45d_base_v133_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_slope_45d_base_v133_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_ret_autocorr_50d_base_v134_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_ret_autocorr_50d_base_v134_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_autocorr_lag5_80d_base_v135_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_autocorr_lag5_80d_base_v135_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_range_30d_base_v136_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_range_30d_base_v136_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_range_zscore_120d_base_v137_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_range_zscore_120d_base_v137_signal},
    "f29rs_f29_relative_strength_vs_benchmark_state_trend_alignment_base_v138_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_state_trend_alignment_base_v138_signal},
    "f29rs_f29_relative_strength_vs_benchmark_ret_ratio_med_30d_base_v139_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_ret_ratio_med_30d_base_v139_signal},
    "f29rs_f29_relative_strength_vs_benchmark_max_underperf_run_120d_base_v140_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_max_underperf_run_120d_base_v140_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_q75_dist_60d_base_v141_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_q75_dist_60d_base_v141_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_iqr_zscore_60d_base_v142_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_iqr_zscore_60d_base_v142_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_pctB_30d_base_v143_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_pctB_30d_base_v143_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_bandwidth_45d_base_v144_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_bandwidth_45d_base_v144_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_dispersion_120d_base_v145_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_dispersion_120d_base_v145_signal},
    "f29rs_f29_relative_strength_vs_benchmark_high_to_benchhigh_30d_base_v146_signal": {"inputs": ["high", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_high_to_benchhigh_30d_base_v146_signal},
    "f29rs_f29_relative_strength_vs_benchmark_low_to_benchlow_30d_base_v147_signal": {"inputs": ["low", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_low_to_benchlow_30d_base_v147_signal},
    "f29rs_f29_relative_strength_vs_benchmark_tail_coexceed_60d_base_v148_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_tail_coexceed_60d_base_v148_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_regslope_90d_base_v149_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_regslope_90d_base_v149_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_regrsq_90d_base_v150_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_regrsq_90d_base_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)

    rng2 = np.random.default_rng(seed + 1)
    bench_ret = np.concatenate([
        rng2.normal(0.0008, 0.009, seg),
        rng2.normal(-0.0003, 0.014, seg),
        rng2.normal(-0.0007, 0.011, seg),
        rng2.normal(0.0006, 0.010, rest),
    ])
    benchmark = 50.0 * np.exp(np.cumsum(bench_ret))

    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
        "benchmark": pd.Series(benchmark, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f29_relative_strength_vs_benchmark_base_076_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
