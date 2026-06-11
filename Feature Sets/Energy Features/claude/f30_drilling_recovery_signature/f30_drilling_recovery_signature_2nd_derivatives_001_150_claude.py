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

def f30drs_f30_drilling_recovery_signature_revrec_5d_base_xc_psw5_slope_v001_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 5)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xc_psw5_slope_v002_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 5)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_5d_base_xc_psw5_slope_v003_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 5)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_10d_base_xc_psw5_slope_v004_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 10)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xc_psw5_slope_v005_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 10)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_10d_base_xc_psw5_slope_v006_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 10)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_21d_base_xc_psw5_slope_v007_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 21)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xc_psw5_slope_v008_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 21)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_21d_base_xc_psw5_slope_v009_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 21)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_42d_base_xc_psw5_slope_v010_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 42)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xc_psw5_slope_v011_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 42)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_42d_base_xc_psw5_slope_v012_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 42)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_63d_base_xc_psw5_slope_v013_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 63)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xc_psw5_slope_v014_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 63)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_63d_base_xc_psw5_slope_v015_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 63)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_84d_base_xc_psw5_slope_v016_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 84)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xc_psw5_slope_v017_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 84)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_84d_base_xc_psw5_slope_v018_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 84)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_126d_base_xc_psw5_slope_v019_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 126)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xc_psw5_slope_v020_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 126)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_126d_base_xc_psw5_slope_v021_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 126)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_189d_base_xc_psw5_slope_v022_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 189)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xc_psw5_slope_v023_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 189)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_189d_base_xc_psw5_slope_v024_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 189)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_252d_base_xc_psw5_slope_v025_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 252)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xc_psw5_slope_v026_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 252)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_252d_base_xc_psw5_slope_v027_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 252)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_378d_base_xc_psw5_slope_v028_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 378)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xc_psw5_slope_v029_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 378)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_378d_base_xc_psw5_slope_v030_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 378)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_504d_base_xc_psw5_slope_v031_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 504)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xc_psw5_slope_v032_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 504)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_504d_base_xc_psw5_slope_v033_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 504)
    base = (base) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_5d_base_xc2_psw5_slope_v034_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 5)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xc2_psw5_slope_v035_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 5)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_5d_base_xc2_psw5_slope_v036_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 5)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_10d_base_xc2_psw5_slope_v037_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 10)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xc2_psw5_slope_v038_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 10)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_10d_base_xc2_psw5_slope_v039_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 10)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_21d_base_xc2_psw5_slope_v040_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 21)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xc2_psw5_slope_v041_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 21)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_21d_base_xc2_psw5_slope_v042_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 21)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_42d_base_xc2_psw5_slope_v043_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 42)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xc2_psw5_slope_v044_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 42)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_42d_base_xc2_psw5_slope_v045_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 42)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_63d_base_xc2_psw5_slope_v046_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 63)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xc2_psw5_slope_v047_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 63)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_63d_base_xc2_psw5_slope_v048_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 63)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_84d_base_xc2_psw5_slope_v049_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 84)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xc2_psw5_slope_v050_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 84)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_84d_base_xc2_psw5_slope_v051_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 84)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_126d_base_xc2_psw5_slope_v052_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 126)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xc2_psw5_slope_v053_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 126)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_126d_base_xc2_psw5_slope_v054_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 126)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_189d_base_xc2_psw5_slope_v055_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 189)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xc2_psw5_slope_v056_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 189)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_189d_base_xc2_psw5_slope_v057_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 189)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_252d_base_xc2_psw5_slope_v058_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 252)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xc2_psw5_slope_v059_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 252)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_252d_base_xc2_psw5_slope_v060_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 252)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_378d_base_xc2_psw5_slope_v061_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 378)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xc2_psw5_slope_v062_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 378)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_378d_base_xc2_psw5_slope_v063_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 378)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_504d_base_xc2_psw5_slope_v064_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 504)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xc2_psw5_slope_v065_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 504)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_504d_base_xc2_psw5_slope_v066_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 504)
    base = (base) * closeadj * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_5d_base_xmc_psw5_slope_v067_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 5)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xmc_psw5_slope_v068_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 5)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_5d_base_xmc_psw5_slope_v069_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 5)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_10d_base_xmc_psw5_slope_v070_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 10)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xmc_psw5_slope_v071_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 10)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_10d_base_xmc_psw5_slope_v072_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 10)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_21d_base_xmc_psw5_slope_v073_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 21)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xmc_psw5_slope_v074_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 21)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_21d_base_xmc_psw5_slope_v075_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 21)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_42d_base_xmc_psw5_slope_v076_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 42)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xmc_psw5_slope_v077_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 42)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_42d_base_xmc_psw5_slope_v078_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 42)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_63d_base_xmc_psw5_slope_v079_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 63)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xmc_psw5_slope_v080_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 63)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_63d_base_xmc_psw5_slope_v081_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 63)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_84d_base_xmc_psw5_slope_v082_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 84)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xmc_psw5_slope_v083_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 84)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_84d_base_xmc_psw5_slope_v084_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 84)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_126d_base_xmc_psw5_slope_v085_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 126)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xmc_psw5_slope_v086_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 126)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_126d_base_xmc_psw5_slope_v087_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 126)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_189d_base_xmc_psw5_slope_v088_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 189)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xmc_psw5_slope_v089_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 189)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_189d_base_xmc_psw5_slope_v090_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 189)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_252d_base_xmc_psw5_slope_v091_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 252)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xmc_psw5_slope_v092_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 252)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_252d_base_xmc_psw5_slope_v093_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 252)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_378d_base_xmc_psw5_slope_v094_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 378)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xmc_psw5_slope_v095_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 378)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_378d_base_xmc_psw5_slope_v096_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 378)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_504d_base_xmc_psw5_slope_v097_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 504)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xmc_psw5_slope_v098_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 504)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_504d_base_xmc_psw5_slope_v099_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 504)
    base = (base) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_5d_base_xzc_psw5_slope_v100_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xzc_psw5_slope_v101_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_5d_base_xzc_psw5_slope_v102_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_10d_base_xzc_psw5_slope_v103_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xzc_psw5_slope_v104_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_10d_base_xzc_psw5_slope_v105_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_21d_base_xzc_psw5_slope_v106_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xzc_psw5_slope_v107_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_21d_base_xzc_psw5_slope_v108_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_42d_base_xzc_psw5_slope_v109_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xzc_psw5_slope_v110_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_42d_base_xzc_psw5_slope_v111_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_63d_base_xzc_psw5_slope_v112_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xzc_psw5_slope_v113_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_63d_base_xzc_psw5_slope_v114_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_84d_base_xzc_psw5_slope_v115_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xzc_psw5_slope_v116_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_84d_base_xzc_psw5_slope_v117_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_126d_base_xzc_psw5_slope_v118_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xzc_psw5_slope_v119_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_126d_base_xzc_psw5_slope_v120_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_189d_base_xzc_psw5_slope_v121_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xzc_psw5_slope_v122_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_189d_base_xzc_psw5_slope_v123_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_252d_base_xzc_psw5_slope_v124_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xzc_psw5_slope_v125_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_252d_base_xzc_psw5_slope_v126_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_378d_base_xzc_psw5_slope_v127_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xzc_psw5_slope_v128_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_378d_base_xzc_psw5_slope_v129_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_504d_base_xzc_psw5_slope_v130_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xzc_psw5_slope_v131_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_504d_base_xzc_psw5_slope_v132_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_5d_base_dmc_psw5_slope_v133_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_dmc_psw5_slope_v134_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_5d_base_dmc_psw5_slope_v135_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_10d_base_dmc_psw5_slope_v136_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_dmc_psw5_slope_v137_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_10d_base_dmc_psw5_slope_v138_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_21d_base_dmc_psw5_slope_v139_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_dmc_psw5_slope_v140_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_21d_base_dmc_psw5_slope_v141_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_42d_base_dmc_psw5_slope_v142_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_dmc_psw5_slope_v143_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_42d_base_dmc_psw5_slope_v144_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_63d_base_dmc_psw5_slope_v145_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_dmc_psw5_slope_v146_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_63d_base_dmc_psw5_slope_v147_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_revrec_84d_base_dmc_psw5_slope_v148_signal(revenue, closeadj):
    base = _f30_revenue_recovery(revenue, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_dmc_psw5_slope_v149_signal(ebitdamargin, closeadj):
    base = _f30_margin_recovery(ebitdamargin, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f30drs_f30_drilling_recovery_signature_recstr_84d_base_dmc_psw5_slope_v150_signal(revenue, ebitda, closeadj):
    base = _f30_recovery_strength(revenue, ebitda, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30drs_f30_drilling_recovery_signature_revrec_5d_base_xc_psw5_slope_v001_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xc_psw5_slope_v002_signal,
    f30drs_f30_drilling_recovery_signature_recstr_5d_base_xc_psw5_slope_v003_signal,
    f30drs_f30_drilling_recovery_signature_revrec_10d_base_xc_psw5_slope_v004_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xc_psw5_slope_v005_signal,
    f30drs_f30_drilling_recovery_signature_recstr_10d_base_xc_psw5_slope_v006_signal,
    f30drs_f30_drilling_recovery_signature_revrec_21d_base_xc_psw5_slope_v007_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xc_psw5_slope_v008_signal,
    f30drs_f30_drilling_recovery_signature_recstr_21d_base_xc_psw5_slope_v009_signal,
    f30drs_f30_drilling_recovery_signature_revrec_42d_base_xc_psw5_slope_v010_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xc_psw5_slope_v011_signal,
    f30drs_f30_drilling_recovery_signature_recstr_42d_base_xc_psw5_slope_v012_signal,
    f30drs_f30_drilling_recovery_signature_revrec_63d_base_xc_psw5_slope_v013_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xc_psw5_slope_v014_signal,
    f30drs_f30_drilling_recovery_signature_recstr_63d_base_xc_psw5_slope_v015_signal,
    f30drs_f30_drilling_recovery_signature_revrec_84d_base_xc_psw5_slope_v016_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xc_psw5_slope_v017_signal,
    f30drs_f30_drilling_recovery_signature_recstr_84d_base_xc_psw5_slope_v018_signal,
    f30drs_f30_drilling_recovery_signature_revrec_126d_base_xc_psw5_slope_v019_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xc_psw5_slope_v020_signal,
    f30drs_f30_drilling_recovery_signature_recstr_126d_base_xc_psw5_slope_v021_signal,
    f30drs_f30_drilling_recovery_signature_revrec_189d_base_xc_psw5_slope_v022_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xc_psw5_slope_v023_signal,
    f30drs_f30_drilling_recovery_signature_recstr_189d_base_xc_psw5_slope_v024_signal,
    f30drs_f30_drilling_recovery_signature_revrec_252d_base_xc_psw5_slope_v025_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xc_psw5_slope_v026_signal,
    f30drs_f30_drilling_recovery_signature_recstr_252d_base_xc_psw5_slope_v027_signal,
    f30drs_f30_drilling_recovery_signature_revrec_378d_base_xc_psw5_slope_v028_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xc_psw5_slope_v029_signal,
    f30drs_f30_drilling_recovery_signature_recstr_378d_base_xc_psw5_slope_v030_signal,
    f30drs_f30_drilling_recovery_signature_revrec_504d_base_xc_psw5_slope_v031_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xc_psw5_slope_v032_signal,
    f30drs_f30_drilling_recovery_signature_recstr_504d_base_xc_psw5_slope_v033_signal,
    f30drs_f30_drilling_recovery_signature_revrec_5d_base_xc2_psw5_slope_v034_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xc2_psw5_slope_v035_signal,
    f30drs_f30_drilling_recovery_signature_recstr_5d_base_xc2_psw5_slope_v036_signal,
    f30drs_f30_drilling_recovery_signature_revrec_10d_base_xc2_psw5_slope_v037_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xc2_psw5_slope_v038_signal,
    f30drs_f30_drilling_recovery_signature_recstr_10d_base_xc2_psw5_slope_v039_signal,
    f30drs_f30_drilling_recovery_signature_revrec_21d_base_xc2_psw5_slope_v040_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xc2_psw5_slope_v041_signal,
    f30drs_f30_drilling_recovery_signature_recstr_21d_base_xc2_psw5_slope_v042_signal,
    f30drs_f30_drilling_recovery_signature_revrec_42d_base_xc2_psw5_slope_v043_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xc2_psw5_slope_v044_signal,
    f30drs_f30_drilling_recovery_signature_recstr_42d_base_xc2_psw5_slope_v045_signal,
    f30drs_f30_drilling_recovery_signature_revrec_63d_base_xc2_psw5_slope_v046_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xc2_psw5_slope_v047_signal,
    f30drs_f30_drilling_recovery_signature_recstr_63d_base_xc2_psw5_slope_v048_signal,
    f30drs_f30_drilling_recovery_signature_revrec_84d_base_xc2_psw5_slope_v049_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xc2_psw5_slope_v050_signal,
    f30drs_f30_drilling_recovery_signature_recstr_84d_base_xc2_psw5_slope_v051_signal,
    f30drs_f30_drilling_recovery_signature_revrec_126d_base_xc2_psw5_slope_v052_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xc2_psw5_slope_v053_signal,
    f30drs_f30_drilling_recovery_signature_recstr_126d_base_xc2_psw5_slope_v054_signal,
    f30drs_f30_drilling_recovery_signature_revrec_189d_base_xc2_psw5_slope_v055_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xc2_psw5_slope_v056_signal,
    f30drs_f30_drilling_recovery_signature_recstr_189d_base_xc2_psw5_slope_v057_signal,
    f30drs_f30_drilling_recovery_signature_revrec_252d_base_xc2_psw5_slope_v058_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xc2_psw5_slope_v059_signal,
    f30drs_f30_drilling_recovery_signature_recstr_252d_base_xc2_psw5_slope_v060_signal,
    f30drs_f30_drilling_recovery_signature_revrec_378d_base_xc2_psw5_slope_v061_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xc2_psw5_slope_v062_signal,
    f30drs_f30_drilling_recovery_signature_recstr_378d_base_xc2_psw5_slope_v063_signal,
    f30drs_f30_drilling_recovery_signature_revrec_504d_base_xc2_psw5_slope_v064_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xc2_psw5_slope_v065_signal,
    f30drs_f30_drilling_recovery_signature_recstr_504d_base_xc2_psw5_slope_v066_signal,
    f30drs_f30_drilling_recovery_signature_revrec_5d_base_xmc_psw5_slope_v067_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xmc_psw5_slope_v068_signal,
    f30drs_f30_drilling_recovery_signature_recstr_5d_base_xmc_psw5_slope_v069_signal,
    f30drs_f30_drilling_recovery_signature_revrec_10d_base_xmc_psw5_slope_v070_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xmc_psw5_slope_v071_signal,
    f30drs_f30_drilling_recovery_signature_recstr_10d_base_xmc_psw5_slope_v072_signal,
    f30drs_f30_drilling_recovery_signature_revrec_21d_base_xmc_psw5_slope_v073_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xmc_psw5_slope_v074_signal,
    f30drs_f30_drilling_recovery_signature_recstr_21d_base_xmc_psw5_slope_v075_signal,
    f30drs_f30_drilling_recovery_signature_revrec_42d_base_xmc_psw5_slope_v076_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xmc_psw5_slope_v077_signal,
    f30drs_f30_drilling_recovery_signature_recstr_42d_base_xmc_psw5_slope_v078_signal,
    f30drs_f30_drilling_recovery_signature_revrec_63d_base_xmc_psw5_slope_v079_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xmc_psw5_slope_v080_signal,
    f30drs_f30_drilling_recovery_signature_recstr_63d_base_xmc_psw5_slope_v081_signal,
    f30drs_f30_drilling_recovery_signature_revrec_84d_base_xmc_psw5_slope_v082_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xmc_psw5_slope_v083_signal,
    f30drs_f30_drilling_recovery_signature_recstr_84d_base_xmc_psw5_slope_v084_signal,
    f30drs_f30_drilling_recovery_signature_revrec_126d_base_xmc_psw5_slope_v085_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xmc_psw5_slope_v086_signal,
    f30drs_f30_drilling_recovery_signature_recstr_126d_base_xmc_psw5_slope_v087_signal,
    f30drs_f30_drilling_recovery_signature_revrec_189d_base_xmc_psw5_slope_v088_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xmc_psw5_slope_v089_signal,
    f30drs_f30_drilling_recovery_signature_recstr_189d_base_xmc_psw5_slope_v090_signal,
    f30drs_f30_drilling_recovery_signature_revrec_252d_base_xmc_psw5_slope_v091_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xmc_psw5_slope_v092_signal,
    f30drs_f30_drilling_recovery_signature_recstr_252d_base_xmc_psw5_slope_v093_signal,
    f30drs_f30_drilling_recovery_signature_revrec_378d_base_xmc_psw5_slope_v094_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xmc_psw5_slope_v095_signal,
    f30drs_f30_drilling_recovery_signature_recstr_378d_base_xmc_psw5_slope_v096_signal,
    f30drs_f30_drilling_recovery_signature_revrec_504d_base_xmc_psw5_slope_v097_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xmc_psw5_slope_v098_signal,
    f30drs_f30_drilling_recovery_signature_recstr_504d_base_xmc_psw5_slope_v099_signal,
    f30drs_f30_drilling_recovery_signature_revrec_5d_base_xzc_psw5_slope_v100_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_xzc_psw5_slope_v101_signal,
    f30drs_f30_drilling_recovery_signature_recstr_5d_base_xzc_psw5_slope_v102_signal,
    f30drs_f30_drilling_recovery_signature_revrec_10d_base_xzc_psw5_slope_v103_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_xzc_psw5_slope_v104_signal,
    f30drs_f30_drilling_recovery_signature_recstr_10d_base_xzc_psw5_slope_v105_signal,
    f30drs_f30_drilling_recovery_signature_revrec_21d_base_xzc_psw5_slope_v106_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_xzc_psw5_slope_v107_signal,
    f30drs_f30_drilling_recovery_signature_recstr_21d_base_xzc_psw5_slope_v108_signal,
    f30drs_f30_drilling_recovery_signature_revrec_42d_base_xzc_psw5_slope_v109_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_xzc_psw5_slope_v110_signal,
    f30drs_f30_drilling_recovery_signature_recstr_42d_base_xzc_psw5_slope_v111_signal,
    f30drs_f30_drilling_recovery_signature_revrec_63d_base_xzc_psw5_slope_v112_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_xzc_psw5_slope_v113_signal,
    f30drs_f30_drilling_recovery_signature_recstr_63d_base_xzc_psw5_slope_v114_signal,
    f30drs_f30_drilling_recovery_signature_revrec_84d_base_xzc_psw5_slope_v115_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_xzc_psw5_slope_v116_signal,
    f30drs_f30_drilling_recovery_signature_recstr_84d_base_xzc_psw5_slope_v117_signal,
    f30drs_f30_drilling_recovery_signature_revrec_126d_base_xzc_psw5_slope_v118_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_126d_base_xzc_psw5_slope_v119_signal,
    f30drs_f30_drilling_recovery_signature_recstr_126d_base_xzc_psw5_slope_v120_signal,
    f30drs_f30_drilling_recovery_signature_revrec_189d_base_xzc_psw5_slope_v121_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_189d_base_xzc_psw5_slope_v122_signal,
    f30drs_f30_drilling_recovery_signature_recstr_189d_base_xzc_psw5_slope_v123_signal,
    f30drs_f30_drilling_recovery_signature_revrec_252d_base_xzc_psw5_slope_v124_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_252d_base_xzc_psw5_slope_v125_signal,
    f30drs_f30_drilling_recovery_signature_recstr_252d_base_xzc_psw5_slope_v126_signal,
    f30drs_f30_drilling_recovery_signature_revrec_378d_base_xzc_psw5_slope_v127_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_378d_base_xzc_psw5_slope_v128_signal,
    f30drs_f30_drilling_recovery_signature_recstr_378d_base_xzc_psw5_slope_v129_signal,
    f30drs_f30_drilling_recovery_signature_revrec_504d_base_xzc_psw5_slope_v130_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_504d_base_xzc_psw5_slope_v131_signal,
    f30drs_f30_drilling_recovery_signature_recstr_504d_base_xzc_psw5_slope_v132_signal,
    f30drs_f30_drilling_recovery_signature_revrec_5d_base_dmc_psw5_slope_v133_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_5d_base_dmc_psw5_slope_v134_signal,
    f30drs_f30_drilling_recovery_signature_recstr_5d_base_dmc_psw5_slope_v135_signal,
    f30drs_f30_drilling_recovery_signature_revrec_10d_base_dmc_psw5_slope_v136_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_10d_base_dmc_psw5_slope_v137_signal,
    f30drs_f30_drilling_recovery_signature_recstr_10d_base_dmc_psw5_slope_v138_signal,
    f30drs_f30_drilling_recovery_signature_revrec_21d_base_dmc_psw5_slope_v139_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_21d_base_dmc_psw5_slope_v140_signal,
    f30drs_f30_drilling_recovery_signature_recstr_21d_base_dmc_psw5_slope_v141_signal,
    f30drs_f30_drilling_recovery_signature_revrec_42d_base_dmc_psw5_slope_v142_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_42d_base_dmc_psw5_slope_v143_signal,
    f30drs_f30_drilling_recovery_signature_recstr_42d_base_dmc_psw5_slope_v144_signal,
    f30drs_f30_drilling_recovery_signature_revrec_63d_base_dmc_psw5_slope_v145_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_63d_base_dmc_psw5_slope_v146_signal,
    f30drs_f30_drilling_recovery_signature_recstr_63d_base_dmc_psw5_slope_v147_signal,
    f30drs_f30_drilling_recovery_signature_revrec_84d_base_dmc_psw5_slope_v148_signal,
    f30drs_f30_drilling_recovery_signature_mgnrec_84d_base_dmc_psw5_slope_v149_signal,
    f30drs_f30_drilling_recovery_signature_recstr_84d_base_dmc_psw5_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_DRILLING_RECOVERY_SIGNATURE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f30_drilling_recovery_signature_2nd_derivatives_001_150_claude: {n_features} features pass")
