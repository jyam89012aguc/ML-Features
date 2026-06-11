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
def _f093_volume_breadth(volume, w):
    return _mean(volume, w) / _mean(volume, w * 2).replace(0, np.nan)


def _f093_share_count_stable(sharesbas, w):
    return 1.0 - _std(sharesbas.pct_change(), w).fillna(0)


def _f093_breadth_proxy(volume, sharesbas, w):
    turnover = volume / sharesbas.replace(0, np.nan)
    return _mean(turnover, w)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_xclose_m1_slope_v001_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_base_m2_slope_v002_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_xclose21_m5_slope_v003_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_xclose63_m10_slope_v004_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_xclose126_m100_slope_v005_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_xclose_m1_slope_v006_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_base_m2_slope_v007_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_xclose21_m5_slope_v008_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_xclose63_m10_slope_v009_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_xclose126_m100_slope_v010_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_xclose_m1_slope_v011_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_base_m2_slope_v012_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_xclose21_m5_slope_v013_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_xclose63_m10_slope_v014_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_xclose126_m100_slope_v015_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_xclose_m1_slope_v016_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_base_m2_slope_v017_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_xclose21_m5_slope_v018_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_xclose63_m10_slope_v019_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_xclose126_m100_slope_v020_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_xclose_m1_slope_v021_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_base_m2_slope_v022_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_xclose21_m5_slope_v023_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_xclose63_m10_slope_v024_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_xclose126_m100_slope_v025_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_xclose_m1_slope_v026_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_base_m2_slope_v027_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_xclose21_m5_slope_v028_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_xclose63_m10_slope_v029_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_xclose126_m100_slope_v030_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_xclose_m1_slope_v031_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_base_m2_slope_v032_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_xclose21_m5_slope_v033_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_xclose63_m10_slope_v034_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_xclose126_m100_slope_v035_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_xclose_m1_slope_v036_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_base_m2_slope_v037_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_xclose21_m5_slope_v038_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_xclose63_m10_slope_v039_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_xclose126_m100_slope_v040_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_xclose_m1_slope_v041_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_base_m2_slope_v042_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_xclose21_m5_slope_v043_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_xclose63_m10_slope_v044_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_xclose126_m100_slope_v045_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_xclose_m1_slope_v046_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_base_m2_slope_v047_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_xclose21_m5_slope_v048_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_xclose63_m10_slope_v049_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_xclose126_m100_slope_v050_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_xclose_m1_slope_v051_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_base_m2_slope_v052_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_xclose21_m5_slope_v053_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_xclose63_m10_slope_v054_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_xclose126_m100_slope_v055_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_xclose_m1_slope_v056_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_base_m2_slope_v057_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_xclose21_m5_slope_v058_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_xclose63_m10_slope_v059_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_xclose126_m100_slope_v060_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_xclose_m1_slope_v061_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_base_m2_slope_v062_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_xclose21_m5_slope_v063_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_xclose63_m10_slope_v064_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_xclose126_m100_slope_v065_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_xclose_m1_slope_v066_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_base_m2_slope_v067_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_xclose21_m5_slope_v068_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_xclose63_m10_slope_v069_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_xclose126_m100_slope_v070_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_xclose_m1_slope_v071_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_base_m2_slope_v072_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_xclose21_m5_slope_v073_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_xclose63_m10_slope_v074_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_xclose126_m100_slope_v075_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_xclose_m1_slope_v076_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_base_m2_slope_v077_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_xclose21_m5_slope_v078_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_xclose63_m10_slope_v079_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_xclose126_m100_slope_v080_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_xclose_m1_slope_v081_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_base_m2_slope_v082_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_xclose21_m5_slope_v083_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_xclose63_m10_slope_v084_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_xclose126_m100_slope_v085_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_xclose_m1_slope_v086_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_base_m2_slope_v087_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_xclose21_m5_slope_v088_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_xclose63_m10_slope_v089_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_xclose126_m100_slope_v090_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_xclose_m1_slope_v091_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_base_m2_slope_v092_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_xclose21_m5_slope_v093_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_xclose63_m10_slope_v094_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_xclose126_m100_slope_v095_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_xclose_m1_slope_v096_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_base_m2_slope_v097_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_xclose21_m5_slope_v098_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_xclose63_m10_slope_v099_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_xclose126_m100_slope_v100_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_xclose_m1_slope_v101_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_base_m2_slope_v102_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_xclose21_m5_slope_v103_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_xclose63_m10_slope_v104_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_xclose126_m100_slope_v105_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_xclose_m1_slope_v106_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_base_m2_slope_v107_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_xclose21_m5_slope_v108_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_xclose63_m10_slope_v109_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_xclose126_m100_slope_v110_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 5)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_xclose_m1_slope_v111_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_base_m2_slope_v112_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_xclose21_m5_slope_v113_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_xclose63_m10_slope_v114_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_xclose126_m100_slope_v115_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_xclose_m1_slope_v116_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_base_m2_slope_v117_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_xclose21_m5_slope_v118_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_xclose63_m10_slope_v119_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_xclose126_m100_slope_v120_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 10)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_xclose_m1_slope_v121_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_base_m2_slope_v122_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_xclose21_m5_slope_v123_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_xclose63_m10_slope_v124_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_xclose126_m100_slope_v125_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_xclose_m1_slope_v126_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_base_m2_slope_v127_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_xclose21_m5_slope_v128_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_xclose63_m10_slope_v129_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_xclose126_m100_slope_v130_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 21)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_xclose_m1_slope_v131_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_base_m2_slope_v132_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_xclose21_m5_slope_v133_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_xclose63_m10_slope_v134_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_xclose126_m100_slope_v135_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_xclose_m1_slope_v136_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_base_m2_slope_v137_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_xclose21_m5_slope_v138_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_xclose63_m10_slope_v139_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_xclose126_m100_slope_v140_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 42)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_xclose_m1_slope_v141_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_base_m2_slope_v142_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_xclose21_m5_slope_v143_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_xclose63_m10_slope_v144_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_xclose126_m100_slope_v145_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_pct(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_xclose_m1_slope_v146_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_base_m2_slope_v147_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv  * 2.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_xclose21_m5_slope_v148_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 21) * 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_xclose63_m10_slope_v149_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 63) * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_xclose126_m100_slope_v150_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    deriv = _slope_diff_norm(base, 63)
    result = deriv * _mean(closeadj, 126) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_xclose_m1_slope_v001_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_base_m2_slope_v002_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_xclose21_m5_slope_v003_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_xclose63_m10_slope_v004_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_5d_xclose126_m100_slope_v005_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_xclose_m1_slope_v006_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_base_m2_slope_v007_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_xclose21_m5_slope_v008_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_xclose63_m10_slope_v009_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_5d_xclose126_m100_slope_v010_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_xclose_m1_slope_v011_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_base_m2_slope_v012_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_xclose21_m5_slope_v013_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_xclose63_m10_slope_v014_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_10d_xclose126_m100_slope_v015_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_xclose_m1_slope_v016_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_base_m2_slope_v017_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_xclose21_m5_slope_v018_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_xclose63_m10_slope_v019_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_10d_xclose126_m100_slope_v020_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_xclose_m1_slope_v021_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_base_m2_slope_v022_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_xclose21_m5_slope_v023_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_xclose63_m10_slope_v024_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_21d_xclose126_m100_slope_v025_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_xclose_m1_slope_v026_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_base_m2_slope_v027_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_xclose21_m5_slope_v028_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_xclose63_m10_slope_v029_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_21d_xclose126_m100_slope_v030_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_xclose_m1_slope_v031_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_base_m2_slope_v032_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_xclose21_m5_slope_v033_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_xclose63_m10_slope_v034_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_42d_xclose126_m100_slope_v035_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_xclose_m1_slope_v036_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_base_m2_slope_v037_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_xclose21_m5_slope_v038_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_xclose63_m10_slope_v039_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_42d_xclose126_m100_slope_v040_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_xclose_m1_slope_v041_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_base_m2_slope_v042_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_xclose21_m5_slope_v043_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_xclose63_m10_slope_v044_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slpct_63d_xclose126_m100_slope_v045_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_xclose_m1_slope_v046_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_base_m2_slope_v047_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_xclose21_m5_slope_v048_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_xclose63_m10_slope_v049_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volumebreadth_5d_slnorm_63d_xclose126_m100_slope_v050_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_xclose_m1_slope_v051_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_base_m2_slope_v052_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_xclose21_m5_slope_v053_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_xclose63_m10_slope_v054_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_5d_xclose126_m100_slope_v055_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_xclose_m1_slope_v056_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_base_m2_slope_v057_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_xclose21_m5_slope_v058_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_xclose63_m10_slope_v059_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_5d_xclose126_m100_slope_v060_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_xclose_m1_slope_v061_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_base_m2_slope_v062_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_xclose21_m5_slope_v063_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_xclose63_m10_slope_v064_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_10d_xclose126_m100_slope_v065_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_xclose_m1_slope_v066_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_base_m2_slope_v067_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_xclose21_m5_slope_v068_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_xclose63_m10_slope_v069_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_10d_xclose126_m100_slope_v070_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_xclose_m1_slope_v071_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_base_m2_slope_v072_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_xclose21_m5_slope_v073_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_xclose63_m10_slope_v074_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_21d_xclose126_m100_slope_v075_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_xclose_m1_slope_v076_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_base_m2_slope_v077_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_xclose21_m5_slope_v078_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_xclose63_m10_slope_v079_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_21d_xclose126_m100_slope_v080_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_xclose_m1_slope_v081_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_base_m2_slope_v082_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_xclose21_m5_slope_v083_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_xclose63_m10_slope_v084_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_42d_xclose126_m100_slope_v085_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_xclose_m1_slope_v086_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_base_m2_slope_v087_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_xclose21_m5_slope_v088_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_xclose63_m10_slope_v089_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_42d_xclose126_m100_slope_v090_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_xclose_m1_slope_v091_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_base_m2_slope_v092_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_xclose21_m5_slope_v093_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_xclose63_m10_slope_v094_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slpct_63d_xclose126_m100_slope_v095_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_xclose_m1_slope_v096_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_base_m2_slope_v097_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_xclose21_m5_slope_v098_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_xclose63_m10_slope_v099_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_sharecountstable_5d_slnorm_63d_xclose126_m100_slope_v100_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_xclose_m1_slope_v101_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_base_m2_slope_v102_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_xclose21_m5_slope_v103_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_xclose63_m10_slope_v104_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_5d_xclose126_m100_slope_v105_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_xclose_m1_slope_v106_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_base_m2_slope_v107_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_xclose21_m5_slope_v108_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_xclose63_m10_slope_v109_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_5d_xclose126_m100_slope_v110_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_xclose_m1_slope_v111_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_base_m2_slope_v112_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_xclose21_m5_slope_v113_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_xclose63_m10_slope_v114_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_10d_xclose126_m100_slope_v115_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_xclose_m1_slope_v116_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_base_m2_slope_v117_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_xclose21_m5_slope_v118_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_xclose63_m10_slope_v119_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_10d_xclose126_m100_slope_v120_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_xclose_m1_slope_v121_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_base_m2_slope_v122_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_xclose21_m5_slope_v123_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_xclose63_m10_slope_v124_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_21d_xclose126_m100_slope_v125_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_xclose_m1_slope_v126_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_base_m2_slope_v127_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_xclose21_m5_slope_v128_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_xclose63_m10_slope_v129_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_21d_xclose126_m100_slope_v130_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_xclose_m1_slope_v131_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_base_m2_slope_v132_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_xclose21_m5_slope_v133_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_xclose63_m10_slope_v134_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_42d_xclose126_m100_slope_v135_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_xclose_m1_slope_v136_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_base_m2_slope_v137_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_xclose21_m5_slope_v138_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_xclose63_m10_slope_v139_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_42d_xclose126_m100_slope_v140_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_xclose_m1_slope_v141_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_base_m2_slope_v142_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_xclose21_m5_slope_v143_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_xclose63_m10_slope_v144_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slpct_63d_xclose126_m100_slope_v145_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_xclose_m1_slope_v146_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_base_m2_slope_v147_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_xclose21_m5_slope_v148_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_xclose63_m10_slope_v149_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_breadthproxy_5d_slnorm_63d_xclose126_m100_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F093_OWNERSHIP_BREADTH_EXPANSION_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {
        "closeadj": closeadj, "volume": volume, "sharesbas": sharesbas,
        "marketcap": marketcap, "dps": dps, "payoutratio": payoutratio,
        "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f093_volume_breadth", "_f093_share_count_stable", "_f093_breadth_proxy")
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
    print(f"OK f093_ownership_breadth_expansion_proxy_2nd_derivatives_001_150_claude: {n_features} features pass")
