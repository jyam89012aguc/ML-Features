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
def _f48_bottom_signature(revenue, w):
    rmin = revenue.rolling(w, min_periods=max(2, w // 2)).min()
    rmean = revenue.rolling(w, min_periods=max(2, w // 2)).mean()
    return (revenue - rmin) / rmean.replace(0, np.nan).abs()


def _f48_margin_bottom(ebitdamargin, w):
    mmin = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).min()
    return (ebitdamargin - mmin)


def _f48_cycle_bottom_score(revenue, ebitda, fcf, w):
    rs = (revenue - revenue.rolling(w, min_periods=max(2, w // 2)).min()) / revenue.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan).abs()
    es = (ebitda - ebitda.rolling(w, min_periods=max(2, w // 2)).min()) / ebitda.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan).abs()
    fs = (fcf - fcf.rolling(w, min_periods=max(2, w // 2)).min()) / fcf.rolling(w, min_periods=max(2, w // 2)).mean().replace(0, np.nan).abs()
    return (rs + es + fs) / 3.0



def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_base_v001_signal(revenue):
    result = _f48_bottom_signature(revenue, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_base_v002_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_base_v003_signal(revenue, closeadj):
    result = np.log((_f48_bottom_signature(revenue, 5)).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_base_v004_signal(revenue, closeadj):
    result = np.sign(_f48_bottom_signature(revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_base_v005_signal(revenue, closeadj):
    result = np.sign(_f48_bottom_signature(revenue, 5)) * (_f48_bottom_signature(revenue, 5)).pow(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_base_v006_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_base_v007_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_base_v008_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_base_v009_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 5), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_base_v010_signal(revenue, closeadj):
    result = _mean(_f48_bottom_signature(revenue, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_base_v011_signal(revenue, closeadj):
    result = _mean(_f48_bottom_signature(revenue, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_base_v012_signal(revenue, closeadj):
    result = _mean(_f48_bottom_signature(revenue, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_base_v013_signal(revenue, closeadj):
    result = _mean(_f48_bottom_signature(revenue, 5), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_base_v014_signal(revenue, closeadj):
    result = _std(_f48_bottom_signature(revenue, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_base_v015_signal(revenue, closeadj):
    result = _std(_f48_bottom_signature(revenue, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_base_v016_signal(revenue, closeadj):
    result = _std(_f48_bottom_signature(revenue, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_base_v017_signal(revenue, closeadj):
    result = _std(_f48_bottom_signature(revenue, 5), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_base_v018_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_base_v019_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_base_v020_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_base_v021_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_base_v022_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_base_v023_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_base_v024_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_base_v025_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_diffN_21_base_v026_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_diffN_42_base_v027_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_diffN_63_base_v028_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_diffN_126_base_v029_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_absexp_21_base_v030_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_negexp_21_base_v031_signal(revenue, closeadj):
    result = -(_f48_bottom_signature(revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_tanh_21_base_v032_signal(revenue, closeadj):
    result = np.tanh(_f48_bottom_signature(revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_invexp_21_base_v033_signal(revenue, closeadj):
    result = 1.0 / (1.0 + (_f48_bottom_signature(revenue, 5)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_clipz_21_base_v034_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 5), 21).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_clipz_42_base_v035_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 5), 42).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_clipz_63_base_v036_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 5), 63).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_clipz_126_base_v037_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 5), 126).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_cubed_21_base_v038_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).pow(3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sqrtabs_21_base_v039_signal(revenue, closeadj):
    result = np.sqrt((_f48_bottom_signature(revenue, 5)).abs() + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logmean_21_base_v040_signal(revenue, closeadj):
    result = np.log(_mean((_f48_bottom_signature(revenue, 5)).abs() + 1.0, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logmean_42_base_v041_signal(revenue, closeadj):
    result = np.log(_mean((_f48_bottom_signature(revenue, 5)).abs() + 1.0, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logmean_63_base_v042_signal(revenue, closeadj):
    result = np.log(_mean((_f48_bottom_signature(revenue, 5)).abs() + 1.0, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logmean_126_base_v043_signal(revenue, closeadj):
    result = np.log(_mean((_f48_bottom_signature(revenue, 5)).abs() + 1.0, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_medN_21_base_v044_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_medN_42_base_v045_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_medN_63_base_v046_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_medN_126_base_v047_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_maxN_21_base_v048_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_maxN_42_base_v049_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_maxN_63_base_v050_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_maxN_126_base_v051_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_skewN_21_base_v052_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_skewN_42_base_v053_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_skewN_63_base_v054_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_skewN_126_base_v055_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_kurtN_21_base_v056_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_kurtN_42_base_v057_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_kurtN_63_base_v058_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_kurtN_126_base_v059_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sumN_21_base_v060_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sumN_42_base_v061_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sumN_63_base_v062_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sumN_126_base_v063_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_raw_21_base_v064_signal(revenue):
    result = _f48_bottom_signature(revenue, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_scXclose_21_base_v065_signal(revenue, closeadj):
    result = (_f48_bottom_signature(revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_logabs_21_base_v066_signal(revenue, closeadj):
    result = np.log((_f48_bottom_signature(revenue, 10)).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_sign_21_base_v067_signal(revenue, closeadj):
    result = np.sign(_f48_bottom_signature(revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_signsq_21_base_v068_signal(revenue, closeadj):
    result = np.sign(_f48_bottom_signature(revenue, 10)) * (_f48_bottom_signature(revenue, 10)).pow(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_zN_21_base_v069_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_zN_42_base_v070_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 10), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_zN_63_base_v071_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_zN_126_base_v072_signal(revenue, closeadj):
    result = _z(_f48_bottom_signature(revenue, 10), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_meanN_21_base_v073_signal(revenue, closeadj):
    result = _mean(_f48_bottom_signature(revenue, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_meanN_42_base_v074_signal(revenue, closeadj):
    result = _mean(_f48_bottom_signature(revenue, 10), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cbt_f48_commodity_bottom_to_top_bottom_signature_10d_meanN_63_base_v075_signal(revenue, closeadj):
    result = _mean(_f48_bottom_signature(revenue, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_raw_21_base_v001_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_scXclose_21_base_v002_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logabs_21_base_v003_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sign_21_base_v004_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_signsq_21_base_v005_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_21_base_v006_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_42_base_v007_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_63_base_v008_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_zN_126_base_v009_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_21_base_v010_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_42_base_v011_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_63_base_v012_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_meanN_126_base_v013_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_21_base_v014_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_42_base_v015_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_63_base_v016_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_stdN_126_base_v017_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_21_base_v018_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_42_base_v019_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_63_base_v020_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_emaN_126_base_v021_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_21_base_v022_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_42_base_v023_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_63_base_v024_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_qrank_126_base_v025_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_diffN_21_base_v026_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_diffN_42_base_v027_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_diffN_63_base_v028_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_diffN_126_base_v029_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_absexp_21_base_v030_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_negexp_21_base_v031_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_tanh_21_base_v032_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_invexp_21_base_v033_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_clipz_21_base_v034_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_clipz_42_base_v035_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_clipz_63_base_v036_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_clipz_126_base_v037_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_cubed_21_base_v038_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sqrtabs_21_base_v039_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logmean_21_base_v040_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logmean_42_base_v041_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logmean_63_base_v042_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_logmean_126_base_v043_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_medN_21_base_v044_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_medN_42_base_v045_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_medN_63_base_v046_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_medN_126_base_v047_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_maxN_21_base_v048_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_maxN_42_base_v049_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_maxN_63_base_v050_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_maxN_126_base_v051_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_skewN_21_base_v052_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_skewN_42_base_v053_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_skewN_63_base_v054_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_skewN_126_base_v055_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_kurtN_21_base_v056_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_kurtN_42_base_v057_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_kurtN_63_base_v058_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_kurtN_126_base_v059_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sumN_21_base_v060_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sumN_42_base_v061_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sumN_63_base_v062_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_5d_sumN_126_base_v063_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_raw_21_base_v064_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_scXclose_21_base_v065_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_logabs_21_base_v066_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_sign_21_base_v067_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_signsq_21_base_v068_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_zN_21_base_v069_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_zN_42_base_v070_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_zN_63_base_v071_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_zN_126_base_v072_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_meanN_21_base_v073_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_meanN_42_base_v074_signal,
    cbt_f48_commodity_bottom_to_top_bottom_signature_10d_meanN_63_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_COMMODITY_BOTTOM_TO_TOP_REGISTRY_001_075 = REGISTRY


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
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "netinc": netinc, "fcf": fcf,
        "eps": eps, "ebitdamargin": ebitdamargin, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_bottom_signature", "_f48_margin_bottom", "_f48_cycle_bottom_score",)
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
    print(f"OK {__file__}: {n_features} features pass")
