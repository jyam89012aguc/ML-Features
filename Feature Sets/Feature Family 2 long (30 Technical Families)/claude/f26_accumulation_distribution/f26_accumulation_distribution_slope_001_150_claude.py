"""f26 A/D slope 001-150 (1st derivative)."""
from __future__ import annotations
import numpy as np
import pandas as pd

def _clv(h, l, c): rng = (h - l).replace(0.0, np.nan); return ((c - l) - (h - c)) / rng
def _r(x): return x.replace([np.inf, -np.inf], np.nan)
def _vs(v, n): return v.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
def _ad(h, l, c, v): return (_clv(h, l, c) * v).cumsum()
def _cmf(h, l, c, v, n): return (_clv(h, l, c) * v).rolling(n, min_periods=n).sum() / _vs(v, n)
def _ru(x, n): return x.rolling(n, min_periods=n)
def _ema(x, n): return x.ewm(span=n, adjust=False, min_periods=n).mean()
def _sd(x, n): return x.rolling(n, min_periods=n).std(ddof=0).replace(0.0, np.nan)
def _mn(x, n): return x.rolling(n, min_periods=n).mean()
def _su(x, n): return x.rolling(n, min_periods=n).sum()
def _ac1(x):
    if len(x) < 3: return np.nan
    sx = pd.Series(x); return float(sx.autocorr(lag=1)) if sx.std(ddof=0) > 0 else np.nan
def _ac5(x):
    if len(x) < 10: return np.nan
    sx = pd.Series(x); return float(sx.autocorr(lag=5)) if sx.std(ddof=0) > 0 else np.nan
def _days_since(x):
    return float(len(x) - 1 - np.where(x > 0.5)[0][-1]) if (x > 0.5).any() else float(len(x))
def _q75(x):
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)) or len(x) < 5: return np.nan
    t = np.quantile(x, 0.75); sel = x[x >= t]
    return float(np.mean(sel)) if len(sel) else np.nan
def _q25(x):
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)) or len(x) < 5: return np.nan
    t = np.quantile(x, 0.25); sel = x[x <= t]
    return float(np.mean(sel)) if len(sel) else np.nan
def _olsslope(x):
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx)); vr = np.sum((t - mt) ** 2)
    if vr == 0.0 or not np.isfinite(mx) or mx == 0.0: return np.nan
    return float((cov / vr) / abs(mx))
def _olsrsq(x):
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx))
    vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
    if vt == 0.0 or vx == 0.0: return np.nan
    r = cov / np.sqrt(vt * vx); return float(r * r)
def _olsresid(x):
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx)); vt = np.sum((t - mt) ** 2)
    if vt == 0.0 or not np.isfinite(mx) or mx == 0.0: return np.nan
    bb = cov / vt; a = mx - bb * mt
    return float(np.std(x - (a + bb * t)) / abs(mx))
def _ent3(x):
    x = x[np.isfinite(x)]
    if len(x) == 0: return np.nan
    pp = float((x > 0.5).sum()) / len(x); pn = float((x < -0.5).sum()) / len(x); pz = max(0.0, 1.0 - pp - pn)
    e = 0.0
    for p in (pp, pn, pz):
        if p > 0.0: e -= p * np.log(p)
    return float(e)
def _mad(x): m = np.mean(x); return float(np.mean(np.abs(x - m)))
def _runs(x):
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)): return np.nan
    cnt = 0; prev = 0.0
    for v in x:
        if v > 0.5 and prev <= 0.5: cnt += 1
        prev = v
    return float(cnt)
def _mfi(h, l, c, v, n):
    tp = (h + l + c) / 3.0; rmf = tp * v; d = np.sign(tp.diff(1))
    pf = _su(rmf.where(d > 0.0, 0.0), n); nf = _su(rmf.where(d < 0.0, 0.0), n).replace(0.0, np.nan)
    return 100.0 - 100.0 / (1.0 + pf / nf)
def _chk(h, l, c, v): ad = _ad(h, l, c, v); return _ema(ad, 3) - _ema(ad, 10)
def _kvf(h, l, c, v): hlc = (h + l + c) / 3.0; return v * np.sign(hlc.diff(1))
def _streak_run(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5:
            c += 1
        else:
            break
    return float(c)
def _max_run(x):
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)):
        return np.nan
    best = 0; cur = 0
    for v in x:
        if v > 0.5:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return float(best)
def _rank_last(x):
    last = x[-1]
    if not np.isfinite(last):
        return np.nan
    return float((x < last).sum()) / float(len(x))
# Slope 001-075
def f26ad_f26_accumulation_distribution_raw_clv_1d_slope_v001_signal(high, low, close):
    b = _clv(high, low, close); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_clv_sign_1d_slope_v002_signal(high, low, close):
    b = np.sign(_clv(high, low, close)); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_clv_mean_5d_slope_v003_signal(high, low, close):
    clv = _clv(high, low, close); b = _mn(clv, 5); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_clv_mean_21d_slope_v004_signal(high, low, close):
    clv = _clv(high, low, close); b = _mn(clv, 21); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_clv_mean_63d_slope_v005_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); b = _mn(clv, 63); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_volratio_5d_slope_v006_signal(high, low, close, volume):
    b = _cmf(high, low, close, volume, 5); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_cmf_50d_slope_v008_signal(high, low, closeadj, volume):
    b = _cmf(high, low, closeadj, volume, 50); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_cmf_100d_slope_v009_signal(high, low, closeadj, volume):
    b = _cmf(high, low, closeadj, volume, 100); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_cmf_sign_21d_slope_v010_signal(high, low, close, volume):
    clv = _clv(high, low, close); num = _su((clv * volume), 21); den = _vs(volume, 21); b = np.sign(num / den); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_cmf50_minus_cmf21_sign_slope_v011_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; n1 = _su(cv, 21); d1 = _vs(volume, 21); n2 = _su(cv, 50); d2 = _vs(volume, 50); b = np.sign((n2 / d2) - (n1 / d1)); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_minus_sma_30d_slope_v012_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); sma = _mn(ad, 30); b = (ad - sma) / sma.abs().replace(0.0, np.nan); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_minus_sma_120d_slope_v013_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); sma = _mn(ad, 120); b = (ad - sma) / sma.abs().replace(0.0, np.nan); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_ad_slope_norm_30d_slope_v014_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); b = (ad - ad.shift(30)) / _vs(volume, 30); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_path_curvature_120d_slope_v015_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; ad = cv.cumsum(); net = (ad - ad.shift(120)).abs(); path = cv.abs().rolling(120, min_periods=120).sum().replace(0.0, np.nan); b = np.log(net.replace(0.0, np.nan)) - np.log(path); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_ad_curv_50d_slope_v016_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); den = _vs(volume, 50); b = (ad - 2.0 * ad.shift(25) + ad.shift(50)) / den; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_chaikin_pct_change_10d_slope_v018_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); prev = co.shift(10); b = np.sign(co - prev) * np.log1p((co - prev).abs() / (prev.abs() + 1.0)); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_chaikin_osc_sign_3_10_slope_v019_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); e3 = _ema(ad, 3); e10 = _ema(ad, 10); b = np.sign(e3 - e10); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_chaikin_zero_streak_60d_slope_v020_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); e3 = _ema(ad, 3); e10 = _ema(ad, 10); s = np.sign(e3 - e10); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()); b = _ru(flip, 60).apply(_streak_run, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_klinger_osc_34_55_slope_v021_signal(high, low, closeadj, volume):
    hlc = high + low + closeadj; trend = np.sign(hlc - hlc.shift(1)); kvf = volume * trend; e34 = _ema(kvf, 34); e55 = _ema(kvf, 55); den = _mn(volume, 55).replace(0.0, np.nan); b = (e34 - e55) / den; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_klinger_sign_34_55_slope_v022_signal(high, low, closeadj, volume):
    hlc = high + low + closeadj; trend = np.sign(hlc - hlc.shift(1)); kvf = volume * trend; e34 = _ema(kvf, 34); e55 = _ema(kvf, 55); b = np.sign(e34 - e55); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_upclv_volsum_21d_slope_v023_signal(high, low, close, volume):
    clv = _clv(high, low, close); pos = (clv * volume).where(clv > 0.0, 0.0); den = _vs(volume, 21); b = _su(pos, 21) / den; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_downclv_volshare_50d_slope_v024_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); neg_vol = volume.where(clv < 0.0, 0.0); den = _vs(volume, 50); b = _su(neg_vol, 50) / den; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_upclv_downclv_ratio_30d_slope_v025_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; pos = _ru(cv.where(cv > 0.0, 0.0), 30).sum(); neg = _ru(-cv.where(cv < 0.0, 0.0), 30).sum().replace(0.0, np.nan); b = np.log(pos.replace(0.0, np.nan) / neg); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_count_clvpos_30d_slope_v026_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); pos = (clv > 0.0).astype(float).where(~clv.isna()); b = _su(pos, 30); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_count_clvneg_75d_slope_v027_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); neg = (clv < 0.0).astype(float).where(~clv.isna()); b = _su(neg, 75); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clvneg_streak_40d_slope_v028_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); neg = (clv < 0.0).astype(float).where(~clv.isna()); b = _ru(neg, 40).apply(_streak_run, raw=True); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_clvpos_streak_40d_slope_v029_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); pos = (clv > 0.0).astype(float).where(~clv.isna()); b = _ru(pos, 40).apply(_streak_run, raw=True); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_high_dist_days_50d_slope_v030_signal(high, low, closeadj, volume):
    cmf = _cmf(high, low, closeadj, volume, 21); flag = (cmf < -0.05).astype(float).where(~cmf.isna()); b = _mn(flag, 50); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_high_acc_days_50d_slope_v031_signal(high, low, closeadj, volume):
    cmf = _cmf(high, low, closeadj, volume, 21); flag = (cmf > 0.05).astype(float).where(~cmf.isna()); b = _mn(flag, 50); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_cmf21_zscore_120d_slope_v032_signal(high, low, closeadj, volume):
    cmf = _cmf(high, low, closeadj, volume, 21); mu = _mn(cmf, 120); sd = _ru(cmf, 120).std(ddof=0).replace(0.0, np.nan); b = (cmf - mu) / sd; return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_cmf50_rank_180d_slope_v033_signal(high, low, closeadj, volume):
    cmf = _cmf(high, low, closeadj, volume, 50); b = _ru(cmf, 180).apply(_rank_last, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_cmf21_slope_10d_slope_v034_signal(high, low, close, volume):
    cmf = _cmf(high, low, close, volume, 21); b = cmf - cmf.shift(10); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_arctan_cmf21_slope_v035_signal(high, low, closeadj, volume):
    cmf = _cmf(high, low, closeadj, volume, 21); b = np.arctan(3.0 * cmf); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_tanh_ad_zscore_60d_slope_v036_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); dev = ad - _mn(ad, 60); sd = _ru(dev, 60).std(ddof=0).replace(0.0, np.nan); b = np.tanh(dev / sd); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_sigmoid_chaikin_3_10_slope_v037_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sd = _ru(co, 60).std(ddof=0).replace(0.0, np.nan); z = co / sd; b = 1.0 / (1.0 + np.exp(-z)); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_ad_obv_corr_60d_slope_v038_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); obv = (np.sign(closeadj.diff(1)) * volume).cumsum(); b = _ru(ad, 60).corr(obv); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_obv_diff_norm_30d_slope_v039_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); obv = (np.sign(closeadj.diff(1)) * volume).cumsum(); den = _vs(volume, 30); b = (ad - obv) / den; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_zscore_60d_slope_v040_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); mu = _mn(ad, 60); sd = _ru(ad, 60).std(ddof=0).replace(0.0, np.nan); b = (ad - mu) / sd; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_rank_200d_slope_v041_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); b = _ru(ad, 200).apply(_rank_last, raw=True); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_mfi_14d_slope_v042_signal(high, low, close, volume):
    mfi = _mfi(high, low, close, volume, 14); b = 2.0 * mfi / 100.0 - 1.0; return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_mfi_28d_slope_v043_signal(high, low, closeadj, volume):
    mfi = _mfi(high, low, closeadj, volume, 28); b = 2.0 * mfi / 100.0 - 1.0; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_mfi14_slope_10d_slope_v044_signal(high, low, closeadj, volume):
    mfi = _mfi(high, low, closeadj, volume, 14); b = mfi - mfi.shift(10); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_pos_mf_ratio_21d_slope_v045_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0; rmf = tp * volume; direction = np.sign(tp.diff(1)); pos = rmf.where(direction > 0.0, 0.0); neg = rmf.where(direction < 0.0, 0.0); psum = _su(pos, 21); nsum = _su((-neg), 21); tot = (psum + nsum).replace(0.0, np.nan); b = psum / tot; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_pos_mf_ratio_100d_slope_v046_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0; rmf = tp * volume; direction = np.sign(tp.diff(1)); pos = rmf.where(direction > 0.0, 0.0); neg = rmf.where(direction < 0.0, 0.0); psum = _su(pos, 100); nsum = _su((-neg), 100); tot = (psum + nsum).replace(0.0, np.nan); b = psum / tot; return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_ad_price_divergence_30d_slope_v047_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); b = np.sign(ad.diff(30)) - np.sign(closeadj.diff(30)); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_price_divergence_100d_slope_v048_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); b = np.sign(ad.diff(100)) - np.sign(closeadj.diff(100)); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clvvol_per_bar_mean_10d_slope_v049_signal(high, low, close, volume):
    clv = _clv(high, low, close); cv = clv * volume; b = _mn(cv, 10) / _mn(volume, 10).replace(0.0, np.nan); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_clvvol_per_bar_z_30d_slope_v050_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; norm = cv / volume.replace(0.0, np.nan); mu = _mn(norm, 30); sd = _ru(norm, 30).std(ddof=0).replace(0.0, np.nan); b = (norm - mu) / sd; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_time_corr_60d_slope_v051_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); t = pd.Series(np.arange(len(ad), dtype=float), index=ad.index); b = _ru(ad, 60).corr(t); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_time_corr_150d_slope_v052_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); t = pd.Series(np.arange(len(ad), dtype=float), index=ad.index); b = _ru(ad, 150).corr(t); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clv_entropy_30d_slope_v053_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj)
    sgn = np.sign(clv)
    return _r(_ru(sgn, 30).apply(_ent3, raw=True).diff(10))
def f26ad_f26_accumulation_distribution_cmf_multiwin_signagree_slope_v054_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj)
    cv = clv * volume
    out = pd.Series(0.0, index=closeadj.index)
    mask = pd.Series(True, index=closeadj.index)
    for n in (21, 50, 100):
        num = cv.rolling(n, min_periods=n).sum()
        den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        cmf = num / den
        out = out + np.sign(cmf)
        mask = mask & ~cmf.isna()
    return _r((out / 3.0).where(mask).diff(21))
def f26ad_f26_accumulation_distribution_chaikin_signal_xover_streak_50d_slope_v055_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sig9 = _ema(co, 9); above = (co > sig9).astype(float).where(~co.isna() & ~sig9.isna()); b = _ru(above, 50).apply(_streak_run, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_chaikin_kurt_120d_slope_v056_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); e3 = _ema(ad, 3); e10 = _ema(ad, 10); den = _vs(volume, 10); co = (e3 - e10) / den; b = _ru(co, 120).kurt(); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_days_since_clv_pos_slope_v057_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj)
    flag = (clv > 0.5).astype(float).where(~clv.isna())
    return _r(_ru(flag, 60).apply(_days_since, raw=True).diff(21))
def f26ad_f26_accumulation_distribution_days_since_clv_neg_slope_v058_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj)
    flag = (clv < -0.5).astype(float).where(~clv.isna())
    return _r(_ru(flag, 60).apply(_days_since, raw=True).diff(21))
def f26ad_f26_accumulation_distribution_cmf21_std_60d_slope_v059_signal(high, low, closeadj, volume):
    cmf = _cmf(high, low, closeadj, volume, 21); b = _ru(cmf, 60).std(ddof=0); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_volwtd_skew_50d_slope_v060_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; den = _vs(volume, 50); mu = _su(cv, 50) / den; dev = clv - mu; m3 = _su((dev ** 3 * volume), 50) / den; m2 = _su((dev ** 2 * volume), 50) / den; sd3 = m2 ** 1.5; b = m3 / sd3.replace(0.0, np.nan); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_ac1_30d_slope_v061_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj)
    return _r(_ru(clv, 30).apply(_ac1, raw=True).diff(10))
def f26ad_f26_accumulation_distribution_clv_ac5_75d_slope_v062_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj)
    return _r(_ru(clv, 75).apply(_ac5, raw=True).diff(21))
def f26ad_f26_accumulation_distribution_clv_high_extreme_frac_45d_slope_v063_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); flag = (clv.abs() > 0.8).astype(float).where(~clv.isna()); b = _mn(flag, 45); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clvvol_volzscore_corr_60d_slope_v064_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); vmu = _mn(volume, 60); vsd = _ru(volume, 60).std(ddof=0).replace(0.0, np.nan); vz = (volume - vmu) / vsd; b = _ru(clv, 60).corr(vz); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_klinger_sign_streak_45d_slope_v065_signal(high, low, closeadj, volume):
    kvf = _kvf(high, low, closeadj, volume); e34 = _ema(kvf, 34); e55 = _ema(kvf, 55); above = (e34 > e55).astype(float).where(~e34.isna() & ~e55.isna()); b = _ru(above, 45).apply(_streak_run, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_klinger_vf_norm_100d_slope_v066_signal(high, low, closeadj, volume):
    kvf = _kvf(high, low, closeadj, volume); den = _vs(volume, 100); b = _su(kvf, 100) / den; return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_mfi14_sign_slope_v067_signal(high, low, close, volume):
    mfi = _mfi(high, low, close, volume, 14); b = np.sign(mfi - 50.0); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_cmf21_minus_cmf100_slope_v068_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; n1 = _su(cv, 21); d1 = _vs(volume, 21); n2 = _su(cv, 100); d2 = _vs(volume, 100); b = (n1 / d1) - (n2 / d2); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_chaikin_3_10_slope_5d_slope_v069_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); e3 = _ema(ad, 3); e10 = _ema(ad, 10); den = _vs(volume, 10); co = (e3 - e10) / den; b = co - co.shift(5); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_williams_ad_slope_30d_slope_v070_signal(high, low, closeadj, volume):
    pc = closeadj.shift(1); up_part = closeadj - low.combine(pc, np.minimum); dn_part = closeadj - high.combine(pc, np.maximum); sgn = np.sign(closeadj - pc); wad_bar = np.where(sgn > 0.0, up_part, np.where(sgn < 0.0, dn_part, 0.0)); wad_bar = pd.Series(wad_bar, index=closeadj.index); wad_vol = wad_bar * volume; den = _vs(volume, 30); b = _su(wad_vol, 30) / den; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_cmf21_kurt_120d_slope_v071_signal(high, low, closeadj, volume):
    cmf = _cmf(high, low, closeadj, volume, 21); b = _ru(cmf, 120).kurt(); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_mfi_overbought_frac_60d_slope_v072_signal(high, low, closeadj, volume):
    mfi = _mfi(high, low, closeadj, volume, 14); flag = (mfi > 70.0).astype(float).where(~mfi.isna()); b = _mn(flag, 60); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_chaikin_zero_xover_count_120d_slope_v073_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); e3 = _ema(ad, 3); e10 = _ema(ad, 10); s = np.sign(e3 - e10); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()); b = _su(flip, 120); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_simple_30d_slope_v074_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); den = _vs(volume, 30); vw = _su((clv * volume), 30) / den; sw = _mn(clv, 30); b = vw - sw; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_cmf21_rank_minus_cmf50_rank_180d_slope_v075_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; n1 = _su(cv, 21); d1 = _vs(volume, 21); cmf1 = n1 / d1; n2 = _su(cv, 50); d2 = _vs(volume, 50); cmf2 = n2 / d2; r1 = _ru(cmf1, 180).apply(_rank_last, raw=True); r2 = _ru(cmf2, 180).apply(_rank_last, raw=True); b = r1 - r2; return _r(b.diff(21))
# Slope 076-150
def f26ad_f26_accumulation_distribution_clv_median_15d_slope_v076_signal(high, low, close):
    clv = _clv(high, low, close); b = _ru(clv, 15).median(); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_clv_iqr_45d_slope_v077_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); q75 = _ru(clv, 45).quantile(0.75); q25 = _ru(clv, 45).quantile(0.25); b = q75 - q25; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_mad_30d_slope_v078_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj)
    return _r(_ru(clv, 30).apply(_mad, raw=True).diff(10))
def f26ad_f26_accumulation_distribution_clv_skew_60d_slope_v079_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); b = _ru(clv, 60).skew(); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_kurt_120d_slope_v080_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); b = _ru(clv, 120).kurt(); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clv_q90_50d_slope_v081_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); b = _ru(clv, 50).quantile(0.90); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_q10_50d_slope_v082_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); b = _ru(clv, 50).quantile(0.10); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_chaikin_hist_3_10_minus_signal_slope_v083_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sig9 = _ema(co, 9); den = _vs(volume, 10); b = (co - sig9) / den; return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_chaikin_signal_distance_60d_slope_v084_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sig9 = _ema(co, 9); b = np.sign(co - sig9); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_pos_minus_neg_count_90d_slope_v085_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); pos = (clv > 0.0).astype(float).where(~clv.isna()); neg = (clv < 0.0).astype(float).where(~clv.isna()); b = _su(pos, 90) - _su(neg, 90); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clv_count_strong_pos_60d_slope_v086_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); flag = (clv > 0.5).astype(float).where(~clv.isna()); b = _su(flag, 60); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_count_strong_neg_60d_slope_v087_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); flag = (clv < -0.5).astype(float).where(~clv.isna()); b = _su(flag, 60); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_rank_in_60d_slope_v088_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); b = _ru(clv, 60).apply(_rank_last, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_volwtd_median_30d_slope_v089_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); norm = (clv * volume) / _mn(volume, 30).replace(0.0, np.nan); b = _ru(norm, 30).median(); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_regslope_60d_slope_v090_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj)
    ad = (clv * volume).cumsum()
    return _r(_ru(ad, 60).apply(_olsslope, raw=True).diff(21))
def f26ad_f26_accumulation_distribution_ad_rsq_120d_slope_v091_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj)
    ad = (clv * volume).cumsum()
    return _r(_ru(ad, 120).apply(_olsrsq, raw=True).diff(63))
def f26ad_f26_accumulation_distribution_ad_residstd_50d_slope_v092_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj)
    ad = (clv * volume).cumsum()
    return _r(_ru(ad, 50).apply(_olsresid, raw=True).diff(21))
def f26ad_f26_accumulation_distribution_clvvol_return_corr_45d_slope_v093_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ret = closeadj.pct_change(1); b = _ru(clv, 45).corr(ret); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_vol_corr_30d_slope_v094_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); lv = np.log(volume.replace(0.0, np.nan)); b = _ru(clv, 30).corr(lv); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_chaikin_acc_25d_slope_v095_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); den = _vs(volume, 25); b = (co - 2.0 * co.shift(12) + co.shift(25)) / den; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_mfi_short_long_diff_slope_v096_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0; rmf = tp * volume; direction = np.sign(tp.diff(1)); pos = rmf.where(direction > 0.0, 0.0); neg = rmf.where(direction < 0.0, 0.0); pf7 = _su(pos, 7); nf7 = _su(neg, 7).replace(0.0, np.nan); pf28 = _su(pos, 28); nf28 = _su(neg, 28).replace(0.0, np.nan); mfi7 = 100.0 - 100.0 / (1.0 + pf7 / nf7); mfi28 = 100.0 - 100.0 / (1.0 + pf28 / nf28); b = mfi7 - mfi28; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_arctan_mfi_zscore_60d_slope_v097_signal(high, low, closeadj, volume):
    mfi = _mfi(high, low, closeadj, volume, 14); mu = _mn(mfi, 60); sd = _ru(mfi, 60).std(ddof=0).replace(0.0, np.nan); b = np.arctan((mfi - mu) / sd); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_cmf21_minus_cmf50_75d_smoothed_slope_v098_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; c21 = _su(cv, 21) / _vs(volume, 21); c50 = _su(cv, 50) / _vs(volume, 50); b = (c21 - c50).ewm(span=10, adjust=False, min_periods=10).mean(); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_days_since_chaikin_xover_45d_slope_v099_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sig9 = _ema(co, 9); s = np.sign(co - sig9); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()); b = _ru(flip, 45).apply(_streak_run, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_acc_zscore_30d_slope_v100_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); acc = ad - 2.0 * ad.shift(15) + ad.shift(30); mu = _mn(acc, 60); sd = _ru(acc, 60).std(ddof=0).replace(0.0, np.nan); b = (acc - mu) / sd; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_chaikin_extreme_count_120d_slope_v101_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sd = _ru(co, 120).std(ddof=0).replace(0.0, np.nan); z = co / sd; flag = (z.abs() > 1.0).astype(float).where(~z.isna()); b = _su(flag, 120); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clv_vol_weighted_mean_15d_slope_v102_signal(high, low, close, volume):
    b = _cmf(high, low, close, volume, 15); return _r(b.diff(5))
def f26ad_f26_accumulation_distribution_chaikin_z_60d_slope_v103_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); mu = _mn(co, 60); sd = _ru(co, 60).std(ddof=0).replace(0.0, np.nan); b = (co - mu) / sd; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_mfi14_rank_120d_slope_v104_signal(high, low, closeadj, volume):
    mfi = _mfi(high, low, closeadj, volume, 14); b = _ru(mfi, 120).apply(_rank_last, raw=True); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_mfi_oversold_frac_45d_slope_v105_signal(high, low, closeadj, volume):
    mfi = _mfi(high, low, closeadj, volume, 14); flag = (mfi < 30.0).astype(float).where(~mfi.isna()); b = _mn(flag, 45); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_klinger_oscillator_norm_z_60d_slope_v106_signal(high, low, closeadj, volume):
    kvf = _kvf(high, low, closeadj, volume); e34 = _ema(kvf, 34); e55 = _ema(kvf, 55); ko = e34 - e55; mu = _mn(ko, 60); sd = _ru(ko, 60).std(ddof=0).replace(0.0, np.nan); b = (ko - mu) / sd; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_return_div_30d_slope_v107_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); ad_chg = ad.diff(30) / _vs(volume, 30); px_chg = closeadj.pct_change(30); b = ad_chg - px_chg; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_clvvol_ac1_45d_slope_v108_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj)
    cv = clv * volume
    return _r(_ru(cv, 45).apply(_ac1, raw=True).diff(21))
def f26ad_f26_accumulation_distribution_chaikin_3_10_signal_dist_z_60d_slope_v109_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sig9 = _ema(co, 9); hist = co - sig9; mu = _mn(hist, 60); sd = _ru(hist, 60).std(ddof=0).replace(0.0, np.nan); b = (hist - mu) / sd; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_pos_streak_max_60d_slope_v110_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); pos = (clv > 0.0).astype(float).where(~clv.isna()); b = _ru(pos, 60).apply(_max_run, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_neg_streak_max_60d_slope_v111_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); neg = (clv < 0.0).astype(float).where(~clv.isna()); b = _ru(neg, 60).apply(_max_run, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_price_corr_50d_slope_v112_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); b = _ru(ad, 50).corr(closeadj); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_price_diff_corr_30d_slope_v113_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); b = _ru(ad.diff(5), 30).corr(closeadj.diff(5)); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_clv_abs_mean_50d_slope_v114_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); b = clv.abs().rolling(50, min_periods=50).mean(); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_high_acc_vol_share_50d_slope_v115_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); strong_vol = volume.where(clv > 0.5, 0.0); den = _vs(volume, 50); b = _su(strong_vol, 50) / den; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_high_dist_vol_share_50d_slope_v116_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); strong_vol = volume.where(clv < -0.5, 0.0); den = _vs(volume, 50); b = _su(strong_vol, 50) / den; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clvvol_max_to_mean_30d_slope_v117_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = (clv * volume).abs(); mx = _ru(cv, 30).max(); mn = _mn(cv, 30).replace(0.0, np.nan); b = mx / mn; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_chaikin_above_signal_xover_count_60d_slope_v118_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sig9 = _ema(co, 9); s = np.sign(co - sig9); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()); b = _su(flip, 60); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_velocity_norm_60d_slope_v119_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; sd = _ru(cv, 60).std(ddof=0).replace(0.0, np.nan); b = cv / sd; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_vol_corr_120d_slope_v120_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); lv = np.log(volume.replace(0.0, np.nan)); b = _ru(clv, 120).corr(lv); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clv_arctan_mean_30d_slope_v121_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); b = np.arctan(3.0 * _mn(clv, 30)); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_tanh_clvvol_z_50d_slope_v122_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; sd = _ru(cv, 50).std(ddof=0).replace(0.0, np.nan); b = np.tanh(cv / sd); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_klinger_signal_dist_norm_slope_v123_signal(high, low, closeadj, volume):
    kvf = _kvf(high, low, closeadj, volume); e34 = _ema(kvf, 34); e55 = _ema(kvf, 55); ko = e34 - e55; sig13 = _ema(ko, 13); hist = ko - sig13; sd = _ru(hist, 60).std(ddof=0).replace(0.0, np.nan); b = hist / sd; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_ema_diff_5_20_slope_v124_signal(high, low, close, volume):
    clv = _clv(high, low, close); ad = (clv * volume).cumsum(); e5 = _ema(ad, 5); e20 = _ema(ad, 20); b = np.log(e5.abs().replace(0.0, np.nan) / e20.abs().replace(0.0, np.nan)); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_obv_zspread_60d_slope_v125_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); obv = (np.sign(closeadj.diff(1)) * volume).cumsum(); z_ad = (ad - _mn(ad, 60)) / _ru(ad, 60).std(ddof=0).replace(0.0, np.nan); z_obv = (obv - _mn(obv, 60)) / _ru(obv, 60).std(ddof=0).replace(0.0, np.nan); b = z_ad - z_obv; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_neg_run_count_45d_slope_v126_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj)
    neg = (clv < 0.0).astype(float).where(~clv.isna())
    return _r(_ru(neg, 45).apply(_runs, raw=True).diff(21))
def f26ad_f26_accumulation_distribution_ad_log_velocity_30d_slope_v127_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); num = (ad - ad.shift(30)).abs(); den = _su(volume, 30); b = np.log(num.replace(0.0, np.nan)) - np.log(den.replace(0.0, np.nan)); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_chaikin_sign_freq_30d_slope_v128_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); e3 = _ema(ad, 3); e10 = _ema(ad, 10); s = np.sign(e3 - e10); b = _mn(s, 30); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_mfi_sign_freq_45d_slope_v129_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0; rmf = tp * volume; direction = np.sign(tp.diff(1)); pos = rmf.where(direction > 0.0, 0.0); neg = rmf.where(direction < 0.0, 0.0); pf = _su(pos, 14); nf = _su(neg, 14).replace(0.0, np.nan); mfi = 100.0 - 100.0 / (1.0 + pf / nf); s = np.sign(mfi - 50.0); b = _mn(s, 45); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clvvol_skew_60d_slope_v130_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; b = _ru(cv, 60).skew(); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_obv_diff_zscore_60d_slope_v131_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); obv = (np.sign(closeadj.diff(1)) * volume).cumsum(); diff = ad - obv; mu = _mn(diff, 60); sd = _ru(diff, 60).std(ddof=0).replace(0.0, np.nan); b = (diff - mu) / sd; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_ad_above_below_freq_90d_slope_v132_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); above = (ad > _mn(ad, 45)).astype(float).where(~_mn(ad, 45).isna()); b = _mn(above, 90); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clv_change_volwtd_45d_slope_v133_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); dclv = clv.diff(1); num = _su((dclv * volume), 45); den = _vs(volume, 45); b = num / den; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_williams_ad_zscore_60d_slope_v134_signal(high, low, closeadj, volume):
    pc = closeadj.shift(1); up_part = closeadj - low.combine(pc, np.minimum); dn_part = closeadj - high.combine(pc, np.maximum); sgn = np.sign(closeadj - pc); wad_bar = np.where(sgn > 0.0, up_part, np.where(sgn < 0.0, dn_part, 0.0)); wad = pd.Series(wad_bar, index=closeadj.index).cumsum(); mu = _mn(wad, 60); sd = _ru(wad, 60).std(ddof=0).replace(0.0, np.nan); b = (wad - mu) / sd; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_klinger_zero_streak_50d_slope_v135_signal(high, low, closeadj, volume):
    kvf = _kvf(high, low, closeadj, volume); e34 = _ema(kvf, 34); e55 = _ema(kvf, 55); s = np.sign(e34 - e55); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()); b = _ru(flip, 50).apply(_streak_run, raw=True); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_skew_rank_120d_slope_v136_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); sk = _ru(clv, 60).skew(); b = _ru(sk, 120).apply(_rank_last, raw=True); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_clvvol_abs_share_50d_slope_v137_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = (clv * volume).abs(); num = _su(cv, 50); den = (_ru(cv, 50).max() * 50.0).replace(0.0, np.nan); b = num / den; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clvvol_ema21_minus_sma21_slope_v138_signal(high, low, close, volume):
    clv = _clv(high, low, close); cv = clv * volume; em = _ema(cv, 21); sm = _mn(cv, 21); den = _mn(volume, 21).replace(0.0, np.nan); b = (em - sm) / den; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_path_efficiency_60d_slope_v139_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv = clv * volume; ad = cv.cumsum(); net = (ad - ad.shift(60)).abs(); path = cv.abs().rolling(60, min_periods=60).sum().replace(0.0, np.nan); b = net / path; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_chaikin_path_efficiency_45d_slope_v140_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); net = (co - co.shift(45)).abs(); path = co.diff(1).abs().rolling(45, min_periods=45).sum().replace(0.0, np.nan); b = net / path; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_volwtd_q75_30d_slope_v141_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj)
    cv = clv * volume
    return _r(_ru(cv, 30).apply(_q75, raw=True).diff(10))
def f26ad_f26_accumulation_distribution_clv_volwtd_q25_30d_slope_v142_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj)
    cv = clv * volume
    return _r(_ru(cv, 30).apply(_q25, raw=True).diff(10))
def f26ad_f26_accumulation_distribution_clvvol_volwtd_kurt_120d_slope_v143_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); norm = (clv * volume) / _mn(volume, 120).replace(0.0, np.nan); b = _ru(norm, 120).kurt(); return _r(b.diff(63))
def f26ad_f26_accumulation_distribution_ad_sign_changes_60d_slope_v144_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); ad = (clv * volume).cumsum(); s = np.sign(ad.diff(5)); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()); b = _su(flip, 60); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_clv_sign_changes_30d_slope_v145_signal(high, low, closeadj):
    clv = _clv(high, low, closeadj); s = np.sign(clv); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna()); b = _su(flip, 30); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_chaikin_above_signal_freq_40d_slope_v146_signal(high, low, closeadj, volume):
    co = _chk(high, low, closeadj, volume); sig9 = _ema(co, 9); above = (co > sig9).astype(float).where(~co.isna() & ~sig9.isna()); b = _mn(above, 40); return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_mfi14_vs_cmf21_diff_slope_v147_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0; rmf = tp * volume; direction = np.sign(tp.diff(1)); pos = rmf.where(direction > 0.0, 0.0); neg = rmf.where(direction < 0.0, 0.0); pf = _su(pos, 14); nf = _su(neg, 14).replace(0.0, np.nan); mfi = 100.0 - 100.0 / (1.0 + pf / nf); mfi_c = 2.0 * mfi / 100.0 - 1.0; clv = _clv(high, low, closeadj); n2 = _su((clv * volume), 21); d2 = _vs(volume, 21); cmf = n2 / d2; b = mfi_c - cmf; return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_ad_log_path_30d_slope_v148_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cv_abs = (clv * volume).abs(); num = _su(cv_abs, 30); den = _vs(volume, 30); b = np.log1p(num / den); return _r(b.diff(10))
def f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_unweighted_75d_slope_v149_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cmf = _su((clv * volume), 75) / _vs(volume, 75); sw = _mn(clv, 75); b = cmf - sw; return _r(b.diff(21))
def f26ad_f26_accumulation_distribution_cmf21_arctan_slope_slope_v150_signal(high, low, closeadj, volume):
    clv = _clv(high, low, closeadj); cmf = _su((clv * volume), 21) / _vs(volume, 21); b = np.arctan(5.0 * (cmf - cmf.shift(15))); return _r(b.diff(10))
_e = [
    (f26ad_f26_accumulation_distribution_raw_clv_1d_slope_v001_signal, ["high", "low", "close"]),
    (f26ad_f26_accumulation_distribution_clv_sign_1d_slope_v002_signal, ["high", "low", "close"]),
    (f26ad_f26_accumulation_distribution_clv_mean_5d_slope_v003_signal, ["high", "low", "close"]),
    (f26ad_f26_accumulation_distribution_clv_mean_21d_slope_v004_signal, ["high", "low", "close"]),
    (f26ad_f26_accumulation_distribution_clv_mean_63d_slope_v005_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_volratio_5d_slope_v006_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf_50d_slope_v008_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf_100d_slope_v009_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf_sign_21d_slope_v010_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf50_minus_cmf21_sign_slope_v011_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_minus_sma_30d_slope_v012_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_minus_sma_120d_slope_v013_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_slope_norm_30d_slope_v014_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_path_curvature_120d_slope_v015_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_curv_50d_slope_v016_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_pct_change_10d_slope_v018_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_osc_sign_3_10_slope_v019_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_zero_streak_60d_slope_v020_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_klinger_osc_34_55_slope_v021_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_klinger_sign_34_55_slope_v022_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_upclv_volsum_21d_slope_v023_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_downclv_volshare_50d_slope_v024_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_upclv_downclv_ratio_30d_slope_v025_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_count_clvpos_30d_slope_v026_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_count_clvneg_75d_slope_v027_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clvneg_streak_40d_slope_v028_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clvpos_streak_40d_slope_v029_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_high_dist_days_50d_slope_v030_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_high_acc_days_50d_slope_v031_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf21_zscore_120d_slope_v032_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf50_rank_180d_slope_v033_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf21_slope_10d_slope_v034_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_arctan_cmf21_slope_v035_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_tanh_ad_zscore_60d_slope_v036_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_sigmoid_chaikin_3_10_slope_v037_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_obv_corr_60d_slope_v038_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_obv_diff_norm_30d_slope_v039_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_zscore_60d_slope_v040_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_rank_200d_slope_v041_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi_14d_slope_v042_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi_28d_slope_v043_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi14_slope_10d_slope_v044_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_pos_mf_ratio_21d_slope_v045_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_pos_mf_ratio_100d_slope_v046_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_price_divergence_30d_slope_v047_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_price_divergence_100d_slope_v048_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clvvol_per_bar_mean_10d_slope_v049_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_clvvol_per_bar_z_30d_slope_v050_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_time_corr_60d_slope_v051_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_time_corr_150d_slope_v052_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_entropy_30d_slope_v053_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_cmf_multiwin_signagree_slope_v054_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_signal_xover_streak_50d_slope_v055_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_kurt_120d_slope_v056_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_days_since_clv_pos_slope_v057_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_days_since_clv_neg_slope_v058_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_cmf21_std_60d_slope_v059_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_volwtd_skew_50d_slope_v060_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_ac1_30d_slope_v061_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_ac5_75d_slope_v062_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_high_extreme_frac_45d_slope_v063_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clvvol_volzscore_corr_60d_slope_v064_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_klinger_sign_streak_45d_slope_v065_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_klinger_vf_norm_100d_slope_v066_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi14_sign_slope_v067_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf21_minus_cmf100_slope_v068_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_3_10_slope_5d_slope_v069_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_williams_ad_slope_30d_slope_v070_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf21_kurt_120d_slope_v071_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi_overbought_frac_60d_slope_v072_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_zero_xover_count_120d_slope_v073_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_simple_30d_slope_v074_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf21_rank_minus_cmf50_rank_180d_slope_v075_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_median_15d_slope_v076_signal, ["high", "low", "close"]),
    (f26ad_f26_accumulation_distribution_clv_iqr_45d_slope_v077_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_mad_30d_slope_v078_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_skew_60d_slope_v079_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_kurt_120d_slope_v080_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_q90_50d_slope_v081_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_q10_50d_slope_v082_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_chaikin_hist_3_10_minus_signal_slope_v083_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_signal_distance_60d_slope_v084_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_pos_minus_neg_count_90d_slope_v085_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_count_strong_pos_60d_slope_v086_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_count_strong_neg_60d_slope_v087_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_rank_in_60d_slope_v088_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_volwtd_median_30d_slope_v089_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_regslope_60d_slope_v090_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_rsq_120d_slope_v091_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_residstd_50d_slope_v092_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clvvol_return_corr_45d_slope_v093_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_vol_corr_30d_slope_v094_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_acc_25d_slope_v095_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi_short_long_diff_slope_v096_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_arctan_mfi_zscore_60d_slope_v097_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf21_minus_cmf50_75d_smoothed_slope_v098_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_days_since_chaikin_xover_45d_slope_v099_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_acc_zscore_30d_slope_v100_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_extreme_count_120d_slope_v101_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_vol_weighted_mean_15d_slope_v102_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_z_60d_slope_v103_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi14_rank_120d_slope_v104_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi_oversold_frac_45d_slope_v105_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_klinger_oscillator_norm_z_60d_slope_v106_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_return_div_30d_slope_v107_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clvvol_ac1_45d_slope_v108_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_3_10_signal_dist_z_60d_slope_v109_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_pos_streak_max_60d_slope_v110_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clv_neg_streak_max_60d_slope_v111_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_ad_price_corr_50d_slope_v112_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_price_diff_corr_30d_slope_v113_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_abs_mean_50d_slope_v114_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_high_acc_vol_share_50d_slope_v115_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_high_dist_vol_share_50d_slope_v116_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clvvol_max_to_mean_30d_slope_v117_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_above_signal_xover_count_60d_slope_v118_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_velocity_norm_60d_slope_v119_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_vol_corr_120d_slope_v120_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_arctan_mean_30d_slope_v121_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_tanh_clvvol_z_50d_slope_v122_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_klinger_signal_dist_norm_slope_v123_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_ema_diff_5_20_slope_v124_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_obv_zspread_60d_slope_v125_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_neg_run_count_45d_slope_v126_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_ad_log_velocity_30d_slope_v127_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_sign_freq_30d_slope_v128_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi_sign_freq_45d_slope_v129_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clvvol_skew_60d_slope_v130_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_obv_diff_zscore_60d_slope_v131_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_above_below_freq_90d_slope_v132_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_change_volwtd_45d_slope_v133_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_williams_ad_zscore_60d_slope_v134_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_klinger_zero_streak_50d_slope_v135_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_skew_rank_120d_slope_v136_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_clvvol_abs_share_50d_slope_v137_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clvvol_ema21_minus_sma21_slope_v138_signal, ["high", "low", "close", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_path_efficiency_60d_slope_v139_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_chaikin_path_efficiency_45d_slope_v140_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_volwtd_q75_30d_slope_v141_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_volwtd_q25_30d_slope_v142_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clvvol_volwtd_kurt_120d_slope_v143_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_sign_changes_60d_slope_v144_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_sign_changes_30d_slope_v145_signal, ["high", "low", "closeadj"]),
    (f26ad_f26_accumulation_distribution_chaikin_above_signal_freq_40d_slope_v146_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_mfi14_vs_cmf21_diff_slope_v147_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_ad_log_path_30d_slope_v148_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_unweighted_75d_slope_v149_signal, ["high", "low", "closeadj", "volume"]),
    (f26ad_f26_accumulation_distribution_cmf21_arctan_slope_slope_v150_signal, ["high", "low", "closeadj", "volume"]),
]
f26_accumulation_distribution_slope_001_150_REGISTRY = {f.__name__: {"inputs": inp, "func": f} for f, inp in _e}


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
    for name, entry in f26_accumulation_distribution_slope_001_150_REGISTRY.items():
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
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
