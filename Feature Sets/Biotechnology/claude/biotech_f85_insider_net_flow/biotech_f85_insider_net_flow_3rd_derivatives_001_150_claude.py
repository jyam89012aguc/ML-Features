"""Family f85 - Insider net buy/sell  (O_Insider_SF2) | 3rd derivatives 001-150"""
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
def _insider_net_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_net_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_net_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw transactionvalue
def inf_f85_insider_net_flow_raw_21d_accel_v001_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw transactionvalue
def inf_f85_insider_net_flow_raw_21d_accel_v002_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw transactionvalue
def inf_f85_insider_net_flow_raw_21d_accel_v003_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw transactionvalue
def inf_f85_insider_net_flow_raw_63d_accel_v004_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw transactionvalue
def inf_f85_insider_net_flow_raw_63d_accel_v005_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw transactionvalue
def inf_f85_insider_net_flow_raw_63d_accel_v006_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw transactionvalue
def inf_f85_insider_net_flow_raw_126d_accel_v007_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw transactionvalue
def inf_f85_insider_net_flow_raw_126d_accel_v008_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw transactionvalue
def inf_f85_insider_net_flow_raw_126d_accel_v009_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw transactionvalue
def inf_f85_insider_net_flow_raw_252d_accel_v010_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw transactionvalue
def inf_f85_insider_net_flow_raw_252d_accel_v011_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw transactionvalue
def inf_f85_insider_net_flow_raw_252d_accel_v012_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw transactionvalue
def inf_f85_insider_net_flow_raw_504d_accel_v013_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw transactionvalue
def inf_f85_insider_net_flow_raw_504d_accel_v014_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw transactionvalue
def inf_f85_insider_net_flow_raw_504d_accel_v015_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log transactionvalue
def inf_f85_insider_net_flow_log_21d_accel_v016_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log transactionvalue
def inf_f85_insider_net_flow_log_21d_accel_v017_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log transactionvalue
def inf_f85_insider_net_flow_log_21d_accel_v018_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log transactionvalue
def inf_f85_insider_net_flow_log_63d_accel_v019_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log transactionvalue
def inf_f85_insider_net_flow_log_63d_accel_v020_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log transactionvalue
def inf_f85_insider_net_flow_log_63d_accel_v021_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log transactionvalue
def inf_f85_insider_net_flow_log_126d_accel_v022_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log transactionvalue
def inf_f85_insider_net_flow_log_126d_accel_v023_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log transactionvalue
def inf_f85_insider_net_flow_log_126d_accel_v024_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log transactionvalue
def inf_f85_insider_net_flow_log_252d_accel_v025_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log transactionvalue
def inf_f85_insider_net_flow_log_252d_accel_v026_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log transactionvalue
def inf_f85_insider_net_flow_log_252d_accel_v027_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log transactionvalue
def inf_f85_insider_net_flow_log_504d_accel_v028_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log transactionvalue
def inf_f85_insider_net_flow_log_504d_accel_v029_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log transactionvalue
def inf_f85_insider_net_flow_log_504d_accel_v030_signal(transactionvalue, closeadj):
    base = _mean(_insider_net_flow_log(transactionvalue), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_21d_accel_v031_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_21d_accel_v032_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_21d_accel_v033_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_63d_accel_v034_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_63d_accel_v035_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_63d_accel_v036_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_126d_accel_v037_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_126d_accel_v038_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_126d_accel_v039_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_252d_accel_v040_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_252d_accel_v041_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_252d_accel_v042_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_504d_accel_v043_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_504d_accel_v044_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare transactionvalue
def inf_f85_insider_net_flow_pershare_504d_accel_v045_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_net_flow_per_share(transactionvalue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_21d_accel_v046_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_21d_accel_v047_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_21d_accel_v048_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_63d_accel_v049_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_63d_accel_v050_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_63d_accel_v051_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_126d_accel_v052_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_126d_accel_v053_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_126d_accel_v054_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_252d_accel_v055_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_252d_accel_v056_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_252d_accel_v057_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_504d_accel_v058_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_504d_accel_v059_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets transactionvalue
def inf_f85_insider_net_flow_per_assets_504d_accel_v060_signal(transactionvalue, assets):
    base = _mean(_insider_net_flow_scaled(transactionvalue, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_21d_accel_v061_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_21d_accel_v062_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_21d_accel_v063_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_63d_accel_v064_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_63d_accel_v065_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_63d_accel_v066_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_126d_accel_v067_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_126d_accel_v068_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_126d_accel_v069_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_252d_accel_v070_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_252d_accel_v071_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_252d_accel_v072_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_504d_accel_v073_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_504d_accel_v074_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap transactionvalue
def inf_f85_insider_net_flow_per_marketcap_504d_accel_v075_signal(transactionvalue, marketcap):
    base = _mean(_insider_net_flow_scaled(transactionvalue, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_21d_accel_v076_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_21d_accel_v077_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_21d_accel_v078_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_63d_accel_v079_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_63d_accel_v080_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_63d_accel_v081_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_126d_accel_v082_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_126d_accel_v083_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_126d_accel_v084_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_252d_accel_v085_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_252d_accel_v086_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_252d_accel_v087_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_504d_accel_v088_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_504d_accel_v089_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity transactionvalue
def inf_f85_insider_net_flow_per_equity_504d_accel_v090_signal(transactionvalue, equity):
    base = _mean(_insider_net_flow_scaled(transactionvalue, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std transactionvalue
def inf_f85_insider_net_flow_std_21d_accel_v091_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std transactionvalue
def inf_f85_insider_net_flow_std_21d_accel_v092_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std transactionvalue
def inf_f85_insider_net_flow_std_21d_accel_v093_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std transactionvalue
def inf_f85_insider_net_flow_std_63d_accel_v094_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std transactionvalue
def inf_f85_insider_net_flow_std_63d_accel_v095_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std transactionvalue
def inf_f85_insider_net_flow_std_63d_accel_v096_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std transactionvalue
def inf_f85_insider_net_flow_std_126d_accel_v097_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std transactionvalue
def inf_f85_insider_net_flow_std_126d_accel_v098_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std transactionvalue
def inf_f85_insider_net_flow_std_126d_accel_v099_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std transactionvalue
def inf_f85_insider_net_flow_std_252d_accel_v100_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std transactionvalue
def inf_f85_insider_net_flow_std_252d_accel_v101_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std transactionvalue
def inf_f85_insider_net_flow_std_252d_accel_v102_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std transactionvalue
def inf_f85_insider_net_flow_std_504d_accel_v103_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std transactionvalue
def inf_f85_insider_net_flow_std_504d_accel_v104_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std transactionvalue
def inf_f85_insider_net_flow_std_504d_accel_v105_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_21d_accel_v106_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_21d_accel_v107_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_21d_accel_v108_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_63d_accel_v109_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_63d_accel_v110_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_63d_accel_v111_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_126d_accel_v112_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_126d_accel_v113_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_126d_accel_v114_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_252d_accel_v115_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_252d_accel_v116_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_252d_accel_v117_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_504d_accel_v118_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_504d_accel_v119_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm transactionvalue
def inf_f85_insider_net_flow_ewm_504d_accel_v120_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq transactionvalue
def inf_f85_insider_net_flow_sq_21d_accel_v121_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq transactionvalue
def inf_f85_insider_net_flow_sq_21d_accel_v122_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq transactionvalue
def inf_f85_insider_net_flow_sq_21d_accel_v123_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq transactionvalue
def inf_f85_insider_net_flow_sq_63d_accel_v124_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq transactionvalue
def inf_f85_insider_net_flow_sq_63d_accel_v125_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq transactionvalue
def inf_f85_insider_net_flow_sq_63d_accel_v126_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq transactionvalue
def inf_f85_insider_net_flow_sq_126d_accel_v127_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq transactionvalue
def inf_f85_insider_net_flow_sq_126d_accel_v128_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq transactionvalue
def inf_f85_insider_net_flow_sq_126d_accel_v129_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq transactionvalue
def inf_f85_insider_net_flow_sq_252d_accel_v130_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq transactionvalue
def inf_f85_insider_net_flow_sq_252d_accel_v131_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq transactionvalue
def inf_f85_insider_net_flow_sq_252d_accel_v132_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq transactionvalue
def inf_f85_insider_net_flow_sq_504d_accel_v133_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq transactionvalue
def inf_f85_insider_net_flow_sq_504d_accel_v134_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq transactionvalue
def inf_f85_insider_net_flow_sq_504d_accel_v135_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z transactionvalue
def inf_f85_insider_net_flow_z_21d_accel_v136_signal(transactionvalue):
    base = _z(transactionvalue, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z transactionvalue
def inf_f85_insider_net_flow_z_21d_accel_v137_signal(transactionvalue):
    base = _z(transactionvalue, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z transactionvalue
def inf_f85_insider_net_flow_z_21d_accel_v138_signal(transactionvalue):
    base = _z(transactionvalue, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z transactionvalue
def inf_f85_insider_net_flow_z_63d_accel_v139_signal(transactionvalue):
    base = _z(transactionvalue, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z transactionvalue
def inf_f85_insider_net_flow_z_63d_accel_v140_signal(transactionvalue):
    base = _z(transactionvalue, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z transactionvalue
def inf_f85_insider_net_flow_z_63d_accel_v141_signal(transactionvalue):
    base = _z(transactionvalue, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z transactionvalue
def inf_f85_insider_net_flow_z_126d_accel_v142_signal(transactionvalue):
    base = _z(transactionvalue, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z transactionvalue
def inf_f85_insider_net_flow_z_126d_accel_v143_signal(transactionvalue):
    base = _z(transactionvalue, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z transactionvalue
def inf_f85_insider_net_flow_z_126d_accel_v144_signal(transactionvalue):
    base = _z(transactionvalue, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z transactionvalue
def inf_f85_insider_net_flow_z_252d_accel_v145_signal(transactionvalue):
    base = _z(transactionvalue, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z transactionvalue
def inf_f85_insider_net_flow_z_252d_accel_v146_signal(transactionvalue):
    base = _z(transactionvalue, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z transactionvalue
def inf_f85_insider_net_flow_z_252d_accel_v147_signal(transactionvalue):
    base = _z(transactionvalue, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z transactionvalue
def inf_f85_insider_net_flow_z_504d_accel_v148_signal(transactionvalue):
    base = _z(transactionvalue, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z transactionvalue
def inf_f85_insider_net_flow_z_504d_accel_v149_signal(transactionvalue):
    base = _z(transactionvalue, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z transactionvalue
def inf_f85_insider_net_flow_z_504d_accel_v150_signal(transactionvalue):
    base = _z(transactionvalue, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
