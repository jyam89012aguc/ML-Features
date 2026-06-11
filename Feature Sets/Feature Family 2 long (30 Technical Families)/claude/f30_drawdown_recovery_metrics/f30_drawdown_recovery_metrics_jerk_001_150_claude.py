"""f30 jerk 001-150."""
from __future__ import annotations
import numpy as np
import pandas as pd
def _bars_since(flag_series, length):
    out = pd.Series(np.nan, index=flag_series.index, dtype=float)
    cnt = np.nan
    v = flag_series.values
    for i in range(length):
        if not np.isfinite(v[i]):
            continue
        if v[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        out.iat[i] = cnt
    return out

def _streak_inc(flag_series, length):
    out = pd.Series(np.nan, index=flag_series.index, dtype=float)
    cnt = np.nan
    v = flag_series.values
    for i in range(length):
        if not np.isfinite(v[i]):
            continue
        if v[i] >= 0.5:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out

def _maxrun(x):
    best = 0; cur = 0
    for v in x:
        if v >= 0.5:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return float(best)

def _avgrun(x):
    runs = []; cur = 0
    for v in x:
        if v >= 0.5:
            cur += 1
        else:
            if cur > 0:
                runs.append(cur); cur = 0
    if cur > 0:
        runs.append(cur)
    return float(np.mean(runs)) if runs else 0.0

def _medrun(x):
    runs = []; cur = 0
    for v in x:
        if v >= 0.5:
            cur += 1
        else:
            if cur > 0:
                runs.append(cur); cur = 0
    if cur > 0:
        runs.append(cur)
    return float(np.median(runs)) if runs else 0.0

def _episodes(x):
    c = 0; in_ep = False
    for v in x:
        if v >= 0.5:
            if not in_ep:
                c += 1; in_ep = True
        else:
            in_ep = False
    return float(c)

def _runskew(x):
    runs = []; cur = 0
    for v in x:
        if v >= 0.5:
            cur += 1
        else:
            if cur > 0:
                runs.append(cur); cur = 0
    if cur > 0:
        runs.append(cur)
    if len(runs) < 3:
        return np.nan
    arr = np.asarray(runs, dtype=float)
    m = arr.mean(); s = arr.std(ddof=0)
    if s <= 0:
        return np.nan
    return float(((arr - m) ** 3).mean() / (s ** 3))

def _worst_run(below_arr, dd_arr):
    best_len = 0; best_sum = 0.0
    cur_len = 0; cur_sum = 0.0
    for v, d in zip(below_arr, dd_arr):
        if v >= 0.5 and np.isfinite(d):
            cur_len += 1; cur_sum += abs(d)
            if cur_len > best_len:
                best_len = cur_len; best_sum = cur_sum
        else:
            cur_len = 0; cur_sum = 0.0
    return float(best_sum / best_len) if best_len > 0 else 0.0

def _rank_last(x):
    return float((np.sum(x <= x[-1]) - 1) / max(1, (len(x) - 1)))

def _ols_slope(x):
    n = len(x); t = np.arange(n, dtype=float); td = t - t.mean(); ss = float((td * td).sum())
    return float(np.dot(x - x.mean(), td) / ss) if ss > 0 else np.nan

def _ols_rsq(x):
    n = len(x); t = np.arange(n, dtype=float); td = t - t.mean(); ss = float((td * td).sum())
    if ss <= 0:
        return np.nan
    xm = x.mean(); xd = x - xm
    sst = float((xd * xd).sum())
    if sst <= 0:
        return np.nan
    b = float(np.dot(xd, td) / ss)
    return float((b * b * ss) / sst)


# ---------------------------------------------------------------------------
# Jerk features 001-075 (mapped to base 001-075)
# ---------------------------------------------------------------------------

def f30dr_f30_drawdown_recovery_metrics_dd_20d_jerk_v001_signal(close):
    k = 5
    b = close / close.rolling(20,20).max() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_63d_jerk_v002_signal(closeadj):
    k = 21
    b = closeadj / closeadj.rolling(63,63).max() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_252d_jerk_v003_signal(closeadj):
    k = 63
    b = closeadj / closeadj.rolling(252,252).max() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_504d_jerk_v004_signal(closeadj):
    k = 63
    b = closeadj / closeadj.rolling(504,504).max() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_maxdd_30d_jerk_v005_signal(closeadj):
    k = 10
    b = (closeadj / closeadj.rolling(30,30).max() - 1.0).rolling(30,30).min()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_maxdd_126d_jerk_v006_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(126,126).max() - 1.0).rolling(126,126).min()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_avgdd_60d_jerk_v007_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(60,60).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_days_50d_jerk_v008_signal(closeadj):
    k = 10
    rmax = closeadj.rolling(50,50).max()
    b = _bars_since((closeadj >= rmax).astype(float).where(~rmax.isna()), len(closeadj))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_days_200d_jerk_v009_signal(closeadj):
    k = 63
    rmax = closeadj.rolling(200,200).max()
    b = _bars_since((closeadj >= rmax).astype(float).where(~rmax.isna()), len(closeadj))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_integral_40d_jerk_v010_signal(closeadj):
    k = 10
    b = (closeadj / closeadj.rolling(40,40).max() - 1.0).abs().rolling(40,40).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_integral_120d_jerk_v011_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(120,120).max() - 1.0).abs().rolling(120,120).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_emerge_decay_45d_jerk_v012_signal(closeadj):
    k = 21
    dd_abs = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs()
    b = dd_abs.rolling(45,45).corr(np.sign(dd_abs.diff()))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_ratio_60d_jerk_v013_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    b = 1.0 - dd.abs() / dd.rolling(60,60).min().abs().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_slope_30d_jerk_v014_signal(closeadj):
    k = 10
    b = (closeadj - closeadj.rolling(30,30).min()) / 30.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_bars_since_trough_90d_jerk_v015_signal(closeadj):
    k = 21
    rmin = closeadj.rolling(90,90).min()
    b = _bars_since((closeadj <= rmin).astype(float).where(~rmin.isna()), len(closeadj))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_std_45d_jerk_v016_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(45,45).max() - 1.0).rolling(45,45).std()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_count_5pct_100d_jerk_v017_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(100,100).max() - 1.0
    b = (dd.abs() > 0.05).astype(float).where(~dd.isna()).rolling(100,100).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_rank_120d_jerk_v018_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(30,30).max() - 1.0).rolling(120,120).apply(_rank_last, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_20d_jerk_v019_signal(close):
    k = 5
    b = close / close.rolling(20,20).min() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_120d_jerk_v020_signal(closeadj):
    k = 21
    b = closeadj / closeadj.rolling(120,120).min() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_max_drawup_50d_jerk_v021_signal(closeadj):
    k = 10
    b = (closeadj / closeadj.rolling(50,50).min() - 1.0).rolling(50,50).max()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_dd_ratio_80d_jerk_v022_signal(closeadj):
    k = 21
    du = closeadj / closeadj.rolling(80,80).min() - 1.0
    dd = closeadj / closeadj.rolling(80,80).max() - 1.0
    b = du.rolling(80,80).max() / dd.rolling(80,80).min().abs().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_skew_75d_jerk_v023_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(75,75).max() - 1.0).rolling(75,75).skew()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_kurt_150d_jerk_v024_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(150,150).max() - 1.0).rolling(150,150).kurt()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_mad_std_60d_jerk_v025_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    mad = dd.rolling(60,60).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    b = mad / dd.rolling(60,60).std().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_ulcer_30d_jerk_v026_signal(closeadj):
    k = 10
    b = np.sqrt(((closeadj / closeadj.rolling(30,30).max() - 1.0) ** 2).rolling(30,30).mean())
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_ulcer_pain_ratio_jerk_v027_signal(closeadj):
    k = 21
    dd_s = closeadj / closeadj.rolling(30,30).max() - 1.0
    dd_l = closeadj / closeadj.rolling(120,120).max() - 1.0
    us = np.sqrt((dd_s ** 2).rolling(30,30).mean())
    ul = np.sqrt((dd_l ** 2).rolling(120,120).mean())
    b = us / ul.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_pain_ratio_60d_jerk_v028_signal(closeadj):
    k = 21
    avg_r = np.log(closeadj / closeadj.shift(1)).rolling(60,60).mean()
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    b = avg_r / np.sqrt((dd ** 2).rolling(60,60).mean()).replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_calmar_252d_jerk_v029_signal(closeadj):
    k = 63
    ret = np.log(closeadj / closeadj.shift(252))
    dd = closeadj / closeadj.rolling(252,252).max() - 1.0
    b = ret / dd.rolling(252,252).min().abs().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_sterling_120d_jerk_v030_signal(closeadj):
    k = 21
    ret = np.log(closeadj / closeadj.shift(120))
    dd = closeadj / closeadj.rolling(120,120).max() - 1.0
    b = ret / dd.rolling(120,120).mean().abs().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_frac_40d_jerk_v031_signal(closeadj):
    k = 10
    rmax = closeadj.rolling(40,40).max()
    b = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(40,40).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_frac_180d_jerk_v032_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(180,180).max()
    b = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(180,180).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_over_atr_30d_jerk_v033_signal(high, low, closeadj):
    k = 10
    dd_abs = (closeadj / closeadj.rolling(30,30).max() - 1.0).abs()
    pc = closeadj.shift(1)
    atr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1).rolling(14, 14).mean()
    b = dd_abs * closeadj / atr.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_over_realvol_90d_jerk_v034_signal(closeadj):
    k = 21
    dd_abs = (closeadj / closeadj.rolling(90,90).max() - 1.0).abs()
    rv = np.log(closeadj / closeadj.shift(1)).rolling(90,90).std()
    b = dd_abs / rv.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_in_dd_5pct_30d_jerk_v035_signal(closeadj):
    k = 10
    dd = closeadj / closeadj.rolling(30,30).max() - 1.0
    b = (dd <= -0.05).astype(float).where(~dd.isna())
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_severe_dd_20pct_252d_jerk_v036_signal(closeadj):
    k = 63
    dd = closeadj / closeadj.rolling(252,252).max() - 1.0
    b = (dd <= -0.20).astype(float).where(~dd.isna())
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_at_new_high_45d_jerk_v037_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(45,45).max()
    b = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_arctan_dd_50d_jerk_v038_signal(closeadj):
    k = 10
    b = np.arctan(10.0 * (closeadj / closeadj.rolling(50,50).max() - 1.0))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_tanh_uw_frac_80d_jerk_v039_signal(closeadj):
    k = 21
    n = 80
    rmax = closeadj.rolling(n, n).max()
    f = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(n, n).mean()
    b = np.tanh(2.0 * f - 1.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_sigmoid_dd_rank_60d_jerk_v040_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    rk = dd.rolling(60,60).apply(_rank_last, raw=True)
    b = 1.0 / (1.0 + np.exp(-6.0 * (rk - 0.5)))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_slope_30d_jerk_v041_signal(closeadj):
    k = 10
    b = (closeadj / closeadj.rolling(30,30).max() - 1.0).diff(5)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_curvature_90d_jerk_v042_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(90,90).max() - 1.0
    b = dd - 2.0 * dd.shift(10) + dd.shift(20)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_shortdd_longdd_ratio_jerk_v043_signal(closeadj):
    k = 21
    dd_s = closeadj / closeadj.rolling(20,20).max() - 1.0
    dd_l = closeadj / closeadj.rolling(120,120).max() - 1.0
    b = dd_s.abs() / dd_l.abs().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_diff_45_180d_jerk_v044_signal(closeadj):
    k = 21
    dd_a = closeadj / closeadj.rolling(45,45).max() - 1.0
    dd_b = closeadj / closeadj.rolling(180,180).max() - 1.0
    b = dd_a - dd_b
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_efficiency_60d_jerk_v045_signal(closeadj):
    k = 10
    rmax = closeadj.rolling(60,60).max(); rmin = closeadj.rolling(60,60).min()
    b = (closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_speed_30d_jerk_v046_signal(closeadj):
    k = 10
    rmin = closeadj.rolling(30,30).min()
    bars = _bars_since((closeadj <= rmin).astype(float).where(~rmin.isna()), len(closeadj))
    b = np.log(closeadj / rmin.replace(0.0, np.nan)) / (bars + 1.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_cum_dd_50d_jerk_v047_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(50,50).max() - 1.0).rolling(50,50).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_weighted_return_75d_jerk_v048_signal(closeadj):
    k = 21
    n = 75
    dd_abs = (closeadj / closeadj.rolling(n, n).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    num = (r * dd_abs).rolling(n, n).sum()
    den = dd_abs.rolling(n, n).sum().replace(0.0, np.nan)
    b = num / den
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_max_uw_length_120d_jerk_v049_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(120,120).max()
    b = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(120,120).apply(_maxrun, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_avg_uw_length_180d_jerk_v050_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(180,180).max()
    b = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(180,180).apply(_avgrun, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_maxdd_atr_60d_jerk_v051_signal(high, low, closeadj):
    k = 21
    mdd = (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(60,60).min().abs()
    pc = closeadj.shift(1)
    atr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1).rolling(21, 21).mean()
    b = mdd * closeadj / atr.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_skew_100d_jerk_v052_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(100,100).min() - 1.0).rolling(100,100).skew()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_kurt_60d_jerk_v053_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(60,60).min() - 1.0).rolling(60,60).kurt()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_recovery_30d_jerk_v054_signal(closeadj):
    k = 10
    du = closeadj / closeadj.rolling(30,30).min() - 1.0
    b = 1.0 - du / du.rolling(30,30).max().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_streak_now_70d_jerk_v055_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(70,70).max()
    b = _streak_inc((closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_zscore_45d_jerk_v056_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(45,45).max() - 1.0
    b = (dd - dd.rolling(45,45).mean()) / dd.rolling(45,45).std().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_v_shape_30d_jerk_v057_signal(closeadj):
    k = 10
    dd = closeadj / closeadj.rolling(30,30).max() - 1.0
    b = (dd - dd.shift(10)).abs() / dd.diff().abs().rolling(10, 10).sum().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_corr_dd_vol_90d_jerk_v058_signal(closeadj):
    k = 21
    dd_abs = (closeadj / closeadj.rolling(90,90).max() - 1.0).abs()
    rv = np.log(closeadj / closeadj.shift(1)).rolling(10, 10).std()
    b = dd_abs.rolling(90,90).corr(rv)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_recovery_asymmetry_75d_jerk_v059_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(75,75).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    rec = ((dd.diff() > 0) & (dd < 0)).astype(float).where(~dd.diff().isna())
    b = (below.rolling(75,75).sum() - rec.rolling(75,75).sum()) / 75.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_episode_count_120d_jerk_v060_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(120,120).max()
    b = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(120,120).apply(_episodes, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_rank_252d_jerk_v061_signal(closeadj):
    k = 63
    b = (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(252,252).apply(_rank_last, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_lag_corr_80d_jerk_v062_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    b = dd.rolling(80,80).corr(dd.shift(10))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_per_uw_day_60d_jerk_v063_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(60,60).max()
    dd = closeadj / rmax - 1.0
    mdd = dd.rolling(60,60).min().abs()
    avg_below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(60,60).mean() * 60.0
    b = mdd / avg_below.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_sig_uw_days_100d_jerk_v064_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(100,100).max()
    out = _bars_since((closeadj >= rmax).astype(float).where(~rmax.isna()), len(closeadj))
    b = 1.0 / (1.0 + np.exp(-(out - 25.0) / 15.0))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_vol_frac_60d_jerk_v065_signal(closeadj, volume):
    k = 21
    rmax = closeadj.rolling(60,60).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    b = (below * volume).rolling(60,60).sum() / volume.rolling(60,60).sum().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_mean_median_ratio_75d_jerk_v066_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(75,75).max() - 1.0
    b = dd.rolling(75,75).mean() / dd.rolling(75,75).median().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_integral_50d_jerk_v067_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(50,50).min() - 1.0).rolling(50,50).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_slope_streak_60d_jerk_v068_signal(closeadj):
    k = 21
    dd_diff = (closeadj / closeadj.rolling(20,20).max() - 1.0).diff()
    b = _streak_inc((dd_diff > 0).astype(float).where(~dd_diff.isna()), len(closeadj))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_per_bar_since_trough_90d_jerk_v069_signal(closeadj):
    k = 21
    dd_abs = (closeadj / closeadj.rolling(90,90).max() - 1.0).abs()
    rmin = closeadj.rolling(90,90).min()
    bars = _bars_since((closeadj <= rmin).astype(float).where(~rmin.isna()), len(closeadj))
    b = dd_abs / (bars + 1.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_flip_rate_50d_jerk_v070_signal(closeadj):
    k = 21
    s = np.sign((closeadj / closeadj.rolling(30,30).max() - 1.0).diff())
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(50,50).sum() / 50.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_arctan_recovery_slope_45d_jerk_v071_signal(closeadj):
    k = 21
    rmin = closeadj.rolling(45,45).min()
    b = np.arctan((closeadj - rmin) / rmin.replace(0.0, np.nan) / 45.0 * 100.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_severe_dd_count_252d_jerk_v072_signal(closeadj):
    k = 63
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    b = (dd <= -0.10).astype(float).where(~dd.isna()).rolling(252,252).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_recoverability_140d_jerk_v073_signal(closeadj):
    k = 21
    rmin = closeadj.rolling(60,60).min(); rmax = closeadj.rolling(60,60).max()
    dd_abs = (closeadj / rmax - 1.0).abs()
    b = ((closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan) * (dd_abs > 0.001).astype(float)).rolling(140, 140).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_accel_norm_60d_jerk_v074_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    b = (dd - 2.0 * dd.shift(5) + dd.shift(10)) / dd.rolling(10, 10).std().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_now_vs_max_120d_jerk_v075_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(120,120).max() - 1.0
    b = dd / dd.rolling(120,120).min().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)


# ---------------------------------------------------------------------------
# Jerk features 076-150 (mapped to base 076-150)
# ---------------------------------------------------------------------------

def f30dr_f30_drawdown_recovery_metrics_dd_15d_jerk_v076_signal(close):
    k = 5
    b = close / close.rolling(15, 15).max() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_42d_jerk_v077_signal(closeadj):
    k = 10
    b = closeadj / closeadj.rolling(42, 42).max() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_378d_jerk_v078_signal(closeadj):
    k = 63
    b = closeadj / closeadj.rolling(378, 378).max() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_40d_jerk_v079_signal(closeadj):
    k = 10
    b = closeadj / closeadj.rolling(40,40).min() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_252d_jerk_v080_signal(closeadj):
    k = 63
    b = closeadj / closeadj.rolling(252,252).min() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_net_du_dd_30d_jerk_v081_signal(close):
    k = 10
    b = (close / close.rolling(30,30).min() - 1.0) + (close / close.rolling(30,30).max() - 1.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_du_product_150d_jerk_v082_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(150,150).min() - 1.0) * (closeadj / closeadj.rolling(150,150).max() - 1.0).abs()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_concavity_60d_jerk_v083_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    b = ((dd + dd.shift(20) - 2.0 * dd.shift(10)) / 100.0 + (dd + dd.shift(10) - 2.0 * dd.shift(5)) / 25.0) / 2.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_local_trough_count_120d_jerk_v084_signal(closeadj):
    k = 21
    rmin20 = closeadj.rolling(20,20).min()
    at_low = (closeadj <= rmin20 + 1e-12).astype(float).where(~rmin20.isna())
    b = at_low.rolling(120,120).apply(_episodes, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_q10_60d_jerk_v085_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(60,60).quantile(0.10)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_iqr_100d_jerk_v086_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(100,100).max() - 1.0
    b = dd.rolling(100,100).quantile(0.75) - dd.rolling(100,100).quantile(0.25)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_newhigh_streak_60d_jerk_v087_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(60,60).max()
    b = _streak_inc((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_newlow_streak_45d_jerk_v088_signal(closeadj):
    k = 21
    rmin = closeadj.rolling(45,45).min()
    b = _streak_inc((closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna()), len(closeadj))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_atr_units_90d_jerk_v089_signal(high, low, closeadj):
    k = 63
    n = 90
    dd_abs = (closeadj / closeadj.rolling(n, n).max() - 1.0).abs()
    pc = closeadj.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(30,30).mean()
    b = dd_abs * closeadj / atr.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_under_negskew_45d_jerk_v090_signal(closeadj):
    k = 21
    n = 45
    dd_abs = (closeadj / closeadj.rolling(n, n).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    sk = r.rolling(n, n).skew()
    flag = (sk < 0).astype(float).where(~sk.isna())
    b = dd_abs * flag
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_ret_in_dd_60d_jerk_v091_signal(closeadj):
    k = 21
    n = 60
    dd = closeadj / closeadj.rolling(n, n).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1))
    in_dd = (dd <= -0.05).astype(float).where(~dd.isna())
    num = (r * in_dd).rolling(n, n).sum()
    den = in_dd.rolling(n, n).sum().replace(0.0, np.nan)
    b = num / den
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_corr_dd_volume_60d_jerk_v092_signal(closeadj, volume):
    k = 21
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    lv = np.log(volume.replace(0.0, np.nan))
    b = dd.rolling(60,60).corr(lv)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_regslope_30d_jerk_v093_signal(closeadj):
    k = 10
    b = (closeadj / closeadj.rolling(30,30).max() - 1.0).rolling(30,30).apply(_ols_slope, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_regslope_120d_jerk_v094_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(120,120).max() - 1.0).rolling(120,120).apply(_ols_slope, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_rsq_time_60d_jerk_v095_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(60,60).apply(_ols_rsq, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_vol_ratio_75d_jerk_v096_signal(closeadj):
    k = 21
    n = 75
    dd = closeadj / closeadj.rolling(n, n).max() - 1.0
    dd_vol = dd.diff().rolling(n, n).std()
    r_vol = np.log(closeadj / closeadj.shift(1)).rolling(n, n).std()
    b = dd_vol / r_vol.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_phase_imbalance_45d_jerk_v097_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    inc = (dd.diff() > 0).astype(float).where(~dd.diff().isna())
    dec = (dd.diff() < 0).astype(float).where(~dd.diff().isna())
    b = (inc.rolling(45,45).sum() - dec.rolling(45,45).sum()) / 45.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_du_integral_diff_60d_jerk_v098_signal(closeadj):
    k = 10
    n = 60
    du = closeadj / closeadj.rolling(n, n).min() - 1.0
    dd_abs = (closeadj / closeadj.rolling(n, n).max() - 1.0).abs()
    b = du.rolling(n, n).sum() - dd_abs.rolling(n, n).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_severity_duration_60d_jerk_v099_signal(closeadj):
    k = 21
    n = 60
    dd_abs = (closeadj / closeadj.rolling(n, n).max() - 1.0).abs()
    rmax = closeadj.rolling(n, n).max()
    at_high = (closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna())
    b = dd_abs * _bars_since(at_high, len(closeadj))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_30_vs_120_jerk_v100_signal(closeadj):
    k = 21
    rmax30 = closeadj.rolling(30,30).max()
    f30 = (closeadj < rmax30 - 1e-12).astype(float).where(~rmax30.isna()).rolling(30,30).mean()
    rmax120 = closeadj.rolling(120,120).max()
    f120 = (closeadj < rmax120 - 1e-12).astype(float).where(~rmax120.isna()).rolling(120,120).mean()
    b = f30 - f120
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_sharpe_60d_jerk_v101_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1)).where(dd < -0.01)
    b = r.rolling(60, min_periods=20).mean() / r.rolling(60, min_periods=20).std().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_max_dd_per_bar_180d_jerk_v102_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(180,180).max() - 1.0).rolling(180,180).min().abs() / 180.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_completeness_60d_jerk_v103_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(60,60).max(); rmin = closeadj.rolling(60,60).min()
    b = ((closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)).where(closeadj / rmax - 1.0 < -0.01)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_runs_skew_120d_jerk_v104_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(120,120).max()
    b = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(120,120).apply(_runskew, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_martin_ratio_90d_jerk_v105_signal(closeadj):
    k = 21
    ret = np.log(closeadj / closeadj.shift(90))
    dd = closeadj / closeadj.rolling(90,90).max() - 1.0
    b = ret / np.sqrt((dd ** 2).rolling(90,90).mean()).replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_max_run_dd_weighted_120d_jerk_v106_signal(closeadj):
    k = 21
    n = 120
    rmax = closeadj.rolling(n, n).max()
    dd = closeadj / rmax - 1.0
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    bv = below.values; dv = dd.values
    for i in range(n - 1, len(closeadj)):
        if np.isnan(bv[i]) or np.isnan(dv[i]):
            continue
        out.iat[i] = _worst_run(bv[i - n + 1: i + 1], dv[i - n + 1: i + 1])
    b = out
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_below_med_freq_50d_jerk_v107_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(50,50).max() - 1.0
    md = dd.rolling(50,50).median()
    b = (dd < md).astype(float).where(~dd.isna() & ~md.isna()).rolling(50,50).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_weighted_return_75d_jerk_v108_signal(closeadj):
    k = 21
    b = np.log(closeadj / closeadj.shift(75)) * (1.0 - (closeadj / closeadj.rolling(75,75).max() - 1.0).abs())
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_autocorr_60d_jerk_v109_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    b = dd.rolling(60,60).corr(dd.shift(5))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_max_mean_ratio_100d_jerk_v110_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(100,100).max() - 1.0
    b = dd.rolling(100,100).min().abs() / dd.rolling(100,100).mean().abs().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_using_lows_25d_jerk_v111_signal(high, low):
    k = 10
    b = low / high.rolling(25, 25).max() - 1.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_intrabar_dd_minus_close_dd_100d_jerk_v112_signal(high, low, closeadj):
    k = 21
    b = (low / high.rolling(100,100).max() - 1.0) - (closeadj / closeadj.rolling(100,100).max() - 1.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_max_dd_step_60d_jerk_v113_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(60,60).max() - 1.0).diff().rolling(60,60).min()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_max_recovery_step_60d_jerk_v114_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(60,60).max() - 1.0).diff().rolling(60,60).max()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_neg_pos_diff_ratio_50d_jerk_v115_signal(closeadj):
    k = 21
    d = (closeadj / closeadj.rolling(50,50).max() - 1.0).diff()
    neg = (-d.where(d < 0, 0.0)).rolling(50,50).sum()
    pos = (d.where(d > 0, 0.0)).rolling(50,50).sum()
    b = neg / (pos + neg).replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_tanh_dd_dur_75d_jerk_v116_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(75,75).max()
    bars = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    b = np.tanh((closeadj / rmax - 1.0).abs() * bars / 75.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_in_highvol_45d_jerk_v117_signal(closeadj):
    k = 21
    dd_abs = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs()
    rv = np.log(closeadj / closeadj.shift(1)).rolling(45,45).std()
    rk = rv.rolling(180,180).apply(_rank_last, raw=True)
    b = dd_abs * (rk >= 0.75).astype(float).where(~rk.isna())
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_cum_recovery_50d_jerk_v118_signal(closeadj):
    k = 21
    d = (closeadj / closeadj.rolling(50,50).max() - 1.0).diff()
    b = d.where(d > 0, 0.0).rolling(50,50).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_cum_deepening_50d_jerk_v119_signal(closeadj):
    k = 21
    d = (closeadj / closeadj.rolling(50,50).max() - 1.0).diff()
    b = (-d).where(d < 0, 0.0).rolling(50,50).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_rank_dd_180d_jerk_v120_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(45,45).max() - 1.0).rolling(180,180).apply(_rank_last, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_room_252d_jerk_v121_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(252,252).max() - 1.0
    b = dd - dd.rolling(252,252).min()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_vol_weighted_dd_60d_jerk_v122_signal(closeadj, volume):
    k = 10
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    b = (dd * volume).rolling(60,60).sum() / volume.rolling(60,60).sum().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_median_run_180d_jerk_v123_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(180,180).max()
    b = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(180,180).apply(_medrun, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_above_q25_freq_90d_jerk_v124_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    q25 = dd.rolling(90,90).quantile(0.25)
    b = (dd > q25).astype(float).where(~q25.isna()).rolling(90,90).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_path_directness_45d_jerk_v125_signal(closeadj):
    k = 21
    n = 45
    dd = closeadj / closeadj.rolling(n, n).max() - 1.0
    direct = (dd - dd.shift(n)).abs()
    path = dd.diff().abs().rolling(n, n).sum()
    b = direct / path.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_peak_trough_age_ratio_120d_jerk_v126_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(120,120).max(); rmin = closeadj.rolling(120,120).min()
    bh = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    bl = _bars_since((closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna()), len(closeadj))
    b = bh - bl
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_semivar_45d_jerk_v127_signal(closeadj):
    k = 21
    dd_abs = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    b = (r * r).where((dd_abs > 0.02) & (r < 0)).rolling(45, min_periods=15).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_vs_cumret_corr_75d_jerk_v128_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    cr = np.log(closeadj).diff(60)
    b = dd.rolling(75,75).corr(cr)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_pos_vs_neg_ret_diff_60d_jerk_v129_signal(closeadj):
    k = 21
    dd_abs = (closeadj / closeadj.rolling(60,60).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    b = dd_abs.where(r > 0).rolling(60, min_periods=10).mean() - dd_abs.where(r < 0).rolling(60, min_periods=10).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_per_bar_120d_jerk_v130_signal(closeadj):
    k = 21
    rmin = closeadj.rolling(120,120).min()
    bars = _bars_since((closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna()), len(closeadj))
    b = np.log(closeadj / rmin.replace(0.0, np.nan)) / (bars + 1.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawdown_rate_from_peak_80d_jerk_v131_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(80,80).max()
    bars = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    b = np.log(rmax.replace(0.0, np.nan) / closeadj) / (bars + 1.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_rec_to_high_freq_180d_jerk_v132_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    dip = (dd <= -0.03).astype(float).where(~dd.isna())
    rmax60 = closeadj.rolling(60,60).max()
    rec_within = (closeadj >= rmax60 - 1e-12).astype(float).where(~rmax60.isna()).rolling(10, 10).max()
    b = ((dip > 0.5) & (rec_within.shift(-10) > 0.5)).astype(float).rolling(180,180).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_quality_z_60d_jerk_v133_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(60,60).max(); rmin = closeadj.rolling(60,60).min()
    rec = (closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)
    b = (rec - rec.rolling(60,60).mean()) / rec.rolling(60,60).std().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_z_long_240d_jerk_v134_signal(closeadj):
    k = 63
    dd = closeadj / closeadj.rolling(30,30).max() - 1.0
    b = (dd - dd.rolling(240,240).mean()) / dd.rolling(240,240).std().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_days_rank_252d_jerk_v135_signal(closeadj):
    k = 63
    rmax = closeadj.rolling(90,90).max()
    bars = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    b = bars.rolling(252,252).apply(_rank_last, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_regime_change_60d_jerk_v136_signal(closeadj):
    k = 21
    recent = (closeadj / closeadj.rolling(30,30).max() - 1.0).abs().rolling(60,60).mean()
    b = recent - recent.shift(60)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_range_75d_jerk_v137_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(75,75).max() - 1.0
    b = dd.rolling(75,75).max() - dd.rolling(75,75).min()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_avg_dd_abs_25d_jerk_v138_signal(close):
    k = 10
    b = (close / close.rolling(25, 25).max() - 1.0).abs().rolling(25, 25).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_halflife_proxy_60d_jerk_v139_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    mindd = dd.rolling(60,60).min()
    b = (dd >= 0.5 * mindd).astype(float).where(~mindd.isna()).rolling(60,60).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_trend_persistence_45d_jerk_v140_signal(closeadj):
    k = 21
    dd_d = (closeadj / closeadj.rolling(20,20).max() - 1.0).diff()
    b = (np.sign(dd_d) * np.sign(dd_d.shift(1)) > 0).astype(float).where(~dd_d.isna() & ~dd_d.shift(1).isna()).rolling(45,45).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_mild_dd_15pct_freq_180d_jerk_v141_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(120,120).max() - 1.0
    b = (dd <= -0.15).astype(float).where(~dd.isna()).rolling(180,180).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_diff_std_50d_jerk_v142_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(30,30).max() - 1.0).diff().rolling(50,50).std()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_calmar_60d_jerk_v143_signal(closeadj):
    k = 10
    ret = np.log(closeadj / closeadj.shift(60))
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    b = ret / dd.rolling(60,60).min().abs().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_realvol_in_dd_45d_jerk_v144_signal(closeadj):
    k = 21
    dd = closeadj / closeadj.rolling(45,45).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1)).where(dd <= -0.02)
    b = r.rolling(45, min_periods=10).std()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_diff_kurt_90d_jerk_v145_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(45,45).max() - 1.0).diff().rolling(90,90).kurt()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_drawup_rank_120d_jerk_v146_signal(closeadj):
    k = 21
    b = (closeadj / closeadj.rolling(30,30).min() - 1.0).rolling(120,120).apply(_rank_last, raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_arctan_dur_45d_jerk_v147_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(45,45).max()
    bars = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    b = np.arctan(bars / 15.0)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_dd_volume_z_45d_jerk_v148_signal(closeadj, volume):
    k = 10
    x = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs() * np.log(volume.replace(0.0, np.nan))
    b = (x - x.rolling(45,45).mean()) / x.rolling(45,45).std().replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_recovery_symmetry_75d_jerk_v149_signal(closeadj):
    k = 21
    dd_d = (closeadj / closeadj.rolling(20,20).max() - 1.0).diff()
    rs = (dd_d > 0).astype(float).where(~dd_d.isna()).rolling(75,75).sum()
    ds = (dd_d < 0).astype(float).where(~dd_d.isna()).rolling(75,75).sum()
    b = rs / ds.replace(0.0, np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)

def f30dr_f30_drawdown_recovery_metrics_uw_bucket_diff_60d_jerk_v150_signal(closeadj):
    k = 21
    rmax = closeadj.rolling(30,30).max()
    recent = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(30,30).mean()
    b = recent - recent.shift(30)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn,*inputs): return fn.__name__,{"inputs":list(inputs),"func":fn}
f30_drawdown_recovery_metrics_jerk_001_150_REGISTRY = dict([
    _e(f30dr_f30_drawdown_recovery_metrics_dd_20d_jerk_v001_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_63d_jerk_v002_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_252d_jerk_v003_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_504d_jerk_v004_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_maxdd_30d_jerk_v005_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_maxdd_126d_jerk_v006_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_avgdd_60d_jerk_v007_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_days_50d_jerk_v008_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_days_200d_jerk_v009_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_integral_40d_jerk_v010_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_integral_120d_jerk_v011_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_emerge_decay_45d_jerk_v012_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_ratio_60d_jerk_v013_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_slope_30d_jerk_v014_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_bars_since_trough_90d_jerk_v015_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_std_45d_jerk_v016_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_count_5pct_100d_jerk_v017_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_rank_120d_jerk_v018_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_20d_jerk_v019_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_120d_jerk_v020_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_drawup_50d_jerk_v021_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_dd_ratio_80d_jerk_v022_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_skew_75d_jerk_v023_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_kurt_150d_jerk_v024_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_mad_std_60d_jerk_v025_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_ulcer_30d_jerk_v026_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_ulcer_pain_ratio_jerk_v027_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_pain_ratio_60d_jerk_v028_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_calmar_252d_jerk_v029_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_sterling_120d_jerk_v030_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_frac_40d_jerk_v031_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_frac_180d_jerk_v032_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_over_atr_30d_jerk_v033_signal,"high","low","closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_over_realvol_90d_jerk_v034_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_in_dd_5pct_30d_jerk_v035_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_severe_dd_20pct_252d_jerk_v036_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_at_new_high_45d_jerk_v037_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_arctan_dd_50d_jerk_v038_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_tanh_uw_frac_80d_jerk_v039_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_sigmoid_dd_rank_60d_jerk_v040_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_slope_30d_jerk_v041_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_curvature_90d_jerk_v042_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_shortdd_longdd_ratio_jerk_v043_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_diff_45_180d_jerk_v044_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_efficiency_60d_jerk_v045_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_speed_30d_jerk_v046_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_cum_dd_50d_jerk_v047_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_weighted_return_75d_jerk_v048_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_uw_length_120d_jerk_v049_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_avg_uw_length_180d_jerk_v050_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_maxdd_atr_60d_jerk_v051_signal,"high","low","closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_skew_100d_jerk_v052_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_kurt_60d_jerk_v053_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_recovery_30d_jerk_v054_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_streak_now_70d_jerk_v055_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_zscore_45d_jerk_v056_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_v_shape_30d_jerk_v057_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_corr_dd_vol_90d_jerk_v058_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_recovery_asymmetry_75d_jerk_v059_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_episode_count_120d_jerk_v060_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_rank_252d_jerk_v061_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_lag_corr_80d_jerk_v062_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_per_uw_day_60d_jerk_v063_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_sig_uw_days_100d_jerk_v064_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_vol_frac_60d_jerk_v065_signal,"closeadj","volume"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_mean_median_ratio_75d_jerk_v066_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_integral_50d_jerk_v067_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_slope_streak_60d_jerk_v068_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_per_bar_since_trough_90d_jerk_v069_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_flip_rate_50d_jerk_v070_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_arctan_recovery_slope_45d_jerk_v071_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_severe_dd_count_252d_jerk_v072_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_recoverability_140d_jerk_v073_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_accel_norm_60d_jerk_v074_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_now_vs_max_120d_jerk_v075_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_15d_jerk_v076_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_42d_jerk_v077_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_378d_jerk_v078_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_40d_jerk_v079_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_252d_jerk_v080_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_net_du_dd_30d_jerk_v081_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_du_product_150d_jerk_v082_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_concavity_60d_jerk_v083_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_local_trough_count_120d_jerk_v084_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_q10_60d_jerk_v085_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_iqr_100d_jerk_v086_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_newhigh_streak_60d_jerk_v087_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_newlow_streak_45d_jerk_v088_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_atr_units_90d_jerk_v089_signal,"high","low","closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_under_negskew_45d_jerk_v090_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_ret_in_dd_60d_jerk_v091_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_corr_dd_volume_60d_jerk_v092_signal,"closeadj","volume"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_regslope_30d_jerk_v093_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_regslope_120d_jerk_v094_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_rsq_time_60d_jerk_v095_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_vol_ratio_75d_jerk_v096_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_phase_imbalance_45d_jerk_v097_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_du_integral_diff_60d_jerk_v098_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_severity_duration_60d_jerk_v099_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_30_vs_120_jerk_v100_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_sharpe_60d_jerk_v101_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_dd_per_bar_180d_jerk_v102_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_completeness_60d_jerk_v103_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_runs_skew_120d_jerk_v104_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_martin_ratio_90d_jerk_v105_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_run_dd_weighted_120d_jerk_v106_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_below_med_freq_50d_jerk_v107_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_weighted_return_75d_jerk_v108_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_autocorr_60d_jerk_v109_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_max_mean_ratio_100d_jerk_v110_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_using_lows_25d_jerk_v111_signal,"high","low"),
    _e(f30dr_f30_drawdown_recovery_metrics_intrabar_dd_minus_close_dd_100d_jerk_v112_signal,"high","low","closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_dd_step_60d_jerk_v113_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_recovery_step_60d_jerk_v114_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_neg_pos_diff_ratio_50d_jerk_v115_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_tanh_dd_dur_75d_jerk_v116_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_in_highvol_45d_jerk_v117_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_cum_recovery_50d_jerk_v118_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_cum_deepening_50d_jerk_v119_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_rank_dd_180d_jerk_v120_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_room_252d_jerk_v121_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_vol_weighted_dd_60d_jerk_v122_signal,"closeadj","volume"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_median_run_180d_jerk_v123_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_above_q25_freq_90d_jerk_v124_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_path_directness_45d_jerk_v125_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_peak_trough_age_ratio_120d_jerk_v126_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_semivar_45d_jerk_v127_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_vs_cumret_corr_75d_jerk_v128_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_pos_vs_neg_ret_diff_60d_jerk_v129_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_per_bar_120d_jerk_v130_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawdown_rate_from_peak_80d_jerk_v131_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_rec_to_high_freq_180d_jerk_v132_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_quality_z_60d_jerk_v133_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_z_long_240d_jerk_v134_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_days_rank_252d_jerk_v135_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_regime_change_60d_jerk_v136_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_range_75d_jerk_v137_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_avg_dd_abs_25d_jerk_v138_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_halflife_proxy_60d_jerk_v139_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_trend_persistence_45d_jerk_v140_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_mild_dd_15pct_freq_180d_jerk_v141_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_diff_std_50d_jerk_v142_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_calmar_60d_jerk_v143_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_realvol_in_dd_45d_jerk_v144_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_diff_kurt_90d_jerk_v145_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_rank_120d_jerk_v146_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_arctan_dur_45d_jerk_v147_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_volume_z_45d_jerk_v148_signal,"closeadj","volume"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_symmetry_75d_jerk_v149_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_bucket_diff_60d_jerk_v150_signal,"closeadj"),
])



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
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f30_drawdown_recovery_metrics_jerk_001_150_REGISTRY.items():
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
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
