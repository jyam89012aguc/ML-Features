import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s vs time index over window w
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (volume-price confirmation) =====
def _f13_obv(close, volume):
    # On-balance volume: signed cumulative volume by price direction
    direction = np.sign(close.diff())
    return (direction * volume).fillna(0.0).cumsum()


def _f13_clv(close, high, low):
    # Close location value within the bar [-1, +1]
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f13_ad_line(close, high, low, volume):
    # Accumulation/Distribution line (Chaikin)
    mfv = _f13_clv(close, high, low) * volume
    return mfv.fillna(0.0).cumsum()


def _f13_cmf(close, high, low, volume, w):
    # Chaikin money flow over window w
    mfv = _f13_clv(close, high, low) * volume
    return _sum(mfv, w) / _sum(volume, w).replace(0, np.nan)


def _f13_typical(close, high, low):
    return (high + low + close) / 3.0


def _f13_mfi(close, high, low, volume, w):
    # Money flow index over window w (0..100)
    tp = _f13_typical(close, high, low)
    rmf = tp * volume
    up = rmf.where(tp.diff() > 0, 0.0)
    dn = rmf.where(tp.diff() < 0, 0.0)
    pmf = _sum(up, w)
    nmf = _sum(dn, w)
    ratio = pmf / nmf.replace(0, np.nan)
    return 100.0 - (100.0 / (1.0 + ratio))


def _f13_force(close, volume, w):
    # Elder force index smoothed over w
    raw = close.diff() * volume
    return raw.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f13_eom(high, low, volume, w):
    # Ease of movement (Arms) smoothed over w; scaled volume
    mid = (high + low) / 2.0
    dist = mid.diff()
    box = volume / (high - low).replace(0, np.nan)
    raw = dist / box.replace(0, np.nan)
    return _mean(raw, w)


def _f13_pvt(close, volume):
    # Price-volume trend cumulative
    return (close.pct_change() * volume).fillna(0.0).cumsum()


# ============================================================
# --- OBV family ---
# OBV slope over a quarter, normalized by avg volume (trend strength)
def f13vc_f13_volume_price_confirmation_obvslope_63d_base_v001_signal(close, volume):
    obv = _f13_obv(close, volume)
    b = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope over a month, normalized by avg volume
def f13vc_f13_volume_price_confirmation_obvslope_21d_base_v002_signal(close, volume):
    obv = _f13_obv(close, volume)
    b = _slope(obv, 21) / _mean(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-price agreement: rolling 21d correlation between OBV level and price level
def f13vc_f13_volume_price_confirmation_obvmom_21d_base_v003_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    b = obv.rolling(21, min_periods=10).corr(closeadj)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV 63d momentum minus 21d momentum (acceleration of accumulation, distinct construction)
def f13vc_f13_volume_price_confirmation_obvmom_63d_base_v004_signal(close, volume):
    obv = _f13_obv(close, volume)
    long_m = (obv - obv.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    short_m = (obv - obv.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    b = long_m - short_m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV displacement: OBV vs its own 63d EMA (normalized)
def f13vc_f13_volume_price_confirmation_obvdisp_63d_base_v005_signal(close, volume):
    obv = _f13_obv(close, volume)
    ema = obv.ewm(span=63, min_periods=21).mean()
    b = (obv - ema) / _sum(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV z-score of its 21d momentum vs 126d history
def f13vc_f13_volume_price_confirmation_obvmomz_126d_base_v006_signal(close, volume):
    obv = _f13_obv(close, volume)
    mom = (obv - obv.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    b = _z(mom, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV acceleration: 21d slope now minus 21d slope a month ago
def f13vc_f13_volume_price_confirmation_obvslopechg_21d_base_v007_signal(close, volume):
    obv = _f13_obv(close, volume)
    sl = _slope(obv, 21) / _mean(volume, 21).replace(0, np.nan)
    b = sl - sl.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized OBV (per-share accumulation) rank vs 126d history
def f13vc_f13_volume_price_confirmation_obvnormrank_126d_base_v008_signal(close, volume):
    obv = _f13_obv(close, volume)
    norm = (obv - obv.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    b = _rank(norm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Accumulation/Distribution line family ---
# A/D line slope over a quarter, normalized by volume scale
def f13vc_f13_volume_price_confirmation_adslope_63d_base_v009_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    b = _slope(ad, 63) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line momentum over 21d scaled by 21d volume sum
def f13vc_f13_volume_price_confirmation_admom_21d_base_v010_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    adn = (ad - ad.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    pxm = closeadj / closeadj.shift(21) - 1.0
    b = adn - np.sign(pxm) * adn.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D line vs price-level divergence: 63d corr between A/D line and price (confirmation)
def f13vc_f13_volume_price_confirmation_admom_63d_base_v011_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    b = ad.rolling(63, min_periods=21).corr(closeadj)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D displacement vs 42d EMA, normalized
def f13vc_f13_volume_price_confirmation_addisp_42d_base_v012_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    ema = ad.ewm(span=42, min_periods=21).mean()
    b = (ad - ema) / _sum(volume, 42).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator: 3d EMA minus 10d EMA of A/D line, normalized
def f13vc_f13_volume_price_confirmation_chaikinosc_base_v013_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    b = osc / _mean(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D displacement (vs 63d EMA) z-scored vs 126d history
def f13vc_f13_volume_price_confirmation_admomz_126d_base_v014_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    disp = (ad - ad.ewm(span=63, min_periods=21).mean()) / _sum(volume, 63).replace(0, np.nan)
    b = _z(disp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D slope acceleration over a month
def f13vc_f13_volume_price_confirmation_adslopechg_63d_base_v015_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    sl = _slope(ad, 63) / _mean(volume, 63).replace(0, np.nan)
    b = sl - sl.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Chaikin money flow family ---
# CMF over 21d (raw accumulation pressure)
def f13vc_f13_volume_price_confirmation_cmf_21d_base_v016_signal(close, high, low, volume):
    b = _f13_cmf(close, high, low, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF over 63d
def f13vc_f13_volume_price_confirmation_cmf_63d_base_v017_signal(close, high, low, volume):
    b = _f13_cmf(close, high, low, volume, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF term-structure spread: short minus long money-flow pressure
def f13vc_f13_volume_price_confirmation_cmfspr_21v63_base_v018_signal(close, high, low, volume):
    s = _f13_cmf(close, high, low, volume, 21)
    l = _f13_cmf(close, high, low, volume, 63)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF momentum: 21d CMF change over a month
def f13vc_f13_volume_price_confirmation_cmfmom_21d_base_v019_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    b = c - c.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF(21) z-scored vs its own 252d history (regime-relative pressure)
def f13vc_f13_volume_price_confirmation_cmfz_252d_base_v020_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF persistence: fraction of last quarter with positive money flow
def f13vc_f13_volume_price_confirmation_cmfpersist_63d_base_v021_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    b = (c > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CMF percentile-rank vs 252d history
def f13vc_f13_volume_price_confirmation_cmfrank_252d_base_v022_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Money-flow index family ---
# MFI over 14d, centered
def f13vc_f13_volume_price_confirmation_mfi_14d_base_v023_signal(close, high, low, volume):
    b = _f13_mfi(close, high, low, volume, 14) - 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI over 21d, centered
def f13vc_f13_volume_price_confirmation_mfi_21d_base_v024_signal(close, high, low, volume):
    b = _f13_mfi(close, high, low, volume, 21) - 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI term-structure spread (14d vs 63d)
def f13vc_f13_volume_price_confirmation_mfispr_14v63_base_v025_signal(close, high, low, volume):
    s = _f13_mfi(close, high, low, volume, 14)
    l = _f13_mfi(close, high, low, volume, 63)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI momentum over a month
def f13vc_f13_volume_price_confirmation_mfimom_14d_base_v026_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    b = m - m.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI overbought pressure: avg distance above 50 when MFI>50 over a quarter
def f13vc_f13_volume_price_confirmation_mfiobtime_63d_base_v027_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    excess = (m - 50.0).clip(lower=0)
    b = _mean(excess, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI oversold pressure: avg distance below 50 when MFI<50 over a quarter
def f13vc_f13_volume_price_confirmation_mfiostime_63d_base_v028_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 14)
    deficit = (50.0 - m).clip(lower=0)
    b = _mean(deficit, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI z-scored vs 252d history
def f13vc_f13_volume_price_confirmation_mfiz_252d_base_v029_signal(close, high, low, volume):
    m = _f13_mfi(close, high, low, volume, 21)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Force index family ---
# Force index smoothed over 13d, normalized by dollar-volume scale
def f13vc_f13_volume_price_confirmation_force_13d_base_v030_signal(close, volume):
    f = _f13_force(close, volume, 13)
    b = f / (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index term-structure: fast 13d force minus slow 63d force (impulse vs base)
def f13vc_f13_volume_price_confirmation_force_21d_base_v031_signal(close, volume):
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    fast = _f13_force(close, volume, 13) / nrm
    slow = _f13_force(close, volume, 63) / nrm
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index sign-persistence over a quarter
def f13vc_f13_volume_price_confirmation_forcepersist_63d_base_v032_signal(close, volume):
    f = _f13_force(close, volume, 13)
    b = np.sign(f).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index z-scored vs 126d history
def f13vc_f13_volume_price_confirmation_forcez_126d_base_v033_signal(close, volume):
    f = _f13_force(close, volume, 13)
    b = _z(f, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index momentum (13d force change over a month)
def f13vc_f13_volume_price_confirmation_forcemom_13d_base_v034_signal(close, volume):
    f = _f13_force(close, volume, 13)
    nrm = (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    fn = f / nrm
    b = fn - fn.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Ease of movement family ---
# EOM smoothed over 14d, scaled
def f13vc_f13_volume_price_confirmation_eom_14d_base_v035_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    b = e * 1e6
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM smoothed over 21d
def f13vc_f13_volume_price_confirmation_eom_21d_base_v036_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 21)
    b = e * 1e6
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM z-scored vs 126d history (regime-relative ease)
def f13vc_f13_volume_price_confirmation_eomz_126d_base_v037_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    b = _z(e, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM sign-persistence over a quarter
def f13vc_f13_volume_price_confirmation_eompersist_63d_base_v038_signal(high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    b = np.sign(e).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume-price divergence family ---
# Price up while volume down: corr between price change and volume change (21d)
def f13vc_f13_volume_price_confirmation_pvcorr_21d_base_v039_signal(closeadj, volume):
    pc = closeadj.pct_change()
    vc = volume.pct_change()
    b = pc.rolling(21, min_periods=10).corr(vc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Price-volume correlation over 63d (>21d window -> closeadj)
def f13vc_f13_volume_price_confirmation_pvcorr_63d_base_v040_signal(closeadj, volume):
    pc = closeadj.pct_change()
    vc = volume.pct_change()
    b = pc.rolling(63, min_periods=21).corr(vc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Divergence: price up-trend with volume down-trend (sign mismatch of slopes)
def f13vc_f13_volume_price_confirmation_pvdiverg_63d_base_v041_signal(closeadj, volume):
    psl = _slope(np.log(closeadj.replace(0, np.nan)), 63)
    vsl = _slope(np.log(volume.replace(0, np.nan)), 63)
    b = np.sign(psl) * (-vsl) * np.log(volume.replace(0, np.nan)).rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up-day vs down-day volume ratio over 21d (effort confirmation)
def f13vc_f13_volume_price_confirmation_updnvol_21d_base_v042_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    dn = volume.where(closeadj.diff() < 0, 0.0)
    b = (_sum(up, 21) - _sum(dn, 21)) / _sum(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Up vs down volume ratio over 63d
def f13vc_f13_volume_price_confirmation_updnvol_63d_base_v043_signal(closeadj, volume):
    up = volume.where(closeadj.diff() > 0, 0.0)
    dn = volume.where(closeadj.diff() < 0, 0.0)
    b = (_sum(up, 63) - _sum(dn, 63)) / _sum(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-weighted return: avg of (return x volume-share) over 21d (effort efficiency)
def f13vc_f13_volume_price_confirmation_vwret_21d_base_v044_signal(closeadj, volume):
    ret = closeadj.pct_change()
    vw = (ret * volume).rolling(21, min_periods=10).sum() / _sum(volume, 21).replace(0, np.nan)
    b = vw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Effort-vs-result: 21d abs price move per unit of volume (price impact efficiency)
def f13vc_f13_volume_price_confirmation_effortresult_21d_base_v045_signal(closeadj, volume):
    move = (closeadj / closeadj.shift(21) - 1.0).abs()
    effort = _sum(volume, 21)
    b = move / effort.replace(0, np.nan) * _mean(volume, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Divergence magnitude: price-up strength times OBV-down strength over 63d
def f13vc_f13_volume_price_confirmation_obvpxdiv_63d_base_v046_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    pxchg = (closeadj / closeadj.shift(21) - 1.0)
    obvchg = (obv - obv.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    div = pxchg.clip(lower=0) * (-obvchg).clip(lower=0)
    b = _mean(div, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Price-volume trend (PVT) family ---
# PVT slope over a quarter, normalized
def f13vc_f13_volume_price_confirmation_pvtslope_63d_base_v047_signal(closeadj, volume):
    pvt = _f13_pvt(closeadj, volume)
    b = _slope(pvt, 63) / _mean(volume, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PVT level vs price-level rolling correlation over 63d (trend confirmation)
def f13vc_f13_volume_price_confirmation_pvtmom_21d_base_v048_signal(closeadj, volume):
    pvt = _f13_pvt(closeadj, volume)
    b = pvt.rolling(63, min_periods=21).corr(closeadj)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PVT displacement vs 42d EMA
def f13vc_f13_volume_price_confirmation_pvtdisp_42d_base_v049_signal(closeadj, volume):
    pvt = _f13_pvt(closeadj, volume)
    ema = pvt.ewm(span=42, min_periods=21).mean()
    b = (pvt - ema) / _sum(volume, 42).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume-weighted CLV / accumulation pressure variants ---
# CLV concentration: gap between volume-weighted CLV and equal-weighted CLV (21d)
def f13vc_f13_volume_price_confirmation_wclv_21d_base_v050_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    vw = _sum(clv * volume, 21) / _sum(volume, 21).replace(0, np.nan)
    ew = _mean(clv, 21)
    b = vw - ew
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CLV distribution skew over 63d (asymmetry of intrabar closing strength)
def f13vc_f13_volume_price_confirmation_clvmean_63d_base_v051_signal(close, high, low):
    clv = _f13_clv(close, high, low)
    b = clv.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CLV persistence: 21d lag-1 autocorrelation of close-location-value
def f13vc_f13_volume_price_confirmation_clvvolcov_21d_base_v052_signal(close, high, low):
    clv = _f13_clv(close, high, low)
    b = clv.rolling(21, min_periods=12).apply(
        lambda a: pd.Series(a).autocorr(lag=1) if np.std(a) > 0 else np.nan, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume-confirmed momentum ---
# Return-volume product trend: cumulative signed-effort over 21d, ranked
def f13vc_f13_volume_price_confirmation_signedeffortrank_21d_base_v053_signal(closeadj, volume):
    se = np.sign(closeadj.diff()) * volume
    cum = _sum(se, 21) / _sum(volume, 21).replace(0, np.nan)
    b = _rank(cum, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-confirmed breakout: 21d return x relative volume (confirmation strength)
def f13vc_f13_volume_price_confirmation_volconfirm_21d_base_v054_signal(closeadj, volume):
    ret = closeadj / closeadj.shift(21) - 1.0
    relv = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    b = ret * relv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Negative-volume-index proxy: cumulative return on low-volume days (21d)
def f13vc_f13_volume_price_confirmation_nvi_21d_base_v055_signal(closeadj, volume):
    quiet = (volume < volume.shift(1)).astype(float)
    contrib = closeadj.pct_change() * quiet
    b = _sum(contrib, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Positive-volume-index proxy: cumulative return on high-volume days (21d)
def f13vc_f13_volume_price_confirmation_pvi_21d_base_v056_signal(closeadj, volume):
    loud = (volume > volume.shift(1)).astype(float)
    contrib = closeadj.pct_change() * loud
    b = _sum(contrib, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Smart-money divergence: PVI minus NVI return contribution (63d)
def f13vc_f13_volume_price_confirmation_pvinvispr_63d_base_v057_signal(closeadj, volume):
    loud = (volume > volume.shift(1)).astype(float)
    quiet = 1.0 - loud
    ret = closeadj.pct_change()
    b = _sum(ret * loud, 63) - _sum(ret * quiet, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Chaikin volatility-confirmation hybrids (still money-flow domain) ---
# CMF interacted with up/down volume balance (double accumulation confirmation)
def f13vc_f13_volume_price_confirmation_cmfvolbal_21d_base_v058_signal(close, high, low, volume):
    cmf = _f13_cmf(close, high, low, volume, 21)
    up = volume.where(close.diff() > 0, 0.0)
    dn = volume.where(close.diff() < 0, 0.0)
    bal = (_sum(up, 21) - _sum(dn, 21)) / _sum(volume, 21).replace(0, np.nan)
    b = cmf * np.sign(bal) * (bal.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# A/D-line vs price divergence: A/D momentum minus price momentum (63d)
def f13vc_f13_volume_price_confirmation_adpxdiv_63d_base_v059_signal(closeadj, close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    adm = (ad - ad.shift(63)) / _sum(volume, 63).replace(0, np.nan)
    pxm = np.sign(closeadj / closeadj.shift(63) - 1.0)
    b = adm * (-pxm) + adm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MFI vs price-RSI-direction divergence (money-flow not confirming price, 14d)
def f13vc_f13_volume_price_confirmation_mfipxdiv_14d_base_v060_signal(closeadj, close, high, low, volume):
    mfi = _f13_mfi(close, high, low, volume, 14) - 50.0
    pxdir = np.sign(closeadj / closeadj.shift(14) - 1.0)
    b = -(np.sign(mfi) * pxdir) * mfi.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Dollar-volume confirmation (>21d uses closeadj) ---
# Price-tilt of accumulation: dollar-weighted CLV minus volume-weighted CLV (63d)
def f13vc_f13_volume_price_confirmation_dvclv_63d_base_v061_signal(closeadj, close, high, low, volume):
    clv = _f13_clv(close, high, low)
    dv = closeadj * volume
    dollar_w = _sum(clv * dv, 63) / _sum(dv, 63).replace(0, np.nan)
    vol_w = _sum(clv * volume, 63) / _sum(volume, 63).replace(0, np.nan)
    b = (dollar_w - vol_w) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Dollar-volume CMF de-trended: 63d dollar-CMF minus its 252d EMA baseline
def f13vc_f13_volume_price_confirmation_dvcmf_63d_base_v062_signal(closeadj, close, high, low, volume):
    clv = _f13_clv(close, high, low)
    dv = closeadj * volume
    mfv = clv * dv
    dvcmf = _sum(mfv, 63) / _sum(dv, 63).replace(0, np.nan)
    b = dvcmf - dvcmf.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force index in dollar terms over 21d, normalized by 252d dollar-vol
def f13vc_f13_volume_price_confirmation_dvforce_21d_base_v063_signal(closeadj, volume):
    raw = closeadj.diff() * volume
    f = raw.ewm(span=21, min_periods=10).mean()
    b = f / _mean(closeadj * volume, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Accumulation streaks & regime ---
# Accumulation streak: consecutive days CMF>0 (capped), centered
def f13vc_f13_volume_price_confirmation_accstreak_base_v064_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    pos = (c > 0).astype(float)
    grp = (pos != pos.shift(1)).cumsum()
    streak = pos.groupby(grp).cumsum()
    b = np.tanh(streak / 21.0) * np.sign(c)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow regime z: 63d CMF minus 252d CMF baseline
def f13vc_f13_volume_price_confirmation_cmfregime_base_v065_signal(close, high, low, volume):
    s = _f13_cmf(close, high, low, volume, 63)
    l = _f13_cmf(close, high, low, volume, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-to-price elasticity: OBV-norm change per unit price change (21d)
def f13vc_f13_volume_price_confirmation_obvelast_21d_base_v066_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    dobv = (obv - obv.shift(21)) / _sum(volume, 21).replace(0, np.nan)
    dpx = closeadj / closeadj.shift(21) - 1.0
    b = dobv / dpx.replace(0, np.nan)
    result = b.clip(-50, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-thrust on up moves: avg relative volume on up days minus down days (21d)
def f13vc_f13_volume_price_confirmation_volthrust_21d_base_v067_signal(closeadj, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    up = relv.where(closeadj.diff() > 0)
    dn = relv.where(closeadj.diff() < 0)
    b = _mean(up, 21) - _mean(dn, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator z-scored vs 126d history
def f13vc_f13_volume_price_confirmation_chaikinoscz_126d_base_v068_signal(close, high, low, volume):
    ad = _f13_ad_line(close, high, low, volume)
    osc = ad.ewm(span=3, min_periods=2).mean() - ad.ewm(span=10, min_periods=5).mean()
    oscn = osc / _mean(volume, 21).replace(0, np.nan)
    b = _z(oscn, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EOM x return: ease-confirmed momentum over 21d
def f13vc_f13_volume_price_confirmation_eomret_21d_base_v069_signal(closeadj, high, low, volume):
    e = _f13_eom(high, low, volume, 14)
    ret = closeadj / closeadj.shift(21) - 1.0
    b = np.sign(e) * (e.abs() ** 0.5) * 1e3 * np.sign(ret)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Force-index vs price-momentum confirmation spread (21d)
def f13vc_f13_volume_price_confirmation_forceconf_21d_base_v070_signal(closeadj, close, volume):
    f = _f13_force(close, volume, 13)
    fn = f / (_mean(volume, 63) * _mean(close.abs(), 63)).replace(0, np.nan)
    pxm = np.sign(closeadj / closeadj.shift(21) - 1.0)
    b = fn * pxm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow breadth: fraction of last 63d with CLV>0 weighted by volume
def f13vc_f13_volume_price_confirmation_mfbreadth_63d_base_v071_signal(close, high, low, volume):
    clv = _f13_clv(close, high, low)
    pos = (clv > 0).astype(float) * volume
    b = _sum(pos, 63) / _sum(volume, 63).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Distribution warning: high-volume down-bars share over 21d
def f13vc_f13_volume_price_confirmation_distwarn_21d_base_v072_signal(closeadj, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    heavy_dn = ((closeadj.diff() < 0) & (relv > 1.0)).astype(float) * relv
    b = _sum(heavy_dn, 21) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Money-flow regime instability: 63d std of the daily CMF(21) series (conviction = low)
def f13vc_f13_volume_price_confirmation_accconv_63d_base_v073_signal(close, high, low, volume):
    c = _f13_cmf(close, high, low, volume, 21)
    b = _std(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope vs price slope confirmation ratio (63d) - trend agreement
def f13vc_f13_volume_price_confirmation_obvpxagree_63d_base_v074_signal(closeadj, close, volume):
    obv = _f13_obv(close, volume)
    obvsl = _slope(obv, 63) / _mean(volume, 63).replace(0, np.nan)
    pxsl = _slope(np.log(closeadj.replace(0, np.nan)), 63)
    b = np.tanh(obvsl) * np.sign(pxsl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Volume-price elasticity dispersion: std of daily |ret|/relvol over 63d
def f13vc_f13_volume_price_confirmation_vpelastdisp_63d_base_v075_signal(closeadj, volume):
    relv = volume / _mean(volume, 63).replace(0, np.nan)
    impact = closeadj.pct_change().abs() / relv.replace(0, np.nan)
    b = _std(impact, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13vc_f13_volume_price_confirmation_obvslope_63d_base_v001_signal,
    f13vc_f13_volume_price_confirmation_obvslope_21d_base_v002_signal,
    f13vc_f13_volume_price_confirmation_obvmom_21d_base_v003_signal,
    f13vc_f13_volume_price_confirmation_obvmom_63d_base_v004_signal,
    f13vc_f13_volume_price_confirmation_obvdisp_63d_base_v005_signal,
    f13vc_f13_volume_price_confirmation_obvmomz_126d_base_v006_signal,
    f13vc_f13_volume_price_confirmation_obvslopechg_21d_base_v007_signal,
    f13vc_f13_volume_price_confirmation_obvnormrank_126d_base_v008_signal,
    f13vc_f13_volume_price_confirmation_adslope_63d_base_v009_signal,
    f13vc_f13_volume_price_confirmation_admom_21d_base_v010_signal,
    f13vc_f13_volume_price_confirmation_admom_63d_base_v011_signal,
    f13vc_f13_volume_price_confirmation_addisp_42d_base_v012_signal,
    f13vc_f13_volume_price_confirmation_chaikinosc_base_v013_signal,
    f13vc_f13_volume_price_confirmation_admomz_126d_base_v014_signal,
    f13vc_f13_volume_price_confirmation_adslopechg_63d_base_v015_signal,
    f13vc_f13_volume_price_confirmation_cmf_21d_base_v016_signal,
    f13vc_f13_volume_price_confirmation_cmf_63d_base_v017_signal,
    f13vc_f13_volume_price_confirmation_cmfspr_21v63_base_v018_signal,
    f13vc_f13_volume_price_confirmation_cmfmom_21d_base_v019_signal,
    f13vc_f13_volume_price_confirmation_cmfz_252d_base_v020_signal,
    f13vc_f13_volume_price_confirmation_cmfpersist_63d_base_v021_signal,
    f13vc_f13_volume_price_confirmation_cmfrank_252d_base_v022_signal,
    f13vc_f13_volume_price_confirmation_mfi_14d_base_v023_signal,
    f13vc_f13_volume_price_confirmation_mfi_21d_base_v024_signal,
    f13vc_f13_volume_price_confirmation_mfispr_14v63_base_v025_signal,
    f13vc_f13_volume_price_confirmation_mfimom_14d_base_v026_signal,
    f13vc_f13_volume_price_confirmation_mfiobtime_63d_base_v027_signal,
    f13vc_f13_volume_price_confirmation_mfiostime_63d_base_v028_signal,
    f13vc_f13_volume_price_confirmation_mfiz_252d_base_v029_signal,
    f13vc_f13_volume_price_confirmation_force_13d_base_v030_signal,
    f13vc_f13_volume_price_confirmation_force_21d_base_v031_signal,
    f13vc_f13_volume_price_confirmation_forcepersist_63d_base_v032_signal,
    f13vc_f13_volume_price_confirmation_forcez_126d_base_v033_signal,
    f13vc_f13_volume_price_confirmation_forcemom_13d_base_v034_signal,
    f13vc_f13_volume_price_confirmation_eom_14d_base_v035_signal,
    f13vc_f13_volume_price_confirmation_eom_21d_base_v036_signal,
    f13vc_f13_volume_price_confirmation_eomz_126d_base_v037_signal,
    f13vc_f13_volume_price_confirmation_eompersist_63d_base_v038_signal,
    f13vc_f13_volume_price_confirmation_pvcorr_21d_base_v039_signal,
    f13vc_f13_volume_price_confirmation_pvcorr_63d_base_v040_signal,
    f13vc_f13_volume_price_confirmation_pvdiverg_63d_base_v041_signal,
    f13vc_f13_volume_price_confirmation_updnvol_21d_base_v042_signal,
    f13vc_f13_volume_price_confirmation_updnvol_63d_base_v043_signal,
    f13vc_f13_volume_price_confirmation_vwret_21d_base_v044_signal,
    f13vc_f13_volume_price_confirmation_effortresult_21d_base_v045_signal,
    f13vc_f13_volume_price_confirmation_obvpxdiv_63d_base_v046_signal,
    f13vc_f13_volume_price_confirmation_pvtslope_63d_base_v047_signal,
    f13vc_f13_volume_price_confirmation_pvtmom_21d_base_v048_signal,
    f13vc_f13_volume_price_confirmation_pvtdisp_42d_base_v049_signal,
    f13vc_f13_volume_price_confirmation_wclv_21d_base_v050_signal,
    f13vc_f13_volume_price_confirmation_clvmean_63d_base_v051_signal,
    f13vc_f13_volume_price_confirmation_clvvolcov_21d_base_v052_signal,
    f13vc_f13_volume_price_confirmation_signedeffortrank_21d_base_v053_signal,
    f13vc_f13_volume_price_confirmation_volconfirm_21d_base_v054_signal,
    f13vc_f13_volume_price_confirmation_nvi_21d_base_v055_signal,
    f13vc_f13_volume_price_confirmation_pvi_21d_base_v056_signal,
    f13vc_f13_volume_price_confirmation_pvinvispr_63d_base_v057_signal,
    f13vc_f13_volume_price_confirmation_cmfvolbal_21d_base_v058_signal,
    f13vc_f13_volume_price_confirmation_adpxdiv_63d_base_v059_signal,
    f13vc_f13_volume_price_confirmation_mfipxdiv_14d_base_v060_signal,
    f13vc_f13_volume_price_confirmation_dvclv_63d_base_v061_signal,
    f13vc_f13_volume_price_confirmation_dvcmf_63d_base_v062_signal,
    f13vc_f13_volume_price_confirmation_dvforce_21d_base_v063_signal,
    f13vc_f13_volume_price_confirmation_accstreak_base_v064_signal,
    f13vc_f13_volume_price_confirmation_cmfregime_base_v065_signal,
    f13vc_f13_volume_price_confirmation_obvelast_21d_base_v066_signal,
    f13vc_f13_volume_price_confirmation_volthrust_21d_base_v067_signal,
    f13vc_f13_volume_price_confirmation_chaikinoscz_126d_base_v068_signal,
    f13vc_f13_volume_price_confirmation_eomret_21d_base_v069_signal,
    f13vc_f13_volume_price_confirmation_forceconf_21d_base_v070_signal,
    f13vc_f13_volume_price_confirmation_mfbreadth_63d_base_v071_signal,
    f13vc_f13_volume_price_confirmation_distwarn_21d_base_v072_signal,
    f13vc_f13_volume_price_confirmation_accconv_63d_base_v073_signal,
    f13vc_f13_volume_price_confirmation_obvpxagree_63d_base_v074_signal,
    f13vc_f13_volume_price_confirmation_vpelastdisp_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_VOLUME_PRICE_CONFIRMATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f13_volume_price_confirmation_base_001_075_claude: %d features pass" % n_features)
