"""f20 jerk 001-150."""
from __future__ import annotations
import numpy as np
import pandas as pd
_I,_N=[np.inf,-np.inf],np.nan
def _e(f,i):
    return (f.__name__,{"inputs":i,"func":f})

def _a(h, l, c, n):
    return _atr(_tr(h, l, c), n)

def _v(s, n):
    return s.pct_change().rolling(n).std(ddof=0)

def _tr(high, low, close):
    pc = close.shift(1)
    return pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)

def _atr(s_tr, n):
    return s_tr.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()

def _rank_window(x):
    return float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else _N

def f20ce_f20_volatility_compression_expansion_bb_in_kc_20d_jerk_v001_signal(high, low, close):
    n = 20; mid = close.rolling(n).mean(); sd = close.rolling(n).std(ddof=0); atr = _a(high, low, close, n)
    sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).astype(float).where(~mid.isna() & ~atr.isna())
    return (sq -2.0*sq.shift(10) + sq.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_bb_in_kc_streak_30d_jerk_v002_signal(high, low, closeadj):
    n = 30; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); atr = _a(high, low, closeadj, n)
    sq = ((mid + 1.5* sd < mid + 1.0* atr) & (mid - 1.5* sd > mid - 1.0* atr)).astype(float).where(~mid.isna() & ~atr.isna()); out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = 0.0
    for i in range(len(sq)):
        v = sq.iat[i]
        if not np.isfinite(v):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if v > 0.5 else 0.0
        out.iat[i] = cnt
    return (out -2.0*out.shift(21) + out.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_squeeze_break_20d_jerk_v003_signal(high, low, close):
    n = 20; mid = close.rolling(n).mean(); sd = close.rolling(n).std(ddof=0); atr = _a(high, low, close, n)
    sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).astype(float).where(~mid.isna() & ~atr.isna()); jb = ((sq.shift(1) > 0.5) & (sq < 0.5)).astype(float)
    signed = jb * np.sign(close - mid)
    return (signed -2.0*signed.shift(5) + signed.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_bbw_div_min_60d_jerk_v004_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); mn = bbw.rolling(60,min_periods=30).min(); base = bbw / mn.replace(0,_N)
    return ((base -2.0*base.shift(21) + base.shift(42)) / base.abs().rolling(21,min_periods=10).mean().replace(0,_N)).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_div_max_60d_jerk_v005_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N); mx = bbw.rolling(60,min_periods=30).max()
    _b = (bbw / mx.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_bbw_rank_120d_jerk_v006_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); rk = bbw.rolling(120,min_periods=60).apply(_rank_window, raw=True)
    return (rk -2.0*rk.shift(21) + rk.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_bbw_rel_avg_252d_jerk_v007_signal(closeadj):
    n = 40; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N); avg = bbw.rolling(252,min_periods=120).mean()
    _b = (bbw / avg.replace(0,_N) - 1.0)
    return (_b -2.0*_b.shift(63) + _b.shift(126)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_5_20_jerk_v008_signal(high, low, close):
    a5 = _a(high, low, close, 5); a20 = _a(high, low, close, 20)
    _b = (a5 / a20.replace(0,_N))
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_10_50_jerk_v009_signal(high, low, closeadj):
    a10 = _a(high, low, closeadj, 10); a50 = _a(high, low, closeadj, 50)
    _b = (a10 / a50.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_rank_100d_jerk_v010_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 14); rk = atr.rolling(100,min_periods=50).apply(_rank_window, raw=True)
    return (rk -2.0*rk.shift(21) + rk.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_decline_streak_20d_jerk_v011_signal(high, low, close):
    atr = _a(high, low, close, 14); cond = (atr.diff() < 0.0).astype(float).where(~atr.diff().isna()); out = pd.Series(_N, index=close.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return (out -2.0*out.shift(5) + out.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_rise_streak_20d_jerk_v012_signal(high, low, close):
    atr = _a(high, low, close, 14); cond = (atr.diff() > 0.0).astype(float).where(~atr.diff().isna()); out = pd.Series(_N, index=close.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return (out -2.0*out.shift(10) + out.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_pctile_low_60d_jerk_v013_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20); q25 = atr.rolling(60,min_periods=30).quantile(0.25)
    _b = (atr < q25).astype(float).where(~atr.isna() & ~q25.isna())
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_nr4_jerk_v014_signal(high, low):
    rng = high - low; mn = rng.rolling(4).min()
    _b = (rng <= mn + 1e-12).astype(float).where(~mn.isna())
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_nr7_jerk_v015_signal(high, low):
    rng = high - low; mn = rng.rolling(7).min()
    _b = (rng <= mn + 1e-12).astype(float).where(~mn.isna())
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_inside_bar_streak_jerk_v016_signal(high, low):
    cond = ((high < high.shift(1)) & (low > low.shift(1))).astype(float).where(~high.shift(1).isna()); out = pd.Series(_N, index=high.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return (out -2.0*out.shift(5) + out.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_outside_bar_streak_jerk_v017_signal(high, low):
    cond = ((high > high.shift(1)) & (low < low.shift(1))).astype(float).where(~high.shift(1).isna()); out = pd.Series(_N, index=high.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return (out -2.0*out.shift(5) + out.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_rank_50d_jerk_v018_signal(high, low):
    rng = high - low
    _b = rng.rolling(50,min_periods=25).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_inside_bar_count_30d_jerk_v019_signal(high, low):
    cond = ((high < high.shift(1)) & (low > low.shift(1))).astype(float).where(~high.shift(1).isna())
    _b = cond.rolling(30,min_periods=20).sum()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_wide_range_count_30d_jerk_v020_signal(high, low, close):
    rng = high - low; atr = _a(high, low, close, 14); wide = (rng > 1.5* atr).astype(float).where(~atr.isna())
    _b = wide.rolling(30,min_periods=20).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol20_slope_sign_jerk_v021_signal(close):
    v = _v(close, 20)
    _b = np.sign(v.diff(5))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol60_slope_sign_jerk_v022_signal(closeadj):
    v = _v(closeadj, 60)
    _b = np.sign(v.diff(21))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_curvature_30d_jerk_v023_signal(closeadj):
    v = _v(closeadj, 30)
    _b = (v -2.0*v.shift(10) + v.shift(20))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_minmax_norm_60d_jerk_v024_signal(closeadj):
    v = _v(closeadj, 20); mn = v.rolling(60,min_periods=30).min(); mx = v.rolling(60,min_periods=30).max()
    _b = ((v - mn) / (mx - mn).replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_zscore_120d_jerk_v025_signal(closeadj):
    v = _v(closeadj, 40); mu = v.rolling(120,min_periods=60).mean(); sd = v.rolling(120,min_periods=60).std(ddof=0)
    _b = ((v - mu) / sd.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_z_below_neg1_flag_jerk_v026_signal(closeadj):
    v = _v(closeadj, 30); mu = v.rolling(100,min_periods=50).mean(); sd = v.rolling(100,min_periods=50).std(ddof=0); z = (v - mu) / sd.replace(0,_N)
    _b = (z < -1.0).astype(float).where(~z.isna())
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_surge_5_60_jerk_v027_signal(close):
    v = _v(close, 5); avg = v.rolling(60,min_periods=30).mean()
    _b = (v / avg.replace(0,_N) - 1.0)
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_above_1p5x_30d_jerk_v028_signal(closeadj):
    v = _v(closeadj, 10); avg = v.rolling(30,min_periods=15).mean()
    _b = (v > 1.5* avg).astype(float).where(~avg.isna())
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_z_above_1_flag_jerk_v029_signal(closeadj):
    v = _v(closeadj, 20); mu = v.rolling(80,min_periods=40).mean(); sd = v.rolling(80,min_periods=40).std(ddof=0); z = (v - mu) / sd.replace(0,_N)
    _b = (z > 1.0).astype(float).where(~z.isna())
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_days_since_squeeze_60d_jerk_v030_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).where(~mid.isna() & ~atr.isna())
    out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = _N
    for i in range(len(sq)):
        v = sq.iat[i]
        if pd.isna(v):
            out.iat[i] = cnt; continue
        if bool(v): cnt = 0.0
        elif np.isfinite(cnt): cnt += 1.0
        out.iat[i] = cnt
    _b = out.clip(upper=60.0)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_days_since_expansion_60d_jerk_v031_signal(high, low, closeadj):
    rng = high - low; atr = _a(high, low, closeadj, 20); cond = (rng > 1.5* atr).where(~atr.isna()); out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = _N
    for i in range(len(cond)):
        v = cond.iat[i]
        if pd.isna(v):
            out.iat[i] = cnt; continue
        if bool(v): cnt = 0.0
        elif np.isfinite(cnt): cnt += 1.0
        out.iat[i] = cnt
    _b = out.clip(upper=60.0)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_compression_streak_30d_jerk_v032_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median()
    cond = (v < med).astype(float).where(~med.isna()); out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return (out -2.0*out.shift(10) + out.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_post_break_expansion_mag_jerk_v033_signal(high, low, close):
    atr14 = _a(high, low, close, 14); raw = (atr14 / atr14.shift(5).replace(0,_N)) - 1.0; s = raw.ewm(span=5, adjust=False, min_periods=5).mean()
    return (s -2.0*s.shift(5) + s.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_failed_breakout_count_60d_jerk_v034_signal(high, low, close):
    n = 20; mid = close.rolling(n).mean(); sd = close.rolling(n).std(ddof=0)
    atr20 = _a(high, low, close, n); sq = ((mid +2.0*sd < mid + 1.5* atr20) & (mid -2.0*sd > mid - 1.5* atr20)).astype(float).where(~mid.isna() & ~atr20.isna())
    returned = ((sq.shift(1) < 0.5) & (sq > 0.5)).astype(float).where(~sq.shift(1).isna()); broke = ((sq.shift(1) > 0.5) & (sq < 0.5)).astype(float).where(~sq.shift(1).isna())
    broke10 = broke.shift(1).rolling(10,min_periods=5).sum(); failed = (returned * (broke10 > 0.5).astype(float)).where(~broke10.isna())
    _b = failed.rolling(60,min_periods=30).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_agree_compression_count_jerk_v035_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr20 = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr20) & (mid -2.0*sd > mid - 1.5* atr20)).astype(float)
    a5 = _a(high, low, closeadj, 5); short_long = (a5 < atr20).astype(float); rng = high - low; nr4 = (rng <= rng.rolling(4).min() + 1e-12).astype(float)
    v = _v(closeadj, 20); mu = v.rolling(60,min_periods=30).mean(); sd2 = v.rolling(60,min_periods=30).std(ddof=0)
    z = (v - mu) / sd2.replace(0,_N); vol_low = (z < 0.0).astype(float); total = sq + short_long + nr4 + vol_low
    _b = total.where(~mid.isna() & ~sd2.isna())
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_agree_expansion_count_jerk_v036_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr20 = _a(high, low, closeadj, n); not_sq = (~((mid +2.0*sd < mid + 1.5* atr20) & (mid -2.0*sd > mid - 1.5* atr20))).astype(float)
    a5 = _a(high, low, closeadj, 5); short_long = (a5 > 1.2 * atr20).astype(float)
    rng = high - low; wide = (rng > 1.5* atr20).astype(float); v = _v(closeadj, 20)
    mu = v.rolling(60,min_periods=30).mean(); sd2 = v.rolling(60,min_periods=30).std(ddof=0); z = (v - mu) / sd2.replace(0,_N); vol_high = (z > 0.0).astype(float)
    _b = (not_sq + short_long + wide + vol_high).where(~mid.isna() & ~sd2.isna())
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_during_contraction_jerk_v037_signal(closeadj, volume):
    v = _v(closeadj, 10); med = v.rolling(30,min_periods=15).median()
    low_mask = (v < med).astype(float).where(~med.isna()); high_mask = (v > med).astype(float).where(~med.isna()); logv = np.log(volume.replace(0,_N))
    avg_low = (logv * low_mask).rolling(20,min_periods=10).sum() / low_mask.rolling(20,min_periods=10).sum().replace(0,_N)
    avg_high = (logv * high_mask).rolling(20,min_periods=10).sum() / high_mask.rolling(20,min_periods=10).sum().replace(0,_N)
    _b = (avg_low - avg_high)
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_volume_z_during_squeeze_jerk_v038_signal(high, low, closeadj, volume):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr = _a(high, low, closeadj, n); sqf = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).astype(float).where(~mid.isna() & ~atr.isna())
    vmu = volume.rolling(60,min_periods=30).mean(); vsd = volume.rolling(60,min_periods=30).std(ddof=0); z = (volume - vmu) / vsd.replace(0,_N)
    num = (z * sqf).rolling(30,min_periods=10).sum(); den = sqf.rolling(30,min_periods=10).sum().replace(0,_N)
    return (num / den -2.0*(num / den).shift(21) + (num / den).shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_arctan_bbw_60d_jerk_v039_signal(closeadj):
    n = 30; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N); mn = bbw.rolling(60,min_periods=30).min()
    _b = np.arctan(bbw / mn.replace(0,_N) - 1.0)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_tanh_volz_60d_jerk_v040_signal(closeadj):
    v = _v(closeadj, 30); mu = v.rolling(60,min_periods=30).mean(); sd = v.rolling(60,min_periods=30).std(ddof=0); z = (v - mu) / sd.replace(0,_N)
    return (np.tanh(z) -2.0*(np.tanh(z)).shift(10) + (np.tanh(z)).shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_sigmoid_bbw_diff_jerk_v041_signal(closeadj):
    n1, n2 = 20, 50; m1 = closeadj.rolling(n1).mean(); s1 = closeadj.rolling(n1).std(ddof=0)
    bbw1 = (4.0* s1) / m1.replace(0,_N); m2 = closeadj.rolling(n2).mean(); s2 = closeadj.rolling(n2).std(ddof=0)
    bbw2 = (4.0* s2) / m2.replace(0,_N); d = bbw1 - bbw2; mu = d.rolling(100,min_periods=50).mean(); sd = d.rolling(100,min_periods=50).std(ddof=0); z = (d - mu) / sd.replace(0,_N)
    _b = (1.0 / (1.0 + np.exp(-z)))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_oscillator_vol_long_short_jerk_v042_signal(closeadj):
    vs = _v(closeadj, 10); vl = _v(closeadj, 60)
    _b = ((vl - vs) / vl.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_squeeze_minus_expand_jerk_v043_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).astype(float); rng = high - low; ex = (rng > 1.5* atr).astype(float)
    _b = (sq - ex).where(~mid.isna() & ~atr.isna())
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_transition_event_signed_jerk_v044_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median(); above = (v > med).astype(float).where(~med.isna())
    _b = (above - above.shift(1))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_transition_count_120d_jerk_v045_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median(); above = (v > med).astype(float).where(~med.isna())
    flips = (above != above.shift(1)).astype(float).where(~above.shift(1).isna() & ~above.isna())
    _b = flips.rolling(120,min_periods=60).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_variance_of_vol_60d_jerk_v046_signal(closeadj):
    v = _v(closeadj, 10)
    _b = v.rolling(60,min_periods=30).var(ddof=0)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_of_vol_rank_120d_jerk_v047_signal(closeadj):
    v = _v(closeadj, 20); vov = v.rolling(20).std(ddof=0)
    _b = vov.rolling(120,min_periods=60).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_squeeze_duration_pre_break_jerk_v048_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).astype(float).where(~mid.isna() & ~atr.isna())
    out = pd.Series(_N, index=closeadj.index, dtype=float); cur = 0.0; last_dur = _N
    for i in range(len(sq)):
        v = sq.iat[i]
        if not np.isfinite(v):
            out.iat[i] = _N; continue
        if v > 0.5:
            cur += 1.0
        else:
            if cur > 0.0: last_dur = cur
            cur = 0.0
        out.iat[i] = last_dur
    return (out -2.0*out.shift(21) + out.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_bbw_acceleration_norm_jerk_v049_signal(closeadj):
    n = 25; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); accel = bbw -2.0*bbw.shift(5) + bbw.shift(10); norm = bbw.abs().rolling(50,min_periods=25).mean()
    _b = (accel / norm.replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_to_close_arctan_jerk_v050_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20); atr_avg = atr.rolling(100,min_periods=50).mean()
    _b = np.arctan(np.log(atr / atr_avg.replace(0,_N)))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_atr_ratio_5_jerk_v051_signal(high, low, close):
    rng = high - low; a5 = _a(high, low, close, 5)
    _b = (rng / a5.replace(0,_N))
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_return_abs_skew_50d_jerk_v052_signal(closeadj):
    r = closeadj.pct_change().abs()
    _b = r.rolling(50,min_periods=25).skew()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_return_abs_kurt_80d_jerk_v053_signal(closeadj):
    r = closeadj.pct_change().abs()
    _b = r.rolling(80,min_periods=40).kurt()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_tr_above_atr_freq_30d_jerk_v054_signal(high, low, close):
    atr = _a(high, low, close, 14); tr = _tr(high, low, close); flag = (tr > atr).astype(float).where(~atr.isna())
    _b = flag.rolling(30,min_periods=15).mean()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_norm_change_jerk_v055_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20)
    _b = ((atr - atr.shift(10)) / atr.shift(10).replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_volofvol_div_vol_60d_jerk_v056_signal(closeadj):
    v = _v(closeadj, 20); vov = v.rolling(20).std(ddof=0)
    _b = (vov / v.replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_donch_width_rank_50d_jerk_v057_signal(high, low):
    hh = high.rolling(20).max(); ll = low.rolling(20).min(); w = hh - ll
    _b = w.rolling(50,min_periods=25).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_donch_width_div_avg_100d_jerk_v058_signal(high, low):
    hh = high.rolling(40).max(); ll = low.rolling(40).min(); w = hh - ll; avg = w.rolling(100,min_periods=50).mean()
    _b = (w / avg.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_c2c_vs_hl_ratio_30d_jerk_v059_signal(high, low, closeadj):
    c2c = closeadj.pct_change().abs(); hl = (high - low) / closeadj.replace(0,_N)
    _b = (c2c.rolling(30,min_periods=15).mean() / hl.rolling(30,min_periods=15).mean().replace(0,_N) - 1.0)
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_body_size_rank_50d_jerk_v060_signal(open_, closeadj):
    body = (closeadj - open_).abs() / closeadj.replace(0,_N)
    _b = body.rolling(50,min_periods=25).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_compress_then_expand_jerk_v061_signal(high, low, closeadj):
    a5 = _a(high, low, closeadj, 5); a40 = _a(high, low, closeadj, 40); r = a5 / a40.replace(0,_N); mn = r.rolling(20,min_periods=10).min()
    return ((r - mn) -2.0*((r - mn)).shift(10) + ((r - mn)).shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_vs_recent_min_30d_jerk_v062_signal(high, low):
    rng = high - low; mn = rng.rolling(30,min_periods=15).min()
    _b = ((rng - mn) / mn.replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_mass_index_25d_jerk_v063_signal(high, low):
    hl = high - low; e1 = hl.ewm(span=9, adjust=False, min_periods=9).mean(); e2 = e1.ewm(span=9, adjust=False, min_periods=9).mean()
    _b = (e1 / e2.replace(0,_N)).rolling(25,min_periods=15).sum()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_chaikin_vol_10_jerk_v064_signal(high, low):
    hl = high - low; e = hl.ewm(span=10, adjust=False, min_periods=10).mean()
    _b = ((e / e.shift(10).replace(0,_N)) - 1.0)
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_chaikin_vol_30_jerk_v065_signal(high, low):
    hl = high - low; e = hl.ewm(span=30, adjust=False, min_periods=30).mean()
    _b = ((e / e.shift(30).replace(0,_N)) - 1.0)
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_bbw_acceleration_sign_jerk_v066_signal(closeadj):
    n = 30; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N)
    _b = np.sign(bbw -2.0*bbw.shift(10) + bbw.shift(20))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_disagreement_count_jerk_v067_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr20 = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr20) & (mid -2.0*sd > mid - 1.5* atr20)).astype(float)
    a5 = _a(high, low, closeadj, 5); sll = (a5 < atr20).astype(float); slh = (a5 > 1.2 * atr20).astype(float); rng = high - low; nr4 = (rng <= rng.rolling(4).min() + 1e-12).astype(float)
    wide = (rng > 1.5* atr20).astype(float); comp = sq + sll + nr4; ex = (1.0 - sq) + slh + wide
    _b = (comp - ex).abs().where(~mid.isna() & ~atr20.isna())
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_coil_score_jerk_v068_signal(high, low):
    rng = high - low; smaller = (rng < rng.shift(1)).astype(float).where(~rng.shift(1).isna())
    _b = smaller.rolling(5).sum()
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_autocorr_30d_jerk_v069_signal(closeadj):
    v = _v(closeadj, 10)
    _b = v.rolling(30,min_periods=20).apply(lambda x: float(pd.Series(x).autocorr(lag=1)) if len(x) > 2 else _N, raw=True)
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_autocorr_50d_jerk_v070_signal(high, low):
    rng = high - low
    _b = rng.rolling(50,min_periods=30).apply(lambda x: float(pd.Series(x).autocorr(lag=1)) if len(x) > 2 else _N, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_compression_roc_30d_jerk_v071_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N)
    _b = (bbw / bbw.shift(30).replace(0,_N) - 1.0)
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_iqr_returns_rank_80d_jerk_v072_signal(closeadj):
    r = closeadj.pct_change(); q75 = r.rolling(20).quantile(0.75); q25 = r.rolling(20).quantile(0.25); iqr = q75 - q25
    _b = iqr.rolling(80,min_periods=40).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_mad_returns_div_avg_jerk_v073_signal(closeadj):
    r = closeadj.pct_change(); mad = r.rolling(30).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True); avg = mad.rolling(100,min_periods=50).mean()
    _b = (mad / avg.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_volume_vol_corr_60d_jerk_v074_signal(closeadj, volume):
    r = closeadj.pct_change().abs(); lv = np.log(volume.replace(0,_N))
    _b = r.rolling(60,min_periods=30).corr(lv)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_spike_count_60d_jerk_v075_signal(closeadj):
    r = closeadj.pct_change(); v = r.rolling(20).std(ddof=0); flag = (r.abs() > 3.0* v).astype(float).where(~v.isna())
    _b = flag.rolling(60,min_periods=30).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_kc_width_div_close_20d_jerk_v076_signal(high, low, close):
    n = 20; atr = _a(high, low, close, n); mid = close.rolling(n).mean()
    _b = ((3.0* atr) / mid.replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_kc_width_rank_120d_jerk_v077_signal(high, low, closeadj):
    n = 40; atr = _a(high, low, closeadj, n); mid = closeadj.rolling(n).mean(); w = (3.0* atr) / mid.replace(0,_N)
    _b = w.rolling(120,min_periods=60).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_kc_vs_bbw_jerk_v078_signal(high, low, closeadj):
    n = 20; atr = _a(high, low, closeadj, n); mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    _b = ((3.0* atr - 4.0* sd) / mid.replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_sqret_short_long_jerk_v079_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    _b = (r2.rolling(30).mean() / r2.rolling(120,min_periods=60).mean().replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_sqret_zscore_60d_jerk_v080_signal(closeadj):
    r2 = closeadj.pct_change() ** 2; mu = r2.rolling(60,min_periods=30).mean(); sd = r2.rolling(60,min_periods=30).std(ddof=0)
    _b = ((r2 - mu) / sd.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_sqret_decline_streak_20d_jerk_v081_signal(closeadj):
    r2 = closeadj.pct_change() ** 2; v = r2.rolling(20).mean(); cond = (v.diff() < 0.0).astype(float).where(~v.diff().isna()); out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return (out -2.0*out.shift(10) + out.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_log_hl_sq_rank_60d_jerk_v082_signal(high, low):
    x = (np.log(high / low.replace(0,_N))) ** 2
    _b = x.rolling(60,min_periods=30).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_log_co_sq_short_long_jerk_v083_signal(open_, closeadj):
    x = (np.log(closeadj / open_.replace(0,_N))) ** 2
    _b = (x.rolling(20).mean() / x.rolling(80,min_periods=40).mean().replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_close_vs_kc_upper_norm_jerk_v084_signal(high, low, closeadj):
    n = 20; atr = _a(high, low, closeadj, n); mid = closeadj.rolling(n).mean()
    _b = ((closeadj - (mid +2.0*atr)) / atr.replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_close_outside_kc_count_30d_jerk_v085_signal(high, low, closeadj):
    n = 40; atr = _a(high, low, closeadj, n); mid = closeadj.rolling(n).mean(); kc_up = mid +2.0*atr; kc_lo = mid -2.0*atr
    flag = ((closeadj > kc_up) | (closeadj < kc_lo)).astype(float).where(~mid.isna())
    _b = flag.rolling(30,min_periods=20).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_volofrange_30d_jerk_v086_signal(high, low):
    rng = high - low
    _b = (rng.rolling(30,min_periods=15).std(ddof=0) / rng.rolling(30,min_periods=15).mean().replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_volofrange_zscore_jerk_v087_signal(high, low, closeadj):
    rng = high - low; cv = rng.rolling(20).std(ddof=0) / rng.rolling(20).mean().replace(0,_N); mu = cv.rolling(100,min_periods=50).mean(); sd = cv.rolling(100,min_periods=50).std(ddof=0)
    _b = ((cv - mu) / sd.replace(0,_N)).where(~closeadj.isna())
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_tr_vs_hl_ratio_20d_jerk_v088_signal(high, low, close):
    rng = (high - low).replace(0,_N); tr = _tr(high, low, close)
    _b = (tr / rng).rolling(20,min_periods=10).mean()
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_gap_jump_count_60d_jerk_v089_signal(high, low, closeadj):
    rng = (high - low).replace(0,_N); tr = _tr(high, low, closeadj); flag = (tr > 1.3 * rng).astype(float).where(~rng.isna())
    _b = flag.rolling(60,min_periods=30).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_regslope_40d_jerk_v090_signal(closeadj):
    v = _v(closeadj, 15)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float); xm = x.mean(); tm = t.mean()
        num = np.dot(x - xm, t - tm); den = np.dot(t - tm, t - tm)
        return float(num / den) if den != 0.0 else _N
    _b = v.rolling(40,min_periods=25).apply(_slope, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_regslope_80d_jerk_v091_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float); xm = x.mean(); tm = t.mean()
        num = np.dot(x - xm, t - tm); den = np.dot(t - tm, t - tm)
        return float(num / den) if den != 0.0 else _N
    _b = atr.rolling(80,min_periods=40).apply(_slope, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_bbw_zdist_to_min_jerk_v092_signal(closeadj):
    n = 30; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); mn = bbw.rolling(200,min_periods=100).min(); sigma = bbw.rolling(200,min_periods=100).std(ddof=0)
    _b = ((bbw - mn) / sigma.replace(0,_N))
    return (_b -2.0*_b.shift(63) + _b.shift(126)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_atr_dist_to_max_60d_jerk_v093_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20); mx = atr.rolling(60,min_periods=30).max(); mu = atr.rolling(60,min_periods=30).mean()
    _b = ((atr - mx) / mu.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_long_horizon_ratio_jerk_v094_signal(closeadj):
    vy = closeadj.pct_change().rolling(252,min_periods=126).std(ddof=0); vq = _v(closeadj, 63)
    _b = (vy / vq.replace(0,_N) - 1.0)
    return (_b -2.0*_b.shift(63) + _b.shift(126)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_med_range_rank_80d_jerk_v095_signal(high, low):
    rng = high - low; med = rng.rolling(20).median()
    _b = med.rolling(80,min_periods=40).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_p10_range_rel_p90_jerk_v096_signal(high, low):
    rng = high - low; q10 = rng.rolling(50,min_periods=25).quantile(0.10); q90 = rng.rolling(50,min_periods=25).quantile(0.90)
    _b = (q10 / q90.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_small_range_cluster_10d_jerk_v097_signal(high, low):
    rng = high - low; q30 = rng.rolling(60,min_periods=30).quantile(0.30); flag = (rng < q30).astype(float).where(~q30.isna())
    _b = flag.rolling(10,min_periods=5).sum()
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_large_range_cluster_10d_jerk_v098_signal(high, low):
    rng = high - low; q70 = rng.rolling(60,min_periods=30).quantile(0.70); flag = (rng > q70).astype(float).where(~q70.isna())
    _b = flag.rolling(10,min_periods=5).sum()
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_up_down_vol_ratio_30d_jerk_v099_signal(closeadj):
    r = closeadj.pct_change(); pos_sq = (r ** 2).where(r > 0.0, 0.0).where(~r.isna()); neg_sq = (r ** 2).where(r < 0.0, 0.0).where(~r.isna())
    upv = pos_sq.rolling(30).mean() ** 0.5; dnv = neg_sq.rolling(30).mean() ** 0.5
    _b = (upv / dnv.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_up_minus_down_vol_z_jerk_v100_signal(closeadj):
    r = closeadj.pct_change(); pos_sq = (r ** 2).where(r > 0.0, 0.0).where(~r.isna()); neg_sq = (r ** 2).where(r < 0.0, 0.0).where(~r.isna())
    upv = pos_sq.rolling(20).mean() ** 0.5; dnv = neg_sq.rolling(20).mean() ** 0.5; diff = upv - dnv; mu = diff.rolling(80,min_periods=40).mean(); sd = diff.rolling(80,min_periods=40).std(ddof=0)
    _b = ((diff - mu) / sd.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_gap_abs_30d_avg_jerk_v101_signal(open_, closeadj):
    pc = closeadj.shift(1); gap = (open_ - pc).abs() / pc.replace(0,_N)
    _b = gap.rolling(30,min_periods=15).mean()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_gap_zscore_60d_jerk_v102_signal(open_, closeadj):
    pc = closeadj.shift(1); gap = (open_ - pc).abs() / pc.replace(0,_N); mu = gap.rolling(60,min_periods=30).mean(); sd = gap.rolling(60,min_periods=30).std(ddof=0)
    _b = ((gap - mu) / sd.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_frac_below_p25_vol_60d_jerk_v103_signal(closeadj):
    v = _v(closeadj, 10); q25 = v.rolling(100,min_periods=50).quantile(0.25); flag = (v < q25).astype(float).where(~q25.isna())
    _b = flag.rolling(60,min_periods=30).mean()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_frac_above_p75_vol_60d_jerk_v104_signal(closeadj):
    v = _v(closeadj, 10); q75 = v.rolling(100,min_periods=50).quantile(0.75); flag = (v > q75).astype(float).where(~q75.isna())
    _b = flag.rolling(60,min_periods=30).mean()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_mom_sign_short_long_jerk_v105_signal(closeadj):
    v10 = _v(closeadj, 10); v40 = _v(closeadj, 40)
    _b = np.sign(v10.diff(20) - v40.diff(20))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_pctile_cross_event_jerk_v106_signal(high, low):
    rng = high - low; rank = rng.rolling(60,min_periods=30).apply(_rank_window, raw=True)
    up = ((rank > 0.75) & (rank.shift(1) <= 0.75)).astype(float); dn = ((rank < 0.25) & (rank.shift(1) >= 0.25)).astype(float)
    _b = (up - dn).where(~rank.isna() & ~rank.shift(1).isna())
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_recent_vol_concentration_jerk_v107_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    _b = (r2.rolling(5).sum() / r2.rolling(30,min_periods=15).sum().replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_tailshare_60d_jerk_v108_signal(closeadj):
    r = closeadj.pct_change(); sd = r.rolling(60,min_periods=30).std(ddof=0); flag = (r.abs() > sd).astype(float).where(~sd.isna())
    _b = flag.rolling(60,min_periods=30).mean()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_dist_from_252d_mean_jerk_v109_signal(closeadj):
    v = _v(closeadj, 30); avg = v.rolling(252,min_periods=126).mean()
    _b = (v / avg.replace(0,_N) - 1.0)
    return (_b -2.0*_b.shift(63) + _b.shift(126)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_drawdown_60d_jerk_v110_signal(closeadj):
    v = _v(closeadj, 20); mx = v.rolling(60,min_periods=30).max()
    _b = ((v - mx) / mx.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_runup_60d_jerk_v111_signal(closeadj):
    v = _v(closeadj, 20); mn = v.rolling(60,min_periods=30).min()
    _b = ((v - mn) / mn.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_3bar_contraction_jerk_v112_signal(high, low):
    rng = high - low; cond = (rng < rng.shift(1)) & (rng.shift(1) < rng.shift(2))
    _b = cond.astype(float).where(~rng.shift(2).isna())
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_3bar_expansion_jerk_v113_signal(high, low):
    rng = high - low; cond = (rng > rng.shift(1)) & (rng.shift(1) > rng.shift(2))
    _b = cond.astype(float).where(~rng.shift(2).isna())
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_pricecurv_vol_30d_jerk_v114_signal(closeadj):
    curv = (closeadj -2.0*closeadj.shift(5) + closeadj.shift(10)) / closeadj.replace(0,_N)
    _b = curv.rolling(30,min_periods=15).std(ddof=0)
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_compression_breadth_jerk_v115_signal(high, low, closeadj):
    r = closeadj.pct_change(); v5 = r.rolling(5).std(ddof=0); v10 = r.rolling(10).std(ddof=0)
    v20 = r.rolling(20).std(ddof=0); v40 = r.rolling(40).std(ddof=0); rng = high - low; rng_avg = rng.rolling(30,min_periods=15).mean()
    a5 = _a(high, low, closeadj, 5); a20 = _a(high, low, closeadj, 20)
    c = (v5 < v20).astype(float) + (v10 < v40).astype(float) + (rng < rng_avg).astype(float) + (a5 < a20).astype(float)
    _b = c.where(~v40.isna() & ~rng_avg.isna())
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_compress_streak_rank_jerk_v116_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median(); cond = (v < med).astype(float).where(~med.isna())
    out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    _b = out.rolling(200,min_periods=100).apply(_rank_window, raw=True)
    return (_b -2.0*_b.shift(63) + _b.shift(126)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_dir_reversals_60d_jerk_v117_signal(closeadj):
    v = _v(closeadj, 20); s = np.sign(v.diff(5)); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    _b = flip.rolling(60,min_periods=30).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_ar1_residual_jerk_v118_signal(closeadj):
    v = _v(closeadj, 20); rho = v.rolling(60,min_periods=30).corr(v.shift(1))
    _b = (v - rho * v.shift(1))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_absret_persistence_60d_jerk_v119_signal(closeadj):
    ar = closeadj.pct_change().abs()
    _b = ar.rolling(60,min_periods=30).corr(ar.shift(1))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_skew_80d_jerk_v120_signal(closeadj):
    v = _v(closeadj, 10)
    _b = v.rolling(80,min_periods=40).skew()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vw_volatility_ratio_jerk_v121_signal(closeadj, volume):
    r = closeadj.pct_change().abs(); num = (r * volume).rolling(20).sum(); den_r = r.rolling(20).sum().replace(0,_N); den_v = volume.rolling(20).sum().replace(0,_N) / 20.0
    _b = (num / (den_r * den_v))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_entropy_50d_jerk_v122_signal(high, low):
    rng = high - low
    def _ent(x):
        q = np.quantile(x, [0.25, 0.5, 0.75])
        buckets = np.array([(x <= q[0]).sum(), ((x > q[0]) & (x <= q[1])).sum(),
                            ((x > q[1]) & (x <= q[2])).sum(), (x > q[2]).sum()], dtype=float)
        p = buckets / buckets.sum(); p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    _b = rng.rolling(50,min_periods=25).apply(_ent, raw=True)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_pctb_extreme_freq_30d_jerk_v123_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    pctb = (closeadj - (m -2.0*sd)) / (4.0* sd).replace(0,_N); flag = ((pctb < 0.05) | (pctb > 0.95)).astype(float).where(~pctb.isna())
    _b = flag.rolling(30,min_periods=15).mean()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_cei_composite_jerk_v124_signal(high, low, closeadj):
    a5 = _a(high, low, closeadj, 5); a40 = _a(high, low, closeadj, 40); t1 = np.tanh(a5 / a40.replace(0,_N) - 1.0)
    v = _v(closeadj, 10); mu = v.rolling(60,min_periods=30).mean(); sd = v.rolling(60,min_periods=30).std(ddof=0); z = (v - mu) / sd.replace(0,_N); t2 = np.tanh(z)
    return ((t1 + t2) -2.0*((t1 + t2)).shift(21) + ((t1 + t2)).shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_days_since_60d_vol_min_jerk_v125_signal(closeadj):
    v = _v(closeadj, 20); mn = v.rolling(60,min_periods=30).min(); at_min = (v <= mn + 1e-12).astype(float).where(~mn.isna())
    out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = _N
    for i in range(len(at_min)):
        x = at_min.iat[i]
        if not np.isfinite(x):
            out.iat[i] = cnt; continue
        if x > 0.5: cnt = 0.0
        elif np.isfinite(cnt): cnt += 1.0
        out.iat[i] = cnt
    _b = out.clip(upper=60.0)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_days_since_60d_vol_max_jerk_v126_signal(closeadj):
    v = _v(closeadj, 20); mx = v.rolling(60,min_periods=30).max(); at_max = (v >= mx - 1e-12).astype(float).where(~mx.isna())
    out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = _N
    for i in range(len(at_max)):
        x = at_max.iat[i]
        if not np.isfinite(x):
            out.iat[i] = cnt; continue
        if x > 0.5: cnt = 0.0
        elif np.isfinite(cnt): cnt += 1.0
        out.iat[i] = cnt
    _b = out.clip(upper=60.0)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_entries_to_compression_jerk_v127_signal(closeadj):
    v = _v(closeadj, 10); q = v.rolling(100,min_periods=50).quantile(0.25); flag = (v < q).astype(float).where(~q.isna())
    entries = ((flag > 0.5) & (flag.shift(1) < 0.5)).astype(float).where(~flag.shift(1).isna())
    _b = entries.rolling(90,min_periods=45).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_exits_from_compression_jerk_v128_signal(closeadj):
    v = _v(closeadj, 10); q = v.rolling(100,min_periods=50).quantile(0.25); flag = (v < q).astype(float).where(~q.isna())
    exits = ((flag < 0.5) & (flag.shift(1) > 0.5)).astype(float).where(~flag.shift(1).isna())
    _b = exits.rolling(90,min_periods=45).sum()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_body_to_range_30d_jerk_v129_signal(open_, high, low, closeadj):
    rng = (high - low).replace(0,_N); body = (closeadj - open_).abs() / rng
    _b = body.rolling(30,min_periods=15).mean()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_wick_share_50d_jerk_v130_signal(open_, high, low, closeadj):
    rng = (high - low).replace(0,_N); wick = (rng - (closeadj - open_).abs()) / rng
    _b = wick.rolling(50,min_periods=25).mean()
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_band_ratio_long_short_jerk_v131_signal(closeadj):
    vs = _v(closeadj, 10); vl = _v(closeadj, 40)
    _b = (vl / vs.replace(0,_N) - 1.0)
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_log_range_sma_diff_jerk_v132_signal(high, low):
    lr = np.log(high / low.replace(0,_N)); s = lr.rolling(25).mean(); L = lr.rolling(100,min_periods=50).mean()
    _b = np.log(s / L.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_pct_decline_30d_jerk_v133_signal(closeadj):
    v = _v(closeadj, 20)
    _b = ((v.shift(30) - v) / v.shift(30).replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_realized_vol_min_jerk_v134_signal(closeadj):
    v = _v(closeadj, 20); mn = v.rolling(100,min_periods=50).min()
    _b = (mn / v.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_realized_vol_max_jerk_v135_signal(closeadj):
    v = _v(closeadj, 20); mx = v.rolling(100,min_periods=50).max()
    _b = (mx / v.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_acceleration_jerk_v136_signal(high, low):
    rng = high - low
    _b = ((rng - rng.shift(5)) - (rng.shift(5) - rng.shift(10)))
    return (_b -2.0*_b.shift(5) + _b.shift(10)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_2deriv_sign_30d_jerk_v137_signal(closeadj):
    v = _v(closeadj, 15)
    _b = np.sign(v -2.0*v.shift(10) + v.shift(20))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_signflip_count_30d_jerk_v138_signal(closeadj):
    s = np.sign(closeadj.pct_change()); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    _b = flip.rolling(30,min_periods=15).sum()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_change_consistent_jerk_v139_signal(closeadj):
    v = _v(closeadj, 15); s = np.sign(v.diff(5))
    _b = s.rolling(30,min_periods=15).mean()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_corr_lag5_60d_jerk_v140_signal(high, low):
    rng = high - low
    _b = rng.rolling(60,min_periods=30).corr(rng.shift(5))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_smoothness_30d_jerk_v141_signal(closeadj):
    v = _v(closeadj, 10); d = v.diff(1)
    _b = (d.rolling(30,min_periods=15).std(ddof=0) / v.rolling(30,min_periods=15).mean().replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_ohlc_dispersion_zscore_jerk_v142_signal(open_, high, low, closeadj):
    disp = pd.concat([open_, high, low, closeadj], axis=1).std(axis=1) / closeadj.replace(0,_N); mu = disp.rolling(100,min_periods=50).mean(); sd = disp.rolling(100,min_periods=50).std(ddof=0)
    _b = ((disp - mu) / sd.replace(0,_N))
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_regime_stability_jerk_v143_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median(); flag = (v > med).astype(float).where(~med.isna())
    flips = (flag != flag.shift(1)).astype(float).where(~flag.shift(1).isna() & ~flag.isna())
    _b = (1.0 - flips.rolling(60,min_periods=30).sum() / 60.0)
    return (_b -2.0*_b.shift(21) + _b.shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_rank_gap_jerk_v144_signal(closeadj):
    v10 = _v(closeadj, 10); v40 = _v(closeadj, 40); r10 = v10.rolling(60,min_periods=30).apply(_rank_window, raw=True)
    r40 = v40.rolling(120,min_periods=60).apply(_rank_window, raw=True)
    return ((r10 - r40) -2.0*((r10 - r40)).shift(21) + ((r10 - r40)).shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_above_p80_30d_jerk_v145_signal(high, low):
    rng = high - low; q = rng.rolling(120,min_periods=60).quantile(0.80); flag = (rng > q).astype(float).where(~q.isna())
    _b = flag.rolling(30,min_periods=15).mean()
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_range_slope_gap_jerk_v146_signal(high, low):
    rng = high - low; s10 = rng.rolling(10).mean(); s40 = rng.rolling(40).mean()
    _b = (s10.diff(10) - s40.diff(10))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_bbw_roc_zscore_jerk_v147_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N); roc = bbw / bbw.shift(5).replace(0,_N) - 1.0
    mu = roc.rolling(60,min_periods=30).mean(); sigma = roc.rolling(60,min_periods=30).std(ddof=0)
    _b = ((roc - mu) / sigma.replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_volgap_5_60_change_jerk_v148_signal(closeadj):
    vs = _v(closeadj, 5); vl = _v(closeadj, 60); gap = vs / vl.replace(0,_N) - 1.0; mu = gap.rolling(30,min_periods=15).mean()
    return ((gap - mu) -2.0*((gap - mu)).shift(21) + ((gap - mu)).shift(42)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_vol_curv_normalized_jerk_v149_signal(closeadj):
    v = _v(closeadj, 20); curv = v -2.0*v.shift(10) + v.shift(20)
    _b = (curv / v.shift(10).replace(0,_N))
    return (_b -2.0*_b.shift(10) + _b.shift(20)).replace(_I, _N)
def f20ce_f20_volatility_compression_expansion_composite_squeeze_jerk_v150_signal(high, low, closeadj):
    a5 = _a(high, low, closeadj, 5); a40 = _a(high, low, closeadj, 40); t1 = np.arctan(-(a5 / a40.replace(0,_N) - 1.0))
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); bbw_avg = bbw.rolling(60,min_periods=30).mean(); t2 = np.arctan(-(bbw / bbw_avg.replace(0,_N) - 1.0))
    v = _v(closeadj, 10); mu = v.rolling(60,min_periods=30).mean(); sigma = v.rolling(60,min_periods=30).std(ddof=0)
    z = (v - mu) / sigma.replace(0,_N); t3 = np.arctan(-z)
    return ((t1 + t2 + t3) -2.0*((t1 + t2 + t3)).shift(21) + ((t1 + t2 + t3)).shift(42)).replace(_I, _N)
f20_volatility_compression_expansion_jerk_001_150_REGISTRY = dict([
_e(f20ce_f20_volatility_compression_expansion_bb_in_kc_20d_jerk_v001_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_bb_in_kc_streak_30d_jerk_v002_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_squeeze_break_20d_jerk_v003_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_div_min_60d_jerk_v004_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_div_max_60d_jerk_v005_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_rank_120d_jerk_v006_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_rel_avg_252d_jerk_v007_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_5_20_jerk_v008_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_10_50_jerk_v009_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_rank_100d_jerk_v010_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_decline_streak_20d_jerk_v011_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_atr_rise_streak_20d_jerk_v012_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_atr_pctile_low_60d_jerk_v013_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_nr4_jerk_v014_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_nr7_jerk_v015_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_inside_bar_streak_jerk_v016_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_outside_bar_streak_jerk_v017_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_range_rank_50d_jerk_v018_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_inside_bar_count_30d_jerk_v019_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_wide_range_count_30d_jerk_v020_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_vol20_slope_sign_jerk_v021_signal, ["close"]),
_e(f20ce_f20_volatility_compression_expansion_vol60_slope_sign_jerk_v022_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_curvature_30d_jerk_v023_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_minmax_norm_60d_jerk_v024_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_zscore_120d_jerk_v025_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_z_below_neg1_flag_jerk_v026_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_surge_5_60_jerk_v027_signal, ["close"]),
_e(f20ce_f20_volatility_compression_expansion_vol_above_1p5x_30d_jerk_v028_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_z_above_1_flag_jerk_v029_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_days_since_squeeze_60d_jerk_v030_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_days_since_expansion_60d_jerk_v031_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_compression_streak_30d_jerk_v032_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_post_break_expansion_mag_jerk_v033_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_failed_breakout_count_60d_jerk_v034_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_agree_compression_count_jerk_v035_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_agree_expansion_count_jerk_v036_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_during_contraction_jerk_v037_signal, ["closeadj","volume"]),
_e(f20ce_f20_volatility_compression_expansion_volume_z_during_squeeze_jerk_v038_signal, ["high","low","closeadj","volume"]),
_e(f20ce_f20_volatility_compression_expansion_arctan_bbw_60d_jerk_v039_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_tanh_volz_60d_jerk_v040_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_sigmoid_bbw_diff_jerk_v041_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_oscillator_vol_long_short_jerk_v042_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_squeeze_minus_expand_jerk_v043_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_transition_event_signed_jerk_v044_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_transition_count_120d_jerk_v045_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_variance_of_vol_60d_jerk_v046_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_of_vol_rank_120d_jerk_v047_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_squeeze_duration_pre_break_jerk_v048_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_acceleration_norm_jerk_v049_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_to_close_arctan_jerk_v050_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_atr_ratio_5_jerk_v051_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_return_abs_skew_50d_jerk_v052_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_return_abs_kurt_80d_jerk_v053_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_tr_above_atr_freq_30d_jerk_v054_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_atr_norm_change_jerk_v055_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_volofvol_div_vol_60d_jerk_v056_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_donch_width_rank_50d_jerk_v057_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_donch_width_div_avg_100d_jerk_v058_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_c2c_vs_hl_ratio_30d_jerk_v059_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_body_size_rank_50d_jerk_v060_signal, ["open","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_compress_then_expand_jerk_v061_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_vs_recent_min_30d_jerk_v062_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_mass_index_25d_jerk_v063_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_chaikin_vol_10_jerk_v064_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_chaikin_vol_30_jerk_v065_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_acceleration_sign_jerk_v066_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_disagreement_count_jerk_v067_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_coil_score_jerk_v068_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_vol_autocorr_30d_jerk_v069_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_autocorr_50d_jerk_v070_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_compression_roc_30d_jerk_v071_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_iqr_returns_rank_80d_jerk_v072_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_mad_returns_div_avg_jerk_v073_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_volume_vol_corr_60d_jerk_v074_signal, ["closeadj","volume"]),
_e(f20ce_f20_volatility_compression_expansion_spike_count_60d_jerk_v075_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_kc_width_div_close_20d_jerk_v076_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_kc_width_rank_120d_jerk_v077_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_kc_vs_bbw_jerk_v078_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_sqret_short_long_jerk_v079_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_sqret_zscore_60d_jerk_v080_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_sqret_decline_streak_20d_jerk_v081_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_log_hl_sq_rank_60d_jerk_v082_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_log_co_sq_short_long_jerk_v083_signal, ["open","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_close_vs_kc_upper_norm_jerk_v084_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_close_outside_kc_count_30d_jerk_v085_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_volofrange_30d_jerk_v086_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_volofrange_zscore_jerk_v087_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_tr_vs_hl_ratio_20d_jerk_v088_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_gap_jump_count_60d_jerk_v089_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_regslope_40d_jerk_v090_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_regslope_80d_jerk_v091_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_zdist_to_min_jerk_v092_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_dist_to_max_60d_jerk_v093_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_long_horizon_ratio_jerk_v094_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_med_range_rank_80d_jerk_v095_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_p10_range_rel_p90_jerk_v096_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_small_range_cluster_10d_jerk_v097_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_large_range_cluster_10d_jerk_v098_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_up_down_vol_ratio_30d_jerk_v099_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_up_minus_down_vol_z_jerk_v100_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_gap_abs_30d_avg_jerk_v101_signal, ["open","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_gap_zscore_60d_jerk_v102_signal, ["open","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_frac_below_p25_vol_60d_jerk_v103_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_frac_above_p75_vol_60d_jerk_v104_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_mom_sign_short_long_jerk_v105_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_pctile_cross_event_jerk_v106_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_recent_vol_concentration_jerk_v107_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_tailshare_60d_jerk_v108_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_dist_from_252d_mean_jerk_v109_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_drawdown_60d_jerk_v110_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_runup_60d_jerk_v111_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_3bar_contraction_jerk_v112_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_3bar_expansion_jerk_v113_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_pricecurv_vol_30d_jerk_v114_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_compression_breadth_jerk_v115_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_compress_streak_rank_jerk_v116_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_dir_reversals_60d_jerk_v117_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_ar1_residual_jerk_v118_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_absret_persistence_60d_jerk_v119_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_skew_80d_jerk_v120_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vw_volatility_ratio_jerk_v121_signal, ["closeadj","volume"]),
_e(f20ce_f20_volatility_compression_expansion_range_entropy_50d_jerk_v122_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_pctb_extreme_freq_30d_jerk_v123_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_cei_composite_jerk_v124_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_days_since_60d_vol_min_jerk_v125_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_days_since_60d_vol_max_jerk_v126_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_entries_to_compression_jerk_v127_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_exits_from_compression_jerk_v128_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_body_to_range_30d_jerk_v129_signal, ["open","high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_wick_share_50d_jerk_v130_signal, ["open","high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_band_ratio_long_short_jerk_v131_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_log_range_sma_diff_jerk_v132_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_vol_pct_decline_30d_jerk_v133_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_realized_vol_min_jerk_v134_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_realized_vol_max_jerk_v135_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_acceleration_jerk_v136_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_vol_2deriv_sign_30d_jerk_v137_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_signflip_count_30d_jerk_v138_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_change_consistent_jerk_v139_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_corr_lag5_60d_jerk_v140_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_vol_smoothness_30d_jerk_v141_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_ohlc_dispersion_zscore_jerk_v142_signal, ["open","high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_regime_stability_jerk_v143_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_rank_gap_jerk_v144_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_above_p80_30d_jerk_v145_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_range_slope_gap_jerk_v146_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_roc_zscore_jerk_v147_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_volgap_5_60_change_jerk_v148_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_curv_normalized_jerk_v149_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_composite_squeeze_jerk_v150_signal, ["high","low","closeadj"]),
])


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed); seg = n // 4; rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret)); adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum(); closeadj = close * np.exp(adj_drift); intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5); high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n))); volume = rng.lognormal(mean=13.0, sigma=0.6, size=n); idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42); results: dict[str, pd.Series] = {}
    for name, entry in f20_volatility_compression_expansion_jerk_001_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252; coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results); assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]; aligned = aligned.replace(_I, _N); corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"; print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
