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

def f30dr_f30_drawdown_recovery_metrics_dd_20d_slope_v001_signal(close):
    return (close / close.rolling(20,20).max() - 1.0).diff(5).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_63d_slope_v002_signal(closeadj):
    return (closeadj / closeadj.rolling(63,63).max() - 1.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_252d_slope_v003_signal(closeadj):
    return (closeadj / closeadj.rolling(252,252).max() - 1.0).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_504d_slope_v004_signal(closeadj):
    return (closeadj / closeadj.rolling(504,504).max() - 1.0).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_maxdd_30d_slope_v005_signal(closeadj):
    return (closeadj / closeadj.rolling(30,30).max() - 1.0).rolling(30,30).min().diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_maxdd_126d_slope_v006_signal(closeadj):
    return (closeadj / closeadj.rolling(126,126).max() - 1.0).rolling(126,126).min().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_avgdd_60d_slope_v007_signal(closeadj):
    return (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(60,60).mean().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_days_50d_slope_v008_signal(closeadj):
    rmax = closeadj.rolling(50,50).max()
    return _bars_since((closeadj >= rmax).astype(float).where(~rmax.isna()), len(closeadj)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_days_200d_slope_v009_signal(closeadj):
    rmax = closeadj.rolling(200,200).max()
    return _bars_since((closeadj >= rmax).astype(float).where(~rmax.isna()), len(closeadj)).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_integral_40d_slope_v010_signal(closeadj):
    return (closeadj / closeadj.rolling(40,40).max() - 1.0).abs().rolling(40,40).sum().diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_integral_120d_slope_v011_signal(closeadj):
    return (closeadj / closeadj.rolling(120,120).max() - 1.0).abs().rolling(120,120).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_emerge_decay_45d_slope_v012_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs()
    return dd_abs.rolling(45,45).corr(np.sign(dd_abs.diff())).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_ratio_60d_slope_v013_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    return (1.0 - dd.abs() / dd.rolling(60,60).min().abs().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_slope_30d_slope_v014_signal(closeadj):
    return ((closeadj - closeadj.rolling(30,30).min()) / 30.0).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_bars_since_trough_90d_slope_v015_signal(closeadj):
    rmin = closeadj.rolling(90,90).min()
    return _bars_since((closeadj <= rmin).astype(float).where(~rmin.isna()), len(closeadj)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_std_45d_slope_v016_signal(closeadj):
    return (closeadj / closeadj.rolling(45,45).max() - 1.0).rolling(45,45).std().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_count_5pct_100d_slope_v017_signal(closeadj):
    dd = closeadj / closeadj.rolling(100,100).max() - 1.0
    return (dd.abs() > 0.05).astype(float).where(~dd.isna()).rolling(100,100).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_rank_120d_slope_v018_signal(closeadj):
    return (closeadj / closeadj.rolling(30,30).max() - 1.0).rolling(120,120).apply(_rank_last, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_20d_slope_v019_signal(close):
    return (close / close.rolling(20,20).min() - 1.0).diff(5).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_120d_slope_v020_signal(closeadj):
    return (closeadj / closeadj.rolling(120,120).min() - 1.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_max_drawup_50d_slope_v021_signal(closeadj):
    return (closeadj / closeadj.rolling(50,50).min() - 1.0).rolling(50,50).max().diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_dd_ratio_80d_slope_v022_signal(closeadj):
    du = closeadj / closeadj.rolling(80,80).min() - 1.0
    dd = closeadj / closeadj.rolling(80,80).max() - 1.0
    return (du.rolling(80,80).max() / dd.rolling(80,80).min().abs().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_skew_75d_slope_v023_signal(closeadj):
    return (closeadj / closeadj.rolling(75,75).max() - 1.0).rolling(75,75).skew().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_kurt_150d_slope_v024_signal(closeadj):
    return (closeadj / closeadj.rolling(150,150).max() - 1.0).rolling(150,150).kurt().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_mad_std_60d_slope_v025_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    mad = dd.rolling(60,60).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    return (mad / dd.rolling(60,60).std().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_ulcer_30d_slope_v026_signal(closeadj):
    return np.sqrt(((closeadj / closeadj.rolling(30,30).max() - 1.0) ** 2).rolling(30,30).mean()).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_ulcer_pain_ratio_slope_v027_signal(closeadj):
    dd_s = closeadj / closeadj.rolling(30,30).max() - 1.0
    dd_l = closeadj / closeadj.rolling(120,120).max() - 1.0
    us = np.sqrt((dd_s ** 2).rolling(30,30).mean())
    ul = np.sqrt((dd_l ** 2).rolling(120,120).mean())
    return (us / ul.replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_pain_ratio_60d_slope_v028_signal(closeadj):
    avg_r = np.log(closeadj / closeadj.shift(1)).rolling(60,60).mean()
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    return (avg_r / np.sqrt((dd ** 2).rolling(60,60).mean()).replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_calmar_252d_slope_v029_signal(closeadj):
    ret = np.log(closeadj / closeadj.shift(252))
    dd = closeadj / closeadj.rolling(252,252).max() - 1.0
    return (ret / dd.rolling(252,252).min().abs().replace(0.0, np.nan)).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_sterling_120d_slope_v030_signal(closeadj):
    ret = np.log(closeadj / closeadj.shift(120))
    dd = closeadj / closeadj.rolling(120,120).max() - 1.0
    return (ret / dd.rolling(120,120).mean().abs().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_frac_40d_slope_v031_signal(closeadj):
    rmax = closeadj.rolling(40,40).max()
    return (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(40,40).mean().diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_frac_180d_slope_v032_signal(closeadj):
    rmax = closeadj.rolling(180,180).max()
    return (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(180,180).mean().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_over_atr_30d_slope_v033_signal(high, low, closeadj):
    dd_abs = (closeadj / closeadj.rolling(30,30).max() - 1.0).abs()
    pc = closeadj.shift(1)
    atr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1).rolling(14,14).mean()
    return (dd_abs * closeadj / atr.replace(0.0, np.nan)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_over_realvol_90d_slope_v034_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(90,90).max() - 1.0).abs()
    rv = np.log(closeadj / closeadj.shift(1)).rolling(90,90).std()
    return (dd_abs / rv.replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_in_dd_5pct_30d_slope_v035_signal(closeadj):
    dd = closeadj / closeadj.rolling(30,30).max() - 1.0
    return (dd <= -0.05).astype(float).where(~dd.isna()).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_severe_dd_20pct_252d_slope_v036_signal(closeadj):
    dd = closeadj / closeadj.rolling(252,252).max() - 1.0
    return (dd <= -0.20).astype(float).where(~dd.isna()).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_at_new_high_45d_slope_v037_signal(closeadj):
    rmax = closeadj.rolling(45,45).max()
    return ((closeadj >= rmax - 1e-12).astype(float)).where(~rmax.isna()).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_arctan_dd_50d_slope_v038_signal(closeadj):
    return np.arctan(10.0 * (closeadj / closeadj.rolling(50,50).max() - 1.0)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_tanh_uw_frac_80d_slope_v039_signal(closeadj):
    rmax = closeadj.rolling(80,80).max()
    f = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(80,80).mean()
    return np.tanh(2.0 * f - 1.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_sigmoid_dd_rank_60d_slope_v040_signal(closeadj):
    rk = (closeadj / closeadj.rolling(20,20).max() - 1.0).rolling(60,60).apply(_rank_last, raw=True)
    return (1.0 / (1.0 + np.exp(-6.0 * (rk - 0.5)))).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_slope_30d_slope_v041_signal(closeadj):
    return (closeadj / closeadj.rolling(30,30).max() - 1.0).diff(5).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_curvature_90d_slope_v042_signal(closeadj):
    dd = closeadj / closeadj.rolling(90,90).max() - 1.0
    return (dd - 2.0 * dd.shift(10) + dd.shift(20)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_shortdd_longdd_ratio_slope_v043_signal(closeadj):
    dd_s = closeadj / closeadj.rolling(20,20).max() - 1.0
    dd_l = closeadj / closeadj.rolling(120,120).max() - 1.0
    return (dd_s.abs() / dd_l.abs().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_diff_45_180d_slope_v044_signal(closeadj):
    dd_a = closeadj / closeadj.rolling(45,45).max() - 1.0
    dd_b = closeadj / closeadj.rolling(180,180).max() - 1.0
    return (dd_a - dd_b).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_efficiency_60d_slope_v045_signal(closeadj):
    rmax = closeadj.rolling(60,60).max(); rmin = closeadj.rolling(60,60).min()
    return ((closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_speed_30d_slope_v046_signal(closeadj):
    rmin = closeadj.rolling(30,30).min()
    bars = _bars_since((closeadj <= rmin).astype(float).where(~rmin.isna()), len(closeadj))
    return (np.log(closeadj / rmin.replace(0.0, np.nan)) / (bars + 1.0)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_cum_dd_50d_slope_v047_signal(closeadj):
    return (closeadj / closeadj.rolling(50,50).max() - 1.0).rolling(50,50).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_weighted_return_75d_slope_v048_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(75,75).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    num = (r * dd_abs).rolling(75,75).sum()
    den = dd_abs.rolling(75,75).sum().replace(0.0, np.nan)
    return (num / den).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_max_uw_length_120d_slope_v049_signal(closeadj):
    rmax = closeadj.rolling(120,120).max()
    return (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(120,120).apply(_maxrun, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_avg_uw_length_180d_slope_v050_signal(closeadj):
    rmax = closeadj.rolling(180,180).max()
    return (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(180,180).apply(_avgrun, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_maxdd_atr_60d_slope_v051_signal(high, low, closeadj):
    mdd = (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(60,60).min().abs()
    pc = closeadj.shift(1)
    atr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1).rolling(21,21).mean()
    return (mdd * closeadj / atr.replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_skew_100d_slope_v052_signal(closeadj):
    return (closeadj / closeadj.rolling(100,100).min() - 1.0).rolling(100,100).skew().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_kurt_60d_slope_v053_signal(closeadj):
    return (closeadj / closeadj.rolling(60,60).min() - 1.0).rolling(60,60).kurt().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_recovery_30d_slope_v054_signal(closeadj):
    du = closeadj / closeadj.rolling(30,30).min() - 1.0
    return (1.0 - du / du.rolling(30,30).max().replace(0.0, np.nan)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_streak_now_70d_slope_v055_signal(closeadj):
    rmax = closeadj.rolling(70,70).max()
    return _streak_inc((closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_zscore_45d_slope_v056_signal(closeadj):
    dd = closeadj / closeadj.rolling(45,45).max() - 1.0
    return ((dd - dd.rolling(45,45).mean()) / dd.rolling(45,45).std().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_v_shape_30d_slope_v057_signal(closeadj):
    dd = closeadj / closeadj.rolling(30,30).max() - 1.0
    return ((dd - dd.shift(10)).abs() / dd.diff().abs().rolling(10,10).sum().replace(0.0, np.nan)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_corr_dd_vol_90d_slope_v058_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(90,90).max() - 1.0).abs()
    return dd_abs.rolling(90,90).corr(np.log(closeadj / closeadj.shift(1)).rolling(10,10).std()).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_recovery_asymmetry_75d_slope_v059_signal(closeadj):
    rmax = closeadj.rolling(75,75).max()
    below_s = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(75,75).sum()
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    rec_s = ((dd.diff() > 0) & (dd < 0)).astype(float).where(~dd.diff().isna()).rolling(75,75).sum()
    return ((below_s - rec_s) / 75.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_episode_count_120d_slope_v060_signal(closeadj):
    rmax = closeadj.rolling(120,120).max()
    return (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(120,120).apply(_episodes, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_rank_252d_slope_v061_signal(closeadj):
    return (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(252,252).apply(_rank_last, raw=True).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_lag_corr_80d_slope_v062_signal(closeadj):
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    return dd.rolling(80,80).corr(dd.shift(10)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_per_uw_day_60d_slope_v063_signal(closeadj):
    rmax = closeadj.rolling(60,60).max()
    mdd = (closeadj / rmax - 1.0).rolling(60,60).min().abs()
    avg_below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(60,60).mean() * 60.0
    return (mdd / avg_below.replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_sig_uw_days_100d_slope_v064_signal(closeadj):
    rmax = closeadj.rolling(100,100).max()
    out = _bars_since((closeadj >= rmax).astype(float).where(~rmax.isna()), len(closeadj))
    return (1.0 / (1.0 + np.exp(-(out - 25.0) / 15.0))).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_vol_frac_60d_slope_v065_signal(closeadj, volume):
    rmax = closeadj.rolling(60,60).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    return ((below * volume).rolling(60,60).sum() / volume.rolling(60,60).sum().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_mean_median_ratio_75d_slope_v066_signal(closeadj):
    dd = closeadj / closeadj.rolling(75,75).max() - 1.0
    return (dd.rolling(75,75).mean() / dd.rolling(75,75).median().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_integral_50d_slope_v067_signal(closeadj):
    return (closeadj / closeadj.rolling(50,50).min() - 1.0).rolling(50,50).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_slope_streak_60d_slope_v068_signal(closeadj):
    dd_diff = (closeadj / closeadj.rolling(20,20).max() - 1.0).diff()
    return _streak_inc((dd_diff > 0).astype(float).where(~dd_diff.isna()), len(closeadj)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_per_bar_since_trough_90d_slope_v069_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(90,90).max() - 1.0).abs()
    rmin = closeadj.rolling(90,90).min()
    bars = _bars_since((closeadj <= rmin).astype(float).where(~rmin.isna()), len(closeadj))
    return (dd_abs / (bars + 1.0)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_flip_rate_50d_slope_v070_signal(closeadj):
    s = np.sign((closeadj / closeadj.rolling(30,30).max() - 1.0).diff())
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return (flip.rolling(50,50).sum() / 50.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_arctan_recovery_slope_45d_slope_v071_signal(closeadj):
    rmin = closeadj.rolling(45,45).min()
    return np.arctan((closeadj - rmin) / rmin.replace(0.0, np.nan) / 45.0 * 100.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_severe_dd_count_252d_slope_v072_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    return (dd <= -0.10).astype(float).where(~dd.isna()).rolling(252,252).sum().diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_recoverability_140d_slope_v073_signal(closeadj):
    rmin = closeadj.rolling(60,60).min(); rmax = closeadj.rolling(60,60).max()
    dd_abs = (closeadj / rmax - 1.0).abs()
    return ((closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan) * (dd_abs > 0.001).astype(float)).rolling(140,140).mean().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_accel_norm_60d_slope_v074_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    return ((dd - 2.0 * dd.shift(5) + dd.shift(10)) / dd.rolling(10,10).std().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_now_vs_max_120d_slope_v075_signal(closeadj):
    dd = closeadj / closeadj.rolling(120,120).max() - 1.0
    return (dd / dd.rolling(120,120).min().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_15d_slope_v076_signal(close):
    return (close / close.rolling(15,15).max() - 1.0).diff(5).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_42d_slope_v077_signal(closeadj):
    return (closeadj / closeadj.rolling(42,42).max() - 1.0).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_378d_slope_v078_signal(closeadj):
    return (closeadj / closeadj.rolling(378,378).max() - 1.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_40d_slope_v079_signal(closeadj):
    return (closeadj / closeadj.rolling(40,40).min() - 1.0).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_252d_slope_v080_signal(closeadj):
    return (closeadj / closeadj.rolling(252,252).min() - 1.0).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_net_du_dd_30d_slope_v081_signal(close):
    return ((close / close.rolling(30,30).min() - 1.0) + (close / close.rolling(30,30).max() - 1.0)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_du_product_150d_slope_v082_signal(closeadj):
    return ((closeadj / closeadj.rolling(150,150).min() - 1.0) * (closeadj / closeadj.rolling(150,150).max() - 1.0).abs()).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_concavity_60d_slope_v083_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    return (((dd + dd.shift(20) - 2.0 * dd.shift(10)) / 100.0 + (dd + dd.shift(10) - 2.0 * dd.shift(5)) / 25.0) / 2.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_local_trough_count_120d_slope_v084_signal(closeadj):
    rmin20 = closeadj.rolling(20,20).min()
    at_low = (closeadj <= rmin20 + 1e-12).astype(float).where(~rmin20.isna())
    return at_low.rolling(120,120).apply(_episodes, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_q10_60d_slope_v085_signal(closeadj):
    return (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(60,60).quantile(0.10).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_iqr_100d_slope_v086_signal(closeadj):
    dd = closeadj / closeadj.rolling(100,100).max() - 1.0
    return (dd.rolling(100,100).quantile(0.75) - dd.rolling(100,100).quantile(0.25)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_newhigh_streak_60d_slope_v087_signal(closeadj):
    rmax = closeadj.rolling(60,60).max()
    return _streak_inc((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_newlow_streak_45d_slope_v088_signal(closeadj):
    rmin = closeadj.rolling(45,45).min()
    return _streak_inc((closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna()), len(closeadj)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_atr_units_90d_slope_v089_signal(high, low, closeadj):
    dd_abs = (closeadj / closeadj.rolling(90,90).max() - 1.0).abs()
    pc = closeadj.shift(1)
    atr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1).rolling(30,30).mean()
    return (dd_abs * closeadj / atr.replace(0.0, np.nan)).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_under_negskew_45d_slope_v090_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs()
    sk = np.log(closeadj / closeadj.shift(1)).rolling(45,45).skew()
    return (dd_abs * (sk < 0).astype(float).where(~sk.isna())).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_ret_in_dd_60d_slope_v091_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1))
    in_dd = (dd <= -0.05).astype(float).where(~dd.isna())
    return ((r * in_dd).rolling(60,60).sum() / in_dd.rolling(60,60).sum().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_corr_dd_volume_60d_slope_v092_signal(closeadj, volume):
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    return dd.rolling(60,60).corr(np.log(volume.replace(0.0, np.nan))).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_regslope_30d_slope_v093_signal(closeadj):
    return (closeadj / closeadj.rolling(30,30).max() - 1.0).rolling(30,30).apply(_ols_slope, raw=True).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_regslope_120d_slope_v094_signal(closeadj):
    return (closeadj / closeadj.rolling(120,120).max() - 1.0).rolling(120,120).apply(_ols_slope, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_rsq_time_60d_slope_v095_signal(closeadj):
    return (closeadj / closeadj.rolling(60,60).max() - 1.0).rolling(60,60).apply(_ols_rsq, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_vol_ratio_75d_slope_v096_signal(closeadj):
    dd_vol = (closeadj / closeadj.rolling(75,75).max() - 1.0).diff().rolling(75,75).std()
    r_vol = np.log(closeadj / closeadj.shift(1)).rolling(75,75).std()
    return (dd_vol / r_vol.replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_phase_imbalance_45d_slope_v097_signal(closeadj):
    dd_d = (closeadj / closeadj.rolling(20,20).max() - 1.0).diff()
    inc = (dd_d > 0).astype(float).where(~dd_d.isna()).rolling(45,45).sum()
    dec = (dd_d < 0).astype(float).where(~dd_d.isna()).rolling(45,45).sum()
    return ((inc - dec) / 45.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_du_integral_diff_60d_slope_v098_signal(closeadj):
    du_s = (closeadj / closeadj.rolling(60,60).min() - 1.0).rolling(60,60).sum()
    dd_s = (closeadj / closeadj.rolling(60,60).max() - 1.0).abs().rolling(60,60).sum()
    return (du_s - dd_s).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_severity_duration_60d_slope_v099_signal(closeadj):
    rmax = closeadj.rolling(60,60).max()
    return ((closeadj / rmax - 1.0).abs() * _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_30_vs_120_slope_v100_signal(closeadj):
    rmax30 = closeadj.rolling(30,30).max(); rmax120 = closeadj.rolling(120,120).max()
    f30 = (closeadj < rmax30 - 1e-12).astype(float).where(~rmax30.isna()).rolling(30,30).mean()
    f120 = (closeadj < rmax120 - 1e-12).astype(float).where(~rmax120.isna()).rolling(120,120).mean()
    return (f30 - f120).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_sharpe_60d_slope_v101_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1)).where(dd < -0.01)
    return (r.rolling(60,20).mean() / r.rolling(60,20).std().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_max_dd_per_bar_180d_slope_v102_signal(closeadj):
    return ((closeadj / closeadj.rolling(180,180).max() - 1.0).rolling(180,180).min().abs() / 180.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_completeness_60d_slope_v103_signal(closeadj):
    rmax = closeadj.rolling(60,60).max(); rmin = closeadj.rolling(60,60).min()
    return ((closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)).where(closeadj / rmax - 1.0 < -0.01).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_runs_skew_120d_slope_v104_signal(closeadj):
    rmax = closeadj.rolling(120,120).max()
    return (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(120,120).apply(_runskew, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_martin_ratio_90d_slope_v105_signal(closeadj):
    ret = np.log(closeadj / closeadj.shift(90))
    dd = closeadj / closeadj.rolling(90,90).max() - 1.0
    return (ret / np.sqrt((dd ** 2).rolling(90,90).mean()).replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_max_run_dd_weighted_120d_slope_v106_signal(closeadj):
    n = 120; rmax = closeadj.rolling(n,n).max()
    dd = closeadj / rmax - 1.0
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    bv = below.values; dv = dd.values
    for i in range(n - 1, len(closeadj)):
        if np.isnan(bv[i]) or np.isnan(dv[i]):
            continue
        out.iat[i] = _worst_run(bv[i - n + 1: i + 1], dv[i - n + 1: i + 1])
    return out.diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_below_med_freq_50d_slope_v107_signal(closeadj):
    dd = closeadj / closeadj.rolling(50,50).max() - 1.0
    md = dd.rolling(50,50).median()
    return (dd < md).astype(float).where(~dd.isna() & ~md.isna()).rolling(50,50).mean().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_weighted_return_75d_slope_v108_signal(closeadj):
    return (np.log(closeadj / closeadj.shift(75)) * (1.0 - (closeadj / closeadj.rolling(75,75).max() - 1.0).abs())).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_autocorr_60d_slope_v109_signal(closeadj):
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    return dd.rolling(60,60).corr(dd.shift(5)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_max_mean_ratio_100d_slope_v110_signal(closeadj):
    dd = closeadj / closeadj.rolling(100,100).max() - 1.0
    return (dd.rolling(100,100).min().abs() / dd.rolling(100,100).mean().abs().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_using_lows_25d_slope_v111_signal(high, low):
    return (low / high.rolling(25,25).max() - 1.0).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_intrabar_dd_minus_close_dd_100d_slope_v112_signal(high, low, closeadj):
    return ((low / high.rolling(100,100).max() - 1.0) - (closeadj / closeadj.rolling(100,100).max() - 1.0)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_max_dd_step_60d_slope_v113_signal(closeadj):
    return (closeadj / closeadj.rolling(60,60).max() - 1.0).diff().rolling(60,60).min().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_max_recovery_step_60d_slope_v114_signal(closeadj):
    return (closeadj / closeadj.rolling(60,60).max() - 1.0).diff().rolling(60,60).max().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_neg_pos_diff_ratio_50d_slope_v115_signal(closeadj):
    d = (closeadj / closeadj.rolling(50,50).max() - 1.0).diff()
    neg = (-d.where(d < 0, 0.0)).rolling(50,50).sum()
    pos = (d.where(d > 0, 0.0)).rolling(50,50).sum()
    return (neg / (pos + neg).replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_tanh_dd_dur_75d_slope_v116_signal(closeadj):
    rmax = closeadj.rolling(75,75).max()
    bars = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    return np.tanh((closeadj / rmax - 1.0).abs() * bars / 75.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_in_highvol_45d_slope_v117_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs()
    rv = np.log(closeadj / closeadj.shift(1)).rolling(45,45).std()
    rk = rv.rolling(180,180).apply(_rank_last, raw=True)
    return (dd_abs * (rk >= 0.75).astype(float).where(~rk.isna())).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_cum_recovery_50d_slope_v118_signal(closeadj):
    d = (closeadj / closeadj.rolling(50,50).max() - 1.0).diff()
    return d.where(d > 0, 0.0).rolling(50,50).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_cum_deepening_50d_slope_v119_signal(closeadj):
    d = (closeadj / closeadj.rolling(50,50).max() - 1.0).diff()
    return (-d).where(d < 0, 0.0).rolling(50,50).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_rank_dd_180d_slope_v120_signal(closeadj):
    return (closeadj / closeadj.rolling(45,45).max() - 1.0).rolling(180,180).apply(_rank_last, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_room_252d_slope_v121_signal(closeadj):
    dd = closeadj / closeadj.rolling(252,252).max() - 1.0
    return (dd - dd.rolling(252,252).min()).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_vol_weighted_dd_60d_slope_v122_signal(closeadj, volume):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    return ((dd * volume).rolling(60,60).sum() / volume.rolling(60,60).sum().replace(0.0, np.nan)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_median_run_180d_slope_v123_signal(closeadj):
    rmax = closeadj.rolling(180,180).max()
    return (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(180,180).apply(_medrun, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_above_q25_freq_90d_slope_v124_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    q25 = dd.rolling(90,90).quantile(0.25)
    return (dd > q25).astype(float).where(~q25.isna()).rolling(90,90).mean().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_path_directness_45d_slope_v125_signal(closeadj):
    n = 45
    dd = closeadj / closeadj.rolling(n,n).max() - 1.0
    direct = (dd - dd.shift(n)).abs()
    path = dd.diff().abs().rolling(n,n).sum()
    return (direct / path.replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_peak_trough_age_ratio_120d_slope_v126_signal(closeadj):
    rmax = closeadj.rolling(120,120).max(); rmin = closeadj.rolling(120,120).min()
    bh = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    bl = _bars_since((closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna()), len(closeadj))
    return (bh - bl).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_semivar_45d_slope_v127_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    return (r * r).where((dd_abs > 0.02) & (r < 0)).rolling(45,15).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_vs_cumret_corr_75d_slope_v128_signal(closeadj):
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    cr = np.log(closeadj).diff(60)
    return dd.rolling(75,75).corr(cr).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_pos_vs_neg_ret_diff_60d_slope_v129_signal(closeadj):
    dd_abs = (closeadj / closeadj.rolling(60,60).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    return (dd_abs.where(r > 0).rolling(60,10).mean() - dd_abs.where(r < 0).rolling(60,10).mean()).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_per_bar_120d_slope_v130_signal(closeadj):
    rmin = closeadj.rolling(120,120).min()
    bars = _bars_since((closeadj <= rmin + 1e-12).astype(float).where(~rmin.isna()), len(closeadj))
    return (np.log(closeadj / rmin.replace(0.0, np.nan)) / (bars + 1.0)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawdown_rate_from_peak_80d_slope_v131_signal(closeadj):
    rmax = closeadj.rolling(80,80).max()
    bars = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    return (np.log(rmax.replace(0.0, np.nan) / closeadj) / (bars + 1.0)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_rec_to_high_freq_180d_slope_v132_signal(closeadj):
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    dip = (dd <= -0.03).astype(float).where(~dd.isna())
    rmax60 = closeadj.rolling(60,60).max()
    rec_within = (closeadj >= rmax60 - 1e-12).astype(float).where(~rmax60.isna()).rolling(10,10).max()
    return ((dip > 0.5) & (rec_within.shift(-10) > 0.5)).astype(float).rolling(180,180).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_quality_z_60d_slope_v133_signal(closeadj):
    rmax = closeadj.rolling(60,60).max(); rmin = closeadj.rolling(60,60).min()
    rec = (closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)
    return ((rec - rec.rolling(60,60).mean()) / rec.rolling(60,60).std().replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_z_long_240d_slope_v134_signal(closeadj):
    dd = closeadj / closeadj.rolling(30,30).max() - 1.0
    return ((dd - dd.rolling(240,240).mean()) / dd.rolling(240,240).std().replace(0.0, np.nan)).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_days_rank_252d_slope_v135_signal(closeadj):
    rmax = closeadj.rolling(90,90).max()
    bars = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    return bars.rolling(252,252).apply(_rank_last, raw=True).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_regime_change_60d_slope_v136_signal(closeadj):
    recent = (closeadj / closeadj.rolling(30,30).max() - 1.0).abs().rolling(60,60).mean()
    return (recent - recent.shift(60)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_range_75d_slope_v137_signal(closeadj):
    dd = closeadj / closeadj.rolling(75,75).max() - 1.0
    return (dd.rolling(75,75).max() - dd.rolling(75,75).min()).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_avg_dd_abs_25d_slope_v138_signal(close):
    return (close / close.rolling(25,25).max() - 1.0).abs().rolling(25,25).mean().diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_halflife_proxy_60d_slope_v139_signal(closeadj):
    dd = closeadj / closeadj.rolling(20,20).max() - 1.0
    mindd = dd.rolling(60,60).min()
    return (dd >= 0.5 * mindd).astype(float).where(~mindd.isna()).rolling(60,60).sum().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_trend_persistence_45d_slope_v140_signal(closeadj):
    dd_d = (closeadj / closeadj.rolling(20,20).max() - 1.0).diff()
    return (np.sign(dd_d) * np.sign(dd_d.shift(1)) > 0).astype(float).where(~dd_d.isna() & ~dd_d.shift(1).isna()).rolling(45,45).mean().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_mild_dd_15pct_freq_180d_slope_v141_signal(closeadj):
    dd = closeadj / closeadj.rolling(120,120).max() - 1.0
    return (dd <= -0.15).astype(float).where(~dd.isna()).rolling(180,180).mean().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_diff_std_50d_slope_v142_signal(closeadj):
    return (closeadj / closeadj.rolling(30,30).max() - 1.0).diff().rolling(50,50).std().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_calmar_60d_slope_v143_signal(closeadj):
    ret = np.log(closeadj / closeadj.shift(60))
    dd = closeadj / closeadj.rolling(60,60).max() - 1.0
    return (ret / dd.rolling(60,60).min().abs().replace(0.0, np.nan)).diff(63).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_realvol_in_dd_45d_slope_v144_signal(closeadj):
    n = 45
    dd = closeadj / closeadj.rolling(n,n).max() - 1.0
    r = np.log(closeadj / closeadj.shift(1)).where(dd <= -0.02)
    return r.rolling(n,10).std().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_diff_kurt_90d_slope_v145_signal(closeadj):
    return (closeadj / closeadj.rolling(45,45).max() - 1.0).diff().rolling(90,90).kurt().diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_drawup_rank_120d_slope_v146_signal(closeadj):
    return (closeadj / closeadj.rolling(30,30).min() - 1.0).rolling(120,120).apply(_rank_last, raw=True).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_arctan_dur_45d_slope_v147_signal(closeadj):
    rmax = closeadj.rolling(45,45).max()
    bars = _bars_since((closeadj >= rmax - 1e-12).astype(float).where(~rmax.isna()), len(closeadj))
    return np.arctan(bars / 15.0).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_dd_volume_z_45d_slope_v148_signal(closeadj, volume):
    x = (closeadj / closeadj.rolling(45,45).max() - 1.0).abs() * np.log(volume.replace(0.0, np.nan))
    return ((x - x.rolling(45,45).mean()) / x.rolling(45,45).std().replace(0.0, np.nan)).diff(10).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_recovery_symmetry_75d_slope_v149_signal(closeadj):
    dd_d = (closeadj / closeadj.rolling(20,20).max() - 1.0).diff()
    rs = (dd_d > 0).astype(float).where(~dd_d.isna()).rolling(75,75).sum()
    ds = (dd_d < 0).astype(float).where(~dd_d.isna()).rolling(75,75).sum()
    return (rs / ds.replace(0.0, np.nan)).diff(21).replace([np.inf,-np.inf],np.nan)
def f30dr_f30_drawdown_recovery_metrics_uw_bucket_diff_60d_slope_v150_signal(closeadj):
    rmax = closeadj.rolling(30,30).max()
    recent = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna()).rolling(30,30).mean()
    return (recent - recent.shift(30)).diff(21).replace([np.inf,-np.inf],np.nan)
def _e(fn,*inputs): return fn.__name__,{"inputs":list(inputs),"func":fn}
f30_drawdown_recovery_metrics_slope_001_150_REGISTRY = dict([
    _e(f30dr_f30_drawdown_recovery_metrics_dd_20d_slope_v001_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_63d_slope_v002_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_252d_slope_v003_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_504d_slope_v004_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_maxdd_30d_slope_v005_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_maxdd_126d_slope_v006_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_avgdd_60d_slope_v007_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_days_50d_slope_v008_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_days_200d_slope_v009_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_integral_40d_slope_v010_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_integral_120d_slope_v011_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_emerge_decay_45d_slope_v012_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_ratio_60d_slope_v013_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_slope_30d_slope_v014_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_bars_since_trough_90d_slope_v015_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_std_45d_slope_v016_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_count_5pct_100d_slope_v017_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_rank_120d_slope_v018_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_20d_slope_v019_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_120d_slope_v020_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_drawup_50d_slope_v021_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_dd_ratio_80d_slope_v022_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_skew_75d_slope_v023_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_kurt_150d_slope_v024_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_mad_std_60d_slope_v025_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_ulcer_30d_slope_v026_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_ulcer_pain_ratio_slope_v027_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_pain_ratio_60d_slope_v028_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_calmar_252d_slope_v029_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_sterling_120d_slope_v030_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_frac_40d_slope_v031_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_frac_180d_slope_v032_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_over_atr_30d_slope_v033_signal,"high","low","closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_over_realvol_90d_slope_v034_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_in_dd_5pct_30d_slope_v035_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_severe_dd_20pct_252d_slope_v036_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_at_new_high_45d_slope_v037_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_arctan_dd_50d_slope_v038_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_tanh_uw_frac_80d_slope_v039_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_sigmoid_dd_rank_60d_slope_v040_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_slope_30d_slope_v041_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_curvature_90d_slope_v042_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_shortdd_longdd_ratio_slope_v043_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_diff_45_180d_slope_v044_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_efficiency_60d_slope_v045_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_speed_30d_slope_v046_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_cum_dd_50d_slope_v047_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_weighted_return_75d_slope_v048_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_uw_length_120d_slope_v049_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_avg_uw_length_180d_slope_v050_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_maxdd_atr_60d_slope_v051_signal,"high","low","closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_skew_100d_slope_v052_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_kurt_60d_slope_v053_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_recovery_30d_slope_v054_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_streak_now_70d_slope_v055_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_zscore_45d_slope_v056_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_v_shape_30d_slope_v057_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_corr_dd_vol_90d_slope_v058_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_recovery_asymmetry_75d_slope_v059_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_episode_count_120d_slope_v060_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_rank_252d_slope_v061_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_lag_corr_80d_slope_v062_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_per_uw_day_60d_slope_v063_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_sig_uw_days_100d_slope_v064_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_vol_frac_60d_slope_v065_signal,"closeadj","volume"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_mean_median_ratio_75d_slope_v066_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_integral_50d_slope_v067_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_slope_streak_60d_slope_v068_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_per_bar_since_trough_90d_slope_v069_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_flip_rate_50d_slope_v070_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_arctan_recovery_slope_45d_slope_v071_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_severe_dd_count_252d_slope_v072_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_recoverability_140d_slope_v073_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_accel_norm_60d_slope_v074_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_now_vs_max_120d_slope_v075_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_15d_slope_v076_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_42d_slope_v077_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_378d_slope_v078_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_40d_slope_v079_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_252d_slope_v080_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_net_du_dd_30d_slope_v081_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_du_product_150d_slope_v082_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_concavity_60d_slope_v083_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_local_trough_count_120d_slope_v084_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_q10_60d_slope_v085_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_iqr_100d_slope_v086_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_newhigh_streak_60d_slope_v087_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_newlow_streak_45d_slope_v088_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_atr_units_90d_slope_v089_signal,"high","low","closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_under_negskew_45d_slope_v090_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_ret_in_dd_60d_slope_v091_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_corr_dd_volume_60d_slope_v092_signal,"closeadj","volume"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_regslope_30d_slope_v093_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_regslope_120d_slope_v094_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_rsq_time_60d_slope_v095_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_vol_ratio_75d_slope_v096_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_phase_imbalance_45d_slope_v097_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_du_integral_diff_60d_slope_v098_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_severity_duration_60d_slope_v099_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_30_vs_120_slope_v100_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_sharpe_60d_slope_v101_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_dd_per_bar_180d_slope_v102_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_completeness_60d_slope_v103_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_runs_skew_120d_slope_v104_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_martin_ratio_90d_slope_v105_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_run_dd_weighted_120d_slope_v106_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_below_med_freq_50d_slope_v107_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_weighted_return_75d_slope_v108_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_autocorr_60d_slope_v109_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_max_mean_ratio_100d_slope_v110_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_using_lows_25d_slope_v111_signal,"high","low"),
    _e(f30dr_f30_drawdown_recovery_metrics_intrabar_dd_minus_close_dd_100d_slope_v112_signal,"high","low","closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_dd_step_60d_slope_v113_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_max_recovery_step_60d_slope_v114_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_neg_pos_diff_ratio_50d_slope_v115_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_tanh_dd_dur_75d_slope_v116_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_in_highvol_45d_slope_v117_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_cum_recovery_50d_slope_v118_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_cum_deepening_50d_slope_v119_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_rank_dd_180d_slope_v120_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_room_252d_slope_v121_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_vol_weighted_dd_60d_slope_v122_signal,"closeadj","volume"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_median_run_180d_slope_v123_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_above_q25_freq_90d_slope_v124_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_path_directness_45d_slope_v125_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_peak_trough_age_ratio_120d_slope_v126_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_semivar_45d_slope_v127_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_vs_cumret_corr_75d_slope_v128_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_pos_vs_neg_ret_diff_60d_slope_v129_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_per_bar_120d_slope_v130_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawdown_rate_from_peak_80d_slope_v131_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_rec_to_high_freq_180d_slope_v132_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_quality_z_60d_slope_v133_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_z_long_240d_slope_v134_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_days_rank_252d_slope_v135_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_regime_change_60d_slope_v136_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_range_75d_slope_v137_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_avg_dd_abs_25d_slope_v138_signal,"close"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_halflife_proxy_60d_slope_v139_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_trend_persistence_45d_slope_v140_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_mild_dd_15pct_freq_180d_slope_v141_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_diff_std_50d_slope_v142_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_calmar_60d_slope_v143_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_realvol_in_dd_45d_slope_v144_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_diff_kurt_90d_slope_v145_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_drawup_rank_120d_slope_v146_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_arctan_dur_45d_slope_v147_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_dd_volume_z_45d_slope_v148_signal,"closeadj","volume"),
    _e(f30dr_f30_drawdown_recovery_metrics_recovery_symmetry_75d_slope_v149_signal,"closeadj"),
    _e(f30dr_f30_drawdown_recovery_metrics_uw_bucket_diff_60d_slope_v150_signal,"closeadj"),
])
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
    open_ = close * np.exp(-rng.normal(0.0, 0.008, size=n) * 0.5)
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
    results = {}
    for name, entry in f30_drawdown_recovery_metrics_slope_001_150_REGISTRY.items():
        out = entry["func"](*[df[c] for c in entry["inputs"]])
        assert isinstance(out, pd.Series) and len(out) == len(df)
        clean = out.dropna()
        assert len(clean) > 0 and (float(clean.std()) > 0.0 or clean.nunique() > 1)
        results[name] = out
    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80
    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:].replace([np.inf,-np.inf],np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    assert max_corr <= 0.95 + 1e-9
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
    _self_test()
