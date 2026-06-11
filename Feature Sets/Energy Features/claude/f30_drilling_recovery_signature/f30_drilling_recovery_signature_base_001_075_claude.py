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
def _f30_revenue_recovery(revenue, w):
    trough = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - trough) / trough.replace(0, np.nan).abs()


def _f30_margin_recovery(ebitdamargin, w):
    trough = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - trough


def _f30_recovery_strength(revenue, ebitda, w):
    rev_t = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    eb_t = ebitda.rolling(w, min_periods=max(1, w // 2)).min()
    rec_rev = (revenue - rev_t) / rev_t.replace(0, np.nan).abs()
    rec_eb = (ebitda - eb_t) / eb_t.replace(0, np.nan).abs()
    return rec_rev + rec_eb


# ===== features =====

def f30drs_f30_drilling_recovery_signature_revrec_5d_base_xc_base_v001_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xc_base_v002_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_5d_base_xc_base_v003_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_10d_base_xc_base_v004_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xc_base_v005_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_10d_base_xc_base_v006_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_21d_base_xc_base_v007_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xc_base_v008_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_21d_base_xc_base_v009_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_42d_base_xc_base_v010_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xc_base_v011_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_42d_base_xc_base_v012_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_63d_base_xc_base_v013_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xc_base_v014_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_63d_base_xc_base_v015_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_84d_base_xc_base_v016_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 84)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xc_base_v017_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 84)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_84d_base_xc_base_v018_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 84)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_126d_base_xc_base_v019_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xc_base_v020_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_126d_base_xc_base_v021_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_189d_base_xc_base_v022_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xc_base_v023_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_189d_base_xc_base_v024_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_252d_base_xc_base_v025_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xc_base_v026_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_252d_base_xc_base_v027_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_378d_base_xc_base_v028_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xc_base_v029_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_378d_base_xc_base_v030_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_504d_base_xc_base_v031_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xc_base_v032_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_504d_base_xc_base_v033_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_5d_base_xc2_base_v034_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xc2_base_v035_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_5d_base_xc2_base_v036_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_10d_base_xc2_base_v037_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xc2_base_v038_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_10d_base_xc2_base_v039_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_21d_base_xc2_base_v040_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xc2_base_v041_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_21d_base_xc2_base_v042_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_42d_base_xc2_base_v043_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xc2_base_v044_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_42d_base_xc2_base_v045_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_63d_base_xc2_base_v046_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xc2_base_v047_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_63d_base_xc2_base_v048_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_84d_base_xc2_base_v049_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 84)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xc2_base_v050_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 84)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_84d_base_xc2_base_v051_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 84)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_126d_base_xc2_base_v052_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xc2_base_v053_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_126d_base_xc2_base_v054_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_189d_base_xc2_base_v055_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xc2_base_v056_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_189d_base_xc2_base_v057_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_252d_base_xc2_base_v058_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xc2_base_v059_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_252d_base_xc2_base_v060_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_378d_base_xc2_base_v061_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xc2_base_v062_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_378d_base_xc2_base_v063_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_504d_base_xc2_base_v064_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xc2_base_v065_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_504d_base_xc2_base_v066_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_5d_base_xmc_base_v067_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 5)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xmc_base_v068_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 5)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_5d_base_xmc_base_v069_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 5)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_10d_base_xmc_base_v070_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 10)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xmc_base_v071_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 10)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_10d_base_xmc_base_v072_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 10)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_21d_base_xmc_base_v073_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 21)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xmc_base_v074_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 21)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_21d_base_xmc_base_v075_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 21)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30drs_f30_drilling_recovery_signature_revrec_5d_base_xc_base_v001_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xc_base_v002_signal,
    f30drs_f30_drilling_recovery_signature_recstr_5d_base_xc_base_v003_signal,
    f30drs_f30_drilling_recovery_signature_revrec_10d_base_xc_base_v004_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xc_base_v005_signal,
    f30drs_f30_drilling_recovery_signature_recstr_10d_base_xc_base_v006_signal,
    f30drs_f30_drilling_recovery_signature_revrec_21d_base_xc_base_v007_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xc_base_v008_signal,
    f30drs_f30_drilling_recovery_signature_recstr_21d_base_xc_base_v009_signal,
    f30drs_f30_drilling_recovery_signature_revrec_42d_base_xc_base_v010_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xc_base_v011_signal,
    f30drs_f30_drilling_recovery_signature_recstr_42d_base_xc_base_v012_signal,
    f30drs_f30_drilling_recovery_signature_revrec_63d_base_xc_base_v013_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xc_base_v014_signal,
    f30drs_f30_drilling_recovery_signature_recstr_63d_base_xc_base_v015_signal,
    f30drs_f30_drilling_recovery_signature_revrec_84d_base_xc_base_v016_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xc_base_v017_signal,
    f30drs_f30_drilling_recovery_signature_recstr_84d_base_xc_base_v018_signal,
    f30drs_f30_drilling_recovery_signature_revrec_126d_base_xc_base_v019_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xc_base_v020_signal,
    f30drs_f30_drilling_recovery_signature_recstr_126d_base_xc_base_v021_signal,
    f30drs_f30_drilling_recovery_signature_revrec_189d_base_xc_base_v022_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xc_base_v023_signal,
    f30drs_f30_drilling_recovery_signature_recstr_189d_base_xc_base_v024_signal,
    f30drs_f30_drilling_recovery_signature_revrec_252d_base_xc_base_v025_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xc_base_v026_signal,
    f30drs_f30_drilling_recovery_signature_recstr_252d_base_xc_base_v027_signal,
    f30drs_f30_drilling_recovery_signature_revrec_378d_base_xc_base_v028_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xc_base_v029_signal,
    f30drs_f30_drilling_recovery_signature_recstr_378d_base_xc_base_v030_signal,
    f30drs_f30_drilling_recovery_signature_revrec_504d_base_xc_base_v031_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xc_base_v032_signal,
    f30drs_f30_drilling_recovery_signature_recstr_504d_base_xc_base_v033_signal,
    f30drs_f30_drilling_recovery_signature_revrec_5d_base_xc2_base_v034_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xc2_base_v035_signal,
    f30drs_f30_drilling_recovery_signature_recstr_5d_base_xc2_base_v036_signal,
    f30drs_f30_drilling_recovery_signature_revrec_10d_base_xc2_base_v037_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xc2_base_v038_signal,
    f30drs_f30_drilling_recovery_signature_recstr_10d_base_xc2_base_v039_signal,
    f30drs_f30_drilling_recovery_signature_revrec_21d_base_xc2_base_v040_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xc2_base_v041_signal,
    f30drs_f30_drilling_recovery_signature_recstr_21d_base_xc2_base_v042_signal,
    f30drs_f30_drilling_recovery_signature_revrec_42d_base_xc2_base_v043_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xc2_base_v044_signal,
    f30drs_f30_drilling_recovery_signature_recstr_42d_base_xc2_base_v045_signal,
    f30drs_f30_drilling_recovery_signature_revrec_63d_base_xc2_base_v046_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xc2_base_v047_signal,
    f30drs_f30_drilling_recovery_signature_recstr_63d_base_xc2_base_v048_signal,
    f30drs_f30_drilling_recovery_signature_revrec_84d_base_xc2_base_v049_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xc2_base_v050_signal,
    f30drs_f30_drilling_recovery_signature_recstr_84d_base_xc2_base_v051_signal,
    f30drs_f30_drilling_recovery_signature_revrec_126d_base_xc2_base_v052_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xc2_base_v053_signal,
    f30drs_f30_drilling_recovery_signature_recstr_126d_base_xc2_base_v054_signal,
    f30drs_f30_drilling_recovery_signature_revrec_189d_base_xc2_base_v055_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xc2_base_v056_signal,
    f30drs_f30_drilling_recovery_signature_recstr_189d_base_xc2_base_v057_signal,
    f30drs_f30_drilling_recovery_signature_revrec_252d_base_xc2_base_v058_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xc2_base_v059_signal,
    f30drs_f30_drilling_recovery_signature_recstr_252d_base_xc2_base_v060_signal,
    f30drs_f30_drilling_recovery_signature_revrec_378d_base_xc2_base_v061_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xc2_base_v062_signal,
    f30drs_f30_drilling_recovery_signature_recstr_378d_base_xc2_base_v063_signal,
    f30drs_f30_drilling_recovery_signature_revrec_504d_base_xc2_base_v064_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xc2_base_v065_signal,
    f30drs_f30_drilling_recovery_signature_recstr_504d_base_xc2_base_v066_signal,
    f30drs_f30_drilling_recovery_signature_revrec_5d_base_xmc_base_v067_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xmc_base_v068_signal,
    f30drs_f30_drilling_recovery_signature_recstr_5d_base_xmc_base_v069_signal,
    f30drs_f30_drilling_recovery_signature_revrec_10d_base_xmc_base_v070_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xmc_base_v071_signal,
    f30drs_f30_drilling_recovery_signature_recstr_10d_base_xmc_base_v072_signal,
    f30drs_f30_drilling_recovery_signature_revrec_21d_base_xmc_base_v073_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xmc_base_v074_signal,
    f30drs_f30_drilling_recovery_signature_recstr_21d_base_xmc_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_DRILLING_RECOVERY_SIGNATURE_REGISTRY_001_075 = REGISTRY


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
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda,
        "assets": assets, "equity": equity, "debt": debt, "cashneq": cashneq,
        "deferredrev": deferredrev, "ppnenet": ppnenet, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f30_revenue_recovery', '_f30_margin_recovery', '_f30_recovery_strength',)
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
    print(f"OK f30_drilling_recovery_signature_base_001_075_claude: {n_features} features pass")
