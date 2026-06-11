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


def _f42_capex_to_ppe(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _f42_property_capex_burn(capex, revenue, w):
    r = capex / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f42_capex_quality(capex, depamor, w):
    r = capex / depamor.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_5d_base_v001_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_10d_base_v002_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_21d_base_v003_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_42d_base_v004_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_63d_base_v005_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_126d_base_v006_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_189d_base_v007_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_252d_base_v008_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_378d_base_v009_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_mean_504d_base_v010_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _mean(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_5d_base_v011_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_10d_base_v012_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_21d_base_v013_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_42d_base_v014_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_63d_base_v015_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_126d_base_v016_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_189d_base_v017_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_252d_base_v018_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_378d_base_v019_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_ema_504d_base_v020_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _ema(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_z_21d_base_v021_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_z_42d_base_v022_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _z(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_z_63d_base_v023_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_z_126d_base_v024_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _z(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_z_189d_base_v025_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _z(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_z_252d_base_v026_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _z(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_z_378d_base_v027_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _z(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2p_z_504d_base_v028_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _z(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_5d_base_v029_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_10d_base_v030_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_21d_base_v031_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_42d_base_v032_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_63d_base_v033_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_126d_base_v034_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_189d_base_v035_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_252d_base_v036_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_378d_base_v037_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burn_504d_base_v038_signal(capex, revenue, closeadj):
    result = _f42_property_capex_burn(capex, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_5d_base_v039_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 5)
    result = _ema(b, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_10d_base_v040_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 10)
    result = _ema(b, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_21d_base_v041_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 21)
    result = _ema(b, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_42d_base_v042_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 42)
    result = _ema(b, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_63d_base_v043_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 63)
    result = _ema(b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_126d_base_v044_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 126)
    result = _ema(b, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_189d_base_v045_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 189)
    result = _ema(b, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_252d_base_v046_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 252)
    result = _ema(b, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_378d_base_v047_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 378)
    result = _ema(b, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnema_504d_base_v048_signal(capex, revenue, closeadj):
    b = _f42_property_capex_burn(capex, revenue, 504)
    result = _ema(b, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnxvol_21d_base_v049_signal(capex, revenue, volume):
    b = _f42_property_capex_burn(capex, revenue, 21)
    result = b * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnxvol_63d_base_v050_signal(capex, revenue, volume):
    b = _f42_property_capex_burn(capex, revenue, 63)
    result = b * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_burnxvol_252d_base_v051_signal(capex, revenue, volume):
    b = _f42_property_capex_burn(capex, revenue, 252)
    result = b * volume
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_5d_base_v052_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_10d_base_v053_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_21d_base_v054_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_42d_base_v055_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_63d_base_v056_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_126d_base_v057_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_189d_base_v058_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_252d_base_v059_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_378d_base_v060_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qual_504d_base_v061_signal(capex, depamor, closeadj):
    result = _f42_capex_quality(capex, depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualz_21d_base_v062_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 21)
    result = _z(q, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualz_42d_base_v063_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 42)
    result = _z(q, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualz_63d_base_v064_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 63)
    result = _z(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualz_126d_base_v065_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 126)
    result = _z(q, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualz_189d_base_v066_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 189)
    result = _z(q, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualz_252d_base_v067_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 252)
    result = _z(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualz_378d_base_v068_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 378)
    result = _z(q, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_qualz_504d_base_v069_signal(capex, depamor, closeadj):
    q = _f42_capex_quality(capex, depamor, 504)
    result = _z(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pstd_21d_base_v070_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pstd_63d_base_v071_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _std(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pstd_126d_base_v072_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _std(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pstd_252d_base_v073_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _std(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pstd_504d_base_v074_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = _std(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f42rci_f42_resort_casino_capex_intensity_c2pdiff_21m63_base_v075_signal(capex, ppnenet, closeadj):
    r = _f42_capex_to_ppe(capex, ppnenet)
    result = (_mean(r, 21) - _mean(r, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_5d_base_v001_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_10d_base_v002_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_21d_base_v003_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_42d_base_v004_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_63d_base_v005_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_126d_base_v006_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_189d_base_v007_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_252d_base_v008_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_378d_base_v009_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_mean_504d_base_v010_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_5d_base_v011_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_10d_base_v012_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_21d_base_v013_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_42d_base_v014_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_63d_base_v015_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_126d_base_v016_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_189d_base_v017_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_252d_base_v018_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_378d_base_v019_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_ema_504d_base_v020_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_z_21d_base_v021_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_z_42d_base_v022_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_z_63d_base_v023_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_z_126d_base_v024_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_z_189d_base_v025_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_z_252d_base_v026_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_z_378d_base_v027_signal,
    f42rci_f42_resort_casino_capex_intensity_c2p_z_504d_base_v028_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_5d_base_v029_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_10d_base_v030_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_21d_base_v031_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_42d_base_v032_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_63d_base_v033_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_126d_base_v034_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_189d_base_v035_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_252d_base_v036_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_378d_base_v037_signal,
    f42rci_f42_resort_casino_capex_intensity_burn_504d_base_v038_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_5d_base_v039_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_10d_base_v040_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_21d_base_v041_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_42d_base_v042_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_63d_base_v043_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_126d_base_v044_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_189d_base_v045_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_252d_base_v046_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_378d_base_v047_signal,
    f42rci_f42_resort_casino_capex_intensity_burnema_504d_base_v048_signal,
    f42rci_f42_resort_casino_capex_intensity_burnxvol_21d_base_v049_signal,
    f42rci_f42_resort_casino_capex_intensity_burnxvol_63d_base_v050_signal,
    f42rci_f42_resort_casino_capex_intensity_burnxvol_252d_base_v051_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_5d_base_v052_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_10d_base_v053_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_21d_base_v054_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_42d_base_v055_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_63d_base_v056_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_126d_base_v057_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_189d_base_v058_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_252d_base_v059_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_378d_base_v060_signal,
    f42rci_f42_resort_casino_capex_intensity_qual_504d_base_v061_signal,
    f42rci_f42_resort_casino_capex_intensity_qualz_21d_base_v062_signal,
    f42rci_f42_resort_casino_capex_intensity_qualz_42d_base_v063_signal,
    f42rci_f42_resort_casino_capex_intensity_qualz_63d_base_v064_signal,
    f42rci_f42_resort_casino_capex_intensity_qualz_126d_base_v065_signal,
    f42rci_f42_resort_casino_capex_intensity_qualz_189d_base_v066_signal,
    f42rci_f42_resort_casino_capex_intensity_qualz_252d_base_v067_signal,
    f42rci_f42_resort_casino_capex_intensity_qualz_378d_base_v068_signal,
    f42rci_f42_resort_casino_capex_intensity_qualz_504d_base_v069_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pstd_21d_base_v070_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pstd_63d_base_v071_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pstd_126d_base_v072_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pstd_252d_base_v073_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pstd_504d_base_v074_signal,
    f42rci_f42_resort_casino_capex_intensity_c2pdiff_21m63_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_RESORT_CASINO_CAPEX_INTENSITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))).values, name="high")
    low = pd.Series((closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))).values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "capex": capex, "ppnenet": ppnenet, "revenue": revenue, "depamor": depamor }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f42_capex_to_ppe", "_f42_property_capex_burn", "_f42_capex_quality")
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
    print(f"OK resort_casino_capex_intensity_base_001_075_claude: {n_features} features pass")
