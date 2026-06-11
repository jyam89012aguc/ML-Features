"""f27_volume_regime jerk 001-150 (2nd derivative). jerk = base - 2*base.shift(k) + base.shift(2k)."""
from __future__ import annotations
import numpy as np
import pandas as pd
def _streak(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])
def _consec_true(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5:
            c += 1
        else:
            break
    return float(c)
def _maxrun(x):
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
def _bucket(r, k):
    out = pd.Series(np.nan, index=r.index, dtype=float)
    m = r.notna()
    out[m] = np.ceil(r[m].clip(lower=1e-9) * float(k))
    return out
def _jk(b, k):
    return (b - 2.0 * b.shift(k) + b.shift(2 * k)).replace([np.inf, -np.inf], np.nan)
def f27vr_f27_volume_regime_q4_bucket_42d_jerk_v001_signal(volume):
    r = volume.rolling(42, 42).rank(pct=True); b = _bucket(r, 4)
    return _jk(b, 21)
def f27vr_f27_volume_regime_q4_bucket_minus_yesterday_252d_jerk_v002_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    return _jk(b - b.shift(1), 63)
def f27vr_f27_volume_regime_count_decile_jumps_120d_jerk_v003_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10)
    j = (b - b.shift(1)).abs(); ev = (j >= 2.0).astype(float).where(j.notna())
    return _jk(ev.rolling(120, 120).sum(), 21)
def f27vr_f27_volume_regime_dispersion_buckets_21d_jerk_v004_signal(volume):
    r = volume.rolling(63, 63).rank(pct=True); b = _bucket(r, 4)
    def _nu(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(len(np.unique(x)))
    return _jk(b.rolling(21, 21).apply(_nu, raw=True), 10)
def f27vr_f27_volume_regime_entry_event_top_d_jerk_v005_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r >= 0.9).astype(float).where(r.notna())
    e = ((s > 0.5) & (s.shift(1) <= 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e, 63)
def f27vr_f27_volume_regime_exit_event_top_q_jerk_v006_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    e = ((s <= 0.5) & (s.shift(1) > 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e, 21)
def f27vr_f27_volume_regime_any_state_flip_q4_jerk_v007_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    f = (b != b.shift(1)).astype(float).where(b.notna() & b.shift(1).notna())
    return _jk(f, 63)
def f27vr_f27_volume_regime_streak_below_med_120d_jerk_v008_signal(volume):
    med = volume.rolling(63, 63).median(); s = (volume < med).astype(float).where(med.notna())
    return _jk(s.rolling(120, 120).apply(_consec_true, raw=True), 21)
def f27vr_f27_volume_regime_multi_top_q_agree_jerk_v009_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(63, 63).rank(pct=True); r3 = volume.rolling(126, 126).rank(pct=True); r4 = volume.rolling(252, 252).rank(pct=True)
    a = (r1 >= 0.75).astype(float) + (r2 >= 0.75).astype(float) + (r3 >= 0.75).astype(float) + (r4 >= 0.75).astype(float)
    m = r1.notna() & r2.notna() & r3.notna() & r4.notna()
    return _jk(a.where(m), 63)
def f27vr_f27_volume_regime_multi_bot_q_agree_jerk_v010_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(63, 63).rank(pct=True); r3 = volume.rolling(126, 126).rank(pct=True); r4 = volume.rolling(252, 252).rank(pct=True)
    a = (r1 <= 0.25).astype(float) + (r2 <= 0.25).astype(float) + (r3 <= 0.25).astype(float) + (r4 <= 0.25).astype(float)
    m = r1.notna() & r2.notna() & r3.notna() & r4.notna()
    return _jk(a.where(m), 63)
def f27vr_f27_volume_regime_v_over_median_21d_jerk_v011_signal(volume):
    """v/median ratio (raw, not log); k=5. Different transform from v080 (log)."""
    med = volume.rolling(21, 21).median()
    return _jk(volume / med.replace(0.0, np.nan), 5)
def f27vr_f27_volume_regime_q4_bucket_diff_short_long_jerk_v012_signal(volume):
    r63 = volume.rolling(63, 63).rank(pct=True); r252 = volume.rolling(252, 252).rank(pct=True)
    return _jk(_bucket(r63, 4) - _bucket(r252, 4), 63)
def f27vr_f27_volume_regime_logv_diff_5d_jerk_v013_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return _jk(lv - lv.shift(5), 21)
def f27vr_f27_volume_regime_lag_v_corr_30d_jerk_v014_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return _jk(lv.rolling(30, 30).corr(lv.shift(1)), 10)
def f27vr_f27_volume_regime_pct_rank_189d_jerk_v015_signal(volume):
    return _jk(volume.rolling(189, 189).rank(pct=True), 63)
def f27vr_f27_volume_regime_dayssince_top_q_change_252d_jerk_v016_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    e = ((s > 0.5) & (s.shift(1) <= 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e.rolling(252, 252).apply(_streak, raw=True), 63)
def f27vr_f27_volume_regime_dayssince_bot_q_change_252d_jerk_v017_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r <= 0.25).astype(float).where(r.notna())
    e = ((s > 0.5) & (s.shift(1) <= 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e.rolling(252, 252).apply(_streak, raw=True), 63)
def f27vr_f27_volume_regime_change_count_q4_120d_jerk_v018_signal(volume):
    r = volume.rolling(63, 63).rank(pct=True); b = _bucket(r, 4)
    f = (b != b.shift(1)).astype(float).where(b.notna() & b.shift(1).notna())
    return _jk(f.rolling(120, 120).sum(), 21)
def f27vr_f27_volume_regime_change_count_top_state_252d_jerk_v019_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r >= 0.9).astype(float).where(r.notna())
    f = (s != s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(f.rolling(252, 252).sum(), 21)
def f27vr_f27_volume_regime_frac_top_q_120d_jerk_v020_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    return _jk(s.rolling(120, 120).mean(), 21)
def f27vr_f27_volume_regime_frac_bot_q_63d_jerk_v021_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); s = (r <= 0.25).astype(float).where(r.notna())
    return _jk(s.rolling(63, 63).mean(), 21)
def f27vr_f27_volume_regime_streak_top_q_120d_jerk_v022_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    return _jk(s.rolling(120, 120).apply(_consec_true, raw=True), 21)
def f27vr_f27_volume_regime_streak_bot_d_180d_jerk_v023_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r <= 0.1).astype(float).where(r.notna())
    return _jk(s.rolling(180, 180).apply(_consec_true, raw=True), 21)
def f27vr_f27_volume_regime_expand_10_60_jerk_v024_signal(volume):
    s10 = volume.rolling(10, 10).mean(); s60 = volume.rolling(60, 60).mean()
    return _jk(np.log(s10 / s60.replace(0.0, np.nan)), 10)
def f27vr_f27_volume_regime_expand_21_126_jerk_v025_signal(volume):
    s1 = volume.rolling(21, 21).mean(); s2 = volume.rolling(126, 126).mean()
    return _jk(np.log(s1 / s2.replace(0.0, np.nan)), 21)
def f27vr_f27_volume_regime_expand_5_42_jerk_v026_signal(volume):
    s1 = volume.rolling(5, 5).mean(); s2 = volume.rolling(42, 42).mean()
    return _jk(np.log(s1 / s2.replace(0.0, np.nan)), 10)
def f27vr_f27_volume_regime_volvol_30d_jerk_v027_signal(volume):
    m = volume.rolling(30, 30).mean(); s = volume.rolling(30, 30).std()
    return _jk(s / m.replace(0.0, np.nan), 10)
def f27vr_f27_volume_regime_volvol_120d_jerk_v028_signal(volume):
    m = volume.rolling(120, 120).mean(); s = volume.rolling(120, 120).std()
    return _jk(s / m.replace(0.0, np.nan), 21)
def f27vr_f27_volume_regime_spike2x_sma20_jerk_v029_signal(volume):
    m = volume.rolling(20, 20).mean()
    return _jk((volume > 2.0 * m).astype(float).where(m.notna()), 5)
def f27vr_f27_volume_regime_dayssince_spike2x_sma20_252d_jerk_v030_signal(volume):
    m = volume.rolling(20, 20).mean(); sp = (volume > 2.0 * m).astype(float).where(m.notna())
    return _jk(sp.rolling(252, 252).apply(_streak, raw=True), 63)
def f27vr_f27_volume_regime_spike_count_3x_sma50_120d_jerk_v031_signal(volume):
    m = volume.rolling(50, 50).mean(); sp = (volume > 3.0 * m).astype(float).where(m.notna())
    return _jk(sp.rolling(120, 120).sum(), 21)
def f27vr_f27_volume_regime_arctan_logv_diff_10d_jerk_v032_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan)); d = lv.diff(10); sd = d.rolling(30, 30).std()
    return _jk(np.arctan(d / sd.replace(0.0, np.nan)), 10)
def f27vr_f27_volume_regime_tanh_volvol_change_60d_jerk_v033_signal(volume):
    m30 = volume.rolling(30, 30).mean(); s30 = volume.rolling(30, 30).std(); cv30 = s30/m30.replace(0.0, np.nan)
    m120 = volume.rolling(120, 120).mean(); s120 = volume.rolling(120, 120).std(); cv120 = s120/m120.replace(0.0, np.nan)
    return _jk(np.tanh(cv30 - cv120), 21)
def f27vr_f27_volume_regime_sigmoid_rankcross_diff_jerk_v034_signal(volume):
    r21 = volume.rolling(21, 21).rank(pct=True); r63 = volume.rolling(63, 63).rank(pct=True)
    x = (r21 - r63) * 6.0
    return _jk(1.0 / (1.0 + np.exp(-x.clip(-30.0, 30.0))), 21)
def f27vr_f27_volume_regime_dv_q4_bucket_252d_jerk_v035_signal(closeadj, volume):
    dv = closeadj * volume; r = dv.rolling(252, 252).rank(pct=True)
    return _jk(_bucket(r, 4), 21)
def f27vr_f27_volume_regime_dv_entry_event_top_d_jerk_v036_signal(closeadj, volume):
    dv = closeadj * volume; r = dv.rolling(252, 252).rank(pct=True); s = (r >= 0.9).astype(float).where(r.notna())
    e = ((s > 0.5) & (s.shift(1) <= 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e, 63)
def f27vr_f27_volume_regime_dv_pricecomp_ratio_42d_jerk_v037_signal(closeadj, volume):
    dvm = (closeadj*volume).rolling(42, 42).mean(); vm = volume.rolling(42, 42).mean(); pm = closeadj.rolling(42, 42).mean()
    return _jk(np.log(dvm / (vm*pm).replace(0.0, np.nan)), 21)
def f27vr_f27_volume_regime_dv_frac_high_60d_jerk_v038_signal(closeadj, volume):
    dv = closeadj*volume; r = dv.rolling(126, 126).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    return _jk(s.rolling(60, 60).mean(), 21)
def f27vr_f27_volume_regime_dayssince_top_d_entry_252d_jerk_v039_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); s = (r >= 0.9).astype(float).where(r.notna())
    e = ((s > 0.5) & (s.shift(1) <= 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e.rolling(252, 252).apply(_streak, raw=True), 63)
def f27vr_f27_volume_regime_dayssince_bot_d_exit_252d_jerk_v040_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); s = (r <= 0.1).astype(float).where(r.notna())
    e = ((s <= 0.5) & (s.shift(1) > 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e.rolling(252, 252).apply(_streak, raw=True), 63)
def f27vr_f27_volume_regime_high_v_avg_diff_84d_jerk_v041_signal(volume):
    r = volume.rolling(84, 84).rank(pct=True)
    it = (r >= 0.75).astype(float).where(r.notna()); ib = (r <= 0.25).astype(float).where(r.notna())
    vt = (volume*it).rolling(84, 84).sum(); ct = it.rolling(84, 84).sum()
    vb = (volume*ib).rolling(84, 84).sum(); cb = ib.rolling(84, 84).sum()
    mt = vt / ct.replace(0.0, np.nan); mb = vb / cb.replace(0.0, np.nan)
    ma = volume.rolling(84, 84).mean()
    return _jk((mt - mb) / ma.replace(0.0, np.nan), 10)
def f27vr_f27_volume_regime_rank_consistency_3w_jerk_v042_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(63, 63).rank(pct=True); r3 = volume.rolling(252, 252).rank(pct=True)
    m = r1.notna() & r2.notna() & r3.notna()
    hi = ((r1>0.5)&(r2>0.5)&(r3>0.5)).astype(float); lo = ((r1<0.5)&(r2<0.5)&(r3<0.5)).astype(float)
    return _jk((hi - lo).where(m), 63)
def f27vr_f27_volume_regime_mean_abs_rank_jump_84d_jerk_v043_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); j = (r - r.shift(1)).abs()
    return _jk(j.rolling(84, 84).mean(), 21)
def f27vr_f27_volume_regime_range_rank_over_windows_jerk_v044_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(63, 63).rank(pct=True); r3 = volume.rolling(189, 189).rank(pct=True)
    mat = pd.concat([r1, r2, r3], axis=1); m = r1.notna() & r2.notna() & r3.notna()
    return _jk((mat.max(axis=1) - mat.min(axis=1)).where(m), 63)
def f27vr_f27_volume_regime_rank_std_60d_jerk_v045_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True)
    return _jk(r.rolling(60, 60).std(), 21)
def f27vr_f27_volume_regime_vol_sharpe_42d_jerk_v046_signal(volume):
    m = volume.rolling(42, 42).mean(); s = volume.rolling(42, 42).std()
    return _jk(m / s.replace(0.0, np.nan), 21)
def f27vr_f27_volume_regime_sign_expand_10_30_jerk_v047_signal(volume):
    s10 = volume.rolling(10, 10).mean(); s30 = volume.rolling(30, 30).mean()
    return _jk(np.sign(s10 - s30), 10)
def f27vr_f27_volume_regime_sign_expand_21_63_jerk_v048_signal(volume):
    s1 = volume.rolling(21, 21).mean(); s2 = volume.rolling(63, 63).mean()
    return _jk(np.sign(s1 - s2), 21)
def f27vr_f27_volume_regime_high_state_z2_jerk_v049_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan)); m = lv.rolling(60, 60).mean(); s = lv.rolling(60, 60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    return _jk((z > 2.0).astype(float).where(z.notna()), 21)
def f27vr_f27_volume_regime_low_state_zneg1_jerk_v050_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan)); m = lv.rolling(60, 60).mean(); s = lv.rolling(60, 60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    return _jk((z < -1.0).astype(float).where(z.notna()), 21)
def f27vr_f27_volume_regime_logv_skew_84d_jerk_v051_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return _jk(lv.rolling(84, 84).skew(), 21)
def f27vr_f27_volume_regime_logv_kurt_126d_jerk_v052_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return _jk(lv.rolling(126, 126).kurt(), 63)
def f27vr_f27_volume_regime_logv_iqr_84d_jerk_v053_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    q75 = lv.rolling(84, 84).quantile(0.75); q25 = lv.rolling(84, 84).quantile(0.25); med = lv.rolling(84, 84).median().abs()
    return _jk((q75 - q25) / med.replace(0.0, np.nan), 21)
def f27vr_f27_volume_regime_decile_change_rate_120d_jerk_v054_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10)
    f = (b != b.shift(1)).astype(float).where(b.notna() & b.shift(1).notna())
    return _jk(f.rolling(120, 120).sum() / 120.0, 21)
def f27vr_f27_volume_regime_markov_stay_high_252d_jerk_v055_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    ih = s > 0.5; nh = s.shift(-1) > 0.5
    both = (ih & nh).astype(float).where(s.notna() & s.shift(-1).notna())
    ch = ih.astype(float).where(s.notna() & s.shift(-1).notna())
    num = both.rolling(252, 252).sum(); den = ch.rolling(252, 252).sum()
    return _jk(num / den.replace(0.0, np.nan), 63)
def f27vr_f27_volume_regime_count_z_extreme_252d_jerk_v056_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan)); m = lv.rolling(60, 60).mean(); s = lv.rolling(60, 60).std()
    z = (lv - m) / s.replace(0.0, np.nan); e = (z.abs() > 1.5).astype(float).where(z.notna())
    return _jk(e.rolling(252, 252).sum(), 63)
def f27vr_f27_volume_regime_v_over_mad_60d_jerk_v057_signal(volume):
    med = volume.rolling(60, 60).median(); dev = (volume - med).abs(); mad = dev.rolling(60, 60).median()
    return _jk((volume - med) / mad.replace(0.0, np.nan), 21)
def f27vr_f27_volume_regime_avg_high_run_length_252d_jerk_v058_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    ci = s.rolling(252, 252).sum()
    e = ((s > 0.5) & (s.shift(1) <= 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    nr = e.rolling(252, 252).sum()
    return _jk(ci / nr.replace(0.0, np.nan), 63)
def f27vr_f27_volume_regime_logv_persistence_acf1_84d_jerk_v059_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    def _a(x):
        s = pd.Series(x)
        if s.std() == 0:
            return np.nan
        return float(s.autocorr(lag=1))
    return _jk(lv.rolling(84, 84).apply(_a, raw=False), 21)
def f27vr_f27_volume_regime_count_low_state_runs_252d_jerk_v060_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); s = (r <= 0.25).astype(float).where(r.notna())
    e = ((s > 0.5) & (s.shift(1) <= 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e.rolling(252, 252).sum(), 63)
def f27vr_f27_volume_regime_dayssince_z_pos2_252d_jerk_v061_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan)); m = lv.rolling(60, 60).mean(); s = lv.rolling(60, 60).std()
    z = (lv - m) / s.replace(0.0, np.nan); f = (z > 2.0).astype(float).where(z.notna())
    return _jk(f.rolling(252, 252).apply(_streak, raw=True), 63)
def f27vr_f27_volume_regime_entropy_quartiles_84d_jerk_v062_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); b = _bucket(r, 4)
    def _e(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True); p = counts / counts.sum(); p = p[p > 0]
        return float(-np.sum(p * np.log(p)))
    return _jk(b.rolling(84, 84).apply(_e, raw=True), 21)
def f27vr_f27_volume_regime_stickiness_q4_84d_jerk_v063_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    sm = (b == b.shift(1)).astype(float).where(b.notna() & b.shift(1).notna())
    return _jk(sm.rolling(84, 84).mean(), 21)
def f27vr_f27_volume_regime_q3_bucket_42d_jerk_v064_signal(volume):
    r = volume.rolling(42, 42).rank(pct=True)
    return _jk(_bucket(r, 3), 10)
def f27vr_f27_volume_regime_dv_streak_high_q_120d_jerk_v065_signal(closeadj, volume):
    dv = closeadj * volume; r = dv.rolling(126, 126).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    return _jk(s.rolling(120, 120).apply(_consec_true, raw=True), 21)
def f27vr_f27_volume_regime_rank_diff_21_189_jerk_v066_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(189, 189).rank(pct=True)
    return _jk(r1 - r2, 63)
def f27vr_f27_volume_regime_dayssince_rankcross_84d_jerk_v067_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(189, 189).rank(pct=True)
    s = np.sign(r1 - r2); f = (s != s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(f.rolling(84, 84).apply(_streak, raw=True), 21)
def f27vr_f27_volume_regime_v_over_max60_jerk_v068_signal(volume):
    """k=63 to be very long, max-window context."""
    mx = volume.rolling(60, 60).max()
    return _jk(np.log(volume / mx.replace(0.0, np.nan)), 63)
def f27vr_f27_volume_regime_v_over_min30_jerk_v069_signal(volume):
    mn = volume.rolling(30, 30).min()
    return _jk(np.log(volume / mn.replace(0.0, np.nan)), 21)
def f27vr_f27_volume_regime_bucket_std_84d_jerk_v070_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    return _jk(b.rolling(84, 84).std(), 21)
def f27vr_f27_volume_regime_xor_short_long_state_jerk_v071_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(252, 252).rank(pct=True)
    a = (r1 >= 0.75).astype(float); b = (r2 >= 0.75).astype(float)
    return _jk((a + b - 2.0*a*b).where(r1.notna() & r2.notna()), 63)
def f27vr_f27_volume_regime_decile_entropy_120d_jerk_v072_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10)
    def _e(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True); p = counts / counts.sum(); p = p[p > 0]
        return float(-np.sum(p * np.log(p)))
    return _jk(b.rolling(120, 120).apply(_e, raw=True), 21)
def f27vr_f27_volume_regime_max_streak_high_q_252d_jerk_v073_signal(volume):
    r = volume.rolling(126, 126).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    return _jk(s.rolling(252, 252).apply(_maxrun, raw=True), 63)
def f27vr_f27_volume_regime_mean_rank_change_signed_84d_jerk_v074_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True)
    return _jk((r - r.shift(1)).rolling(84, 84).mean(), 21)
def f27vr_f27_volume_regime_cv_rank_across_windows_jerk_v075_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(63, 63).rank(pct=True); r3 = volume.rolling(126, 126).rank(pct=True); r4 = volume.rolling(252, 252).rank(pct=True)
    mat = pd.concat([r1, r2, r3, r4], axis=1); m = r1.notna() & r2.notna() & r3.notna() & r4.notna()
    return _jk((mat.std(axis=1) / mat.mean(axis=1).replace(0.0, np.nan)).where(m), 63)
def f27vr_f27_volume_regime_sextile_bucket_84d_jerk_v076_signal(volume):
    """k=10 short-window to differ from v035 (DV q4 k=21)."""
    r = volume.rolling(84, 84).rank(pct=True); b = _bucket(r, 6)
    return _jk(b, 10)
def f27vr_f27_volume_regime_octile_change_count_60d_jerk_v077_signal(volume):
    r = volume.rolling(168, 168).rank(pct=True); b = _bucket(r, 8)
    f = (b != b.shift(1)).astype(float).where(b.notna() & b.shift(1).notna())
    return _jk(f.rolling(60, 60).sum(), 21)
def f27vr_f27_volume_regime_v_kurt_252d_jerk_v079_signal(volume):
    return _jk(volume.rolling(252, 252).kurt(), 63)
def f27vr_f27_volume_regime_sma_v_ratio_10_252_jerk_v081_signal(volume):
    s10 = volume.rolling(10, 10).mean(); s252 = volume.rolling(252, 252).mean()
    return _jk(np.log(s10 / s252.replace(0.0, np.nan)), 63)
def f27vr_f27_volume_regime_up_trans_count_q3_120d_jerk_v082_signal(volume):
    r = volume.rolling(84, 84).rank(pct=True); b = _bucket(r, 3)
    up = (b > b.shift(1)).astype(float).where(b.notna() & b.shift(1).notna())
    return _jk(up.rolling(120, 120).sum(), 21)
def f27vr_f27_volume_regime_down_trans_count_q3_120d_jerk_v083_signal(volume):
    r = volume.rolling(84, 84).rank(pct=True); b = _bucket(r, 3)
    dn = (b < b.shift(1)).astype(float).where(b.notna() & b.shift(1).notna())
    return _jk(dn.rolling(120, 120).sum(), 21)
def f27vr_f27_volume_regime_v_per_range_pctrank_84d_jerk_v084_signal(high, low, volume):
    rng = (high - low).replace(0.0, np.nan)
    return _jk((volume/rng).rolling(84, 84).rank(pct=True), 21)
def f27vr_f27_volume_regime_v_per_range_high_state_120d_jerk_v085_signal(high, low, volume):
    rng = (high - low).replace(0.0, np.nan); vpr = volume/rng; med = vpr.rolling(120, 120).median()
    s = (vpr > med).astype(float).where(med.notna())
    return _jk(s.rolling(120, 120).mean(), 21)
def f27vr_f27_volume_regime_up_v_frac_42d_jerk_v086_signal(close, volume):
    up = (close > close.shift(1)).astype(float); med = volume.rolling(42, 42).median()
    c = (up * (volume > med).astype(float)).where(med.notna())
    return _jk(c.rolling(42, 42).mean(), 21)
def f27vr_f27_volume_regime_down_v_frac_84d_jerk_v087_signal(closeadj, volume):
    dn = (closeadj < closeadj.shift(1)).astype(float); med = volume.rolling(84, 84).median()
    c = (dn * (volume > med).astype(float)).where(med.notna())
    return _jk(c.rolling(84, 84).mean(), 21)
def f27vr_f27_volume_regime_shock_pct_max60_jerk_v088_signal(volume):
    mx = volume.shift(1).rolling(60, 60).max()
    return _jk((volume > 1.5*mx).astype(float).where(mx.notna()), 21)
def f27vr_f27_volume_regime_dayssince_shock_max60_252d_jerk_v089_signal(volume):
    mx = volume.shift(1).rolling(60, 60).max(); sh = (volume > 1.5*mx).astype(float).where(mx.notna())
    return _jk(sh.rolling(252, 252).apply(_streak, raw=True), 63)
def f27vr_f27_volume_regime_bars_in_top_q_42d_jerk_v090_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    return _jk(s.rolling(42, 42).sum(), 21)
def f27vr_f27_volume_regime_bars_in_bot_q_42d_jerk_v091_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r <= 0.25).astype(float).where(r.notna())
    return _jk(s.rolling(42, 42).sum(), 21)
def f27vr_f27_volume_regime_topbot_diff_84d_jerk_v092_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); st = (r >= 0.75).astype(float).where(r.notna()); sb = (r <= 0.25).astype(float).where(r.notna())
    return _jk(st.rolling(84, 84).sum() - sb.rolling(84, 84).sum(), 21)
def f27vr_f27_volume_regime_median_crossings_60d_jerk_v093_signal(volume):
    med = volume.rolling(30, 30).median(); s = np.sign(volume - med)
    f = (s != s.shift(1)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(f.rolling(60, 60).sum(), 21)
def f27vr_f27_volume_regime_logv_acf2_60d_jerk_v094_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    def _a(x):
        s = pd.Series(x)
        if s.std() == 0:
            return np.nan
        return float(s.autocorr(lag=2))
    return _jk(lv.rolling(60, 60).apply(_a, raw=False), 21)
def f27vr_f27_volume_regime_mode_bucket_q4_60d_jerk_v095_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    def _m(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True)
        return float(vals[np.argmax(counts)])
    return _jk(b.rolling(60, 60).apply(_m, raw=True), 21)
def f27vr_f27_volume_regime_calm_state_jerk_v096_signal(volume):
    m = volume.rolling(30, 30).mean(); s = volume.rolling(30, 30).std(); cv = s / m.replace(0.0, np.nan); cvm = cv.rolling(120, 120).median()
    return _jk((cv < cvm).astype(float).where(cv.notna() & cvm.notna()), 21)
def f27vr_f27_volume_regime_streak_calm_84d_jerk_v097_signal(volume):
    m = volume.rolling(30, 30).mean(); s = volume.rolling(30, 30).std(); cv = s / m.replace(0.0, np.nan); cvm = cv.rolling(120, 120).median()
    st = (cv < cvm).astype(float).where(cv.notna() & cvm.notna())
    return _jk(st.rolling(84, 84).apply(_consec_true, raw=True), 21)
def f27vr_f27_volume_regime_dv_frac_low_42d_jerk_v098_signal(closeadj, volume):
    dv = closeadj * volume; r = dv.rolling(126, 126).rank(pct=True); s = (r <= 0.25).astype(float).where(r.notna())
    return _jk(s.rolling(42, 42).mean(), 21)
def f27vr_f27_volume_regime_dv_count_extreme_z_120d_jerk_v099_signal(closeadj, volume):
    ldv = np.log((closeadj*volume).replace(0.0, np.nan)); m = ldv.rolling(60, 60).mean(); s = ldv.rolling(60, 60).std()
    z = (ldv - m) / s.replace(0.0, np.nan); e = (z.abs() > 2.0).astype(float).where(z.notna())
    return _jk(e.rolling(120, 120).sum(), 21)
def f27vr_f27_volume_regime_bucket_skew_84d_jerk_v100_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10)
    return _jk(b.rolling(84, 84).skew(), 21)
def f27vr_f27_volume_regime_corr_rank_42_126_60d_jerk_v101_signal(volume):
    r1 = volume.rolling(42, 42).rank(pct=True); r2 = volume.rolling(126, 126).rank(pct=True)
    return _jk(r1.rolling(60, 60).corr(r2), 21)
def f27vr_f27_volume_regime_dayssince_mode_change_84d_jerk_v102_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    def _m(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        vals, counts = np.unique(x, return_counts=True)
        return float(vals[np.argmax(counts)])
    mo = b.rolling(60, 60).apply(_m, raw=True)
    f = (mo != mo.shift(1)).astype(float).where(mo.notna() & mo.shift(1).notna())
    return _jk(f.rolling(84, 84).apply(_streak, raw=True), 21)
def f27vr_f27_volume_regime_sign_rank21_minus_rank63_jerk_v103_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(63, 63).rank(pct=True)
    return _jk(np.sign(r1 - r2), 21)
def f27vr_f27_volume_regime_sign_rank63_minus_rank252_jerk_v104_signal(volume):
    r1 = volume.rolling(63, 63).rank(pct=True); r2 = volume.rolling(252, 252).rank(pct=True)
    return _jk(np.sign(r1 - r2), 63)
def f27vr_f27_volume_regime_pct_change_30d_jerk_v105_signal(volume):
    return _jk(volume / volume.shift(30).replace(0.0, np.nan) - 1.0, 21)
def f27vr_f27_volume_regime_pct_change_120d_jerk_v106_signal(volume):
    return _jk(volume / volume.shift(120).replace(0.0, np.nan) - 1.0, 63)
def f27vr_f27_volume_regime_avg_v_high_q_minus_overall_84d_jerk_v107_signal(volume):
    r = volume.rolling(84, 84).rank(pct=True); it = (r >= 0.75).astype(float).where(r.notna())
    nu = (volume*it).rolling(84, 84).sum(); de = it.rolling(84, 84).sum(); mt = nu / de.replace(0.0, np.nan)
    ma = volume.rolling(84, 84).mean()
    return _jk((mt - ma) / ma.replace(0.0, np.nan), 21)
def f27vr_f27_volume_regime_spike_freq_252d_jerk_v108_signal(volume):
    m = volume.rolling(30, 30).mean(); sp = (volume > 2.5*m).astype(float).where(m.notna())
    return _jk(sp.rolling(252, 252).sum(), 63)
def f27vr_f27_volume_regime_dayssince_q90_event_120d_jerk_v109_signal(volume):
    r = volume.rolling(60, 60).rank(pct=True); e = (r >= 0.90).astype(float).where(r.notna())
    return _jk(e.rolling(120, 120).apply(_streak, raw=True), 21)
def f27vr_f27_volume_regime_mode_share_60d_jerk_v110_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    def _ms(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        _, c = np.unique(x, return_counts=True)
        return float(np.max(c) / len(x))
    return _jk(b.rolling(60, 60).apply(_ms, raw=True), 21)
def f27vr_f27_volume_regime_lowtomed_lift_jerk_v111_signal(volume):
    """k=10 with double-shift form."""
    mn = volume.rolling(30, 30).min(); mx = volume.rolling(30, 30).max()
    nu = np.log(volume / mn.replace(0.0, np.nan)); de = np.log(mx / mn.replace(0.0, np.nan))
    return _jk(nu / de.replace(0.0, np.nan), 10)
def f27vr_f27_volume_regime_mean_bucket_jump_q4_84d_jerk_v112_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4); j = (b - b.shift(1)).abs()
    return _jk(j.rolling(84, 84).mean(), 21)
def f27vr_f27_volume_regime_rs_logv_84d_jerk_v113_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    def _rs(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        y = x - x.mean(); z = np.cumsum(y); R = z.max() - z.min(); S = x.std(ddof=0)
        if S == 0.0:
            return np.nan
        return float(R / S)
    return _jk(lv.rolling(84, 84).apply(_rs, raw=True), 21)
def f27vr_f27_volume_regime_run_length_avg_high_120d_jerk_v114_signal(volume):
    r = volume.rolling(84, 84).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna()); ci = s.rolling(120, 120).sum()
    e = ((s > 0.5) & (s.shift(1) <= 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    nr = e.rolling(120, 120).sum()
    return _jk(ci / nr.replace(0.0, np.nan), 21)
def f27vr_f27_volume_regime_max_bucket_jump_84d_jerk_v115_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10); j = (b - b.shift(1)).abs()
    return _jk(j.rolling(84, 84).max(), 21)
def f27vr_f27_volume_regime_window_same_decile_count_jerk_v116_signal(volume):
    r1 = volume.rolling(63, 63).rank(pct=True); r2 = volume.rolling(126, 126).rank(pct=True); r3 = volume.rolling(252, 252).rank(pct=True)
    b1 = np.ceil(r1.where(r1.notna()).clip(lower=1e-9) * 10.0); b2 = np.ceil(r2.where(r2.notna()).clip(lower=1e-9) * 10.0); b3 = np.ceil(r3.where(r3.notna()).clip(lower=1e-9) * 10.0)
    agg = ((b1 == b2).astype(float) + (b2 == b3).astype(float) + (b1 == b3).astype(float))
    m = r1.notna() & r2.notna() & r3.notna()
    return _jk(agg.where(m), 63)
def f27vr_f27_volume_regime_streak_below_sma60_120d_jerk_v117_signal(volume):
    m = volume.rolling(60, 60).mean(); s = (volume < m).astype(float).where(m.notna())
    return _jk(s.rolling(120, 120).apply(_consec_true, raw=True), 21)
def f27vr_f27_volume_regime_streak_above_sma120_180d_jerk_v118_signal(volume):
    m = volume.rolling(120, 120).mean(); s = (volume > m).astype(float).where(m.notna())
    return _jk(s.rolling(180, 180).apply(_consec_true, raw=True), 63)
def f27vr_f27_volume_regime_count_ge_3_horizons_high_jerk_v119_signal(volume):
    r1 = volume.rolling(21, 21).rank(pct=True); r2 = volume.rolling(63, 63).rank(pct=True); r3 = volume.rolling(126, 126).rank(pct=True); r4 = volume.rolling(252, 252).rank(pct=True)
    c = ((r1>=0.6).astype(float)+(r2>=0.6).astype(float)+(r3>=0.6).astype(float)+(r4>=0.6).astype(float))
    m = r1.notna() & r2.notna() & r3.notna() & r4.notna()
    return _jk((c >= 3.0).astype(float).where(m), 63)
def f27vr_f27_volume_regime_v_minus_median_z_42d_jerk_v120_signal(volume):
    med = volume.rolling(60, 60).median(); q75 = volume.rolling(60, 60).quantile(0.75); q25 = volume.rolling(60, 60).quantile(0.25); iqr = q75 - q25
    return _jk(((volume - med) / iqr.replace(0.0, np.nan)).rolling(42, 42).mean(), 21)
def f27vr_f27_volume_regime_sign_v_sma100_jerk_v121_signal(volume):
    m = volume.rolling(100, 100).mean()
    return _jk(np.sign(volume - m), 21)
def f27vr_f27_volume_regime_sign_v_sma15_jerk_v122_signal(volume):
    m = volume.rolling(15, 15).mean()
    return _jk(np.sign(volume - m), 5)
def f27vr_f27_volume_regime_volvol_of_volvol_120d_jerk_v123_signal(volume):
    m = volume.rolling(30, 30).mean(); s = volume.rolling(30, 30).std(); cv = s / m.replace(0.0, np.nan)
    return _jk(cv.rolling(120, 120).std(), 21)
def f27vr_f27_volume_regime_regslope_bucket_q4_84d_jerk_v124_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    def _sl(x):
        n = len(x); t = np.arange(n, dtype=float); mt = t.mean(); mx = x.mean()
        cv = np.sum((t-mt)*(x-mx)); vt = np.sum((t-mt)**2)
        if vt == 0.0:
            return np.nan
        return float(cv / vt)
    return _jk(b.rolling(84, 84).apply(_sl, raw=True), 21)
def f27vr_f27_volume_regime_v_to_max_dist_index_42d_jerk_v125_signal(volume):
    def _ax(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(len(x)-1-int(np.argmax(x)))
    return _jk(volume.rolling(42, 42).apply(_ax, raw=True), 21)
def f27vr_f27_volume_regime_v_to_min_dist_index_84d_jerk_v126_signal(volume):
    def _an(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(len(x)-1-int(np.argmin(x)))
    return _jk(volume.rolling(84, 84).apply(_an, raw=True), 21)
def f27vr_f27_volume_regime_stickiness_decile_30d_jerk_v127_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10)
    sm = (b == b.shift(5)).astype(float).where(b.notna() & b.shift(5).notna())
    return _jk(sm.rolling(30, 30).mean(), 10)
def f27vr_f27_volume_regime_logv_accel_5_5_jerk_v128_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return _jk(lv.diff(5).diff(5), 5)
def f27vr_f27_volume_regime_sign_logv_accel_10_10_jerk_v129_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    return _jk(np.sign(lv.diff(10).diff(10)), 10)
def f27vr_f27_volume_regime_volvol_short_minus_long_jerk_v130_signal(volume):
    m1 = volume.rolling(30, 30).mean(); s1 = volume.rolling(30, 30).std(); cv1 = s1/m1.replace(0.0, np.nan)
    m2 = volume.rolling(120, 120).mean(); s2 = volume.rolling(120, 120).std(); cv2 = s2/m2.replace(0.0, np.nan)
    return _jk(cv1 - cv2, 63)
def f27vr_f27_volume_regime_dv_exit_event_top_q_jerk_v131_signal(closeadj, volume):
    dv = closeadj * volume; r = dv.rolling(126, 126).rank(pct=True); s = (r >= 0.75).astype(float).where(r.notna())
    e = ((s <= 0.5) & (s.shift(1) > 0.5)).astype(float).where(s.notna() & s.shift(1).notna())
    return _jk(e, 21)
def f27vr_f27_volume_regime_dv_dayssince_low_state_jerk_v132_signal(closeadj, volume):
    dv = closeadj * volume; r = dv.rolling(126, 126).rank(pct=True); e = (r <= 0.1).astype(float).where(r.notna())
    return _jk(e.rolling(252, 252).apply(_streak, raw=True), 63)
def f27vr_f27_volume_regime_bucket_acf1_120d_jerk_v133_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10)
    def _a(x):
        s = pd.Series(x)
        if s.std() == 0:
            return np.nan
        return float(s.autocorr(lag=1))
    return _jk(b.rolling(120, 120).apply(_a, raw=False), 21)
def f27vr_f27_volume_regime_v_drawdown_from_max252_jerk_v134_signal(volume):
    """k=21 to differ from v015 (k=63 jerk on rank189)."""
    mx = volume.rolling(252, 252).max()
    return _jk(np.log(volume / mx.replace(0.0, np.nan)), 21)
def f27vr_f27_volume_regime_bracket_z_logv_60d_jerk_v135_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan)); m = lv.rolling(60, 60).mean(); s = lv.rolling(60, 60).std()
    z = (lv - m) / s.replace(0.0, np.nan)
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    mz = z.notna(); zz = z[mz]
    cls = pd.Series(0.0, index=zz.index, dtype=float)
    cls[zz <= -2.0] = -2.0; cls[(zz > -2.0) & (zz <= -1.0)] = -1.0
    cls[(zz >= 1.0) & (zz < 2.0)] = 1.0; cls[zz >= 2.0] = 2.0
    out[mz] = cls
    return _jk(out, 21)
def f27vr_f27_volume_regime_std_over_median_60d_jerk_v136_signal(volume):
    s = volume.rolling(60, 60).std(); med = volume.rolling(60, 60).median()
    return _jk(s / med.replace(0.0, np.nan), 21)
def f27vr_f27_volume_regime_count_top20_84d_jerk_v137_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r >= 0.80).astype(float).where(r.notna())
    return _jk(s.rolling(84, 84).sum(), 21)
def f27vr_f27_volume_regime_logv_winsor_over_mean_120d_jerk_v138_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan))
    def _w(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        lo = np.quantile(x, 0.05); hi = np.quantile(x, 0.95)
        return float(np.mean(np.clip(x, lo, hi)))
    return _jk(lv.rolling(120, 120).apply(_w, raw=True) - lv.rolling(120, 120).mean(), 63)
def f27vr_f27_volume_regime_top_decile_freq_252d_jerk_v139_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); s = (r >= 0.9).astype(float).where(r.notna())
    return _jk(s.rolling(252, 252).mean(), 63)
def f27vr_f27_volume_regime_signflip_v_sma_42d_jerk_v140_signal(volume):
    m = volume.rolling(21, 21).mean(); sg = np.sign(volume - m)
    f = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna())
    return _jk(f.rolling(42, 42).sum() / 42.0, 21)
def f27vr_f27_volume_regime_weighted_avg_bucket_q4_60d_jerk_v141_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    w = np.arange(1, 61, dtype=float); w /= w.sum()
    def _wm(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(np.dot(x, w))
    return _jk(b.rolling(60, 60).apply(_wm, raw=True), 21)
def f27vr_f27_volume_regime_bucket_var_short_over_long_jerk_v143_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 4)
    v1 = b.rolling(30, 30).var(); v2 = b.rolling(120, 120).var()
    return _jk(v1 / v2.replace(0.0, np.nan), 21)
def f27vr_f27_volume_regime_bucket_freq_std_120d_jerk_v144_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10)
    def _fs(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        _, c = np.unique(x, return_counts=True)
        return float(np.std(c))
    return _jk(b.rolling(120, 120).apply(_fs, raw=True), 63)
def f27vr_f27_volume_regime_distinct_deciles_60d_jerk_v145_signal(volume):
    r = volume.rolling(252, 252).rank(pct=True); b = _bucket(r, 10)
    def _nu(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        return float(len(np.unique(x)))
    return _jk(b.rolling(60, 60).apply(_nu, raw=True), 21)
def f27vr_f27_volume_regime_quiet_60d_streak_jerk_v146_signal(volume):
    r = volume.rolling(60, 60).rank(pct=True); s = (r <= 0.3).astype(float).where(r.notna())
    return _jk(s.rolling(60, 60).apply(_consec_true, raw=True), 21)
def f27vr_f27_volume_regime_dv_shock_3x_sma40_jerk_v147_signal(closeadj, volume):
    dv = closeadj * volume; m = dv.rolling(40, 40).mean()
    return _jk((dv > 3.0*m).astype(float).where(m.notna()), 21)
def f27vr_f27_volume_regime_rank_regslope_60d_jerk_v148_signal(volume):
    r = volume.rolling(84, 84).rank(pct=True)
    def _sl(x):
        n = len(x); t = np.arange(n, dtype=float); mt = t.mean(); mx = x.mean()
        cv = np.sum((t-mt)*(x-mx)); vt = np.sum((t-mt)**2)
        if vt == 0.0:
            return np.nan
        return float(cv / vt)
    return _jk(r.rolling(60, 60).apply(_sl, raw=True), 21)
def f27vr_f27_volume_regime_frac_abszgt1_120d_jerk_v149_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan)); m = lv.rolling(60, 60).mean(); s = lv.rolling(60, 60).std()
    z = (lv - m) / s.replace(0.0, np.nan); st = (z.abs() > 1.0).astype(float).where(z.notna())
    return _jk(st.rolling(120, 120).mean(), 21)
def f27vr_f27_volume_regime_big_bucket_leap_count_42d_jerk_v150_signal(volume):
    r = volume.rolling(84, 84).rank(pct=True); b = _bucket(r, 3); d = (b - b.shift(1)).abs()
    lp = (d == 2.0).astype(float).where(d.notna())
    return _jk(lp.rolling(42, 42).sum(), 21)
f27_volume_regime_jerk_001_150_REGISTRY = {
    "f27vr_f27_volume_regime_q4_bucket_42d_jerk_v001_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_q4_bucket_42d_jerk_v001_signal},
    "f27vr_f27_volume_regime_q4_bucket_minus_yesterday_252d_jerk_v002_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_q4_bucket_minus_yesterday_252d_jerk_v002_signal},
    "f27vr_f27_volume_regime_count_decile_jumps_120d_jerk_v003_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_decile_jumps_120d_jerk_v003_signal},
    "f27vr_f27_volume_regime_dispersion_buckets_21d_jerk_v004_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dispersion_buckets_21d_jerk_v004_signal},
    "f27vr_f27_volume_regime_entry_event_top_d_jerk_v005_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_entry_event_top_d_jerk_v005_signal},
    "f27vr_f27_volume_regime_exit_event_top_q_jerk_v006_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_exit_event_top_q_jerk_v006_signal},
    "f27vr_f27_volume_regime_any_state_flip_q4_jerk_v007_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_any_state_flip_q4_jerk_v007_signal},
    "f27vr_f27_volume_regime_streak_below_med_120d_jerk_v008_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_below_med_120d_jerk_v008_signal},
    "f27vr_f27_volume_regime_multi_top_q_agree_jerk_v009_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_multi_top_q_agree_jerk_v009_signal},
    "f27vr_f27_volume_regime_multi_bot_q_agree_jerk_v010_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_multi_bot_q_agree_jerk_v010_signal},
    "f27vr_f27_volume_regime_v_over_median_21d_jerk_v011_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_over_median_21d_jerk_v011_signal},
    "f27vr_f27_volume_regime_q4_bucket_diff_short_long_jerk_v012_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_q4_bucket_diff_short_long_jerk_v012_signal},
    "f27vr_f27_volume_regime_logv_diff_5d_jerk_v013_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_diff_5d_jerk_v013_signal},
    "f27vr_f27_volume_regime_lag_v_corr_30d_jerk_v014_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_lag_v_corr_30d_jerk_v014_signal},
    "f27vr_f27_volume_regime_pct_rank_189d_jerk_v015_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_pct_rank_189d_jerk_v015_signal},
    "f27vr_f27_volume_regime_dayssince_top_q_change_252d_jerk_v016_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_top_q_change_252d_jerk_v016_signal},
    "f27vr_f27_volume_regime_dayssince_bot_q_change_252d_jerk_v017_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_bot_q_change_252d_jerk_v017_signal},
    "f27vr_f27_volume_regime_change_count_q4_120d_jerk_v018_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_change_count_q4_120d_jerk_v018_signal},
    "f27vr_f27_volume_regime_change_count_top_state_252d_jerk_v019_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_change_count_top_state_252d_jerk_v019_signal},
    "f27vr_f27_volume_regime_frac_top_q_120d_jerk_v020_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_frac_top_q_120d_jerk_v020_signal},
    "f27vr_f27_volume_regime_frac_bot_q_63d_jerk_v021_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_frac_bot_q_63d_jerk_v021_signal},
    "f27vr_f27_volume_regime_streak_top_q_120d_jerk_v022_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_top_q_120d_jerk_v022_signal},
    "f27vr_f27_volume_regime_streak_bot_d_180d_jerk_v023_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_bot_d_180d_jerk_v023_signal},
    "f27vr_f27_volume_regime_expand_10_60_jerk_v024_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_expand_10_60_jerk_v024_signal},
    "f27vr_f27_volume_regime_expand_21_126_jerk_v025_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_expand_21_126_jerk_v025_signal},
    "f27vr_f27_volume_regime_expand_5_42_jerk_v026_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_expand_5_42_jerk_v026_signal},
    "f27vr_f27_volume_regime_volvol_30d_jerk_v027_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_volvol_30d_jerk_v027_signal},
    "f27vr_f27_volume_regime_volvol_120d_jerk_v028_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_volvol_120d_jerk_v028_signal},
    "f27vr_f27_volume_regime_spike2x_sma20_jerk_v029_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_spike2x_sma20_jerk_v029_signal},
    "f27vr_f27_volume_regime_dayssince_spike2x_sma20_252d_jerk_v030_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_spike2x_sma20_252d_jerk_v030_signal},
    "f27vr_f27_volume_regime_spike_count_3x_sma50_120d_jerk_v031_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_spike_count_3x_sma50_120d_jerk_v031_signal},
    "f27vr_f27_volume_regime_arctan_logv_diff_10d_jerk_v032_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_arctan_logv_diff_10d_jerk_v032_signal},
    "f27vr_f27_volume_regime_tanh_volvol_change_60d_jerk_v033_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_tanh_volvol_change_60d_jerk_v033_signal},
    "f27vr_f27_volume_regime_sigmoid_rankcross_diff_jerk_v034_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sigmoid_rankcross_diff_jerk_v034_signal},
    "f27vr_f27_volume_regime_dv_q4_bucket_252d_jerk_v035_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_q4_bucket_252d_jerk_v035_signal},
    "f27vr_f27_volume_regime_dv_entry_event_top_d_jerk_v036_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_entry_event_top_d_jerk_v036_signal},
    "f27vr_f27_volume_regime_dv_pricecomp_ratio_42d_jerk_v037_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_pricecomp_ratio_42d_jerk_v037_signal},
    "f27vr_f27_volume_regime_dv_frac_high_60d_jerk_v038_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_frac_high_60d_jerk_v038_signal},
    "f27vr_f27_volume_regime_dayssince_top_d_entry_252d_jerk_v039_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_top_d_entry_252d_jerk_v039_signal},
    "f27vr_f27_volume_regime_dayssince_bot_d_exit_252d_jerk_v040_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_bot_d_exit_252d_jerk_v040_signal},
    "f27vr_f27_volume_regime_high_v_avg_diff_84d_jerk_v041_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_high_v_avg_diff_84d_jerk_v041_signal},
    "f27vr_f27_volume_regime_rank_consistency_3w_jerk_v042_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rank_consistency_3w_jerk_v042_signal},
    "f27vr_f27_volume_regime_mean_abs_rank_jump_84d_jerk_v043_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mean_abs_rank_jump_84d_jerk_v043_signal},
    "f27vr_f27_volume_regime_range_rank_over_windows_jerk_v044_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_range_rank_over_windows_jerk_v044_signal},
    "f27vr_f27_volume_regime_rank_std_60d_jerk_v045_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rank_std_60d_jerk_v045_signal},
    "f27vr_f27_volume_regime_vol_sharpe_42d_jerk_v046_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_vol_sharpe_42d_jerk_v046_signal},
    "f27vr_f27_volume_regime_sign_expand_10_30_jerk_v047_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_expand_10_30_jerk_v047_signal},
    "f27vr_f27_volume_regime_sign_expand_21_63_jerk_v048_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_expand_21_63_jerk_v048_signal},
    "f27vr_f27_volume_regime_high_state_z2_jerk_v049_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_high_state_z2_jerk_v049_signal},
    "f27vr_f27_volume_regime_low_state_zneg1_jerk_v050_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_low_state_zneg1_jerk_v050_signal},
    "f27vr_f27_volume_regime_logv_skew_84d_jerk_v051_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_skew_84d_jerk_v051_signal},
    "f27vr_f27_volume_regime_logv_kurt_126d_jerk_v052_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_kurt_126d_jerk_v052_signal},
    "f27vr_f27_volume_regime_logv_iqr_84d_jerk_v053_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_iqr_84d_jerk_v053_signal},
    "f27vr_f27_volume_regime_decile_change_rate_120d_jerk_v054_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_decile_change_rate_120d_jerk_v054_signal},
    "f27vr_f27_volume_regime_markov_stay_high_252d_jerk_v055_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_markov_stay_high_252d_jerk_v055_signal},
    "f27vr_f27_volume_regime_count_z_extreme_252d_jerk_v056_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_z_extreme_252d_jerk_v056_signal},
    "f27vr_f27_volume_regime_v_over_mad_60d_jerk_v057_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_over_mad_60d_jerk_v057_signal},
    "f27vr_f27_volume_regime_avg_high_run_length_252d_jerk_v058_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_avg_high_run_length_252d_jerk_v058_signal},
    "f27vr_f27_volume_regime_logv_persistence_acf1_84d_jerk_v059_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_persistence_acf1_84d_jerk_v059_signal},
    "f27vr_f27_volume_regime_count_low_state_runs_252d_jerk_v060_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_low_state_runs_252d_jerk_v060_signal},
    "f27vr_f27_volume_regime_dayssince_z_pos2_252d_jerk_v061_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_z_pos2_252d_jerk_v061_signal},
    "f27vr_f27_volume_regime_entropy_quartiles_84d_jerk_v062_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_entropy_quartiles_84d_jerk_v062_signal},
    "f27vr_f27_volume_regime_stickiness_q4_84d_jerk_v063_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_stickiness_q4_84d_jerk_v063_signal},
    "f27vr_f27_volume_regime_q3_bucket_42d_jerk_v064_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_q3_bucket_42d_jerk_v064_signal},
    "f27vr_f27_volume_regime_dv_streak_high_q_120d_jerk_v065_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_streak_high_q_120d_jerk_v065_signal},
    "f27vr_f27_volume_regime_rank_diff_21_189_jerk_v066_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rank_diff_21_189_jerk_v066_signal},
    "f27vr_f27_volume_regime_dayssince_rankcross_84d_jerk_v067_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_rankcross_84d_jerk_v067_signal},
    "f27vr_f27_volume_regime_v_over_max60_jerk_v068_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_over_max60_jerk_v068_signal},
    "f27vr_f27_volume_regime_v_over_min30_jerk_v069_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_over_min30_jerk_v069_signal},
    "f27vr_f27_volume_regime_bucket_std_84d_jerk_v070_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_std_84d_jerk_v070_signal},
    "f27vr_f27_volume_regime_xor_short_long_state_jerk_v071_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_xor_short_long_state_jerk_v071_signal},
    "f27vr_f27_volume_regime_decile_entropy_120d_jerk_v072_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_decile_entropy_120d_jerk_v072_signal},
    "f27vr_f27_volume_regime_max_streak_high_q_252d_jerk_v073_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_max_streak_high_q_252d_jerk_v073_signal},
    "f27vr_f27_volume_regime_mean_rank_change_signed_84d_jerk_v074_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mean_rank_change_signed_84d_jerk_v074_signal},
    "f27vr_f27_volume_regime_cv_rank_across_windows_jerk_v075_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_cv_rank_across_windows_jerk_v075_signal},
    "f27vr_f27_volume_regime_sextile_bucket_84d_jerk_v076_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sextile_bucket_84d_jerk_v076_signal},
    "f27vr_f27_volume_regime_octile_change_count_60d_jerk_v077_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_octile_change_count_60d_jerk_v077_signal},
    "f27vr_f27_volume_regime_v_kurt_252d_jerk_v079_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_kurt_252d_jerk_v079_signal},
    "f27vr_f27_volume_regime_sma_v_ratio_10_252_jerk_v081_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sma_v_ratio_10_252_jerk_v081_signal},
    "f27vr_f27_volume_regime_up_trans_count_q3_120d_jerk_v082_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_up_trans_count_q3_120d_jerk_v082_signal},
    "f27vr_f27_volume_regime_down_trans_count_q3_120d_jerk_v083_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_down_trans_count_q3_120d_jerk_v083_signal},
    "f27vr_f27_volume_regime_v_per_range_pctrank_84d_jerk_v084_signal": {"inputs": ["high", "low", "volume"], "func": f27vr_f27_volume_regime_v_per_range_pctrank_84d_jerk_v084_signal},
    "f27vr_f27_volume_regime_v_per_range_high_state_120d_jerk_v085_signal": {"inputs": ["high", "low", "volume"], "func": f27vr_f27_volume_regime_v_per_range_high_state_120d_jerk_v085_signal},
    "f27vr_f27_volume_regime_up_v_frac_42d_jerk_v086_signal": {"inputs": ["close", "volume"], "func": f27vr_f27_volume_regime_up_v_frac_42d_jerk_v086_signal},
    "f27vr_f27_volume_regime_down_v_frac_84d_jerk_v087_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_down_v_frac_84d_jerk_v087_signal},
    "f27vr_f27_volume_regime_shock_pct_max60_jerk_v088_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_shock_pct_max60_jerk_v088_signal},
    "f27vr_f27_volume_regime_dayssince_shock_max60_252d_jerk_v089_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_shock_max60_252d_jerk_v089_signal},
    "f27vr_f27_volume_regime_bars_in_top_q_42d_jerk_v090_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bars_in_top_q_42d_jerk_v090_signal},
    "f27vr_f27_volume_regime_bars_in_bot_q_42d_jerk_v091_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bars_in_bot_q_42d_jerk_v091_signal},
    "f27vr_f27_volume_regime_topbot_diff_84d_jerk_v092_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_topbot_diff_84d_jerk_v092_signal},
    "f27vr_f27_volume_regime_median_crossings_60d_jerk_v093_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_median_crossings_60d_jerk_v093_signal},
    "f27vr_f27_volume_regime_logv_acf2_60d_jerk_v094_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_acf2_60d_jerk_v094_signal},
    "f27vr_f27_volume_regime_mode_bucket_q4_60d_jerk_v095_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mode_bucket_q4_60d_jerk_v095_signal},
    "f27vr_f27_volume_regime_calm_state_jerk_v096_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_calm_state_jerk_v096_signal},
    "f27vr_f27_volume_regime_streak_calm_84d_jerk_v097_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_calm_84d_jerk_v097_signal},
    "f27vr_f27_volume_regime_dv_frac_low_42d_jerk_v098_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_frac_low_42d_jerk_v098_signal},
    "f27vr_f27_volume_regime_dv_count_extreme_z_120d_jerk_v099_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_count_extreme_z_120d_jerk_v099_signal},
    "f27vr_f27_volume_regime_bucket_skew_84d_jerk_v100_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_skew_84d_jerk_v100_signal},
    "f27vr_f27_volume_regime_corr_rank_42_126_60d_jerk_v101_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_corr_rank_42_126_60d_jerk_v101_signal},
    "f27vr_f27_volume_regime_dayssince_mode_change_84d_jerk_v102_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_mode_change_84d_jerk_v102_signal},
    "f27vr_f27_volume_regime_sign_rank21_minus_rank63_jerk_v103_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_rank21_minus_rank63_jerk_v103_signal},
    "f27vr_f27_volume_regime_sign_rank63_minus_rank252_jerk_v104_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_rank63_minus_rank252_jerk_v104_signal},
    "f27vr_f27_volume_regime_pct_change_30d_jerk_v105_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_pct_change_30d_jerk_v105_signal},
    "f27vr_f27_volume_regime_pct_change_120d_jerk_v106_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_pct_change_120d_jerk_v106_signal},
    "f27vr_f27_volume_regime_avg_v_high_q_minus_overall_84d_jerk_v107_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_avg_v_high_q_minus_overall_84d_jerk_v107_signal},
    "f27vr_f27_volume_regime_spike_freq_252d_jerk_v108_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_spike_freq_252d_jerk_v108_signal},
    "f27vr_f27_volume_regime_dayssince_q90_event_120d_jerk_v109_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_dayssince_q90_event_120d_jerk_v109_signal},
    "f27vr_f27_volume_regime_mode_share_60d_jerk_v110_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mode_share_60d_jerk_v110_signal},
    "f27vr_f27_volume_regime_lowtomed_lift_jerk_v111_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_lowtomed_lift_jerk_v111_signal},
    "f27vr_f27_volume_regime_mean_bucket_jump_q4_84d_jerk_v112_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_mean_bucket_jump_q4_84d_jerk_v112_signal},
    "f27vr_f27_volume_regime_rs_logv_84d_jerk_v113_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rs_logv_84d_jerk_v113_signal},
    "f27vr_f27_volume_regime_run_length_avg_high_120d_jerk_v114_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_run_length_avg_high_120d_jerk_v114_signal},
    "f27vr_f27_volume_regime_max_bucket_jump_84d_jerk_v115_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_max_bucket_jump_84d_jerk_v115_signal},
    "f27vr_f27_volume_regime_window_same_decile_count_jerk_v116_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_window_same_decile_count_jerk_v116_signal},
    "f27vr_f27_volume_regime_streak_below_sma60_120d_jerk_v117_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_below_sma60_120d_jerk_v117_signal},
    "f27vr_f27_volume_regime_streak_above_sma120_180d_jerk_v118_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_streak_above_sma120_180d_jerk_v118_signal},
    "f27vr_f27_volume_regime_count_ge_3_horizons_high_jerk_v119_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_ge_3_horizons_high_jerk_v119_signal},
    "f27vr_f27_volume_regime_v_minus_median_z_42d_jerk_v120_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_minus_median_z_42d_jerk_v120_signal},
    "f27vr_f27_volume_regime_sign_v_sma100_jerk_v121_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_v_sma100_jerk_v121_signal},
    "f27vr_f27_volume_regime_sign_v_sma15_jerk_v122_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_v_sma15_jerk_v122_signal},
    "f27vr_f27_volume_regime_volvol_of_volvol_120d_jerk_v123_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_volvol_of_volvol_120d_jerk_v123_signal},
    "f27vr_f27_volume_regime_regslope_bucket_q4_84d_jerk_v124_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_regslope_bucket_q4_84d_jerk_v124_signal},
    "f27vr_f27_volume_regime_v_to_max_dist_index_42d_jerk_v125_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_to_max_dist_index_42d_jerk_v125_signal},
    "f27vr_f27_volume_regime_v_to_min_dist_index_84d_jerk_v126_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_to_min_dist_index_84d_jerk_v126_signal},
    "f27vr_f27_volume_regime_stickiness_decile_30d_jerk_v127_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_stickiness_decile_30d_jerk_v127_signal},
    "f27vr_f27_volume_regime_logv_accel_5_5_jerk_v128_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_accel_5_5_jerk_v128_signal},
    "f27vr_f27_volume_regime_sign_logv_accel_10_10_jerk_v129_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_sign_logv_accel_10_10_jerk_v129_signal},
    "f27vr_f27_volume_regime_volvol_short_minus_long_jerk_v130_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_volvol_short_minus_long_jerk_v130_signal},
    "f27vr_f27_volume_regime_dv_exit_event_top_q_jerk_v131_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_exit_event_top_q_jerk_v131_signal},
    "f27vr_f27_volume_regime_dv_dayssince_low_state_jerk_v132_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_dayssince_low_state_jerk_v132_signal},
    "f27vr_f27_volume_regime_bucket_acf1_120d_jerk_v133_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_acf1_120d_jerk_v133_signal},
    "f27vr_f27_volume_regime_v_drawdown_from_max252_jerk_v134_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_v_drawdown_from_max252_jerk_v134_signal},
    "f27vr_f27_volume_regime_bracket_z_logv_60d_jerk_v135_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bracket_z_logv_60d_jerk_v135_signal},
    "f27vr_f27_volume_regime_std_over_median_60d_jerk_v136_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_std_over_median_60d_jerk_v136_signal},
    "f27vr_f27_volume_regime_count_top20_84d_jerk_v137_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_count_top20_84d_jerk_v137_signal},
    "f27vr_f27_volume_regime_logv_winsor_over_mean_120d_jerk_v138_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_logv_winsor_over_mean_120d_jerk_v138_signal},
    "f27vr_f27_volume_regime_top_decile_freq_252d_jerk_v139_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_top_decile_freq_252d_jerk_v139_signal},
    "f27vr_f27_volume_regime_signflip_v_sma_42d_jerk_v140_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_signflip_v_sma_42d_jerk_v140_signal},
    "f27vr_f27_volume_regime_weighted_avg_bucket_q4_60d_jerk_v141_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_weighted_avg_bucket_q4_60d_jerk_v141_signal},
    "f27vr_f27_volume_regime_bucket_var_short_over_long_jerk_v143_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_var_short_over_long_jerk_v143_signal},
    "f27vr_f27_volume_regime_bucket_freq_std_120d_jerk_v144_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_bucket_freq_std_120d_jerk_v144_signal},
    "f27vr_f27_volume_regime_distinct_deciles_60d_jerk_v145_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_distinct_deciles_60d_jerk_v145_signal},
    "f27vr_f27_volume_regime_quiet_60d_streak_jerk_v146_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_quiet_60d_streak_jerk_v146_signal},
    "f27vr_f27_volume_regime_dv_shock_3x_sma40_jerk_v147_signal": {"inputs": ["closeadj", "volume"], "func": f27vr_f27_volume_regime_dv_shock_3x_sma40_jerk_v147_signal},
    "f27vr_f27_volume_regime_rank_regslope_60d_jerk_v148_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_rank_regslope_60d_jerk_v148_signal},
    "f27vr_f27_volume_regime_frac_abszgt1_120d_jerk_v149_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_frac_abszgt1_120d_jerk_v149_signal},
    "f27vr_f27_volume_regime_big_bucket_leap_count_42d_jerk_v150_signal": {"inputs": ["volume"], "func": f27vr_f27_volume_regime_big_bucket_leap_count_42d_jerk_v150_signal},
}
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
    for name, entry in f27_volume_regime_jerk_001_150_REGISTRY.items():
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
