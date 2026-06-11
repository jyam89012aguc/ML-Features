"""f23 OBV-family slopes 001-150. base.diff(k) per ROC bracket."""
from __future__ import annotations

import numpy as np
import pandas as pd
def _streak_consec(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5:
            c += 1
        else:
            break
    return float(c)
def _streak_days_since(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])
def _obv(c, v):
    return (np.sign(c.diff()) * v).cumsum()
def _adl(h, l, c, v):
    return (((c - l) - (h - c)) / (h - l).replace(0.0, np.nan) * v).cumsum()
def _pvt(c, v):
    return (c.pct_change() * v).cumsum()
def _kvo(h, l, c, v):
    tp = (h + l + c) / 3.0
    vf = v * np.sign(tp.diff())
    return vf.ewm(span=34, adjust=False, min_periods=34).mean() - vf.ewm(span=55, adjust=False, min_periods=55).mean()
def _nvi(c, v):
    r = c.pct_change(); vd = v < v.shift(1)
    f = np.where(vd, 1.0 + r, 1.0); f = np.where(np.isfinite(f), f, 1.0)
    s = pd.Series(np.cumprod(f), index=c.index); s.iloc[0] = np.nan
    return s
def _pvi(c, v):
    r = c.pct_change(); vu = v > v.shift(1)
    f = np.where(vu, 1.0 + r, 1.0); f = np.where(np.isfinite(f), f, 1.0)
    s = pd.Series(np.cumprod(f), index=c.index); s.iloc[0] = np.nan
    return s
def f23ob_f23_on_balance_volume_family_obv_norm_volsma20_slope_v001_signal(close, volume):
    obv = _obv(close, volume)
    base = obv / volume.rolling(20, min_periods=20).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff21_diff63_ratio_slope_v002_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.diff(21) / obv.diff(63).replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_netfrac_60d_slope_v003_signal(open, closeadj, volume):
    sv = np.sign(closeadj - open) * volume
    num = sv.rolling(60, min_periods=60).sum()
    den = volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    base = num / den
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_slope_10d_norm_slope_v004_signal(close, volume):
    obv = _obv(close, volume)
    v = volume.rolling(10, min_periods=10).mean().replace(0.0, np.nan)
    base = obv.diff(10) / v
    return base.diff(5).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_slope_42d_norm_slope_v005_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    v = volume.rolling(42, min_periods=42).mean().replace(0.0, np.nan)
    base = obv.diff(42) / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_dist_sma20_slope_v006_signal(close, volume):
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=20).mean()
    v = volume.rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    base = (obv - m) / v
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_dist_ema100_slope_v007_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    e = obv.ewm(span=100, adjust=False, min_periods=100).mean()
    v = volume.rolling(100, min_periods=100).mean().replace(0.0, np.nan)
    base = (obv - e) / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_sign_obv_sma20_slope_v008_signal(close, volume):
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=20).mean()
    return np.sign(obv - m).diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_sign_obv_ema60_slope_v009_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    e = obv.ewm(span=60, adjust=False, min_periods=60).mean()
    return np.sign(obv - e).diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_sign_obv_shift21_slope_v010_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    return np.sign(obv - obv.shift(21)).diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_daysince_obv_sma20_50d_slope_v011_signal(close, volume):
    obv = _obv(close, volume)
    diff = obv - obv.rolling(20, min_periods=20).mean()
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    base = flip.rolling(50, min_periods=50).apply(_streak_days_since, raw=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_streak_obv_above_sma40_60d_slope_v012_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    m = obv.rolling(40, min_periods=40).mean()
    sgn = (obv > m).astype(float).where(~m.isna())
    base = sgn.rolling(60, min_periods=60).apply(_streak_consec, raw=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_relchange_15d_slope_v013_signal(close, volume):
    obv = _obv(close, volume)
    base = (obv - obv.shift(15)) / obv.abs().replace(0.0, np.nan)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_curv_30d_norm_slope_v014_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    c = obv - 2.0 * obv.shift(15) + obv.shift(30)
    v = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    base = c / v
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_slope_30d_norm_slope_v015_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    v = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    base = adl.diff(30) / v
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_close_corr_60d_slope_v016_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    base = adl.diff(5).rolling(60, min_periods=60).corr(closeadj.pct_change(5))
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_diff_zscore_50d_slope_v017_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    d = adl.diff(10)
    mu = d.rolling(50, min_periods=50).mean()
    sd = d.rolling(50, min_periods=50).std()
    base = (d - mu) / sd.replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_slope_21d_slope_v018_signal(close, volume):
    pvt = _pvt(close, volume)
    v = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    base = pvt.diff(21) / v
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_dist_ema63_slope_v019_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    e = pvt.ewm(span=63, adjust=False, min_periods=63).mean()
    v = volume.rolling(63, min_periods=63).mean().replace(0.0, np.nan)
    base = (pvt - e) / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_sign_pvt_sma100_slope_v020_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    m = pvt.rolling(100, min_periods=100).mean()
    return np.sign(pvt - m).diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_zscore_60d_slope_v021_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    mu = obv.rolling(60, min_periods=60).mean()
    sd = obv.rolling(60, min_periods=60).std()
    base = (obv - mu) / sd.replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvhl_pctrank_140d_slope_v022_signal(high, volume):
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    base = obvhl.rolling(140, min_periods=140).rank(pct=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_madstd_ratio_60d_slope_v023_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    d = obv.diff()
    mad = d.rolling(60, min_periods=60).apply(
        lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    sd = d.rolling(60, min_periods=60).std()
    base = mad / sd.replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_pctrank_180d_slope_v024_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.rolling(180, min_periods=180).rank(pct=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvhl_slope_21d_norm_slope_v025_signal(high, volume):
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    v = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    base = obvhl.diff(21) / v
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_sign_obvhl_sma40_slope_v026_signal(high, volume):
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    m = obvhl.rolling(40, min_periods=40).mean()
    return np.sign(obvhl - m).diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_slope_15d_norm_slope_v027_signal(open, close, volume):
    obvco = (np.sign(close - open) * volume).cumsum()
    v = volume.rolling(15, min_periods=15).mean().replace(0.0, np.nan)
    base = obvco.diff(15) / v
    return base.diff(5).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_zscore_90d_slope_v028_signal(open, closeadj, volume):
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    mu = obvco.rolling(90, min_periods=90).mean()
    sd = obvco.rolling(90, min_periods=90).std()
    base = (obvco - mu) / sd.replace(0.0, np.nan)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_close_sign_div_21d_slope_v029_signal(close, volume):
    obv = _obv(close, volume)
    base = np.sign(obv.diff(21)) - np.sign(close.diff(21))
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_close_slopediff_42d_slope_v030_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    v = volume.rolling(42, min_periods=42).mean().replace(0.0, np.nan)
    base = obv.diff(42) / v - closeadj.pct_change(42) * 100.0
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_force_index_ema13_slope_v031_signal(close, volume):
    fi = close.diff() * volume
    base = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_fi_zscore_120d_slope_v032_signal(closeadj, volume):
    fi = closeadj.diff() * volume
    e = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    mu = e.rolling(120, min_periods=120).mean()
    sd = e.rolling(120, min_periods=120).std()
    base = (e - mu) / sd.replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_fi_sign_streak_30d_slope_v033_signal(close, volume):
    fi = close.diff() * volume
    e = fi.ewm(span=5, adjust=False, min_periods=5).mean()
    sgn = (e > 0).astype(float).where(~e.isna())
    base = sgn.rolling(30, min_periods=30).apply(_streak_consec, raw=True)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_nvi_dist_ema100_slope_v034_signal(closeadj, volume):
    nvi = _nvi(closeadj, volume)
    e = nvi.ewm(span=100, adjust=False, min_periods=100).mean()
    base = np.log(nvi / e)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvi_dist_ema60_slope_v035_signal(closeadj, volume):
    pvi = _pvi(closeadj, volume)
    e = pvi.ewm(span=60, adjust=False, min_periods=60).mean()
    base = np.log(pvi / e)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_nvi_pvi_logratio_slope_v036_signal(closeadj, volume):
    r = closeadj.pct_change()
    v_down = volume < volume.shift(1)
    v_up = volume > volume.shift(1)
    f_n = np.where(v_down, 1.0 + r, 1.0)
    f_p = np.where(v_up, 1.0 + r, 1.0)
    f_n = np.where(np.isfinite(f_n), f_n, 1.0)
    f_p = np.where(np.isfinite(f_p), f_p, 1.0)
    nvi = pd.Series(np.cumprod(f_n), index=closeadj.index); nvi.iloc[0] = np.nan
    pvi = pd.Series(np.cumprod(f_p), index=closeadj.index); pvi.iloc[0] = np.nan
    base = np.log(nvi / pvi)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_klinger_kvo_slope_v037_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    base = (vf.ewm(span=34, adjust=False, min_periods=34).mean()
            - vf.ewm(span=55, adjust=False, min_periods=55).mean())
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_klinger_vf_netfrac_30d_slope_v038_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    num = vf.rolling(30, min_periods=30).sum()
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    base = num / den
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_signflip_count_30d_slope_v039_signal(close, volume):
    obv = _obv(close, volume)
    s = np.sign(obv.diff())
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    base = flip.rolling(30, min_periods=30).sum()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_zscore_diff_60d_slope_v040_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    d = pvt.diff(10)
    mu = d.rolling(60, min_periods=60).mean()
    sd = d.rolling(60, min_periods=60).std()
    base = (d - mu) / sd.replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff_autocorr_60d_slope_v041_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    d = obv.diff()
    base = d.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_lead_close_corr_42d_slope_v042_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.diff(5).rolling(42, min_periods=42).corr(closeadj.pct_change(5).shift(-5))
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_regslope_40d_slope_v043_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    v = volume.rolling(40, min_periods=40).mean().replace(0.0, np.nan)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx)); var = np.sum((t - mt) ** 2)
        if var == 0.0 or not np.isfinite(mx):
            return np.nan
        return float(cov / var)
    sl = obv.rolling(40, min_periods=40).apply(_slope, raw=True)
    base = sl / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_rsq_80d_slope_v044_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        r = cov / np.sqrt(vt * vx)
        return float(r * r)
    base = obv.rolling(80, min_periods=80).apply(_rsq, raw=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_price_corr_60d_slope_v045_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.rolling(60, min_periods=60).corr(closeadj)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_price_corr_180d_slope_v046_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.rolling(180, min_periods=180).corr(closeadj)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_signflip_60d_slope_v047_signal(open, closeadj, volume):
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    s = np.sign(obvco.diff())
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    base = flip.rolling(60, min_periods=60).sum()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_tanh_obv_slope_30d_slope_v048_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    v = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    raw = obv.diff(30) / v
    sd = raw.rolling(60, min_periods=60).std()
    base = np.tanh(raw / sd.replace(0.0, np.nan))
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_netfrac_120d_slope_v050_signal(closeadj, volume):
    sv = np.sign(closeadj.diff()) * volume
    num = sv.rolling(120, min_periods=120).sum()
    den = volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    base = num / den
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_pct_vs_close_pct_15d_slope_v051_signal(close, volume):
    obv = _obv(close, volume)
    base = obv.pct_change(15) * 0.001 - close.pct_change(15)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_signedlog_obv_dist_sma30_slope_v052_signal(close, volume):
    obv = _obv(close, volume)
    d = obv - obv.rolling(30, min_periods=30).mean()
    base = np.sign(d) * np.log1p(d.abs())
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_fracabove_sma30_50d_slope_v053_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    m = obv.rolling(30, min_periods=30).mean()
    sgn = (obv > m).astype(float).where(~m.isna())
    base = sgn.rolling(50, min_periods=50).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_fracabove_ema100_140d_slope_v054_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    e = obv.ewm(span=100, adjust=False, min_periods=100).mean()
    sgn = (obv > e).astype(float).where(~e.isna())
    base = sgn.rolling(140, min_periods=140).mean()
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff_zscore_42d_slope_v055_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    d = obv.diff()
    mu = d.rolling(42, min_periods=42).mean()
    sd = d.rolling(42, min_periods=42).std()
    base = (d - mu) / sd.replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_obv_sign_agree_30d_slope_v056_signal(high, low, closeadj, volume):
    obv = _obv(closeadj, volume)
    adl = _adl(high, low, closeadj, volume)
    s_o = np.sign(obv.diff(5))
    s_a = np.sign(adl.diff(5))
    agree = (s_o == s_a).astype(float).where(~s_o.isna() & ~s_a.isna())
    base = agree.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_sign_kvo_signal_slope_v057_signal(high, low, closeadj, volume):
    kvo = _kvo(high, low, closeadj, volume)
    sig = kvo.ewm(span=13, adjust=False, min_periods=13).mean()
    return np.sign(kvo - sig).diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_fi_signpos_frac_50d_slope_v058_signal(closeadj, volume):
    fi = closeadj.diff() * volume
    e = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    sgn = (e > 0).astype(float).where(~e.isna())
    base = sgn.rolling(50, min_periods=50).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_adl_ma50dist_diff_slope_v059_signal(high, low, closeadj, volume):
    obv = _obv(closeadj, volume)
    adl = _adl(high, low, closeadj, volume)
    v = volume.rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    a = (obv - obv.rolling(50, min_periods=50).mean()) / v
    b = (adl - adl.rolling(50, min_periods=50).mean()) / v
    base = a - b
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_rsq_60d_slope_v060_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        r = cov / np.sqrt(vt * vx)
        return float(r * r)
    base = pvt.rolling(60, min_periods=60).apply(_rsq, raw=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_revrate_sma20_50d_slope_v061_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    diff = obv - obv.rolling(20, min_periods=20).mean()
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    base = flip.rolling(50, min_periods=50).sum() / 50.0
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvhl_zscore_70d_slope_v062_signal(high, volume):
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    mu = obvhl.rolling(70, min_periods=70).mean()
    sd = obvhl.rolling(70, min_periods=70).std()
    base = (obvhl - mu) / sd.replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_efficiency_30d_slope_v064_signal(closeadj, volume):
    sv = np.sign(closeadj.diff()) * volume
    num = sv.rolling(30, min_periods=30).sum().abs()
    den = sv.abs().rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    base = num / den
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_efficiency_120d_slope_v065_signal(closeadj, volume):
    sv = np.sign(closeadj.diff()) * volume
    num = sv.rolling(120, min_periods=120).sum().abs()
    den = sv.abs().rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    base = num / den
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_pctrank_120d_slope_v066_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    base = adl.rolling(120, min_periods=120).rank(pct=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_ma_ribbon_count_slope_v067_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    mas = [obv.rolling(k, min_periods=k).mean() for k in (10, 20, 40, 80, 160)]
    cnt = pd.Series(0.0, index=obv.index)
    mask = ~mas[0].isna()
    for m in mas:
        cnt = cnt + (obv > m).astype(float)
        mask = mask & ~m.isna()
    base = cnt.where(mask)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_signed_logmadiff_30_90_slope_v068_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    diff = obv.rolling(30, min_periods=30).mean() - obv.rolling(90, min_periods=90).mean()
    v = volume.rolling(90, min_periods=90).mean().replace(0.0, np.nan)
    raw = diff / v
    base = np.sign(raw) * np.log1p(raw.abs())
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_kvo_stoch_80d_slope_v069_signal(high, low, closeadj, volume):
    kvo = _kvo(high, low, closeadj, volume)
    hi = kvo.rolling(80, min_periods=80).max()
    lo = kvo.rolling(80, min_periods=80).min()
    base = (kvo - lo) / (hi - lo).replace(0.0, np.nan)
    sd = base.rolling(60, min_periods=60).std()
    return (base.diff(63) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_nvi_pctrank_180d_slope_v070_signal(closeadj, volume):
    nvi = _nvi(closeadj, volume)
    base = nvi.rolling(180, min_periods=180).rank(pct=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_fi_tanh_z_60d_slope_v071_signal(closeadj, volume):
    fi = closeadj.diff() * volume
    e = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    mu = e.rolling(60, min_periods=60).mean()
    sd = e.rolling(60, min_periods=60).std()
    base = np.tanh((e - mu) / sd.replace(0.0, np.nan))
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_obv_corr_90d_slope_v072_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    pvt = _pvt(closeadj, volume)
    base = obv.rolling(90, min_periods=90).corr(pvt)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_regresid_60d_slope_v073_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    def _r(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx)); vt = np.sum((t - mt) ** 2)
        if vt == 0.0:
            return np.nan
        b = cov / vt; a = mx - b * mt
        return float(np.std(x - (a + b * t)))
    rs = obv.rolling(60, min_periods=60).apply(_r, raw=True)
    base = rs / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff_skew_80d_slope_v074_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.diff().rolling(80, min_periods=80).skew()
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff_kurt_120d_slope_v075_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.diff().rolling(120, min_periods=120).kurt()
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_chaikin_osc_norm_slope_v077_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    osc = adl.ewm(span=3, adjust=False, min_periods=3).mean() - adl.ewm(span=10, adjust=False, min_periods=10).mean()
    v = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    base = osc / v
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_sign_chaikin_osc_slope_v078_signal(high, low, close, volume):
    adl = _adl(high, low, close, volume)
    osc = adl.ewm(span=3, adjust=False, min_periods=3).mean() - adl.ewm(span=10, adjust=False, min_periods=10).mean()
    return np.sign(osc).diff(5).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_mfv_sign_streak_20d_slope_v079_signal(high, low, close, volume):
    rng = (high - low).replace(0.0, np.nan)
    mfv = ((close - low) - (high - close)) / rng * volume
    sgn = (mfv > 0).astype(float).where(~mfv.isna())
    base = sgn.rolling(20, min_periods=20).apply(_streak_consec, raw=True)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_mfv_sma63_norm_slope_v080_signal(high, low, closeadj, volume):
    rng = (high - low).replace(0.0, np.nan)
    mfv = ((closeadj - low) - (high - closeadj)) / rng * volume
    sm = mfv.rolling(63, min_periods=63).mean()
    v = volume.rolling(63, min_periods=63).mean().replace(0.0, np.nan)
    base = sm / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_ma_short_minus_long_30_90_slope_v081_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    diff = obv.rolling(30, min_periods=30).mean() - obv.rolling(90, min_periods=90).mean()
    v = volume.rolling(90, min_periods=90).mean().replace(0.0, np.nan)
    base = diff / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_ema_short_minus_long_10_40_slope_v082_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    diff = obv.ewm(span=10, adjust=False, min_periods=10).mean() - obv.ewm(span=40, adjust=False, min_periods=40).mean()
    v = volume.rolling(40, min_periods=40).mean().replace(0.0, np.nan)
    base = diff / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_multi_sign_count_slope_v083_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    mas = [obv.rolling(k, min_periods=k).mean() for k in (10, 30, 60, 120)]
    cnt = pd.Series(0.0, index=obv.index); mask = ~mas[0].isna()
    for m in mas:
        cnt = cnt + (obv > m).astype(float); mask = mask & ~m.isna()
    base = cnt.where(mask)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_pctB_50d_slope_v084_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    m = obv.rolling(50, min_periods=50).mean()
    sd = obv.rolling(50, min_periods=50).std()
    upper = m + 2.0 * sd; lower = m - 2.0 * sd
    base = (obv - lower) / (upper - lower).replace(0.0, np.nan)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_bandwidth_50d_slope_v085_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    sd = obv.rolling(50, min_periods=50).std()
    v = volume.rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    base = 4.0 * sd / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_velocity_30d_slope_v086_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    v = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    base = adl.diff(5) / v
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_curv_60d_slope_v087_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    c = adl - 2.0 * adl.shift(30) + adl.shift(60)
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    base = c / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_close_rank_diff_60d_slope_v088_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = (obv.rolling(60, min_periods=60).rank(pct=True)
            - closeadj.rolling(60, min_periods=60).rank(pct=True))
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_close_rank_diff_180d_slope_v089_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = (obv.rolling(180, min_periods=180).rank(pct=True)
            - closeadj.rolling(180, min_periods=180).rank(pct=True))
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff_std_45d_slope_v090_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.diff().rolling(45, min_periods=45).std()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff_std_norm_45d_slope_v091_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    sd = obv.diff().rolling(45, min_periods=45).std()
    v = volume.rolling(45, min_periods=45).mean().replace(0.0, np.nan)
    base = sd / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_dist_sma25_slope_v092_signal(open, closeadj, volume):
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    m = obvco.rolling(25, min_periods=25).mean()
    v = volume.rolling(25, min_periods=25).mean().replace(0.0, np.nan)
    base = (obvco - m) / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_efficiency_45d_slope_v093_signal(open, closeadj, volume):
    sv = np.sign(closeadj - open) * volume
    num = sv.rolling(45, min_periods=45).sum().abs()
    den = sv.abs().rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    base = num / den
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvhl_dist_sma60_slope_v094_signal(high, volume):
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    m = obvhl.rolling(60, min_periods=60).mean()
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    base = (obvhl - m) / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvhl_efficiency_80d_slope_v095_signal(high, volume):
    sv = np.sign(high.diff()) * volume
    num = sv.rolling(80, min_periods=80).sum().abs()
    den = sv.abs().rolling(80, min_periods=80).sum().replace(0.0, np.nan)
    base = num / den
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_lag_corr_5d_60d_slope_v096_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.diff(5).rolling(60, min_periods=60).corr(closeadj.pct_change(5).shift(5))
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_nvi_slope_63d_slope_v097_signal(closeadj, volume):
    nvi = _nvi(closeadj, volume)
    base = nvi.pct_change(63)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvi_slope_63d_slope_v098_signal(closeadj, volume):
    pvi = _pvi(closeadj, volume)
    base = pvi.pct_change(63)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_sign_nvi_ema100_slope_v099_signal(closeadj, volume):
    nvi = _nvi(closeadj, volume)
    e = nvi.ewm(span=100, adjust=False, min_periods=100).mean()
    return np.sign(nvi - e).diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_kvo_zscore_120d_slope_v100_signal(high, low, closeadj, volume):
    kvo = _kvo(high, low, closeadj, volume)
    mu = kvo.rolling(120, min_periods=120).mean()
    sd = kvo.rolling(120, min_periods=120).std()
    base = (kvo - mu) / sd.replace(0.0, np.nan)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_vf_corr_close_60d_slope_v101_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    base = vf.rolling(60, min_periods=60).corr(closeadj.diff())
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_fi_ema_100d_norm_slope_v102_signal(closeadj, volume):
    fi = closeadj.diff() * volume
    e = fi.ewm(span=100, adjust=False, min_periods=100).mean()
    sm = (volume * closeadj.diff().abs()).rolling(100, min_periods=100).mean().replace(0.0, np.nan)
    base = e / sm
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_fi_skew_60d_slope_v103_signal(closeadj, volume):
    fi = closeadj.diff() * volume
    base = fi.rolling(60, min_periods=60).skew()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff5_diff21_ratio_slope_v104_signal(close, volume):
    obv = _obv(close, volume)
    base = obv.diff(5) / obv.diff(21).replace(0.0, np.nan)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff21_pct_of_voltotal_slope_v105_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    base = obv.diff(21) / den
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_regslope_120d_slope_v106_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    v = volume.rolling(120, min_periods=120).mean().replace(0.0, np.nan)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx)); var = np.sum((t - mt) ** 2)
        if var == 0.0 or not np.isfinite(mx):
            return np.nan
        return float(cov / var)
    sl = obv.rolling(120, min_periods=120).apply(_slope, raw=True)
    base = sl / v
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_rsq_100d_slope_v107_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        r = cov / np.sqrt(vt * vx)
        return float(r * r)
    base = adl.rolling(100, min_periods=100).apply(_rsq, raw=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_daysince_obv_shift42_80d_slope_v108_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    s = np.sign(obv - obv.shift(42))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    base = flip.rolling(80, min_periods=80).apply(_streak_days_since, raw=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_below_ema60_streak_80d_slope_v109_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    e = obv.ewm(span=60, adjust=False, min_periods=60).mean()
    sgn = (obv < e).astype(float).where(~e.isna())
    base = sgn.rolling(80, min_periods=80).apply(_streak_consec, raw=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_vs_obv_corr_60d_slope_v110_signal(open, closeadj, volume):
    obv = _obv(closeadj, volume)
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    base = obvco.diff(5).rolling(60, min_periods=60).corr(obv.diff(5))
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvhl_vs_obv_corr_90d_slope_v111_signal(high, closeadj, volume):
    obv = _obv(closeadj, volume)
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    base = obvhl.diff(10).rolling(90, min_periods=90).corr(obv.diff(10))
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_fi_corr_60d_slope_v112_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    fi = closeadj.diff() * volume
    base = obv.diff(5).rolling(60, min_periods=60).corr(fi)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_stoch_50d_slope_v113_signal(open, closeadj, volume):
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    hi = obvco.rolling(50, min_periods=50).max()
    lo = obvco.rolling(50, min_periods=50).min()
    base = (obvco - lo) / (hi - lo).replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_shiftratio_30_90_slope_v114_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = (obv - obv.shift(30)) / (obv - obv.shift(90)).replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_detrended_z_80d_slope_v115_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    v = volume.rolling(80, min_periods=80).mean().replace(0.0, np.nan)
    def _resid_last(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx)); vt = np.sum((t - mt) ** 2)
        if vt == 0.0:
            return np.nan
        b = cov / vt; a = mx - b * mt
        return float(x[-1] - (a + b * t[-1]))
    rs = obv.rolling(80, min_periods=80).apply(_resid_last, raw=True)
    base = rs / v
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_signed_vol_emaratio_5_20_slope_v116_signal(close, volume):
    sv = np.sign(close.diff()) * volume
    e_s = sv.ewm(span=5, adjust=False, min_periods=5).mean()
    e_l = sv.ewm(span=20, adjust=False, min_periods=20).mean()
    base = e_s / e_l.replace(0.0, np.nan)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_signed_vol_zscore_50d_slope_v117_signal(closeadj, volume):
    sv = np.sign(closeadj.diff()) * volume
    mu = sv.rolling(50, min_periods=50).mean()
    sd = sv.rolling(50, min_periods=50).std()
    base = (sv - mu) / sd.replace(0.0, np.nan)
    base_n = base / base.abs().rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    return base_n.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_cumvolume_ratio_slope_v118_signal(close, volume):
    obv = _obv(close, volume)
    base = obv / volume.cumsum().replace(0.0, np.nan)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_zscore_70d_slope_v119_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    mu = adl.rolling(70, min_periods=70).mean()
    sd = adl.rolling(70, min_periods=70).std()
    base = (adl - mu) / sd.replace(0.0, np.nan)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_fracabove_sma40_50d_slope_v120_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    m = adl.rolling(40, min_periods=40).mean()
    sgn = (adl > m).astype(float).where(~m.isna())
    base = sgn.rolling(50, min_periods=50).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_zscore_70d_slope_v121_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    mu = pvt.rolling(70, min_periods=70).mean()
    sd = pvt.rolling(70, min_periods=70).std()
    base = (pvt - mu) / sd.replace(0.0, np.nan)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_pctrank_180d_slope_v122_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    base = pvt.rolling(180, min_periods=180).rank(pct=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_fi_short_long_ratio_slope_v123_signal(close, volume):
    fi = close.diff() * volume
    s = fi.ewm(span=5, adjust=False, min_periods=5).mean()
    l = fi.ewm(span=20, adjust=False, min_periods=20).mean()
    base = s / l.replace(0.0, np.nan)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_fi_arctan_z_30d_slope_v124_signal(close, volume):
    fi = close.diff() * volume
    mu = fi.rolling(30, min_periods=30).mean()
    sd = fi.rolling(30, min_periods=30).std()
    z = (fi - mu) / sd.replace(0.0, np.nan)
    base = np.arctan(z)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_kvo_ema_slope_42d_slope_v125_signal(high, low, closeadj, volume):
    kvo = _kvo(high, low, closeadj, volume)
    v = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    base = kvo.diff(21) / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_kvo_signal_distance_slope_v126_signal(high, low, closeadj, volume):
    kvo = _kvo(high, low, closeadj, volume)
    sig = kvo.ewm(span=13, adjust=False, min_periods=13).mean()
    v = volume.rolling(13, min_periods=13).mean().replace(0.0, np.nan)
    base = (kvo - sig) / v
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_chaikin_osc_pctrank_120d_slope_v127_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    osc = adl.ewm(span=3, adjust=False, min_periods=3).mean() - adl.ewm(span=10, adjust=False, min_periods=10).mean()
    base = osc.rolling(120, min_periods=120).rank(pct=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_nvi_pctrank_60d_slope_v128_signal(closeadj, volume):
    nvi = _nvi(closeadj, volume)
    base = nvi.rolling(60, min_periods=60).rank(pct=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvi_pctrank_120d_slope_v129_signal(closeadj, volume):
    pvi = _pvi(closeadj, volume)
    base = pvi.rolling(120, min_periods=120).rank(pct=True)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_nvi_zscore_90d_slope_v130_signal(closeadj, volume):
    nvi = _nvi(closeadj, volume)
    mu = nvi.rolling(90, min_periods=90).mean()
    sd = nvi.rolling(90, min_periods=90).std()
    base = (nvi - mu) / sd.replace(0.0, np.nan)
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_direction_entropy_50d_slope_v131_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    bn = (obv.diff() > 0).astype(float).where(~obv.diff().isna())
    p = bn.rolling(50, min_periods=50).mean()
    p_clip = p.clip(1e-9, 1.0 - 1e-9)
    h = -(p_clip * np.log2(p_clip) + (1.0 - p_clip) * np.log2(1.0 - p_clip))
    base = h.where(~p.isna())
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_signedlog_level_norm_slope_v132_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    v = volume.rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    r = obv / v
    base = np.sign(r) * np.log1p(r.abs())
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_adl_revrate_sma30_60d_slope_v133_signal(high, low, closeadj, volume):
    adl = _adl(high, low, closeadj, volume)
    diff = adl - adl.rolling(30, min_periods=30).mean()
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    base = flip.rolling(60, min_periods=60).sum() / 60.0
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_ma_short_long_diff_slope_v134_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    diff = pvt.rolling(20, min_periods=20).mean() - pvt.rolling(80, min_periods=80).mean()
    v = volume.rolling(80, min_periods=80).mean().replace(0.0, np.nan)
    base = diff / v
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_pvt_tanh_slope_30d_slope_v135_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    d = pvt.diff(30)
    sd = d.rolling(60, min_periods=60).std()
    base = np.tanh(d / sd.replace(0.0, np.nan))
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff_autocorr5_90d_slope_v136_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    d = obv.diff()
    base = d.rolling(90, min_periods=90).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_close_zscore_diff_45d_slope_v137_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    mu_o = obv.rolling(45, min_periods=45).mean(); sd_o = obv.rolling(45, min_periods=45).std()
    mu_c = closeadj.rolling(45, min_periods=45).mean(); sd_c = closeadj.rolling(45, min_periods=45).std()
    z_o = (obv - mu_o) / sd_o.replace(0.0, np.nan)
    z_c = (closeadj - mu_c) / sd_c.replace(0.0, np.nan)
    base = z_o - z_c
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_uppct_60d_slope_v138_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    bn = (obv.diff() > 0).astype(float).where(~obv.diff().isna())
    base = bn.rolling(60, min_periods=60).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_drawdown_120d_slope_v139_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    peak = obv.rolling(120, min_periods=120).max()
    v = volume.rolling(120, min_periods=120).mean().replace(0.0, np.nan)
    base = (peak - obv) / v
    return base.diff(63).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_diff_winsor_60d_slope_v140_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    d = obv.diff()
    def _wins(x):
        if len(x) < 5:
            return np.nan
        lo = np.quantile(x, 0.1); hi = np.quantile(x, 0.9)
        return float(np.mean(np.clip(x, lo, hi)))
    sm = d.rolling(60, min_periods=60).apply(_wins, raw=True)
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    base = sm / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_adl_pvt_sign_agreement_slope_v141_signal(high, low, closeadj, volume):
    obv = _obv(closeadj, volume)
    adl = _adl(high, low, closeadj, volume)
    pvt = _pvt(closeadj, volume)
    base = np.sign(obv.diff(10)) + np.sign(adl.diff(10)) + np.sign(pvt.diff(10))
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_iqr_60d_norm_slope_v142_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    q75 = obv.rolling(60, min_periods=60).quantile(0.75)
    q25 = obv.rolling(60, min_periods=60).quantile(0.25)
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    base = (q75 - q25) / v
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_close_lag_obv_corr_42d_slope_v143_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = closeadj.pct_change(5).rolling(42, min_periods=42).corr(obv.diff(5).shift(5))
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_cv_30d_slope_v144_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    sd = obv.rolling(30, min_periods=30).std()
    mu = obv.rolling(30, min_periods=30).mean().abs().replace(0.0, np.nan)
    base = sd / mu
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_kvo_fracpos_40d_slope_v145_signal(high, low, closeadj, volume):
    kvo = _kvo(high, low, closeadj, volume)
    sgn = (kvo > 0).astype(float).where(~kvo.isna())
    base = sgn.rolling(40, min_periods=40).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvco_upvol_downvol_logratio_slope_v146_signal(open, closeadj, volume):
    upv = volume.where(closeadj > open, 0.0)
    dnv = volume.where(closeadj < open, 0.0)
    u = upv.rolling(30, min_periods=30).sum()
    d = dnv.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    base = np.log(u / d)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvhl_streak_above_sma40_50d_slope_v147_signal(high, volume):
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    m = obvhl.rolling(40, min_periods=40).mean()
    sgn = (obvhl > m).astype(float).where(~m.isna())
    base = sgn.rolling(50, min_periods=50).apply(_streak_consec, raw=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_daysince_pvt_sma50_70d_slope_v148_signal(closeadj, volume):
    pvt = _pvt(closeadj, volume)
    diff = pvt - pvt.rolling(50, min_periods=50).mean()
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    base = flip.rolling(70, min_periods=70).apply(_streak_days_since, raw=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obvdiff_closediff_corr_30d_slope_v149_signal(closeadj, volume):
    obv = _obv(closeadj, volume)
    base = obv.diff().rolling(30, min_periods=30).corr(closeadj.diff())
    return base.diff(10).replace([np.inf, -np.inf], np.nan)
def f23ob_f23_on_balance_volume_family_obv_co_ratio_120d_slope_v150_signal(open, closeadj, volume):
    sv_co = np.sign(closeadj - open) * volume
    sv_obv = np.sign(closeadj.diff()) * volume
    num = sv_co.rolling(120, min_periods=120).sum()
    den = sv_obv.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    base = num / den
    return base.diff(63).replace([np.inf, -np.inf], np.nan)

_ENTRIES = [
    (f23ob_f23_on_balance_volume_family_obv_norm_volsma20_slope_v001_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff21_diff63_ratio_slope_v002_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_netfrac_60d_slope_v003_signal, ["open", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_slope_10d_norm_slope_v004_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_slope_42d_norm_slope_v005_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_dist_sma20_slope_v006_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_dist_ema100_slope_v007_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_sign_obv_sma20_slope_v008_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_sign_obv_ema60_slope_v009_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_sign_obv_shift21_slope_v010_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_daysince_obv_sma20_50d_slope_v011_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_streak_obv_above_sma40_60d_slope_v012_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_relchange_15d_slope_v013_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_curv_30d_norm_slope_v014_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_slope_30d_norm_slope_v015_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_close_corr_60d_slope_v016_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_diff_zscore_50d_slope_v017_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_slope_21d_slope_v018_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_dist_ema63_slope_v019_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_sign_pvt_sma100_slope_v020_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_zscore_60d_slope_v021_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvhl_pctrank_140d_slope_v022_signal, ["high", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_madstd_ratio_60d_slope_v023_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_pctrank_180d_slope_v024_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvhl_slope_21d_norm_slope_v025_signal, ["high", "volume"]),
    (f23ob_f23_on_balance_volume_family_sign_obvhl_sma40_slope_v026_signal, ["high", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_slope_15d_norm_slope_v027_signal, ["open", "close", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_zscore_90d_slope_v028_signal, ["open", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_close_sign_div_21d_slope_v029_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_close_slopediff_42d_slope_v030_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_force_index_ema13_slope_v031_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_fi_zscore_120d_slope_v032_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_fi_sign_streak_30d_slope_v033_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_nvi_dist_ema100_slope_v034_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvi_dist_ema60_slope_v035_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_nvi_pvi_logratio_slope_v036_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_klinger_kvo_slope_v037_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_klinger_vf_netfrac_30d_slope_v038_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_signflip_count_30d_slope_v039_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_zscore_diff_60d_slope_v040_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff_autocorr_60d_slope_v041_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_lead_close_corr_42d_slope_v042_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_regslope_40d_slope_v043_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_rsq_80d_slope_v044_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_price_corr_60d_slope_v045_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_price_corr_180d_slope_v046_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_signflip_60d_slope_v047_signal, ["open", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_tanh_obv_slope_30d_slope_v048_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_netfrac_120d_slope_v050_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_pct_vs_close_pct_15d_slope_v051_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_signedlog_obv_dist_sma30_slope_v052_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_fracabove_sma30_50d_slope_v053_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_fracabove_ema100_140d_slope_v054_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff_zscore_42d_slope_v055_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_obv_sign_agree_30d_slope_v056_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_sign_kvo_signal_slope_v057_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_fi_signpos_frac_50d_slope_v058_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_adl_ma50dist_diff_slope_v059_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_rsq_60d_slope_v060_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_revrate_sma20_50d_slope_v061_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvhl_zscore_70d_slope_v062_signal, ["high", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_efficiency_30d_slope_v064_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_efficiency_120d_slope_v065_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_pctrank_120d_slope_v066_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_ma_ribbon_count_slope_v067_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_signed_logmadiff_30_90_slope_v068_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_kvo_stoch_80d_slope_v069_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_nvi_pctrank_180d_slope_v070_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_fi_tanh_z_60d_slope_v071_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_obv_corr_90d_slope_v072_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_regresid_60d_slope_v073_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff_skew_80d_slope_v074_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff_kurt_120d_slope_v075_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_chaikin_osc_norm_slope_v077_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_sign_chaikin_osc_slope_v078_signal, ["high", "low", "close", "volume"]),
    (f23ob_f23_on_balance_volume_family_mfv_sign_streak_20d_slope_v079_signal, ["high", "low", "close", "volume"]),
    (f23ob_f23_on_balance_volume_family_mfv_sma63_norm_slope_v080_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_ma_short_minus_long_30_90_slope_v081_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_ema_short_minus_long_10_40_slope_v082_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_multi_sign_count_slope_v083_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_pctB_50d_slope_v084_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_bandwidth_50d_slope_v085_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_velocity_30d_slope_v086_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_curv_60d_slope_v087_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_close_rank_diff_60d_slope_v088_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_close_rank_diff_180d_slope_v089_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff_std_45d_slope_v090_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff_std_norm_45d_slope_v091_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_dist_sma25_slope_v092_signal, ["open", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_efficiency_45d_slope_v093_signal, ["open", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvhl_dist_sma60_slope_v094_signal, ["high", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvhl_efficiency_80d_slope_v095_signal, ["high", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_lag_corr_5d_60d_slope_v096_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_nvi_slope_63d_slope_v097_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvi_slope_63d_slope_v098_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_sign_nvi_ema100_slope_v099_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_kvo_zscore_120d_slope_v100_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_vf_corr_close_60d_slope_v101_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_fi_ema_100d_norm_slope_v102_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_fi_skew_60d_slope_v103_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff5_diff21_ratio_slope_v104_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff21_pct_of_voltotal_slope_v105_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_regslope_120d_slope_v106_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_rsq_100d_slope_v107_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_daysince_obv_shift42_80d_slope_v108_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_below_ema60_streak_80d_slope_v109_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_vs_obv_corr_60d_slope_v110_signal, ["open", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvhl_vs_obv_corr_90d_slope_v111_signal, ["high", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_fi_corr_60d_slope_v112_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_stoch_50d_slope_v113_signal, ["open", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_shiftratio_30_90_slope_v114_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_detrended_z_80d_slope_v115_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_signed_vol_emaratio_5_20_slope_v116_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_signed_vol_zscore_50d_slope_v117_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_cumvolume_ratio_slope_v118_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_zscore_70d_slope_v119_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_fracabove_sma40_50d_slope_v120_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_zscore_70d_slope_v121_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_pctrank_180d_slope_v122_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_fi_short_long_ratio_slope_v123_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_fi_arctan_z_30d_slope_v124_signal, ["close", "volume"]),
    (f23ob_f23_on_balance_volume_family_kvo_ema_slope_42d_slope_v125_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_kvo_signal_distance_slope_v126_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_chaikin_osc_pctrank_120d_slope_v127_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_nvi_pctrank_60d_slope_v128_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvi_pctrank_120d_slope_v129_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_nvi_zscore_90d_slope_v130_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_direction_entropy_50d_slope_v131_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_signedlog_level_norm_slope_v132_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_adl_revrate_sma30_60d_slope_v133_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_ma_short_long_diff_slope_v134_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_pvt_tanh_slope_30d_slope_v135_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff_autocorr5_90d_slope_v136_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_close_zscore_diff_45d_slope_v137_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_uppct_60d_slope_v138_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_drawdown_120d_slope_v139_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_diff_winsor_60d_slope_v140_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_adl_pvt_sign_agreement_slope_v141_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_iqr_60d_norm_slope_v142_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_close_lag_obv_corr_42d_slope_v143_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_cv_30d_slope_v144_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_kvo_fracpos_40d_slope_v145_signal, ["high", "low", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvco_upvol_downvol_logratio_slope_v146_signal, ["open", "closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvhl_streak_above_sma40_50d_slope_v147_signal, ["high", "volume"]),
    (f23ob_f23_on_balance_volume_family_daysince_pvt_sma50_70d_slope_v148_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obvdiff_closediff_corr_30d_slope_v149_signal, ["closeadj", "volume"]),
    (f23ob_f23_on_balance_volume_family_obv_co_ratio_120d_slope_v150_signal, ["open", "closeadj", "volume"]),
]

f23_on_balance_volume_family_slope_001_150_REGISTRY = {fn.__name__: {"inputs": inp, "func": fn} for fn, inp in _ENTRIES}
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
    for name, entry in f23_on_balance_volume_family_slope_001_150_REGISTRY.items():
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
