"""f29 slope 001-150 (1st derivative). Each fn inlines its RS base formula."""
from __future__ import annotations
import numpy as np
import pandas as pd
def _sma(s, n): return s.rolling(n, min_periods=n).mean()
def _r(x): return x.replace([np.inf, -np.inf], np.nan)
def _ema(s, n): return s.ewm(span=n, adjust=False, min_periods=n).mean()
def _wma(s, n):
    w = np.arange(1, n + 1, dtype=float); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)
def _wilder(s, n): return s.ewm(alpha=1.0/float(n), adjust=False, min_periods=n).mean()
def _dema(s, n):
    e1 = _ema(s, n); e2 = _ema(e1, n); return 2.0 * e1 - e2
def _tema(s, n):
    e1 = _ema(s, n); e2 = _ema(e1, n); e3 = _ema(e2, n); return 3.0 * e1 - 3.0 * e2 + e3
def _rdd(s, n):
    return (s / s.rolling(n, min_periods=n).max()) - 1.0
def _streak_up(x):
    out = np.full(len(x), np.nan, dtype=float); r = 0
    for i in range(len(x)):
        if not np.isfinite(x[i]): continue
        r = r + 1 if x[i] > 0 else 0
        out[i] = float(r)
    return out
def _streak_dn(x):
    out = np.full(len(x), np.nan, dtype=float); r = 0
    for i in range(len(x)):
        if not np.isfinite(x[i]): continue
        r = r + 1 if x[i] < 0 else 0
        out[i] = float(r)
    return out
def _max_run(x):
    if not np.all(np.isfinite(x)): return np.nan
    m = 0; cur = 0
    for v in x:
        if v > 0.5:
            cur += 1
            if cur > m: m = cur
        else:
            cur = 0
    return float(m)
def _spearman(a, b, n):
    out = pd.Series(np.nan, index=a.index, dtype=float)
    av = a.values; bv = b.values
    for i in range(n - 1, len(a)):
        wa = av[i-n+1:i+1]; wb = bv[i-n+1:i+1]
        if not (np.all(np.isfinite(wa)) and np.all(np.isfinite(wb))): continue
        ra = pd.Series(wa).rank().values; rbv = pd.Series(wb).rank().values
        mra = ra.mean(); mrb = rbv.mean()
        num = np.sum((ra-mra)*(rbv-mrb)); den = np.sqrt(np.sum((ra-mra)**2)*np.sum((rbv-mrb)**2))
        if den <= 0.0: continue
        out.iat[i] = float(num/den)
    return out

# Features 001-150 (slopes) --------------------------------------------------
def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_10d_slope_v001_signal(close, benchmark):
    b = close.pct_change(10) - benchmark.pct_change(10)
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_60d_slope_v002_signal(closeadj, benchmark):
    b = closeadj.pct_change(60) - benchmark.pct_change(60)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_200d_slope_v003_signal(closeadj, benchmark):
    b = closeadj.pct_change(200) - benchmark.pct_change(200)
    return _r(b.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_log_rs_ratio_slope_v004_signal(closeadj, benchmark):
    b = np.log(closeadj / benchmark)
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_cumret_ratio_45d_slope_v005_signal(closeadj, benchmark):
    b = (closeadj / closeadj.shift(45)) / (benchmark / benchmark.shift(45)) - 1.0
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_sma_logrs_20d_slope_v006_signal(close, benchmark):
    rs = np.log(close / benchmark); b = rs - _sma(rs, 20)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_ema_logrs_50d_slope_v007_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); b = rs - _ema(rs, 50)
    return _r((b.diff(21) / b.abs().rolling(21, min_periods=21).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_rs_mad_30d_slope_v008_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); mu = rs.rolling(30, min_periods=30).mean()
    b = (rs - mu).abs().rolling(30, min_periods=30).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_ema_diff_logrs_20_60_slope_v009_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); b = _ema(rs, 20) - _ema(rs, 60)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_rank_120d_slope_v010_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    b = rs.rolling(120, min_periods=120).apply(
        lambda x: (np.sum(x <= x[-1]) - 1) / (len(x) - 1) if len(x) > 1 else np.nan, raw=True)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_beta_45d_slope_v011_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(45, min_periods=45).cov(rb); var = rb.rolling(45, min_periods=45).var()
    b = cov / var.replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_beta_120d_slope_v012_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(120, min_periods=120).cov(rb); var = rb.rolling(120, min_periods=120).var()
    b = cov / var.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_alpha_60d_slope_v013_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(60, min_periods=60).cov(rb); var = rb.rolling(60, min_periods=60).var()
    beta = cov / var.replace(0.0, np.nan)
    b = rs.rolling(60, min_periods=60).mean() - beta * rb.rolling(60, min_periods=60).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_beta_zscore_60d_slope_v014_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(30, min_periods=30).cov(rb); var = rb.rolling(30, min_periods=30).var()
    beta = cov / var.replace(0.0, np.nan)
    mu = beta.rolling(60, min_periods=60).mean(); sd = beta.rolling(60, min_periods=60).std(ddof=0)
    b = (beta - mu) / sd.replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_idio_vol_80d_slope_v015_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(80, min_periods=80).cov(rb); var = rb.rolling(80, min_periods=80).var()
    beta = cov / var.replace(0.0, np.nan); resid = rs - beta * rb
    b = resid.rolling(80, min_periods=80).std(ddof=0)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_beta_rank_120d_slope_v016_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(30, min_periods=30).cov(rb); var = rb.rolling(30, min_periods=30).var()
    beta = cov / var.replace(0.0, np.nan)
    b = beta.rolling(120, min_periods=120).apply(
        lambda x: (np.sum(x <= x[-1]) - 1) / (len(x) - 1) if len(x) > 1 else np.nan, raw=True)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_corr_returns_30d_slope_v017_signal(close, benchmark):
    b = close.pct_change().rolling(30, min_periods=30).corr(benchmark.pct_change())
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_corr_abs_returns_60d_slope_v018_signal(closeadj, benchmark):
    a = closeadj.pct_change().abs(); bb = benchmark.pct_change().abs()
    b = a.rolling(60, min_periods=60).corr(bb)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_spearman_corr_60d_slope_v019_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    b = _spearman(rs, rb, 60)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_leadlag_corr_45d_slope_v020_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change().shift(3)
    b = rs.rolling(45, min_periods=45).corr(rb)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_corr_levels_80d_slope_v021_signal(closeadj, benchmark):
    b = np.log(closeadj).rolling(80, min_periods=80).corr(np.log(benchmark))
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_corr_diff_30_120_slope_v022_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    c30 = rs.rolling(30, min_periods=30).corr(rb); c120 = rs.rolling(120, min_periods=120).corr(rb)
    b = c30 - c120
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_tracking_err_30d_slope_v023_signal(close, benchmark):
    diff = close.pct_change() - benchmark.pct_change()
    b = diff.rolling(30, min_periods=30).std(ddof=0)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_tracking_err_120d_slope_v024_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(120, min_periods=120).std(ddof=0)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_info_ratio_200d_slope_v025_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    mu = diff.rolling(200, min_periods=200).mean(); sd = diff.rolling(200, min_periods=200).std(ddof=0)
    b = mu / sd.replace(0.0, np.nan)
    return _r((b.diff(21) / b.abs().rolling(21, min_periods=21).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_active_return_zscore_80d_slope_v026_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    mu_s = diff.rolling(20, min_periods=20).mean(); mu_l = diff.rolling(80, min_periods=80).mean()
    sd_l = diff.rolling(80, min_periods=80).std(ddof=0)
    b = (mu_s - mu_l) / sd_l.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_up_capture_60d_slope_v027_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    up = (rb > 0).astype(float)
    num = (rs * up).rolling(60, min_periods=60).sum(); den = (rb * up).rolling(60, min_periods=60).sum()
    b = num / den.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_down_capture_60d_slope_v028_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    dn = (rb < 0).astype(float)
    num = (rs * dn).rolling(60, min_periods=60).sum(); den = (rb * dn).rolling(60, min_periods=60).sum()
    b = num / den.replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_up_minus_down_capture_90d_slope_v029_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    up = (rb > 0).astype(float); dn = (rb < 0).astype(float)
    nu = (rs * up).rolling(90, min_periods=90).sum() / (rb * up).rolling(90, min_periods=90).sum().replace(0.0, np.nan)
    nd = (rs * dn).rolling(90, min_periods=90).sum() / (rb * dn).rolling(90, min_periods=90).sum().replace(0.0, np.nan)
    b = nu - nd
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_up_day_outperf_frac_45d_slope_v030_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    up = (rb > 0).astype(float)
    outp = ((rs > rb) & (rb > 0)).astype(float)
    num = outp.rolling(45, min_periods=45).sum()
    den = up.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    b = num / den
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_dn_day_outperf_frac_60d_slope_v031_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    dn = (rb < 0).astype(float)
    outp = ((rs > rb) & (rb < 0)).astype(float)
    num = outp.rolling(60, min_periods=60).sum()
    den = dn.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    b = num / den
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_outperf_count_30d_slope_v032_signal(close, benchmark):
    diff = close.pct_change() - benchmark.pct_change()
    b = (diff > 0).astype(float).rolling(30, min_periods=30).sum()
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_outperf_count_120d_slope_v033_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = (diff > 0).astype(float).rolling(120, min_periods=120).sum()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_outperf_streak_slope_v034_signal(close, benchmark):
    diff = close.pct_change() - benchmark.pct_change()
    b = pd.Series(_streak_up(diff.values), index=close.index, dtype=float)
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_underperf_streak_slope_v035_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = pd.Series(_streak_dn(diff.values), index=closeadj.index, dtype=float)
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_max_streak_outperf_60d_slope_v036_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    sig = (diff > 0).astype(float).where(diff.notna())
    b = sig.rolling(60, min_periods=60).apply(_max_run, raw=True)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_outperf_excess_pct_50d_slope_v037_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    cnt = (diff > 0).astype(float).rolling(50, min_periods=50).sum()
    b = cnt / 50.0 - 0.5
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_dd_diff_60d_slope_v038_signal(closeadj, benchmark):
    b = _rdd(closeadj, 60) - _rdd(benchmark, 60)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_dd_diff_200d_slope_v039_signal(closeadj, benchmark):
    b = _rdd(closeadj, 200) - _rdd(benchmark, 200)
    return _r(b.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_dd_ratio_120d_slope_v040_signal(closeadj, benchmark):
    b = _rdd(closeadj, 120) / _rdd(benchmark, 120).replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_willr_14d_slope_v041_signal(close, benchmark):
    rs = np.log(close / benchmark)
    hi = rs.rolling(14, min_periods=14).max(); lo = rs.rolling(14, min_periods=14).min()
    b = (rs - hi) / (hi - lo).replace(0.0, np.nan)
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_rs_stoch_30d_slope_v042_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    hi = rs.rolling(30, min_periods=30).max(); lo = rs.rolling(30, min_periods=30).min()
    b = (rs - lo) / (hi - lo).replace(0.0, np.nan) - 0.5
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_cmo_20d_slope_v043_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); d = rs.diff()
    up = d.where(d > 0, 0.0); dn = (-d).where(d < 0, 0.0)
    su = up.rolling(20, min_periods=20).sum(); sd = dn.rolling(20, min_periods=20).sum()
    b = (su - sd) / (su + sd).replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_hurst_60d_slope_v044_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    def _h(x):
        if not np.all(np.isfinite(x)): return np.nan
        m = x.mean(); dev = x - m; z = np.cumsum(dev)
        R = z.max() - z.min(); S = x.std(ddof=0)
        if S == 0.0 or R/S <= 0.0: return np.nan
        return float(np.log(R/S) / np.log(len(x)))
    b = rs.rolling(60, min_periods=60).apply(_h, raw=True)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_efficiency_50d_slope_v045_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    num = (rs - rs.shift(50)).abs(); den = rs.diff().abs().rolling(50, min_periods=50).sum()
    b = num / den.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_curv_45d_slope_v046_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    b = rs - 2.0 * rs.shift(22) + rs.shift(44)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_accel_diff_slope_v047_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    b = (rs - rs.shift(5)) - (rs.shift(5) - rs.shift(10))
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_rs_slope_regression_30d_slope_v048_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    def _slp(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t-mt)*(x-mx)); vt = np.sum((t-mt)**2)
        if vt == 0.0 or not np.isfinite(mx) or abs(mx) < 1e-12: return np.nan
        return float(cov/vt)
    b = rs.rolling(30, min_periods=30).apply(_slp, raw=True)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_sign_outperf_slope_v049_signal(close, benchmark):
    b = np.sign(close.pct_change() - benchmark.pct_change())
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_state_4regime_slope_v050_signal(closeadj, benchmark):
    s_ret = closeadj / closeadj.shift(20) - 1.0; b_ret = benchmark / benchmark.shift(20) - 1.0
    s_up = (s_ret > 0).astype(int); b_up = (b_ret > 0).astype(int)
    bv = ((1 - s_up) * 2 + (1 - b_up)).astype(float).where(s_ret.notna() & b_ret.notna())
    return _r(bv.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_outperf_uptrend_flag_slope_v051_signal(close, benchmark):
    diff = close.pct_change(10) - benchmark.pct_change(10)
    up = (close > _sma(close, 20)).astype(int) - (close <= _sma(close, 20)).astype(int)
    out = pd.Series(0.0, index=close.index, dtype=float)
    out = out.mask((diff > 0) & (up > 0), 1.0)
    out = out.mask((diff < 0) & (up < 0), -1.0)
    b = out.where(diff.notna())
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_decouple_flag_30d_slope_v052_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    sd = diff.rolling(30, min_periods=30).std(ddof=0)
    b = (diff.abs() > 2.0 * sd).astype(float).where(sd.notna())
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_arctan_active_return_sum_30d_slope_v053_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = np.arctan(diff.rolling(30, min_periods=30).sum() * 10.0)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_tanh_idiovol_ratio_80d_slope_v054_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(80, min_periods=80).cov(rb); var = rb.rolling(80, min_periods=80).var()
    beta = cov / var.replace(0.0, np.nan); resid = rs - beta * rb
    ivol = resid.rolling(80, min_periods=80).std(ddof=0)
    tvol = rs.rolling(80, min_periods=80).std(ddof=0).replace(0.0, np.nan)
    b = np.tanh(ivol / tvol - 0.5)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_sigmoid_tracking_resid_60d_slope_v055_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(60, min_periods=60).cov(rb); var = rb.rolling(60, min_periods=60).var()
    beta = cov / var.replace(0.0, np.nan); resid = rs - beta * rb
    rstd = resid.rolling(60, min_periods=60).std(ddof=0)
    tstd = (rs - rb).rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    b = 1.0 / (1.0 + np.exp(-(rstd / tstd - 1.0) * 5.0)) - 0.5
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_vol_ratio_60d_slope_v056_signal(closeadj, benchmark):
    rs = closeadj.pct_change().rolling(60, min_periods=60).std(ddof=0)
    rb = benchmark.pct_change().rolling(60, min_periods=60).std(ddof=0)
    b = np.log(rs / rb.replace(0.0, np.nan))
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_sortino_diff_90d_slope_v057_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    ds_rs = rs.where(rs < 0).rolling(90, min_periods=10).std(ddof=0)
    ds_rb = rb.where(rb < 0).rolling(90, min_periods=10).std(ddof=0)
    sr_rs = rs.rolling(90, min_periods=90).mean() / ds_rs.replace(0.0, np.nan)
    sr_rb = rb.rolling(90, min_periods=90).mean() / ds_rb.replace(0.0, np.nan)
    b = sr_rs - sr_rb
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_treynor_60d_slope_v058_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(60, min_periods=60).cov(rb); var = rb.rolling(60, min_periods=60).var()
    beta = cov / var.replace(0.0, np.nan)
    alpha = rs.rolling(60, min_periods=60).mean() - beta * rb.rolling(60, min_periods=60).mean()
    b = alpha / beta.replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_corr_zscore_60d_slope_v059_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    c = rs.rolling(20, min_periods=20).corr(rb)
    mu = c.rolling(60, min_periods=60).mean(); sd = c.rolling(60, min_periods=60).std(ddof=0)
    b = (c - mu) / sd.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_high_corr_frac_120d_slope_v060_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    c = rs.rolling(20, min_periods=20).corr(rb); med = c.rolling(120, min_periods=120).median()
    b = (c > med).astype(float).where(med.notna()).rolling(120, min_periods=120).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_decouple_days_count_80d_slope_v061_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    mism = (np.sign(rs) != np.sign(rb)).astype(float)
    b = mism.rolling(80, min_periods=80).sum()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_volatility_45d_slope_v062_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    b = rs.rolling(45, min_periods=45).std(ddof=0)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_zscore_50d_slope_v063_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    mu = rs.rolling(50, min_periods=50).mean(); sd = rs.rolling(50, min_periods=50).std(ddof=0)
    b = (rs - mu) / sd.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_bench_corr_lag5_30d_slope_v064_signal(close, benchmark):
    rs = close.pct_change(); rb = benchmark.pct_change().shift(-5)
    b = rs.rolling(30, min_periods=30).corr(rb)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_active_return_skew_80d_slope_v065_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(80, min_periods=80).skew()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_active_return_kurt_80d_slope_v066_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(80, min_periods=80).kurt()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p75_50d_slope_v067_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(50, min_periods=50).quantile(0.75)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p25_50d_slope_v068_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(50, min_periods=50).quantile(0.25)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_outperf_iqr_50d_slope_v069_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(50, min_periods=50).quantile(0.75) - diff.rolling(50, min_periods=50).quantile(0.25)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_new_high_count_60d_slope_v070_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); rmax = rs.rolling(60, min_periods=60).max()
    b = ((rs >= rmax - 1e-12).astype(float).where(rmax.notna())).rolling(60, min_periods=60).sum()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_argmax_60d_slope_v071_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    def _am(x):
        if not np.all(np.isfinite(x)): return np.nan
        return float(np.argmax(x))
    b = rs.rolling(60, min_periods=60).apply(_am, raw=True)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_argmin_120d_slope_v072_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    def _ami(x):
        if not np.all(np.isfinite(x)): return np.nan
        return float(np.argmin(x))
    b = rs.rolling(120, min_periods=120).apply(_ami, raw=True)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_above_ma_count_80d_slope_v073_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); ma = _sma(rs, 40)
    b = (rs > ma).astype(float).rolling(80, min_periods=80).sum()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_beta_diff_45_120_slope_v074_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov45 = rs.rolling(45, min_periods=45).cov(rb); var45 = rb.rolling(45, min_periods=45).var()
    cov120 = rs.rolling(120, min_periods=120).cov(rb); var120 = rb.rolling(120, min_periods=120).var()
    b = cov45 / var45.replace(0.0, np.nan) - cov120 / var120.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_above_zero_streak_slope_v075_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); mu = rs.rolling(120, min_periods=120).mean()
    rsv = rs.values; muv = mu.values
    out = np.full(len(rsv), np.nan, dtype=float); run = 0
    for i in range(len(rsv)):
        if not (np.isfinite(muv[i]) and np.isfinite(rsv[i])): continue
        run = run + 1 if rsv[i] > muv[i] else 0
        out[i] = float(run)
    b = pd.Series(out, index=closeadj.index, dtype=float)
    return _r(b.diff(21))

# === 076-150 slopes ===
def f29rs_f29_relative_strength_vs_benchmark_downside_beta_60d_slope_v076_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    mask = (rb < 0).astype(float); n = 60
    cnt = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu_rs = (rs * mask).rolling(n, min_periods=n).sum() / cnt
    mu_rb = (rb * mask).rolling(n, min_periods=n).sum() / cnt
    cov = ((rs - mu_rs) * (rb - mu_rb) * mask).rolling(n, min_periods=n).sum() / cnt
    var = (((rb - mu_rb) ** 2) * mask).rolling(n, min_periods=n).sum() / cnt
    b = cov / var.replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_upside_beta_60d_slope_v077_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    mask = (rb > 0).astype(float); n = 60
    cnt = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu_rs = (rs * mask).rolling(n, min_periods=n).sum() / cnt
    mu_rb = (rb * mask).rolling(n, min_periods=n).sum() / cnt
    cov = ((rs - mu_rs) * (rb - mu_rb) * mask).rolling(n, min_periods=n).sum() / cnt
    var = (((rb - mu_rb) ** 2) * mask).rolling(n, min_periods=n).sum() / cnt
    b = cov / var.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_beta_asymm_diff_60d_slope_v078_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change(); n = 60
    pieces = []
    for sgn in (1.0, -1.0):
        m = ((rb > 0) if sgn > 0 else (rb < 0)).astype(float)
        cnt = m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        mu_rs = (rs * m).rolling(n, min_periods=n).sum() / cnt
        mu_rb = (rb * m).rolling(n, min_periods=n).sum() / cnt
        cov = ((rs - mu_rs) * (rb - mu_rb) * m).rolling(n, min_periods=n).sum() / cnt
        var = (((rb - mu_rb) ** 2) * m).rolling(n, min_periods=n).sum() / cnt
        pieces.append(cov / var.replace(0.0, np.nan))
    b = pieces[0] - pieces[1]
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_kendall_tau_returns_60d_slope_v079_signal(closeadj, benchmark):
    rs = closeadj.pct_change().values; rb = benchmark.pct_change().values
    out = np.full(len(rs), np.nan, dtype=float); n = 60
    for i in range(n - 1, len(rs)):
        wa = rs[i-n+1:i+1]; wb = rb[i-n+1:i+1]
        if not (np.all(np.isfinite(wa)) and np.all(np.isfinite(wb))): continue
        c = 0; d = 0
        for j in range(n - 1):
            for k in range(j + 1, n):
                sa = wa[j] - wa[k]; sb = wb[j] - wb[k]
                if sa * sb > 0: c += 1
                elif sa * sb < 0: d += 1
        out[i] = (c - d) / (n * (n - 1) / 2.0)
    b = pd.Series(out, index=closeadj.index, dtype=float)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_corr_squared_returns_60d_slope_v080_signal(closeadj, benchmark):
    rs2 = closeadj.pct_change() ** 2; rb2 = benchmark.pct_change() ** 2
    b = rs2.rolling(60, min_periods=60).corr(rb2)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_corr_diff_lag1_60d_slope_v081_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    c0 = rs.rolling(60, min_periods=60).corr(rb); c1 = rs.rolling(60, min_periods=60).corr(rb.shift(1))
    b = c1 - c0
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_dema_logrs_30d_slope_v082_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); b = rs - _dema(rs, 30)
    return _r((b.diff(21) / b.abs().rolling(21, min_periods=21).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_tema_slope_logrs_40d_slope_v083_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); t = _tema(rs, 40); b = t - t.shift(10)
    return _r((b.diff(10) / b.abs().rolling(10, min_periods=10).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_wilder_logrs_25d_slope_v084_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); b = rs - _wilder(rs, 25)
    return _r((b.diff(10) / b.abs().rolling(10, min_periods=10).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_te_zscore_120d_slope_v085_signal(closeadj, benchmark):
    te = (closeadj.pct_change() - benchmark.pct_change()).rolling(30, min_periods=30).std(ddof=0)
    mu = te.rolling(120, min_periods=120).mean(); sd = te.rolling(120, min_periods=120).std(ddof=0)
    b = (te - mu) / sd.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_active_pain_index_80d_slope_v086_signal(closeadj, benchmark):
    s_dd = _rdd(closeadj, 80); b_dd = _rdd(benchmark, 80)
    b = s_dd.rolling(80, min_periods=80).mean() - b_dd.rolling(80, min_periods=80).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_active_ulcer_60d_slope_v087_signal(closeadj, benchmark):
    s_dd = _rdd(closeadj, 60); b_dd = _rdd(benchmark, 60)
    s_ulc = np.sqrt((s_dd ** 2).rolling(60, min_periods=60).mean())
    b_ulc = np.sqrt((b_dd ** 2).rolling(60, min_periods=60).mean())
    b = s_ulc - b_ulc
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_days_since_rs_peak_120d_slope_v088_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark).values; out = np.full(len(rs), np.nan, dtype=float); n = 120
    for i in range(n - 1, len(rs)):
        w = rs[i-n+1:i+1]
        if not np.all(np.isfinite(w)): continue
        out[i] = float((n - 1) - int(np.argmax(w)))
    b = pd.Series(out, index=closeadj.index, dtype=float)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_days_since_rs_trough_120d_slope_v089_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark).values; out = np.full(len(rs), np.nan, dtype=float); n = 120
    for i in range(n - 1, len(rs)):
        w = rs[i-n+1:i+1]
        if not np.all(np.isfinite(w)): continue
        out[i] = float((n - 1) - int(np.argmin(w)))
    b = pd.Series(out, index=closeadj.index, dtype=float)
    return _r(b.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_rs_new_low_count_60d_slope_v090_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); rmin = rs.rolling(60, min_periods=60).min()
    flag = (rs <= rmin + 1e-12).astype(float).where(rmin.notna())
    b = flag.rolling(60, min_periods=60).sum()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_calmar_diff_120d_slope_v091_signal(closeadj, benchmark):
    s_ret = closeadj / closeadj.shift(120) - 1.0; b_ret = benchmark / benchmark.shift(120) - 1.0
    s_dd = _rdd(closeadj, 120).rolling(120, min_periods=120).min().abs().replace(0.0, np.nan)
    b_dd = _rdd(benchmark, 120).rolling(120, min_periods=120).min().abs().replace(0.0, np.nan)
    b = s_ret / s_dd - b_ret / b_dd
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_omega_diff_60d_slope_v092_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    pos = diff.where(diff > 0, 0.0).rolling(60, min_periods=60).sum()
    neg = (-diff.where(diff < 0, 0.0)).rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    b = pos / neg - 1.0
    return _r((b.diff(10) / b.abs().rolling(10, min_periods=10).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_joint_vol_regime_45d_slope_v093_signal(closeadj, benchmark):
    sv = closeadj.pct_change().rolling(45, min_periods=45).std(ddof=0)
    bv = benchmark.pct_change().rolling(45, min_periods=45).std(ddof=0)
    sm = sv.rolling(200, min_periods=200).median(); bm = bv.rolling(200, min_periods=200).median()
    s_hi = (sv > sm).astype(int); b_hi = (bv > bm).astype(int)
    state = (s_hi * 2 + b_hi).astype(float).where(sm.notna() & bm.notna())
    return _r(state.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_vol_gap_zscore_60d_slope_v094_signal(closeadj, benchmark):
    sv = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    bv = benchmark.pct_change().rolling(20, min_periods=20).std(ddof=0)
    gap = sv - bv
    mu = gap.rolling(60, min_periods=60).mean(); sd = gap.rolling(60, min_periods=60).std(ddof=0)
    b = (gap - mu) / sd.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_active_iqr_zscore_120d_slope_v095_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    iqr = diff.rolling(50, min_periods=50).quantile(0.75) - diff.rolling(50, min_periods=50).quantile(0.25)
    mu = iqr.rolling(120, min_periods=120).mean(); sd = iqr.rolling(120, min_periods=120).std(ddof=0)
    b = (iqr - mu) / sd.replace(0.0, np.nan)
    return _r(b.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_active_return_min_45d_slope_v096_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(45, min_periods=45).min()
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_active_return_max_45d_slope_v097_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(45, min_periods=45).max()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_active_return_median_60d_slope_v098_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(60, min_periods=60).median()
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_active_return_p90_minus_p10_60d_slope_v099_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    b = diff.rolling(60, min_periods=60).quantile(0.9) - diff.rolling(60, min_periods=60).quantile(0.1)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_sign_agreement_60d_slope_v100_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    match = (np.sign(rs) == np.sign(rb)).astype(float)
    b = match.rolling(60, min_periods=60).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_jaccard_up_45d_slope_v101_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    s_up = (rs > 0).astype(int); b_up = (rb > 0).astype(int)
    inter = (s_up * b_up).rolling(45, min_periods=45).sum()
    union = ((s_up + b_up) > 0).astype(int).rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    b = inter / union
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_volwt_active_ret_60d_slope_v102_signal(closeadj, benchmark, volume):
    diff = closeadj.pct_change() - benchmark.pct_change()
    num = (diff * volume).rolling(60, min_periods=60).sum()
    den = volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    b = num / den
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_volwt_corr_45d_slope_v103_signal(closeadj, benchmark, volume):
    rs = closeadj.pct_change(); rb = benchmark.pct_change(); n = 45
    wsum = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu_rs = (rs * volume).rolling(n, min_periods=n).sum() / wsum
    mu_rb = (rb * volume).rolling(n, min_periods=n).sum() / wsum
    cov = ((rs - mu_rs) * (rb - mu_rb) * volume).rolling(n, min_periods=n).sum() / wsum
    var_rs = (((rs - mu_rs) ** 2) * volume).rolling(n, min_periods=n).sum() / wsum
    var_rb = (((rb - mu_rb) ** 2) * volume).rolling(n, min_periods=n).sum() / wsum
    b = cov / np.sqrt(var_rs * var_rb).replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_drawdown_90d_slope_v104_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); rmax = rs.rolling(90, min_periods=90).max()
    b = rs - rmax
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_recovery_progress_120d_slope_v105_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    hi = rs.rolling(120, min_periods=120).max(); lo = rs.rolling(120, min_periods=120).min()
    b = (rs - lo) / (hi - lo).replace(0.0, np.nan)
    return _r(b.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_rs_momentum_short_minus_long_slope_v106_signal(closeadj, benchmark):
    rs = closeadj / benchmark
    s = np.log(rs / rs.shift(15)); l = np.log(rs / rs.shift(90))
    b = s - l
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_log_distance_sma_100d_slope_v107_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); b = rs - _sma(rs, 100)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_ema_logrs_30_180_diff_slope_v108_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); b = _ema(rs, 30) - _ema(rs, 180)
    return _r(b.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_active_dd_depth_45d_slope_v109_signal(closeadj, benchmark):
    cum = np.log(closeadj / benchmark); rmax = cum.rolling(45, min_periods=45).max()
    b = cum - rmax
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_active_dd_avg_depth_60d_slope_v110_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); rmax = rs.rolling(60, min_periods=60).max()
    b = (rs - rmax).rolling(60, min_periods=60).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_gini_60d_slope_v111_signal(closeadj, benchmark):
    diff = (closeadj.pct_change() - benchmark.pct_change()).abs()
    def _g(x):
        if not np.all(np.isfinite(x)): return np.nan
        y = np.sort(x); n = len(y)
        if y.sum() == 0: return np.nan
        cum = np.cumsum(y)
        return float((n + 1 - 2 * cum.sum() / cum[-1]) / n)
    b = diff.rolling(60, min_periods=60).apply(_g, raw=True)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_entropy_60d_slope_v112_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    pos = (diff > 0).astype(float); p = pos.rolling(60, min_periods=60).mean()
    eps = 1e-12
    b = -p * np.log2(p + eps) - (1 - p) * np.log2(1 - p + eps)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_signed_outperf_intensity_30d_slope_v113_signal(close, benchmark):
    diff = close.pct_change() - benchmark.pct_change()
    sig = np.sign(diff) * np.sqrt(diff.abs())
    b = sig.rolling(30, min_periods=30).mean()
    return _r((b.diff(5) / b.abs().rolling(5, min_periods=5).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_winsor_active_mean_60d_slope_v114_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    def _wm(x):
        if not np.all(np.isfinite(x)) or len(x) < 5: return np.nan
        lo = np.quantile(x, 0.1); hi = np.quantile(x, 0.9)
        return float(np.mean(np.clip(x, lo, hi)))
    b = diff.rolling(60, min_periods=60).apply(_wm, raw=True)
    return _r((b.diff(10) / b.abs().rolling(10, min_periods=10).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_beta_curvature_slope_v115_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    def _be(n):
        cov = rs.rolling(n, min_periods=n).cov(rb); var = rb.rolling(n, min_periods=n).var()
        return cov / var.replace(0.0, np.nan)
    b = _be(30) - 2.0 * _be(60) + _be(120)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_pivot_break_30d_slope_v116_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); med = rs.rolling(30, min_periods=30).median()
    iqr = rs.rolling(30, min_periods=30).quantile(0.75) - rs.rolling(30, min_periods=30).quantile(0.25)
    b = (rs - med) / iqr.replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_chop_index_45d_slope_v117_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); n = 45
    s_tr = rs.diff().abs().rolling(n, min_periods=n).sum()
    hi = rs.rolling(n, min_periods=n).max(); lo = rs.rolling(n, min_periods=n).min()
    rng = (hi - lo).replace(0.0, np.nan)
    b = 100.0 * np.log10(s_tr / rng) / np.log10(n)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_outperf_count_diff_short_long_slope_v118_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    c30 = (diff > 0).astype(float).rolling(30, min_periods=30).mean()
    c120 = (diff > 0).astype(float).rolling(120, min_periods=120).mean()
    b = c30 - c120
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_consecutive_outperf_freq_80d_slope_v119_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    dv = diff.values
    s2 = np.full(len(dv), np.nan, dtype=float)
    for i in range(1, len(dv)):
        if not (np.isfinite(dv[i]) and np.isfinite(dv[i-1])): continue
        s2[i] = 1.0 if (dv[i] > 0 and dv[i-1] > 0) else 0.0
    b = pd.Series(s2, index=closeadj.index, dtype=float).rolling(80, min_periods=80).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_5d_slope_v120_signal(close, benchmark):
    b = close.pct_change(5) - benchmark.pct_change(5)
    return _r(b.diff(5))
def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_120d_slope_v121_signal(closeadj, benchmark):
    b = closeadj.pct_change(120) - benchmark.pct_change(120)
    return _r(b.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_diff_5_60_slope_v122_signal(close, closeadj, benchmark):
    short = close.pct_change(5) - benchmark.pct_change(5)
    long_ = closeadj.pct_change(60) - benchmark.pct_change(60)
    b = short - long_
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_bench_extreme_outperf_60d_slope_v123_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change(); n = 60
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    for i in range(n - 1, len(closeadj)):
        r_b = rb.iloc[i-n+1:i+1].values; r_s = rs.iloc[i-n+1:i+1].values
        if not (np.all(np.isfinite(r_b)) and np.all(np.isfinite(r_s))): continue
        thr = np.quantile(r_b, 0.9); sel = r_s[r_b >= thr]
        if len(sel) == 0: continue
        out.iat[i] = float(np.mean(sel))
    return _r(out.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_bench_extreme_underperf_60d_slope_v124_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change(); n = 60
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    for i in range(n - 1, len(closeadj)):
        r_b = rb.iloc[i-n+1:i+1].values; r_s = rs.iloc[i-n+1:i+1].values
        if not (np.all(np.isfinite(r_b)) and np.all(np.isfinite(r_s))): continue
        thr = np.quantile(r_b, 0.1); sel = r_s[r_b <= thr]
        if len(sel) == 0: continue
        out.iat[i] = float(np.mean(sel))
    return _r(out.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_logrs_rank_250d_slope_v125_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    b = rs.rolling(250, min_periods=250).apply(
        lambda x: (np.sum(x <= x[-1]) - 1) / (len(x) - 1) if len(x) > 1 else np.nan, raw=True)
    return _r(b.diff(63))
def f29rs_f29_relative_strength_vs_benchmark_active_ret_rank_30d_slope_v126_signal(close, benchmark):
    diff = close.pct_change() - benchmark.pct_change()
    b = diff.rolling(30, min_periods=30).apply(
        lambda x: (np.sum(x <= x[-1]) - 1) / (len(x) - 1) if len(x) > 1 else np.nan, raw=True)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_corr_recent_vs_past_120d_slope_v127_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    c_now = rs.rolling(30, min_periods=30).corr(rb); c_old = c_now.shift(60)
    b = c_now - c_old
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_active_ret_bench_vol_interaction_60d_slope_v128_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    bvol = benchmark.pct_change().abs()
    b = diff.rolling(60, min_periods=60).corr(bvol)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_active_ret_volnorm_30d_slope_v129_signal(close, benchmark):
    diff = close.pct_change() - benchmark.pct_change()
    num = diff.rolling(30, min_periods=30).sum()
    den = benchmark.pct_change().rolling(30, min_periods=30).std(ddof=0).replace(0.0, np.nan)
    b = num / (den * 30.0)
    return _r((b.diff(21) / b.abs().rolling(21, min_periods=21).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_uptrend_slope_v130_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    bench_up = (benchmark > _sma(benchmark, 60))
    cond = diff.where(bench_up); b = cond.rolling(60, min_periods=10).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_downtrend_slope_v131_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    bench_dn = (benchmark < _sma(benchmark, 60))
    cond = diff.where(bench_dn); b = cond.rolling(60, min_periods=10).mean()
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_corr_slope_60d_slope_v132_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    c = rs.rolling(20, min_periods=20).corr(rb)
    b = c.diff(30)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_beta_slope_45d_slope_v133_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(30, min_periods=30).cov(rb); var = rb.rolling(30, min_periods=30).var()
    beta = cov / var.replace(0.0, np.nan); b = beta.diff(45)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_active_ret_autocorr_50d_slope_v134_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change(); diff_lag = diff.shift(1)
    b = diff.rolling(50, min_periods=50).corr(diff_lag)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_autocorr_lag5_80d_slope_v135_signal(closeadj, benchmark):
    drs = np.log(closeadj / benchmark).diff()
    b = drs.rolling(80, min_periods=80).corr(drs.shift(5))
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_range_30d_slope_v136_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    b = rs.rolling(30, min_periods=30).max() - rs.rolling(30, min_periods=30).min()
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_range_zscore_120d_slope_v137_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    rng = rs.rolling(30, min_periods=30).max() - rs.rolling(30, min_periods=30).min()
    mu = rng.rolling(120, min_periods=120).mean(); sd = rng.rolling(120, min_periods=120).std(ddof=0)
    b = (rng - mu) / sd.replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_state_trend_alignment_slope_v138_signal(closeadj, benchmark):
    s_up = (closeadj > _sma(closeadj, 100)); b_up = (benchmark > _sma(benchmark, 100))
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    out = out.mask(s_up & b_up, 1.0); out = out.mask((~s_up) & (~b_up), -1.0)
    valid = _sma(closeadj, 100).notna() & _sma(benchmark, 100).notna()
    b = out.where(valid)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_ret_ratio_med_30d_slope_v139_signal(close, benchmark):
    rs = close.pct_change(); rb = benchmark.pct_change().replace(0.0, np.nan)
    ratio = rs / rb; b = ratio.rolling(30, min_periods=10).median()
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_max_underperf_run_120d_slope_v140_signal(closeadj, benchmark):
    diff = closeadj.pct_change() - benchmark.pct_change()
    sig = (diff < 0).astype(float).where(diff.notna())
    b = sig.rolling(120, min_periods=120).apply(_max_run, raw=True)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_q75_dist_60d_slope_v141_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    b = rs - rs.rolling(60, min_periods=60).quantile(0.75)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_iqr_zscore_60d_slope_v142_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    q1 = rs.rolling(60, min_periods=60).quantile(0.25); q3 = rs.rolling(60, min_periods=60).quantile(0.75)
    med = rs.rolling(60, min_periods=60).median()
    b = (rs - med) / (q3 - q1).replace(0.0, np.nan)
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_rs_pctB_30d_slope_v143_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); mu = _sma(rs, 30); sd = rs.rolling(30, min_periods=30).std(ddof=0)
    lo = mu - 2.0 * sd; hi = mu + 2.0 * sd
    b = (rs - lo) / (hi - lo).replace(0.0, np.nan)
    return _r((b.diff(21) / b.abs().rolling(21, min_periods=21).mean().replace(0.0, np.nan)))
def f29rs_f29_relative_strength_vs_benchmark_rs_bandwidth_45d_slope_v144_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark); mu = _sma(rs, 45); sd = rs.rolling(45, min_periods=45).std(ddof=0)
    b = 4.0 * sd / mu.abs().replace(0.0, np.nan)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_beta_dispersion_120d_slope_v145_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    cov = rs.rolling(20, min_periods=20).cov(rb); var = rb.rolling(20, min_periods=20).var()
    beta = cov / var.replace(0.0, np.nan)
    b = beta.rolling(120, min_periods=120).std(ddof=0)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_high_to_benchhigh_30d_slope_v146_signal(high, benchmark):
    sh = high.rolling(30, min_periods=30).max(); bh = benchmark.rolling(30, min_periods=30).max()
    b = sh / bh.replace(0.0, np.nan) - 1.0
    return _r(b.diff(10))
def f29rs_f29_relative_strength_vs_benchmark_low_to_benchlow_30d_slope_v147_signal(low, benchmark):
    sl = low.rolling(30, min_periods=30).min(); bl = benchmark.rolling(30, min_periods=30).min()
    b = sl / bl.replace(0.0, np.nan) - 1.0
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_tail_coexceed_60d_slope_v148_signal(closeadj, benchmark):
    rs = closeadj.pct_change(); rb = benchmark.pct_change()
    qs = rs.rolling(60, min_periods=60).quantile(0.1); qb = rb.rolling(60, min_periods=60).quantile(0.1)
    flag = ((rs <= qs) & (rb <= qb)).astype(float).where(qs.notna() & qb.notna())
    b = flag.rolling(60, min_periods=60).mean()
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_regslope_90d_slope_v149_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    def _slp(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t-mt)*(x-mx)); vt = np.sum((t-mt)**2)
        if vt == 0.0: return np.nan
        return float(cov/vt)
    b = rs.rolling(90, min_periods=90).apply(_slp, raw=True)
    return _r(b.diff(21))
def f29rs_f29_relative_strength_vs_benchmark_rs_regrsq_90d_slope_v150_signal(closeadj, benchmark):
    rs = np.log(closeadj / benchmark)
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t-mt)*(x-mx)); vt = np.sum((t-mt)**2); vx = np.sum((x-mx)**2)
        if vt == 0.0 or vx == 0.0: return np.nan
        r = cov / np.sqrt(vt*vx); return float(r*r)
    b = rs.rolling(90, min_periods=90).apply(_rsq, raw=True)
    return _r(b.diff(63))
_e = [
    (f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_10d_slope_v001_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_60d_slope_v002_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_200d_slope_v003_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_log_rs_ratio_slope_v004_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_cumret_ratio_45d_slope_v005_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_sma_logrs_20d_slope_v006_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_ema_logrs_50d_slope_v007_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_mad_30d_slope_v008_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_ema_diff_logrs_20_60_slope_v009_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_rank_120d_slope_v010_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_45d_slope_v011_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_120d_slope_v012_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_alpha_60d_slope_v013_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_zscore_60d_slope_v014_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_idio_vol_80d_slope_v015_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_rank_120d_slope_v016_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_returns_30d_slope_v017_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_abs_returns_60d_slope_v018_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_spearman_corr_60d_slope_v019_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_leadlag_corr_45d_slope_v020_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_levels_80d_slope_v021_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_diff_30_120_slope_v022_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_tracking_err_30d_slope_v023_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_tracking_err_120d_slope_v024_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_info_ratio_200d_slope_v025_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_return_zscore_80d_slope_v026_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_up_capture_60d_slope_v027_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_down_capture_60d_slope_v028_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_up_minus_down_capture_90d_slope_v029_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_up_day_outperf_frac_45d_slope_v030_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_dn_day_outperf_frac_60d_slope_v031_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_count_30d_slope_v032_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_count_120d_slope_v033_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_streak_slope_v034_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_underperf_streak_slope_v035_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_max_streak_outperf_60d_slope_v036_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_excess_pct_50d_slope_v037_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_dd_diff_60d_slope_v038_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_dd_diff_200d_slope_v039_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_dd_ratio_120d_slope_v040_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_willr_14d_slope_v041_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_stoch_30d_slope_v042_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_cmo_20d_slope_v043_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_hurst_60d_slope_v044_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_efficiency_50d_slope_v045_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_curv_45d_slope_v046_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_accel_diff_slope_v047_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_slope_regression_30d_slope_v048_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_sign_outperf_slope_v049_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_state_4regime_slope_v050_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_uptrend_flag_slope_v051_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_decouple_flag_30d_slope_v052_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_arctan_active_return_sum_30d_slope_v053_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_tanh_idiovol_ratio_80d_slope_v054_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_sigmoid_tracking_resid_60d_slope_v055_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_vol_ratio_60d_slope_v056_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_sortino_diff_90d_slope_v057_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_treynor_60d_slope_v058_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_zscore_60d_slope_v059_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_high_corr_frac_120d_slope_v060_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_decouple_days_count_80d_slope_v061_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_volatility_45d_slope_v062_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_zscore_50d_slope_v063_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_bench_corr_lag5_30d_slope_v064_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_return_skew_80d_slope_v065_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_return_kurt_80d_slope_v066_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p75_50d_slope_v067_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_mag_p25_50d_slope_v068_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_iqr_50d_slope_v069_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_new_high_count_60d_slope_v070_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_argmax_60d_slope_v071_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_argmin_120d_slope_v072_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_above_ma_count_80d_slope_v073_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_diff_45_120_slope_v074_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_above_zero_streak_slope_v075_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_downside_beta_60d_slope_v076_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_upside_beta_60d_slope_v077_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_asymm_diff_60d_slope_v078_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_kendall_tau_returns_60d_slope_v079_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_squared_returns_60d_slope_v080_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_diff_lag1_60d_slope_v081_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_dema_logrs_30d_slope_v082_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_tema_slope_logrs_40d_slope_v083_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_wilder_logrs_25d_slope_v084_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_te_zscore_120d_slope_v085_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_pain_index_80d_slope_v086_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_ulcer_60d_slope_v087_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_days_since_rs_peak_120d_slope_v088_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_days_since_rs_trough_120d_slope_v089_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_new_low_count_60d_slope_v090_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_calmar_diff_120d_slope_v091_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_omega_diff_60d_slope_v092_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_joint_vol_regime_45d_slope_v093_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_vol_gap_zscore_60d_slope_v094_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_iqr_zscore_120d_slope_v095_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_return_min_45d_slope_v096_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_return_max_45d_slope_v097_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_return_median_60d_slope_v098_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_return_p90_minus_p10_60d_slope_v099_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_sign_agreement_60d_slope_v100_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_jaccard_up_45d_slope_v101_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_volwt_active_ret_60d_slope_v102_signal, ["closeadj", "benchmark", "volume"]),
    (f29rs_f29_relative_strength_vs_benchmark_volwt_corr_45d_slope_v103_signal, ["closeadj", "benchmark", "volume"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_drawdown_90d_slope_v104_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_recovery_progress_120d_slope_v105_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_momentum_short_minus_long_slope_v106_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_log_distance_sma_100d_slope_v107_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_ema_logrs_30_180_diff_slope_v108_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_dd_depth_45d_slope_v109_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_dd_avg_depth_60d_slope_v110_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_gini_60d_slope_v111_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_entropy_60d_slope_v112_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_signed_outperf_intensity_30d_slope_v113_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_winsor_active_mean_60d_slope_v114_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_curvature_slope_v115_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_pivot_break_30d_slope_v116_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_chop_index_45d_slope_v117_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_outperf_count_diff_short_long_slope_v118_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_consecutive_outperf_freq_80d_slope_v119_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_5d_slope_v120_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_120d_slope_v121_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_pctdiff_diff_5_60_slope_v122_signal, ["close", "closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_bench_extreme_outperf_60d_slope_v123_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_bench_extreme_underperf_60d_slope_v124_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_logrs_rank_250d_slope_v125_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_ret_rank_30d_slope_v126_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_recent_vs_past_120d_slope_v127_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_ret_bench_vol_interaction_60d_slope_v128_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_ret_volnorm_30d_slope_v129_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_uptrend_slope_v130_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_relperf_in_bench_downtrend_slope_v131_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_corr_slope_60d_slope_v132_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_slope_45d_slope_v133_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_active_ret_autocorr_50d_slope_v134_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_autocorr_lag5_80d_slope_v135_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_range_30d_slope_v136_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_range_zscore_120d_slope_v137_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_state_trend_alignment_slope_v138_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_ret_ratio_med_30d_slope_v139_signal, ["close", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_max_underperf_run_120d_slope_v140_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_q75_dist_60d_slope_v141_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_iqr_zscore_60d_slope_v142_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_pctB_30d_slope_v143_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_bandwidth_45d_slope_v144_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_beta_dispersion_120d_slope_v145_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_high_to_benchhigh_30d_slope_v146_signal, ["high", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_low_to_benchlow_30d_slope_v147_signal, ["low", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_tail_coexceed_60d_slope_v148_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_regslope_90d_slope_v149_signal, ["closeadj", "benchmark"]),
    (f29rs_f29_relative_strength_vs_benchmark_rs_regrsq_90d_slope_v150_signal, ["closeadj", "benchmark"]),
]
f29_relative_strength_vs_benchmark_slope_001_150_REGISTRY = {f.__name__: {"inputs": inp, "func": f} for f, inp in _e}
# Self-test ------------------------------------------------------------------

def _synthetic_inputs(n=800, seed=42):
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg), rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg), rng.normal(0.0008, 0.012, rest),
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
        rng2.normal(0.0008, 0.009, seg), rng2.normal(-0.0003, 0.014, seg),
        rng2.normal(-0.0007, 0.011, seg), rng2.normal(0.0006, 0.010, rest),
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

def _self_test():
    df = _synthetic_inputs(n=800, seed=42)
    results = {}
    for name, entry in f29_relative_strength_vs_benchmark_slope_001_150_REGISTRY.items():
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
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%}"
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
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
    _self_test()
