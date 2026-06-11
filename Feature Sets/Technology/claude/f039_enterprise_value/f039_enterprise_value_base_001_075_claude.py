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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f039_ev_to_mcap(ev, marketcap):
    return ev / marketcap.replace(0, np.nan).abs()


# 21d mean of ev_lvl scaled by closeadj
def f039env_f039_enterprise_value_ev_lvl_mean_21d_base_v001_signal(ev, closeadj):
    base = ev
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_lvl scaled by closeadj
def f039env_f039_enterprise_value_ev_lvl_mean_63d_base_v002_signal(ev, closeadj):
    base = ev
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_lvl scaled by closeadj
def f039env_f039_enterprise_value_ev_lvl_mean_126d_base_v003_signal(ev, closeadj):
    base = ev
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_lvl scaled by closeadj
def f039env_f039_enterprise_value_ev_lvl_mean_252d_base_v004_signal(ev, closeadj):
    base = ev
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_lvl scaled by closeadj
def f039env_f039_enterprise_value_ev_lvl_mean_504d_base_v005_signal(ev, closeadj):
    base = ev
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_to_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_to_mcap_mean_21d_base_v006_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_to_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_to_mcap_mean_63d_base_v007_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_to_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_to_mcap_mean_126d_base_v008_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_to_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_to_mcap_mean_252d_base_v009_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_to_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_to_mcap_mean_504d_base_v010_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_minus_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_minus_mcap_mean_21d_base_v011_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_minus_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_minus_mcap_mean_63d_base_v012_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_minus_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_minus_mcap_mean_126d_base_v013_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_minus_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_minus_mcap_mean_252d_base_v014_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_minus_mcap scaled by closeadj
def f039env_f039_enterprise_value_ev_minus_mcap_mean_504d_base_v015_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_neg_flag scaled by closeadj
def f039env_f039_enterprise_value_ev_neg_flag_mean_21d_base_v016_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_neg_flag scaled by closeadj
def f039env_f039_enterprise_value_ev_neg_flag_mean_63d_base_v017_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_neg_flag scaled by closeadj
def f039env_f039_enterprise_value_ev_neg_flag_mean_126d_base_v018_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_neg_flag scaled by closeadj
def f039env_f039_enterprise_value_ev_neg_flag_mean_252d_base_v019_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_neg_flag scaled by closeadj
def f039env_f039_enterprise_value_ev_neg_flag_mean_504d_base_v020_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of log_ev scaled by closeadj
def f039env_f039_enterprise_value_log_ev_mean_21d_base_v021_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of log_ev scaled by closeadj
def f039env_f039_enterprise_value_log_ev_mean_63d_base_v022_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of log_ev scaled by closeadj
def f039env_f039_enterprise_value_log_ev_mean_126d_base_v023_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of log_ev scaled by closeadj
def f039env_f039_enterprise_value_log_ev_mean_252d_base_v024_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of log_ev scaled by closeadj
def f039env_f039_enterprise_value_log_ev_mean_504d_base_v025_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_per_share scaled by closeadj
def f039env_f039_enterprise_value_ev_per_share_mean_21d_base_v026_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_per_share scaled by closeadj
def f039env_f039_enterprise_value_ev_per_share_mean_63d_base_v027_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_per_share scaled by closeadj
def f039env_f039_enterprise_value_ev_per_share_mean_126d_base_v028_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_per_share scaled by closeadj
def f039env_f039_enterprise_value_ev_per_share_mean_252d_base_v029_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_per_share scaled by closeadj
def f039env_f039_enterprise_value_ev_per_share_mean_504d_base_v030_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ev_to_asset scaled by closeadj
def f039env_f039_enterprise_value_ev_to_asset_mean_21d_base_v031_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ev_to_asset scaled by closeadj
def f039env_f039_enterprise_value_ev_to_asset_mean_63d_base_v032_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ev_to_asset scaled by closeadj
def f039env_f039_enterprise_value_ev_to_asset_mean_126d_base_v033_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ev_to_asset scaled by closeadj
def f039env_f039_enterprise_value_ev_to_asset_mean_252d_base_v034_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ev_to_asset scaled by closeadj
def f039env_f039_enterprise_value_ev_to_asset_mean_504d_base_v035_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_median_63d_base_v036_signal(ev, closeadj):
    base = ev
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_median_252d_base_v037_signal(ev, closeadj):
    base = ev
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_median_504d_base_v038_signal(ev, closeadj):
    base = ev
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_median_63d_base_v039_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_median_252d_base_v040_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_median_504d_base_v041_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_median_63d_base_v042_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_median_252d_base_v043_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_median_504d_base_v044_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_median_63d_base_v045_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_median_252d_base_v046_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_median_504d_base_v047_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of log_ev
def f039env_f039_enterprise_value_log_ev_median_63d_base_v048_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of log_ev
def f039env_f039_enterprise_value_log_ev_median_252d_base_v049_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of log_ev
def f039env_f039_enterprise_value_log_ev_median_504d_base_v050_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_median_63d_base_v051_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_median_252d_base_v052_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_median_504d_base_v053_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_median_63d_base_v054_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_median_252d_base_v055_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_median_504d_base_v056_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_rmax_252d_base_v057_signal(ev, closeadj):
    base = ev
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_rmax_504d_base_v058_signal(ev, closeadj):
    base = ev
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_rmax_252d_base_v059_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_rmax_504d_base_v060_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_rmax_252d_base_v061_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_rmax_504d_base_v062_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_rmax_252d_base_v063_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_neg_flag
def f039env_f039_enterprise_value_ev_neg_flag_rmax_504d_base_v064_signal(ev, closeadj):
    base = (ev < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of log_ev
def f039env_f039_enterprise_value_log_ev_rmax_252d_base_v065_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of log_ev
def f039env_f039_enterprise_value_log_ev_rmax_504d_base_v066_signal(ev, closeadj):
    base = np.log(ev.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_rmax_252d_base_v067_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_per_share
def f039env_f039_enterprise_value_ev_per_share_rmax_504d_base_v068_signal(ev, sharesbas, closeadj):
    base = ev / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_rmax_252d_base_v069_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ev_to_asset
def f039env_f039_enterprise_value_ev_to_asset_rmax_504d_base_v070_signal(ev, assets, closeadj):
    base = ev / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_rmin_252d_base_v071_signal(ev, closeadj):
    base = ev
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ev_lvl
def f039env_f039_enterprise_value_ev_lvl_rmin_504d_base_v072_signal(ev, closeadj):
    base = ev
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_rmin_252d_base_v073_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ev_to_mcap
def f039env_f039_enterprise_value_ev_to_mcap_rmin_504d_base_v074_signal(ev, marketcap, closeadj):
    base = _f039_ev_to_mcap(ev, marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ev_minus_mcap
def f039env_f039_enterprise_value_ev_minus_mcap_rmin_252d_base_v075_signal(ev, marketcap, closeadj):
    base = ev - marketcap
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

