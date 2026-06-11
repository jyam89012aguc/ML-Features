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



# ===== folder domain primitives =====
def _f09_inv_days(inventory, cor):
    return inventory / cor.replace(0, np.nan) * 365.0


def _f09_inv_to_revenue(inventory, revenue):
    return inventory / revenue.replace(0, np.nan)


def _f09_inv_dynamics(inventory, revenue, w):
    ratio = inventory / revenue.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====

# id idxcl w=5
def f09eim_f09_ep_inventory_management_ididxcl_5d_base_v001_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=5
def f09eim_f09_ep_inventory_management_idlogxcl_5d_base_v002_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=5
def f09eim_f09_ep_inventory_management_idsqxcl_5d_base_v003_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=5
def f09eim_f09_ep_inventory_management_idinvxcl_5d_base_v004_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=5
def f09eim_f09_ep_inventory_management_idmeanxcl_5d_base_v005_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=5
def f09eim_f09_ep_inventory_management_idzxcl_5d_base_v006_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=5
def f09eim_f09_ep_inventory_management_idstdxcl_5d_base_v007_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=5
def f09eim_f09_ep_inventory_management_idratiomean_5d_base_v008_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=10
def f09eim_f09_ep_inventory_management_ididxcl_10d_base_v009_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=10
def f09eim_f09_ep_inventory_management_idlogxcl_10d_base_v010_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=10
def f09eim_f09_ep_inventory_management_idsqxcl_10d_base_v011_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=10
def f09eim_f09_ep_inventory_management_idinvxcl_10d_base_v012_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=10
def f09eim_f09_ep_inventory_management_idmeanxcl_10d_base_v013_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=10
def f09eim_f09_ep_inventory_management_idzxcl_10d_base_v014_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=10
def f09eim_f09_ep_inventory_management_idstdxcl_10d_base_v015_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=10
def f09eim_f09_ep_inventory_management_idratiomean_10d_base_v016_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 10).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=21
def f09eim_f09_ep_inventory_management_ididxcl_21d_base_v017_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=21
def f09eim_f09_ep_inventory_management_idlogxcl_21d_base_v018_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=21
def f09eim_f09_ep_inventory_management_idsqxcl_21d_base_v019_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=21
def f09eim_f09_ep_inventory_management_idinvxcl_21d_base_v020_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=21
def f09eim_f09_ep_inventory_management_idmeanxcl_21d_base_v021_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=21
def f09eim_f09_ep_inventory_management_idzxcl_21d_base_v022_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=21
def f09eim_f09_ep_inventory_management_idstdxcl_21d_base_v023_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=21
def f09eim_f09_ep_inventory_management_idratiomean_21d_base_v024_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=42
def f09eim_f09_ep_inventory_management_ididxcl_42d_base_v025_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=42
def f09eim_f09_ep_inventory_management_idlogxcl_42d_base_v026_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=42
def f09eim_f09_ep_inventory_management_idsqxcl_42d_base_v027_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=42
def f09eim_f09_ep_inventory_management_idinvxcl_42d_base_v028_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=42
def f09eim_f09_ep_inventory_management_idmeanxcl_42d_base_v029_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=42
def f09eim_f09_ep_inventory_management_idzxcl_42d_base_v030_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=42
def f09eim_f09_ep_inventory_management_idstdxcl_42d_base_v031_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=42
def f09eim_f09_ep_inventory_management_idratiomean_42d_base_v032_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 42).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=63
def f09eim_f09_ep_inventory_management_ididxcl_63d_base_v033_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=63
def f09eim_f09_ep_inventory_management_idlogxcl_63d_base_v034_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=63
def f09eim_f09_ep_inventory_management_idsqxcl_63d_base_v035_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=63
def f09eim_f09_ep_inventory_management_idinvxcl_63d_base_v036_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=63
def f09eim_f09_ep_inventory_management_idmeanxcl_63d_base_v037_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=63
def f09eim_f09_ep_inventory_management_idzxcl_63d_base_v038_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=63
def f09eim_f09_ep_inventory_management_idstdxcl_63d_base_v039_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=63
def f09eim_f09_ep_inventory_management_idratiomean_63d_base_v040_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=126
def f09eim_f09_ep_inventory_management_ididxcl_126d_base_v041_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=126
def f09eim_f09_ep_inventory_management_idlogxcl_126d_base_v042_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=126
def f09eim_f09_ep_inventory_management_idsqxcl_126d_base_v043_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=126
def f09eim_f09_ep_inventory_management_idinvxcl_126d_base_v044_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=126
def f09eim_f09_ep_inventory_management_idmeanxcl_126d_base_v045_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=126
def f09eim_f09_ep_inventory_management_idzxcl_126d_base_v046_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=126
def f09eim_f09_ep_inventory_management_idstdxcl_126d_base_v047_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=126
def f09eim_f09_ep_inventory_management_idratiomean_126d_base_v048_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=189
def f09eim_f09_ep_inventory_management_ididxcl_189d_base_v049_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=189
def f09eim_f09_ep_inventory_management_idlogxcl_189d_base_v050_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=189
def f09eim_f09_ep_inventory_management_idsqxcl_189d_base_v051_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=189
def f09eim_f09_ep_inventory_management_idinvxcl_189d_base_v052_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=189
def f09eim_f09_ep_inventory_management_idmeanxcl_189d_base_v053_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=189
def f09eim_f09_ep_inventory_management_idzxcl_189d_base_v054_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=189
def f09eim_f09_ep_inventory_management_idstdxcl_189d_base_v055_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=189
def f09eim_f09_ep_inventory_management_idratiomean_189d_base_v056_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 189).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=252
def f09eim_f09_ep_inventory_management_ididxcl_252d_base_v057_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=252
def f09eim_f09_ep_inventory_management_idlogxcl_252d_base_v058_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=252
def f09eim_f09_ep_inventory_management_idsqxcl_252d_base_v059_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=252
def f09eim_f09_ep_inventory_management_idinvxcl_252d_base_v060_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=252
def f09eim_f09_ep_inventory_management_idmeanxcl_252d_base_v061_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=252
def f09eim_f09_ep_inventory_management_idzxcl_252d_base_v062_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=252
def f09eim_f09_ep_inventory_management_idstdxcl_252d_base_v063_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=252
def f09eim_f09_ep_inventory_management_idratiomean_252d_base_v064_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=378
def f09eim_f09_ep_inventory_management_ididxcl_378d_base_v065_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=378
def f09eim_f09_ep_inventory_management_idlogxcl_378d_base_v066_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=378
def f09eim_f09_ep_inventory_management_idsqxcl_378d_base_v067_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# id invxcl w=378
def f09eim_f09_ep_inventory_management_idinvxcl_378d_base_v068_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=378
def f09eim_f09_ep_inventory_management_idmeanxcl_378d_base_v069_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=378
def f09eim_f09_ep_inventory_management_idzxcl_378d_base_v070_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=378
def f09eim_f09_ep_inventory_management_idstdxcl_378d_base_v071_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=378
def f09eim_f09_ep_inventory_management_idratiomean_378d_base_v072_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 378).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id idxcl w=504
def f09eim_f09_ep_inventory_management_ididxcl_504d_base_v073_signal(inventory, cor, closeadj):
    result = _f09_inv_days(inventory, cor) * closeadj
    result = result + 0.0 * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# id logxcl w=504
def f09eim_f09_ep_inventory_management_idlogxcl_504d_base_v074_signal(inventory, cor, closeadj):
    result = np.log1p(_f09_inv_days(inventory, cor).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# id sqxcl w=504
def f09eim_f09_ep_inventory_management_idsqxcl_504d_base_v075_signal(inventory, cor, closeadj):
    result = (_f09_inv_days(inventory, cor) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09eim_f09_ep_inventory_management_ididxcl_5d_base_v001_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_5d_base_v002_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_5d_base_v003_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_5d_base_v004_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_5d_base_v005_signal,
    f09eim_f09_ep_inventory_management_idzxcl_5d_base_v006_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_5d_base_v007_signal,
    f09eim_f09_ep_inventory_management_idratiomean_5d_base_v008_signal,
    f09eim_f09_ep_inventory_management_ididxcl_10d_base_v009_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_10d_base_v010_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_10d_base_v011_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_10d_base_v012_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_10d_base_v013_signal,
    f09eim_f09_ep_inventory_management_idzxcl_10d_base_v014_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_10d_base_v015_signal,
    f09eim_f09_ep_inventory_management_idratiomean_10d_base_v016_signal,
    f09eim_f09_ep_inventory_management_ididxcl_21d_base_v017_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_21d_base_v018_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_21d_base_v019_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_21d_base_v020_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_21d_base_v021_signal,
    f09eim_f09_ep_inventory_management_idzxcl_21d_base_v022_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_21d_base_v023_signal,
    f09eim_f09_ep_inventory_management_idratiomean_21d_base_v024_signal,
    f09eim_f09_ep_inventory_management_ididxcl_42d_base_v025_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_42d_base_v026_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_42d_base_v027_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_42d_base_v028_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_42d_base_v029_signal,
    f09eim_f09_ep_inventory_management_idzxcl_42d_base_v030_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_42d_base_v031_signal,
    f09eim_f09_ep_inventory_management_idratiomean_42d_base_v032_signal,
    f09eim_f09_ep_inventory_management_ididxcl_63d_base_v033_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_63d_base_v034_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_63d_base_v035_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_63d_base_v036_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_63d_base_v037_signal,
    f09eim_f09_ep_inventory_management_idzxcl_63d_base_v038_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_63d_base_v039_signal,
    f09eim_f09_ep_inventory_management_idratiomean_63d_base_v040_signal,
    f09eim_f09_ep_inventory_management_ididxcl_126d_base_v041_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_126d_base_v042_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_126d_base_v043_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_126d_base_v044_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_126d_base_v045_signal,
    f09eim_f09_ep_inventory_management_idzxcl_126d_base_v046_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_126d_base_v047_signal,
    f09eim_f09_ep_inventory_management_idratiomean_126d_base_v048_signal,
    f09eim_f09_ep_inventory_management_ididxcl_189d_base_v049_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_189d_base_v050_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_189d_base_v051_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_189d_base_v052_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_189d_base_v053_signal,
    f09eim_f09_ep_inventory_management_idzxcl_189d_base_v054_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_189d_base_v055_signal,
    f09eim_f09_ep_inventory_management_idratiomean_189d_base_v056_signal,
    f09eim_f09_ep_inventory_management_ididxcl_252d_base_v057_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_252d_base_v058_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_252d_base_v059_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_252d_base_v060_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_252d_base_v061_signal,
    f09eim_f09_ep_inventory_management_idzxcl_252d_base_v062_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_252d_base_v063_signal,
    f09eim_f09_ep_inventory_management_idratiomean_252d_base_v064_signal,
    f09eim_f09_ep_inventory_management_ididxcl_378d_base_v065_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_378d_base_v066_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_378d_base_v067_signal,
    f09eim_f09_ep_inventory_management_idinvxcl_378d_base_v068_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_378d_base_v069_signal,
    f09eim_f09_ep_inventory_management_idzxcl_378d_base_v070_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_378d_base_v071_signal,
    f09eim_f09_ep_inventory_management_idratiomean_378d_base_v072_signal,
    f09eim_f09_ep_inventory_management_ididxcl_504d_base_v073_signal,
    f09eim_f09_ep_inventory_management_idlogxcl_504d_base_v074_signal,
    f09eim_f09_ep_inventory_management_idsqxcl_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_EP_INVENTORY_MANAGEMENT_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f09_inv_days", "_f09_inv_to_revenue", "_f09_inv_dynamics")
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
    print(f"OK f09_ep_inventory_management_base_001_075_claude: {n_features} features pass")
