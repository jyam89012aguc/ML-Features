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
def _f075_gm_yoy(grossmargin, w):
    return grossmargin.diff(periods=w) * grossmargin


def _f075_gm_expansion(grossmargin, w):
    avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return (grossmargin - avg) * grossmargin


def _f075_pricing_power(grossmargin, w):
    avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (grossmargin - avg) / sd.replace(0, np.nan) * grossmargin

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v001_signal(grossmargin, closeadj):
    result = _f075_gm_yoy(grossmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v002_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v003_signal(grossmargin, closeadj):
    result = np.sign(_f075_gm_yoy(grossmargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v004_signal(grossmargin, closeadj):
    result = _mean(_f075_gm_yoy(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v005_signal(grossmargin, closeadj):
    result = _std(_f075_gm_yoy(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v006_signal(grossmargin, closeadj):
    result = _z(_f075_gm_yoy(grossmargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v007_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 21)) * (_f075_gm_yoy(grossmargin, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v008_signal(grossmargin, closeadj):
    result = np.sqrt((_f075_gm_yoy(grossmargin, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v009_signal(grossmargin, closeadj):
    result = np.log1p((_f075_gm_yoy(grossmargin, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v010_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v011_signal(grossmargin, closeadj):
    result = _mean(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v012_signal(grossmargin, closeadj):
    result = _std(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v013_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v014_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v015_signal(grossmargin, closeadj):
    result = _z(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v016_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v017_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v018_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v019_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v020_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v021_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v022_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 252)) * (_f075_gm_yoy(grossmargin, 252)) * (_f075_gm_yoy(grossmargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v023_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v024_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 252)) - (_f075_gm_yoy(grossmargin, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v025_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 252)) / (_f075_gm_yoy(grossmargin, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v026_signal(grossmargin, closeadj):
    result = _f075_gm_expansion(grossmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v027_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v028_signal(grossmargin, closeadj):
    result = np.sign(_f075_gm_expansion(grossmargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v029_signal(grossmargin, closeadj):
    result = _mean(_f075_gm_expansion(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v030_signal(grossmargin, closeadj):
    result = _std(_f075_gm_expansion(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v031_signal(grossmargin, closeadj):
    result = _z(_f075_gm_expansion(grossmargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v032_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 21)) * (_f075_gm_expansion(grossmargin, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v033_signal(grossmargin, closeadj):
    result = np.sqrt((_f075_gm_expansion(grossmargin, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v034_signal(grossmargin, closeadj):
    result = np.log1p((_f075_gm_expansion(grossmargin, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v035_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v036_signal(grossmargin, closeadj):
    result = _mean(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v037_signal(grossmargin, closeadj):
    result = _std(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v038_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v039_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v040_signal(grossmargin, closeadj):
    result = _z(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v041_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v042_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v043_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v044_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v045_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v046_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v047_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 252)) * (_f075_gm_expansion(grossmargin, 252)) * (_f075_gm_expansion(grossmargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v048_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v049_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 252)) - (_f075_gm_expansion(grossmargin, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v050_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 252)) / (_f075_gm_expansion(grossmargin, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v051_signal(grossmargin, closeadj):
    result = _f075_pricing_power(grossmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v052_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v053_signal(grossmargin, closeadj):
    result = np.sign(_f075_pricing_power(grossmargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v054_signal(grossmargin, closeadj):
    result = _mean(_f075_pricing_power(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v055_signal(grossmargin, closeadj):
    result = _std(_f075_pricing_power(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v056_signal(grossmargin, closeadj):
    result = _z(_f075_pricing_power(grossmargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v057_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 21)) * (_f075_pricing_power(grossmargin, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v058_signal(grossmargin, closeadj):
    result = np.sqrt((_f075_pricing_power(grossmargin, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v059_signal(grossmargin, closeadj):
    result = np.log1p((_f075_pricing_power(grossmargin, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v060_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v061_signal(grossmargin, closeadj):
    result = _mean(_f075_pricing_power(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v062_signal(grossmargin, closeadj):
    result = _std(_f075_pricing_power(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v063_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v064_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v065_signal(grossmargin, closeadj):
    result = _z(_f075_pricing_power(grossmargin, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v066_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v067_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v068_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v069_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v070_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v071_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v072_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 252)) * (_f075_pricing_power(grossmargin, 252)) * (_f075_pricing_power(grossmargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v073_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v074_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 252)) - (_f075_pricing_power(grossmargin, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v075_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 252)) / (_f075_pricing_power(grossmargin, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v001_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v002_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v003_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v004_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v005_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v006_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v007_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v008_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v009_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v010_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v011_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v012_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v013_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v014_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v015_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v016_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v017_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v018_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v019_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v020_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v021_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v022_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v023_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v024_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v025_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v026_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v027_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v028_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v029_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v030_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v031_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v032_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v033_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v034_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v035_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v036_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v037_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v038_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v039_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v040_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v041_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v042_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v043_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v044_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v045_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v046_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v047_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v048_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v049_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v050_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v051_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v052_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v053_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v054_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v055_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v056_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v057_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v058_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v059_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v060_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v061_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v062_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v063_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v064_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v065_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v066_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v067_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v068_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v069_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v070_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v071_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v072_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v073_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v074_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F075_GROSS_MARGIN_EXPANSION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    cols = {"grossmargin": grossmargin, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f075_gm_yoy", "_f075_gm_expansion", "_f075_pricing_power")
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
    print(f"OK f075_gross_margin_expansion_001_075_claude: {n_features} features pass")
