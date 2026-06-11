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
def _f18_sga_to_revenue(sgna, revenue):
    return sgna / revenue.replace(0, np.nan).abs()


def _f18_cac_efficiency(sgna, revenue, w):
    rev_growth = revenue.pct_change(periods=w)
    return rev_growth / (sgna / revenue.replace(0, np.nan).abs()).replace(0, np.nan)


def _f18_acquisition_leverage(sgna, revenue, w):
    sga_growth = sgna.pct_change(periods=w)
    rev_growth = revenue.pct_change(periods=w)
    return rev_growth - sga_growth


# ===== features =====
def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v001_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v002_signal(sgna, revenue, closeadj):
    result = _mean(_f18_sga_to_revenue(sgna, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v003_signal(sgna, revenue, closeadj):
    result = _mean(_f18_sga_to_revenue(sgna, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v004_signal(sgna, revenue, closeadj):
    result = _mean(_f18_sga_to_revenue(sgna, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v005_signal(sgna, revenue, closeadj):
    result = _std(_f18_sga_to_revenue(sgna, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v006_signal(sgna, revenue, closeadj):
    result = _std(_f18_sga_to_revenue(sgna, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v007_signal(sgna, revenue, closeadj):
    result = _std(_f18_sga_to_revenue(sgna, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v008_signal(sgna, revenue, closeadj):
    result = _z(_f18_sga_to_revenue(sgna, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v009_signal(sgna, revenue, closeadj):
    result = _z(_f18_sga_to_revenue(sgna, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v010_signal(sgna, revenue, closeadj):
    result = _z(_f18_sga_to_revenue(sgna, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v011_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v012_signal(sgna, revenue, closeadj):
    result = (-_f18_sga_to_revenue(sgna, revenue)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v013_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v014_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v015_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v016_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v017_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v018_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v019_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v020_signal(sgna, revenue, closeadj):
    result = np.log(_f18_sga_to_revenue(sgna, revenue).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v021_signal(sgna, revenue, closeadj):
    result = np.sign(_f18_sga_to_revenue(sgna, revenue)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v022_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v023_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v024_signal(sgna, revenue, closeadj):
    result = _f18_sga_to_revenue(sgna, revenue).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v025_signal(sgna, revenue, closeadj):
    result = (_f18_sga_to_revenue(sgna, revenue).rolling(21, min_periods=max(1, 21 // 2)).max() - _f18_sga_to_revenue(sgna, revenue).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v026_signal(sgna, revenue, closeadj):
    result = (_f18_sga_to_revenue(sgna, revenue).rolling(63, min_periods=max(1, 63 // 2)).max() - _f18_sga_to_revenue(sgna, revenue).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v027_signal(sgna, revenue, closeadj):
    result = (_f18_sga_to_revenue(sgna, revenue).rolling(252, min_periods=max(1, 252 // 2)).max() - _f18_sga_to_revenue(sgna, revenue).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v028_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v029_signal(sgna, revenue, closeadj):
    result = _mean(_f18_cac_efficiency(sgna, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v030_signal(sgna, revenue, closeadj):
    result = _mean(_f18_cac_efficiency(sgna, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v031_signal(sgna, revenue, closeadj):
    result = _mean(_f18_cac_efficiency(sgna, revenue, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v032_signal(sgna, revenue, closeadj):
    result = _std(_f18_cac_efficiency(sgna, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v033_signal(sgna, revenue, closeadj):
    result = _std(_f18_cac_efficiency(sgna, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v034_signal(sgna, revenue, closeadj):
    result = _std(_f18_cac_efficiency(sgna, revenue, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v035_signal(sgna, revenue, closeadj):
    result = _z(_f18_cac_efficiency(sgna, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v036_signal(sgna, revenue, closeadj):
    result = _z(_f18_cac_efficiency(sgna, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v037_signal(sgna, revenue, closeadj):
    result = _z(_f18_cac_efficiency(sgna, revenue, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v038_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v039_signal(sgna, revenue, closeadj):
    result = (-_f18_cac_efficiency(sgna, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v040_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21) * _f18_cac_efficiency(sgna, revenue, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v041_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v042_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v043_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v044_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v045_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v046_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v047_signal(sgna, revenue, closeadj):
    result = np.log(_f18_cac_efficiency(sgna, revenue, 21).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v048_signal(sgna, revenue, closeadj):
    result = np.sign(_f18_cac_efficiency(sgna, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v049_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v050_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v051_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 21).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v052_signal(sgna, revenue, closeadj):
    result = (_f18_cac_efficiency(sgna, revenue, 21).rolling(21, min_periods=max(1, 21 // 2)).max() - _f18_cac_efficiency(sgna, revenue, 21).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v053_signal(sgna, revenue, closeadj):
    result = (_f18_cac_efficiency(sgna, revenue, 21).rolling(63, min_periods=max(1, 63 // 2)).max() - _f18_cac_efficiency(sgna, revenue, 21).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v054_signal(sgna, revenue, closeadj):
    result = (_f18_cac_efficiency(sgna, revenue, 21).rolling(252, min_periods=max(1, 252 // 2)).max() - _f18_cac_efficiency(sgna, revenue, 21).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v055_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v056_signal(sgna, revenue, closeadj):
    result = _mean(_f18_cac_efficiency(sgna, revenue, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v057_signal(sgna, revenue, closeadj):
    result = _mean(_f18_cac_efficiency(sgna, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v058_signal(sgna, revenue, closeadj):
    result = _mean(_f18_cac_efficiency(sgna, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v059_signal(sgna, revenue, closeadj):
    result = _std(_f18_cac_efficiency(sgna, revenue, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v060_signal(sgna, revenue, closeadj):
    result = _std(_f18_cac_efficiency(sgna, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v061_signal(sgna, revenue, closeadj):
    result = _std(_f18_cac_efficiency(sgna, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v062_signal(sgna, revenue, closeadj):
    result = _z(_f18_cac_efficiency(sgna, revenue, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v063_signal(sgna, revenue, closeadj):
    result = _z(_f18_cac_efficiency(sgna, revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v064_signal(sgna, revenue, closeadj):
    result = _z(_f18_cac_efficiency(sgna, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v065_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v066_signal(sgna, revenue, closeadj):
    result = (-_f18_cac_efficiency(sgna, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v067_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63) * _f18_cac_efficiency(sgna, revenue, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v068_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v069_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v070_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v071_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v072_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v073_signal(sgna, revenue, closeadj):
    result = _f18_cac_efficiency(sgna, revenue, 63).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v074_signal(sgna, revenue, closeadj):
    result = np.log(_f18_cac_efficiency(sgna, revenue, 63).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v075_signal(sgna, revenue, closeadj):
    result = np.sign(_f18_cac_efficiency(sgna, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v001_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v002_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v003_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v004_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v005_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v006_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v007_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v008_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v009_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v010_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v011_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v012_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v013_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v014_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v015_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v016_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v017_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v018_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v019_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v020_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v021_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v022_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v023_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v024_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v025_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v026_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_base_v027_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v028_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v029_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v030_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v031_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v032_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v033_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v034_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v035_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v036_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v037_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v038_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v039_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v040_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v041_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v042_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v043_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v044_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v045_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v046_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v047_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v048_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v049_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v050_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v051_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v052_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v053_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_21d_base_v054_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v055_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v056_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v057_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v058_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v059_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v060_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v061_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v062_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v063_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v064_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v065_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v066_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v067_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v068_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v069_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v070_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v071_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v072_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v073_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v074_signal,
    f18hca_f18_healthit_customer_acquisition_cacefficiency_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_HEALTHIT_CUSTOMER_ACQUISITION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "sgna": sgna,
        "opex": opex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f18_sga_to_revenue', '_f18_cac_efficiency', '_f18_acquisition_leverage')
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
    print(f"OK f18_healthit_customer_acquisition_base_001_075_claude: {n_features} features pass")
