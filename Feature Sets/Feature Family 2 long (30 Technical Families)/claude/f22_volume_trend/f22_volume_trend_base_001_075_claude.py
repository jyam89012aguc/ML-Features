"""f22_volume_trend base features 001-075.

Domain: SMOOTHED / TRENDED volume — moving averages of volume (SMA/EMA/WMA/
Wilder), volume MA slopes/curvatures, volume MA crossovers (sign + days-
since + streaks), volume MA distances (log/z/pct), cross-window volume MA
ratios, volume oscillators, dollar-volume MA trends, volume on advance vs
decline, smoothed-volume regime/percentile, OLS slope / R^2 of volume,
trended dollar volume.

Distinct from f21 (raw volume statistics): every feature here passes volume
(or dollar-volume) through a moving average / smoother BEFORE extracting
the signal. Distinct from f24 (price-volume confirmation): we never combine
volume with price-trend direction except for the up/down day split, and
even there the output is the volume-trend differential, not the price-
volume confirmation. NaN policy: never fillna(<v>); only replace([inf,
-inf], nan) at final return. Window > 21d on volume-derived MAs uses the
closeadj-driven dollar-volume series where price is involved. Each function
spells its formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (smoothing kernels for volume). Each feature spells its full
# formula inline; helpers only construct the smoothing primitive.
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wma(s: pd.Series, n: int) -> pd.Series:
    w = np.arange(1, n + 1, dtype=float); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _hma(s: pd.Series, n: int) -> pd.Series:
    half = max(2, n // 2); sqn = max(2, int(np.sqrt(n)))
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)


def _streak_lastflip(x):
    """Distance (in bars) since last flip in a binary sign-flip series."""
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


# ---------------------------------------------------------------------------
# Features 001-075. Heavy structural diversity for corr<=0.95.
# ---------------------------------------------------------------------------


# === Volume MA distance (continuous, log) ==================================


def f22vt_f22_volume_trend_logvol_sma_8d_base_v001_signal(volume):
    """log(volume / SMA(volume,8)). ONE short-window volume MA log-distance.
    Spaced widely from other level-distance features to avoid corr."""
    return np.log(volume / _sma(volume, 8)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsmadiff_50_200_base_v002_signal(volume):
    """log(SMA(vol,50) / SMA(vol,200)). Mid/long volume MA ratio."""
    return np.log(_sma(volume, 50) / _sma(volume, 200)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_sma_200d_resid_base_v003_signal(volume):
    """log(volume/SMA(vol,200)) MINUS log(volume/SMA(vol,40)). Residual long
    minus short level-distance — cancels common volume-level component."""
    return (np.log(volume / _sma(volume, 200)) - np.log(volume / _sma(volume, 40))).replace([np.inf, -np.inf], np.nan)


# === Volume MA distance, kernel diversity ==================================


def f22vt_f22_volume_trend_volsma_volwma_diff_20d_base_v004_signal(volume):
    """log(SMA(vol,20) / WMA(vol,20)). Kernel-diff across two smoothings.
    Cancels absolute drift; captures smoothing-shape difference."""
    return np.log(_sma(volume, 20) / _wma(volume, 20)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volwilder_acceleration_40d_base_v005_signal(volume):
    """Wilder(vol,40) 21d-curvature normalized by |Wilder|. Wilder-kernel
    volume MA 2nd-derivative — structurally distinct from level features."""
    a = _wilder(volume, 40)
    return ((a - 2.0 * a.shift(21) + a.shift(42)) / a.abs()).replace([np.inf, -np.inf], np.nan)


# === Cross-window volume MA ratios =========================================




def f22vt_f22_volume_trend_vol_ema_10_120_ratio_base_v007_signal(volume):
    """log(EMA(vol,10) / EMA(vol,120)). Short/long volume EMA ratio."""
    return np.log(_ema(volume, 10) / _ema(volume, 120)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_vol_wma_sma_diff_60d_base_v008_signal(volume):
    """log(WMA(vol,60) / SMA(vol,60)). Same-window kernel-shape diff between
    weighted and simple MA. Distinct from cross-window ratios."""
    return np.log(_wma(volume, 60) / _sma(volume, 60)).replace([np.inf, -np.inf], np.nan)


# === Volume oscillator (Chaikin-style) =====================================


def f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_base_v009_signal(volume):
    """((SMA(vol,5)-SMA(vol,50))/SMA(vol,50)) MINUS ((EMA(vol,10)-EMA(vol,40))/EMA(vol,40)).
    Difference of two volume oscillators at different windows/kernels —
    decorrelates from each individual oscillator and from log-ratios."""
    s1 = (_sma(volume, 5) - _sma(volume, 50)) / _sma(volume, 50)
    s2 = (_ema(volume, 10) - _ema(volume, 40)) / _ema(volume, 40)
    return (s1 - s2).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema_xover_freq_120d_base_v010_signal(volume):
    """Number of sign-flips of (EMA(vol,10)-EMA(vol,40)) over 120 bars / 120.
    Frequency-domain trend-stability measure on volume crossover; bounded
    in [0,1] — distinct from level-ratio features."""
    s = np.sign(_ema(volume, 10) - _ema(volume, 40))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Volume MA crossover sign (DISCRETE) ===================================


def f22vt_f22_volume_trend_sign_vol_sma_21_base_v011_signal(volume):
    """sign(volume - SMA(volume,21)). Discrete volume-MA crossover trend filter."""
    return np.sign(volume - _sma(volume, 21)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_volsma_5_20_base_v012_signal(volume):
    """sign(SMA(vol,5) - SMA(vol,20)). Volume short/long MA crossover sign."""
    return np.sign(_sma(volume, 5) - _sma(volume, 20)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_volema_30_90_base_v013_signal(volume):
    """sign(EMA(vol,30) - EMA(vol,90)). Mid/long volume EMA crossover sign."""
    return np.sign(_ema(volume, 30) - _ema(volume, 90)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_sign_volwilder_sma_60d_base_v014_signal(volume):
    """sign(Wilder(vol,60) - SMA(vol,60)). Kernel-cross at single window."""
    return np.sign(_wilder(volume, 60) - _sma(volume, 60)).replace([np.inf, -np.inf], np.nan)


# === Volume MA days-since cross (count) ====================================


def f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_base_v015_signal(volume):
    """Days since last sign-flip of (vol > SMA(vol,21)). Count, integer."""
    s = np.sign(volume - _sma(volume, 21))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).apply(_streak_lastflip, raw=True).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_daysince_volsma_5_50_180d_base_v016_signal(volume):
    """Days since last cross of SMA(vol,5) and SMA(vol,50)."""
    s = np.sign(_sma(volume, 5) - _sma(volume, 50))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(180, min_periods=180).apply(_streak_lastflip, raw=True).replace([np.inf, -np.inf], np.nan)


# === Streak counts (volume above its MA) ===================================


def f22vt_f22_volume_trend_streak_above_volsma20_45d_base_v017_signal(volume):
    """Current consecutive-bar streak of volume > SMA(vol,20), measured over 45d."""
    above = (volume > _sma(volume, 20)).astype(float).where(~_sma(volume, 20).isna())
    return above.rolling(45, min_periods=45).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_streak_below_volema50_140d_base_v018_signal(volume):
    """Current consecutive-bar streak of volume < EMA(vol,50), measured over 140d."""
    below = (volume < _ema(volume, 50)).astype(float).where(~_ema(volume, 50).isna())
    return below.rolling(140, min_periods=140).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume MA slope (SMA/EMA at varied windows) ===========================


def f22vt_f22_volume_trend_volsma25_slope_base_v019_signal(volume):
    """SMA(vol,25) 10-bar diff / |SMA(vol,25)|. Normalized volume-MA slope."""
    m = _sma(volume, 25)
    return (m.diff(10) / m.abs()).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema80_slope_base_v020_signal(volume):
    """EMA(vol,80) 21-bar diff / |EMA(vol,80)|. Mid-long volume EMA slope."""
    m = _ema(volume, 80)
    return (m.diff(21) / m.abs()).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_base_v021_signal(volume):
    """Normalized WMA(vol,40) 10d-slope MINUS normalized SMA(vol,80) 10d-slope.
    Slope-spread feature; decorrelates from raw single-MA slope features
    by canceling the common volume-regime drift."""
    a = _wma(volume, 40); b = _sma(volume, 80)
    return (a.diff(10) / a.abs() - b.diff(10) / b.abs()).replace([np.inf, -np.inf], np.nan)


# === Volume MA curvature (2nd diff) ========================================


def f22vt_f22_volume_trend_volema30_curv_base_v022_signal(volume):
    """EMA(vol,30) curvature: 2nd diff over 10-bar / |EMA|. Volume-MA acceleration."""
    m = _ema(volume, 30)
    return ((m - 2.0 * m.shift(10) + m.shift(20)) / m.abs()).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma60_curv_base_v023_signal(volume):
    """SMA(vol,60) curvature: 2nd diff over 21-bar / |SMA|."""
    m = _sma(volume, 60)
    return ((m - 2.0 * m.shift(21) + m.shift(42)) / m.abs()).replace([np.inf, -np.inf], np.nan)


# === Z-score of vol relative to MA =========================================


def f22vt_f22_volume_trend_volz_sma25_base_v024_signal(volume):
    """(vol - SMA(vol,25)) / std(vol,25). Volume z-score relative to short MA."""
    m = _sma(volume, 25)
    sd = volume.rolling(25, min_periods=25).std()
    return ((volume - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_base_v025_signal(volume):
    """((vol-EMA(vol,90))/std90) MINUS ((vol-SMA(vol,25))/std25).
    Z-score spread, captures volume-trend regime difference across
    horizons, decorrelating from each individual z-score."""
    m1 = _sma(volume, 25); sd1 = volume.rolling(25, min_periods=25).std()
    m2 = _ema(volume, 90); sd2 = volume.rolling(90, min_periods=90).std()
    z1 = (volume - m1) / sd1.replace(0.0, np.nan)
    z2 = (volume - m2) / sd2.replace(0.0, np.nan)
    return (z2 - z1).replace([np.inf, -np.inf], np.nan)


# === Smoothed volume regime percentile rank ================================


def f22vt_f22_volume_trend_rank_volsma15_90d_base_v026_signal(volume):
    """Percentile rank of SMA(vol,15) over trailing 90d window."""
    m = _sma(volume, 15)
    return m.rolling(90, min_periods=90).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_rank_volema60_252d_base_v027_signal(volume):
    """Percentile rank of EMA(vol,60) over trailing 252d window."""
    m = _ema(volume, 60)
    return m.rolling(252, min_periods=252).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === Trended volume in own range (stochastic on volume MA) =================


def f22vt_f22_volume_trend_stoch_volsma_30_120d_base_v028_signal(volume):
    """(SMA(vol,30) - min) / (max - min) over 120d. Volume-MA stochastic."""
    m = _sma(volume, 30)
    mn = m.rolling(120, min_periods=120).min()
    mx = m.rolling(120, min_periods=120).max()
    return ((m - mn) / (mx - mn).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_stoch_volema_70_252d_base_v029_signal(volume):
    """(EMA(vol,70) - min) / (max - min) over 252d. Long volume-MA stochastic."""
    m = _ema(volume, 70)
    mn = m.rolling(252, min_periods=252).min()
    mx = m.rolling(252, min_periods=252).max()
    return ((m - mn) / (mx - mn).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume rate-of-change (long) ==========================================


def f22vt_f22_volume_trend_logvol_roc_21d_base_v030_signal(volume):
    """log(vol / vol.shift(21)). Volume 21d log rate-of-change."""
    return np.log(volume / volume.shift(21)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_roc_63d_base_v031_signal(volume):
    """log(vol / vol.shift(63)). Volume 63d log rate-of-change."""
    return np.log(volume / volume.shift(63)).replace([np.inf, -np.inf], np.nan)


# === Volume MA divergence (slope spread) ===================================


def f22vt_f22_volume_trend_volsma_slope_spread_10_50_base_v032_signal(volume):
    """SMA(vol,10) 10d-slope minus SMA(vol,50) 10d-slope, normalized."""
    m10 = _sma(volume, 10); m50 = _sma(volume, 50)
    s10 = m10.diff(10) / m10.abs(); s50 = m50.diff(10) / m50.abs()
    return (s10 - s50).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volema_slope_spread_20_120_base_v033_signal(volume):
    """EMA(vol,20) 21d-slope minus EMA(vol,120) 21d-slope, normalized."""
    m20 = _ema(volume, 20); m120 = _ema(volume, 120)
    s20 = m20.diff(21) / m20.abs(); s120 = m120.diff(21) / m120.abs()
    return (s20 - s120).replace([np.inf, -np.inf], np.nan)


# === Volume on advance vs decline ==========================================


def f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_base_v034_signal(close, volume):
    """SMA of volume on up-days minus SMA of volume on down-days, 30d."""
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    long_avg = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    diff = up.rolling(30, min_periods=30).mean() - dn.rolling(30, min_periods=30).mean()
    return (diff / long_avg).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_upvol_downvol_ratio_60d_base_v035_signal(closeadj, volume):
    """log(SMA(up-vol,60) / SMA(down-vol,60)). Up/down volume MA ratio."""
    up = volume.where(closeadj.diff() > 0.0, 0.0)
    dn = volume.where(closeadj.diff() < 0.0, 0.0)
    a = up.rolling(60, min_periods=60).mean()
    b = dn.rolling(60, min_periods=60).mean()
    return np.log(a.replace(0.0, np.nan) / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_upvol_downvol_ratio_150d_base_v036_signal(closeadj, volume):
    """log(EMA(up-vol,150) / EMA(down-vol,150)). Long-horizon up/down volume ratio."""
    up = volume.where(closeadj.diff() > 0.0, 0.0)
    dn = volume.where(closeadj.diff() < 0.0, 0.0)
    a = up.ewm(span=150, adjust=False, min_periods=150).mean()
    b = dn.ewm(span=150, adjust=False, min_periods=150).mean()
    return np.log(a.replace(0.0, np.nan) / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Dollar-volume MA (DV) trend ===========================================


def f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_base_v037_signal(closeadj, volume):
    """Normalized 21d-slope of EMA(DV,40) MINUS normalized 21d-slope of EMA(DV,120).
    Cross-window slope spread on dollar-volume MA — captures DV-MA divergence."""
    dv = closeadj * volume
    a = _ema(dv, 40); b = _ema(dv, 120)
    return (a.diff(21) / a.abs() - b.diff(21) / b.abs()).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_base_v038_signal(closeadj, volume):
    """log(SMA(DV,120)) - log(SMA(DV,40)). Long minus short DV-SMA log levels —
    cross-window DV ratio (cancels common DV drift)."""
    dv = closeadj * volume
    return (np.log(_sma(dv, 120)) - np.log(_sma(dv, 40))).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_ema_25_100_ratio_base_v039_signal(closeadj, volume):
    """log(EMA(DV,25) / EMA(DV,100)). Short vs long dollar-volume EMA ratio."""
    dv = closeadj * volume
    return np.log(_ema(dv, 25) / _ema(dv, 100)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_dv_sma60_slope_base_v040_signal(closeadj, volume):
    """SMA(DV,60) 21d-slope / |SMA(DV,60)|. Mid-window dollar-volume MA slope."""
    dv = closeadj * volume
    m = _sma(dv, 60)
    return (m.diff(21) / m.abs()).replace([np.inf, -np.inf], np.nan)


# === OLS slope / R^2 of (log) volume =======================================


def f22vt_f22_volume_trend_logvol_olsslope_30d_base_v041_signal(volume):
    """OLS slope of log(volume) over 30 bars, normalized by mean(log volume).
    Reg-slope is structurally distinct from MA-diff slope."""
    return np.log(volume).rolling(30, min_periods=30).apply(_reg_slope_norm, raw=True).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_olsslope_120d_base_v042_signal(volume):
    """OLS slope of log(volume) over 120 bars, normalized."""
    return np.log(volume).rolling(120, min_periods=120).apply(_reg_slope_norm, raw=True).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_rsq_45d_base_v043_signal(volume):
    """R^2 of OLS fit of log(volume) over 45 bars. Trend-strength metric."""
    return np.log(volume).rolling(45, min_periods=45).apply(_reg_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logvol_rsq_180d_base_v044_signal(volume):
    """R^2 of OLS fit of log(volume) over 180 bars. Long-horizon."""
    return np.log(volume).rolling(180, min_periods=180).apply(_reg_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume MA confirmation (price & volume both above their MAs) ==========


def f22vt_f22_volume_trend_vma_pma_agree_sign_60d_base_v045_signal(closeadj, volume):
    """sign(vol - SMA(vol,60)) * sign(closeadj - SMA(closeadj,60)).
    +1 when volume and price agree (both above or both below). -1 when
    they disagree. Discrete confirmation across volume/price MAs."""
    a = np.sign(volume - _sma(volume, 60))
    b = np.sign(closeadj - _sma(closeadj, 60))
    return (a * b).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_vma_pma_agree_freq_120d_base_v046_signal(closeadj, volume):
    """Fraction of last 120 bars where vol-vs-SMA agrees with price-vs-SMA, at n=30.
    Continuous between 0 and 1, distinct from binary sign feature."""
    a = (volume > _sma(volume, 30)).astype(float)
    b = (closeadj > _sma(closeadj, 30)).astype(float)
    agree = (a == b).astype(float).where(~_sma(volume, 30).isna() & ~_sma(closeadj, 30).isna())
    return agree.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Trended VWAP-like (cumulative-DV / cumulative-vol) ====================


def f22vt_f22_volume_trend_avgprice_dvcum_30d_base_v047_signal(closeadj, volume):
    """30d-rolling sum(closeadj*vol) / sum(vol). Trended average price; the
    SMOOTHING here is the cumulation-window which is volume-weighted. The
    sign captured is whether trended dollar-flow VWAP exceeds spot."""
    dv = closeadj * volume
    num = dv.rolling(30, min_periods=30).sum()
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    vwap = num / den
    return np.log(vwap / closeadj).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_avgprice_dvcum_120d_base_v048_signal(closeadj, volume):
    """120d rolling-VWAP versus closeadj — long-horizon trended dollar-flow."""
    dv = closeadj * volume
    num = dv.rolling(120, min_periods=120).sum()
    den = volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    vwap = num / den
    return np.log(vwap / closeadj).replace([np.inf, -np.inf], np.nan)


# === Smoothed-volume tanh/arctan bounded transforms ========================


def f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_base_v049_signal(volume):
    """tanh of (normalized 10d-slope of SMA(vol,30) MINUS that of EMA(vol,30)).
    Captures disagreement between SMA and EMA volume MA slopes — bounded
    and structurally different from level-distance features."""
    a = _sma(volume, 30); b = _ema(volume, 30)
    spread = a.diff(10) / a.abs() - b.diff(10) / b.abs()
    return np.tanh(spread).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_arctan_volsma_slope_50d_base_v050_signal(volume):
    """arctan of SMA(vol,50) 21d-slope / SMA(vol,50). Bounded MA slope."""
    m = _sma(volume, 50)
    return np.arctan((m.diff(21) / m.abs())).replace([np.inf, -np.inf], np.nan)


# === Cross-window log-MA differentials =====================================


def f22vt_f22_volume_trend_volwma_20_80_ratio_base_v051_signal(volume):
    """log(WMA(vol,20) / WMA(vol,80)). WMA short/long volume ratio - kernel diversity."""
    return np.log(_wma(volume, 20) / _wma(volume, 80)).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volwilder_30_90_ratio_base_v052_signal(volume):
    """log(Wilder(vol,30) / Wilder(vol,90)). Wilder short/long volume ratio."""
    return np.log(_wilder(volume, 30) / _wilder(volume, 90)).replace([np.inf, -np.inf], np.nan)


# === Trend strength: fraction of positive vol-MA slopes ====================


def f22vt_f22_volume_trend_volema_posslope_frac_45d_base_v053_signal(volume):
    """Fraction of last 45 days that EMA(vol,30) was rising (positive 5d-diff)."""
    m = _ema(volume, 30)
    pos = (m.diff(5) > 0.0).astype(float).where(~m.diff(5).isna())
    return pos.rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_volsma_posslope_frac_120d_base_v054_signal(volume):
    """Fraction of last 120 days that SMA(vol,60) was rising (10d-diff > 0)."""
    m = _sma(volume, 60)
    pos = (m.diff(10) > 0.0).astype(float).where(~m.diff(10).isna())
    return pos.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Kernel dispersion across volume MAs ===================================


def f22vt_f22_volume_trend_vol_kernel_disp_40d_base_v055_signal(volume):
    """Coefficient-of-variation across {SMA,EMA,WMA,Wilder,HMA}(vol,40).
    Dispersion of volume smoothings at same window."""
    n = 40
    mat = pd.concat([_sma(volume, n), _ema(volume, n), _wma(volume, n),
                     _wilder(volume, n), _hma(volume, n)], axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume MA ribbon ordering count =======================================


def f22vt_f22_volume_trend_ribbon_order_sma_base_v056_signal(volume):
    """Count of strictly-ordered ribbon pairs across SMA(vol, {10,20,40,80,160}).
    Discrete count from 0 to 10. Distinct from log-ratio features."""
    sn = [_sma(volume, k) for k in (10, 20, 40, 80, 160)]
    cnt = pd.Series(0.0, index=volume.index)
    mask = ~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i + 1, len(sn)):
            cnt = cnt + (sn[i] > sn[j]).astype(float)
            mask = mask & ~sn[i].isna() & ~sn[j].isna()
    return cnt.where(mask).replace([np.inf, -np.inf], np.nan)


# === DV MA z-score =========================================================


def f22vt_f22_volume_trend_dv_z_ema70_diff_volz_base_v057_signal(closeadj, volume):
    """((DV-EMA(DV,70))/std70) MINUS ((vol-EMA(vol,70))/std70).
    Dollar-volume z-score MINUS volume z-score at same window; isolates
    the PRICE-induced trend in DV beyond pure volume."""
    dv = closeadj * volume
    md = _ema(dv, 70); sdd = dv.rolling(70, min_periods=70).std()
    zd = (dv - md) / sdd.replace(0.0, np.nan)
    mv = _ema(volume, 70); sdv = volume.rolling(70, min_periods=70).std()
    zv = (volume - mv) / sdv.replace(0.0, np.nan)
    return (zd - zv).replace([np.inf, -np.inf], np.nan)


# === Volume oscillator on EMA short vs SMA long ============================


def f22vt_f22_volume_trend_volsma_acceleration_zscore_base_v058_signal(volume):
    """Z-score of SMA(vol,20).diff(5)/SMA(vol,20) over 60d trailing window.
    Z-score of normalized short-window volume MA slope — captures
    extremity of volume-MA acceleration."""
    m = _sma(volume, 20)
    sl = m.diff(5) / m.abs()
    mu = sl.rolling(60, min_periods=60).mean()
    sd = sl.rolling(60, min_periods=60).std()
    return ((sl - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Long-horizon volume regime z-score on log-volume ======================


def f22vt_f22_volume_trend_logvolma_z_252d_base_v059_signal(volume):
    """((SMA(logvol,40)) - mean over 252d) / std over 252d. Long-regime z."""
    m = _sma(np.log(volume), 40)
    return ((m - m.rolling(252, min_periods=252).mean()) /
            m.rolling(252, min_periods=252).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Cumulative-up-vol vs cumulative-down-vol over MA window ===============


def f22vt_f22_volume_trend_cumupdn_ratio_45d_base_v060_signal(close, volume):
    """log of (cum up-vol)/(cum down-vol) over 45 bars. Force-index-like trend."""
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(45, min_periods=45).sum()
    b = dn.rolling(45, min_periods=45).sum()
    return np.log(a.replace(0.0, np.nan) / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Long-horizon dollar-volume slope sign =================================


def f22vt_f22_volume_trend_sign_dv_sma_slope_100d_base_v061_signal(closeadj, volume):
    """sign of SMA(DV,100) 63d-diff. Discrete dollar-volume trend direction."""
    dv = closeadj * volume
    m = _sma(dv, 100)
    return np.sign(m.diff(63)).replace([np.inf, -np.inf], np.nan)


# === Volume range over its trend (smoothed vs smoothed range) =============


def f22vt_f22_volume_trend_volsma_normrange_60d_base_v062_signal(volume):
    """(max(SMA(vol,30),60d) - min(SMA(vol,30),60d)) / SMA(vol,30).
    Range of smoothed volume over its own value — trended-volume volatility."""
    m = _sma(volume, 30)
    rng = m.rolling(60, min_periods=60).max() - m.rolling(60, min_periods=60).min()
    return (rng / m.abs()).replace([np.inf, -np.inf], np.nan)


# === EMA-of-up-vol minus EMA-of-down-vol normalized =======================


def f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_base_v063_signal(close, volume):
    """(EMA(up-vol,30)-EMA(down-vol,30))/EMA(vol,30). Klinger-like trend
    component using EMA smoothing of signed volume."""
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.ewm(span=30, adjust=False, min_periods=30).mean()
    b = dn.ewm(span=30, adjust=False, min_periods=30).mean()
    norm = volume.ewm(span=30, adjust=False, min_periods=30).mean().replace(0.0, np.nan)
    return ((a - b) / norm).replace([np.inf, -np.inf], np.nan)


# === Klinger short - long ==================================================


def f22vt_f22_volume_trend_klinger_34_55_base_v064_signal(close, volume):
    """Klinger-like signed-volume EMA34 minus EMA55, normalized."""
    sgn = np.sign(close.diff())
    sv = sgn * volume
    a = sv.ewm(span=34, adjust=False, min_periods=34).mean()
    b = sv.ewm(span=55, adjust=False, min_periods=55).mean()
    norm = volume.ewm(span=55, adjust=False, min_periods=55).mean().replace(0.0, np.nan)
    return ((a - b) / norm).replace([np.inf, -np.inf], np.nan)


# === Volume MA convergence (abs of MA diff over volume) ====================


def f22vt_f22_volume_trend_volma_convergence_55d_base_v065_signal(volume):
    """|EMA(vol,10) - EMA(vol,55)| / EMA(vol,55). Bounded MA convergence
    metric (never negative). Decorrelates from signed MA-diff features."""
    a = _ema(volume, 10); b = _ema(volume, 55)
    return ((a - b).abs() / b.abs()).replace([np.inf, -np.inf], np.nan)


# === Days-since rising volume MA ===========================================


def f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_base_v066_signal(volume):
    """Days since last flip of sign(SMA(vol,40).diff(10)) over 100d window."""
    m = _sma(volume, 40)
    s = np.sign(m.diff(10))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(100, min_periods=100).apply(_streak_lastflip, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume MA percentile across many windows ==============================


def f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_base_v067_signal(volume):
    """Rank of SMA(vol,30) across (SMA(vol,n) for n in {10,30,90,180}) at
    each bar — which window's MA is highest? Discrete-like 0..3 rank."""
    sn = [_sma(volume, k) for k in (10, 30, 90, 180)]
    mat = pd.concat(sn, axis=1)
    mask = mat.isna().any(axis=1)
    return mat.rank(axis=1, pct=False).iloc[:, 1].where(~mask).replace([np.inf, -np.inf], np.nan)


# === Trend strength: slope dispersion across windows =======================


def f22vt_f22_volume_trend_volma_slope_dispersion_80d_base_v068_signal(volume):
    """Std of normalized 10d-slopes across SMA(vol, [20,40,60,80,100]).
    Bounded non-negative; captures inconsistency across windows."""
    sl = []
    for n in (20, 40, 60, 80, 100):
        m = _sma(volume, n)
        sl.append(m.diff(10) / m.abs())
    mat = pd.concat(sl, axis=1)
    return mat.std(axis=1).replace([np.inf, -np.inf], np.nan)


# === Volume MA Hurst-like persistence (autocorr of MA returns) =============


def f22vt_f22_volume_trend_volsma_ac1_60d_base_v069_signal(volume):
    """Autocorrelation lag-1 of SMA(vol,20).diff() over 60d window.
    Persistence of volume-MA changes — distinct trend-character metric."""
    m = _sma(volume, 20).diff()
    return m.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Volume MA log-skewness on the volume distribution =====================


def f22vt_f22_volume_trend_logvol_skew_120d_base_v070_signal(volume):
    """Skewness of log(volume) over 120 bars, then EMA-smoothed. Trended skew
    of volume distribution."""
    sk = np.log(volume).rolling(60, min_periods=60).skew()
    return sk.ewm(span=120, adjust=False, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Trend smoothing: HMA-based volume distance ============================


def f22vt_f22_volume_trend_hma_vol_curvature_30d_base_v071_signal(volume):
    """HMA(vol,30) curvature: 2nd-diff over 10-bar / |HMA|. HMA is responsive
    Hull MA; curvature isolates 2nd-derivative volume trend changes."""
    m = _hma(volume, 30)
    return ((m - 2.0 * m.shift(10) + m.shift(20)) / m.abs()).replace([np.inf, -np.inf], np.nan)


# === Volume slope ratio: short slope / long slope (sign of ratio) ==========


def f22vt_f22_volume_trend_sign_volslope_short_long_base_v072_signal(volume):
    """sign((EMA(vol,15).diff(10)) - (EMA(vol,60).diff(10))). Discrete
    short-vs-long volume momentum agreement."""
    a = _ema(volume, 15).diff(10)
    b = _ema(volume, 60).diff(10)
    return np.sign(a - b).replace([np.inf, -np.inf], np.nan)


# === Volume MA distance, very-long horizon, log-scale ======================


def f22vt_f22_volume_trend_logvolma_long_zscore_300d_base_v073_signal(volume):
    """((SMA(vol,90) - mean SMA(vol,90) over 300d) / std over 300d).
    Long-horizon trended-volume z-score."""
    m = _sma(volume, 90)
    return ((m - m.rolling(300, min_periods=300).mean()) /
            m.rolling(300, min_periods=300).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Up-vol MA vs down-vol MA crossover days-since =========================


def f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_base_v074_signal(close, volume):
    """Days since last cross of SMA(up-vol,30) and SMA(down-vol,30) over 200d."""
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(30, min_periods=30).mean()
    b = dn.rolling(30, min_periods=30).mean()
    s = np.sign(a - b)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(200, min_periods=200).apply(_streak_lastflip, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume MA reversion rate (frequency of MA flipping sign of slope) =====


def f22vt_f22_volume_trend_volma_slope_flip_freq_120d_base_v075_signal(volume):
    """Number of sign flips of SMA(vol,30).diff(5) over 120 bars / 120.
    Measures how oscillatory the smoothed-volume trend has been."""
    m = _sma(volume, 30)
    s = np.sign(m.diff(5))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


f22_volume_trend_base_001_075_REGISTRY = {
    "f22vt_f22_volume_trend_logvol_sma_8d_base_v001_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_sma_8d_base_v001_signal},
    "f22vt_f22_volume_trend_volsmadiff_50_200_base_v002_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsmadiff_50_200_base_v002_signal},
    "f22vt_f22_volume_trend_logvol_sma_200d_resid_base_v003_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_sma_200d_resid_base_v003_signal},
    "f22vt_f22_volume_trend_volsma_volwma_diff_20d_base_v004_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_volwma_diff_20d_base_v004_signal},
    "f22vt_f22_volume_trend_volwilder_acceleration_40d_base_v005_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwilder_acceleration_40d_base_v005_signal},
    "f22vt_f22_volume_trend_vol_ema_10_120_ratio_base_v007_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_ema_10_120_ratio_base_v007_signal},
    "f22vt_f22_volume_trend_vol_wma_sma_diff_60d_base_v008_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_wma_sma_diff_60d_base_v008_signal},
    "f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_base_v009_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_osc_diff_short_minus_long_base_v009_signal},
    "f22vt_f22_volume_trend_volema_xover_freq_120d_base_v010_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_xover_freq_120d_base_v010_signal},
    "f22vt_f22_volume_trend_sign_vol_sma_21_base_v011_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_vol_sma_21_base_v011_signal},
    "f22vt_f22_volume_trend_sign_volsma_5_20_base_v012_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_volsma_5_20_base_v012_signal},
    "f22vt_f22_volume_trend_sign_volema_30_90_base_v013_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_volema_30_90_base_v013_signal},
    "f22vt_f22_volume_trend_sign_volwilder_sma_60d_base_v014_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_volwilder_sma_60d_base_v014_signal},
    "f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_base_v015_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_vol_xmasma21_120d_base_v015_signal},
    "f22vt_f22_volume_trend_daysince_volsma_5_50_180d_base_v016_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_volsma_5_50_180d_base_v016_signal},
    "f22vt_f22_volume_trend_streak_above_volsma20_45d_base_v017_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_streak_above_volsma20_45d_base_v017_signal},
    "f22vt_f22_volume_trend_streak_below_volema50_140d_base_v018_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_streak_below_volema50_140d_base_v018_signal},
    "f22vt_f22_volume_trend_volsma25_slope_base_v019_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma25_slope_base_v019_signal},
    "f22vt_f22_volume_trend_volema80_slope_base_v020_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema80_slope_base_v020_signal},
    "f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_base_v021_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwma40_slope_minus_volsma80_slope_base_v021_signal},
    "f22vt_f22_volume_trend_volema30_curv_base_v022_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema30_curv_base_v022_signal},
    "f22vt_f22_volume_trend_volsma60_curv_base_v023_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma60_curv_base_v023_signal},
    "f22vt_f22_volume_trend_volz_sma25_base_v024_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volz_sma25_base_v024_signal},
    "f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_base_v025_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volz_ema90_minus_volz_sma25_base_v025_signal},
    "f22vt_f22_volume_trend_rank_volsma15_90d_base_v026_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_rank_volsma15_90d_base_v026_signal},
    "f22vt_f22_volume_trend_rank_volema60_252d_base_v027_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_rank_volema60_252d_base_v027_signal},
    "f22vt_f22_volume_trend_stoch_volsma_30_120d_base_v028_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_stoch_volsma_30_120d_base_v028_signal},
    "f22vt_f22_volume_trend_stoch_volema_70_252d_base_v029_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_stoch_volema_70_252d_base_v029_signal},
    "f22vt_f22_volume_trend_logvol_roc_21d_base_v030_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_roc_21d_base_v030_signal},
    "f22vt_f22_volume_trend_logvol_roc_63d_base_v031_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_roc_63d_base_v031_signal},
    "f22vt_f22_volume_trend_volsma_slope_spread_10_50_base_v032_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_slope_spread_10_50_base_v032_signal},
    "f22vt_f22_volume_trend_volema_slope_spread_20_120_base_v033_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_slope_spread_20_120_base_v033_signal},
    "f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_base_v034_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_upvol_downvol_diff_sma_30d_base_v034_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ratio_60d_base_v035_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_upvol_downvol_ratio_60d_base_v035_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ratio_150d_base_v036_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_upvol_downvol_ratio_150d_base_v036_signal},
    "f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_base_v037_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_ema_slope_diff_40_120_base_v037_signal},
    "f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_base_v038_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_logsma_120_minus_logsma40_base_v038_signal},
    "f22vt_f22_volume_trend_dv_ema_25_100_ratio_base_v039_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_ema_25_100_ratio_base_v039_signal},
    "f22vt_f22_volume_trend_dv_sma60_slope_base_v040_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_sma60_slope_base_v040_signal},
    "f22vt_f22_volume_trend_logvol_olsslope_30d_base_v041_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_olsslope_30d_base_v041_signal},
    "f22vt_f22_volume_trend_logvol_olsslope_120d_base_v042_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_olsslope_120d_base_v042_signal},
    "f22vt_f22_volume_trend_logvol_rsq_45d_base_v043_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_rsq_45d_base_v043_signal},
    "f22vt_f22_volume_trend_logvol_rsq_180d_base_v044_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_rsq_180d_base_v044_signal},
    "f22vt_f22_volume_trend_vma_pma_agree_sign_60d_base_v045_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_vma_pma_agree_sign_60d_base_v045_signal},
    "f22vt_f22_volume_trend_vma_pma_agree_freq_120d_base_v046_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_vma_pma_agree_freq_120d_base_v046_signal},
    "f22vt_f22_volume_trend_avgprice_dvcum_30d_base_v047_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_avgprice_dvcum_30d_base_v047_signal},
    "f22vt_f22_volume_trend_avgprice_dvcum_120d_base_v048_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_avgprice_dvcum_120d_base_v048_signal},
    "f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_base_v049_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_tanh_vol_ma_slope_dispersion_base_v049_signal},
    "f22vt_f22_volume_trend_arctan_volsma_slope_50d_base_v050_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_arctan_volsma_slope_50d_base_v050_signal},
    "f22vt_f22_volume_trend_volwma_20_80_ratio_base_v051_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwma_20_80_ratio_base_v051_signal},
    "f22vt_f22_volume_trend_volwilder_30_90_ratio_base_v052_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwilder_30_90_ratio_base_v052_signal},
    "f22vt_f22_volume_trend_volema_posslope_frac_45d_base_v053_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_posslope_frac_45d_base_v053_signal},
    "f22vt_f22_volume_trend_volsma_posslope_frac_120d_base_v054_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_posslope_frac_120d_base_v054_signal},
    "f22vt_f22_volume_trend_vol_kernel_disp_40d_base_v055_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_kernel_disp_40d_base_v055_signal},
    "f22vt_f22_volume_trend_ribbon_order_sma_base_v056_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_ribbon_order_sma_base_v056_signal},
    "f22vt_f22_volume_trend_dv_z_ema70_diff_volz_base_v057_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_z_ema70_diff_volz_base_v057_signal},
    "f22vt_f22_volume_trend_volsma_acceleration_zscore_base_v058_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_acceleration_zscore_base_v058_signal},
    "f22vt_f22_volume_trend_logvolma_z_252d_base_v059_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvolma_z_252d_base_v059_signal},
    "f22vt_f22_volume_trend_cumupdn_ratio_45d_base_v060_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_cumupdn_ratio_45d_base_v060_signal},
    "f22vt_f22_volume_trend_sign_dv_sma_slope_100d_base_v061_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_sign_dv_sma_slope_100d_base_v061_signal},
    "f22vt_f22_volume_trend_volsma_normrange_60d_base_v062_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_normrange_60d_base_v062_signal},
    "f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_base_v063_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_upvol_downvol_ema_diff_30d_base_v063_signal},
    "f22vt_f22_volume_trend_klinger_34_55_base_v064_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_klinger_34_55_base_v064_signal},
    "f22vt_f22_volume_trend_volma_convergence_55d_base_v065_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_convergence_55d_base_v065_signal},
    "f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_base_v066_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_volsma_slope_pos_100d_base_v066_signal},
    "f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_base_v067_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_rank_within_kernel_60d_base_v067_signal},
    "f22vt_f22_volume_trend_volma_slope_dispersion_80d_base_v068_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_slope_dispersion_80d_base_v068_signal},
    "f22vt_f22_volume_trend_volsma_ac1_60d_base_v069_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_ac1_60d_base_v069_signal},
    "f22vt_f22_volume_trend_logvol_skew_120d_base_v070_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_skew_120d_base_v070_signal},
    "f22vt_f22_volume_trend_hma_vol_curvature_30d_base_v071_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_hma_vol_curvature_30d_base_v071_signal},
    "f22vt_f22_volume_trend_sign_volslope_short_long_base_v072_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_volslope_short_long_base_v072_signal},
    "f22vt_f22_volume_trend_logvolma_long_zscore_300d_base_v073_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvolma_long_zscore_300d_base_v073_signal},
    "f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_base_v074_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_daysince_upvol_downvol_cross_200d_base_v074_signal},
    "f22vt_f22_volume_trend_volma_slope_flip_freq_120d_base_v075_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_slope_flip_freq_120d_base_v075_signal},
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
    for name, entry in f22_volume_trend_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
