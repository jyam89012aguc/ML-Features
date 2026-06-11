"""f20 slope 001-150."""
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

def f20ce_f20_volatility_compression_expansion_bb_in_kc_20d_slope_v001_signal(high, low, close):
    n = 20; mid = close.rolling(n).mean(); sd = close.rolling(n).std(ddof=0); atr = _a(high, low, close, n)
    sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).astype(float).where(~mid.isna() & ~atr.isna())
    return sq.diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bb_in_kc_streak_30d_slope_v002_signal(high, low, closeadj):
    n = 30; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); atr = _a(high, low, closeadj, n)
    sq = ((mid + 1.5* sd < mid + 1.0* atr) & (mid - 1.5* sd > mid - 1.0* atr)).astype(float).where(~mid.isna() & ~atr.isna()); out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = 0.0
    for i in range(len(sq)):
        v = sq.iat[i]
        if not np.isfinite(v):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if v > 0.5 else 0.0
        out.iat[i] = cnt
    return out.diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_squeeze_break_20d_slope_v003_signal(high, low, close):
    n = 20; mid = close.rolling(n).mean(); sd = close.rolling(n).std(ddof=0); atr = _a(high, low, close, n)
    sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).astype(float).where(~mid.isna() & ~atr.isna()); jb = ((sq.shift(1) > 0.5) & (sq < 0.5)).astype(float)
    signed = jb * np.sign(close - mid)
    return signed.diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_div_min_60d_slope_v004_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); mn = bbw.rolling(60,min_periods=30).min(); base = bbw / mn.replace(0,_N)
    return (base.diff(21) / base.abs().rolling(21,min_periods=10).mean().replace(0,_N)).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_div_max_60d_slope_v005_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N); mx = bbw.rolling(60,min_periods=30).max()
    return (bbw / mx.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_rank_120d_slope_v006_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); rk = bbw.rolling(120,min_periods=60).apply(_rank_window, raw=True)
    return rk.diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_rel_avg_252d_slope_v007_signal(closeadj):
    n = 40; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N); avg = bbw.rolling(252,min_periods=120).mean()
    return (bbw / avg.replace(0,_N) - 1.0).diff(63).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_5_20_slope_v008_signal(high, low, close):
    a5 = _a(high, low, close, 5); a20 = _a(high, low, close, 20)
    return (a5 / a20.replace(0,_N)).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_10_50_slope_v009_signal(high, low, closeadj):
    a10 = _a(high, low, closeadj, 10); a50 = _a(high, low, closeadj, 50)
    return (a10 / a50.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_rank_100d_slope_v010_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 14); rk = atr.rolling(100,min_periods=50).apply(_rank_window, raw=True)
    return rk.diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_decline_streak_20d_slope_v011_signal(high, low, close):
    atr = _a(high, low, close, 14); cond = (atr.diff() < 0.0).astype(float).where(~atr.diff().isna()); out = pd.Series(_N, index=close.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return out.diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_rise_streak_20d_slope_v012_signal(high, low, close):
    atr = _a(high, low, close, 14); cond = (atr.diff() > 0.0).astype(float).where(~atr.diff().isna()); out = pd.Series(_N, index=close.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return out.diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_pctile_low_60d_slope_v013_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20); q25 = atr.rolling(60,min_periods=30).quantile(0.25)
    return (atr < q25).astype(float).where(~atr.isna() & ~q25.isna()).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_nr4_slope_v014_signal(high, low):
    rng = high - low; mn = rng.rolling(4).min()
    return (rng <= mn + 1e-12).astype(float).where(~mn.isna()).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_nr7_slope_v015_signal(high, low):
    rng = high - low; mn = rng.rolling(7).min()
    return (rng <= mn + 1e-12).astype(float).where(~mn.isna()).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_inside_bar_streak_slope_v016_signal(high, low):
    cond = ((high < high.shift(1)) & (low > low.shift(1))).astype(float).where(~high.shift(1).isna()); out = pd.Series(_N, index=high.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return out.diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_outside_bar_streak_slope_v017_signal(high, low):
    cond = ((high > high.shift(1)) & (low < low.shift(1))).astype(float).where(~high.shift(1).isna()); out = pd.Series(_N, index=high.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return out.diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_rank_50d_slope_v018_signal(high, low):
    rng = high - low
    return rng.rolling(50,min_periods=25).apply(_rank_window, raw=True).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_inside_bar_count_30d_slope_v019_signal(high, low):
    cond = ((high < high.shift(1)) & (low > low.shift(1))).astype(float).where(~high.shift(1).isna())
    return cond.rolling(30,min_periods=20).sum().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_wide_range_count_30d_slope_v020_signal(high, low, close):
    rng = high - low; atr = _a(high, low, close, 14); wide = (rng > 1.5* atr).astype(float).where(~atr.isna())
    return wide.rolling(30,min_periods=20).sum().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol20_slope_sign_slope_v021_signal(close):
    v = _v(close, 20)
    return np.sign(v.diff(5)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol60_slope_sign_slope_v022_signal(closeadj):
    v = _v(closeadj, 60)
    return np.sign(v.diff(21)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_curvature_30d_slope_v023_signal(closeadj):
    v = _v(closeadj, 30)
    return (v -2.0*v.shift(10) + v.shift(20)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_minmax_norm_60d_slope_v024_signal(closeadj):
    v = _v(closeadj, 20); mn = v.rolling(60,min_periods=30).min(); mx = v.rolling(60,min_periods=30).max()
    return ((v - mn) / (mx - mn).replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_zscore_120d_slope_v025_signal(closeadj):
    v = _v(closeadj, 40); mu = v.rolling(120,min_periods=60).mean(); sd = v.rolling(120,min_periods=60).std(ddof=0)
    return ((v - mu) / sd.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_z_below_neg1_flag_slope_v026_signal(closeadj):
    v = _v(closeadj, 30); mu = v.rolling(100,min_periods=50).mean(); sd = v.rolling(100,min_periods=50).std(ddof=0); z = (v - mu) / sd.replace(0,_N)
    return (z < -1.0).astype(float).where(~z.isna()).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_surge_5_60_slope_v027_signal(close):
    v = _v(close, 5); avg = v.rolling(60,min_periods=30).mean()
    return (v / avg.replace(0,_N) - 1.0).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_above_1p5x_30d_slope_v028_signal(closeadj):
    v = _v(closeadj, 10); avg = v.rolling(30,min_periods=15).mean()
    return (v > 1.5* avg).astype(float).where(~avg.isna()).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_z_above_1_flag_slope_v029_signal(closeadj):
    v = _v(closeadj, 20); mu = v.rolling(80,min_periods=40).mean(); sd = v.rolling(80,min_periods=40).std(ddof=0); z = (v - mu) / sd.replace(0,_N)
    return (z > 1.0).astype(float).where(~z.isna()).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_days_since_squeeze_60d_slope_v030_signal(high, low, closeadj):
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
    return out.clip(upper=60.0).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_days_since_expansion_60d_slope_v031_signal(high, low, closeadj):
    rng = high - low; atr = _a(high, low, closeadj, 20); cond = (rng > 1.5* atr).where(~atr.isna()); out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = _N
    for i in range(len(cond)):
        v = cond.iat[i]
        if pd.isna(v):
            out.iat[i] = cnt; continue
        if bool(v): cnt = 0.0
        elif np.isfinite(cnt): cnt += 1.0
        out.iat[i] = cnt
    return out.clip(upper=60.0).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_compression_streak_30d_slope_v032_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median()
    cond = (v < med).astype(float).where(~med.isna()); out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return out.diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_post_break_expansion_mag_slope_v033_signal(high, low, close):
    atr14 = _a(high, low, close, 14); raw = (atr14 / atr14.shift(5).replace(0,_N)) - 1.0; s = raw.ewm(span=5, adjust=False, min_periods=5).mean()
    return s.diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_failed_breakout_count_60d_slope_v034_signal(high, low, close):
    n = 20; mid = close.rolling(n).mean(); sd = close.rolling(n).std(ddof=0)
    atr20 = _a(high, low, close, n); sq = ((mid +2.0*sd < mid + 1.5* atr20) & (mid -2.0*sd > mid - 1.5* atr20)).astype(float).where(~mid.isna() & ~atr20.isna())
    returned = ((sq.shift(1) < 0.5) & (sq > 0.5)).astype(float).where(~sq.shift(1).isna()); broke = ((sq.shift(1) > 0.5) & (sq < 0.5)).astype(float).where(~sq.shift(1).isna())
    broke10 = broke.shift(1).rolling(10,min_periods=5).sum(); failed = (returned * (broke10 > 0.5).astype(float)).where(~broke10.isna())
    return failed.rolling(60,min_periods=30).sum().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_agree_compression_count_slope_v035_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr20 = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr20) & (mid -2.0*sd > mid - 1.5* atr20)).astype(float)
    a5 = _a(high, low, closeadj, 5); short_long = (a5 < atr20).astype(float); rng = high - low; nr4 = (rng <= rng.rolling(4).min() + 1e-12).astype(float)
    v = _v(closeadj, 20); mu = v.rolling(60,min_periods=30).mean(); sd2 = v.rolling(60,min_periods=30).std(ddof=0)
    z = (v - mu) / sd2.replace(0,_N); vol_low = (z < 0.0).astype(float); total = sq + short_long + nr4 + vol_low
    return total.where(~mid.isna() & ~sd2.isna()).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_agree_expansion_count_slope_v036_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr20 = _a(high, low, closeadj, n); not_sq = (~((mid +2.0*sd < mid + 1.5* atr20) & (mid -2.0*sd > mid - 1.5* atr20))).astype(float)
    a5 = _a(high, low, closeadj, 5); short_long = (a5 > 1.2 * atr20).astype(float)
    rng = high - low; wide = (rng > 1.5* atr20).astype(float); v = _v(closeadj, 20)
    mu = v.rolling(60,min_periods=30).mean(); sd2 = v.rolling(60,min_periods=30).std(ddof=0); z = (v - mu) / sd2.replace(0,_N); vol_high = (z > 0.0).astype(float)
    return (not_sq + short_long + wide + vol_high).where(~mid.isna() & ~sd2.isna()).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_during_contraction_slope_v037_signal(closeadj, volume):
    v = _v(closeadj, 10); med = v.rolling(30,min_periods=15).median()
    low_mask = (v < med).astype(float).where(~med.isna()); high_mask = (v > med).astype(float).where(~med.isna()); logv = np.log(volume.replace(0,_N))
    avg_low = (logv * low_mask).rolling(20,min_periods=10).sum() / low_mask.rolling(20,min_periods=10).sum().replace(0,_N)
    avg_high = (logv * high_mask).rolling(20,min_periods=10).sum() / high_mask.rolling(20,min_periods=10).sum().replace(0,_N)
    return (avg_low - avg_high).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_volume_z_during_squeeze_slope_v038_signal(high, low, closeadj, volume):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr))
    vmu = volume.rolling(60,min_periods=30).mean(); vsd = volume.rolling(60,min_periods=30).std(ddof=0); z = (volume - vmu) / vsd.replace(0,_N)
    return z.where(sq).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_arctan_bbw_60d_slope_v039_signal(closeadj):
    n = 30; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N); mn = bbw.rolling(60,min_periods=30).min()
    return np.arctan(bbw / mn.replace(0,_N) - 1.0).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_tanh_volz_60d_slope_v040_signal(closeadj):
    v = _v(closeadj, 30); mu = v.rolling(60,min_periods=30).mean(); sd = v.rolling(60,min_periods=30).std(ddof=0); z = (v - mu) / sd.replace(0,_N)
    return np.tanh(z).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_sigmoid_bbw_diff_slope_v041_signal(closeadj):
    n1, n2 = 20, 50; m1 = closeadj.rolling(n1).mean(); s1 = closeadj.rolling(n1).std(ddof=0)
    bbw1 = (4.0* s1) / m1.replace(0,_N); m2 = closeadj.rolling(n2).mean(); s2 = closeadj.rolling(n2).std(ddof=0)
    bbw2 = (4.0* s2) / m2.replace(0,_N); d = bbw1 - bbw2; mu = d.rolling(100,min_periods=50).mean(); sd = d.rolling(100,min_periods=50).std(ddof=0); z = (d - mu) / sd.replace(0,_N)
    return (1.0 / (1.0 + np.exp(-z))).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_oscillator_vol_long_short_slope_v042_signal(closeadj):
    vs = _v(closeadj, 10); vl = _v(closeadj, 60)
    return ((vl - vs) / vl.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_squeeze_minus_expand_slope_v043_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr) & (mid -2.0*sd > mid - 1.5* atr)).astype(float); rng = high - low; ex = (rng > 1.5* atr).astype(float)
    return (sq - ex).where(~mid.isna() & ~atr.isna()).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_transition_event_signed_slope_v044_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median(); above = (v > med).astype(float).where(~med.isna())
    return (above - above.shift(1)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_transition_count_120d_slope_v045_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median(); above = (v > med).astype(float).where(~med.isna())
    flips = (above != above.shift(1)).astype(float).where(~above.shift(1).isna() & ~above.isna())
    return flips.rolling(120,min_periods=60).sum().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_variance_of_vol_60d_slope_v046_signal(closeadj):
    v = _v(closeadj, 10)
    return v.rolling(60,min_periods=30).var(ddof=0).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_of_vol_rank_120d_slope_v047_signal(closeadj):
    v = _v(closeadj, 20); vov = v.rolling(20).std(ddof=0)
    return vov.rolling(120,min_periods=60).apply(_rank_window, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_squeeze_duration_pre_break_slope_v048_signal(high, low, closeadj):
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
    return out.diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_acceleration_norm_slope_v049_signal(closeadj):
    n = 25; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); accel = bbw -2.0*bbw.shift(5) + bbw.shift(10); norm = bbw.abs().rolling(50,min_periods=25).mean()
    return (accel / norm.replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_to_close_arctan_slope_v050_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20); atr_avg = atr.rolling(100,min_periods=50).mean()
    return np.arctan(np.log(atr / atr_avg.replace(0,_N))).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_atr_ratio_5_slope_v051_signal(high, low, close):
    rng = high - low; a5 = _a(high, low, close, 5)
    return (rng / a5.replace(0,_N)).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_return_abs_skew_50d_slope_v052_signal(closeadj):
    r = closeadj.pct_change().abs()
    return r.rolling(50,min_periods=25).skew().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_return_abs_kurt_80d_slope_v053_signal(closeadj):
    r = closeadj.pct_change().abs()
    return r.rolling(80,min_periods=40).kurt().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_tr_above_atr_freq_30d_slope_v054_signal(high, low, close):
    atr = _a(high, low, close, 14); tr = _tr(high, low, close); flag = (tr > atr).astype(float).where(~atr.isna())
    return flag.rolling(30,min_periods=15).mean().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_norm_change_slope_v055_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20)
    return ((atr - atr.shift(10)) / atr.shift(10).replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_volofvol_div_vol_60d_slope_v056_signal(closeadj):
    v = _v(closeadj, 20); vov = v.rolling(20).std(ddof=0)
    return (vov / v.replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_donch_width_rank_50d_slope_v057_signal(high, low):
    hh = high.rolling(20).max(); ll = low.rolling(20).min(); w = hh - ll
    return w.rolling(50,min_periods=25).apply(_rank_window, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_donch_width_div_avg_100d_slope_v058_signal(high, low):
    hh = high.rolling(40).max(); ll = low.rolling(40).min(); w = hh - ll; avg = w.rolling(100,min_periods=50).mean()
    return (w / avg.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_c2c_vs_hl_ratio_30d_slope_v059_signal(high, low, closeadj):
    c2c = closeadj.pct_change().abs(); hl = (high - low) / closeadj.replace(0,_N)
    return (c2c.rolling(30,min_periods=15).mean() / hl.rolling(30,min_periods=15).mean().replace(0,_N) - 1.0).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_body_size_rank_50d_slope_v060_signal(open_, closeadj):
    body = (closeadj - open_).abs() / closeadj.replace(0,_N)
    return body.rolling(50,min_periods=25).apply(_rank_window, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_compress_then_expand_slope_v061_signal(high, low, closeadj):
    a5 = _a(high, low, closeadj, 5); a40 = _a(high, low, closeadj, 40); r = a5 / a40.replace(0,_N); mn = r.rolling(20,min_periods=10).min()
    return (r - mn).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_vs_recent_min_30d_slope_v062_signal(high, low):
    rng = high - low; mn = rng.rolling(30,min_periods=15).min()
    return ((rng - mn) / mn.replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_mass_index_25d_slope_v063_signal(high, low):
    hl = high - low; e1 = hl.ewm(span=9, adjust=False, min_periods=9).mean(); e2 = e1.ewm(span=9, adjust=False, min_periods=9).mean()
    return (e1 / e2.replace(0,_N)).rolling(25,min_periods=15).sum().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_chaikin_vol_10_slope_v064_signal(high, low):
    hl = high - low; e = hl.ewm(span=10, adjust=False, min_periods=10).mean()
    return ((e / e.shift(10).replace(0,_N)) - 1.0).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_chaikin_vol_30_slope_v065_signal(high, low):
    hl = high - low; e = hl.ewm(span=30, adjust=False, min_periods=30).mean()
    return ((e / e.shift(30).replace(0,_N)) - 1.0).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_acceleration_sign_slope_v066_signal(closeadj):
    n = 30; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N)
    return np.sign(bbw -2.0*bbw.shift(10) + bbw.shift(20)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_disagreement_count_slope_v067_signal(high, low, closeadj):
    n = 20; mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    atr20 = _a(high, low, closeadj, n); sq = ((mid +2.0*sd < mid + 1.5* atr20) & (mid -2.0*sd > mid - 1.5* atr20)).astype(float)
    a5 = _a(high, low, closeadj, 5); sll = (a5 < atr20).astype(float); slh = (a5 > 1.2 * atr20).astype(float); rng = high - low; nr4 = (rng <= rng.rolling(4).min() + 1e-12).astype(float)
    wide = (rng > 1.5* atr20).astype(float); comp = sq + sll + nr4; ex = (1.0 - sq) + slh + wide
    return (comp - ex).abs().where(~mid.isna() & ~atr20.isna()).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_coil_score_slope_v068_signal(high, low):
    rng = high - low; smaller = (rng < rng.shift(1)).astype(float).where(~rng.shift(1).isna())
    return smaller.rolling(5).sum().diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_autocorr_30d_slope_v069_signal(closeadj):
    v = _v(closeadj, 10)
    return v.rolling(30,min_periods=20).apply(lambda x: float(pd.Series(x).autocorr(lag=1)) if len(x) > 2 else _N, raw=True).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_autocorr_50d_slope_v070_signal(high, low):
    rng = high - low
    return rng.rolling(50,min_periods=30).apply(lambda x: float(pd.Series(x).autocorr(lag=1)) if len(x) > 2 else _N, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_compression_roc_30d_slope_v071_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N)
    return (bbw / bbw.shift(30).replace(0,_N) - 1.0).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_iqr_returns_rank_80d_slope_v072_signal(closeadj):
    r = closeadj.pct_change(); q75 = r.rolling(20).quantile(0.75); q25 = r.rolling(20).quantile(0.25); iqr = q75 - q25
    return iqr.rolling(80,min_periods=40).apply(_rank_window, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_mad_returns_div_avg_slope_v073_signal(closeadj):
    r = closeadj.pct_change(); mad = r.rolling(30).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True); avg = mad.rolling(100,min_periods=50).mean()
    return (mad / avg.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_volume_vol_corr_60d_slope_v074_signal(closeadj, volume):
    r = closeadj.pct_change().abs(); lv = np.log(volume.replace(0,_N))
    return r.rolling(60,min_periods=30).corr(lv).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_spike_count_60d_slope_v075_signal(closeadj):
    r = closeadj.pct_change(); v = r.rolling(20).std(ddof=0); flag = (r.abs() > 3.0* v).astype(float).where(~v.isna())
    return flag.rolling(60,min_periods=30).sum().diff(21).replace(_I, _N)



def f20ce_f20_volatility_compression_expansion_kc_width_div_close_20d_slope_v076_signal(high, low, close):
    n = 20; atr = _a(high, low, close, n); mid = close.rolling(n).mean()
    return ((3.0* atr) / mid.replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_kc_width_rank_120d_slope_v077_signal(high, low, closeadj):
    n = 40; atr = _a(high, low, closeadj, n); mid = closeadj.rolling(n).mean(); w = (3.0* atr) / mid.replace(0,_N)
    return w.rolling(120,min_periods=60).apply(_rank_window, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_kc_vs_bbw_slope_v078_signal(high, low, closeadj):
    n = 20; atr = _a(high, low, closeadj, n); mid = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    return ((3.0* atr - 4.0* sd) / mid.replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_sqret_short_long_slope_v079_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    return (r2.rolling(30).mean() / r2.rolling(120,min_periods=60).mean().replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_sqret_zscore_60d_slope_v080_signal(closeadj):
    r2 = closeadj.pct_change() ** 2; mu = r2.rolling(60,min_periods=30).mean(); sd = r2.rolling(60,min_periods=30).std(ddof=0)
    return ((r2 - mu) / sd.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_sqret_decline_streak_20d_slope_v081_signal(closeadj):
    r2 = closeadj.pct_change() ** 2; v = r2.rolling(20).mean(); cond = (v.diff() < 0.0).astype(float).where(~v.diff().isna()); out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return out.diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_log_hl_sq_rank_60d_slope_v082_signal(high, low):
    x = (np.log(high / low.replace(0,_N))) ** 2
    return x.rolling(60,min_periods=30).apply(_rank_window, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_log_co_sq_short_long_slope_v083_signal(open_, closeadj):
    x = (np.log(closeadj / open_.replace(0,_N))) ** 2
    return (x.rolling(20).mean() / x.rolling(80,min_periods=40).mean().replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_close_vs_kc_upper_norm_slope_v084_signal(high, low, closeadj):
    n = 20; atr = _a(high, low, closeadj, n); mid = closeadj.rolling(n).mean()
    return ((closeadj - (mid +2.0*atr)) / atr.replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_close_outside_kc_count_30d_slope_v085_signal(high, low, closeadj):
    n = 40; atr = _a(high, low, closeadj, n); mid = closeadj.rolling(n).mean(); kc_up = mid +2.0*atr; kc_lo = mid -2.0*atr
    flag = ((closeadj > kc_up) | (closeadj < kc_lo)).astype(float).where(~mid.isna())
    return flag.rolling(30,min_periods=20).sum().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_volofrange_30d_slope_v086_signal(high, low):
    rng = high - low
    return (rng.rolling(30,min_periods=15).std(ddof=0) / rng.rolling(30,min_periods=15).mean().replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_volofrange_zscore_slope_v087_signal(high, low, closeadj):
    rng = high - low; cv = rng.rolling(20).std(ddof=0) / rng.rolling(20).mean().replace(0,_N); mu = cv.rolling(100,min_periods=50).mean(); sd = cv.rolling(100,min_periods=50).std(ddof=0)
    return ((cv - mu) / sd.replace(0,_N)).where(~closeadj.isna()).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_tr_vs_hl_ratio_20d_slope_v088_signal(high, low, close):
    rng = (high - low).replace(0,_N); tr = _tr(high, low, close)
    return (tr / rng).rolling(20,min_periods=10).mean().diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_gap_jump_count_60d_slope_v089_signal(high, low, closeadj):
    rng = (high - low).replace(0,_N); tr = _tr(high, low, closeadj); flag = (tr > 1.3 * rng).astype(float).where(~rng.isna())
    return flag.rolling(60,min_periods=30).sum().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_regslope_40d_slope_v090_signal(closeadj):
    v = _v(closeadj, 15)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float); xm = x.mean(); tm = t.mean()
        num = np.dot(x - xm, t - tm); den = np.dot(t - tm, t - tm)
        return float(num / den) if den != 0.0 else _N
    return v.rolling(40,min_periods=25).apply(_slope, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_regslope_80d_slope_v091_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float); xm = x.mean(); tm = t.mean()
        num = np.dot(x - xm, t - tm); den = np.dot(t - tm, t - tm)
        return float(num / den) if den != 0.0 else _N
    return atr.rolling(80,min_periods=40).apply(_slope, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_zdist_to_min_slope_v092_signal(closeadj):
    n = 30; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); mn = bbw.rolling(200,min_periods=100).min(); sigma = bbw.rolling(200,min_periods=100).std(ddof=0)
    return ((bbw - mn) / sigma.replace(0,_N)).diff(63).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_atr_dist_to_max_60d_slope_v093_signal(high, low, closeadj):
    atr = _a(high, low, closeadj, 20); mx = atr.rolling(60,min_periods=30).max(); mu = atr.rolling(60,min_periods=30).mean()
    return ((atr - mx) / mu.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_long_horizon_ratio_slope_v094_signal(closeadj):
    vy = closeadj.pct_change().rolling(252,min_periods=126).std(ddof=0); vq = _v(closeadj, 63)
    return (vy / vq.replace(0,_N) - 1.0).diff(63).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_med_range_rank_80d_slope_v095_signal(high, low):
    rng = high - low; med = rng.rolling(20).median()
    return med.rolling(80,min_periods=40).apply(_rank_window, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_p10_range_rel_p90_slope_v096_signal(high, low):
    rng = high - low; q10 = rng.rolling(50,min_periods=25).quantile(0.10); q90 = rng.rolling(50,min_periods=25).quantile(0.90)
    return (q10 / q90.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_small_range_cluster_10d_slope_v097_signal(high, low):
    rng = high - low; q30 = rng.rolling(60,min_periods=30).quantile(0.30); flag = (rng < q30).astype(float).where(~q30.isna())
    return flag.rolling(10,min_periods=5).sum().diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_large_range_cluster_10d_slope_v098_signal(high, low):
    rng = high - low; q70 = rng.rolling(60,min_periods=30).quantile(0.70); flag = (rng > q70).astype(float).where(~q70.isna())
    return flag.rolling(10,min_periods=5).sum().diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_up_down_vol_ratio_30d_slope_v099_signal(closeadj):
    r = closeadj.pct_change(); pos_sq = (r ** 2).where(r > 0.0, 0.0).where(~r.isna()); neg_sq = (r ** 2).where(r < 0.0, 0.0).where(~r.isna())
    upv = pos_sq.rolling(30).mean() ** 0.5; dnv = neg_sq.rolling(30).mean() ** 0.5
    return (upv / dnv.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_up_minus_down_vol_z_slope_v100_signal(closeadj):
    r = closeadj.pct_change(); pos_sq = (r ** 2).where(r > 0.0, 0.0).where(~r.isna()); neg_sq = (r ** 2).where(r < 0.0, 0.0).where(~r.isna())
    upv = pos_sq.rolling(20).mean() ** 0.5; dnv = neg_sq.rolling(20).mean() ** 0.5; diff = upv - dnv; mu = diff.rolling(80,min_periods=40).mean(); sd = diff.rolling(80,min_periods=40).std(ddof=0)
    return ((diff - mu) / sd.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_gap_abs_30d_avg_slope_v101_signal(open_, closeadj):
    pc = closeadj.shift(1); gap = (open_ - pc).abs() / pc.replace(0,_N)
    return gap.rolling(30,min_periods=15).mean().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_gap_zscore_60d_slope_v102_signal(open_, closeadj):
    pc = closeadj.shift(1); gap = (open_ - pc).abs() / pc.replace(0,_N); mu = gap.rolling(60,min_periods=30).mean(); sd = gap.rolling(60,min_periods=30).std(ddof=0)
    return ((gap - mu) / sd.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_frac_below_p25_vol_60d_slope_v103_signal(closeadj):
    v = _v(closeadj, 10); q25 = v.rolling(100,min_periods=50).quantile(0.25); flag = (v < q25).astype(float).where(~q25.isna())
    return flag.rolling(60,min_periods=30).mean().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_frac_above_p75_vol_60d_slope_v104_signal(closeadj):
    v = _v(closeadj, 10); q75 = v.rolling(100,min_periods=50).quantile(0.75); flag = (v > q75).astype(float).where(~q75.isna())
    return flag.rolling(60,min_periods=30).mean().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_mom_sign_short_long_slope_v105_signal(closeadj):
    v10 = _v(closeadj, 10); v40 = _v(closeadj, 40)
    return np.sign(v10.diff(20) - v40.diff(20)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_pctile_cross_event_slope_v106_signal(high, low):
    rng = high - low; rank = rng.rolling(60,min_periods=30).apply(_rank_window, raw=True)
    up = ((rank > 0.75) & (rank.shift(1) <= 0.75)).astype(float); dn = ((rank < 0.25) & (rank.shift(1) >= 0.25)).astype(float)
    return (up - dn).where(~rank.isna() & ~rank.shift(1).isna()).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_recent_vol_concentration_slope_v107_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    return (r2.rolling(5).sum() / r2.rolling(30,min_periods=15).sum().replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_tailshare_60d_slope_v108_signal(closeadj):
    r = closeadj.pct_change(); sd = r.rolling(60,min_periods=30).std(ddof=0); flag = (r.abs() > sd).astype(float).where(~sd.isna())
    return flag.rolling(60,min_periods=30).mean().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_dist_from_252d_mean_slope_v109_signal(closeadj):
    v = _v(closeadj, 30); avg = v.rolling(252,min_periods=126).mean()
    return (v / avg.replace(0,_N) - 1.0).diff(63).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_drawdown_60d_slope_v110_signal(closeadj):
    v = _v(closeadj, 20); mx = v.rolling(60,min_periods=30).max()
    return ((v - mx) / mx.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_runup_60d_slope_v111_signal(closeadj):
    v = _v(closeadj, 20); mn = v.rolling(60,min_periods=30).min()
    return ((v - mn) / mn.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_3bar_contraction_slope_v112_signal(high, low):
    rng = high - low; cond = (rng < rng.shift(1)) & (rng.shift(1) < rng.shift(2))
    return cond.astype(float).where(~rng.shift(2).isna()).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_3bar_expansion_slope_v113_signal(high, low):
    rng = high - low; cond = (rng > rng.shift(1)) & (rng.shift(1) > rng.shift(2))
    return cond.astype(float).where(~rng.shift(2).isna()).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_pricecurv_vol_30d_slope_v114_signal(closeadj):
    curv = (closeadj -2.0*closeadj.shift(5) + closeadj.shift(10)) / closeadj.replace(0,_N)
    return curv.rolling(30,min_periods=15).std(ddof=0).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_compression_breadth_slope_v115_signal(high, low, closeadj):
    r = closeadj.pct_change(); v5 = r.rolling(5).std(ddof=0); v10 = r.rolling(10).std(ddof=0)
    v20 = r.rolling(20).std(ddof=0); v40 = r.rolling(40).std(ddof=0); rng = high - low; rng_avg = rng.rolling(30,min_periods=15).mean()
    a5 = _a(high, low, closeadj, 5); a20 = _a(high, low, closeadj, 20)
    c = (v5 < v20).astype(float) + (v10 < v40).astype(float) + (rng < rng_avg).astype(float) + (a5 < a20).astype(float)
    return c.where(~v40.isna() & ~rng_avg.isna()).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_compress_streak_rank_slope_v116_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median(); cond = (v < med).astype(float).where(~med.isna())
    out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = _N; continue
        cnt = cnt + 1.0 if x > 0.5 else 0.0
        out.iat[i] = cnt
    return out.rolling(200,min_periods=100).apply(_rank_window, raw=True).diff(63).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_dir_reversals_60d_slope_v117_signal(closeadj):
    v = _v(closeadj, 20); s = np.sign(v.diff(5)); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60,min_periods=30).sum().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_ar1_residual_slope_v118_signal(closeadj):
    v = _v(closeadj, 20); rho = v.rolling(60,min_periods=30).corr(v.shift(1))
    return (v - rho * v.shift(1)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_absret_persistence_60d_slope_v119_signal(closeadj):
    ar = closeadj.pct_change().abs()
    return ar.rolling(60,min_periods=30).corr(ar.shift(1)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_skew_80d_slope_v120_signal(closeadj):
    v = _v(closeadj, 10)
    return v.rolling(80,min_periods=40).skew().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vw_volatility_ratio_slope_v121_signal(closeadj, volume):
    r = closeadj.pct_change().abs(); num = (r * volume).rolling(20).sum(); den_r = r.rolling(20).sum().replace(0,_N); den_v = volume.rolling(20).sum().replace(0,_N) / 20.0
    return (num / (den_r * den_v)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_entropy_50d_slope_v122_signal(high, low):
    rng = high - low
    def _ent(x):
        q = np.quantile(x, [0.25, 0.5, 0.75])
        buckets = np.array([(x <= q[0]).sum(), ((x > q[0]) & (x <= q[1])).sum(),
                            ((x > q[1]) & (x <= q[2])).sum(), (x > q[2]).sum()], dtype=float)
        p = buckets / buckets.sum(); p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return rng.rolling(50,min_periods=25).apply(_ent, raw=True).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_pctb_extreme_freq_30d_slope_v123_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    pctb = (closeadj - (m -2.0*sd)) / (4.0* sd).replace(0,_N); flag = ((pctb < 0.05) | (pctb > 0.95)).astype(float).where(~pctb.isna())
    return flag.rolling(30,min_periods=15).mean().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_cei_composite_slope_v124_signal(high, low, closeadj):
    a5 = _a(high, low, closeadj, 5); a40 = _a(high, low, closeadj, 40); t1 = np.tanh(a5 / a40.replace(0,_N) - 1.0)
    v = _v(closeadj, 10); mu = v.rolling(60,min_periods=30).mean(); sd = v.rolling(60,min_periods=30).std(ddof=0); z = (v - mu) / sd.replace(0,_N); t2 = np.tanh(z)
    return (t1 + t2).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_days_since_60d_vol_min_slope_v125_signal(closeadj):
    v = _v(closeadj, 20); mn = v.rolling(60,min_periods=30).min(); at_min = (v <= mn + 1e-12).astype(float).where(~mn.isna())
    out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = _N
    for i in range(len(at_min)):
        x = at_min.iat[i]
        if not np.isfinite(x):
            out.iat[i] = cnt; continue
        if x > 0.5: cnt = 0.0
        elif np.isfinite(cnt): cnt += 1.0
        out.iat[i] = cnt
    return out.clip(upper=60.0).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_days_since_60d_vol_max_slope_v126_signal(closeadj):
    v = _v(closeadj, 20); mx = v.rolling(60,min_periods=30).max(); at_max = (v >= mx - 1e-12).astype(float).where(~mx.isna())
    out = pd.Series(_N, index=closeadj.index, dtype=float); cnt = _N
    for i in range(len(at_max)):
        x = at_max.iat[i]
        if not np.isfinite(x):
            out.iat[i] = cnt; continue
        if x > 0.5: cnt = 0.0
        elif np.isfinite(cnt): cnt += 1.0
        out.iat[i] = cnt
    return out.clip(upper=60.0).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_entries_to_compression_slope_v127_signal(closeadj):
    v = _v(closeadj, 10); q = v.rolling(100,min_periods=50).quantile(0.25); flag = (v < q).astype(float).where(~q.isna())
    entries = ((flag > 0.5) & (flag.shift(1) < 0.5)).astype(float).where(~flag.shift(1).isna())
    return entries.rolling(90,min_periods=45).sum().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_exits_from_compression_slope_v128_signal(closeadj):
    v = _v(closeadj, 10); q = v.rolling(100,min_periods=50).quantile(0.25); flag = (v < q).astype(float).where(~q.isna())
    exits = ((flag < 0.5) & (flag.shift(1) > 0.5)).astype(float).where(~flag.shift(1).isna())
    return exits.rolling(90,min_periods=45).sum().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_body_to_range_30d_slope_v129_signal(open_, high, low, closeadj):
    rng = (high - low).replace(0,_N); body = (closeadj - open_).abs() / rng
    return body.rolling(30,min_periods=15).mean().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_wick_share_50d_slope_v130_signal(open_, high, low, closeadj):
    rng = (high - low).replace(0,_N); wick = (rng - (closeadj - open_).abs()) / rng
    return wick.rolling(50,min_periods=25).mean().diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_band_ratio_long_short_slope_v131_signal(closeadj):
    vs = _v(closeadj, 10); vl = _v(closeadj, 40)
    return (vl / vs.replace(0,_N) - 1.0).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_log_range_sma_diff_slope_v132_signal(high, low):
    lr = np.log(high / low.replace(0,_N)); s = lr.rolling(25).mean(); L = lr.rolling(100,min_periods=50).mean()
    return np.log(s / L.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_pct_decline_30d_slope_v133_signal(closeadj):
    v = _v(closeadj, 20)
    return ((v.shift(30) - v) / v.shift(30).replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_realized_vol_min_slope_v134_signal(closeadj):
    v = _v(closeadj, 20); mn = v.rolling(100,min_periods=50).min()
    return (mn / v.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_realized_vol_max_slope_v135_signal(closeadj):
    v = _v(closeadj, 20); mx = v.rolling(100,min_periods=50).max()
    return (mx / v.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_acceleration_slope_v136_signal(high, low):
    rng = high - low
    return ((rng - rng.shift(5)) - (rng.shift(5) - rng.shift(10))).diff(5).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_2deriv_sign_30d_slope_v137_signal(closeadj):
    v = _v(closeadj, 15)
    return np.sign(v -2.0*v.shift(10) + v.shift(20)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_signflip_count_30d_slope_v138_signal(closeadj):
    s = np.sign(closeadj.pct_change()); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30,min_periods=15).sum().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_change_consistent_slope_v139_signal(closeadj):
    v = _v(closeadj, 15); s = np.sign(v.diff(5))
    return s.rolling(30,min_periods=15).mean().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_corr_lag5_60d_slope_v140_signal(high, low):
    rng = high - low
    return rng.rolling(60,min_periods=30).corr(rng.shift(5)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_smoothness_30d_slope_v141_signal(closeadj):
    v = _v(closeadj, 10); d = v.diff(1)
    return (d.rolling(30,min_periods=15).std(ddof=0) / v.rolling(30,min_periods=15).mean().replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_ohlc_dispersion_zscore_slope_v142_signal(open_, high, low, closeadj):
    disp = pd.concat([open_, high, low, closeadj], axis=1).std(axis=1) / closeadj.replace(0,_N); mu = disp.rolling(100,min_periods=50).mean(); sd = disp.rolling(100,min_periods=50).std(ddof=0)
    return ((disp - mu) / sd.replace(0,_N)).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_regime_stability_slope_v143_signal(closeadj):
    v = _v(closeadj, 20); med = v.rolling(60,min_periods=30).median(); flag = (v > med).astype(float).where(~med.isna())
    flips = (flag != flag.shift(1)).astype(float).where(~flag.shift(1).isna() & ~flag.isna())
    return (1.0 - flips.rolling(60,min_periods=30).sum() / 60.0).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_rank_gap_slope_v144_signal(closeadj):
    v10 = _v(closeadj, 10); v40 = _v(closeadj, 40); r10 = v10.rolling(60,min_periods=30).apply(_rank_window, raw=True)
    r40 = v40.rolling(120,min_periods=60).apply(_rank_window, raw=True)
    return (r10 - r40).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_above_p80_30d_slope_v145_signal(high, low):
    rng = high - low; q = rng.rolling(120,min_periods=60).quantile(0.80); flag = (rng > q).astype(float).where(~q.isna())
    return flag.rolling(30,min_periods=15).mean().diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_range_slope_gap_slope_v146_signal(high, low):
    rng = high - low; s10 = rng.rolling(10).mean(); s40 = rng.rolling(40).mean()
    return (s10.diff(10) - s40.diff(10)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_bbw_roc_zscore_slope_v147_signal(closeadj):
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0); bbw = (4.0* sd) / m.replace(0,_N); roc = bbw / bbw.shift(5).replace(0,_N) - 1.0
    mu = roc.rolling(60,min_periods=30).mean(); sigma = roc.rolling(60,min_periods=30).std(ddof=0)
    return ((roc - mu) / sigma.replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_volgap_5_60_change_slope_v148_signal(closeadj):
    vs = _v(closeadj, 5); vl = _v(closeadj, 60); gap = vs / vl.replace(0,_N) - 1.0; mu = gap.rolling(30,min_periods=15).mean()
    return (gap - mu).diff(21).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_vol_curv_normalized_slope_v149_signal(closeadj):
    v = _v(closeadj, 20); curv = v -2.0*v.shift(10) + v.shift(20)
    return (curv / v.shift(10).replace(0,_N)).diff(10).replace(_I, _N)

def f20ce_f20_volatility_compression_expansion_composite_squeeze_slope_v150_signal(high, low, closeadj):
    a5 = _a(high, low, closeadj, 5); a40 = _a(high, low, closeadj, 40); t1 = np.arctan(-(a5 / a40.replace(0,_N) - 1.0))
    n = 20; m = closeadj.rolling(n).mean(); sd = closeadj.rolling(n).std(ddof=0)
    bbw = (4.0* sd) / m.replace(0,_N); bbw_avg = bbw.rolling(60,min_periods=30).mean(); t2 = np.arctan(-(bbw / bbw_avg.replace(0,_N) - 1.0))
    v = _v(closeadj, 10); mu = v.rolling(60,min_periods=30).mean(); sigma = v.rolling(60,min_periods=30).std(ddof=0)
    z = (v - mu) / sigma.replace(0,_N); t3 = np.arctan(-z)
    return (t1 + t2 + t3).diff(21).replace(_I, _N)


f20_volatility_compression_expansion_slope_001_150_REGISTRY = dict([
_e(f20ce_f20_volatility_compression_expansion_bb_in_kc_20d_slope_v001_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_bb_in_kc_streak_30d_slope_v002_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_squeeze_break_20d_slope_v003_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_div_min_60d_slope_v004_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_div_max_60d_slope_v005_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_rank_120d_slope_v006_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_rel_avg_252d_slope_v007_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_5_20_slope_v008_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_atr_short_long_ratio_10_50_slope_v009_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_rank_100d_slope_v010_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_decline_streak_20d_slope_v011_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_atr_rise_streak_20d_slope_v012_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_atr_pctile_low_60d_slope_v013_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_nr4_slope_v014_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_nr7_slope_v015_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_inside_bar_streak_slope_v016_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_outside_bar_streak_slope_v017_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_range_rank_50d_slope_v018_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_inside_bar_count_30d_slope_v019_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_wide_range_count_30d_slope_v020_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_vol20_slope_sign_slope_v021_signal, ["close"]),
_e(f20ce_f20_volatility_compression_expansion_vol60_slope_sign_slope_v022_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_curvature_30d_slope_v023_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_minmax_norm_60d_slope_v024_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_zscore_120d_slope_v025_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_z_below_neg1_flag_slope_v026_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_surge_5_60_slope_v027_signal, ["close"]),
_e(f20ce_f20_volatility_compression_expansion_vol_above_1p5x_30d_slope_v028_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_z_above_1_flag_slope_v029_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_days_since_squeeze_60d_slope_v030_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_days_since_expansion_60d_slope_v031_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_compression_streak_30d_slope_v032_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_post_break_expansion_mag_slope_v033_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_failed_breakout_count_60d_slope_v034_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_agree_compression_count_slope_v035_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_agree_expansion_count_slope_v036_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_during_contraction_slope_v037_signal, ["closeadj","volume"]),
_e(f20ce_f20_volatility_compression_expansion_volume_z_during_squeeze_slope_v038_signal, ["high","low","closeadj","volume"]),
_e(f20ce_f20_volatility_compression_expansion_arctan_bbw_60d_slope_v039_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_tanh_volz_60d_slope_v040_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_sigmoid_bbw_diff_slope_v041_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_oscillator_vol_long_short_slope_v042_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_squeeze_minus_expand_slope_v043_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_transition_event_signed_slope_v044_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_transition_count_120d_slope_v045_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_variance_of_vol_60d_slope_v046_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_of_vol_rank_120d_slope_v047_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_squeeze_duration_pre_break_slope_v048_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_acceleration_norm_slope_v049_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_to_close_arctan_slope_v050_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_atr_ratio_5_slope_v051_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_return_abs_skew_50d_slope_v052_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_return_abs_kurt_80d_slope_v053_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_tr_above_atr_freq_30d_slope_v054_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_atr_norm_change_slope_v055_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_volofvol_div_vol_60d_slope_v056_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_donch_width_rank_50d_slope_v057_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_donch_width_div_avg_100d_slope_v058_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_c2c_vs_hl_ratio_30d_slope_v059_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_body_size_rank_50d_slope_v060_signal, ["open","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_compress_then_expand_slope_v061_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_vs_recent_min_30d_slope_v062_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_mass_index_25d_slope_v063_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_chaikin_vol_10_slope_v064_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_chaikin_vol_30_slope_v065_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_acceleration_sign_slope_v066_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_disagreement_count_slope_v067_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_coil_score_slope_v068_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_vol_autocorr_30d_slope_v069_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_autocorr_50d_slope_v070_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_compression_roc_30d_slope_v071_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_iqr_returns_rank_80d_slope_v072_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_mad_returns_div_avg_slope_v073_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_volume_vol_corr_60d_slope_v074_signal, ["closeadj","volume"]),
_e(f20ce_f20_volatility_compression_expansion_spike_count_60d_slope_v075_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_kc_width_div_close_20d_slope_v076_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_kc_width_rank_120d_slope_v077_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_kc_vs_bbw_slope_v078_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_sqret_short_long_slope_v079_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_sqret_zscore_60d_slope_v080_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_sqret_decline_streak_20d_slope_v081_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_log_hl_sq_rank_60d_slope_v082_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_log_co_sq_short_long_slope_v083_signal, ["open","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_close_vs_kc_upper_norm_slope_v084_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_close_outside_kc_count_30d_slope_v085_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_volofrange_30d_slope_v086_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_volofrange_zscore_slope_v087_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_tr_vs_hl_ratio_20d_slope_v088_signal, ["high","low","close"]),
_e(f20ce_f20_volatility_compression_expansion_gap_jump_count_60d_slope_v089_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_regslope_40d_slope_v090_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_regslope_80d_slope_v091_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_zdist_to_min_slope_v092_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_atr_dist_to_max_60d_slope_v093_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_long_horizon_ratio_slope_v094_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_med_range_rank_80d_slope_v095_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_p10_range_rel_p90_slope_v096_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_small_range_cluster_10d_slope_v097_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_large_range_cluster_10d_slope_v098_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_up_down_vol_ratio_30d_slope_v099_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_up_minus_down_vol_z_slope_v100_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_gap_abs_30d_avg_slope_v101_signal, ["open","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_gap_zscore_60d_slope_v102_signal, ["open","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_frac_below_p25_vol_60d_slope_v103_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_frac_above_p75_vol_60d_slope_v104_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_mom_sign_short_long_slope_v105_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_pctile_cross_event_slope_v106_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_recent_vol_concentration_slope_v107_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_tailshare_60d_slope_v108_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_dist_from_252d_mean_slope_v109_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_drawdown_60d_slope_v110_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_runup_60d_slope_v111_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_3bar_contraction_slope_v112_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_3bar_expansion_slope_v113_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_pricecurv_vol_30d_slope_v114_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_compression_breadth_slope_v115_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_compress_streak_rank_slope_v116_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_dir_reversals_60d_slope_v117_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_ar1_residual_slope_v118_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_absret_persistence_60d_slope_v119_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_skew_80d_slope_v120_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vw_volatility_ratio_slope_v121_signal, ["closeadj","volume"]),
_e(f20ce_f20_volatility_compression_expansion_range_entropy_50d_slope_v122_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_pctb_extreme_freq_30d_slope_v123_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_cei_composite_slope_v124_signal, ["high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_days_since_60d_vol_min_slope_v125_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_days_since_60d_vol_max_slope_v126_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_entries_to_compression_slope_v127_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_exits_from_compression_slope_v128_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_body_to_range_30d_slope_v129_signal, ["open","high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_wick_share_50d_slope_v130_signal, ["open","high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_band_ratio_long_short_slope_v131_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_log_range_sma_diff_slope_v132_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_vol_pct_decline_30d_slope_v133_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_realized_vol_min_slope_v134_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_realized_vol_max_slope_v135_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_acceleration_slope_v136_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_vol_2deriv_sign_30d_slope_v137_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_signflip_count_30d_slope_v138_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_change_consistent_slope_v139_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_corr_lag5_60d_slope_v140_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_vol_smoothness_30d_slope_v141_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_ohlc_dispersion_zscore_slope_v142_signal, ["open","high","low","closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_regime_stability_slope_v143_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_rank_gap_slope_v144_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_range_above_p80_30d_slope_v145_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_range_slope_gap_slope_v146_signal, ["high","low"]),
_e(f20ce_f20_volatility_compression_expansion_bbw_roc_zscore_slope_v147_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_volgap_5_60_change_slope_v148_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_vol_curv_normalized_slope_v149_signal, ["closeadj"]),
_e(f20ce_f20_volatility_compression_expansion_composite_squeeze_slope_v150_signal, ["high","low","closeadj"]),
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
    for name, entry in f20_volatility_compression_expansion_slope_001_150_REGISTRY.items():
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
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"; print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
