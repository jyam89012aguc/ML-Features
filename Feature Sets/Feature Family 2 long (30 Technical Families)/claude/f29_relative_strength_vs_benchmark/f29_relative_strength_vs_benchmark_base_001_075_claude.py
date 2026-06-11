"""f29_relative_strength_vs_benchmark base features 001-075.

Domain: relative strength vs a benchmark series. Every feature references
BOTH the stock's closeadj/close and a benchmark series. Categories used in
this file: raw RS (pct-diff, log-ratio, cumulative outperformance), RS-MA,
RS rank, rolling beta/alpha (cov/var, residual std), correlation (Pearson,
Spearman, returns, lead-lag), tracking error & information ratio, up/down
capture, outperformance streaks/counts, drawdown comparison, RS oscillator
(RSI/stoch of RS), RS slope/curvature/accel, 4-state regime, bounded
transforms (arctan/tanh/sigmoid), risk-adjusted differentials, correlation
regime (high/low corr periods, decoupling days). NaN policy: never
fillna(<value>); only replace([inf,-inf], nan) at final return. Windows
> 21d use closeadj; <= 21d use close. Functions accept benchmark as a
named input from the registry.
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


def _wma(s: pd.Series, n: int) -> pd.Series:
    w = np.arange(1, n + 1, dtype=float); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _rolling_drawdown(s: pd.Series, n: int) -> pd.Series:
    rmax = s.rolling(n, min_periods=n).max()
    return (s / rmax) - 1.0


def _rank_pct(x):
    n = len(x)
    if n < 2 or not np.isfinite(x[-1]):
        return np.nan
    return float(np.sum(x <= x[-1]) - 1) / float(n - 1)


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === Raw relative-strength ===

def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_10d_base_v001_signal(close, benchmark):
    """closeadj.pct_change(10) - benchmark.pct_change(10): 10-day outperformance."""
    return (close.pct_change(10) - benchmark.pct_change(10)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_60d_base_v002_signal(closeadj, benchmark):
    """closeadj.pct_change(60) - benchmark.pct_change(60): medium-term outperformance."""
    return (closeadj.pct_change(60) - benchmark.pct_change(60)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_200d_base_v003_signal(closeadj, benchmark):
    """closeadj.pct_change(200) - benchmark.pct_change(200): long-term outperformance."""
    return (closeadj.pct_change(200) - benchmark.pct_change(200)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_log_rs_ratio_base_v004_signal(closeadj, benchmark):
    """log(closeadj / benchmark) instantaneous log relative-strength level."""
    return np.log(closeadj / benchmark).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_cumret_ratio_45d_base_v005_signal(closeadj, benchmark):
    """(closeadj/closeadj.shift(45)) / (benchmark/benchmark.shift(45)) - 1.
    Cumulative outperformance ratio centered on zero."""
    rs = (closeadj / closeadj.shift(45)) / (benchmark / benchmark.shift(45))
    return (rs - 1.0).replace([np.inf, -np.inf], np.nan)


# === RS moving averages ===

def f29rs_f29_relative_strength_vs_benchmark_sma_logrs_20d_base_v006_signal(close, benchmark):
    """SMA(log(close/benchmark), 20) - log(close/benchmark) MA deviation."""
    rs = np.log(close / benchmark)
    return (rs - _sma(rs, 20)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_ema_logrs_50d_base_v007_signal(closeadj, benchmark):
    """log(closeadj/benchmark) - EMA(50) of same. Trend in RS series."""
    rs = np.log(closeadj / benchmark)
    return (rs - _ema(rs, 50)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_mad_30d_base_v008_signal(closeadj, benchmark):
    """Mean absolute deviation of log RS from its mean over 30d. RS dispersion."""
    rs = np.log(closeadj / benchmark)
    mu = rs.rolling(30, min_periods=30).mean()
    return (rs - mu).abs().rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_ema_diff_logrs_20_60_base_v009_signal(closeadj, benchmark):
    """EMA(20) - EMA(60) of log(closeadj/benchmark). RS MACD-like."""
    rs = np.log(closeadj / benchmark)
    return (_ema(rs, 20) - _ema(rs, 60)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_rank_120d_base_v010_signal(closeadj, benchmark):
    """Percentile rank of log(closeadj/benchmark) over 120 days."""
    rs = np.log(closeadj / benchmark)
    out = rs.rolling(120, min_periods=120).apply(
        lambda x: (np.sum(x <= x[-1]) - 1) / (len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    )
    return out.replace([np.inf, -np.inf], np.nan)


# === Rolling beta and alpha ===

def f29rs_f29_relative_strength_vs_benchmark_beta_45d_base_v011_signal(closeadj, benchmark):
    """Rolling beta(45) of stock returns on benchmark returns: cov/var."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(45, min_periods=45).cov(rb)
    var = rb.rolling(45, min_periods=45).var()
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_beta_120d_base_v012_signal(closeadj, benchmark):
    """Rolling beta(120). Longer-window beta differs in dynamics from 45d."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(120, min_periods=120).cov(rb)
    var = rb.rolling(120, min_periods=120).var()
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_alpha_60d_base_v013_signal(closeadj, benchmark):
    """Jensen alpha = mean(stock_ret) - beta * mean(bench_ret) over 60d."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(60, min_periods=60).cov(rb)
    var = rb.rolling(60, min_periods=60).var()
    beta = cov / var.replace(0.0, np.nan)
    return (rs.rolling(60, min_periods=60).mean() - beta * rb.rolling(60, min_periods=60).mean()).replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_beta_zscore_60d_base_v014_signal(closeadj, benchmark):
    """Z-score of rolling beta(30) over a 60d horizon. Beta stability."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(30, min_periods=30).cov(rb)
    var = rb.rolling(30, min_periods=30).var()
    beta = cov / var.replace(0.0, np.nan)
    mu = beta.rolling(60, min_periods=60).mean()
    sd = beta.rolling(60, min_periods=60).std(ddof=0)
    return ((beta - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_idio_vol_80d_base_v015_signal(closeadj, benchmark):
    """Idiosyncratic volatility: std(stock_ret - beta * bench_ret) over 80d."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(80, min_periods=80).cov(rb)
    var = rb.rolling(80, min_periods=80).var()
    beta = cov / var.replace(0.0, np.nan)
    resid = rs - beta * rb
    return resid.rolling(80, min_periods=80).std(ddof=0).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_beta_rank_120d_base_v016_signal(closeadj, benchmark):
    """Percentile rank of rolling beta(30) within trailing 120d window."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(30, min_periods=30).cov(rb)
    var = rb.rolling(30, min_periods=30).var()
    beta = cov / var.replace(0.0, np.nan)
    out = beta.rolling(120, min_periods=120).apply(
        lambda x: (np.sum(x <= x[-1]) - 1) / (len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    )
    return out.replace([np.inf, -np.inf], np.nan)


# === Correlation features ===

def f29rs_f29_relative_strength_vs_benchmark_corr_returns_30d_base_v017_signal(close, benchmark):
    """Rolling Pearson correlation of stock returns vs benchmark returns (30d)."""
    return close.pct_change().rolling(30, min_periods=30).corr(benchmark.pct_change()).replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_corr_abs_returns_60d_base_v018_signal(closeadj, benchmark):
    """Correlation of |stock_ret| and |bench_ret| over 60d. Co-movement in magnitude
    (volatility comovement) vs sign — different from level/return correlation."""
    rs = closeadj.pct_change().abs()
    rb = benchmark.pct_change().abs()
    return rs.rolling(60, min_periods=60).corr(rb).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_spearman_corr_60d_base_v019_signal(closeadj, benchmark):
    """Rolling Spearman rank correlation of returns over 60d."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    return _spearman_rolling(rs, rb, 60)


def _spearman_rolling(a: pd.Series, b: pd.Series, n: int) -> pd.Series:
    out = pd.Series(np.nan, index=a.index, dtype=float)
    av = a.values
    bv = b.values
    for i in range(n - 1, len(a)):
        wa = av[i - n + 1: i + 1]
        wb = bv[i - n + 1: i + 1]
        if not (np.all(np.isfinite(wa)) and np.all(np.isfinite(wb))):
            continue
        ra = pd.Series(wa).rank().values
        rbv = pd.Series(wb).rank().values
        mra = ra.mean(); mrb = rbv.mean()
        num = np.sum((ra - mra) * (rbv - mrb))
        den = np.sqrt(np.sum((ra - mra) ** 2) * np.sum((rbv - mrb) ** 2))
        if den <= 0.0:
            continue
        out.iat[i] = float(num / den)
    return out.replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_leadlag_corr_45d_base_v020_signal(closeadj, benchmark):
    """Corr(stock_ret_t, bench_ret_{t-3}) over 45d. Lead-lag: does benchmark lead stock?"""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change().shift(3)
    return rs.rolling(45, min_periods=45).corr(rb).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_corr_levels_80d_base_v021_signal(closeadj, benchmark):
    """Correlation of log(close) and log(benchmark) LEVELS over 80d."""
    return np.log(closeadj).rolling(80, min_periods=80).corr(np.log(benchmark)).replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_corr_diff_30_120_base_v022_signal(closeadj, benchmark):
    """Short-window 30d return corr minus long-window 120d return corr.
    Captures regime change in correlation."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    c30 = rs.rolling(30, min_periods=30).corr(rb)
    c120 = rs.rolling(120, min_periods=120).corr(rb)
    return (c30 - c120).replace([np.inf, -np.inf], np.nan)


# === Tracking error / information ratio ===

def f29rs_f29_relative_strength_vs_benchmark_tracking_err_30d_base_v023_signal(close, benchmark):
    """Tracking error: std of (stock_ret - bench_ret) over 30d."""
    diff = close.pct_change() - benchmark.pct_change()
    return diff.rolling(30, min_periods=30).std(ddof=0).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_tracking_err_120d_base_v024_signal(closeadj, benchmark):
    """Tracking error over 120d. Long-window persistence of active risk."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return diff.rolling(120, min_periods=120).std(ddof=0).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_info_ratio_200d_base_v025_signal(closeadj, benchmark):
    """Information ratio: mean / std of active return over 200d (long horizon distinct from 60d cluster)."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    mu = diff.rolling(200, min_periods=200).mean()
    sd = diff.rolling(200, min_periods=200).std(ddof=0)
    return (mu / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_return_zscore_80d_base_v026_signal(closeadj, benchmark):
    """Z-score of mean active return: ((rs_mean - long_mean) / long_std) over 80d.
    Different from info ratio: uses long-window normalization."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    mu_s = diff.rolling(20, min_periods=20).mean()
    mu_l = diff.rolling(80, min_periods=80).mean()
    sd_l = diff.rolling(80, min_periods=80).std(ddof=0)
    return ((mu_s - mu_l) / sd_l.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Up/Down capture ===

def f29rs_f29_relative_strength_vs_benchmark_up_capture_60d_base_v027_signal(closeadj, benchmark):
    """Sum(stock_ret on bench-up days) / Sum(bench_ret on bench-up days) over 60d.
    >1 means stock outperforms in bench rallies."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    up_mask = (rb > 0).astype(float)
    num = (rs * up_mask).rolling(60, min_periods=60).sum()
    den = (rb * up_mask).rolling(60, min_periods=60).sum()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_down_capture_60d_base_v028_signal(closeadj, benchmark):
    """Down-capture: stock ret sum / bench ret sum on bench-DOWN days.
    <1 (positive ratio) means stock falls less in selloffs."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    dn_mask = (rb < 0).astype(float)
    num = (rs * dn_mask).rolling(60, min_periods=60).sum()
    den = (rb * dn_mask).rolling(60, min_periods=60).sum()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_up_minus_down_capture_90d_base_v029_signal(closeadj, benchmark):
    """Up-capture minus Down-capture (90d). Positive when stock is asymmetric in its favor."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    up = (rb > 0).astype(float)
    dn = (rb < 0).astype(float)
    nu = (rs * up).rolling(90, min_periods=90).sum() / (rb * up).rolling(90, min_periods=90).sum().replace(0.0, np.nan)
    nd = (rs * dn).rolling(90, min_periods=90).sum() / (rb * dn).rolling(90, min_periods=90).sum().replace(0.0, np.nan)
    return (nu - nd).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_up_day_outperf_frac_45d_base_v030_signal(closeadj, benchmark):
    """Fraction of bench-up days where stock_ret > bench_ret, in trailing 45d."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    up_mask = (rb > 0).astype(float)
    outp = ((rs > rb) & (rb > 0)).astype(float)
    num = outp.rolling(45, min_periods=45).sum()
    den = up_mask.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_dn_day_outperf_frac_60d_base_v031_signal(closeadj, benchmark):
    """Fraction of bench-down days where stock_ret > bench_ret (defense), trailing 60d."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    dn_mask = (rb < 0).astype(float)
    outp = ((rs > rb) & (rb < 0)).astype(float)
    num = outp.rolling(60, min_periods=60).sum()
    den = dn_mask.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === Outperformance streaks/counts ===

def f29rs_f29_relative_strength_vs_benchmark_outperf_count_30d_base_v032_signal(close, benchmark):
    """Count of days in trailing 30d where stock_ret > bench_ret. Integer."""
    diff = close.pct_change() - benchmark.pct_change()
    return (diff > 0).astype(float).rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_outperf_count_120d_base_v033_signal(closeadj, benchmark):
    """Count of trailing 120d where stock outperformed benchmark."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return (diff > 0).astype(float).rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_outperf_streak_base_v034_signal(close, benchmark):
    """Current consecutive run length of outperformance days (stock_ret > bench_ret)."""
    diff = close.pct_change() - benchmark.pct_change()
    dvals = diff.values
    out = np.full(len(dvals), np.nan, dtype=float)
    run = 0
    for i in range(len(dvals)):
        if not np.isfinite(dvals[i]):
            continue
        if dvals[i] > 0:
            run += 1
        else:
            run = 0
        out[i] = float(run)
    return pd.Series(out, index=close.index, dtype=float).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_underperf_streak_base_v035_signal(closeadj, benchmark):
    """Current consecutive run of UNDERperformance days (stock_ret <= bench_ret)."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    dvals = diff.values
    out = np.full(len(dvals), np.nan, dtype=float)
    run = 0
    for i in range(len(dvals)):
        if not np.isfinite(dvals[i]):
            continue
        if dvals[i] < 0:
            run += 1
        else:
            run = 0
        out[i] = float(run)
    return pd.Series(out, index=closeadj.index, dtype=float).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_max_streak_outperf_60d_base_v036_signal(closeadj, benchmark):
    """Maximum consecutive outperformance run length seen within the trailing 60-day window."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    sig = (diff > 0).astype(float).where(diff.notna())

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

    arr = sig.rolling(60, min_periods=60).apply(_max_run, raw=True)
    return arr.replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_outperf_excess_pct_50d_base_v037_signal(closeadj, benchmark):
    """(outperf_count / 50d) - 0.5: signed outperformance frequency excess."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    cnt = (diff > 0).astype(float).rolling(50, min_periods=50).sum()
    return (cnt / 50.0 - 0.5).replace([np.inf, -np.inf], np.nan)


# === Drawdown comparison ===

def f29rs_f29_relative_strength_vs_benchmark_dd_diff_60d_base_v038_signal(closeadj, benchmark):
    """Stock drawdown(60d) - benchmark drawdown(60d). More negative = stock weaker."""
    sdd = _rolling_drawdown(closeadj, 60)
    bdd = _rolling_drawdown(benchmark, 60)
    return (sdd - bdd).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_dd_diff_200d_base_v039_signal(closeadj, benchmark):
    """Stock vs benchmark drawdown difference at 200d."""
    sdd = _rolling_drawdown(closeadj, 200)
    bdd = _rolling_drawdown(benchmark, 200)
    return (sdd - bdd).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_dd_ratio_120d_base_v040_signal(closeadj, benchmark):
    """Ratio: stock_drawdown / benchmark_drawdown over 120d (both <= 0)."""
    sdd = _rolling_drawdown(closeadj, 120)
    bdd = _rolling_drawdown(benchmark, 120)
    return (sdd / bdd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === RS oscillators (RSI / stoch) ===

def f29rs_f29_relative_strength_vs_benchmark_rs_willr_14d_base_v041_signal(close, benchmark):
    """Williams %R style of log RS over 14d: (rs - hi) / (hi - lo). In [-1,0]; -0.5 = mid."""
    rs = np.log(close / benchmark)
    hi = rs.rolling(14, min_periods=14).max()
    lo = rs.rolling(14, min_periods=14).min()
    return ((rs - hi) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_stoch_30d_base_v042_signal(closeadj, benchmark):
    """Stochastic of log RS over 30d: (rs - min) / (max - min) - 0.5."""
    rs = np.log(closeadj / benchmark)
    hi = rs.rolling(30, min_periods=30).max()
    lo = rs.rolling(30, min_periods=30).min()
    return ((rs - lo) / (hi - lo).replace(0.0, np.nan) - 0.5).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_cmo_20d_base_v043_signal(closeadj, benchmark):
    """Chande Momentum Oscillator of log RS over 20d: (sum_up - sum_dn) / (sum_up + sum_dn)."""
    rs = np.log(closeadj / benchmark)
    d = rs.diff()
    up = d.where(d > 0, 0.0)
    dn = (-d).where(d < 0, 0.0)
    su = up.rolling(20, min_periods=20).sum()
    sd = dn.rolling(20, min_periods=20).sum()
    return ((su - sd) / (su + sd).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === RS momentum (slope / curvature / acceleration of RS) ===

def f29rs_f29_relative_strength_vs_benchmark_rs_hurst_60d_base_v044_signal(closeadj, benchmark):
    """Hurst exponent (R/S) of log RS series over 60d. Memory/trendiness of RS line."""
    rs = np.log(closeadj / benchmark)

    def _hurst(x):
        n = len(x)
        if n < 16 or not np.all(np.isfinite(x)):
            return np.nan
        mean = x.mean()
        dev = x - mean
        z = np.cumsum(dev)
        R = z.max() - z.min()
        S = x.std(ddof=0)
        if S == 0.0 or R / S <= 0.0:
            return np.nan
        return float(np.log(R / S) / np.log(n))

    return rs.rolling(60, min_periods=60).apply(_hurst, raw=True).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_efficiency_50d_base_v045_signal(closeadj, benchmark):
    """Kaufman efficiency on log RS over 50d: |rs(t) - rs(t-50)| / sum(|drs|) within window.
    Bounded [0,1]; distinct from slope and z-score."""
    rs = np.log(closeadj / benchmark)
    num = (rs - rs.shift(50)).abs()
    den = rs.diff().abs().rolling(50, min_periods=50).sum()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_curv_45d_base_v046_signal(closeadj, benchmark):
    """Curvature of log RS: rs - 2*rs.shift(k) + rs.shift(2k), k=22 over 45d window."""
    rs = np.log(closeadj / benchmark)
    return (rs - 2.0 * rs.shift(22) + rs.shift(44)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_accel_diff_base_v047_signal(closeadj, benchmark):
    """(rs - rs.shift(5)) - (rs.shift(5) - rs.shift(10)): acceleration of log RS."""
    rs = np.log(closeadj / benchmark)
    return ((rs - rs.shift(5)) - (rs.shift(5) - rs.shift(10))).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_slope_regression_30d_base_v048_signal(closeadj, benchmark):
    """Linear-regression slope of log RS vs time over 30d, normalized by |mean| of RS."""
    rs = np.log(closeadj / benchmark)

    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx)); vt = np.sum((t - mt) ** 2)
        if vt == 0.0 or not np.isfinite(mx) or abs(mx) < 1e-12:
            return np.nan
        return float(cov / vt)

    return rs.rolling(30, min_periods=30).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


# === Discrete states / 4-state regime ===

def f29rs_f29_relative_strength_vs_benchmark_sign_outperf_base_v049_signal(close, benchmark):
    """sign(stock_ret - bench_ret): +1 outperform, -1 underperform, 0 tie. Discrete daily."""
    diff = close.pct_change() - benchmark.pct_change()
    return np.sign(diff).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_state_4regime_base_v050_signal(closeadj, benchmark):
    """4-state regime in {0,1,2,3} based on (stock_up?, bench_up?) over 20d windows.
    0: both up; 1: stock up & bench down; 2: stock down & bench up; 3: both down."""
    s_ret = closeadj / closeadj.shift(20) - 1.0
    b_ret = benchmark / benchmark.shift(20) - 1.0
    s_up = (s_ret > 0).astype(int)
    b_up = (b_ret > 0).astype(int)
    out = (1 - s_up) * 2 + (1 - b_up)
    return out.astype(float).where(s_ret.notna() & b_ret.notna()).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_outperf_uptrend_flag_base_v051_signal(close, benchmark):
    """+1 if outperform AND stock uptrend (>SMA20); -1 if underperform AND stock downtrend; else 0."""
    diff = close.pct_change(10) - benchmark.pct_change(10)
    up = (close > _sma(close, 20)).astype(int) - (close <= _sma(close, 20)).astype(int)
    out = pd.Series(0.0, index=close.index, dtype=float)
    out = out.where(diff.isna(), 0.0)
    out = out.mask((diff > 0) & (up > 0), 1.0)
    out = out.mask((diff < 0) & (up < 0), -1.0)
    return out.where(diff.notna()).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_decouple_flag_30d_base_v052_signal(closeadj, benchmark):
    """1 on days where |stock_ret - bench_ret| > 2x rolling std (30d) of that diff. Decoupling indicator."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    sd = diff.rolling(30, min_periods=30).std(ddof=0)
    return ((diff.abs() > 2.0 * sd).astype(float).where(sd.notna())).replace([np.inf, -np.inf], np.nan)


# === Bounded transforms ===

def f29rs_f29_relative_strength_vs_benchmark_arctan_active_return_sum_30d_base_v053_signal(closeadj, benchmark):
    """arctan(sum of active returns over 30d * scale). Bounded version of short-term active return.
    Different window from raw pctdiff_60d so not a duplicate."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    s = diff.rolling(30, min_periods=30).sum()
    return np.arctan(s * 10.0).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_tanh_idiovol_ratio_80d_base_v054_signal(closeadj, benchmark):
    """tanh(idio_vol / total_stock_vol - 0.5) over 80d. Bounded fraction of stock vol that
    is non-systematic. Distinct from beta and alpha."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(80, min_periods=80).cov(rb)
    var = rb.rolling(80, min_periods=80).var()
    beta = cov / var.replace(0.0, np.nan)
    resid = rs - beta * rb
    ivol = resid.rolling(80, min_periods=80).std(ddof=0)
    tvol = rs.rolling(80, min_periods=80).std(ddof=0).replace(0.0, np.nan)
    return np.tanh(ivol / tvol - 0.5).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_sigmoid_tracking_resid_60d_base_v055_signal(closeadj, benchmark):
    """sigmoid of (residual / tracking_err - 1) over 60d. Bounded measure of unusual residual size.
    Distinct from alpha (uses residual std rather than mean)."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(60, min_periods=60).cov(rb)
    var = rb.rolling(60, min_periods=60).var()
    beta = cov / var.replace(0.0, np.nan)
    resid = rs - beta * rb
    rstd = resid.rolling(60, min_periods=60).std(ddof=0)
    tstd = (rs - rb).rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    z = rstd / tstd - 1.0
    return (1.0 / (1.0 + np.exp(-z * 5.0)) - 0.5).replace([np.inf, -np.inf], np.nan)


# === Risk-adjusted differentials ===

def f29rs_f29_relative_strength_vs_benchmark_vol_ratio_60d_base_v056_signal(closeadj, benchmark):
    """log(std(stock_ret,60) / std(bench_ret,60)). Relative volatility — distinct from
    mu-based Sharpe-diff; isolates risk."""
    rs = closeadj.pct_change().rolling(60, min_periods=60).std(ddof=0)
    rb = benchmark.pct_change().rolling(60, min_periods=60).std(ddof=0)
    return np.log(rs / rb.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_sortino_diff_90d_base_v057_signal(closeadj, benchmark):
    """Sortino(stock,90) - Sortino(bench,90): mu / downside_std (downside std uses min_periods=10)."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    ds_rs = rs.where(rs < 0).rolling(90, min_periods=10).std(ddof=0)
    ds_rb = rb.where(rb < 0).rolling(90, min_periods=10).std(ddof=0)
    sr_rs = rs.rolling(90, min_periods=90).mean() / ds_rs.replace(0.0, np.nan)
    sr_rb = rb.rolling(90, min_periods=90).mean() / ds_rb.replace(0.0, np.nan)
    return (sr_rs - sr_rb).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_treynor_60d_base_v058_signal(closeadj, benchmark):
    """Treynor-ish: alpha(60) / beta(60). Excess return per unit of systematic risk."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov = rs.rolling(60, min_periods=60).cov(rb)
    var = rb.rolling(60, min_periods=60).var()
    beta = cov / var.replace(0.0, np.nan)
    alpha = rs.rolling(60, min_periods=60).mean() - beta * rb.rolling(60, min_periods=60).mean()
    return (alpha / beta.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Correlation regime / high-low corr distinction ===

def f29rs_f29_relative_strength_vs_benchmark_corr_zscore_60d_base_v059_signal(closeadj, benchmark):
    """Z-score of rolling 20d return correlation over a 60d window. Spikes flag regime change."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    c = rs.rolling(20, min_periods=20).corr(rb)
    mu = c.rolling(60, min_periods=60).mean()
    sd = c.rolling(60, min_periods=60).std(ddof=0)
    return ((c - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_high_corr_frac_120d_base_v060_signal(closeadj, benchmark):
    """Fraction of trailing 120d where 20d return correlation exceeds its 120d median."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    c = rs.rolling(20, min_periods=20).corr(rb)
    med = c.rolling(120, min_periods=120).median()
    return (c > med).astype(float).where(med.notna()).rolling(120, min_periods=120).mean().replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_decouple_days_count_80d_base_v061_signal(closeadj, benchmark):
    """Count of trailing 80d where sign(stock_ret) != sign(bench_ret). Decoupling count."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    mismatch = (np.sign(rs) != np.sign(rb)).astype(float)
    return mismatch.rolling(80, min_periods=80).sum().replace([np.inf, -np.inf], np.nan)


# === Additional diverse RS features ===

def f29rs_f29_relative_strength_vs_benchmark_rs_volatility_45d_base_v062_signal(closeadj, benchmark):
    """std of log RS series over 45d. RS-line volatility."""
    rs = np.log(closeadj / benchmark)
    return rs.rolling(45, min_periods=45).std(ddof=0).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_50d_base_v063_signal(closeadj, benchmark):
    """Z-score of log RS over 50d window."""
    rs = np.log(closeadj / benchmark)
    mu = rs.rolling(50, min_periods=50).mean()
    sd = rs.rolling(50, min_periods=50).std(ddof=0)
    return ((rs - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_bench_corr_lag5_30d_base_v064_signal(close, benchmark):
    """Corr(stock_ret_t, bench_ret_{t+5}) over 30d. Lead-lag: does stock lead?"""
    rs = close.pct_change()
    rb = benchmark.pct_change().shift(-5)
    return rs.rolling(30, min_periods=30).corr(rb).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_return_skew_80d_base_v065_signal(closeadj, benchmark):
    """Skewness of (stock_ret - bench_ret) over 80d."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return diff.rolling(80, min_periods=80).skew().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_active_return_kurt_80d_base_v066_signal(closeadj, benchmark):
    """Kurtosis of (stock_ret - bench_ret) over 80d."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return diff.rolling(80, min_periods=80).kurt().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p75_50d_base_v067_signal(closeadj, benchmark):
    """75th percentile of active return magnitude over 50d. Captures right-tail outperformance."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return diff.rolling(50, min_periods=50).quantile(0.75).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p25_50d_base_v068_signal(closeadj, benchmark):
    """25th percentile of active return over 50d. Left-tail / worst-case underperformance."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return diff.rolling(50, min_periods=50).quantile(0.25).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_outperf_iqr_50d_base_v069_signal(closeadj, benchmark):
    """IQR of active return over 50d: p75 - p25. Active-risk-like dispersion."""
    diff = closeadj.pct_change() - benchmark.pct_change()
    return (diff.rolling(50, min_periods=50).quantile(0.75) - diff.rolling(50, min_periods=50).quantile(0.25)).replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_rs_new_high_count_60d_base_v070_signal(closeadj, benchmark):
    """Count of trailing 60d where log RS hit a new 60-day rolling max. Discrete momentum count."""
    rs = np.log(closeadj / benchmark)
    rmax = rs.rolling(60, min_periods=60).max()
    return ((rs >= rmax - 1e-12).astype(float).where(rmax.notna())).rolling(60, min_periods=60).sum().replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_rs_argmax_60d_base_v071_signal(closeadj, benchmark):
    """Position (0..59) of max log(RS) within trailing 60-day window. Recency of peak RS."""
    rs = np.log(closeadj / benchmark)

    def _argmax(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(np.argmax(x))

    return rs.rolling(60, min_periods=60).apply(_argmax, raw=True).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_argmin_120d_base_v072_signal(closeadj, benchmark):
    """Position (0..119) of min log(RS) within trailing 120-day window. Recency of trough."""
    rs = np.log(closeadj / benchmark)

    def _argmin(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(np.argmin(x))

    return rs.rolling(120, min_periods=120).apply(_argmin, raw=True).replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_rs_above_ma_count_80d_base_v073_signal(closeadj, benchmark):
    """Count of trailing 80d where log(RS) > SMA(log(RS), 40). RS bull-state count."""
    rs = np.log(closeadj / benchmark)
    ma = _sma(rs, 40)
    return (rs > ma).astype(float).rolling(80, min_periods=80).sum().replace([np.inf, -np.inf], np.nan)


def f29rs_f29_relative_strength_vs_benchmark_beta_diff_45_120_base_v074_signal(closeadj, benchmark):
    """beta(45) - beta(120). Beta term-structure shift."""
    rs = closeadj.pct_change()
    rb = benchmark.pct_change()
    cov45 = rs.rolling(45, min_periods=45).cov(rb)
    var45 = rb.rolling(45, min_periods=45).var()
    cov120 = rs.rolling(120, min_periods=120).cov(rb)
    var120 = rb.rolling(120, min_periods=120).var()
    return (cov45 / var45.replace(0.0, np.nan) - cov120 / var120.replace(0.0, np.nan)).replace(
        [np.inf, -np.inf], np.nan
    )


def f29rs_f29_relative_strength_vs_benchmark_rs_above_zero_streak_base_v075_signal(closeadj, benchmark):
    """Current consecutive run length where log(closeadj/benchmark) > rolling mean(120d).
    Persistent above-mean RS state. Reset on cross below."""
    rs = np.log(closeadj / benchmark)
    mu = rs.rolling(120, min_periods=120).mean()
    rsv = rs.values; muv = mu.values
    out = np.full(len(rsv), np.nan, dtype=float)
    run = 0
    for i in range(len(rsv)):
        if not (np.isfinite(muv[i]) and np.isfinite(rsv[i])):
            continue
        if rsv[i] > muv[i]:
            run += 1
        else:
            run = 0
        out[i] = float(run)
    return pd.Series(out, index=closeadj.index, dtype=float).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f29_relative_strength_vs_benchmark_base_001_075_REGISTRY = {
    "f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_10d_base_v001_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_10d_base_v001_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_60d_base_v002_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_60d_base_v002_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_200d_base_v003_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_200d_base_v003_signal},
    "f29rs_f29_relative_strength_vs_benchmark_log_rs_ratio_base_v004_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_log_rs_ratio_base_v004_signal},
    "f29rs_f29_relative_strength_vs_benchmark_cumret_ratio_45d_base_v005_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_cumret_ratio_45d_base_v005_signal},
    "f29rs_f29_relative_strength_vs_benchmark_sma_logrs_20d_base_v006_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_sma_logrs_20d_base_v006_signal},
    "f29rs_f29_relative_strength_vs_benchmark_ema_logrs_50d_base_v007_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_ema_logrs_50d_base_v007_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_mad_30d_base_v008_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_mad_30d_base_v008_signal},
    "f29rs_f29_relative_strength_vs_benchmark_ema_diff_logrs_20_60_base_v009_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_ema_diff_logrs_20_60_base_v009_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_rank_120d_base_v010_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_rank_120d_base_v010_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_45d_base_v011_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_45d_base_v011_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_120d_base_v012_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_120d_base_v012_signal},
    "f29rs_f29_relative_strength_vs_benchmark_alpha_60d_base_v013_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_alpha_60d_base_v013_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_zscore_60d_base_v014_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_zscore_60d_base_v014_signal},
    "f29rs_f29_relative_strength_vs_benchmark_idio_vol_80d_base_v015_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_idio_vol_80d_base_v015_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_rank_120d_base_v016_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_rank_120d_base_v016_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_returns_30d_base_v017_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_returns_30d_base_v017_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_abs_returns_60d_base_v018_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_abs_returns_60d_base_v018_signal},
    "f29rs_f29_relative_strength_vs_benchmark_spearman_corr_60d_base_v019_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_spearman_corr_60d_base_v019_signal},
    "f29rs_f29_relative_strength_vs_benchmark_leadlag_corr_45d_base_v020_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_leadlag_corr_45d_base_v020_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_levels_80d_base_v021_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_levels_80d_base_v021_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_diff_30_120_base_v022_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_diff_30_120_base_v022_signal},
    "f29rs_f29_relative_strength_vs_benchmark_tracking_err_30d_base_v023_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_tracking_err_30d_base_v023_signal},
    "f29rs_f29_relative_strength_vs_benchmark_tracking_err_120d_base_v024_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_tracking_err_120d_base_v024_signal},
    "f29rs_f29_relative_strength_vs_benchmark_info_ratio_200d_base_v025_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_info_ratio_200d_base_v025_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_return_zscore_80d_base_v026_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_return_zscore_80d_base_v026_signal},
    "f29rs_f29_relative_strength_vs_benchmark_up_capture_60d_base_v027_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_up_capture_60d_base_v027_signal},
    "f29rs_f29_relative_strength_vs_benchmark_down_capture_60d_base_v028_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_down_capture_60d_base_v028_signal},
    "f29rs_f29_relative_strength_vs_benchmark_up_minus_down_capture_90d_base_v029_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_up_minus_down_capture_90d_base_v029_signal},
    "f29rs_f29_relative_strength_vs_benchmark_up_day_outperf_frac_45d_base_v030_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_up_day_outperf_frac_45d_base_v030_signal},
    "f29rs_f29_relative_strength_vs_benchmark_dn_day_outperf_frac_60d_base_v031_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_dn_day_outperf_frac_60d_base_v031_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_count_30d_base_v032_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_count_30d_base_v032_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_count_120d_base_v033_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_count_120d_base_v033_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_streak_base_v034_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_streak_base_v034_signal},
    "f29rs_f29_relative_strength_vs_benchmark_underperf_streak_base_v035_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_underperf_streak_base_v035_signal},
    "f29rs_f29_relative_strength_vs_benchmark_max_streak_outperf_60d_base_v036_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_max_streak_outperf_60d_base_v036_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_excess_pct_50d_base_v037_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_excess_pct_50d_base_v037_signal},
    "f29rs_f29_relative_strength_vs_benchmark_dd_diff_60d_base_v038_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_dd_diff_60d_base_v038_signal},
    "f29rs_f29_relative_strength_vs_benchmark_dd_diff_200d_base_v039_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_dd_diff_200d_base_v039_signal},
    "f29rs_f29_relative_strength_vs_benchmark_dd_ratio_120d_base_v040_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_dd_ratio_120d_base_v040_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_willr_14d_base_v041_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_willr_14d_base_v041_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_stoch_30d_base_v042_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_stoch_30d_base_v042_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_cmo_20d_base_v043_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_cmo_20d_base_v043_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_hurst_60d_base_v044_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_hurst_60d_base_v044_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_efficiency_50d_base_v045_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_efficiency_50d_base_v045_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_curv_45d_base_v046_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_curv_45d_base_v046_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_accel_diff_base_v047_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_accel_diff_base_v047_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_slope_regression_30d_base_v048_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_slope_regression_30d_base_v048_signal},
    "f29rs_f29_relative_strength_vs_benchmark_sign_outperf_base_v049_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_sign_outperf_base_v049_signal},
    "f29rs_f29_relative_strength_vs_benchmark_state_4regime_base_v050_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_state_4regime_base_v050_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_uptrend_flag_base_v051_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_uptrend_flag_base_v051_signal},
    "f29rs_f29_relative_strength_vs_benchmark_decouple_flag_30d_base_v052_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_decouple_flag_30d_base_v052_signal},
    "f29rs_f29_relative_strength_vs_benchmark_arctan_active_return_sum_30d_base_v053_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_arctan_active_return_sum_30d_base_v053_signal},
    "f29rs_f29_relative_strength_vs_benchmark_tanh_idiovol_ratio_80d_base_v054_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_tanh_idiovol_ratio_80d_base_v054_signal},
    "f29rs_f29_relative_strength_vs_benchmark_sigmoid_tracking_resid_60d_base_v055_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_sigmoid_tracking_resid_60d_base_v055_signal},
    "f29rs_f29_relative_strength_vs_benchmark_vol_ratio_60d_base_v056_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_vol_ratio_60d_base_v056_signal},
    "f29rs_f29_relative_strength_vs_benchmark_sortino_diff_90d_base_v057_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_sortino_diff_90d_base_v057_signal},
    "f29rs_f29_relative_strength_vs_benchmark_treynor_60d_base_v058_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_treynor_60d_base_v058_signal},
    "f29rs_f29_relative_strength_vs_benchmark_corr_zscore_60d_base_v059_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_corr_zscore_60d_base_v059_signal},
    "f29rs_f29_relative_strength_vs_benchmark_high_corr_frac_120d_base_v060_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_high_corr_frac_120d_base_v060_signal},
    "f29rs_f29_relative_strength_vs_benchmark_decouple_days_count_80d_base_v061_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_decouple_days_count_80d_base_v061_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_volatility_45d_base_v062_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_volatility_45d_base_v062_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_zscore_50d_base_v063_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_zscore_50d_base_v063_signal},
    "f29rs_f29_relative_strength_vs_benchmark_bench_corr_lag5_30d_base_v064_signal": {"inputs": ["close", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_bench_corr_lag5_30d_base_v064_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_return_skew_80d_base_v065_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_return_skew_80d_base_v065_signal},
    "f29rs_f29_relative_strength_vs_benchmark_active_return_kurt_80d_base_v066_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_active_return_kurt_80d_base_v066_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p75_50d_base_v067_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p75_50d_base_v067_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p25_50d_base_v068_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p25_50d_base_v068_signal},
    "f29rs_f29_relative_strength_vs_benchmark_outperf_iqr_50d_base_v069_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_outperf_iqr_50d_base_v069_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_new_high_count_60d_base_v070_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_new_high_count_60d_base_v070_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_argmax_60d_base_v071_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_argmax_60d_base_v071_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_argmin_120d_base_v072_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_argmin_120d_base_v072_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_above_ma_count_80d_base_v073_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_above_ma_count_80d_base_v073_signal},
    "f29rs_f29_relative_strength_vs_benchmark_beta_diff_45_120_base_v074_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_beta_diff_45_120_base_v074_signal},
    "f29rs_f29_relative_strength_vs_benchmark_rs_above_zero_streak_base_v075_signal": {"inputs": ["closeadj", "benchmark"], "func": f29rs_f29_relative_strength_vs_benchmark_rs_above_zero_streak_base_v075_signal},
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
    for name, entry in f29_relative_strength_vs_benchmark_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
