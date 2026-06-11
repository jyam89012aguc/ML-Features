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


# 21d acceleration of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_accel_21d_3d_v001_signal(pb, closeadj):
    base = pb
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_accel_63d_3d_v002_signal(pb, closeadj):
    base = pb
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_accel_126d_3d_v003_signal(pb, closeadj):
    base = pb
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_accel_252d_3d_v004_signal(pb, closeadj):
    base = pb
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_accel_21d_3d_v005_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_accel_63d_3d_v006_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_accel_126d_3d_v007_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_accel_252d_3d_v008_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_accel_21d_3d_v009_signal(bvps, closeadj):
    base = bvps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_accel_63d_3d_v010_signal(bvps, closeadj):
    base = bvps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_accel_126d_3d_v011_signal(bvps, closeadj):
    base = bvps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_accel_252d_3d_v012_signal(bvps, closeadj):
    base = bvps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_accel_21d_3d_v013_signal(tbvps, closeadj):
    base = tbvps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_accel_63d_3d_v014_signal(tbvps, closeadj):
    base = tbvps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_accel_126d_3d_v015_signal(tbvps, closeadj):
    base = tbvps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_accel_252d_3d_v016_signal(tbvps, closeadj):
    base = tbvps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_accel_21d_3d_v017_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_accel_63d_3d_v018_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_accel_126d_3d_v019_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_accel_252d_3d_v020_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of book_yield
def f071pbv_f071_price_book_valuation_book_yield_accel_21d_3d_v021_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of book_yield
def f071pbv_f071_price_book_valuation_book_yield_accel_63d_3d_v022_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of book_yield
def f071pbv_f071_price_book_valuation_book_yield_accel_126d_3d_v023_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of book_yield
def f071pbv_f071_price_book_valuation_book_yield_accel_252d_3d_v024_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_accel_21d_3d_v025_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_accel_63d_3d_v026_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_accel_126d_3d_v027_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_accel_252d_3d_v028_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_accel_21d_3d_v029_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_accel_63d_3d_v030_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_accel_126d_3d_v031_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_accel_252d_3d_v032_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_accel_21d_3d_v033_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_accel_63d_3d_v034_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_accel_126d_3d_v035_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_accel_252d_3d_v036_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_accel_21d_3d_v037_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_accel_63d_3d_v038_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_accel_126d_3d_v039_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_accel_252d_3d_v040_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_accel_21d_3d_v045_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_accel_63d_3d_v046_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_accel_126d_3d_v047_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_accel_252d_3d_v048_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_accel_21d_3d_v049_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_accel_63d_3d_v050_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_accel_126d_3d_v051_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_accel_252d_3d_v052_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slopez_21d_z126_3d_v053_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slopez_63d_z252_3d_v054_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slopez_126d_z252_3d_v055_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_slopez_252d_z504_3d_v056_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slopez_21d_z126_3d_v057_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slopez_63d_z252_3d_v058_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slopez_126d_z252_3d_v059_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_slopez_252d_z504_3d_v060_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slopez_21d_z126_3d_v061_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slopez_63d_z252_3d_v062_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slopez_126d_z252_3d_v063_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_slopez_252d_z504_3d_v064_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slopez_21d_z126_3d_v065_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slopez_63d_z252_3d_v066_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slopez_126d_z252_3d_v067_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_slopez_252d_z504_3d_v068_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slopez_21d_z126_3d_v069_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slopez_63d_z252_3d_v070_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slopez_126d_z252_3d_v071_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_slopez_252d_z504_3d_v072_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slopez_21d_z126_3d_v073_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slopez_63d_z252_3d_v074_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slopez_126d_z252_3d_v075_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of book_yield
def f071pbv_f071_price_book_valuation_book_yield_slopez_252d_z504_3d_v076_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slopez_21d_z126_3d_v077_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slopez_63d_z252_3d_v078_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slopez_126d_z252_3d_v079_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_slopez_252d_z504_3d_v080_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slopez_21d_z126_3d_v081_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slopez_63d_z252_3d_v082_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slopez_126d_z252_3d_v083_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_slopez_252d_z504_3d_v084_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slopez_21d_z126_3d_v085_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slopez_63d_z252_3d_v086_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slopez_126d_z252_3d_v087_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_slopez_252d_z504_3d_v088_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slopez_21d_z126_3d_v089_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slopez_63d_z252_3d_v090_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slopez_126d_z252_3d_v091_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_slopez_252d_z504_3d_v092_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_jerk_21d_3d_v105_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_jerk_63d_3d_v106_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_jerk_126d_3d_v107_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_jerk_21d_3d_v108_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_jerk_63d_3d_v109_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_jerk_126d_3d_v110_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_jerk_21d_3d_v111_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_jerk_63d_3d_v112_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_jerk_126d_3d_v113_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_jerk_21d_3d_v114_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_jerk_63d_3d_v115_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_jerk_126d_3d_v116_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_jerk_21d_3d_v117_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_jerk_63d_3d_v118_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_jerk_126d_3d_v119_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of book_yield
def f071pbv_f071_price_book_valuation_book_yield_jerk_21d_3d_v120_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of book_yield
def f071pbv_f071_price_book_valuation_book_yield_jerk_63d_3d_v121_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of book_yield
def f071pbv_f071_price_book_valuation_book_yield_jerk_126d_3d_v122_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_jerk_21d_3d_v123_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_jerk_63d_3d_v124_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_jerk_126d_3d_v125_signal(pb, closeadj):
    base = pb.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_jerk_21d_3d_v126_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_jerk_63d_3d_v127_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_jerk_126d_3d_v128_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_jerk_21d_3d_v129_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_jerk_63d_3d_v130_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_jerk_126d_3d_v131_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_jerk_21d_3d_v132_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_jerk_63d_3d_v133_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_jerk_126d_3d_v134_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_jerk_21d_3d_v138_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_jerk_63d_3d_v139_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_jerk_126d_3d_v140_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_jerk_21d_3d_v141_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_jerk_63d_3d_v142_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_jerk_126d_3d_v143_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_lvl smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_lvl_smoothaccel_63d_sm252_3d_v144_signal(pb, closeadj):
    base = pb
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_lvl smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_lvl_smoothaccel_252d_sm504_3d_v145_signal(pb, closeadj):
    base = pb
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_calc smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_calc_smoothaccel_63d_sm252_3d_v146_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_calc smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_calc_smoothaccel_252d_sm504_3d_v147_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of bvps_lvl smoothed over 252d
def f071pbv_f071_price_book_valuation_bvps_lvl_smoothaccel_63d_sm252_3d_v148_signal(bvps, closeadj):
    base = bvps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of bvps_lvl smoothed over 504d
def f071pbv_f071_price_book_valuation_bvps_lvl_smoothaccel_252d_sm504_3d_v149_signal(bvps, closeadj):
    base = bvps
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tbvps_lvl smoothed over 252d
def f071pbv_f071_price_book_valuation_tbvps_lvl_smoothaccel_63d_sm252_3d_v150_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tbvps_lvl smoothed over 504d
def f071pbv_f071_price_book_valuation_tbvps_lvl_smoothaccel_252d_sm504_3d_v151_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of p_to_tbv smoothed over 252d
def f071pbv_f071_price_book_valuation_p_to_tbv_smoothaccel_63d_sm252_3d_v152_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of p_to_tbv smoothed over 504d
def f071pbv_f071_price_book_valuation_p_to_tbv_smoothaccel_252d_sm504_3d_v153_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of book_yield smoothed over 252d
def f071pbv_f071_price_book_valuation_book_yield_smoothaccel_63d_sm252_3d_v154_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of book_yield smoothed over 504d
def f071pbv_f071_price_book_valuation_book_yield_smoothaccel_252d_sm504_3d_v155_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_yoy smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_yoy_smoothaccel_63d_sm252_3d_v156_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_yoy smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_yoy_smoothaccel_252d_sm504_3d_v157_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_peer_sector_dist smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_peer_sector_dist smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_peer_sector_z smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_peer_sector_z smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_peer_industry_dist smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_peer_industry_dist smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_peer_mcap_bucket_dist smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_peer_mcap_bucket_dist smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_peer_sector_pctile smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_peer_sector_pctile smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of pb_peer_industry_pctile smoothed over 252d
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of pb_peer_industry_pctile smoothed over 504d
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_accelz_21d_z252_3d_v170_signal(pb, closeadj):
    base = pb
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_accelz_63d_z504_3d_v171_signal(pb, closeadj):
    base = pb
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_accelz_21d_z252_3d_v172_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_accelz_63d_z504_3d_v173_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_accelz_21d_z252_3d_v174_signal(bvps, closeadj):
    base = bvps
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_accelz_63d_z504_3d_v175_signal(bvps, closeadj):
    base = bvps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_accelz_21d_z252_3d_v176_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_accelz_63d_z504_3d_v177_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_accelz_21d_z252_3d_v178_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_accelz_63d_z504_3d_v179_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of book_yield
def f071pbv_f071_price_book_valuation_book_yield_accelz_21d_z252_3d_v180_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of book_yield
def f071pbv_f071_price_book_valuation_book_yield_accelz_63d_z504_3d_v181_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_accelz_21d_z252_3d_v182_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_accelz_63d_z504_3d_v183_signal(pb, closeadj):
    base = pb.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_accelz_21d_z252_3d_v184_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_accelz_63d_z504_3d_v185_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_accelz_21d_z252_3d_v186_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_accelz_63d_z504_3d_v187_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_accelz_21d_z252_3d_v188_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_accelz_63d_z504_3d_v189_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pb_lvl (raw count, no price scaling)
def f071pbv_f071_price_book_valuation_pb_lvl_signflip_63d_3d_v196_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pb_lvl (raw count, no price scaling)
def f071pbv_f071_price_book_valuation_pb_lvl_signflip_252d_3d_v197_signal(pb, closeadj):
    base = pb
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in pb_calc (raw count, no price scaling)
def f071pbv_f071_price_book_valuation_pb_calc_signflip_63d_3d_v198_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in pb_calc (raw count, no price scaling)
def f071pbv_f071_price_book_valuation_pb_calc_signflip_252d_3d_v199_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in bvps_lvl (raw count, no price scaling)
def f071pbv_f071_price_book_valuation_bvps_lvl_signflip_63d_3d_v200_signal(bvps, closeadj):
    base = bvps
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

