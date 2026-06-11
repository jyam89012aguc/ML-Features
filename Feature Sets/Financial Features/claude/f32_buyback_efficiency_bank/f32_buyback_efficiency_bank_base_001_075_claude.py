import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5

def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _qrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====

def _f32_share_change(sharesbas, w):
    return sharesbas.pct_change(periods=w)


def _f32_buyback_intensity(sharesbas, closeadj, w):
    ch = sharesbas.pct_change(periods=w)
    return (-ch) * closeadj


def _f32_buyback_timing(sharesbas, closeadj, pb, w):
    ch = sharesbas.pct_change(periods=w)
    return (-ch) * (1.0 / pb.replace(0, np.nan).abs()) * closeadj


# ===== features =====
def f32beb_f32_buyback_efficiency_bank_sharechange_5d_base_v001_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_10d_base_v002_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_21d_base_v003_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_42d_base_v004_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_63d_base_v005_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_126d_base_v006_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_189d_base_v007_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_252d_base_v008_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_378d_base_v009_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechange_504d_base_v010_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeabs_21d_base_v011_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeabs_63d_base_v012_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeabs_126d_base_v013_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeabs_252d_base_v014_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeabs_504d_base_v015_signal(sharesbas, closeadj):
    result = _f32_share_change(sharesbas, 504).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_5d_base_v016_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_10d_base_v017_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_21d_base_v018_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_42d_base_v019_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_63d_base_v020_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_126d_base_v021_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_189d_base_v022_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_252d_base_v023_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_378d_base_v024_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintens_504d_base_v025_signal(sharesbas, closeadj):
    result = _f32_buyback_intensity(sharesbas, closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_5d_base_v026_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_10d_base_v027_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_21d_base_v028_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_42d_base_v029_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_63d_base_v030_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_126d_base_v031_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_189d_base_v032_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_252d_base_v033_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_378d_base_v034_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtiming_504d_base_v035_signal(sharesbas, closeadj, pb):
    result = _f32_buyback_timing(sharesbas, closeadj, pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangemean_21d_base_v036_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 21)
    result = _mean(g, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangemean_63d_base_v037_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 63)
    result = _mean(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangemean_126d_base_v038_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 126)
    result = _mean(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangemean_252d_base_v039_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 252)
    result = _mean(g, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangemean_504d_base_v040_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 504)
    result = _mean(g, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangemean_42d_base_v041_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 42)
    result = _mean(g, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangestd_21d_base_v042_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 21)
    result = _std(g, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangestd_63d_base_v043_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 63)
    result = _std(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangestd_126d_base_v044_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 126)
    result = _std(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangestd_252d_base_v045_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 252)
    result = _std(g, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangestd_504d_base_v046_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 504)
    result = _std(g, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangestd_42d_base_v047_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 42)
    result = _std(g, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangez_63d_base_v048_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 63)
    result = _z(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangez_126d_base_v049_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 126)
    result = _z(g, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangez_252d_base_v050_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 252)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangez_504d_base_v051_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 504)
    result = _z(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangez_21d_base_v052_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 21)
    result = _z(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangez_42d_base_v053_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 42)
    result = _z(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensema_21d_base_v054_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 21)
    result = _ema(base, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensema_63d_base_v055_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 63)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensema_126d_base_v056_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 126)
    result = _ema(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensema_252d_base_v057_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 252)
    result = _ema(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensema_504d_base_v058_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 504)
    result = _ema(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingema_21d_base_v059_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 21)
    result = _ema(base, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingema_63d_base_v060_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 63)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingema_126d_base_v061_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 126)
    result = _ema(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingema_252d_base_v062_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 252)
    result = _ema(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingema_504d_base_v063_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 504)
    result = _ema(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexpb_21d_base_v064_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 21)
    result = g * pb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexpb_63d_base_v065_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 63)
    result = g * pb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexpb_126d_base_v066_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 126)
    result = g * pb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexpb_252d_base_v067_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 252)
    result = g * pb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexpb_504d_base_v068_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 504)
    result = g * pb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_shareswach_21d_base_v069_signal(sharesbas, shareswa, closeadj):
    g = _f32_share_change(sharesbas, 21)
    g2 = shareswa.pct_change(periods=21)
    result = (g + g2) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_shareswach_63d_base_v070_signal(sharesbas, shareswa, closeadj):
    g = _f32_share_change(sharesbas, 63)
    g2 = shareswa.pct_change(periods=63)
    result = (g + g2) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_shareswach_126d_base_v071_signal(sharesbas, shareswa, closeadj):
    g = _f32_share_change(sharesbas, 126)
    g2 = shareswa.pct_change(periods=126)
    result = (g + g2) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_shareswach_252d_base_v072_signal(sharesbas, shareswa, closeadj):
    g = _f32_share_change(sharesbas, 252)
    g2 = shareswa.pct_change(periods=252)
    result = (g + g2) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_shareswach_504d_base_v073_signal(sharesbas, shareswa, closeadj):
    g = _f32_share_change(sharesbas, 504)
    g2 = shareswa.pct_change(periods=504)
    result = (g + g2) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_shareswach_42d_base_v074_signal(sharesbas, shareswa, closeadj):
    g = _f32_share_change(sharesbas, 42)
    g2 = shareswa.pct_change(periods=42)
    result = (g + g2) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_shareswach_10d_base_v075_signal(sharesbas, shareswa, closeadj):
    g = _f32_share_change(sharesbas, 10)
    g2 = shareswa.pct_change(periods=10)
    result = (g + g2) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32beb_f32_buyback_efficiency_bank_sharechange_5d_base_v001_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_10d_base_v002_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_21d_base_v003_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_42d_base_v004_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_63d_base_v005_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_126d_base_v006_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_189d_base_v007_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_252d_base_v008_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_378d_base_v009_signal,
    f32beb_f32_buyback_efficiency_bank_sharechange_504d_base_v010_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeabs_21d_base_v011_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeabs_63d_base_v012_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeabs_126d_base_v013_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeabs_252d_base_v014_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeabs_504d_base_v015_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_5d_base_v016_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_10d_base_v017_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_21d_base_v018_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_42d_base_v019_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_63d_base_v020_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_126d_base_v021_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_189d_base_v022_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_252d_base_v023_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_378d_base_v024_signal,
    f32beb_f32_buyback_efficiency_bank_bbintens_504d_base_v025_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_5d_base_v026_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_10d_base_v027_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_21d_base_v028_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_42d_base_v029_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_63d_base_v030_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_126d_base_v031_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_189d_base_v032_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_252d_base_v033_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_378d_base_v034_signal,
    f32beb_f32_buyback_efficiency_bank_bbtiming_504d_base_v035_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangemean_21d_base_v036_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangemean_63d_base_v037_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangemean_126d_base_v038_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangemean_252d_base_v039_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangemean_504d_base_v040_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangemean_42d_base_v041_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangestd_21d_base_v042_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangestd_63d_base_v043_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangestd_126d_base_v044_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangestd_252d_base_v045_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangestd_504d_base_v046_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangestd_42d_base_v047_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangez_63d_base_v048_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangez_126d_base_v049_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangez_252d_base_v050_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangez_504d_base_v051_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangez_21d_base_v052_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangez_42d_base_v053_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensema_21d_base_v054_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensema_63d_base_v055_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensema_126d_base_v056_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensema_252d_base_v057_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensema_504d_base_v058_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingema_21d_base_v059_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingema_63d_base_v060_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingema_126d_base_v061_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingema_252d_base_v062_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingema_504d_base_v063_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexpb_21d_base_v064_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexpb_63d_base_v065_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexpb_126d_base_v066_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexpb_252d_base_v067_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexpb_504d_base_v068_signal,
    f32beb_f32_buyback_efficiency_bank_shareswach_21d_base_v069_signal,
    f32beb_f32_buyback_efficiency_bank_shareswach_63d_base_v070_signal,
    f32beb_f32_buyback_efficiency_bank_shareswach_126d_base_v071_signal,
    f32beb_f32_buyback_efficiency_bank_shareswach_252d_base_v072_signal,
    f32beb_f32_buyback_efficiency_bank_shareswach_504d_base_v073_signal,
    f32beb_f32_buyback_efficiency_bank_shareswach_42d_base_v074_signal,
    f32beb_f32_buyback_efficiency_bank_shareswach_10d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_BUYBACK_EFFICIENCY_BANK_REGISTRY_001_075 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f32_share_change", "_f32_buyback_intensity", "_f32_buyback_timing",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f32_buyback_efficiency_bank_base_001_075_claude: {n_features} features pass")
