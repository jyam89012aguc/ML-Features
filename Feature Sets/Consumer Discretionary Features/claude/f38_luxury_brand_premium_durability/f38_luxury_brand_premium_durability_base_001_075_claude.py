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


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_5d_base_v001_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_10d_base_v002_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_base_v003_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_42d_base_v004_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_base_v005_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_base_v006_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_189d_base_v007_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_base_v008_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_base_v009_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloor_504d_base_v010_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_5d_base_v011_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_10d_base_v012_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_21d_base_v013_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_42d_base_v014_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_63d_base_v015_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_126d_base_v016_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_189d_base_v017_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_252d_base_v018_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_378d_base_v019_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prempers_504d_base_v020_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_base_v021_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_42d_base_v022_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_base_v023_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_base_v024_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_189d_base_v025_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_base_v026_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_base_v027_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_504d_base_v028_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_100d_base_v029_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 100)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdur_150d_base_v030_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 150)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_21d_base_v031_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 21)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_63d_base_v032_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_126d_base_v033_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 126)
    result = d.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_189d_base_v034_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 189)
    result = d.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_252d_base_v035_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 252)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_504d_base_v036_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 504)
    result = d.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prepersdiff_21d_base_v037_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 21)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prepersdiff_63d_base_v038_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prepersdiff_126d_base_v039_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 126)
    result = d.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prepersdiff_189d_base_v040_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 189)
    result = d.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prepersdiff_252d_base_v041_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 252)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_prepersdiff_504d_base_v042_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 504)
    result = d.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_base_v043_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 21)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_base_v044_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_base_v045_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 126)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_189d_base_v046_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 189)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_base_v047_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 252)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_504d_base_v048_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 504)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurema_21d_base_v049_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurema_63d_base_v050_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurema_126d_base_v051_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurema_189d_base_v052_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _ema(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurema_252d_base_v053_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurema_504d_base_v054_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _ema(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_63d_base_v055_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_126d_base_v056_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_189d_base_v057_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_252d_base_v058_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_378d_base_v059_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_504d_base_v060_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preprxrev_21d_base_v061_signal(ebitdamargin, revenue, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 21)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preprxrev_63d_base_v062_signal(ebitdamargin, revenue, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preprxrev_126d_base_v063_signal(ebitdamargin, revenue, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 126)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preprxrev_189d_base_v064_signal(ebitdamargin, revenue, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 189)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preprxrev_252d_base_v065_signal(ebitdamargin, revenue, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 252)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preprxrev_504d_base_v066_signal(ebitdamargin, revenue, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 504)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurz_63d_base_v067_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurz_252d_base_v068_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloormean_189d_base_v069_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = _mean(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorstd_252d_base_v070_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxnm_126d_base_v071_signal(ebitdamargin, netmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 126)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxnm_252d_base_v072_signal(ebitdamargin, netmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 252)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxnm_252d_base_v073_signal(grossmargin, ebitdamargin, revenue, netmargin, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = d * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxgm_252d_base_v074_signal(grossmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurmean_252d_base_v075_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = _mean(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_5d_base_v001_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_10d_base_v002_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_21d_base_v003_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_42d_base_v004_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_63d_base_v005_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_126d_base_v006_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_189d_base_v007_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_252d_base_v008_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_378d_base_v009_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloor_504d_base_v010_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_5d_base_v011_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_10d_base_v012_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_21d_base_v013_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_42d_base_v014_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_63d_base_v015_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_126d_base_v016_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_189d_base_v017_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_252d_base_v018_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_378d_base_v019_signal,
    f38lbp_f38_luxury_brand_premium_durability_prempers_504d_base_v020_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_21d_base_v021_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_42d_base_v022_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_63d_base_v023_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_126d_base_v024_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_189d_base_v025_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_252d_base_v026_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_378d_base_v027_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_504d_base_v028_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_100d_base_v029_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdur_150d_base_v030_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_21d_base_v031_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_63d_base_v032_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_126d_base_v033_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_189d_base_v034_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_252d_base_v035_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorchg_504d_base_v036_signal,
    f38lbp_f38_luxury_brand_premium_durability_prepersdiff_21d_base_v037_signal,
    f38lbp_f38_luxury_brand_premium_durability_prepersdiff_63d_base_v038_signal,
    f38lbp_f38_luxury_brand_premium_durability_prepersdiff_126d_base_v039_signal,
    f38lbp_f38_luxury_brand_premium_durability_prepersdiff_189d_base_v040_signal,
    f38lbp_f38_luxury_brand_premium_durability_prepersdiff_252d_base_v041_signal,
    f38lbp_f38_luxury_brand_premium_durability_prepersdiff_504d_base_v042_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_21d_base_v043_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_63d_base_v044_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_126d_base_v045_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_189d_base_v046_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_252d_base_v047_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnm_504d_base_v048_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurema_21d_base_v049_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurema_63d_base_v050_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurema_126d_base_v051_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurema_189d_base_v052_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurema_252d_base_v053_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurema_504d_base_v054_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_63d_base_v055_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_126d_base_v056_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_189d_base_v057_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_252d_base_v058_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_378d_base_v059_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorz_504d_base_v060_signal,
    f38lbp_f38_luxury_brand_premium_durability_preprxrev_21d_base_v061_signal,
    f38lbp_f38_luxury_brand_premium_durability_preprxrev_63d_base_v062_signal,
    f38lbp_f38_luxury_brand_premium_durability_preprxrev_126d_base_v063_signal,
    f38lbp_f38_luxury_brand_premium_durability_preprxrev_189d_base_v064_signal,
    f38lbp_f38_luxury_brand_premium_durability_preprxrev_252d_base_v065_signal,
    f38lbp_f38_luxury_brand_premium_durability_preprxrev_504d_base_v066_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurz_63d_base_v067_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurz_252d_base_v068_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloormean_189d_base_v069_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorstd_252d_base_v070_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxnm_126d_base_v071_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxnm_252d_base_v072_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxnm_252d_base_v073_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxgm_252d_base_v074_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurmean_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_LUXURY_BRAND_PREMIUM_DURABILITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f38_luxury_brand_premium_durability_001_075_claude: {n_features} features pass")
