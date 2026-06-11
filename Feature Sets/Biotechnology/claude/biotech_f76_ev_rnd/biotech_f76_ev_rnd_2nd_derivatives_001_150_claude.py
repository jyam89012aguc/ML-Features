"""Family f76 - EV / R&D  (M_Valuation) | 2nd derivatives 001-150"""
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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _ev_rnd_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ev_rnd_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ev_rnd_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw ev
def evd_f76_ev_rnd_raw_21d_slope_v001_signal(ev, closeadj):
    base = _mean(ev, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw ev
def evd_f76_ev_rnd_raw_21d_slope_v002_signal(ev, closeadj):
    base = _mean(ev, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw ev
def evd_f76_ev_rnd_raw_21d_slope_v003_signal(ev, closeadj):
    base = _mean(ev, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw ev
def evd_f76_ev_rnd_raw_63d_slope_v004_signal(ev, closeadj):
    base = _mean(ev, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw ev
def evd_f76_ev_rnd_raw_63d_slope_v005_signal(ev, closeadj):
    base = _mean(ev, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw ev
def evd_f76_ev_rnd_raw_63d_slope_v006_signal(ev, closeadj):
    base = _mean(ev, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw ev
def evd_f76_ev_rnd_raw_126d_slope_v007_signal(ev, closeadj):
    base = _mean(ev, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw ev
def evd_f76_ev_rnd_raw_126d_slope_v008_signal(ev, closeadj):
    base = _mean(ev, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw ev
def evd_f76_ev_rnd_raw_126d_slope_v009_signal(ev, closeadj):
    base = _mean(ev, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw ev
def evd_f76_ev_rnd_raw_252d_slope_v010_signal(ev, closeadj):
    base = _mean(ev, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw ev
def evd_f76_ev_rnd_raw_252d_slope_v011_signal(ev, closeadj):
    base = _mean(ev, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw ev
def evd_f76_ev_rnd_raw_252d_slope_v012_signal(ev, closeadj):
    base = _mean(ev, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw ev
def evd_f76_ev_rnd_raw_504d_slope_v013_signal(ev, closeadj):
    base = _mean(ev, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw ev
def evd_f76_ev_rnd_raw_504d_slope_v014_signal(ev, closeadj):
    base = _mean(ev, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw ev
def evd_f76_ev_rnd_raw_504d_slope_v015_signal(ev, closeadj):
    base = _mean(ev, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log ev
def evd_f76_ev_rnd_log_21d_slope_v016_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log ev
def evd_f76_ev_rnd_log_21d_slope_v017_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log ev
def evd_f76_ev_rnd_log_21d_slope_v018_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log ev
def evd_f76_ev_rnd_log_63d_slope_v019_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log ev
def evd_f76_ev_rnd_log_63d_slope_v020_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log ev
def evd_f76_ev_rnd_log_63d_slope_v021_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log ev
def evd_f76_ev_rnd_log_126d_slope_v022_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log ev
def evd_f76_ev_rnd_log_126d_slope_v023_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log ev
def evd_f76_ev_rnd_log_126d_slope_v024_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log ev
def evd_f76_ev_rnd_log_252d_slope_v025_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log ev
def evd_f76_ev_rnd_log_252d_slope_v026_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log ev
def evd_f76_ev_rnd_log_252d_slope_v027_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log ev
def evd_f76_ev_rnd_log_504d_slope_v028_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log ev
def evd_f76_ev_rnd_log_504d_slope_v029_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log ev
def evd_f76_ev_rnd_log_504d_slope_v030_signal(ev, closeadj):
    base = _mean(_ev_rnd_log(ev), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare ev
def evd_f76_ev_rnd_pershare_21d_slope_v031_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare ev
def evd_f76_ev_rnd_pershare_21d_slope_v032_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare ev
def evd_f76_ev_rnd_pershare_21d_slope_v033_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare ev
def evd_f76_ev_rnd_pershare_63d_slope_v034_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare ev
def evd_f76_ev_rnd_pershare_63d_slope_v035_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare ev
def evd_f76_ev_rnd_pershare_63d_slope_v036_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare ev
def evd_f76_ev_rnd_pershare_126d_slope_v037_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare ev
def evd_f76_ev_rnd_pershare_126d_slope_v038_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare ev
def evd_f76_ev_rnd_pershare_126d_slope_v039_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare ev
def evd_f76_ev_rnd_pershare_252d_slope_v040_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare ev
def evd_f76_ev_rnd_pershare_252d_slope_v041_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare ev
def evd_f76_ev_rnd_pershare_252d_slope_v042_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare ev
def evd_f76_ev_rnd_pershare_504d_slope_v043_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare ev
def evd_f76_ev_rnd_pershare_504d_slope_v044_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare ev
def evd_f76_ev_rnd_pershare_504d_slope_v045_signal(ev, sharesbas, closeadj):
    base = _mean(_ev_rnd_per_share(ev, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets ev
def evd_f76_ev_rnd_per_assets_21d_slope_v046_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets ev
def evd_f76_ev_rnd_per_assets_21d_slope_v047_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets ev
def evd_f76_ev_rnd_per_assets_21d_slope_v048_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets ev
def evd_f76_ev_rnd_per_assets_63d_slope_v049_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets ev
def evd_f76_ev_rnd_per_assets_63d_slope_v050_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets ev
def evd_f76_ev_rnd_per_assets_63d_slope_v051_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets ev
def evd_f76_ev_rnd_per_assets_126d_slope_v052_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets ev
def evd_f76_ev_rnd_per_assets_126d_slope_v053_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets ev
def evd_f76_ev_rnd_per_assets_126d_slope_v054_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets ev
def evd_f76_ev_rnd_per_assets_252d_slope_v055_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets ev
def evd_f76_ev_rnd_per_assets_252d_slope_v056_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets ev
def evd_f76_ev_rnd_per_assets_252d_slope_v057_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets ev
def evd_f76_ev_rnd_per_assets_504d_slope_v058_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets ev
def evd_f76_ev_rnd_per_assets_504d_slope_v059_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets ev
def evd_f76_ev_rnd_per_assets_504d_slope_v060_signal(ev, assets):
    base = _mean(_ev_rnd_scaled(ev, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_21d_slope_v061_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_21d_slope_v062_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_21d_slope_v063_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_63d_slope_v064_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_63d_slope_v065_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_63d_slope_v066_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_126d_slope_v067_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_126d_slope_v068_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_126d_slope_v069_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_252d_slope_v070_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_252d_slope_v071_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_252d_slope_v072_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_504d_slope_v073_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_504d_slope_v074_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap ev
def evd_f76_ev_rnd_per_marketcap_504d_slope_v075_signal(ev, marketcap):
    base = _mean(_ev_rnd_scaled(ev, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity ev
def evd_f76_ev_rnd_per_equity_21d_slope_v076_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity ev
def evd_f76_ev_rnd_per_equity_21d_slope_v077_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity ev
def evd_f76_ev_rnd_per_equity_21d_slope_v078_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity ev
def evd_f76_ev_rnd_per_equity_63d_slope_v079_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity ev
def evd_f76_ev_rnd_per_equity_63d_slope_v080_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity ev
def evd_f76_ev_rnd_per_equity_63d_slope_v081_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity ev
def evd_f76_ev_rnd_per_equity_126d_slope_v082_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity ev
def evd_f76_ev_rnd_per_equity_126d_slope_v083_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity ev
def evd_f76_ev_rnd_per_equity_126d_slope_v084_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity ev
def evd_f76_ev_rnd_per_equity_252d_slope_v085_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity ev
def evd_f76_ev_rnd_per_equity_252d_slope_v086_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity ev
def evd_f76_ev_rnd_per_equity_252d_slope_v087_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity ev
def evd_f76_ev_rnd_per_equity_504d_slope_v088_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity ev
def evd_f76_ev_rnd_per_equity_504d_slope_v089_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity ev
def evd_f76_ev_rnd_per_equity_504d_slope_v090_signal(ev, equity):
    base = _mean(_ev_rnd_scaled(ev, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std ev
def evd_f76_ev_rnd_std_21d_slope_v091_signal(ev, closeadj):
    base = _std(ev, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std ev
def evd_f76_ev_rnd_std_21d_slope_v092_signal(ev, closeadj):
    base = _std(ev, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std ev
def evd_f76_ev_rnd_std_21d_slope_v093_signal(ev, closeadj):
    base = _std(ev, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std ev
def evd_f76_ev_rnd_std_63d_slope_v094_signal(ev, closeadj):
    base = _std(ev, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std ev
def evd_f76_ev_rnd_std_63d_slope_v095_signal(ev, closeadj):
    base = _std(ev, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std ev
def evd_f76_ev_rnd_std_63d_slope_v096_signal(ev, closeadj):
    base = _std(ev, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std ev
def evd_f76_ev_rnd_std_126d_slope_v097_signal(ev, closeadj):
    base = _std(ev, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std ev
def evd_f76_ev_rnd_std_126d_slope_v098_signal(ev, closeadj):
    base = _std(ev, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std ev
def evd_f76_ev_rnd_std_126d_slope_v099_signal(ev, closeadj):
    base = _std(ev, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std ev
def evd_f76_ev_rnd_std_252d_slope_v100_signal(ev, closeadj):
    base = _std(ev, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std ev
def evd_f76_ev_rnd_std_252d_slope_v101_signal(ev, closeadj):
    base = _std(ev, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std ev
def evd_f76_ev_rnd_std_252d_slope_v102_signal(ev, closeadj):
    base = _std(ev, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std ev
def evd_f76_ev_rnd_std_504d_slope_v103_signal(ev, closeadj):
    base = _std(ev, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std ev
def evd_f76_ev_rnd_std_504d_slope_v104_signal(ev, closeadj):
    base = _std(ev, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std ev
def evd_f76_ev_rnd_std_504d_slope_v105_signal(ev, closeadj):
    base = _std(ev, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm ev
def evd_f76_ev_rnd_ewm_21d_slope_v106_signal(ev, closeadj):
    base = ev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm ev
def evd_f76_ev_rnd_ewm_21d_slope_v107_signal(ev, closeadj):
    base = ev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm ev
def evd_f76_ev_rnd_ewm_21d_slope_v108_signal(ev, closeadj):
    base = ev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm ev
def evd_f76_ev_rnd_ewm_63d_slope_v109_signal(ev, closeadj):
    base = ev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm ev
def evd_f76_ev_rnd_ewm_63d_slope_v110_signal(ev, closeadj):
    base = ev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm ev
def evd_f76_ev_rnd_ewm_63d_slope_v111_signal(ev, closeadj):
    base = ev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm ev
def evd_f76_ev_rnd_ewm_126d_slope_v112_signal(ev, closeadj):
    base = ev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm ev
def evd_f76_ev_rnd_ewm_126d_slope_v113_signal(ev, closeadj):
    base = ev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm ev
def evd_f76_ev_rnd_ewm_126d_slope_v114_signal(ev, closeadj):
    base = ev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm ev
def evd_f76_ev_rnd_ewm_252d_slope_v115_signal(ev, closeadj):
    base = ev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm ev
def evd_f76_ev_rnd_ewm_252d_slope_v116_signal(ev, closeadj):
    base = ev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm ev
def evd_f76_ev_rnd_ewm_252d_slope_v117_signal(ev, closeadj):
    base = ev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm ev
def evd_f76_ev_rnd_ewm_504d_slope_v118_signal(ev, closeadj):
    base = ev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm ev
def evd_f76_ev_rnd_ewm_504d_slope_v119_signal(ev, closeadj):
    base = ev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm ev
def evd_f76_ev_rnd_ewm_504d_slope_v120_signal(ev, closeadj):
    base = ev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq ev
def evd_f76_ev_rnd_sq_21d_slope_v121_signal(ev, closeadj):
    base = _mean(ev * ev, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq ev
def evd_f76_ev_rnd_sq_21d_slope_v122_signal(ev, closeadj):
    base = _mean(ev * ev, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq ev
def evd_f76_ev_rnd_sq_21d_slope_v123_signal(ev, closeadj):
    base = _mean(ev * ev, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq ev
def evd_f76_ev_rnd_sq_63d_slope_v124_signal(ev, closeadj):
    base = _mean(ev * ev, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq ev
def evd_f76_ev_rnd_sq_63d_slope_v125_signal(ev, closeadj):
    base = _mean(ev * ev, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq ev
def evd_f76_ev_rnd_sq_63d_slope_v126_signal(ev, closeadj):
    base = _mean(ev * ev, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq ev
def evd_f76_ev_rnd_sq_126d_slope_v127_signal(ev, closeadj):
    base = _mean(ev * ev, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq ev
def evd_f76_ev_rnd_sq_126d_slope_v128_signal(ev, closeadj):
    base = _mean(ev * ev, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq ev
def evd_f76_ev_rnd_sq_126d_slope_v129_signal(ev, closeadj):
    base = _mean(ev * ev, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq ev
def evd_f76_ev_rnd_sq_252d_slope_v130_signal(ev, closeadj):
    base = _mean(ev * ev, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq ev
def evd_f76_ev_rnd_sq_252d_slope_v131_signal(ev, closeadj):
    base = _mean(ev * ev, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq ev
def evd_f76_ev_rnd_sq_252d_slope_v132_signal(ev, closeadj):
    base = _mean(ev * ev, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq ev
def evd_f76_ev_rnd_sq_504d_slope_v133_signal(ev, closeadj):
    base = _mean(ev * ev, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq ev
def evd_f76_ev_rnd_sq_504d_slope_v134_signal(ev, closeadj):
    base = _mean(ev * ev, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq ev
def evd_f76_ev_rnd_sq_504d_slope_v135_signal(ev, closeadj):
    base = _mean(ev * ev, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z ev
def evd_f76_ev_rnd_z_21d_slope_v136_signal(ev):
    base = _z(ev, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z ev
def evd_f76_ev_rnd_z_21d_slope_v137_signal(ev):
    base = _z(ev, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z ev
def evd_f76_ev_rnd_z_21d_slope_v138_signal(ev):
    base = _z(ev, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z ev
def evd_f76_ev_rnd_z_63d_slope_v139_signal(ev):
    base = _z(ev, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z ev
def evd_f76_ev_rnd_z_63d_slope_v140_signal(ev):
    base = _z(ev, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z ev
def evd_f76_ev_rnd_z_63d_slope_v141_signal(ev):
    base = _z(ev, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z ev
def evd_f76_ev_rnd_z_126d_slope_v142_signal(ev):
    base = _z(ev, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z ev
def evd_f76_ev_rnd_z_126d_slope_v143_signal(ev):
    base = _z(ev, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z ev
def evd_f76_ev_rnd_z_126d_slope_v144_signal(ev):
    base = _z(ev, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z ev
def evd_f76_ev_rnd_z_252d_slope_v145_signal(ev):
    base = _z(ev, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z ev
def evd_f76_ev_rnd_z_252d_slope_v146_signal(ev):
    base = _z(ev, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z ev
def evd_f76_ev_rnd_z_252d_slope_v147_signal(ev):
    base = _z(ev, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z ev
def evd_f76_ev_rnd_z_504d_slope_v148_signal(ev):
    base = _z(ev, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z ev
def evd_f76_ev_rnd_z_504d_slope_v149_signal(ev):
    base = _z(ev, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z ev
def evd_f76_ev_rnd_z_504d_slope_v150_signal(ev):
    base = _z(ev, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
