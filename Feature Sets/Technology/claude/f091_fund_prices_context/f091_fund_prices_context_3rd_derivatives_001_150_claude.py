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
def _f091_etf_rel(closeadj, etf_close):
    return closeadj.pct_change(periods=63) - etf_close.pct_change(periods=63)


# 21d acceleration of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_accel_21d_3d_v001_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_accel_63d_3d_v002_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_accel_126d_3d_v003_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_accel_252d_3d_v004_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_accel_21d_3d_v005_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_accel_63d_3d_v006_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_accel_126d_3d_v007_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_accel_252d_3d_v008_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_accel_21d_3d_v009_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_accel_63d_3d_v010_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_accel_126d_3d_v011_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_accel_252d_3d_v012_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_accel_21d_3d_v013_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_accel_63d_3d_v014_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_accel_126d_3d_v015_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_accel_252d_3d_v016_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_accel_21d_3d_v017_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_accel_63d_3d_v018_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_accel_126d_3d_v019_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_accel_252d_3d_v020_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_accel_21d_3d_v021_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_accel_63d_3d_v022_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_accel_126d_3d_v023_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_accel_252d_3d_v024_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_accel_21d_3d_v025_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_accel_63d_3d_v026_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_accel_126d_3d_v027_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_accel_252d_3d_v028_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slopez_21d_z126_3d_v029_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slopez_63d_z252_3d_v030_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slopez_126d_z252_3d_v031_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slopez_252d_z504_3d_v032_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slopez_21d_z126_3d_v033_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slopez_63d_z252_3d_v034_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slopez_126d_z252_3d_v035_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slopez_252d_z504_3d_v036_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slopez_21d_z126_3d_v037_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slopez_63d_z252_3d_v038_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slopez_126d_z252_3d_v039_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slopez_252d_z504_3d_v040_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slopez_21d_z126_3d_v041_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slopez_63d_z252_3d_v042_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slopez_126d_z252_3d_v043_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slopez_252d_z504_3d_v044_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slopez_21d_z126_3d_v045_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slopez_63d_z252_3d_v046_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slopez_126d_z252_3d_v047_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slopez_252d_z504_3d_v048_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slopez_21d_z126_3d_v049_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slopez_63d_z252_3d_v050_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slopez_126d_z252_3d_v051_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slopez_252d_z504_3d_v052_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slopez_21d_z126_3d_v053_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slopez_63d_z252_3d_v054_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slopez_126d_z252_3d_v055_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slopez_252d_z504_3d_v056_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_jerk_21d_3d_v057_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_jerk_63d_3d_v058_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_jerk_126d_3d_v059_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_jerk_21d_3d_v060_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_jerk_63d_3d_v061_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_jerk_126d_3d_v062_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_jerk_21d_3d_v063_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_jerk_63d_3d_v064_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_jerk_126d_3d_v065_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_jerk_21d_3d_v066_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_jerk_63d_3d_v067_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_jerk_126d_3d_v068_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_jerk_21d_3d_v069_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_jerk_63d_3d_v070_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_jerk_126d_3d_v071_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_jerk_21d_3d_v072_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_jerk_63d_3d_v073_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_jerk_126d_3d_v074_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_jerk_21d_3d_v075_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_jerk_63d_3d_v076_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_jerk_126d_3d_v077_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rel_xlk_63d smoothed over 252d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_smoothaccel_63d_sm252_3d_v078_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rel_xlk_63d smoothed over 504d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_smoothaccel_252d_sm504_3d_v079_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rel_xlk_252d smoothed over 252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_smoothaccel_63d_sm252_3d_v080_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rel_xlk_252d smoothed over 504d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_smoothaccel_252d_sm504_3d_v081_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rel_smh_252d smoothed over 252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_smoothaccel_63d_sm252_3d_v082_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rel_smh_252d smoothed over 504d
def f091fnd_f091_fund_prices_context_rel_smh_252d_smoothaccel_252d_sm504_3d_v083_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rel_igv_252d smoothed over 252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_smoothaccel_63d_sm252_3d_v084_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rel_igv_252d smoothed over 504d
def f091fnd_f091_fund_prices_context_rel_igv_252d_smoothaccel_252d_sm504_3d_v085_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of xlk_trend_252 smoothed over 252d
def f091fnd_f091_fund_prices_context_xlk_trend_252_smoothaccel_63d_sm252_3d_v086_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of xlk_trend_252 smoothed over 504d
def f091fnd_f091_fund_prices_context_xlk_trend_252_smoothaccel_252d_sm504_3d_v087_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of smh_trend_252 smoothed over 252d
def f091fnd_f091_fund_prices_context_smh_trend_252_smoothaccel_63d_sm252_3d_v088_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of smh_trend_252 smoothed over 504d
def f091fnd_f091_fund_prices_context_smh_trend_252_smoothaccel_252d_sm504_3d_v089_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of igv_trend_252 smoothed over 252d
def f091fnd_f091_fund_prices_context_igv_trend_252_smoothaccel_63d_sm252_3d_v090_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of igv_trend_252 smoothed over 504d
def f091fnd_f091_fund_prices_context_igv_trend_252_smoothaccel_252d_sm504_3d_v091_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_accelz_21d_z252_3d_v092_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_accelz_63d_z504_3d_v093_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_accelz_21d_z252_3d_v094_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_accelz_63d_z504_3d_v095_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_accelz_21d_z252_3d_v096_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_accelz_63d_z504_3d_v097_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_accelz_21d_z252_3d_v098_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_accelz_63d_z504_3d_v099_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_accelz_21d_z252_3d_v100_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_accelz_63d_z504_3d_v101_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_accelz_21d_z252_3d_v102_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_accelz_63d_z504_3d_v103_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_accelz_21d_z252_3d_v104_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_accelz_63d_z504_3d_v105_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rel_xlk_63d (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_rel_xlk_63d_signflip_63d_3d_v106_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rel_xlk_63d (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_rel_xlk_63d_signflip_252d_3d_v107_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rel_xlk_252d (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_rel_xlk_252d_signflip_63d_3d_v108_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rel_xlk_252d (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_rel_xlk_252d_signflip_252d_3d_v109_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rel_smh_252d (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_rel_smh_252d_signflip_63d_3d_v110_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rel_smh_252d (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_rel_smh_252d_signflip_252d_3d_v111_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rel_igv_252d (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_rel_igv_252d_signflip_63d_3d_v112_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rel_igv_252d (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_rel_igv_252d_signflip_252d_3d_v113_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in xlk_trend_252 (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_xlk_trend_252_signflip_63d_3d_v114_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in xlk_trend_252 (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_xlk_trend_252_signflip_252d_3d_v115_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in smh_trend_252 (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_smh_trend_252_signflip_63d_3d_v116_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in smh_trend_252 (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_smh_trend_252_signflip_252d_3d_v117_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in igv_trend_252 (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_igv_trend_252_signflip_63d_3d_v118_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in igv_trend_252 (raw count, no price scaling)
def f091fnd_f091_fund_prices_context_igv_trend_252_signflip_252d_3d_v119_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rel_xlk_63d normalized by 252d range
def f091fnd_f091_fund_prices_context_rel_xlk_63d_rngaccel_63d_r252_3d_v120_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rel_xlk_63d normalized by 504d range
def f091fnd_f091_fund_prices_context_rel_xlk_63d_rngaccel_252d_r504_3d_v121_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rel_xlk_252d normalized by 252d range
def f091fnd_f091_fund_prices_context_rel_xlk_252d_rngaccel_63d_r252_3d_v122_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rel_xlk_252d normalized by 504d range
def f091fnd_f091_fund_prices_context_rel_xlk_252d_rngaccel_252d_r504_3d_v123_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rel_smh_252d normalized by 252d range
def f091fnd_f091_fund_prices_context_rel_smh_252d_rngaccel_63d_r252_3d_v124_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rel_smh_252d normalized by 504d range
def f091fnd_f091_fund_prices_context_rel_smh_252d_rngaccel_252d_r504_3d_v125_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rel_igv_252d normalized by 252d range
def f091fnd_f091_fund_prices_context_rel_igv_252d_rngaccel_63d_r252_3d_v126_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rel_igv_252d normalized by 504d range
def f091fnd_f091_fund_prices_context_rel_igv_252d_rngaccel_252d_r504_3d_v127_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of xlk_trend_252 normalized by 252d range
def f091fnd_f091_fund_prices_context_xlk_trend_252_rngaccel_63d_r252_3d_v128_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of xlk_trend_252 normalized by 504d range
def f091fnd_f091_fund_prices_context_xlk_trend_252_rngaccel_252d_r504_3d_v129_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of smh_trend_252 normalized by 252d range
def f091fnd_f091_fund_prices_context_smh_trend_252_rngaccel_63d_r252_3d_v130_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of smh_trend_252 normalized by 504d range
def f091fnd_f091_fund_prices_context_smh_trend_252_rngaccel_252d_r504_3d_v131_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of igv_trend_252 normalized by 252d range
def f091fnd_f091_fund_prices_context_igv_trend_252_rngaccel_63d_r252_3d_v132_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of igv_trend_252 normalized by 504d range
def f091fnd_f091_fund_prices_context_igv_trend_252_rngaccel_252d_r504_3d_v133_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_cumslope_21d_3d_v134_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_cumslope_63d_3d_v135_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_cumslope_252d_3d_v136_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_cumslope_21d_3d_v137_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_cumslope_63d_3d_v138_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_cumslope_252d_3d_v139_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_cumslope_21d_3d_v140_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_cumslope_63d_3d_v141_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_cumslope_252d_3d_v142_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_cumslope_21d_3d_v143_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_cumslope_63d_3d_v144_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_cumslope_252d_3d_v145_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_cumslope_21d_3d_v146_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_cumslope_63d_3d_v147_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_cumslope_252d_3d_v148_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_cumslope_21d_3d_v149_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_cumslope_63d_3d_v150_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

