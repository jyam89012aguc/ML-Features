"""f21_raw_volume_metrics slope 001-150 (1st derivative)."""
from __future__ import annotations

import numpy as np
import pandas as pd

def _sma(s, n): return s.rolling(n, min_periods=n).mean()
def _ema(s, n): return s.ewm(span=n, adjust=False, min_periods=n).mean()
def _mad(x): return float(np.mean(np.abs(x - np.mean(x))))

def _streak_last_true(x):
    idx = np.where(x > 0.5)[0]
    return float(len(x)) if idx.size == 0 else float(len(x) - 1 - idx[-1])

def _consec_true(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5: c += 1
        else: break
    return float(c)

def _hurst_rs(x):
    n = len(x)
    if n < 16 or not np.all(np.isfinite(x)):
        return np.nan
    y = np.asarray(x, dtype=float); dev = y - y.mean()
    z = np.cumsum(dev); R = z.max() - z.min(); S = y.std(ddof=0)
    if S == 0.0 or not np.isfinite(R / S) or R / S <= 0.0:
        return np.nan
    return float(np.log(R / S) / np.log(n))

def _acf_lag(x, k):
    if len(x) < k + 2 or not np.all(np.isfinite(x)):
        return np.nan
    a = x[k:]; b = x[:-k]
    if a.std() == 0.0 or b.std() == 0.0:
        return np.nan
    return float(np.corrcoef(a, b)[0, 1])

def _acf_l1(x): return _acf_lag(x, 1)
def _acf_l2(x): return _acf_lag(x, 2)
def _acf_l5(x): return _acf_lag(x, 5)

def _gini(x):
    if np.any(x < 0.0) or len(x) < 2 or not np.all(np.isfinite(x)): return np.nan
    y = np.sort(x); n = len(y); s = y.sum()
    return np.nan if s == 0.0 else float((n + 1.0 - 2.0 * np.cumsum(y).sum() / s) / n)

def _ent10(x):
    if len(x) < 5 or not np.all(np.isfinite(x)) or np.all(x == x[0]): return np.nan
    h, _ = np.histogram(x, bins=10); p = h / h.sum(); p = p[p > 0.0]
    return float(-np.sum(p * np.log(p)))

def _theil(x):
    if len(x) < 5 or not np.all(np.isfinite(x)) or np.any(x <= 0.0): return np.nan
    m = x.mean()
    if m == 0.0: return np.nan
    r = x / m
    return float(np.sum(r * np.log(r)) / len(x))

def _ax_max(x):
    return np.nan if len(x) == 0 or not np.all(np.isfinite(x)) else float((len(x) - 1 - int(np.argmax(x))) / max(1, len(x) - 1))

def _ax_min(x):
    return np.nan if len(x) == 0 or not np.all(np.isfinite(x)) else float((len(x) - 1 - int(np.argmin(x))) / max(1, len(x) - 1))

def _winsor_mean(x):
    if not np.all(np.isfinite(x)): return np.nan
    lo = np.quantile(x, 0.10); hi = np.quantile(x, 0.90)
    return float(np.mean(np.clip(x, lo, hi)))

def _trimmed_mean(x):
    if not np.all(np.isfinite(x)) or len(x) < 5: return np.nan
    k = int(np.floor(0.1 * len(x)))
    if k * 2 >= len(x): return np.nan
    y = np.sort(x)
    return float(np.mean(y[k:len(y) - k]))

def _runs(x):
    if len(x) < 10 or not np.all(np.isfinite(x)): return np.nan
    b = (x > np.median(x)).astype(int)
    if b.sum() == 0 or b.sum() == len(b): return np.nan
    return float((int(np.sum(b[1:] != b[:-1])) + 1) / (len(b) / 2.0))

def _t5_share(x):
    if len(x) < 6 or not np.all(np.isfinite(x)): return np.nan
    s = x.sum()
    return np.nan if s == 0.0 else float(np.sort(x)[::-1][:5].sum() / s)

def _us75(x):
    if len(x) < 5 or not np.all(np.isfinite(x)): return np.nan
    q = np.quantile(x, 0.75); s = x.sum()
    return np.nan if s == 0.0 else float(x[x > q].sum() / s)

def _ls25(x):
    if len(x) < 5 or not np.all(np.isfinite(x)): return np.nan
    q = np.quantile(x, 0.25); s = x.sum()
    return np.nan if s == 0.0 else float(x[x < q].sum() / s)

def _ta10(x):
    if len(x) < 20 or not np.all(np.isfinite(x)): return np.nan
    y = np.sort(x); k = max(1, int(0.1 * len(y)))
    top = y[-k:].mean(); bot = y[:k].mean()
    return np.nan if bot == 0.0 or top == 0.0 else float(np.log(top / bot))

def _tail_top10(x):
    if len(x) < 10 or not np.all(np.isfinite(x)): return np.nan
    y = np.sort(x)[::-1]; k = max(1, int(0.1 * len(y)))
    top = y[:k].mean(); rest = y[k:].mean()
    return np.nan if rest == 0.0 else float(top / rest)

def _sp(x):
    if len(x) < 5 or not np.all(np.isfinite(x)): return np.nan
    y = np.sort(x)[::-1]
    return np.nan if y[0] == 0.0 else float(np.log(y[1] / y[0]))

def _slp(x):
    t = np.arange(len(x), dtype=float)
    if not np.all(np.isfinite(x)): return np.nan
    mt = t.mean(); cov = np.sum((t - mt) * (x - x.mean())); var = np.sum((t - mt) ** 2)
    return np.nan if var == 0.0 else float(cov / var)

def _r2(x):
    t = np.arange(len(x), dtype=float)
    if not np.all(np.isfinite(x)): return np.nan
    mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx)); vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
    return np.nan if vt == 0.0 or vx == 0.0 else float((cov * cov) / (vt * vx))

def _ar1(x):
    if len(x) < 4 or not np.all(np.isfinite(x)): return np.nan
    a = x[1:]; b = x[:-1]; mb = b.mean()
    var = np.sum((b - mb) ** 2)
    return np.nan if var == 0.0 else float(np.sum((b - mb) * (a - a.mean())) / var)

def _ago_max(x):
    return np.nan if len(x) == 0 or not np.all(np.isfinite(x)) else float(len(x) - 1 - int(np.argmax(x)))

def _detr_std(x):
    if len(x) < 30 or not np.all(np.isfinite(x)): return np.nan
    t = np.arange(len(x), dtype=float); mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx)); var = np.sum((t - mt) ** 2)
    if var == 0.0: return np.nan
    slope = cov / var
    return float((x - (slope * t + (mx - slope * mt))).std())

def _kl_halves(x):
    if len(x) < 20 or not np.all(np.isfinite(x)): return np.nan
    h = len(x) // 2; a = x[:h]; b = x[h:]
    lo = float(min(a.min(), b.min())); hi = float(max(a.max(), b.max()))
    if hi <= lo: return np.nan
    edges = np.linspace(lo, hi, 9)
    ha, _ = np.histogram(a, bins=edges); hb, _ = np.histogram(b, bins=edges)
    eps = 1e-6
    pa = (ha + eps) / (ha.sum() + 8.0 * eps); pb = (hb + eps) / (hb.sum() + 8.0 * eps)
    return float(np.sum(pa * np.log(pa / pb)) + np.sum(pb * np.log(pb / pa)))

def _gap_top10(x):
    if len(x) < 20 or not np.all(np.isfinite(x)): return np.nan
    hits = np.where(x >= np.quantile(x, 0.90))[0]
    return float(len(x)) if hits.size < 2 else float(np.diff(hits).max())

def _longest_run(x):
    if len(x) == 0 or not np.all(np.isfinite(x)): return np.nan
    best = 0; cur = 0
    for v in x:
        if v > 0.5:
            cur += 1
            if cur > best: best = cur
        else: cur = 0
    return float(best)

def _signed_streak(x):
    if len(x) == 0: return np.nan
    last = x[-1]
    if last == 0.0: return 0.0
    c = 0
    for v in x[::-1]:
        if v == last: c += 1
        else: break
    return float(c) * float(np.sign(last))

def _net(x): return np.nan if len(x) == 0 else float(x.sum())

def _dft_sl(x):
    if not np.all(np.isfinite(x)) or len(x) < 30: return np.nan
    x0 = x - x.mean(); n = len(x0)
    ks = max(1, int(round(n / 5.0))); kl = max(1, int(round(n / 30.0)))
    if ks >= n or kl >= n or ks == kl: return np.nan
    fft = np.fft.rfft(x0)
    a = float(np.abs(fft[ks])); b = float(np.abs(fft[kl]))
    return np.nan if b == 0.0 else float(a / b)

def _com(x):
    if len(x) == 0 or not np.all(np.isfinite(x)) or np.any(x < 0.0): return np.nan
    s = x.sum()
    if s == 0.0: return np.nan
    t = np.arange(len(x), dtype=float)
    return float(np.sum(t * x) / s / max(1.0, len(x) - 1.0))

def f21rv_f21_raw_volume_metrics_logvol_sma5_5d_slope_v001_signal(volume):
    return np.log(volume / _sma(volume, 5)).diff(5).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_sma5_sma50_10d_slope_v002_signal(volume):
    return np.log(_sma(volume, 5) / _sma(volume, 50)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_sma20_sma200_63d_slope_v003_signal(volume):
    return np.log(_sma(volume, 20) / _sma(volume, 200)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_ema_diff_10_60_21d_slope_v004_signal(volume):
    return np.log(_ema(volume, 10) / _ema(volume, 60)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_median_vol_ratio_20_120_21d_slope_v005_signal(volume):
    return np.log(volume.rolling(20, min_periods=20).median() / volume.rolling(120, min_periods=120).median().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_volz_21d_5d_slope_v006_signal(volume):
    return ((volume - _sma(volume, 21)) / volume.rolling(21, min_periods=21).std().replace(0.0, np.nan)).diff(5).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_volrank_60d_10d_slope_v007_signal(volume):
    return volume.rolling(60, min_periods=60).rank(pct=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_signed_share_30d_10d_slope_v008_signal(close, closeadj, volume):
    dv = closeadj * volume
    return ((np.sign(close.diff(1)) * dv).rolling(30, min_periods=30).sum() / dv.rolling(30, min_periods=30).sum().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_termstruct_5_252_63d_slope_v009_signal(closeadj, volume):
    dv = closeadj * volume
    return np.log(_sma(dv, 5) / _sma(dv, 252)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_termstruct_20_120_21d_slope_v010_signal(closeadj, volume):
    dv = closeadj * volume
    return np.log(_sma(dv, 20) / _sma(dv, 120)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_skew_60d_21d_slope_v011_signal(volume):
    return volume.rolling(60, min_periods=60).skew().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_kurt_180d_63d_slope_v012_signal(volume):
    return volume.rolling(180, min_periods=180).kurt().diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_skew_120d_21d_slope_v013_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(120, min_periods=120).skew().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_kurt_40d_10d_slope_v014_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(40, min_periods=40).kurt().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_mad_over_std_45d_21d_slope_v015_signal(volume):
    return (volume.rolling(45, min_periods=45).apply(_mad, raw=True) / volume.rolling(45, min_periods=45).std().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_cv_60d_21d_slope_v016_signal(volume):
    m = _sma(volume, 60); sd = volume.rolling(60, min_periods=60).std()
    return (sd / m.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_gini_30d_10d_slope_v017_signal(volume):
    return volume.rolling(30, min_periods=30).apply(_gini, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_iqr_over_med_50d_21d_slope_v018_signal(volume):
    q25 = volume.rolling(50, min_periods=50).quantile(0.25)
    q75 = volume.rolling(50, min_periods=50).quantile(0.75)
    med = volume.rolling(50, min_periods=50).median()
    return ((q75 - q25) / med.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_volpct_1d_5d_slope_v019_signal(volume):
    return volume.pct_change(1).diff(5).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_diff_1d_5d_slope_v020_signal(volume):
    return np.log(volume / volume.shift(1)).diff(5).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_abs_logvol_diff_10d_5d_slope_v021_signal(volume):
    return np.log(volume / volume.shift(1)).abs().rolling(10, min_periods=10).mean().diff(5).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_spike_bin_21d_10d_slope_v022_signal(volume):
    m = _sma(volume, 21)
    return (volume > 2.0 * m).astype(float).where(~m.isna()).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_spike_count_60d_21d_slope_v023_signal(volume):
    m = _sma(volume, 21)
    return (volume > 2.0 * m).astype(float).where(~m.isna()).rolling(60, min_periods=60).sum().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_spike_mag_60d_63d_slope_v024_signal(volume):
    m = _sma(volume, 21)
    return (volume / m.replace(0.0, np.nan)).rolling(60, min_periods=60).max().diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dayssince_spike_80d_21d_slope_v025_signal(volume):
    m = _sma(volume, 21)
    return (volume > 2.0 * m).astype(float).where(~m.isna()).rolling(80, min_periods=80).apply(_streak_last_true, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dry_bin_21d_10d_slope_v026_signal(volume):
    m = _sma(volume, 21)
    return (volume < 0.5 * m).astype(float).where(~m.isna()).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dry_streak_60d_21d_slope_v027_signal(volume):
    m = _sma(volume, 21)
    return (volume < 0.5 * m).astype(float).where(~m.isna()).rolling(60, min_periods=60).apply(_consec_true, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dry_count_120d_63d_slope_v028_signal(volume):
    m = _sma(volume, 21)
    return (volume < 0.5 * m).astype(float).where(~m.isna()).rolling(120, min_periods=120).sum().diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_std_30d_10d_slope_v029_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(30, min_periods=30).std().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_volofvol_60d_21d_slope_v030_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(20, min_periods=20).std().rolling(60, min_periods=60).std().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_range_over_mean_40d_10d_slope_v031_signal(volume):
    return ((volume.rolling(40, min_periods=40).max() - volume.rolling(40, min_periods=40).min()) / _sma(volume, 40).replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_pctchg_std_45d_21d_slope_v032_signal(volume):
    return volume.pct_change(1).rolling(45, min_periods=45).std().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_acf_lag1_45d_10d_slope_v033_signal(volume):
    return volume.rolling(45, min_periods=45).apply(_acf_l1, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_acf_lag5_80d_21d_slope_v034_signal(volume):
    return volume.rolling(80, min_periods=80).apply(_acf_l5, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_acf_lag1_120d_63d_slope_v035_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(120, min_periods=120).apply(_acf_l1, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_share_top5_30d_10d_slope_v036_signal(volume):
    return volume.rolling(30, min_periods=30).apply(_t5_share, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_cone_45d_21d_slope_v037_signal(volume):
    mn = volume.rolling(45, min_periods=45).min(); mx = volume.rolling(45, min_periods=45).max()
    return ((volume - mn) / (mx - mn).replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_change_streak_40d_10d_slope_v038_signal(volume):
    return np.sign(volume.diff(1)).rolling(40, min_periods=40).apply(_net, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_meanrev_rate_50d_21d_slope_v039_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(50, min_periods=50).apply(_ar1, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_sharpe_45d_21d_slope_v040_signal(volume):
    m = _sma(volume, 45); sd = volume.rolling(45, min_periods=45).std()
    return (m / sd.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_high_vol_top25_60d_21d_slope_v041_signal(volume):
    q = volume.rolling(60, min_periods=60).quantile(0.75)
    return (volume > q).astype(float).where(~q.isna()).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_low_vol_bot25_60d_63d_slope_v042_signal(volume):
    q = volume.rolling(60, min_periods=60).quantile(0.25)
    return (volume < q).astype(float).where(~q.isna()).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dayssince_highvol_100d_21d_slope_v043_signal(volume):
    q = volume.rolling(100, min_periods=100).quantile(0.90)
    return (volume > q).astype(float).where(~q.isna()).rolling(100, min_periods=100).apply(_streak_last_true, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dayssince_lowvol_100d_63d_slope_v044_signal(volume):
    q = volume.rolling(100, min_periods=100).quantile(0.10)
    return (volume < q).astype(float).where(~q.isna()).rolling(100, min_periods=100).apply(_streak_last_true, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_stoch_30d_21d_slope_v045_signal(volume):
    mn = volume.rolling(30, min_periods=30).min(); mx = volume.rolling(30, min_periods=30).max()
    return (100.0 * (volume - mn) / (mx - mn).replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_signed_vol_norm_20d_5d_slope_v046_signal(close, volume):
    s = np.sign(close.diff(1)); m = _sma(volume, 20)
    return (s * volume / m.replace(0.0, np.nan)).diff(5).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_signed_vol_share_40d_10d_slope_v047_signal(close, volume):
    s = np.sign(close.diff(1))
    return ((s * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_acf_sign_flips_50d_21d_slope_v048_signal(volume):
    s = np.sign(volume.diff(1))
    return (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()).rolling(50, min_periods=50).mean().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_max_to_min_30d_10d_slope_v049_signal(volume):
    return np.log(volume.rolling(30, min_periods=30).max() / volume.rolling(30, min_periods=30).min().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_signed_logvol_diff_25d_21d_slope_v050_signal(volume):
    return np.sign(np.log(volume / volume.shift(1))).rolling(25, min_periods=25).sum().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_streak_up_30d_10d_slope_v051_signal(volume):
    return (volume.diff(1) > 0.0).astype(float).where(~volume.diff(1).isna()).rolling(30, min_periods=30).apply(_consec_true, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_streak_down_30d_21d_slope_v052_signal(volume):
    return (volume.diff(1) < 0.0).astype(float).where(~volume.diff(1).isna()).rolling(30, min_periods=30).apply(_consec_true, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_entropy_30d_10d_slope_v053_signal(volume):
    return volume.rolling(30, min_periods=30).apply(_ent10, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_logslope_60d_21d_slope_v054_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(60, min_periods=60).apply(_slp, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_logslope_r2_80d_63d_slope_v055_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(80, min_periods=80).apply(_r2, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_max_argmax_50d_10d_slope_v056_signal(volume):
    return volume.rolling(50, min_periods=50).apply(_ax_max, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_min_argmin_50d_21d_slope_v057_signal(volume):
    return volume.rolling(50, min_periods=50).apply(_ax_min, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_pct_up_days_120d_63d_slope_v058_signal(volume):
    return (volume.diff(1) > 0.0).astype(float).where(~volume.diff(1).isna()).rolling(120, min_periods=120).mean().diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_acf_change_lag1_60d_21d_slope_v059_signal(volume):
    return volume.pct_change(1).rolling(60, min_periods=60).apply(_acf_l1, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_pctchg_skew_60d_63d_slope_v060_signal(volume):
    return volume.pct_change(1).rolling(60, min_periods=60).skew().diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_iqr_over_med_140d_21d_slope_v061_signal(closeadj, volume):
    dv = closeadj * volume
    q25 = dv.rolling(140, min_periods=140).quantile(0.25); q75 = dv.rolling(140, min_periods=140).quantile(0.75)
    return ((q75 - q25) / dv.rolling(140, min_periods=140).median().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_cv_90d_21d_slope_v062_signal(closeadj, volume):
    dv = closeadj * volume; m = _sma(dv, 90); sd = dv.rolling(90, min_periods=90).std()
    return (sd / m.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_volofvol_80d_21d_slope_v063_signal(closeadj, volume):
    return np.log((closeadj * volume).replace(0.0, np.nan)).rolling(20, min_periods=20).std().rolling(80, min_periods=80).std().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_pct_extreme_30d_10d_slope_v064_signal(volume):
    z = (volume - _sma(volume, 21)) / volume.rolling(21, min_periods=21).std().replace(0.0, np.nan)
    return (z.abs() > 1.5).astype(float).where(~z.isna()).rolling(30, min_periods=30).mean().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_dispnorm_70d_63d_slope_v065_signal(volume):
    q10 = volume.rolling(70, min_periods=70).quantile(0.10); q90 = volume.rolling(70, min_periods=70).quantile(0.90)
    return ((q90 - q10) / (q90 + q10).replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_volume_zero_streak_50d_21d_slope_v066_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return (lv.rolling(5, min_periods=5).mean() - lv.rolling(50, min_periods=50).mean()).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_acf_lag2_60d_21d_slope_v067_signal(volume):
    return volume.rolling(60, min_periods=60).apply(_acf_l2, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_logsharpe_120d_63d_slope_v068_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return (lv.rolling(120, min_periods=120).mean() / lv.rolling(120, min_periods=120).std().replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_above_below_ratio_45d_10d_slope_v069_signal(volume):
    m = _sma(volume, 21)
    return ((volume > m).astype(float).where(~m.isna()).rolling(45, min_periods=45).mean() - 0.5).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_pctchg_abs_45d_21d_slope_v070_signal(volume):
    return volume.pct_change(1).abs().rolling(45, min_periods=45).mean().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_streak_high_50d_10d_slope_v071_signal(volume):
    m = _sma(volume, 21)
    return (volume > m).astype(float).where(~m.isna()).rolling(50, min_periods=50).apply(_consec_true, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_acf_lag1_70d_21d_slope_v072_signal(closeadj, volume):
    return (closeadj * volume).rolling(70, min_periods=70).apply(_acf_l1, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_zerocenter_norm_15d_10d_slope_v073_signal(volume):
    med = volume.rolling(15, min_periods=15).median()
    q25 = volume.rolling(15, min_periods=15).quantile(0.25); q75 = volume.rolling(15, min_periods=15).quantile(0.75)
    return ((volume - med) / (q75 - q25).replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_runs_test_60d_21d_slope_v074_signal(volume):
    return volume.rolling(60, min_periods=60).apply(_runs, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_extreme_tail_75d_63d_slope_v075_signal(volume):
    return volume.rolling(75, min_periods=75).apply(_tail_top10, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_dd_from_max_60d_10d_slope_v076_signal(volume):
    return np.log(volume / volume.rolling(60, min_periods=60).max().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_gain_from_min_60d_21d_slope_v077_signal(volume):
    return np.log(volume / volume.rolling(60, min_periods=60).min().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_dd_from_max_200d_63d_slope_v078_signal(volume):
    return np.log(volume / volume.rolling(200, min_periods=200).max().replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_hurst_60d_21d_slope_v079_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(60, min_periods=60).apply(_hurst_rs, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_hurst_180d_63d_slope_v080_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(180, min_periods=180).apply(_hurst_rs, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_fisher_50d_21d_slope_v081_signal(volume):
    r = (2.0 * volume.rolling(50, min_periods=50).rank(pct=True) - 1.0).clip(-0.999, 0.999)
    return (0.5 * np.log((1.0 + r) / (1.0 - r))).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_pctB_30d_10d_slope_v082_signal(volume):
    m = _sma(volume, 30); sd = volume.rolling(30, min_periods=30).std()
    return ((volume - (m - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_bandwidth_90d_63d_slope_v083_signal(volume):
    return (4.0 * volume.rolling(90, min_periods=90).std() / _sma(volume, 90).replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_streak_above_med_120d_21d_slope_v084_signal(volume):
    med = volume.rolling(120, min_periods=120).median()
    return (volume > med).astype(float).where(~med.isna()).rolling(120, min_periods=120).apply(_longest_run, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_peak_count_120d_63d_slope_v085_signal(volume):
    a = volume.shift(1); b = volume.shift(-1)
    peak = ((volume > a) & (volume > b)).astype(float).where(~a.isna() & ~b.isna())
    return (peak.rolling(120, min_periods=120).sum() / 120.0).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_osc_ema5_sma20_10d_slope_v086_signal(volume):
    s = _sma(volume, 20)
    return ((_ema(volume, 5) - s) / s.replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_osc_sma10_sma40_21d_slope_v087_signal(volume):
    b = _sma(volume, 40)
    return ((_sma(volume, 10) - b) / b.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_mfi_14d_5d_slope_v088_signal(close, volume):
    s = np.sign(close.diff(1))
    pos = (volume * (s > 0).astype(float)).rolling(14, min_periods=14).sum()
    neg = (volume * (s < 0).astype(float)).rolling(14, min_periods=14).sum()
    return (100.0 - 100.0 / (1.0 + pos / neg.replace(0.0, np.nan))).diff(5).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_rank_quartile_252d_63d_slope_v089_signal(volume):
    q25 = volume.rolling(252, min_periods=252).quantile(0.25)
    q50 = volume.rolling(252, min_periods=252).quantile(0.50)
    q75 = volume.rolling(252, min_periods=252).quantile(0.75)
    return ((volume > q25).astype(float) + (volume > q50).astype(float) + (volume > q75).astype(float)).where(~q25.isna()).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_med_ratio_15_90_21d_slope_v090_signal(volume):
    return np.log(volume.rolling(15, min_periods=15).median() / volume.rolling(90, min_periods=90).median().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_macd_signal_25_75_63d_slope_v091_signal(volume):
    m = _ema(volume, 25) - _ema(volume, 75)
    return ((m - m.ewm(span=35, adjust=False, min_periods=35).mean()) / _sma(volume, 252).replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_gini_60d_21d_slope_v092_signal(closeadj, volume):
    return (closeadj * volume).rolling(60, min_periods=60).apply(_gini, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_pctchg_std_60d_21d_slope_v093_signal(closeadj, volume):
    return (closeadj * volume).pct_change(1).rolling(60, min_periods=60).std().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_extreme_count_60d_21d_slope_v094_signal(closeadj, volume):
    dv = closeadj * volume; m = _sma(dv, 60)
    return (dv > 2.0 * m).astype(float).where(~m.isna()).rolling(60, min_periods=60).sum().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_reversion_score_30d_10d_slope_v095_signal(volume):
    s = np.sign(volume - _sma(volume, 10))
    return (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()).rolling(30, min_periods=30).sum().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dayssince_q75_cross_120d_63d_slope_v096_signal(volume):
    q = volume.rolling(120, min_periods=120).quantile(0.75)
    return (volume > q).astype(float).where(~q.isna()).rolling(120, min_periods=120).apply(_streak_last_true, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dayssince_dry_120d_21d_slope_v097_signal(volume):
    m = _sma(volume, 21)
    return (volume < 0.5 * m).astype(float).where(~m.isna()).rolling(120, min_periods=120).apply(_streak_last_true, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_med_ratio_5_50_10d_slope_v098_signal(volume):
    return np.log(volume.rolling(5, min_periods=5).median() / volume.rolling(50, min_periods=50).median().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_med_diff_q_20d_5d_slope_v099_signal(volume):
    med = volume.rolling(20, min_periods=20).median()
    q25 = volume.rolling(20, min_periods=20).quantile(0.25); q75 = volume.rolling(20, min_periods=20).quantile(0.75)
    return ((med - q25) / (q75 - q25).replace(0.0, np.nan)).diff(5).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_hf_lf_diff_21d_slope_v100_signal(volume):
    b = _sma(volume, 100)
    return ((_sma(volume, 3) - b) / b.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_uppertail_share_45d_10d_slope_v101_signal(volume):
    return volume.rolling(45, min_periods=45).apply(_us75, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_lowertail_share_45d_21d_slope_v102_signal(volume):
    return volume.rolling(45, min_periods=45).apply(_ls25, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_diff_skew_60d_63d_slope_v103_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).diff(1).rolling(60, min_periods=60).skew().diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_diff_kurt_90d_21d_slope_v104_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).diff(1).rolling(90, min_periods=90).kurt().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_corr_with_lag10_60d_21d_slope_v105_signal(volume):
    return volume.rolling(60, min_periods=60).corr(volume.shift(10)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_kl_halves_60d_63d_slope_v106_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(60, min_periods=60).apply(_kl_halves, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_near_unchanged_30d_10d_slope_v107_signal(volume):
    return (np.log(volume / volume.shift(1)).abs() < 0.05).astype(float).where(~volume.shift(1).isna()).rolling(30, min_periods=30).mean().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_expansion_5_to_30_10d_slope_v108_signal(volume):
    return (volume.rolling(5, min_periods=5).sum() / volume.shift(5).rolling(25, min_periods=25).sum().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_q_skew_60d_21d_slope_v109_signal(volume):
    q25 = volume.rolling(60, min_periods=60).quantile(0.25)
    q50 = volume.rolling(60, min_periods=60).quantile(0.50)
    q75 = volume.rolling(60, min_periods=60).quantile(0.75)
    return (((q75 - q50) - (q50 - q25)) / (q75 - q25).replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_signed_vol_zscore_30d_10d_slope_v110_signal(close, volume):
    sv = np.sign(close.diff(1)) * volume
    return ((sv - _sma(sv, 30)) / sv.rolling(30, min_periods=30).std().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_signed_vol_skew_60d_21d_slope_v111_signal(close, volume):
    return (np.sign(close.diff(1)) * volume).rolling(60, min_periods=60).skew().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_dd_dur_50d_21d_slope_v112_signal(volume):
    return volume.rolling(50, min_periods=50).apply(_ago_max, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_entropy_100d_63d_slope_v113_signal(volume):
    return volume.rolling(100, min_periods=100).apply(_ent10, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_compression_45d_21d_slope_v114_signal(volume):
    return (volume.rolling(45, min_periods=45).std() / volume.rolling(180, min_periods=180).std().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_spike_cluster_50d_10d_slope_v115_signal(volume):
    m = _sma(volume, 21)
    spike = (volume > 1.5 * m).astype(float).where(~m.isna())
    return ((spike > 0.5) & (spike.shift(1) < 0.5)).astype(float).where(~spike.isna() & ~spike.shift(1).isna()).rolling(50, min_periods=50).sum().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_halfreg_60d_21d_slope_v116_signal(volume):
    a = volume.rolling(30, min_periods=30).mean(); b = volume.shift(30).rolling(30, min_periods=30).mean()
    return ((a - b) / volume.rolling(60, min_periods=60).std().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_std_rank_120d_63d_slope_v117_signal(volume):
    return volume.rolling(20, min_periods=20).std().rolling(120, min_periods=120).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_jb_50d_10d_slope_v118_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    sk = lv.rolling(50, min_periods=50).skew(); ku = lv.rolling(50, min_periods=50).kurt()
    return (sk ** 2 + ku ** 2 / 4.0).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_roc_today_vs_25d_ago_10d_slope_v120_signal(volume):
    return np.log(volume / volume.shift(25)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_roc_today_vs_100d_ago_21d_slope_v121_signal(volume):
    return np.log(volume / volume.shift(100)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_pctchg_skew_60d_21d_slope_v122_signal(closeadj, volume):
    return (closeadj * volume).pct_change(1).rolling(60, min_periods=60).skew().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_dd_max_depth_60d_21d_slope_v123_signal(volume):
    dd = np.log(volume / volume.rolling(60, min_periods=60).max().replace(0.0, np.nan))
    return dd.rolling(60, min_periods=60).min().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logdv_skew_90d_63d_slope_v124_signal(closeadj, volume):
    return np.log((closeadj * volume).replace(0.0, np.nan)).rolling(90, min_periods=90).skew().diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_ema30_ema90_log_21d_slope_v125_signal(volume):
    return np.log(_ema(volume, 30) / _ema(volume, 90)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_com_50d_10d_slope_v126_signal(volume):
    return volume.rolling(50, min_periods=50).apply(_com, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_detrended_std_180d_63d_slope_v127_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(180, min_periods=180).apply(_detr_std, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_atr_like_30d_10d_slope_v128_signal(volume):
    return (_sma(volume.diff(1).abs(), 30) / _sma(volume, 30).replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_signed_streak_40d_21d_slope_v129_signal(volume):
    return np.sign(volume.diff(1)).rolling(40, min_periods=40).apply(_signed_streak, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_intensity_index_40d_10d_slope_v130_signal(volume):
    return (volume / volume.rolling(20, min_periods=20).median().replace(0.0, np.nan)).rolling(40, min_periods=40).mean().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_tail_asym_120d_21d_slope_v131_signal(volume):
    return volume.rolling(120, min_periods=120).apply(_ta10, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_signed_dv_flip_rate_60d_21d_slope_v132_signal(close, closeadj, volume):
    ssign = np.sign(np.sign(close.diff(1)) * closeadj * volume)
    return (ssign != ssign.shift(1)).astype(float).where(~ssign.isna() & ~ssign.shift(1).isna()).rolling(60, min_periods=60).mean().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_dft_short_long_60d_21d_slope_v133_signal(volume):
    return np.log(volume.replace(0.0, np.nan)).rolling(60, min_periods=60).apply(_dft_sl, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_theil_45d_10d_slope_v134_signal(volume):
    return volume.rolling(45, min_periods=45).apply(_theil, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_second_peak_60d_21d_slope_v135_signal(volume):
    return volume.rolling(60, min_periods=60).apply(_sp, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_change_sharpe_60d_63d_slope_v136_signal(volume):
    d = volume.diff(1)
    return (_sma(d, 60) / d.rolling(60, min_periods=60).std().replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_med_asym_80d_21d_slope_v137_signal(volume):
    med = volume.rolling(80, min_periods=80).median()
    over = (volume > med).astype(float).where(~med.isna()); under = (volume < med).astype(float).where(~med.isna())
    return ((over.rolling(80, min_periods=80).sum() - under.rolling(80, min_periods=80).sum()) / 80.0).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_persistence_40d_10d_slope_v138_signal(volume):
    d = volume - _sma(volume, 20)
    return (np.sign(d) == np.sign(d.shift(1))).astype(float).where(~d.isna() & ~d.shift(1).isna()).rolling(40, min_periods=40).mean().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_dv_max_gap_top10_252d_63d_slope_v139_signal(closeadj, volume):
    return (closeadj * volume).rolling(252, min_periods=252).apply(_gap_top10, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_winsor_diff_60d_21d_slope_v140_signal(volume):
    w = volume.rolling(60, min_periods=60).apply(_winsor_mean, raw=True)
    return np.log(w / _sma(volume, 60).replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_trimmed_diff_80d_63d_slope_v141_signal(volume):
    t = volume.rolling(80, min_periods=80).apply(_trimmed_mean, raw=True)
    return np.log(t / _sma(volume, 80).replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_lull_count_60d_21d_slope_v142_signal(volume):
    m = _sma(volume, 21)
    return ((volume > 0.5 * m) & (volume < 1.5 * m)).astype(float).where(~m.isna()).rolling(60, min_periods=60).sum().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_argmin_120d_63d_slope_v143_signal(volume):
    return volume.rolling(120, min_periods=120).apply(_ax_min, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_spike_intensity_45d_10d_slope_v144_signal(volume):
    m = _sma(volume, 21); rel = volume / m.replace(0.0, np.nan)
    return rel.where((rel > 2.0).astype(float).where(~m.isna()) > 0.5).rolling(45, min_periods=1).mean().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_max_1d_growth_40d_10d_slope_v145_signal(volume):
    return np.log(volume / volume.shift(1)).rolling(40, min_periods=40).max().diff(10).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_min_1d_growth_40d_21d_slope_v146_signal(volume):
    return np.log(volume / volume.shift(1)).rolling(40, min_periods=40).min().diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_dispersion_lag_60d_63d_slope_v147_signal(volume):
    return (volume.rolling(60, min_periods=60).std() / volume.shift(20).rolling(60, min_periods=60).std().replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_logvol_diff_signaling_70d_21d_slope_v148_signal(volume):
    d = np.log(volume.replace(0.0, np.nan)).diff(1)
    return (_sma(d, 70) / d.rolling(70, min_periods=70).std().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_mad_rank_120d_21d_slope_v149_signal(volume):
    return volume.rolling(30, min_periods=30).apply(_mad, raw=True).rolling(120, min_periods=120).rank(pct=True).diff(21).replace([np.inf, -np.inf], np.nan)

def f21rv_f21_raw_volume_metrics_vol_geom_arith_diff_60d_10d_slope_v150_signal(volume):
    return np.log(np.exp(np.log(volume.replace(0.0, np.nan)).rolling(60, min_periods=60).mean()) / _sma(volume, 60).replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)

f21_raw_volume_metrics_slope_001_150_REGISTRY = {
    "f21rv_f21_raw_volume_metrics_logvol_sma5_5d_slope_v001_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_sma5_5d_slope_v001_signal},
    "f21rv_f21_raw_volume_metrics_logvol_sma5_sma50_10d_slope_v002_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_sma5_sma50_10d_slope_v002_signal},
    "f21rv_f21_raw_volume_metrics_logvol_sma20_sma200_63d_slope_v003_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_sma20_sma200_63d_slope_v003_signal},
    "f21rv_f21_raw_volume_metrics_logvol_ema_diff_10_60_21d_slope_v004_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_ema_diff_10_60_21d_slope_v004_signal},
    "f21rv_f21_raw_volume_metrics_median_vol_ratio_20_120_21d_slope_v005_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_median_vol_ratio_20_120_21d_slope_v005_signal},
    "f21rv_f21_raw_volume_metrics_volz_21d_5d_slope_v006_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_volz_21d_5d_slope_v006_signal},
    "f21rv_f21_raw_volume_metrics_volrank_60d_10d_slope_v007_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_volrank_60d_10d_slope_v007_signal},
    "f21rv_f21_raw_volume_metrics_dv_signed_share_30d_10d_slope_v008_signal": {"inputs": ["close", "closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_signed_share_30d_10d_slope_v008_signal},
    "f21rv_f21_raw_volume_metrics_dv_termstruct_5_252_63d_slope_v009_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_termstruct_5_252_63d_slope_v009_signal},
    "f21rv_f21_raw_volume_metrics_dv_termstruct_20_120_21d_slope_v010_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_termstruct_20_120_21d_slope_v010_signal},
    "f21rv_f21_raw_volume_metrics_vol_skew_60d_21d_slope_v011_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_skew_60d_21d_slope_v011_signal},
    "f21rv_f21_raw_volume_metrics_vol_kurt_180d_63d_slope_v012_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_kurt_180d_63d_slope_v012_signal},
    "f21rv_f21_raw_volume_metrics_logvol_skew_120d_21d_slope_v013_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_skew_120d_21d_slope_v013_signal},
    "f21rv_f21_raw_volume_metrics_logvol_kurt_40d_10d_slope_v014_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_kurt_40d_10d_slope_v014_signal},
    "f21rv_f21_raw_volume_metrics_vol_mad_over_std_45d_21d_slope_v015_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_mad_over_std_45d_21d_slope_v015_signal},
    "f21rv_f21_raw_volume_metrics_vol_cv_60d_21d_slope_v016_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_cv_60d_21d_slope_v016_signal},
    "f21rv_f21_raw_volume_metrics_vol_gini_30d_10d_slope_v017_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_gini_30d_10d_slope_v017_signal},
    "f21rv_f21_raw_volume_metrics_vol_iqr_over_med_50d_21d_slope_v018_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_iqr_over_med_50d_21d_slope_v018_signal},
    "f21rv_f21_raw_volume_metrics_volpct_1d_5d_slope_v019_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_volpct_1d_5d_slope_v019_signal},
    "f21rv_f21_raw_volume_metrics_logvol_diff_1d_5d_slope_v020_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_diff_1d_5d_slope_v020_signal},
    "f21rv_f21_raw_volume_metrics_abs_logvol_diff_10d_5d_slope_v021_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_abs_logvol_diff_10d_5d_slope_v021_signal},
    "f21rv_f21_raw_volume_metrics_spike_bin_21d_10d_slope_v022_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_spike_bin_21d_10d_slope_v022_signal},
    "f21rv_f21_raw_volume_metrics_spike_count_60d_21d_slope_v023_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_spike_count_60d_21d_slope_v023_signal},
    "f21rv_f21_raw_volume_metrics_spike_mag_60d_63d_slope_v024_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_spike_mag_60d_63d_slope_v024_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_spike_80d_21d_slope_v025_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_spike_80d_21d_slope_v025_signal},
    "f21rv_f21_raw_volume_metrics_dry_bin_21d_10d_slope_v026_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dry_bin_21d_10d_slope_v026_signal},
    "f21rv_f21_raw_volume_metrics_dry_streak_60d_21d_slope_v027_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dry_streak_60d_21d_slope_v027_signal},
    "f21rv_f21_raw_volume_metrics_dry_count_120d_63d_slope_v028_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dry_count_120d_63d_slope_v028_signal},
    "f21rv_f21_raw_volume_metrics_logvol_std_30d_10d_slope_v029_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_std_30d_10d_slope_v029_signal},
    "f21rv_f21_raw_volume_metrics_vol_volofvol_60d_21d_slope_v030_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_volofvol_60d_21d_slope_v030_signal},
    "f21rv_f21_raw_volume_metrics_vol_range_over_mean_40d_10d_slope_v031_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_range_over_mean_40d_10d_slope_v031_signal},
    "f21rv_f21_raw_volume_metrics_vol_pctchg_std_45d_21d_slope_v032_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pctchg_std_45d_21d_slope_v032_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_lag1_45d_10d_slope_v033_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_lag1_45d_10d_slope_v033_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_lag5_80d_21d_slope_v034_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_lag5_80d_21d_slope_v034_signal},
    "f21rv_f21_raw_volume_metrics_logvol_acf_lag1_120d_63d_slope_v035_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_acf_lag1_120d_63d_slope_v035_signal},
    "f21rv_f21_raw_volume_metrics_vol_share_top5_30d_10d_slope_v036_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_share_top5_30d_10d_slope_v036_signal},
    "f21rv_f21_raw_volume_metrics_vol_cone_45d_21d_slope_v037_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_cone_45d_21d_slope_v037_signal},
    "f21rv_f21_raw_volume_metrics_vol_change_streak_40d_10d_slope_v038_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_change_streak_40d_10d_slope_v038_signal},
    "f21rv_f21_raw_volume_metrics_vol_meanrev_rate_50d_21d_slope_v039_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_meanrev_rate_50d_21d_slope_v039_signal},
    "f21rv_f21_raw_volume_metrics_vol_sharpe_45d_21d_slope_v040_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_sharpe_45d_21d_slope_v040_signal},
    "f21rv_f21_raw_volume_metrics_high_vol_top25_60d_21d_slope_v041_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_high_vol_top25_60d_21d_slope_v041_signal},
    "f21rv_f21_raw_volume_metrics_low_vol_bot25_60d_63d_slope_v042_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_low_vol_bot25_60d_63d_slope_v042_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_highvol_100d_21d_slope_v043_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_highvol_100d_21d_slope_v043_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_lowvol_100d_63d_slope_v044_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_lowvol_100d_63d_slope_v044_signal},
    "f21rv_f21_raw_volume_metrics_vol_stoch_30d_21d_slope_v045_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_stoch_30d_21d_slope_v045_signal},
    "f21rv_f21_raw_volume_metrics_signed_vol_norm_20d_5d_slope_v046_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_vol_norm_20d_5d_slope_v046_signal},
    "f21rv_f21_raw_volume_metrics_signed_vol_share_40d_10d_slope_v047_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_vol_share_40d_10d_slope_v047_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_sign_flips_50d_21d_slope_v048_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_sign_flips_50d_21d_slope_v048_signal},
    "f21rv_f21_raw_volume_metrics_vol_max_to_min_30d_10d_slope_v049_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_max_to_min_30d_10d_slope_v049_signal},
    "f21rv_f21_raw_volume_metrics_signed_logvol_diff_25d_21d_slope_v050_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_signed_logvol_diff_25d_21d_slope_v050_signal},
    "f21rv_f21_raw_volume_metrics_vol_streak_up_30d_10d_slope_v051_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_streak_up_30d_10d_slope_v051_signal},
    "f21rv_f21_raw_volume_metrics_vol_streak_down_30d_21d_slope_v052_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_streak_down_30d_21d_slope_v052_signal},
    "f21rv_f21_raw_volume_metrics_vol_entropy_30d_10d_slope_v053_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_entropy_30d_10d_slope_v053_signal},
    "f21rv_f21_raw_volume_metrics_vol_logslope_60d_21d_slope_v054_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_logslope_60d_21d_slope_v054_signal},
    "f21rv_f21_raw_volume_metrics_vol_logslope_r2_80d_63d_slope_v055_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_logslope_r2_80d_63d_slope_v055_signal},
    "f21rv_f21_raw_volume_metrics_vol_max_argmax_50d_10d_slope_v056_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_max_argmax_50d_10d_slope_v056_signal},
    "f21rv_f21_raw_volume_metrics_vol_min_argmin_50d_21d_slope_v057_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_min_argmin_50d_21d_slope_v057_signal},
    "f21rv_f21_raw_volume_metrics_vol_pct_up_days_120d_63d_slope_v058_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pct_up_days_120d_63d_slope_v058_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_change_lag1_60d_21d_slope_v059_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_change_lag1_60d_21d_slope_v059_signal},
    "f21rv_f21_raw_volume_metrics_vol_pctchg_skew_60d_63d_slope_v060_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pctchg_skew_60d_63d_slope_v060_signal},
    "f21rv_f21_raw_volume_metrics_dv_iqr_over_med_140d_21d_slope_v061_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_iqr_over_med_140d_21d_slope_v061_signal},
    "f21rv_f21_raw_volume_metrics_dv_cv_90d_21d_slope_v062_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_cv_90d_21d_slope_v062_signal},
    "f21rv_f21_raw_volume_metrics_dv_volofvol_80d_21d_slope_v063_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_volofvol_80d_21d_slope_v063_signal},
    "f21rv_f21_raw_volume_metrics_vol_pct_extreme_30d_10d_slope_v064_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pct_extreme_30d_10d_slope_v064_signal},
    "f21rv_f21_raw_volume_metrics_vol_dispnorm_70d_63d_slope_v065_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dispnorm_70d_63d_slope_v065_signal},
    "f21rv_f21_raw_volume_metrics_volume_zero_streak_50d_21d_slope_v066_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_volume_zero_streak_50d_21d_slope_v066_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_lag2_60d_21d_slope_v067_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_lag2_60d_21d_slope_v067_signal},
    "f21rv_f21_raw_volume_metrics_vol_logsharpe_120d_63d_slope_v068_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_logsharpe_120d_63d_slope_v068_signal},
    "f21rv_f21_raw_volume_metrics_vol_above_below_ratio_45d_10d_slope_v069_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_above_below_ratio_45d_10d_slope_v069_signal},
    "f21rv_f21_raw_volume_metrics_vol_pctchg_abs_45d_21d_slope_v070_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pctchg_abs_45d_21d_slope_v070_signal},
    "f21rv_f21_raw_volume_metrics_vol_streak_high_50d_10d_slope_v071_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_streak_high_50d_10d_slope_v071_signal},
    "f21rv_f21_raw_volume_metrics_dv_acf_lag1_70d_21d_slope_v072_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_acf_lag1_70d_21d_slope_v072_signal},
    "f21rv_f21_raw_volume_metrics_vol_zerocenter_norm_15d_10d_slope_v073_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_zerocenter_norm_15d_10d_slope_v073_signal},
    "f21rv_f21_raw_volume_metrics_vol_runs_test_60d_21d_slope_v074_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_runs_test_60d_21d_slope_v074_signal},
    "f21rv_f21_raw_volume_metrics_vol_extreme_tail_75d_63d_slope_v075_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_extreme_tail_75d_63d_slope_v075_signal},
    "f21rv_f21_raw_volume_metrics_vol_dd_from_max_60d_10d_slope_v076_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dd_from_max_60d_10d_slope_v076_signal},
    "f21rv_f21_raw_volume_metrics_vol_gain_from_min_60d_21d_slope_v077_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_gain_from_min_60d_21d_slope_v077_signal},
    "f21rv_f21_raw_volume_metrics_vol_dd_from_max_200d_63d_slope_v078_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dd_from_max_200d_63d_slope_v078_signal},
    "f21rv_f21_raw_volume_metrics_logvol_hurst_60d_21d_slope_v079_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_hurst_60d_21d_slope_v079_signal},
    "f21rv_f21_raw_volume_metrics_logvol_hurst_180d_63d_slope_v080_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_hurst_180d_63d_slope_v080_signal},
    "f21rv_f21_raw_volume_metrics_vol_fisher_50d_21d_slope_v081_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_fisher_50d_21d_slope_v081_signal},
    "f21rv_f21_raw_volume_metrics_vol_pctB_30d_10d_slope_v082_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pctB_30d_10d_slope_v082_signal},
    "f21rv_f21_raw_volume_metrics_vol_bandwidth_90d_63d_slope_v083_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_bandwidth_90d_63d_slope_v083_signal},
    "f21rv_f21_raw_volume_metrics_vol_streak_above_med_120d_21d_slope_v084_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_streak_above_med_120d_21d_slope_v084_signal},
    "f21rv_f21_raw_volume_metrics_vol_peak_count_120d_63d_slope_v085_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_peak_count_120d_63d_slope_v085_signal},
    "f21rv_f21_raw_volume_metrics_vol_osc_ema5_sma20_10d_slope_v086_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_osc_ema5_sma20_10d_slope_v086_signal},
    "f21rv_f21_raw_volume_metrics_vol_osc_sma10_sma40_21d_slope_v087_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_osc_sma10_sma40_21d_slope_v087_signal},
    "f21rv_f21_raw_volume_metrics_vol_mfi_14d_5d_slope_v088_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_vol_mfi_14d_5d_slope_v088_signal},
    "f21rv_f21_raw_volume_metrics_vol_rank_quartile_252d_63d_slope_v089_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_rank_quartile_252d_63d_slope_v089_signal},
    "f21rv_f21_raw_volume_metrics_vol_med_ratio_15_90_21d_slope_v090_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_med_ratio_15_90_21d_slope_v090_signal},
    "f21rv_f21_raw_volume_metrics_vol_macd_signal_25_75_63d_slope_v091_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_macd_signal_25_75_63d_slope_v091_signal},
    "f21rv_f21_raw_volume_metrics_dv_gini_60d_21d_slope_v092_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_gini_60d_21d_slope_v092_signal},
    "f21rv_f21_raw_volume_metrics_dv_pctchg_std_60d_21d_slope_v093_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_pctchg_std_60d_21d_slope_v093_signal},
    "f21rv_f21_raw_volume_metrics_dv_extreme_count_60d_21d_slope_v094_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_extreme_count_60d_21d_slope_v094_signal},
    "f21rv_f21_raw_volume_metrics_vol_reversion_score_30d_10d_slope_v095_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_reversion_score_30d_10d_slope_v095_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_q75_cross_120d_63d_slope_v096_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_q75_cross_120d_63d_slope_v096_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_dry_120d_21d_slope_v097_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_dry_120d_21d_slope_v097_signal},
    "f21rv_f21_raw_volume_metrics_vol_med_ratio_5_50_10d_slope_v098_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_med_ratio_5_50_10d_slope_v098_signal},
    "f21rv_f21_raw_volume_metrics_vol_med_diff_q_20d_5d_slope_v099_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_med_diff_q_20d_5d_slope_v099_signal},
    "f21rv_f21_raw_volume_metrics_vol_hf_lf_diff_21d_slope_v100_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_hf_lf_diff_21d_slope_v100_signal},
    "f21rv_f21_raw_volume_metrics_vol_uppertail_share_45d_10d_slope_v101_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_uppertail_share_45d_10d_slope_v101_signal},
    "f21rv_f21_raw_volume_metrics_vol_lowertail_share_45d_21d_slope_v102_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_lowertail_share_45d_21d_slope_v102_signal},
    "f21rv_f21_raw_volume_metrics_logvol_diff_skew_60d_63d_slope_v103_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_diff_skew_60d_63d_slope_v103_signal},
    "f21rv_f21_raw_volume_metrics_logvol_diff_kurt_90d_21d_slope_v104_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_diff_kurt_90d_21d_slope_v104_signal},
    "f21rv_f21_raw_volume_metrics_vol_corr_with_lag10_60d_21d_slope_v105_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_corr_with_lag10_60d_21d_slope_v105_signal},
    "f21rv_f21_raw_volume_metrics_vol_kl_halves_60d_63d_slope_v106_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_kl_halves_60d_63d_slope_v106_signal},
    "f21rv_f21_raw_volume_metrics_vol_near_unchanged_30d_10d_slope_v107_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_near_unchanged_30d_10d_slope_v107_signal},
    "f21rv_f21_raw_volume_metrics_vol_expansion_5_to_30_10d_slope_v108_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_expansion_5_to_30_10d_slope_v108_signal},
    "f21rv_f21_raw_volume_metrics_vol_q_skew_60d_21d_slope_v109_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_q_skew_60d_21d_slope_v109_signal},
    "f21rv_f21_raw_volume_metrics_signed_vol_zscore_30d_10d_slope_v110_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_vol_zscore_30d_10d_slope_v110_signal},
    "f21rv_f21_raw_volume_metrics_signed_vol_skew_60d_21d_slope_v111_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_vol_skew_60d_21d_slope_v111_signal},
    "f21rv_f21_raw_volume_metrics_vol_dd_dur_50d_21d_slope_v112_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dd_dur_50d_21d_slope_v112_signal},
    "f21rv_f21_raw_volume_metrics_vol_entropy_100d_63d_slope_v113_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_entropy_100d_63d_slope_v113_signal},
    "f21rv_f21_raw_volume_metrics_vol_compression_45d_21d_slope_v114_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_compression_45d_21d_slope_v114_signal},
    "f21rv_f21_raw_volume_metrics_vol_spike_cluster_50d_10d_slope_v115_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_spike_cluster_50d_10d_slope_v115_signal},
    "f21rv_f21_raw_volume_metrics_vol_halfreg_60d_21d_slope_v116_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_halfreg_60d_21d_slope_v116_signal},
    "f21rv_f21_raw_volume_metrics_vol_std_rank_120d_63d_slope_v117_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_std_rank_120d_63d_slope_v117_signal},
    "f21rv_f21_raw_volume_metrics_vol_jb_50d_10d_slope_v118_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_jb_50d_10d_slope_v118_signal},
    "f21rv_f21_raw_volume_metrics_vol_roc_today_vs_25d_ago_10d_slope_v120_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_roc_today_vs_25d_ago_10d_slope_v120_signal},
    "f21rv_f21_raw_volume_metrics_vol_roc_today_vs_100d_ago_21d_slope_v121_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_roc_today_vs_100d_ago_21d_slope_v121_signal},
    "f21rv_f21_raw_volume_metrics_dv_pctchg_skew_60d_21d_slope_v122_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_pctchg_skew_60d_21d_slope_v122_signal},
    "f21rv_f21_raw_volume_metrics_vol_dd_max_depth_60d_21d_slope_v123_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dd_max_depth_60d_21d_slope_v123_signal},
    "f21rv_f21_raw_volume_metrics_logdv_skew_90d_63d_slope_v124_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_logdv_skew_90d_63d_slope_v124_signal},
    "f21rv_f21_raw_volume_metrics_vol_ema30_ema90_log_21d_slope_v125_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_ema30_ema90_log_21d_slope_v125_signal},
    "f21rv_f21_raw_volume_metrics_vol_com_50d_10d_slope_v126_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_com_50d_10d_slope_v126_signal},
    "f21rv_f21_raw_volume_metrics_logvol_detrended_std_180d_63d_slope_v127_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_detrended_std_180d_63d_slope_v127_signal},
    "f21rv_f21_raw_volume_metrics_vol_atr_like_30d_10d_slope_v128_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_atr_like_30d_10d_slope_v128_signal},
    "f21rv_f21_raw_volume_metrics_vol_signed_streak_40d_21d_slope_v129_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_signed_streak_40d_21d_slope_v129_signal},
    "f21rv_f21_raw_volume_metrics_vol_intensity_index_40d_10d_slope_v130_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_intensity_index_40d_10d_slope_v130_signal},
    "f21rv_f21_raw_volume_metrics_vol_tail_asym_120d_21d_slope_v131_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_tail_asym_120d_21d_slope_v131_signal},
    "f21rv_f21_raw_volume_metrics_signed_dv_flip_rate_60d_21d_slope_v132_signal": {"inputs": ["close", "closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_dv_flip_rate_60d_21d_slope_v132_signal},
    "f21rv_f21_raw_volume_metrics_vol_dft_short_long_60d_21d_slope_v133_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dft_short_long_60d_21d_slope_v133_signal},
    "f21rv_f21_raw_volume_metrics_vol_theil_45d_10d_slope_v134_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_theil_45d_10d_slope_v134_signal},
    "f21rv_f21_raw_volume_metrics_vol_second_peak_60d_21d_slope_v135_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_second_peak_60d_21d_slope_v135_signal},
    "f21rv_f21_raw_volume_metrics_vol_change_sharpe_60d_63d_slope_v136_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_change_sharpe_60d_63d_slope_v136_signal},
    "f21rv_f21_raw_volume_metrics_vol_med_asym_80d_21d_slope_v137_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_med_asym_80d_21d_slope_v137_signal},
    "f21rv_f21_raw_volume_metrics_vol_persistence_40d_10d_slope_v138_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_persistence_40d_10d_slope_v138_signal},
    "f21rv_f21_raw_volume_metrics_dv_max_gap_top10_252d_63d_slope_v139_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_max_gap_top10_252d_63d_slope_v139_signal},
    "f21rv_f21_raw_volume_metrics_vol_winsor_diff_60d_21d_slope_v140_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_winsor_diff_60d_21d_slope_v140_signal},
    "f21rv_f21_raw_volume_metrics_vol_trimmed_diff_80d_63d_slope_v141_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_trimmed_diff_80d_63d_slope_v141_signal},
    "f21rv_f21_raw_volume_metrics_vol_lull_count_60d_21d_slope_v142_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_lull_count_60d_21d_slope_v142_signal},
    "f21rv_f21_raw_volume_metrics_vol_argmin_120d_63d_slope_v143_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_argmin_120d_63d_slope_v143_signal},
    "f21rv_f21_raw_volume_metrics_vol_spike_intensity_45d_10d_slope_v144_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_spike_intensity_45d_10d_slope_v144_signal},
    "f21rv_f21_raw_volume_metrics_vol_max_1d_growth_40d_10d_slope_v145_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_max_1d_growth_40d_10d_slope_v145_signal},
    "f21rv_f21_raw_volume_metrics_vol_min_1d_growth_40d_21d_slope_v146_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_min_1d_growth_40d_21d_slope_v146_signal},
    "f21rv_f21_raw_volume_metrics_vol_dispersion_lag_60d_63d_slope_v147_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dispersion_lag_60d_63d_slope_v147_signal},
    "f21rv_f21_raw_volume_metrics_logvol_diff_signaling_70d_21d_slope_v148_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_diff_signaling_70d_21d_slope_v148_signal},
    "f21rv_f21_raw_volume_metrics_vol_mad_rank_120d_21d_slope_v149_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_mad_rank_120d_21d_slope_v149_signal},
    "f21rv_f21_raw_volume_metrics_vol_geom_arith_diff_60d_10d_slope_v150_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_geom_arith_diff_60d_10d_slope_v150_signal},
}

def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed); seg = n // 4; rest = n - 3 * seg
    ret = np.concatenate([rng.normal(0.0012, 0.011, seg), rng.normal(-0.0005, 0.018, seg), rng.normal(-0.0010, 0.014, seg), rng.normal(0.0008, 0.012, rest)])
    close = 50.0 * np.exp(np.cumsum(ret))
    closeadj = close * np.exp(rng.normal(0.0, 0.0003, size=n).cumsum())
    intraday = rng.normal(0.0, 0.008, size=n); open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({"open": pd.Series(open_, index=idx, dtype=float), "high": pd.Series(high, index=idx, dtype=float), "low": pd.Series(low, index=idx, dtype=float), "close": pd.Series(close, index=idx, dtype=float), "closeadj": pd.Series(closeadj, index=idx, dtype=float), "volume": pd.Series(volume, index=idx, dtype=float)})

def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f21_raw_volume_metrics_slope_001_150_REGISTRY.items():
        out = entry["func"](*[df[c] for c in entry["inputs"]])
        assert isinstance(out, pd.Series) and len(out) == len(df), f"{name}: bad shape"
        clean = out.dropna()
        assert len(clean) > 0 and (float(clean.std()) > 0.0 or clean.nunique() > 1), f"{name}: constant"
        results[name] = out
    warm = 252
    frac = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5) / len(results)
    assert frac >= 0.80, f"coverage too low: {frac:.2%}"
    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:].replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs(); np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
    _self_test()
