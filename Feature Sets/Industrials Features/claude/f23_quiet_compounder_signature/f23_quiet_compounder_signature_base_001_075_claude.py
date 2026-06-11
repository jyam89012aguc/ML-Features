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
def _f23_low_vol_signal(closeadj, w):
    # negative of vol of returns -> high = low vol = quiet
    rets = closeadj.pct_change()
    vol = rets.rolling(w, min_periods=max(1, w // 2)).std()
    return -vol


def _f23_steady_earnings_growth(netinc, w):
    # mean growth minus std growth -> high = steady positive growth
    growth = netinc.pct_change(periods=w)
    mu = growth.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = growth.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f23_compounder_composite(closeadj, netinc, w):
    # add low-vol signal and steady growth
    lv = _f23_low_vol_signal(closeadj, w)
    se = _f23_steady_earnings_growth(netinc, w)
    return lv + se


# v001..v015 low-vol signal
def f23qcs_f23_quiet_compounder_signature_lowvol_21d_base_v001_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_63d_base_v002_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_126d_base_v003_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_252d_base_v004_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_504d_base_v005_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_5d_base_v006_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_10d_base_v007_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_42d_base_v008_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_189d_base_v009_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_378d_base_v010_signal(closeadj):
    result = _f23_low_vol_signal(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_mean_252d_base_v011_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_z_252d_base_v012_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_z_504d_base_v013_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_std_252d_base_v014_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_ema_63d_base_v015_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 21)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016..v030 steady earnings growth
def f23qcs_f23_quiet_compounder_signature_steady_21d_base_v016_signal(netinc, closeadj):
    result = _f23_steady_earnings_growth(netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_63d_base_v017_signal(netinc, closeadj):
    result = _f23_steady_earnings_growth(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_126d_base_v018_signal(netinc, closeadj):
    result = _f23_steady_earnings_growth(netinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_252d_base_v019_signal(netinc, closeadj):
    result = _f23_steady_earnings_growth(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_504d_base_v020_signal(netinc, closeadj):
    result = _f23_steady_earnings_growth(netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_42d_base_v021_signal(netinc, closeadj):
    result = _f23_steady_earnings_growth(netinc, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_189d_base_v022_signal(netinc, closeadj):
    result = _f23_steady_earnings_growth(netinc, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_378d_base_v023_signal(netinc, closeadj):
    result = _f23_steady_earnings_growth(netinc, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_mean_252d_base_v024_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_z_252d_base_v025_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_z_504d_base_v026_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_std_252d_base_v027_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_ema_63d_base_v028_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_sq_base_v029_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_log_base_v030_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031..v045 compounder composite
def f23qcs_f23_quiet_compounder_signature_composite_21d_base_v031_signal(closeadj, netinc):
    result = _f23_compounder_composite(closeadj, netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_63d_base_v032_signal(closeadj, netinc):
    result = _f23_compounder_composite(closeadj, netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_126d_base_v033_signal(closeadj, netinc):
    result = _f23_compounder_composite(closeadj, netinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_252d_base_v034_signal(closeadj, netinc):
    result = _f23_compounder_composite(closeadj, netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_504d_base_v035_signal(closeadj, netinc):
    result = _f23_compounder_composite(closeadj, netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_42d_base_v036_signal(closeadj, netinc):
    result = _f23_compounder_composite(closeadj, netinc, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_189d_base_v037_signal(closeadj, netinc):
    result = _f23_compounder_composite(closeadj, netinc, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_378d_base_v038_signal(closeadj, netinc):
    result = _f23_compounder_composite(closeadj, netinc, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_mean_252d_base_v039_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_z_252d_base_v040_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_z_504d_base_v041_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_std_252d_base_v042_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_ema_63d_base_v043_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_sq_base_v044_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_log_base_v045_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046..v075 combos and variants
def f23qcs_f23_quiet_compounder_signature_lowvol_x_steady_base_v046_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    result = lv * se * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_plus_steady_base_v047_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    result = (lv + se) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_minus_steady_base_v048_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    result = (lv - se) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_w_252_steady_w_252_base_v049_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 252)
    se = _f23_steady_earnings_growth(netinc, 252)
    result = (lv + se) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_triple_w_base_v050_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    c = _f23_compounder_composite(closeadj, netinc, 63)
    result = (0.4 * lv + 0.4 * se + 0.2 * c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_rank_252d_base_v051_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_rank_252d_base_v052_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_rank_252d_base_v053_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_diff_21d_base_v054_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_diff_21d_base_v055_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_diff_21d_base_v056_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_cross_21_252_base_v057_signal(closeadj):
    a = _f23_low_vol_signal(closeadj, 21)
    b = _f23_low_vol_signal(closeadj, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_cross_63_252_base_v058_signal(netinc, closeadj):
    a = _f23_steady_earnings_growth(netinc, 63)
    b = _f23_steady_earnings_growth(netinc, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_cross_63_252_base_v059_signal(closeadj, netinc):
    a = _f23_compounder_composite(closeadj, netinc, 63)
    b = _f23_compounder_composite(closeadj, netinc, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_xebitda_base_v060_signal(closeadj, ebitda):
    base = _f23_low_vol_signal(closeadj, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_xebitda_base_v061_signal(netinc, ebitda, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_xebitda_base_v062_signal(closeadj, netinc, ebitda):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_xeps_base_v063_signal(closeadj, eps):
    base = _f23_low_vol_signal(closeadj, 63)
    pg = eps / (eps.rolling(252, min_periods=63).mean().replace(0, np.nan).abs() + 1e-9)
    result = base * pg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_xeps_base_v064_signal(netinc, eps, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    pg = eps / (eps.rolling(252, min_periods=63).mean().replace(0, np.nan).abs() + 1e-9)
    result = base * pg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_med_252d_base_v065_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_med_252d_base_v066_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_med_252d_base_v067_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_range_252d_base_v068_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_range_252d_base_v069_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_range_252d_base_v070_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_max_252d_base_v071_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_steady_max_252d_base_v072_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_min_252d_base_v073_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_lowvol_inv_base_v074_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = (1.0 / (base.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f23qcs_f23_quiet_compounder_signature_composite_inv_base_v075_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = (1.0 / (base.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23qcs_f23_quiet_compounder_signature_lowvol_21d_base_v001_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_63d_base_v002_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_126d_base_v003_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_252d_base_v004_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_504d_base_v005_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_5d_base_v006_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_10d_base_v007_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_42d_base_v008_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_189d_base_v009_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_378d_base_v010_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_mean_252d_base_v011_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_z_252d_base_v012_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_z_504d_base_v013_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_std_252d_base_v014_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_ema_63d_base_v015_signal,
    f23qcs_f23_quiet_compounder_signature_steady_21d_base_v016_signal,
    f23qcs_f23_quiet_compounder_signature_steady_63d_base_v017_signal,
    f23qcs_f23_quiet_compounder_signature_steady_126d_base_v018_signal,
    f23qcs_f23_quiet_compounder_signature_steady_252d_base_v019_signal,
    f23qcs_f23_quiet_compounder_signature_steady_504d_base_v020_signal,
    f23qcs_f23_quiet_compounder_signature_steady_42d_base_v021_signal,
    f23qcs_f23_quiet_compounder_signature_steady_189d_base_v022_signal,
    f23qcs_f23_quiet_compounder_signature_steady_378d_base_v023_signal,
    f23qcs_f23_quiet_compounder_signature_steady_mean_252d_base_v024_signal,
    f23qcs_f23_quiet_compounder_signature_steady_z_252d_base_v025_signal,
    f23qcs_f23_quiet_compounder_signature_steady_z_504d_base_v026_signal,
    f23qcs_f23_quiet_compounder_signature_steady_std_252d_base_v027_signal,
    f23qcs_f23_quiet_compounder_signature_steady_ema_63d_base_v028_signal,
    f23qcs_f23_quiet_compounder_signature_steady_sq_base_v029_signal,
    f23qcs_f23_quiet_compounder_signature_steady_log_base_v030_signal,
    f23qcs_f23_quiet_compounder_signature_composite_21d_base_v031_signal,
    f23qcs_f23_quiet_compounder_signature_composite_63d_base_v032_signal,
    f23qcs_f23_quiet_compounder_signature_composite_126d_base_v033_signal,
    f23qcs_f23_quiet_compounder_signature_composite_252d_base_v034_signal,
    f23qcs_f23_quiet_compounder_signature_composite_504d_base_v035_signal,
    f23qcs_f23_quiet_compounder_signature_composite_42d_base_v036_signal,
    f23qcs_f23_quiet_compounder_signature_composite_189d_base_v037_signal,
    f23qcs_f23_quiet_compounder_signature_composite_378d_base_v038_signal,
    f23qcs_f23_quiet_compounder_signature_composite_mean_252d_base_v039_signal,
    f23qcs_f23_quiet_compounder_signature_composite_z_252d_base_v040_signal,
    f23qcs_f23_quiet_compounder_signature_composite_z_504d_base_v041_signal,
    f23qcs_f23_quiet_compounder_signature_composite_std_252d_base_v042_signal,
    f23qcs_f23_quiet_compounder_signature_composite_ema_63d_base_v043_signal,
    f23qcs_f23_quiet_compounder_signature_composite_sq_base_v044_signal,
    f23qcs_f23_quiet_compounder_signature_composite_log_base_v045_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_x_steady_base_v046_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_plus_steady_base_v047_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_minus_steady_base_v048_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_w_252_steady_w_252_base_v049_signal,
    f23qcs_f23_quiet_compounder_signature_triple_w_base_v050_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_rank_252d_base_v051_signal,
    f23qcs_f23_quiet_compounder_signature_steady_rank_252d_base_v052_signal,
    f23qcs_f23_quiet_compounder_signature_composite_rank_252d_base_v053_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_diff_21d_base_v054_signal,
    f23qcs_f23_quiet_compounder_signature_steady_diff_21d_base_v055_signal,
    f23qcs_f23_quiet_compounder_signature_composite_diff_21d_base_v056_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_cross_21_252_base_v057_signal,
    f23qcs_f23_quiet_compounder_signature_steady_cross_63_252_base_v058_signal,
    f23qcs_f23_quiet_compounder_signature_composite_cross_63_252_base_v059_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_xebitda_base_v060_signal,
    f23qcs_f23_quiet_compounder_signature_steady_xebitda_base_v061_signal,
    f23qcs_f23_quiet_compounder_signature_composite_xebitda_base_v062_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_xeps_base_v063_signal,
    f23qcs_f23_quiet_compounder_signature_steady_xeps_base_v064_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_med_252d_base_v065_signal,
    f23qcs_f23_quiet_compounder_signature_steady_med_252d_base_v066_signal,
    f23qcs_f23_quiet_compounder_signature_composite_med_252d_base_v067_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_range_252d_base_v068_signal,
    f23qcs_f23_quiet_compounder_signature_steady_range_252d_base_v069_signal,
    f23qcs_f23_quiet_compounder_signature_composite_range_252d_base_v070_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_max_252d_base_v071_signal,
    f23qcs_f23_quiet_compounder_signature_steady_max_252d_base_v072_signal,
    f23qcs_f23_quiet_compounder_signature_composite_min_252d_base_v073_signal,
    f23qcs_f23_quiet_compounder_signature_lowvol_inv_base_v074_signal,
    f23qcs_f23_quiet_compounder_signature_composite_inv_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_QUIET_COMPOUNDER_SIGNATURE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")

    cols = {"closeadj": closeadj, "netinc": netinc, "ebitda": ebitda, "eps": eps}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f23_low_vol_signal", "_f23_steady_earnings_growth", "_f23_compounder_composite")
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
    print(f"OK f23_quiet_compounder_signature_base_001_075_claude: {n_features} features pass")
