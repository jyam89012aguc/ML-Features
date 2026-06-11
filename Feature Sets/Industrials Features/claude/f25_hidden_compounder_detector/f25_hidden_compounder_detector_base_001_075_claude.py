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
def _f25_quiet_fcf_compound(fcf, w):
    # FCF growth rate consistency: mean growth minus std growth
    g = fcf.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f25_low_attention_high_growth(closeadj, volume, fcf, w):
    # low volume z-score (low attention) and high FCF growth
    vz = -((volume - volume.rolling(w, min_periods=max(1, w // 2)).mean())
           / volume.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan))
    g = fcf.pct_change(periods=w)
    gm = g.rolling(w, min_periods=max(1, w // 2)).mean()
    return vz + gm


def _f25_compounder_undiscovered(fcf, marketcap, w):
    # FCF yield trend: FCF/MarketCap rolling mean — higher means undiscovered compounder
    yield_ = fcf / marketcap.replace(0, np.nan).abs()
    return yield_.rolling(w, min_periods=max(1, w // 2)).mean()


# v001..v025 quiet fcf compound
def f25hcd_f25_hidden_compounder_detector_qfcf_21d_base_v001_signal(fcf, closeadj):
    result = _f25_quiet_fcf_compound(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_63d_base_v002_signal(fcf, closeadj):
    result = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_126d_base_v003_signal(fcf, closeadj):
    result = _f25_quiet_fcf_compound(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_252d_base_v004_signal(fcf, closeadj):
    result = _f25_quiet_fcf_compound(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_504d_base_v005_signal(fcf, closeadj):
    result = _f25_quiet_fcf_compound(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_42d_base_v006_signal(fcf, closeadj):
    result = _f25_quiet_fcf_compound(fcf, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_189d_base_v007_signal(fcf, closeadj):
    result = _f25_quiet_fcf_compound(fcf, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_378d_base_v008_signal(fcf, closeadj):
    result = _f25_quiet_fcf_compound(fcf, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_mean_252d_base_v009_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_z_252d_base_v010_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_z_504d_base_v011_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_std_252d_base_v012_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_ema_63d_base_v013_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_sq_base_v014_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_log_base_v015_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_xclose2_base_v016_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_rank252_base_v017_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_cross_63_252_base_v018_signal(fcf, closeadj):
    a = _f25_quiet_fcf_compound(fcf, 63)
    b = _f25_quiet_fcf_compound(fcf, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_min_252d_base_v019_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_max_252d_base_v020_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_range_252d_base_v021_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_med_252d_base_v022_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_demean_base_v023_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_abs_base_v024_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_inv_base_v025_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = (1.0 / (base.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026..v050 low_attention_high_growth
def f25hcd_f25_hidden_compounder_detector_lahg_21d_base_v026_signal(closeadj, volume, fcf):
    result = _f25_low_attention_high_growth(closeadj, volume, fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_63d_base_v027_signal(closeadj, volume, fcf):
    result = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_126d_base_v028_signal(closeadj, volume, fcf):
    result = _f25_low_attention_high_growth(closeadj, volume, fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_252d_base_v029_signal(closeadj, volume, fcf):
    result = _f25_low_attention_high_growth(closeadj, volume, fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_504d_base_v030_signal(closeadj, volume, fcf):
    result = _f25_low_attention_high_growth(closeadj, volume, fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_42d_base_v031_signal(closeadj, volume, fcf):
    result = _f25_low_attention_high_growth(closeadj, volume, fcf, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_189d_base_v032_signal(closeadj, volume, fcf):
    result = _f25_low_attention_high_growth(closeadj, volume, fcf, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_mean_252d_base_v033_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_z_252d_base_v034_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_std_252d_base_v035_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_ema_63d_base_v036_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_sq_base_v037_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_log_base_v038_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_rank252_base_v039_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_cross_63_252_base_v040_signal(closeadj, volume, fcf):
    a = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    b = _f25_low_attention_high_growth(closeadj, volume, fcf, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_min_252d_base_v041_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_max_252d_base_v042_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_range_252d_base_v043_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_med_252d_base_v044_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_demean_base_v045_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_abs_base_v046_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_inv_base_v047_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = (1.0 / (base.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_xclose2_base_v048_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_xvolume_base_v049_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    vg = volume / (volume.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * vg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_lahg_sign_base_v050_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051..v075 undiscovered compounder + combos
def f25hcd_f25_hidden_compounder_detector_und_21d_base_v051_signal(fcf, marketcap, closeadj):
    result = _f25_compounder_undiscovered(fcf, marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_63d_base_v052_signal(fcf, marketcap, closeadj):
    result = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_126d_base_v053_signal(fcf, marketcap, closeadj):
    result = _f25_compounder_undiscovered(fcf, marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_252d_base_v054_signal(fcf, marketcap, closeadj):
    result = _f25_compounder_undiscovered(fcf, marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_504d_base_v055_signal(fcf, marketcap, closeadj):
    result = _f25_compounder_undiscovered(fcf, marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_z_252d_base_v056_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_std_252d_base_v057_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_ema_63d_base_v058_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_rank252_base_v059_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_diff_21d_base_v060_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_demean_base_v061_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_xclose2_base_v062_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_sq_base_v063_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_log_base_v064_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_med_252d_base_v065_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_x_und_base_v066_signal(fcf, marketcap, closeadj):
    q = _f25_quiet_fcf_compound(fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = q * u * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_plus_und_base_v067_signal(fcf, marketcap, closeadj):
    q = _f25_quiet_fcf_compound(fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = (q + u) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_x_lahg_base_v068_signal(closeadj, volume, fcf):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = q * l * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_x_lahg_base_v069_signal(closeadj, volume, fcf, marketcap):
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = l * u * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_triple_sum_base_v070_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = (q + l + u) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_triple_w_base_v071_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = (0.4 * q + 0.3 * l + 0.3 * u) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_triple_product_base_v072_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = q * l * u * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_cross_63_252_base_v073_signal(fcf, marketcap, closeadj):
    a = _f25_compounder_undiscovered(fcf, marketcap, 63)
    b = _f25_compounder_undiscovered(fcf, marketcap, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_qfcf_x_fcf_base_v074_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    fg = fcf / (fcf.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * fg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f25hcd_f25_hidden_compounder_detector_und_x_mcap_base_v075_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    mg = marketcap / (marketcap.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * mg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25hcd_f25_hidden_compounder_detector_qfcf_21d_base_v001_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_63d_base_v002_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_126d_base_v003_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_252d_base_v004_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_504d_base_v005_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_42d_base_v006_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_189d_base_v007_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_378d_base_v008_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_mean_252d_base_v009_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_z_252d_base_v010_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_z_504d_base_v011_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_std_252d_base_v012_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_ema_63d_base_v013_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_sq_base_v014_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_log_base_v015_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_xclose2_base_v016_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_rank252_base_v017_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_cross_63_252_base_v018_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_min_252d_base_v019_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_max_252d_base_v020_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_range_252d_base_v021_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_med_252d_base_v022_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_demean_base_v023_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_abs_base_v024_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_inv_base_v025_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_21d_base_v026_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_63d_base_v027_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_126d_base_v028_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_252d_base_v029_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_504d_base_v030_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_42d_base_v031_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_189d_base_v032_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_mean_252d_base_v033_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_z_252d_base_v034_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_std_252d_base_v035_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_ema_63d_base_v036_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_sq_base_v037_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_log_base_v038_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_rank252_base_v039_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_cross_63_252_base_v040_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_min_252d_base_v041_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_max_252d_base_v042_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_range_252d_base_v043_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_med_252d_base_v044_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_demean_base_v045_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_abs_base_v046_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_inv_base_v047_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_xclose2_base_v048_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_xvolume_base_v049_signal,
    f25hcd_f25_hidden_compounder_detector_lahg_sign_base_v050_signal,
    f25hcd_f25_hidden_compounder_detector_und_21d_base_v051_signal,
    f25hcd_f25_hidden_compounder_detector_und_63d_base_v052_signal,
    f25hcd_f25_hidden_compounder_detector_und_126d_base_v053_signal,
    f25hcd_f25_hidden_compounder_detector_und_252d_base_v054_signal,
    f25hcd_f25_hidden_compounder_detector_und_504d_base_v055_signal,
    f25hcd_f25_hidden_compounder_detector_und_z_252d_base_v056_signal,
    f25hcd_f25_hidden_compounder_detector_und_std_252d_base_v057_signal,
    f25hcd_f25_hidden_compounder_detector_und_ema_63d_base_v058_signal,
    f25hcd_f25_hidden_compounder_detector_und_rank252_base_v059_signal,
    f25hcd_f25_hidden_compounder_detector_und_diff_21d_base_v060_signal,
    f25hcd_f25_hidden_compounder_detector_und_demean_base_v061_signal,
    f25hcd_f25_hidden_compounder_detector_und_xclose2_base_v062_signal,
    f25hcd_f25_hidden_compounder_detector_und_sq_base_v063_signal,
    f25hcd_f25_hidden_compounder_detector_und_log_base_v064_signal,
    f25hcd_f25_hidden_compounder_detector_und_med_252d_base_v065_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_x_und_base_v066_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_plus_und_base_v067_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_x_lahg_base_v068_signal,
    f25hcd_f25_hidden_compounder_detector_und_x_lahg_base_v069_signal,
    f25hcd_f25_hidden_compounder_detector_triple_sum_base_v070_signal,
    f25hcd_f25_hidden_compounder_detector_triple_w_base_v071_signal,
    f25hcd_f25_hidden_compounder_detector_triple_product_base_v072_signal,
    f25hcd_f25_hidden_compounder_detector_und_cross_63_252_base_v073_signal,
    f25hcd_f25_hidden_compounder_detector_qfcf_x_fcf_base_v074_signal,
    f25hcd_f25_hidden_compounder_detector_und_x_mcap_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_HIDDEN_COMPOUNDER_DETECTOR_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    fcf = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")

    cols = {"closeadj": closeadj, "volume": volume, "fcf": fcf, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f25_quiet_fcf_compound", "_f25_low_attention_high_growth", "_f25_compounder_undiscovered")
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
    print(f"OK f25_hidden_compounder_detector_base_001_075_claude: {n_features} features pass")
