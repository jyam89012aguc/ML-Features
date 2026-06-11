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
def _f071_pb(marketcap, equity):
    return marketcap / equity.replace(0, np.nan).abs()


# 21d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slope_21d_2d_v001_signal(pb, closeadj):
    base = pb
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slope_63d_2d_v002_signal(pb, closeadj):
    base = pb
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slope_126d_2d_v003_signal(pb, closeadj):
    base = pb
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slope_252d_2d_v004_signal(pb, closeadj):
    base = pb
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slope_504d_2d_v005_signal(pb, closeadj):
    base = pb
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slope_21d_2d_v006_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slope_63d_2d_v007_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slope_126d_2d_v008_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slope_252d_2d_v009_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slope_504d_2d_v010_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slope_21d_2d_v011_signal(bvps, closeadj):
    base = bvps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slope_63d_2d_v012_signal(bvps, closeadj):
    base = bvps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slope_126d_2d_v013_signal(bvps, closeadj):
    base = bvps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slope_252d_2d_v014_signal(bvps, closeadj):
    base = bvps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slope_504d_2d_v015_signal(bvps, closeadj):
    base = bvps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slope_21d_2d_v016_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slope_63d_2d_v017_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slope_126d_2d_v018_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slope_252d_2d_v019_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slope_504d_2d_v020_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slope_21d_2d_v021_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slope_63d_2d_v022_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slope_126d_2d_v023_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slope_252d_2d_v024_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slope_504d_2d_v025_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slope_21d_2d_v026_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slope_63d_2d_v027_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slope_126d_2d_v028_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slope_252d_2d_v029_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slope_504d_2d_v030_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slope_21d_2d_v031_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slope_63d_2d_v032_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slope_126d_2d_v033_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slope_252d_2d_v034_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slope_504d_2d_v035_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slope_21d_2d_v036_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slope_63d_2d_v037_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slope_126d_2d_v038_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slope_252d_2d_v039_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slope_504d_2d_v040_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slope_21d_2d_v041_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slope_63d_2d_v042_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slope_126d_2d_v043_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slope_252d_2d_v044_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slope_504d_2d_v045_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slope_21d_2d_v046_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slope_63d_2d_v047_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slope_126d_2d_v048_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slope_252d_2d_v049_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slope_504d_2d_v050_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slope_21d_2d_v056_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slope_63d_2d_v057_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slope_126d_2d_v058_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slope_252d_2d_v059_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slope_504d_2d_v060_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slope_21d_2d_v061_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slope_63d_2d_v062_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slope_126d_2d_v063_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slope_252d_2d_v064_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slope_504d_2d_v065_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_sm21_sl21_2d_v066_signal(pb, closeadj):
    base = _mean(pb, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_sm63_sl21_2d_v067_signal(pb, closeadj):
    base = _mean(pb, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_sm63_sl63_2d_v068_signal(pb, closeadj):
    base = _mean(pb, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_sm252_sl63_2d_v069_signal(pb, closeadj):
    base = _mean(pb, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_sm252_sl126_2d_v070_signal(pb, closeadj):
    base = _mean(pb, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_sm21_sl21_2d_v071_signal(marketcap, equity, closeadj):
    base = _mean(_f071_pb(marketcap, equity), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_sm63_sl21_2d_v072_signal(marketcap, equity, closeadj):
    base = _mean(_f071_pb(marketcap, equity), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_sm63_sl63_2d_v073_signal(marketcap, equity, closeadj):
    base = _mean(_f071_pb(marketcap, equity), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_sm252_sl63_2d_v074_signal(marketcap, equity, closeadj):
    base = _mean(_f071_pb(marketcap, equity), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_sm252_sl126_2d_v075_signal(marketcap, equity, closeadj):
    base = _mean(_f071_pb(marketcap, equity), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_sm21_sl21_2d_v076_signal(bvps, closeadj):
    base = _mean(bvps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_sm63_sl21_2d_v077_signal(bvps, closeadj):
    base = _mean(bvps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_sm63_sl63_2d_v078_signal(bvps, closeadj):
    base = _mean(bvps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_sm252_sl63_2d_v079_signal(bvps, closeadj):
    base = _mean(bvps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_sm252_sl126_2d_v080_signal(bvps, closeadj):
    base = _mean(bvps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_sm21_sl21_2d_v081_signal(tbvps, closeadj):
    base = _mean(tbvps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_sm63_sl21_2d_v082_signal(tbvps, closeadj):
    base = _mean(tbvps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_sm63_sl63_2d_v083_signal(tbvps, closeadj):
    base = _mean(tbvps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_sm252_sl63_2d_v084_signal(tbvps, closeadj):
    base = _mean(tbvps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_sm252_sl126_2d_v085_signal(tbvps, closeadj):
    base = _mean(tbvps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_sm21_sl21_2d_v086_signal(close, tbvps, closeadj):
    base = _mean(close / tbvps.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_sm63_sl21_2d_v087_signal(close, tbvps, closeadj):
    base = _mean(close / tbvps.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_sm63_sl63_2d_v088_signal(close, tbvps, closeadj):
    base = _mean(close / tbvps.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_sm252_sl63_2d_v089_signal(close, tbvps, closeadj):
    base = _mean(close / tbvps.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_sm252_sl126_2d_v090_signal(close, tbvps, closeadj):
    base = _mean(close / tbvps.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_sm21_sl21_2d_v091_signal(equity, marketcap, closeadj):
    base = _mean(equity / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_sm63_sl21_2d_v092_signal(equity, marketcap, closeadj):
    base = _mean(equity / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_sm63_sl63_2d_v093_signal(equity, marketcap, closeadj):
    base = _mean(equity / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_sm252_sl63_2d_v094_signal(equity, marketcap, closeadj):
    base = _mean(equity / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_sm252_sl126_2d_v095_signal(equity, marketcap, closeadj):
    base = _mean(equity / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_sm21_sl21_2d_v096_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_sm63_sl21_2d_v097_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_sm63_sl63_2d_v098_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_sm252_sl63_2d_v099_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_sm252_sl126_2d_v100_signal(pb, closeadj):
    base = _mean(pb.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_sm21_sl21_2d_v101_signal(pb, pb_sector_med, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_sm63_sl21_2d_v102_signal(pb, pb_sector_med, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_sm63_sl63_2d_v103_signal(pb, pb_sector_med, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_sm252_sl63_2d_v104_signal(pb, pb_sector_med, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_sm252_sl126_2d_v105_signal(pb, pb_sector_med, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_sm21_sl21_2d_v106_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_sm63_sl21_2d_v107_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_sm63_sl63_2d_v108_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_sm252_sl63_2d_v109_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_sm252_sl126_2d_v110_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = _mean((pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_sm21_sl21_2d_v111_signal(pb, pb_industry_med, closeadj):
    base = _mean((pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_sm63_sl21_2d_v112_signal(pb, pb_industry_med, closeadj):
    base = _mean((pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_sm63_sl63_2d_v113_signal(pb, pb_industry_med, closeadj):
    base = _mean((pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_sm252_sl63_2d_v114_signal(pb, pb_industry_med, closeadj):
    base = _mean((pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_sm252_sl126_2d_v115_signal(pb, pb_industry_med, closeadj):
    base = _mean((pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(pb, pb_mcap_med, closeadj):
    base = _mean((pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(pb, pb_mcap_med, closeadj):
    base = _mean((pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(pb, pb_mcap_med, closeadj):
    base = _mean((pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(pb, pb_mcap_med, closeadj):
    base = _mean((pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(pb, pb_mcap_med, closeadj):
    base = _mean((pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_sm21_sl21_2d_v121_signal(pb_sector_pctile, closeadj):
    base = _mean(pb_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_sm63_sl21_2d_v122_signal(pb_sector_pctile, closeadj):
    base = _mean(pb_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_sm63_sl63_2d_v123_signal(pb_sector_pctile, closeadj):
    base = _mean(pb_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_sm252_sl63_2d_v124_signal(pb_sector_pctile, closeadj):
    base = _mean(pb_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_sm252_sl126_2d_v125_signal(pb_sector_pctile, closeadj):
    base = _mean(pb_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_sm21_sl21_2d_v126_signal(pb_industry_pctile, closeadj):
    base = _mean(pb_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_sm63_sl21_2d_v127_signal(pb_industry_pctile, closeadj):
    base = _mean(pb_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_sm63_sl63_2d_v128_signal(pb_industry_pctile, closeadj):
    base = _mean(pb_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_sm252_sl63_2d_v129_signal(pb_industry_pctile, closeadj):
    base = _mean(pb_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_sm252_sl126_2d_v130_signal(pb_industry_pctile, closeadj):
    base = _mean(pb_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_pctslope_21d_2d_v131_signal(pb, closeadj):
    base = pb
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_pctslope_63d_2d_v132_signal(pb, closeadj):
    base = pb
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_pctslope_252d_2d_v133_signal(pb, closeadj):
    base = pb
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_pctslope_21d_2d_v134_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_pctslope_63d_2d_v135_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_pctslope_252d_2d_v136_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_pctslope_21d_2d_v137_signal(bvps, closeadj):
    base = bvps
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_pctslope_63d_2d_v138_signal(bvps, closeadj):
    base = bvps
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_pctslope_252d_2d_v139_signal(bvps, closeadj):
    base = bvps
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_pctslope_21d_2d_v140_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_pctslope_63d_2d_v141_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_pctslope_252d_2d_v142_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_pctslope_21d_2d_v143_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_pctslope_63d_2d_v144_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_pctslope_252d_2d_v145_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_pctslope_21d_2d_v146_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_pctslope_63d_2d_v147_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_pctslope_252d_2d_v148_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_pctslope_21d_2d_v149_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_pctslope_63d_2d_v150_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_pctslope_252d_2d_v151_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_pctslope_21d_2d_v152_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_pctslope_63d_2d_v153_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_pctslope_252d_2d_v154_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_pctslope_21d_2d_v155_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_pctslope_63d_2d_v156_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_pctslope_252d_2d_v157_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_pctslope_21d_2d_v158_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_pctslope_63d_2d_v159_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_pctslope_252d_2d_v160_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_pctslope_21d_2d_v164_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_pctslope_63d_2d_v165_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_pctslope_252d_2d_v166_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_pctslope_21d_2d_v167_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_pctslope_63d_2d_v168_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_pctslope_252d_2d_v169_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_sgnslope_21d_2d_v170_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_sgnslope_63d_2d_v171_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_sgnslope_252d_2d_v172_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_sgnslope_21d_2d_v173_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_sgnslope_63d_2d_v174_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_sgnslope_252d_2d_v175_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_sgnslope_21d_2d_v176_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_sgnslope_63d_2d_v177_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_sgnslope_252d_2d_v178_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_sgnslope_21d_2d_v179_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_sgnslope_63d_2d_v180_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_sgnslope_252d_2d_v181_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_sgnslope_21d_2d_v182_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_sgnslope_63d_2d_v183_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_sgnslope_252d_2d_v184_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_sgnslope_21d_2d_v185_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_sgnslope_63d_2d_v186_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of book_yield
def f071pbv_f071_price_book_valuation_book_yield_sgnslope_252d_2d_v187_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_sgnslope_21d_2d_v188_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_sgnslope_63d_2d_v189_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_sgnslope_252d_2d_v190_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_sgnslope_21d_2d_v191_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_sgnslope_63d_2d_v192_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_sgnslope_252d_2d_v193_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_sgnslope_21d_2d_v194_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_sgnslope_63d_2d_v195_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_sgnslope_252d_2d_v196_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_sgnslope_21d_2d_v197_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_sgnslope_63d_2d_v198_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_sgnslope_252d_2d_v199_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

