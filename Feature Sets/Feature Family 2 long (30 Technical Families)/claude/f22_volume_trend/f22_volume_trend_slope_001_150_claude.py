"""f22_volume_trend slope features 001-150 (1st derivative).
Each function spells its base formula inline (smoothed/trended volume), then
returns base.diff(k).replace([inf,-inf],nan). k follows the ROC bracket of
the base's primary window:  <=5d:k=5;  6-21d:k=5 or 10;  22-63d:k=10 or 21;
64-200d:k=21 or 63;  >200d:k=63. NaN policy: only the final replace().
"""
from __future__ import annotations
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (smoothing primitives)
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# Slope features 001-150 (1st derivative of each base feature)
# ---------------------------------------------------------------------------


def f22vt_f22_volume_trend_logvol_sma_8d_slope_v001_signal(volume):
    return np.log(volume / _sma(volume, 8)).diff(5).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsmadiff_50_200_slope_v002_signal(volume):
    return np.log(_sma(volume, 50) / _sma(volume, 200)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_sma_200d_resid_slope_v003_signal(volume):
    return (np.log(volume / _sma(volume, 200)) - np.log(volume / _sma(volume, 40))).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_volwma_diff_20d_slope_v004_signal(volume):
    return np.log(_sma(volume, 20) / _wma(volume, 20)).diff(5).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volwilder_acceleration_40d_slope_v005_signal(volume):
    a = _wilder(volume, 40)
    return ((a - 2.0 * a.shift(21) + a.shift(42)) / a.abs()).diff(10).replace([np.inf, -np.inf], np.nan)




def f22vt_f22_volume_trend_vol_ema_10_120_ratio_slope_v007_signal(volume):
    return np.log(_ema(volume, 10) / _ema(volume, 120)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_vol_wma_sma_diff_60d_slope_v008_signal(volume):
    return np.log(_wma(volume, 60) / _sma(volume, 60)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_slope_v009_signal(volume):
    s1 = (_sma(volume, 5) - _sma(volume, 50)) / _sma(volume, 50)
    s2 = (_ema(volume, 10) - _ema(volume, 40)) / _ema(volume, 40)
    return (s1 - s2).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema_xover_freq_120d_slope_v010_signal(volume):
    s = np.sign(_ema(volume, 10) - _ema(volume, 40))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).mean().diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_vol_sma_21_slope_v011_signal(volume):
    return np.sign(volume - _sma(volume, 21)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_volsma_5_20_slope_v012_signal(volume):
    return np.sign(_sma(volume, 5) - _sma(volume, 20)).diff(5).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_volema_30_90_slope_v013_signal(volume):
    return np.sign(_ema(volume, 30) - _ema(volume, 90)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_volwilder_sma_60d_slope_v014_signal(volume):
    return np.sign(_wilder(volume, 60) - _sma(volume, 60)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_slope_v015_signal(volume):
    s = np.sign(volume - _sma(volume, 21))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).apply(_streak_lastflip, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_daysince_volsma_5_50_180d_slope_v016_signal(volume):
    s = np.sign(_sma(volume, 5) - _sma(volume, 50))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(180, min_periods=180).apply(_streak_lastflip, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_streak_above_volsma20_45d_slope_v017_signal(volume):
    above = (volume > _sma(volume, 20)).astype(float).where(~_sma(volume, 20).isna())
    return above.rolling(45, min_periods=45).apply(_consec, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_streak_below_volema50_140d_slope_v018_signal(volume):
    below = (volume < _ema(volume, 50)).astype(float).where(~_ema(volume, 50).isna())
    return below.rolling(140, min_periods=140).apply(_consec, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma25_slope_slope_v019_signal(volume):
    m = _sma(volume, 25)
    return (m.diff(10) / m.abs()).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema80_slope_slope_v020_signal(volume):
    m = _ema(volume, 80)
    return (m.diff(21) / m.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_slope_v021_signal(volume):
    a = _wma(volume, 40); b = _sma(volume, 80)
    return (a.diff(10) / a.abs() - b.diff(10) / b.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema30_curv_slope_v022_signal(volume):
    m = _ema(volume, 30)
    return ((m - 2.0 * m.shift(10) + m.shift(20)) / m.abs()).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma60_curv_slope_v023_signal(volume):
    m = _sma(volume, 60)
    return ((m - 2.0 * m.shift(21) + m.shift(42)) / m.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volz_sma25_slope_v024_signal(volume):
    m = _sma(volume, 25); sd = volume.rolling(25, min_periods=25).std()
    return ((volume - m) / sd.replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_slope_v025_signal(volume):
    m1 = _sma(volume, 25); sd1 = volume.rolling(25, min_periods=25).std()
    m2 = _ema(volume, 90); sd2 = volume.rolling(90, min_periods=90).std()
    z1 = (volume - m1) / sd1.replace(0.0, np.nan)
    z2 = (volume - m2) / sd2.replace(0.0, np.nan)
    return (z2 - z1).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_rank_volsma15_90d_slope_v026_signal(volume):
    return _sma(volume, 15).rolling(90, min_periods=90).rank(pct=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_rank_volema60_252d_slope_v027_signal(volume):
    return _ema(volume, 60).rolling(252, min_periods=252).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_stoch_volsma_30_120d_slope_v028_signal(volume):
    m = _sma(volume, 30)
    mn = m.rolling(120, min_periods=120).min(); mx = m.rolling(120, min_periods=120).max()
    return ((m - mn) / (mx - mn).replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_stoch_volema_70_252d_slope_v029_signal(volume):
    m = _ema(volume, 70)
    mn = m.rolling(252, min_periods=252).min(); mx = m.rolling(252, min_periods=252).max()
    return ((m - mn) / (mx - mn).replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_roc_21d_slope_v030_signal(volume):
    return np.log(volume / volume.shift(21)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_roc_63d_slope_v031_signal(volume):
    return np.log(volume / volume.shift(63)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_slope_spread_10_50_slope_v032_signal(volume):
    m10 = _sma(volume, 10); m50 = _sma(volume, 50)
    s10 = m10.diff(10) / m10.abs(); s50 = m50.diff(10) / m50.abs()
    return (s10 - s50).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema_slope_spread_20_120_slope_v033_signal(volume):
    m20 = _ema(volume, 20); m120 = _ema(volume, 120)
    s20 = m20.diff(21) / m20.abs(); s120 = m120.diff(21) / m120.abs()
    return (s20 - s120).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_slope_v034_signal(close, volume):
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    long_avg = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    diff = up.rolling(30, min_periods=30).mean() - dn.rolling(30, min_periods=30).mean()
    return (diff / long_avg).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_upvol_downvol_ratio_60d_slope_v035_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0.0, 0.0)
    dn = volume.where(closeadj.diff() < 0.0, 0.0)
    a = up.rolling(60, min_periods=60).mean()
    b = dn.rolling(60, min_periods=60).mean()
    return np.log(a.replace(0.0, np.nan) / b.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_upvol_downvol_ratio_150d_slope_v036_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0.0, 0.0)
    dn = volume.where(closeadj.diff() < 0.0, 0.0)
    a = up.ewm(span=150, adjust=False, min_periods=150).mean()
    b = dn.ewm(span=150, adjust=False, min_periods=150).mean()
    return np.log(a.replace(0.0, np.nan) / b.replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_slope_v037_signal(closeadj, volume):
    dv = closeadj * volume
    a = _ema(dv, 40); b = _ema(dv, 120)
    return (a.diff(21) / a.abs() - b.diff(21) / b.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_slope_v038_signal(closeadj, volume):
    dv = closeadj * volume
    return (np.log(_sma(dv, 120)) - np.log(_sma(dv, 40))).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_ema_25_100_ratio_slope_v039_signal(closeadj, volume):
    dv = closeadj * volume
    return np.log(_ema(dv, 25) / _ema(dv, 100)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_sma60_slope_slope_v040_signal(closeadj, volume):
    dv = closeadj * volume; m = _sma(dv, 60)
    return (m.diff(21) / m.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_olsslope_30d_slope_v041_signal(volume):
    return np.log(volume).rolling(30, min_periods=30).apply(_reg_slope_norm, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_olsslope_120d_slope_v042_signal(volume):
    return np.log(volume).rolling(120, min_periods=120).apply(_reg_slope_norm, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_rsq_45d_slope_v043_signal(volume):
    return np.log(volume).rolling(45, min_periods=45).apply(_reg_rsq, raw=True).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_rsq_180d_slope_v044_signal(volume):
    return np.log(volume).rolling(180, min_periods=180).apply(_reg_rsq, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_vma_pma_agree_sign_60d_slope_v045_signal(closeadj, volume):
    a = np.sign(volume - _sma(volume, 60))
    b = np.sign(closeadj - _sma(closeadj, 60))
    return (a * b).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_vma_pma_agree_freq_120d_slope_v046_signal(closeadj, volume):
    a = (volume > _sma(volume, 30)).astype(float)
    b = (closeadj > _sma(closeadj, 30)).astype(float)
    agree = (a == b).astype(float).where(~_sma(volume, 30).isna() & ~_sma(closeadj, 30).isna())
    return agree.rolling(120, min_periods=120).mean().diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_avgprice_dvcum_30d_slope_v047_signal(closeadj, volume):
    dv = closeadj * volume
    num = dv.rolling(30, min_periods=30).sum()
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return np.log((num / den) / closeadj).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_avgprice_dvcum_120d_slope_v048_signal(closeadj, volume):
    dv = closeadj * volume
    num = dv.rolling(120, min_periods=120).sum()
    den = volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return np.log((num / den) / closeadj).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_slope_v049_signal(volume):
    a = _sma(volume, 30); b = _ema(volume, 30)
    spread = a.diff(10) / a.abs() - b.diff(10) / b.abs()
    return np.tanh(spread).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_arctan_volsma_slope_50d_slope_v050_signal(volume):
    m = _sma(volume, 50)
    return np.arctan(m.diff(21) / m.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volwma_20_80_ratio_slope_v051_signal(volume):
    return np.log(_wma(volume, 20) / _wma(volume, 80)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volwilder_30_90_ratio_slope_v052_signal(volume):
    return np.log(_wilder(volume, 30) / _wilder(volume, 90)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema_posslope_frac_45d_slope_v053_signal(volume):
    m = _ema(volume, 30)
    pos = (m.diff(5) > 0.0).astype(float).where(~m.diff(5).isna())
    return pos.rolling(45, min_periods=45).mean().diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_posslope_frac_120d_slope_v054_signal(volume):
    m = _sma(volume, 60)
    pos = (m.diff(10) > 0.0).astype(float).where(~m.diff(10).isna())
    return pos.rolling(120, min_periods=120).mean().diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_vol_kernel_disp_40d_slope_v055_signal(volume):
    n = 40
    mat = pd.concat([_sma(volume, n), _ema(volume, n), _wma(volume, n),
                     _wilder(volume, n), _hma(volume, n)], axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1).replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_ribbon_order_sma_slope_v056_signal(volume):
    sn = [_sma(volume, k) for k in (10, 20, 40, 80, 160)]
    cnt = pd.Series(0.0, index=volume.index); mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    return cnt.where(mask).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_z_ema70_diff_volz_slope_v057_signal(closeadj, volume):
    dv = closeadj * volume
    md = _ema(dv, 70); sdd = dv.rolling(70, min_periods=70).std()
    zd = (dv - md) / sdd.replace(0.0, np.nan)
    mv = _ema(volume, 70); sdv = volume.rolling(70, min_periods=70).std()
    zv = (volume - mv) / sdv.replace(0.0, np.nan)
    return (zd - zv).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_acceleration_zscore_slope_v058_signal(volume):
    m = _sma(volume, 20)
    sl = m.diff(5) / m.abs()
    mu = sl.rolling(60, min_periods=60).mean(); sd = sl.rolling(60, min_periods=60).std()
    return ((sl - mu) / sd.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvolma_z_252d_slope_v059_signal(volume):
    m = _sma(np.log(volume), 40)
    return ((m - m.rolling(252, min_periods=252).mean()) /
            m.rolling(252, min_periods=252).std().replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_cumupdn_ratio_45d_slope_v060_signal(close, volume):
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(45, min_periods=45).sum()
    b = dn.rolling(45, min_periods=45).sum()
    return np.log(a.replace(0.0, np.nan) / b.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_dv_sma_slope_100d_slope_v061_signal(closeadj, volume):
    dv = closeadj * volume
    return np.sign(_sma(dv, 100).diff(63)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_normrange_60d_slope_v062_signal(volume):
    m = _sma(volume, 30)
    rng = m.rolling(60, min_periods=60).max() - m.rolling(60, min_periods=60).min()
    return (rng / m.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_slope_v063_signal(close, volume):
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.ewm(span=30, adjust=False, min_periods=30).mean()
    b = dn.ewm(span=30, adjust=False, min_periods=30).mean()
    norm = volume.ewm(span=30, adjust=False, min_periods=30).mean().replace(0.0, np.nan)
    return ((a - b) / norm).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_klinger_34_55_slope_v064_signal(close, volume):
    sv = np.sign(close.diff()) * volume
    a = sv.ewm(span=34, adjust=False, min_periods=34).mean()
    b = sv.ewm(span=55, adjust=False, min_periods=55).mean()
    norm = volume.ewm(span=55, adjust=False, min_periods=55).mean().replace(0.0, np.nan)
    return ((a - b) / norm).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_convergence_55d_slope_v065_signal(volume):
    a = _ema(volume, 10); b = _ema(volume, 55)
    return ((a - b).abs() / b.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_slope_v066_signal(volume):
    m = _sma(volume, 40); s = np.sign(m.diff(10))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(100, min_periods=100).apply(_streak_lastflip, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_slope_v067_signal(volume):
    sn = [_sma(volume, k) for k in (10, 30, 90, 180)]
    mat = pd.concat(sn, axis=1); mask = mat.isna().any(axis=1)
    return mat.rank(axis=1, pct=False).iloc[:, 1].where(~mask).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_slope_dispersion_80d_slope_v068_signal(volume):
    sl = []
    for n in (20, 40, 60, 80, 100):
        m = _sma(volume, n)
        sl.append(m.diff(10) / m.abs())
    return pd.concat(sl, axis=1).std(axis=1).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_ac1_60d_slope_v069_signal(volume):
    m = _sma(volume, 20).diff()
    return m.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=True
    ).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_skew_120d_slope_v070_signal(volume):
    sk = np.log(volume).rolling(60, min_periods=60).skew()
    return sk.ewm(span=120, adjust=False, min_periods=120).mean().diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_hma_vol_curvature_30d_slope_v071_signal(volume):
    m = _hma(volume, 30)
    return ((m - 2.0 * m.shift(10) + m.shift(20)) / m.abs()).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_volslope_short_long_slope_v072_signal(volume):
    a = _ema(volume, 15).diff(10); b = _ema(volume, 60).diff(10)
    return np.sign(a - b).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvolma_long_zscore_300d_slope_v073_signal(volume):
    m = _sma(volume, 90)
    return ((m - m.rolling(300, min_periods=300).mean()) /
            m.rolling(300, min_periods=300).std().replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_slope_v074_signal(close, volume):
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(30, min_periods=30).mean(); b = dn.rolling(30, min_periods=30).mean()
    s = np.sign(a - b)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(200, min_periods=200).apply(_streak_lastflip, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_slope_flip_freq_120d_slope_v075_signal(volume):
    m = _sma(volume, 30); s = np.sign(m.diff(5))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).mean().diff(21).replace([np.inf, -np.inf], np.nan)


# === Slopes 076-150 (correspond to base 076-150) ===========================


def f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_slope_v076_signal(volume):
    a = _wma(volume, 55); b = _sma(volume, 55)
    return (a.diff(21) / a.abs() - b.diff(21) / b.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_squeeze_30d_slope_v077_signal(volume):
    n = 30
    mat = pd.concat([_sma(volume, n), _ema(volume, n), _wma(volume, n)], axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1).replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_smoothvol_hurst_120d_slope_v078_signal(volume):
    return _sma(volume, 10).diff().rolling(120, min_periods=120).apply(_hurst_rs, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_slope_v079_signal(volume):
    s = np.sign(_ema(volume, 15).diff(5) - _ema(volume, 60).diff(5))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(45, min_periods=45).mean().diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logdv_olsslope_60d_slope_v080_signal(closeadj, volume):
    return np.log(closeadj * volume).rolling(60, min_periods=60).apply(_reg_slope_norm, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logdv_olsslope_180d_slope_v081_signal(closeadj, volume):
    return np.log(closeadj * volume).rolling(180, min_periods=180).apply(_reg_slope_norm, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logdv_rsq_90d_slope_v082_signal(closeadj, volume):
    return np.log(closeadj * volume).rolling(90, min_periods=90).apply(_reg_rsq, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_arctan_volsma_dist_15d_slope_v083_signal(volume):
    m = _sma(volume, 15); sd = volume.rolling(15, min_periods=15).std()
    return np.arctan((volume - m) / sd.replace(0.0, np.nan)).diff(5).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma40_ac5_120d_slope_v084_signal(volume):
    m = _sma(volume, 40).diff()
    return m.rolling(120, min_periods=120).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan, raw=True
    ).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_range_to_std_60d_slope_v085_signal(volume):
    m = _sma(volume, 25)
    rng = m.rolling(60, min_periods=60).max() - m.rolling(60, min_periods=60).min()
    sd = m.rolling(60, min_periods=60).std()
    return (rng / sd.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_kernel_slope_agree_45d_slope_v086_signal(volume):
    n = 45; k = 10
    sl = [_sma(volume, n), _ema(volume, n), _wma(volume, n), _wilder(volume, n), _hma(volume, n)]
    pos = pd.Series(0.0, index=volume.index); neg = pd.Series(0.0, index=volume.index)
    mask = ~sl[0].isna()
    for s in sl:
        d = s.diff(k)
        pos = pos + (d > 0.0).astype(float)
        neg = neg + (d < 0.0).astype(float)
        mask = mask & ~d.isna()
    return (pos - neg).where(mask).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_dvma_corr_60d_slope_v087_signal(closeadj, volume):
    a = _sma(volume, 20); b = _sma(closeadj * volume, 20)
    return a.rolling(60, min_periods=60).corr(b).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_trend_rsq_120d_slope_v088_signal(volume):
    return _sma(volume, 30).rolling(120, min_periods=120).apply(_reg_rsq, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_streak_vol_osc_pos_60d_slope_v089_signal(volume):
    above = (_sma(volume, 10) > _sma(volume, 50)).astype(float).where(~_sma(volume, 50).isna())
    return above.rolling(60, min_periods=60).apply(_consec, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_daysince_voldn_emaup_90d_slope_v090_signal(volume):
    m = _ema(volume, 40); s = np.sign(m.diff(10))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(90, min_periods=90).apply(_streak_lastflip, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_elasticity_50d_slope_v091_signal(volume):
    m = _sma(volume, 50)
    dev = (volume - m).abs().rolling(10, min_periods=10).mean()
    return (m.diff(10) / dev.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_netvol_ema_slope_45d_slope_v092_signal(close, volume):
    sv = np.sign(close.diff()) * volume
    ratio = (sv.ewm(span=45, adjust=False, min_periods=45).mean() /
             volume.ewm(span=45, adjust=False, min_periods=45).mean().replace(0.0, np.nan))
    return ratio.diff(10).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_slope_v093_signal(close, volume):
    sv = np.sign(close.diff()) * volume
    e = sv.ewm(span=10, adjust=False, min_periods=10).mean()
    return ((e - e.rolling(75, min_periods=75).mean()) /
            e.rolling(75, min_periods=75).std().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_ad_line_slope_120d_slope_v094_signal(high, low, closeadj, volume):
    rng = (high - low).replace(0.0, np.nan)
    mfm = ((closeadj - low) - (high - closeadj)) / rng
    mfv = mfm * volume
    norm = volume.rolling(120, min_periods=120).mean().replace(0.0, np.nan)
    return (mfv.rolling(120, min_periods=120).sum() / norm).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvolma_rank_200_500d_slope_v095_signal(volume):
    return _sma(np.log(volume), 200).rolling(500, min_periods=500).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_above_band_freq_45d_slope_v096_signal(volume):
    m = _sma(volume, 20); sd = volume.rolling(20, min_periods=20).std()
    upper = m + sd
    above = (volume > upper).astype(float).where(~upper.isna())
    return above.rolling(45, min_periods=45).mean().diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_below_band_freq_120d_slope_v097_signal(volume):
    m = _sma(volume, 30); sd = volume.rolling(30, min_periods=30).std()
    lower = m - sd
    below = (volume < lower).astype(float).where(~lower.isna())
    return below.rolling(120, min_periods=120).mean().diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_slope_v098_signal(closeadj, volume):
    dv = closeadj * volume
    a = _sma(dv, 30); b = _sma(dv, 120)
    return (a.diff(21) / a.abs() - b.diff(21) / b.abs()).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_streak_above_volwma25_60d_slope_v099_signal(volume):
    above = (volume > _wma(volume, 25)).astype(float).where(~_wma(volume, 25).isna())
    return above.rolling(60, min_periods=60).apply(_consec, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema_swing_180d_slope_v100_signal(volume):
    m = _ema(volume, 40)
    rng = m.rolling(180, min_periods=180).max() - m.rolling(180, min_periods=180).min()
    mn = m.rolling(180, min_periods=180).mean().replace(0.0, np.nan)
    return (rng / mn).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_jerk_75d_slope_v101_signal(volume):
    m = _sma(volume, 75); k = 21
    third = m - 3.0 * m.shift(k) + 3.0 * m.shift(2 * k) - m.shift(3 * k)
    return (third / m.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_force_index_ema13_to_ema50_slope_v102_signal(close, volume):
    fi = close.diff() * volume
    a = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    b = fi.ewm(span=50, adjust=False, min_periods=50).mean()
    return (a / b.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_mfi_trend_ema_30d_slope_v103_signal(high, low, closeadj, volume):
    tp = (high + low + closeadj) / 3.0
    mf = tp * volume
    pos = mf.where(tp > tp.shift(1), 0.0); neg = mf.where(tp < tp.shift(1), 0.0)
    a = pos.ewm(span=30, adjust=False, min_periods=30).mean()
    b = neg.ewm(span=30, adjust=False, min_periods=30).mean()
    return np.log(a.replace(0.0, np.nan) / b.replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_slope_v104_signal(volume):
    m = _sma(volume, 30)
    def _f(x):
        if len(x) < 4: return np.nan
        q1 = np.quantile(x, 0.25); q3 = np.quantile(x, 0.75); med = np.median(x)
        if med == 0.0 or not np.isfinite(med): return np.nan
        return float((q3 - q1) / med)
    return m.rolling(60, min_periods=60).apply(_f, raw=True).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_slope_v105_signal(volume):
    m = _sma(volume, 20)
    pct = (volume - m) / m.replace(0.0, np.nan)
    sm = pct.ewm(span=25, adjust=False, min_periods=25).mean()
    above = (sm > 0.0).astype(float).where(~sm.isna())
    return above.rolling(60, min_periods=60).mean().diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema_long_ratio_to_3sma_slope_v106_signal(volume):
    a = np.log(_ema(volume, 180))
    b = np.log(_sma(volume, 60)).rolling(100, min_periods=100).mean()
    return (a - b).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_reversion_freq_100d_slope_v107_signal(volume):
    d = volume - _sma(volume, 20); s = np.sign(d)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(100, min_periods=100).mean().diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_double_cross_volsma_slope_v108_signal(volume):
    a = np.sign(volume - _sma(volume, 10))
    b = np.sign(_sma(volume, 10) - _sma(volume, 40))
    return (a * b).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_drawdown_from_max_252d_slope_v109_signal(closeadj, volume):
    dv = closeadj * volume; m = _ema(dv, 30)
    mx = m.rolling(252, min_periods=252).max().replace(0.0, np.nan)
    return np.log(m / mx).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_gain_from_min_120d_slope_v110_signal(volume):
    m = _sma(volume, 30)
    mn = m.rolling(120, min_periods=120).min().replace(0.0, np.nan)
    return np.log(m / mn).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_diff_over_std_30d_slope_v111_signal(volume):
    lv = np.log(volume); sd = lv.rolling(30, min_periods=30).std()
    return ((lv - lv.shift(30)) / sd.replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_slope_sign_count_60d_slope_v112_signal(volume):
    cnt = pd.Series(0.0, index=volume.index); mask = ~_sma(volume, 150).isna()
    for n in (10, 30, 60, 90, 150):
        d = _sma(volume, n).diff(10)
        cnt = cnt + (d > 0.0).astype(float)
        mask = mask & ~d.isna()
    return cnt.where(mask).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_slope_v113_signal(volume):
    sw = _sma(volume, 30); lw = _sma(volume, 180)
    sd = sw.rolling(180, min_periods=180).std()
    return ((sw - lw) / sd.replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema_slope_pctchg_45d_slope_v114_signal(volume):
    sl = _ema(volume, 30).diff(5); base_sl = sl.shift(45)
    return ((sl - base_sl) / base_sl.abs().replace(0.0, np.nan)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logdv_hurst_120d_slope_v115_signal(closeadj, volume):
    return np.log(closeadj * volume).diff().rolling(120, min_periods=120).apply(_hurst_rs, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_upvol_downvol_ema30_slope_v116_signal(close, volume):
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.ewm(span=30, adjust=False, min_periods=30).mean()
    b = dn.ewm(span=30, adjust=False, min_periods=30).mean()
    return np.sign(a - b).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_slope_v117_signal(volume):
    a = _sma(volume, 10); b = _sma(volume, 60)
    sd = volume.rolling(60, min_periods=60).std()
    return ((a - b) / sd.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_bandwidth_40d_slope_v118_signal(volume):
    m = _sma(volume, 15)
    sd = m.rolling(40, min_periods=40).std()
    mn = m.rolling(40, min_periods=40).mean().replace(0.0, np.nan)
    return (sd / mn).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_rev_rank_300d_slope_v119_signal(volume):
    return (1.0 - _sma(volume, 45).rolling(300, min_periods=300).rank(pct=True)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_center_pos_90d_slope_v120_signal(volume):
    m = _sma(volume, 20)
    mu = m.rolling(90, min_periods=90).mean()
    rng = m.rolling(90, min_periods=90).max() - m.rolling(90, min_periods=90).min()
    return ((m - mu) / rng.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_slope_v121_signal(volume):
    m = _sma(volume, 15)
    sd = m.rolling(60, min_periods=60).std()
    mad = m.rolling(60, min_periods=60).apply(
        lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    return (mad / sd.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_smoothvol_skew_90d_slope_v122_signal(volume):
    return _sma(volume, 30).rolling(90, min_periods=90).skew().diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_smoothvol_kurt_180d_slope_v123_signal(volume):
    return _sma(volume, 40).rolling(180, min_periods=180).kurt().diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_slope_v124_signal(volume):
    s = np.sign(_sma(volume, 30).diff(5))
    return s.rolling(90, min_periods=90).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=True
    ).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_cum_excess_volma_120d_slope_v125_signal(volume):
    m = _sma(volume, 30); excess = (volume - m).clip(lower=0.0)
    a = excess.rolling(120, min_periods=120).sum()
    b = volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return (a / b).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema30_convex_frac_60d_slope_v126_signal(volume):
    m = _ema(volume, 30)
    curv = m - 2.0 * m.shift(5) + m.shift(10)
    pos = (curv > 0.0).astype(float).where(~curv.isna())
    return pos.rolling(60, min_periods=60).mean().diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_rank_180d_slope_v127_signal(closeadj, volume):
    return _ema(closeadj * volume, 40).rolling(180, min_periods=180).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_daysince_volsma_signflip_252d_slope_v128_signal(volume):
    s = np.sign(volume - _sma(volume, 40))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(252, min_periods=252).apply(_streak_lastflip, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_slope_v129_signal(close, volume):
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(30, min_periods=30).mean(); b = dn.rolling(30, min_periods=30).mean()
    za = (a - a.rolling(60, min_periods=60).mean()) / a.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    zb = (b - b.rolling(60, min_periods=60).mean()) / b.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    return (za - zb).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_pctroc_45d_slope_v130_signal(volume):
    m = _sma(volume, 25)
    return (m / m.shift(45) - 1.0).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_per_price_ma_60d_slope_v131_signal(closeadj, volume):
    dv = closeadj * volume
    return np.log(_ema(dv, 60) / (closeadj * _ema(volume, 60))).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_slope_consistency_120d_slope_v132_signal(volume):
    spread = _ema(volume, 30) - _ema(volume, 90)
    return spread.rolling(120, min_periods=120).apply(_reg_rsq, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_slope_v133_signal(volume):
    o = (_sma(volume, 5) - _sma(volume, 30)) / _sma(volume, 30).replace(0.0, np.nan)
    return (o - o.shift(45)).diff(10).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_max_min_diff_log_252d_slope_v134_signal(volume):
    m = _ema(volume, 50)
    mx = m.rolling(252, min_periods=252).max(); mn = m.rolling(252, min_periods=252).min()
    return np.log(mx / mn.replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_spread_rank_252d_slope_v135_signal(volume):
    spread = _sma(volume, 15) - _sma(volume, 60)
    return spread.rolling(252, min_periods=252).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_slope_v136_signal(close, volume):
    sv = np.sign(close.diff()) * volume
    a = sv.ewm(span=20, adjust=False, min_periods=20).mean()
    b = sv.ewm(span=80, adjust=False, min_periods=80).mean()
    return np.log(a.abs().replace(0.0, np.nan) / b.abs().replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_signconsistency_90d_slope_v137_signal(volume):
    s1 = np.sign(_sma(volume, 10) - _sma(volume, 30))
    s2 = np.sign(_sma(volume, 30) - _sma(volume, 90))
    agree = (s1 == s2).astype(float).where(~s1.isna() & ~s2.isna())
    return agree.rolling(90, min_periods=90).mean().diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_ma_log_rank_252d_slope_v138_signal(closeadj, volume):
    return np.log(_sma(closeadj * volume, 40)).rolling(252, min_periods=252).rank(pct=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_slope_v139_signal(volume):
    m = _sma(volume, 50)
    sl = m.diff(10); cu = m - 2.0 * m.shift(10) + m.shift(20)
    return (sl / cu.replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sigmoid_volma_spread_70d_slope_v140_signal(volume):
    x = np.log(_sma(volume, 20) / _sma(volume, 70))
    return (1.0 / (1.0 + np.exp(-x))).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_regslope_normalized_180d_slope_v141_signal(volume):
    return _sma(volume, 40).rolling(180, min_periods=180).apply(_reg_slope_norm, raw=True).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_slope_v142_signal(volume):
    m = _sma(volume, 20)
    mid = (m.rolling(60, min_periods=60).max() + m.rolling(60, min_periods=60).min()) / 2.0
    above = (m > mid).astype(float).where(~mid.isna())
    return above.rolling(120, min_periods=120).mean().diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_slope_v143_signal(closeadj, volume):
    lr = np.log(closeadj * volume).diff(30)
    return lr.ewm(span=45, adjust=False, min_periods=45).mean().diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_minus_med_120d_slope_v144_signal(volume):
    m = _sma(volume, 25); med = m.rolling(120, min_periods=120).median()
    return ((m - med) / med.replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_slope_v145_signal(volume):
    sl = _sma(volume, 30).diff(10)
    return (sl / sl.shift(30).replace(0.0, np.nan)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_log_volma_long_z_504d_slope_v146_signal(volume):
    m = _sma(np.log(volume), 60)
    return ((m - m.rolling(504, min_periods=504).mean()) /
            m.rolling(504, min_periods=504).std().replace(0.0, np.nan)).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_dv_ma_15_60_slope_v147_signal(closeadj, volume):
    dv = closeadj * volume
    return np.sign(_ema(dv, 15) - _ema(dv, 60)).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_slope_v148_signal(closeadj, volume):
    a = _sma(volume, 60); b = _sma(closeadj, 60)
    return (a.diff(21) / a.abs() - b.diff(21) / b.abs()).diff(21).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_ema_range_norm_252d_slope_v149_signal(closeadj, volume):
    m = _ema(closeadj * volume, 30)
    rng = m.rolling(252, min_periods=252).max() - m.rolling(252, min_periods=252).min()
    mn = m.rolling(252, min_periods=252).mean().replace(0.0, np.nan)
    return (rng / mn).diff(63).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_composite_volma_score_slope_v150_signal(volume):
    a = np.sign(_sma(volume, 20) - _sma(volume, 80))
    b = np.sign(_sma(volume, 80).diff(21))
    c = _sma(volume, 20).rolling(252, min_periods=252).rank(pct=True) - 0.5
    return (a + b + c).diff(63).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f22_volume_trend_slope_001_150_REGISTRY = {
    "f22vt_f22_volume_trend_logvol_sma_8d_slope_v001_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_sma_8d_slope_v001_signal},
    "f22vt_f22_volume_trend_volsmadiff_50_200_slope_v002_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsmadiff_50_200_slope_v002_signal},
    "f22vt_f22_volume_trend_logvol_sma_200d_resid_slope_v003_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_sma_200d_resid_slope_v003_signal},
    "f22vt_f22_volume_trend_volsma_volwma_diff_20d_slope_v004_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_volwma_diff_20d_slope_v004_signal},
    "f22vt_f22_volume_trend_volwilder_acceleration_40d_slope_v005_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwilder_acceleration_40d_slope_v005_signal},
    "f22vt_f22_volume_trend_vol_ema_10_120_ratio_slope_v007_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_ema_10_120_ratio_slope_v007_signal},
    "f22vt_f22_volume_trend_vol_wma_sma_diff_60d_slope_v008_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_wma_sma_diff_60d_slope_v008_signal},
    "f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_slope_v009_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_slope_v009_signal},
    "f22vt_f22_volume_trend_volema_xover_freq_120d_slope_v010_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_xover_freq_120d_slope_v010_signal},
    "f22vt_f22_volume_trend_sign_vol_sma_21_slope_v011_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_vol_sma_21_slope_v011_signal},
    "f22vt_f22_volume_trend_sign_volsma_5_20_slope_v012_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_volsma_5_20_slope_v012_signal},
    "f22vt_f22_volume_trend_sign_volema_30_90_slope_v013_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_volema_30_90_slope_v013_signal},
    "f22vt_f22_volume_trend_sign_volwilder_sma_60d_slope_v014_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_volwilder_sma_60d_slope_v014_signal},
    "f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_slope_v015_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_slope_v015_signal},
    "f22vt_f22_volume_trend_daysince_volsma_5_50_180d_slope_v016_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_volsma_5_50_180d_slope_v016_signal},
    "f22vt_f22_volume_trend_streak_above_volsma20_45d_slope_v017_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_streak_above_volsma20_45d_slope_v017_signal},
    "f22vt_f22_volume_trend_streak_below_volema50_140d_slope_v018_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_streak_below_volema50_140d_slope_v018_signal},
    "f22vt_f22_volume_trend_volsma25_slope_slope_v019_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma25_slope_slope_v019_signal},
    "f22vt_f22_volume_trend_volema80_slope_slope_v020_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema80_slope_slope_v020_signal},
    "f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_slope_v021_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_slope_v021_signal},
    "f22vt_f22_volume_trend_volema30_curv_slope_v022_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema30_curv_slope_v022_signal},
    "f22vt_f22_volume_trend_volsma60_curv_slope_v023_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma60_curv_slope_v023_signal},
    "f22vt_f22_volume_trend_volz_sma25_slope_v024_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volz_sma25_slope_v024_signal},
    "f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_slope_v025_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_slope_v025_signal},
    "f22vt_f22_volume_trend_rank_volsma15_90d_slope_v026_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_rank_volsma15_90d_slope_v026_signal},
    "f22vt_f22_volume_trend_rank_volema60_252d_slope_v027_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_rank_volema60_252d_slope_v027_signal},
    "f22vt_f22_volume_trend_stoch_volsma_30_120d_slope_v028_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_stoch_volsma_30_120d_slope_v028_signal},
    "f22vt_f22_volume_trend_stoch_volema_70_252d_slope_v029_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_stoch_volema_70_252d_slope_v029_signal},
    "f22vt_f22_volume_trend_logvol_roc_21d_slope_v030_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_roc_21d_slope_v030_signal},
    "f22vt_f22_volume_trend_logvol_roc_63d_slope_v031_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_roc_63d_slope_v031_signal},
    "f22vt_f22_volume_trend_volsma_slope_spread_10_50_slope_v032_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_slope_spread_10_50_slope_v032_signal},
    "f22vt_f22_volume_trend_volema_slope_spread_20_120_slope_v033_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_slope_spread_20_120_slope_v033_signal},
    "f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_slope_v034_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_slope_v034_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ratio_60d_slope_v035_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_upvol_downvol_ratio_60d_slope_v035_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ratio_150d_slope_v036_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_upvol_downvol_ratio_150d_slope_v036_signal},
    "f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_slope_v037_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_slope_v037_signal},
    "f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_slope_v038_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_slope_v038_signal},
    "f22vt_f22_volume_trend_dv_ema_25_100_ratio_slope_v039_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_ema_25_100_ratio_slope_v039_signal},
    "f22vt_f22_volume_trend_dv_sma60_slope_slope_v040_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_sma60_slope_slope_v040_signal},
    "f22vt_f22_volume_trend_logvol_olsslope_30d_slope_v041_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_olsslope_30d_slope_v041_signal},
    "f22vt_f22_volume_trend_logvol_olsslope_120d_slope_v042_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_olsslope_120d_slope_v042_signal},
    "f22vt_f22_volume_trend_logvol_rsq_45d_slope_v043_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_rsq_45d_slope_v043_signal},
    "f22vt_f22_volume_trend_logvol_rsq_180d_slope_v044_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_rsq_180d_slope_v044_signal},
    "f22vt_f22_volume_trend_vma_pma_agree_sign_60d_slope_v045_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_vma_pma_agree_sign_60d_slope_v045_signal},
    "f22vt_f22_volume_trend_vma_pma_agree_freq_120d_slope_v046_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_vma_pma_agree_freq_120d_slope_v046_signal},
    "f22vt_f22_volume_trend_avgprice_dvcum_30d_slope_v047_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_avgprice_dvcum_30d_slope_v047_signal},
    "f22vt_f22_volume_trend_avgprice_dvcum_120d_slope_v048_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_avgprice_dvcum_120d_slope_v048_signal},
    "f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_slope_v049_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_slope_v049_signal},
    "f22vt_f22_volume_trend_arctan_volsma_slope_50d_slope_v050_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_arctan_volsma_slope_50d_slope_v050_signal},
    "f22vt_f22_volume_trend_volwma_20_80_ratio_slope_v051_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwma_20_80_ratio_slope_v051_signal},
    "f22vt_f22_volume_trend_volwilder_30_90_ratio_slope_v052_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwilder_30_90_ratio_slope_v052_signal},
    "f22vt_f22_volume_trend_volema_posslope_frac_45d_slope_v053_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_posslope_frac_45d_slope_v053_signal},
    "f22vt_f22_volume_trend_volsma_posslope_frac_120d_slope_v054_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_posslope_frac_120d_slope_v054_signal},
    "f22vt_f22_volume_trend_vol_kernel_disp_40d_slope_v055_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_kernel_disp_40d_slope_v055_signal},
    "f22vt_f22_volume_trend_ribbon_order_sma_slope_v056_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_ribbon_order_sma_slope_v056_signal},
    "f22vt_f22_volume_trend_dv_z_ema70_diff_volz_slope_v057_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_z_ema70_diff_volz_slope_v057_signal},
    "f22vt_f22_volume_trend_volsma_acceleration_zscore_slope_v058_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_acceleration_zscore_slope_v058_signal},
    "f22vt_f22_volume_trend_logvolma_z_252d_slope_v059_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvolma_z_252d_slope_v059_signal},
    "f22vt_f22_volume_trend_cumupdn_ratio_45d_slope_v060_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_cumupdn_ratio_45d_slope_v060_signal},
    "f22vt_f22_volume_trend_sign_dv_sma_slope_100d_slope_v061_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_sign_dv_sma_slope_100d_slope_v061_signal},
    "f22vt_f22_volume_trend_volsma_normrange_60d_slope_v062_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_normrange_60d_slope_v062_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_slope_v063_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_slope_v063_signal},
    "f22vt_f22_volume_trend_klinger_34_55_slope_v064_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_klinger_34_55_slope_v064_signal},
    "f22vt_f22_volume_trend_volma_convergence_55d_slope_v065_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_convergence_55d_slope_v065_signal},
    "f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_slope_v066_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_slope_v066_signal},
    "f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_slope_v067_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_slope_v067_signal},
    "f22vt_f22_volume_trend_volma_slope_dispersion_80d_slope_v068_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_slope_dispersion_80d_slope_v068_signal},
    "f22vt_f22_volume_trend_volsma_ac1_60d_slope_v069_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_ac1_60d_slope_v069_signal},
    "f22vt_f22_volume_trend_logvol_skew_120d_slope_v070_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_skew_120d_slope_v070_signal},
    "f22vt_f22_volume_trend_hma_vol_curvature_30d_slope_v071_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_hma_vol_curvature_30d_slope_v071_signal},
    "f22vt_f22_volume_trend_sign_volslope_short_long_slope_v072_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_volslope_short_long_slope_v072_signal},
    "f22vt_f22_volume_trend_logvolma_long_zscore_300d_slope_v073_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvolma_long_zscore_300d_slope_v073_signal},
    "f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_slope_v074_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_slope_v074_signal},
    "f22vt_f22_volume_trend_volma_slope_flip_freq_120d_slope_v075_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_slope_flip_freq_120d_slope_v075_signal},
    "f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_slope_v076_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_slope_v076_signal},
    "f22vt_f22_volume_trend_volma_squeeze_30d_slope_v077_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_squeeze_30d_slope_v077_signal},
    "f22vt_f22_volume_trend_smoothvol_hurst_120d_slope_v078_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_hurst_120d_slope_v078_signal},
    "f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_slope_v079_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_slope_v079_signal},
    "f22vt_f22_volume_trend_logdv_olsslope_60d_slope_v080_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_logdv_olsslope_60d_slope_v080_signal},
    "f22vt_f22_volume_trend_logdv_olsslope_180d_slope_v081_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_logdv_olsslope_180d_slope_v081_signal},
    "f22vt_f22_volume_trend_logdv_rsq_90d_slope_v082_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_logdv_rsq_90d_slope_v082_signal},
    "f22vt_f22_volume_trend_arctan_volsma_dist_15d_slope_v083_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_arctan_volsma_dist_15d_slope_v083_signal},
    "f22vt_f22_volume_trend_volsma40_ac5_120d_slope_v084_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma40_ac5_120d_slope_v084_signal},
    "f22vt_f22_volume_trend_volsma_range_to_std_60d_slope_v085_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_range_to_std_60d_slope_v085_signal},
    "f22vt_f22_volume_trend_kernel_slope_agree_45d_slope_v086_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_kernel_slope_agree_45d_slope_v086_signal},
    "f22vt_f22_volume_trend_volma_dvma_corr_60d_slope_v087_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_volma_dvma_corr_60d_slope_v087_signal},
    "f22vt_f22_volume_trend_volsma_trend_rsq_120d_slope_v088_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_trend_rsq_120d_slope_v088_signal},
    "f22vt_f22_volume_trend_streak_vol_osc_pos_60d_slope_v089_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_streak_vol_osc_pos_60d_slope_v089_signal},
    "f22vt_f22_volume_trend_daysince_voldn_emaup_90d_slope_v090_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_voldn_emaup_90d_slope_v090_signal},
    "f22vt_f22_volume_trend_volma_elasticity_50d_slope_v091_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_elasticity_50d_slope_v091_signal},
    "f22vt_f22_volume_trend_netvol_ema_slope_45d_slope_v092_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_netvol_ema_slope_45d_slope_v092_signal},
    "f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_slope_v093_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_slope_v093_signal},
    "f22vt_f22_volume_trend_ad_line_slope_120d_slope_v094_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f22vt_f22_volume_trend_ad_line_slope_120d_slope_v094_signal},
    "f22vt_f22_volume_trend_logvolma_rank_200_500d_slope_v095_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvolma_rank_200_500d_slope_v095_signal},
    "f22vt_f22_volume_trend_volsma_above_band_freq_45d_slope_v096_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_above_band_freq_45d_slope_v096_signal},
    "f22vt_f22_volume_trend_volsma_below_band_freq_120d_slope_v097_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_below_band_freq_120d_slope_v097_signal},
    "f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_slope_v098_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_slope_v098_signal},
    "f22vt_f22_volume_trend_streak_above_volwma25_60d_slope_v099_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_streak_above_volwma25_60d_slope_v099_signal},
    "f22vt_f22_volume_trend_volema_swing_180d_slope_v100_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_swing_180d_slope_v100_signal},
    "f22vt_f22_volume_trend_volsma_jerk_75d_slope_v101_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_jerk_75d_slope_v101_signal},
    "f22vt_f22_volume_trend_force_index_ema13_to_ema50_slope_v102_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_force_index_ema13_to_ema50_slope_v102_signal},
    "f22vt_f22_volume_trend_mfi_trend_ema_30d_slope_v103_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f22vt_f22_volume_trend_mfi_trend_ema_30d_slope_v103_signal},
    "f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_slope_v104_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_slope_v104_signal},
    "f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_slope_v105_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_slope_v105_signal},
    "f22vt_f22_volume_trend_volema_long_ratio_to_3sma_slope_v106_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_long_ratio_to_3sma_slope_v106_signal},
    "f22vt_f22_volume_trend_volma_reversion_freq_100d_slope_v107_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_reversion_freq_100d_slope_v107_signal},
    "f22vt_f22_volume_trend_sign_double_cross_volsma_slope_v108_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_double_cross_volsma_slope_v108_signal},
    "f22vt_f22_volume_trend_dv_drawdown_from_max_252d_slope_v109_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_drawdown_from_max_252d_slope_v109_signal},
    "f22vt_f22_volume_trend_volma_gain_from_min_120d_slope_v110_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_gain_from_min_120d_slope_v110_signal},
    "f22vt_f22_volume_trend_logvol_diff_over_std_30d_slope_v111_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_diff_over_std_30d_slope_v111_signal},
    "f22vt_f22_volume_trend_volma_slope_sign_count_60d_slope_v112_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_slope_sign_count_60d_slope_v112_signal},
    "f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_slope_v113_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_slope_v113_signal},
    "f22vt_f22_volume_trend_volema_slope_pctchg_45d_slope_v114_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_slope_pctchg_45d_slope_v114_signal},
    "f22vt_f22_volume_trend_logdv_hurst_120d_slope_v115_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_logdv_hurst_120d_slope_v115_signal},
    "f22vt_f22_volume_trend_sign_upvol_downvol_ema30_slope_v116_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_sign_upvol_downvol_ema30_slope_v116_signal},
    "f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_slope_v117_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_slope_v117_signal},
    "f22vt_f22_volume_trend_volma_bandwidth_40d_slope_v118_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_bandwidth_40d_slope_v118_signal},
    "f22vt_f22_volume_trend_volsma_rev_rank_300d_slope_v119_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_rev_rank_300d_slope_v119_signal},
    "f22vt_f22_volume_trend_volsma_center_pos_90d_slope_v120_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_center_pos_90d_slope_v120_signal},
    "f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_slope_v121_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_slope_v121_signal},
    "f22vt_f22_volume_trend_smoothvol_skew_90d_slope_v122_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_skew_90d_slope_v122_signal},
    "f22vt_f22_volume_trend_smoothvol_kurt_180d_slope_v123_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_kurt_180d_slope_v123_signal},
    "f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_slope_v124_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_slope_v124_signal},
    "f22vt_f22_volume_trend_cum_excess_volma_120d_slope_v125_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_cum_excess_volma_120d_slope_v125_signal},
    "f22vt_f22_volume_trend_volema30_convex_frac_60d_slope_v126_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema30_convex_frac_60d_slope_v126_signal},
    "f22vt_f22_volume_trend_dv_rank_180d_slope_v127_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_rank_180d_slope_v127_signal},
    "f22vt_f22_volume_trend_daysince_volsma_signflip_252d_slope_v128_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_volsma_signflip_252d_slope_v128_signal},
    "f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_slope_v129_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_slope_v129_signal},
    "f22vt_f22_volume_trend_volsma_pctroc_45d_slope_v130_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_pctroc_45d_slope_v130_signal},
    "f22vt_f22_volume_trend_dv_per_price_ma_60d_slope_v131_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_per_price_ma_60d_slope_v131_signal},
    "f22vt_f22_volume_trend_volma_slope_consistency_120d_slope_v132_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_slope_consistency_120d_slope_v132_signal},
    "f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_slope_v133_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_slope_v133_signal},
    "f22vt_f22_volume_trend_volma_max_min_diff_log_252d_slope_v134_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_max_min_diff_log_252d_slope_v134_signal},
    "f22vt_f22_volume_trend_volma_spread_rank_252d_slope_v135_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_spread_rank_252d_slope_v135_signal},
    "f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_slope_v136_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_slope_v136_signal},
    "f22vt_f22_volume_trend_volma_signconsistency_90d_slope_v137_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_signconsistency_90d_slope_v137_signal},
    "f22vt_f22_volume_trend_dv_ma_log_rank_252d_slope_v138_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_ma_log_rank_252d_slope_v138_signal},
    "f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_slope_v139_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_slope_v139_signal},
    "f22vt_f22_volume_trend_sigmoid_volma_spread_70d_slope_v140_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sigmoid_volma_spread_70d_slope_v140_signal},
    "f22vt_f22_volume_trend_volsma_regslope_normalized_180d_slope_v141_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_regslope_normalized_180d_slope_v141_signal},
    "f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_slope_v142_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_slope_v142_signal},
    "f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_slope_v143_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_slope_v143_signal},
    "f22vt_f22_volume_trend_volma_minus_med_120d_slope_v144_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_minus_med_120d_slope_v144_signal},
    "f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_slope_v145_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_slope_v145_signal},
    "f22vt_f22_volume_trend_log_volma_long_z_504d_slope_v146_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_log_volma_long_z_504d_slope_v146_signal},
    "f22vt_f22_volume_trend_sign_dv_ma_15_60_slope_v147_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_sign_dv_ma_15_60_slope_v147_signal},
    "f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_slope_v148_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_slope_v148_signal},
    "f22vt_f22_volume_trend_dv_ema_range_norm_252d_slope_v149_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_ema_range_norm_252d_slope_v149_signal},
    "f22vt_f22_volume_trend_composite_volma_score_slope_v150_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_composite_volma_score_slope_v150_signal},
}


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
    for name, entry in f22_volume_trend_slope_001_150_REGISTRY.items():
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
