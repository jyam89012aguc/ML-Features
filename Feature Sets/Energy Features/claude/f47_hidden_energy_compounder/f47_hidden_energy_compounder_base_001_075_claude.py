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
def _f47_quiet_fcf_growth(fcf, w):
    g = fcf.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(2, w // 2)).std()
    return g / sd.replace(0, np.nan).abs()


def _f47_low_attention_growth(closeadj, volume, fcf, w):
    dv = closeadj * volume
    attn = dv.rolling(w, min_periods=max(2, w // 2)).mean()
    g = fcf.pct_change(periods=w)
    return (g / attn.replace(0, np.nan).abs()) * closeadj


def _f47_hidden_quality(fcf, roic, w):
    fg = fcf.pct_change(periods=w)
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    return (fg * rq)



def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_base_v001_signal(fcf):
    result = _f47_quiet_fcf_growth(fcf, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_base_v002_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_base_v003_signal(fcf, closeadj):
    result = np.log((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_base_v004_signal(fcf, closeadj):
    result = np.sign(_f47_quiet_fcf_growth(fcf, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_base_v005_signal(fcf, closeadj):
    result = np.sign(_f47_quiet_fcf_growth(fcf, 5)) * (_f47_quiet_fcf_growth(fcf, 5)).pow(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_base_v006_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_base_v007_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_base_v008_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_base_v009_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_base_v010_signal(fcf, closeadj):
    result = _mean(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_base_v011_signal(fcf, closeadj):
    result = _mean(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_base_v012_signal(fcf, closeadj):
    result = _mean(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_base_v013_signal(fcf, closeadj):
    result = _mean(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_base_v014_signal(fcf, closeadj):
    result = _std(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_base_v015_signal(fcf, closeadj):
    result = _std(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_base_v016_signal(fcf, closeadj):
    result = _std(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_base_v017_signal(fcf, closeadj):
    result = _std(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_base_v018_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_base_v019_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).ewm(span=42, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_base_v020_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_base_v021_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_base_v022_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_base_v023_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_base_v024_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_base_v025_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_diffN_21_base_v026_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_diffN_42_base_v027_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_diffN_63_base_v028_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_diffN_126_base_v029_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_absexp_21_base_v030_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_negexp_21_base_v031_signal(fcf, closeadj):
    result = -(_f47_quiet_fcf_growth(fcf, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_tanh_21_base_v032_signal(fcf, closeadj):
    result = np.tanh(_f47_quiet_fcf_growth(fcf, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_invexp_21_base_v033_signal(fcf, closeadj):
    result = 1.0 / (1.0 + (_f47_quiet_fcf_growth(fcf, 5)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_clipz_21_base_v034_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 5), 21).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_clipz_42_base_v035_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 5), 42).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_clipz_63_base_v036_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 5), 63).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_clipz_126_base_v037_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 5), 126).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_cubed_21_base_v038_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).pow(3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sqrtabs_21_base_v039_signal(fcf, closeadj):
    result = np.sqrt((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logmean_21_base_v040_signal(fcf, closeadj):
    result = np.log(_mean((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logmean_42_base_v041_signal(fcf, closeadj):
    result = np.log(_mean((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logmean_63_base_v042_signal(fcf, closeadj):
    result = np.log(_mean((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logmean_126_base_v043_signal(fcf, closeadj):
    result = np.log(_mean((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_medN_21_base_v044_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_medN_42_base_v045_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_medN_63_base_v046_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_medN_126_base_v047_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_minN_21_base_v048_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_minN_42_base_v049_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_minN_63_base_v050_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_minN_126_base_v051_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_maxN_21_base_v052_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_maxN_42_base_v053_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_maxN_63_base_v054_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_maxN_126_base_v055_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_skewN_21_base_v056_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_skewN_42_base_v057_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_skewN_63_base_v058_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_skewN_126_base_v059_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_kurtN_21_base_v060_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_kurtN_42_base_v061_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_kurtN_63_base_v062_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_kurtN_126_base_v063_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sumN_21_base_v064_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sumN_42_base_v065_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sumN_63_base_v066_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sumN_126_base_v067_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_raw_21_base_v068_signal(fcf):
    result = _f47_quiet_fcf_growth(fcf, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_scXclose_21_base_v069_signal(fcf, closeadj):
    result = (_f47_quiet_fcf_growth(fcf, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_logabs_21_base_v070_signal(fcf, closeadj):
    result = np.log((_f47_quiet_fcf_growth(fcf, 10)).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_sign_21_base_v071_signal(fcf, closeadj):
    result = np.sign(_f47_quiet_fcf_growth(fcf, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_signsq_21_base_v072_signal(fcf, closeadj):
    result = np.sign(_f47_quiet_fcf_growth(fcf, 10)) * (_f47_quiet_fcf_growth(fcf, 10)).pow(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_zN_21_base_v073_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_zN_42_base_v074_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 10), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_zN_63_base_v075_signal(fcf, closeadj):
    result = _z(_f47_quiet_fcf_growth(fcf, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_base_v001_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_base_v002_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_base_v003_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_base_v004_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_base_v005_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_base_v006_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_base_v007_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_base_v008_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_base_v009_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_base_v010_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_base_v011_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_base_v012_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_base_v013_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_base_v014_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_base_v015_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_base_v016_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_base_v017_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_base_v018_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_base_v019_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_base_v020_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_base_v021_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_base_v022_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_base_v023_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_base_v024_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_base_v025_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_diffN_21_base_v026_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_diffN_42_base_v027_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_diffN_63_base_v028_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_diffN_126_base_v029_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_absexp_21_base_v030_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_negexp_21_base_v031_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_tanh_21_base_v032_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_invexp_21_base_v033_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_clipz_21_base_v034_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_clipz_42_base_v035_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_clipz_63_base_v036_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_clipz_126_base_v037_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_cubed_21_base_v038_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sqrtabs_21_base_v039_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logmean_21_base_v040_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logmean_42_base_v041_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logmean_63_base_v042_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logmean_126_base_v043_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_medN_21_base_v044_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_medN_42_base_v045_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_medN_63_base_v046_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_medN_126_base_v047_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_minN_21_base_v048_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_minN_42_base_v049_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_minN_63_base_v050_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_minN_126_base_v051_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_maxN_21_base_v052_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_maxN_42_base_v053_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_maxN_63_base_v054_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_maxN_126_base_v055_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_skewN_21_base_v056_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_skewN_42_base_v057_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_skewN_63_base_v058_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_skewN_126_base_v059_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_kurtN_21_base_v060_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_kurtN_42_base_v061_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_kurtN_63_base_v062_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_kurtN_126_base_v063_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sumN_21_base_v064_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sumN_42_base_v065_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sumN_63_base_v066_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sumN_126_base_v067_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_raw_21_base_v068_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_scXclose_21_base_v069_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_logabs_21_base_v070_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_sign_21_base_v071_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_signsq_21_base_v072_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_zN_21_base_v073_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_zN_42_base_v074_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_10d_zN_63_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HIDDEN_ENERGY_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f47_quiet_fcf_growth", "_f47_low_attention_growth", "_f47_hidden_quality",)
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
