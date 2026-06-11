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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f039_ev_to_mcap(ev, marketcap):
    return ev / marketcap.replace(0, np.nan).abs()


# 21d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slope_21d_2d_v001_signal(ev, closeadj):
    base = ev
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slope_63d_2d_v002_signal(ev, closeadj):
    base = ev
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slope_126d_2d_v003_signal(ev, closeadj):
    base = ev
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slope_252d_2d_v004_signal(ev, closeadj):
    base = ev
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_slope_504d_2d_v005_signal(ev, closeadj):
    base = ev
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slope_21d_2d_v006_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slope_63d_2d_v007_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slope_126d_2d_v008_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slope_252d_2d_v009_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_slope_504d_2d_v010_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slope_21d_2d_v011_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slope_63d_2d_v012_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slope_126d_2d_v013_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slope_252d_2d_v014_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_slope_504d_2d_v015_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slope_21d_2d_v016_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slope_63d_2d_v017_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slope_126d_2d_v018_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slope_252d_2d_v019_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_slope_504d_2d_v020_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of log_ev
def f039env_f039_enterprise_value_log_ev_slope_21d_2d_v021_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log_ev
def f039env_f039_enterprise_value_log_ev_slope_63d_2d_v022_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of log_ev
def f039env_f039_enterprise_value_log_ev_slope_126d_2d_v023_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log_ev
def f039env_f039_enterprise_value_log_ev_slope_252d_2d_v024_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of log_ev
def f039env_f039_enterprise_value_log_ev_slope_504d_2d_v025_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slope_21d_2d_v026_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slope_63d_2d_v027_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slope_126d_2d_v028_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slope_252d_2d_v029_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_slope_504d_2d_v030_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slope_21d_2d_v031_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slope_63d_2d_v032_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slope_126d_2d_v033_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slope_252d_2d_v034_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_slope_504d_2d_v035_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_sm21_sl21_2d_v036_signal(ev, closeadj):
    base = _mean(ev, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_sm63_sl21_2d_v037_signal(ev, closeadj):
    base = _mean(ev, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_sm63_sl63_2d_v038_signal(ev, closeadj):
    base = _mean(ev, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_sm252_sl63_2d_v039_signal(ev, closeadj):
    base = _mean(ev, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_sm252_sl126_2d_v040_signal(ev, closeadj):
    base = _mean(ev, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_sm21_sl21_2d_v041_signal(ev, marketcap, closeadj):
    base = _mean(_f039_ev_to_mcap(ev, marketcap), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_sm63_sl21_2d_v042_signal(ev, marketcap, closeadj):
    base = _mean(_f039_ev_to_mcap(ev, marketcap), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_sm63_sl63_2d_v043_signal(ev, marketcap, closeadj):
    base = _mean(_f039_ev_to_mcap(ev, marketcap), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_sm252_sl63_2d_v044_signal(ev, marketcap, closeadj):
    base = _mean(_f039_ev_to_mcap(ev, marketcap), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_sm252_sl126_2d_v045_signal(ev, marketcap, closeadj):
    base = _mean(_f039_ev_to_mcap(ev, marketcap), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_sm21_sl21_2d_v046_signal(ev, marketcap, closeadj):
    base = _mean(ev - marketcap, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_sm63_sl21_2d_v047_signal(ev, marketcap, closeadj):
    base = _mean(ev - marketcap, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_sm63_sl63_2d_v048_signal(ev, marketcap, closeadj):
    base = _mean(ev - marketcap, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_sm252_sl63_2d_v049_signal(ev, marketcap, closeadj):
    base = _mean(ev - marketcap, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_sm252_sl126_2d_v050_signal(ev, marketcap, closeadj):
    base = _mean(ev - marketcap, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_sm21_sl21_2d_v051_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_sm63_sl21_2d_v052_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_sm63_sl63_2d_v053_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_sm252_sl63_2d_v054_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_sm252_sl126_2d_v055_signal(ev, closeadj):
    base = _mean((ev < 0).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of log_ev
def f039env_f039_enterprise_value_log_ev_sm21_sl21_2d_v056_signal(ev, closeadj):
    base = _mean(np.log(ev.abs().replace(0, np.nan)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of log_ev
def f039env_f039_enterprise_value_log_ev_sm63_sl21_2d_v057_signal(ev, closeadj):
    base = _mean(np.log(ev.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of log_ev
def f039env_f039_enterprise_value_log_ev_sm63_sl63_2d_v058_signal(ev, closeadj):
    base = _mean(np.log(ev.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of log_ev
def f039env_f039_enterprise_value_log_ev_sm252_sl63_2d_v059_signal(ev, closeadj):
    base = _mean(np.log(ev.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of log_ev
def f039env_f039_enterprise_value_log_ev_sm252_sl126_2d_v060_signal(ev, closeadj):
    base = _mean(np.log(ev.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_sm21_sl21_2d_v061_signal(ev, sharesbas, closeadj):
    base = _mean(ev / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_sm63_sl21_2d_v062_signal(ev, sharesbas, closeadj):
    base = _mean(ev / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_sm63_sl63_2d_v063_signal(ev, sharesbas, closeadj):
    base = _mean(ev / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_sm252_sl63_2d_v064_signal(ev, sharesbas, closeadj):
    base = _mean(ev / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_sm252_sl126_2d_v065_signal(ev, sharesbas, closeadj):
    base = _mean(ev / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_sm21_sl21_2d_v066_signal(ev, assets, closeadj):
    base = _mean(ev / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_sm63_sl21_2d_v067_signal(ev, assets, closeadj):
    base = _mean(ev / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_sm63_sl63_2d_v068_signal(ev, assets, closeadj):
    base = _mean(ev / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_sm252_sl63_2d_v069_signal(ev, assets, closeadj):
    base = _mean(ev / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_sm252_sl126_2d_v070_signal(ev, assets, closeadj):
    base = _mean(ev / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_pctslope_21d_2d_v071_signal(ev, closeadj):
    base = ev
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_pctslope_63d_2d_v072_signal(ev, closeadj):
    base = ev
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_pctslope_252d_2d_v073_signal(ev, closeadj):
    base = ev
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_pctslope_21d_2d_v074_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_pctslope_63d_2d_v075_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_pctslope_252d_2d_v076_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_pctslope_21d_2d_v077_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_pctslope_63d_2d_v078_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_pctslope_252d_2d_v079_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_pctslope_21d_2d_v080_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_pctslope_63d_2d_v081_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_pctslope_252d_2d_v082_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of log_ev
def f039env_f039_enterprise_value_log_ev_pctslope_21d_2d_v083_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of log_ev
def f039env_f039_enterprise_value_log_ev_pctslope_63d_2d_v084_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of log_ev
def f039env_f039_enterprise_value_log_ev_pctslope_252d_2d_v085_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_pctslope_21d_2d_v086_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_pctslope_63d_2d_v087_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_pctslope_252d_2d_v088_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_pctslope_21d_2d_v089_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_pctslope_63d_2d_v090_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_pctslope_252d_2d_v091_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_sgnslope_21d_2d_v092_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_sgnslope_63d_2d_v093_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_sgnslope_252d_2d_v094_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_sgnslope_21d_2d_v095_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_sgnslope_63d_2d_v096_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_sgnslope_252d_2d_v097_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_sgnslope_21d_2d_v098_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_sgnslope_63d_2d_v099_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_sgnslope_252d_2d_v100_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_sgnslope_21d_2d_v101_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_sgnslope_63d_2d_v102_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_sgnslope_252d_2d_v103_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of log_ev
def f039env_f039_enterprise_value_log_ev_sgnslope_21d_2d_v104_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of log_ev
def f039env_f039_enterprise_value_log_ev_sgnslope_63d_2d_v105_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of log_ev
def f039env_f039_enterprise_value_log_ev_sgnslope_252d_2d_v106_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_sgnslope_21d_2d_v107_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_sgnslope_63d_2d_v108_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_sgnslope_252d_2d_v109_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_sgnslope_21d_2d_v110_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_sgnslope_63d_2d_v111_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_sgnslope_252d_2d_v112_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_logmagslope_21d_2d_v113_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_logmagslope_63d_2d_v114_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_logmagslope_252d_2d_v115_signal(ev, closeadj):
    base = ev
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_logmagslope_21d_2d_v116_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_logmagslope_63d_2d_v117_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_logmagslope_252d_2d_v118_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_logmagslope_21d_2d_v119_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_logmagslope_63d_2d_v120_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_logmagslope_252d_2d_v121_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_logmagslope_21d_2d_v122_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_logmagslope_63d_2d_v123_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_logmagslope_252d_2d_v124_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of log_ev
def f039env_f039_enterprise_value_log_ev_logmagslope_21d_2d_v125_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of log_ev
def f039env_f039_enterprise_value_log_ev_logmagslope_63d_2d_v126_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of log_ev
def f039env_f039_enterprise_value_log_ev_logmagslope_252d_2d_v127_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_logmagslope_21d_2d_v128_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_logmagslope_63d_2d_v129_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_logmagslope_252d_2d_v130_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_logmagslope_21d_2d_v131_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_logmagslope_63d_2d_v132_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_logmagslope_252d_2d_v133_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_lvl|
def f039env_f039_enterprise_value_ev_lvl_logslope_63d_2d_v134_signal(ev, closeadj):
    base = np.log((ev).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_lvl|
def f039env_f039_enterprise_value_ev_lvl_logslope_252d_2d_v135_signal(ev, closeadj):
    base = np.log((ev).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_to_mcap|
def f039env_f039_enterprise_value_ev_to_mcap_logslope_63d_2d_v136_signal(ev, marketcap, closeadj):
    base = np.log((_f039_ev_to_mcap(ev, marketcap)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_to_mcap|
def f039env_f039_enterprise_value_ev_to_mcap_logslope_252d_2d_v137_signal(ev, marketcap, closeadj):
    base = np.log((_f039_ev_to_mcap(ev, marketcap)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_minus_mcap|
def f039env_f039_enterprise_value_ev_minus_mcap_logslope_63d_2d_v138_signal(ev, marketcap, closeadj):
    base = np.log((ev - marketcap).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_minus_mcap|
def f039env_f039_enterprise_value_ev_minus_mcap_logslope_252d_2d_v139_signal(ev, marketcap, closeadj):
    base = np.log((ev - marketcap).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_neg_flag|
def f039env_f039_enterprise_value_ev_neg_flag_logslope_63d_2d_v140_signal(ev, closeadj):
    base = np.log(((ev < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_neg_flag|
def f039env_f039_enterprise_value_ev_neg_flag_logslope_252d_2d_v141_signal(ev, closeadj):
    base = np.log(((ev < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|log_ev|
def f039env_f039_enterprise_value_log_ev_logslope_63d_2d_v142_signal(ev, closeadj):
    base = np.log((np.log(ev.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|log_ev|
def f039env_f039_enterprise_value_log_ev_logslope_252d_2d_v143_signal(ev, closeadj):
    base = np.log((np.log(ev.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_per_share|
def f039env_f039_enterprise_value_ev_per_share_logslope_63d_2d_v144_signal(ev, sharesbas, closeadj):
    base = np.log((ev / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_per_share|
def f039env_f039_enterprise_value_ev_per_share_logslope_252d_2d_v145_signal(ev, sharesbas, closeadj):
    base = np.log((ev / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ev_to_asset|
def f039env_f039_enterprise_value_ev_to_asset_logslope_63d_2d_v146_signal(ev, assets, closeadj):
    base = np.log((ev / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ev_to_asset|
def f039env_f039_enterprise_value_ev_to_asset_logslope_252d_2d_v147_signal(ev, assets, closeadj):
    base = np.log((ev / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

