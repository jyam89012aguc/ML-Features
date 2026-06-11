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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f38_margin_floor(grossmargin, w):
    # Rolling minimum of grossmargin -- the "floor"
    return grossmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f38_premium_persistence(ebitdamargin, w):
    # Mean margin / std margin (signal-to-noise of margin)
    m = _mean(ebitdamargin, w)
    s = _std(ebitdamargin, w)
    return m / s.replace(0, np.nan)


def _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, w):
    # Margin level x (1 / revenue volatility)
    mean_gm = _mean(grossmargin, w)
    mean_em = _mean(ebitdamargin, w)
    rev_vol = _std(revenue.pct_change(), w)
    return (mean_gm + mean_em) / rev_vol.replace(0, np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v001_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v002_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v003_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v004_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v005_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v006_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v007_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v008_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v009_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v010_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v011_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v012_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v013_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v014_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v015_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v016_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v017_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v018_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v019_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v020_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v021_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v022_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v023_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v024_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v025_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v026_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v027_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v028_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v029_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v030_signal(grossmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v031_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v032_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v033_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v034_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v035_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v036_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v037_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v038_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v039_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v040_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v041_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v042_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v043_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v044_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v045_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v046_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v047_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v048_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v049_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v050_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v051_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v052_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v053_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v054_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v055_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v056_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v057_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v058_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v059_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v060_signal(ebitdamargin, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v061_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v062_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v063_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v064_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v065_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v066_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v067_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v068_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v069_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v070_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v071_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v072_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v073_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v074_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v075_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v076_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v077_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v078_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 126)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v079_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v080_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v081_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v082_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v083_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v084_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v085_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v086_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v087_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v088_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 378)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v089_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 378)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v090_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 378)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v091_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21) * netmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v092_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21) * netmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v093_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21) * netmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v094_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21) * netmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v095_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21) * netmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v096_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 21) * netmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v097_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63) * netmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v098_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63) * netmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v099_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63) * netmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v100_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63) * netmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v101_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63) * netmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v102_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 63) * netmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v103_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126) * netmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v104_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126) * netmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v105_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126) * netmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v106_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126) * netmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v107_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126) * netmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v108_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 126) * netmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v109_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252) * netmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v110_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252) * netmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v111_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252) * netmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v112_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252) * netmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v113_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252) * netmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v114_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 252) * netmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v115_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378) * netmargin
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v116_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378) * netmargin
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v117_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378) * netmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v118_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378) * netmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v119_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378) * netmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v120_signal(grossmargin, netmargin, closeadj):
    base = _f38_margin_floor(grossmargin, 378) * netmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v121_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21) * (revenue / 1e9)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v122_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21) * (revenue / 1e9)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v123_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21) * (revenue / 1e9)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v124_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21) * (revenue / 1e9)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v125_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21) * (revenue / 1e9)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v126_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 21) * (revenue / 1e9)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v127_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63) * (revenue / 1e9)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v128_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63) * (revenue / 1e9)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v129_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63) * (revenue / 1e9)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v130_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63) * (revenue / 1e9)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v131_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63) * (revenue / 1e9)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v132_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 63) * (revenue / 1e9)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v133_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126) * (revenue / 1e9)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v134_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126) * (revenue / 1e9)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v135_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126) * (revenue / 1e9)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v136_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126) * (revenue / 1e9)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v137_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126) * (revenue / 1e9)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v138_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 126) * (revenue / 1e9)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v139_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252) * (revenue / 1e9)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v140_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252) * (revenue / 1e9)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v141_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252) * (revenue / 1e9)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v142_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252) * (revenue / 1e9)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v143_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252) * (revenue / 1e9)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v144_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 252) * (revenue / 1e9)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v145_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378) * (revenue / 1e9)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v146_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378) * (revenue / 1e9)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v147_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378) * (revenue / 1e9)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v148_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378) * (revenue / 1e9)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v149_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378) * (revenue / 1e9)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v150_signal(ebitdamargin, revenue, closeadj):
    base = _f38_premium_persistence(ebitdamargin, 378) * (revenue / 1e9)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v001_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v002_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v003_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v004_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v005_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_slope_v006_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v007_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v008_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v009_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v010_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v011_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_slope_v012_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v013_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v014_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v015_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v016_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v017_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_slope_v018_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v019_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v020_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v021_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v022_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v023_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_slope_v024_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v025_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v026_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v027_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v028_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v029_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_slope_v030_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v031_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v032_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v033_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v034_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v035_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_21d_slope_v036_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v037_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v038_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v039_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v040_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v041_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_63d_slope_v042_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v043_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v044_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v045_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v046_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v047_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_126d_slope_v048_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v049_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v050_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v051_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v052_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v053_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_252d_slope_v054_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v055_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v056_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v057_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v058_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v059_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_378d_slope_v060_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v061_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v062_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v063_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v064_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v065_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_slope_v066_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v067_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v068_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v069_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v070_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v071_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_slope_v072_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v073_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v074_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v075_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v076_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v077_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_slope_v078_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v079_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v080_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v081_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v082_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v083_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_slope_v084_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v085_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v086_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v087_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v088_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v089_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_slope_v090_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v091_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v092_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v093_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v094_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v095_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_slope_v096_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v097_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v098_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v099_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v100_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v101_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_slope_v102_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v103_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v104_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v105_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v106_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v107_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_slope_v108_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v109_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v110_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v111_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v112_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v113_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_slope_v114_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v115_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v116_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v117_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v118_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v119_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_378d_slope_v120_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v121_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v122_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v123_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v124_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v125_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_21d_slope_v126_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v127_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v128_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v129_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v130_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v131_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_63d_slope_v132_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v133_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v134_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v135_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v136_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v137_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_126d_slope_v138_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v139_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v140_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v141_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v142_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v143_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_252d_slope_v144_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v145_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v146_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v147_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v148_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v149_signal,
    f38lbp_f38_luxury_brand_premium_durability_perpxrev_378d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_LUXURY_BRAND_PREMIUM_DURABILITY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f38_margin_floor", "_f38_premium_persistence", "_f38_luxury_durability_score",)
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
    print(f"OK f38_luxury_brand_premium_durability_slope_001_150_claude: {n_features} features pass")
