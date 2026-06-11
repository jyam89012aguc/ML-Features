"""f22_volume_trend jerk features 001-150 (2nd derivative).
Each function spells its base formula inline; returns (b - 2*b.shift(k) +
b.shift(2*k)).replace([inf,-inf],nan). k follows ROC bracket of base window.
"""
from __future__ import annotations
import numpy as np
import pandas as pd


def _sma(s, n):
    return s.rolling(n, min_periods=n).mean()

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

def _wma(s, n):
    w = np.arange(1, n + 1, dtype=float); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)

def _wilder(s, n):
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()

def _hma(s, n):
    half = max(2, n // 2); sqn = max(2, int(np.sqrt(n)))
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)

def _streak_lastflip(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])

def _consec(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5: c += 1
        else: break
    return float(c)

def _reg_slope_norm(x):
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx)); vr = np.sum((t - mt) ** 2)
    if vr == 0.0 or not np.isfinite(mx) or mx == 0.0:
        return np.nan
    return float((cov / vr) / mx)

def _reg_rsq(x):
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx))
    vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
    if vt == 0.0 or vx == 0.0:
        return np.nan
    r = cov / np.sqrt(vt * vx)
    return float(r * r)

def _hurst_rs(x):
    n = len(x)
    if n < 16: return np.nan
    y = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(y)): return np.nan
    mean = y.mean(); dev = y - mean; z = np.cumsum(dev)
    R = z.max() - z.min(); S = y.std(ddof=0)
    if S == 0.0 or not np.isfinite(R / S) or R / S <= 0.0: return np.nan
    return float(np.log(R / S) / np.log(n))


def f22vt_f22_volume_trend_logvol_sma_8d_jerk_v001_signal(volume):
    k=5;b = np.log(volume / _sma(volume, 8))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsmadiff_50_200_jerk_v002_signal(volume):
    k=63;b = np.log(_sma(volume, 50) / _sma(volume, 200))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_sma_200d_resid_jerk_v003_signal(volume):
    k=63;b = np.log(volume / _sma(volume, 200)) - np.log(volume / _sma(volume, 40))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_volwma_diff_20d_jerk_v004_signal(volume):
    k=10;b = np.log(_sma(volume, 20) / _wma(volume, 20))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volwilder_acceleration_40d_jerk_v005_signal(volume):
    k=21;a=_wilder(volume,40)
    b = (a - 2.0 * a.shift(21) + a.shift(42)) / a.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_vol_sma_5_50_ratio_jerk_v006_signal(volume):
    k=21;b = np.log(_sma(volume, 5) / _sma(volume, 50))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_vol_ema_10_120_ratio_jerk_v007_signal(volume):
    k=63;b = np.log(_ema(volume, 10) / _ema(volume, 120))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_vol_wma_sma_diff_60d_jerk_v008_signal(volume):
    k=21;b = np.log(_wma(volume, 60) / _sma(volume, 60))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_jerk_v009_signal(volume):
    k=21;s1 = (_sma(volume, 5) - _sma(volume, 50)) / _sma(volume, 50)
    s2 = (_ema(volume, 10) - _ema(volume, 40)) / _ema(volume, 40)
    b = s1 - s2
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema_xover_freq_120d_jerk_v010_signal(volume):
    k=63;s = np.sign(_ema(volume, 10) - _ema(volume, 40))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(120,120).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_vol_sma_21_jerk_v011_signal(volume):
    k=10;b = np.sign(volume - _sma(volume, 21))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_volsma_5_20_jerk_v012_signal(volume):
    k=10;b = np.sign(_sma(volume, 5) - _sma(volume, 20))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_volema_30_90_jerk_v013_signal(volume):
    k=21;b = np.sign(_ema(volume, 30) - _ema(volume, 90))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_volwilder_sma_60d_jerk_v014_signal(volume):
    k=63;b = np.sign(_wilder(volume, 60) - _sma(volume, 60))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_jerk_v015_signal(volume):
    k=21;s = np.sign(volume - _sma(volume, 21))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(120,120).apply(_streak_lastflip, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_daysince_volsma_5_50_180d_jerk_v016_signal(volume):
    k=63;s = np.sign(_sma(volume, 5) - _sma(volume, 50))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(180,180).apply(_streak_lastflip, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_streak_above_volsma20_45d_jerk_v017_signal(volume):
    k=10;above = (volume > _sma(volume, 20)).astype(float).where(~_sma(volume, 20).isna())
    b = above.rolling(45,45).apply(_consec, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_streak_below_volema50_140d_jerk_v018_signal(volume):
    k=21;below = (volume < _ema(volume, 50)).astype(float).where(~_ema(volume, 50).isna())
    b = below.rolling(140,140).apply(_consec, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma25_slope_jerk_v019_signal(volume):
    k=10;m=_sma(volume,25); b = m.diff(10) / m.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema80_slope_jerk_v020_signal(volume):
    k=63;m=_ema(volume,80); b = m.diff(21) / m.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_jerk_v021_signal(volume):
    k=21;a=_wma(volume,40); c=_sma(volume,80)
    b = a.diff(10) / a.abs() - c.diff(10) / c.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema30_curv_jerk_v022_signal(volume):
    k=21;m=_ema(volume,30)
    b = (m - 2.0 * m.shift(10) + m.shift(20)) / m.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma60_curv_jerk_v023_signal(volume):
    k=10;m=_sma(volume,60)
    b = (m - 2.0 * m.shift(21) + m.shift(42)) / m.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volz_sma25_jerk_v024_signal(volume):
    k=21;m=_sma(volume,25); sd = volume.rolling(25,25).std()
    b = (volume - m) / sd.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_jerk_v025_signal(volume):
    k=63;m1=_sma(volume,25); sd1 = volume.rolling(25,25).std()
    m2=_ema(volume,90); sd2 = volume.rolling(90,90).std()
    z1 = (volume - m1) / sd1.replace(0.0, np.nan)
    z2 = (volume - m2) / sd2.replace(0.0, np.nan)
    b = z2 - z1
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_rank_volsma15_90d_jerk_v026_signal(volume):
    k=21;b=_sma(volume,15).rolling(90,90).rank(pct=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_rank_volema60_252d_jerk_v027_signal(volume):
    k=63;b=_ema(volume,60).rolling(252,252).rank(pct=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_stoch_volsma_30_120d_jerk_v028_signal(volume):
    k=10;m=_sma(volume,30)
    mn = m.rolling(120,120).min(); mx = m.rolling(120,120).max()
    b = (m - mn) / (mx - mn).replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_stoch_volema_70_252d_jerk_v029_signal(volume):
    k=63;m=_ema(volume,70)
    mn = m.rolling(252,252).min(); mx = m.rolling(252,252).max()
    b = (m - mn) / (mx - mn).replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_roc_21d_jerk_v030_signal(volume):
    k=10;b = np.log(volume / volume.shift(21))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_roc_63d_jerk_v031_signal(volume):
    k=21;b = np.log(volume / volume.shift(63))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_slope_spread_10_50_jerk_v032_signal(volume):
    k=21;m10=_sma(volume,10); m50=_sma(volume,50)
    s10 = m10.diff(10) / m10.abs(); s50 = m50.diff(10) / m50.abs()
    b = s10 - s50
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema_slope_spread_20_120_jerk_v033_signal(volume):
    k=63;m20=_ema(volume,20); m120=_ema(volume,120)
    s20 = m20.diff(21) / m20.abs(); s120 = m120.diff(21) / m120.abs()
    b = s20 - s120
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_jerk_v034_signal(close, volume):
    k=21;up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    long_avg = volume.rolling(30,30).mean().replace(0.0, np.nan)
    diff = up.rolling(30,30).mean() - dn.rolling(30,30).mean()
    b = diff / long_avg
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_upvol_downvol_ratio_60d_jerk_v035_signal(closeadj, volume):
    k=21;up = volume.where(closeadj.diff() > 0.0, 0.0)
    dn = volume.where(closeadj.diff() < 0.0, 0.0)
    a = up.rolling(60,60).mean(); c = dn.rolling(60,60).mean()
    b = np.log(a.replace(0.0, np.nan) / c.replace(0.0, np.nan))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_upvol_downvol_ratio_150d_jerk_v036_signal(closeadj, volume):
    k=63;up = volume.where(closeadj.diff() > 0.0, 0.0)
    dn = volume.where(closeadj.diff() < 0.0, 0.0)
    a = up.ewm(span=150, adjust=False, min_periods=150).mean()
    c = dn.ewm(span=150, adjust=False, min_periods=150).mean()
    b = np.log(a.replace(0.0, np.nan) / c.replace(0.0, np.nan))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_jerk_v037_signal(closeadj, volume):
    k=63;dv = closeadj * volume
    a = _ema(dv, 40); c = _ema(dv, 120)
    b = a.diff(21) / a.abs() - c.diff(21) / c.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_jerk_v038_signal(closeadj, volume):
    k=21;dv = closeadj * volume
    b = np.log(_sma(dv, 120)) - np.log(_sma(dv, 40))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_ema_25_100_ratio_jerk_v039_signal(closeadj, volume):
    k=63;dv = closeadj * volume
    b = np.log(_ema(dv, 25) / _ema(dv, 100))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_sma60_slope_jerk_v040_signal(closeadj, volume):
    k=21;dv = closeadj * volume; m = _sma(dv, 60)
    b = m.diff(21) / m.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_olsslope_30d_jerk_v041_signal(volume):
    k=21;b = np.log(volume).rolling(30,30).apply(_reg_slope_norm, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_olsslope_120d_jerk_v042_signal(volume):
    k=63;b = np.log(volume).rolling(120,120).apply(_reg_slope_norm, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_rsq_45d_jerk_v043_signal(volume):
    k=21;b = np.log(volume).rolling(45,45).apply(_reg_rsq, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_rsq_180d_jerk_v044_signal(volume):
    k=63;b = np.log(volume).rolling(180,180).apply(_reg_rsq, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_vma_pma_agree_sign_60d_jerk_v045_signal(closeadj, volume):
    k=63;a = np.sign(volume - _sma(volume, 60))
    c = np.sign(closeadj - _sma(closeadj, 60))
    b = a * c
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_vma_pma_agree_freq_120d_jerk_v046_signal(closeadj, volume):
    k=21;a = (volume > _sma(volume, 30)).astype(float)
    c = (closeadj > _sma(closeadj, 30)).astype(float)
    agree = (a == c).astype(float).where(~_sma(volume, 30).isna() & ~_sma(closeadj, 30).isna())
    b = agree.rolling(120,120).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_avgprice_dvcum_30d_jerk_v047_signal(closeadj, volume):
    k=10;dv = closeadj * volume
    num = dv.rolling(30,30).sum()
    den = volume.rolling(30,30).sum().replace(0.0, np.nan)
    b = np.log((num / den) / closeadj)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_avgprice_dvcum_120d_jerk_v048_signal(closeadj, volume):
    k=63;dv = closeadj * volume
    num = dv.rolling(120,120).sum()
    den = volume.rolling(120,120).sum().replace(0.0, np.nan)
    b = np.log((num / den) / closeadj)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_jerk_v049_signal(volume):
    k=21;a=_sma(volume,30); c=_ema(volume,30)
    spread = a.diff(10) / a.abs() - c.diff(10) / c.abs()
    b = np.tanh(spread)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_arctan_volsma_slope_50d_jerk_v050_signal(volume):
    k=10;m=_sma(volume,50); b = np.arctan(m.diff(21) / m.abs())
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volwma_20_80_ratio_jerk_v051_signal(volume):
    k=63;b = np.log(_wma(volume, 20) / _wma(volume, 80))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volwilder_30_90_ratio_jerk_v052_signal(volume):
    k=21;b = np.log(_wilder(volume, 30) / _wilder(volume, 90))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema_posslope_frac_45d_jerk_v053_signal(volume):
    k=21;m=_ema(volume,30); pos = (m.diff(5) > 0.0).astype(float).where(~m.diff(5).isna())
    b = pos.rolling(45,45).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_posslope_frac_120d_jerk_v054_signal(volume):
    k=63;m=_sma(volume,60); pos = (m.diff(10) > 0.0).astype(float).where(~m.diff(10).isna())
    b = pos.rolling(120,120).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_vol_kernel_disp_40d_jerk_v055_signal(volume):
    k=21;n = 40
    mat = pd.concat([_sma(volume, n), _ema(volume, n), _wma(volume, n),
                     _wilder(volume, n), _hma(volume, n)], axis=1)
    b = mat.std(axis=1) / mat.mean(axis=1).replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_ribbon_order_sma_jerk_v056_signal(volume):
    k=63;sn = [_sma(volume, kk) for kk in (10, 20, 40, 80, 160)]
    cnt = pd.Series(0.0, index=volume.index); mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    b = cnt.where(mask)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_z_ema70_diff_volz_jerk_v057_signal(closeadj, volume):
    k=21;dv = closeadj * volume
    md = _ema(dv, 70); sdd = dv.rolling(70,70).std()
    zd = (dv - md) / sdd.replace(0.0, np.nan)
    mv=_ema(volume,70); sdv = volume.rolling(70,70).std()
    zv = (volume - mv) / sdv.replace(0.0, np.nan)
    b = zd - zv
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_acceleration_zscore_jerk_v058_signal(volume):
    k=21;m=_sma(volume,20)
    sl = m.diff(5) / m.abs()
    mu = sl.rolling(60,60).mean(); sd = sl.rolling(60,60).std()
    b = (sl - mu) / sd.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvolma_z_252d_jerk_v059_signal(volume):
    k=63;m = _sma(np.log(volume), 40)
    b = (m - m.rolling(252,252).mean()) / m.rolling(252,252).std().replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_cumupdn_ratio_45d_jerk_v060_signal(close, volume):
    k=21;up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(45,45).sum(); c = dn.rolling(45,45).sum()
    b = np.log(a.replace(0.0, np.nan) / c.replace(0.0, np.nan))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_dv_sma_slope_100d_jerk_v061_signal(closeadj, volume):
    k=63;dv = closeadj * volume
    b = np.sign(_sma(dv, 100).diff(63))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_normrange_60d_jerk_v062_signal(volume):
    k=63;m=_sma(volume,30)
    rng = m.rolling(60,60).max() - m.rolling(60,60).min()
    b = rng / m.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_jerk_v063_signal(close, volume):
    k=10;up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.ewm(span=30, adjust=False, min_periods=30).mean()
    c = dn.ewm(span=30, adjust=False, min_periods=30).mean()
    norm = volume.ewm(span=30, adjust=False, min_periods=30).mean().replace(0.0, np.nan)
    b = (a - c) / norm
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_klinger_34_55_jerk_v064_signal(close, volume):
    k=21;sv = np.sign(close.diff()) * volume
    a = sv.ewm(span=34, adjust=False, min_periods=34).mean()
    c = sv.ewm(span=55, adjust=False, min_periods=55).mean()
    norm = volume.ewm(span=55, adjust=False, min_periods=55).mean().replace(0.0, np.nan)
    b = (a - c) / norm
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_convergence_55d_jerk_v065_signal(volume):
    k=21;a=_ema(volume,10); c=_ema(volume,55)
    b = (a - c).abs() / c.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_jerk_v066_signal(volume):
    k=21;m=_sma(volume,40); s = np.sign(m.diff(10))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(100,100).apply(_streak_lastflip, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_jerk_v067_signal(volume):
    k=21;sn = [_sma(volume, kk) for kk in (10, 30, 90, 180)]
    mat = pd.concat(sn, axis=1); mask = mat.isna().any(axis=1)
    b = mat.rank(axis=1, pct=False).iloc[:, 1].where(~mask)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_slope_dispersion_80d_jerk_v068_signal(volume):
    k=63;sl = []
    for n in (20, 40, 60, 80, 100):
        m=_sma(volume,n)
        sl.append(m.diff(10) / m.abs())
    b = pd.concat(sl, axis=1).std(axis=1)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_ac1_60d_jerk_v069_signal(volume):
    k=21;m=_sma(volume,20).diff()
    b = m.rolling(60,60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_skew_120d_jerk_v070_signal(volume):
    k=63;sk = np.log(volume).rolling(60,60).skew()
    b = sk.ewm(span=120, adjust=False, min_periods=120).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_hma_vol_curvature_30d_jerk_v071_signal(volume):
    k=21;m=_hma(volume,30)
    b = (m - 2.0 * m.shift(10) + m.shift(20)) / m.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_volslope_short_long_jerk_v072_signal(volume):
    k=21;a=_ema(volume,15).diff(10); c=_ema(volume,60).diff(10)
    b = np.sign(a - c)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvolma_long_zscore_300d_jerk_v073_signal(volume):
    k=63;m=_sma(volume,90)
    b = (m - m.rolling(300,300).mean()) / m.rolling(300,300).std().replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_jerk_v074_signal(close, volume):
    k=63;up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(30,30).mean(); c = dn.rolling(30,30).mean()
    s = np.sign(a - c)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(200,200).apply(_streak_lastflip, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_slope_flip_freq_120d_jerk_v075_signal(volume):
    k=21;m=_sma(volume,30); s = np.sign(m.diff(5))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(120,120).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_jerk_v076_signal(volume):
    k=21;a=_wma(volume,55); c=_sma(volume,55)
    b = a.diff(21) / a.abs() - c.diff(21) / c.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_squeeze_30d_jerk_v077_signal(volume):
    k=21;n = 30
    mat = pd.concat([_sma(volume, n), _ema(volume, n), _wma(volume, n)], axis=1)
    b = mat.std(axis=1) / mat.mean(axis=1).replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_smoothvol_hurst_120d_jerk_v078_signal(volume):
    k=21;b=_sma(volume,10).diff().rolling(120,120).apply(_hurst_rs, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_jerk_v079_signal(volume):
    k=21;s = np.sign(_ema(volume, 15).diff(5) - _ema(volume, 60).diff(5))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(45,45).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logdv_olsslope_60d_jerk_v080_signal(closeadj, volume):
    k=21;b = np.log(closeadj * volume).rolling(60,60).apply(_reg_slope_norm, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logdv_olsslope_180d_jerk_v081_signal(closeadj, volume):
    k=63;b = np.log(closeadj * volume).rolling(180,180).apply(_reg_slope_norm, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logdv_rsq_90d_jerk_v082_signal(closeadj, volume):
    k=63;b = np.log(closeadj * volume).rolling(90,90).apply(_reg_rsq, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_arctan_volsma_dist_15d_jerk_v083_signal(volume):
    k=10;m=_sma(volume,15); sd = volume.rolling(15,15).std()
    b = np.arctan((volume - m) / sd.replace(0.0, np.nan))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma40_ac5_120d_jerk_v084_signal(volume):
    k=21;m=_sma(volume,40).diff()
    b = m.rolling(120,120).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_range_to_std_60d_jerk_v085_signal(volume):
    k=63;m=_sma(volume,25)
    rng = m.rolling(60,60).max() - m.rolling(60,60).min()
    sd = m.rolling(60,60).std()
    b = rng / sd.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_kernel_slope_agree_45d_jerk_v086_signal(volume):
    k=21;n = 45; kk = 10
    sl = [_sma(volume, n), _ema(volume, n), _wma(volume, n), _wilder(volume, n), _hma(volume, n)]
    pos = pd.Series(0.0, index=volume.index); neg = pd.Series(0.0, index=volume.index)
    mask = ~sl[0].isna()
    for s in sl:
        d = s.diff(kk)
        pos = pos + (d > 0.0).astype(float)
        neg = neg + (d < 0.0).astype(float)
        mask = mask & ~d.isna()
    b = (pos - neg).where(mask)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_dvma_corr_60d_jerk_v087_signal(closeadj, volume):
    k=21;a=_sma(volume,20); c = _sma(closeadj * volume, 20)
    b = a.rolling(60,60).corr(c)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_trend_rsq_120d_jerk_v088_signal(volume):
    k=63;b=_sma(volume,30).rolling(120,120).apply(_reg_rsq, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_streak_vol_osc_pos_60d_jerk_v089_signal(volume):
    k=21;above = (_sma(volume, 10) > _sma(volume, 50)).astype(float).where(~_sma(volume, 50).isna())
    b = above.rolling(60,60).apply(_consec, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_daysince_voldn_emaup_90d_jerk_v090_signal(volume):
    k=63;m=_ema(volume,40); s = np.sign(m.diff(10))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(90,90).apply(_streak_lastflip, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_elasticity_50d_jerk_v091_signal(volume):
    k=21;m=_sma(volume,50)
    dev = (volume - m).abs().rolling(10,10).mean()
    b = m.diff(10) / dev.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_netvol_ema_slope_45d_jerk_v092_signal(close, volume):
    k=21;sv = np.sign(close.diff()) * volume
    ratio = (sv.ewm(span=45, adjust=False, min_periods=45).mean() /
             volume.ewm(span=45, adjust=False, min_periods=45).mean().replace(0.0, np.nan))
    b = ratio.diff(10)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_jerk_v093_signal(close, volume):
    k=10;sv = np.sign(close.diff()) * volume
    e = sv.ewm(span=10, adjust=False, min_periods=10).mean()
    b = (e - e.rolling(75,75).mean()) / e.rolling(75,75).std().replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_ad_line_slope_120d_jerk_v094_signal(high, low, closeadj, volume):
    k=63;rng = (high - low).replace(0.0, np.nan)
    mfm = ((closeadj - low) - (high - closeadj)) / rng
    mfv = mfm * volume
    norm = volume.rolling(120,120).mean().replace(0.0, np.nan)
    b = mfv.rolling(120,120).sum() / norm
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvolma_rank_200_500d_jerk_v095_signal(volume):
    k=21;b = _sma(np.log(volume), 100).rolling(300,300).rank(pct=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_above_band_freq_45d_jerk_v096_signal(volume):
    k=21;m=_sma(volume,20); sd = volume.rolling(20,20).std()
    upper = m + sd
    above = (volume > upper).astype(float).where(~upper.isna())
    b = above.rolling(45,45).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_below_band_freq_120d_jerk_v097_signal(volume):
    k=21;m=_sma(volume,30); sd = volume.rolling(30,30).std()
    lower = m - sd
    below = (volume < lower).astype(float).where(~lower.isna())
    b = below.rolling(120,120).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_jerk_v098_signal(closeadj, volume):
    k=21;dv = closeadj * volume
    a = _sma(dv, 30); c = _sma(dv, 120)
    b = a.diff(21) / a.abs() - c.diff(21) / c.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_streak_above_volwma25_60d_jerk_v099_signal(volume):
    k=21;above = (volume > _wma(volume, 25)).astype(float).where(~_wma(volume, 25).isna())
    b = above.rolling(60,60).apply(_consec, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema_swing_180d_jerk_v100_signal(volume):
    k=21;m=_ema(volume,40)
    rng = m.rolling(180,180).max() - m.rolling(180,180).min()
    mn = m.rolling(180,180).mean().replace(0.0, np.nan)
    b = rng / mn
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_jerk_75d_jerk_v101_signal(volume):
    k=63;m=_sma(volume,75); kk = 21
    third = m - 3.0 * m.shift(kk) + 3.0 * m.shift(2 * kk) - m.shift(3 * kk)
    b = third / m.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_force_index_ema13_to_ema50_jerk_v102_signal(close, volume):
    k=10;fi = close.diff() * volume
    a = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    c = fi.ewm(span=50, adjust=False, min_periods=50).mean()
    b = a / c.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_mfi_trend_ema_30d_jerk_v103_signal(high, low, closeadj, volume):
    k=21;tp = (high + low + closeadj) / 3.0
    mf = tp * volume
    pos = mf.where(tp > tp.shift(1), 0.0); neg = mf.where(tp < tp.shift(1), 0.0)
    a = pos.ewm(span=30, adjust=False, min_periods=30).mean()
    c = neg.ewm(span=30, adjust=False, min_periods=30).mean()
    b = np.log(a.replace(0.0, np.nan) / c.replace(0.0, np.nan))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_jerk_v104_signal(volume):
    k=63;m=_sma(volume,30)
    def _f(x):
        if len(x) < 4: return np.nan
        q1 = np.quantile(x, 0.25); q3 = np.quantile(x, 0.75); med = np.median(x)
        if med == 0.0 or not np.isfinite(med): return np.nan
        return float((q3 - q1) / med)
    b = m.rolling(60,60).apply(_f, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_jerk_v105_signal(volume):
    k=63;m=_sma(volume,20)
    pct = (volume - m) / m.replace(0.0, np.nan)
    sm = pct.ewm(span=25, adjust=False, min_periods=25).mean()
    above = (sm > 0.0).astype(float).where(~sm.isna())
    b = above.rolling(60,60).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema_long_ratio_to_3sma_jerk_v106_signal(volume):
    k=21;a = np.log(_ema(volume, 180))
    c = np.log(_sma(volume, 60)).rolling(100,100).mean()
    b = a - c
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_reversion_freq_100d_jerk_v107_signal(volume):
    k=63;d = volume - _sma(volume, 20); s = np.sign(d)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(100,100).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_double_cross_volsma_jerk_v108_signal(volume):
    k=21;a = np.sign(volume - _sma(volume, 10))
    c = np.sign(_sma(volume, 10) - _sma(volume, 40))
    b = a * c
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_drawdown_from_max_252d_jerk_v109_signal(closeadj, volume):
    k=63;dv = closeadj * volume; m = _ema(dv, 30)
    mx = m.rolling(252,252).max().replace(0.0, np.nan)
    b = np.log(m / mx)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_gain_from_min_120d_jerk_v110_signal(volume):
    k=21;m=_sma(volume,30)
    mn = m.rolling(120,120).min().replace(0.0, np.nan)
    b = np.log(m / mn)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logvol_diff_over_std_30d_jerk_v111_signal(volume):
    k=21;lv = np.log(volume); sd = lv.rolling(30,30).std()
    b = (lv - lv.shift(30)) / sd.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_slope_sign_count_60d_jerk_v112_signal(volume):
    k=63;cnt = pd.Series(0.0, index=volume.index); mask = ~_sma(volume, 150).isna()
    for n in (10, 30, 60, 90, 150):
        d=_sma(volume,n).diff(10)
        cnt = cnt + (d > 0.0).astype(float)
        mask = mask & ~d.isna()
    b = cnt.where(mask)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_jerk_v113_signal(volume):
    k=63;sw=_sma(volume,30); lw=_sma(volume,180)
    sd = sw.rolling(180,180).std()
    b = (sw - lw) / sd.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema_slope_pctchg_45d_jerk_v114_signal(volume):
    k=21;sl=_ema(volume,30).diff(5); base_sl = sl.shift(45)
    b = (sl - base_sl) / base_sl.abs().replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_logdv_hurst_120d_jerk_v115_signal(closeadj, volume):
    k=21;b = np.log(closeadj * volume).diff().rolling(120,120).apply(_hurst_rs, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_upvol_downvol_ema30_jerk_v116_signal(close, volume):
    k=21;up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.ewm(span=30, adjust=False, min_periods=30).mean()
    c = dn.ewm(span=30, adjust=False, min_periods=30).mean()
    b = np.sign(a - c)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_jerk_v117_signal(volume):
    k=63;a=_sma(volume,10); c=_sma(volume,60)
    sd = volume.rolling(60,60).std()
    b = (a - c) / sd.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_bandwidth_40d_jerk_v118_signal(volume):
    k=21;m=_sma(volume,15)
    sd = m.rolling(40,40).std()
    mn = m.rolling(40,40).mean().replace(0.0, np.nan)
    b = sd / mn
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_rev_rank_300d_jerk_v119_signal(volume):
    k=63;b = 1.0 - _sma(volume, 45).rolling(300,300).rank(pct=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_center_pos_90d_jerk_v120_signal(volume):
    k=63;m=_sma(volume,20)
    mu = m.rolling(90,90).mean()
    rng = m.rolling(90,90).max() - m.rolling(90,90).min()
    b = (m - mu) / rng.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_jerk_v121_signal(volume):
    k=21;m=_sma(volume,15)
    sd = m.rolling(60,60).std()
    mad = m.rolling(60,60).apply(
        lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    b = mad / sd.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_smoothvol_skew_90d_jerk_v122_signal(volume):
    k=63;b=_sma(volume,30).rolling(90,90).skew()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_smoothvol_kurt_180d_jerk_v123_signal(volume):
    k=21;b=_sma(volume,40).rolling(180,180).kurt()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_jerk_v124_signal(volume):
    k=21;s = np.sign(_sma(volume, 30).diff(5))
    b = s.rolling(90,90).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_cum_excess_volma_120d_jerk_v125_signal(volume):
    k=21;m=_sma(volume,30); excess = (volume - m).clip(lower=0.0)
    a = excess.rolling(120,120).sum()
    c = volume.rolling(120,120).sum().replace(0.0, np.nan)
    b = a / c
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volema30_convex_frac_60d_jerk_v126_signal(volume):
    k=63;m=_ema(volume,30)
    curv = m - 2.0 * m.shift(5) + m.shift(10)
    pos = (curv > 0.0).astype(float).where(~curv.isna())
    b = pos.rolling(60,60).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_rank_180d_jerk_v127_signal(closeadj, volume):
    k=21;b = _ema(closeadj * volume, 40).rolling(180,180).rank(pct=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_daysince_volsma_signflip_252d_jerk_v128_signal(volume):
    k=63;s = np.sign(volume - _sma(volume, 40))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(252,252).apply(_streak_lastflip, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_jerk_v129_signal(close, volume):
    k=21;up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(30,30).mean(); c = dn.rolling(30,30).mean()
    za = (a - a.rolling(60,60).mean()) / a.rolling(60,60).std().replace(0.0, np.nan)
    zb = (c - c.rolling(60,60).mean()) / c.rolling(60,60).std().replace(0.0, np.nan)
    b = za - zb
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_pctroc_45d_jerk_v130_signal(volume):
    k=21;m=_sma(volume,25); b = m / m.shift(45) - 1.0
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_per_price_ma_60d_jerk_v131_signal(closeadj, volume):
    k=21;dv = closeadj * volume
    b = np.log(_ema(dv, 60) / (closeadj * _ema(volume, 60)))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_slope_consistency_120d_jerk_v132_signal(volume):
    k=21;spread=_ema(volume,30) - _ema(volume, 90)
    b = spread.rolling(120,120).apply(_reg_rsq, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_jerk_v133_signal(volume):
    k=21;o = (_sma(volume, 5) - _sma(volume, 30)) / _sma(volume, 30).replace(0.0, np.nan)
    b = o - o.shift(45)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_max_min_diff_log_252d_jerk_v134_signal(volume):
    k=63;m=_ema(volume,50)
    mx = m.rolling(252,252).max(); mn = m.rolling(252,252).min()
    b = np.log(mx / mn.replace(0.0, np.nan))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_spread_rank_252d_jerk_v135_signal(volume):
    k=21;spread=_sma(volume,15) - _sma(volume, 60)
    b = spread.rolling(252,252).rank(pct=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_jerk_v136_signal(close, volume):
    k=21;sv = np.sign(close.diff()) * volume
    a = sv.ewm(span=20, adjust=False, min_periods=20).mean()
    c = sv.ewm(span=80, adjust=False, min_periods=80).mean()
    b = np.log(a.abs().replace(0.0, np.nan) / c.abs().replace(0.0, np.nan))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_signconsistency_90d_jerk_v137_signal(volume):
    k=21;s1 = np.sign(_sma(volume, 10) - _sma(volume, 30))
    s2 = np.sign(_sma(volume, 30) - _sma(volume, 90))
    agree = (s1 == s2).astype(float).where(~s1.isna() & ~s2.isna())
    b = agree.rolling(90,90).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_ma_log_rank_252d_jerk_v138_signal(closeadj, volume):
    k=21;b = np.log(_sma(closeadj * volume, 40)).rolling(252,252).rank(pct=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_jerk_v139_signal(volume):
    k=21;m=_sma(volume,50)
    sl = m.diff(10); cu = m - 2.0 * m.shift(10) + m.shift(20)
    b = sl / cu.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sigmoid_volma_spread_70d_jerk_v140_signal(volume):
    k=63;x = np.log(_sma(volume, 20) / _sma(volume, 70))
    b = 1.0 / (1.0 + np.exp(-x))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volsma_regslope_normalized_180d_jerk_v141_signal(volume):
    k=21;b=_sma(volume,40).rolling(180,180).apply(_reg_slope_norm, raw=True)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_jerk_v142_signal(volume):
    k=21;m=_sma(volume,20)
    mid = (m.rolling(60,60).max() + m.rolling(60,60).min()) / 2.0
    above = (m > mid).astype(float).where(~mid.isna())
    b = above.rolling(120,120).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_jerk_v143_signal(closeadj, volume):
    k=21;lr = np.log(closeadj * volume).diff(30)
    b = lr.ewm(span=45, adjust=False, min_periods=45).mean()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_minus_med_120d_jerk_v144_signal(volume):
    k=21;m=_sma(volume,25); med = m.rolling(120,120).median()
    b = (m - med) / med.replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_jerk_v145_signal(volume):
    k=21;sl=_sma(volume,30).diff(10)
    b = sl / sl.shift(30).replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_log_volma_long_z_504d_jerk_v146_signal(volume):
    k=63;m = _sma(np.log(volume), 60)
    b = (m - m.rolling(504,504).mean()) / m.rolling(504,504).std().replace(0.0, np.nan)
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_sign_dv_ma_15_60_jerk_v147_signal(closeadj, volume):
    k=21;dv = closeadj * volume
    b = np.sign(_ema(dv, 15) - _ema(dv, 60))
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_jerk_v148_signal(closeadj, volume):
    k=21;a=_sma(volume,60); c = _sma(closeadj, 60)
    b = a.diff(21) / a.abs() - c.diff(21) / c.abs()
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_dv_ema_range_norm_252d_jerk_v149_signal(closeadj, volume):
    k=63;m = _ema(closeadj * volume, 30)
    rng = m.rolling(252,252).max() - m.rolling(252,252).min()
    mn = m.rolling(252,252).mean().replace(0.0, np.nan)
    b = rng / mn
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f22vt_f22_volume_trend_composite_volma_score_jerk_v150_signal(volume):
    k=21;a = np.sign(_sma(volume, 20) - _sma(volume, 80))
    c = np.sign(_sma(volume, 80).diff(21))
    d=_sma(volume,20).rolling(252,252).rank(pct=True) - 0.5
    b = a + c + d
    return (b-2*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)


f22_volume_trend_jerk_001_150_REGISTRY = {
    "f22vt_f22_volume_trend_logvol_sma_8d_jerk_v001_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_sma_8d_jerk_v001_signal},
    "f22vt_f22_volume_trend_volsmadiff_50_200_jerk_v002_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsmadiff_50_200_jerk_v002_signal},
    "f22vt_f22_volume_trend_logvol_sma_200d_resid_jerk_v003_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_sma_200d_resid_jerk_v003_signal},
    "f22vt_f22_volume_trend_volsma_volwma_diff_20d_jerk_v004_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_volwma_diff_20d_jerk_v004_signal},
    "f22vt_f22_volume_trend_volwilder_acceleration_40d_jerk_v005_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volwilder_acceleration_40d_jerk_v005_signal},
    "f22vt_f22_volume_trend_vol_sma_5_50_ratio_jerk_v006_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_vol_sma_5_50_ratio_jerk_v006_signal},
    "f22vt_f22_volume_trend_vol_ema_10_120_ratio_jerk_v007_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_vol_ema_10_120_ratio_jerk_v007_signal},
    "f22vt_f22_volume_trend_vol_wma_sma_diff_60d_jerk_v008_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_vol_wma_sma_diff_60d_jerk_v008_signal},
    "f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_jerk_v009_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_jerk_v009_signal},
    "f22vt_f22_volume_trend_volema_xover_freq_120d_jerk_v010_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema_xover_freq_120d_jerk_v010_signal},
    "f22vt_f22_volume_trend_sign_vol_sma_21_jerk_v011_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_sign_vol_sma_21_jerk_v011_signal},
    "f22vt_f22_volume_trend_sign_volsma_5_20_jerk_v012_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_sign_volsma_5_20_jerk_v012_signal},
    "f22vt_f22_volume_trend_sign_volema_30_90_jerk_v013_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_sign_volema_30_90_jerk_v013_signal},
    "f22vt_f22_volume_trend_sign_volwilder_sma_60d_jerk_v014_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_sign_volwilder_sma_60d_jerk_v014_signal},
    "f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_jerk_v015_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_jerk_v015_signal},
    "f22vt_f22_volume_trend_daysince_volsma_5_50_180d_jerk_v016_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_daysince_volsma_5_50_180d_jerk_v016_signal},
    "f22vt_f22_volume_trend_streak_above_volsma20_45d_jerk_v017_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_streak_above_volsma20_45d_jerk_v017_signal},
    "f22vt_f22_volume_trend_streak_below_volema50_140d_jerk_v018_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_streak_below_volema50_140d_jerk_v018_signal},
    "f22vt_f22_volume_trend_volsma25_slope_jerk_v019_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma25_slope_jerk_v019_signal},
    "f22vt_f22_volume_trend_volema80_slope_jerk_v020_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema80_slope_jerk_v020_signal},
    "f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_jerk_v021_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_jerk_v021_signal},
    "f22vt_f22_volume_trend_volema30_curv_jerk_v022_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema30_curv_jerk_v022_signal},
    "f22vt_f22_volume_trend_volsma60_curv_jerk_v023_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma60_curv_jerk_v023_signal},
    "f22vt_f22_volume_trend_volz_sma25_jerk_v024_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volz_sma25_jerk_v024_signal},
    "f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_jerk_v025_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_jerk_v025_signal},
    "f22vt_f22_volume_trend_rank_volsma15_90d_jerk_v026_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_rank_volsma15_90d_jerk_v026_signal},
    "f22vt_f22_volume_trend_rank_volema60_252d_jerk_v027_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_rank_volema60_252d_jerk_v027_signal},
    "f22vt_f22_volume_trend_stoch_volsma_30_120d_jerk_v028_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_stoch_volsma_30_120d_jerk_v028_signal},
    "f22vt_f22_volume_trend_stoch_volema_70_252d_jerk_v029_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_stoch_volema_70_252d_jerk_v029_signal},
    "f22vt_f22_volume_trend_logvol_roc_21d_jerk_v030_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_roc_21d_jerk_v030_signal},
    "f22vt_f22_volume_trend_logvol_roc_63d_jerk_v031_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_roc_63d_jerk_v031_signal},
    "f22vt_f22_volume_trend_volsma_slope_spread_10_50_jerk_v032_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_slope_spread_10_50_jerk_v032_signal},
    "f22vt_f22_volume_trend_volema_slope_spread_20_120_jerk_v033_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema_slope_spread_20_120_jerk_v033_signal},
    "f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_jerk_v034_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_jerk_v034_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ratio_60d_jerk_v035_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_upvol_downvol_ratio_60d_jerk_v035_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ratio_150d_jerk_v036_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_upvol_downvol_ratio_150d_jerk_v036_signal},
    "f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_jerk_v037_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_jerk_v037_signal},
    "f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_jerk_v038_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_jerk_v038_signal},
    "f22vt_f22_volume_trend_dv_ema_25_100_ratio_jerk_v039_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_ema_25_100_ratio_jerk_v039_signal},
    "f22vt_f22_volume_trend_dv_sma60_slope_jerk_v040_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_sma60_slope_jerk_v040_signal},
    "f22vt_f22_volume_trend_logvol_olsslope_30d_jerk_v041_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_olsslope_30d_jerk_v041_signal},
    "f22vt_f22_volume_trend_logvol_olsslope_120d_jerk_v042_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_olsslope_120d_jerk_v042_signal},
    "f22vt_f22_volume_trend_logvol_rsq_45d_jerk_v043_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_rsq_45d_jerk_v043_signal},
    "f22vt_f22_volume_trend_logvol_rsq_180d_jerk_v044_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_rsq_180d_jerk_v044_signal},
    "f22vt_f22_volume_trend_vma_pma_agree_sign_60d_jerk_v045_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_vma_pma_agree_sign_60d_jerk_v045_signal},
    "f22vt_f22_volume_trend_vma_pma_agree_freq_120d_jerk_v046_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_vma_pma_agree_freq_120d_jerk_v046_signal},
    "f22vt_f22_volume_trend_avgprice_dvcum_30d_jerk_v047_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_avgprice_dvcum_30d_jerk_v047_signal},
    "f22vt_f22_volume_trend_avgprice_dvcum_120d_jerk_v048_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_avgprice_dvcum_120d_jerk_v048_signal},
    "f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_jerk_v049_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_jerk_v049_signal},
    "f22vt_f22_volume_trend_arctan_volsma_slope_50d_jerk_v050_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_arctan_volsma_slope_50d_jerk_v050_signal},
    "f22vt_f22_volume_trend_volwma_20_80_ratio_jerk_v051_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volwma_20_80_ratio_jerk_v051_signal},
    "f22vt_f22_volume_trend_volwilder_30_90_ratio_jerk_v052_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volwilder_30_90_ratio_jerk_v052_signal},
    "f22vt_f22_volume_trend_volema_posslope_frac_45d_jerk_v053_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema_posslope_frac_45d_jerk_v053_signal},
    "f22vt_f22_volume_trend_volsma_posslope_frac_120d_jerk_v054_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_posslope_frac_120d_jerk_v054_signal},
    "f22vt_f22_volume_trend_vol_kernel_disp_40d_jerk_v055_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_vol_kernel_disp_40d_jerk_v055_signal},
    "f22vt_f22_volume_trend_ribbon_order_sma_jerk_v056_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_ribbon_order_sma_jerk_v056_signal},
    "f22vt_f22_volume_trend_dv_z_ema70_diff_volz_jerk_v057_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_z_ema70_diff_volz_jerk_v057_signal},
    "f22vt_f22_volume_trend_volsma_acceleration_zscore_jerk_v058_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_acceleration_zscore_jerk_v058_signal},
    "f22vt_f22_volume_trend_logvolma_z_252d_jerk_v059_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvolma_z_252d_jerk_v059_signal},
    "f22vt_f22_volume_trend_cumupdn_ratio_45d_jerk_v060_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_cumupdn_ratio_45d_jerk_v060_signal},
    "f22vt_f22_volume_trend_sign_dv_sma_slope_100d_jerk_v061_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_sign_dv_sma_slope_100d_jerk_v061_signal},
    "f22vt_f22_volume_trend_volsma_normrange_60d_jerk_v062_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_normrange_60d_jerk_v062_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_jerk_v063_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_jerk_v063_signal},
    "f22vt_f22_volume_trend_klinger_34_55_jerk_v064_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_klinger_34_55_jerk_v064_signal},
    "f22vt_f22_volume_trend_volma_convergence_55d_jerk_v065_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_convergence_55d_jerk_v065_signal},
    "f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_jerk_v066_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_jerk_v066_signal},
    "f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_jerk_v067_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_jerk_v067_signal},
    "f22vt_f22_volume_trend_volma_slope_dispersion_80d_jerk_v068_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_slope_dispersion_80d_jerk_v068_signal},
    "f22vt_f22_volume_trend_volsma_ac1_60d_jerk_v069_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_ac1_60d_jerk_v069_signal},
    "f22vt_f22_volume_trend_logvol_skew_120d_jerk_v070_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_skew_120d_jerk_v070_signal},
    "f22vt_f22_volume_trend_hma_vol_curvature_30d_jerk_v071_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_hma_vol_curvature_30d_jerk_v071_signal},
    "f22vt_f22_volume_trend_sign_volslope_short_long_jerk_v072_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_sign_volslope_short_long_jerk_v072_signal},
    "f22vt_f22_volume_trend_logvolma_long_zscore_300d_jerk_v073_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvolma_long_zscore_300d_jerk_v073_signal},
    "f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_jerk_v074_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_jerk_v074_signal},
    "f22vt_f22_volume_trend_volma_slope_flip_freq_120d_jerk_v075_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_slope_flip_freq_120d_jerk_v075_signal},
    "f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_jerk_v076_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_jerk_v076_signal},
    "f22vt_f22_volume_trend_volma_squeeze_30d_jerk_v077_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_squeeze_30d_jerk_v077_signal},
    "f22vt_f22_volume_trend_smoothvol_hurst_120d_jerk_v078_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_smoothvol_hurst_120d_jerk_v078_signal},
    "f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_jerk_v079_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_jerk_v079_signal},
    "f22vt_f22_volume_trend_logdv_olsslope_60d_jerk_v080_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_logdv_olsslope_60d_jerk_v080_signal},
    "f22vt_f22_volume_trend_logdv_olsslope_180d_jerk_v081_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_logdv_olsslope_180d_jerk_v081_signal},
    "f22vt_f22_volume_trend_logdv_rsq_90d_jerk_v082_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_logdv_rsq_90d_jerk_v082_signal},
    "f22vt_f22_volume_trend_arctan_volsma_dist_15d_jerk_v083_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_arctan_volsma_dist_15d_jerk_v083_signal},
    "f22vt_f22_volume_trend_volsma40_ac5_120d_jerk_v084_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma40_ac5_120d_jerk_v084_signal},
    "f22vt_f22_volume_trend_volsma_range_to_std_60d_jerk_v085_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_range_to_std_60d_jerk_v085_signal},
    "f22vt_f22_volume_trend_kernel_slope_agree_45d_jerk_v086_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_kernel_slope_agree_45d_jerk_v086_signal},
    "f22vt_f22_volume_trend_volma_dvma_corr_60d_jerk_v087_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_volma_dvma_corr_60d_jerk_v087_signal},
    "f22vt_f22_volume_trend_volsma_trend_rsq_120d_jerk_v088_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_trend_rsq_120d_jerk_v088_signal},
    "f22vt_f22_volume_trend_streak_vol_osc_pos_60d_jerk_v089_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_streak_vol_osc_pos_60d_jerk_v089_signal},
    "f22vt_f22_volume_trend_daysince_voldn_emaup_90d_jerk_v090_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_daysince_voldn_emaup_90d_jerk_v090_signal},
    "f22vt_f22_volume_trend_volma_elasticity_50d_jerk_v091_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_elasticity_50d_jerk_v091_signal},
    "f22vt_f22_volume_trend_netvol_ema_slope_45d_jerk_v092_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_netvol_ema_slope_45d_jerk_v092_signal},
    "f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_jerk_v093_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_jerk_v093_signal},
    "f22vt_f22_volume_trend_ad_line_slope_120d_jerk_v094_signal": {"inputs":["high","low","closeadj","volume"],"func":f22vt_f22_volume_trend_ad_line_slope_120d_jerk_v094_signal},
    "f22vt_f22_volume_trend_logvolma_rank_200_500d_jerk_v095_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvolma_rank_200_500d_jerk_v095_signal},
    "f22vt_f22_volume_trend_volsma_above_band_freq_45d_jerk_v096_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_above_band_freq_45d_jerk_v096_signal},
    "f22vt_f22_volume_trend_volsma_below_band_freq_120d_jerk_v097_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_below_band_freq_120d_jerk_v097_signal},
    "f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_jerk_v098_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_jerk_v098_signal},
    "f22vt_f22_volume_trend_streak_above_volwma25_60d_jerk_v099_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_streak_above_volwma25_60d_jerk_v099_signal},
    "f22vt_f22_volume_trend_volema_swing_180d_jerk_v100_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema_swing_180d_jerk_v100_signal},
    "f22vt_f22_volume_trend_volsma_jerk_75d_jerk_v101_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_jerk_75d_jerk_v101_signal},
    "f22vt_f22_volume_trend_force_index_ema13_to_ema50_jerk_v102_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_force_index_ema13_to_ema50_jerk_v102_signal},
    "f22vt_f22_volume_trend_mfi_trend_ema_30d_jerk_v103_signal": {"inputs":["high","low","closeadj","volume"],"func":f22vt_f22_volume_trend_mfi_trend_ema_30d_jerk_v103_signal},
    "f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_jerk_v104_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_jerk_v104_signal},
    "f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_jerk_v105_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_jerk_v105_signal},
    "f22vt_f22_volume_trend_volema_long_ratio_to_3sma_jerk_v106_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema_long_ratio_to_3sma_jerk_v106_signal},
    "f22vt_f22_volume_trend_volma_reversion_freq_100d_jerk_v107_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_reversion_freq_100d_jerk_v107_signal},
    "f22vt_f22_volume_trend_sign_double_cross_volsma_jerk_v108_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_sign_double_cross_volsma_jerk_v108_signal},
    "f22vt_f22_volume_trend_dv_drawdown_from_max_252d_jerk_v109_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_drawdown_from_max_252d_jerk_v109_signal},
    "f22vt_f22_volume_trend_volma_gain_from_min_120d_jerk_v110_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_gain_from_min_120d_jerk_v110_signal},
    "f22vt_f22_volume_trend_logvol_diff_over_std_30d_jerk_v111_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_logvol_diff_over_std_30d_jerk_v111_signal},
    "f22vt_f22_volume_trend_volma_slope_sign_count_60d_jerk_v112_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_slope_sign_count_60d_jerk_v112_signal},
    "f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_jerk_v113_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_jerk_v113_signal},
    "f22vt_f22_volume_trend_volema_slope_pctchg_45d_jerk_v114_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema_slope_pctchg_45d_jerk_v114_signal},
    "f22vt_f22_volume_trend_logdv_hurst_120d_jerk_v115_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_logdv_hurst_120d_jerk_v115_signal},
    "f22vt_f22_volume_trend_sign_upvol_downvol_ema30_jerk_v116_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_sign_upvol_downvol_ema30_jerk_v116_signal},
    "f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_jerk_v117_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_jerk_v117_signal},
    "f22vt_f22_volume_trend_volma_bandwidth_40d_jerk_v118_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_bandwidth_40d_jerk_v118_signal},
    "f22vt_f22_volume_trend_volsma_rev_rank_300d_jerk_v119_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_rev_rank_300d_jerk_v119_signal},
    "f22vt_f22_volume_trend_volsma_center_pos_90d_jerk_v120_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_center_pos_90d_jerk_v120_signal},
    "f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_jerk_v121_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_jerk_v121_signal},
    "f22vt_f22_volume_trend_smoothvol_skew_90d_jerk_v122_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_smoothvol_skew_90d_jerk_v122_signal},
    "f22vt_f22_volume_trend_smoothvol_kurt_180d_jerk_v123_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_smoothvol_kurt_180d_jerk_v123_signal},
    "f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_jerk_v124_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_jerk_v124_signal},
    "f22vt_f22_volume_trend_cum_excess_volma_120d_jerk_v125_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_cum_excess_volma_120d_jerk_v125_signal},
    "f22vt_f22_volume_trend_volema30_convex_frac_60d_jerk_v126_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volema30_convex_frac_60d_jerk_v126_signal},
    "f22vt_f22_volume_trend_dv_rank_180d_jerk_v127_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_rank_180d_jerk_v127_signal},
    "f22vt_f22_volume_trend_daysince_volsma_signflip_252d_jerk_v128_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_daysince_volsma_signflip_252d_jerk_v128_signal},
    "f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_jerk_v129_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_jerk_v129_signal},
    "f22vt_f22_volume_trend_volsma_pctroc_45d_jerk_v130_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_pctroc_45d_jerk_v130_signal},
    "f22vt_f22_volume_trend_dv_per_price_ma_60d_jerk_v131_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_per_price_ma_60d_jerk_v131_signal},
    "f22vt_f22_volume_trend_volma_slope_consistency_120d_jerk_v132_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_slope_consistency_120d_jerk_v132_signal},
    "f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_jerk_v133_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_jerk_v133_signal},
    "f22vt_f22_volume_trend_volma_max_min_diff_log_252d_jerk_v134_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_max_min_diff_log_252d_jerk_v134_signal},
    "f22vt_f22_volume_trend_volma_spread_rank_252d_jerk_v135_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_spread_rank_252d_jerk_v135_signal},
    "f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_jerk_v136_signal": {"inputs":["close","volume"],"func":f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_jerk_v136_signal},
    "f22vt_f22_volume_trend_volma_signconsistency_90d_jerk_v137_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_signconsistency_90d_jerk_v137_signal},
    "f22vt_f22_volume_trend_dv_ma_log_rank_252d_jerk_v138_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_ma_log_rank_252d_jerk_v138_signal},
    "f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_jerk_v139_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_jerk_v139_signal},
    "f22vt_f22_volume_trend_sigmoid_volma_spread_70d_jerk_v140_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_sigmoid_volma_spread_70d_jerk_v140_signal},
    "f22vt_f22_volume_trend_volsma_regslope_normalized_180d_jerk_v141_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volsma_regslope_normalized_180d_jerk_v141_signal},
    "f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_jerk_v142_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_jerk_v142_signal},
    "f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_jerk_v143_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_jerk_v143_signal},
    "f22vt_f22_volume_trend_volma_minus_med_120d_jerk_v144_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_minus_med_120d_jerk_v144_signal},
    "f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_jerk_v145_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_jerk_v145_signal},
    "f22vt_f22_volume_trend_log_volma_long_z_504d_jerk_v146_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_log_volma_long_z_504d_jerk_v146_signal},
    "f22vt_f22_volume_trend_sign_dv_ma_15_60_jerk_v147_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_sign_dv_ma_15_60_jerk_v147_signal},
    "f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_jerk_v148_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_jerk_v148_signal},
    "f22vt_f22_volume_trend_dv_ema_range_norm_252d_jerk_v149_signal": {"inputs":["closeadj","volume"],"func":f22vt_f22_volume_trend_dv_ema_range_norm_252d_jerk_v149_signal},
    "f22vt_f22_volume_trend_composite_volma_score_jerk_v150_signal": {"inputs":["volume"],"func":f22vt_f22_volume_trend_composite_volma_score_jerk_v150_signal},
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
    for name, entry in f22_volume_trend_jerk_001_150_REGISTRY.items():
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
