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
def _f089_share_decline(sharesbas, w):
    return -(sharesbas.diff(periods=w) / sharesbas.abs().shift(w).replace(0, np.nan))


def _f089_retained_growth(retearn, w):
    return retearn.diff(periods=w) / retearn.abs().shift(w).replace(0, np.nan)


def _f089_insider_signal_proxy(sharesbas, retearn, w):
    sd = -(sharesbas.diff(periods=w) / sharesbas.abs().shift(w).replace(0, np.nan))
    rg = retearn.diff(periods=w) / retearn.abs().shift(w).replace(0, np.nan)
    return sd + rg

def f089nib_f089_net_insider_buying_proxy_shd_5d_slope_v001_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_5d_slope_v002_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_5d_slope_v003_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_10d_slope_v004_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_10d_slope_v005_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_10d_slope_v006_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_21d_slope_v007_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_21d_slope_v008_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_21d_slope_v009_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_42d_slope_v010_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_42d_slope_v011_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_42d_slope_v012_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_63d_slope_v013_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_63d_slope_v014_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_63d_slope_v015_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_126d_slope_v016_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_126d_slope_v017_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_126d_slope_v018_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_189d_slope_v019_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_189d_slope_v020_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_189d_slope_v021_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_252d_slope_v022_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_252d_slope_v023_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_252d_slope_v024_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_378d_slope_v025_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_378d_slope_v026_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_378d_slope_v027_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_504d_slope_v028_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_504d_slope_v029_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_504d_slope_v030_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_5d_slope_v031_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_5d_slope_v032_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_5d_slope_v033_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_10d_slope_v034_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_10d_slope_v035_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_10d_slope_v036_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_21d_slope_v037_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_21d_slope_v038_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_21d_slope_v039_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_42d_slope_v040_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_42d_slope_v041_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_42d_slope_v042_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_63d_slope_v043_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_63d_slope_v044_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_63d_slope_v045_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_126d_slope_v046_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_126d_slope_v047_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_126d_slope_v048_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_189d_slope_v049_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_189d_slope_v050_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_189d_slope_v051_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_252d_slope_v052_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_252d_slope_v053_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_252d_slope_v054_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_378d_slope_v055_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_378d_slope_v056_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_378d_slope_v057_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_504d_slope_v058_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_504d_slope_v059_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_504d_slope_v060_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_5d_slope_v061_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_5d_slope_v062_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_5d_slope_v063_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_10d_slope_v064_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_10d_slope_v065_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_10d_slope_v066_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_21d_slope_v067_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_21d_slope_v068_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_21d_slope_v069_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_42d_slope_v070_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_42d_slope_v071_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_42d_slope_v072_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_63d_slope_v073_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_63d_slope_v074_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_63d_slope_v075_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_126d_slope_v076_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_126d_slope_v077_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_126d_slope_v078_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_189d_slope_v079_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_189d_slope_v080_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_189d_slope_v081_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_252d_slope_v082_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_252d_slope_v083_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_252d_slope_v084_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_378d_slope_v085_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_378d_slope_v086_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_378d_slope_v087_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shd_504d_slope_v088_signal(sharesbas, closeadj):
    base = _f089_share_decline(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtg_504d_slope_v089_signal(retearn, closeadj):
    base = _f089_retained_growth(retearn, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_isp_504d_slope_v090_signal(sharesbas, retearn, closeadj):
    base = _f089_insider_signal_proxy(sharesbas, retearn, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_5d_slope_v091_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 5)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_5d_slope_v092_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 5)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_5d_slope_v093_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 5)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_10d_slope_v094_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 10)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_10d_slope_v095_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 10)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_10d_slope_v096_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 10)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_21d_slope_v097_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 21)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_21d_slope_v098_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 21)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_21d_slope_v099_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 21)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_42d_slope_v100_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 42)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_42d_slope_v101_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 42)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_42d_slope_v102_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 42)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_63d_slope_v103_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 63)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_63d_slope_v104_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 63)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_63d_slope_v105_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 63)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_126d_slope_v106_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 126)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_126d_slope_v107_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 126)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_126d_slope_v108_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 126)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_189d_slope_v109_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 189)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_189d_slope_v110_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 189)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_189d_slope_v111_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 189)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_252d_slope_v112_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 252)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_252d_slope_v113_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 252)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_252d_slope_v114_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 252)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_378d_slope_v115_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 378)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_378d_slope_v116_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 378)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_378d_slope_v117_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 378)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdsq_504d_slope_v118_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 504)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgsq_504d_slope_v119_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 504)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispsq_504d_slope_v120_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 504)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_5d_slope_v121_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_5d_slope_v122_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_5d_slope_v123_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_10d_slope_v124_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 10)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_10d_slope_v125_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 10)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_10d_slope_v126_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 10)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_21d_slope_v127_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 21)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_21d_slope_v128_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 21)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_21d_slope_v129_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 21)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_42d_slope_v130_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 42)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_42d_slope_v131_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 42)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_42d_slope_v132_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 42)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_63d_slope_v133_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 63)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_63d_slope_v134_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 63)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_63d_slope_v135_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 63)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_126d_slope_v136_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 126)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_126d_slope_v137_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 126)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_126d_slope_v138_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 126)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_189d_slope_v139_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 189)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_189d_slope_v140_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 189)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_189d_slope_v141_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 189)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_252d_slope_v142_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 252)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_252d_slope_v143_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 252)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_252d_slope_v144_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 252)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_378d_slope_v145_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 378)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_378d_slope_v146_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 378)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_378d_slope_v147_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 378)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_shdab_504d_slope_v148_signal(sharesbas, closeadj):
    base = (_f089_share_decline(sharesbas, 504)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_rtgab_504d_slope_v149_signal(retearn, closeadj):
    base = (_f089_retained_growth(retearn, 504)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f089nib_f089_net_insider_buying_proxy_ispab_504d_slope_v150_signal(sharesbas, retearn, closeadj):
    base = (_f089_insider_signal_proxy(sharesbas, retearn, 504)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f089nib_f089_net_insider_buying_proxy_shd_5d_slope_v001_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_5d_slope_v002_signal,
    f089nib_f089_net_insider_buying_proxy_isp_5d_slope_v003_signal,
    f089nib_f089_net_insider_buying_proxy_shd_10d_slope_v004_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_10d_slope_v005_signal,
    f089nib_f089_net_insider_buying_proxy_isp_10d_slope_v006_signal,
    f089nib_f089_net_insider_buying_proxy_shd_21d_slope_v007_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_21d_slope_v008_signal,
    f089nib_f089_net_insider_buying_proxy_isp_21d_slope_v009_signal,
    f089nib_f089_net_insider_buying_proxy_shd_42d_slope_v010_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_42d_slope_v011_signal,
    f089nib_f089_net_insider_buying_proxy_isp_42d_slope_v012_signal,
    f089nib_f089_net_insider_buying_proxy_shd_63d_slope_v013_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_63d_slope_v014_signal,
    f089nib_f089_net_insider_buying_proxy_isp_63d_slope_v015_signal,
    f089nib_f089_net_insider_buying_proxy_shd_126d_slope_v016_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_126d_slope_v017_signal,
    f089nib_f089_net_insider_buying_proxy_isp_126d_slope_v018_signal,
    f089nib_f089_net_insider_buying_proxy_shd_189d_slope_v019_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_189d_slope_v020_signal,
    f089nib_f089_net_insider_buying_proxy_isp_189d_slope_v021_signal,
    f089nib_f089_net_insider_buying_proxy_shd_252d_slope_v022_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_252d_slope_v023_signal,
    f089nib_f089_net_insider_buying_proxy_isp_252d_slope_v024_signal,
    f089nib_f089_net_insider_buying_proxy_shd_378d_slope_v025_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_378d_slope_v026_signal,
    f089nib_f089_net_insider_buying_proxy_isp_378d_slope_v027_signal,
    f089nib_f089_net_insider_buying_proxy_shd_504d_slope_v028_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_504d_slope_v029_signal,
    f089nib_f089_net_insider_buying_proxy_isp_504d_slope_v030_signal,
    f089nib_f089_net_insider_buying_proxy_shd_5d_slope_v031_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_5d_slope_v032_signal,
    f089nib_f089_net_insider_buying_proxy_isp_5d_slope_v033_signal,
    f089nib_f089_net_insider_buying_proxy_shd_10d_slope_v034_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_10d_slope_v035_signal,
    f089nib_f089_net_insider_buying_proxy_isp_10d_slope_v036_signal,
    f089nib_f089_net_insider_buying_proxy_shd_21d_slope_v037_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_21d_slope_v038_signal,
    f089nib_f089_net_insider_buying_proxy_isp_21d_slope_v039_signal,
    f089nib_f089_net_insider_buying_proxy_shd_42d_slope_v040_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_42d_slope_v041_signal,
    f089nib_f089_net_insider_buying_proxy_isp_42d_slope_v042_signal,
    f089nib_f089_net_insider_buying_proxy_shd_63d_slope_v043_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_63d_slope_v044_signal,
    f089nib_f089_net_insider_buying_proxy_isp_63d_slope_v045_signal,
    f089nib_f089_net_insider_buying_proxy_shd_126d_slope_v046_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_126d_slope_v047_signal,
    f089nib_f089_net_insider_buying_proxy_isp_126d_slope_v048_signal,
    f089nib_f089_net_insider_buying_proxy_shd_189d_slope_v049_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_189d_slope_v050_signal,
    f089nib_f089_net_insider_buying_proxy_isp_189d_slope_v051_signal,
    f089nib_f089_net_insider_buying_proxy_shd_252d_slope_v052_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_252d_slope_v053_signal,
    f089nib_f089_net_insider_buying_proxy_isp_252d_slope_v054_signal,
    f089nib_f089_net_insider_buying_proxy_shd_378d_slope_v055_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_378d_slope_v056_signal,
    f089nib_f089_net_insider_buying_proxy_isp_378d_slope_v057_signal,
    f089nib_f089_net_insider_buying_proxy_shd_504d_slope_v058_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_504d_slope_v059_signal,
    f089nib_f089_net_insider_buying_proxy_isp_504d_slope_v060_signal,
    f089nib_f089_net_insider_buying_proxy_shd_5d_slope_v061_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_5d_slope_v062_signal,
    f089nib_f089_net_insider_buying_proxy_isp_5d_slope_v063_signal,
    f089nib_f089_net_insider_buying_proxy_shd_10d_slope_v064_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_10d_slope_v065_signal,
    f089nib_f089_net_insider_buying_proxy_isp_10d_slope_v066_signal,
    f089nib_f089_net_insider_buying_proxy_shd_21d_slope_v067_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_21d_slope_v068_signal,
    f089nib_f089_net_insider_buying_proxy_isp_21d_slope_v069_signal,
    f089nib_f089_net_insider_buying_proxy_shd_42d_slope_v070_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_42d_slope_v071_signal,
    f089nib_f089_net_insider_buying_proxy_isp_42d_slope_v072_signal,
    f089nib_f089_net_insider_buying_proxy_shd_63d_slope_v073_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_63d_slope_v074_signal,
    f089nib_f089_net_insider_buying_proxy_isp_63d_slope_v075_signal,
    f089nib_f089_net_insider_buying_proxy_shd_126d_slope_v076_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_126d_slope_v077_signal,
    f089nib_f089_net_insider_buying_proxy_isp_126d_slope_v078_signal,
    f089nib_f089_net_insider_buying_proxy_shd_189d_slope_v079_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_189d_slope_v080_signal,
    f089nib_f089_net_insider_buying_proxy_isp_189d_slope_v081_signal,
    f089nib_f089_net_insider_buying_proxy_shd_252d_slope_v082_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_252d_slope_v083_signal,
    f089nib_f089_net_insider_buying_proxy_isp_252d_slope_v084_signal,
    f089nib_f089_net_insider_buying_proxy_shd_378d_slope_v085_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_378d_slope_v086_signal,
    f089nib_f089_net_insider_buying_proxy_isp_378d_slope_v087_signal,
    f089nib_f089_net_insider_buying_proxy_shd_504d_slope_v088_signal,
    f089nib_f089_net_insider_buying_proxy_rtg_504d_slope_v089_signal,
    f089nib_f089_net_insider_buying_proxy_isp_504d_slope_v090_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_5d_slope_v091_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_5d_slope_v092_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_5d_slope_v093_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_10d_slope_v094_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_10d_slope_v095_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_10d_slope_v096_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_21d_slope_v097_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_21d_slope_v098_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_21d_slope_v099_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_42d_slope_v100_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_42d_slope_v101_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_42d_slope_v102_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_63d_slope_v103_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_63d_slope_v104_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_63d_slope_v105_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_126d_slope_v106_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_126d_slope_v107_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_126d_slope_v108_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_189d_slope_v109_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_189d_slope_v110_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_189d_slope_v111_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_252d_slope_v112_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_252d_slope_v113_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_252d_slope_v114_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_378d_slope_v115_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_378d_slope_v116_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_378d_slope_v117_signal,
    f089nib_f089_net_insider_buying_proxy_shdsq_504d_slope_v118_signal,
    f089nib_f089_net_insider_buying_proxy_rtgsq_504d_slope_v119_signal,
    f089nib_f089_net_insider_buying_proxy_ispsq_504d_slope_v120_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_5d_slope_v121_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_5d_slope_v122_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_5d_slope_v123_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_10d_slope_v124_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_10d_slope_v125_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_10d_slope_v126_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_21d_slope_v127_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_21d_slope_v128_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_21d_slope_v129_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_42d_slope_v130_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_42d_slope_v131_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_42d_slope_v132_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_63d_slope_v133_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_63d_slope_v134_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_63d_slope_v135_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_126d_slope_v136_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_126d_slope_v137_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_126d_slope_v138_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_189d_slope_v139_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_189d_slope_v140_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_189d_slope_v141_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_252d_slope_v142_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_252d_slope_v143_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_252d_slope_v144_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_378d_slope_v145_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_378d_slope_v146_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_378d_slope_v147_signal,
    f089nib_f089_net_insider_buying_proxy_shdab_504d_slope_v148_signal,
    f089nib_f089_net_insider_buying_proxy_rtgab_504d_slope_v149_signal,
    f089nib_f089_net_insider_buying_proxy_ispab_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F089_NET_INSIDER_BUYING_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f089_net_insider_buying_proxy_2nd_derivatives_001_150_claude: {n_features} features pass")
