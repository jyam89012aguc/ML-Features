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
def _f089_share_decline(sharesbas, w):
    return -(sharesbas.diff(periods=w) / sharesbas.abs().shift(w).replace(0, np.nan))


def _f089_retained_growth(retearn, w):
    return retearn.diff(periods=w) / retearn.abs().shift(w).replace(0, np.nan)


def _f089_insider_signal_proxy(sharesbas, retearn, w):
    sd = -(sharesbas.diff(periods=w) / sharesbas.abs().shift(w).replace(0, np.nan))
    rg = retearn.diff(periods=w) / retearn.abs().shift(w).replace(0, np.nan)
    return sd + rg

def f089nib_f089_net_insider_buying_proxy_shd_5d_base_v001_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_5d_base_v002_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_5d_base_v003_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_10d_base_v004_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_10d_base_v005_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_10d_base_v006_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_21d_base_v007_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_21d_base_v008_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_21d_base_v009_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_42d_base_v010_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_42d_base_v011_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_42d_base_v012_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_63d_base_v013_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_63d_base_v014_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_63d_base_v015_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_126d_base_v016_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_126d_base_v017_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_126d_base_v018_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_189d_base_v019_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_189d_base_v020_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_189d_base_v021_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_252d_base_v022_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_252d_base_v023_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_252d_base_v024_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_378d_base_v025_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_378d_base_v026_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_378d_base_v027_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_504d_base_v028_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_504d_base_v029_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_504d_base_v030_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_5d_base_v031_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_5d_base_v032_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_5d_base_v033_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_10d_base_v034_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_10d_base_v035_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_10d_base_v036_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_21d_base_v037_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_21d_base_v038_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_21d_base_v039_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_42d_base_v040_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_42d_base_v041_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_42d_base_v042_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_63d_base_v043_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_63d_base_v044_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_63d_base_v045_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_126d_base_v046_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_126d_base_v047_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_126d_base_v048_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_189d_base_v049_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_189d_base_v050_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_189d_base_v051_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_252d_base_v052_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_252d_base_v053_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_252d_base_v054_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_378d_base_v055_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_378d_base_v056_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_378d_base_v057_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdabs_504d_base_v058_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgabs_504d_base_v059_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispabs_504d_base_v060_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsqrt_5d_base_v061_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsqrt_5d_base_v062_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsqrt_5d_base_v063_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsqrt_10d_base_v064_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsqrt_10d_base_v065_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsqrt_10d_base_v066_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsqrt_21d_base_v067_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsqrt_21d_base_v068_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsqrt_21d_base_v069_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsqrt_42d_base_v070_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsqrt_42d_base_v071_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsqrt_42d_base_v072_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsqrt_63d_base_v073_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsqrt_63d_base_v074_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsqrt_63d_base_v075_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f089nib_f089_net_insider_buying_proxy_shd_5d_base_v001_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_5d_base_v002_signal,
    f089nib_f089_net_insider_buying_proxy_isp_5d_base_v003_signal,
    f089nib_f089_net_insider_buying_proxy_shd_10d_base_v004_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_10d_base_v005_signal,
    f089nib_f089_net_insider_buying_proxy_isp_10d_base_v006_signal,
    f089nib_f089_net_insider_buying_proxy_shd_21d_base_v007_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_21d_base_v008_signal,
    f089nib_f089_net_insider_buying_proxy_isp_21d_base_v009_signal,
    f089nib_f089_net_insider_buying_proxy_shd_42d_base_v010_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_42d_base_v011_signal,
    f089nib_f089_net_insider_buying_proxy_isp_42d_base_v012_signal,
    f089nib_f089_net_insider_buying_proxy_shd_63d_base_v013_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_63d_base_v014_signal,
    f089nib_f089_net_insider_buying_proxy_isp_63d_base_v015_signal,
    f089nib_f089_net_insider_buying_proxy_shd_126d_base_v016_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_126d_base_v017_signal,
    f089nib_f089_net_insider_buying_proxy_isp_126d_base_v018_signal,
    f089nib_f089_net_insider_buying_proxy_shd_189d_base_v019_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_189d_base_v020_signal,
    f089nib_f089_net_insider_buying_proxy_isp_189d_base_v021_signal,
    f089nib_f089_net_insider_buying_proxy_shd_252d_base_v022_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_252d_base_v023_signal,
    f089nib_f089_net_insider_buying_proxy_isp_252d_base_v024_signal,
    f089nib_f089_net_insider_buying_proxy_shd_378d_base_v025_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_378d_base_v026_signal,
    f089nib_f089_net_insider_buying_proxy_isp_378d_base_v027_signal,
    f089nib_f089_net_insider_buying_proxy_shd_504d_base_v028_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_504d_base_v029_signal,
    f089nib_f089_net_insider_buying_proxy_isp_504d_base_v030_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_5d_base_v031_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_5d_base_v032_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_5d_base_v033_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_10d_base_v034_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_10d_base_v035_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_10d_base_v036_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_21d_base_v037_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_21d_base_v038_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_21d_base_v039_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_42d_base_v040_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_42d_base_v041_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_42d_base_v042_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_63d_base_v043_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_63d_base_v044_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_63d_base_v045_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_126d_base_v046_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_126d_base_v047_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_126d_base_v048_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_189d_base_v049_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_189d_base_v050_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_189d_base_v051_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_252d_base_v052_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_252d_base_v053_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_252d_base_v054_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_378d_base_v055_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_378d_base_v056_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_378d_base_v057_signal,
    f089nib_f089_net_insider_buying_proxy_shdabs_504d_base_v058_signal,
    f089nib_f089_net_insider_buying_proxy_rtgabs_504d_base_v059_signal,
    f089nib_f089_net_insider_buying_proxy_ispabs_504d_base_v060_signal,
    f089nib_f089_net_insider_buying_proxy_shdsqrt_5d_base_v061_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsqrt_5d_base_v062_signal,
    f089nib_f089_net_insider_buying_proxy_ispsqrt_5d_base_v063_signal,
    f089nib_f089_net_insider_buying_proxy_shdsqrt_10d_base_v064_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsqrt_10d_base_v065_signal,
    f089nib_f089_net_insider_buying_proxy_ispsqrt_10d_base_v066_signal,
    f089nib_f089_net_insider_buying_proxy_shdsqrt_21d_base_v067_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsqrt_21d_base_v068_signal,
    f089nib_f089_net_insider_buying_proxy_ispsqrt_21d_base_v069_signal,
    f089nib_f089_net_insider_buying_proxy_shdsqrt_42d_base_v070_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsqrt_42d_base_v071_signal,
    f089nib_f089_net_insider_buying_proxy_ispsqrt_42d_base_v072_signal,
    f089nib_f089_net_insider_buying_proxy_shdsqrt_63d_base_v073_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsqrt_63d_base_v074_signal,
    f089nib_f089_net_insider_buying_proxy_ispsqrt_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F089_NET_INSIDER_BUYING_PROXY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    retearn = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")

    cols = {"sharesbas": sharesbas, "closeadj": closeadj, "retearn": retearn}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f089_share_decline", "_f089_retained_growth", "_f089_insider_signal_proxy",)
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
    print(f"OK f089_net_insider_buying_proxy_base_001_075_claude: {n_features} features pass")
