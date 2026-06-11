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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (volume-price confirmation) =====
def _f15_obv(close, volume):
    return (np.sign(close.diff()) * volume).fillna(0.0).cumsum()


def _f15_signed_dollar(closeadj, volume):
    return (np.sign(closeadj.diff()) * closeadj * volume).fillna(0.0).cumsum()


def _f15_clv(close, high, low):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f15_adline(close, high, low, volume):
    return (_f15_clv(close, high, low) * volume).fillna(0.0).cumsum()


def _f15_cmf(close, high, low, volume, w):
    mfv = _f15_clv(close, high, low) * volume
    num = mfv.rolling(w, min_periods=max(2, w // 2)).sum()
    den = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    return num / den


def _f15_mfi(close, high, low, volume, w):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    up = rmf.where(tp.diff() > 0, 0.0)
    dn = rmf.where(tp.diff() < 0, 0.0)
    pos = up.rolling(w, min_periods=max(2, w // 2)).sum()
    neg = dn.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + pos / neg)


def _f15_force(closeadj, volume, w):
    return (closeadj.diff() * volume).ewm(span=w, min_periods=max(2, w // 2)).mean()


def _f15_updownvol(close, volume, w):
    up = volume.where(close.diff() > 0, 0.0)
    dn = volume.where(close.diff() < 0, 0.0)
    su = up.rolling(w, min_periods=max(2, w // 2)).sum()
    sd = dn.rolling(w, min_periods=max(2, w // 2)).sum()
    return (su - sd) / (su + sd).replace(0, np.nan)


def _f15_pvt(closeadj, volume):
    return (closeadj.pct_change() * volume).fillna(0.0).cumsum()


def _f15_eom(closeadj, high, low, volume, w):
    mid = (high + low) / 2.0
    box = volume / (high - low).replace(0, np.nan)
    return (mid.diff() / box.replace(0, np.nan)).rolling(w, min_periods=max(2, w // 2)).mean()


def _f15_cumforce(closeadj, volume):
    return (closeadj.diff() * volume).fillna(0.0).cumsum()


def _f15_obvz(close, volume, w):
    return _z(_f15_obv(close, volume), w)


def _f15_adz(close, high, low, volume, w):
    return _z(_f15_adline(close, high, low, volume), w)


def _f15_vwclv(close, high, low, volume, w):
    clv = _f15_clv(close, high, low)
    num = (clv * volume).rolling(w, min_periods=max(2, w // 2)).sum()
    den = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    return num / den


def _f15_vwapgap(closeadj, volume, w):
    pv = (closeadj * volume).rolling(w, min_periods=max(2, w // 2)).sum()
    v = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    return closeadj / (pv / v) - 1.0


# 2nd math derivative (jerk): rate of change of the slope of a base over w days.
def _jerk(base, w):
    sl = base.diff(w) / float(w)
    return sl.diff(w) / float(w)


# ============================================================
# --- OBV z-score slopes (accumulation trend velocity) ---
def f15vc_f15_volume_price_confirmation_obvz_63d_jerk_v001_signal(close, volume):
    base = _f15_obvz(close, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvz_63d_jerk_v002_signal(close, volume):
    base = _f15_obvz(close, volume, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvz_126d_jerk_v003_signal(close, volume):
    base = _f15_obvz(close, volume, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvz_126d_jerk_v004_signal(close, volume):
    base = _f15_obvz(close, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvz_252d_jerk_v005_signal(close, volume):
    base = _f15_obvz(close, volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvz_252d_jerk_v006_signal(close, volume):
    base = _f15_obvz(close, volume, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- A/D z-score slopes ---
def f15vc_f15_volume_price_confirmation_adz_63d_jerk_v007_signal(close, high, low, volume):
    base = _f15_adz(close, high, low, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_adz_126d_jerk_v008_signal(close, high, low, volume):
    base = _f15_adz(close, high, low, volume, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_adz_126d_jerk_v009_signal(close, high, low, volume):
    base = _f15_adz(close, high, low, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_adz_252d_jerk_v010_signal(close, high, low, volume):
    base = _f15_adz(close, high, low, volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_adz_252d_jerk_v011_signal(close, high, low, volume):
    base = _f15_adz(close, high, low, volume, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Chaikin money-flow slopes ---
def f15vc_f15_volume_price_confirmation_cmf_21d_jerk_v012_signal(close, high, low, volume):
    base = _f15_cmf(close, high, low, volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmf_21d_jerk_v013_signal(close, high, low, volume):
    base = _f15_cmf(close, high, low, volume, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmf_63d_jerk_v014_signal(close, high, low, volume):
    base = _f15_cmf(close, high, low, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmf_63d_jerk_v015_signal(close, high, low, volume):
    base = _f15_cmf(close, high, low, volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmf_126d_jerk_v016_signal(close, high, low, volume):
    base = _f15_cmf(close, high, low, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmf_126d_jerk_v017_signal(close, high, low, volume):
    base = _f15_cmf(close, high, low, volume, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Money-flow index slopes ---
def f15vc_f15_volume_price_confirmation_mfi_14d_jerk_v018_signal(close, high, low, volume):
    base = _f15_mfi(close, high, low, volume, 14)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfi_21d_jerk_v019_signal(close, high, low, volume):
    base = _f15_mfi(close, high, low, volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfi_21d_jerk_v020_signal(close, high, low, volume):
    base = _f15_mfi(close, high, low, volume, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfi_63d_jerk_v021_signal(close, high, low, volume):
    base = _f15_mfi(close, high, low, volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfi_63d_jerk_v022_signal(close, high, low, volume):
    base = _f15_mfi(close, high, low, volume, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Force index z slopes ---
def f15vc_f15_volume_price_confirmation_forcesign_jerk_v023_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 13)
    base = np.sign(fi).rolling(42, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forcez_21d_jerk_v024_signal(closeadj, volume):
    base = _z(_f15_force(closeadj, volume, 21), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forcez_21d_jerk_v025_signal(closeadj, volume):
    base = _z(_f15_force(closeadj, volume, 21), 126)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forcez_63d_jerk_v026_signal(closeadj, volume):
    base = _z(_f15_force(closeadj, volume, 63), 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forcez_63d_jerk_v027_signal(closeadj, volume):
    base = _z(_f15_force(closeadj, volume, 63), 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Up/down volume share slopes ---
def f15vc_f15_volume_price_confirmation_udvol_21d_jerk_v028_signal(close, volume):
    base = _f15_updownvol(close, volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_udvol_63d_jerk_v029_signal(close, volume):
    base = _f15_updownvol(close, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_udvol_63d_jerk_v030_signal(close, volume):
    base = _f15_updownvol(close, volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_udvol_126d_jerk_v031_signal(close, volume):
    base = _f15_updownvol(close, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- PVT z slopes ---
def f15vc_f15_volume_price_confirmation_pvtz_63d_jerk_v032_signal(closeadj, volume):
    base = _z(_f15_pvt(closeadj, volume), 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_pvtz_126d_jerk_v033_signal(closeadj, volume):
    base = _z(_f15_pvt(closeadj, volume), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_pvtz_126d_jerk_v034_signal(closeadj, volume):
    base = _z(_f15_pvt(closeadj, volume), 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Signed dollar-volume flow vs price divergence slopes ---
def f15vc_f15_volume_price_confirmation_sdvdiv_63d_jerk_v035_signal(closeadj, volume):
    sdv_sl = _z(_f15_signed_dollar(closeadj, volume).diff(63) / 63.0, 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    base = sdv_sl - px_sl
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_sdvdiv_126d_jerk_v036_signal(closeadj, volume):
    sdv_sl = _z(_f15_signed_dollar(closeadj, volume).diff(126) / 126.0, 252)
    px_sl = _z((closeadj - closeadj.shift(126)) / 126.0, 252)
    base = sdv_sl - px_sl
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Ease of movement slopes ---
def f15vc_f15_volume_price_confirmation_eom_21d_jerk_v037_signal(closeadj, high, low, volume):
    base = _z(_f15_eom(closeadj, high, low, volume, 21), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_eom_63d_jerk_v038_signal(closeadj, high, low, volume):
    base = _z(_f15_eom(closeadj, high, low, volume, 63), 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Close location value slopes ---
def f15vc_f15_volume_price_confirmation_clv_21d_jerk_v039_signal(close, high, low):
    base = _f15_clv(close, high, low).rolling(21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_distday_jerk_v040_signal(close, high, low, volume):
    weak = ((close.diff() < 0) & (_f15_clv(close, high, low) < 0))
    base = volume.where(weak, 0.0).rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_accday_jerk_v041_signal(close, high, low, volume):
    strong = ((close.diff() > 0) & (_f15_clv(close, high, low) > 0))
    base = volume.where(strong, 0.0).rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- VWAP-gap slopes ---
def f15vc_f15_volume_price_confirmation_vwapgap_21d_jerk_v042_signal(closeadj, volume):
    base = _f15_vwapgap(closeadj, volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_vwapgap_63d_jerk_v043_signal(closeadj, volume):
    base = _f15_vwapgap(closeadj, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_vwapgap_63d_jerk_v044_signal(closeadj, volume):
    base = _f15_vwapgap(closeadj, volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- CMF rank slopes ---
def f15vc_f15_volume_price_confirmation_cmfrank_63d_jerk_v045_signal(close, high, low, volume):
    base = _rank(_f15_cmf(close, high, low, volume, 63), 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmfrank_21d_jerk_v046_signal(close, high, low, volume):
    base = _rank(_f15_cmf(close, high, low, volume, 21), 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Force EMA rank slopes ---
def f15vc_f15_volume_price_confirmation_forcerank_21d_jerk_v047_signal(closeadj, volume):
    base = _rank(_f15_force(closeadj, volume, 21), 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forcerank_63d_jerk_v048_signal(closeadj, volume):
    base = _rank(_f15_force(closeadj, volume, 63), 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- MFI rank slopes ---
def f15vc_f15_volume_price_confirmation_mfihot_jerk_v049_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 14)
    base = (mfi > 70).astype(float).rolling(42, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfirank_63d_jerk_v050_signal(close, high, low, volume):
    base = _rank(_f15_mfi(close, high, low, volume, 63), 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Force-EMA term-spread slopes (fast vs slow money pressure) ---
def f15vc_f15_volume_price_confirmation_forcetermspr_jerk_v051_signal(closeadj, volume):
    scale = (closeadj.diff().abs() * volume).ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    base = (_f15_force(closeadj, volume, 8) - _f15_force(closeadj, volume, 34)) / scale
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forcetermspr_jerk_v052_signal(closeadj, volume):
    scale = (closeadj.diff().abs() * volume).ewm(span=126, min_periods=63).mean().replace(0, np.nan)
    base = (_f15_force(closeadj, volume, 21) - _f15_force(closeadj, volume, 89)) / scale
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Chaikin oscillator slopes ---
def f15vc_f15_volume_price_confirmation_chaikinosc_jerk_v053_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    base = ad.ewm(span=21, min_periods=10).mean() - ad.ewm(span=63, min_periods=21).mean()
    base = _z(base, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_chaikinosc_jerk_v054_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    base = ad.ewm(span=21, min_periods=10).mean() - ad.ewm(span=63, min_periods=21).mean()
    base = _z(base, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- OBV momentum-osc slopes ---
def f15vc_f15_volume_price_confirmation_obvosc_jerk_v055_signal(close, volume):
    obv = _f15_obv(close, volume)
    scale = obv.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = (obv.ewm(span=21, min_periods=10).mean() - obv.ewm(span=63, min_periods=21).mean()) / scale
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvosc_jerk_v056_signal(close, volume):
    obv = _f15_obv(close, volume)
    scale = obv.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = (obv.ewm(span=21, min_periods=10).mean() - obv.ewm(span=63, min_periods=21).mean()) / scale
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- VWAP-gap z slopes ---
def f15vc_f15_volume_price_confirmation_vwapgapz_63d_jerk_v057_signal(closeadj, volume):
    base = _z(_f15_vwapgap(closeadj, volume, 63), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_vwapgapz_63d_jerk_v058_signal(closeadj, volume):
    base = _z(_f15_vwapgap(closeadj, volume, 63), 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume-price correlation slopes ---
def f15vc_f15_volume_price_confirmation_vpcorr_63d_jerk_v059_signal(closeadj, volume):
    base = closeadj.pct_change().rolling(63, min_periods=21).corr(volume.pct_change())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_vpcorr_126d_jerk_v060_signal(closeadj, volume):
    base = closeadj.pct_change().rolling(126, min_periods=63).corr(volume.pct_change())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- A/D range-position slopes ---
def f15vc_f15_volume_price_confirmation_adrngpos_jerk_v061_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    hi = ad.rolling(252, min_periods=63).max()
    lo = ad.rolling(252, min_periods=63).min()
    base = (ad - lo) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvrngpos_jerk_v062_signal(close, volume):
    obv = _f15_obv(close, volume)
    hi = obv.rolling(126, min_periods=63).max()
    lo = obv.rolling(126, min_periods=63).min()
    base = (obv - lo) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- NVI / PVI slopes ---
def f15vc_f15_volume_price_confirmation_nvitrend_jerk_v063_signal(close, volume):
    ret = close.pct_change()
    quiet = (volume.diff() < 0)
    nvi = (1.0 + ret.where(quiet, 0.0).fillna(0.0)).cumprod()
    base = nvi / nvi.ewm(span=126, min_periods=63).mean().replace(0, np.nan) - 1.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_pvitrend_jerk_v064_signal(close, volume):
    ret = close.pct_change()
    loud = (volume.diff() > 0)
    pvi = (1.0 + ret.where(loud, 0.0).fillna(0.0)).cumprod()
    base = pvi / pvi.ewm(span=126, min_periods=63).mean().replace(0, np.nan) - 1.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- CMF term-spread slopes ---
def f15vc_f15_volume_price_confirmation_cmfspr_jerk_v065_signal(close, high, low, volume):
    base = _f15_cmf(close, high, low, volume, 21) - _f15_cmf(close, high, low, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfivolasym_jerk_v066_signal(close, high, low, volume):
    tp = (high + low + close) / 3.0
    upv = volume.where(tp.diff() > 0, np.nan)
    dnv = volume.where(tp.diff() < 0, np.nan)
    base = np.log(upv.rolling(63, min_periods=15).mean() / dnv.rolling(63, min_periods=15).mean().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume-weighted return slopes ---
def f15vc_f15_volume_price_confirmation_vwret_21d_jerk_v067_signal(closeadj, volume):
    ret = closeadj.pct_change()
    num = (ret * volume).rolling(21, min_periods=10).sum()
    den = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    base = _z(num / den, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_retvolasym_jerk_v068_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = (ret.clip(lower=0) * volume).rolling(63, min_periods=21).sum()
    dn = (ret.clip(upper=0).abs() * volume).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- CMF persistence slopes ---
def f15vc_f15_volume_price_confirmation_cmfpersist_jerk_v069_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    base = (cmf > 0).astype(float).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forcepersist_jerk_v070_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 13)
    base = np.sign(fi).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Effort-vs-result slopes ---
def f15vc_f15_volume_price_confirmation_effres_jerk_v071_signal(closeadj, volume):
    base = _z(volume, 63) - _z(closeadj.pct_change().abs(), 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_effres_jerk_v072_signal(closeadj, volume):
    base = _z(volume, 126) - _z(closeadj.pct_change().abs(), 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume-confirmed momentum slopes ---
def f15vc_f15_volume_price_confirmation_volmom_jerk_v073_signal(close, closeadj, volume):
    ret = closeadj / closeadj.shift(63) - 1.0
    base = np.tanh(3.0 * ret) * _f15_updownvol(close, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_dvmom_jerk_v074_signal(closeadj, volume):
    ret = closeadj / closeadj.shift(63) - 1.0
    dv = closeadj * volume
    dvrel = dv.rolling(21, min_periods=10).mean() / dv.rolling(126, min_periods=63).mean().replace(0, np.nan)
    base = np.tanh(3.0 * ret) * dvrel
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- CMF-trend interaction slopes ---
def f15vc_f15_volume_price_confirmation_cmftrend_jerk_v075_signal(close, high, low, closeadj, volume):
    base = _f15_cmf(close, high, low, volume, 63) * np.sign(closeadj - closeadj.shift(63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmftrend_jerk_v076_signal(close, high, low, closeadj, volume):
    base = _f15_cmf(close, high, low, volume, 63) * np.sign(closeadj - closeadj.shift(63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- OBV-price divergence slopes ---
def f15vc_f15_volume_price_confirmation_obvdiv_jerk_v077_signal(close, closeadj, volume):
    obv_sl = _z(_f15_obv(close, volume).diff(63) / 63.0, 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    base = px_sl - obv_sl
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_addiv_jerk_v078_signal(close, high, low, closeadj, volume):
    ad_sl = _z(_f15_adline(close, high, low, volume).diff(63) / 63.0, 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    base = ad_sl - px_sl
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Money-flow composite slopes ---
def f15vc_f15_volume_price_confirmation_mfcomp_jerk_v079_signal(close, high, low, volume):
    cmf = _z(_f15_cmf(close, high, low, volume, 21), 126)
    mfi = _z(_f15_mfi(close, high, low, volume, 21) - 50.0, 126)
    base = (cmf + mfi) / 2.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfcomp_jerk_v080_signal(close, high, low, volume):
    cmf = _z(_f15_cmf(close, high, low, volume, 21), 126)
    mfi = _z(_f15_mfi(close, high, low, volume, 21) - 50.0, 126)
    base = (cmf + mfi) / 2.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- A/D-OBV spread slopes ---
def f15vc_f15_volume_price_confirmation_adobvspr_jerk_v081_signal(close, high, low, volume):
    base = _f15_adz(close, high, low, volume, 126) - _f15_obvz(close, volume, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_adobvspr_jerk_v082_signal(close, high, low, volume):
    base = _f15_adz(close, high, low, volume, 126) - _f15_obvz(close, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- CLV-skew slopes (volume-weighted minus unweighted intrabar bias) ---
def f15vc_f15_volume_price_confirmation_clvskew_jerk_v083_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    base = _f15_vwclv(close, high, low, volume, 63) - clv.rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_clvskew_jerk_v084_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    base = _f15_vwclv(close, high, low, volume, 63) - clv.rolling(63, min_periods=21).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Force-index dispersion slopes ---
def f15vc_f15_volume_price_confirmation_forcedisp_jerk_v085_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 13)
    base = _std(fi, 63) / fi.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmfdisp_jerk_v086_signal(close, high, low, volume):
    base = _std(_f15_cmf(close, high, low, volume, 21), 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- MFI band slopes ---
def f15vc_f15_volume_price_confirmation_mfiband_jerk_v087_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 14)
    base = ((mfi - 80).clip(lower=0) - (20 - mfi).clip(lower=0)).rolling(21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfiabove50_jerk_v088_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 21)
    base = (mfi > 50).astype(float).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Up-volume thrust slopes ---
def f15vc_f15_volume_price_confirmation_upvolz_jerk_v089_signal(close, volume):
    upvol = volume.where(close.diff() > 0, np.nan)
    base = _z(upvol.rolling(21, min_periods=8).mean(), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_volthrust_jerk_v090_signal(closeadj, volume):
    base = (np.sign(closeadj.diff()) * _z(volume, 63)).rolling(21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Distribution / accumulation count slopes ---
def f15vc_f15_volume_price_confirmation_addaycount_jerk_v091_signal(close, high, low, volume):
    mfv = _f15_clv(close, high, low) * volume
    base = ((mfv > 0).astype(float) - (mfv < 0).astype(float)).rolling(126, min_periods=63).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_updaycount_jerk_v092_signal(close, volume):
    up = (close.diff() > 0).astype(float)
    dn = (close.diff() < 0).astype(float)
    base = (up - dn).rolling(126, min_periods=63).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- VWAP-gap (21d) plain slopes at longer windows ---
def f15vc_f15_volume_price_confirmation_vwapgap_126d_jerk_v093_signal(closeadj, volume):
    base = _f15_vwapgap(closeadj, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmf_252d_jerk_v094_signal(close, high, low, volume):
    base = _f15_cmf(close, high, low, volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume elasticity slopes ---
def f15vc_f15_volume_price_confirmation_volelast_jerk_v095_signal(closeadj, volume):
    absret = closeadj.pct_change().abs()
    volz = _z(volume, 63)
    cov = (absret * volz).rolling(63, min_periods=21).mean() - absret.rolling(63, min_periods=21).mean() * volz.rolling(63, min_periods=21).mean()
    base = cov / volz.rolling(63, min_periods=21).var().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_vrcorr_jerk_v096_signal(closeadj, volume):
    base = closeadj.pct_change().rolling(63, min_periods=21).corr(np.log(volume.replace(0, np.nan)))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- MFI detrended slopes ---
def f15vc_f15_volume_price_confirmation_mfistreak_jerk_v097_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 21)
    side = np.sign(mfi - 50.0).fillna(0.0)
    grp = (side != side.shift()).cumsum()
    age = side.groupby(grp).cumcount() + 1
    base = (side * age) / 63.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfidetr_jerk_v098_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 63)
    base = mfi - mfi.rolling(126, min_periods=63).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Chaikin oscillator (raw) slopes ---
def f15vc_f15_volume_price_confirmation_forceosc_jerk_v099_signal(closeadj, volume):
    raw = closeadj.diff() * volume
    scale = raw.abs().ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    base = (raw.ewm(span=13, min_periods=7).mean() - raw.ewm(span=63, min_periods=21).mean()) / scale
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forceosc_jerk_v100_signal(closeadj, volume):
    raw = closeadj.diff() * volume
    scale = raw.abs().ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    base = (raw.ewm(span=13, min_periods=7).mean() - raw.ewm(span=63, min_periods=21).mean()) / scale
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- OBV range-position slopes (where OBV sits in its own range) ---
def f15vc_f15_volume_price_confirmation_obvrng63_jerk_v101_signal(close, volume):
    obv = _f15_obv(close, volume)
    hi = obv.rolling(63, min_periods=21).max()
    lo = obv.rolling(63, min_periods=21).min()
    base = (obv - lo) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_adrng126_jerk_v102_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    hi = ad.rolling(126, min_periods=63).max()
    lo = ad.rolling(126, min_periods=63).min()
    base = (ad - lo) / (hi - lo).replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Money-flow-volume z slopes ---
def f15vc_f15_volume_price_confirmation_mfvz_jerk_v103_signal(close, high, low, volume):
    mfv = _f15_clv(close, high, low) * volume
    base = _z(mfv.rolling(21, min_periods=10).mean(), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfvnoise_jerk_v104_signal(close, high, low, volume):
    mfv = _f15_clv(close, high, low) * volume
    base = mfv.rolling(63, min_periods=21).std() / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- A/D acceleration-as-level slopes ---
def f15vc_f15_volume_price_confirmation_adaccel_jerk_v105_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    scale = ad.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    base = ((ad - ad.shift(63)) - (ad - ad.shift(126)) * 0.5) / scale
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_pvtmom_jerk_v106_signal(closeadj, volume):
    pvt = _f15_pvt(closeadj, volume)
    scale = pvt.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = ((pvt - pvt.shift(21)) / 21.0 - (pvt - pvt.shift(63)) / 63.0) / scale
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- VWAP-gap above-VWAP persistence slopes (fraction of time price > VWAP) ---
def f15vc_f15_volume_price_confirmation_abovevwap_jerk_v107_signal(closeadj, volume):
    gap = _f15_vwapgap(closeadj, volume, 21)
    base = (gap > 0).astype(float).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_eom_5d_jerk_v108_signal(closeadj, high, low, volume):
    base = _z(_f15_eom(closeadj, high, low, volume, 5), 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- CMF regime slopes ---
def f15vc_f15_volume_price_confirmation_cmfregime_jerk_v109_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    base = ((cmf > 0.05).astype(float) - (cmf < -0.05).astype(float)).rolling(252, min_periods=63).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfiextr_jerk_v110_signal(close, high, low, volume):
    mfi = _f15_mfi(close, high, low, volume, 14)
    base = ((mfi > 80).astype(float) - (mfi < 20).astype(float)).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Force ratio slopes ---
def f15vc_f15_volume_price_confirmation_forceratio_jerk_v111_signal(closeadj, volume):
    scale = (closeadj.diff().abs() * volume).ewm(span=126, min_periods=63).mean().replace(0, np.nan)
    base = (_f15_force(closeadj, volume, 63) - _f15_force(closeadj, volume, 126)) / scale
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_forcechop_jerk_v112_signal(closeadj, volume):
    fi = _f15_force(closeadj, volume, 13)
    chop = fi.diff().abs() / fi.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    base = chop.rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Up-down volume magnitude asymmetry slopes ---
def f15vc_f15_volume_price_confirmation_volasym_jerk_v113_signal(close, volume):
    up = volume.where(close.diff() > 0, np.nan)
    dn = volume.where(close.diff() < 0, np.nan)
    base = np.log(up.rolling(63, min_periods=15).mean() / dn.rolling(63, min_periods=15).mean().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_volasym_jerk_v114_signal(close, volume):
    up = volume.where(close.diff() > 0, np.nan)
    dn = volume.where(close.diff() < 0, np.nan)
    base = np.log(up.rolling(126, min_periods=30).mean() / dn.rolling(126, min_periods=30).mean().replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Silent-distribution slopes (down-volume share active only while 63d trend up) ---
def f15vc_f15_volume_price_confirmation_silentdist_jerk_v115_signal(close, closeadj, volume):
    dn = volume.where(close.diff() < 0, 0.0).rolling(21, min_periods=10).sum()
    tot = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    trend_up = (closeadj.diff(63) > 0).astype(float)
    base = (dn / tot - 0.5) * trend_up
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cleanconf_jerk_v116_signal(close, closeadj, volume):
    obv_up = (_f15_obv(close, volume).diff(21) > 0)
    px_up = (closeadj.diff(21) > 0)
    base = (obv_up & px_up).astype(float).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- PVI-NVI divergence slopes ---
def f15vc_f15_volume_price_confirmation_pvinvi_jerk_v117_signal(close, volume):
    ret = close.pct_change()
    pvi = (1.0 + ret.where(volume.diff() > 0, 0.0).fillna(0.0)).cumprod()
    nvi = (1.0 + ret.where(volume.diff() < 0, 0.0).fillna(0.0)).cumprod()
    base = _z(pvi, 126) - _z(nvi, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_pvinvi_jerk_v118_signal(close, volume):
    ret = close.pct_change()
    pvi = (1.0 + ret.where(volume.diff() > 0, 0.0).fillna(0.0)).cumprod()
    nvi = (1.0 + ret.where(volume.diff() < 0, 0.0).fillna(0.0)).cumprod()
    base = _z(pvi, 126) - _z(nvi, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Greed / panic concentration slopes ---
def f15vc_f15_volume_price_confirmation_greedconc_jerk_v119_signal(closeadj, volume):
    ret = closeadj.pct_change()
    big_up = (ret > ret.rolling(63, min_periods=21).quantile(0.8))
    base = _z(volume, 63).where(big_up, np.nan).rolling(63, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_panicconc_jerk_v120_signal(closeadj, volume):
    ret = closeadj.pct_change()
    big_dn = (ret < ret.rolling(63, min_periods=21).quantile(0.2))
    base = _z(volume, 63).where(big_dn, np.nan).rolling(63, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Dual-confirmation slopes ---
def f15vc_f15_volume_price_confirmation_dualconf_jerk_v121_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    mfi = _f15_mfi(close, high, low, volume, 21) - 50.0
    base = ((np.sign(cmf) == np.sign(mfi)).astype(float) * np.sign(cmf)).rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mficmfspr_jerk_v122_signal(close, high, low, volume):
    base = _z(_f15_mfi(close, high, low, volume, 21) - 50.0, 126) - _z(_f15_cmf(close, high, low, volume, 21), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- OBV drawdown slopes ---
def f15vc_f15_volume_price_confirmation_obvdd_jerk_v123_signal(close, volume):
    obv = _f15_obv(close, volume)
    peak = obv.rolling(126, min_periods=63).max()
    base = (obv - peak) / obv.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_addd_jerk_v124_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    peak = ad.rolling(126, min_periods=63).max()
    base = (ad - peak) / ad.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume-CLV concentration slopes ---
def f15vc_f15_volume_price_confirmation_volclvconc_jerk_v125_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    topv = volume.where(clv > 0.5, 0.0).rolling(63, min_periods=21).sum()
    botv = volume.where(clv < -0.5, 0.0).rolling(63, min_periods=21).sum()
    base = (topv - botv) / (topv + botv).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_clvbreadth_jerk_v126_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    s = (clv > 0.3334).astype(float)
    w = (clv < -0.3334).astype(float)
    vs = (s * volume).rolling(63, min_periods=21).sum()
    vw = (w * volume).rolling(63, min_periods=21).sum()
    base = (vs - vw) / (vs + vw).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- CMF-surge interaction slopes ---
def f15vc_f15_volume_price_confirmation_cmfsurge_jerk_v127_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    base = (cmf * _z(volume, 63).clip(lower=0)).rolling(21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmfbreak_jerk_v128_signal(close, high, low, closeadj, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    hi_prior = closeadj.shift(1).rolling(63, min_periods=21).max()
    gate = (closeadj > hi_prior).astype(float).rolling(21, min_periods=10).mean()
    base = cmf * gate
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Churn slopes ---
def f15vc_f15_volume_price_confirmation_churn_jerk_v129_signal(closeadj, volume):
    voltr = _z(volume.cumsum().diff(63) / 63.0, 126)
    pxtr = _z(closeadj.diff(63).abs() / closeadj.rolling(63, min_periods=21).mean().replace(0, np.nan), 126)
    base = voltr - pxtr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_vprankcorr_jerk_v130_signal(closeadj, volume):
    retr = closeadj.pct_change().rolling(63, min_periods=21).rank(pct=True)
    volr = volume.rolling(63, min_periods=21).rank(pct=True)
    base = retr.rolling(63, min_periods=21).corr(volr)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Conviction accumulation slopes ---
def f15vc_f15_volume_price_confirmation_convaccum_jerk_v131_signal(close, closeadj, volume):
    w = closeadj.pct_change().abs() * volume
    up = w.where(close.diff() > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = w.where(close.diff() < 0, 0.0).rolling(21, min_periods=10).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_convaccum_jerk_v132_signal(close, closeadj, volume):
    w = closeadj.pct_change().abs() * volume
    up = w.where(close.diff() > 0, 0.0).rolling(63, min_periods=21).sum()
    dn = w.where(close.diff() < 0, 0.0).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- OBV-AD spread slopes (short) ---
def f15vc_f15_volume_price_confirmation_obvadspr63_jerk_v133_signal(close, high, low, volume):
    obv_sl = _z(_f15_obv(close, volume).diff(63) / 63.0, 126)
    ad_sl = _z(_f15_adline(close, high, low, volume).diff(63) / 63.0, 126)
    base = obv_sl - ad_sl
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvpvtspr_jerk_v134_signal(close, closeadj, volume):
    obv_sl = _z(_f15_obv(close, volume).diff(63) / 63.0, 126)
    pvt_sl = _z(_f15_pvt(closeadj, volume).diff(63) / 63.0, 126)
    base = obv_sl - pvt_sl
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- MFI divergence slopes ---
def f15vc_f15_volume_price_confirmation_mfidiv_jerk_v135_signal(close, high, low, closeadj, volume):
    mfi = _f15_mfi(close, high, low, volume, 21)
    base = _z(closeadj - closeadj.shift(63), 126) - _z(mfi - mfi.shift(63), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_pvtdiv_jerk_v136_signal(closeadj, volume):
    pvt_sl = _z(_f15_pvt(closeadj, volume).diff(63) / 63.0, 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    base = pvt_sl - px_sl
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- CMF stability slopes ---
def f15vc_f15_volume_price_confirmation_cmfstable_jerk_v137_signal(close, high, low, volume):
    cmf = _f15_cmf(close, high, low, volume, 21)
    base = cmf.rolling(63, min_periods=21).mean() / cmf.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvstab_jerk_v138_signal(close, volume):
    obv = _f15_obv(close, volume)
    sl = obv.diff(21)
    scale = obv.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    base = (sl.rolling(126, min_periods=63).mean() / scale) / (sl / scale).rolling(126, min_periods=63).std().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Distribution-day slopes ---
def f15vc_f15_volume_price_confirmation_distrib_jerk_v139_signal(close, high, low, volume):
    weak = ((close.diff() < 0) & (_f15_clv(close, high, low) < 0))
    base = volume.where(weak, 0.0).rolling(126, min_periods=63).sum() / volume.rolling(126, min_periods=63).sum().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_mfconc_jerk_v140_signal(close, high, low, volume):
    clv = _f15_clv(close, high, low)
    volrank = volume.rolling(126, min_periods=63).rank(pct=True)
    num = (clv * volume).where(volrank > 0.75, 0.0).rolling(126, min_periods=63).sum()
    den = volume.where(volrank > 0.75, 0.0).rolling(126, min_periods=63).sum().replace(0, np.nan)
    base = num / den
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Cumulative force divergence slopes ---
def f15vc_f15_volume_price_confirmation_forcediv_jerk_v141_signal(closeadj, volume):
    f_sl = _z(_f15_cumforce(closeadj, volume).diff(63) / 63.0, 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    base = f_sl - px_sl
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_nvidiv_jerk_v142_signal(close, closeadj, volume):
    ret = close.pct_change()
    nvi = (1.0 + ret.where(volume.diff() < 0, 0.0).fillna(0.0)).cumprod()
    nvi_sl = _z((nvi - nvi.shift(63)) / 63.0, 126)
    px_sl = _z((closeadj - closeadj.shift(63)) / 63.0, 126)
    base = nvi_sl - px_sl
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- A/D slow-momentum slopes ---
def f15vc_f15_volume_price_confirmation_admomslow_jerk_v143_signal(close, high, low, volume):
    ad = _f15_adline(close, high, low, volume)
    scale = ad.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    base = ((ad - ad.shift(126)) - (ad - ad.shift(252)) * 0.5) / scale
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_cmfrankmom_jerk_v144_signal(close, high, low, volume):
    rk = _rank(_f15_cmf(close, high, low, volume, 21), 252)
    base = rk - rk.shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Volume-confirmed drawdown slopes ---
def f15vc_f15_volume_price_confirmation_voldd_jerk_v145_signal(close, closeadj, volume):
    peak = closeadj.rolling(63, min_periods=21).max()
    dd = closeadj / peak.replace(0, np.nan) - 1.0
    dn_share = _f15_updownvol(close, volume, 21).clip(upper=0).abs()
    base = dd * (1.0 + dn_share)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_flowcomp_jerk_v146_signal(close, high, low, closeadj, volume):
    obv = _z(_f15_obv(close, volume).diff(63) / 63.0, 126)
    ad = _z(_f15_adline(close, high, low, volume).diff(63) / 63.0, 126)
    pvt = _z(_f15_pvt(closeadj, volume).diff(63) / 63.0, 126)
    base = (obv + ad + pvt) / 3.0 * np.sign(closeadj.diff(63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Thrust dispersion slopes ---
def f15vc_f15_volume_price_confirmation_thrustdisp_jerk_v147_signal(close, volume):
    thrust = np.sign(close.diff()) * _z(volume, 63)
    base = thrust.rolling(63, min_periods=21).std()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_obvmomz_jerk_v148_signal(close, volume):
    base = _z(_f15_obv(close, volume).diff(21), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# --- Long-horizon money-flow trend slopes ---
def f15vc_f15_volume_price_confirmation_cmftrend126_jerk_v149_signal(close, high, low, closeadj, volume):
    base = _f15_cmf(close, high, low, volume, 126) * np.sign(closeadj - closeadj.shift(126))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15vc_f15_volume_price_confirmation_adobvlevel_jerk_v150_signal(close, high, low, volume):
    base = _f15_adz(close, high, low, volume, 126) - _f15_obvz(close, volume, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15vc_f15_volume_price_confirmation_obvz_63d_jerk_v001_signal,
    f15vc_f15_volume_price_confirmation_obvz_63d_jerk_v002_signal,
    f15vc_f15_volume_price_confirmation_obvz_126d_jerk_v003_signal,
    f15vc_f15_volume_price_confirmation_obvz_126d_jerk_v004_signal,
    f15vc_f15_volume_price_confirmation_obvz_252d_jerk_v005_signal,
    f15vc_f15_volume_price_confirmation_obvz_252d_jerk_v006_signal,
    f15vc_f15_volume_price_confirmation_adz_63d_jerk_v007_signal,
    f15vc_f15_volume_price_confirmation_adz_126d_jerk_v008_signal,
    f15vc_f15_volume_price_confirmation_adz_126d_jerk_v009_signal,
    f15vc_f15_volume_price_confirmation_adz_252d_jerk_v010_signal,
    f15vc_f15_volume_price_confirmation_adz_252d_jerk_v011_signal,
    f15vc_f15_volume_price_confirmation_cmf_21d_jerk_v012_signal,
    f15vc_f15_volume_price_confirmation_cmf_21d_jerk_v013_signal,
    f15vc_f15_volume_price_confirmation_cmf_63d_jerk_v014_signal,
    f15vc_f15_volume_price_confirmation_cmf_63d_jerk_v015_signal,
    f15vc_f15_volume_price_confirmation_cmf_126d_jerk_v016_signal,
    f15vc_f15_volume_price_confirmation_cmf_126d_jerk_v017_signal,
    f15vc_f15_volume_price_confirmation_mfi_14d_jerk_v018_signal,
    f15vc_f15_volume_price_confirmation_mfi_21d_jerk_v019_signal,
    f15vc_f15_volume_price_confirmation_mfi_21d_jerk_v020_signal,
    f15vc_f15_volume_price_confirmation_mfi_63d_jerk_v021_signal,
    f15vc_f15_volume_price_confirmation_mfi_63d_jerk_v022_signal,
    f15vc_f15_volume_price_confirmation_forcesign_jerk_v023_signal,
    f15vc_f15_volume_price_confirmation_forcez_21d_jerk_v024_signal,
    f15vc_f15_volume_price_confirmation_forcez_21d_jerk_v025_signal,
    f15vc_f15_volume_price_confirmation_forcez_63d_jerk_v026_signal,
    f15vc_f15_volume_price_confirmation_forcez_63d_jerk_v027_signal,
    f15vc_f15_volume_price_confirmation_udvol_21d_jerk_v028_signal,
    f15vc_f15_volume_price_confirmation_udvol_63d_jerk_v029_signal,
    f15vc_f15_volume_price_confirmation_udvol_63d_jerk_v030_signal,
    f15vc_f15_volume_price_confirmation_udvol_126d_jerk_v031_signal,
    f15vc_f15_volume_price_confirmation_pvtz_63d_jerk_v032_signal,
    f15vc_f15_volume_price_confirmation_pvtz_126d_jerk_v033_signal,
    f15vc_f15_volume_price_confirmation_pvtz_126d_jerk_v034_signal,
    f15vc_f15_volume_price_confirmation_sdvdiv_63d_jerk_v035_signal,
    f15vc_f15_volume_price_confirmation_sdvdiv_126d_jerk_v036_signal,
    f15vc_f15_volume_price_confirmation_eom_21d_jerk_v037_signal,
    f15vc_f15_volume_price_confirmation_eom_63d_jerk_v038_signal,
    f15vc_f15_volume_price_confirmation_clv_21d_jerk_v039_signal,
    f15vc_f15_volume_price_confirmation_distday_jerk_v040_signal,
    f15vc_f15_volume_price_confirmation_accday_jerk_v041_signal,
    f15vc_f15_volume_price_confirmation_vwapgap_21d_jerk_v042_signal,
    f15vc_f15_volume_price_confirmation_vwapgap_63d_jerk_v043_signal,
    f15vc_f15_volume_price_confirmation_vwapgap_63d_jerk_v044_signal,
    f15vc_f15_volume_price_confirmation_cmfrank_63d_jerk_v045_signal,
    f15vc_f15_volume_price_confirmation_cmfrank_21d_jerk_v046_signal,
    f15vc_f15_volume_price_confirmation_forcerank_21d_jerk_v047_signal,
    f15vc_f15_volume_price_confirmation_forcerank_63d_jerk_v048_signal,
    f15vc_f15_volume_price_confirmation_mfihot_jerk_v049_signal,
    f15vc_f15_volume_price_confirmation_mfirank_63d_jerk_v050_signal,
    f15vc_f15_volume_price_confirmation_forcetermspr_jerk_v051_signal,
    f15vc_f15_volume_price_confirmation_forcetermspr_jerk_v052_signal,
    f15vc_f15_volume_price_confirmation_chaikinosc_jerk_v053_signal,
    f15vc_f15_volume_price_confirmation_chaikinosc_jerk_v054_signal,
    f15vc_f15_volume_price_confirmation_obvosc_jerk_v055_signal,
    f15vc_f15_volume_price_confirmation_obvosc_jerk_v056_signal,
    f15vc_f15_volume_price_confirmation_vwapgapz_63d_jerk_v057_signal,
    f15vc_f15_volume_price_confirmation_vwapgapz_63d_jerk_v058_signal,
    f15vc_f15_volume_price_confirmation_vpcorr_63d_jerk_v059_signal,
    f15vc_f15_volume_price_confirmation_vpcorr_126d_jerk_v060_signal,
    f15vc_f15_volume_price_confirmation_adrngpos_jerk_v061_signal,
    f15vc_f15_volume_price_confirmation_obvrngpos_jerk_v062_signal,
    f15vc_f15_volume_price_confirmation_nvitrend_jerk_v063_signal,
    f15vc_f15_volume_price_confirmation_pvitrend_jerk_v064_signal,
    f15vc_f15_volume_price_confirmation_cmfspr_jerk_v065_signal,
    f15vc_f15_volume_price_confirmation_mfivolasym_jerk_v066_signal,
    f15vc_f15_volume_price_confirmation_vwret_21d_jerk_v067_signal,
    f15vc_f15_volume_price_confirmation_retvolasym_jerk_v068_signal,
    f15vc_f15_volume_price_confirmation_cmfpersist_jerk_v069_signal,
    f15vc_f15_volume_price_confirmation_forcepersist_jerk_v070_signal,
    f15vc_f15_volume_price_confirmation_effres_jerk_v071_signal,
    f15vc_f15_volume_price_confirmation_effres_jerk_v072_signal,
    f15vc_f15_volume_price_confirmation_volmom_jerk_v073_signal,
    f15vc_f15_volume_price_confirmation_dvmom_jerk_v074_signal,
    f15vc_f15_volume_price_confirmation_cmftrend_jerk_v075_signal,
    f15vc_f15_volume_price_confirmation_cmftrend_jerk_v076_signal,
    f15vc_f15_volume_price_confirmation_obvdiv_jerk_v077_signal,
    f15vc_f15_volume_price_confirmation_addiv_jerk_v078_signal,
    f15vc_f15_volume_price_confirmation_mfcomp_jerk_v079_signal,
    f15vc_f15_volume_price_confirmation_mfcomp_jerk_v080_signal,
    f15vc_f15_volume_price_confirmation_adobvspr_jerk_v081_signal,
    f15vc_f15_volume_price_confirmation_adobvspr_jerk_v082_signal,
    f15vc_f15_volume_price_confirmation_clvskew_jerk_v083_signal,
    f15vc_f15_volume_price_confirmation_clvskew_jerk_v084_signal,
    f15vc_f15_volume_price_confirmation_forcedisp_jerk_v085_signal,
    f15vc_f15_volume_price_confirmation_cmfdisp_jerk_v086_signal,
    f15vc_f15_volume_price_confirmation_mfiband_jerk_v087_signal,
    f15vc_f15_volume_price_confirmation_mfiabove50_jerk_v088_signal,
    f15vc_f15_volume_price_confirmation_upvolz_jerk_v089_signal,
    f15vc_f15_volume_price_confirmation_volthrust_jerk_v090_signal,
    f15vc_f15_volume_price_confirmation_addaycount_jerk_v091_signal,
    f15vc_f15_volume_price_confirmation_updaycount_jerk_v092_signal,
    f15vc_f15_volume_price_confirmation_vwapgap_126d_jerk_v093_signal,
    f15vc_f15_volume_price_confirmation_cmf_252d_jerk_v094_signal,
    f15vc_f15_volume_price_confirmation_volelast_jerk_v095_signal,
    f15vc_f15_volume_price_confirmation_vrcorr_jerk_v096_signal,
    f15vc_f15_volume_price_confirmation_mfistreak_jerk_v097_signal,
    f15vc_f15_volume_price_confirmation_mfidetr_jerk_v098_signal,
    f15vc_f15_volume_price_confirmation_forceosc_jerk_v099_signal,
    f15vc_f15_volume_price_confirmation_forceosc_jerk_v100_signal,
    f15vc_f15_volume_price_confirmation_obvrng63_jerk_v101_signal,
    f15vc_f15_volume_price_confirmation_adrng126_jerk_v102_signal,
    f15vc_f15_volume_price_confirmation_mfvz_jerk_v103_signal,
    f15vc_f15_volume_price_confirmation_mfvnoise_jerk_v104_signal,
    f15vc_f15_volume_price_confirmation_adaccel_jerk_v105_signal,
    f15vc_f15_volume_price_confirmation_pvtmom_jerk_v106_signal,
    f15vc_f15_volume_price_confirmation_abovevwap_jerk_v107_signal,
    f15vc_f15_volume_price_confirmation_eom_5d_jerk_v108_signal,
    f15vc_f15_volume_price_confirmation_cmfregime_jerk_v109_signal,
    f15vc_f15_volume_price_confirmation_mfiextr_jerk_v110_signal,
    f15vc_f15_volume_price_confirmation_forceratio_jerk_v111_signal,
    f15vc_f15_volume_price_confirmation_forcechop_jerk_v112_signal,
    f15vc_f15_volume_price_confirmation_volasym_jerk_v113_signal,
    f15vc_f15_volume_price_confirmation_volasym_jerk_v114_signal,
    f15vc_f15_volume_price_confirmation_silentdist_jerk_v115_signal,
    f15vc_f15_volume_price_confirmation_cleanconf_jerk_v116_signal,
    f15vc_f15_volume_price_confirmation_pvinvi_jerk_v117_signal,
    f15vc_f15_volume_price_confirmation_pvinvi_jerk_v118_signal,
    f15vc_f15_volume_price_confirmation_greedconc_jerk_v119_signal,
    f15vc_f15_volume_price_confirmation_panicconc_jerk_v120_signal,
    f15vc_f15_volume_price_confirmation_dualconf_jerk_v121_signal,
    f15vc_f15_volume_price_confirmation_mficmfspr_jerk_v122_signal,
    f15vc_f15_volume_price_confirmation_obvdd_jerk_v123_signal,
    f15vc_f15_volume_price_confirmation_addd_jerk_v124_signal,
    f15vc_f15_volume_price_confirmation_volclvconc_jerk_v125_signal,
    f15vc_f15_volume_price_confirmation_clvbreadth_jerk_v126_signal,
    f15vc_f15_volume_price_confirmation_cmfsurge_jerk_v127_signal,
    f15vc_f15_volume_price_confirmation_cmfbreak_jerk_v128_signal,
    f15vc_f15_volume_price_confirmation_churn_jerk_v129_signal,
    f15vc_f15_volume_price_confirmation_vprankcorr_jerk_v130_signal,
    f15vc_f15_volume_price_confirmation_convaccum_jerk_v131_signal,
    f15vc_f15_volume_price_confirmation_convaccum_jerk_v132_signal,
    f15vc_f15_volume_price_confirmation_obvadspr63_jerk_v133_signal,
    f15vc_f15_volume_price_confirmation_obvpvtspr_jerk_v134_signal,
    f15vc_f15_volume_price_confirmation_mfidiv_jerk_v135_signal,
    f15vc_f15_volume_price_confirmation_pvtdiv_jerk_v136_signal,
    f15vc_f15_volume_price_confirmation_cmfstable_jerk_v137_signal,
    f15vc_f15_volume_price_confirmation_obvstab_jerk_v138_signal,
    f15vc_f15_volume_price_confirmation_distrib_jerk_v139_signal,
    f15vc_f15_volume_price_confirmation_mfconc_jerk_v140_signal,
    f15vc_f15_volume_price_confirmation_forcediv_jerk_v141_signal,
    f15vc_f15_volume_price_confirmation_nvidiv_jerk_v142_signal,
    f15vc_f15_volume_price_confirmation_admomslow_jerk_v143_signal,
    f15vc_f15_volume_price_confirmation_cmfrankmom_jerk_v144_signal,
    f15vc_f15_volume_price_confirmation_voldd_jerk_v145_signal,
    f15vc_f15_volume_price_confirmation_flowcomp_jerk_v146_signal,
    f15vc_f15_volume_price_confirmation_thrustdisp_jerk_v147_signal,
    f15vc_f15_volume_price_confirmation_obvmomz_jerk_v148_signal,
    f15vc_f15_volume_price_confirmation_cmftrend126_jerk_v149_signal,
    f15vc_f15_volume_price_confirmation_adobvlevel_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VOLUME_PRICE_CONFIRMATION_REGISTRY_3RD_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
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

    print("OK f15_volume_price_confirmation_3rd_derivatives_001_150_claude: %d features pass" % n_features)
