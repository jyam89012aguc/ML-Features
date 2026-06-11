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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _qrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====

def _f35_payout_floor(payoutratio, w):
    return payoutratio.rolling(w, min_periods=max(1, w // 2)).min()


def _f35_payout_durability(payoutratio, eps, w):
    mu = payoutratio.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = eps.rolling(w, min_periods=max(1, w // 2)).std()
    return mu / sd.replace(0, np.nan)


def _f35_payout_sustainability(payoutratio, fcfps, w):
    margin = (1.0 - payoutratio)
    fcf_g = fcfps.pct_change(periods=w)
    return margin * fcf_g


# ===== features =====
def f35bpd_f35_bank_payout_durability_payoutfloor_5d_base_v001_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_10d_base_v002_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_21d_base_v003_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_42d_base_v004_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_63d_base_v005_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_126d_base_v006_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_189d_base_v007_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_252d_base_v008_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_378d_base_v009_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloor_504d_base_v010_signal(payoutratio, closeadj):
    result = _f35_payout_floor(payoutratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_5d_base_v011_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_10d_base_v012_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_21d_base_v013_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_42d_base_v014_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_63d_base_v015_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_126d_base_v016_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_189d_base_v017_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_252d_base_v018_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_378d_base_v019_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdur_504d_base_v020_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_5d_base_v021_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_10d_base_v022_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_21d_base_v023_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_42d_base_v024_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_63d_base_v025_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_126d_base_v026_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_189d_base_v027_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_252d_base_v028_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_378d_base_v029_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsust_504d_base_v030_signal(payoutratio, fcfps, closeadj):
    result = _f35_payout_sustainability(payoutratio, fcfps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorz_63d_base_v031_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorz_126d_base_v032_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorz_252d_base_v033_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorz_504d_base_v034_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorz_21d_base_v035_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorz_42d_base_v036_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurema_21d_base_v037_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 21)
    result = _ema(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurema_63d_base_v038_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 63)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurema_126d_base_v039_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurema_252d_base_v040_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 252)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurema_504d_base_v041_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 504)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurema_42d_base_v042_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 42)
    result = _ema(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustz_63d_base_v043_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustz_126d_base_v044_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustz_252d_base_v045_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustz_504d_base_v046_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustz_21d_base_v047_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxdps_21d_base_v048_signal(payoutratio, dps, closeadj):
    base = _f35_payout_floor(payoutratio, 21)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxdps_63d_base_v049_signal(payoutratio, dps, closeadj):
    base = _f35_payout_floor(payoutratio, 63)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxdps_126d_base_v050_signal(payoutratio, dps, closeadj):
    base = _f35_payout_floor(payoutratio, 126)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxdps_252d_base_v051_signal(payoutratio, dps, closeadj):
    base = _f35_payout_floor(payoutratio, 252)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloorxdps_504d_base_v052_signal(payoutratio, dps, closeadj):
    base = _f35_payout_floor(payoutratio, 504)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdps_21d_base_v053_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 21)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdps_63d_base_v054_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 63)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdps_126d_base_v055_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 126)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdps_252d_base_v056_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 252)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurxdps_504d_base_v057_signal(payoutratio, eps, dps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 504)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxdps_21d_base_v058_signal(payoutratio, fcfps, dps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 21)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxdps_63d_base_v059_signal(payoutratio, fcfps, dps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 63)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxdps_126d_base_v060_signal(payoutratio, fcfps, dps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 126)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxdps_252d_base_v061_signal(payoutratio, fcfps, dps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 252)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustxdps_504d_base_v062_signal(payoutratio, fcfps, dps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 504)
    result = base * dps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloordiff_21d_base_v063_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 21)
    result = (base - base.shift(7)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloordiff_63d_base_v064_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloordiff_126d_base_v065_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 126)
    result = (base - base.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloordiff_252d_base_v066_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 252)
    result = (base - base.shift(84)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutfloordiff_504d_base_v067_signal(payoutratio, closeadj):
    base = _f35_payout_floor(payoutratio, 504)
    result = (base - base.shift(168)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurqrank_63d_base_v068_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 63)
    result = _qrank(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurqrank_126d_base_v069_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 126)
    result = _qrank(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurqrank_252d_base_v070_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 252)
    result = _qrank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurqrank_504d_base_v071_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 504)
    result = _qrank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutdurqrank_21d_base_v072_signal(payoutratio, eps, closeadj):
    base = _f35_payout_durability(payoutratio, eps, 21)
    result = _qrank(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustmean_63d_base_v073_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustmean_252d_base_v074_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 252)
    result = _mean(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35bpd_f35_bank_payout_durability_payoutsustmean_504d_base_v075_signal(payoutratio, fcfps, closeadj):
    base = _f35_payout_sustainability(payoutratio, fcfps, 504)
    result = _mean(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35bpd_f35_bank_payout_durability_payoutfloor_5d_base_v001_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_10d_base_v002_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_21d_base_v003_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_42d_base_v004_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_63d_base_v005_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_126d_base_v006_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_189d_base_v007_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_252d_base_v008_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_378d_base_v009_signal,
    f35bpd_f35_bank_payout_durability_payoutfloor_504d_base_v010_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_5d_base_v011_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_10d_base_v012_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_21d_base_v013_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_42d_base_v014_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_63d_base_v015_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_126d_base_v016_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_189d_base_v017_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_252d_base_v018_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_378d_base_v019_signal,
    f35bpd_f35_bank_payout_durability_payoutdur_504d_base_v020_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_5d_base_v021_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_10d_base_v022_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_21d_base_v023_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_42d_base_v024_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_63d_base_v025_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_126d_base_v026_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_189d_base_v027_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_252d_base_v028_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_378d_base_v029_signal,
    f35bpd_f35_bank_payout_durability_payoutsust_504d_base_v030_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorz_63d_base_v031_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorz_126d_base_v032_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorz_252d_base_v033_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorz_504d_base_v034_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorz_21d_base_v035_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorz_42d_base_v036_signal,
    f35bpd_f35_bank_payout_durability_payoutdurema_21d_base_v037_signal,
    f35bpd_f35_bank_payout_durability_payoutdurema_63d_base_v038_signal,
    f35bpd_f35_bank_payout_durability_payoutdurema_126d_base_v039_signal,
    f35bpd_f35_bank_payout_durability_payoutdurema_252d_base_v040_signal,
    f35bpd_f35_bank_payout_durability_payoutdurema_504d_base_v041_signal,
    f35bpd_f35_bank_payout_durability_payoutdurema_42d_base_v042_signal,
    f35bpd_f35_bank_payout_durability_payoutsustz_63d_base_v043_signal,
    f35bpd_f35_bank_payout_durability_payoutsustz_126d_base_v044_signal,
    f35bpd_f35_bank_payout_durability_payoutsustz_252d_base_v045_signal,
    f35bpd_f35_bank_payout_durability_payoutsustz_504d_base_v046_signal,
    f35bpd_f35_bank_payout_durability_payoutsustz_21d_base_v047_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxdps_21d_base_v048_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxdps_63d_base_v049_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxdps_126d_base_v050_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxdps_252d_base_v051_signal,
    f35bpd_f35_bank_payout_durability_payoutfloorxdps_504d_base_v052_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdps_21d_base_v053_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdps_63d_base_v054_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdps_126d_base_v055_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdps_252d_base_v056_signal,
    f35bpd_f35_bank_payout_durability_payoutdurxdps_504d_base_v057_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxdps_21d_base_v058_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxdps_63d_base_v059_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxdps_126d_base_v060_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxdps_252d_base_v061_signal,
    f35bpd_f35_bank_payout_durability_payoutsustxdps_504d_base_v062_signal,
    f35bpd_f35_bank_payout_durability_payoutfloordiff_21d_base_v063_signal,
    f35bpd_f35_bank_payout_durability_payoutfloordiff_63d_base_v064_signal,
    f35bpd_f35_bank_payout_durability_payoutfloordiff_126d_base_v065_signal,
    f35bpd_f35_bank_payout_durability_payoutfloordiff_252d_base_v066_signal,
    f35bpd_f35_bank_payout_durability_payoutfloordiff_504d_base_v067_signal,
    f35bpd_f35_bank_payout_durability_payoutdurqrank_63d_base_v068_signal,
    f35bpd_f35_bank_payout_durability_payoutdurqrank_126d_base_v069_signal,
    f35bpd_f35_bank_payout_durability_payoutdurqrank_252d_base_v070_signal,
    f35bpd_f35_bank_payout_durability_payoutdurqrank_504d_base_v071_signal,
    f35bpd_f35_bank_payout_durability_payoutdurqrank_21d_base_v072_signal,
    f35bpd_f35_bank_payout_durability_payoutsustmean_63d_base_v073_signal,
    f35bpd_f35_bank_payout_durability_payoutsustmean_252d_base_v074_signal,
    f35bpd_f35_bank_payout_durability_payoutsustmean_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_BANK_PAYOUT_DURABILITY_REGISTRY_001_075 = REGISTRY



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
    domain_primitives = ("_f35_payout_floor", "_f35_payout_durability", "_f35_payout_sustainability",)
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
    print(f"OK f35_bank_payout_durability_base_001_075_claude: {n_features} features pass")
