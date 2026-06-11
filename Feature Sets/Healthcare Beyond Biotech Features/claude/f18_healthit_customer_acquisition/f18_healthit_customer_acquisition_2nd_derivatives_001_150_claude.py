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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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
def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v001_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v002_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v003_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v004_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v005_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v006_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v007_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v008_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v009_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v010_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v011_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v012_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v013_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v014_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v015_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v016_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v017_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v018_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v019_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v020_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v021_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v022_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v023_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v024_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v025_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v026_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v027_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v028_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v029_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v030_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v031_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v032_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * closeadj
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v033_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v034_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v035_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v036_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v037_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v038_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v039_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v040_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v041_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v042_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v043_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v044_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v045_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v046_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v047_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v048_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v049_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v050_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v051_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v052_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v053_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v054_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v055_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v056_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v057_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v058_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v059_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v060_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v061_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v062_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v063_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v064_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v065_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v066_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v067_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v068_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v069_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v070_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v071_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v072_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v073_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v074_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v075_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v076_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v077_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v078_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v079_signal(sgna, revenue):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v080_signal(sgna, revenue, closeadj):
    base = _mean(_f18_sga_to_revenue(sgna, revenue), 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v081_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v082_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v083_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v084_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v085_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v086_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v087_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v088_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v089_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v090_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v091_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v092_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v093_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v094_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v095_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v096_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v097_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v098_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v099_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v100_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v101_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v102_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v103_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v104_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v105_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v106_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v107_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v108_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v109_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v110_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v111_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v112_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v113_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v114_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v115_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v116_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v117_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v118_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v119_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v120_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v121_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v122_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v123_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v124_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v125_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v126_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v127_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v128_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v129_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v130_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v131_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v132_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v133_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v134_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v135_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v136_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v137_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v138_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v139_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v140_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v141_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v142_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v143_signal(sgna, revenue):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v144_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue) * _f18_sga_to_revenue(sgna, revenue).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v145_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v146_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs() * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v147_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v148_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs() * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v149_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v150_signal(sgna, revenue, closeadj):
    base = _f18_sga_to_revenue(sgna, revenue).abs() * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v001_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v002_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v003_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v004_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v005_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v006_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v007_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v008_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v009_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v010_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v011_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v012_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v013_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v014_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v015_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v016_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v017_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v018_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v019_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v020_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v021_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v022_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v023_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v024_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v025_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v026_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v027_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v028_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v029_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v030_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v031_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v032_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v033_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v034_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v035_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v036_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v037_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v038_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v039_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v040_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v041_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v042_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v043_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v044_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v045_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v046_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v047_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v048_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v049_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v050_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v051_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v052_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v053_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v054_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v055_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v056_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v057_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v058_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v059_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v060_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v061_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v062_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v063_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v064_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v065_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v066_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v067_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v068_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v069_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v070_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v071_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v072_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v073_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v074_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v075_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v076_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v077_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v078_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v079_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v080_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v081_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v082_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v083_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v084_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v085_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v086_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v087_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v088_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v089_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v090_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v091_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v092_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v093_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v094_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v095_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v096_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v097_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v098_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v099_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v100_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v101_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v102_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v103_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v104_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v105_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v106_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v107_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v108_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v109_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v110_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v111_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v112_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v113_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v114_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v115_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v116_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v117_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v118_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v119_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v120_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v121_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v122_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v123_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v124_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v125_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v126_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v127_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v128_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v129_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v130_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v131_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v132_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v133_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v134_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v135_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v136_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v137_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v138_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v139_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v140_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v141_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v142_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v143_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v144_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v145_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v146_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v147_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v148_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v149_signal,
    f18hca_f18_healthit_customer_acquisition_sgatorevenue_21d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_HEALTHIT_CUSTOMER_ACQUISITION_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f18_healthit_customer_acquisition_2nd_derivatives_001_150_claude: {n_features} features pass")
